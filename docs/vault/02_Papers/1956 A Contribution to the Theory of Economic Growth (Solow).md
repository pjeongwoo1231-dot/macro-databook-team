---
title: A Contribution to the Theory of Economic Growth
type: paper
journal: The Quarterly Journal of Economics, Vol. 70, No. 1 (Feb. 1956), pp. 65-94. DOI 10.2307/1884513
date: 1956
author: Robert M. Solow (MIT)
created: 2026-08-12
updated: 2026-08-12
status: done
verification: full
reliability: academic
verified: 원문 전문 정독 완료(2026-08-12, JSTOR 스캔 30p — I~VII절 전 절 대조. §VI 기술진보 확장의 성장률 서술에서 내적 불일치 1건 발견, 아래 Red Team ① 참조)
source_file: macro_classics/solow1956.pdf
tags: [type/paper, domain/growth, region/us, method/미분방정식, method/비교정학]
concepts: [Solow-model, Harrod-Domar, knife-edge, capital-labor-ratio, constant-returns, variable-proportions, balanced-growth, Inada]
related: ["[[1956 Economic Growth and Capital Accumulation (Swan)]]", "[[1988 On the Mechanics of Economic Development (Lucas)]]", "[[1986 Increasing Returns and Long-Run Growth (Romer)]]", "[[1990 Endogenous Technological Change (Romer)]]", "[[1982 Time to Build and Aggregate Fluctuations (Kydland & Prescott)]]"]
JEL: 원문에 없음(1956년 논문)
---

# A Contribution to the Theory of Economic Growth (Solow, 1956)

> **이 논문의 주장은 "저축이 성장을 만든다"가 아니다. 정반대다 — "저축은 성장률을 못 바꾼다"이다.**
> 그리고 이 결론은 실증이 아니라 **가정 하나를 바꿔서** 나온다: 고정계수 → 가변계수.

## 1. Bibliographic Information / One-Sentence Thesis

- **Title**: A Contribution to the Theory of Economic Growth
- **Author**: Robert M. Solow
- **Year**: 1956 / **Journal**: QJE 70(1), 65-94
- **Field**: 성장이론 · **Keywords**: 신고전파 성장모형, 해로드-도마, 요소대체, 균형성장경로

**One-Sentence Thesis**
이 논문은 **자본-노동 대체가능성**이 **자본-노동비율 r의 자기조정**을 통해 **해로드-도마의 "칼날 위 균형"을 소멸시킨다**는 것을 보여준다.

## 2. Research Question

- **Q1**: 해로드-도마의 불안정성(자연성장률 n ≠ 보증성장률 s/C면 실업 또는 인플레가 누적)은 **모형의 결론인가, 가정의 산물인가?**
- **Q2**: 고정계수 대신 가변계수(신고전파 생산함수)를 넣으면 완전고용 성장경로가 존재하고 **안정적인가?**

## 3. Literature Gap

**Existing Literature**
- Harrod-Domar 계열: 장기 문제를 **단기 도구**(승수·가속도계수·"그" 자본계수)로 다룬다. 저자가 직접 지적한 특징이다.
- Solow-Samuelson(1953) 균형성장 정리.

**Limitation**
- 해로드-도마의 칼날 결론은 **"고정비율 생산(요소 대체 불가)"이라는 crucial assumption 하나**에 전적으로 의존한다. 저자의 서두 표현: "결과가 특정한 crucial assumption에서만 흘러나온다면, 그 가정이 의심스러울 때 결과도 의심스럽다."

**Contribution of This Paper**
- 해로드-도마의 **모든 가정을 유지한 채 고정비율만 제거**해 결론이 뒤집힘을 보인다. 이것이 이 논문의 방법론적 핵심이다 — 반박이 아니라 **가정의 국소적 해체**.
- 부수적으로 임금·이자·기술진보·탄력적 노동공급·조세·내생적 인구증가까지 같은 도식(Figure I)으로 확장한다.

## 4. Core Mechanism

