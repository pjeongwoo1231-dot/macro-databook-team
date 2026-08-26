"""주식 대차거래 — 공매도 압력의 대리지표.

금융위 주식대차정보 API(공공데이터포털). **대차잔고는 빌려간 주식이 아직 상환되지 않은 잔량**이라
공매도 포지션의 대용으로 널리 쓰인다. 잔고가 쌓이면 하락 베팅이 누적됐다는 뜻이고,
급감하면 숏커버링 압력으로 읽는다.

주의 — 대차 ≠ 공매도
- 대차에는 **차익거래·헤지·의결권 목적**도 섞인다. 전부 하락 베팅이 아니다
- 그래서 **수준보다 변화**를, **절대액보다 시가총액 대비 비율**을 보는 편이 낫다

API 메모 (2026-08-05 확인)
- 엔드포인트 `apis.data.go.kr/1160100/GetStocLendBorrInfoService_V2` (`/service/` 없음)
- 오퍼레이션 `getStLendAndBorrItemRank_V2` — 공개 문서에 영문명이 없어 탐색으로 찾았다
- `basDt=YYYYMMDD` 로 하루치(전 종목 ~2,800건). `beginBasDt/endBasDt`는 **먹히지 않는다**
- 전체 8,075,623건 · 2008-01-02부터
- 최신 구간은 `isinCd`가 6자리 단축코드, 과거는 12자리 ISIN — **혼용되므로 조인 시 주의**
"""
from __future__ import annotations

import csv
import json
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, timedelta
from typing import Any

from .core import OUTPUT_DIR
from .fetchers.base import result, throttle

LEND_DIR = OUTPUT_DIR / "lending"
BASE = ("https://apis.data.go.kr/1160100/GetStocLendBorrInfoService_V2"
        "/getStLendAndBorrItemRank_V2")


def fetch_day(day: str, key: str, rows: int = 5000) -> list[dict[str, Any]]:
    """하루치 전 종목. day=YYYYMMDD. 휴장일이면 빈 리스트."""
    throttle("apis.data.go.kr", 0.4)
    q = {"serviceKey": key, "resultType": "json", "numOfRows": str(rows),
         "pageNo": "1", "basDt": day}
    url = BASE + "?" + urllib.parse.urlencode(q)
    req = urllib.request.Request(url, headers={"User-Agent": "macro-databook/0.1"})
    with urllib.request.urlopen(req, timeout=40) as r:
        data = json.loads(r.read().decode("utf-8"))
    body = data.get("response", {}).get("body", {})
    items = (body.get("items") or {}).get("item") or []
    if isinstance(items, dict):
        items = [items]
    out = []
    for it in items:
        try:
            out.append({
                "date": day,
                "code": str(it.get("isinCd", "")),
                "name": str(it.get("isinCdNm", "")),
                "bal_amt": float(it.get("lnbBal") or 0),          # 대차잔고 금액(원)
                "bal_qty": float(it.get("lnbRmanStckCnt") or 0),  # 대차잔고 주식수
                "new_qty": float(it.get("lnbCclStckCnt") or 0),   # 신규 체결
                "rdpt_qty": float(it.get("rdptStckCnt") or 0),    # 상환
            })
        except (TypeError, ValueError):
            continue
    return out


def _key(env: dict[str, str]) -> str:
    return env.get("DATA_GO_KR_LENDBORR_KEY", "")


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """일일 수집용 — 최근 영업일들의 **시장 전체 대차잔고 총액**(조원)."""
    key = _key(env)
    if not key:
        return result(ind, "fail", error="DATA_GO_KR_LENDBORR_KEY 없음 (.env 확인)")
    obs: list[dict[str, Any]] = []
    d = date.today()
    tries = 0
    while len(obs) < 5 and tries < 12:
        tries += 1
        d -= timedelta(days=1)
        if d.weekday() >= 5:
            continue
        try:
            rows = fetch_day(d.strftime("%Y%m%d"), key)
        except Exception:
            continue
        if not rows:
            continue
        tot = sum(r["bal_amt"] for r in rows) / 1e12   # 원 → 조원
        obs.append({"date": d.isoformat(), "value": round(tot, 2),
                    "label": f"대차잔고 총액(조원, {len(rows):,}종목)"})
    if not obs:
        return result(ind, "fail", error="최근 영업일 데이터 없음")
    return result(ind, "ok", observations=obs,
                  source_url="https://www.data.go.kr/data/15059612/openapi.do")


