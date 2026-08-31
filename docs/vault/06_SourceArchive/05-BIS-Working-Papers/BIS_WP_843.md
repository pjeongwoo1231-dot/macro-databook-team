---
title: "BIS WP 843 — Dollar borrowing, firm-characteristics, and FX-hedged funding opportunities"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 843
published: "February 2020"
authors: "Leonardo Gambacorta , Sergio Mayordomo and José María Serena Garralda"
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
  - "covered-interest-rate-parity"
  - "corporate-basis"
  - "dollar-borrowing"
  - "foreign-currency-issuance"
  - "firm-level-determinants"
  - "bond-spreads"
  - "fx-hedged-funding"
  - "limits-of-arbitrage"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 843 — Dollar borrowing, firm-characteristics, and FX-hedged funding opportunities

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

이 연구는 2007–2016년 기업-채권 매칭 데이터를 이용해 '기업기준'(크로스통화 베이시스 + 잔차화 신용스프레드)이 긍정적일 때 비미국 선진국 기업이 로컬 차입을 합성(달러발행+스왑)으로 대체한다고 실증한다. 핵심 발견은 고신용 기업이 기업기준 확대에 더 민감하게 반응해 달러 발행을 늘리는 반면, 달러 자산·매출이 큰 기업은 이미 높은 달러 발행 비중을 유지하되 기업기준 변화에는 덜 반응한다는 점이다. 다만 표본이 선진국 상장 대형기업에 국한되고 달러 노출 측정·내생성 문제 등 식별상의 제약이 있어 결과 해석과 일반화에는 주의가 필요하다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 비(非)미국 비금융기업의 달러 채권 차입이 기업 특성(신용등급·달러 자산·달러 매출)과 FX-헤지 비용절감 기회(기업 기준, corporate basis)에 어떻게 연관되는가? |
| 방법 | 기업-채권 매칭 데이터(기업 재무제표·채권발행)를 사용해 1) 잔차화된 기업 신용스프레드를 분기 단위 횡단면 회귀로 추정(채권·발행자 특성·통화-분기 더미 포함), 2) 기업기준(corporate basis)=5년물 크로스통화 스왑 베이시스(CIP 편차)+잔차화 신용스프레드로 구성, 3) 종속변수는 분기별 기업의 달러채권 비중(달러/(달러+자국통화))이며 로지스틱 링크를 쓴 GLM(분수응답)으로 추정, 4) 신용위험·달러 자산·상호작용항·다수 통제변수 포함, 5) 견고성으로 유사분석(유로 참조), 등급 관련 결과에 대해 Coarsened Exact Matching(CEM) 가중치를 이용한 보정 실시. |
| 자료·범위 | 기본 샘플은 2016년 12월 시점 주요 글로벌 지수 구성 종목인 7,211개 비금융기업(미국·유로존·일본·영국·스위스·캐나다)과 2007Q1–2016Q4의 기업별 분기 발행액(통화별) 매칭. 잔차화 신용스프레드 추정에는 2004Q1–2016Q4 기간의 기업채 약 40,614개(5,082개 기업)를 사용. 기업별 달러 발행자 분포(예: 일본 253, 유로지역 208, 영국 126, 캐나다 101, 스위스 41) 등으로 분석을 수행. 달러 노출(자산·매출)은 공시된 지리적 세그먼트(미국/아메리카)를 기준으로 마지막 이용 가능 재무제표에서 이진·연속 지표로 측정. 표본은 선진국 기업에 한정(신흥국 제외). |
| 주제 | covered interest rate parity, corporate basis, dollar borrowing, foreign currency issuance, firm-level determinants, bond spreads, FX-hedged funding, limits of arbitrage |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장: 기업기준(corporate basis)이 확대될 때(즉, 달러로 발행해 자국통화로 스왑하는 것이 상대적으로 저렴할 때) 비미국 비금융기업의 달러 발행 비중이 평균적으로 증가한다.
- 저자 주장: 이 효과는 2013–2016 후기(포스트-위기) 기간에 더 뚜렷하며, CIP 편차와 신용스프레드 불균형이 컸던 시기에 강하다.
- 저자 주장: 신용도가 매우 높은(AA- 초과) 기업은 기업기준의 확대에 대해 달러 전환 민감도가 더 크다(즉, 안전등급 기업이 FX-헤지 수익 기회를 더 적극적으로 이용).
- 저자 주장: 달러 매출 또는 장기달러자산이 큰 기업은 대체로 달러 발행 비중이 높아 자산·부채 통화매칭(헤지)을 위해 달러 발행을 유지하지만, 기업기준 변화에는 민감하게 반응하지 않는다.
- 저자 주장: 달러 자산·매출 노출이 없는 기업은 기업기준이 확대될 때 로컬 차입 대신 합성(달러발행+스왑) 차입으로 전환하는 경향이 있다.
- 저자 주장: 결과적으로 기업기준이 확대되면 달러 차입자의 구성(composition)이 바뀌어 고신용 등급 기업의 비중이 상대적으로 증가한다.
- 저자 주장: 유로를 외화로 삼는 검증에서는 유사한 방향성이 있으나 표본과 검열(censoring) 문제가 있어 결과 해석에 주의가 필요하다.

