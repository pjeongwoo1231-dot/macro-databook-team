"""Diebold-Li(2006) 3요인 추정 — 레벨·기울기·곡률.

`topics`/`dyntopics`의 재현 실패에 남은 마지막 의심: **곡선 요인을 프록시로 썼다**는 점.
버터플라이(2×10Y−2Y−30Y) 대신 **Nelson-Siegel 적재를 고정하고 횡단면 OLS**로 요인을 뽑는다.

Nelson-Siegel:

    y(τ) = β1 + β2·(1−e^(−λτ))/(λτ) + β3·[(1−e^(−λτ))/(λτ) − e^(−λτ)]

- **β1 = 레벨**  (적재 1 — 전 만기 공통)
- **β2 = 기울기** (적재가 단기 1 → 장기 0. **부호 주의**: β2는 −(장기−단기)에 해당)
- **β3 = 곡률**  (적재가 중기에서 최대)

λ는 Diebold-Li를 따라 **0.0609**로 고정한다(만기 단위 = 개월).
이 값에서 곡률 적재가 30개월 부근에서 최대가 된다.

**2단계 추정**: λ 고정 → 매일 횡단면 OLS로 β를 얻는다.
Diebold-Li 원논문의 1단계(상태공간+칼만)는 β에 AR(1)을 부과하는데,
여기서는 **일별 요인 시계열이 목적**이라 2단계로 충분하다(원논문도 두 방식이 유사하다고 보고).

만기 11개(1M~30Y)를 쓴다. **3개만 쓰면 3요인이 정확식별되어 잔차가 0**이 되므로 의미가 없다.
"""
from __future__ import annotations

import csv
from typing import Any

import numpy as np

from .core import OUTPUT_DIR

HIST = OUTPUT_DIR / "history"
OUT = OUTPUT_DIR / "curve"
LAMBDA = 0.0609

# FRED 계열 → 만기(개월)
MATURITIES: dict[str, float] = {
    "DGS1MO": 1, "DGS3MO": 3, "DGS6MO": 6, "DGS1": 12, "DGS2": 24,
    "DGS3": 36, "DGS5": 60, "DGS7": 84, "DGS10": 120, "DGS20": 240, "DGS30": 360,
}


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


def loadings(tau: np.ndarray, lam: float = LAMBDA) -> np.ndarray:
    """[1, 기울기적재, 곡률적재] — (n_tau, 3)."""
    x = lam * tau
    a = (1.0 - np.exp(-x)) / x
    return np.column_stack([np.ones_like(tau), a, a - np.exp(-x)])


def estimate(min_points: int = 7) -> dict[str, dict[str, float]]:
    """일자별 3요인. 만기가 min_points개 미만인 날은 건너뛴다."""
    data = {k: _series(k) for k in MATURITIES}
    have = [k for k, v in data.items() if v]
    if len(have) < min_points:
        return {}
    days = set.intersection(*[set(data[k]) for k in have[:3]]) if have else set()
    days = set()
    for k in have:
        days |= set(data[k])

    out: dict[str, dict[str, float]] = {}
    for d in sorted(days):
        ks = [k for k in have if d in data[k]]
        if len(ks) < min_points:
            continue
        tau = np.array([MATURITIES[k] for k in ks], dtype=float)
        y = np.array([data[k][d] for k in ks], dtype=float)
        Z = loadings(tau)
        beta, *_ = np.linalg.lstsq(Z, y, rcond=None)
        resid = y - Z @ beta
        out[d] = {"level": float(beta[0]), "slope": float(beta[1]),
                  "curvature": float(beta[2]),
                  "rmse": float(np.sqrt((resid ** 2).mean())), "n_tau": len(ks)}
    return out


def curve_factors_ns() -> dict[str, dict[str, float]]:
    """topics 모듈이 쓰는 형식(level/slope/curvature)으로 반환."""
    est = estimate()
    return {d: {"level": v["level"], "slope": v["slope"], "curvature": v["curvature"]}
            for d, v in est.items()}


def run() -> int:
    est = estimate()
    if not est:
        print("커브 데이터 부족 — `python -m databook history` 먼저")
        return 1
    days = sorted(est)
    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / "ns_factors.csv"
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "level", "slope", "curvature", "rmse", "n_tau"])
        for d in days:
            v = est[d]
            w.writerow([d, round(v["level"], 5), round(v["slope"], 5),
                        round(v["curvature"], 5), round(v["rmse"], 5), v["n_tau"]])

    rm = np.array([est[d]["rmse"] for d in days])
    nt = np.array([est[d]["n_tau"] for d in days])
    print(f"Nelson-Siegel 3요인 추정 (λ={LAMBDA}) — {len(days):,}일  {days[0]} ~ {days[-1]}")
    print(f"  만기 수 중앙값 {int(np.median(nt))}개 · 적합 RMSE 평균 {rm.mean()*100:.1f}bp "
          f"(중앙값 {np.median(rm)*100:.1f}bp)")
    for k in ("level", "slope", "curvature"):
        v = np.array([est[d][k] for d in days])
        print(f"  {k:10s} 평균 {v.mean():7.3f} · 표준편차 {v.std():6.3f} "
              f"· 최근값 {est[days[-1]][k]:7.3f}")

    # 프록시와의 상관 — 대체가 정당했는지 사후 점검
    d2, d10, d30 = _series("DGS2"), _series("DGS10"), _series("DGS30")
    common = [d for d in days if d in d2 and d in d10 and d in d30]
    if len(common) > 100:
        prox = {
            "level": np.array([d30[d] for d in common]),
            "slope": np.array([d30[d] - d2[d] for d in common]),
            "curvature": np.array([2 * d10[d] - d2[d] - d30[d] for d in common]),
        }
        print("\n버터플라이 프록시와의 상관 (수준 / 일간 변화)")
        for k in ("level", "slope", "curvature"):
            ns = np.array([est[d][k] for d in common])
            r = float(np.corrcoef(ns, prox[k])[0, 1])
            dn, dp = np.diff(ns), np.diff(prox[k])
            rd = float(np.corrcoef(dn, dp)[0, 1])
            print(f"  {k:10s} 수준 r={r:+.3f}   변화 r={rd:+.3f}")
    print(f"\n  → {p}")
    print("\n⚠ NS의 slope(β2)는 부호가 (단기−장기) 방향이다 — 프록시(장기−단기)와 부호가 반대로 나올 수 있다.")
    return 0
