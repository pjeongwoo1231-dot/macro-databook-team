---
title: "On the Behaviour of Commodity Prices"
type: paper
journal: Review of Economic Studies 59(1), 1–23 (1992-01)
date: 1992
author: Angus Deaton (Princeton), Guy Laroque (INSEE, Paris)
url: https://www.princeton.edu/~deaton/downloads/On_The_Behaviour_of_Commodity_Prices.pdf
local_pdf: "Attachments/macro_classics/deaton_laroque1992.pdf"
tags: [type/paper, method/rational-expectations, domain/commodities]
concepts: [경쟁적 저장모형, 음의 재고 불가, 비선형성, 왜도, 가격 폭발, 자기상관 퍼즐]
status: done
verification: full
reliability: academic
text_basis: local-pdf
verified: "○ 저자 공개 PDF를 내려받아 전문 판독(2026-08-15). 아래 인용문은 추출 텍스트 그대로. REStud 59(1) 1–23 · 상품 13종 · sha256 332deef4…"
promoted_from: "[[L42 On the Behaviour of Commodity Prices]]"
related: ["[[1996 Competitive Storage and Commodity Price Dynamics (Deaton & Laroque)]]", "[[1993 The Present Value Model of Rational Commodity Pricing (Pindyck)]]", "[[원자재 재고]]", "[[선물 곡선 (Futures Curve)]]", "[[2009 Not All Oil Price Shocks Are Alike (Kilian)]]"]
---

# 재고는 음수가 될 수 없다 — 그 하나가 원자재 가격을 비대칭으로 만든다 (Deaton & Laroque, 1992)

> Review of Economic Studies 59(1) 1–23, 1992년 1월. **PDF가 볼트 안에 있다** — 전문 판독본이다.

## 왜 중요한가 — 볼트가 쓰던 규칙의 근거가 여기 있다

[[2009 Not All Oil Price Shocks Are Alike (Kilian)]] 노트에 이렇게 적어뒀다 —
*"재고↑ + 지정학 뉴스↑ + 생산 불변이면 예비적 수요"*.
**그 판별의 이론적 근거가 이 논문이다.** 지금까지 볼트에는 규칙만 있고 근거가 없었다.

핵심은 한 줄로 요약된다. **시장 전체가 음(-)의 재고를 가질 수 없다.**
너무 당연해 보이는 제약인데, 이것 하나가 원자재 가격의 성질 대부분을 만들어낸다.

## 논지 — 저자의 문장

> *"A central feature of the model is the explicit recognition of the fact that it is impossible
> for the market as a whole to carry negative inventories, and this introduces an
> essential non-linearity which carries through into non-linearity of the predicted
> commodity price series."*

**왜 비선형이 되는가.** 풍작이면 남는 것을 저장해 다음 기로 넘긴다 — 가격 하락이 완충된다.
그런데 흉작이면? **빌려올 재고가 없다.** 저장은 한쪽 방향으로만 작동한다.

그래서 가격은 **아래로는 눌리고 위로는 열린다**:

> *"It explains the skewness, and the existence of rare but violent explosions in prices,
> coupled with a high degree of price autocorrelation in more normal times."*

**① 왜도(skewness)** — 분포가 위로 긴 꼬리를 갖는다
**② 드물지만 격렬한 폭발** — 재고가 바닥나는 순간 가격이 튄다
**③ 평상시의 높은 자기상관** — 재고가 있는 동안은 가격이 완만히 이어진다

상품 13종에 적용해 **대부분에서 조건부 기댓값·조건부 분산의 예측이 자료와 부합**함을 보인다.

## 저자가 스스로 인정한 실패

> *"…the analysis does not yield a fully satisfactory explanation for the high autocorrelation
> observed in the data."*

**저장모형이 자기상관의 크기까지는 설명하지 못한다.** 저자들이 초록에 직접 적었다.
이 미해결 문제가 이후 문헌([[1996 Competitive Storage and Commodity Price Dynamics (Deaton & Laroque)]] 포함)의 출발점이 된다.

### ⚠ 2026-08-18 유보 — 이 실패가 수치 오류였을 수 있다