```
자본-노동 대체 허용 (요소 가변비율)
 ↓
1st-order: 한계생산성 체감 → 자본이 노동보다 빨리 쌓이면 자본수익률 하락
 ↓
2nd-order: 실질임금 ↑ · 실질임대료 ↓ (요소가격이 r로만 결정)
 ↓
3rd-order: 저축·투자 sF(r,1)가 필요증가분 nr에 수렴 → ṙ → 0
 ↓
실물경제: 균형성장 r* 로 수렴, 이후 K·L·Y가 모두 n으로 성장
```

**핵심 미분방정식 (원문 식 (6))**

$$\dot r = sF(r,1) - nr, \qquad r \equiv K/L$$

`sF(r,1)` 곡선과 `nr` 직선의 교점이 r\*이며, 교점에서 **보증성장률 = 자연성장률**이 "행운이 아니라 수요-공급 조정의 결과"로 성립한다.

**Economic Logic**
칼날이 사라지는 이유는 **가격이 수량을 조정하기 때문**이 아니라, **기술 자체가 비율을 조정할 여지를 주기 때문**이다. 저자는 두 관점을 명시적으로 분리한다 — (i) 실업·과잉설비가 안 생기려면 자본이 따라가야 할 경로, (ii) 그 경로를 실제로 만들어내는 시장행태(임금·임대료·이자의 완전신축).

**Cobb-Douglas 특수해** (Y = K^a L^{1-a}): r\* = (s/n)^{1/(1-a)}, Y/L → (s/n)^{a/(1-a)}, **K/Y = s/n**.

## 5. Shock Classification

- [x] **Technology Shock** (§VI 확장에서 A(t) 도입)
- [x] **Productivity Shock**
- [ ] Demand / Monetary / Credit / Financial / Commodity / Trade / Capital Flow
- [x] Fiscal Shock (§VI 조세 확장 — 세율 t, 재투자 비율 v)
- [x] Expectation Shock (§VII 유동성선호·투자 불확실성 — 다만 "여기서는 다루지 않는다"고 명시)

**Primary Shock**: 없음(정상상태 비교정학 모형). 충격이 아니라 **파라미터 s·n·A의 수준 변화**를 다룬다.

## 6. Transmission Mechanism

```
저축률 s ↑
 ↓ 전달경로: sF(r,1) 곡선의 상방 확대(uniform blow-up)
 ↓ 중간변수: 균형 자본-노동비율 r* ↑, 자본계수 K/Y = s/n ↑
 ↓ 실물경제: 1인당 소득 수준 ↑ — 그러나 장기 성장률은 여전히 n
 ↓ 금융시장: 균형 실질임대료 q/p = an/s ↓, 실질임금 (1−a)(s/n)^{a/(1−a)} ↑
```

**Explanation**
s의 변화는 **level effect이지 growth effect가 아니다.** 조세 확장에서도 동일하다 — 비례소득세는 실효저축률을 `s + (v−s)t`로 옮길 뿐이며, 정부가 민간보다 더 투자하느냐(v > s)가 방향을 정한다. **재정정책은 곡선을 위아래로 옮기지, 기울기를 못 바꾼다.**

## 7. Key Variables

**Macroeconomic**: [[GDP 성장률]] · [[잠재성장률]] · [[총요소생산성 (TFP)]] · 자본-노동비율 r · 인구증가율 n · 저축률 s
**Financial**: 실질이자율 i, 자본의 실질임대료 q/p — 원문 식 (12) `i = q/p − (dp/dt)/p` 로 명목이자율과 자기이자율(own-rate)이 연결된다.
**Commodity**: 없음(단일 복합재 모형)
**Leading / Coincident / Lagging**: 해당 없음 — 이 논문의 시간 개념은 순환이 아니라 **점근적 수렴**이다. 저자 스스로 반감기 개념을 쓰지 않으며, [[1988 On the Mechanics of Economic Development (Lucas)]]가 같은 구조에 "반감기 약 11년"을 붙인다.

## 8. Empirical Strategy

- **Data**: 없음 — **순수 이론논문이다.** 표도, 회귀도, 국가자료도 없다.
- **Sample Period / Country / Frequency**: 해당 없음
- **Method**: 1계 미분방정식의 정성적 해석 + 3개 생산함수 예시(고정계수 · Cobb-Douglas · CES p=1/2)
- **Identification Strategy**: 없음
- **Main Model**: `ṙ = sF(r,1) − nr`

