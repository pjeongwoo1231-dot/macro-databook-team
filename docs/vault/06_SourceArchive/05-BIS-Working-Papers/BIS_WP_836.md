---
title: "BIS WP 836 — FX spot and swap market liquidity spillovers"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 836
published: "January 2020"
authors: "Ingomar Krohn and Vladyslav Sushko"
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
  - "fx-liquidity"
  - "fx-swaps"
  - "spot-market-liquidity"
  - "funding-liquidity"
  - "covered-interest-parity"
  - "dealer-behaviour"
  - "g-sibs"
  - "market-microstructure"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 836 — FX spot and swap market liquidity spillovers

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

이 논문은 Refinitiv의 딜러·클라이언트 호가를 사용해 JPY/USD와 EUR/USD의 스팟·1개월 스왑 시장 유동성을 동시에 분석했다. 주요 발견은 (1) 스팟과 스왑 유동성의 강한 공동변동성, (2) 스왑의 포워드 할인(CIP 편차)으로 측정되는 펀딩유동성 악화가 스왑뿐 아니라 스팟 스프레드 확대와도 연관된다는 점, (3) 이러한 펀딩→시장 유동성 연결이 2014년 중반 이후 강화되었고 분기말에 특히 심화되었다는 점이다. 원인은 대형(G-SIB) 딜러의 분기말 스왑 호가 축소(윈도우드레싱)와, 이로 인한 소형 딜러의 대체공급이나 가격발견 기여 부족으로 설명된다. 다만 분석은 특정 데이터(Refinitiv 호가), 통화쌍(JPY/EUR-USD), 만기(1개월)와 기간(2010–2017)으로 한정되며 거래체결·볼륨·호가깊이 미포함, 인터딜러 시장 미포착 등으로 외삽(일반화)과 인과 귀속에는 주의가 필요하다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | FX 스팟과 1개월 FX 스왑 시장의 유동성은 어떻게 상호연계되어 있으며, 특히 스왑(펀딩) 유동성의 변동이 스팟(시장) 유동성에 어떤 전파(스필오버)를 일으키는가? |
| 방법 | Refinitiv Tick History의 딜러별 밀리초·틱 단위 호가를 시간(hourly) 단위로 집계(마지막 호가)하고, 스팟·1개월 스왑(스왑포인트)·OIS로부터 각각의 호가 기반 시장유동성(매수·매도 스프레드)과 펀딩유동성(포워드 할인·CIP 편차)을 계산함. 거래량·체결정보 대신 호가·호가빈도·고유딜러수·딜러클래스(G-SIB 대 비G-SIB)·은행별 분기별 재무지표(S&P Capital IQ)를 결합. 시계열 인과관계는 ARDL 기반 조건부 오차수정모형(ECM)과 Pesaran-Shin-Smith 바운드 테스트, 분산·회귀·패널회귀(은행별 QE 활동비율)로 분석함. 식별전략으로 분기말(quarter-end) 특수를 외생적 펀딩충격 식별변수로 활용. |
| 자료·범위 | 샘플: 2010-02-01 ~ 2017-05-31. 통화쌍: JPY/USD, EUR/USD. 거래수단: 스팟 호가와 1개월 스왑 포인트 호가(Refinitiv). 은행 재무데이터: 분기별 S&P Capital IQ. 분석단위: 시간별(주요 결과는 hourly→일·분기 요약). 주의: 주로 딜러→클라이언트 호가를 포착하며 상호딜러(brokered) 인터딜러 시장·다른 전자거래소 일부(EBS 등)는 완전 포괄하지 않음. |
| 주제 | FX liquidity, FX swaps, spot market liquidity, funding liquidity, covered interest parity, dealer behaviour, G-SIBs, market microstructure, window dressing, regulatory effects |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장: 스팟과 1개월 스왑의 호가(매수·매도 스프레드)는 강한 공동변동성을 보이며 두 시장의 시장유동성은 밀접히 연계되어 있다.
- 저자 주장: 스왑에서 관찰되는 포워드 할인(및 CIP 편차)으로 측정한 FX 펀딩유동성 악화는 스왑 시장의 스프레드 확대뿐만 아니라 스팟 시장의 스프레드 확대와도 강하게 연관되어 있다.
- 저자 주장: 이 스왑→스팟 유동성 연계(펀딩→시장 유동성 영향)는 대략 2014년 중반 이후 크게 강화되었고, 특히 분기말·연말에 더 두드러진다.
- 저자 주장: G-SIB로 분류된 대형 딜러들이 분기말·연말에 스왑 호가 게시를 줄이는(풀백) 경향이 확인되며, 이 행동이 스왑·스팟 유동성 악화와 CIP 위반과 연관된다.
- 저자 주장: 비(非)G-SIB 소형 딜러들이 대형 딜러의 공백을 일정 부분 메우지만, 소형 딜러의 스왑 스프레드는 대체로 더 넓고 포워드 호가의 분산(가격발견 기여)은 대형보다 약해 결과적으로 유동성 회복은 불완전하다.
- 저자 주장: 딜러 경쟁(호가 빈도·활성 딜러 수)의 시장유동성 개선 효과는 시기·시장별로 약화되었고, 특히 스왑 시장에서 대형 딜러의 한계적 개선효과가 줄어들었다.
- 정량적 언급(저자 제시): 펀딩유동성의 표준편차급 악화는 스왑 스프레드와 스팟 스프레드를 각각 수십 bp(예: JPY에서 수십bp 규모)로 확대시키는 것으로 보고된다.
- 저자 결론: 전반적으로 펀딩유동성이 스팟 시장 유동성의 중요한 결정요인이 되었으며, 대형 딜러의 분기말 창구정리가 스왑만이 아니라 스팟에도 유동성 리스크 전파를 일으킨다.

