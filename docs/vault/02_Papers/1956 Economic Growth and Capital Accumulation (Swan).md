---
title: Economic Growth and Capital Accumulation
type: paper
journal: Economic Record, Vol. 32, No. 2 (Nov. 1956), pp. 334-361. DOI 10.1111/j.1475-4932.1956.tb00434.x
date: 1956
author: Trevor W. Swan (Australian National University)
created: 2026-08-12
updated: 2026-08-12
status: draft
verification: none
reliability: academic
verified: "❌ 원문 미확보 — Wiley 유료, Unpaywall 조회 결과 is_oa=false (2026-08-12). 본문은 카카오톡 수신 노트를 채택했고 원문 대조는 이뤄지지 않았다"
source_file: 없음
tags: [type/paper, domain/growth, method/미분방정식, flag/unverified]
concepts: [Solow-Swan, Swan-diagram, capital-widening, capital-deepening, steady-state]
related: ["[[1956 A Contribution to the Theory of Economic Growth (Solow)]]", "[[1988 On the Mechanics of Economic Development (Lucas)]]", "[[1992 A Contribution to the Empirics of Economic Growth (Mankiw, Romer & Weil)]]"]
import_origin: 카카오톡 수신 — Macro Paper Notes / 원본 파일명 'Swan (1956) — Economic Growth and Capital Accumulation.md'
JEL: 원문에 없음
---

> ⚠ **원문 미대조.** 본문은 외부 작성 노트를 수신해 규약 정규화한 것이다.
> **제텔로 분해하지 않았고, 수치를 다른 노트의 근거로 인용하지 않는다.**
> **단 2026-08-21 개정으로 「① 명제 층위」 인용은 허용된다** — 교과서적 정설을 수치 없이 인용할 때에 한하며,
> 인용 지점에 "원문 미대조"를 병기한다. → [[원문검증 논문 MOC]] 「인용 규칙 개정」

## 원문 확보 상태 (2026-08-12 시도 기록)

| 경로 | 결과 |
|---|---|
| Wiley Online Library | 유료 (기관 접근 필요) |
| Unpaywall API (DOI 10.1111/j.1475-4932.1956.tb00434.x) | `is_oa: false` — OA 사본 없음 |
| 대학 강의 페이지 사본 검색 | 실패 |

**확보 경로 제안**: 학교 도서관 Wiley 구독 / RISS 해외학술논문 신청 / Economic Record 아카이브.

## 원문 확보 시 최우선 대조 항목

1. **Swan 다이어그램의 축이 Solow Figure I과 실제로 같은가.** 통설은 "Swan은 저축률과 필요투자율을 **비율**로 그렸다"인데, 이 구조 차이가 정책 함의 차이를 만드는지 확인.
2. **감가상각 δ를 명시했는가.** [[1956 A Contribution to the Theory of Economic Growth (Solow)]] 원문은 "순산출"로 처리해 **δ가 식에 없다**(원문 대조 확인). 현대 교과서의 `ṙ = sf(r) − (n+δ)r`가 Solow가 아니라 **Swan에서 왔는지**가 이 항목의 핵심이다. 아래 본문도 (n+δ) 형태를 쓰고 있으므로 반드시 확인할 것.
3. **기술진보를 어떻게 도입했는가.** Solow의 힉스중립 A(t) 서술에는 내적 불일치가 있다(해당 노트 Red Team ①). Swan의 처리가 다르면 어느 쪽이 균형성장경로와 정합적인지 판정 가능.
4. **완전고용을 가정으로 넣었는지, 도출했는지.**
5. **오스트레일리아 자료를 썼는지** — 썼다면 Solow와 달리 실증 요소를 가진다.

## 왜 Solow와 같이 읽는가

두 사람이 **같은 해 다른 대륙에서 같은 결론**에 도달했다는 사실 자체가 정보다.
공유한 것은 자료가 아니라 **문제의식**(해로드-도마의 칼날)과 **도구**(규모수익불변 생산함수)였다.
즉 이 결론은 데이터가 아니라 **가정에서 나왔다**. 이는 Solow 노트 Red Team ④(데이터가 한 줄도 없다)와 같은 방향의 논점이다.

---

# Economic Growth and Capital Accumulation

## 1. Bibliographic Information

- **Title:** Economic Growth and Capital Accumulation
- **Authors:** Trevor W. Swan
- **Year:** 1956
- **Journal / Working Paper:** Economic Record, Vol. 32, No. 63, pp. 334–361
- **DOI / URL:** 10.1111/j.1475-4932.1956.tb00434.x
- **Research Field:** Growth Theory, Macroeconomics
- **Keywords:** neoclassical growth, capital accumulation, Swan diagram, steady state, factor substitution, exogenous growth

### One-Sentence Thesis
이 논문은 **가변적 요소 대체(탄력적 생산함수)**가 **자본-노동 비율의 자기조정 메커니즘**을 통해 **Harrod-Domar의 불안정 성장경로를 안정적 장기 균형으로 대체**할 수 있음을 보여준다.

---

## 2. Research Question

