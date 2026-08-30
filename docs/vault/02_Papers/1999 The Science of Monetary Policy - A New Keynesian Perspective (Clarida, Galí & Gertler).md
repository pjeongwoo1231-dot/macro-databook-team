---
title: The Science of Monetary Policy - A New Keynesian Perspective
type: paper
journal: Journal of Economic Literature, Vol. 37, No. 4, pp. 1661-1707
date: 1999
author: Richard Clarida, Jordi Galí, Mark Gertler
created: 2026-08-12
updated: 2026-08-12
status: draft
verification: none
reliability: academic
verified: "❌ 원문 미대조. 카카오톡 수신 노트(2026-08-12 임포트)를 볼트 규약으로 정규화한 것 — 수치·표현은 원문 확보 후 재검증 필요"
source_file: 없음 (외부 작성 노트 수신)
tags: [type/paper, domain/policy, domain/inflation, region/us, method/뉴케인지언DSGE, flag/unverified]
concepts: [NK-IS, NKPC, Taylor-rule, divine-coincidence, natural-rate, optimal-policy]
import_origin: 카카오톡 수신 — Macro Paper Notes / 원본 파일명 'Clarida, Galí & Gertler (1999) — The Science of Monetary Policy.md'
---
> ⚠ **원문 미대조 노트다.** 외부에서 작성된 것을 수신해 볼트 규약으로 정규화만 했다.
> 이 볼트의 [[원문검증 논문 MOC]] 기준을 통과하지 않았으므로 **제텔로 분해하지 않았고, 수치를 인용하지 않는다.**
> **단 2026-08-21 개정으로 「① 명제 층위」 인용은 허용된다** — 교과서적 정설을 수치 없이 인용할 때에 한하며,
> 인용 지점에 "원문 미대조"를 병기한다. → [[원문검증 논문 MOC]] 「인용 규칙 개정」
> 원문 확보 후 `status: verified`로 갱신한다.

﻿---
tags:
  - macro/monetary-policy
  - new-keynesian
  - optimal-policy
  - nkpc
  - forward-looking
aliases:
  - "Clarida Gali Gertler 1999"
  - "Science of Monetary Policy"
  - "CGG 1999"
year: 1999
author: "Clarida, Galí & Gertler"
---

# The Science of Monetary Policy

## 1. Bibliographic Information

- **Title:** The Science of Monetary Policy: A New Keynesian Perspective
- **Authors:** Richard Clarida, Jordi Galí, Mark Gertler
- **Year:** 1999
- **Journal / Working Paper:** Journal of Economic Literature, Vol. 37, No. 4, pp. 1661-1707
- **Research Field:** Monetary Economics, New Keynesian Macroeconomics
- **Keywords:** New Keynesian model, NK IS curve, NKPC, Taylor Rule, optimal monetary policy, Divine Coincidence, forward-looking, natural rate

### One-Sentence Thesis
이 논문은 **미시적 최적화에 기반한 New Keynesian 3-방정식 모형**이 **최적 통화 정책의 이론적 기초**를 제공하며, 인플레이션 안정화가 동시에 산출 갭 안정화를 달성하는 **Divine Coincidence**를 도출함을 보여준다.

---

## 2. Research Question

- **Question 1:** 미시적 최적화에 기반한 거시 모형에서 최적 통화 정책은 무엇인가?
- **Question 2:** 인플레이션 안정화와 산출 갭 안정화 간 트레이드오프가 존재하는가?

---

## 3. Literature Gap

**Existing Literature**
- 기존 IS-LM 모형: 미시 기초 결여; 기대 외생적
- [[1993 Discretion versus Policy Rules in Practice (Taylor)]]: 경험적 규칙; 이론적 최적성 불명확

**Limitation**
- 기대의 역할과 forward-looking 행동을 통합한 최적 정책 프레임워크 부재

**Contribution of This Paper**
- 미시 기초 있는 NK 3-방정식 시스템; 최적 정책 도출; Taylor Principle 이론적 근거; Divine Coincidence 명명

---

## 4. Core Mechanism

```
Cause / Shock: 통화 정책 충격 또는 기술 충격 (자연 이자율 r^n 변동)
      ↓
1st-order Effect: NK IS Curve — x_t = E_t[x_{t+1}] - sigma*(i_t - E_t[pi_{t+1}] - r^n_t)
      ↓
2nd-order Effect: NK Phillips Curve — pi_t = beta*E_t[pi_{t+1}] + kappa*x_t
      ↓
3rd-order Effect: 최적 정책: 산출 갭 = 0이면 동시에 인플레이션 = 0 (Divine Coincidence)
      ↓
Real Economy: 공급 충격 없으면 pi 안정화 = x 안정화; 공급 충격 있으면 트레이드오프
```

**Economic Logic**
- NK IS: 기간 간 소비 최적화의 log-linear 근사; r^n = 자연 실질 이자율
- NKPC: Calvo 가격 결정 → 인플레이션은 기대 인플레이션 + 한계 비용(output gap)의 함수
- 최적 정책: natural rate 추적 (i → r^n) → x = 0 → pi = 0

