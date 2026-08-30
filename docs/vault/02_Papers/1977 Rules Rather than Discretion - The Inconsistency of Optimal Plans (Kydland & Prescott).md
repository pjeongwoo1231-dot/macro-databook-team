---
title: Rules Rather than Discretion - The Inconsistency of Optimal Plans
type: paper
journal: Journal of Political Economy, Vol. 85, No. 3, pp. 473-492
date: 1977
author: Finn E. Kydland, Edward C. Prescott
created: 2026-08-12
updated: 2026-08-12
status: draft
verification: none
reliability: academic
verified: "❌ 원문 미대조. 카카오톡 수신 노트(2026-08-12 임포트)를 볼트 규약으로 정규화한 것 — 수치·표현은 원문 확보 후 재검증 필요"
source_file: 없음 (외부 작성 노트 수신)
tags: [type/paper, domain/policy, domain/inflation, method/동태적최적화, flag/unverified]
concepts: [time-inconsistency, discretion, commitment, inflation-bias, policy-rule]
import_origin: 카카오톡 수신 — Macro Paper Notes / 원본 파일명 'Kydland & Prescott (1977) — Rules Rather than Discretion.md'
---
> ⚠ **원문 미대조 노트다.** 외부에서 작성된 것을 수신해 볼트 규약으로 정규화만 했다.
> 이 볼트의 [[원문검증 논문 MOC]] 기준을 통과하지 않았으므로 **제텔로 분해하지 않았고, 수치를 인용하지 않는다.**
> **단 2026-08-21 개정으로 「① 명제 층위」 인용은 허용된다** — 교과서적 정설을 수치 없이 인용할 때에 한하며,
> 인용 지점에 "원문 미대조"를 병기한다. → [[원문검증 논문 MOC]] 「인용 규칙 개정」
> 원문 확보 후 `status: verified`로 갱신한다.

﻿---
tags:
  - macro/monetary-policy
  - time-inconsistency
  - rules-vs-discretion
  - inflation-bias
  - dynamic-inconsistency
aliases:
  - "Kydland Prescott 1977"
  - "Rules Rather than Discretion"
  - "Time Inconsistency"
year: 1977
author: "Kydland & Prescott"
---

# Rules Rather than Discretion

## 1. Bibliographic Information

- **Title:** Rules Rather than Discretion: The Inconsistency of Optimal Plans
- **Authors:** Finn E. Kydland, Edward C. Prescott
- **Year:** 1977
- **Journal / Working Paper:** Journal of Political Economy, Vol. 85, No. 3, pp. 473-492
- **Research Field:** Monetary Policy, Public Economics, Game Theory
- **Keywords:** time inconsistency, dynamic inconsistency, inflation bias, precommitment, rules vs. discretion, optimal policy, Ramsey problem

### One-Sentence Thesis
이 논문은 **합리적 기대를 가진 민간과 정책 당국의 전략적 상호작용**에서 **시간 비일관성(time inconsistency)** 이 발생하여 **재량적 정책 하에서 항상 사회 후생 열위의 인플레이션 편의가 초래**됨을 보여준다.

---

## 2. Research Question

- **Question 1:** 왜 최적 계획(optimal plan)을 시간이 지남에 따라 지속적으로 실행하는 것이 어려운가?
- **Question 2:** 재량적 통화 정책이 왜 사회 최적보다 열위인가?

---

## 3. Literature Gap

**Existing Literature**
- 표준 경제학: 재량적 정책이 최적 — 각 시점에서 최적화
- Ramsey (1927): 조세 이론에서 최적 계획 개념 도입

**Limitation**
- 민간의 기대와 전략적 반응 무시; 사전(ex ante) 약속과 사후(ex post) 최적화 차이 간과

**Contribution of This Paper**
- 시간 비일관성 개념의 정립; 게임이론 적용으로 재량 정책의 구조적 열위 증명; 통화 정책뿐 아니라 특허, 조세, 치수 등 광범위한 정책 영역에 적용

---

## 4. Core Mechanism

```
Cause / Shock: 재량적 중앙은행이 매 기간 최적화 (실업을 u* 이하로 낮추려는 유인)
      ↓
1st-order Effect: 민간이 중앙은행의 인플레이션 유인을 예측 → 높은 기대 인플레이션 형성
      ↓
2nd-order Effect: 높은 pi^e 상황에서 중앙은행의 최적 대응은 실제로 높은 인플레이션 생산
      ↓
3rd-order Effect: Nash 균형: 높은 인플레이션 + 자연 실업률 동시 달성 → Pareto-열위
      ↓
Welfare Loss: 인플레이션 비용 발생 + 고용 목표 미달 — 사회 후생 손실 (inflation bias)
```

