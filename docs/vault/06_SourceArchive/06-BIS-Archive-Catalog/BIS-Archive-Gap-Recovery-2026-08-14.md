---
title: "BIS 아카이브 누락 보완 — 2026-08-14"
type: report
institution: "Bank for International Settlements"
created: 2026-08-14
updated: 2026-08-14
archive_status: "gap-recovered"
tags:
  - flag/partial-check
  - bis
  - provenance
  - collection-status
  - manual-recovery
status: working
verification: partial
reliability: institutional
verified: "△ 마누스가 공식 원문을 확보해 쓴 종합 서술. 각 주장에 원문 각주가 달려 있다 — 서술 인용 가능, 수치는 각주 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: cited-primary
vault_tier: E
---

# BIS 아카이브 누락 보완 — 2026-08-14

## 무엇이 틀렸나

원 패키지의 [[BIS-Archive-Collection-Status]]는 "Working Papers 레코드 536건 전수 대조,
535건 검증 통과, 1건 공식 철회, **미확인·대기 0건**"으로 보고했다. 실제 수집 범위를
번호로 나열해 보면 **WP 819–1371 구간**이며, 그 안에서 18개 번호가 비어 있었다.

문서화된 예외는 [[BIS-WP-1323-Withdrawn]] 하나뿐이었다. 나머지 **17건(820–835, 996)은
사유 기록 없이 누락**돼 있었고, 확인 결과 전부 bis.org에 공개 PDF가 정상적으로 존재했다.

즉 536이라는 분모는 BIS Working Papers 시리즈의 실제 모집단이 아니라 **수집 스크립트가
확보한 레코드 수**였고, 그 위에서 "전수 완료"가 선언됐다. 수집 실패가 침묵으로 처리되면
카탈로그의 빈칸은 "그런 논문이 없다"로 잘못 읽힌다. 이 노트는 그 빈칸을 메운 기록이다.

## 남은 범위 한계

이 보완은 819–1371 구간의 구멍만 메운다. BIS Working Papers 시리즈는 1979년 1호부터
발행되므로 **819 이전 800편 가까이는 여전히 이 라이브러리 밖에 있다.** 라이브러리를
"BIS 전수"로 부르지 말고 "BIS WP 819–1371 구간"으로 부르는 편이 정확하다.

## 보완한 17건

| 노트 | 제목 | 발행 | 분량 | 상태 |
|---|---|---|---|---|
| [[BIS_WP_820-catalog]] | Policy Uncertainty and Bank Mortgage Credit | October 2019 | 50쪽 | 확보·해시 완료 |
| [[BIS_WP_821-catalog]] | What do almost 20 years of micro data and two crisis say about the relationship between central bank and interbank market liquidity? Evidence from Italy | November 2019 | 59쪽 | 확보·해시 완료 |
| [[BIS_WP_822-catalog]] | China's Shadow Banking: Bank's Shadow and Traditional Shadow Banking | November 2019 | 47쪽 | 확보·해시 완료 |
| [[BIS_WP_823-catalog]] | Unintended Side Effects: Stress Tests, Entrepreneurship, and Innovation | November 2019 | 55쪽 | 확보·해시 완료 |
| [[BIS_WP_824-catalog]] | Spread the Word: International Spillovers from Central Bank Communication | December 2019 | 55쪽 | 확보·해시 완료 |
| [[BIS_WP_825-catalog]] | Examining macroprudential policy and its macroeconomic effects � some new evidence | December 2019 | 37쪽 | 확보·해시 완료 |
| [[BIS_WP_826-catalog]] | The Cost of Clearing Fragmentation | December 2019 | 47쪽 | 확보·해시 완료 |
| [[BIS_WP_827-catalog]] | Bank Loan Supply during Crises: The Importance of Geographic Diversification | December 2019 | 71쪽 | 확보·해시 완료 |
| [[BIS_WP_828-catalog]] | The currency composition of foreign exchange reserves | December 2019 | 38쪽 | 확보·해시 완료 |
| [[BIS_WP_829-catalog]] | Central banking in challenging times | December 2019 | 29쪽 | 확보·해시 완료 |
| [[BIS_WP_830-catalog]] | De jure benchmark bonds | December 2019 | 29쪽 | 확보·해시 완료 |
| [[BIS_WP_831-catalog]] | Believing in bail-in? Market discipline and the pricing of bail-in bonds | December 2019 | 36쪽 | 확보·해시 완료 |
| [[BIS_WP_832-catalog]] | Hedger of Last Resort: Evidence from Brazilian FX Interventions, Local Credit and Global Financial Cycles | December 2019 | 50쪽 | 확보·해시 완료 |
| [[BIS_WP_833-catalog]] | Central Counterparty Exposure in Stressed Markets | December 2019 | 51쪽 | 확보·해시 완료 |
| [[BIS_WP_834-catalog]] | How do machine learning and non-traditional data affect credit scoring? New evidence from a Chinese fintech firm | December 2019 | 24쪽 | 확보·해시 완료 |
| [[BIS_WP_835-catalog]] | The Cost of Steering in Financial Markets: Evidence from the Mortgage Market | December 2019 | 71쪽 | 확보·해시 완료 |
| [[BIS_WP_996-catalog]] | Monetary policy expectation errors | January 2022 | 83쪽 | 확보·해시 완료 |

원문 PDF는 `06-BIS-Archive-Catalog/PDFs/`에 실제로 보관했고 각 노트에 SHA-256을 기록했다.
원 패키지의 535건은 해시만 있고 PDF가 동봉되지 않아 대조 검증이 불가능하다는 점과 구분된다.

## 이 17건의 해석 상태

전부 `human_verified: false`, `catalog_method: "manual-recovery-2026-08-14"`다.
원 패키지의 결정론적 키워드 주제색인은 규칙을 재현할 수 없어 부여하지 않았다.
따라서 [[BIS-Fulltext-Topic-Index]]의 주제별 목록에는 나타나지 않으며, 별도 섹션에서만
접근된다. 주제색인이 필요하면 원 규칙을 확보한 뒤 일괄 재생성해야 한다.

## References

[1]: https://www.bis.org/publ/work825.pdf "BIS Working Paper 825"
[2]: https://www.bis.org/publ/work996.pdf "BIS Working Paper 996"
[3]: https://www.bis.org/list/research/index.htm "Bank for International Settlements, Research and publications"
