"""동태적 NMF — 정적 토픽모형이 "시대"를 잡는 문제의 해법 시도.

`topics` 모듈의 재현 실패 진단: FOMC 성명서는 **어휘가 시대별로 통째로 교체**되는 코퍼스라
정적 TF-IDF+NMF가 주제가 아니라 레짐을 잡았다(QE기 → 정상화기 → 긴축기).

**Greene·Cross(2016) 방식**으로 우회한다.

1. 코퍼스를 **시간 창(window)** 으로 나눈다
2. **창 안에서** NMF를 돌린다 — 창 내부에서는 어휘가 안정적이라 진짜 주제가 잡힌다
3. 모든 창의 토픽-단어 벡터를 **쌓아서** 다시 NMF를 돌린다
4. 2차 NMF의 토픽 = **여러 시대에 걸쳐 반복되는 주제**(dynamic topic)

핵심 직관: 2010년의 `asset purchases`와 2023년의 `balance sheet`는 어휘가 달라 1차에서는
다른 창의 다른 토픽으로 잡히지만, **둘 다 "대차대조표 정책" 창-토픽**이므로 2차에서 묶일 수 있다.

⚠ 그래도 어휘가 **완전히** 교체되면 2차에서도 안 묶인다. 이 방법의 한계다.
"""
from __future__ import annotations

import csv
import math
from typing import Any

import numpy as np

from .core import OUTPUT_DIR
from .topics import (OUT_DIR, build_tfidf, curve_factors, load_corpus, nmf,
                     regress_topics, umass_coherence)

DYN_DIR = OUTPUT_DIR / "topics"


def windows(dates: list[str], n_win: int) -> list[list[int]]:
    """문서를 시간 순으로 n_win개 창에 균등 분할."""
    n = len(dates)
    size = math.ceil(n / n_win)
    return [list(range(i, min(i + size, n))) for i in range(0, n, size)]


def project(X: np.ndarray, H: np.ndarray, iters: int = 300) -> np.ndarray:
    """H를 고정하고 W만 갱신 — 문서를 주어진 토픽 공간에 사영한다."""
    rng = np.random.default_rng(0)
    W = np.abs(rng.normal(0, 1, (X.shape[0], H.shape[0]))) * 0.01 + 1e-6
    eps = 1e-10
    HHt = H @ H.T
    XHt = X @ H.T
    for _ in range(iters):
        W *= XHt / (W @ HHt + eps)
    return W


def run(n_win: int = 5, k_win: int = 4, k_dyn: int = 4,
        since_year: int = 0, seed: int = 0, topn: int = 12, use_ns: bool = False) -> int:
    dates, docs = load_corpus(since_year)
    if len(docs) < 40:
        print(f"코퍼스 부족({len(docs)}건) — `python -m databook fedtext` 먼저")
        return 1
    X, vocab = build_tfidf(docs)
    tag = f" · {since_year}년 이후" if since_year else ""
    print(f"문서 {len(docs)}건 · 어휘 {len(vocab):,}개 ({dates[0]} ~ {dates[-1]}){tag}")
    print(f"창 {n_win}개 × 창내 토픽 {k_win}개 → 동태적 토픽 {k_dyn}개")

    # 1~2단계: 창별 NMF
    wins = windows(dates, n_win)
    stack, origin = [], []
    print("\n창별 토픽 추출")
    for wi, idx in enumerate(wins):
        if len(idx) < k_win + 2:
            print(f"  W{wi+1}: 문서 {len(idx)}건 — 너무 적어 생략")
            continue
        Xw = X[idx]
        kw = min(k_win, len(idx) - 1)
        _, Hw = nmf(Xw, kw, seed=seed)
        for t in range(kw):
            v = Hw[t]
            nrm = np.linalg.norm(v)
            if nrm > 0:
                stack.append(v / nrm)
                origin.append(wi)
        print(f"  W{wi+1}: {dates[idx[0]][:4]}~{dates[idx[-1]][:4]}  문서 {len(idx):3d}  토픽 {kw}")

    if len(stack) < k_dyn + 1:
        print("창-토픽이 부족하다")
        return 1
    B = np.vstack(stack)

    # 3~4단계: 창-토픽 행렬에 2차 NMF
    Wd, Hd = nmf(B, k_dyn, seed=seed)
    docs_bin = (X > 0).astype(np.float64)
    coh = umass_coherence(Hd, docs_bin, vocab)
    print(f"\n동태적 토픽 {k_dyn}개 · UMass 일관성 {coh:.4f}")

    print("\n동태적 토픽별 상위 단어")
    for t in range(k_dyn):
        top = np.argsort(Hd[t])[::-1][:topn]
        print(f"  D{t+1}: {' · '.join(vocab[i] for i in top)}")

    # 각 동태적 토픽이 어느 창에서 나왔는지 — 시대에 갇혔는지 확인하는 진단
    print("\n동태적 토픽 × 창 분포 (창-토픽 가중 합, 행 정규화)")
    dist = np.zeros((k_dyn, n_win))
    for r, wi in enumerate(origin):
        dist[:, wi] += Wd[r]
    dist = dist / np.where(dist.sum(axis=1, keepdims=True) == 0, 1, dist.sum(axis=1, keepdims=True))
    hdr = "  " + "".join(f"   W{w+1}" for w in range(n_win))
    print(hdr)
    spread = []
    for t in range(k_dyn):
        row = "".join(f"{dist[t, w]:6.2f}" for w in range(n_win))
        # 엔트로피로 '시대 편중'을 잰다 (1=고르게 분포, 0=한 창에 집중)
        p_ = dist[t][dist[t] > 0]
        ent = float(-(p_ * np.log(p_)).sum() / math.log(n_win)) if len(p_) > 1 else 0.0
        spread.append(ent)
        print(f"  D{t+1}{row}   분산도 {ent:.2f}")
    print(f"\n  평균 분산도 {np.mean(spread):.2f}  (1에 가까울수록 여러 시대에 걸친 진짜 주제)")

    # 문서를 동태적 토픽 공간에 사영
    Wdoc = project(X, Hd)
    s = Wdoc.sum(axis=1, keepdims=True)
    Wn = Wdoc / np.where(s == 0, 1, s)

    DYN_DIR.mkdir(parents=True, exist_ok=True)
    with (DYN_DIR / "dyn_doc_topics.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date"] + [f"D{t+1}" for t in range(k_dyn)])
        for i, d in enumerate(dates):
            w.writerow([f"{d[:4]}-{d[4:6]}-{d[6:]}"] + [round(float(x), 5) for x in Wn[i]])
    with (DYN_DIR / "dyn_topic_terms.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["topic", "rank", "term", "weight"])
        for t in range(k_dyn):
            for r, i in enumerate(np.argsort(Hd[t])[::-1][:30], 1):
                w.writerow([f"D{t+1}", r, vocab[i], round(float(Hd[t, i]), 6)])

    if use_ns:
        from .nelsonsiegel import curve_factors_ns
        cf = curve_factors_ns()
        print("\n곡선 요인: Nelson-Siegel 3요인")
    else:
        cf = curve_factors()
    if cf:
        regress_topics(dates, Wn, cf)
    print(f"\n  → {DYN_DIR}")
    print("\n⚠ 창 내부에서도 어휘가 완전히 교체되면 2차 NMF도 시대를 잡는다 — 위 '분산도'로 확인할 것.")
    return 0
