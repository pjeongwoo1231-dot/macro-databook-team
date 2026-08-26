"""종목 ↔ 업종 매핑 + 업종 단위 수급 집계.

**왜 필요한가** — 토스 백필로 전 4,300종목의 수급 패널이 생겼는데
**패널에 업종 코드가 없다.** 그래서 "신용융자가 어느 업종에 쏠렸나"를 물을 수 없었다.
`sectors.py`는 업종별 등락률만 받고 구성종목은 받지 않는다. 그 빈칸을 메운다.

**출처** — 네이버 금융 업종 상세(`sise_group_detail.naver?type=upjong&no=N`), 원천 KRX.
업종 목록 1회 + 업종당 1회 = 약 80회 요청.

⚠ **한 종목이 한 업종에만 속한다** — 네이버 분류 기준이다. GICS·KRX 표준분류와 다를 수 있다.
⚠ **코스피·코스닥이 섞여 있다.** 업종 집계에서 시장을 나눠 보려면 `_universe.csv`의 market을 쓴다.
⚠ 스크랩이라 **사이트 개편에 깨진다.** 구성종목이 0개로 오면 실패로 남기고 조용히 넘어가지 않는다.
"""
from __future__ import annotations

import csv
import io
import json
import re
import statistics as st
import time
from datetime import date
from pathlib import Path
from typing import Any

from .core import OUTPUT_DIR
from .fetchers.base import BROWSER_UA, get_text

MAP_PATH = OUTPUT_DIR / "sectors" / "_symbol_sector.csv"
AGG_DIR = OUTPUT_DIR / "sectors"
STOCKS = OUTPUT_DIR / "history" / "toss" / "stocks"
UNIVERSE = OUTPUT_DIR / "history" / "toss" / "_universe.csv"

LIST_URL = "https://finance.naver.com/sise/sise_group.naver?type=upjong"
DETAIL_URL = "https://finance.naver.com/sise/sise_group_detail.naver?type=upjong&no={no}"

# ⚠ 네이버 목록 페이지는 & 를 엔티티로 escape 하지 않는다 — &amp; 로 찾으면 0건이 나온다
_LINK = re.compile(r'sise_group_detail\.naver\?type=upjong&(?:amp;)?no=(\d+)">([^<]+)</a>')
_ITEM = re.compile(r'/item/main\.naver\?code=(\d{6})">([^<]+)</a>')


def fetch_map(sleep: float = 0.4, log=print) -> list[dict[str, str]]:
    html = get_text(LIST_URL, headers={"User-Agent": BROWSER_UA}, encoding="euc-kr")
    sectors = []
    for no, name in _LINK.findall(html):
        nm = name.strip()
        if nm and (no, nm) not in sectors:
            sectors.append((no, nm))
    log(f"업종 {len(sectors)}개")

    rows: list[dict[str, str]] = []
    empty: list[str] = []
    for i, (no, name) in enumerate(sectors, 1):
        try:
            h = get_text(DETAIL_URL.format(no=no), headers={"User-Agent": BROWSER_UA},
                         encoding="euc-kr")
        except Exception as e:
            empty.append(f"{name}({type(e).__name__})")
            continue
        items = _ITEM.findall(h)
        if not items:
            empty.append(f"{name}(구성종목 0)")
            continue
        for code, sname in items:
            rows.append({"symbol": code, "name": sname.strip(),
                         "sector": name, "sector_no": no})
        if i % 20 == 0:
            log(f"  {i}/{len(sectors)} · 누적 {len(rows):,}종목")
        time.sleep(sleep)

    if empty:
        log(f"⚠ 구성종목을 못 받은 업종 {len(empty)}개: {', '.join(empty[:5])}")
    MAP_PATH.parent.mkdir(parents=True, exist_ok=True)
    with MAP_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["symbol", "name", "sector", "sector_no"])
        w.writeheader()
        w.writerows(rows)
    log(f"매핑 {len(rows):,}행 · 고유 종목 {len({r['symbol'] for r in rows}):,}개 → {MAP_PATH}")
    return rows


def load_map() -> dict[str, str]:
    if not MAP_PATH.exists():
        return {}
    return {r["symbol"]: r["sector"]
            for r in csv.DictReader(io.open(MAP_PATH, encoding="utf-8"))}


# ── 파생 지표 ───────────────────────────────────────────────
def _panel(sym: str) -> list[dict[str, str]]:
    p = STOCKS / f"{sym}.csv"
    if not p.exists():
        return []
    return list(csv.DictReader(io.open(p, encoding="utf-8")))


