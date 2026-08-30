---
title: Production Growth and Business Cycles I - The Basic Neoclassical Model
type: paper
journal: Journal of Monetary Economics, Vol. 21, No. 2–3, pp. 195–232 (Part I); 309–341 (Part II). DOI/URL 10.1016/0304-3923(88)90030-X
date: 1988
author: Robert G. King, Charles I. Plosser, Sergio T. Rebelo
created: 2026-08-12
updated: 2026-08-12
status: draft
verification: none
reliability: academic
verified: "❌ 원문 미대조. 카카오톡 수신 노트(2026-08-12 임포트)를 볼트 규약으로 정규화한 것 — 수치·표현은 원문 확보 후 재검증 필요"
source_file: 없음 (외부 작성 노트 수신)
tags: [type/paper, domain/growth, region/us, method/캘리브레이션, method/선형근사, flag/unverified]
concepts: [RBC, balanced-growth-path, King-Plosser-Rebelo-preferences, log-linearization, great-ratios]
import_origin: 카카오톡 수신 — Macro Paper Notes / 원본 파일명 'King, Plosser & Rebelo (1988) — Production, Growth and Business Cycles.md'
---
> ⚠ **원문 미대조 노트다.** 외부에서 작성된 것을 수신해 볼트 규약으로 정규화만 했다.
> 이 볼트의 [[원문검증 논문 MOC]] 기준을 통과하지 않았으므로 **제텔로 분해하지 않았고, 수치를 인용하지 않는다.**
> **단 2026-08-21 개정으로 「① 명제 층위」 인용은 허용된다** — 교과서적 정설을 수치 없이 인용할 때에 한하며,
> 인용 지점에 "원문 미대조"를 병기한다. → [[원문검증 논문 MOC]] 「인용 규칙 개정」
> 원문 확보 후 `status: verified`로 갱신한다.

# Production, Growth and Business Cycles

## 1. Bibliographic Information

- **Title:** Production, Growth and Business Cycles
- **Authors:** Robert G. King, Charles I. Plosser, Sergio T. Rebelo
- **Year:** 1988
- **Journal / Working Paper:** Journal of Monetary Economics, Vol. 21, No. 2–3, pp. 195–232 (Part I); 309–341 (Part II)
- **DOI / URL:** 10.1016/0304-3923(88)90030-X
- **Research Field:** Business Cycle Theory, Growth Theory, DSGE, Macroeconomics
- **Keywords:** balanced growth path, BGP, business cycles, growth-cycle integration, time-separable utility, neoclassical, King-Plosser-Rebelo preferences, technology shock

### One-Sentence Thesis
이 논문은 **장기 균형 성장경로(BGP)와 단기 경기변동이 동일한 신고전파 모형 내에서 통합적으로 도출**될 수 있음을 보여주되, 이를 위해 **BGP와 양립하는 효용 함수(KPR preferences)와 생산 기술 구조**가 필요함을 밝힌다.

---

## 2. Research Question

- **Question 1:** 장기 성장(balanced growth path)과 단기 경기변동을 하나의 통일된 신고전파 모형으로 동시에 설명할 수 있는가?
- **Question 2:** Balanced growth path(BGP)와 양립하는 효용 함수와 기술 구조의 조건은 무엇인가?

---

## 3. Literature Gap

**Existing Literature**
- Solow(1956): 장기 성장 설명에 특화; 경기변동 설명 없음
- [[1982 Time to Build and Aggregate Fluctuations (Kydland & Prescott)]]: 경기변동 설명에 특화; 성장 경로와의 일관성 검토 미흡

**Limitation**
- 성장 모형과 경기변동 모형이 분리되어 있어 내적 일관성 부족; 경기변동 모형이 장기 성장 사실(Kaldor stylized facts)과 부합하는지 불명확

**Contribution of This Paper**
- BGP(balanced growth path)의 존재 조건을 도출하고, 이와 일관된 효용 함수(King-Plosser-Rebelo preferences) 특성화; 통합 모형에서 기술 충격이 성장 추세 주변의 단기 변동을 만들어냄을 보임; 성장회계와 경기변동 분석의 이론적 통일

---

## 4. Core Mechanism

