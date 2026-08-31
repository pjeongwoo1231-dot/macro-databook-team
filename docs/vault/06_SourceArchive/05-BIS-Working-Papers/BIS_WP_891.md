---
title: "BIS WP 891 — At the crossroads in the transition away from LIBOR - from overnight to term rates"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 891
published: "October 2020"
authors: "Basil Guggenheim and Andreas Schrimpf"
source_kind: "working-paper"
peer_reviewed: false
primary_text_read: true  # 추출 전문 기준. 사람 대조 아님
human_verified: false
analysis_model: "gpt-5-mini"
analysis_confidence: "not-calibrated"
relevance_score: 1
created: 2026-08-14
updated: 2026-08-14
archive_status: "llm-structured-unverified"
tags:
  - flag/partial-check
  - bis
  - working-paper
  - "libor-전환"
  - "리스크프리-단기금리(rfr)"
  - "sofr-/-effr"
  - "term-rate-설계-(in-arrears-vs-in-advance)"
  - "advance-basis(지연-기저)"
  - "대출시장/현금상품-설계"
  - "헤지·파생상품-유동성"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 891 — At the crossroads in the transition away from LIBOR - from overnight to term rates

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

저자들은 RFR 전환에서 이상적 기준은 RFR를 복리해 만기(‘in arrears’)에 정산하는 것이라 보지만, 현금시장 일부 참가자들은 사전확정 금리를 요구한다는 현실적 제약을 지적한다. 파생에서 만든 전진(term) 금리는 유동성·기대오차 문제로 완전한 대안이 아니며, 과거 관측치를 이용한 'in advance' 사전확정 방식은 선결정성을 제공하되 중앙은행 금리 변화 시 'advance basis'가 발생한다. 이를 완화하는 실무적 방안으로(1) OIS 기대를 이용해 계약초 조정요인(µ_Y)을 도입해 현재가치 차이를 보정하고 헤지하거나, (2) 과거 전체기간 대신 직전 짧은 관측기간(예: 1주)을 써서 사전확정 금리를 산출하는 방법을 제시·비교했다. 경험분석(EFFR 기반)에서 관측기간 단축 방식이 평균·변동성 측면에서 가장 우수해, 분기지급 등 실무조건을 유지하면서도 in‑arrears와의 기저를 작게 유지하는 현실적 해법으로 권고된다. 다만 EFFR→SOFR 일반화, 조정요인 기대오차, 단축관측의 단기변동성 증대 등은 유의해야 한다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 대출 등 현금상품에서 LIBOR 대신 O/N 리스크프리금리(RFR)를 쓸 때, 사전에 확정된(term) 금리를 어떻게 설계할 수 있나? 'in advance' 방식에서 발생하는 기저(basis)를 어떻게 축소·가격화·헤지할 수 있나? |
| 방법 | 저자들은 이론적 도식(복리식, 기저 정의)과 경험적 비교를 병행함. 장기 시계열 비교를 위해 EFFR(및 SOFR 프록시)를 사용해 다양한 '기저' α(전진·파생 기반), β(표준 in-advance), γ(조정요소 추가), δ(단축 관측기간) 등을 계산·비교하고 통계(평균, 표준편차)로 성능을 평가함. |
| 자료·범위 | 일일 O/N 금리(주로 EFFR)와 OIS(3개월 등) 시장 데이터 사용, 샘플 대략 2002–2020. SOFR는 역사가 짧아 논의·예시에서 프록시(문헌 제공)를 병행 사용함. 분석은 주로 USD 계열 사례(EFFR proxy) 기반임. |
| 주제 | LIBOR 전환, 리스크프리 단기금리(RFR), SOFR / EFFR, term rate 설계 (in-arrears vs in-advance), advance basis(지연 기저), 대출시장/현금상품 설계, 헤지·파생상품 유동성 |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장: RFR를 복리해 만기(‘in arrears’)에 정산하는 방식이 이상적이며 파생시장과 완전한 헤지를 가능케 해 바람직함.
- 저자 주장: 현금상품 이용자(특히 중소기업·소매고객)는 사전확정(pre-determined) 금리를 선호하는데, 이는 주로 현금흐름 관리·구식 IT제약·법적 통지요건 등 현실적 제약 때문임.
- 저자 주장: 파생시장에서 구성한 전진(포워드)형 term rate는 기대·유동성·위기 시 증발 위험 때문에 현금상품의 보편적 대안으로 적절하지 않을 수 있음.
- 저자 주장: 'in advance'(과거 관측치를 이용한 사전확정) 방식은 선결정이라는 장점을 제공하나, 중앙은행의 급격한 정책금리 변화 시 ‘advance basis’(lagged behaviour)가 발생함.
- 저자 주장: advance basis를 줄이는 실무적 방안 두 가지는 (i) 계약초에 상수 조정요인(µ_Y)으로 현재가치 차이를 보정하고 이를 OIS 기대치로 가격·헤지하거나 계약으로 보장, (ii) 이전 전체 기간 대신 짧은 관측기간(예: 직전 1주)을 사용해 표본을 갱신하는 것임.
- 저자 주장(경험결과): EFFR 사례에서 직전 1주 관측으로 산출한 in‑advance 금리(분기 지급)는 평균기저와 변동성 면에서 조정요인을 쓰는 방식보다 우수했음(표본 통계: α mean≈4bp sd≈15bp, β mean≈2bp sd≈36bp, γ mean≈21bp sd≈37bp, δ mean≈0bp sd≈20bp).
- 저자 주장: 조정요인 방식은 기대(예: OIS 곡선)에 크게 의존하므로 기대오차가 크면 기저가 커지고 변동성도 증대됨; 조정요인은 OIS로 헤지하거나 계약상 만기 보상으로 처리 가능함.
- 저자 주장: 관측기간을 단축하면 사전확정성(quarterly 지급)을 유지하면서도 advance basis를 실무적으로 낮출 수 있어, RFR 도입을 촉진하는 현실적 해법이 될 수 있음.

