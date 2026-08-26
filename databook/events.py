"""매크로 이벤트 캘린더 + 코스피 반응 수익률 분해.

두 가지를 만든다.

1. **이벤트 캘린더** — FRED 릴리스 일정 API에서 미국 주요 지표의 **실제 발표일**을 받는다.
   "매월 몇째 주" 같은 추정이 아니라 BLS/BEA가 실제로 발표한 날짜다.

2. **반응 수익률** — 코스피 OHLC를 받아 익일 수익률을 **갭과 장중으로 분해**한다.

왜 분해하는가: 미국 지표는 한국시간 밤(보통 21:30/22:30 KST)에 나온다.
따라서 반응은 **다음 거래일 시가에 대부분 반영**되고, 장중은 다른 요인이 섞인다.
종가-종가 하나로 뭉치면 두 효과가 상쇄되어 계수가 0으로 보인다.

    gap     = ln(당일 시가 / 전일 종가)     ← 미국 발표의 1차 반응
    intra   = ln(당일 종가 / 당일 시가)     ← 국내 장중 요인
    close   = gap + intra                  ← 흔히 쓰는 익일 수익률

산출물은 `output/events/` 에 CSV로 쓴다. 분석 스크립트용 데이터다.
"""
from __future__ import annotations

import csv
import json
import math
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any

from .core import OUTPUT_DIR, load_env
from .fetchers.base import BROWSER_UA, get_json

EVENTS_DIR = OUTPUT_DIR / "events"
REL_BASE = "https://api.stlouisfed.org/fred/release/dates"
YAHOO = "https://query1.finance.yahoo.com/v8/finance/chart/"

# FRED release_id → (짧은 코드, 한글명). 코드는 회귀의 더미변수 이름이 된다.
RELEASES: dict[int, tuple[str, str]] = {
    10: ("CPI", "소비자물가"),
    50: ("NFP", "고용상황(비농업고용·실업률)"),
    53: ("GDP", "GDP"),
    54: ("PCE", "개인소득·지출(PCE 물가)"),
    46: ("PPI", "생산자물가"),
    9: ("RETAIL", "소매판매"),
    13: ("INDPRO", "산업생산"),
    192: ("JOLTS", "구인·이직(JOLTS)"),
}

DEFAULT_INDEX = "^KS11"  # 코스피


def fetch_release_dates(release_id: int, api_key: str, start: str) -> list[str]:
    url = (f"{REL_BASE}?release_id={release_id}&api_key={api_key}&file_type=json"
           f"&realtime_start={start}&realtime_end=2030-12-31&limit=10000&sort_order=asc")
    data = get_json(url)
    return [d["date"] for d in data.get("release_dates", [])]