```
Cause / Shock: TFP 충격(일시적 또는 지속적)
      ↓
1st-order Effect: 현재 시점 실질 임금·이자율 변화 (BGP 주변)
      ↓
2nd-order Effect: 가계의 기간 간 소비·여가 대체 (BGP와 양립하는 선호체계 하에서)
      ↓
3rd-order Effect: 자본 축적 경로 조정 → BGP로의 이행 과정
      ↓
Real Economy: BGP 추세 주변의 단기 변동(경기변동) + 장기 성장 경로 유지
```

**Economic Logic**
- BGP 존재 조건: 기술 진보가 노동증강적(labor-augmenting)이고, 효용 함수가 소비와 여가에 대해 balanced growth와 양립해야 함. KPR preferences: U(c,l) = [c^α·(1−l)^(1−α)]^(1−σ)/(1−σ) (σ≠1) 또는 U = αln(c) + (1−α)ln(1−l) (σ=1). 이 형태에서만 성장과 함께 노동 공급이 일정하게 유지됨(Kaldor 사실과 일치).

---

## 5. Shock Classification

- [ ] Demand Shock
- [ ] Supply Shock
- [ ] Monetary Shock
- [ ] Fiscal Shock
- [ ] Credit Shock
- [ ] Financial Shock
- [ ] Commodity Shock
- [x] Technology Shock
- [x] Productivity Shock
- [ ] Trade Shock
- [ ] Capital Flow Shock
- [ ] Expectation Shock

**Primary Shock:** 노동증강적 기술 충격(labor-augmenting technology shock); 일시적 및 지속적 충격 모두 분석

---

## 6. Transmission Mechanism

```
Shock: 노동증강 기술 충격(A_t 변화)
  ↓
Transmission Channel: 실질 임금·이자율 변화 → 소비·여가의 기간 간 대체 (KPR 선호 하)
  ↓
Intermediate Variables: 자본 축적 속도 변화, 노동 공급 변동
  ↓
Real Economy: BGP 주변의 단기 변동; 장기적으로 BGP 복귀
  ↓
Financial Markets: [추론] 실질이자율이 BGP 수준으로 복귀하는 경로 추적 가능
```

**Explanation**
- KPR preferences의 핵심: 상대적 위험회피계수(CRRA)가 1이 아닌 경우에도 소득·대체효과가 상쇄되어 노동 공급이 실질임금 성장에 무관 → Kaldor stylized fact (노동 시간의 장기 안정성) 달성. 일시적 충격: 이행 과정 후 BGP 복귀. 지속적 충격: BGP 자체가 이동.

---

## 7. Key Variables

**Macroeconomic**
- 기술 수준 A_t (노동증강적)
- 소비 c_t, 여가(1−h_t), 자본 K_t
- 효용 함수 파라미터: α(소비 비중), σ(위험회피)
- Kaldor stylized facts: 장기 노동 시간·자본/산출 비율·실질이자율의 안정성

**Financial**
- 실질이자율 r_t = αA_t^(1−α)k_t^(α−1) − δ (BGP에서 일정)
- [추론] 주식 배당 수익률과 성장률의 관계

**Commodity**
- 해당 없음

**Leading / Coincident / Lagging**
- 기술 충격: 선행(leading) driver
- 자본 스톡: lagging (조정 느림)
- 소비·노동: coincident (KPR 선호 하)

---

## 8. Empirical Strategy

- **Data:** 미국 장기 성장 자료 (Kaldor stylized facts 확인); 캘리브레이션
- **Sample Period:** 장기 데이터 (성장 사실 검증)
- **Country / Region:** 미국 (주로)
- **Frequency:** 연간(장기 성장 분석) + 분기(경기변동 분석)
- **Method:** 이론 분석 + 캘리브레이션; BGP 조건 수학적 도출; 수치 시뮬레이션
- **Identification Strategy:** 외부 파라미터 고정 (미시 증거 + 장기 성장 사실)
- **Main Model:** 노동증강 기술 진보 + KPR preferences + 신고전파 성장 + AR(1) TFP

**Correlation or Causality?**
- 이론 모형의 수학적 도출 + 캘리브레이션 비교; 통계적 인과 식별 없음

---

