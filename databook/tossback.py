"""토스증권 Open API 장기 백필 — 커서를 끝까지 밀어 CSV로 축적한다.

`run`은 '오늘 상태'를 보려고 최근 몇 개만 받는다. 이 모듈은 반대로
**커서(`before`/`until`)를 소진할 때까지 페이징**해서 전 이력을 내려받는다.
산출물은 사람이 읽는 노트가 아니라 분석 스크립트가 먹는 데이터라
Obsidian이 아니라 `output/history/toss/`에 쓴다(history.py와 같은 자리).

저장 형식이 둘로 갈린다 — 일부러 그렇게 했다
- **시장 계열**(지수·국채·투자자별 매매대금): `output/history/toss/{계열}.csv`,
  `date,value` — history.py의 FRED·Yahoo와 **같은 규약**이라 기존 분석 코드가 그대로 먹는다
- **종목 패널**(공매도·신용·대차·프로그램·투자자별): `output/history/toss/stocks/{종목}.csv`,
  **와이드 포맷**(date + 지표 컬럼 15개). 종목당 계열이 15개라 `date,value`로 쪼개면
  파일이 종목수×15개가 된다(전 종목이면 6만 개). 한 종목의 수급은 같이 봐야 의미가 있으므로
  한 파일에 담는다. **규약을 벗어난 유일한 지점이고, 이유는 이것뿐이다.**

**증분이 기본**이다. CSV가 있으면 마지막 날짜까지만 거슬러 올라가고 멈춘다.
`--full`이면 처음부터 다시 받는다. 종목 루프는 체크포인트를 남겨
중간에 끊겨도 다음 실행이 이어서 간다.

⚠ **토큰은 동시에 하나만 산다.** 이 백필과 `python -m databook run`을
**동시에 돌리면 서로 401**을 만든다. 수집이 끝난 뒤에 돌릴 것.

⚠ 실측 처리량(2026-08-19): 스로틀 없이 **약 370req/분**까지 429가 안 났다.
기본 간격은 그보다 넉넉하게 잡고, 429가 나면 자동으로 더 벌린다.

⚠ 이력 깊이(2026-08-19 실측): 캔들·수급 모두 **2020~2021년**까지 커서가 살아 있다.
**신용거래만 2023-04**에서 끊긴다. 그보다 과거는 API에 없다 — 없는 걸 만들지 않는다.
"""
from __future__ import annotations

import csv
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

from .core import OUTPUT_DIR, load_env
from .fetchers.tossinvest import _get

TOSS_DIR = OUTPUT_DIR / "history" / "toss"
STOCK_DIR = TOSS_DIR / "stocks"
CKPT = TOSS_DIR / "_checkpoint.json"
MANIFEST = OUTPUT_DIR / "history" / "_manifest.json"

DEFAULT_SINCE = "2000-01-01"      # API가 주는 데까지 = 사실상 전량
MAX_PAGES = 400                   # 폭주 방지용 상한. 정상 종료는 커서 소진이다
FX_FIRST = "2022-12-16"           # 이보다 과거 환율은 404 (2026-08-19 이분탐색으로 확인)

INDEX_SYMBOLS = ["KOSPI", "KOSDAQ"]
BOND_SYMBOLS = ["KR_BOND_2Y", "KR_BOND_3Y", "KR_BOND_5Y",
                "KR_BOND_10Y", "KR_BOND_20Y", "KR_BOND_30Y"]
KINDS = ["short", "credit", "lending", "investor", "program"]
_KIND_EP = {"short": "short-selling", "credit": "credit-trades", "lending": "securities-lending",
            "investor": "investor-trading", "program": "program-trades"}

# 종목 패널 컬럼 — 순서가 곧 CSV 헤더다
PANEL_COLS = ["short_rate", "short_amt", "credit_qty", "credit_rate",
              "lending_qty", "lending_amt", "net_foreigner", "net_institution",
              "net_individual", "net_other", "foreign_hold_rate", "foreign_limit_rate",
              "prog_arb", "prog_nonarb", "close"]


