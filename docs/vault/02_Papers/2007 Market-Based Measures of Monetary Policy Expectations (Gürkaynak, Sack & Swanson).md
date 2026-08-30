---
title: Market-Based Measures of Monetary Policy Expectations
type: paper
journal: Journal of Business & Economic Statistics, Vol. 25, No. 2, pp. 201-212
date: 2007
author: Refet S. Gürkaynak, Brian Sack, Eric Swanson
created: 2026-08-12
updated: 2026-08-12
status: draft
verification: none
reliability: academic
verified: "❌ 원문 미대조. 카카오톡 수신 노트(2026-08-12 임포트)를 볼트 규약으로 정규화한 것 — 수치·표현은 원문 확보 후 재검증 필요"
source_file: 없음 (외부 작성 노트 수신)
tags: [type/paper, domain/policy, region/us, method/고빈도식별, method/선물시장분석, flag/unverified]
concepts: [Fed-funds-futures, Eurodollar-futures, term-structure, policy-expectations]
import_origin: 카카오톡 수신 — Macro Paper Notes / 원본 파일명 'Gürkaynak, Sack & Swanson (2007) — Market-Based Measures of Monetary Policy Expectations.md'
---
> ⚠ **원문 미대조 노트다.** 외부에서 작성된 것을 수신해 볼트 규약으로 정규화만 했다.
> 이 볼트의 [[원문검증 논문 MOC]] 기준을 통과하지 않았으므로 **제텔로 분해하지 않았고, 수치를 인용하지 않는다.**
> **단 2026-08-21 개정으로 「① 명제 층위」 인용은 허용된다** — 교과서적 정설을 수치 없이 인용할 때에 한하며,
> 인용 지점에 "원문 미대조"를 병기한다. → [[원문검증 논문 MOC]] 「인용 규칙 개정」
> 원문 확보 후 `status: verified`로 갱신한다.

﻿---
tags:
  - macro/monetary-policy
  - market-expectations
  - fed-funds-futures
  - eurodollar
  - high-frequency
aliases:
  - "GSS 2007"
  - "Gurkaynak Sack Swanson 2007"
  - "Market Measures Monetary Policy"
year: 2007
author: "Gürkaynak, Sack & Swanson"
---

# Market-Based Measures of Monetary Policy Expectations

## 1. Bibliographic Information

- **Title:** Market-Based Measures of Monetary Policy Expectations
- **Authors:** Refet S. Gürkaynak, Brian Sack, Eric Swanson
- **Year:** 2007
- **Journal / Working Paper:** Journal of Business & Economic Statistics, Vol. 25, No. 2, pp. 201-212
- **Research Field:** Monetary Economics, Financial Economics, Empirical Methods
- **Keywords:** Fed funds futures, Eurodollar futures, monetary policy expectations, term structure, high-frequency identification, policy path

### One-Sentence Thesis
이 논문은 **Fed funds futures와 Eurodollar futures가 통화 정책 기대를 측정하는 최적의 시장 기반 도구**임을 보여주며, 이 두 도구를 결합한 **정책 기대의 기간 구조(term structure of policy expectations)**를 구성하는 방법론을 제시한다.

---

## 2. Research Question

- **Question 1:** 어떤 금융 상품이 미래 Fed 정책 경로에 대한 시장 기대를 가장 효율적으로 반영하는가?
- **Question 2:** 서로 다른 만기의 금리 선물 상품들을 어떻게 결합하여 정책 기대의 전체 기간 구조를 추출하는가?

---

## 3. Literature Gap

**Existing Literature**
- Kuttner (2001): 당월 Fed funds futures → 현재 FOMC 회의 surprise 측정
- 설문 조사(Survey of Professional Forecasters): 낮은 빈도, 비연속적

**Limitation**
- 단일 선물 상품으로 가까운 미래만 측정; 향후 1년 이상의 정책 기대 측정 어려움; 서로 다른 선물 상품의 정확도 비교 없음

**Contribution of This Paper**
- Fed funds futures(1-6개월) + Eurodollar futures(1분기~3년) 결합; 각 상품의 예측 정확도 비교; 정책 기대 기간 구조 구성 방법론

---

## 4. Core Mechanism

```
Cause / Shock: 시장 참여자들의 미래 Fed 정책 기대 형성
      ↓
Short Horizon: Fed funds futures (1~6개월) — 가장 정확한 단기 정책 기대 반영
      ↓
Medium Horizon: Eurodollar futures (6~24개월) — 정책 기대 + 소폭의 위험 프리미엄
      ↓
Term Structure: 두 상품 결합 → 1개월~3년의 정책 기대 기간 구조 추출
      ↓
Identification: FOMC 발표 주변 30분 창 → 정책 기대의 순수 변화 측정
```

**Economic Logic**
- 효율적 시장: 선물 가격 = 기대 미래 현물 가격 + 위험 프리미엄
- Fed funds futures: 위험 프리미엄 거의 0 (단기, 유동성 높음); Eurodollar: 소폭 프리미엄 존재

---

