---
title: Global risk aversion and US corporate default risk premium
type: paper
journal: BCP Business & Management, EMFRM 2022, Vol.38 (2023), pp.158-163
date: 2023
author: Jiawei Yuan (University of Warwick)
created: 2026-07-28
status: done
verification: full
reliability: opinion
verified: 원문 대조 완료(2026-07-28, 6p) · **FRED 원자료로 직접 재현 완료**
source_file: EMFRM+2022-158-163.pdf
tags: [type/paper, domain/risk, region/us, method/OLS, flag/needs-review]
concepts: [VIX, risk-aversion, default-risk-premium, log-linear, 단위해석오류]
related: ["[[2014 The Impact of Global Volatility on Asian Financial Markets (Kang·Choi·Yoon)]]", "[[2022 VIX Impact on Chinese Corporate Bond Default (Zhou)]]"]
---

# Global risk aversion and US corporate default risk premium

> ⚠ **인용 주의.** 추정치는 재현되지만 **논문의 핵심 해석이 100배 틀렸다.**
> 종속변수 정의도 "부도위험 프리미엄"이 아니다. `reliability: opinion` · `flag/needs-review`

## 논문이 한 것

- 모형: `premium_t = α₀ + α₁·log(VIX_t) + ε_t` — **단변량 OLS**
- 표본: 2008.01~2017.12 월별, n=132, WIND 데이터베이스
- premium = **Moody's 회사채 수익률 − 연방기금금리**
- 결과: **α₁ = 2.3802** (SE 0.2088) · 상수 −1.9826 (SE 0.6114) · p=0.000 · R² = 0.500
- 논문의 해석(초록·서론·결과·결론 **4회 반복**):
  > "a one-percentage-point change in the VIX leads to an increase of **2.3802 percentage points** in the US corporate risk premium"

## 직접 재현 (2026-07-28, FRED 원자료)

코드 `_System/Analysis/vix_default_premium_replication.py`

| 사양 | α₁ | SE | 상수 | R² |
|---|---|---|---|---|
| **논문 보고** | **2.3802** | 0.2088 | −1.9826 | 0.500 |
| **Moody's Baa − FF** (재현) | **2.3292** | 0.1757 | −1.6656 | 0.598 |
| Moody's Aaa − FF | 1.1550 | 0.1666 | +0.5984 | 0.290 |

→ **추정치는 재현된다.** 논문이 쓴 것은 **Baa**다(명시하지 않았다).
   n 차이(120 vs 132)는 표본 시작점 표기 차이로 보인다.

## 치명적 오류 ① — 해석이 100배 틀렸다

설명변수는 **log(VIX)** 인데 해석은 **VIX 수준**으로 한다.

```
log-선형 모형:  Δpremium = α₁ · Δ(log VIX) = α₁ · (ΔVIX / VIX)

올바른 해석 : VIX가 **1% 상승** → 프리미엄 +0.0233%p  (= α₁/100)
논문의 해석 : VIX가 **1포인트 상승** → 프리미엄 +2.3802%p
```

논문 서술을 실제 위기에 적용하면:

| 국면 | 논문 서술대로 | 올바른 해석 |
|---|---|---|
| VIX 12 → 80 (리먼·코로나) | **+162%p (16,185bp)** | **+4.42%p** |
| VIX 15 → 40 (2018) | +60%p | +2.28%p |
| VIX 13 → 65 (2024 캐리청산) | +124%p | +3.75%p |

**미 회사채 스프레드가 162%p 벌어지는 일은 존재하지 않는다.**
반면 위기에 +4.4%p(440bp)는 실제 관측치와 잘 맞는다.
→ **추정은 타당하고 해석만 틀렸다.** 논문의 결론 문장은 그대로 인용 불가.

## 치명적 오류 ② — 종속변수가 부도위험 프리미엄이 아니다

"Moody's 회사채 − **연방기금금리**"는 만기가 전혀 다른 두 금리의 차다.
Moody's 계열은 장기(20~30년 평균), FF는 익일물이다.
→ 이 "프리미엄"에는 **신용스프레드 + 기간프리미엄 + 정책금리 경로 기대**가 뒤섞인다.