class Throttle:
    """429가 나면 간격을 늘리고, 조용하면 서서히 줄인다.

    **워커 스레드가 공유한다** — 간격은 프로세스 전체의 호출 간격이지 스레드당이 아니다.
    락 안에서 잠들기 때문에 N개 워커가 있어도 서버가 받는 초당 요청 수는 1/interval로 묶인다.
    """

    def __init__(self, interval: float = 0.18) -> None:
        self.interval = interval
        self.calls = 0
        self.hits429 = 0
        self._last = 0.0
        self.floor = interval          # 429로 벌어진 간격을 되돌릴 때의 하한 = 사용자가 고른 간격
        self._quiet = 0                # 마지막 429 이후 조용히 지나간 호출 수
        self._lk = threading.Lock()

    def wait(self) -> None:
        with self._lk:
            gap = self.interval - (time.monotonic() - self._last)
            if gap > 0:
                time.sleep(gap)
            self._last = time.monotonic()
            self.calls += 1

    def penalize(self) -> None:
        """429를 맞으면 벌린다 — 단 **되돌아올 수 있을 만큼만** 벌린다.

        처음 판은 상한 3초·회복 200콜마다 10%였는데, 그러면 한 번 최대로 벌어진 뒤
        원래 간격으로 돌아오는 데 수천 콜(몇 시간)이 걸린다. 실제로 그 일이 났다 —
        429 몇 번에 처리량이 분당 95콜까지 떨어지고 회복되지 않았다.
        **벌은 즉각적이되 짧아야 한다.**
        """
        with self._lk:
            self.hits429 += 1
            self.interval = min(self.interval * 1.5, 0.8)
            self._quiet = 0

    def relax(self) -> None:
        with self._lk:
            self._quiet += 1
            if self._quiet >= 40:      # 40콜 조용하면 20%씩 되돌린다(벌 1.5배 → 회복 3~4스텝)
                self._quiet = 0
                self.interval = max(self.interval * 0.8, self.floor)


def _f(x: Any) -> float | None:
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _call(path: str, env: dict[str, str], th: Throttle, **q: Any) -> Any:
    """_get은 429를 자체 재시도한다. 여기서는 그 위에 간격 조정만 얹는다."""
    th.wait()
    try:
        return _get(path, env, **q)
    except RuntimeError as e:
        if "HTTP 429" in str(e):
            th.penalize()
            time.sleep(2.0)
            th.wait()
            return _get(path, env, **q)
        raise
    finally:
        th.relax()


# ── CSV 입출력 ──────────────────────────────────────────────
def read_series(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    out: dict[str, str] = {}
    with path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if row.get("date"):
                out[row["date"]] = row.get("value", "")
    return out


def write_series(path: Path, rows: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "value"])
        for d in sorted(rows):
            w.writerow([d, rows[d]])


