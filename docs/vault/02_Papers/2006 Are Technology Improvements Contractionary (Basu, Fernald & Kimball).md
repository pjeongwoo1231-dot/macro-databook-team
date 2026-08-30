---
title: "Are Technology Improvements Contractionary?"
type: paper
journal: American Economic Review 96(5) (2006). 볼트 보유본은 NBER WP 10592 (2004-06)
date: 2006
author: Susanto Basu (Boston College), John Fernald (FRBSF), Miles Kimball (Michigan)
url: https://www.nber.org/papers/w10592
tags: [type/paper, method/growth-accounting, domain/productivity]
concepts: [기술충격, 가동률 조정, 단기 수축, 가격경직성, RBC 반증]
status: done
verification: partial
reliability: academic
text_basis: human-fulltext
verified: "○ NBER WP 10592 공개 PDF의 표지·초록 직접 판독(2026-08-14). ⚠ **판독본은 2004년 WP**이고 출판본은 AER 96(5) 2006 — 수치·표현이 달라졌을 수 있어 인용 시 출판본 확인"
promoted_from: "[[L5 Are Technology Improvements Contractionary-]]"
related: ["[[2014 A Quarterly, Utilization-Adjusted Series on Total Factor Productivity (Fernald)]]", "[[1986 Theory Ahead of Business Cycle Measurement (Prescott)]]", "[[총요소생산성 (TFP)]]"]
---

# 기술이 좋아지면 단기적으로 투입이 줄어든다 (Basu, Fernald & Kimball)

> American Economic Review 96(5), 2006. **볼트 보유본은 NBER WP 10592(2004-06)** 공개 PDF.
> ⚠ 아래는 WP판 초록 기준이다. 출판본과 표현이 다를 수 있다.

## 왜 중요한가 — 우리 문제와 직결

**[[2014 A Quarterly, Utilization-Adjusted Series on Total Factor Productivity (Fernald)]]의
가동률 조정이 여기서 나왔다.** DataBook이 받는 `dtfp_util`의 방법론 원전이다.

그리고 볼트의 RBC 계열([[1986 Theory Ahead of Business Cycle Measurement (Prescott)]],
[[1983 Real Business Cycles (Long & Plosser)]], [[1982 Time to Build and Aggregate Fluctuations (Kydland & Prescott)]])에
대한 **정면 반증**이다. 볼트에 RBC는 있는데 그 반증이 없었다.

## 논지

제목이 질문이고 저자들의 답은 초록 첫 단어다 — **"Yes."**

가동률(자본·노동), 비일정 규모수익, 불완전경쟁, 집계효과를 통제한
**총기술변화 측정치**를 만들고 그 충격반응을 본다.

**충격 시점에 기술이 개선되면 투입 사용과 비주거 투자가 급감한다. 산출은 거의 변하지 않는다.**
몇 년의 시차를 두고 투입과 투자가 정상으로 돌아오며 **산출이 크게 상승한다.**

이 패턴은 **표준 1부문 RBC 모형과 양립하지 않는다** — RBC는 기술 개선이 즉시 확장적이고
투입·산출이 곧바로 오른다고 예측한다. 반면 **단순 가격경직성 모형과는 정합적**이다:
기술이 좋아지면 같은 산출을 더 적은 투입으로 만들 수 있는데 가격이 굳어 수요가 안 늘면
**투입을 줄인다.**

## 한계와 적용 범위

- **사서(추가)**: 기술 측정 자체가 **여러 통제(가동률·규모수익·경쟁도·집계)에 의존**한다.
  통제가 틀리면 충격도 틀린다 — 이 논문의 결론은 **측정 방법과 한 몸**이다
- **사서(추가)**: 판독본이 **2004년 WP**다. 출판본(AER 2006)에서 수치·표현이 바뀌었을 수 있다
- **사서(추가)**: "몇 년의 시차"라는 서술만 확인했고 **구체적 시차·크기는 인용하지 않는다**
  (본문 전체는 읽지 않았다)
- **사서(추가)**: 미국 데이터다. 가격경직성 정도가 다른 경제에서는 부호가 달라질 수 있다

## 인과 사슬

기술 개선 → 같은 산출에 필요한 투입 감소
→ (가격이 경직적이라 수요가 즉시 안 늘면) **투입·비주거투자 급감**, 산출 거의 불변
→ 수년 후 가격 조정 → 투입 회복 + **산출 크게 상승**

**Comment**: 두 가지가 우리 쪽에 남는다.

**① 측정의 교훈** — raw TFP는 기술이 아니다. 가동률을 걷어내야 한다.
그 결과가 [[2014 A Quarterly, Utilization-Adjusted Series on Total Factor Productivity (Fernald)]]의
`dtfp_util`이고, 지금 그 값이 **−2.16%**(2026 상반기)다.

**② 해석의 교훈** — 설령 기술이 개선되더라도 **단기에는 투입이 줄어든다.**
따라서 "생산성이 좋아지니 고용이 늘 것"이라는 추론은 이 논문이 지지하지 않는다.
[[RegimeView 1.0 (2026-08-09)]]의 `low-hire`를 **기술 개선의 단기 부작용**으로 읽는
해석 경로가 하나 더 생긴다 — 다만 지금은 `dtfp_util`이 음수라 이 경로가 작동할 조건이 아니다.

## 관련 개념

- 방법의 구현체 — [[2014 A Quarterly, Utilization-Adjusted Series on Total Factor Productivity (Fernald)]]
- 반증 대상(RBC) — [[1986 Theory Ahead of Business Cycle Measurement (Prescott)]] ·
  [[1983 Real Business Cycles (Long & Plosser)]] · [[1982 Time to Build and Aggregate Fluctuations (Kydland & Prescott)]]
- 성장회계 원전 — [[1957 Technical Change and the Aggregate Production Function (Solow)]]
- 지표 — [[총요소생산성 (TFP)]] · [[RegimeView 1.0 (2026-08-09)]]

## References

[1]: https://www.nber.org/papers/w10592 "Basu, Fernald and Kimball (2004), Are Technology Improvements Contractionary?, NBER WP 10592 — published AER 96(5) 2006"