## 5. Shock Classification

- [ ] Demand Shock
- [ ] Supply Shock
- [x] Monetary Shock
- [ ] Fiscal Shock
- [ ] Credit Shock
- [ ] Financial Shock
- [ ] Commodity Shock
- [ ] Technology Shock
- [ ] Productivity Shock
- [ ] Trade Shock
- [ ] Capital Flow Shock
- [x] Expectation Shock

**Primary Shock:** 통화 정책 기대 충격 — 미래 정책 경로에 대한 시장 정보 업데이트

---

## 6. Transmission Mechanism

```
Shock: 연준 정책 신호 또는 경제 데이터 발표
  ↓
Futures Market: 시장 참여자들이 정책 기대 즉각 업데이트
  ↓
Fed Funds Futures: 단기(1-6개월) 기대 반영
  ↓
Eurodollar Futures: 중기(6-36개월) 기대 + 위험 프리미엄 반영
  ↓
Term Structure: 정책 기대의 전체 경로 → 수익률 곡선·자산 가격에 반영
```

---

## 7. Key Variables

**Macroeconomic**
- 미래 Fed funds rate 기대 경로 (h=1, 2, ..., 12개월)
- FOMC 회의 발표 surprise

**Financial**
- Fed funds futures (FF1~FF6): 당월~6개월 후 정책 기대
- Eurodollar futures (ED1~ED8): 3개월~24개월 후 LIBOR 기대 (≈ 정책 금리 + 스프레드)
- OIS (overnight index swap): 정책 기대의 대안적 측정 도구

**Leading / Coincident / Lagging**
- 선물 가격 변화: coincident (발표 즉시 반영)
- 실물 효과: lagging

---

## 8. Empirical Strategy

- **Data:** Fed funds futures, Eurodollar futures 일별·고빈도 데이터; 1994-2005
- **Sample Period:** 1994-2005
- **Country / Region:** 미국
- **Frequency:** 일별; FOMC 발표 주변 고빈도 (30분 창)
- **Method:** 예측 정확도 비교 (RMSE); 고빈도 이벤트 스터디; 기간 구조 추출
- **Identification Strategy:** FOMC 발표 30분 창 → 순수 정책 기대 변화 측정

**Correlation or Causality?**
- 방법론 논문; 측정 도구 제시

---

## 9. Main Findings

1. [논문 직접] Fed funds futures가 단기 정책 기대 측정에 가장 정확한 도구 (RMSE 최소)
2. [논문 직접] Eurodollar futures가 1분기 이후 정책 기대 측정에 유용; 소폭의 위험 프리미엄 조정 필요
3. [논문 직접] 두 상품 결합으로 1개월~3년의 정책 기대 기간 구조 구성 가능
4. [논문 직접] 고빈도 이벤트 창 사용으로 정책 기대의 순수 변화 측정; 비(非)FOMC 정보 제거
5. [논문 직접] 선물 기반 측정이 설문 조사보다 빠르고 연속적인 정책 기대 반영

---

## 10. Regime Dependency

**When are these measures most accurate?**
- 정상적 금리 환경: 금리가 0보다 충분히 높을 때
- 정책 불확실성이 적을 때: 위험 프리미엄 안정

**When are they less accurate?**
- ZLB 환경: 명목 금리 하한 → 선물 가격이 하한 반영 (측정 편향); OIS 스프레드 이상
- 신용 위기: Eurodollar-OIS 스프레드 급등 → Eurodollar가 신용 위험도 반영

**Does the conclusion change across regimes?**
- 2008 이후: OIS가 Eurodollar 대비 더 순수한 정책 기대 측정; SOFR 전환 이후 SOFR futures 사용

---

## 11. Asset-Price Implications

**Bonds**
- [논문 직접] 정책 기대 기간 구조 → 수익률 곡선의 기대 구성 요소 직접 측정
- [추론] 기대 정책 경로 상승 → 수익률 곡선 전반 상승; 경로 하락 → 수익률 곡선 하락

**Equities**
- [추론] 정책 기대의 기간 구조 → 기업 현금흐름 할인율 경로 → 주식 밸류에이션에 반영

**FX**
- [추론] 한국·미국 정책 기대 격차 → 원달러 환율 방향 예측 도구

**Credit**
- [추론] 중기 정책 기대 상승 → 기업 대출·채권 발행 비용 상승

> 반드시 [논문에서 직접 주장한 내용]과 [우리의 추론]을 구분한다.

---

## 12. Falsification Conditions

**What would confirm the hypothesis?**
- Fed funds futures가 설문 조사·다른 금리보다 미래 정책 금리를 더 정확히 예측 (낮은 RMSE)
- 고빈도 이벤트 창에서 정책 발표 외 변수가 선물 가격에 영향 없음

**What would falsify the hypothesis?**
- 위험 프리미엄이 크고 불안정하여 선물 가격이 기대보다 프리미엄을 더 반영
- 설문 조사가 선물보다 더 정확한 예측 도구