def fetch_ohlc(symbol: str, start: str) -> dict[str, dict[str, float]]:
    """Yahoo chart API — 일별 OHLC. 결측(휴장·데이터 누락) 행은 버린다."""
    p1 = int(datetime.strptime(start, "%Y-%m-%d").timestamp())
    p2 = int(datetime.utcnow().timestamp())
    url = f"{YAHOO}{urllib.parse.quote(symbol)}?period1={p1}&period2={p2}&interval=1d"
    req = urllib.request.Request(url, headers={"User-Agent": BROWSER_UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    res = data["chart"]["result"][0]
    q = res["indicators"]["quote"][0]
    out: dict[str, dict[str, float]] = {}
    for i, ts in enumerate(res["timestamp"]):
        o, c = q["open"][i], q["close"][i]
        if o in (None, 0) or c in (None, 0):
            continue
        d = datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d")
        out[d] = {"open": float(o), "close": float(c),
                  "high": float(q["high"][i] or c), "low": float(q["low"][i] or c)}
    return out


def build_returns(ohlc: dict[str, dict[str, float]]) -> dict[str, dict[str, float]]:
    """거래일 순서대로 갭·장중·종가 로그수익률(%)을 계산."""
    days = sorted(ohlc)
    out: dict[str, dict[str, float]] = {}
    for i in range(1, len(days)):
        d, prev = days[i], days[i - 1]
        po, pc = ohlc[prev]["close"], ohlc[d]["close"]
        o = ohlc[d]["open"]
        if po <= 0 or o <= 0 or pc <= 0:
            continue
        gap = math.log(o / po) * 100
        intra = math.log(pc / o) * 100
        rng = (ohlc[d]["high"] - ohlc[d]["low"]) / po * 100
        out[d] = {"gap": gap, "intraday": intra, "close_to_close": gap + intra,
                  "range": rng,
                  # 일중 변동폭 0 = 휴장 플레이스홀더/데이터 결손. 회귀에서 제외할 것
                  "suspect": 1 if rng == 0 else 0}
    return out


def next_trading_day(d: str, trading_days: list[str]) -> str | None:
    """미국 발표일 d 이후 첫 한국 거래일. 발표가 한국 밤이므로 당일이 아니라 '다음 날'이 반응일."""
    for t in trading_days:
        if t > d:
            return t
    return None


def collect(since: str = "2000-01-01", symbol: str = DEFAULT_INDEX,
            dry_run: bool = False) -> int:
    env = load_env()
    key = env.get("FRED_API_KEY", "")
    if not key and not dry_run:
        print("FRED_API_KEY 없음 (.env 확인)")
        return 1

    if dry_run:
        print(f"이벤트 {len(RELEASES)}종 · 지수 {symbol} · 시작 {since} (dry-run)")
        for rid, (code, name) in RELEASES.items():
            print(f"  release_id={rid:4d}  {code:7s} {name}")
        return 0

    print(f"이벤트 캘린더 수집 — {len(RELEASES)}종 · 시작 {since}")
    events: list[tuple[str, str, str]] = []  # (발표일, 코드, 한글명)
    for rid, (code, name) in RELEASES.items():
        try:
            dates = [d for d in fetch_release_dates(rid, key, since) if d >= since]
        except Exception as e:
            print(f"  [FAIL] {code:7s} {type(e).__name__}: {e}")
            continue
        events.extend((d, code, name) for d in dates)
        print(f"  [OK  ] {code:7s} {len(dates):>4d}건  {dates[0] if dates else '-'} ~ {dates[-1] if dates else '-'}")

    print(f"\n지수 OHLC 수집 — {symbol}")
    try:
        ohlc = fetch_ohlc(symbol, since)
    except Exception as e:
        print(f"  [FAIL] {type(e).__name__}: {e}")
        return 1
    rets = build_returns(ohlc)
    days = sorted(rets)
    print(f"  [OK  ] 거래일 {len(days):,}일  {days[0]} ~ {days[-1]}")

    EVENTS_DIR.mkdir(parents=True, exist_ok=True)

    # 1) 이벤트 캘린더
    cal = EVENTS_DIR / "calendar.csv"
    with cal.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["release_date", "event_code", "event_name", "reaction_date"])
        for d, code, name in sorted(events):
            w.writerow([d, code, name, next_trading_day(d, days) or ""])

    # 2) 지수 수익률 (갭/장중 분해)
    ret = EVENTS_DIR / f"{symbol.lstrip('^')}_returns.csv"
    with ret.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "gap_pct", "intraday_pct", "close_to_close_pct", "range_pct", "suspect"])
        for d in days:
            r = rets[d]
            w.writerow([d, f"{r['gap']:.4f}", f"{r['intraday']:.4f}",
                        f"{r['close_to_close']:.4f}", f"{r['range']:.4f}", r["suspect"]])

    # 3) 회귀용 조인 테이블 — 반응일 기준, 이벤트 더미 wide 포맷
    codes = sorted({c for c, _ in RELEASES.values()} | {c for _, c, _ in events})
    by_day: dict[str, set[str]] = {}
    for d, code, _ in events:
        rd = next_trading_day(d, days)
        if rd:
            by_day.setdefault(rd, set()).add(code)
    panel = EVENTS_DIR / "event_panel.csv"
    with panel.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "gap_pct", "intraday_pct", "close_to_close_pct", "range_pct",
                    "suspect", "n_events"] + [f"ev_{c}" for c in codes])
        for d in days:
            r = rets[d]
            ev = by_day.get(d, set())
            w.writerow([d, f"{r['gap']:.4f}", f"{r['intraday']:.4f}",
                        f"{r['close_to_close']:.4f}", f"{r['range']:.4f}", r["suspect"], len(ev)]
                       + [1 if c in ev else 0 for c in codes])

    hit = sum(1 for d in days if d in by_day)
    print(f"\n완료: 이벤트 {len(events):,}건 · 거래일 {len(days):,}일 · 이벤트가 붙은 거래일 {hit:,}일")
    print(f"  → {cal}")
    print(f"  → {ret}")
    print(f"  → {panel}")
    print("\n주의: 반응일은 '발표일 다음 한국 거래일'이다. 미국 발표가 한국 밤이라 "
          "당일 종가에는 반영될 수 없다(look-ahead 방지).")
    return 0