---

## 5. Shock Classification

- [x] Demand Shock
- [x] Supply Shock
- [x] Monetary Shock
- [ ] Fiscal Shock
- [ ] Credit Shock
- [ ] Financial Shock
- [ ] Commodity Shock
- [x] Technology Shock
- [ ] Productivity Shock
- [ ] Trade Shock
- [ ] Capital Flow Shock
- [x] Expectation Shock

**Primary Shock:** 자연 이자율(r^n) 변동 — 기술 충격, 선호 충격으로 발생

---

## 6. Transmission Mechanism

```
Shock: 통화 정책 긴축 (i 인상)
  ↓
NK IS Channel: 실질 금리 상승 → 소비·투자 감소 → 산출 갭 음수
  ↓
NKPC Channel: 산출 갭 하락 → 인플레이션 감소 (kappa*x 항 감소)
  ↓
Expectation Channel: 기대 인플레이션 하락 (NKPC forward-looking) → 현재 인플레이션 추가 하락
  ↓
Real Economy: 인플레이션 목표 수렴; 산출 갭 자연률 복귀 (optimal policy)
```

---

## 7. Key Variables

**Macroeconomic**
- x_t (output gap), pi_t (인플레이션), i_t (명목 금리), r^n_t (자연 실질 이자율)
- beta (할인인자 ~0.99), sigma (소비 대체 탄력성 역수), kappa (NKPC 기울기)
- kappa = alpha*(1 - alpha)*(1 - alpha*beta) / alpha * (sigma + phi) (Calvo 모형 파라미터)

**Financial**
- 실질 금리 갭: i_t - E_t[pi_{t+1}] - r^n_t → 총수요 결정의 핵심
- [추론] 자산 가격: 명목 금리 경로가 장기 채권 가격 결정

**Leading / Coincident / Lagging**
- 기대 인플레이션: leading (NKPC의 forward-looking 항)
- 산출 갭: coincident
- 실현 인플레이션: coincident to lagging

---

## 8. Empirical Strategy

- **Data:** 이론 논문 (미시 기초 기반 모형 구축)
- **Method:** 동태 최적화 모형; Calvo 가격 결정; Ramsey optimal policy 도출
- **Main Model:** NK IS + NKPC + 정책 규칙

**Correlation or Causality?**
- 이론 논문; 실증 검증은 Clarida, Galí & Gertler (2000 AER) "Monetary Policy Rules and Macroeconomic Stability"

---

## 9. Main Findings

1. [논문 직접] NK 3-방정식 모형: IS Curve (forward-looking), NKPC (forward-looking), 통화 정책 규칙
2. [논문 직접] Divine Coincidence: 비용 충격(cost-push shock) 없으면 인플레이션 안정화 = 산출 갭 안정화 동시 달성
3. [논문 직접] 최적 정책: 자연 이자율(r^n) 추적; 중앙은행이 "natural rate of interest" 변동에 반응
4. [논문 직접] Taylor Principle의 이론적 근거: phi_pi > 1이어야 균형 유일 (determinacy)
5. [논문 직접] 공급 충격(cost-push) 존재 시 인플레이션-산출 갭 트레이드오프 → Flexible Price 목표에서 이탈 필요

---

## 10. Regime Dependency

**When is the mechanism stronger (Divine Coincidence)?**
- 공급 충격(cost-push) 없는 환경; 기술 충격이 주요 business cycle 원인

**When is Divine Coincidence break down?**
- [[Blanchard & Galí (2007) — Real Wage Rigidities and the New Keynesian Model]]: 실질 임금 경직성 → 공급 충격이 인플레이션-산출 갭 트레이드오프 유발
- Oil price shocks: cost-push 충격이 강한 경우

**Does the conclusion change across regimes?**
- ZLB에서: i 하한으로 자연 이자율 추적 불가 → 기대 채널(forward guidance)이 핵심 수단

---

## 11. Asset-Price Implications

**Bonds**
- [논문 직접] 최적 정책에서 자연 이자율 추적 → 단기 금리가 r^n 경로 따라감 → 장기 금리는 기대가설로 결정
- [추론] 공급 충격 시 인플레이션-산출 갭 트레이드오프 → 통화 정책 불확실성 증가 → 채권 프리미엄 상승

**Equities**
- [추론] 최적 정책 하에서 산출 갭 안정 → 기업 이익 변동성 감소 → 주식 위험 프리미엄 하락 (낮은 할인율)

**FX**
- [추론] 자연 이자율 추적 정책 → 국내외 금리차 안정 → 환율 변동성 감소

**Credit**
- [추론] 산출 갭 안정화 → 채무 불이행 위험 감소 → 크레딧 스프레드 축소

> 반드시 [논문에서 직접 주장한 내용]과 [우리의 추론]을 구분한다.

---

## 12. Falsification Conditions

**What would confirm the hypothesis?**
- 공급 충격 없는 환경에서 인플레이션 안정화 시 동시에 산출 안정화 달성
- Taylor Principle 위반 중앙은행에서 인플레이션 불안정

