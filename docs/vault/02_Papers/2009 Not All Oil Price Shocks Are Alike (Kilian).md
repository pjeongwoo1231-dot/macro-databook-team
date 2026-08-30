---
title: "Not All Oil Price Shocks Are Alike: Disentangling Demand and Supply Shocks in the Crude Oil Market"
type: paper
journal: American Economic Review 99(3), 1053–1069 (2009)
date: 2009
author: Lutz Kilian (Michigan / Dallas Fed)
doi: 10.1257/aer.99.3.1053
url: https://www.aeaweb.org/articles?id=10.1257/aer.99.3.1053
tags: [type/paper, method/structural-VAR, domain/commodities]
concepts: [유가충격 분해, 공급충격, 총수요충격, 예비적 수요, 구조 VAR]
status: done
verification: partial
reliability: academic
text_basis: cited-primary
verified: "△ 서지 확정(2026-08-14): AER 99(3) 1053–1069. 본문 유료라 미열람 — **수치 인용 금지**"
promoted_from: "[[L216 Not All Oil Price Shocks Are Alike]]"
related: ["[[2009 The Impact of Oil Price Shocks on the U.S. Stock Market (Kilian & Park)]]", "[[2008 Exogenous Oil Supply Shocks (Kilian)]]", "[[2019 Structural Interpretation of VARs with Incomplete Identification (Baumeister & Hamilton)]]", "[[WTI (국제유가)]]"]
---

# 유가충격 분해의 표준 논문 (Kilian, 2009)

> American Economic Review 99(3) 1053–1069, 2009. `doi:10.1257/aer.99.3.1053`
> ⚠ **본문 미열람**(유료). 서지만 확정했다. **수치는 인용하지 않는다.**

## 왜 중요한가 — 우리 문제와 직결

[[WTI (국제유가)]] 노드의 30년 계보에서 **3단계의 원논문**이다.
[[2009 The Impact of Oil Price Shocks on the U.S. Stock Market (Kilian & Park)]]가
주식시장에 적용한 분해가 바로 이 논문의 것이다.

제목이 곧 실무 규칙이다 — **"모든 유가충격이 같지 않다."**

## 논지

세계 원유시장을 **구조 VAR**로 모형화해 유가 변동을 셋으로 분해한다.

| 충격 | 내용 | 실물 함의 |
|---|---|---|
| **원유 공급충격** | 산유량 자체의 교란 | 비용충격. 물가↑ 산출↓ |
| **총수요충격** | 세계 경기 확장에 따른 수요 | 유가↑지만 성장 신호 |
| **예비적(원유시장 특수) 수요충격** | 미래 공급 불안 대비 재고 수요 | 실물 공급은 그대로인데 가격만 상승 |

**같은 크기의 유가 상승도 어느 충격이냐에 따라 미국 거시경제 반응이 다르다.**
따라서 유가를 단일 외생변수로 넣는 회귀는 부적절하다.

## 한계와 적용 범위

- **사서(추가)**: 본문 미열람이므로 **충격별 반응 크기·분산분해 비율을 인용하지 않는다**
- **사서(추가)**: 식별이 **부호·배제 제약**에 의존한다. 이 식별 자체를
  [[2019 Structural Interpretation of VARs with Incomplete Identification (Baumeister & Hamilton)]]가
  정면으로 재검토한다 — **이 논문을 채택할 때 그 반론도 함께 봐야 한다**
- **사서(추가)**: 표본이 셰일 이전이다. 미국의 산유국 지위 변화가 공급충격의 부호를 바꿀 수 있다
- **사서(추가)**: 한국은 석유 수입국이라 **예비적 수요 충격**이 특히 중요하다 —
  지정학 긴장이 실제 차질 없이 유가를 올리는 국면이 그것이다

## 인과 사슬

유가 상승 관측 → **원인 분해 필요**
→ 공급 차질: 비용충격 → [[CPI (소비자물가지수)]]↑ [[산업생산]]↓
→ 총수요: 성장 신호 → 주가·산출 양(+) 가능
→ 예비적 수요([[지정학적 리스크]]): 가격만 상승, 실물 공급 불변
→ **[[WTI (국제유가)]] 수준만으로는 부호를 정할 수 없다**

**Comment**: DataBook 실무 — `미 원유재고`·`미 원유생산`·`지정학 뉴스`를 함께 받으므로
예비적 수요(재고↑ + 지정학 뉴스↑ + 생산 불변)와 실제 공급 차질(생산↓)을 거칠게나마 가를 수 있다.
[[2024-2026-Comparative-Mechanism-Map]] 1단계의 "에너지 충격"을 읽을 때 이 구분을 먼저 적용할 것.

## 관련 개념

- 주식시장 적용 — [[2009 The Impact of Oil Price Shocks on the U.S. Stock Market (Kilian & Park)]]
- 공급충격의 크기 — [[2008 Exogenous Oil Supply Shocks (Kilian)]]
- 식별에 대한 반론 — [[2019 Structural Interpretation of VARs with Incomplete Identification (Baumeister & Hamilton)]]
- 계보 — [[1983 Oil and the Macroeconomy Since World War II (Hamilton)]] ·
  [[1996 This Is What Happened to the Oil Price-Macroeconomy Relationship (Hamilton)]] ·
  [[2018 Oil Prices and the Stock Market (Ready)]]
- 지표 — [[WTI (국제유가)]] · [[지정학적 리스크]]

## References

[1]: https://www.aeaweb.org/articles?id=10.1257/aer.99.3.1053 "Kilian (2009), Not All Oil Price Shocks Are Alike, AER 99(3) 1053–1069"
