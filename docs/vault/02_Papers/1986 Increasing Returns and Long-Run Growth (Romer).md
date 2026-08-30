---
title: Increasing Returns and Long-Run Growth
type: paper
journal: Journal of Political Economy, Vol. 94, No. 5 (Oct. 1986), pp. 1002-1037. DOI 10.1086/261420
date: 1986
author: Paul M. Romer (University of Rochester 당시)
created: 2026-08-12
updated: 2026-08-12
status: draft
verification: none
reliability: academic
verified: "❌ 원문 미확보 — JPE 유료, Unpaywall 조회 결과 is_oa=false (2026-08-12). 본문은 카카오톡 수신 노트를 채택했고 원문 대조는 이뤄지지 않았다. 단 아래 '교차검증된 2건'은 다른 논문 원문에서 직접 확인함"
source_file: 없음
tags: [type/paper, domain/growth, method/최적제어, flag/unverified]
concepts: [increasing-returns, knowledge-spillover, non-convexity, divergence, learning-by-investment]
related: ["[[1988 On the Mechanics of Economic Development (Lucas)]]", "[[1990 Endogenous Technological Change (Romer)]]", "[[1956 A Contribution to the Theory of Economic Growth (Solow)]]"]
import_origin: 카카오톡 수신 — Macro Paper Notes / 원본 파일명 'Romer (1986) — Increasing Returns and Long-Run Growth.md'
JEL: 원문에 없음
---

> ⚠ **원문 미대조.** 본문은 외부 작성 노트를 수신해 규약 정규화한 것이다.
> **제텔로 분해하지 않았고, 수치를 다른 노트의 근거로 인용하지 않는다.**
> **단 2026-08-21 개정으로 「① 명제 층위」 인용은 허용된다** — 교과서적 정설을 수치 없이 인용할 때에 한하며,
> 인용 지점에 "원문 미대조"를 병기한다. → [[원문검증 논문 MOC]] 「인용 규칙 개정」

## 원문 확보 상태 (2026-08-12 시도 기록)

| 경로 | 결과 |
|---|---|
| JPE (University of Chicago Press) | 유료 |
| Unpaywall API (DOI 10.1086/261420) | `is_oa: false` |
| dklevine.com · klenow(Stanford) · 각 대학 강의 사본 | 직접 시도 모두 실패 |

## 교차검증된 2건 — 다른 논문 **원문에서 직접 읽은** 내용이라 신뢰 가능

**① Lucas(1988) 각주 12 (원문 대조 완료)**
> "외부효과가 있을 때의 균형행동에 대한 이 정식화는 Arrow(1962)와 Romer(1986)에서 가져왔다.
> Romer는 실제로 h(t) 경로 공간에서 **고정점 문제**를 푼다."

→ Romer(1986)의 기술적 기여 하나가 **외부효과 하 경쟁균형을 경로공간의 고정점으로 정식화**한 것임을 확인.

**② Romer(1990) 본문 (원문 대조 완료) — 저자 본인의 자기비판**
> "Arrow(1962)의 학습효과 모형과 나의 첫 모형(Romer 1986)에서 A의 성장률은 **가정에 의해 K의 성장률과 같도록 강제**되었다.
> 그 결과 투자세액공제처럼 K 축적을 늘리는 개입은 필연적으로 A의 축적도 늘렸다."

→ **이 논문을 "투자 촉진이 기술진보를 낳는다"의 근거로 쓰면 안 된다. 저자가 4년 뒤 스스로 철회한 고리다.**
→ 그 결합을 끊는 것이 [[1990 Endogenous Technological Change (Romer)]]의 핵심 진전이며, 두 논문은 **계승이 아니라 정정 관계**다.

## 원문 확보 시 최우선 대조 항목

1. 수확체증이 **지식의 외부효과**인가 **학습효과**인가.
2. **발산(divergence)** 을 실제로 주장하는가. Lucas(1988)는 이 논문을 인용하면서 **수준 격차의 영속성**만 가져간다.
3. **성장률이 시간에 따라 가속**하는가. 그렇다면 강한 반증가능 명제다 — 선진국 성장률은 20세기 내내 안정적이었다.
4. 고정점 정식화의 존재·유일성 조건.
5. 캘리브레이션이 있는가. 없다면 Solow(1956)와 같은 순수이론 논문으로 분류해야 한다.