def read_panel(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    out: dict[str, dict[str, str]] = {}
    with path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            d = row.pop("date", None)
            if d:
                out[d] = {k: v for k, v in row.items() if v not in ("", None)}
    return out


def write_panel(path: Path, rows: dict[str, dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date"] + PANEL_COLS, extrasaction="ignore")
        w.writeheader()
        for d in sorted(rows):
            w.writerow({"date": d, **rows[d]})


# ── 페이징 ──────────────────────────────────────────────────
def _page_candles(path: str, env, th, since: str, stop_at: str | None,
                  **extra: Any) -> dict[str, dict]:
    """캔들 — nextBefore 커서. count 상한 200.

    ⚠ 지수·국채는 심볼이 경로에 있지만 **종목 캔들(`/api/v1/candles`)은 `symbol`이 쿼리다.**
    extra로 받아 넘긴다.
    """
    out: dict[str, dict] = {}
    cursor = None
    for _ in range(MAX_PAGES):
        q: dict[str, Any] = {"interval": "1d", "count": 200, **extra}
        if cursor:
            q["before"] = cursor
        d = _call(path, env, th, **q) or {}
        candles = d.get("candles") or []
        if not candles:
            break
        for k in candles:
            day = (k.get("timestamp") or "")[:10]
            if day:
                out[day] = k
        oldest = min(out)
        if oldest < since or (stop_at and oldest <= stop_at):
            break
        cursor = d.get("nextBefore")
        if not cursor:
            break
    return out


def _page_records(path: str, env, th, since: str, stop_at: str | None,
                  **extra: Any) -> dict[str, dict]:
    """수급 계열 — nextUntil 커서. count 상한 100."""
    out: dict[str, dict] = {}
    cursor = None
    for _ in range(MAX_PAGES):
        q: dict[str, Any] = {"count": 100, **extra}
        if cursor:
            q["until"] = cursor
        d = _call(path, env, th, **q) or {}
        recs = d.get("records") or []
        if not recs:
            break
        for r in recs:
            day = r.get("date")
            if day:
                out[day] = r
        oldest = min(out)
        if oldest < since or (stop_at and oldest <= stop_at):
            break
        cursor = d.get("nextUntil")
        if not cursor:
            break
    return out


def _stop_at(existing: dict, full: bool) -> str | None:
    """증분: 이미 가진 가장 최근 날짜까지만 거슬러 올라간다."""
    return None if (full or not existing) else max(existing)


# ── 시장 계열 ───────────────────────────────────────────────
def backfill_market(env, th, since: str, full: bool, log) -> list[dict]:
    """지수 2 + 국채 6 캔들, 지수 투자자별 매매대금."""
    man: list[dict] = []
    for sym in INDEX_SYMBOLS + BOND_SYMBOLS:
        is_bond = sym.startswith("KR_BOND")
        sid = f"TOSS_{sym}" + ("" if is_bond else "_CLOSE")
        p = TOSS_DIR / f"{sid}.csv"
        cur = read_series(p)
        got = _page_candles(f"/api/v1/market-indicators/{sym}/candles", env, th,
                            since, _stop_at(cur, full))
        before = len(cur)
        for day, k in got.items():
            v = _f(k.get("closePrice"))
            if v is not None:
                cur[day] = f"{v:g}"
        write_series(p, cur)
        log(f"  {sid:26} {len(cur):>6,}행 (+{len(cur)-before})  "
            f"{min(cur) if cur else '-'} ~ {max(cur) if cur else '-'}")
        man.append({"series_id": sid, "name": f"{sym} 일봉 종가", "rows": len(cur),
                    "start": min(cur) if cur else None, "end": max(cur) if cur else None,
                    "csv": f"history/toss/{sid}.csv", "source": "tossinvest",
                    "tier": 1, "team": "", "units": "%" if is_bond else "pt",
                    "fetched_at": date.today().isoformat()})

    # 지수 투자자별 — 순매수(억원). 기관 세부 4종 포함
    who_map = [("individual", "INDIVIDUAL"), ("foreigner", "FOREIGNER"),
               ("institution", "INSTITUTION"), ("otherCorporation", "OTHERCORP")]
    br_map = [("pensionFund", "PENSION"), ("financialInvestment", "FININV"),
              ("trust", "TRUST"), ("insurance", "INSURANCE")]
    for sym in INDEX_SYMBOLS:
        series: dict[str, dict[str, str]] = {}
        probe = TOSS_DIR / f"TOSS_{sym}_FLOW_FOREIGNER.csv"
        got = _page_records(f"/api/v1/market-indicators/{sym}/investor-trading", env, th,
                            since, _stop_at(read_series(probe), full), interval="1d")
        for day, r in got.items():
            for key, tag in who_map:
                blk = r.get(key) or {}
                b, s = _f(blk.get("buyAmount")), _f(blk.get("sellAmount"))
                if b is not None and s is not None:
                    series.setdefault(tag, {})[day] = f"{(b - s) / 1e8:.0f}"
            br = ((r.get("institution") or {}).get("breakdown") or {})
            for key, tag in br_map:
                blk = br.get(key) or {}
                b, s = _f(blk.get("buyAmount")), _f(blk.get("sellAmount"))
                if b is not None and s is not None:
                    series.setdefault(f"INST_{tag}", {})[day] = f"{(b - s) / 1e8:.0f}"
        for tag, rows in sorted(series.items()):
            sid = f"TOSS_{sym}_FLOW_{tag}"
            p = TOSS_DIR / f"{sid}.csv"
            cur = read_series(p)
            before = len(cur)
            cur.update(rows)
            write_series(p, cur)
            log(f"  {sid:26} {len(cur):>6,}행 (+{len(cur)-before})  "
                f"{min(cur) if cur else '-'} ~ {max(cur) if cur else '-'}")
            man.append({"series_id": sid, "name": f"{sym} {tag} 순매수", "rows": len(cur),
                        "start": min(cur) if cur else None, "end": max(cur) if cur else None,
                        "csv": f"history/toss/{sid}.csv", "source": "tossinvest",
                        "tier": 1, "team": "", "units": "억원",
                        "fetched_at": date.today().isoformat()})
    return man


def backfill_fx(env, th, since: str, full: bool, log) -> list[dict]:
    """USD/KRW 일별 — `dateTime`을 하루씩 넣어 받는다(1일 = 1콜).

    ⚠ **2022-12-16 이전은 404**(2026-08-19 이분탐색으로 확인). 그 앞은 FRED·ECOS를 쓴다.
    ⚠ 영업일만 값이 있다. 주말·휴장일은 404가 정상이라 실패로 세지 않는다.
    """
    sid = "TOSS_USDKRW"
    p = TOSS_DIR / f"{sid}.csv"
    cur = read_series(p)
    before = len(cur)
    start = date.fromisoformat(max(FX_FIRST, since))
    today = date.today()
    day = today
    miss = 0
    while day >= start:
        key = day.isoformat()
        if day.weekday() > 4 or (not full and key in cur):
            day -= timedelta(days=1)
            continue
        try:
            d = _call("/api/v1/exchange-rate", env, th, baseCurrency="USD",
                      quoteCurrency="KRW", dateTime=f"{key}T15:30:00+09:00") or {}
        except RuntimeError as e:
            if "HTTP 404" in str(e):     # 휴장일 — 정상
                d = {}
            else:
                raise
        v = _f(d.get("rate"))
        if v is not None:
            cur[key] = f"{v:g}"
            miss = 0
        else:
            miss += 1
            if not full and miss > 12:   # 증분 실행에서 이미 가진 구간에 닿았다
                break
        day -= timedelta(days=1)
    write_series(p, cur)
    log(f"  {sid:26} {len(cur):>6,}행 (+{len(cur)-before})  "
        f"{min(cur) if cur else '-'} ~ {max(cur) if cur else '-'}")
    return [{"series_id": sid, "name": "USD/KRW (토스, 15:30 기준)", "rows": len(cur),
             "start": min(cur) if cur else None, "end": max(cur) if cur else None,
             "csv": f"history/toss/{sid}.csv", "source": "tossinvest", "tier": 1,
             "team": "", "units": "원", "fetched_at": date.today().isoformat()}]


def backfill_calendar(env, th, ahead_days: int, back_days: int, log) -> list[dict]:
    """장 운영 캘린더 — 하루 1콜. 값 1=정규장 개장, 0=휴장.

    왜 받는가 — **과거 휴장일은 캔들에 빠진 평일로 역산할 수 있지만, 미래 휴장일은 그럴 수 없다.**
    이벤트 캘린더·영업일 계산에 앞날의 휴장일이 필요해서 이쪽은 API로 받는다.
    """
    out: list[dict] = []
    for mk in ("KR", "US"):
        sid = f"TOSS_CAL_{mk}"
        p = TOSS_DIR / f"{sid}.csv"
        cur = read_series(p)
        before = len(cur)
        today = date.today()
        for off in range(-back_days, ahead_days + 1):
            day = today + timedelta(days=off)
            key = day.isoformat()
            if key in cur and off < 0:      # 과거는 안 변한다 — 다시 안 받는다
                continue
            d = _call(f"/api/v1/market-calendar/{mk}", env, th, date=key) or {}
            blk = (d.get("today") or {})
            body = blk.get("integrated") or blk
            open_ = 1 if ((body.get("regularMarket") or {}).get("startTime")) else 0
            cur[key] = str(open_)
        write_series(p, cur)
        log(f"  {sid:26} {len(cur):>6,}행 (+{len(cur)-before})  "
            f"{min(cur) if cur else '-'} ~ {max(cur) if cur else '-'}  "
            f"휴장 {sum(1 for v in cur.values() if v == '0'):,}일")
        out.append({"series_id": sid, "name": f"{mk} 정규장 개장 여부", "rows": len(cur),
                    "start": min(cur) if cur else None, "end": max(cur) if cur else None,
                    "csv": f"history/toss/{sid}.csv", "source": "tossinvest", "tier": 2,
                    "team": "", "units": "1=개장", "fetched_at": date.today().isoformat()})
    return out


def backfill_intraday(env, th, log) -> list[dict]:
    """지수 1분봉 — 이벤트 스터디(갭/장중 분해)용.

    ⚠ **보관 기간이 짧다. 실측 약 8영업일치(2,800봉)뿐**이다.
    장기 축적을 원하면 **매일 돌려 이어붙이는 수밖에 없다** — 한 번에 몰아 받을 수 없다.
    그래서 증분 병합이 기본이고, 기존 행은 절대 지우지 않는다.
    """
    out: list[dict] = []
    for sym in INDEX_SYMBOLS:
        sid = f"TOSS_{sym}_1M"
        p = TOSS_DIR / f"{sid}.csv"
        cur = read_series(p)
        before = len(cur)
        cursor = None
        for _ in range(20):
            q: dict[str, Any] = {"interval": "1m", "count": 200}
            if cursor:
                q["before"] = cursor
            d = _call(f"/api/v1/market-indicators/{sym}/candles", env, th, **q) or {}
            candles = d.get("candles") or []
            if not candles:
                break
            for k in candles:
                ts = (k.get("timestamp") or "")[:16]     # 분 단위 키
                v = _f(k.get("closePrice"))
                if ts and v is not None:
                    cur[ts] = f"{v:g}"
            cursor = d.get("nextBefore")
            if not cursor:
                break
        write_series(p, cur)
        log(f"  {sid:26} {len(cur):>6,}행 (+{len(cur)-before})  "
            f"{min(cur) if cur else '-'} ~ {max(cur) if cur else '-'}")
        out.append({"series_id": sid, "name": f"{sym} 1분봉 종가", "rows": len(cur),
                    "start": min(cur) if cur else None, "end": max(cur) if cur else None,
                    "csv": f"history/toss/{sid}.csv", "source": "tossinvest", "tier": 2,
                    "team": "", "units": "pt", "fetched_at": date.today().isoformat()})
    return out


# ── 종목 유니버스 ───────────────────────────────────────────
def load_universe(env, th, log) -> list[dict]:
    """전 종목 마스터 + 시가총액. 시총 순으로 정렬해 돌려준다.

    ⚠ `/api/v1/stocks`·`/prices`는 심볼을 묶어 보낼 수 있다 —
    한 번에 몇 개까지 되는지는 스펙에 없어 실측으로 100개씩 자른다.
    """
    rows: list[dict] = []
    for mk in ("KOSPI", "KOSDAQ"):
        got = _call("/api/v1/stocks/all", env, th, market=mk) or []
        for r in got:
            r["market"] = mk
            rows.append(r)
    log(f"  전 종목 마스터 {len(rows):,}개 (KOSPI+KOSDAQ)")

    syms = [r["symbol"] for r in rows]
    info: dict[str, dict] = {}
    price: dict[str, dict] = {}
    for i in range(0, len(syms), 100):
        chunk = ",".join(syms[i:i + 100])
        for r in (_call("/api/v1/stocks", env, th, symbols=chunk) or []):
            info[r.get("symbol")] = r
        for r in (_call("/api/v1/prices", env, th, symbols=chunk) or []):
            price[r.get("symbol")] = r
    for r in rows:
        s = r["symbol"]
        sh = _f((info.get(s) or {}).get("sharesOutstanding"))
        px = _f((price.get(s) or {}).get("lastPrice"))
        r["shares"] = sh
        r["price"] = px
        r["mktcap"] = (sh * px / 1e12) if (sh and px) else 0.0
    rows.sort(key=lambda r: r["mktcap"], reverse=True)
    have = sum(1 for r in rows if r["mktcap"] > 0)
    log(f"  시가총액 산출 {have:,}/{len(rows):,}개 · 최대 {rows[0]['mktcap']:,.0f}조원 "
        f"({rows[0].get('name')})")
    return rows


def save_universe(rows: list[dict], log) -> None:
    p = TOSS_DIR / "_universe.csv"
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["symbol", "name", "market", "securityType", "isinCode",
                    "shares", "price", "mktcap_trillion"])
        for r in rows:
            w.writerow([r.get("symbol"), r.get("name"), r.get("market"),
                        r.get("securityType"), r.get("isinCode"),
                        f"{r['shares']:.0f}" if r.get("shares") else "",
                        f"{r['price']:g}" if r.get("price") else "",
                        f"{r['mktcap']:.4f}" if r.get("mktcap") else ""])
    log(f"  → {p}")


# ── 종목 패널 ───────────────────────────────────────────────
def backfill_symbol(sym: str, env, th, since: str, full: bool,
                    kinds: list[str], with_close: bool) -> tuple[int, int]:
    p = STOCK_DIR / f"{sym}.csv"
    panel = read_panel(p)
    before = len(panel)
    stop = _stop_at(panel, full)

    def put(day: str, col: str, val: Any) -> None:
        if val is None:
            return
        panel.setdefault(day, {})[col] = f"{val:g}" if isinstance(val, float) else str(val)

    for kind in kinds:
        got = _page_records(f"/api/v1/stocks/{sym}/{_KIND_EP[kind]}", env, th, since, stop)
        for day, r in got.items():
            if kind == "short":
                rate = _f(r.get("shortSellingVolumeRate"))
                put(day, "short_rate", round(rate * 100, 4) if rate is not None else None)
                amt = _f(r.get("shortSellingAmount"))
                put(day, "short_amt", round(amt / 1e8, 1) if amt is not None else None)
            elif kind == "credit":
                m = r.get("marginLoan") or {}
                put(day, "credit_qty", _f(m.get("balanceQuantity")))
                cr = _f(m.get("balanceRate"))
                put(day, "credit_rate", round(cr * 100, 4) if cr is not None else None)
            elif kind == "lending":
                put(day, "lending_qty", _f(r.get("balanceQuantity")))
                la = _f(r.get("balanceAmount"))
                put(day, "lending_amt", round(la / 1e8, 1) if la is not None else None)
            elif kind == "program":
                put(day, "prog_arb", _f((r.get("arbitrage") or {}).get("netBuyVolume")))
                put(day, "prog_nonarb", _f((r.get("nonArbitrage") or {}).get("netBuyVolume")))
            else:  # investor
                for key, col in (("foreigner", "net_foreigner"), ("institution", "net_institution"),
                                 ("individual", "net_individual"), ("otherCorporation", "net_other")):
                    blk = r.get(key)
                    put(day, col, _f(blk.get("netBuyVolume")) if isinstance(blk, dict) else None)
                fh = r.get("foreignerHolding") or {}
                hr = _f(fh.get("holdingRate"))
                put(day, "foreign_hold_rate", round(hr * 100, 3) if hr is not None else None)
                hq, lq = _f(fh.get("holdingQuantity")), _f(fh.get("limitQuantity"))
                put(day, "foreign_limit_rate", round(hq / lq * 100, 3) if (hq and lq) else None)

    if with_close:
        got = _page_candles("/api/v1/candles", env, th, since, stop,
                            symbol=sym, adjusted="true")
        for day, k in got.items():
            put(day, "close", _f(k.get("closePrice")))

    write_panel(p, panel)
    return len(panel), len(panel) - before


def _load_ckpt() -> dict:
    if CKPT.exists():
        try:
            return json.loads(CKPT.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def _save_ckpt(d: dict) -> None:
    CKPT.parent.mkdir(parents=True, exist_ok=True)
    CKPT.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")


def update_manifest(entries: list[dict]) -> None:
    """history.py와 같은 _manifest.json에 얹는다 — 다른 소스 항목은 건드리지 않는다."""
    prev: dict[str, dict] = {}
    if MANIFEST.exists():
        try:
            prev = {m["series_id"]: m
                    for m in json.loads(MANIFEST.read_text(encoding="utf-8")).get("series", [])}
        except Exception:
            prev = {}
    prev.update({m["series_id"]: m for m in entries})
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps({
        "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "series_count": len(prev),
        "series": sorted(prev.values(), key=lambda m: m["series_id"]),
    }, ensure_ascii=False, indent=2), encoding="utf-8")


def collect(what: str = "all", since: str = DEFAULT_SINCE, top: int = 100,
            symbols: list[str] | None = None, kinds: list[str] | None = None,
            full: bool = False, with_close: bool = True, dry_run: bool = False,
            resume: bool = True, interval: float = 0.18, workers: int = 8) -> int:
    env = load_env()
    if not (env.get("TOSSINVEST_CLIENT_ID") and env.get("TOSSINVEST_CLIENT_SECRET")):
        print("TOSSINVEST_CLIENT_ID/SECRET 없음 — 이 키는 **각자 본인 앱**으로 발급합니다"
              "(허용 IP가 사람마다 달라 공유가 불가능). https://developers.tossinvest.com "
              "→ 앱 생성 → 본인 공인 IP 등록 → `python -m databook setup`")
        return 1
    kinds = kinds or KINDS
    bad = [k for k in kinds if k not in _KIND_EP]
    if bad:
        print(f"모르는 kind: {bad} — 가능: {list(_KIND_EP)}")
        return 1

    from .tosslock import toss_lock
    with toss_lock(f"tossback --what {what}", wait=0.0) as got:
        if not got:
            return 1
        return _collect(env, what, since, top, symbols, kinds, full, with_close,
                        dry_run, resume, interval, workers)


def _collect(env, what, since, top, symbols, kinds, full, with_close,
             dry_run, resume, interval, workers) -> int:
    th = Throttle(interval)
    t0 = time.time()
    lines: list[str] = []

    def log(s: str) -> None:
        print(s, flush=True)
        lines.append(s)

    man: list[dict] = []
    do_market = what in ("all", "market")
    do_stocks = what in ("all", "stocks")
    do_fx = what in ("all", "market", "fx")
    do_cal = what in ("all", "market", "calendar")
    do_intra = what in ("all", "market", "intraday")

    if do_market:
        log(f"[시장 계열] 지수 2 + 국채 6 캔들 · 투자자별 매매대금 (since {since})")
        if dry_run:
            log("  (dry-run — 호출 안 함)")
        else:
            man += backfill_market(env, th, since, full, log)

    if do_fx and not dry_run:
        log(f"[환율] USD/KRW 일별 (가용 시작 {FX_FIRST})")
        man += backfill_fx(env, th, since, full, log)

    if do_cal and not dry_run:
        log("[캘린더] 장 운영 여부 — 과거 400일 + 향후 400일")
        man += backfill_calendar(env, th, 400, 400, log)

    if do_intra and not dry_run:
        log("[1분봉] 지수 — 보관 약 8영업일뿐이라 매일 돌려야 쌓인다")
        man += backfill_intraday(env, th, log)

    universe: list[dict] = []
    if do_stocks:
        if symbols:
            targets = [{"symbol": s, "name": s, "mktcap": 0.0} for s in symbols]
            log(f"[종목 패널] 지정 {len(targets)}종목 · kinds={kinds}")
        else:
            log("[유니버스] 전 종목 마스터 + 시가총액 산출")
            if dry_run:
                log("  (dry-run — 호출 안 함)")
                targets = []
            else:
                universe = load_universe(env, th, log)
                save_universe(universe, log)
                targets = universe if top <= 0 else universe[:top]
                cover = (sum(r["mktcap"] for r in targets)
                         / max(sum(r["mktcap"] for r in universe), 1e-9) * 100)
                log(f"[종목 패널] 시총 상위 {len(targets):,}종목 "
                    f"(전체 시총의 {cover:.1f}%) · kinds={kinds}")

        ck = _load_ckpt() if resume else {}
        done: set[str] = set(ck.get("done", [])) if (resume and not full) else set()
        todo = [r for r in targets if r["symbol"] not in done]
        if dry_run:
            for i, r in enumerate(todo, 1):
                log(f"  [{i:4d}/{len(todo)}] {r['symbol']} (dry-run)")
        else:
            # 직렬로는 종목당 약 16초(호출 96회 × 왕복 0.16초) → 4,300종목이면 19시간이다.
            # 병목은 스로틀이 아니라 **왕복 지연**이라 워커를 늘리면 그대로 줄어든다.
            # 서버가 받는 초당 요청 수는 공유 Throttle이 계속 묶으므로 429 위험은 그대로다.
            if todo:
                _get("/api/v1/prices", env, symbols=todo[0]["symbol"])   # 토큰 선점 — 워커들이 동시에 발급해 서로 죽이는 걸 막는다
            lk = threading.Lock()
            n_done = 0

            def work(r: dict) -> tuple[dict, Any]:
                try:
                    return r, backfill_symbol(r["symbol"], env, th, since, full, kinds, with_close)
                except Exception as e:
                    return r, e

            with ThreadPoolExecutor(max_workers=workers) as pool:
                futs = [pool.submit(work, r) for r in todo]
                for fut in as_completed(futs):
                    r, res = fut.result()
                    sym = r["symbol"]
                    with lk:
                        n_done += 1
                        i = n_done
                        if isinstance(res, Exception):
                            log(f"  [{i:4d}/{len(todo)}] {sym:8} FAIL {type(res).__name__}: {str(res)[:90]}")
                        else:
                            rows, added = res
                            done.add(sym)
                            el = time.time() - t0
                            eta = (len(todo) - i) * el / max(i, 1) / 60
                            log(f"  [{i:4d}/{len(todo)}] {sym:8} {r.get('name', '')[:12]:14} "
                                f"{rows:>5,}행 (+{added})  {th.calls:,}콜 {el:.0f}초 "
                                f"{th.calls/max(el,1)*60:.0f}req/분 간격{th.interval:.2f} "
                                f"429×{th.hits429} ETA {eta:.0f}분")
                        if i % 20 == 0:
                            _save_ckpt({"done": sorted(done),
                                        "updated": datetime.now().isoformat(timespec="seconds")})
        if not dry_run:
            _save_ckpt({"done": sorted(done), "updated": datetime.now().isoformat(timespec="seconds")})
            man.append({"series_id": "TOSS_STOCK_PANEL", "name": "종목 수급 패널(와이드)",
                        "rows": len(done), "start": None, "end": date.today().isoformat(),
                        "csv": "history/toss/stocks/{symbol}.csv", "source": "tossinvest",
                        "tier": 1, "team": "", "units": "혼합",
                        "fetched_at": date.today().isoformat()})

    if dry_run:
        return 0
    if man:
        update_manifest(man)
    el = time.time() - t0
    print(f"\n완료: {th.calls:,}콜 / {el:.0f}초 ({th.calls/max(el,1)*60:.0f}req/분) "
          f"· 429 {th.hits429}회 · 최종 간격 {th.interval:.2f}초")
    print(f"  → {TOSS_DIR}")
    return 0
