---
title: "BIS WP 884 — Retailer markup and exchange rate pass-through: Evidence from the Mexican CPI micro data"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 884
published: "September 2020"
authors: "Fernando Pérez-Cervantes"
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
  - "exchange-rate-pass-through"
  - "retailer-markups"
  - "cpi-microdata"
  - "retail-competition"
  - "mexico"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 884 — Retailer markup and exchange rate pass-through: Evidence from the Mexican CPI micro data

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

저자는 소매업체의 시장점유율이 마크업 수준과 유연성을 동시에 결정하여 환율의 소비자가격 반영률(ERPT)이 매장유형별로 달라지고, 매장유형 정보를 회귀에서 누락하면 ERPT가 편향(멕시코 사례에서 단기적 하향편향 약 340bp·6개월 기준)을 받는다고 이론·실증적으로 주장한다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 소매업체의 시장지배력(마켓쉐어)이 소매가격의 마크업 유연성과 환율전달(ERPT) 추정에 어떤 영향을 미치는가? |
| 방법 | 저자는 계층적(nested) CES 선호를 갖는 구조모형을 제시하여 소매업체별 최적 마크업의 폐쇄형 해를 도출하고, 멕시코 INEGI CPI 마이크로데이터(2009.06–2018.06)를 이용해 매장유형·소매업체 고정효과를 포함한 로그 가격변화 회귀로 ERPT 추정치의 편향을 실증적으로 검사한다. 식별을 위해 생산자·소매부가가치 입력가격을 외생으로 가정하고 선호(맛) 파라미터를 시간불변으로 가정한다. |
| 자료·범위 | INEGI CPI 마이크로데이터(2009.06–2018.06) 전체 관측 약 2,300만건; 월말 최종관찰만 사용 시 약 1,088만건; 본 논문은 거래가능(merchandise) 상품으로 표본 축소 후 약 792만건 사용. INEGI가 부여한 6개 매장유형(슈퍼마켓, 편의점, 공중시장·플라자, 백화점, 전문점, 프라이스클럽)과 46개 도시 수준. 자료상 점포 주소는 없어(점포명+도시로 동일 점포로 간주) 체인 판별은 저자 기준으로 수행. 0의 가격변화 관측치는 회귀에서 제외(조건부 pass-through). |
| 주제 | exchange rate pass-through, retailer markups, CPI microdata, retail competition, Mexico |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 이론: 소매업체의 점포유형 시장점유율(sτ`)·업체내점유율(srτ`)이 perceived elasticity를 결정하여 동일 점포 내 모든 상품에 대해 공통 마크업(상품별 동일)이 형성된다.
- 이론: 점유율이 클수록(=마크업이 높을수록) 마크업의 유연성이 커져 동일 비용충격(예: 환율변동)에 대한 가격 반응(백분율 변화)은 작아진다.
- 이론적 예측 1: 개별적으로 추정하면 시장점유율이 큰 점포일수록 측정된 ERPT가 낮다.
- 이론적 예측 2: 도시 내에서 무시할 수 있는(영(0) 측정) 시장점유율을 가진 점포들에 대해선 점포유형에 관계없이 동일한 ERPT가 관찰된다.
- 실증: 멕시코 CPI 마이크로데이터에서 동일 상품·동일 도시라도 매장유형별 가격수준과 가격변동성이 유의하게 다름(예: 편의점 가격변동성은 슈퍼마켓의 약 2배, 공중시장은 슈퍼마켓의 1.6배, 백화점은 0.9배).
- 실증: 매장유형 고정효과를 포함하면 ERPT 추정치가 커짐(6개월 변화 기준, 매장유형 통제 전후 차이 약 0.034 = 340bp), 즉 매장유형 미통합 시 ERPT가 하향편향됨.
- 실증: 체인으로 분류되지 않는(저자 기준) 점포들(무시가능 점유율)에 대해서는 매장유형 통제가 ERPT 추정에 거의 영향을 미치지 않음(모형예측과 일치).
- 실증: 기간을 길게(예: 14개월) 잡으면 장기적으로 ERPT가 수렴하여 점포유형 미통합 편향이 줄어드는 경향을 보임(단기에서는 편향 존재).
- 실증: 슈퍼마켓·백화점은 ERPT가 낮고, 공중시장·편의점·전문점은 ERPT가 높은 것으로 관찰됨; 체인 점포의 전달률이 비체인보다 낮게 나타남.

