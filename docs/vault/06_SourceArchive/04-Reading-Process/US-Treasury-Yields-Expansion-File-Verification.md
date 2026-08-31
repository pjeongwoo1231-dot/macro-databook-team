---
title: "US Treasury Yields Expansion File Verification"
type: "file-verification-log"
reference_date: "2026-08-15 GMT+9"
verification_status: "passed-with-documented-access-limitations"
tags:
  - US-Treasury
  - primary-sources
  - integrity
  - file-verification
---

# 미국 국채금리 확장 원문: 파일 보관·검증 기록

이 노트는 [[US-Treasury-Yields-2026-Expansion-Primary-Source-Catalog]]에 기록한 추가 `verified-primary-source` 22건 중 로컬 보관이 가능한 공식 원문을 파일 단위로 검증한 결과다. 모든 보관 PDF는 `pdfinfo`로 페이지 수를 확인하고 `pdftotext`로 텍스트 추출 가능성을 확인했다. 공식 HTML은 파일 크기·차단 문구·문서 구조를 확인했다.

## 요약

| 항목 | 결과 |
|---|---:|
| 추가로 직접 검토한 공식 원문 | 22건 |
| 로컬 보관·파일 검증 통과 | 19건 |
| 보관 PDF | 6건 |
| 보관 공식 HTML | 13건 |
| 자동 다운로드 차단으로 로컬 보관 실패 | 3건 |
| 손상·비정상 PDF | 0건 |
| 보관 파일 중 텍스트 추출 불가 PDF | 0건 |

> **검증 상태의 의미:** 로컬 파일 보관 실패는 원문 미열람과 다르다. SEC, IMF, OECD 원문은 공식 완전 HTML 또는 공식 PDF를 직접 열람해 내용 검증을 완료했지만, 각 사이트의 자동 수집 방어(HTTP 403)로 이 보관 폴더에 복사하지 못했다. 이 3건은 `verified-primary-source`로 유지하되 보관 제약을 명시한다.

## 로컬 보관·검증 통과 파일

| 파일명 | 형식 | 검사 결과 |
|---|---|---|
| CFTC-2024-The-Treasury-Cash-Futures-Basis-Trade-and-Effective-Risk-Management-Practices.pdf | PDF, 20쪽 | 텍스트 추출 가능 |
| Chicago-Fed-Letter-516-How-the-US-Treasury-Futures-Market-and-the-Basis-Trade-Could-Be-Affected-Part-1.html | 공식 HTML | 저장 HTML 검증 통과 |
| FRBDallas-2026-Term-funding-premium-Time-is-money-even-absent-interest-rate-risk.html | 공식 HTML | 저장 HTML 검증 통과 |
| FRBNY-2023-Collaboration-Toward-Increased-Resilience-of-the-Treasury-Market.html | 공식 HTML | 저장 HTML 검증 통과 |
| FRBNY-2024-Measuring-Treasury-Market-Depth.html | 공식 HTML | 저장 HTML 검증 통과 |
| FRBNY-2025-Recent-Developments-in-Treasury-Market-Liquidity-and-Funding-Conditions.html | 공식 HTML | 저장 HTML 검증 통과 |
| FRBNY-2026-Repo-Market-Structure-and-Monetary-Policy-Implementation.html | 공식 HTML | 저장 HTML 검증 통과 |
| FRBNY-2026-Treasury-Market-Liquidity-Since-April-2025.html | 공식 HTML | 저장 HTML 검증 통과 |
| FRBNY-Staff-Report-1070-Dealer-Capacity-and-US-Treasury-Market-Functionality.pdf | PDF, 70쪽 | 텍스트 추출 가능 |
| FRBSF-2026-Treasury-Yield-Premiums.html | 공식 HTML | 저장 HTML 검증 통과 |
| Federal-Reserve-2021-Sizing-hedge-funds-Treasury-market-activities-and-holdings.html | 공식 HTML | 저장 HTML 검증 통과 |
| Federal-Reserve-2024-Quantifying-Treasury-Cash-Futures-Basis-Trades.html | 공식 HTML | 저장 HTML 검증 통과 |
| IAWG-2024-Enhancing-the-Resilience-of-the-US-Treasury-Market-2024-Staff-Progress-Report.pdf | PDF, 15쪽 | 텍스트 추출 가능 |
| NBER-W34018-Revisiting-the-Interest-Rate-Effects-of-Federal-Debt.pdf | PDF, 29쪽 | 텍스트 추출 가능 |
| OFR-2026-Calm-Markets-and-Underlying-Risks-Highlights-from-the-OFRs-2025-Annual-Report.html | 공식 HTML | 저장 HTML 검증 통과 |
| OFR-2026-How-Will-Central-Clearing-Impact-the-Repo-Market.html | 공식 HTML | 저장 HTML 검증 통과 |
| OFR-Brief-20-01-Basis-Trades-and-Treasury-Market-Illiquidity.pdf | PDF, 18쪽 | 텍스트 추출 가능 |
| OFRBrief-26-01-Hedge-Fund-Participation-in-Cleared-Repo.pdf | PDF, 10쪽 | 텍스트 추출 가능 |
| Treasury-TBAC-2026-Minutes-of-the-Meeting-May-5-2026.html | 공식 HTML | 저장 HTML 검증 통과 |

## 로컬 보관 제약이 있는 직접 검토 원문

| 기관 | 원문 제목(원문 표기) | 직접 열람 상태 | 로컬 보관 상태 | 제약 |
|---|---|---|---|---|
| IMF | *Global Financial Stability Report, April 2025; Chapter 1: Enhancing Resilience Amid Global Trade Uncertainty* | 공식 PDF 직접 열람 | 미보관 | 자동 다운로드 HTTP 403 |
| OECD | *Global Debt Report 2026, Chapter 3: The investor base for government and corporate bond markets* | 공식 완전 HTML 직접 열람 | 미보관 | 자동 다운로드 HTTP 403 |
| SEC | Uyeda, *Update on the SEC’s Work Toward Treasury Clearing Implementation [August 2026]* | 공식 완전 HTML 직접 열람 | 미보관 | 자동 다운로드 HTTP 403 |

## 재현 절차

보관 폴더는 `05-Primary-PDFs/US-Treasury-Yields-2026-Expansion/`이고, 파일 단위 검사 결과의 TSV 원본은 볼트 외부 작업 경로 `us-treasury-yields-expansion-file-verification.tsv`에 저장했다. 검증 절차는 PDF MIME 형식·페이지 수·텍스트 추출 가능성, HTML의 차단 응답 여부·파일 크기·문서 구조를 함께 확인한다.

## 연결 노트

- [[US-Treasury-Yields-2026-Expansion-Primary-Source-Catalog]]
- [[US-Treasury-Yields-2026-Core-Source-Summary]]
- [[US-Treasury-Yields-File-Verification]]
- [[US-Treasury-Yields-2026-Mechanism-Map]]