**Correlation or Causality?**
**둘 다 아니다.** 이 논문에는 실증적 인과 주장이 없다. 여기서 나오는 "s는 성장률에 영향이 없다"는 **모형 내부의 논리적 귀결**이지 데이터에서 추출한 인과가 아니다.
→ 이 구분이 실무에서 자주 무너진다. "솔로우 모형이 보여줬다"고 인용되는 것 대부분은 [[1988 On the Mechanics of Economic Development (Lucas)]]나 Mankiw-Romer-Weil(1992) 같은 **후속 실증**의 결과다.

## 9. Main Findings

1. **가변비율 + 규모수익불변 하에서 자연/보증 성장률의 대립은 성립하지 않는다.** Cobb-Douglas의 경우 칼날은 **결코** 존재할 수 없다.
2. **균형 r\*는 안정적**이며 초기 자본스톡과 무관하게 수렴한다(Figure I).
3. **그러나 안정성은 필연이 아니다.** 저자는 곧바로 세 가지 예외를 그린다 — 복수균형(Figure II: r₁·r₃ 안정, r₂ 불안정), 균형 부재(Figure III: 무한 성장 또는 영구 빈곤화), 내생적 인구증가 하의 빈곤함정(Figure IX).
4. **장기 1인당 성장률은 s와 무관**하고 오직 기술진보 g에만 의존한다(§VI).
5. **Keynes적 경직성은 칼날을 되살린다** — §VII에서 실질임금을 r̄에 고정하면 `s/r̄·F(r̄,1) < n`일 때 실업이 누적적으로 증가한다. 즉 **불안정성은 생산기술이 아니라 가격경직성에서 온다**는 것이 저자의 최종 위치다.

## 10. Regime Dependency

**When is the mechanism stronger?**
- **요소대체탄력성이 클수록** 조정이 빠르다. 저자가 명시: "장기적으로 요소비율이 널리 가변적일수록 [균형이 존재하는] 중간 구간이 넓어진다."
- 실질임금·이자가 신축적일수록.

**When is the mechanism weaker?**
- 실질임금 경직 → r이 r̄에 고정 → 안정화 메커니즘 정지, 해로드형 불안정 부활(§VII 원문).
- **유동성함정** — 이자율이 하한에 걸리면 자본의 과소가동이 발생하고, 저자는 여기서 **"실물 신고전파 모형으로 기술하려는 시도의 무익함이 명백해진다"** 고 스스로 인정하며 화폐동학의 필요를 인정한다.
- 저축률이 이자에 반응하면(s(r)) 조정이 **더 안정화**된다(r 높으면 저축 위축).

**Does the conclusion change across regimes?**
**바뀐다, 그리고 저자가 먼저 말한다.** 이 논문의 §VII은 "위의 모든 것은 동전의 신고전파 면"이라는 문장으로 시작한다. 완전고용을 가정한 것이지 증명한 것이 아니다.

## 11. Asset-Price Implications

> ⚠ 아래는 **[논문에서 직접 주장한 내용]** 과 **[우리의 추론]** 을 분리해 적는다.

**Bonds** — [논문] 균형성장에서 실질임대료 q/p = an/s로 **상수**에 수렴한다. 자본축적이 계속되어도 수익률은 더 안 떨어진다.
[우리의 추론] 이것이 실질중립금리(r\*)를 "인구증가율 n / 저축률 s"의 비율로 읽는 현대 논의의 원형이다. **인구증가 둔화 → n ↓ → 균형 실질임대료 ↓** 는 이 모형이 직접 함의하는 저금리론이다. 다만 원문은 [[기준금리]]나 통화정책을 다루지 않는다.

**Equities** — [논문] Cobb-Douglas에서는 노동몫이 1−a로 **불변**. CES(p=1/2) 예시에서는 노동몫이 `1 − a√(s/n)`이 되어 **n이 높을수록 노동몫 ↑, s가 높을수록 노동몫 ↓**.
[우리의 추론] 자본몫 = 이익률의 장기 상한이라는 점에서, **저축과잉·저출산 조합은 구조적으로 자본몫을 밀어올린다**. 원문의 CES 예시가 이 방향을 명시적으로 지지한다.

