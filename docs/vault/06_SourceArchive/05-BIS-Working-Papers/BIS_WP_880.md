---
title: "BIS WP 880 — Rise of the central bank digital currencies: drivers, approaches and technologies"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 880
published: "August 2020"
authors: "Raphael Auer , Giulio Cornelli and Jon Frost"
source_kind: "working-paper"
peer_reviewed: false
primary_text_read: true  # 추출 전문 기준. 사람 대조 아님
human_verified: false
analysis_model: "gpt-5-mini"
analysis_confidence: "not-calibrated"
relevance_score: 2
created: 2026-08-14
updated: 2026-08-14
archive_status: "llm-structured-unverified"
tags:
  - flag/partial-check
  - bis
  - working-paper
  - "central-bank-digital-currency"
  - "retail-cbdc"
  - "wholesale-cbdc"
  - "distributed-ledger-technology"
  - "payment-system-design"
  - "cross-country-drivers"
  - "policy-approaches"
  - "financial-inclusion"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 880 — Rise of the central bank digital currencies: drivers, approaches and technologies

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

본 논문은 공개 중앙은행 자료를 기반으로 구축한 CBDC 프로젝트 지수를 통해 175개 관측치의 횡단면 분석을 수행하여, CBDC 연구·개발은 디지털화(모바일 보급)와 국가의 혁신능력과 양(+)의 상관관계를 가지며 소매·도매 목적에 따라 다른 경제구조(비공식경제·금융발달)에 연관된다는 점을 제시함. 다만 분석은 공개발표 기반·횡단면 상관분석이라는 한계로 인과 추론·비공개 활동 포착에는 제약이 있고 파일럿상의 기술선택이 최종 설계를 예단하지 못함을 명확히 해야 함.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 어떤 경제·제도적 요인이 각국의 CBDC 연구·개발을 촉진하는가? 중앙은행들이 채택한 정책적 접근과 기술 설계는 어떠하며, 국가별 차이는 어떤 요인과 연관되는가? |
| 방법 | 저자들은 중앙은행의 공개 보고·연설을 바탕으로 175개국(또는 통화권) 대상의 CBDC 프로젝트 지수(CBDCPI)와 연관 지표(연설 태도 점수, 구글/바이두 검색지수)를 구성하고, 횡단면 ordered probit·probit 회귀로 전체·소매·도매 CBDC 및 설계 속성(아키텍처, 인프라, 접근 방식)과 국가지표의 상관관계를 분석하며 중국·스웨덴·캐나다 사례를 심층 기술함. |
| 자료·범위 | 주요 원천은 중앙은행 보고서·연설, BIS 연설 데이터베이스, Google Trends(및 중국의 Baidu), WIPO·World Bank 등 공개지표임. 종속변수는 0(무)·1(연구)·2(파일럿)·3(실사용) 범주의 CBDC 프로젝트 지수(소매·도매 및 전체)이며 표본은 2013–2019 평균(검색지수는 2013–2020) 기반으로 175관측치를 사용. 공개 발표된 중앙은행 자료만 반영하고, 누락치는 제로로 대체함. |
| 주제 | central bank digital currency, retail CBDC, wholesale CBDC, distributed ledger technology, payment system design, cross-country drivers, policy approaches, financial inclusion |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장: CBDC 연구·개발(전체 지수)은 휴대전화 보급률(디지털 인프라)과 국가의 혁신역량(예: WIPO 지표)과 유의하게 양(+)의 관계를 보임.
- 저자 주장: 소매(일반 목적) CBDC 연구는 비공식(비공개·비공식 경제) 규모가 큰 국가일수록 더 진전된 경향을 보이며, 이는 거래 기록·포용성 관련 동기와 연관될 수 있음.
- 저자 주장: 도매 CBDC는 금융발달 수준이 높은 경제에서 더 진전되어 있으며, 이는 도매 결제 효율성 수요와 부합함.
- 저자 주장: 기술·설계 측면에서 다수 중앙은행은 중앙은행에 대한 직접(현금성) 청구권을 유지하되 고객접점 서비스는 민간 중개기관이 담당하는 '하이브리드/중개' 형태를 선호하거나 검토 중임. 간접(합성) 모델은 중앙은행 보고서에서 지지받지 못함.
- 저자 주장: 초기 실증·프로토타입은 DLT 기반이 많은 편이지만, 중앙은행 보고서상 대부분은 허가형 DLT를 실험 대상으로 삼고 있으며 권한 없는(permissionless) DLT는 고려 대상이 아님.
- 저자 주장: 접근방식은 계정기반이 우세하고, 완전한 무기명(현금 수준의 익명성)을 허용하는 토큰형 접근은 소수만 검토 중임.
- 저자 주장: 사례연구에서 중국(DC/EP)은 하이브리드·준계정형·혼합 인프라를, 스웨덴(e-krona)과 캐나다는 계정기반·하이브리드형(캐나다는 발행시점에 '비상계획' 강조)을 중심으로 상이한 설계를 추구함.

