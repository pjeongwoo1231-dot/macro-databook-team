---
title: A Contribution to the Empirics of Economic Growth
type: paper
journal: Quarterly Journal of Economics, Vol. 107, No. 2, pp. 407–437. DOI/URL 10.2307/2118477
date: 1992
author: N. Gregory Mankiw, David Romer, David N. Weil
created: 2026-08-12
updated: 2026-08-12
status: done
verification: full
reliability: academic
verified: "✅ 2026-08-21 원문 전문 대조. 저자(David Romer) 배포본 PDF 31p, Table I·II·V·VI 직접 확인. 임포트 노트의 수치 오류 5건 정정 — 아래 대조 기록 참조"
source_file: Attachments/mankiw_romer_weil1992.pdf (eml.berkeley.edu/~dromer/papers/MRW_QJE1992.pdf)
text_basis: 원문 PDF 전문 (PyMuPDF 추출, 텍스트 레이어 정상)
tags: [type/paper, domain/growth, region/emerging, method/횡단면회귀, method/조건부수렴검정]
concepts: [augmented-Solow, human-capital, conditional-convergence, Summers-Heston]
import_origin: 카카오톡 수신 — Macro Paper Notes / 원본 파일명 'Mankiw, Romer & Weil (1992) — A Contribution to the Empirics of Economic Growth.md'
---
> ✅ **2026-08-21 원문 전문 대조 완료.** `verification: full` — **수치 인용 가능.**
> 대조본: 저자 David Romer 배포 PDF(QJE 107(2), 407–437, 31p). Table I·II·V·VI 직접 확인.

## ⚠ 대조에서 정정한 것 (임포트 노트의 오류 5건)

이 노트는 2026-08-12 카카오톡 수신본이었다. 원문과 맞춰 보니 **아래가 틀렸다.**
2차 노트가 어떻게 틀리는지 보여주는 사례라 삭제하지 않고 기록으로 남긴다.

| # | 임포트 노트의 서술 | 원문 | 성격 |
|---|---|---|---|
| 1 | 수렴속도 **λ ≈ 0.0228 추정** | **원문에 그런 값이 없다.** 실제 implied λ = 0.0137(비산유)·0.0182(중간)·0.0203(OECD) | **날조** |
| 2 | 2%/년은 "추정" | 2%는 α=β=1/3, n+g+δ=0.06을 **대입한 이론 예측치**. 반감기 35년도 예측 | 예측↔추정 혼동 |
| 3 | 단순 Solow에서 **α̂ ≈ 0.59** | 0.59는 **R²**다. 비산유 implied α는 **0.60**(0.02) | R²와 계수 혼동 |
| 4 | 표본 = "98개국(비산유 75 + OECD 22)" | **세 개의 별도 표본**: 비산유 98 · 중간 75 · OECD 22 | 표본 구조 오해 |
| 5 | 설명력 낮은 곳 = "아프리카 저소득국" | **OECD 표본**이다. Table I R² = **0.01**, Table II = 0.24 | **방향 반대** |

추가 확인: MRW는 g와 δ를 따로 놓지 않았다. **g+δ = 0.05를 통째로 가정**하고
*"reasonable changes in this assumption have little effect"* 라고 적었다.
(g=0.02·δ=0.03 분해는 원문의 가정이 아니라 §III 예시 계산의 n+g+δ=0.06에서 온 것이다.)

# A Contribution to the Empirics of Economic Growth

## 1. Bibliographic Information

- **Title:** A Contribution to the Empirics of Economic Growth
- **Authors:** N. Gregory Mankiw, David Romer, David N. Weil
- **Year:** 1992
- **Journal / Working Paper:** Quarterly Journal of Economics, Vol. 107, No. 2, pp. 407–437
- **DOI / URL:** 10.2307/2118477
- **Research Field:** Growth Empirics, Development Economics, Macroeconomics
- **Keywords:** Solow model, augmented Solow, human capital, conditional convergence, cross-country regression, growth regression, β-convergence, steady state, Mankiw-Romer-Weil

### One-Sentence Thesis
이 논문은 **인적자본(교육 투자)을 포함한 확장 Solow 모형**이 **국가 횡단면 회귀분석**을 통해 **국가 간 1인당 소득 격차의 약 78%를 설명하며 조건부 수렴을 확인**한다는 것을 보여준다.

