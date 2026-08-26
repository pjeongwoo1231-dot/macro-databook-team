"""빅테크 실적발표 캘린더 — MANGOS / Fab 10.

한국 증시는 미국 빅테크 실적에 반응한다. 특히 반도체·AI 밸류체인 비중이 큰 코스피는
NVDA 실적 다음날 갭으로 반응하는 일이 잦다. 그 반응을 **재는** 데이터를 만든다.

바스켓 정의 (2026년 기준)
- **MANGOS** — Meta · Anthropic · Nvidia · Google · OpenAI · SpaceX
  AI 스택(모델·칩·사용자·클라우드·인프라) 중심. Apple·Microsoft·Amazon·Tesla를 뺀다.
- **Fab 10** (Vanda Research, "Frontier AI & Big Tech 10") — Magnificent 7 + SpaceX + OpenAI + Anthropic

⚠ **Anthropic과 OpenAI는 비상장이라 실적발표가 없다.** 바스켓에는 들어가지만 이 캘린더에는 안 잡힌다.
바스켓 수익률을 계산할 때 "6종목 중 4종목만 관측된다"는 점을 반드시 명시할 것.

데이터 한계 (2026-08-05 확인)
- Nasdaq `earnings-surprise` API는 **최근 4분기만** 준다. 장기 이벤트 스터디는 이 소스로 불가능하다.
- 향후 일정은 날짜별 캘린더를 훑어야 한다(요청 1건/일). 기본 120일로 제한한다.
- `SPCX`(SpaceX)는 2026년 6월 상장이라 **실적 이력이 없다.**
"""
from __future__ import annotations

import csv
import json
import urllib.request
from datetime import date, datetime, timedelta
from typing import Any

from .core import OUTPUT_DIR
from .fetchers.base import BROWSER_UA, throttle

EARN_DIR = OUTPUT_DIR / "earnings"
NASDAQ = "https://api.nasdaq.com/api"

# 티커 → 표시명. 비상장은 ticker=None
BASKETS: dict[str, dict[str, str | None]] = {
    "MANGOS": {
        "Meta": "META",
        "Anthropic": None,        # 비상장
        "Nvidia": "NVDA",
        "Google": "GOOGL",
        "OpenAI": None,           # 비상장
        "SpaceX": "SPCX",
    },
    "FAB10": {
        "Nvidia": "NVDA",
        "Apple": "AAPL",
        "Alphabet": "GOOGL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Meta": "META",
        "Tesla": "TSLA",
        "SpaceX": "SPCX",
        "OpenAI": None,
        "Anthropic": None,
    },
}


