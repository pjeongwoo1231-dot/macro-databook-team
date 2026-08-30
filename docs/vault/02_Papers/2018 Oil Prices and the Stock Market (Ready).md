---
title: "Oil Prices and the Stock Market"
type: paper
journal: Review of Finance (2018). 볼트 보유본은 2013-02-04 초고
date: 2018
author: Robert C. Ready (Simon School, University of Rochester)
url: https://publications.dyson.cornell.edu/research/doc/oil_and_stock_market.pdf
tags: [type/paper, method/shock-decomposition, domain/commodities]
concepts: [유가 공급충격, 유가 수요충격, 오일 베타, 직교화 식별, 소비지출 제약]
source_file: 로컬 사본 — 2013-02-04 draft PDF (공개)
status: done
verification: partial
reliability: academic
text_basis: human-fulltext
verified: "○ 초록·서론 전문 직접 판독(2026-08-14). ⚠ **다만 판독본은 2013-02-04 초고**이고 출판본은 Review of Finance(2018)다. 아래 수치는 초고 기준 — 출판본에서 달라졌을 수 있으므로 인용 시 출판본 확인"
promoted_from: "[[L49 Oil Prices and the Stock Market]]"
related: ["[[2009 The Impact of Oil Price Shocks on the U.S. Stock Market (Kilian & Park)]]", "[[WTI (국제유가)]]", "[[KOSPI]]", "[[RegimeView 1.0 (2026-08-09)]]"]
---

# 유가와 주가가 무관해 보이는 건 두 충격이 상쇄되기 때문이다 (Ready)

> Review of Finance (2018). **볼트 보유본은 2013-02-04 초고 PDF**(공개).
> ⚠ 아래 수치는 **초고 기준**이다. 출판본에서 표본·수치가 바뀌었을 수 있으니
> 인용할 때는 Review of Finance 게재본을 확인할 것.

## 왜 중요한가 — 우리 문제와 직결

DataBook은 `WTI`·`유가 Brent`·`미 원유재고`·`미 원유생산`을 수집하고,
[[2024-2026-Comparative-Mechanism-Map]]은 1단계를 **에너지 충격**으로 잡는다.
그런데 **"유가가 오르면 주가가 어떻게 되나"** 라는 기본 질문에 볼트가 답을 갖고 있지 않았다.

이 논문의 출발점이 정확히 그 퍼즐이다 — 저자의 표현으로
**"Where is the Oil Price Beta?"** 1983~2012년 월간 미국 주가수익률을 유가 변화에 단순 회귀하면
**사실상 관계가 없다.**

## 방법 — 유가 변화를 둘로 가른다

| 구분 | 정의 |
|---|---|
| **공급충격** | 유가 변화 중 **산유기업 지수의 동시 수익률에 직교하는** 부분 |
| **수요충격** | 나머지(= 산유기업 수익률로 설명되는 예측값) |

직관: 수요가 늘어 유가가 오르면 **산유기업 주가도 같이 오른다.**
공급이 막혀 유가가 오르면 산유기업 주가는 그만큼 반응하지 않는다.
→ 산유기업 수익률에 **직교하는 부분**을 공급충격으로 본다.

전방편의(look-ahead bias)를 피하려 **롤링 회귀**로 구성한다.
구성상 두 계열이 유가 변동 전부를 설명하며, **공급충격이 전체 변동의 약 80%**를 차지한다.

## 원문에서 확인한 결과 (초고 기준)

**1. 무관해 보이는 건 상쇄 때문이다.** 나눠 보면 둘 다 주가와 강하게 연관된다.

**2. 공급충격은 음(−), 수요충격은 양(+).**
- 공급충격이 미국 총주가 월간 변동의 **약 6%** 설명 (금융위기 제외 시 **10%**)
- 수요충격이 **추가로 38%** 설명

**3. 경로가 예상과 다르다.** 공급충격의 음의 효과가 **석유를 많이 쓰는 산업에 집중되지 않고
소비재 생산기업에서 가장 강하다.** 저자는 이를 **유가 충격이 소비지출 제약을 통해 작동한다**는
증거로 해석한다.

**4. 국제적으로도 성립하며, 효과는 석유 수입국에서 가장 강하다.**

## 한계와 적용 범위

- **저자(명시)**: 식별은 **산유기업 지수 수익률의 직교화**에 의존한다. 산유기업 주가가
  유가 외의 요인(자체 자본구조·규제)에 크게 반응하면 분해가 오염된다
- **사서(추가)**: **판독본이 초고다.** 6%·10%·38%·80%는 2013년 초고 값이다
- **사서(추가)**: 표본이 **1983~2012**다. 셰일 이후 미국이 순수출국에 가까워진 구조 변화와
  2022년 전쟁발 공급충격은 들어 있지 않다. **미국의 "석유 수입국" 지위가 바뀌었다**는 점이
  결과의 외적타당성에 직접 걸린다
- **사서(추가)**: **한국은 대표적 석유 수입국**이다. 이 논문 논리대로면 공급충격의 음의 효과가
  미국보다 강해야 한다 — [[KOSPI]]로 같은 분해를 돌려보는 것이 검증 과제다

## 인과 사슬

유가 상승 → **(a) 공급 요인이면**: 산유기업 주가 미반응 → 소비지출 제약
→ **소비재 기업** 주가 하락 → 총주가 음(−)
→ **(b) 수요 요인이면**: 세계 수요 강세 신호 → 산유기업·총주가 동반 상승 양(+)
→ 둘이 섞이면 **[[WTI (국제유가)]]-주가 상관이 0으로 보인다**

**Comment**: 실무 규칙 하나 — **유가 지표를 단일 변수로 쓰지 말 것.**
DataBook은 WTI·Brent·원유재고·원유생산을 함께 받으므로, **재고·생산 지표로 공급/수요를
가르는 근사**가 가능하다. 그리고 이 논문이 보인 "소비재 기업이 가장 크게 맞는다"는 결과는
[[2018 Really Uncertain Business Cycles (Bloom, Floetotto, Jaimovich, Saporta-Eksten & Terry)]]가
말한 **소비 축의 중요성**과 같은 방향을 가리킨다.

## 관련 개념

- 같은 분해, 다른 방법 — [[2009 The Impact of Oil Price Shocks on the U.S. Stock Market (Kilian & Park)]]
- 유가-거시 원전 — [[1983 Oil and the Macroeconomy Since World War II (Hamilton)]] ·
  [[1996 This Is What Happened to the Oil Price-Macroeconomy Relationship (Hamilton)]]
- 소비 축 — [[2018 Really Uncertain Business Cycles (Bloom, Floetotto, Jaimovich, Saporta-Eksten & Terry)]]
- 지표 — [[WTI (국제유가)]] · [[KOSPI]] · [[2024-2026-Comparative-Mechanism-Map]]

## References

[1]: https://publications.dyson.cornell.edu/research/doc/oil_and_stock_market.pdf "Ready, Oil Prices and the Stock Market (2013 draft; published Review of Finance 2018)"