## 메커니즘과 연결고리

- 디지털 인프라(모바일 보급)는 중앙은행이 기술적 실험과 프로토타입을 수행할 물리적·운용적 기반을 제공하여 CBDC 프로젝트 추진을 용이하게 함.
- 혁신역량(국가·제도)은 기술시험·시스템 설계 역량과 민간 협업 가능성을 높여 CBDC 연구·개발 진전을 촉진함.
- 비공식경제 규모가 큰 국가는 거래기록 확보·탈세·범죄방지 목적 등으로 소매 CBDC 도입 동기를 가질 가능성이 있음(다만 상관관계일 뿐 확정적 인과는 아님).
- 금융발달이 높은 국가는 금융기관 간 대량결제 효율화 수요로 도매 CBDC 연구가 진전될 가능성이 큼.
- 국가별 제도·정책 우선순위(예: 현금 감소, 민간 결제망 독점, AML/CFT 규제)는 아키텍처·접근(계정·토큰)·인프라 선택에 영향을 줌.

## 한계와 적용 범위

- 저자 표명·암시 제한: CBDCPI는 공개적으로 발표된 중앙은행 R&D·파일럿만 포함하므로 비공개 프로젝트나 비중앙은행 주도의 민간 시도는 포착하지 못함.
- 지표 구성상의 제약: 일부 변수(예: 혁신지표, 비공식경제 규모, 계정 보유율)는 관측치가 제한적이며, 누락치는 0으로 대체되어 편향을 초래할 수 있음.
- 식별·해석상의 한계: 횡단면 상관관계 분석(ordered probit)은 인과관계 규명 대신 연관성 제시로 한정되며, 설명변수들 간 다중공선성(예: 디지털화·소득·정부효율성)이 존재해 개별 요인의 순수한 효과 분리에 제약이 있음.
- 기간·언어 제약: 중국 등 일부 국가의 자료는 영어 번역이 제한적이어서 저자들이 보충정보를 사용했으나 여전히 정보비대칭 가능성이 있음.
- 설계·파일럿 해석 주의: 프로토타입·파일럿에서의 기술선택(DLT 등)은 확정된 대규모 운영 설계와 다를 수 있으며, 파일럿 성과가 곧 최종 채택으로 연결된다는 보장은 없음.
- 정책의존성: 중앙은행 연설 태도·검색지수는 공표·관심의 표지일 뿐 내부 의사결정·정책우선순위를 완전 대변하지 못할 수 있음.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_880-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[설비가동률]]
- [[AI 자본지출]]
- [[CPI (소비자물가지수)]]
- [[산업생산]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work880.pdf](https://www.bis.org/publ/work880.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work880.htm](https://www.bis.org/publ/work880.htm)


## References

[1]: https://www.bis.org/publ/work880.pdf "BIS Working Paper 880: Rise of the central bank digital currencies: drivers, approaches and technologies"