## 9. Main Findings

1. [논문 직접] BGP 존재를 위한 필요·충분 조건 도출: 기술 진보는 노동증강적이어야 하며, 효용 함수는 KPR 형태이어야 함.
2. [논문 직접] KPR preferences 하에서 Kaldor stylized facts(노동 시간 안정성, 자본/산출 비율 안정성, 실질이자율 안정성) 재현 가능.
3. 일시적 기술 충격은 BGP 주변의 경기변동을 만들어냄 (Kydland-Prescott과 동일 결론).
4. 지속적(permanent) 기술 충격은 BGP 수준 자체를 이동시킴 → 성장과 변동의 통합.
5. 화폐·명목 변수 없이 실물 모형으로 성장과 변동을 단일 틀에서 설명 가능.

---

## 10. Regime Dependency

**When is the mechanism stronger?**
- 기술 충격의 지속성이 높을수록 BGP 이동 효과 강화
- 자본과 노동의 대체 탄력성이 적정 범위일 때 BGP 수렴 속도 적절

**When is the mechanism weaker?**
- 조세 왜곡·규제가 존재하면 BGP 경로 자체가 왜곡됨
- 금융 마찰이 있으면 이행 과정이 모형 예측과 다름

**Does the conclusion change across regimes?**
- 세율 변화(Rebelo 1991)가 BGP 성장률에 영향 → 재정 정책의 성장 효과로 확장; 인적자본 포함 시 BGP 성장률 추가 채널

---

## 11. Asset-Price Implications

**Bonds**
- [논문 간접 주장] BGP에서 실질이자율 일정: r* = α/β − 1 + g (성장률 g에 비례). 성장률 상승 시 실질금리 상승 → 채권 가격 하락

**Equities**
- [추론] BGP에서 주식 수익률 = 실질이자율 + 위험 프리미엄 → 성장률과 양의 관계; 경기 확장기 주가 상승과 일치

**FX**
- [해당 없음 — 폐쇄경제]

**Commodities**
- [해당 없음]

**Credit**
- [해당 없음]

> 반드시 [논문에서 직접 주장한 내용]과 [우리의 추론]을 구분한다.

---

## 12. Falsification Conditions

**What would confirm the hypothesis?**
- 장기 데이터에서 Kaldor 사실 성립 + 경기변동이 BGP 주변의 확률적 변동으로 해석 가능
- 노동 공급이 장기적으로 안정적임을 국가 횡단면에서 확인

**What would falsify the hypothesis?**
- 노동 시간이 1인당 소득과 함께 장기 증가 (BGP 불성립; Boppart & Krusell 2016: 일부 선진국에서 노동 시간 감소 관찰)
- KPR 형태 이외의 선호로 Kaldor 사실이 더 잘 설명됨

**Variables to monitor**
- 장기 노동 시간 추세, 자본/산출 비율 안정성, 실질이자율 장기 추세, 소비/소득 비율

---

## 13. Contradictory / Alternative Literature

**Supporting Papers**
- [[1982 Time to Build and Aggregate Fluctuations (Kydland & Prescott)]]: 동일 RBC 충격 구조
- [[1986 Theory Ahead of Business Cycle Measurement (Prescott)]]: 동일 캘리브레이션 방법론
- Rebelo (1991): KPR 모형 확장으로 내생 성장에서 조세 효과 분석

**Contradictory Papers**
- Boppart & Krusell (2016): "Labor supply in the past, present, and future" — 장기 노동 시간 변화 관찰, KPR 선호의 수정 필요
- [[1988 On the Mechanics of Economic Development (Lucas)]]: 인적자본 없는 BGP는 성장의 원천 설명 미흡

**Why do the results differ?**
- Time period: 장기 노동 시간 추세가 국가·시대마다 다름
- Country: 유럽에서 노동 시간 장기 감소 → BGP 이탈 관찰
- Data: 측정 기준에 따라 노동 시간 안정성 여부 상이
- Identification: 성장과 변동의 공통 구조 가정의 타당성
- Economic regime: 인적자본·제도 변화 시 BGP 자체 이동

---

## 14. Connections to Other Papers