- **Question 1:** Harrod-Domar knife-edge 문제는 요소 대체를 허용하면 해소되는가?
- **Question 2:** 자본 축적과 인구 성장의 상호작용이 장기 균형을 어떻게 결정하는가?

---

## 3. Literature Gap

**Existing Literature**
- Harrod(1939)·Domar(1946): 고정 기술계수 생산함수 → knife-edge 불안정; 자본주의 경제의 만성 불안정을 예측

**Limitation**
- 요소 간 대체가 전혀 없다는 Leontief 가정은 현실과 거리가 있으며, 소폭의 파라미터 변화도 경제를 폭발적 팽창 또는 만성 실업으로 몰아넣음

**Contribution of This Paper**
- Solow(1956)와 동시 독립적으로 탄력적 생산함수를 도입하여 안정적 steady state를 도출; "Swan Diagram"이라는 그래픽 분석 도구를 통해 직관적으로 수렴 과정을 시각화

---

## 4. Core Mechanism

```
Cause / Shock: 저축률 변화 또는 인구증가율 충격
      ↓
1st-order Effect: 실제 자본-노동 비율(k)과 균형 비율(k*) 괴리 발생
      ↓
2nd-order Effect: 요소 간 대체(임금/자본비용 조정) → k가 k* 방향으로 이동
      ↓
3rd-order Effect: 저축 = 필요 투자 조건 달성
      ↓
Real Economy: 안정적 steady state 달성; 1인당 소득 수준 확정
```

**Economic Logic**
- Swan Diagram: 가로축 k(자본-노동 비율), 세로축 y(1인당 생산). 실제 저축곡선(s·f(k))과 필요 자본공급선((n+δ)·k)의 교점이 steady state. 교점의 안정성은 저축곡선의 기울기가 필요투자선보다 낮은 구간에서 보장됨.

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

**Primary Shock:** 외생적 기술 진보 (Solow와 동일 구조); 저축률 변화는 수준 효과만 발생

---

## 6. Transmission Mechanism

```
Shock: 인구증가율(n) 상승
  ↓
Transmission Channel: 1인당 자본량 희석(capital dilution) 효과
  ↓
Intermediate Variables: 실제 k vs 균형 k* 괴리, 요소 가격 조정
  ↓
Real Economy: 새로운 (낮은) steady state k* 달성, 1인당 소득 하락
  ↓
Financial Markets: [순수 실물 이론 모형]
```

**Explanation**
- Swan Diagram의 핵심: 두 곡선의 교점이 이동할 때 경제가 안정적으로 추적. 저축률 상승은 저축곡선을 위로 이동 → 새로운 더 높은 k* 달성 (수준 효과만). 기술 진보는 1인당 생산 함수 자체를 위로 이동시켜 지속적 성장 가능.

---

## 7. Key Variables

**Macroeconomic**
- 1인당 자본량 k = K/L
- 1인당 소득 y = f(k)
- 저축률 s, 인구증가율 n, 감가상각률 δ
- 외생적 기술 진보율 g

**Financial**
- 해당 없음

**Commodity**
- 해당 없음

**Leading / Coincident / Lagging**
- 자본량: lagging
- 1인당 소득: coincident with capital

---

## 8. Empirical Strategy

- **Data:** 이론 모형 (실증 없음)
- **Sample Period:** 해당 없음
- **Country / Region:** 해당 없음
- **Frequency:** 해당 없음
- **Method:** 그래픽 분석 (Swan Diagram), 수리 경제학
- **Identification Strategy:** 해당 없음
- **Main Model:** s·f(k) = (n+δ)·k → steady-state 조건 (Solow와 동일)

**Correlation or Causality?**
- 수학적 모형에서 인과관계 도출; 실증 없음

---

## 9. Main Findings

1. 요소 대체 탄력성이 양(+)이면 경제는 Harrod-Domar 불안정성 없이 steady state로 수렴.
2. Steady state k*는 저축률·인구증가율·기술 수준에 의해 결정되며 유일하고 안정적.
3. 저축률 상승은 1인당 소득 수준을 높이지만 장기 성장률은 기술진보율 g로 고정.
4. 인구 성장은 1인당 자본 희석(dilution)을 통해 1인당 소득을 낮춤.
5. Swan Diagram으로 비교 정학(comparative statics) 분석이 간결하게 가능함을 보임.

---

## 10. Regime Dependency

**When is the mechanism stronger?**
- 요소 대체 탄력성(σ)이 클수록 수렴이 빠르고 안정성 강화

**When is the mechanism weaker?**
- σ → 0 (Leontief 근접 시) Harrod-Domar 불안정성 재현; 지식경제에서 수확체감 가정 약화

**Does the conclusion change across regimes?**
- Solow와 동일한 결론; 내생성장(Romer/Lucas)으로 가면 저축률의 영구 성장효과 가능

---

## 11. Asset-Price Implications

**Bonds**
- [추론] Steady-state 실질이자율 = MPK − δ; 자본 심화(capital deepening)에 따라 장기 실질금리 하락 경향

**Equities**
- [추론] 수확체감 → 성숙 경제에서 주식 실질수익률 하락 압력

