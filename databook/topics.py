"""FOMC 성명서 토픽 모델링 — NMF + 수익률곡선 반응.

Crayton(2018)의 방법론을 재현한다. 그 논문은 FOMC 성명서를 NMF로 토픽 분해한 뒤
토픽 비중의 변화가 **수익률곡선의 곡률(curvature)** 변동을 유의하게 설명한다고 보고했다
(수준·기울기에는 유의한 영향 없음).

의존성을 늘리지 않으려고 **TF-IDF와 NMF를 numpy로 직접 구현**했다.
scikit-learn을 요구하지 않는다 — 이 도구는 공개 배포본이다.

NMF는 Lee·Seung 곱셈 갱신(Frobenius). 초기값은 고정 시드라 **재현 가능**하다.
LDA와 달리 결과가 실행마다 달라지지 않는 것이 NMF를 쓰는 이유 중 하나다.

토픽 수 k는 **UMass 일관성(coherence)** 으로 자동 선택한다.
⚠ 단 "자동이라 자의성이 없다"는 말은 과장이다 — **일관성 측정치 선택 자체가 자의적**이다.
"""
from __future__ import annotations

import csv
import math
import re
from pathlib import Path
from typing import Any

import numpy as np

from .core import OUTPUT_DIR

TEXT_DIR = OUTPUT_DIR / "fedtext" / "statements"
OUT_DIR = OUTPUT_DIR / "topics"
HIST_DIR = OUTPUT_DIR / "history"

# 성명서에 상시 등장해 토픽 구분에 기여하지 못하는 어휘 + 표준 불용어
STOP = set("""a an the and or but if while of to in on at by for with from as is are was were be been
being do does did have has had not no nor so than then there here this that these those it its it's
we our us they their them he she his her which who whom what when where why how all any both each few
more most other some such only own same too very can will just should now up down out off over under
again further once about above below between into through during before after
committee federal reserve board governors bank president vote voting voted members member meeting
mr chairman vice today statement release percent point points inflation rate rates policy
""".split())

TOKEN_RE = re.compile(r"[a-z]{3,}")


def load_corpus(since_year: int = 0) -> tuple[list[str], list[list[str]]]:
    dates, docs = [], []
    for f in sorted(TEXT_DIR.glob("*.txt")):
        if since_year and int(f.stem[:4]) < since_year:
            continue
        txt = f.read_text(encoding="utf-8").lower()
        toks = [t for t in TOKEN_RE.findall(txt) if t not in STOP]
        if len(toks) < 40:
            continue
        dates.append(f.stem)
        docs.append(toks)
    return dates, docs


def build_tfidf(docs: list[list[str]], min_df: int = 5, max_df_ratio: float = 0.9
                ) -> tuple[np.ndarray, list[str]]:
    n = len(docs)
    df: dict[str, int] = {}
    for d in docs:
        for w in set(d):
            df[w] = df.get(w, 0) + 1
    vocab = sorted(w for w, c in df.items() if c >= min_df and c <= n * max_df_ratio)
    idx = {w: i for i, w in enumerate(vocab)}
    X = np.zeros((n, len(vocab)), dtype=np.float64)
    for i, d in enumerate(docs):
        for w in d:
            j = idx.get(w)
            if j is not None:
                X[i, j] += 1.0
    # 서브선형 TF × 스무딩 IDF
    tf = np.where(X > 0, 1.0 + np.log(np.maximum(X, 1e-12)), 0.0)
    dfv = np.array([df[w] for w in vocab], dtype=np.float64)
    idf = np.log((1.0 + n) / (1.0 + dfv)) + 1.0
    M = tf * idf
    norms = np.linalg.norm(M, axis=1, keepdims=True)
    return M / np.where(norms == 0, 1.0, norms), vocab


