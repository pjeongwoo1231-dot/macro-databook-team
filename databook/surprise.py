"""서프라이즈 기반 이벤트 회귀 — "올랐나 내렸나"를 재는 시도.

`eventreg`는 이벤트 **더미**만 써서 "발표일에 변동성이 커진다"까지만 답했다.
방향을 재려면 **예상 대비 차이(서프라이즈)** 가 필요한데 무료 컨센서스가 없다.

**대안: 금리 기반 서프라이즈**
발표 직후 **미 2년물 금리 변동(ΔDGS2)** 을 서프라이즈의 대용으로 쓴다.
단기 금리는 데이터에 가장 민감하게 반응하고, 통화정책 서프라이즈 문헌의 표준 접근이다
(Kuttner 2001은 연방기금선물, 여기서는 무료로 얻을 수 있는 2년물).

**해석**
- ΔDGS2 > 0 = 예상보다 강한 지표(매파적 재평가)
- ΔDGS2 < 0 = 예상보다 약한 지표(비둘기적 재평가)

**왜 순환이 아닌가**: 서프라이즈는 **미국 시장**에서, 종속변수는 **다음 날 한국 시장**에서 온다.
같은 자산의 같은 시점을 양쪽에 쓰지 않는다.

⚠ 한계 — ΔDGS2에는 그날의 **다른 뉴스**도 섞인다. 순수한 지표 서프라이즈가 아니다.
⚠ **미 주식(ES=F) 야간 수익률을 통제하면** "미국 주가 움직임을 넘어선 반응"을 묻는 다른 질문이 된다.
   두 사양을 모두 보고한다.
"""
from __future__ import annotations

import csv
from datetime import datetime
from typing import Any

import numpy as np

from .core import OUTPUT_DIR
from .topics import ols

EV_DIR = OUTPUT_DIR / "events"
HIST = OUTPUT_DIR / "history"


