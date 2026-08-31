---
title: "BIS WP 888 — Competitive effects of IPOs: evidence from Chinese listing suspensions"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 888
published: "September 2020"
authors: "Frank Packer and Mark M Spiegel"
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
  - "initial-public-offerings-(ipos)"
  - "china"
  - "competition"
  - "asset-space-competition"
  - "listing-suspensions"
  - "event-study-/-panel-regression"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 888 — Competitive effects of IPOs: evidence from Chinese listing suspensions

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

저자들은 중국의 전면적 IPO 중단 사례를 이용해, 산업 내 대기 IPO의 규모(또는 지연일 가중 규모)가 큰 경우 기존 상장기업이 중단 공시에서 상대적 이익을 보는 '직접적 경쟁 완화' 효과를 실증했고, 과거 수익률 공분산이 높은 경우에는 '자산공간(대체자산) 효과'도 관찰되었다고 주장한다. 또한 더 수익성·생산성이 높은 기업은 이런 호재로부터 덜 이득을 본다는 이질성 결과를 보고한다. 다만 식별은 중단의 예기치 않음과 투자자의 기대가 불편향적이라는 가정에 의존하며, 자산공간 채널의 상호작용 항은 표본·추정방법에 따라 민감하게 변동해 해석에 주의가 필요하다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 중국의 전면적 IPO 중단(상장 보류) 공시가 기존 상장기업의 주가에 어떠한 경쟁적 영향을 미치는가? (직접적 산업경쟁 채널과 자산공급·상관관계 채널의 상대적 중요성 및 기업별 이질성) |
| 방법 | 세 차례(2008–09, 2012–14, 2015) 중국의 전면 IPO 중단 공시 시점을 이용한 패널 OLS 회귀분석(산업별 클러스터 표준오차). 종속변수는 공시 직후 1일(및 민감도 점검을 위한 2일) 주가수익률. 주요 설명변수는 i) 산업 수준에서 대기 중인(지연된) IPO의 시장가치 비중(IP O) 및 지연일 가중치(DIP O), ii) 개별주식의 과거 3년 월수익률과 IPO 대기 포트폴리오의 공분산(COV). 성과(수익성·생산성) 지표와 상호작용항으로 이질성 검정. 추가로 가중최소제곱, 윈저·트림, 서브샘플(국유·비국유, 거래소별) 등 강건성 검사 수행. |
| 자료·범위 | 상하이·선전 거래소 상장기업 패널(총 관측치 약 6,045개), 세 번의 IPO 중단 시점에 각각 관측. 중단으로 연기된 IPO 대기기업 총 158개(2008:30, 2012:66, 2015:62). 주요 데이터원은 WIND(재무·시장지표) 및 CSRC(승인·중단일). 주요 변수: 공시 전 3년 수익률로 계산한 공분산, IPO 실현액(후속 상장 기준)으로 산출한 산업내 비중, 수익성(영업·순이익성 등), 레버리지·시가총액·P/B 등 통제변수. 사건창 기본은 1일(추가로 2일 검사). |
| 주제 | Initial public offerings (IPOs), China, Competition, Asset-space competition, Listing suspensions, Event study / panel regression |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장: IPO 중단 공시는 산업에서 대기 중이던 IPO의 비중이 큰 기존 상장기업에 대해 평균적으로 긍정적(초과) 주가효과를 가져왔다(직접적 경쟁 채널 지지).
- 저자 주장: 상장 대기기업과 수익률이 과거에 높게 공분산을 보였던 상장기업도 공시일에 더 높은 수익을 기록했고(자산공간 채널 지지), 이는 IPO가 '유사한 리스크·수익 특성'의 자산 공급을 증가시킬 수 있음을 시사한다.
- 저자 주장: 기업 성과(수익성·생산성)가 좋은 기업일수록 IPO 중단의 긍정적 효과로부터 덜 이득을 보았고(상호작용 효과), 즉 취약한 기업들이 더 민감하게 반응했다.
- 저자 주장: 결과는 다양한 성과 지표(순이익률, ROA, ROE, ROI, 영업생산성)와 DIPO(지연일 가중)로 대체해도 전반적으로 견고하게 유지된다.
- 저자 언급·발견: 자산공간 채널(COV)과 그 성과 상호작용 항은 직접 경쟁 채널보다 통계적·방법론적으로 덜 강건한 경향이 있다(특히 대형주·상하이 상장군, WLS 적용 시 약화).
- 추가 관찰: 샘플·사양 변화, 윈저·트림, 가중회귀 등 다양한 강건성 검사에서 직접 경쟁 변수와 그 상호작용은 비교적 안정적이나, 자산공간 상호작용 항은 민감하게 변동했다.

## 메커니즘과 연결고리

- 직접적 경쟁 채널: 대기 중인 IPO의 예상공모(또는 시장가치)가 해당 산업의 기존 상장기업 시장점유·수익성에 위협이 되어, 중단 시점에 그 위험이 완화되어 기존 주가가 상승한다.
- 지연가중(DIP O): 규제기관이 큐를 존중해 긴 대기기간을 가진 IPO가 더 큰 충격을 주므로, 지연일로 가중한 산업별 비중이 큰 기업일수록 영향이 커진다.
- 자산공간(대체자산) 채널: 대기 IPO들이 제공할 유사한 위험·수익 특성의 투자대안(자산공급)을 줄이면, 기존의 높은 공분산을 가진 상장기업에 대한 수요가 상대적으로 유지되어 주가가 상승한다.
- 이질성 기제: 수익성·생산성이 높은 '건강한' 기업은 경쟁 충격에 대한 방어력이 커서, 동일한 산업·공분산 노출을 가진 경우에도 중단의 긍정적 영향이 작게 나타난다.

## 한계와 적용 범위

- 저자들도 지적하는 바와 같이 IPO 중단 자체는 종종 거시·시장 여건 악화에 대응해 시행되어 중단 공시가 집합적 거시신호(부정적 정보)를 포함할 수 있어 완전한 외생성은 제한적이다.
- 식별은 '중단이 예기치 못했다'는 가정과 투자자가 대기 IPO들의 최종 규모·상장여부를 불편향적으로 기대했다는 가정에 의존한다; 논문은 이 가정을 직접 검증하지 못함.
- COV(자산공간) 지표는 과거 3년 월수익률 공분산과 실현된 IPO 크기 가중치를 사용하므로, 향후 공분산 구조 변화나 IPO가 실제로 실현되지 않는 경우에 측정오차가 발생할 수 있다.
- 사건창을 주로 1일(및 일부 2일)로 좁게 설정해 단기 주가효과만 평가하며 중·장기 실적·운영적 영향은 제한적으로만 논의됨(관련 연구와 차별화는 있으나 장기효과는 별도 분석 필요).
- 샘플은 중국의 세 번의 대규모 중단 사례에 한정되어 결과의 국제적 일반화에는 제한이 있다.
- 산업 클러스터 표준오차·표본 가중 등 표준오차 처리에 민감도가 일부 관찰되며, 특정 서브샘플(상하이 상장군, 대형주 등)에서 효과 강도가 변동함.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_888-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[산업생산]]
- [[통화정책]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work888.pdf](https://www.bis.org/publ/work888.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work888.htm](https://www.bis.org/publ/work888.htm)


## References

[1]: https://www.bis.org/publ/work888.pdf "BIS Working Paper 888: Competitive effects of IPOs: evidence from Chinese listing suspensions"