---

# Increasing Returns and Long-Run Growth

## 1. Bibliographic Information

- **Title:** Increasing Returns and Long-Run Growth
- **Authors:** Paul M. Romer
- **Year:** 1986
- **Journal / Working Paper:** Journal of Political Economy, Vol. 94, No. 5, pp. 1002–1037
- **DOI / URL:** 10.1086/261420
- **Research Field:** Endogenous Growth Theory, Macroeconomics
- **Keywords:** knowledge spillover, increasing returns, endogenous growth, AK model, externality, Arrow learning-by-doing, competitive equilibrium, divergence, non-convexity

### One-Sentence Thesis
이 논문은 **지식(knowledge)의 비경합적·외부 효과적 속성**이 **집계 수준에서 수확불변 또는 수확체증**을 만들어내어 **기술 진보를 내생화하고 지속적 성장·국가 간 발산을 설명**한다는 것을 보여준다.

---

## 2. Research Question

- **Question 1:** 경쟁 균형에서 지속적인 1인당 성장이 가능한가, 그리고 그 원천은 무엇인가?
- **Question 2:** 지식의 외부 효과가 집계 생산성에 어떻게 수확불변을 부여하는가?

---

## 3. Literature Gap

**Existing Literature**
- Solow(1956)·Swan(1956): 수확체감 → 수렴, 장기 성장은 오직 외생 기술진보
- Arrow(1962) "learning by doing": 투자 경험이 지식을 생성하나 일반 균형 모형화 미완

**Limitation**
- 신고전파 성장론은 기술진보의 원천을 설명하지 못하고 외생으로 처리; 국가 간 영구적 소득 격차 설명 불가

**Contribution of This Paper**
- 지식을 생산요소로 명시 모형화하고, 지식의 비경합성(non-rivalry)이 개별 기업 수준의 수확체감·집계 수준의 수확불변을 동시에 허용함을 보임; 균형 성장률이 저축률·정책에 의해 내생적으로 결정됨을 도출

---

## 4. Core Mechanism

```
Cause / Shock: 개별 기업의 투자(자본 축적) 결정
      ↓
1st-order Effect: 개별 기업 지식(k_i) 증가 → 기업 생산성 상승
      ↓
2nd-order Effect: 지식 spillover → 집계 지식(K) 상승 → 모든 기업 생산성 향상
      ↓
3rd-order Effect: 집계 수준 수확불변 → 성장률의 지속적 양(+) 유지
      ↓
Real Economy: 영구적 성장, 수렴 없음, 선도 경제의 영구 우위
```

**Economic Logic**
- 개별 기업 생산함수: y_i = A·k_i^α·K^(1−α) (K: 집계 지식 = spillover)
- 개별 기업은 K를 외생으로 취급(경쟁적) → 사적으로는 α < 1 수확체감
- 집계 수준: Y = A·K (K = 합산 자본) → 수확불변 → AK 모형
- 성장률 = s·A − δ − n → 저축률(s)이 영구 성장률을 결정 (Solow와 근본적 차이)

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

**Primary Shock:** 지식 외부 효과(knowledge spillover)에 의한 집계 생산성 충격; 내생적 기술 진보

---

## 6. Transmission Mechanism

```
Shock: 저축률(s) 상승 → 투자 증가
  ↓
Transmission Channel: 자본 축적 → 지식 생성 → Spillover 발생
  ↓
Intermediate Variables: 집계 지식 K 상승, 모든 기업의 TFP 향상
  ↓
Real Economy: 성장률 영구 상승 (sA − δ − n 증가)
  ↓
Financial Markets: [추론] 고성장 기대 → 주식가치 상승, 실질금리 상승 가능
```

**Explanation**
- 핵심: 개별 기업이 투자할 때 지식이라는 공공재 성격의 부산물을 생산하고, 이것이 다른 기업으로 무상 이전(spillover). 이 외부 효과가 없으면 사적 최적 = 사회적 최적; 있으면 시장이 지식을 과소 생산 → 시장실패 → 저성장 균형.

---

## 7. Key Variables

**Macroeconomic**
- 집계 지식/자본 K, 개별 기업 지식 k_i
- 저축률 s (= 투자율)
- 성장률 γ = s·A − δ − n
- 집계 생산함수 Y = A·K