**표본기간이 하필 제로금리 구간이다.**

| 항목 | 값 |
|---|---|
| FF 평균 / 중앙값 | 0.42% / **0.16%** |
| FF ≤ 0.25%인 개월 | **85 / 120 (71%)** |
| (Baa − FF) 와 Baa 수준의 상관 | **0.835** |

→ 표본의 71%에서 이 변수는 **사실상 Baa 수익률 수준 그 자체**다.
   즉 "VIX와 부도위험"이 아니라 **"VIX와 회사채 수익률 수준"** 을 추정한 것이다.

**진짜 신용스프레드로 바꾸면 계수가 달라진다**

| 종속변수 | α₁ | R² |
|---|---|---|
| Baa − FF (논문 사양) | 2.3292 | 0.598 |
| **Baa − 미 국채 10년** (BAA10Y) | **1.6705** | **0.693** |

→ 기간프리미엄을 걷어내면 계수가 **28% 작아지고** 적합도는 오른다.
   논문 계수의 약 3분의 1이 **신용이 아니라 만기 구조**에서 온다.

## 치명적 오류 ③ — 제목·초록·본문·논의가 서로 다른 나라를 말한다

| 층 | 대상 |
|---|---|
| **제목** | **US** corporate default risk premium |
| **초록 첫 문장** | "the default rate of **China's** bond market has been increasing… explores the impact on **Chinese** corporate bond default" |
| **실제 분석** | **미국** 데이터만 (Moody's, FF, VIX) |
| **결과 논의** | 대부분 **중국** — 지방정부 융자평대(LGFV), 산둥·상하이 2018년 사례, 8.11 환율개혁, 위안화 절하와 자본유출 |

→ **회귀식에 중국 변수가 하나도 없는데 논의의 절반이 중국이다.**
   [[매크로 해석 프레임]] 3단계의 "네 층 대조"에 정확히 걸린다.

## 그 밖의 문제

**④ 표본 밖 사건을 근거로 든다** — 표본은 2017.12에 끝나는데
논의에서 "2018년 지방정부 융자평대…", "2019년 현재 환율·자본계정 압력은 낮지만…"을 서술한다.

**⑤ 단위근 검정·통제변수·자기상관 보정이 전부 없다**
월별 수준 변수 두 개의 단변량 OLS다. 두 계열 모두 지속성이 높아 **허구회귀 위험**이 있는데
ADF/PP 검정도, Newey-West도, 통제변수(국채금리·기간스프레드·거시)도 없다.
R²=0.500은 추세를 공유하는 두 계열에서 쉽게 나온다.

**⑥ 모형 서술이 자기 식과 모순** — 본문은 α₁이 "one-unit VIX index"의 효과라고 쓰는데
식 (1)의 설명변수는 log VIX다. **오류 ①의 근원이 여기 있다.**

**⑦ 한계 절 없음** · 6페이지 컨퍼런스 프로시딩, 단독 저자, 동료심사 수준 불명

## 그래도 쓸 수 있는 것

**올바르게 해석한 계수는 이 vault에서 쓸 수 있다.**

> [[VIX]]가 1% 오르면 미 Baa 신용스프레드(국채 10년 대비)가 **약 1.7bp** 확대된다 (R²=0.69).
> 위기 국면(VIX 12→80)이면 누적 **+3.2%p** 수준.

이는 [[2014 The Impact of Global Volatility on Asian Financial Markets (Kang·Choi·Yoon)]]의
"VIX → 아시아 주식·환율" 과 짝을 이뤄 **VIX의 전달 경로를 신용시장까지 확장**한다.

## 관련 개념

[[VIX]] · [[신용스프레드]] · [[기업 부도]] · [[신용사이클]] · [[장단기 금리차]] · [[기준금리]]

## 관련 MOC

- [[지표 MOC]] · [[매크로 해석 프레임]] · [[제텔 MOC]]
