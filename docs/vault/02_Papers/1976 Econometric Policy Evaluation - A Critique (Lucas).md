---
title: Econometric Policy Evaluation - A Critique
type: paper
journal: Carnegie-Rochester Conference Series on Public Policy, Vol. 1, pp. 19-46. DOI/URL 10.1016/S0167-2231(76)80003-6
date: 1976
author: Robert E. Lucas Jr.
created: 2026-08-12
updated: 2026-08-12
status: draft
verification: none
reliability: academic
verified: "❌ 원문 미대조. 카카오톡 수신 노트(2026-08-12 임포트)를 볼트 규약으로 정규화한 것 — 수치·표현은 원문 확보 후 재검증 필요"
source_file: 없음 (외부 작성 노트 수신)
tags: [type/paper, domain/policy, method/계량모형비판, flag/unverified]
concepts: [Lucas-critique, deep-parameters, rational-expectations, structural-change, policy-invariance]
import_origin: 카카오톡 수신 — Macro Paper Notes / 원본 파일명 'Lucas (1976) — Econometric Policy Evaluation A Critique.md'
---
> ⚠ **원문 미대조 노트다.** 외부에서 작성된 것을 수신해 볼트 규약으로 정규화만 했다.
> 이 볼트의 [[원문검증 논문 MOC]] 기준을 통과하지 않았으므로 **제텔로 분해하지 않았고, 수치를 인용하지 않는다.**
> **단 2026-08-21 개정으로 「① 명제 층위」 인용은 허용된다** — 교과서적 정설을 수치 없이 인용할 때에 한하며,
> 인용 지점에 "원문 미대조"를 병기한다. → [[원문검증 논문 MOC]] 「인용 규칙 개정」
> 원문 확보 후 `status: verified`로 갱신한다.

﻿---
tags:
  - macro/methodology
  - lucas-critique
  - rational-expectations
  - dsge
  - econometrics
  - lucas
aliases:
  - "Lucas 1976"
  - "Lucas Critique"
year: 1976
author: Lucas
---

# Econometric Policy Evaluation A Critique

## 1. Bibliographic Information

- **Title:** Econometric Policy Evaluation: A Critique
- **Authors:** Robert E. Lucas Jr.
- **Year:** 1976
- **Journal / Working Paper:** Carnegie-Rochester Conference Series on Public Policy, Vol. 1, pp. 19-46
- **DOI / URL:** 10.1016/S0167-2231(76)80003-6
- **Research Field:** Macroeconometrics, Methodology, Monetary Economics, Rational Expectations
- **Keywords:** Lucas Critique, rational expectations, policy evaluation, structural parameters, deep parameters, policy invariance, econometric model, DSGE, Phillips Curve

### One-Sentence Thesis
이 논문은 **경제 행위자들이 합리적 기대를 형성**하므로 **기존 계량경제 모형의 파라미터들이 정책 변화에 따라 변화**하며, 이로 인해 **기존 계량 모형을 이용한 정책 효과 분석이 근본적으로 오류**임을 보여준다.

---

## 2. Research Question

- **Question 1:** 기존 대형 계량경제 모형으로 정책 효과를 신뢰할 수 있게 예측할 수 있는가?
- **Question 2:** 정책 변화에 불변인(policy-invariant) 구조 파라미터를 어떻게 찾을 수 있는가?

---

## 3. Literature Gap

**Existing Literature**
- 1960-70년대 대형 Keynesian 계량 모형(Klein-Goldberger, MPS, DRI): 역사적 데이터에 파라미터 추정 후 정책 시뮬레이션 사용
- Phillips Curve: 인플레이션-실업 간 안정적 역관계로 정책 수단 활용

**Limitation**
- 역사 데이터 추정 파라미터가 정책 체제 변화 하에서도 안정적이라는 암묵적 가정; 합리적 기대를 무시하여 행위자의 정책 반응 미포착

**Contribution of This Paper**
- 합리적 기대 하에서 행위자의 최적화 결정은 정책 체제에 의존 -> 정책 변화 시 행위자 행동의 파라미터가 변화 -> 기존 모형의 예측이 틀림; 정책 분석을 위해서는 선호.기술.정보 구조(deep parameters)에 기반한 구조 모형(DSGE)이 필요함을 주장

---

## 4. Core Mechanism

```
Cause / Shock: 정책 체제 변화 (e.g., 인플레이션 목표 변경)
      down
1st-order Effect: 합리적 기대 행위자들이 새 정책 체제를 인식하고 기대 수정
      down
2nd-order Effect: 소비.투자.임금 협상 등 최적화 결정 파라미터 변화
      down
3rd-order Effect: 기존 계량 모형의 파라미터가 새 체제에서 달라짐
      down
Real Economy: 기존 모형으로의 정책 예측이 실제와 체계적으로 다름 (모형 실패)
```

