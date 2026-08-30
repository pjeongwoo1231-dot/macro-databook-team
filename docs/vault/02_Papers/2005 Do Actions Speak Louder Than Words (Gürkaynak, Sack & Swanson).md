---
title: Do Actions Speak Louder Than Words
type: paper
journal: International Journal of Central Banking, Vol. 1, No. 1, pp. 55-93
date: 2005
author: Refet S. Gürkaynak, Brian Sack, Eric Swanson
created: 2026-08-12
updated: 2026-08-12
status: draft
verification: none
reliability: academic
verified: "❌ 원문 미대조. 카카오톡 수신 노트(2026-08-12 임포트)를 볼트 규약으로 정규화한 것 — 수치·표현은 원문 확보 후 재검증 필요"
source_file: 없음 (외부 작성 노트 수신)
tags: [type/paper, domain/policy, domain/asset, region/us, method/요인분해, method/고빈도식별, flag/unverified]
concepts: [forward-guidance, target-factor, path-factor, FOMC-statement, policy-surprise]
import_origin: 카카오톡 수신 — Macro Paper Notes / 원본 파일명 'Gürkaynak, Sack & Swanson (2005) — Do Actions Speak Louder Than Words - The Response of Asset Prices to Monetary Policy Actions and Statements.md'
---
> ⚠ **원문 미대조 노트다.** 외부에서 작성된 것을 수신해 볼트 규약으로 정규화만 했다.
> 이 볼트의 [[원문검증 논문 MOC]] 기준을 통과하지 않았으므로 **제텔로 분해하지 않았고, 수치를 인용하지 않는다.**
> **단 2026-08-21 개정으로 「① 명제 층위」 인용은 허용된다** — 교과서적 정설을 수치 없이 인용할 때에 한하며,
> 인용 지점에 "원문 미대조"를 병기한다. → [[원문검증 논문 MOC]] 「인용 규칙 개정」
> 원문 확보 후 `status: verified`로 갱신한다.

﻿---
tags:
  - macro/monetary-policy
  - forward-guidance
  - high-frequency
  - factor-model
  - asset-prices
aliases:
  - "GSS 2005"
  - "Gurkaynak Sack Swanson 2005"
  - "Target Path Factor"
year: 2005
author: "Gürkaynak, Sack & Swanson"
---

# Do Actions Speak Louder Than Words - The Response of Asset Prices to Monetary Policy Actions and Statements

## 1. Bibliographic Information

- **Title:** Do Actions Speak Louder Than Words? The Response of Asset Prices to Monetary Policy Actions and Statements
- **Authors:** Refet S. Gürkaynak, Brian Sack, Eric Swanson
- **Year:** 2005
- **Journal / Working Paper:** International Journal of Central Banking, Vol. 1, No. 1, pp. 55-93
- **Research Field:** Monetary Economics, Financial Economics
- **Keywords:** forward guidance, monetary policy surprise, target factor, path factor, high-frequency identification, FOMC statement, asset prices

### One-Sentence Thesis
이 논문은 **FOMC 발표에 내재된 통화 정책 surprise를 '목표 요인(target factor)'과 '경로 요인(path factor)'으로 분해**하여, **연준의 발표문(statements)이 금리 결정과 독립적으로 자산 가격을 유의미하게 움직이는** forward guidance의 실증적 중요성을 보여준다.

---

## 2. Research Question

- **Question 1:** FOMC 금리 결정과 별도로 발표문(statement)이 자산 가격에 독립적인 영향을 주는가?
- **Question 2:** 통화 정책 surprise를 어떻게 두 가지 독립적 요인으로 분해할 수 있는가?

---

## 3. Literature Gap

