---
title: "The Impact of Oil Price Shocks on the U.S. Stock Market"
type: paper
journal: International Economic Review 50(4), 1267–1287 (2009)
date: 2009
author: Lutz Kilian (Michigan / Dallas Fed), Cheolbeom Park (Korea University)
doi: 10.1111/j.1468-2354.2009.00568.x
url: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-2354.2009.00568.x
tags: [type/paper, method/structural-VAR, domain/commodities]
concepts: [유가충격 분해, 공급충격, 총수요충격, 원유시장 특수수요, 예비적 수요]
status: done
verification: partial
reliability: academic
text_basis: cited-primary
verified: "△ 서지 확정(2026-08-14): IER 50(4) 1267–1287, doi:10.1111/j.1468-2354.2009.00568.x. 원 2차 요약(L48)의 URL은 **무관한 논문**(NBER w14588 = 비디오 대여업 계약)이었다 — 이 노트에서 바로잡는다. 본문 유료라 미열람, **수치 인용 금지**"
promoted_from: "[[L48 The Impact of Oil Price Shocks on the U.S. Stock Market]]"
related: ["[[2018 Oil Prices and the Stock Market (Ready)]]", "[[WTI (국제유가)]]", "[[2024-2026-Comparative-Mechanism-Map]]"]
---

# 유가는 하나의 충격이 아니다 — 세 가지로 갈라야 한다 (Kilian & Park, 2009)

> International Economic Review 50(4) 1267–1287, 2009. `doi:10.1111/j.1468-2354.2009.00568.x`
> ⚠ **본문 미열람**(유료). 서지만 확정했다. **수치는 인용하지 않는다.**

> 📌 원 2차 요약 [[L48 The Impact of Oil Price Shocks on the U.S. Stock Market]]은 출처를
> `nber.org/papers/w14588`로 적었는데, 그 번호는 **비디오 대여업 계약에 관한 논문**이다.
> 유가와 무관하다. 경위: [[05_Library 중복 판별 (2026-08-14)]]
>
> 공저자 **Cheolbeom Park는 고려대** 소속이다 — 한국 연구자가 쓴 유가 표준 참조다.

## 왜 중요한가 — 우리 문제와 직결

[[2018 Oil Prices and the Stock Market (Ready)]]와 **같은 문제, 다른 해법**이다.
Ready는 주가(산유기업 지수)로 갈랐고, Kilian-Park는 **구조 VAR**로 가른다.
둘이 같은 방향의 결론에 **독립적인 방법으로** 도달한다는 점이 중요하다.

그리고 이 분해가 [[2024-2026-Comparative-Mechanism-Map]] 1단계
(관세·지정학·공급망·에너지)의 해석에 직접 걸린다 —
**같은 유가 상승도 원인이 다르면 주가·실물 반응이 반대**다.

## 논지

유가 변화를 원인별로 **셋**으로 분해한다.

| 충격 | 내용 |
|---|---|
| **원유 공급충격** | 산유량 자체의 변화 |
| **총수요충격** | 세계 경기 확장에 따른 수요 증가 |
| **원유시장 특수수요충격** | 미래 공급 불안에 대비한 **예비적 수요**(precautionary demand) |

미국 실질 주가수익률의 반응은 **어느 충격이냐에 따라 크게 다르다.**
따라서 "유가 상승"을 단일 변수로 넣고 효과를 추정하는 관행은 부적절하다.

## 한계와 적용 범위

- **사서(추가)**: 본문 미열람이므로 **충격별 반응 크기·기여도를 인용하지 않는다**
- **사서(추가)**: 구조 VAR 식별은 **부호·배제 제약**에 의존한다. Ready가 주가 기반 직교화로
  다른 식별을 쓴 것이 서로에 대한 강건성 점검이 된다 — 두 방법이 같은 방향이면 신뢰도가 오른다
- **사서(추가)**: 표본이 셰일 이전이다. 미국의 산유국 지위 변화가 공급충격의 부호를
  바꿀 수 있다(수입국일 때와 수출국일 때 총주가 반응이 다르다)
- **사서(추가)**: 한국 적용 시 **예비적 수요 충격**이 특히 중요하다 —
  지정학 긴장이 실제 공급 차질 없이 유가를 올리는 국면이 그것이다.
  DataBook의 `지정학 — 중동` 뉴스 지표와 함께 읽을 것

## 인과 사슬

유가 상승 → **원인 분해**
→ ① 공급 차질: 비용충격 → 실물·주가 음(−)
→ ② 세계 총수요 강세: 성장 신호 → 주가 양(+)일 수 있음
→ ③ 예비적 수요(지정학 불안): 실물 공급은 그대로인데 가격만 상승 → 별도 반응
→ **[[WTI (국제유가)]] 수준만 보면 셋이 섞여 부호를 못 정한다**

**Comment**: 실무 규칙 — **유가 지표에 "왜 올랐나"를 항상 붙인다.**
DataBook은 `미 원유재고`·`미 원유생산`·`지정학 뉴스`를 함께 받으므로
③(예비적 수요)과 ①(실제 공급 차질)을 어느 정도 가를 수 있다.
[[2025 Post-Pandemic Global Inflation and Disinflation (Clarida, NBER W33885)]]이
2021~22년을 "공급충격 + 완화적 정책"으로 정리했는데, 그 공급충격도 이 셋 중 무엇이었는지
구분하면 정책 함의가 달라진다.

## 관련 개념

- 독립적 재확인 — [[2018 Oil Prices and the Stock Market (Ready)]]
- 유가-거시 원전 — [[1983 Oil and the Macroeconomy Since World War II (Hamilton)]] ·
  [[1996 This Is What Happened to the Oil Price-Macroeconomy Relationship (Hamilton)]]
- 국면 지도 — [[2024-2026-Comparative-Mechanism-Map]]
- 지표 — [[WTI (국제유가)]] · [[지정학적 리스크]]

## References

[1]: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-2354.2009.00568.x "Kilian and Park (2009), The Impact of Oil Price Shocks on the U.S. Stock Market, IER 50(4) 1267–1287"