**Economic Logic**
- 사전 약속 균형(Ramsey): 낮은 인플레이션 + 자연 실업률 → 사회 최적
- 재량 균형(Nash): 높은 인플레이션 + 자연 실업률 → 사회 열위
- 약속 가능하면 Pareto 개선 — 사전 약속의 가치 존재

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

**Primary Shock:** 정책 체제(policy regime)의 재량성 — 중앙은행의 동태적 최적화 충격

---

## 6. Transmission Mechanism

```
Shock: 재량적 중앙은행의 인플레이션 생산 유인
  ↓
Transmission Channel: 합리적 기대 → 민간이 기대 인플레이션 즉각 조정
  ↓
Intermediate Variables: 높은 pi^e → 임금·가격 설정에 반영
  ↓
Real Economy: 중앙은행이 높은 pi^e 상황에서 실질 균형 달성하려면 실제 pi도 높여야
  ↓
Equilibrium: 인플레이션 편의 = lambda*(k-1) (k: 목표 고용 초과; lambda: 고용 가중치)
```

---

## 7. Key Variables

**Macroeconomic**
- pi (인플레이션), pi^e (기대), u (실업), u* (자연실업률), u_target (목표 실업률 < u*)
- lambda (중앙은행 고용 목표 가중치), k = u*/u_target (초과 고용 목표 배율)
- 손실함수: L = pi^2/2 + lambda*(u - k*u*)^2

**Financial**
- [추론] 인플레이션 위험 프리미엄: 재량 체제 → 더 높은 장기 채권 금리

**Leading / Coincident / Lagging**
- 기대 인플레이션: leading (즉각 반응)
- 실제 인플레이션: coincident

---

## 8. Empirical Strategy

- **Data:** 이론 논문 (수학적 모형)
- **Method:** 동태 프로그래밍; 게임이론 (Stackelberg game); 비교 정태
- **Main Model:** 민간의 Phillips Curve + 중앙은행 손실함수의 게임

**Correlation or Causality?**
- 이론 논증; 이후 Barro-Gordon (1983)이 게임이론으로 명시화; Walsh(2003) 교과서로 정형화

---

## 9. Main Findings

1. [논문 직접] 재량적 최적화는 시간 비일관적: 사전에 발표한 최적 계획이 사후에 이행할 유인이 없음
2. [논문 직접] 재량 균형은 Pareto-열위: 규칙(precommitment)보다 항상 나쁜 결과
3. [논문 직접] 인플레이션 편의(inflation bias) 존재: 사회적 최적 인플레이션보다 높은 균형 인플레이션
4. [논문 직접] 통화 정책뿐 아니라 특허법, 치수 정책, 자본 조세 등 광범위한 정책에 적용
5. 해결책: 헌법적 제약, 독립적 중앙은행, 보수적 중앙은행장 (Rogoff 1985)

---

## 10. Regime Dependency

**When is the mechanism stronger (inflation bias)?**
- 중앙은행의 고용 목표 가중치(lambda)가 클수록
- 자연실업률과 목표 실업률의 괴리가 클수록
- 민간의 합리적 기대 형성 능력이 강할수록

**When is the mechanism weaker?**
- 명확한 인플레이션 목표와 높은 중앙은행 독립성: 평판 메커니즘 작동
- 보수적 중앙은행장 (lambda 낮음): Rogoff(1985) 해결책
- 수익률 연동 계약(Svensson 1997): 인플레이션 페널티로 유인 해결

**Does the conclusion change across regimes?**
- 인플레이션 목표제(IT) 도입 이후: 명시적 약속 메커니즘으로 inflation bias 실질적 해소; 그러나 구조적 유인은 여전히 존재

---

## 11. Asset-Price Implications

**Bonds**
- [논문 간접] 재량적 중앙은행 → 높은 인플레이션 기대 위험 프리미엄 → 장기 채권 금리 상승
- [추론] 규칙(IT) 도입 → 인플레이션 기대 안정 → 장기 채권 금리 하락, 변동성 감소

**Equities**
- [추론] 인플레이션 편의 환경 → 주식 실질 가치 불확실성 증가; IT 도입 → 불확실성 감소 → 밸류에이션 상승

**Commodities**
- [추론] 인플레이션 편의 → 실물 자산(금) 수요 증가 → 가격 상승

**Credit**
- [추론] 높은 인플레이션 불확실성 → 장기 고정금리 대출 감소; 변동금리 증가

> 반드시 [논문에서 직접 주장한 내용]과 [우리의 추론]을 구분한다.

---

## 12. Falsification Conditions