## 메커니즘과 연결고리

- advance basis는 동일한 만기의 연속된 복리(in‑arrears 다음 기간과 이전 기간 복리)의 차이로 발생하며, 중앙은행의 이산적(계단형) 금리정책 전환시 특히 확대됨.
- 파생 기반 전진(term) 금리는 기대오차·기간 프리미엄(terminflation/term premium)·파생시장 유동성 변화에 의해 in‑arrears와의 괴리를 가질 수 있음(α 기저).
- 조정요인(µ_Y)은 계약 초에 마지막(미실현) 복리 지급분을 추정해 PV 차이를 보정하는 방식이며, 추정근거로 OIS 곡선을 사용하면 헤지 가능하지만 기대오차에 취약함.
- 관측기간 단축(예: 직전 1주)은 과거 전체 기간보다 최신금리 정보를 더 반영해 응답성을 높이고 advance basis 평균·변동을 줄이나, 표본이 작아져 금리 자체의 단기 변동성은 증가함.
- 헤지 메커니즘으로는 OIS를 이용한 파생 헤지(조정요인의 경우) 또는 계약상 마지막 지급시점에 in‑arrears와의 차이를 정산하는 방식(계약적 보완)이 존재함.

## 한계와 적용 범위

- 저자 명시 한계: 본문 경험적 분석은 EFFR(및 SOFR 프록시)을 사용한 USD계 예시 중심이며, SOFR 자체의 장기간 관측치가 부족해 프록시 사용·일부 근사를 포함함.
- 저자 명시 한계: 조정요인(µ_Y) 유도에서 단순 근사(예: 로그 근사 ln(1+x)≈x, 할인 무시 등)를 사용해 수학적 정확도가 완전하지 않음(소규모 x 가정 필요).
- 저자 명시 한계: 전진형(term from derivatives)은 파생시장 유동성·위기시 수급 붕괴 위험에 민감하므로 모델·가격 추정의 안정성이 제한될 수 있음.
- 저자 명시 한계: 'in advance' 방식은 LIBOR가 포함한 신용·유동성 민감성(은행 자금조달비용 반영)을 재현하지 못함(신용요소가 필요한 상품에는 부적절).
- 분석자(도서관원) 범위주의: EFFR 결과를 SOFR·다른 통화권 RFR에 일반화할 때 각국 시장구조·파생유동성·법규 차이로 성능 차이가 날 수 있음(논문도 제한적 언급).
- 분석자 범위주의: 제시된 통계(평균·표준편차)는 특정 샘플기간(2002–2020)의 역사적 사건(예: GFC, 2019 스파이크)에 민감하므로 향후 구조 변화시 재평가 필요함.
- 분석자 범위주의: 단축 관측기간 선택(예: 1주)은 기저 축소와 함께 금리변동성(일별·단기 변동)의 증가를 초래할 수 있으며, 실무 수용성(회계·리스크관리·규제준수)은 추가 검증 필요.
- 분석자 범위주의: 조정요인·계약적 보상은 법률·회계·상업적 합의가 필요하고 실행상 복잡성·거래상대방신용위험(대비 자체 위험) 발생 가능.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_891-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[글로벌 유동성]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work891.pdf](https://www.bis.org/publ/work891.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work891.htm](https://www.bis.org/publ/work891.htm)


## References

[1]: https://www.bis.org/publ/work891.pdf "BIS Working Paper 891: At the crossroads in the transition away from LIBOR - from overnight to term rates"