def collect(days: int = 60, env: dict[str, str] | None = None,
            with_sector: bool = True, dry_run: bool = False) -> int:
    from .core import load_env
    env = env or load_env()
    key = _key(env)
    if not key:
        print("DATA_GO_KR_LENDBORR_KEY 없음 (.env 확인)")
        return 1
    print(f"주식 대차거래 — 최근 {days}영업일")
    if dry_run:
        return 0

    LEND_DIR.mkdir(parents=True, exist_ok=True)
    daily: list[dict[str, Any]] = []
    per_stock: dict[str, dict[str, float]] = {}   # 최신일 종목별
    d = date.today()
    got = 0
    while got < days:
        d -= timedelta(days=1)
        if d.weekday() >= 5:
            continue
        if (date.today() - d).days > days * 2 + 30:
            break
        ds = d.strftime("%Y%m%d")
        try:
            rows = fetch_day(ds, key)
        except Exception as e:
            print(f"  [FAIL] {ds}: {type(e).__name__}")
            continue
        if not rows:
            continue
        got += 1
        tot_amt = sum(r["bal_amt"] for r in rows)
        daily.append({"date": f"{ds[:4]}-{ds[4:6]}-{ds[6:]}",
                      "n_stocks": len(rows),
                      "bal_amt_trn": round(tot_amt / 1e12, 3),
                      "new_qty": int(sum(r["new_qty"] for r in rows)),
                      "rdpt_qty": int(sum(r["rdpt_qty"] for r in rows))})
        if not per_stock:      # 가장 최근일 기준으로만 종목별을 남긴다
            per_stock = {r["code"]: {"name": r["name"], "bal_amt": r["bal_amt"],
                                     "bal_qty": r["bal_qty"]} for r in rows}
            latest = ds
        if got % 20 == 0:
            print(f"    {got}/{days} …")

    if not daily:
        print("  수집된 날짜가 없다")
        return 1
    daily.sort(key=lambda r: r["date"])
    p = LEND_DIR / "market_daily.csv"
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date", "n_stocks", "bal_amt_trn", "new_qty", "rdpt_qty"])
        w.writeheader()
        w.writerows(daily)
    print(f"\n시장 전체 대차잔고 (조원)")
    for r in daily[-5:]:
        print(f"  {r['date']}  {r['bal_amt_trn']:>8,.1f}조  ({r['n_stocks']:,}종목)")

    ps = LEND_DIR / f"by_stock_{latest}.csv"
    with ps.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["code", "name", "bal_amt", "bal_qty"])
        for c, v in sorted(per_stock.items(), key=lambda x: -x[1]["bal_amt"]):
            w.writerow([c, v["name"], int(v["bal_amt"]), int(v["bal_qty"])])

    # 업종별 집계 — sectors 모듈의 업종↔종목 매핑을 재사용한다
    if with_sector:
        try:
            from .sectors import fetch_list, fetch_sector_members
            secs = fetch_list()
            print(f"\n업종별 대차잔고 집계 — {len(secs)}개 업종")
            out = []
            for r in secs:
                mem = fetch_sector_members(r["no"])
                amt = sum(per_stock[c]["bal_amt"] for c in mem if c in per_stock)
                n = sum(1 for c in mem if c in per_stock)
                out.append({"date": f"{latest[:4]}-{latest[4:6]}-{latest[6:]}",
                            "sector": r["sector"], "bal_amt_bn": round(amt / 1e9, 1),
                            "n_matched": n, "change_pct": r["change_pct"]})
            out.sort(key=lambda x: -x["bal_amt_bn"])
            pv = LEND_DIR / f"by_sector_{latest}.csv"
            with pv.open("w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=["date", "sector", "bal_amt_bn", "n_matched", "change_pct"])
                w.writeheader()
                w.writerows(out)
            for r in out[:5]:
                print(f"  {r['sector'][:20]:22s} {r['bal_amt_bn']:>10,.0f}십억  ({r['n_matched']}종목)")
            print(f"  → {pv}")
        except Exception as e:
            print(f"  업종 집계 실패: {type(e).__name__}: {e}")

    print(f"\n  → {p}\n  → {ps}")
    print("\n⚠ 대차 ≠ 공매도. 차익거래·헤지 목적이 섞인다 — 수준보다 변화를, 절대액보다 시총 대비를 볼 것.")
    return 0