**FX** — [논문] 폐쇄경제이므로 함의 없음.

**Commodities** — [논문] 없음. 다만 저자는 **"희소하고 증가 불가능한 자원(토지)이 없다고 가정한다"** 고 명시하고, 있다면 모형이 **리카도적**이 되어 규모수익체감으로 간다고 적는다.
[우리의 추론] 원자재 제약이 구속적인 레짐에서는 이 논문의 결론(균형성장 수렴) 자체가 적용 범위 밖이다. [[에너지 전환]]·[[구리 가격]] 같은 자원제약 논의에 솔로우를 그대로 갖다 쓰면 안 되는 이유다.

**Credit** — [논문] 없음(저축=투자 항등식). 저자 스스로 §VII에서 "완전예견과 시점간 차익거래 위에 신뢰할 만한 투자이론을 세울 수 없다"고 적는다.

## 12. Falsification Conditions

**What would confirm the hypothesis?**
- 저축률이 영구적으로 오른 경제에서 성장률이 **일시적으로만** 오르고 새 수준에서 멈추는 것.
- 자본-산출비율 K/Y가 s/n 근방에서 안정적일 것.
- 초기 자본이 적은 경제가 **더 빨리** 성장할 것(조건부 수렴).

**What would falsify the hypothesis?**
- 저축률 차이가 **영구적 성장률 차이**를 만드는 경우.
- 자본-노동비율이 크게 다른 국가들 사이에 **자본이 흐르지 않는** 경우 → [[1988 On the Mechanics of Economic Development (Lucas)]]가 정확히 이 반증을 제기한다(루카스 역설).
- 실질임금이 신축적인데도 성장경로가 발산하는 경우.

**Variables to monitor**
[[잠재성장률]] · K/Y 자본계수 · [[총요소생산성 (TFP)]] 기여도 · 노동몫 · 인구증가율 n

## 13. Contradictory / Alternative Literature

**Supporting Papers**
- [[1956 Economic Growth and Capital Accumulation (Swan)]] — 같은 해 독립적으로 동일 결론.
- Mankiw-Romer-Weil(1992) — 인적자본을 추가한 확장 솔로우가 국가 간 소득분산의 약 80%를 설명(원문 미보유, 인용 시 재검증 필요).

**Contradictory Papers**
- [[1986 Increasing Returns and Long-Run Growth (Romer)]] — 규모수익불변 가정을 깨면 수렴이 사라진다.
- [[1988 On the Mechanics of Economic Development (Lucas)]] — 요소이동성 하에서 수렴 예측이 관측과 정면충돌.
- [[1990 Government Spending in a Simple Model of Endogenous Growth (Barro)]] — 재정지출이 level이 아니라 **growth** 효과를 갖는 구조를 제시.

**Why do the results differ?**
- **Time period**: 1956년에는 국가 간 패널 자료가 없었다. 반론은 전부 1980년대 크로스컨트리 자료 등장 이후.
- **Country**: 솔로우는 사실상 선진국 1개 경제를 상정. 반론은 개도국 포함 표본.
- **Data**: 원문에 데이터 없음.
- **Identification**: 원문에 식별전략 없음.
- **Economic regime**: 자본이동이 막힌 폐쇄경제 vs 개방·자본이동 레짐. 후자에서 수렴 예측이 무너진다.

## 14. Connections to Other Papers

- **SUPPORTS** — [[1956 Economic Growth and Capital Accumulation (Swan)]]
- **CONTRADICTS** — Harrod-Domar 계열(칼날 명제)
- **EXTENDS** — [[1982 Time to Build and Aggregate Fluctuations (Kydland & Prescott)]] · [[1988 Production Growth and Business Cycles I - The Basic Neoclassical Model (King, Plosser & Rebelo)]] — 같은 성장모형에 확률적 기술충격을 넣어 **경기변동 모형으로 재사용**한다. RBC는 솔로우의 반박이 아니라 **솔로우의 확률적 확장**이다.
- **CRITIQUES** — [[1986 Increasing Returns and Long-Run Growth (Romer)]] · [[1988 On the Mechanics of Economic Development (Lucas)]] · [[1990 Endogenous Technological Change (Romer)]]
- **APPLIES** — [[1990 Government Spending in a Simple Model of Endogenous Growth (Barro)]]

