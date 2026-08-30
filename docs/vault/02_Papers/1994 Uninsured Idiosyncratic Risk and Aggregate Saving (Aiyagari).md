---
title: Uninsured Idiosyncratic Risk and Aggregate Saving
type: paper
journal: Quarterly Journal of Economics, Vol. 109, No. 3, pp. 659–684. DOI/URL 10.2307/2118417
date: 1994
author: S. Rao Aiyagari
created: 2026-08-12
updated: 2026-08-12
status: draft
verification: none
reliability: academic
verified: "❌ 원문 미대조. 카카오톡 수신 노트(2026-08-12 임포트)를 볼트 규약으로 정규화한 것 — 수치·표현은 원문 확보 후 재검증 필요"
source_file: 없음 (외부 작성 노트 수신)
tags: [type/paper, domain/risk, region/us, method/일반균형시뮬레이션, method/불완전시장, flag/unverified]
concepts: [incomplete-markets, precautionary-saving, heterogeneous-agents, Bewley-Aiyagari, wealth-distribution]
import_origin: 카카오톡 수신 — Macro Paper Notes / 원본 파일명 'Aiyagari (1994) — Uninsured Idiosyncratic Risk and Aggregate Saving.md'
---
> ⚠ **원문 미대조 노트다.** 외부에서 작성된 것을 수신해 볼트 규약으로 정규화만 했다.
> 이 볼트의 [[원문검증 논문 MOC]] 기준을 통과하지 않았으므로 **제텔로 분해하지 않았고, 수치를 인용하지 않는다.**
> **단 2026-08-21 개정으로 「① 명제 층위」 인용은 허용된다** — 교과서적 정설을 수치 없이 인용할 때에 한하며,
> 인용 지점에 "원문 미대조"를 병기한다. → [[원문검증 논문 MOC]] 「인용 규칙 개정」
> 원문 확보 후 `status: verified`로 갱신한다.

# Uninsured Idiosyncratic Risk and Aggregate Saving

## 1. Bibliographic Information

- **Title:** Uninsured Idiosyncratic Risk and Aggregate Saving
- **Authors:** S. Rao Aiyagari
- **Year:** 1994
- **Journal / Working Paper:** Quarterly Journal of Economics, Vol. 109, No. 3, pp. 659–684
- **DOI / URL:** 10.2307/2118417
- **Research Field:** Macroeconomics, Incomplete Markets, Heterogeneous Agents, Savings Theory
- **Keywords:** precautionary saving, idiosyncratic risk, incomplete markets, Bewley model, heterogeneous agents, stationary distribution, wealth distribution, buffer stock saving, borrowing constraint

### One-Sentence Thesis
이 논문은 **보험 불가능한 개인별 소득 충격(uninsured idiosyncratic risk)**이 **예비적 저축 동기(precautionary saving)**를 통해 **집계 저축률과 자본 스톡을 대표 행위자 모형 예측보다 영구적으로 높인다**는 것을 보여준다.

---

## 2. Research Question

- **Question 1:** 불완전 시장에서 개인별 소득 리스크가 집계 저축률에 얼마나 영향을 주는가?
- **Question 2:** 이질적 가계와 차입 제약이 존재할 때 정상 분포(stationary distribution)가 존재하며 이것이 관측된 부 불평등을 설명할 수 있는가?

---

## 3. Literature Gap

**Existing Literature**
- 대표 행위자 모형(Ramsey-Cass-Koopmans): 모든 리스크는 집계 충격만 존재; 완전 보험 시장 가정 → 소득 변동이 저축률에 영향 없음
- [[1986 Stationary Monetary Equilibrium with a Continuum of Independently Fluctuating Consumers (Bewley)]]: 이질적 가계 불완전 시장 모형의 이론적 기초 제시; 정량적 분석 부재

**Limitation**
- 완전 시장 가정 하에서 개인별 소득 리스크는 집계에서 상쇄되어 집계 저축에 영향 없음; 현실적 부 불평등 설명 불가

**Contribution of This Paper**
- Bewley 모형을 정량적으로 풀어 집계 저축, 균형 이자율, 자본 스톡을 대표 행위자 모형과 비교; 불완전 시장 일반균형 모형(HANK의 선구)의 계산 방법론 확립

---

## 4. Core Mechanism