def nmf(X: np.ndarray, k: int, iters: int = 400, seed: int = 0
        ) -> tuple[np.ndarray, np.ndarray]:
    """Lee·Seung 곱셈 갱신. X ≈ W @ H, 전부 비음수."""
    rng = np.random.default_rng(seed)
    n, m = X.shape
    scale = math.sqrt(max(X.mean(), 1e-12) / k)
    W = np.abs(rng.normal(0, 1, (n, k))) * scale + 1e-6
    H = np.abs(rng.normal(0, 1, (k, m))) * scale + 1e-6
    eps = 1e-10
    for _ in range(iters):
        H *= (W.T @ X) / (W.T @ W @ H + eps)
        W *= (X @ H.T) / (W @ H @ H.T + eps)
    return W, H


def umass_coherence(H: np.ndarray, docs_bin: np.ndarray, vocab: list[str],
                    topn: int = 10) -> float:
    """UMass: 토픽 상위어들의 문서 공출현 로그확률 평균. 값이 클수록(0에 가까울수록) 일관적."""
    eps = 1.0
    scores = []
    for t in range(H.shape[0]):
        top = np.argsort(H[t])[::-1][:topn]
        s = []
        for a in range(1, len(top)):
            for b in range(a):
                wi, wj = top[a], top[b]
                d_j = docs_bin[:, wj].sum()
                d_ij = (docs_bin[:, wi] * docs_bin[:, wj]).sum()
                if d_j > 0:
                    s.append(math.log((d_ij + eps) / d_j))
        if s:
            scores.append(sum(s) / len(s))
    return sum(scores) / len(scores) if scores else float("-inf")