**What would falsify the hypothesis?**
- 공급 충격 없이도 인플레이션-산출 갭 트레이드오프 존재
- Taylor Principle 충족에도 불구한 인플레이션 불안정성

**Variables to monitor**
- 자연 이자율 추정값(r*), 산출 갭 추정, NKPC 기울기(kappa), Calvo parameter

---

## 13. Contradictory / Alternative Literature

**Supporting Papers**
- Woodford (2003): "Interest and Prices" — NK 이론 완성; 최적 정책의 완전한 기초
- Galí (2008): NK 교과서

**Contradictory Papers**
- [[Blanchard & Galí (2007) — Real Wage Rigidities and the New Keynesian Model]]: Divine Coincidence 비판 — 실질 임금 경직성으로 트레이드오프 발생
- HANK 모형: 이질적 행위자 → NK IS Curve의 집계 문제

---

## 14. Connections to Other Papers

**SUPPORTS**
- [[1993 Discretion versus Policy Rules in Practice (Taylor)]]: Taylor Rule의 이론적 최적성 기초 제공
- [[1977 Rules Rather than Discretion - The Inconsistency of Optimal Plans (Kydland & Prescott)]]: 규칙 기반 정책의 NK 이론 구현

**CONTRADICTED BY**
- [[Blanchard & Galí (2007) — Real Wage Rigidities and the New Keynesian Model]]: Divine Coincidence 붕괴
- [[Eggertsson & Woodford (2003) — The Zero Bound on Interest Rates and Optimal Monetary Policy]]: ZLB에서 최적 정책 변화

**EXTENDS**
- [[Christiano, Eichenbaum & Evans (2005) — Nominal Rigidities and the Dynamic Effects of a Shock to Monetary Policy]]: DSGE 실증으로 확장

---

## 15. Zettelkasten Atomic Notes

### ZK Note 1
**Claim:** NK 3-방정식 모형 (NK IS + NKPC + 정책 규칙)이 현대 중앙은행 통화 정책의 표준 분석 틀이다.
**Mechanism:** NK IS: 소비 최적화 → 수요; NKPC: Calvo 가격 결정 → 공급; 정책 규칙: 두 방정식을 닫는 세 번째 방정식
**Evidence:** [직접] 이론 도출; 이후 DSGE 모형의 공통 핵심 구조로 채택 (Fed, ECB, BOE 모델)
**Implication:** 이 3방정식을 이해하면 현대 거시 통화론의 95%를 이해 가능; 수식 암기보다 경제 논리 이해가 핵심
**Connected Notes:** [[Christiano, Eichenbaum & Evans (2005) — Nominal Rigidities and the Dynamic Effects of a Shock to Monetary Policy]], [[1993 Discretion versus Policy Rules in Practice (Taylor)]]

### ZK Note 2
**Claim:** Divine Coincidence: 공급 충격이 없으면 인플레이션 안정화가 동시에 산출 갭 안정화를 달성한다.
**Mechanism:** NKPC: pi_t = beta*E_t[pi_{t+1}] + kappa*x_t; cost-push shock 없으면 pi = 0 → x = 0 자동; 두 목표가 충돌 없음
**Evidence:** [직접] 이론 도출; 실증: 비용 충격 없는 기간 인플레이션-산출 동반 안정화
**Implication:** 공급 충격이 없는 환경에서 인플레이션 목표제(IT)가 두 가지 목표 동시 달성 가능한 이유; 그러나 2021-2022 공급 충격이 트레이드오프 노출
**Connected Notes:** [[Blanchard & Galí (2007) — Real Wage Rigidities and the New Keynesian Model]], [[Bernanke & Blanchard (2023) — What Caused the U.S. Pandemic-Era Inflation]]

### ZK Note 3
**Claim:** NKPC는 backward-looking(adaptive expectations)이 아니라 forward-looking이다.
**Mechanism:** pi_t = beta*E_t[pi_{t+1}] + kappa*x_t → 현재 인플레이션이 미래 기대 인플레이션의 함수; 기대 관리(expectation management)가 인플레이션 통제의 핵심
**Evidence:** [직접] Calvo 가격 결정 미시 기초; 실증: Galí & Gertler (1999 JME) — forward-looking 항이 통계적으로 유의
**Implication:** 인플레이션은 현재 경기만이 아니라 미래 경기 기대에 의존 → 중앙은행의 forward guidance가 핵심 정책 수단; 기대 고착이 인플레이션 통제의 핵심
**Connected Notes:** [[Eggertsson & Woodford (2003) — The Zero Bound on Interest Rates and Optimal Monetary Policy]], [[Hazell, Herreno, Nakamura & Steinsson (2022) — The Slope of the Phillips Curve Evidence from U.S. States]]

---

## 16. One-Sentence Takeaway

이 논문을 한 문장으로 기억한다면: **New Keynesian 모형에서 중앙은행이 인플레이션만 잘 통제하면 경기 안정화도 자동으로 달성된다 — 좋은 인플레이션 통제자가 곧 좋은 경기 안정화자이다 (공급 충격이 없는 한).**

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