**Economic Logic**
- Phillips Curve 사례: 역사적 데이터로 추정한 pi = f(u)는 인플레이션이 항상 놀라움을 주던 체제에서 얻어진 것. 중앙은행이 이를 이용해 실업을 낮추려 하면 -> 민간이 이를 예측 -> 기대 인플레이션 상승 -> Phillips Curve 자체가 이동 -> 정책 효과 없음.
- Lucas Critique 수식: y_t = alpha*(m_t - E_{t-1}[m_t]) + epsilon_t; 만약 중앙은행이 m_t = gamma*u_{t-1}로 체계적 규칙을 사용하면 -> E_{t-1}[m_t] = gamma*u_{t-1} -> y_t = alpha*epsilon_t (체계적 정책 무효화)

---

## 5. Shock Classification

- [ ] Demand Shock
- [ ] Supply Shock
- [x] Monetary Shock
- [x] Fiscal Shock
- [ ] Credit Shock
- [ ] Financial Shock
- [ ] Commodity Shock
- [ ] Technology Shock
- [ ] Productivity Shock
- [ ] Trade Shock
- [ ] Capital Flow Shock
- [x] Expectation Shock

**Primary Shock:** 정책 체제 변화(policy regime change) -- 통화.재정 정책 규칙의 변화가 기대와 행동을 변화시키는 충격

---

## 6. Transmission Mechanism

```
Shock: 정책 체제 변화 (e.g., 중앙은행이 인플레이션 억제로 방향 전환)
  down
Transmission Channel: 합리적 기대 형성 -> 민간의 기대 인플레이션 조정
  down
Intermediate Variables: 임금 협상.소비.투자 결정의 파라미터 변화
  down
Real Economy: 새 체제에서 소비-소득 관계, 임금-인플레이션 관계 등이 달라짐
  down
Financial Markets: [추론] 채권 시장이 정책 체제 변화를 즉각 반영 -> 기대 인플레이션 변동
```

**Explanation**
- "계량경제 모형의 최적 제어(optimal control)는 환상이다": 정책 파라미터 변화가 모형 파라미터를 변화시키므로, 고정된 파라미터 모형으로 최적 정책을 찾는 것은 자기 모순적.

---

## 7. Key Variables

**Macroeconomic**
- 정책 체제(policy regime): 통화.재정 규칙의 구조적 특성
- Deep parameters: 선호(beta, gamma, sigma), 기술(alpha, delta), 정보 구조
- 기대 형성 메커니즘: E_t[.] (합리적 기대 전제)
- Phillips Curve 기울기: 정책 체제에 따라 변하는 추정 파라미터

**Financial**
- 기대 인플레이션: 채권 시장의 핵심 결정 변수
- [추론] 장단기 금리차(yield spread): 정책 체제 변화 시 즉각 반응

**Commodity**
- 해당 없음

**Leading / Coincident / Lagging**
- 기대: leading (정책 공표 즉시 반응)
- 소비.투자 결정: coincident to slightly lagging
- 인플레이션: lagging (기대 변화 후 실물 경로 통해)

---

## 8. Empirical Strategy

- **Data:** 이론 논문 (실증 데이터 없음); Sargent(1976, 1983) 등이 이후 실증 검증
- **Sample Period:** 해당 없음
- **Country / Region:** 해당 없음
- **Frequency:** 해당 없음
- **Method:** 이론 논증; 수학 모형(합리적 기대 모형); 기존 모형들의 한계 비판
- **Identification Strategy:** 해당 없음 (이론 비판 논문)
- **Main Model:** y_t = f(x_t, theta(lambda)); theta가 정책 파라미터 lambda의 함수 -> lambda 변화 시 theta 변화

**Correlation or Causality?**
- 이론 논증; 실증적 인과 식별 없음 -- 방법론 비판 논문

---

## 9. Main Findings

1. [논문 직접] 계량경제 모형의 파라미터는 정책 체제(policy regime)에 의존하므로 정책 변화 시 파라미터가 변함 -> 기존 모형으로 정책 효과 예측 불가.
2. [논문 직접] Phillips Curve는 안정적 관계가 아님 -- 통화 정책 체제에 따라 기울기.위치 모두 변함; 스태그플레이션(1970년대)으로 실증적으로 확인.
3. [논문 직접] 정책 분석을 위해서는 deep parameters(선호.기술.정보)에 기반한 구조 모형이 필요.
4. 체계적 정책의 무효성(policy ineffectiveness): 합리적 기대 하에서 예측 가능한 통화 정책은 실질 산출에 영향 없음 (Sargent-Wallace 1975와 연결).
5. 최적 제어(optimal control) 방법론의 거시 모형 적용이 근본적으로 부적절함을 논증.

