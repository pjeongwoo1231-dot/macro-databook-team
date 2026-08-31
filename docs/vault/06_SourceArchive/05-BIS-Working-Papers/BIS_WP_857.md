---
title: "BIS WP 857 — International bank lending and corporate debt structure"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 857
published: "April 2020"
authors: "José María Serena Garralda and Serafeim Tsoukas"
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
  - "credit-lines"
  - "bank-capital-requirements"
  - "cross-border-bank-lending"
  - "non-bank-financial-intermediaries"
  - "corporate-debt-structure"
  - "difference-in-differences"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 857 — International bank lending and corporate debt structure

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

이 논문은 2011년 EBA의 자본요건 강화가 EU계 은행의 대외대출을 축소시키는 공급충격으로 작용했고, 특히 미국에 본사를 둔 상장기업의 경우 그 충격이 은행의 신용한도(commitments) 축소로 나타났다고 실증한다. 축소된 은행 신용한도는 미국 내 비은행(주로 투자은행 등)의 신용한도 확대(대체)를 통해 대부분 보완되었고 회사채시장은 유의미한 대체역할을 하지 못했다. 연구는 대형 상장기업·신디케이티드론 기반의 기업부채에 대한 단기효과를 규명하지만, SME·비상장기업·장기효과나 은행 내부 조정메커니즘에 대해서는 일반화하기 어렵다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 유럽감독기관(EBA)의 2011년 자본요건 강화(대상 EU은행)에 따른 국제적 은행 탈레버리지(shock)가 기업의 부채구조(은행대출·비은행대출·회사채)와 대출종류(신용한도 vs 기한부대출)에 어떤 영향을 미치며, 국내 비은행이 이를 대체할 수 있는가? |
| 방법 | 차이-인-차이(DID) 설계: 2009Q3–2014Q1 패널을 활용해 EBA의 2011Q3 자본요건 강화 전(2010Q2·2011Q2)과 후(2012Q3·2013Q3)를 비교·분석. 처리군은 2011Q2 시점에 유럽 은행 대출의 절반 이상이 EBA 대상은행에서 온 기업(=Treated), 대조군은 그 외 EBA 의존 유럽대출 보유 기업. 종속변수로 기업별 부채 스톡(은행대출·비은행대출·회사채, 신용한도·기한부 대출 구분). 기업 고정효과·자산규모·유형자산비율 통제, 표준오차는 기업단위 클러스터링. |
| 자료·범위 | 상장·공시기업 중심의 은행의존 기업 패널(총 2,830개 기업: EU 1,117개, 미국 1,415개, 기타 선진 215개), 기간 2009Q3–2014Q1. 회계자료는 Capital IQ, 채권·신디케이티드론은 Refinitiv SDC Platinum, 대주체·업종·국가정보는 Refinitiv Eikon 이용. 대출·채권은 원칙적으로 최종모회사(consolidated ultimate parent) 기준으로 통합 집계. 신용한도에는 미인출 약정 포함. |
| 주제 | credit lines, bank capital requirements, cross-border bank lending, non-bank financial intermediaries, corporate debt structure, difference-in-differences |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 결과: EBA의 자본요건 강화 이후 EBA-의존성이 높은 기업의 은행대출이 대조군보다 감소함.
- 저자 결과: 감소는 주로 미국에 본사를 둔 기업에서 관찰되며, EU에 본사를 둔 대형 상장기업의 은행대출은 탄력적(유의한 축소 없음).
- 저자 결과: 감소된 은행대출은 기한부(term)대출이 아니라 '신용한도(credit lines)'에서 주로 발생함 — 미국 기업의 은행 신용한도는 처리군에서 약 18% 감소.
- 저자 결과: 총 크레딧(은행+비은행) 수준은 처리군에서 급감하지 않았고, 미국 비은행(특히 투자은행 등)으로부터의 신용한도 확대가 관찰됨(비은행 신용한도는 처리군에서 약 64% 증가).
- 저자 결과: 회사채 발행 증가는 작고(기사단계 영향은 약 11%로 모호), 비은행 기한부대출은 유의한 증가를 보이지 않음. 즉 대체는 주로 비은행 신용한도를 통해 이뤄짐.
- 저자 결과: 신용 공급 이동은 주로 과거에 해당 시장을 이용한 '집약적(intensive margin)' 기업에서 발생 — 이전에 채권·비은행 대출 경험이 있던 기업이 대체 금융을 더 확보함.
- 저자 결과(구조적 함의): 국내 대출시장에서 은행·비은행이 공존하면 국외은행 자금 축소를 완화할 수 있으나, 비은행 비중 확대는 자금 조달의 취약성(도매성 단기조달 의존성) 증가로 이어질 수 있음.
- 저자 결과(시장구조): EBA 대상 은행은 미영업권에서의 순위·중요도가 하락했고(non-EBA·비은행이 일부 시장점유를 확대), 미국 리그테이블에서 비은행의 금액 기준 중요성이 상승하는 정황이 관찰됨.