## 메커니즘과 연결고리

- 스왑 가격(스왑포인트)의 포워드 할인은 한 통화를 다른 통화로 단기 자금을 조달하는 비용을 반영하여 FX 펀딩유동성을 전달하는 채널 역할을 한다.
- 대형(G-SIB) 딜러는 규제상 복잡성·G-SIB 점수·자본·유동성 비율을 관리하기 위해 분기말에 스왑 포지션·호가를 줄이는 '윈도우드레싱'을 하며, 이로 인해 스왑 유동성이 악화된다.
- 스왑 유동성 악화는 스왑의 포워드 가격 형성 과정을 통해 스팟 가격 산정에 영향을 주어 스팟 스프레드를 확대시키는 스필오버를 발생시킨다.
- 소형 딜러의 대체 공급은 호가(스프레드)가 넓고 포워드 호가 분산이 커 가격발견 기여도가 낮아 완전한 유동성 회복을 가져오지 못한다.
- 딜러 경쟁(호가 빈도·활성 딜러 수)의 축소는 시장유동성 개선의 한계효과를 약화시키며, 이 효과는 스왑에서 더 뚜렷하다.

## 한계와 적용 범위

- 데이터 대표성: 분석은 Refinitiv에 제출된 딜러·클라이언트 전자호가에 의존하며, 브로커드 인터딜러 시장(예: EBS)과 일부 거래·호가·거래소 채널은 포착이 제한되어 있어 전체 FX 시장을 완전하게 대표한다고 보기 어렵다.
- 관측치 제한: 데이터에 체결가격·거래량·호가깊이(order-book depth) 정보는 없어 유동성 측정이 호가 기반(스프레드) 지표에 국한된다.
- 상품·기간 범위: 분석은 JPY/USD와 EUR/USD 두 교차에, 1개월 스왑만을 대상으로 하므로 결과를 다른 통화쌍·만기(예: 장기 크로스커런시 스왑)로 일반화할 때 주의가 필요하다.
- 식별 및 해석 한계: 분기말을 '외생적' 펀딩충격 식별자로 사용했으나 분기말 행태는 규제·수요·시즌성 등 복합요인에 결합되어 있어 완전한 외생성은 보장되지 않는다; 규제 도입 시계열(점진적 적용)로 인해 규제효과 귀속에는 시차·혼동요인이 존재한다.
- 모형·통계적 한계: ARDL/ECM 접근은 장기공적관계 가정과 구조적 안정성을 전제로 하며, 저자도 2014년대에 구조적 변화(분기점)를 확인하여 샘플을 분할했으나 추가적인 미발견 구조전환 가능성은 남아 있다.
- 은행자료 제약: 은행별 분기재무데이터(S&P Capital IQ) 표본이 완전하지 않아 패널분석의 표본크기가 제약되고 일부 추정은 표본감소에 민감할 수 있다.
- 측정 해석: 포워드 할인·CIP 편차를 펀딩유동성의 직접적 지표로 사용하지만, 이들에는 신용프리미엄·거래비용·수요구조 변화 등 다른 요인도 섞여 있을 수 있다.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_836-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[글로벌 유동성]]
- [[산업생산]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work836.pdf](https://www.bis.org/publ/work836.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work836.htm](https://www.bis.org/publ/work836.htm)


## References

[1]: https://www.bis.org/publ/work836.pdf "BIS Working Paper 836: FX spot and swap market liquidity spillovers"