---

## 10. Regime Dependency

**When is the mechanism stronger?**
- 민간의 합리적 기대 형성 능력이 강할수록: 정보 접근성 높은 선진 경제
- 정책 체제가 명확하고 공표될 때: 기대 반응이 빠름
- 중앙은행 독립성.신뢰도가 높을 때: 기대 채널이 더 중요해짐

**When is the mechanism weaker?**
- 정책 불투명성.놀라움이 클 때: 기대 반응이 느리거나 불완전
- 비합리적 기대(bounded rationality): Lucas Critique 완화
- 단기 계약.메뉴 비용 등 마찰이 강한 환경: 기대가 행동에 즉각 반영되지 않음

**Does the conclusion change across regimes?**
- 기대 고착(expectations anchoring): 중앙은행 신뢰도가 높으면 인플레이션 기대가 잘 고정 -> Phillips Curve가 일부 안정성 회복; Woodford(2003): forward guidance의 기대 채널이 핵심 통화 정책 수단으로 발전

---

## 11. Asset-Price Implications

**Bonds**
- [논문 간접] 정책 체제 변화 -> 기대 인플레이션 즉각 재조정 -> 채권 수익률 변동; 체제 전환(e.g., Volcker 긴축 1979)이 장기 채권 금리 급등으로 이어짐

**Equities**
- [추론] 정책 체제 변화 -> 기업 미래 현금흐름 할인율 변화 -> 주가 재평가; 인플레이션 체제 전환이 주식 밸류에이션에 구조적 영향

**FX**
- [추론] 통화 정책 체제 전환 -> 환율 기대 즉각 변화 -> 즉각적 환율 조정 (Dornbusch 1976 overshooting과 연결)

**Commodities**
- [추론] 인플레이션 억제 체제 전환 -> 기대 인플레이션 하락 -> 인플레이션 헤지 자산(금.원자재) 수요 하락 -> 가격 하락 압력

**Credit**
- [추론] 정책 체제 신뢰성 상승 -> 기대 인플레이션 안정 -> 장기 기업 자금 조달 비용 하락 -> 크레딧 스프레드 축소

> 반드시 [논문에서 직접 주장한 내용]과 [우리의 추론]을 구분한다.

---

## 12. Falsification Conditions

**What would confirm the hypothesis?**
- 정책 체제 변화 전후로 계량 모형의 파라미터가 구조적으로 변함 (Chow test, Bai-Perron 구조 변화 검정)
- Phillips Curve의 기울기가 인플레이션 기대 체제에 따라 달라짐 (1960s vs. 1970s vs. post-Volcker)

**What would falsify the hypothesis?**
- 계량 모형의 파라미터가 다양한 정책 체제에서 안정적 -> Lucas Critique 무관련
- 행동경제학 증거: 실제 행위자가 비합리적 기대를 형성하여 기대 채널이 약함

**Variables to monitor**
- 인플레이션 기대(TIPS 스프레드, Survey of Professional Forecasters), Phillips Curve 기울기 추세, 구조 변화 검정 결과, 정책 체제 전환 전후 VAR 파라미터 안정성

---

## 13. Contradictory / Alternative Literature

**Supporting Papers**
- Sargent & Wallace (1975): 합리적 기대 하 정책 무효성 명시
- Sargent (1983): "The End of Four Big Inflations" -- 인플레이션 체제 전환 시 기대 채널의 즉각적 작동 실증
- Taylor (1993): Taylor Rule -- 체제(rule)의 명시적 공약으로 기대 안정화

**Contradictory Papers**
- Sims (1980): VAR 방법론 -- "A-theoretical"한 방식으로 Lucas Critique 회피 시도
- 행동 거시경제학: 실제 기대 형성이 완전 합리적이지 않음 -> Lucas Critique의 강도 완화

**Why do the results differ?**
- Data: 파라미터 안정성 검정이 혼재된 결과
- Identification: 정책 체제 변화의 외생성 식별 어려움
- Economic regime: 비합리적 기대.습관 형성이 강한 경제에서 Lucas Critique 완화
- Country: 중앙은행 신뢰도에 따라 기대 채널의 강도 상이

---

## 14. Connections to Other Papers