**FX**
- [해당 없음 — 폐쇄경제 모형]

**Commodities**
- [해당 없음]

**Credit**
- [해당 없음]

> 반드시 [논문에서 직접 주장한 내용]과 [우리의 추론]을 구분한다.

---

## 12. Falsification Conditions

**What would confirm the hypothesis?**
- 저축률이 다른 유사 국가들이 서로 다른 1인당 소득 수준으로 수렴(수준 효과 확인)
- 기술 진보율이 높은 국가가 장기 성장률 우위 지속

**What would falsify the hypothesis?**
- 저축률이 영구적으로 성장률에 영향을 준다면 Solow-Swan 가정 기각
- 국가 간 조건부 수렴이 존재하지 않을 경우

**Variables to monitor**
- 요소 대체 탄력성 추정치, 국가별 자본-산출 비율, β-수렴 계수

---

## 13. Contradictory / Alternative Literature

**Supporting Papers**
- [[1956 A Contribution to the Theory of Economic Growth (Solow)]]: 동일 결론, 동시 독립 발견
- Mankiw, Romer & Weil (1992): 인적자본 포함 Solow-Swan 실증 검증

**Contradictory Papers**
- [[1986 Increasing Returns and Long-Run Growth (Romer)]]: 수확불변·발산 가능성 제시
- [[1988 On the Mechanics of Economic Development (Lucas)]]: 인적자본 외부성으로 수렴 예측 기각

**Why do the results differ?**
- Time period: 해당 없음 (이론적 차이)
- Country: 해당 없음
- Data: 해당 없음
- Identification: 내생성장론은 지식의 비경합성 가정이 다름
- Economic regime: 지식집약 경제에서 수확체감 부적합

---

## 14. Connections to Other Papers

**SUPPORTS**
- [[1956 A Contribution to the Theory of Economic Growth (Solow)]]: 동일 모형 독립 도출

**CONTRADICTS**
- [[1986 Increasing Returns and Long-Run Growth (Romer)]]: 외생 기술진보 가정 비판
- [[1988 On the Mechanics of Economic Development (Lucas)]]: 수렴 예측 부정

**EXTENDS**
- [[1988 Production Growth and Business Cycles I - The Basic Neoclassical Model (King, Plosser & Rebelo)]]: Solow-Swan BGP를 경기변동 분석에 통합

**CRITIQUES**
- [[1990 Endogenous Technological Change (Romer)]]: 기술을 외생으로 두는 것 비판

**APPLIES**
- 해당 없음 (본 논문 자체가 응용)

---

## 15. Zettelkasten Atomic Notes

### ZK Note 1
**Claim:** Swan Diagram은 Solow 모형의 수렴 과정을 그래픽으로 직관화한다.

**Mechanism:** 가로축 k, 세로축 y·k. 저축곡선 s·f(k)와 필요투자선 (n+δ)k의 교점이 k*; 교점 좌측에서 k̇ > 0, 우측에서 k̇ < 0 → 수렴

**Evidence:** 수학적 논증 + 그래픽 분석

**Implication:** 비교 정학적 분석 도구로서 직관적 정책 분석 가능; 저축률·인구증가율 충격의 steady-state 효과를 즉시 파악

**Connected Notes:** [[1956 A Contribution to the Theory of Economic Growth (Solow)]]

---

### ZK Note 2
**Claim:** Solow와 Swan은 동시에 독립적으로 신고전파 성장 모형을 완성했다.

**Mechanism:** 동일한 생산함수 구조, 동일한 자본축적 방정식, 동일한 steady-state 결론 — 두 논문 모두 1956년 같은 해 출판

**Evidence:** 두 논문의 핵심 수식과 결론이 사실상 동일

**Implication:** "Solow-Swan Model"이라는 공동 명명; 서로 독립적으로 같은 결론에 도달했다는 사실이 이론의 강건성을 지지

**Connected Notes:** [[1956 A Contribution to the Theory of Economic Growth (Solow)]]

---

### ZK Note 3
**Claim:** 요소 대체 탄력성이 양수이기만 하면 Harrod-Domar 불안정성은 사라진다.

**Mechanism:** 생산함수가 탄력적이면 실질임금/이자율 조정을 통해 자본-노동 비율이 자동 조정됨 → knife-edge 조건 불필요

**Evidence:** CES/Cobb-Douglas 등 임의의 신고전파 생산함수에서 steady state 존재·유일·안정 수학적 증명

**Implication:** 성장의 불안정성은 생산기술의 문제이지 자본주의 체제의 본질적 결함이 아님; Keynesian 비관론(Harrod-Domar) 반박

**Connected Notes:** [[1956 A Contribution to the Theory of Economic Growth (Solow)]], [[1982 Time to Build and Aggregate Fluctuations (Kydland & Prescott)]]

---

## 16. One-Sentence Takeaway

이 논문을 한 문장으로 기억한다면: **요소 대체만 허용해도 Harrod-Domar의 "불안정한 자본주의" 결론은 사라지고, 경제는 자동으로 안정적 균형으로 수렴한다.**

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
