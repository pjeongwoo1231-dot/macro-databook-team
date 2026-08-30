---
title: "Can Exchange Rates Forecast Commodity Prices?"
type: paper
journal: NBER Working Paper 13901 (2008) · 저널판 Quarterly Journal of Economics 125(3), 1145–1194 (2010, DOI 10.1162/qjec.2010.125.3.1145)
date: 2010
author: Yu-Chin Chen, Kenneth Rogoff, Barbara Rossi
doi: 10.3386/w13901
url: https://www.nber.org/papers/w13901
tags: [type/paper, domain/fx, domain/commodities, method/forecasting]
concepts: [원자재통화, 선행지표, 표본외 예측력, 선물시장 유동성, 전방주시 변수]
status: done
verification: full
reliability: working-paper
text_basis: full-text
verified: "✅ 2026-08-28 NBER 공개본(2008-07 개정) **전문 판독**(약 8.1만 자). 서지 Crossref 확정(10.3386/w13901). QJE 최종본과 수치가 다를 수 있다"
promoted_from: "[[Library MOC]]"
related: ["[[Library MOC]]", "[[1988 The Excess Co-Movement of Commodity Prices (Pindyck & Rotemberg)]]", "[[2016 Forty Years of Oil Price Fluctuations - Why the Price of Oil May Still Surprise Us (Baumeister & Kilian)]]", "[[원·달러 환율]]"]
---

# 원자재 가격은 환율이 먼저 안다 (Chen, Rogoff & Rossi, 2010)

> NBER WP 13901 / QJE 125(3). **호주·캐나다·칠레·뉴질랜드·남아공** — 원자재 수출 소국 5개국의 환율이
> 세계 원자재 가격을 예측하는지 본다.

## 결과 — 방향이 한쪽으로만 강하다

| 방향 | 결과 |
|---|---|
| **환율 → 원자재 가격** | **표본내·표본외 모두 견고**. 비달러 교차환율을 써도, 고지속성 정상성을 가정해도 유지 |
| 원자재 가격 → 환율 | 구조변화를 허용하면 표본내 Granger 인과는 있으나 **표본외에서는 견고하지 않다** |

**환율 기반 예측이 선물가격 기반 예측을 능가**한다(Diebold-Mariano 검정).

## 왜 비대칭인가 — 저자들의 이론

> **환율은 근본적으로 전방주시(forward-looking) 변수**라 미래 원자재 가격 정보를 담는다.
> **원자재 가격은 수요·공급이 모두 비탄력적이라 당면한 현재 상황에 민감**하다.

즉 두 변수는 정보의 시간축이 다르다. 환율은 미래를 반영하고, 원자재는 현재를 반영한다.

## 정책적 쓸모 — 저자들이 직접 강조한 것

개별 원자재, 특히 **광범위한 원자재 종합지수는 깊이 있는 선물시장이 없다.**
2008년 6월 버냉키 의장도 장기 선물계약 시장이 비유동적이라 **선물가격이 정보를 제대로 집계하지 못할 수 있다**고 지적했다.
저자들은 **환율이 그 대안 정보원**이라고 답한다.

## 우리 파이프라인에 바로 쓸 것

이건 우리 DataBook에 **당장 붙일 수 있는 선행지표**다.

1. **AUD·CAD·CLP·NZD·ZAR를 원자재 선행지표로 편입**한다. 이미 환율 계열을 수집하고 있으므로
   추가 비용 없이 **원자재 방향성의 조기 신호**를 얻는다
2. [[2016 Forty Years of Oil Price Fluctuations - Why the Price of Oil May Still Surprise Us (Baumeister & Kilian)]]가
   "채점 기준은 그때 기대되던 경로여야 한다"고 했는데, **그 기대 경로를 선물커브가 아니라 환율에서 뽑을 수 있다** —
   특히 선물시장이 얇은 품목(농산물·니켈·희토류)에서 결정적이다
3. **역방향은 쓰지 않는다.** "원자재가 올랐으니 자원국 통화가 오를 것"은 이 논문이 표본외에서 기각한 관계다.
   우리 코퍼스에 이 형태의 주장이 나오면 **약한 근거로 등급을 내려야 한다**

## Red Team

1. 표본이 **2008년 1월까지**다. 이후 원자재 슈퍼사이클 종료·셰일·중국 둔화·2022년 에너지 위기를 포함하지 않는다.
   특히 **AUD는 2010년대 이후 중국 철광석 수요의 함수**가 되어 관계의 성격이 바뀌었을 수 있다.
2. 대상국은 **세계 원자재 수출의 소수 지분**만 갖는다(1999년 기준 호주는 5% 미만).
   예측력이 '원자재 익스포저'가 아니라 **환율의 일반적 전방주시성**에서 올 가능성이 남는다.
3. 구조변화 허용 방법(Rossi 계열)에 결과가 의존한다 — 브레이크 설정을 바꾸면 역방향 결과가 달라질 수 있다.
4. **표본외 예측력이 통계적으로 유의하다는 것이 거래 가능한 크기라는 뜻은 아니다.**