def _get(url: str) -> Any:
    throttle("api.nasdaq.com", 0.8)
    req = urllib.request.Request(url, headers={
        "User-Agent": BROWSER_UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode("utf-8"))


def tickers(basket: str | None = None) -> dict[str, str]:
    """상장된 것만. 티커 → 표시명. 두 바스켓에 겹치는 종목(GOOGL 등)은 한 번만."""
    out: dict[str, str] = {}
    for bname, members in BASKETS.items():
        if basket and bname != basket.upper():
            continue
        for name, tk in members.items():
            if tk:
                out.setdefault(tk, name)
    return out


def fetch_surprise(ticker: str) -> list[dict[str, Any]]:
    """최근 4분기 실적 서프라이즈. 없으면 빈 리스트."""
    try:
        d = _get(f"{NASDAQ}/company/{ticker}/earnings-surprise")
        rows = (d.get("data") or {}).get("earningsSurpriseTable", {}).get("rows") or []
    except Exception:
        return []
    out = []
    for r in rows:
        try:
            rd = datetime.strptime(r["dateReported"], "%m/%d/%Y").date().isoformat()
        except Exception:
            continue
        def num(v: Any) -> float | None:
            try:
                return float(str(v).replace("$", "").replace(",", "").strip())
            except (TypeError, ValueError):
                return None
        out.append({
            "date_reported": rd,
            "fiscal_quarter": r.get("fiscalQtrEnd", ""),
            "eps": num(r.get("eps")),
            "consensus": num(r.get("consensusForecast")),
            "surprise_pct": num(r.get("percentageSurprise")),
        })
    return sorted(out, key=lambda x: x["date_reported"])


def fetch_calendar(day: str, wanted: set[str]) -> list[dict[str, Any]]:
    try:
        d = _get(f"{NASDAQ}/calendar/earnings?date={day}")
        rows = (d.get("data") or {}).get("rows") or []
    except Exception:
        return []
    return [{"date": day, "symbol": r.get("symbol", ""), "name": r.get("name", ""),
             "time": r.get("time", ""), "fiscal_quarter": r.get("fiscalQuarterEnding", "")}
            for r in rows if r.get("symbol") in wanted]


def collect(basket: str | None = None, ahead: int = 120, dry_run: bool = False) -> int:
    tk = tickers(basket)   # 티커 → 이름
    private = [n for b, mem in BASKETS.items()
               if not basket or b == (basket or "").upper()
               for n, v in mem.items() if v is None]
    print(f"바스켓: {basket.upper() if basket else 'MANGOS + FAB10'}")
    print(f"  상장 {len(tk)}종목: {', '.join(sorted(tk))}")
    if private:
        print(f"  ⚠ 비상장 {len(set(private))}곳(실적발표 없음): {', '.join(sorted(set(private)))}")
    if dry_run:
        return 0

    EARN_DIR.mkdir(parents=True, exist_ok=True)
    wanted = set(tk)

    # 1) 최근 4분기 실적 서프라이즈
    print("\n실적 서프라이즈 (최근 4분기)")
    sur_rows: list[dict[str, Any]] = []
    for t, name in sorted(tk.items()):
        rows = fetch_surprise(t)
        if not rows:
            print(f"  [--  ] {t:6s} 이력 없음 (신규 상장 등)")
            continue
        for r in rows:
            sur_rows.append({"symbol": t, "company": name, **r})
        last = rows[-1]
        print(f"  [OK  ] {t:6s} {len(rows)}건  최근 {last['date_reported']} "
              f"EPS {last['eps']} vs 예상 {last['consensus']} → 서프라이즈 {last['surprise_pct']}%")
    if sur_rows:
        p = EARN_DIR / "surprise.csv"
        with p.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["symbol", "company", "date_reported",
                                              "fiscal_quarter", "eps", "consensus", "surprise_pct"])
            w.writeheader()
            w.writerows(sorted(sur_rows, key=lambda r: (r["date_reported"], r["symbol"])))

    # 2) 향후 일정
    print(f"\n향후 실적 일정 (앞으로 {ahead}일 스캔)")
    today = date.today()
    upcoming: list[dict[str, Any]] = []
    for i in range(ahead):
        d = today + timedelta(days=i)
        if d.weekday() >= 5:          # 주말은 발표가 없다 — 요청 낭비 방지
            continue
        hits = fetch_calendar(d.isoformat(), wanted)
        for h in hits:
            print(f"  {h['date']}  {h['symbol']:6s} {h['name'][:32]:34s} {h['time']}")
        upcoming.extend(hits)
    if upcoming:
        p = EARN_DIR / "upcoming.csv"
        with p.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["date", "symbol", "name", "time", "fiscal_quarter"])
            w.writeheader()
            w.writerows(sorted(upcoming, key=lambda r: (r["date"], r["symbol"])))
    else:
        print("  (해당 기간에 잡힌 일정 없음)")

    # 3) 코스피 반응 조인
    # 빅테크는 미 장 마감 후(한국시간 새벽) 발표하므로, 반응은 '발표일 다음 한국 거래일'의
    # 시가 갭에 실린다. events 모듈과 같은 분해를 쓴다.
    if sur_rows:
        try:
            from .events import build_returns, fetch_ohlc, next_trading_day
            rets = build_returns(fetch_ohlc("^KS11", "2024-01-01"))
            days = sorted(rets)
            rp = EARN_DIR / "earnings_reaction.csv"
            n = 0
            with rp.open("w", encoding="utf-8", newline="") as f:
                w = csv.writer(f)
                w.writerow(["date_reported", "symbol", "surprise_pct", "reaction_date",
                            "kospi_gap_pct", "kospi_intraday_pct", "kospi_close_pct"])
                for r in sorted(sur_rows, key=lambda x: x["date_reported"]):
                    rd = next_trading_day(r["date_reported"], days)
                    if not rd:
                        continue
                    k = rets[rd]
                    w.writerow([r["date_reported"], r["symbol"], r["surprise_pct"], rd,
                                f"{k['gap']:.4f}", f"{k['intraday']:.4f}",
                                f"{k['close_to_close']:.4f}"])
                    n += 1
            print(f"\n코스피 반응 조인: {n}건 → {rp.name}")
        except Exception as e:
            print(f"\n코스피 반응 조인 실패: {type(e).__name__}: {e}")

    print(f"\n완료: 서프라이즈 {len(sur_rows)}건 · 예정 {len(upcoming)}건")
    print(f"  → {EARN_DIR}")
    print("\n⚠ 과거 이력은 Nasdaq API가 최근 4분기만 제공한다. 장기 이벤트 스터디는 이 소스로 불가능하다.")
    return 0
