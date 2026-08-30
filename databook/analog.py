"""과거 유사 국면 탐색 — "그때는 이랬는데 이번엔 무엇이 다른가".

왜 만드나
    「좋은 시황의 규칙」이 요구하는 근거 3축 중 **사례**가 늘 비어 있었다.
    기저율은 "조건 A가 있었던 n번" 하나로 뭉뚱그리는데, 사람이 알고 싶은 것은
    **어느 시점이 지금과 닮았고 그때 무슨 일이 있었나**다.

    다만 볼트 규칙이 못 박아둔 것이 있다 — **배열은 방향을 알려주지 않는다.**
    2026-08-25에 "실질금리 주도 긴축 → 한국 주식 하락"이 기저율(13구간 중앙값 −0.1%)로
    기각됐다. 그래서 이 모듈은 방향을 말하지 않는다. **이웃을 찾아 그때의 결과를 늘어놓고,
    지금이 그들과 어디서 갈라지는지를 숫자로 보여줄 뿐이다.**

방법
    ① 상태 벡터 — 금리 분해·신용·변동성·금융여건·달러를 z점수로
    ② 거리 — 가중 유클리드. 가까운 순으로 이웃을 뽑되 **90일 이내 중복은 하나로**
    ③ 결과 — 각 이웃 이후 +1·+3·+6개월 자산 변화
    ④ 차이 — 지금과 그 이웃이 **가장 크게 갈리는 축**을 명시한다.
       이게 "그때와 이번의 다른 점"이고, 결과를 그대로 옮기면 안 되는 이유다

⚠ 한계 (인용 전에 반드시 함께 읽는다)
    - 이웃이 가깝다는 것은 **관측된 축들만** 가깝다는 뜻이다. 정책 국면·제도·
      전쟁 유무처럼 벡터에 없는 것은 비교되지 않았다.
    - 표본은 2003년 이후(TIPS 계열 시작)라 20여 년뿐이다.
    - 결과는 **그 시점에 그랬다**는 기록이지 예측이 아니다.
"""
from __future__ import annotations

import csv
import datetime as dt
import math
import statistics as st
from pathlib import Path
from typing import Any

from .core import OUTPUT_DIR

# 상태 축: (라벨, 계열, 종류, 가중치)
#   level = 그 시점 수준의 백분위 / chg = 3개월 변화(bp 또는 %)
AXES: list[tuple[str, str, str, float]] = [
    ("실질금리 3개월 변화", "DFII10", "chg", 1.0),
    ("BEI 3개월 변화", "T10YIE", "chg", 1.0),
    ("5y5y 3개월 변화", "T5YIFR", "chg", 1.0),
    ("실질금리 수준", "DFII10", "level", 0.8),
    ("커브 2s10s", "_CURVE", "level", 0.8),
    ("Baa 스프레드 수준", "BAA10Y", "level", 1.0),
    ("VIX 수준", "VIXCLS", "level", 0.8),
    ("금융여건 NFCI", "NFCI", "level", 0.8),
]

# 결과 자산: (라벨, 계열, 표기)
OUTCOMES: list[tuple[str, str, str]] = [
    ("코스피", "KS11", "%"),
    ("금", "GC_F", "%"),
    ("WTI", "DCOILWTICO", "%"),
    ("미 10Y", "DGS10", "bp"),
    ("Baa 스프레드", "BAA10Y", "bp"),
]
HORIZONS = [(30, "1개월"), (91, "3개월"), (182, "6개월")]


def _load(name: str) -> dict[dt.date, float]:
    p = OUTPUT_DIR / "history" / f"{name}.csv"
    out: dict[dt.date, float] = {}
    if not p.exists():
        return out
    with p.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            k = list(r.keys())
            try:
                out[dt.date.fromisoformat(r[k[0]][:10])] = float(r[k[1]])
            except Exception:
                pass
    return out


def _at(s: dict[dt.date, float], d: dt.date):
    ks = [k for k in s if k <= d]
    return s[max(ks)] if ks else None


def _series() -> dict[str, dict[dt.date, float]]:
    S = {n: _load(n) for n in {a[1] for a in AXES} | {o[1] for o in OUTCOMES} if not n.startswith("_")}
    d10, d2 = S.get("DGS10") or _load("DGS10"), _load("DGS2")
    S["DGS10"] = d10
    S["_CURVE"] = {d: d10[d] - d2[d] for d in set(d10) & set(d2)}
    return S


def _state(S, d: dt.date) -> list[float] | None:
    """그 시점의 상태 벡터(원값). 하나라도 없으면 None."""
    v = []
    for _, name, kind, _w in AXES:
        s = S.get(name) or {}
        cur = _at(s, d)
        if cur is None:
            return None
        if kind == "chg":
            prev = _at(s, d - dt.timedelta(days=91))
            if prev is None:
                return None
            v.append((cur - prev) * 100)
        else:
            v.append(cur)
    return v