**What would confirm the hypothesis?**
- 독립성 낮은 중앙은행 국가에서 높은 인플레이션 편의 관찰 (1970년대 경험)
- 인플레이션 타겟팅 도입 후 인플레이션 기대 안정화 및 인플레이션 하락

**What would falsify the hypothesis?**
- 재량적 중앙은행이 일관적으로 낮은 인플레이션 달성 (평판 없이); 민간이 합리적 기대 미형성

**Variables to monitor**
- 인플레이션 기대 (장기 survey, TIPS), 중앙은행 독립성 지수, 실현 인플레이션 vs. 목표

---

## 13. Contradictory / Alternative Literature

**Supporting Papers**
- [[1983 Rules Discretion and Reputation in a Model of Monetary Policy (Barro & Gordon)]]: 반복 게임으로 명시화
- Walsh (1995): 인플레이션 페널티 계약으로 time inconsistency 해결

**Contradictory Papers**
- Svensson (1997): 유연한 인플레이션 타겟팅이 재량의 장점 유지 가능 주장
- 행동 경제학: 중앙은행이 실제로 비합리적 기대를 가진 민간과 상호작용 시 이론 약화

---

## 14. Connections to Other Papers

**SUPPORTS**
- [[1968 The Role of Monetary Policy (Friedman)]]: 자연실업률 기반 인플레이션 편의
- [[1993 Discretion versus Policy Rules in Practice (Taylor)]]: 실용적 규칙 제안

**EXTENDS**
- [[1976 Econometric Policy Evaluation - A Critique (Lucas)]]: 정책 파라미터 불안정성 → 시간 비일관성으로 확장

**APPLIES**
- 중앙은행 독립성 설계; 인플레이션 목표제(IT); 재정 준칙

---

## 15. Zettelkasten Atomic Notes

### ZK Note 1
**Claim:** 최적 정책은 시간 비일관적이다 — 사전에 선언한 최적 계획이 사후에는 이탈 유인이 생긴다.
**Mechanism:** 민간이 계획을 믿고 행동 → 중앙은행은 이제 다른 최적화 문제에 직면 → 이탈이 최적; 약속의 credibility 문제
**Evidence:** [직접] 수학적 증명; 특허법(사후 독점 이윤 허용 vs. 사전 혁신 유인), 치수 정책(사후 구조 vs. 사전 범람원 정착 억제) 예시
**Implication:** 모든 정책 설계에서 사전 약속 메커니즘 필요; 규칙·독립 기관·헌법적 제약의 경제적 근거
**Connected Notes:** [[1983 Rules Discretion and Reputation in a Model of Monetary Policy (Barro & Gordon)]], [[1976 Econometric Policy Evaluation - A Critique (Lucas)]]

### ZK Note 2
**Claim:** 재량 균형 인플레이션은 사회 최적보다 항상 높다 (인플레이션 편의).
**Mechanism:** 손실함수 L = pi^2 + lambda*(u - k*u*)^2 최소화 → 고용 목표(k*u* < u*)로 인해 항상 일부 인플레이션 생산이 최적; 민간이 예측하여 pi^e 올림 → 균형에서 높은 pi, 자연 u
**Evidence:** [직접] 수학적 도출; Barro-Gordon(1983)이 실증 근거 추가
**Implication:** 중앙은행에 고용 의무(dual mandate) 부여 시 인플레이션 편의 심화; 물가안정 단일 목표(ECB 모델)의 장점
**Connected Notes:** [[1999 The Science of Monetary Policy - A New Keynesian Perspective (Clarida, Galí & Gertler)]], [[1983 Rules Discretion and Reputation in a Model of Monetary Policy (Barro & Gordon)]]

### ZK Note 3
**Claim:** 시간 비일관성은 통화 정책에만 국한되지 않고 조세, 무역, 규제 등 모든 정책 영역에 적용된다.
**Mechanism:** 어떤 정책이든 민간의 사전 투자·결정에 의존하는 순간, 정부는 사후적으로 이탈 유인 보유
**Evidence:** [직접] 특허법 예시: 혁신 후 특허 독점 보장 파기 유인; 자본 조세: 투자 결정 후 높은 세율 부과 유인
**Implication:** 제도·규칙·국제 협약이 정부 재량을 제한하는 경제적 이유 — 단순 행정 효율이 아니라 약속 credibility 확보
**Connected Notes:** [[1982 Time to Build and Aggregate Fluctuations (Kydland & Prescott)]]

---

## 16. One-Sentence Takeaway

이 논문을 한 문장으로 기억한다면: **중앙은행이 매 순간 최선을 다해 결정하면 민간이 그것을 예측하여 인플레이션 기대를 올리고, 결국 인플레이션만 높아지는 함정에 빠진다 — 좋은 의도의 재량은 나쁜 결과를 낳는다.**

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