**SUPPORTS**
- [[1982 Time to Build and Aggregate Fluctuations (Kydland & Prescott)]]: Lucas Critique에 면역된 구조 모형(DSGE)의 필요성 -> KP(1982)가 해결책 제시
- [[1988 Production Growth and Business Cycles I - The Basic Neoclassical Model (King, Plosser & Rebelo)]]: Deep parameters 기반 구조 모형

**CONTRADICTS**
- 기존 대형 Keynesian 계량 모형(MPS, DRI 등): 파라미터 안정성 가정 비판
- IS-LM 기반 정책 분석: 합리적 기대 무시 비판

**EXTENDS**
- Muth(1961) 합리적 기대 개념을 계량경제 방법론 비판으로 발전

**CRITIQUES**
- 케인지언 정책 분석 전반: 행동 파라미터가 정책에 의존함을 간과하는 방법론적 오류 비판

**APPLIES**
- DSGE 모형의 이론적 정당화; 중앙은행 forward guidance의 기대 채널 이해; 인플레이션 타겟팅의 기대 고착 효과 분석

---

## 15. Zettelkasten Atomic Notes

### ZK Note 1
**Claim:** 계량경제 모형의 파라미터는 정책 체제에 의존하므로 정책 변화 시 신뢰할 수 없다.

**Mechanism:** 행위자의 최적화 결정 -> 파라미터 = 선호.기술.기대의 함수; 정책 변화 -> 기대 변화 -> 파라미터 변화 -> 기존 모형의 예측 오류

**Evidence:** [논문 직접] 수학적 논증; Phillips Curve 기울기 변화 사례; 1970년대 스태그플레이션으로 실증

**Implication:** 계량 모형을 이용한 정책 최적화는 자기 모순적; 모든 정책 분석은 deep parameters에 기반한 구조 모형에서 수행해야 함 -> DSGE 혁명의 직접 원인

**Connected Notes:** [[1982 Time to Build and Aggregate Fluctuations (Kydland & Prescott)]], [[1988 Production Growth and Business Cycles I - The Basic Neoclassical Model (King, Plosser & Rebelo)]]

---

### ZK Note 2
**Claim:** Phillips Curve는 안정적 정책 도구가 아니라 정책 체제에 따라 이동하는 내생 변수이다.

**Mechanism:** 역사적 Phillips Curve 추정 -> 정책 당국이 이를 이용 -> 민간이 정책 패턴 예측 -> 기대 인플레이션 조정 -> Phillips Curve 이동; 체계적 사용 -> 무효화

**Evidence:** [논문 직접] 이론 논증; Sargent(1983): 1920년대 중부유럽 인플레이션 체제 전환 시 즉각적 인플레이션 하락 (기대 채널 실증)

**Implication:** 인플레이션-실업 트레이드오프는 단기적.일시적; 장기에서 tradeoff 없음 (Friedman 1968과 일치); 인플레이션 타겟팅의 신뢰성이 핵심

**Connected Notes:** [[1986 Theory Ahead of Business Cycle Measurement (Prescott)]], [[1984 Equilibrium Unemployment as a Worker Discipline Device (Shapiro & Stiglitz)]]

---

### ZK Note 3
**Claim:** Lucas Critique는 DSGE 모형 혁명의 방법론적 원동력이다.

**Mechanism:** Lucas Critique -> 기존 계량 모형 불신 -> 합리적 기대 + deep parameters 기반 구조 모형(DSGE) 필요 -> Kydland-Prescott(1982), RBC, New Keynesian DSGE로 발전

**Evidence:** 이후 30년간 중앙은행.학계가 DSGE를 기본 정책 분석 도구로 채택; 2008년 이후 비판과 함께 HANK 등으로 발전

**Implication:** 방법론 혁명의 중요성: 개별 모형보다 분석 도구의 패러다임이 경제학 발전 방향을 결정; 현재도 machine learning 예측 모형 vs. 구조 모형 논쟁에서 Lucas Critique의 논리가 구조 모형 지지의 핵심 논거

**Connected Notes:** [[1982 Time to Build and Aggregate Fluctuations (Kydland & Prescott)]], [[1988 Production Growth and Business Cycles I - The Basic Neoclassical Model (King, Plosser & Rebelo)]], [[1986 Theory Ahead of Business Cycle Measurement (Prescott)]]

---

## 16. One-Sentence Takeaway

이 논문을 한 문장으로 기억한다면: **사람들은 정부의 정책 패턴을 예측하고 행동을 바꾸므로, 과거 데이터로 추정한 경제 모형은 정책이 바뀌는 순간 쓸모없어진다 -- 이것이 거시 경제학의 방법론을 완전히 뒤바꾼 Lucas Critique이다.**

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