---

## 2. Research Question

- **Question 1:** Solow 모형이 국가 간 1인당 소득 격차를 실증적으로 설명할 수 있는가?
- **Question 2:** 인적자본을 포함한 확장 Solow 모형이 내생성장론(Romer, Lucas)보다 데이터를 더 잘 설명하는가?

---

## 3. Literature Gap

**Existing Literature**
- [[1956 A Contribution to the Theory of Economic Growth (Solow)]]: 이론 모형이나 체계적 실증 검증 부재
- [[1986 Increasing Returns and Long-Run Growth (Romer)]], [[1988 On the Mechanics of Economic Development (Lucas)]]: 내생성장론은 수렴 부정; Solow 반박

**Limitation**
- Solow 모형의 실증 검증이 체계적으로 이루어지지 않았으며, 인적자본 누락에 따른 추정 편의(omitted variable bias) 문제가 미해결

**Contribution of This Paper**
- 98개국 횡단면 데이터를 이용한 체계적 실증; 인적자본 누락 시 Solow의 물적자본 계수가 과대 추정됨을 보임; 확장 Solow가 수렴 속도·소득 수준 모두 잘 예측하며 조건부 수렴 확인

---

## 4. Core Mechanism

```
Cause / Shock: 국가별 저축률(s)·인적자본 투자(s_h)·인구증가율(n) 차이
      ↓
1st-order Effect: 국가별 물적자본·인적자본 steady state 수준 차이
      ↓
2nd-order Effect: Steady state 1인당 소득 수준 격차 발생
      ↓
3rd-order Effect: 각국이 자국 steady state로 수렴 (조건부 수렴)
      ↓
Real Economy: 초기 소득이 낮아도 steady state가 높으면 빠른 성장 (조건부 수렴)
```

**Economic Logic**
- 확장 생산함수: Y = K^α · H^β · (AL)^(1−α−β)
- Steady state 1인당 소득: ln(y*) = ln(A) + gt − [(α+β)/(1−α−β)]ln(n+g+δ) + [α/(1−α−β)]ln(s_k) + [β/(1−α−β)]ln(s_h)
- 실증 추정: α ≈ 1/3, β ≈ 1/3 → 물적·인적자본의 산출 탄력성 각 1/3; 총 자본 탄력성 2/3

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

**Primary Shock:** 저축률·인적자본 투자율·인구증가율의 국가 간 구조적 차이 (파라미터 이질성)

---

## 6. Transmission Mechanism

```
Shock: 저축률 또는 인적자본 투자율 변화
  ↓
Transmission Channel: 물적·인적자본 축적 경로 변화 → steady state 변화
  ↓
Intermediate Variables: 자본-노동 비율, 인적자본 스톡
  ↓
Real Economy: 1인당 소득 수준 및 성장률 변화 (이행 과정 중)
  ↓
Financial Markets: [추론] 인적자본·물적자본 수익률 격차 → 자본 이동 결정
```

**Explanation**
- 핵심 실증 결과: 단순 Solow(R²=0.59) → 확장 Solow(R²=0.78). 인적자본 프록시로 중등교육 취학률 사용. 수렴 속도 추정: 연 2%/년 (조건부 수렴 속도).

---

## 7. Key Variables

**Macroeconomic**
- 물적자본 저축률 s_k (투자/GDP)
- 인적자본 투자율 s_h (중등교육 취학률 × 근로연령 비율)
- 인구증가율 n, **g + δ = 0.05 (원문 가정 — g와 δ를 따로 놓지 않는다)**
- 1인당 실질 GDP (Penn World Tables)

**Financial**
- [추론] 물적자본 수익률: 저자본·저인적자본 국가에서 높을 것이나 Lucas Paradox로 자본 유입 없음

**Commodity**
- 해당 없음

**Leading / Coincident / Lagging**
- 저축률·교육 투자: leading (steady state 결정)
- 1인당 소득: lagging (수렴 과정 길어짐)

---

## 8. Empirical Strategy

