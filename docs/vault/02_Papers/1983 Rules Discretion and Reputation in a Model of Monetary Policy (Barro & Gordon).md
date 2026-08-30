---
title: Rules Discretion and Reputation in a Model of Monetary Policy
type: paper
journal: Journal of Monetary Economics, Vol. 12, No. 1, pp. 101-121
date: 1983
author: Robert J. Barro, David B. Gordon
created: 2026-08-12
updated: 2026-08-12
status: draft
verification: none
reliability: academic
verified: "❌ 원문 미대조. 카카오톡 수신 노트(2026-08-12 임포트)를 볼트 규약으로 정규화한 것 — 수치·표현은 원문 확보 후 재검증 필요"
source_file: 없음 (외부 작성 노트 수신)
tags: [type/paper, domain/policy, domain/inflation, method/반복게임, method/내시균형, flag/unverified]
concepts: [inflation-bias, reputation, trigger-strategy, time-inconsistency, precommitment]
import_origin: 카카오톡 수신 — Macro Paper Notes / 원본 파일명 'Barro & Gordon (1983) — Rules, Discretion and Reputation in a Model of Monetary Policy.md'
---
> ⚠ **원문 미대조 노트다.** 외부에서 작성된 것을 수신해 볼트 규약으로 정규화만 했다.
> 이 볼트의 [[원문검증 논문 MOC]] 기준을 통과하지 않았으므로 **제텔로 분해하지 않았고, 수치를 인용하지 않는다.**
> **단 2026-08-21 개정으로 「① 명제 층위」 인용은 허용된다** — 교과서적 정설을 수치 없이 인용할 때에 한하며,
> 인용 지점에 "원문 미대조"를 병기한다. → [[원문검증 논문 MOC]] 「인용 규칙 개정」
> 원문 확보 후 `status: verified`로 갱신한다.

﻿---
tags:
  - macro/monetary-policy
  - inflation-bias
  - reputation
  - game-theory
  - time-inconsistency
aliases:
  - "Barro Gordon 1983"
  - "Rules Discretion Reputation"
year: 1983
author: "Barro & Gordon"
---

# Rules, Discretion and Reputation in a Model of Monetary Policy

## 1. Bibliographic Information

- **Title:** Rules, Discretion and Reputation in a Model of Monetary Policy
- **Authors:** Robert J. Barro, David B. Gordon
- **Year:** 1983
- **Journal / Working Paper:** Journal of Monetary Economics, Vol. 12, No. 1, pp. 101-121
- **Research Field:** Monetary Policy, Game Theory
- **Keywords:** inflation bias, reputation, Nash equilibrium, trigger strategy, repeated game, time inconsistency, precommitment

### One-Sentence Thesis
이 논문은 **중앙은행과 민간의 반복 게임**에서 **평판 메커니즘(trigger strategy)**이 약속 없이도 낮은 인플레이션 달성을 지지할 수 있지만, **일회성 Nash 균형은 항상 인플레이션 편의를 내재**함을 보여준다.

---

## 2. Research Question

- **Question 1:** 재량적 통화 정책의 Nash 균형 인플레이션은 얼마인가?
- **Question 2:** 평판(reputation)이 시간 비일관성 문제를 해결할 수 있는가?

---

## 3. Literature Gap

**Existing Literature**
- [[1977 Rules Rather than Discretion - The Inconsistency of Optimal Plans (Kydland & Prescott)]]: 규칙의 우월성 논증; 단, 어떻게 규칙에 약속하는가 불명확
- Barro-Gordon (1983a, JME companion): 단순 모형 분석

**Limitation**
- 일회성 게임 분석; 반복 게임에서의 평판 동학 미포함; Nash 균형 인플레이션의 정량적 도출 부재

**Contribution of This Paper**
- 명시적 Nash 균형 인플레이션 도출; 반복 게임의 평판 균형 분석; 규칙(commitment) - 재량(discretion) - 평판(reputation)의 3가지 정책 체제 비교

---

## 4. Core Mechanism

```
Cause / Shock: 중앙은행의 재량적 정책 (일회성 게임)
      ↓
Nash Equilibrium: pi_bar = b*(k-1) (b: Phillips Curve 기울기, k: 고용 목표 초과배율)
      ↓
Repeated Game: 중앙은행이 미래 평판 손실 비용 고려 (무한 반복 게임)
      ↓
Trigger Strategy: 중앙은행 이탈 → 민간이 영구적으로 높은 기대 인플레이션 부과
      ↓
Reputation Equilibrium: 충분히 낮은 할인율 하에서 낮은 인플레이션 유지 가능
```

**Economic Logic**
- 이탈 이익(cheating gain) < 평판 손실(reputation loss) → 낮은 인플레이션 지속
- 균형: 세 종류의 pi — 약속(0), 평판(0 < pi < pi_bar), 재량(pi_bar)

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