## 15. Zettelkasten Atomic Notes

### ZK Note 1 — 해로드의 칼날은 결론이 아니라 가정이었다
- **Claim**: 성장경로의 불안정성은 경제의 성질이 아니라 **고정계수 생산함수라는 가정 하나**에서 나온다.
- **Mechanism**: 고정계수에서는 자본이 남아도 노동으로 대체할 수 없어 요소 하나가 항상 유휴가 된다 → 가격이 조정해도 수량이 못 따라간다. 대체를 허용하면 r이 움직여 `sF(r,1)`이 `nr`을 향해 조정된다.
- **Evidence**: 원문 §IV Example 1이 고정계수 케이스를 그대로 재현해 세 경우(n>s/a, n=s/a, n<s/a) 모두 유휴가 발생함을 보이고, Example 2에서 Cobb-Douglas면 **파라미터와 무관하게 항상** 안정 균형이 존재함을 보인다.
- **Implication**: 모형이 극단적 결론을 낼 때 **어느 가정이 crucial인지 먼저 찾는다**는 방법론. 이 논문의 진짜 기여는 결론이 아니라 이 절차다.
- **Connected Notes**: [[1956 Economic Growth and Capital Accumulation (Swan)]] · [[총요소생산성 (TFP)]]

### ZK Note 2 — 저축률은 성장률이 아니라 소득 수준을 바꾼다
- **Claim**: 저축률 s의 영구적 상승은 1인당 소득의 **수준**을 올리지만 장기 **성장률**은 못 바꾼다.
- **Mechanism**: s ↑ → `sF(r,1)` 곡선 상방 이동 → 새 교점 r\* ↑ → 이행기 동안만 성장률이 n을 초과 → 새 균형에서 다시 n.
- **Evidence**: Cobb-Douglas 해에서 r\* = (s/n)^{1/(1−a)}, Y/L → (s/n)^{a/(1−a)} — 모두 **수준**의 식이며 성장률 식에 s가 등장하지 않는다. 조세 확장도 실효저축률을 `s+(v−s)t`로 옮길 뿐이다.
- **Implication**: [[재정정책]]·저축 유인 세제의 성장 효과를 주장할 때, **level effect를 growth effect로 파는 것**이 가장 흔한 오류다. Lucas(1988)는 이를 두고 "1956년의 결론인데 오늘날까지 널리, 그리고 매우 불행하게도 무시된다"고 적는다.
- **Connected Notes**: [[1990 Government Spending in a Simple Model of Endogenous Growth (Barro)]] · [[재정정책]] · [[잠재성장률]]

### ZK Note 3 — 솔로우 모형의 빈곤함정은 수확체증 없이도 생긴다
- **Claim**: 규모수익불변·요소가분성만으로도 **"작은 투자는 정체로, 큰 투자 한 방은 자립적 성장으로"** 가는 구조가 만들어진다.
- **Mechanism**: 인구증가율을 소득의 함수 n(r)로 두면 `nr` 직선이 곡선으로 휘어 교점이 둘 생긴다(r₁ 안정, r₂ 불안정). r₂를 넘기면 자기증식적 확장, 못 넘기면 r₁로 회귀.
- **Evidence**: 원문 §VI "Variable Population Growth" · Figure IX. 저자의 문장: "불가분성이나 수확체증이 **전혀 없는데도** 이런 상황이 발생할 수 있음을 보여준다는 점이 흥미롭다."
- **Implication**: **빅푸시(big push) 논리는 수확체증을 필요로 하지 않는다.** 개발정책 논쟁에서 "수확체증을 가정해야만 함정이 나온다"는 통념은 틀렸다.
- **Connected Notes**: [[1986 Increasing Returns and Long-Run Growth (Romer)]] · [[1990 Endogenous Technological Change (Romer)]] (Romer 1990도 H가 낮으면 성장이 아예 없는 정체 케이스를 낸다)