def _read_series(name: str) -> dict[str, float]:
    p = HIST_DIR / f"{name}.csv"
    if not p.exists():
        return {}
    out = {}
    with p.open(encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            try:
                out[r["date"]] = float(r["value"])
            except (TypeError, ValueError):
                continue
    return out


def curve_factors() -> dict[str, dict[str, float]]:
    """레벨·기울기·곡률 대용. Diebold-Li 추정 대신 표준 프록시를 쓴다.

    level = 30Y · slope = 30Y − 2Y · curvature = 2×10Y − 2Y − 30Y (버터플라이)
    """
    d2, d10, d30 = _read_series("DGS2"), _read_series("DGS10"), _read_series("DGS30")
    out: dict[str, dict[str, float]] = {}
    for d in set(d2) & set(d10) & set(d30):
        out[d] = {"level": d30[d], "slope": d30[d] - d2[d],
                  "curvature": 2 * d10[d] - d2[d] - d30[d]}
    return out


def run(kmin: int = 2, kmax: int = 12, topn: int = 12, seed: int = 0,
        k_fixed: int | None = None, since_year: int = 0, use_ns: bool = False) -> int:
    dates, docs = load_corpus(since_year)
    if not docs:
        print(f"코퍼스 없음 — 먼저 `python -m databook fedtext` 실행 ({TEXT_DIR})")
        return 1
    X, vocab = build_tfidf(docs)
    tag = f" · {since_year}년 이후" if since_year else ""
    print(f"문서 {len(docs)}건 · 어휘 {len(vocab):,}개  ({dates[0]} ~ {dates[-1]}){tag}")

    docs_bin = (X > 0).astype(np.float64)
    if k_fixed:
        W, H = nmf(X, k_fixed, seed=seed)
        best_k = k_fixed
        print(f"\n토픽 수 고정: k = {best_k} "
              f"(일관성 {umass_coherence(H, docs_bin, vocab):.4f})")
    else:
        print("\n토픽 수 선택 (UMass 일관성, 클수록 좋음)")
        best_k, best_c, cache = kmin, float("-inf"), {}
        for k in range(kmin, kmax + 1):
            W_, H_ = nmf(X, k, seed=seed)
            c = umass_coherence(H_, docs_bin, vocab)
            cache[k] = (W_, H_, c)
            mark = ""
            if c > best_c:
                best_k, best_c, mark = k, c, "  ←"
            print(f"  k={k:2d}  coherence {c:8.4f}{mark}")
        W, H, _ = cache[best_k]
        print(f"\n선택된 k = {best_k}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print("\n토픽별 상위 단어")
    topic_words = []
    for t in range(best_k):
        top = np.argsort(H[t])[::-1][:topn]
        words = [vocab[i] for i in top]
        topic_words.append(words)
        print(f"  T{t+1}: {' · '.join(words)}")

    with (OUT_DIR / "topic_terms.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["topic", "rank", "term", "weight"])
        for t in range(best_k):
            for r, i in enumerate(np.argsort(H[t])[::-1][:30], 1):
                w.writerow([f"T{t+1}", r, vocab[i], round(float(H[t, i]), 6)])

    Wn = W / np.where(W.sum(axis=1, keepdims=True) == 0, 1, W.sum(axis=1, keepdims=True))
    with (OUT_DIR / "doc_topics.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date"] + [f"T{t+1}" for t in range(best_k)])
        for i, d in enumerate(dates):
            w.writerow([f"{d[:4]}-{d[4:6]}-{d[6:]}"] + [round(float(x), 5) for x in Wn[i]])

    # 수익률곡선 반응 — Crayton과 같은 설계: 종속변수는 |Δ요인|
    if use_ns:
        from .nelsonsiegel import curve_factors_ns
        cf = curve_factors_ns()
        print("\n곡선 요인: Nelson-Siegel 3요인 (Diebold-Li, λ=0.0609)")
    else:
        cf = curve_factors()
        print("\n곡선 요인: 버터플라이 프록시")
    if cf:
        days = sorted(cf)
        rows = []
        for i, d in enumerate(dates):
            iso = f"{d[:4]}-{d[4:6]}-{d[6:]}"
            j = None
            for x in days:
                if x >= iso:
                    j = days.index(x)
                    break
            if j is None or j == 0:
                continue
            cur, prev = cf[days[j]], cf[days[j - 1]]
            rows.append({"date": iso, "curve_date": days[j],
                         **{f"abs_d_{k}": abs(cur[k] - prev[k]) for k in ("level", "slope", "curvature")},
                         **{f"T{t+1}": float(Wn[i, t]) for t in range(best_k)}})
        if rows:
            with (OUT_DIR / "curve_response.csv").open("w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(rows[0]))
                w.writeheader()
                w.writerows(rows)
            allday = {}
            for i in range(1, len(days)):
                c0, c1 = cf[days[i - 1]], cf[days[i]]
                for k in ("level", "slope", "curvature"):
                    allday.setdefault(k, []).append(abs(c1[k] - c0[k]))
            print(f"\n성명서 발표일 vs 전체 거래일 — |Δ| 평균 (bp)")
            print(f"{'요인':12s}{'발표일':>10s}{'전체':>10s}{'비율':>8s}")
            for k in ("level", "slope", "curvature"):
                a = float(np.mean([r[f"abs_d_{k}"] for r in rows])) * 100
                b = float(np.mean(allday[k])) * 100
                print(f"  {k:10s}{a:9.2f}{b:10.2f}{a/b:8.2f}x")
            print(f"\n  발표일 {len(rows)}건 · 전체 거래일 {len(days)-1}건")
    if cf:
        regress_topics(dates, Wn, cf)

    print(f"\n  → {OUT_DIR}")
    print("\n⚠ |Δ|는 변동성이지 방향이 아니다. '영향 있다'는 '변동성이 커졌다'는 뜻일 뿐이다.")
    print("⚠ 유니그램만 쓰므로 'not accommodative' 같은 부정어·연어가 깨진다.")
    return 0

def ols(y: np.ndarray, X: np.ndarray, names: list[str]) -> list[tuple[str, float, float, float]]:
    """절편 포함 OLS. (이름, 계수, t, p) 목록. p는 정규근사 양측."""
    n, k = X.shape
    XtX_inv = np.linalg.pinv(X.T @ X)
    b = XtX_inv @ X.T @ y
    resid = y - X @ b
    dof = max(n - k, 1)
    s2 = float(resid @ resid) / dof
    se = np.sqrt(np.maximum(np.diag(s2 * XtX_inv), 1e-300))
    out = []
    for i, nm in enumerate(names):
        t = float(b[i] / se[i])
        pv = 2 * (1 - 0.5 * (1 + math.erf(abs(t) / math.sqrt(2))))
        out.append((nm, float(b[i]), t, pv))
    return out


def regress_topics(dates: list[str], Wn: np.ndarray, cf: dict[str, dict[str, float]]) -> None:
    """|Δ요인| ~ 토픽 비중 변화 + 통제(VIX·기간스프레드·신용스프레드).

    ⚠ 토픽 비중은 행 합이 1이라 **모든 토픽을 넣으면 완전공선성**이 된다.
    k개 중 **k−1개만** 쓴다(마지막 토픽이 기준 범주).
    Crayton은 이 문제를 명시하지 않았는데, 정규화 여부에 따라 달라진다.
    """
    vix = _read_series("VIXCLS")
    term = _read_series("T10Y2Y")
    baa = _read_series("BAA10Y")          # ICE OAS는 2023년부터라 장기 대용
    days = sorted(cf)
    k = Wn.shape[1]

    rows = []
    prev_w = None
    for i, d in enumerate(dates):
        iso = f"{d[:4]}-{d[4:6]}-{d[6:]}"
        j = next((n for n, x in enumerate(days) if x >= iso), None)
        if j is None or j == 0:
            prev_w = Wn[i]
            continue
        cd, pd_ = days[j], days[j - 1]
        if not all(cd in s for s in (vix, term, baa)):
            prev_w = Wn[i]
            continue
        if prev_w is None:
            prev_w = Wn[i]
            continue
        dw = Wn[i] - prev_w
        rows.append({
            "abs": {f: abs(cf[cd][f] - cf[pd_][f]) * 100 for f in ("level", "slope", "curvature")},
            "dw": dw, "absdw": np.abs(dw),
            "vix": vix[cd], "term": term[cd], "baa": baa[cd],
        })
        prev_w = Wn[i]

    if len(rows) < 30:
        print(f"\n회귀 표본 부족({len(rows)}건) — 통제변수 결측 확인 필요")
        return

    names = ["const"] + [f"dT{t+1}" for t in range(k - 1)] + ["|dT1|", "VIX", "TermSpr", "BaaSpr"]
    X = np.column_stack([
        np.ones(len(rows)),
        *[np.array([r["dw"][t] for r in rows]) for t in range(k - 1)],
        np.array([r["absdw"][0] for r in rows]),
        np.array([r["vix"] for r in rows]),
        np.array([r["term"] for r in rows]),
        np.array([r["baa"] for r in rows]),
    ])
    print(f"\n토픽 변화 → 곡선 반응 회귀  (n={len(rows)}, 종속변수 |Δ요인| bp)")
    print(f"  통제: VIX · 기간스프레드(T10Y2Y) · 신용스프레드(Baa−10Y)")
    print(f"  ⚠ 토픽 비중 합이 1이라 dT{k}는 제외(기준 범주)")
    for f in ("level", "slope", "curvature"):
        y = np.array([r["abs"][f] for r in rows])
        res = ols(y, X, names)
        sig = [x for x in res if x[0] != "const" and x[3] < 0.10]
        print(f"\n  [{f}]  유의(p<0.10) 항: {len(sig)}")
        for nm, b, t, pv in res:
            star = "***" if pv < 0.01 else "**" if pv < 0.05 else "*" if pv < 0.10 else ""
            print(f"    {nm:9s} {b:>9.3f}  t={t:>6.2f}  p={pv:.3f} {star}")