**Primary Shock:** 정책 신뢰성 충격 (credibility shock) — 중앙은행의 이탈·평판 훼손

---

## 6. Transmission Mechanism

```
Shock: 중앙은행의 인플레이션 유인 (고용 목표 달성 압력)
  ↓
Transmission Channel: 합리적 기대 민간이 인플레이션 예측 → pi^e 결정
  ↓
Intermediate Variables: 중앙은행 최적 대응: pi*(pi^e) 함수
  ↓
Real Economy: Nash 균형: pi = pi^e = pi_bar (인플레이션 편의)
  ↓
Reputation Dynamics: 반복 게임에서 미래 처벌 위협 → 균형 pi 하락 가능
```

---

## 7. Key Variables

**Macroeconomic**
- pi (인플레이션), pi^e (기대), u (실업), b (Phillips Curve 기울기)
- k (목표 고용 초과: k > 1 → 고용 목표가 자연률 이상), lambda (고용 가중치)
- Nash 균형: pi_bar = lambda*b*(k-1) / (1 + lambda*b^2)
- 할인인자 theta: 평판 메커니즘의 작동 조건

**Financial**
- [추론] 장기 채권 인플레이션 위험 프리미엄: 재량 체제 vs. 규칙 체제

**Leading / Coincident / Lagging**
- 기대 인플레이션: leading; 중앙은행 신뢰도 지표: coincident

---

## 8. Empirical Strategy

- **Data:** 이론 논문 (게임이론 모형)
- **Method:** Nash 균형 도출; 반복 게임 분석; trigger strategy 조건 도출
- **Main Model:** L_t = (pi_t)^2/2 + lambda*(u_t - k*u*)^2; Phillips Curve: u_t = u* - b*(pi_t - pi^e_t)

**Correlation or Causality?**
- 이론 논증; 이후 실증: 중앙은행 독립성과 인플레이션 간 관계 (Alesina & Summers 1993)

---

## 9. Main Findings

1. [논문 직접] 재량 Nash 균형 인플레이션: pi_bar = lambda*b*(k-1) — 고용 목표 초과분과 Phillips Curve 기울기에 비례
2. [논문 직접] 평판 균형이 지속되는 조건: 이탈 이익 < 미래 평판 손실의 현재 가치
3. [논문 직접] 평판 균형은 다양한 pi 수준 지지 가능 (복수 균형) → 조정(coordination) 문제 발생
4. [논문 직접] 가장 낮은 인플레이션 균형은 약속(commitment) 균형; 가장 높은 것은 Nash 재량 균형
5. 제도 설계 함의: 독립적 중앙은행, 보수적 중앙은행장(Rogoff 1985), IT 체제

---

## 10. Regime Dependency

**When is the reputation mechanism stronger?**
- 중앙은행의 기간(tenure)이 길수록; 할인인자(theta) 높을수록
- 인플레이션 이탈이 즉각 관찰 가능할 때 (투명성 높을 때)
- 이탈에 대한 처벌이 강하고 신뢰할 수 있을 때

**When is the mechanism weaker?**
- 정치적 압력; 선거 주기; 중앙은행 수장 잦은 교체 (단기 horizon)
- 경제적 위기: 단기 고용 유인이 매우 클 때

**Does the conclusion change across regimes?**
- IT 체제: 명시적 인플레이션 목표가 평판 메커니즘을 공식화하여 강화; 그러나 복수 균형 문제는 제도 설계로 해결

---

## 11. Asset-Price Implications

**Bonds**
- [논문 간접] 낮은 평판 중앙은행 → 높은 기대 인플레이션 → 장기 채권 금리에 위험 프리미엄 반영
- [추론] 중앙은행 신뢰도 훼손 사건(예: 예상치 못한 이탈) → 인플레이션 기대 불안정 → 채권 금리 급등

**Equities**
- [추론] 인플레이션 편의 환경 → 불확실성 증가 → 주식 위험 프리미엄 상승 → P/E 비율 하락

**FX**
- [추론] 낮은 평판 중앙은행 국가 → 환율 변동성 높음; 신뢰도 상실 → 통화 가치 절하 압력

**Commodities**
- [추론] 인플레이션 편의 우려 → 금·원자재 인플레이션 헤지 수요 증가

> 반드시 [논문에서 직접 주장한 내용]과 [우리의 추론]을 구분한다.

---

## 12. Falsification Conditions

**What would confirm the hypothesis?**
- 독립성 낮은 중앙은행 국가에서 일관되게 높은 인플레이션 편의 관찰
- IT 도입 후 장기 인플레이션 하락 및 기대 인플레이션 안정화