- **Data:** Penn World Tables (Summers & Heston), UNESCO 교육 데이터. **세 개의 별도 표본: 비산유 98 · 중간 75 · OECD 22**
- **Sample Period:** 1960–1985
- **Country / Region:** 비산유 98 / 중간 75 / OECD 22 — **표본마다 결과가 갈린다**
- **Frequency:** 25년 평균값 (장기 평균으로 단기 변동 제거)
- **Method:** OLS 횡단면 회귀 (cross-country regression); 제한 회귀(restricted regression)로 이론 계수 비율 검증
- **Identification Strategy:** 저축률·인구증가율을 외생적으로 가정; OLS (내생성 문제 인정하나 IV 미사용)
- **Main Model:** ln(y_i) = α_0 + α_1·ln(s_k) + α_2·ln(s_h) − α_3·ln(n+g+δ) + ε_i

**Correlation or Causality?**
- [논문 직접 인정] OLS 추정 → 저축률 내생성 문제 존재; 조건부 상관관계에 가까움. 저축률의 진정한 외생적 결정 요인 미분리.

---

## 9. Main Findings

*(2026-08-21 원문 대조 완료 — 표 번호와 표본을 명시한다)*

1. **[Table I·II, 비산유 98]** 교과서 Solow R² = 0.59 → 확장 Solow R² = **0.78**.
2. **[Table II, 비산유]** implied α = **0.31** (0.04), β = **0.28** (0.03).
   α+β ≈ 0.59 < 1 → **수확체감 유지**(내생성장 α+β=1과 갈리는 지점).
3. **[Table I, 비산유]** 인적자본 누락 시 implied α = **0.60** (0.02) — 자본소득분배율 1/3의 약 두 배.
4. **[Table V, 조건부수렴]** implied λ = **0.0137**(비산유) · 0.0182(중간) · 0.0203(OECD).
   **연 2%는 이론 예측치이고 추정치가 아니다.** 반감기 35년도 예측값이다.
5. **[Table VI, 제약 수렴회귀]** implied α = **0.48** (0.07), β = 0.23 (0.05) —
   **Table II의 0.31/0.28과 다르다.** 정상상태 가정을 푸느냐가 값을 가른다.
6. **[Table I·II, OECD 22]** R² = **0.01** → 0.24, implied α = 0.14 (s.e. 0.15, 유의하지 않음).
   **선진국 표본에서는 수준 회귀가 작동하지 않는다.**

## 10. Regime Dependency

**When is the mechanism stronger?**
- 초기 자본 희소 국가 + 높은 교육 투자: 빠른 수렴 속도
- 제도·거버넌스가 양호하여 저축이 실제 자본 축적으로 연결될 때

**When is the mechanism weaker?**
- 교육의 질이 취학률로 측정되지 않는 경우 (측정 오류)
- 인적자본의 외부 효과가 강하면 Solow 예측이 빗나감 (Lucas 지지)

**Does the conclusion change across regimes?**
- **OECD 표본에서 수준 회귀가 무너진다**(Table I R² = 0.01 / Table II 0.24). 반면 **수렴 회귀는 OECD가 가장 잘 맞는다**(Table V R² 0.65). MRW는 이를 2차대전발 정상상태 이탈로 설명한다.
- ⚠ 임포트 노트의 "아프리카 저소득국에서 설명력 낮음"은 **원문과 반대**였다(2026-08-21 대조).

---

## 11. Asset-Price Implications

**Bonds**
- [추론] 조건부 수렴 → 신흥국의 잠재 성장률이 선진국보다 높음 → 신흥국 국채의 장기 실질금리 상승 가능성

**Equities**
- [추론] Steady state 소득이 높은 국가(고저축·고교육)의 주식시장 장기 우위 예측

**FX**
- [추론] 조건부 수렴 과정에서 성장률이 높은 신흥국 통화는 장기 실질절상 경향

**Commodities**
- [해당 없음]

**Credit**
- [추론] 인적자본 높은 국가: 신용 접근성 양호 (생산성·소득 높음)

> 반드시 [논문에서 직접 주장한 내용]과 [우리의 추론]을 구분한다.

---

## 12. Falsification Conditions

**What would confirm the hypothesis?**
- 저축률·교육·인구증가율을 통제한 후 초기 소득과 성장률 간 음(−) 관계 유지 (조건부 수렴)
- α+β ≈ 2/3: 자본 소득 분배율의 이론 예측과 데이터 일치