### ZK Note 4 — 완전고용은 이 모형의 결과가 아니라 입력이다
- **Claim**: 솔로우 모형의 안정성은 **실질임금 신축성**을 전제로 하며, 임금이 경직되면 해로드형 누적 실업이 그대로 돌아온다.
- **Mechanism**: 실질임금을 (w/p)̄로 고정 → 한계생산성 조건이 r을 r̄에 고정 → 조정변수가 사라짐 → 고용이 `(s/r̄)F(r̄,1)` 속도로 증가하는데 이것이 n보다 작으면 실업이 지수적으로 누적.
- **Evidence**: 원문 §VII "Rigid Wages" — 저자가 직접 도출한다. 같은 절에서 유동성함정도 "경직된 요소가격"으로 동일하게 취급한다.
- **Implication**: 솔로우를 "케인즈 반박"으로 읽는 것은 오독이다. 저자는 **두 세계가 다른 가정 위에 있고 자신은 신고전파 쪽만 그렸다**고 명시한다. 레짐 판단에서 가격신축성 여부가 어느 모형을 쓸지의 스위치다.
- **Connected Notes**: [[통화정책]] · [[실업률]] · [[1986 Theory Ahead of Business Cycle Measurement (Prescott)]]

## 16. One-Sentence Takeaway

> **이 논문을 한 문장으로 기억한다면: 성장률은 저축이 아니라 기술이 정한다 — 단, 가격이 움직일 수 있을 때만.**

## 인과 사슬

저축률 s ↑ → 자본-노동비율 r ↑ → 자본 한계생산 ↓ → 실질임금 ↑ · 실질임대료 ↓
→ 새 균형 r\*에서 **[[GDP 성장률]] 은 다시 n으로 복귀** (수준만 상승)

[[총요소생산성 (TFP)]] 증가율 g ↑ → 1인당 [[GDP 성장률]] ↑ (**유일한 항구적 성장 동인**)
→ [[잠재성장률]] ↑

인구증가율 n ↓ → 균형 자본-노동비율 r\* ↑ → 자본 실질임대료 q/p = an/s ↓
→ (우리의 추론) 구조적 저금리 압력 → [[기준금리]] 중립수준 ↓

**실질임금 경직** → r이 r̄에 고정 → 조정 메커니즘 정지 → [[실업률]] 누적 상승 (§VII, 저자 직접 도출)

**Comment**: 이 볼트에서 솔로우는 **"성장 논문"이 아니라 "레짐 스위치 논문"** 으로 쓰는 편이 유용하다.
가격이 움직이는 레짐에서는 §I~VI(수렴·수준효과), 가격이 막힌 레짐에서는 §VII(누적 불균형)이 적용된다.
[[RegimeView 1.0]]이 상정하는 공급제약형 확장은 §VI의 기술진보 항 g와 §VII의 경직성 중 어느 쪽으로 읽느냐에 따라 함의가 갈리므로, 이 논문은 결론이 아니라 **분기점**으로 인용해야 한다.

## 저자가 밝힌 한계

- **완전고용을 가정으로 넣었다**(§VII 첫 문장에서 명시). 케인즈적 경직성·불확실성·유동성선호는 "존재하지 않는다는 주장이 아니라 다루지 않았다"고 적는다.
- **투자이론이 없다** — "완전예견과 시점간 차익거래 위에 신뢰할 만한 투자이론을 세울 수 없다"(§VII 마지막).
- **화폐가 없다** — 자산선택(현금 vs 자본) 문제로 가면 "화폐동학의 필요를 피할 수 없다"고 스스로 인정.
- **토지·자원 제약을 제외**했다(§II 각주 2).

## 검증 필요 · 반박 포인트 (Red Team)

**① §VI 기술진보 확장의 성장률 서술이 내적으로 맞지 않는다 — 원문 대조로 발견 (확신도: 상)**

원문 pp.85-86(§VI Neutral Technological Change, Cobb-Douglas, A(t)=e^{gt}, b ≡ 1−a)에서 저자는 세 가지를 연달아 적는다.

| 원문 서술 | 값 |
|---|---|
| 자본스톡 증가율 | **n + g/b** |
| 실질산출 증가율 | **n + ag/b** |
| 자본계수 K/Y 증가율 | (n+g/b) − (n+ag/b) = **g** |