**SUPPORTS**
- [[1982 Time to Build and Aggregate Fluctuations (Kydland & Prescott)]]: RBC 패러다임 공유·강화
- [[1986 Theory Ahead of Business Cycle Measurement (Prescott)]]: 동일 방법론

**CONTRADICTS**
- 성장과 변동을 분리된 모형으로 다루는 접근 비판

**EXTENDS**
- [[1956 A Contribution to the Theory of Economic Growth (Solow)]]: Solow BGP를 동적 최적화 + 경기변동 모형으로 통합
- [[1983 Real Business Cycles (Long & Plosser)]]: 다부문 RBC에 성장 구조 통합 가능성 제시

**CRITIQUES**
- 화폐 없는 실물 모형이 현실 경제의 명목 변동을 설명하지 못함을 간접 노출

**APPLIES**
- 현대 DSGE 모형의 표준 선호 구조(KPR preferences)로 직접 채택

---

## 15. Zettelkasten Atomic Notes

### ZK Note 1
**Claim:** KPR preferences가 BGP와 경기변동을 동시에 설명하는 효용 함수의 유일한 형태이다.

**Mechanism:** BGP에서 노동 공급이 일정하려면 소득효과 = 대체효과; 이는 U(c,l) = [c^α·(1−l)^(1−α)]^(1−σ)/(1−σ) 형태에서만 달성됨. 이것이 KPR preferences.

**Evidence:** [논문 직접] 수학적 증명: BGP와 동적 최적화를 동시에 만족하는 효용 함수의 필요 형태 도출

**Implication:** 모든 DSGE 모형에서 KPR(또는 그 특수 형태인 log-utility)가 표준 선호 구조로 채택됨; 파라미터 σ 추정이 거시 연구의 핵심 과제

**Connected Notes:** [[1982 Time to Build and Aggregate Fluctuations (Kydland & Prescott)]], [[1983 Real Business Cycles (Long & Plosser)]]

---

### ZK Note 2
**Claim:** Kaldor stylized facts가 BGP 이론의 경험적 기초이자 성장-변동 통합 모형의 구속 조건이다.

**Mechanism:** Kaldor(1961) 6가지 사실: ① 1인당 산출 지속 성장, ② 자본 스톡 지속 성장, ③ 실질이자율 안정, ④ 자본/노동 비율 상승, ⑤ 자본/산출 비율 안정, ⑥ 노동 소득 분배율 안정. KPR 모형이 이 모든 사실을 재현함.

**Evidence:** [논문 직접] 미국 장기 데이터로 Kaldor 사실 확인; 모형 시뮬레이션과 비교

**Implication:** 어떤 성장·경기변동 모형도 Kaldor 사실과 충돌하면 기각 가능; 이론의 강건성 체크리스트

**Connected Notes:** [[1956 A Contribution to the Theory of Economic Growth (Solow)]], [[1986 Theory Ahead of Business Cycle Measurement (Prescott)]]

---

### ZK Note 3
**Claim:** 성장과 경기변동은 분리된 현상이 아니라 동일한 실물 모형의 장기·단기 귀결이다.

**Mechanism:** 지속적 충격 → BGP 수준 이동(성장), 일시적 충격 → BGP 주변 변동(경기변동); 하나의 모형 구조에서 양자가 내생적으로 도출

**Evidence:** [논문 직접] 동일 파라미터로 장기 성장 사실과 단기 경기변동 사실을 동시 재현

**Implication:** 성장 정책과 안정화 정책을 분리하여 설계하는 것이 이론적으로 오류일 수 있음 → 통합적 정책 설계 필요; 현대 DSGE의 장기 균형 + 단기 변동 통합 구조의 이론적 정당화

**Connected Notes:** [[1982 Time to Build and Aggregate Fluctuations (Kydland & Prescott)]], [[1956 A Contribution to the Theory of Economic Growth (Solow)]], [[1990 Endogenous Technological Change (Romer)]]

---

## 16. One-Sentence Takeaway

이 논문을 한 문장으로 기억한다면: **경제성장과 경기변동은 사실 같은 모형의 장기와 단기 모습이며, 이 둘을 하나로 묶으려면 효용 함수가 아주 특별한 형태(KPR)여야 한다는 것을 밝혔다.**

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