**Existing Literature**
- [[2005 What Explains the Stock Market's Reaction to Federal Reserve Policy (Bernanke & Kuttner)]]: 단일 surprise measure (Fed funds futures); 현재 결정만 반영
- Kuttner (2001): 당월 Fed funds futures → 현재 금리 결정 surprise

**Limitation**
- 향후 정책 경로(expected path)에 대한 정보가 자산 가격에 미치는 효과를 별도로 측정하지 못함

**Contribution of This Paper**
- FOMC 발표 주변 고빈도 데이터에 요인 모형 적용; target factor(현재 결정)와 path factor(미래 경로) 분리; 각각의 자산 가격 효과 별도 추정

---

## 4. Core Mechanism

```
Cause / Shock: FOMC 회의 발표 (금리 결정 + 발표문)
      ↓
Target Factor: 현재 회의에서의 예상치 못한 금리 변화 → 단기 금리에 집중된 효과
      ↓
Path Factor: 발표문이 시사하는 향후 정책 경로 변화 → 중장기 금리에 집중된 효과
      ↓
Asset Price Response: 두 요인 각각이 독립적으로 금리 곡선·주가·환율에 영향
      ↓
Forward Guidance: Path factor의 효과가 target factor와 독립적으로 유의미함 실증
```

**Economic Logic**
- 단기 금리 futures(FF1~FF4) 변화를 행렬로 쌓아 주성분 분석(PCA) → 첫 두 요인이 FOMC 주변 분산의 대부분 설명
- 요인 회전: Factor 1 = target factor (당일 금리 변화와 최대 상관); Factor 2 = path factor

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

**Primary Shock:** 통화 정책 정보 충격 — target 결정 + forward guidance(path)

---

## 6. Transmission Mechanism

```
Shock: FOMC 발표 (금리 동결 + 매파적 발표문)
  ↓
Target Factor: 현재 금리 변화 없음 → target factor 충격 없음
  ↓
Path Factor: 발표문 "will remain firm" → 미래 금리 인상 기대 상승 → path factor 양수
  ↓
Yield Curve: 단기 금리 소폭 상승; 장기 금리 더 크게 상승 (path factor 중장기 영향)
  ↓
Asset Prices: 주가 하락 (할인율 상승); 달러 강세 (금리 차익 기대)
```

---

## 7. Key Variables

**Macroeconomic**
- FOMC 회의 발표일 이벤트 창 (30분 또는 당일)
- 정책 경로 기대: Fed funds futures 1-6개월물 변화

**Financial**
- Target factor, path factor (직교화된 두 요인)
- 2년, 5년, 10년 국채 금리; S&P 500; 달러 인덱스
- Eurodollar futures (policy path의 시장 기대 반영)

**Leading / Coincident / Lagging**
- Path factor → 중장기 금리: 즉각 (발표 즉시)
- 실물 경제: lagging

---

## 8. Empirical Strategy

- **Data:** FOMC 발표일 고빈도 금리 futures 데이터; 1991-2004
- **Sample Period:** 1991-2004
- **Country / Region:** 미국
- **Frequency:** 고빈도 (30분 창, intraday)
- **Method:** 주성분 분석(PCA) → 요인 회전 → OLS 회귀 (요인 → 자산 가격)
- **Identification Strategy:** 고빈도 이벤트 창으로 역인과 제거; 요인 직교화로 두 충격 분리

**Correlation or Causality?**
- 고빈도 이벤트 스터디 → 인과 식별 강력

---

## 9. Main Findings

1. [논문 직접] FOMC 발표 주변 금리 변동은 두 요인 (target, path)으로 대부분 설명
2. [논문 직접] Path factor (forward guidance)가 장기 금리에 target factor보다 더 강하게 영향
3. [논문 직접] 발표문(statements)이 금리 결정과 독립적으로 금리 곡선·주가를 유의미하게 움직임
4. [논문 직접] 1999년 이후 연준의 명시적 forward guidance 도입 → path factor의 중요성 증가
5. [논문 직접] 2년 국채가 path factor에 가장 민감하게 반응; 10년 채권은 다소 덜 민감

---

## 10. Regime Dependency

**When is path factor more important?**
- ZLB 환경: target factor 분산 거의 0 → path factor (forward guidance)가 사실상 유일한 정책 도구
- 명시적 forward guidance 도입 기간: 2008년 이후 "low for long" 공약
- 정책 불확실성이 높을 때: 발표문이 더 많은 정보 제공

**When is target factor more important?**
- 정책 예측 어려운 환경; 급격한 금리 변화; 정상 금리 사이클

**Does the conclusion change across regimes?**
- 2008-2015 ZLB 이후: forward guidance가 주요 정책 수단으로 부상 → path factor 분석의 중요성 입증; [[Eggertsson & Woodford (2003) — The Zero Bound on Interest Rates and Optimal Monetary Policy]]의 이론 실증

---

## 11. Asset-Price Implications

**Bonds**
- [논문 직접] Path factor → 2년, 5년 국채 금리에 강한 영향; 장기 금리도 유의미한 반응
- [논문 직접] Target factor → 초단기 금리 집중; path factor → 중장기 수익률 곡선 이동

**Equities**
- [논문 직접] Path factor도 주가에 유의미한 영향: 미래 정책 경로 상향 → 주가 하락 압력
- [추론] Forward guidance 완화 (path factor 음수) → 주가 상승 (할인율 기대 경로 하락)

**FX**
- [추론] Path factor 상승 (긴축 forward guidance) → 달러 강세 (미래 금리 차익 기대)

**Credit**
- [추론] Path factor가 중장기 금리에 영향 → 기업 대출 금리·채권 발행 비용에 파급

> 반드시 [논문에서 직접 주장한 내용]과 [우리의 추론]을 구분한다.

---

## 12. Falsification Conditions

**What would confirm the hypothesis?**
- Path factor가 장기 금리에 target factor보다 독립적이고 유의미한 영향
- 발표문만 변화하고 금리 동결 시에도 자산 가격이 유의미하게 반응

**What would falsify the hypothesis?**
- 두 요인으로 분해했을 때 path factor가 금리 곡선 설명에 기여 없음
- 발표문이 금리 결정 이상의 독립적 정보 없음

**Variables to monitor**
- FOMC 발표 전후 30분 창 금리 변화; Eurodollar futures 곡선 이동; 주가·환율 반응

---

## 13. Contradictory / Alternative Literature

**Supporting Papers**
- Gürkaynak, Sack & Swanson (2007): Eurodollar futures로 정책 기대 측정 확장
- Nakamura & Steinsson (2018): 정보 효과 통제 후에도 path factor 유의미

**Contradictory Papers**
- [[Miranda-Agrippino & Ricco (2021) — The Transmission of Monetary Policy Shocks]]: 정보 효과 (Greenbook 통제)로 표준 surprise 측정의 편향 지적; path factor도 정보 효과 포함 가능성

---

## 14. Connections to Other Papers

**SUPPORTS**
- [[Eggertsson & Woodford (2003) — The Zero Bound on Interest Rates and Optimal Monetary Policy]]: ZLB에서 forward guidance(path factor) 실증
- [[2005 What Explains the Stock Market's Reaction to Federal Reserve Policy (Bernanke & Kuttner)]]: 단일 surprise → 두 요인으로 확장

**EXTENDS**
- Kuttner (2001): 당월 futures만 사용 → 다수 선물 + 요인 모형으로 확장

**APPLIES**
- 중앙은행 커뮤니케이션 효과 측정; QE·forward guidance의 시장 효과 분석; 중앙은행 발표문 감정 분석과 연결

---

## 15. Zettelkasten Atomic Notes

### ZK Note 1
**Claim:** FOMC 통화 정책 surprise는 두 개의 독립 요인 — target factor(현재 결정)와 path factor(미래 경로) — 으로 분해된다.
**Mechanism:** 여러 만기의 Fed futures 변화를 PCA → 두 요인이 FOMC 주변 분산 대부분 설명; 요인 회전으로 target/path 해석 부여
**Evidence:** [직접] 1991-2004 고빈도 데이터; 두 요인이 cumulative variance의 90% 이상 설명
**Implication:** 단일 surprise measure는 정보 손실; 두 요인 분해가 통화 정책의 현재 결정 vs. 미래 의도를 구분하는 핵심 도구
**Connected Notes:** [[2007 Market-Based Measures of Monetary Policy Expectations (Gürkaynak, Sack & Swanson)]], [[Miranda-Agrippino & Ricco (2021) — The Transmission of Monetary Policy Shocks]]

### ZK Note 2
**Claim:** 연준의 발표문(forward guidance)이 금리 결정과 독립적으로 자산 가격을 움직인다.
**Mechanism:** Path factor가 target factor와 직교화된 후에도 장기 금리·주가에 유의미한 영향 → 발표문이 독립 정보 포함
**Evidence:** [직접] 1999년 이후 명시적 forward guidance 도입 사례에서 path factor의 영향력 증가 확인
**Implication:** "말도 행동이다": 중앙은행 발표문이 금리 결정만큼 중요한 정책 도구; 커뮤니케이션 정책이 통화 정책 자체임
**Connected Notes:** [[Eggertsson & Woodford (2003) — The Zero Bound on Interest Rates and Optimal Monetary Policy]], [[2005 What Explains the Stock Market's Reaction to Federal Reserve Policy (Bernanke & Kuttner)]]

### ZK Note 3
**Claim:** ZLB에서 target factor가 0에 고정되면 path factor (forward guidance)가 유일한 통화 정책 수단이 된다.
**Mechanism:** 명목 금리 하한 → target factor 분산 없음 → path factor만 남음; 연준의 "low for long" 공약이 중장기 금리를 낮춰 수요 자극
**Evidence:** [추론] 2008-2015 ZLB 기간 Fed forward guidance의 효과; Swanson(2021) ZLB 기간 데이터로 직접 확인
**Implication:** ZLB 이론([[Eggertsson & Woodford (2003) — The Zero Bound on Interest Rates and Optimal Monetary Policy]])과 실증의 연결; "lower for longer" 약속의 시장 기반 효과 측정 가능
**Connected Notes:** [[Eggertsson & Woodford (2003) — The Zero Bound on Interest Rates and Optimal Monetary Policy]], [[Woodford (1995) — Price-Level Determinacy Without Control of a Monetary Aggregate]]

---

## 16. One-Sentence Takeaway

이 논문을 한 문장으로 기억한다면: **연준이 금리를 바꾸지 않아도 "앞으로 금리를 오래 유지하겠다"는 말 한마디가 장기 금리와 주가를 실제로 움직인다 — 말(forward guidance)도 통화 정책이다.**

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
