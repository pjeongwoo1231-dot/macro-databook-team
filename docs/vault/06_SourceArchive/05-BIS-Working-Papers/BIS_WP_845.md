---
title: "BIS WP 845 — Foreign banks, liquidity shocks, and credit stability"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 845
published: "March 2020"
authors: "Daniel Belton , Leonardo Gambacorta , Sotirios Kokas and Raoul Minetti"
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
  - "foreign-banks"
  - "liquidity-shocks"
  - "wholesale-funding"
  - "syndicated-loans"
  - "fdic-assessment"
  - "bank-lending-channel"
  - "liquidity-hoarding"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 845 — Foreign banks, liquidity shocks, and credit stability

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

저자들은 2011년 FDIC의 평가기준 변경이 미국 내 보험대상 은행과 비보험(외국계 지점)에 상반된 자금비용 충격을 야기했다고 가정하고(DID), 이를 콜리포트·DealScan 매칭자료로 분석하였다. 핵심 결과는 비보험 외국계 지점이 상대적 자금여건 개선에도 불구하고 준비금·현금 보유를 늘리며 신디케이트론 참여(리드빈도·점유율·건수·총액)를 줄였다는 것이다. 저자들은 IOER, 대체불완전성, 대차대조표 비용 및 정보제약(모니터링·대출기회 제한)을 주요 기제로 제시한다. 다만 동시 발생한 국제충격·자료제약·내생성 문제 및 표본·제도적 특수성 때문에 인과해석과 일반화에는 주의가 필요하다는 점을 본문과 본 카드의 한계로 명시함.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 2011년 FDIC 평가기준 변경(평가기반 확대)이 미국 내 보험대상 은행과 비보험(외국계 지점)의 자금비용에 미친 차별적 충격이 은행의 유동성 보유와 신용공급(특히 신디케이티드론 참여)에 어떤 영향을 주었나? |
| 방법 | 콜리포트(FFIEC) 분기별 은행 대차대조표와 DealScan 신디케이트론을 손매칭하여, 비보험 비중을 처리그룹으로 한 차이의차이(DID) 추정. 은행패널에는 Arellano–Bond(동태 패널) 사용, 대출거래 수준 회귀에는 차입자·대출자 고정효과 포함한 OLS(강건표준오차·군집) 사용. 여러 견고성 검사(유럽·비유럽 분리, 외국보험은행 분리, 본국*연도 고정효과 등). |
| 자료·범위 | 2001Q1–2014Q2 표본(주요 결과는 2009Q2–2013Q1 근방 분석 포함). 자료: FFIEC 031/041(미국 은행 통합보고), FFIEC 002(외국은행 지점/대리점), FR Y-7Q, FR Y-9C(지주), DealScan(신디케이트론), Osiris(차입기업 재무). 신디케이트론은 신규·비금융·비공공유틸리티 대출, Term B 제외. 비보험군은 FDIC 보험평가 대상에서 면제된 약 200개 외국계 지점·대리점. |
| 주제 | foreign banks, liquidity shocks, wholesale funding, syndicated loans, FDIC assessment, bank lending channel, liquidity hoarding |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장: 2011년 FDIC 평가기준 변경은 보험은행에는 도매자금 비용을 상대적으로 높이는 충격이었고, 비보험 외국계 지점에는 상대적 자금비용 완화(긍정적 충격)를 제공했다고 식별됨.
- 저자 주장: 비보험 외국계 지점은 상대적으로 유동성(현금·준비금)을 유의미하게 늘림(유동성 비축·리저브 증가).
- 저자 주장: 동일시점에 비보험 외국계 지점은 신디케이트론에서 더 수동적이었음(리드 비중·리드 선임 확률·개별 딜 점유율 감소).
- 저자 주장: 광의적·집중적 측면 모두에서 신디케이티드 대출의 축소가 관찰됨(참가 건수·리드 건수·분기별 총 제공액 감소).
- 저자 주장: 대차대조표 수준에서는 총대출 및 C&I 대출이 제한적으로나마 감소하는 결과가 일부 사양에서 관찰됨(효과 크기는 신디케이트론 지표보다 작거나 비일관적).
- 저자 주장: 결과는 유럽지역 위기와 동시성 문제를 고려한 유럽·비유럽 분할, 외국 보험여부 분리, 본국*연도 고정효과 등에서 전반적으로 견조함.
- 저자 해석: 비보험 지점은 자금비용 개선에도 불구하고 IOER(초과지급준비 이자)·잔존한 대차대조표 비용·모니터링·대출기회 특성 등으로 유동성 보유를 선호하며 대출(특히 신디케이트론) 확대 대신 유동성 비축을 선택했다고 봄.

## 메커니즘과 연결고리

- 저자 제시 기제: FDIC 평가기준 확대는 보험은행의 도매자금 비용을 상대적으로 상승시켜 도매조달 축소 유인(소비·구조조정 유도).
- 유동성 보유 유인: IOER(연준의 초과지급준비 이자)로 초과준비 보유가 수익을 창출하여 유동성 비축 선호를 강화.
- 대체 불완전성: 소매예금과 도매자금 간 대체불완전성으로 인해 보험은행은 대체조달 비용 상승 → 대출 축소 가능.
- 잔존적 대차대조표 비용(레버리지 규제 등): 현금·준비금 증가는 레버리지 기준에서 비용을 유발해 대출 대신 보수적 운용 유도.
- 정보·선택제약: 외국은행은 불투명 차입기업에 대한 대출에서 소극적('체리픽'·모니터링 축소, 일종의 'lazy bank' 효과)일 수 있어 유동성 충격이 곧바로 대출확대로 연결되지 않음.

## 한계와 적용 범위

- 식별 한계: 처치변수는 정책시행(2011Q2) 전후 DID인데 무작위화 아님으로, 동시 발생한 충격(예: 유럽 주권위기) 완전 제거 불가 — 저자도 이 점을 인지하고 분할·본국*연도 FE 등으로 대응했으나 잔존 교란 가능성 있음.
- 자료·표본 범위: DealScan은 일부 거래의 은행별 점유율·담보정보가 결측이며 신디케이트론은 은행의 전체 대출 활동의 부분집합(연구 대상 외 대출·리테일 대출 제외). 따라서 전체 신용공급 일반화에는 제약이 있음.
- 측정·타이밍: FDIC의 구체적 평가율은 공개되지 않음. 본 연구는 정책 발효시점을 2011Q2로 지정(대안 시점도 점검)했으나 정책효과의 정확한 시점·경로에는 불확실성 존재.
- 외생성·선택문제: 은행의 신디케이트 참여 자체가 내생적(예: 은행·차입자 매칭 변화)이라 완전한 인과추론에는 추가 강한 가정 필요.
- 시계열·제도 한계: 표본은 2014Q2로 종료되어 이후 IHC 규제 변화(2015–2016) 등으로 인한 구조적 전환은 반영하지 못함.
- 해석 범위: 결과는 미국 시장·해당 기간(대규모 초과준비·IOER 존재) 특수성에 의존하므로 다른 제도·시기(예: IOER 부재)로 일반화시 주의 필요.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_845-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[글로벌 유동성]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work845.pdf](https://www.bis.org/publ/work845.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work845.htm](https://www.bis.org/publ/work845.htm)


## References

[1]: https://www.bis.org/publ/work845.pdf "BIS Working Paper 845: Foreign banks, liquidity shocks, and credit stability"