```
Cause / Shock: 개인별 소득 충격(e_i,t) — 보험 불가능, AR(1) 과정
      ↓
1st-order Effect: 개인 소득 변동 → 소비 평탄화 불완전
      ↓
2nd-order Effect: 차입 제약(borrowing constraint) → 나쁜 충격에 대비 예비 저축 필요
      ↓
3rd-order Effect: 모든 가계의 예비 저축 동기 → 집계 저축↑, 집계 자본 스톡↑
      ↓
Real Economy: 균형 이자율 하락 (자본 공급↑), 자본-노동 비율 상승 → 임금 상승
```

**Economic Logic**
- 대표 행위자 모형: K = K*(r); r은 주관적 할인율에서 결정
- Aiyagari 모형: 예비 저축 동기로 집계 저축 함수가 우상향 이동 → 동일 r에서 더 높은 K; 균형에서 r < ρ (이자율이 대표 행위자 모형보다 낮음)
- 직관: 나쁜 소득 충격 시 차입 불가 → 자산을 buffer stock으로 유지 → 모두가 이러면 집계 자산↑

---

## 5. Shock Classification

- [ ] Demand Shock
- [x] Supply Shock
- [ ] Monetary Shock
- [ ] Fiscal Shock
- [ ] Credit Shock
- [ ] Financial Shock
- [ ] Commodity Shock
- [ ] Technology Shock
- [ ] Productivity Shock
- [ ] Trade Shock
- [ ] Capital Flow Shock
- [ ] Expectation Shock

**Primary Shock:** 보험 불가능한 개인별 소득 충격(idiosyncratic labor income risk) — 집계 충격이 아닌 개인 고유 충격

---

## 6. Transmission Mechanism

```
Shock: 개인 i의 노동 소득 충격 (e_i,t 하락)
  ↓
Transmission Channel: 완전 보험 시장 없음 → 소비 완전 평탄화 불가
  ↓
Intermediate Variables: 차입 제약 → 자산 감소 or 예비 저축 적립 결정
  ↓
Real Economy: 집계 자산 수요↑ (buffer stock) → 균형 이자율↓, 자본 스톡↑
  ↓
Financial Markets: 위험 없는 자산(무위험 채권)에 대한 초과 수요 → 무위험 이자율↓ (Risk-free rate puzzle 연결)
```

**Explanation**
- 정상 분포(stationary distribution) 존재 조건: 차입 상한(a ≥ a_min)이 있고 소득 과정이 에르고딕(ergodic)이면 자산 분포가 수렴. Huggett(1993)의 순수 교환 경제를 생산 경제로 확장.

---

## 7. Key Variables

**Macroeconomic**
- 개인 자산 a_i, 노동 소득 충격 e_i (AR(1) 과정)
- 차입 하한 a_min (≥ 0 또는 음수)
- 집계 자본 스톡 K = ∫a_i dF(a), 균형 이자율 r
- 소득 충격의 분산 σ²_e, 지속성 ρ_e

**Financial**
- 무위험 이자율 r: 대표 행위자 예측보다 낮음 (예비 저축의 집계 효과)
- [추론] 부 분포의 오른쪽 꼬리 두께 → 소득 불평등 지수(Gini)와 연결

**Commodity**
- 해당 없음

**Leading / Coincident / Lagging**
- 개인 소득 충격: 동시
- 자산 축적: lagging (느린 buffer stock 조정)
- 집계 자본 스톡: 장기 steady state에서 결정

---

## 8. Empirical Strategy