[[2011 The Economics of Grain Price Volatility (Wright)]](AEPP 33(1), 전문 판독)이 전하는 Cafiero et al.의 지적:

- Deaton-Laroque(1992)의 **수치 예제는 모형의 일반적 실패를 입증하지 못한다** — 수요곡선 기울기만 바꿔도 자료 수준의 높은 자기상관이 재현된다. 즉 "모형의 일반적 특성"이 아니다
- D-L(1995·1996)의 **PML 추정에서 꺾인 수요의 근사에 수치 부정확성**이 있어 추정에 큰 편의가 생기고, 그 결과 **꺾임 가격 p\* 를 과소추정**했다. 저장 빈도도 함께 과소평가된다
- 이를 고치고 단위당 고정 저장비용을 허용하면 **여러 품목에서 상관 추정치가 더 높아진다**

→ **이 노트의 "자기상관 설명 실패"를 폐기하지 않는다. 유보로 내린다.**
Cafiero et al. 원문을 직접 확인하기 전까지는 **"저장모형은 자기상관을 설명하지 못한다"를 확정 진술로 인용하지 않는다.**
⚠ 전달자인 Wright는 경쟁 모형의 당사자([[1991 Storage and Commodity Markets (Williams & Wright)]] 저자)이므로 이해관계가 있다.

## 한계와 적용 범위

- **저자(명시)**: 자기상관 설명 실패. 위 인용 그대로다
- **저자(명시)**: 수확이 **iid**이고 현재·과거 가격에 반응하지 않는다고 가정한다.
  저자들이 *"the simplest possible form of the theory"* 라고 밝힌다
- **사서(추가)**: 표본이 **연간 자료, 농산물 중심 13종**이다. 원유·금속에 그대로 옮기면 안 된다 —
  특히 원유는 **생산 조절이 가능**해 iid 수확 가정과 거리가 있다
- **사서(추가)**: 이 모형에 **투기 자금**은 없다. 순수 저장 동기만 있다.
  금융화 논쟁([[2012 Index Investment and the Financialization of Commodities (Tang & Xiong)]])은
  **이 모형이 설명하지 못하는 잔차를 두고 벌어지는 싸움**이다

## 인과 사슬

공급 충격 → 재고로 완충 시도
→ **풍작**: 저장 가능 → 가격 하락 완충 → 자기상관↑
→ **흉작**: 음의 재고 불가 → **완충 불가** → 가격 폭발
→ 결과: 왜도 + 드문 폭발 + 평상시 지속성
→ **[[원자재 재고]] 수준이 가격 반응 함수의 기울기를 결정한다**

**Comment**: 실무 규칙 — **원자재 가격을 볼 때 재고 수준을 먼저 본다.**
같은 크기의 공급 차질이라도 **재고가 두꺼우면 가격이 안 움직이고, 얇으면 폭발한다.**
DataBook에 [[원자재 재고]]가 이미 있으므로 **가격과 재고를 짝지어 읽는 것이 기본**이다.

그리고 대칭성 가정을 버려야 한다. **원자재 가격의 상승 위험과 하락 위험은 크기가 다르다** —
[[RegimeView 1.0 (2026-08-09)]]에서 유가 시나리오를 대칭으로 잡으면 상방을 과소평가한다.

## 관련 개념

- 후속 추정 — [[1996 Competitive Storage and Commodity Price Dynamics (Deaton & Laroque)]]
- 편의수익 측정 — [[1993 The Present Value Model of Rational Commodity Pricing (Pindyck)]]
- 유가 적용 — [[2009 Not All Oil Price Shocks Are Alike (Kilian)]] · [[2008 Exogenous Oil Supply Shocks (Kilian)]]
- 금융화 논쟁 — [[2012 Index Investment and the Financialization of Commodities (Tang & Xiong)]]
- 지표 — [[원자재 재고]] · [[선물 곡선 (Futures Curve)]] · [[WTI (국제유가)]]

## References

[1]: https://www.princeton.edu/~deaton/downloads/On_The_Behaviour_of_Commodity_Prices.pdf "Deaton and Laroque (1992), On the Behaviour of Commodity Prices, REStud 59(1) 1–23 — 볼트 내 PDF 판독본"