**Financial**
- [추론] 지식 외부성 → 사회 수익률 > 사적 수익률 → 시장 과소 투자
- 성장률 = s·A − (δ+n) → s가 높을수록 영구 성장률 상승 (Solow와 다름)

**Commodity**
- 해당 없음

**Leading / Coincident / Lagging**
- 투자율(s): 성장률 결정의 선행 변수
- 집계 지식(K): 누적 시계열로 성장 경로 결정

---

## 8. Empirical Strategy

- **Data:** 이론 모형 (직접 실증 없음); Arrow(1962) learning-by-doing 결과 참조
- **Sample Period:** 해당 없음
- **Country / Region:** 해당 없음
- **Frequency:** 해당 없음
- **Method:** 최적 성장 이론, 동태 최적화, 경쟁 균형 vs 사회적 최적 분석
- **Identification Strategy:** 해당 없음
- **Main Model:** AK형 모형; 균형 성장률 = s·A − δ − n

**Correlation or Causality?**
- 이론 모형에서 인과 구조 수학적 도출; 실증 식별 없음

---

## 9. Main Findings

1. 경쟁 균형에서도 내생적 지속 성장이 가능: 성장률 = s·A − δ − n > 0이면 발산.
2. 저축률(s)이 영구 성장률에 영향을 줌 → Solow의 "수준 효과만" 결론 반박.
3. 지식 외부성 → 시장실패: 분권화 균형 성장률 < 사회적 최적 성장률.
4. 수렴 없음: 초기에 더 많이 안 국가·기업이 영구적으로 앞서감.
5. 정부의 R&D 보조, 투자 세제 혜택이 영구 성장률을 제고할 수 있음 (정책 효과의 근본적 확대).

---

## 10. Regime Dependency

**When is the mechanism stronger?**
- 지식 집약 산업 비중이 높을수록; 특허 보호가 약해 spillover가 강할수록
- 집적 경제(agglomeration): 기업 밀집 지역에서 spillover 가속

**When is the mechanism weaker?**
- 지식 보호(특허·지식재산권)가 강해 spillover 차단되는 경우 → Romer(1990)으로 이어짐
- 물적자본 이동이 제한된 폐쇄 경제에서 외부 효과가 약화

**Does the conclusion change across regimes?**
- 특허·독점이 도입되면 외부 효과 채널이 약화되고 시장구조가 달라짐 → Romer(1990)의 독점적 경쟁 모형으로 진화

---

## 11. Asset-Price Implications

**Bonds**
- [추론] 성장률이 저축률에 연동 → 고저축 경제에서 실질금리 상승 가능 (Solow와 방향 다를 수 있음)

**Equities**
- [추론] 지식 외부성 → 사회 수익률 > 사적 수익률 → 주식가치가 사회적 최적 대비 과소평가
- [추론] 고성장 경로 진입 국가·섹터 주식은 복리로 장기 우위

**FX**
- [추론] 선도 경제(초기 지식 우위)의 통화는 장기 강세 경향

**Commodities**
- [해당 없음]

**Credit**
- [추론] 지식 자산의 담보화 어려움 → 지식집약 기업의 신용 접근 제약 (시장실패)

> 반드시 [논문에서 직접 주장한 내용]과 [우리의 추론]을 구분한다.

---

## 12. Falsification Conditions

**What would confirm the hypothesis?**
- 저축률·투자율이 높은 국가가 장기적으로 더 높은 성장률 유지
- 국가 간 소득 분산이 시간에 따라 확대 (절대적 발산)

**What would falsify the hypothesis?**
- 저축률이 성장률에 무관하고 오직 소득 수준만 결정 (Solow 지지)
- 지식 외부 효과를 직접 측정했을 때 통계적으로 유의하지 않음

**Variables to monitor**
- 저축률과 장기 성장률 cross-country 관계, R&D 지출과 TFP 성장, 지식 집적 지역의 성장 프리미엄

---

## 13. Contradictory / Alternative Literature

**Supporting Papers**
- [[1988 On the Mechanics of Economic Development (Lucas)]]: 외부 효과를 통한 내생 성장, 동일 방향
- Young (1991): learning-by-doing의 지식 spillover 경험적 지지