## 메커니즘과 연결고리

- 모형: 소비자는 매장유형→매장→상품의 3단계 nested CES 선택을 하며, 소매업체는 다종상품을 판매하는 단일공장(single-plant)으로 가정.
- 마크업 형성: 각 소매업체의 공통 마크업 M_rτ = ε_rτ/(ε_rτ − 1)이며 perceived elasticity ε_rτ는 매장유형 점유율(sτ`)과 소매업체 점유율(srτ`)에 의해 결정됨.
- 유연성 메커니즘: 점유율이 클수록 ε_rτ가 작아(=마크업이 큼) 동일한 비용충격에 대해 마크업을 조정(유연성)할 여지가 커짐 → 가격의 비용전달(패스스루)은 줄어듦.
- 측정편향 경로: 관측가능한 회귀에서 매장유형·소매업체 상대가격 변화를 통제하지 않으면 마크업 유연성(평균 0인 항)이 잠재적 누락변수로 작용하여 ERPT 추정치가 편향됨.
- 특수케이스: 모든 소매업체가 영(0) 점유율이면 마크업은 비유연(고정)이고 기존 문헌의 ERPT 추정식으로 귀결되어 편향이 사라짐.

## 한계와 적용 범위

- 식별 가정: 생산자 가격과 소매 부가가치 입력가격들을 소매자의 관점에서 외생(exogenous)으로 가정함(생산자측의 pricing-to-market 또는 전략적 대응을 모형화하지 않음).
- 선호 고정 가정: β(맛)과 CES 탄력 등 선호 파라미터를 시간불변으로 가정함; 이 가정이 깨지면 마크업·ERPT 식별에 영향이 있음.
- 자료 한계: INEGI 데이터에 점포 주소가 없어 점포 식별을 점포명+도시로 처리했음(동일명 다른 점포 혼동 가능성).
- 자료 한계: 생산자 가격·거래량(수량) 데이터가 CPI 마이크로데이터에 포함되지 않아 생산자-소매자 간 전략적 상호작용이나 수량 반응을 검증하지 못함.
- 샘플 처리: 가격 변화가 0인 관측치는 회귀에서 제외(조건부 pass-through 추정); 이로 인해 결과는 가격이 변경된 경우에 대한 조건부 효과임.
- 추정상의 근사: 소매부가가치 입력들의 가격을 관측가능한 지수(예: 환율, 전기요금, 임금 등)로 근사했으며 해당 지수의 측정오차가 존재할 수 있음.
- 외삽 제한: 실증 결과는 멕시코 2009.06–2018.06 기간·샘플(거래가능 상품, INEGI 표본설계) 범위에 해당하므로 다른 나라·기간으로 일반화할 때 주의 필요.
- 모형적 제한: 균형 일반균형 효과(예: 점포구조 변화가 생산자·수요에 미치는 피드백)와 생산자 측 전략(예: Stackelberg 설정)은 본문 모형에서 다루지 않음.
- 체인 분류: 체인 여부 판정은 저자 기준으로 수행되었으며 점유율 측정의 완전한 대체(예: 매출 기반 점유율)로 보증되지는 않음.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_884-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[CPI (소비자물가지수)]]
- [[원·달러 환율]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work884.pdf](https://www.bis.org/publ/work884.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work884.htm](https://www.bis.org/publ/work884.htm)


## References

[1]: https://www.bis.org/publ/work884.pdf "BIS Working Paper 884: Retailer markup and exchange rate pass-through: Evidence from the Mexican CPI micro data"