def find(asof: dt.date, top: int = 6, gap_days: int = 90) -> dict[str, Any]:
    S = _series()
    common = sorted(set.intersection(*(set(S[n]) for _, n, _, _ in AXES if S.get(n))))
    common = [d for d in common if d <= asof]
    if len(common) < 500:
        raise SystemExit("상태 벡터를 만들 계열이 부족합니다 — `python -m databook history`를 먼저 돌리세요.")

    states: dict[dt.date, list[float]] = {}
    for d in common:
        v = _state(S, d)
        if v is not None:
            states[d] = v
    if asof not in states:
        asof = max(states)
    cur = states[asof]

    # z점수 — 축마다 분포가 달라 그대로 빼면 큰 단위가 지배한다
    cols = list(zip(*states.values()))
    mu = [st.mean(c) for c in cols]
    sd = [st.pstdev(c) or 1.0 for c in cols]
    w = [a[3] for a in AXES]

    def dist(v):
        return math.sqrt(sum(wi * ((a - m) / s - (b - m) / s) ** 2
                             for a, b, m, s, wi in zip(v, cur, mu, sd, w)))

    # 최근 1년은 이웃에서 뺀다 — 지금과 겹쳐 "자기 자신"이 뽑힌다
    cands = sorted(((dist(v), d) for d, v in states.items()
                    if d <= asof - dt.timedelta(days=365)), key=lambda x: x[0])
    picked: list[tuple[float, dt.date]] = []
    for dd, d in cands:
        if all(abs((d - p[1]).days) > gap_days for p in picked):
            picked.append((dd, d))
        if len(picked) >= top:
            break

    last = {n: (max(S[n]) if S.get(n) else asof) for _, n, _ in OUTCOMES}
    rows = []
    for dd, d in picked:
        out: dict[str, Any] = {"date": d, "dist": dd}
        for lab, name, unit in OUTCOMES:
            s = S.get(name) or {}
            a = _at(s, d)
            for hz, hlab in HORIZONS:
                tgt = d + dt.timedelta(days=hz)
                b = _at(s, tgt) if tgt <= last[name] else None
                if a is None or b is None or (unit == "%" and not a):
                    out[f"{lab}·{hlab}"] = None
                else:
                    out[f"{lab}·{hlab}"] = (b / a - 1) * 100 if unit == "%" else (b - a) * 100
        # 지금과 가장 크게 갈리는 축
        gaps = sorted((((states[d][k] - mu[k]) / sd[k] - (cur[k] - mu[k]) / sd[k], AXES[k][0],
                        states[d][k], cur[k]) for k in range(len(AXES))),
                      key=lambda x: -abs(x[0]))
        out["gaps"] = gaps[:3]
        rows.append(out)

    stats: dict[str, dict[str, Any]] = {}
    for lab, _n, unit in OUTCOMES:
        for _hz, hlab in HORIZONS:
            vals = [r[f"{lab}·{hlab}"] for r in rows if r.get(f"{lab}·{hlab}") is not None]
            if vals:
                stats[f"{lab}·{hlab}"] = {
                    "n": len(vals), "median": st.median(vals),
                    "neg": sum(1 for v in vals if v < 0),
                    "min": min(vals), "max": max(vals), "unit": unit}
    return {"asof": asof, "cur": dict(zip((a[0] for a in AXES), cur)),
            "rows": rows, "stats": stats, "pool": len(states)}


def cmd_analog(asof: str | None, top: int) -> int:
    a = dt.date.fromisoformat(asof) if asof else dt.date.today()
    r = find(a, top=top)

    print(f"\n유사 국면 탐색  ·  기준 {r['asof']}  ·  후보 {r['pool']:,}일 (2003~)")
    print("=" * 74)
    print("현재 상태")
    for k, v in r["cur"].items():
        print(f"    {k:20} {v:>9.2f}")
    print("\n가장 닮은 국면 — 그 뒤 무슨 일이 있었나")
    print("=" * 74)
    for x in r["rows"]:
        print(f"\n  {x['date']}   거리 {x['dist']:.2f}")
        line = []
        for lab, _n, unit in OUTCOMES:
            cells = []
            for _hz, hlab in HORIZONS:
                v = x.get(f"{lab}·{hlab}")
                cells.append("  —  " if v is None else (f"{v:+6.1f}{'%' if unit=='%' else 'bp'}"))
            line.append(f"    {lab:8} " + " ".join(cells))
        print("\n".join(line))
        print("    이번과 다른 점:")
        for z, name, then, now in x["gaps"]:
            print(f"      {name:20} 그때 {then:>8.2f}  →  지금 {now:>8.2f}   (z차 {z:+.2f})")

    print("\n" + "=" * 74)
    print("이웃들의 결과 요약 (예측이 아니라 기록이다)")
    for lab, _n, unit in OUTCOMES:
        cells = []
        for _hz, hlab in HORIZONS:
            s = r["stats"].get(f"{lab}·{hlab}")
            cells.append("  —  " if not s else
                         f"{s['median']:+6.1f}{'%' if unit=='%' else 'bp'}(음 {s['neg']}/{s['n']})")
        print(f"  {lab:10} " + "  ".join(cells))
    print("\n  ⚠ 이웃이 가깝다는 것은 **관측된 축들만** 가깝다는 뜻이다.")
    print("    정책 국면·제도·전쟁 유무처럼 벡터에 없는 것은 비교되지 않았다.")
    print("    결과는 그 시점의 기록이지 예측이 아니다 — 위 「이번과 다른 점」을 함께 읽는다.")
    return 0
