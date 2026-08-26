"""미국 매크로 이벤트 → 코스피 반응 회귀.

원 기획서의 "③ 회귀 기반 계수 추정 툴"에 해당한다.
`events` 모듈이 만든 `event_panel.csv`를 읽어 **이벤트 더미의 계수와 유의성**을 추정한다.

핵심 설계 — **갭과 장중을 나눠서 본다**
미국 지표는 한국시간 밤에 발표되므로 반응은 **다음 거래일 시가 갭**에 실린다.
종가-종가 하나로 뭉치면 갭 효과와 장중 요인이 섞여 계수가 0으로 보일 수 있다.
따라서 같은 회귀를 gap / intraday / close_to_close 세 종속변수에 각각 돌린다.

통제
- 요일 더미(월~목, 금요일 기준) · 월 더미는 생략(이벤트가 특정 월에 몰리지 않음)
- **전일 |수익률|** — 변동성 군집(volatility clustering) 흡수
- `suspect=1`(일중 변동폭 0 = 데이터 결손) 행 제외

주의
- 이벤트 더미는 **"발표가 있었다"** 만 나타낸다. **서프라이즈 크기가 아니다.**
  컨센서스 데이터가 없어 방향성 해석은 불가능하다
- 같은 날 여러 지표가 함께 발표되므로 더미들이 서로 상관된다
"""
from __future__ import annotations

import csv
import math
from datetime import datetime
from typing import Any

import numpy as np

from .core import OUTPUT_DIR
from .topics import ols

PANEL = OUTPUT_DIR / "events" / "event_panel.csv"
OUT = OUTPUT_DIR / "events"


def load_panel() -> list[dict[str, Any]]:
    if not PANEL.exists():
        return []
    rows = []
    with PANEL.open(encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if r.get("suspect") == "1":
                continue
            try:
                r["_d"] = datetime.strptime(r["date"], "%Y-%m-%d")
                for k in ("gap_pct", "intraday_pct", "close_to_close_pct", "range_pct"):
                    r[k] = float(r[k])
            except (ValueError, KeyError):
                continue
            rows.append(r)
    rows.sort(key=lambda r: r["_d"])
    return rows


def build(rows: list[dict[str, Any]], codes: list[str], absolute: bool
          ) -> tuple[np.ndarray, list[str], dict[str, np.ndarray]]:
    n = len(rows)
    cols = [np.ones(n)]
    names = ["const"]
    for c in codes:                      # 이벤트 더미
        cols.append(np.array([1.0 if r.get(f"ev_{c}") == "1" else 0.0 for r in rows]))
        names.append(c)
    for wd in range(4):                  # 월~목 (금요일 기준범주)
        cols.append(np.array([1.0 if r["_d"].weekday() == wd else 0.0 for r in rows]))
        names.append(["Mon", "Tue", "Wed", "Thu"][wd])
    lag = [0.0] + [abs(rows[i - 1]["close_to_close_pct"]) for i in range(1, n)]
    cols.append(np.array(lag))
    names.append("lag|ret|")
    X = np.column_stack(cols)
    ys = {}
    for k, lbl in (("gap_pct", "gap"), ("intraday_pct", "intraday"),
                   ("close_to_close_pct", "close")):
        v = np.array([r[k] for r in rows])
        ys[lbl] = np.abs(v) if absolute else v
    return X, names, ys


def _report(title: str, X: np.ndarray, names: list[str], ys: dict[str, np.ndarray],
            codes: list[str]) -> list[dict[str, Any]]:
    print(f"\n{'='*66}\n{title}\n{'='*66}")
    out = []
    for lbl, y in ys.items():
        res = ols(y, X, names)
        ev = [r for r in res if r[0] in codes]
        sig = [r for r in ev if r[3] < 0.10]
        print(f"\n[{lbl}]  이벤트 더미 {len(ev)}개 중 유의(p<0.10) {len(sig)}개")
        for nm, b, t, pv in sorted(ev, key=lambda x: x[3]):
            star = "***" if pv < 0.01 else "**" if pv < 0.05 else "*" if pv < 0.10 else ""
            print(f"    {nm:8s} {b:>8.4f}  t={t:>6.2f}  p={pv:.3f} {star}")
            out.append({"spec": title, "dep": lbl, "term": nm,
                        "coef": round(b, 5), "t": round(t, 3), "p": round(pv, 4)})
    return out


def run() -> int:
    rows = load_panel()
    if len(rows) < 100:
        print(f"패널 부족({len(rows)}행) — 먼저 `python -m databook events` 실행")
        return 1
    codes = sorted(c[3:] for c in rows[0] if c.startswith("ev_"))
    n_ev = sum(1 for r in rows if int(r.get("n_events", 0)) > 0)
    print(f"거래일 {len(rows):,}일 ({rows[0]['date']} ~ {rows[-1]['date']}) · "
          f"이벤트가 붙은 날 {n_ev:,}일 · 이벤트 {len(codes)}종")
    print("통제: 요일 더미(금요일 기준) · 전일 |수익률|")

    recs: list[dict[str, Any]] = []
    X, names, ys = build(rows, codes, absolute=False)
    recs += _report("A. 방향 (수익률 부호 그대로)", X, names, ys, codes)
    X, names, ys = build(rows, codes, absolute=True)
    recs += _report("B. 변동성 (|수익률|)", X, names, ys, codes)

    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / "regression.csv"
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["spec", "dep", "term", "coef", "t", "p"])
        w.writeheader()
        w.writerows(recs)
    print(f"\n  → {p}")
    print("\n⚠ 이벤트 더미는 '발표가 있었다'만 나타낸다 — **서프라이즈 크기가 아니다.**")
    print("⚠ 같은 날 여러 지표가 함께 발표되므로 더미끼리 상관된다. 개별 계수의 해석은 조심할 것.")
    return 0
