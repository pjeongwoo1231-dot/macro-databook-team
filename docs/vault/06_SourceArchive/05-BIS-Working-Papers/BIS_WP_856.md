---
title: "BIS WP 856 — Volatility spillovers and capital buffers among the G-SIBs"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 856
published: "April 2020"
authors: "Paul D McNelis and James Yetman"
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
  - "volatility-spillovers"
  - "global-systemically-important-banks-(g-sibs)"
  - "bank-capital-(cet1)"
  - "connectedness"
  - "vector-autoregression-(var)"
  - "regularisation-/-elastic-net"
  - "diebold–yilmaz-generalized-fevd"
  - "market-based-risk-measures"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 856 — Volatility spillovers and capital buffers among the G-SIBs

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

이 논문은 일일 주식의 범위변동성(OHLC 기반 Garman–Klass 근사)을 이용해 VAR(정규화된 elastic net)과 Diebold–Yilmaz 일반화 FEVD로 G-SIB 간 변동성 스필오버를 측정했다. 주요 발견은 BCBS의 G-SIB 버킷이 높을수록 다른 G-SIB들에 대한 외향 스필오버가 크고, CET1 비율이 높을수록 특히 상위 버킷 은행의 스필오버를 더 크게 줄인다는 점이다. 결과는 미국상장 표본과 전체 국내상장 확장표본에서 일관되며 여러 로버스트니스 체크를 거쳤다. 다만 측정은 시장가격 기반의 변동성 공통성과 관련되며, 정규화·시계열 동기화·자본·버킷 간의 내생성 등 설계상 한계로 인해 인과관계가 완전히 확정되지는 않는다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | G-SIB들 간의 일일 주식 변동성(범위 volatility) 스필오버가 BCBS의 G-SIB 버킷과 어떻게 관련되는지, 그리고 CET1 자본비율이 이러한 스필오버를 감소시키는지 여부를 규명한다. |
| 방법 | 일일 OHLC(시가·종가·고가·저가)로부터 Garman–Klass 근사 범위변동성 산출, 이를 기초로 20개(미국상장) 및 확장된 31개(국내상장) G-SIB의 일별 범위변동성 시계열에 대해 lag=5인 VAR을 적합하되 파라미터 과다로 elastic net(α=0.5)으로 정규화 시행. λ는 5분할 시계열 교차검증으로 선택. Pesaran–Shin 일반화 예측오차분해(generalized FEVD)로 10일선행 분해를 구해 은행별 외향(outward)/내향(inward) 연결성 산출. 주로 150일 롤링(미국상장)·250일 롤링(전표본)으로 시계열 변화 추적. |
| 자료·범위 | 2007-10-18 ~ 2018-09-28 일별 주가(OHLC) 사용. 초기분석은 NYSE에 상장된 20개 G-SIB(ADR/ADS 포함), 확장분석은 본국 상장 기준의 31개 G-SIB(중국계는 홍콩 상장 가격 사용). CET1 비율은 분기별 보고치를 사용(결측 시 선형 보간). 아시아·유럽 거래시간 비동기성 문제를 확인하기 위해 아시아·유럽 데이터에 대해 0~1일 시차 실험 수행. |
| 주제 | volatility spillovers, global systemically important banks (G-SIBs), bank capital (CET1), connectedness, vector autoregression (VAR), regularisation / elastic net, Diebold–Yilmaz generalized FEVD, market-based risk measures |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장: BCBS가 부여한 G-SIB 버킷과 은행의 외향 연결성(다른 G-SIB들에 대한 변동성 스필오버 규모) 사이에 강한 양(+)의 상관관계가 존재함.
- 저자 주장: CET1 자본비율이 높을수록 외향 연결성이 감소하며, 이 효과는 G-SIB 버킷이 높을수록(더 체계적 중요도가 클수록) 더 크게 나타남(상호작용항 부호는 음성, 통계적 유의).
- 저자 주장: 전체 표본의 오프대각 합으로 계산한 총 스필오버 지수는 약 78.34%로 산출되었고, 롤링 추정치 기준으로는 많은 기간에 걸쳐 외향 연결성이 90%를 초과하기도 함(시점별 급증: GFC, 2011 신용등급 강등, 2015–16 등).
- 저자 주장: 미국상장 표본에서 Bank of America, BNY Mellon, Morgan Stanley 등이 순(순전달) 리스크 전파자(net transmitter)로 식별되었고 일부 은행(예: Credit Suisse, HSBC, ING, Wells Fargo)은 순수신자(net receiver)로 관찰됨.
- 저자 주장: 결과는 다양한 로버스트니스 검사에서 견조함(예: Tier 1 자본으로 대체, 정책불확실성 지표 추가, 아시아·유럽 록킹/시차 처리 등).
- 저자 주장: 미국상장 표본을 본국상장 표본(확대)으로 확장해도 주요 결과(버킷 양(+)관계, 버킷×CET1의 음(-) 상호작용)는 유사하게 나타남.