## 메커니즘과 연결고리

- 기업기준(=크로스통화 스왑 베이시스 + 잔차화 신용스프레드)이 양(+)이면 '달러로 발행 후 자국통화로 스왑'하는 합성 차입이 직접 자국통화 발행보다 비용적으로 유리해진다.
- 고신용(very high-grade) 기업은 투자자에게 달러 안전자산의 대체물을 제공할 수 있어, 달러 안전자산 부족시 기업기준 확대에 따른 자금조달 기회를 더 적극적으로 활용한다.
- 달러로 가격표시되는 자산(달러 매출·장기자산)을 보유한 기업은 통화매칭 목적상 달러 발행 비중이 높아지며, 이러한 기업들은 기업기준 변화와 무관하게 달러 발행을 지속하는 경향이 있다.
- 중개기관의 한계(CIP 편차)는 FX 헤지 비용을 변화시키고, 이로 인해 합성로컬차입 수요가 유발되어 통화 선택(발행통화)이 변한다.
- 기업기준 확대는 단순히 전체 달러발행을 늘리기보다 발행자 구성(신용구조·노출구조)을 변화시켜 '더 안전한' 발행자 비중을 높인다.

## 한계와 적용 범위

- 표본 범위 제한: 분석은 주요 선진국에 본사를 둔 상장 대형기업에 한정되어 있어(글로벌 지수 구성종목), 결과를 중소기업이나 신흥국으로 일반화하기는 어렵다.
- 자산·매출 달러 노출 측정 한계: 지리적 세그먼트(미국/아메리카)에 기반한 이진·비율 지표를 사용하고 마지막 공시 재무제표를 고정적으로 활용해 시계열 변화를 반영하지 못하며 '미국 지역 = 달러노출' 가정이 완전하지 않을 수 있다.
- 식별의제한: 기업기준과 달러 발행 모두 기업의 발행 전략·시장참여·신용상태와 동시결정적일 수 있어 잠재적 내생성(endogeneity) 문제가 존재한다(논문은 광범위한 통제와 고정효과 사용으로 일부 보정했으나 완전한 인과식별을 보장하지는 않음).
- 잔차화 신용스프레드 한계: 횡단면 회귀로 통화·분기 고정효과를 통해 잔차를 얻지만 관측 불가능한 통화별·시기별 위험요인이나 비대칭적 수요충격이 완전히 제거되었는지는 불확실하다.
- 관찰 가능성(샘플 사이즈) 제한: 동일 발행자가 다통화로 발행한 경우가 상대적으로 적어(다통화 발행 기업 수 제한) 통화간 비교에 표본제약이 존재한다.
- 유로 관련 결과의 취약성: 유로를 대상으로 한 검증은 발행건수 부족과 검열(많은 관측치가 0 또는 1에 몰림)으로 해석에 유의해야 한다.
- 정책·시장구조 변화 반영 한계: 기업기준은 중개기관의 헤지공급능력·전세계 안전자산 수요 등 구조적 요인에 민감한데, 이러한 구조 변화의 이질적 영향은 완전히 분리되지 않음.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_843-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[신용스프레드]]
- [[산업생산]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work843.pdf](https://www.bis.org/publ/work843.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work843.htm](https://www.bis.org/publ/work843.htm)


## References

[1]: https://www.bis.org/publ/work843.pdf "BIS Working Paper 843: Dollar borrowing, firm-characteristics, and FX-hedged funding opportunities"