def _f(x: Any) -> float | None:
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def derive(log=print) -> dict[str, Any]:
    """원계열에서 계산되는 파생 지표.

    - **신용융자/시가총액 비율** — 잔고 주수만으로는 종목 크기에 휘둘린다.
      시총으로 나눠야 종목 간 비교가 된다
    - **대차잔고/상장주식수 비율** — 같은 이유
    - **공매도 비중 20일 평균** — 일별 값은 튄다
    각각 **자기 표본 백분위**를 함께 낸다 — 수준이 아니라 위치가 판정 재료다.
    """
    uni = {r["symbol"]: r for r in csv.DictReader(io.open(UNIVERSE, encoding="utf-8"))}
    smap = load_map()
    out = []
    for p in STOCKS.glob("*.csv"):
        sym = p.stem
        u = uni.get(sym)
        if not u:
            continue
        shares = _f(u.get("shares"))
        cap = _f(u.get("mktcap_trillion")) or 0.0
        rows = _panel(sym)
        if not rows:
            continue
        rec = {"symbol": sym, "name": u.get("name", sym), "market": u.get("market", ""),
               "sector": smap.get(sym, ""), "cap": cap, "date": rows[-1]["date"]}

        def col(c):
            return [(r["date"], float(r[c])) for r in rows if r.get(c)]

        # 신용융자 / 시총
        cq = col("credit_qty")
        if cq and cap and shares:
            price = cap * 1e12 / shares
            ser = [(d, v * price / (cap * 1e12) * 100) for d, v in cq]   # 잔고금액/시총 %
            vals = [v for _, v in ser]
            rec["credit_to_cap"] = round(vals[-1], 4)
            rec["credit_to_cap_pct"] = round(sum(1 for x in vals if x < vals[-1]) / len(vals) * 100, 1)
        # 대차 / 상장주식수
        lq = col("lending_qty")
        if lq and shares:
            vals = [v / shares * 100 for _, v in lq]
            rec["lending_to_shares"] = round(vals[-1], 4)
            rec["lending_to_shares_pct"] = round(sum(1 for x in vals if x < vals[-1]) / len(vals) * 100, 1)
        # 공매도 20일 평균
        sr = col("short_rate")
        if len(sr) >= 20:
            v20 = st.mean(v for _, v in sr[-20:])
            allm = [st.mean(v for _, v in sr[max(0, i - 19):i + 1]) for i in range(19, len(sr))]
            rec["short_ma20"] = round(v20, 3)
            rec["short_ma20_pct"] = round(sum(1 for x in allm if x < v20) / len(allm) * 100, 1)
        fh = col("foreign_hold_rate")
        if fh:
            rec["foreign_hold_rate"] = fh[-1][1]
            if len(fh) > 21:
                rec["foreign_chg20"] = round(fh[-1][1] - fh[-21][1], 3)
        out.append(rec)

    dpath = AGG_DIR / f"derived_{date.today().isoformat()}.csv"
    cols = ["symbol", "name", "market", "sector", "cap", "date", "credit_to_cap",
            "credit_to_cap_pct", "lending_to_shares", "lending_to_shares_pct",
            "short_ma20", "short_ma20_pct", "foreign_hold_rate", "foreign_chg20"]
    dpath.parent.mkdir(parents=True, exist_ok=True)
    with dpath.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(out)
    log(f"파생 지표 {len(out):,}종목 → {dpath.name}")
    return {"rows": out, "path": dpath}


def aggregate(rows: list[dict], log=print) -> None:
    """업종 단위 집계 — 시총 가중이 기본. 단순평균은 소형주가 지배해서 못 쓴다."""
    by: dict[str, list[dict]] = {}
    for r in rows:
        if r.get("sector"):
            by.setdefault(r["sector"], []).append(r)

    agg = []
    for sec, items in by.items():
        capsum = sum(i["cap"] for i in items) or 1e-9

        def wavg(k):
            vs = [(i[k], i["cap"]) for i in items if i.get(k) is not None and i["cap"] > 0]
            return round(sum(v * c for v, c in vs) / sum(c for _, c in vs), 3) if vs else None

        def avg_pct(k):
            vs = [i[k] for i in items if i.get(k) is not None]
            return round(st.mean(vs), 1) if vs else None

        agg.append({
            "sector": sec, "n": len(items), "cap_trillion": round(capsum, 1),
            "credit_to_cap_w": wavg("credit_to_cap"),
            "credit_pct_avg": avg_pct("credit_to_cap_pct"),
            "lending_to_shares_w": wavg("lending_to_shares"),
            "lending_pct_avg": avg_pct("lending_to_shares_pct"),
            "short_ma20_w": wavg("short_ma20"),
            "foreign_hold_w": wavg("foreign_hold_rate"),
            "foreign_chg20_w": wavg("foreign_chg20"),
        })
    agg.sort(key=lambda a: -(a["cap_trillion"]))
    p = AGG_DIR / f"sector_flows_{date.today().isoformat()}.csv"
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(agg[0]))
        w.writeheader()
        w.writerows(agg)
    log(f"업종 집계 {len(agg)}개 → {p.name}")
    return agg


def collect(remap: bool = False, log=print) -> int:
    if remap or not MAP_PATH.exists():
        fetch_map(log=log)
    elif log:
        log(f"기존 매핑 사용 ({MAP_PATH.name}) — 다시 받으려면 --remap")
    d = derive(log=log)
    if not d["rows"]:
        log("파생 지표 없음 — 백필(`tossback --what stocks`)이 먼저다")
        return 1
    aggregate(d["rows"], log=log)
    return 0
