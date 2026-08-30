---
title: "Measuring Uncertainty"
type: paper
journal: American Economic Review 105(3) (2015)
date: 2015
author: Kyle Jurado, Sydney C. Ludvigson, Serena Ng
doi: 10.1257/aer.20131193
url: https://www.aeaweb.org/articles?id=10.1257/aer.20131193
tags: [type/paper, method/factor-model, domain/uncertainty]
concepts: [불확실성 측정, 조건부 분산, 예측오차, 대용지표 비판, 공통요인]
status: done
verification: partial
reliability: academic
text_basis: cited-primary
verified: "△ 서지 확정(2026-08-14, AER 105(3), doi:10.1257/aer.20131193). 본문 유료라 미열람 — **수치 인용 금지**"
promoted_from: "[[L22 Measuring Uncertainty]]"
related: ["[[2009 The Impact of Uncertainty Shocks (Bloom)]]", "[[VIX]]", "[[신용스프레드의 정보는 기대부도가 아니라 잔차에 있다]]", "[[RegimeView 1.0 (2026-08-09)]]"]
---

# VIX는 불확실성이 아니다 (Jurado, Ludvigson & Ng, 2015)

> American Economic Review 105(3), 2015. `doi:10.1257/aer.20131193`
> ⚠ **본문 미열람**(유료). 서지만 확정했다. **수치는 인용하지 않는다.**

## 왜 중요한가 — 우리 문제와 직결

**이 4편 중 실무적으로 가장 중요합니다.** DataBook은 VIX·VIX3M·VIX 텀스트럭처·
EPU(미국 일별·통화정책 범주·한국 월간)를 **이미 수집 중**인데, 이 논문은
**그 지표들이 불확실성을 제대로 재고 있지 않을 수 있다**고 말한다.

그리고 볼트에 이미 같은 형태의 교훈이 있다 —
[[신용스프레드의 정보는 기대부도가 아니라 잔차에 있다]].
Gilchrist-Zakrajšek이 신용스프레드에서 **기대부도 성분을 빼야 정보가 남는다**고 했듯이,
JLN은 변동성에서 **예측 가능한 성분을 빼야 불확실성이 남는다**고 한다. **같은 논리 구조다.**

## 논지

불확실성은 **관측변수의 변동성이 아니다.**

주가 변동성(VIX), 예측자 간 의견 불일치, 신문 기사 빈도 같은 대용지표는
**예측 가능한 변동**과 **위험프리미엄·레버리지·심리** 같은 다른 요소를 함께 담는다.
변동이 크더라도 그것이 **예측 가능**하다면 경제주체에게 불확실한 것이 아니다.

올바른 측정은 **미래 예측오차의 조건부 분산** — 즉 "예측 가능한 부분을 모두 제거한 뒤
남는 예측 불가능성"이다. 저자들은 대규모 거시·금융 시계열에서 공통요인을 뽑아
각 계열의 예측오차 분산을 추정하고 이를 집계해 **거시 불확실성 지수**를 만든다.

이렇게 측정하면 **불확실성 급등 사건이 기존 대용지표보다 훨씬 드물게** 나타난다.

## 한계와 적용 범위

- **사서(추가)**: 본문 미열람이므로 **급등 사건의 개수·시점·충격 크기를 인용하지 않는다**
- **사서(추가)**: JLN 지수는 **예측모형에 의존**한다. 어떤 변수로 무엇을 예측하느냐가
  "예측 가능한 부분"의 크기를 정한다 — 즉 이 측정도 모형 선택에서 자유롭지 않다
- **사서(추가)**: 실무 제약이 크다. **JLN 지수는 실시간 갱신이 느리고** VIX·EPU처럼
  일별로 오지 않는다. DataBook에 넣기 어렵다는 뜻이며, 그래서 **VIX·EPU를 쓰되
  한계를 알고 쓰는 것**이 현실적이다

## 인과 사슬

(잘못된 경로) [[VIX]] 급등 → "불확실성 상승"으로 해석 → 대기행동 예상
→ **그런데 그 급등이 위험프리미엄·레버리지 청산이었다면** 실물 반응이 안 나온다

(올바른 경로) 예측오차의 조건부 분산 상승 → **진짜 불확실성** → 대기행동 → 실물

**Comment**: [[RegimeView 1.0 (2026-08-09)]]에 주는 실무 규칙 하나 —
**VIX·EPU가 오를 때 "불확실성 충격"이라고 바로 쓰지 말 것.**
그 상승이 예측 가능한 것이었는지(FOMC·지표 발표 일정), 위험프리미엄 이동인지 구분해야 한다.
[[2009 The Impact of Uncertainty Shocks (Bloom)]]의 V자 반등 예측도 **측정이 맞을 때만** 성립한다.

→ 최소한의 보완: DataBook의 **VIX 텀스트럭처(VIX3M/VIX)**를 함께 보면
단기 이벤트발 급등과 지속적 불확실성 상승이 어느 정도 갈린다. 이미 수집 중이다.

## 관련 개념

- 같은 논리 구조 — [[신용스프레드의 정보는 기대부도가 아니라 잔차에 있다]] ·
  [[2012 Credit Spreads and Business Cycle Fluctuations (Gilchrist & Zakrajsek)]]
- 반박 대상 — [[2009 The Impact of Uncertainty Shocks (Bloom)]] ·
  [[2016 Measuring Economic Policy Uncertainty (Baker, Bloom & Davis)]]
- 식별 일반 문제 — [[고빈도 통화 서프라이즈는 충격의 자격을 갖추지 못했다 — 자기상관되고 예측 가능하다]]
- 지표 — [[VIX]] · [[RegimeView 1.0 (2026-08-09)]]

## References

[1]: https://www.aeaweb.org/articles?id=10.1257/aer.20131193 "Jurado, Ludvigson and Ng (2015), Measuring Uncertainty, AER 105(3)"