- **Data:** 수치 시뮬레이션 (calibrated model); 미국 소득·부 분포 데이터와 비교
- **Sample Period:** 해당 없음 (정상 상태 분석)
- **Country / Region:** 미국 (파라미터 캘리브레이션)
- **Frequency:** 해당 없음
- **Method:** 동태 프로그래밍(value function iteration); 정상 분포 계산; 집계 균형 탐색 (r, K, w를 동시에 결정)
- **Identification Strategy:** 소득 과정의 분산(σ)·지속성(ρ)·차입 제약 수준을 외부에서 고정 후 균형 비교
- **Main Model:** Bellman equation: V(a,e) = max_{c,a'} {u(c) + β·E[V(a',e')]}; s.t. c + a' = (1+r)a + we; a' ≥ a_min

**Correlation or Causality?**
- [논문 직접] 이론 모형 + 캘리브레이션; 실증적 인과 식별이 아닌 정량적 비교 (집계 저축 비율, r, 부 분포)

---

## 9. Main Findings

1. [논문 직접] 불완전 시장 모형에서 집계 저축률은 대표 행위자 모형보다 유의하게 높음 (예비 저축 효과).
2. [논문 직접] 균형 이자율(r)이 주관적 할인율(ρ)보다 낮아짐 → r = ρ인 대표 행위자 예측과 다름.
3. [논문 직접] 소득 충격의 분산·지속성이 클수록 예비 저축 효과 강화.
4. 차입 제약이 강할수록(a_min이 0에 가까울수록) 예비 저축 동기 강화.
5. 정상 부 분포가 오른쪽 꼬리 두꺼운 형태(fat-tailed) → 부 불평등의 방향을 질적으로 재현하나 미국 실제 최상위층 부 집중은 과소 예측.

---

## 10. Regime Dependency

**When is the mechanism stronger?**
- 소득 충격의 분산(σ²_e)과 지속성(ρ_e)이 높을수록; 차입 제약이 강할수록
- 사회 안전망이 부실한 경제: 실업보험 없으면 예비 저축 더 크게 필요

**When is the mechanism weaker?**
- 완전한 사회보험(실업급여, 건강보험 등) → 예비 저축 동기 약화
- 금융시장 발전으로 차입 제약 완화 → buffer stock 필요성 감소

**Does the conclusion change across regimes?**
- 사회보험 확충 → 예비 저축↓ → 집계 저축률 하락 → 자본 스톡 하락 가능; 복지 국가 vs. 자유 시장 경제의 집계 저축 차이를 이 채널로 설명 가능

---

## 11. Asset-Price Implications

**Bonds**
- [논문 간접] 무위험 자산 초과 수요 → 무위험 이자율 하락 → **Risk-free rate puzzle 부분 설명**: Mehra-Prescott (1985)의 퍼즐에서 무위험 이자율이 데이터보다 모형에서 높은 문제를 예비 저축이 낮춤

**Equities**
- [추론] 위험 자산 보유 여력이 낮은 하위 가계 → 주식 시장 참여율 낮음 → 주식 수익률 프리미엄 유지

**FX**
- [추론] 예비 저축 강한 나라(높은 소득 불확실성): 경상수지 흑자 경향 → 환율 절상 압력

**Commodities**
- [해당 없음]

**Credit**
- [추론] 차입 제약 → 신용 시장에서 유동성 함정 가능성; 소득 충격 시 채무 상환 어려움 → 소비자 신용 부실 위험

> 반드시 [논문에서 직접 주장한 내용]과 [우리의 추론]을 구분한다.

---

## 12. Falsification Conditions

**What would confirm the hypothesis?**
- 소득 불확실성이 높은 개인·국가에서 저축률이 통계적으로 유의하게 높음 (예비 저축 직접 증거)
- 사회보험 확충 시 개인 저축률이 의도한 방향으로 감소 (Attanasio & Davis 1996 등)

**What would falsify the hypothesis?**
- 소득 불확실성과 저축률 간 관계 없음 → 완전 보험 시장 또는 예비 저축 동기 부재
- 부 불평등이 예비 저축 모형이 예측하는 것보다 훨씬 크고 다른 원인(상속, 운) 지배 (Castaneda et al. 2003: 소득 상위 집중 재현 어려움)

**Variables to monitor**
- 가계 저축률과 소득 분산 관계, 사회보험 수준과 저축률, 부 지니계수, 무위험 이자율과 성장률 격차

---

## 13. Contradictory / Alternative Literature

**Supporting Papers**
- [[1986 Stationary Monetary Equilibrium with a Continuum of Independently Fluctuating Consumers (Bewley)]]: 이론적 기반 제공
- Carroll (1997): "Buffer-Stock Saving" — 예비 저축의 미시 증거 및 이론 발전
- Huggett (1993): 순수 교환 경제에서 유사 결과

**Contradictory Papers**
- Ramsey-Cass-Koopmans(대표 행위자): 완전 보험 시장에서 예비 저축 없음
- Castaneda, Diaz-Gimenez & Rios-Rull (2003): 미국 최상위 부 집중도 재현 위해 수명 주기 + 대형 소득 충격 추가 필요 → 순수 Aiyagari 예비 저축만으로는 불충분

**Why do the results differ?**
- Data: 소득 충격 과정 추정 방법에 따라 예비 저축 크기 상이
- Identification: 소득 불확실성의 외생적 측정 어려움
- Economic regime: 사회보험 수준·금융시장 발전에 따라 예비 저축 중요성 상이
- Country: 가계 부채 허용 수준이 국가마다 다름

---

## 14. Connections to Other Papers

**SUPPORTS**
- [[1986 Stationary Monetary Equilibrium with a Continuum of Independently Fluctuating Consumers (Bewley)]]: 이론 기반을 정량 모형으로 발전

**CONTRADICTS**
- Ramsey-Cass-Koopmans 대표 행위자 모형: 개인별 이질성·불완전 시장이 집계에 중요한 영향을 미침을 보여줌

**EXTENDS**
- [[1986 Stationary Monetary Equilibrium with a Continuum of Independently Fluctuating Consumers (Bewley)]]: Bewley 모형을 생산 경제에서 수치적으로 풀어 집계 저축·이자율 도출

**CRITIQUES**
- 대표 행위자 DSGE(Kydland-Prescott 등): 이질성 무시로 집계 저축 결정 요인 오해

**APPLIES**
- HANK (Heterogeneous Agent New Keynesian) 모형의 직접 선구; 통화 정책의 분배 효과 분석에 응용

---

## 15. Zettelkasten Atomic Notes

### ZK Note 1
**Claim:** 예비적 저축(precautionary saving)이 불완전 시장에서 집계 자본 스톡을 대표 행위자 예측보다 높인다.

**Mechanism:** 차입 불가 + 나쁜 소득 충격 가능성 → 자산을 buffer stock으로 유지; 모든 가계의 예비 저축 합산 → 집계 저축 > 대표 행위자 예측

**Evidence:** [논문 직접] 소득 충격 분산·지속성 증가 시 균형 자본 스톡 단조 증가; r < ρ 확인

**Implication:** 사회보험 확대는 예비 저축을 줄여 집계 자본 스톡 하락 → 성장에 양면적 효과 (보험 vs. 저축); 경기 침체 시 소득 불확실성 증가 → 소비 감소 더 심화 (정책 채널)

**Connected Notes:** [[1986 Stationary Monetary Equilibrium with a Continuum of Independently Fluctuating Consumers (Bewley)]], [[1956 A Contribution to the Theory of Economic Growth (Solow)]]

---

### ZK Note 2
**Claim:** 불완전 시장 이질적 가계 모형에서 균형 이자율이 주관적 할인율보다 낮다.

**Mechanism:** 예비 저축 → 자본 공급 초과 → r < ρ; 대표 행위자에서 r = ρ인 반면 불완전 시장에서 r이 낮아짐

**Evidence:** [논문 직접] 수치 균형에서 r < ρ; 소득 충격이 클수록 r이 더 낮아짐

**Implication:** Risk-free rate puzzle(Mehra-Prescott) 부분 해결 → 무위험 이자율이 낮은 이유는 예비 저축 수요 때문; 장기 중립금리(r*) 하락의 구조적 원인으로 소득 불확실성 증가·불완전 보험 제시

**Connected Notes:** [[1982 Time to Build and Aggregate Fluctuations (Kydland & Prescott)]], [[1986 Stationary Monetary Equilibrium with a Continuum of Independently Fluctuating Consumers (Bewley)]]

---

### ZK Note 3
**Claim:** 이질적 가계 모형이 부 불평등의 패턴을 질적으로 재현하나 최상위 집중은 과소 예측한다.

**Mechanism:** 정상 분포가 오른쪽 꼬리 두꺼운 형태 → 상위 가계의 자산 집중; 그러나 미국 최상위 1%의 부 집중도(40%)를 재현하려면 추가 요소 필요 (대형 소득 충격, 상속, 수익률 이질성)

**Evidence:** [논문 직접] 캘리브레이션 결과와 미국 SCF 부 분포 비교; 중간 분위는 잘 맞으나 최상위 예측 부족

**Implication:** 순수 예비 저축 모형만으로는 부의 극단적 집중 설명 불가 → 이후 연구(Benhabib-Bisin-Zhu 2011: 수익률 이질성; De Nardi 2004: 상속)로 확장

**Connected Notes:** [[1986 Stationary Monetary Equilibrium with a Continuum of Independently Fluctuating Consumers (Bewley)]], [[1992 A Contribution to the Empirics of Economic Growth (Mankiw, Romer & Weil)]]

---

## 16. One-Sentence Takeaway

이 논문을 한 문장으로 기억한다면: **나쁜 일이 생겼을 때 빌릴 수 없다는 공포가 모든 사람을 필요 이상으로 저축하게 만들고, 이것이 모이면 경제 전체의 자본 스톡이 완전 시장 예측보다 커진다.**

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
