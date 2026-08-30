---
title: Effects of Fed policy rate forecasts on real yields and inflation expectations at the zero lower bound
type: paper
series: BIS Working Papers No 873
date: 2020-07
author: Gabriele Galati (DNB), Richhild Moessner (BIS)
url: https://www.bis.org/publ/work873.pdf
tags: [type/paper, method/event-study, domain/policy]
concepts: [포워드가이던스, 점도표, 실질금리, 기대인플레이션, 제로하한, 정책 신뢰성]
source_file: 06_SourceArchive/06-BIS-Archive-Catalog/PDFs (원문 URL 보존, 로컬 사본은 감사용)
status: done
verification: full
reliability: working-paper
text_basis: human-fulltext
verified: 원문 대조 완료(2026-08-14). 표본기간·핵심 수치·결론부 직접 확인. tier A 승격
related: ["[[기관 예측 신뢰도 스코어카드]]", "[[2022 Monetary Policy Expectation Errors (Schmeling, Schrimpf & Steffensen)]]", "[[2003 The Zero Bound on Interest Rates and Optimal Monetary Policy (Eggertsson & Woodford)]]", "[[원문 아카이브 MOC]]"]
---

# 점도표는 실질금리를 움직이면서 기대인플레는 건드리지 않았다 (Galati & Moessner, 2020)

> BIS Working Paper No 873, 2020년 7월. JEL: E52, E58

## 왜 중요한가 — 우리 문제와 직결

[[기관 예측 신뢰도 스코어카드]]는 Fed SEP를 **얼마나 맞혔나**로 채점한다.
이 논문은 같은 SEP를 **얼마나 움직였나**로 본다. 예측 정확도와 시장 영향력은 다른 축이고,
스코어카드에 빠져 있던 쪽이 이것이다.

더 중요한 건 짝이 되는 논문이 이미 볼트에 있다는 점이다.
[[2022 Monetary Policy Expectation Errors (Schmeling, Schrimpf & Steffensen)]]는
**시장이 Fed를 잘못 읽는다**(인하 폭 과소평가)고 하고, 이 논문은 **Fed가 점도표로 시장을
움직이는 데는 성공했다**고 한다. 둘은 모순이 아니라 같은 동전의 양면이다 —
평시의 신호 전달은 작동하고, **꼬리 충격에 대한 반응함수 학습이 실패**한다.

## 방법과 자료

| 항목 | 내용 |
|---|---|
| 질문 | ZLB에서 Fed가 SEP로 발표한 **정책금리 전망**이 실질금리와 기대인플레를 움직였는가. 그리고 그것이 정책 신뢰성을 해쳤는가 |
| 표본 | **일별, 2012-01-01 ~ 2015-07-31** — SEP가 정책금리 전망을 게시하기 시작한 2012년 1월부터, ZLB 이탈(2015-12) 직전까지 |
| 식별 | SEP 정책금리 전망의 **서프라이즈**(예상 대비 이탈)를 이벤트로 사용 |
| 종속변수 | 국채·물가연동채에서 뽑은 **선도 실질금리**와 **BEI(손익분기 인플레)**, 2~10년 지평 |

## 원문에서 확인한 결과

**1. 실질금리는 예상 방향으로 유의하게 움직였다.** 3~10년 지평에서 유의하다.
크기는 구체적이다 — **ZLB 이탈까지의 예상 기간이 100일 늘어나면 3~6년 선도 실질금리가
약 6bp 하락**한다.

> *"Surprises in SEP forecasts corresponding to an increase of 100 days in the projected
> time to lift-off by the Fed from the ZLB led to a reduction of around 6 basis points in
> forward real yields at medium horizons of three to six years ahead."*

**2. 기대인플레는 거의 안 움직였다.** 수익률곡선 전 구간에서 그렇고, 특히 정책 신뢰성의
표준 척도인 **5년 후 5년 BEI(5y5y)가 유의하게 영향받지 않았다.**

**3. 저자의 해석** — Fed는 ZLB에서 점도표로 **실질금리를 움직이면서도 신뢰성을 훼손하지
않았다.** 우려됐던 "조건부 전망이 무조건적 약속으로 오독되어 시간비일관성을 낳는다"는
시나리오는 데이터에서 확인되지 않았다.

## 한계와 적용 범위

- **저자(명시)**: 표본이 **ZLB 국면(2012~2015)에 한정**된다. 정상 금리 국면이나
  긴축 국면으로 일반화할 수 없다
- **저자(명시)**: 서프라이즈 측정이 SEP 공표 전 시장 예상의 대리변수에 의존한다
- **사서(추가)**: "기대인플레가 안 움직였다"는 **양날의 결과**다. 신뢰성 유지의 증거이기도
  하지만, ZLB에서 **기대인플레를 끌어올려 실질금리를 낮추려는 정책 의도의 실패**로도 읽힌다.
  원문은 전자로 해석하지만 후자를 배제하지 않는다
- **사서(추가)**: 볼트의 [[고빈도 통화 서프라이즈는 충격의 자격을 갖추지 못했다 — 자기상관되고 예측 가능하다]]가
  이 식별전략에 직접적인 반론이다. **서프라이즈가 예측 가능하면 이벤트 스터디의 외생성
  가정이 깨진다.** 이 논문은 그 검정을 하지 않았다 — 재현할 때 반드시 확인할 것

## 인과 사슬

SEP 점도표 서프라이즈(ZLB 이탈 시점 +100일)
→ 선도 **실질금리** −6bp (3~6년) → [[장단기 금리차]] 변화
→ 그러나 [[BEI (기대인플레이션)]] 5y5y는 **무반응**
→ [[통화정책]] 신뢰성 유지 (또는 기대 견인 실패)

**Comment**: 명목금리 하나로 정책 스탠스를 읽지 말라는 [[Monetary-Policy-Transmission-and-International-Spillovers]]의
논지와 같은 방향이다. 여기선 **명목이 아니라 실질과 기대를 갈라 봐야** 무엇이 움직였는지 보인다.
볼트의 [[물가 압력은 장기금리로, 실물은 단기금리로 — 충격은 만기별로 분업한다]]와 대조하면,
이 논문은 **정책 커뮤니케이션 충격이 만기별로 어떻게 분업하는지**를 보여주는 사례가 된다.

## 관련 개념

- 짝 논문(시장 쪽 오차) — [[2022 Monetary Policy Expectation Errors (Schmeling, Schrimpf & Steffensen)]]
- 채점 대상 — [[기관 예측 신뢰도 스코어카드]]
- ZLB 이론 — [[2003 The Zero Bound on Interest Rates and Optimal Monetary Policy (Eggertsson & Woodford)]]
- 식별 반론 — [[고빈도 통화 서프라이즈는 충격의 자격을 갖추지 못했다 — 자기상관되고 예측 가능하다]]
- 등급 체계 — [[원문 아카이브 MOC]] · [[원문대조 감사 2026-08-14]]

## References

[1]: https://www.bis.org/publ/work873.pdf "Galati and Moessner (2020), Effects of Fed policy rate forecasts on real yields and inflation expectations at the zero lower bound, BIS WP 873"