**What would falsify the hypothesis?**
- 평판 없이도 재량 중앙은행이 일관적으로 낮은 인플레이션 달성
- 반복 게임 없이도 약속 균형이 자발적으로 달성되는 사례

**Variables to monitor**
- 중앙은행 독립성 지수(CBI), 장기 인플레이션 기대 survey, 실현 인플레이션 vs. 목표

---

## 13. Contradictory / Alternative Literature

**Supporting Papers**
- Alesina & Summers (1993): 중앙은행 독립성과 낮은 인플레이션 간 강한 상관관계 실증
- Rogoff (1985): 보수적 중앙은행장으로 lambda 낮춰 인플레이션 편의 해결

**Contradictory Papers**
- Svensson (1997): 유연한 IT — 재량적 요소 유지하면서도 낮은 인플레이션 달성 가능 주장
- 행동 경제학: 민간의 비합리적 기대 → 평판 메커니즘 약화

---

## 14. Connections to Other Papers

**SUPPORTS**
- [[1977 Rules Rather than Discretion - The Inconsistency of Optimal Plans (Kydland & Prescott)]]: 시간 비일관성 이론의 게임이론적 완성
- [[1993 Discretion versus Policy Rules in Practice (Taylor)]]: 실증적 규칙의 근거

**EXTENDS**
- [[1968 The Role of Monetary Policy (Friedman)]]: 자연실업률 + 기대 → 게임이론 균형으로 확장

**APPLIES**
- 중앙은행 독립성 제도 설계; 인플레이션 타겟팅의 이론적 기초

---

## 15. Zettelkasten Atomic Notes

### ZK Note 1
**Claim:** 재량 Nash 균형 인플레이션은 0이 아니라 lambda*b*(k-1) > 0이다.
**Mechanism:** 중앙은행 손실함수 최적화 → FOC: pi = lambda*b*(u* - u_t); Phillips Curve 대입 → 균형 pi = lambda*b*(k-1)/(1+lambda*b^2)
**Evidence:** [직접] 수학적 도출; 1970년대 미국 경험적 패턴과 정성적 일치
**Implication:** 인플레이션 편의 크기는 관측 가능한 파라미터로 예측 가능; 고용 가중치(lambda), 목표 초과분(k-1), 필립스 기울기(b)가 핵심
**Connected Notes:** [[1977 Rules Rather than Discretion - The Inconsistency of Optimal Plans (Kydland & Prescott)]], [[1999 The Science of Monetary Policy - A New Keynesian Perspective (Clarida, Galí & Gertler)]]

### ZK Note 2
**Claim:** 평판(reputation)은 명시적 약속 없이도 낮은 인플레이션 달성 가능한 메커니즘이다.
**Mechanism:** 반복 게임 + trigger strategy: 이탈 발각 → 영구적 Nash 균형 인플레이션 처벌; 이탈 이익 < 처벌 현재 가치 → 준수 유인
**Evidence:** [직접] 이론 도출; 조건: theta > 이탈 이익 / (이탈 이익 + 평판 손실)
**Implication:** 독립적 중앙은행의 신뢰도가 구축되면 명시적 규칙 없이도 낮은 인플레이션 가능; 그러나 복수 균형 조정 문제가 남음
**Connected Notes:** [[1983 Rules Discretion and Reputation in a Model of Monetary Policy (Barro & Gordon)]], [[1993 Discretion versus Policy Rules in Practice (Taylor)]]

### ZK Note 3
**Claim:** 평판 균형은 복수 균형이므로 조정(coordination) 문제가 발생한다 — 제도적 해결이 필요하다.
**Mechanism:** 이탈 이익 < 처벌 현재 가치를 만족하는 모든 pi 수준이 균형 → 어떤 균형이 선택될지 모형이 결정 못 함
**Evidence:** [직접] 게임이론 분석; 국가별 인플레이션 차이: 동일 independent CB 이론에도 국가별 큰 차이
**Implication:** 단순 반복 게임만으로 충분치 않음; 명시적 IT, 물가 준칙, 국제 협약 등 조정 장치 필요; 조정 장치의 역할: 균형 선택(equilibrium selection) + 처벌의 credibility 강화
**Connected Notes:** [[Eggertsson & Woodford (2003) — The Zero Bound on Interest Rates and Optimal Monetary Policy]], [[1993 Discretion versus Policy Rules in Practice (Taylor)]]

---

## 16. One-Sentence Takeaway

이 논문을 한 문장으로 기억한다면: **중앙은행이 언제나 눈앞의 최선을 선택하면 민간은 이를 예측하여 인플레이션 기대를 높이고, 결국 인플레이션만 높은 나쁜 균형에 빠진다 — 규칙이든 평판이든 약속의 신뢰성이 통화 정책의 핵심이다.**

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
