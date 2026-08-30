---
title: The effectiveness of macroprudential policies and capital controls against volatile capital inflows
type: paper
series: BIS Working Papers No 867
date: 2020-06
author: Jon Frost (BIS), Hiro Ito (Portland State University), René van Stralen (De Nederlandsche Bank)
url: https://www.bis.org/publ/work867.pdf
tags: [type/paper, method/propensity-score-matching, method/panel, domain/policy]
concepts: [거시건전성정책, 자본통제, 자본유입, 외환기반 규제, 은행위기, 통화위기]
status: done
verification: full
reliability: working-paper
text_basis: human-fulltext
verified: 원문 대조 완료(2026-08-14). 83개국·2000-17·PSM·3년 지평 등 13개 항목 확인. tier A 승격
related: ["[[Sudden-Stop-and-Bridge-Finance]]", "[[Monetary-Policy-Transmission-and-International-Spillovers]]", "[[원문 아카이브 MOC]]"]
---

# 자본통제는 효과가 없었고 외환기반 거시건전성은 있었다 (Frost, Ito & van Stralen, 2020)

> BIS Working Paper No 867, 2020년 6월. JEL: F38, G01, G28

## 왜 중요한가 — 우리 문제와 직결

[[Sudden-Stop-and-Bridge-Finance]]와 [[Monetary-Policy-Transmission-and-International-Spillovers]]는
"자본흐름 급변에 통화정책만으로 대응하기 어렵고 거시건전성·자본흐름관리를 함께 써야 한다"고
정리한다. **그런데 그 둘이 같은 것인지 다른 것인지는 말하지 않는다.**

이 논문의 기여가 정확히 거기다 — **외환기반(FX-based) 거시건전성정책**과 **자본통제**를
갈라서 비교한다. 결과는 둘이 다르다는 것이고, 방향도 비대칭이다.
볼트 제텔 [[미국이 좋아서 올리는 금리도 한국에는 악재다]]가 말하는 대외 취약성에 대해
**어떤 도구가 실제로 듣는가**를 실증으로 답한다.

## 방법과 자료

| 항목 | 내용 |
|---|---|
| 표본 | **83개국, 2000–2017년** 패널 |
| 핵심 구분 | **FX 기반 MaP**(일부 자본통제와 유사) vs **비FX 기반 MaP** vs **자본통제(CC)** |
| 식별 | **성향점수매칭(PSM)** — 정책을 도입하는 나라가 애초에 다르다는 **선택편향을 통제** |
| 종속변수 | 자본유입의 **규모**와 **구성**, 그리고 향후 3년 내 자본유입 급증·**은행위기**·**통화위기** 확률 |

## 원문에서 확인한 결과

**1. FX 기반 거시건전성정책이 발동된 곳에서 자본유입 규모가 더 낮다.**

**2. 자본통제의 부과는 자본유입의 규모에도 구성에도 유의한 효과가 없다.**
> *"The imposition of CCs does not have a significant effect on the volume or composition
> of capital inflows."*

**3. 거시건전성정책의 발동은 이후 3년간 은행위기 확률과 자본유입 급증 확률이 낮은 것과
연관된다.** 통화위기 확률은 별개 항목으로 검정한다.

## 한계와 적용 범위

- **사서(추가)**: PSM은 **관측 가능한** 특성의 선택편향만 통제한다. "위기 위험을 감지한
  나라가 규제를 도입한다"는 **역인과**는 관측되지 않는 정보에 의존하면 남는다.
  저자들도 인과가 아니라 연관(associated)으로 서술한다
- **사서(추가)**: FX 기반 MaP와 자본통제의 **경계가 원래 흐릿하다.** 저자들이 "일부 자본통제와
  유사할 수 있다"고 인정한 분류가 결과를 좌우한다. 분류 규칙이 바뀌면 결론도 바뀔 수 있다
- **사서(추가)**: 표본이 **2017년에 끝난다.** 2020년 코로나 자본유출, 2022년 미국 긴축기의
  신흥국 유출은 들어 있지 않다
- **사서(추가)**: 한국은 FX 기반 규제(선물환포지션 한도·외환건전성부담금)를 쓰는 대표 사례다.
  이 논문의 결론이 한국에 유리하게 읽히기 쉬운데, **국가별 효과가 아니라 패널 평균**임을 잊지 말 것

## 인과 사슬

글로벌 위험선호 변화 → [[글로벌 유동성]] 확장 → 신흥국 자본유입 급증
→ (FX 기반 MaP 발동 시) 유입 **규모 축소** → 3년 내 은행위기 확률 하락
→ (자본통제만 부과 시) 유입 규모·구성 **변화 없음**

**Comment**: 정책 이름이 아니라 **작동 지점**으로 갈라 봐야 한다는 것이 이 논문의 실무적
교훈이다. 자본통제는 국경에서 막고, FX 기반 MaP는 **금융기관 대차대조표의 통화 불일치**를
제약한다. 후자가 들었다는 것은 취약성의 소재가 유입 자체가 아니라 **누가 어떤 통화로
차입했는가**에 있다는 뜻이다 — [[Credit-Leverage-Risk-Pricing-Loop]]의 "외화 불일치" 조건과 같은 지점.

## 관련 개념

- 메커니즘 — [[Sudden-Stop-and-Bridge-Finance]] · [[Monetary-Policy-Transmission-and-International-Spillovers]]
- 한국 적용 — [[미국이 좋아서 올리는 금리도 한국에는 악재다]] · [[원·달러 환율]]
- 글로벌 유동성 측정 — [[2019 On the Monetary Measures of Global Liquidity (Hashmi & Bhatti)]]
- 등급 체계 — [[원문 아카이브 MOC]]

## References

[1]: https://www.bis.org/publ/work867.pdf "Frost, Ito and van Stralen (2020), The effectiveness of macroprudential policies and capital controls against volatile capital inflows, BIS WP 867"
