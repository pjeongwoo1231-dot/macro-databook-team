---
title: "Structural Interpretation of Vector Autoregressions with Incomplete Identification: Revisiting the Role of Oil Supply and Demand Shocks"
type: paper
journal: American Economic Review 109(5), 1873–1910 (2019). NBER WP 24167 (2017-12)
date: 2019
author: Christiane J. S. Baumeister (Notre Dame), James D. Hamilton (UC San Diego)
url: https://www.nber.org/papers/w24167
tags: [type/paper, method/bayesian-SVAR, domain/commodities]
concepts: [불완전 식별, 베이지안 SVAR, 사전분포, 유가 공급충격, 재고]
status: done
verification: partial
reliability: academic
text_basis: human-fulltext
verified: "○ NBER WP 24167 개정판 PDF의 표지·초록 직접 판독(2026-08-14). 결론 문장 확인. ⚠ 판독본은 **2017-12 WP**이고 출판본은 AER 109(5) 2019 — 수치는 출판본 확인 필요"
promoted_from: "[[L220 Structural Interpretation of Vector Autoregressions with Incomplete Identification]]"
related: ["[[2009 Not All Oil Price Shocks Are Alike (Kilian)]]", "[[2018 Really Uncertain Business Cycles (Bloom, Floetotto, Jaimovich, Saporta-Eksten & Terry)]]", "[[WTI (국제유가)]]", "[[고빈도 통화 서프라이즈는 충격의 자격을 갖추지 못했다 — 자기상관되고 예측 가능하다]]"]
---

# 식별 가정을 확실한 것처럼 쓰지 말자 (Baumeister & Hamilton, 2019)

> American Economic Review 109(5) 1873–1910, 2019. **볼트 판독본은 NBER WP 24167(2017-12) 개정판.**
> ⚠ WP판 초록 기준이다. 출판본에서 수치가 달라졌을 수 있다.

## 왜 중요한가 — 우리 문제와 직결

**방법론 논문인데 결과가 실질적이다.** [[2009 Not All Oil Price Shocks Are Alike (Kilian)]]의
분해를 **다른 식별로 다시 하면 답이 바뀐다**는 것을 보인다.

그리고 볼트에 이미 같은 종류의 경고가 있다 —
[[고빈도 통화 서프라이즈는 충격의 자격을 갖추지 못했다 — 자기상관되고 예측 가능하다]].
그쪽은 통화충격 식별, 이쪽은 유가충격 식별이다. **둘 다 "식별 가정이 결과를 만든다"** 는 얘기다.

## 논지 — 방법

> *"Traditional approaches to structural vector autoregressions can be viewed as special cases
> of Bayesian inference arising from very strong prior beliefs."*

전통적 SVAR은 일부 구조를 **확실히 아는 것처럼**(식별 가정) 다루고 나머지는
**완전히 모르는 것처럼** 다룬다. 저자들은 이 **전부 아니면 전무(all-or-nothing)** 접근을 비판하고,
**식별 가정 자체의 불확실성**을 사전분포로 명시하는 일반화를 제안한다.

## 논지 — 결과

같은 데이터에 이 접근을 적용해 유가 공급·수요 충격을 다시 추정한다.

> *"Supply disruptions turn out to be a bigger factor in historical oil price movements and
> inventory accumulation a smaller factor than implied by earlier estimates.
> Supply shocks lead to a reduction in global economic activity after a significant lag,
> whereas shocks to oil demand do not."*

**① 공급 차질의 비중이 기존 추정보다 크다.**
**② 재고 축적(예비적 수요)의 비중은 더 작다.**
**③ 공급충격은 상당한 시차를 두고 세계 경제활동을 위축시키지만, 수요충격은 그렇지 않다.**

## 한계와 적용 범위

- **사서(추가)**: 이 논문도 **사전분포 선택에서 자유롭지 않다.** "불확실성을 명시한다"는 것이
  "가정이 없다"는 뜻은 아니다. 다만 **가정을 드러내 놓고 민감도를 볼 수 있게** 한 것이 기여다
- **사서(추가)**: 판독본이 **2017년 WP**다. 출판본(AER 2019)에서 수치가 바뀌었을 수 있다
- **사서(추가)**: Kilian 계열과 **어느 쪽이 맞는지 이 노트가 판정하지 않는다.**
  두 결과가 갈린다는 사실 자체가 기록 대상이다

## 인과 사슬

식별 가정을 확실한 것으로 취급 → 특정 분해 결과 도출
→ **가정의 불확실성을 명시하면** → 공급 비중↑, 재고(예비적 수요) 비중↓
→ 공급충격은 **시차를 두고** 세계 경제활동 위축, 수요충격은 아님
→ 같은 데이터에서 **정책 함의가 달라진다**

**Comment**: 우리 쪽에 남는 규칙은 유가가 아니라 **방법**이다.

**"분해 결과를 인용할 때 식별 전략을 함께 적는다."**
[[2024-2026-Comparative-Mechanism-Map]]이나 [[RegimeView 1.0 (2026-08-09)]]에서
"공급충격이 물가를 얼마 올렸다"류를 쓸 때, **누구의 식별인지**가 빠지면
다른 식별로는 다른 답이 나온다는 사실이 숨는다.

[[2008 The Cyclical Behavior of Equilibrium Unemployment and Vacancies Revisited (Hagedorn & Manovskii)]]의
보정 교훈과 같은 계열이다 — **모형·데이터가 같아도 가정을 바꾸면 결론이 뒤집힌다.**

## 관련 개념

- 재검토 대상 — [[2009 Not All Oil Price Shocks Are Alike (Kilian)]] ·
  [[2008 Exogenous Oil Supply Shocks (Kilian)]]
- 같은 종류의 식별 경고 — [[고빈도 통화 서프라이즈는 충격의 자격을 갖추지 못했다 — 자기상관되고 예측 가능하다]] ·
  [[2008 The Cyclical Behavior of Equilibrium Unemployment and Vacancies Revisited (Hagedorn & Manovskii)]]
- 계보 — [[WTI (국제유가)]]

## References

[1]: https://www.nber.org/papers/w24167 "Baumeister and Hamilton (2017), Structural Interpretation of VARs with Incomplete Identification, NBER WP 24167 — published AER 109(5) 2019"