## 메커니즘과 연결고리

- 저자 제시 메커니즘: BCBS의 G-SIB 평가(규모·상호연결성·대체가능성·국경간 활동·복잡성 등)가 클수록 해당 은행의 문제에 대한 시장의 파급효과가 커져 외향 변동성 스필오버가 증가한다고 해석.
- 저자 제시 메커니즘: CET1 자본비율 증가는 해당 은행의 손실흡수능력을 높여 시장에서의 불안정성·전염성 정보를 완화하고, 따라서 다른 은행으로의 변동성 전달을 줄인다는 채널.
- 경기·정책·정황 충격(예: GFC, 미국 신용등급 강등, 브렉시트, 유가·중국 성장 둔화)은 동시다발적 변동성 상승을 야기하며, 이때 중심적 G-SIB들이 외향 스필오버 확대를 통해 타은행 변동성에 더 크게 기여.

## 한계와 적용 범위

- 저자들이 명시하거나 설계상 명백한 한계: 사용한 지표는 '일일 주식 변동성 범위'로 시장참가자의 위험인식(가격 반응)을 반영하나, 이는 대차대조표 기반의 직접적 재무전염이나 실제 디폴트 발생의 전파와는 동일하지 않음(시장 기반 척도).
- VAR+FEVD 접근은 설명변수 간 선형관계와 충격정의에 의존하며, 일반화된 FEVD로 변수순서 의존성은 제거했으나 VAR 모형화 자체의 가정(선형성, 정상성 등)은 결과에 영향 가능.
- 정규화(Elastic net)는 과다파라미터 문제를 완화하나 계수를 0으로 축소하는 특성 때문에 연결성 추정치가 과소편향될 수 있음(저자 지적).
- G-SIB 버킷과 CET1는 정책·보고체계에 의해 상호연관될 수 있어(예: 높은 버킷에 대한 규제상 추가 자본 요구) 내생성(endogeneity) 우려가 존재함; 저자도 이 문제를 부분적으로 논의하나 인과관계 확정에는 제한이 있음.
- CET1 비율은 분기 데이터여서 일일 롤링 외향 연결성과 시계열 동기화가 완전치 않음(결측치는 선형 보간 사용) — 자본비율의 시계열 측정오차 가능.
- 아시아·유럽·미국의 거래시간 비동기성을 보정하기 위해 0~1일 시차를 실험했으나, 이산 거래시간·뉴스·비동기 정보전파의 완전한 통제는 어려움.
- 회귀모형의 R2 수준(보고된 예: 0.24~0.29)은 설명력 제한을 시사하며, 기타 미측정 요인(비은행시장, 신용·유동성 시장채널 등)이 연결성에 기여할 수 있음.
- G-SIB 미지정 기간에 해당 은행을 버킷 0으로 처리한 코딩 결정은 일부 관측치의 해석에 영향 가능.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_856-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[통화정책]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work856.pdf](https://www.bis.org/publ/work856.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work856.htm](https://www.bis.org/publ/work856.htm)


## References

[1]: https://www.bis.org/publ/work856.pdf "BIS Working Paper 856: Volatility spillovers and capital buffers among the G-SIBs"
