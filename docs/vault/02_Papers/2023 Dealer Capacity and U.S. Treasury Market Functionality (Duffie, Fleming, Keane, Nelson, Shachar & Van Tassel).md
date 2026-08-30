---
title: "Dealer Capacity and U.S. Treasury Market Functionality"
type: paper
journal: Federal Reserve Bank of New York Staff Reports No. 1070 (Aug 2023, rev. Oct 2023) · doi 10.59576/sr.1070
date: 2023
author: Darrell Duffie (Stanford) · Michael Fleming · Frank Keane · Claire Nelson · Or Shachar · Peter Van Tassel (NY Fed 외)
url: https://doi.org/10.59576/sr.1070
tags: [type/paper, method/실증, domain/liquidity, domain/credit]
concepts: [딜러 중개역량, 대차대조표 이용률, 비유동성, 간헐적 구속제약, 비선형]
status: done
verification: full
reliability: institutional
text_basis: local-pdf
verified: "✔ 전문 판독(2026-08-18) — 볼트 보유 PDF `06_SourceArchive/05-Primary-PDFs/US-Treasury-Yields-2026-Expansion/FRBNY-Staff-Report-1070-...pdf`(70쪽) 초록·§본문 직접 확인"
promoted_from: "06_SourceArchive (아카이브 PDF) — [[1차 문헌 찾기 (아카이브 진입로)]] 경로로 승격한 첫 배치"
related: ["[[글로벌 유동성]]", "[[신용스프레드]]", "[[2012 Credit Spreads and Business Cycle Fluctuations (Gilchrist & Zakrajsek)]]", "[[RegimeView 1.0 (2026-08-09)]]"]
archive_pdf: "06_SourceArchive/05-Primary-PDFs/FRBNY-Staff-Report-1070-Dealer-Capacity-and-US-Treasury-Market-Functionality.pdf"
---

# 딜러 대차대조표는 **평소엔 안 보이다가 임계를 넘으면 갑자기 구속된다** (Duffie 외, 2023)

> NY Fed Staff Report 1070. **볼트 보유 PDF 전문 판독** — 인용 가능.

## 왜 중요한가 — 우리 문제와 직결

2026-08-15에 볼트는 **딜러 레포 −164bn을 "중개기관 위험한도 수축"으로 읽었다가 철회**했다
(전 표본 백분위 97%·z −0.68 = 평상시 등락). 그때 남은 질문이 *"그럼 언제부터가 스트레스인가"* 였다.
**이 논문이 그 답의 형태를 준다 — 수준이 아니라 이용률의 임계다.**

## 핵심 결과

**① 국채시장 유동성의 대부분은 금리 변동성으로 설명된다.** 여기까지는 기존 이해와 같다.

**② 그런데 딜러 대차대조표 **이용률**이 충분히 높아지면, 유동성이 **변동성이 예측하는 수준보다 훨씬 나빠진다**.**
잔차 비유동성이 약 **3 표준편차** 더 악화되는 구간이 관측되고, 관계는 **뚜렷하게 비선형**이다.
→ 저자들의 해석: **간헐적으로 구속되는(occasionally binding) 중개역량 제약**의 존재와 정합적이다.

**③ 2020년 3월이 그 사례다.** 3월 12일(WHO 팬데믹 선언일) 국채 비유동성 1주성분이
평균 대비 **5.4 표준편차**까지 치솟았고, 딜러 이용률도 같은 시점에 급등했다.

**④ 측정 방법**: 1차 딜러의 **주간 FR 2004** 순·총 포지션(국채·MBS·회사채) + 고객 거래,
그리고 대형 BHC 채권부문의 **VaR**(보고치 + 일별 손익 분위회귀 추정치).

## 우리 시스템에 적용

1. **[[글로벌 유동성]]의 딜러 레포 규칙을 "수준"에서 "이용률·비선형"으로 고쳐 읽는다** —
   백분위 97%가 곧 스트레스가 아니라는 8/15 판정은 유지되지만,
   **판정 근거가 "평상시 등락"이 아니라 "제약이 아직 구속되지 않았다"** 로 바뀐다
2. **관측 가능한 대용**: 우리는 FR 2004 개별 자료도 BHC VaR도 못 본다.
   대신 **딜러 레포 잔액(수량) × 금리 변동성(MOVE)** 의 조합으로 이용률 국면을 근사한다 — 다음 작업 후보
3. **비선형이므로 회귀 계수 하나로 판정하지 않는다** — 이것이 이 논문의 방법론적 교훈이다

## Red Team

1. **이용률의 임계값을 논문이 하나의 숫자로 주지 않는다.** "충분히 높으면"이라는 조건부 진술이며,
   우리 쪽에서 임계를 쓰려면 **자체 추정이 필요하다**(볼트 규칙: 임계는 재서 만든다)
2. **표본이 2020년 3월에 크게 좌우된다.** 단일 사건 의존 위험
3. **FR 2004는 비공개 세부 자료**다 — 재현 불가. [[IOER이 연방기금시장의 참가자 구조를 뒤집었다 — FHLB가 공급의 78%]]에서 겪은 것과 같은 문제
4. Staff Report는 **동료심사 문서가 아니다**

## 관련 노트

- [[글로벌 유동성]] · [[신용스프레드]] · [[1차 문헌 찾기 (아카이브 진입로)]]