**What would falsify the hypothesis?**
- 저축률이 성장률과 무관 → 내생성장 지지
- 통제 후에도 수렴 없음 → 다중 균형 또는 외부 효과 지배
- Islam (1995) 패널 분석: 국가 고정효과 포함 시 수렴 속도 급상승 (~9%/년) → MRW 추정치 과소 편의 가능성

**Variables to monitor**
- 교육의 질 지표(PISA 등), 저축률의 내생적 결정 요인, 제도·거버넌스 지표 통제 후 수렴 계수

---

## 13. Contradictory / Alternative Literature

**Supporting Papers**
- Barro & Sala-i-Martin (1992): 미국 주(州) 간 절대 수렴 확인
- Islam (1995): 패널 분석으로 MRW 수렴 확인하나 속도는 더 높음

**Contradictory Papers**
- [[1986 Increasing Returns and Long-Run Growth (Romer)]]: 수렴 없음, 내생 성장
- Pritchett (1997): "Divergence, Big Time" — 국가 간 소득 격차 장기 확대; Solow 수렴 예측 기각
- Quah (1993): bimodal 소득 분포 ("Twin Peaks") → 중간 소득 함정

**Why do the results differ?**
- Time period: 1960–85 vs. 이후 기간에서 수렴 패턴 상이
- Country: 아프리카 제외 샘플과 전체 샘플 결과 다름
- Data: 교육 투자 측정(취학률 vs. 학업 성취도) 방법 차이
- Identification: 저축률 내생성 → IV 추정치 상이할 가능성
- Economic regime: 제도·거버넌스 이질성이 핵심 교란 요인

---

## 14. Connections to Other Papers

**SUPPORTS**
- [[1956 A Contribution to the Theory of Economic Growth (Solow)]]: Solow 이론의 체계적 실증 지지
- [[1956 Economic Growth and Capital Accumulation (Swan)]]: Solow-Swan 모형의 실증적 타당성 확인

**CONTRADICTS**
- [[1986 Increasing Returns and Long-Run Growth (Romer)]]: 내생성장의 발산 예측 반박
- [[1988 On the Mechanics of Economic Development (Lucas)]]: 인적자본 외부성 불필요; 사적 수익만으로 충분

**EXTENDS**
- [[1956 A Contribution to the Theory of Economic Growth (Solow)]]: 인적자본 추가로 설명력 대폭 개선

**CRITIQUES**
- [[1986 Increasing Returns and Long-Run Growth (Romer)]], [[1988 On the Mechanics of Economic Development (Lucas)]]: 이론적으로 흥미롭지만 데이터 설명력이 확장 Solow보다 낮다고 주장

**APPLIES**
- Barro (1991): 성장 회귀의 광범위한 실증 응용

---

## 15. Zettelkasten Atomic Notes

**2026-08-21 분해 완료 — `04_Zettel/`에 4건.** 아래 초안(임포트 노트의 ZK Note 1~3)은
수치 오류를 포함하고 있어 폐기하고, 원문 대조본으로 다시 썼다.

1. [[인적자본을 빼면 자본 탄력성이 두 배로 부풀려진다 — α 0.60 vs 0.31]] — 누락변수편의
2. [[MRW의 수렴속도 2퍼센트는 추정치가 아니라 이론 예측치다]] — **판정규칙**(2차 문헌 거르기)
3. [[같은 논문이 표에 따라 자본 탄력성을 0.31로도 0.48로도 보고한다]] — **판정규칙**(표 번호 요구)
4. [[확장 Solow의 설명력 78퍼센트는 OECD 표본에서 무너진다 — R² 0.01]] — 표본의존성

> 폐기한 초안의 오류: ZK1이 R²(0.59)를 계수 α로 적었고, ZK3이 원문에 없는 λ=0.0228을 실었다.

## 16. One-Sentence Takeaway

이 논문을 한 문장으로 기억한다면: **사람에 대한 투자(교육)까지 포함하면 Solow 모형 하나로 전 세계 국가 간 소득 격차의 78%를 설명할 수 있으며, 가난한 나라도 저축하고 교육하면 부유한 나라를 따라잡는다.**

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