**Contradictory Papers**
- [[1956 A Contribution to the Theory of Economic Growth (Solow)]]: 수확체감 → 수렴, 저축률은 수준 효과만
- Mankiw, Romer & Weil (1992): 조건부 수렴 확인 → Solow 지지

**Why do the results differ?**
- Time period: 수렴 여부는 국가 샘플·기간에 민감
- Country: 선진국만 보면 수렴 관찰; 전체 국가에서는 발산
- Data: 지식 외부성의 직접 측정 극히 어려움
- Identification: spillover의 인과적 추정 요구
- Economic regime: 규모의 경제 존재 여부가 핵심 실증 질문

---

## 14. Connections to Other Papers

**SUPPORTS**
- [[1988 On the Mechanics of Economic Development (Lucas)]]: 동일하게 외부 효과 기반 내생 성장 주장

**CONTRADICTS**
- [[1956 A Contribution to the Theory of Economic Growth (Solow)]]: 수확체감·수렴 가정 정면 도전
- [[1956 Economic Growth and Capital Accumulation (Swan)]]: 동일

**EXTENDS**
- Arrow (1962) "learning-by-doing"을 일반 균형 성장 모형으로 확장

**CRITIQUES**
- [[1956 A Contribution to the Theory of Economic Growth (Solow)]]: 기술진보 외생 처리의 설명력 한계 비판

**APPLIES**
- [[1990 Endogenous Technological Change (Romer)]]: 본 논문의 지식 외부성을 명시적 R&D 모형으로 발전

---

## 15. Zettelkasten Atomic Notes

### ZK Note 1
**Claim:** 지식의 비경합성(non-rivalry)이 집계 수준의 수확불변을 가능하게 한다.

**Mechanism:** 지식은 동시에 여러 기업이 사용 가능(비경합적) → 기업 수 증가 시 지식 비용 0으로 복제 → 집계 규모에 수확불변 또는 체증

**Evidence:** 생산함수 동차성 분석: 개별 기업 1차 동차, 집계 수준 1차 동차 이상

**Implication:** 지식경제에서는 독점적 경쟁이 자연스럽게 발생; 완전경쟁 가정이 부적합 → Romer(1990)으로 진화

**Connected Notes:** [[1990 Endogenous Technological Change (Romer)]], [[1988 On the Mechanics of Economic Development (Lucas)]]

---

### ZK Note 2
**Claim:** 저축률이 영구 성장률을 결정한다 — Solow와의 근본적 차이.

**Mechanism:** AK 모형: γ = s·A − δ − n; s↑ → γ↑ (수준이 아닌 성장률 효과)

**Evidence:** 집계 생산함수 Y = AK에서 수학적으로 도출

**Implication:** 저축 장려 정책이 장기 성장률을 영구적으로 높일 수 있음 → 정책 레버리지가 Solow보다 훨씬 큼

**Connected Notes:** [[1956 A Contribution to the Theory of Economic Growth (Solow)]], [[1990 Government Spending in a Simple Model of Endogenous Growth (Barro)]]

---

### ZK Note 3
**Claim:** 지식 외부성에 의한 시장실패로 사회 최적보다 과소 성장한다.

**Mechanism:** 개별 기업은 spillover(외부 효과) 고려 없이 투자 결정 → 사회적 한계 생산 > 사적 한계 생산 → 과소 투자

**Evidence:** 분권화 균형 성장률 < 사회적 최적 성장률 (수리 증명)

**Implication:** R&D 보조금·투자 세제 혜택이 파레토 개선을 달성할 수 있음; 자유 시장만으로는 충분한 혁신 달성 불가

**Connected Notes:** [[1988 On the Mechanics of Economic Development (Lucas)]], [[1990 Endogenous Technological Change (Romer)]], [[1990 Government Spending in a Simple Model of Endogenous Growth (Barro)]]

---

## 16. One-Sentence Takeaway

이 논문을 한 문장으로 기억한다면: **지식은 공공재처럼 퍼져나가기 때문에 저축과 투자가 증가하면 사회 전체 생산성이 함께 올라가고, 이것이 왜 열심히 저축하는 나라가 영구적으로 더 빠른 성장을 누리는지를 설명한다.**

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
