---
title: "출처 선택과 원문 열람 로그"
type: report
created: 2026-08-13
updated: 2026-08-13
archive_status: "verified-primary-source"
tags:
  - flag/partial-check
  - research-method
  - provenance
  - primary-source
status: working
verification: partial
reliability: institutional
verified: "△ 마누스가 공식 원문을 확보해 쓴 종합 서술. 각 주장에 원문 각주가 달려 있다 — 서술 인용 가능, 수치는 각주 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: cited-primary
vault_tier: E
---

# 출처 선택과 원문 열람 로그

## 목적

이 파일은 이 노트 묶음의 주장 범위를 통제한다. 모든 노트가 ‘직접 읽은 공식 무료 원문’에 근거한다는 기준을 재현 가능하게 남기고, 읽지 못했거나 원문이 확보되지 않은 자료가 사실 근거로 섞이는 것을 막는다.

## 포함 기준

| 기준 | 적용 방식 |
|---|---|
| 공식성 | BIS·IMF·NBER가 직접 공개한 URL 또는 사용자 제공 BIS 공식 PDF를 사용했다 |
| 무료 전문 | HTML 전문 또는 PDF 전문을 실제로 열람하고 텍스트를 확인한 문헌만 포함했다 |
| 주제 적합성 | 글로벌 금융위기, 코로나 충격, 코로나 이후 인플레이션·정상화, 국제 통화파급, 금융시장 인프라 중 적어도 하나와 직접 연결되는 문헌을 선택했다 |
| 문헌 위상 표시 | 기관 보고서와 Working Paper를 구분했다. Working Paper는 동료심사 전이라는 원문 표기를 보존했다 |
| 한계 기록 | 표본·국가·기간·식별·모형의 한계를 문헌 노트와 사건·메커니즘 노트에 명시했다 |

## 직접 열람한 원문 목록

