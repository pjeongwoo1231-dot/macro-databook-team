---
title: "BIS WP 847 — The dollar, bank leverage and real economic activity: an evolving relationship"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 847
published: "March 2020"
authors: "Burcu Erik , Marco Jacopo Lombardi , Dubravko Mihaljek and Hyun Song Shin"
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
  - "financial-conditions"
  - "us-dollar-exchange-rate"
  - "bank-leverage"
  - "global-pmis"
  - "world-trade"
  - "nowcasting"
  - "covered-interest-parity"
  - "market-based-intermediation"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 847 — The dollar, bank leverage and real economic activity: an evolving relationship

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

저자들은 GFC 이후 금융중개 구조의 변화(은행권 약화·시장중개 확대)와 CIP 편차 확대 등으로 인해 광범위한 달러지수가 글로벌 제조업 PMI와 세계무역에 미치는 영향이 강화되었고, 전통적 위험지표인 VIX의 설명력은 감소했다고 주장한다. 분석은 월별 VAR과 금융지표 주성분을 이용한 현측·충격반응분석을 통해 이 같은 구조적 변화의 정합성을 제시하나, 식별과 표본선택·인과채널 분리 측면에서 추가적 미시증거와 신중한 해석이 필요하다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 금융여건(특히 광범위한 달러지수)이 글로벌 제조업 PMI와 세계무역 성장에 미치는 영향이 대(大)금융위기 전후로 어떻게 변화했는가? |
| 방법 | 월별 소규모 VAR(6지연)과 월별 회귀(현월 PMI를 금융지표 1주성분으로 설명), 표본을 사전-GFC(1998–2007)와 사후-GFC(2010–2019)로 분리하여 충격반응함수와 요인 적재(factor loading) 변화를 비교. PMI 관련 변수는 설문 중앙일 전후 30일 변화로 계산하여 시점정을 반영. 식별은 Cholesky(주식→달러→PMI→무역) 시계열 순서 기반. |
| 자료·범위 | 1998년 2월~2019년 10월(전체), 사전-GFC(1998–2007)와 사후-GFC(2010–2019) 분할표본; 변수: 세계주가지수(가중평균), FRB 무역가중 달러지수(여러 버전 사용), 글로벌 제조업 PMI(미국 제외), 세계무역량 지수, VIX, 기업스프레드, 달러표시 대외신용·대출(EME 대상) 등. 월간 변경은 PMI 설문 중심 30일 창으로 계산. |
| 주제 | financial conditions, US dollar exchange rate, bank leverage, global PMIs, world trade, nowcasting, covered interest parity, market-based intermediation |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자들은 대(大)금융위기 이전에는 달러 절상 충격이 글로벌 PMI와 세계무역을 다소 확장시키는 반응을 보였다고 보고한다.
- 저자들은 대금융위기 이후에는 달러 절상 충격이 글로벌 PMI와 세계무역을 수축시키는 방향으로 관계가 역전되었다고 주장한다.
- 저자들은 VIX의 설명력이 사후(GFC) 기간에 감소했고, 반대로 달러지수의 영향력이 증가했다고 보고한다(금융지표 1주성분의 적재 변화).
- 저자들은 GFC 이후 공식은행권 자산·자본 성장 둔화와 더불어 시장기반 중개(market-based intermediation)의 상대적 중요성 증가를 관찰한다.
- 저자들은 달러 강세가 EME에 대한 달러표시 신용성장의 둔화와 음(負)의 상관관계를 보이며, 달러는 은행 대차대조표비용의 바로미터 역할을 한다고 제시한다.
- 저자들은 금융지표 1주성분을 이용한 PMI 현측(nowcasting) 성능이 벤치마크(AR(1))에 비해 유의미한 개선을 보이나, GFC를 제외하면 개선폭이 줄어든다고 보고한다.
- 저자들은 CIP 편차의 확대와 달러강세의 관련성을 관찰하며, 이는 달러가 '밸런스시트 비용(price of balance sheet)'의 지표 역할을 할 수 있음을 시사한다고 주장한다.

## 메커니즘과 연결고리

- 밸류앳리스크(VaR)·리스크수용능력 채널: 달러 절상/절하는 글로벌 은행의 포트폴리오 위험과 VaR 제약을 변동시켜 달러표시 대출 공급을 조정함.
- 대차대조표 비용 채널(CIP 관련): CIP의 붕괴·편차 확대를 통해 달러 강세가 은행의 달러 조달비용을 상승시켜 신용공급을 축소할 수 있음.
- 운전자본(working capital) 채널: 글로벌 공급사슬에 참여하는 제조업체는 달러표시 신용에 의존하므로 달러 신용경색은 실물생산·무역을 제약함.
- 송장(invoicing) 통화 채널: 달러로 청구되는 무역의 경우 달러 강세가 비(非)미국 쌍국 간 무역량에 경쟁력 영향을 주어 무역을 감소시킬 수 있음.
- 시장기반 중개 확대 채널: GFC 이후 시장기반·비은행중개자 비중 증가로 달러와 금융여건의 연결 고리가 강화됨.

## 한계와 적용 범위

- VAR 식별은 Cholesky 순서(주식→달러→PMI→무역)에 의존하며 이는 시점(타이밍) 가정에 크게 의존한다(설문 응답이 중앙일에 이뤄진다는 추가 가정 포함).
- 연구는 GFC 기간을 의도적으로 제외하여 위기 자체의 역학이 결과에 미치는 영향을 배제했으므로 위기 중·직후 거동을 일반화하기 어렵다.
- 달러충격의 원인(예: 통화정책·무역·위험회피 등)을 완전히 분리하지 못해 인과관계 해석에 제한이 있다.
- 금융지표 1주성분은 여러 변수의 선형 결합이며, 특정 변수(달러·VIX 등)의 역할은 주성분 구성에 민감할 수 있다.
- 은행 레버리지 관련 관찰은 브로커-딜러 섹터 및 표본 은행 그룹에 기초하므로 모든 은행·비은행 중개자에 보편적으로 적용되기 어렵다.
- 무역·신용·PMI 관계는 표본(1998–2019, 종료 2019년 10월)과 사후 완화된 통화·규제 환경 등 시기 특수성에 영향을 받을 수 있어 이후 기간으로 일반화할 때 주의가 필요하다.
- 논문 자체가 제시하는 한계: 달러의 역할이 늘어났다는 결과는 관측된 연관성에 근거하며, 정확한 채널(인보이싱 vs 자금공급 등)을 완전히 구분하려면 결합된 미시자료 분석이 필요하다고 명시됨.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_847-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[PMI (구매관리자지수)]]
- [[DXY (달러지수)]]
- [[산업생산]]
- [[VIX]]
- [[통화정책]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work847.pdf](https://www.bis.org/publ/work847.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work847.htm](https://www.bis.org/publ/work847.htm)


## References

[1]: https://www.bis.org/publ/work847.pdf "BIS Working Paper 847: The dollar, bank leverage and real economic activity: an evolving relationship"