def _series(name: str) -> dict[str, float]:
    p = HIST / f"{name}.csv"
    if not p.exists():
        return {}
    out: dict[str, float] = {}
    with p.open(encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            try:
                out[r["date"]] = float(r["value"])
            except (TypeError, ValueError):
                continue
    return out


def _diff(s: dict[str, float]) -> dict[str, float]:
    ks = sorted(s)
    return {ks[i]: s[ks[i]] - s[ks[i - 1]] for i in range(1, len(ks))}


def _logret(s: dict[str, float]) -> dict[str, float]:
    ks = sorted(s)
    out = {}
    for i in range(1, len(ks)):
        a, b = s[ks[i - 1]], s[ks[i]]
        if a > 0 and b > 0:
            out[ks[i]] = float(np.log(b / a) * 100)
    return out


def build_rows() -> tuple[list[dict[str, Any]], list[str]]:
    cal = EV_DIR / "calendar.csv"
    pan = EV_DIR / "event_panel.csv"
    if not cal.exists() or not pan.exists():
        return [], []

    # 반응일 → 코스피 갭/장중
    kospi: dict[str, dict[str, float]] = {}
    with pan.open(encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if r.get("suspect") == "1":
                continue
            try:
                kospi[r["date"]] = {"gap": float(r["gap_pct"]),
                                    "intra": float(r["intraday_pct"]),
                                    "close": float(r["close_to_close_pct"])}
            except (TypeError, ValueError):
                continue

    # 발표일 → 이벤트 코드들, 반응일
    rel: dict[str, dict[str, Any]] = {}
    with cal.open(encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            rd, code, react = r["release_date"], r["event_code"], r["reaction_date"]
            if not react:
                continue
            rel.setdefault(rd, {"react": react, "codes": set()})["codes"].add(code)

    d2 = _diff(_series("DGS2"))          # bp 아님 — %p 단위. 100 곱해 bp로
    es = _logret(_series("ES_F"))        # 미 주가 선물 로그수익률(%)
    rows: list[dict[str, Any]] = []
    for rd, v in sorted(rel.items()):
        react = v["react"]
        if rd not in d2 or react not in kospi:
            continue
        rows.append({
            "release": rd, "react": react,
            "surprise_bp": d2[rd] * 100,
            "us_eq": es.get(rd, 0.0),
            "has_es": rd in es,
            "codes": v["codes"],
            **kospi[react],
        })
    codes = sorted({c for r in rows for c in r["codes"]})
    return rows, codes


def _design(rows: list[dict[str, Any]], with_eq: bool) -> tuple[np.ndarray, list[str]]:
    n = len(rows)
    cols = [np.ones(n), np.array([r["surprise_bp"] for r in rows])]
    names = ["const", "surprise"]
    if with_eq:
        cols.append(np.array([r["us_eq"] for r in rows]))
        names.append("US_eq")
    for wd in range(4):
        cols.append(np.array([1.0 if datetime.strptime(r["react"], "%Y-%m-%d").weekday() == wd
                              else 0.0 for r in rows]))
        names.append(["Mon", "Tue", "Wed", "Thu"][wd])
    return np.column_stack(cols), names


def run() -> int:
    rows, codes = build_rows()
    if len(rows) < 100:
        print(f"표본 부족({len(rows)}건) — `events`·`history` 먼저 실행")
        return 1
    rows = [r for r in rows if r["has_es"]]
    print(f"발표일 {len(rows):,}건 · 이벤트 {len(codes)}종 "
          f"({rows[0]['release']} ~ {rows[-1]['release']})")
    s = np.array([r["surprise_bp"] for r in rows])
    print(f"서프라이즈(ΔDGS2) 평균 {s.mean():+.2f}bp · 표준편차 {s.std():.2f}bp · "
          f"|최대| {np.abs(s).max():.0f}bp")

    recs = []
    for with_eq in (False, True):
        tag = "B. 미 주가 통제 후" if with_eq else "A. 서프라이즈만"
        X, names = _design(rows, with_eq)
        print(f"\n{'='*62}\n{tag}\n{'='*62}")
        for dep in ("gap", "intra", "close"):
            y = np.array([r[dep] for r in rows])
            res = ols(y, X, names)
            print(f"\n[{dep}]")
            for nm, b, t, pv in res:
                if nm in ("Mon", "Tue", "Wed", "Thu"):
                    continue
                star = "***" if pv < 0.01 else "**" if pv < 0.05 else "*" if pv < 0.10 else ""
                print(f"    {nm:9s} {b:>9.4f}  t={t:>6.2f}  p={pv:.3f} {star}")
                recs.append({"spec": tag, "dep": dep, "term": nm,
                             "coef": round(b, 6), "t": round(t, 3), "p": round(pv, 4)})

    # 이벤트별 서프라이즈 민감도 (갭 종속)
    print(f"\n{'='*62}\nC. 이벤트별 서프라이즈 민감도 (종속=갭, 미 주가 통제)\n{'='*62}")
    for c in codes:
        sub = [r for r in rows if c in r["codes"]]
        if len(sub) < 40:
            print(f"  {c:8s} 표본 {len(sub)}건 — 생략")
            continue
        X, names = _design(sub, True)
        y = np.array([r["gap"] for r in sub])
        res = ols(y, X, names)
        b, t, pv = next((x[1], x[2], x[3]) for x in res if x[0] == "surprise")
        star = "***" if pv < 0.01 else "**" if pv < 0.05 else "*" if pv < 0.10 else ""
        print(f"  {c:8s} n={len(sub):3d}  β={b:>8.4f}  t={t:>6.2f}  p={pv:.3f} {star}")
        recs.append({"spec": "C. 이벤트별", "dep": "gap", "term": c,
                     "coef": round(b, 6), "t": round(t, 3), "p": round(pv, 4)})

    p = EV_DIR / "surprise_regression.csv"
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["spec", "dep", "term", "coef", "t", "p"])
        w.writeheader()
        w.writerows(recs)
    print(f"\n  → {p}")
    print("\n⚠ ΔDGS2에는 그날의 다른 뉴스도 섞인다 — 순수한 지표 서프라이즈가 아니다.")
    print("⚠ B는 '미 주가 움직임을 넘어선 반응'을 묻는 다른 질문이다. A와 함께 읽을 것.")
    return 0