| 파일 | 기관·발행일 | 원문 전문 | 주된 역할 |
|---|---|---|---|
| [[BIS-2009-79th-Annual-Report]] | BIS, 2009-06 | [PDF](https://www.bis.org/publ/arpdf/ar2009e.pdf) | 금융위기의 축적·증폭·정책전파 |
| [[BIS-2020-Annual-Economic-Report]] | BIS, 2020-06-30 | [HTML](https://www.bis.org/publ/arpdf/ar2020e1.htm) | 코로나 서든스톱과 금융증폭 |
| [[BIS-2022-Annual-Economic-Report]] | BIS, 2022-06-26 | [HTML](https://www.bis.org/publ/arpdf/ar2022e1.htm) | 인플레이션·정상화·금융취약성 |
| [[BIS-WP-866-CCP-Model-Risk]] | BIS, 2020-05 | [PDF](https://www.bis.org/publ/work866.pdf) | CCP 모형위험과 손실분담 유인 |
| [[BIS-WP-870-Forward-Guidance-Spillovers]] | BIS, 2020-07 | [PDF](https://www.bis.org/publ/work870.pdf) | 포워드가이던스의 국제 파급 |
| [[IMF-WEO-2020-Great-Lockdown]] | IMF, 2020-10 | [PDF](https://www.imf.org/-/media/files/publications/weo/2020/october/english/text.pdf) | 봉쇄·자발적 거리두기·분배 |
| [[NBER-W27141-Cost-of-Covid-Crisis]] | NBER, 2020-05 | [PDF](https://www.nber.org/system/files/working_papers/w27141/w27141.pdf) | 가계 소비·고용·기대 |
| [[NBER-W32859-Drivers-of-Post-Pandemic-Inflation]] | NBER, 2024-08 | [PDF](https://www.nber.org/system/files/working_papers/w32859/w32859.pdf) | 사후 인플레이션의 수요·공급 분해 |
| [[BOJ-WP-11E06-Asian-Financial-Linkage]] | BOJ, 2011-08 | [PDF](https://www.boj.or.jp/en/research/wps_rev/wps_2011/data/wp11e06.pdf) | 아시아 금융시장·실물경제의 파급 중심 |
| [[WorldBank-GEP-June-2026]] | World Bank, 2026-06 | [PDF](https://thedocs.worldbank.org/en/doc/2b672b3b0415d6b66c45b66579db4ef5-0050012026/original/GEP-Jun-2026.pdf) | 지정학적 에너지 충격·EMDE 부채·금리·성장 |

## 사용자 제공 BIS 아카이브의 처리

사용자가 제공한 `QUALITY-CHECK.json`과 `수집결과보고.md`는 BIS Working Papers 536건 중 원문 PDF·텍스트가 확보된 것이 4건이고, 원문 미확보가 532건이라고 기록한다. 이 묶음에서는 원문이 확보된 `BIS_WP_866.pdf`, `BIS_WP_870.pdf`만 직접 읽고 사용했다. 원문이 확보되지 않은 532건은 공식 URL이 있어도 본문·표·한계를 추정할 수 없으므로 포함하지 않았다.

| 처리 | 문서 수 | 이 묶음에서의 사용 |
|---|---:|---|
| 공식 PDF와 텍스트가 확보됨 | 4 | 주제 적합성과 원문 열람을 확인한 2건을 포함 |
| 공식 URL만 보존되고 원문 미확보 | 532 | 제외 |
| 중복 판정 | 0 | 별도 병합 불필요 |

## 추가 자료 처리 기록

사용자 제공 BIS 추출 아카이브에는 WP 838, 849, 866, 870의 PDF·텍스트가 확보되어 있다. 기존 패키지에는 주제 적합성이 높은 WP 866과 WP 870을 포함했고, WP 838과 WP 849는 각각 fintech adoption과 green-bond reserve management를 다루므로 현재의 금융위기·국제 파급 코어와 직접 중복되지 않아 후보 보류로 둔다. NBER 목록은 후보 탐색용으로 사용하되, 원문 전문을 직접 읽고 연구설계·robustness·후속 연구를 확인한 뒤에만 편입한다.

BIS Annual Economic Report 2026은 공식 페이지와 133쪽 PDF, 장별 주제는 확인했으나 전체 본문 분석 전까지는 검증 진행 중으로 둔다. 공식 페이지는 fiscal–financial stability nexus, 고공공부채와 변화하는 금융시장, 비은행금융, 인플레이션 동학, 디지털 금융과 화폐 신뢰를 핵심 축으로 제시한다.

## 2022~2023년 핵심 원문 추가

| 파일 | 기관·발행일 | 원문 전문 | 주된 역할 |
|---|---|---|---|
| [[2022-2023-Core-Source-Summary]] | BIS·BOJ·Fed·IMF·NBER·World Bank, 2022–2023 | [통합 요약 노트](../03-Sources/2022-2023-Core-Source-Summary.md) 및 각 공식 PDF/HTML | 인플레이션·긴축·자본흐름·국제 파급·금융안정 |
| BIS Annual Economic Report 2023 | BIS, 2023-06 | [PDF](https://www.bis.org/publ/arpdf/ar2023e.pdf) | 디스인플레이션·은행 스트레스·재정·통화정책 |
| BIS WP 1032 | BIS, 2022-07 | [PDF](https://www.bis.org/publ/work1032.pdf) | EME 자본흐름·서든스톱·통화정책 상충 |
| BIS WP 1069 | BIS, 2023-01 | [PDF](https://www.bis.org/publ/work1069.pdf) | 글로벌 금융사이클·외환유동성 완충 |
| BIS WP 1090 | BIS, 2023-04 | [PDF](https://www.bis.org/publ/work1090.pdf) | 재정정책–금융안정 연계 |
| BOJ Central Bank Finances and Monetary Policy Conduct | BOJ, 2023-12 | [PDF](https://www.boj.or.jp/en/research/brp/ron_2023/data/ron231212a.pdf) | 중앙은행 대차대조표·손익·통화 신뢰 |
| Fed FEDS Note, U.S. Interest Rates and Emerging Market Currencies | Fed, 2023-10 | [HTML](https://www.federalreserve.gov/econres/notes/feds-notes/u-s-interest-rates-and-emerging-market-currencies-taking-stock-10-years-after-the-taper-tantrum-20231004.html) | 미국 금리·위험프리미엄·EME 통화 |
| IMF GFSR 2023 Chapter 1 | IMF, 2023-10 | [PDF](https://www.imf.org/-/media/files/publications/gfsr/2023/october/english/ch1.pdf) | 긴축 장기화·자산 재가격·은행·부동산 |
| IMF WP/23/107 | IMF, 2023-05 | [PDF](https://www.imf.org/-/media/files/publications/wp/2023/english/wpiea2023107-print-pdf.pdf) | 미국 뉴스·통화정책의 EM 파급 |
| NBER WP 31263 | NBER, 2023-05 | [PDF](https://www.nber.org/system/files/working_papers/w31263/w31263.pdf) | 유가·통화정책·인플레이션 급등 |
| NBER WP 31520 | NBER, 2023-08 | [PDF](https://www.nber.org/system/files/working_papers/w31520/w31520.pdf) | Fed 정책체계·인플레이션 대응 |
| World Bank GEP June 2023 | World Bank, 2023-06 | [PDF](https://openknowledge.worldbank.org/bitstreams/2106db86-a217-4f8f-81f2-7397feb83c1f/download) | 세계성장·긴축·은행 스트레스·EMDE |

## 확장 수집본 추가 검증

이번 확장분에서는 BIS WP 1043·1047·1050, BOJ 22-E-14·22-E-15·23-E-13, NBER WP 30751·30887을 공식 원문 PDF로 확보하고 초록·서론·핵심 결과를 직접 확인했다. 이 8건을 기존 11건에 추가해 직접 원문을 확보·열람한 자료는 총 21건이다. BOJ 22-E-13은 응답 파일이 비정상적으로 작아 보류했고, 서버 지연으로 확보하지 못한 후보는 읽은 자료로 집계하지 않았다.

| 추가 문헌 | 연도 | 검증 상태 | 연결 주제 |
|---|---:|---|---|
| BIS WP 1043 | 2022 | PDF 확보·직접 열람 | 경기수축 장기 상흔 |
| BIS WP 1047 | 2022 | PDF 확보·직접 열람 | 수요·공급 인플레이션 |
| BIS WP 1050 | 2022 | PDF 확보·직접 열람 | 고령화·은행 위험선택 |
| BOJ 22-E-14 | 2022 | PDF 확보·직접 열람 | NBFI·fire sale·국제 전염 |
| BOJ 22-E-15 | 2022 | PDF 확보·직접 열람 | 지역은행·글로벌 펀드 중복 |
| BOJ 23-E-13 | 2023 | PDF 확보·직접 열람 | 생산단계 비용압력·물가 전가 |
| NBER WP 30751 | 2022 | PDF·NBER 원문 페이지 확인 | 금융시장 심리·통화정책 상충 |
| NBER WP 30887 | 2023 | PDF 확보·직접 열람 | 국제 자본흐름 압력·글로벌 요인 |

| IMF GFSR April 2023 | 2023 | 공식 HTML 보고서 페이지 직접 열람 | 은행불안·NBFI·금융분절 |
| IMF WEO October 2022 | 2022 | 공식 HTML 보고서 페이지 직접 열람 | 세계성장·인플레이션·정책조합 |

## 해석 규칙

기관 보고서는 발행 시점의 세계경제·정책 진단이다. 따라서 미래 예측의 적중 여부와 무관하게 ‘당시 어떤 위험을 어떻게 프레이밍했는지’를 이해하는 데 사용한다. Working Paper는 저자들의 연구질문·자료·식별·추정 결과를 담지만, 동료심사나 후속 개정의 가능성을 별도로 둔다. 두 유형을 섞어 ‘확정된 사실’처럼 서술하지 않는다.

각 외부 사실에는 원문 URL을 참조 링크로 둔다. 원문에 없는 수치, 최신 시장자료, 국가별 정책평가, 개인화된 투자 판단은 이 패키지에 추가하지 않았다.

- 원 수집 계획서: [[2022-2023-source-plan]]

## 2024~2026년 확장 수집본

2024~2026년 자료 중 PDF 또는 공식 HTML 원문을 확보하고 핵심 본문을 직접 확인한 자료는 9건이다. 기관 보고서와 연구논문을 구분했으며, 제목·검색 결과만 확인한 자료는 집계하지 않았다.

| 문헌 | 연도 | 검증 상태 | 핵심 주제 |
|---|---:|---|---|
| BIS Annual Economic Report 2025 | 2025 | 공식 PDF 확보·직접 열람 | 무역 불확실성·FX swap·NBFI |
| BOJ Review 2026-E-4 | 2026 | 공식 PDF 확보·직접 열람 | 자연이자율·금융조건 |
| BOJ WP 25-E-06 | 2025 | 공식 PDF 확보·초록·서론 직접 열람 | 인플레이션 기대 |
| Fed FEDS Note | 2025 | 공식 HTML 확보·본문 직접 열람 | 인플레이션 불확실성 전파 |
| IMF GFSR April 2026 | 2026 | 공식 PDF·페이지 직접 열람 | 국채·NBFI·신흥국 위험 |
| IMF GFSR April 2026 Chapter 2 | 2026 | 공식 PDF·장별 요약 직접 열람 | NBFI·EM 자본흐름 |
| NBER WP 32810 | 2024 | NBER 페이지·PDF·초록 직접 열람 | 외환보유액·세계금리·레버리지 |
| OECD Economic Outlook 2025 Issue 2 | 2025 | 공식 HTML 페이지 직접 열람 | 관세·AI·NBFI·재정 |
| World Bank GEP January 2026 | 2026 | 공식 PDF·집행요약 직접 열람 | EMDE·재정준칙·프런티어시장 |

직접 검증하지 않은 2024~2026년 후보는 읽은 자료로 세지 않았으며, 이후 추가 수집 시에도 같은 기준을 적용한다.

## 2024~2026년 2차 확장 검증

추가 배치에서 BIS WP 1285, BOJ WP 26-E-05·26-E-06·26-E-09, BOJ Review 26-E-09, World Bank GEP June 2025 Chapter 1, NBER WP 33885, IMF WP 25/212·25/96·25/66·25/79, Fed FEDS 2025-074·2025-037·2025-023의 공식 PDF를 확보하고 초록·집행요약·핵심 결과를 직접 확인했다. 기존 9건에 14건을 더해 2024~2026년 직접 확보·열람 집계는 **23건**이다. 제목과 검색 결과만 확인한 후보는 집계하지 않았다.

이번 배치의 핵심 축은 동아시아 r-star와 정책 파급, 일본 시장참가자의 정책인식, 비은행으로의 신용이동, 비전통적 통화정책의 재정효과, 고인플레이션의 경로의존성, 글로벌 공급충격과 IT 체계, 통화정책 불확실성과 커뮤니케이션이다.

## 2024~2026년 3차 확장 검증

추가로 Federal Reserve Monetary Policy Report March 2024, BOJ-IMES Conference Summary 2024, BIS Annual Economic Report 2026의 공식 PDF를 확보하고 핵심 요약·목차·정책 논점을 직접 확인했다. 이에 따라 2024~2026년 직접 확보·열람 원문은 **총 26건**이 되었다. IMF 2024 Working Paper 196은 공식 URL이 404로 확인되어 이번 집계에 포함하지 않았다.

## 2024~2026년 4차 확장 검증

Fed FEDS 2026-005r1, IMF WP 25/202, IMF WP 25/175의 공식 PDF를 확보하고 초록·서론·핵심 분석 범위를 직접 확인했다. 이에 따라 2024~2026년 직접 확보·열람 원문은 **총 29건**이다. 이번 배치의 핵심은 미국 LSAP의 유로지역 은행자본 전파, 신흥국 국내채무 재조정, 스리랑카 국가채무 구조조정이다.

### 볼트 측 정정 (2026-08-14)

위 4개 배치의 집계는 **29건**이지만, [[2024-2026-Core-Source-Summary]]가 실제로 다루는
문헌은 **34건**이고 각주도 34개다. 로그 표에 빠진 5건은 OECD Economic Outlook
Interim Report(2024-09 · 2025-09 · 2026-03), OECD Economic Outlook Volume 2024 Issue 1,
World Bank GEP January 2025다. 이 중 OECD 4건은 PDF가 볼트에 있다.

과대집계가 아니라 **과소집계**라 인용 안전성에는 문제가 없지만, 로그가 수집의 기록인 이상
요약 노트와 어긋나면 안 된다. 다음 납품에서 맞출 것 — `MANUS-REQUEST.md` 2번 항목.

<!-- 2026-08-15 증분: 마누스 패치본에서 2016~2018 절만 추려 덧붙임. 기존 내용 불변 -->

## 2016~2018년 증분 원문 검증

2016~2018년 구간에는 기존 기준본이 없어 신규 증분으로 BIS Annual Economic Report 2016·2017·2018 세 건을 추가했다. 세 PDF의 공식 원문, 표지·연도·목차와 금융안정·통화정책·부채·은행–비은행 관련 장을 직접 확인했다. 이 세 자료는 코로나19 충격의 원인을 분석하는 연구가 아니라, 2020년 sudden stop 이전의 저금리·부채·금융사이클·정상화·거시건전성 취약성의 기준선을 제공하는 기관 보고서로 분류한다.

검증 상태: `verified-primary-source` 3건, `official-page-only` 0건, `candidate-not-read` 0건.

> **볼트 추가 검증**: 위 세 PDF를 볼트에서 `pdftotext`로 직접 판독해 대조했다(2026-08-15).
> 장 제목·핵심 개념·인용문이 모두 일치했다 — [[BIS-AER-2016]] · [[BIS-AER-2017]] · [[BIS-AER-2018]].
> 이 세 건은 볼트에서 `verification: full` / `text_basis: local-pdf`다.

<!-- 2026-08-15 증분: 미국 국채금리 1차·2차 확장 검증 기록 추가 -->

## 미국 국채금리 심층 원문 검증 — 2026-08-15 기준

2026년 8월 15일을 기준으로 미국 국채금리·term premium·재정·발행·repo·NBFI·시장기능을 다루는 원문을 별도 주제 세트로 재수집했다. **공식 PDF 또는 완전한 공식 HTML을 확보하고**, 초록·집행요약·관련 방법·결과·정책 단락을 직접 확인한 원문은 **16건**이다.

이 16건 중 BIS *Annual Economic Report 2026, Chapter II*와 IMF *Global Financial Stability Report, April 2026*은 기존 2024~2026 핵심 세트에 이미 포함되어 있다. 따라서 기존 33건에 중복 없이 **14건을 추가**하며, 2024~2026년 직접 검증 원문 집계는 **47건**이 된다. 이 별도 주제 세트의 16건은 `[[US-Treasury-Yields-2026-Core-Source-Summary]]`와 `[[US-Treasury-Yields-2026-Mechanism-Map]]`에서 원문별 역할과 한계를 확인한다.

| 기관 | 문헌 | 연도 | 형식 | 검증 상태 | 직접 확인한 핵심 범위 |
|---|---|---:|---|---|---|
| BIS | Annual Economic Report 2026, Chapter II: High public debt and shifting financial markets: challenges for central banks | 2026 | PDF/HTML | 기존 33건에 포함·재검토 | fiscal–financial nexus, sovereign yields, NBFI, repo |
| BIS | Stablecoins and safe asset prices, Working Papers No 1270 | 2025/2026 revised | PDF/HTML | 신규 verified-primary-source | short-term Treasury bill yields, 식별·결과·한계 |
| CBO | The Budget and Economic Outlook: 2026 to 2036 | 2026 | 공식 HTML | 신규 verified-primary-source | debt, deficit, interest rate baseline, 가정 |
| Federal Reserve Board | Decomposing Hedge Funds’ U.S. Treasury Exposures | 2026 | 공식 HTML | 신규 verified-primary-source | Form PF 분해, basis/swap-spread/repo, 측정한계 |
| Federal Reserve Board | Financial Stability Report – May 2026, Chapter 3 | 2026 | PDF/HTML | 신규 verified-primary-source | hedge-fund leverage, dealer intermediation, bank rate risk |
| Federal Reserve Board | FOMC Minutes, June 16–17, 2026 | 2026 | 공식 HTML | 신규 verified-primary-source | Treasury yield movement, ownership composition, term-premium 논평 |
| Federal Reserve Board | H.15 Selected Interest Rates (Daily), August 14, 2026 | 2026 | 공식 HTML | 신규 verified-primary-source | 2026-08-13 Treasury constant-maturity·TIPS 수익률 |
| Federal Reserve Board | Monetary Policy Report – July 2026 | 2026 | PDF/HTML | 신규 verified-primary-source | 연초 이후 금리 변동, inflation compensation |
| Federal Reserve Board | The Cross-Border Trail of the Treasury Basis Trade | 2025 | 공식 HTML | 신규 verified-primary-source | Cayman hedge funds, TIC 측정한계, repo |
| Federal Reserve Board | Why have far-forward nominal Treasury rates increased so much in the past few years? Old risks reemerge in an era of Fed credibility | 2026 | 공식 HTML | 신규 verified-primary-source | far-forward decomposition, supply/fiscal risk 해석 |
| Federal Reserve Bank of New York | Treasury Term Premia (ACM estimates) | 수시 갱신 | 공식 HTML | 신규 verified-primary-source | 5요인 무차익 term-premium 방법론 |
| Financial Stability Board | Leverage in Nonbank Financial Intermediation: Final report | 2025 | PDF/HTML | 신규 verified-primary-source | core-market NBFI leverage, data, cross-border policy |
| IMF | Global Financial Stability Report, April 2026 | 2026 | PDF/HTML | 기존 33건에 포함·재검토 | core sovereign rollover, NBFI deleveraging, sovereign–bank nexus |
| NBER | Treasury Supply Shocks: Propagation Through Debt Expansion and Maturity Adjustment, Working Paper 35098 | 2026 | PDF/공식 페이지 | 신규 verified-primary-source | high-frequency auction identification, debt/maturity shocks |
| U.S. Treasury / TBAC | Minutes of the Meeting of the Treasury Borrowing Advisory Committee August 4, 2026 | 2026 | 공식 HTML | 신규 verified-primary-source | issuance, SOMA, repo, transparency, intraday repo |
| U.S. Treasury / TBAC | Treasury Presentation to TBAC, Fiscal Year 2026 Q3 Report | 2026 | PDF | 신규 verified-primary-source | borrowing outlook, auction composition, demand, scenario limits |

보존 검증: 15개 원문 파일(PDF 8건, HTML 7건)은 `05-Primary-PDFs/US-Treasury-Yields-2026/`에 저장했다. PDF는 MIME 형식·페이지 수·텍스트 추출을 검사했고, HTML은 문서구조를 확인했다. CBO 보고서는 공식 완전 HTML을 직접 열람했지만 자동 다운로드가 403으로 차단되어 로컬 파일 목록에서는 제외했다. 이는 `official-page-only`이 아니라 **공식 전문 직접 열람 완료·보존 경로 제한**으로 기록한다.

## 미국 국채금리 심층 원문 2차 확장 — 2026-08-15 기준

기존 미국 국채금리 심층 세트의 `verified-primary-source` 16건에 **22건**을 추가로 직접 검토했다. 이에 따라 해당 주제 묶음은 총 **38건**의 `verified-primary-source`로 구성된다. 이번 확장은 2020년 3월 dash for cash, 2021년 hedged-fund Treasury·repo 노출, 2023년 dealer capacity·중앙청산 논의, 2024년 시장깊이·basis-trade 측정·IAWG Staff Progress Report, 2025년 관세 충격·부채의 장기금리 효과, 2026년 term funding premium·repo·중앙청산 이행·투자자기반까지의 시계열을 보강한다.

| 구분 | 건수 | 검증 상태 | 비고 |
|---|---:|---|---|
| 기존 미국 국채금리 심층 세트 | 16 | `verified-primary-source` | 기존 2024~2026 핵심 세트와 2건 중복을 별도 관리 |
| 이번 2차 확장 | 22 | `verified-primary-source` | 기존 주제 세트와 중복 없이 새로 검토한 공식 원문 |
| 미국 국채금리 주제 묶음 합계 | **38** | `verified-primary-source` | 연도별 전체 라이브러리 집계와는 별도로, 주제 기준 중복 제거 집계 |
| 공식 전문 직접 열람·로컬 파일 미보관 | 3 | `verified-primary-source` | SEC·IMF·OECD: HTTP 403으로 자동 다운로드만 실패 |
| 본문 미열람 후보 | 1 | `candidate-not-read` | IMF *Repo Rate Dynamics: The Role of Dealers, Hedge Funds, and Issuance*: 공식 landing page 발견, 본문 Access Denied로 집계 제외 |

추가 22건의 정확한 제목·저자·문헌유형·직접 열람 범위·한계·공식 URL은 [[US-Treasury-Yields-2026-Expansion-Primary-Source-Catalog]]에, 로컬 보관 파일의 MIME·페이지 수·텍스트 추출 검증은 [[US-Treasury-Yields-Expansion-File-Verification]]에 기록했다. **후보·검색결과·제목만 확인한 자료는 위 38건에 포함하지 않았다.**
