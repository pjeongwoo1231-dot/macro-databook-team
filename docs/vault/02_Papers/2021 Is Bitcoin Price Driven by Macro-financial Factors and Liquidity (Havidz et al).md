---
title: Is Bitcoin Price Driven by Macro-financial Factors and Liquidity? A Global Consumer Survey Empirical Study
type: paper
journal: Organizations and Markets in Emerging Economies, 2021, vol. 12, no. 2(24), pp. 399-414. DOI 10.15388/omee.2021.12.62
date: 2021
author: Shinta Amalina Hazrati Havidz(Bina Nusantara University, 교신) · Viendya Ervina Karman · Indra Yudha Mambea(ITB)
created: 2026-08-05
status: done
verification: full
reliability: academic
verified: 원문 대조(2026-08-05, pymupdf 전문 추출 16p — 초록·서론 정독. 회귀표 개별 계수는 미대조)
source_file: 22607-54738.pdf
tags: [type/paper, domain/crypto, region/global, method/고정효과모형, method/GMM, method/패널]
concepts: [macro-financial, liquidity-ratio, 대체자산, 금, 달러, 투기자산]
related: ["[[2018 Do global factors impact bitcoin prices - wavelet approach (Das & Kannadhasan)]]", "[[2022 Liquidity Connectedness in Cryptocurrency Market (Hasan et al)]]", "[[2019 Determining Factors of Kimchi Premium (Jeong Hun Oh)]]"]
---

# Is Bitcoin Price Driven by Macro-financial Factors and Liquidity? (Havidz et al., 2021)

> [[2018 Do global factors impact bitcoin prices - wavelet approach (Das & Kannadhasan)]]와 **같은 질문, 다른 방법**.
> 웨이블릿(시간–주파수)이 아니라 **18개국 패널 회귀**로 접근한다.

## 핵심 결과

**설계**
- 표본: **18개국, 주간 데이터, 2017-01-01 ~ 2019-12-29, 총 2,826 관측치**
- 방법: **고정효과모형(FEM) + GMM**
- 설명변수 — 거시금융: **환율 · 주가지수 · 금리 · 금** / 내부요인: **유동성 비율**

**결과**
| 변수 | 결과 |
|---|---|
| **미 달러** | 비트코인 거래를 **증폭**시킨다 |
| **금리** ↑ | 투기자산으로서 비트코인에 투자할 **유인 감소** |
| **금** | 비트코인의 **대체자산**으로 작동 |
| **유동성** | 비트코인은 유동성이 높아 **투자자를 끌어들인다** |
| **주가지수** | **비유의** |

## 모형 선택의 근거

국가별 이질성을 통제하기 위해 **고정효과**를, 내생성(가격과 유동성의 동시결정)을 다루기 위해 **GMM**을 함께 쓴다.
단일 국가·단일 시계열이 아니라 **18개국 패널**을 구성한 것이 이 논문의 차별점이다.

## 인과 사슬

[[기준금리]] ↑ → 무위험 수익률 상승 → **투기자산 비트코인의 상대매력 하락** → 수요 감소

[[DXY (달러지수)]] 변동 → 비트코인 **거래 활동 증폭**

금 가격 → **대체자산 관계** → 비트코인 수요와 경합

주식([[KOSPI]]류 지수) → **비유의** → 단순 "위험자산 동조"로 설명되지 않는다

**Comment**: 이 논문의 값은 **"주가지수는 비유의"** 라는 음의 결과에 있다.
[[2018 Do global factors impact bitcoin prices - wavelet approach (Das & Kannadhasan)]]가
"단기에는 절연, 중장기에는 동조"라고 했던 것과 겹쳐 읽으면 —
**주간 빈도·2017~2019 표본에서는 주식과의 동조가 잡히지 않는다.**
2020년 이후 기관 자금 유입으로 주식-크립토 상관이 크게 올라갔다는 후속 보고들과 대비되므로,
[[스테이블코인]]·크립토 노드에는 **"동조성은 시기에 따라 달라진다"**는 조건을 유지할 것.

## 저자가 밝힌 한계

초록·서론 범위에서 **명시적 한계 절은 확인되지 않는다.** 결론은 투자자·규제당국 함의 중심이다.

## 검증 필요 · 반박 포인트 (Red Team)

**① 표본 기간이 2017~2019년이다**
비트코인 역사에서 **2017 버블 → 2018 붕괴 → 2019 회복**이라는 극단적 구간이다.
이 3년의 결과를 **일반화하기 어렵다.** 2020년 이후 기관 진입·ETF 국면은 완전히 다른 체제일 수 있다.

**② "18개국 패널"의 의미**
비트코인 가격은 **글로벌 단일 시장**에서 형성된다. 국가별로 나눈 것은 거래소·통화 기준의 차이일 텐데,
그렇다면 국가 간 변동이 **환율 변동을 재측정한 것**에 가까울 수 있다. 종속변수 정의 확인이 필요하다.

**③ 유동성 비율의 내생성**
가격이 오르면 거래가 늘고 유동성이 개선된다 — **역인과**가 강한 변수다.
GMM으로 처리했다고 밝히지만, 도구변수의 타당성 검정(과다식별 검정 등) 결과를 확인해야 한다.

**④ 게재지 인지도**
Vilnius University Press의 오픈액세스 저널이다. 심사를 거친 학술지이나
이 vault 기준으로는 **후속 인용 여부를 함께 보는 것**이 안전하다.

## 관련 개념

[[스테이블코인]] · [[김치프리미엄]] · [[DXY (달러지수)]] · [[기준금리]]

## 관련 MOC

- [[지표 MOC]] · [[원문검증 논문 MOC]]