## 메커니즘과 연결고리

- 저자 주장 메커니즘: EBA의 통합(consolidated) 자본요건 강화는 해당 은행들이 비거주 채무를 줄이는 식으로 포트폴리오 재조정(해외 익스포저 축소)을 유도했고, 이로써 대외 신용한도 공급이 감소함.
- 신용한도 특성: 신용한도는 유동성(비소비성 약정· contingency) 제공 수단이므로 은행이 유동성 제약에 직면하면 신용한도를 우선적으로 축소할 인센티브가 있음(기한부대출은 발행·판매가 용이해 은행이 덜 축소할 수 있음).
- 비은행 대체: 국내 비은행(주로 투자은행 등 도매성 자금조달 기관)은 단기 유동성·도매조달을 통해 신용한도를 제공할 수 있어 은행의 신용한도 축소를 부분적으로 대체함.
- 시장대체의 한계: 회사채시장은 주로 기한부 장기조달에 유리하므로(대형·공시기업 대상) 신용한도 축소에 대해 완전대체가 되기 어렵고, 실제로 채권증가 효과는 작거나 취약함.

## 한계와 적용 범위

- 논문 제시: 식별은 EBA 자본요건 강화가 은행측 공급충격을 유발했으며, 처리군의 수요(또는 수요의 상대적 변화)가 대조군과 다르지 않다는 가정에 의존함(공통추세 가정).
- 논문 제시: 표본은 상장·공시 기업 중심의 '대형·은행의존' 기업군으로 구성되어 중소기업(SME)이나 비공시·비상장 기업으로 일반화할 수 없음을 저자들이 명시함(특히 SME는 다른 영향받음).
- 논문 제시: 분석은 기업의 부채 스톡(기업 측 관찰치)을 이용하며 은행 측의 대차대조표·자금조달구조를 직접 관찰하는 연구설계가 아님 — 따라서 은행의 내부 조정 메커니즘은 간접적 추론에 의존.
- 논문 제시·보완: 유럽 재정위기(GIIPS) 영향 등 동시발생 충격 가능성을 고려해 GIIPS 대출을 제외하는 등 로버스트니스 점검을 수행했으나 완전한 동시충격 제거는 완전보장 불가.
- 방법·자료상 암시적 한계(분석가적 제언): 처리군 정의(2011Q2 기준 EBA 대출 비중 >50%)·리드어레인저 비중을 프로라타로 배분하는 방식 등은 결과에 민감할 수 있음(대체적 임계값·배분법에 따라 차이 가능).
- 방법상 한계: 패널을 사전·사후 두 시점으로 '압축'해 비교하는 설계(각 기간 내 2분기만 사용)로 단기(즉각적) 효과에 초점을 맞추며, 장기적 동학·지속성은 평가하지 않음.
- 자료·측정 한계: Refinitiv SDC·Eikon·Capital IQ의 관측 범위는 시장 전체와 완전일치하지 않을 수 있고, 리드어레인저·은행/비은행 분류에 일부 오분류 가능성이 존재.
- 외부적 해석주의: 리그테이블(대출 순위) 변동은 EBA 충격과 동시발생한 다른 구조적·수요측 변화(예: 개별 은행 전략, 시장 환경)와도 관련될 수 있어 인과관계 해석에 신중함 필요.
- 범위제한: 연구는 2010–2013년 시기와 선진국 대기업 표본에 기반하므로 다른 시기(예: GFC 직후 이외 시기)나 신흥시장으로의 외삽은 제한적임.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_857-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[글로벌 유동성]]
- [[산업생산]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work857.pdf](https://www.bis.org/publ/work857.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work857.htm](https://www.bis.org/publ/work857.htm)


## References

[1]: https://www.bis.org/publ/work857.pdf "BIS Working Paper 857: International bank lending and corporate debt structure"
