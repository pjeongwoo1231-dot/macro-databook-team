---
title: "This Is What Happened to the Oil Price-Macroeconomy Relationship"
type: paper
journal: Journal of Monetary Economics 38(2), 215–220 (1996)
date: 1996
author: James D. Hamilton (UC San Diego)
url: https://www.sciencedirect.com/science/article/pii/S0304393296012822
tags: [type/paper, method/time-series, domain/commodities]
concepts: [순유가상승, 되돌림, 비대칭성, 변수 정의, 관계의 소멸]
status: done
verification: partial
reliability: academic
text_basis: cited-primary
verified: "△ 서지 확정(2026-08-14). ScienceDirect 링크는 HTTP 403(봇 차단)이라 접속 확인은 못 했으나 PII S0304393296012822 형식은 정상. 본문 미열람 — **수치 인용 금지**"
promoted_from: "[[L47 This Is What Happened to the Oil Price-Macroeconomy Relationship]]"
related: ["[[1983 Oil and the Macroeconomy Since World War II (Hamilton)]]", "[[2009 The Impact of Oil Price Shocks on the U.S. Stock Market (Kilian & Park)]]", "[[WTI (국제유가)]]"]
---

# 관계가 사라진 게 아니라 변수를 잘못 만든 것이다 (Hamilton, 1996)

> Journal of Monetary Economics 38(2) 215–220, 1996.
> ⚠ **본문 미열람.** ScienceDirect가 403(봇 차단)이라 접속 확인도 못 했다.
> **수치는 인용하지 않는다.**

## 왜 중요한가 — 우리 문제와 직결

[[1983 Oil and the Macroeconomy Since World War II (Hamilton)]]의 관계가
1980년대 중반 이후 **깨진 것처럼 보였다.** 유가가 크게 올라도 침체가 오지 않았다.
이 논문은 **관계가 사라진 게 아니라 유가 변수를 잘못 정의했기 때문**이라고 답한다.

**우리 쪽에 주는 교훈이 여기 있다** — 지표가 예전처럼 작동하지 않을 때
"레짐이 바뀌었다"고 결론짓기 전에 **변수 정의를 먼저 의심**해야 한다.
[[RegimeView 1.0 (2026-08-09)]]이 트리거를 개정할 때마다 부딪히는 문제와 같다.

## 논지

문제는 **되돌림(rebound)** 이다.

분기별 유가가 크게 오르는 경우 중 상당수는 **직전 하락분을 되돌리는 것**일 뿐이다.
그런 상승은 새로운 비용충격이 아니므로 실물에 같은 효과를 주지 않는다.
그런데 단순 변화율은 둘을 구분하지 못한다.

해법은 **순유가상승(net oil price increase)** — 예컨대 **직전 1년(연간) 최고치를 넘어선 부분만**
충격으로 센다. 이 정의를 쓰면 **유가충격과 경기침체의 역사적 관계가 여전히 나타난다.**

핵심은 **비대칭성**이다. 유가 **상승**은 실물에 영향을 주지만 **하락**은 대칭적 반대 효과를
주지 않는다. 따라서 대칭적 변화율 변수는 애초에 잘못된 도구다.

## 한계와 적용 범위

- **사서(추가)**: "직전 1년 최고치"라는 **기준 자체가 임의적**이다. 3년 기준·2년 기준으로
  바꾸면 결과가 달라질 수 있다 — 이것이 후속 문헌(Kilian 계열)이 파고든 지점이다.
  **변수 정의로 관계를 살렸다면, 그 정의가 데이터에 과적합된 것은 아닌가**
- **사서(추가)**: 비대칭성의 **미시적 이유**를 이 논문이 규명하지는 않는다.
  조정비용·불확실성·부문 재배치 등 후보가 여럿이다 —
  [[2009 The Impact of Uncertainty Shocks (Bloom)]]의 대기행동이 후보 중 하나다
- **사서(추가)**: Kilian-Park는 **다른 답**을 낸다. 변수 정의가 아니라 **충격의 원인**을
  갈라야 한다는 것. 두 해법이 경쟁한다는 점을 기록해 둔다

## 인과 사슬

유가 상승 관측 → **(a) 직전 하락의 되돌림이면**: 새 비용충격 아님 → 실물 무반응
→ **(b) 1년 최고치 초과분이면**: 진짜 충격 → [[경기침체]] 위험
→ 단순 변화율은 (a)와 (b)를 섞어 **관계가 사라진 것처럼 보이게 만든다**

**Comment**: 볼트 실무에 바로 옮길 수 있는 규칙 —
**DataBook의 WTI를 전월비·전년비로만 보지 말고 "직전 12개월 최고치 대비"도 함께 볼 것.**
파생지표로 만들 수 있다(`derived.py`). 지금은 없다.

그리고 더 일반적인 교훈: [[RegimeView 1.0 (2026-08-09)]]의 트리거가 안 켜질 때
**"레짐이 다르다"와 "변수 정의가 틀렸다"를 구분**해야 한다. Hamilton은 후자였다.
[[2008 The Cyclical Behavior of Equilibrium Unemployment and Vacancies Revisited (Hagedorn & Manovskii)]]의
보정 교훈과 같은 종류의 경고다.

## 관련 개념

- 원 관계 — [[1983 Oil and the Macroeconomy Since World War II (Hamilton)]]
- 경쟁 해법(원인 분해) — [[2009 The Impact of Oil Price Shocks on the U.S. Stock Market (Kilian & Park)]] ·
  [[2018 Oil Prices and the Stock Market (Ready)]]
- 같은 종류의 방법론 경고 — [[2008 The Cyclical Behavior of Equilibrium Unemployment and Vacancies Revisited (Hagedorn & Manovskii)]]
- 지표 — [[WTI (국제유가)]] · [[경기침체]] · [[RegimeView 1.0 (2026-08-09)]]

## References

[1]: https://www.sciencedirect.com/science/article/pii/S0304393296012822 "Hamilton (1996), This Is What Happened to the Oil Price-Macroeconomy Relationship, JME 38(2) 215–220"