세 번째는 앞 두 개로부터 정확히 따라 나오므로 서술은 **자기일관적**이다. 문제는 두 번째다.
저축-투자 항등식 `K̇ = sY` 에서 `K̇/K = s·(Y/K)`. 자본이 일정률로 지수성장하면 좌변이 상수이므로 **Y/K도 상수**여야 하고, 따라서 **Y와 K는 같은 속도로 성장**해야 한다. 즉 Y도 n + g/b로 자라고 **K/Y는 상수**여야 한다.
생산함수로 직접 확인해도 같다: r = K/L가 g/b로 자라면 Y/L = e^{gt}·r^a 의 증가율은 g + a·g/b = g(a+b)/b = **g/b**.
→ **산출증가율은 n + ag/b가 아니라 n + g/b이고, K/Y는 g가 아니라 0으로 자란다.**
저자가 A(t)의 **직접 효과(g)** 를 산출증가율에서 빠뜨린 것으로 보인다. 이 오차 때문에 원문은 "a > 1/2이면 성장률이 n+g보다도 빠를 수 있다"는 조건부 문장을 붙였는데, 올바른 값 n+g/b는 **항상** n+g보다 크므로 그 조건 자체가 불필요해진다.
- **왜 중요한가**: 힉스중립 기술진보 + Cobb-Douglas는 사실 노동증대형과 동치라 **균형성장경로가 존재한다**(K/Y 일정). 원문 서술대로면 K/Y가 영구히 발산해 균형성장이 없는 것처럼 읽힌다. 이 차이는 "카할도 정형화 사실(K/Y 안정)과 솔로우 모형이 정합적인가"라는 논점에 직접 걸린다.
- **확인 방법**: 원문 식 (13a)와 그 해(OCR에서 수식 이미지가 탈락)를 스캔 이미지로 직접 대조할 것. 위 반증은 본문 산문 서술과 `K̇=sY` 항등식만으로 성립하므로 결론은 바뀌지 않을 것으로 본다.

**② "장기 성장률 = n"은 **완전고용 + 신축가격**의 동어반복에 가깝다 (확신도: 중)**
L이 외생적으로 n으로 자라고 모든 노동이 항상 고용된다고 가정했으므로, 규모수익불변 하에서 Y가 n으로 자라는 것은 거의 정의다. 모형이 실제로 증명한 것은 "성장률이 n이다"가 아니라 **"r이 발산하지 않는다"** 이다.

**③ 안정성은 그림 하나에서 나온다 (확신도: 상)**
Figure I의 강한 안정성은 `sF(r,1)`을 원점 통과·위로 볼록하게 **그렸기 때문**이며, 저자 본인이 곧바로 Figure II(복수균형)·III(균형 부재)를 제시한다. 오늘날 교과서가 이 예외를 생략하고 Figure I만 가르치면서 **"솔로우 모형 = 무조건 수렴"** 이라는 잘못된 요약이 굳었다. 실제 원문은 **이나다 조건을 부과하지 않는다.**

**④ 데이터가 한 줄도 없다 (확신도: 상)**
이 논문은 실증논문이 아니다. "솔로우가 보여줬다"로 인용되는 실증 명제는 대부분 Solow(1957) 성장회계나 그 이후 문헌의 것이다. 인용 시 반드시 분리할 것.

**⑤ n을 외생으로 둔 것이 결론의 절반을 만든다 (확신도: 중)**
§VI에서 n = n(r)로 내생화하는 순간 **빈곤함정(복수균형)** 이 나타난다(ZK Note 3). 즉 "수렴한다"는 결론은 **인구증가를 외생 상수로 두었기 때문**이며, 저자는 이것을 알고 있었고 명시적으로 보여준다. 저출산·고령화 레짐에 이 모형을 적용할 때 반드시 짚어야 할 지점이다.

## 관련 개념

[[총요소생산성 (TFP)]] · [[인적자본]] · [[잠재성장률]] · [[GDP 성장률]] · [[산출갭]] · [[실업률]] · [[기준금리]] · [[재정정책]] · [[통화정책]]

## 관련 MOC

- [[매크로 고전 논문 MOC]] · [[원문검증 논문 MOC]] · [[매크로 해석 프레임]]
