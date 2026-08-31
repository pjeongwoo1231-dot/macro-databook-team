---
title: "BIS WP 1188 — Finding a needle in a haystack: a machine learning framework for anomaly detection in payment systems"
type: primary_source
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 1188
published: "May 2024"
authors: "Ajit Desai , Anneke Kosse and Jacob Sharples"
source_kind: "working-paper"
peer_reviewed: false
primary_text_available: true
fulltext_verified: true
pages: 33
text_characters: 101399
sha256: "31ae87429745b7a8f2eb7da7045493c4418e6ad36ae5e97d08c5988a54fa936d"
catalog_filename: "BIS_WP_1188-catalog.md"
human_verified: false
catalog_method: "deterministic-keyword-index"
created: 2026-08-14
updated: 2026-08-14
archive_status: "official-fulltext-catalogued"
tags:
  - flag/partial-check
  - bis
  - working-paper
  - digital-finance-payments-and-cbdc
  - macro-modelling-forecasting-and-data
  - banking-and-financial-stability
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF에서 추출한 초록·서지·SHA-256. 원문 파일 미동봉이라 볼트에서 재대조 불가 — 초록 범위 밖 주장은 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: extracted-abstract
vault_tier: D
---

# BIS WP 1188 — Finding a needle in a haystack: a machine learning framework for anomaly detection in payment systems

> 이 파일은 공식 PDF 전문을 로컬 아카이브에 확보하고, 재현 가능한 키워드 규칙으로 색인한 **원문 카탈로그 노트**입니다. 분석적 요약 노트가 아니며, 저자의 주장·방법·한계를 인용하려면 원문 전문을 직접 확인해야 합니다.

| 항목 | 내용 |
|---|---|
| 저자 | Ajit Desai , Anneke Kosse and Jacob Sharples |
| 발행 | May 2024 |
| 공식 PDF | [전문](https://www.bis.org/publ/work1188.pdf) |
| 공식 랜딩페이지 | [페이지](https://www.bis.org/publ/work1188.htm) |
| 검증 | PDF 서명·페이지 수·텍스트 추출·SHA-256 확인 |
| 페이지·텍스트 | 33쪽 · 101,399자 |
| 자동 주제색인 | digital-finance-payments-and-cbdc, macro-modelling-forecasting-and-data, banking-and-financial-stability |
| 일치 점수 | digital-finance-payments-and-cbdc: 20, macro-modelling-forecasting-and-data: 16, banking-and-financial-stability: 13 |

## 원문 초록 또는 원문 선두 발췌

We propose a flexible machine learning (ML) framework for real-time transaction monitoring in high-value payment systems (HVPS), which are a central piece of a country’s financial infras- tructure. This framework can be used by system operators and overseers to detect anomalous transactions, which—if caused by a cyber attack or an operational outage and left undetected— could have serious implications for the HVPS, its participants and the financial system more broadly. Given the substantial volume of payments settled each day and the scarcity of actual anomalous transactions in HVPS, detecting anomalies resembles an attempt to find a needle in a haystack. Therefore, our framework uses a layered approach. In the first layer, a supervised ML algorithm is used to identify and separate ‘typical’ payments from ‘unusual’ payments. In the second layer, only the ‘unusual’ payments are run through an unsupervised ML algorithm for anomaly detection. We test this framework using artificially manipulated transactions and payments data from the Canadian HVPS. The ML algorithm employed in the first layer achieves a detection rate of 93%, marking a significant improvement over commonly-used econometric models. Moreover, the ML algorithm used in the second layer marks the artificially manipulated transactions as nearly twice as suspicious as the original transactions, proving its effectiveness.

## 연결

- 상위 색인: [[BIS-Fulltext-Topic-Index]]

## References

[1]: https://www.bis.org/publ/work1188.pdf "BIS Working Paper 1188: Finding a needle in a haystack: a machine learning framework for anomaly detection in payment systems"