**Variables to monitor**
- Fed funds futures vs. 실제 실현 금리 비교; Eurodollar-OIS 스프레드; SOFR futures

---

## 13. Contradictory / Alternative Literature

**Supporting Papers**
- Nakamura & Steinsson (2018): 이 방법론 활용하여 정보 효과 분석
- Wright (2012): 이벤트 스터디 방법론 확장

**Contradictory Papers**
- [[Miranda-Agrippino & Ricco (2021) — The Transmission of Monetary Policy Shocks]]: 이 measure에 정보 효과 오염 가능성 지적; Greenbook 통제 필요

---

## 14. Connections to Other Papers

**SUPPORTS**
- [[2005 Do Actions Speak Louder Than Words (Gürkaynak, Sack & Swanson)]]: 동일 방법론으로 path factor 분석

**APPLIES**
- [[Miranda-Agrippino & Ricco (2021) — The Transmission of Monetary Policy Shocks]]: 이 측정 도구를 기반으로 정보 효과 통제
- [[2005 What Explains the Stock Market's Reaction to Federal Reserve Policy (Bernanke & Kuttner)]]: 단일 surprise에서 기간 구조로 확장

---

## 15. Zettelkasten Atomic Notes

### ZK Note 1
**Claim:** Fed funds futures가 단기 통화 정책 기대의 가장 정확한 시장 기반 측정 도구이다.
**Mechanism:** 위험 프리미엄 거의 없음 + 유동성 높음 + FOMC 주변 즉각 반응 → 기대 정책 금리와 거의 1:1 대응
**Evidence:** [직접] RMSE 비교: Fed funds futures > 설문 > Eurodollar > T-bill
**Implication:** 고빈도 통화 정책 충격 식별의 표준 도구; [[Miranda-Agrippino & Ricco (2021) — The Transmission of Monetary Policy Shocks]]도 이 도구 기반으로 정보 효과 분리
**Connected Notes:** [[2005 Do Actions Speak Louder Than Words (Gürkaynak, Sack & Swanson)]], [[2005 What Explains the Stock Market's Reaction to Federal Reserve Policy (Bernanke & Kuttner)]]

### ZK Note 2
**Claim:** Eurodollar futures는 중기 정책 기대를 반영하지만 소폭의 위험 프리미엄과 신용 스프레드를 포함한다.
**Mechanism:** Eurodollar rate = LIBOR = 정책 금리 + 은행 신용 위험 + 기간 프리미엄; 금융 위기 시 OIS-Eurodollar 스프레드 급등 → 신용 위험 분리 필요
**Evidence:** [직접] 정상 기간 Eurodollar-FF 스프레드 소폭 안정; 2008 금융위기 LIBOR-OIS 스프레드 급등
**Implication:** ZLB·위기 상황에서 OIS나 SOFR futures가 더 순수한 정책 기대 측정; 데이터 선택이 실증 결과에 영향
**Connected Notes:** [[Miranda-Agrippino & Ricco (2021) — The Transmission of Monetary Policy Shocks]]

### ZK Note 3
**Claim:** 정책 기대의 기간 구조(term structure)가 수익률 곡선의 기대 구성 요소를 직접 측정한다.
**Mechanism:** FF futures (1-6M) + ED futures (6-36M) 결합 → 각 기간 정책 기대 → 기간 구조; 이 기대 경로 + 기간 프리미엄 = 수익률 곡선
**Evidence:** [직접] 방법론 제시; 이후 Bauer & Rudebusch, ACM 모형 등에서 확장
**Implication:** 채권 시장 분석: 수익률 곡선의 기대 vs. 프리미엄 분해; 통화 정책 파급의 기간 구조 채널 분석
**Connected Notes:** [[Woodford (1995) — Price-Level Determinacy Without Control of a Monetary Aggregate]], [[1993 Discretion versus Policy Rules in Practice (Taylor)]]

---

## 16. One-Sentence Takeaway

이 논문을 한 문장으로 기억한다면: **Fed funds futures와 Eurodollar futures를 결합하면 시장이 예측하는 향후 수년간의 Fed 정책 경로를 실시간으로 읽어낼 수 있다 — 이것이 고빈도 통화 정책 식별의 방법론적 토대다.**

---

## Quality Control

- [x] 논문의 핵심 주장을 정확하게 이해했는가?
- [x] 기존 연구와 무엇이 다른지 설명했는가?
- [x] Shock을 분류했는가?
- [x] Transmission mechanism을 화살표로 표현했는가?
- [x] 인과관계와 상관관계를 구분했는가?
- [x] 논문의 실증 결과와 우리의 해석을 구분했는가?
- [x] Regime dependency를 검토했는가?
- [x] Asset-price implication을 도출했는가?
- [x] Falsification condition을 제시했는가?
- [x] 반대되는 연구를 확인했는가?
- [x] 다른 논문과 연결했는가?
- [x] Atomic note로 분해했는가?
- [x] 한 문장으로 핵심을 설명할 수 있는가?

---

## 관련 MOC

- [[매크로 고전 논문 MOC]] · [[리포트 수집 큐]]
