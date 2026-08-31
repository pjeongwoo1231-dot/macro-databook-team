---
title: "거시경제 원문 라이브러리 — 가져오기 안내"
type: MOC
created: 2026-08-13
updated: 2026-08-14
archive_status: "verified-primary-source"
tags:
  - macroeconomics
  - financial-stability
  - obsidian
  - primary-sources
status: working
verification: n-a
reliability: institutional
verified: "△ 색인 노트. 항목의 검증 등급은 각 노트의 verification·text_basis 를 따른다"
related: ["[[원문 아카이브 MOC]]"]
text_basis: index
vault_tier: M
---

# 거시경제 원문 라이브러리

이 묶음은 **공식 기관 또는 저자의 무료 원문 전문에 연결되는 자료만**으로 구성한 Obsidian 호환 Markdown 라이브러리입니다. 금융위기와 코로나는 출발점일 뿐이며, 라이브러리는 성장·물가·통화·재정·부채·자본흐름·금융안정·주택신용·노동분배·기후금융·구조개혁을 하나의 탐색 구조에 넣습니다. 이 패키지는 투자 권고가 아니라, 주장·자료·식별·한계·적용 범위를 분리해 읽기 위한 연구 도구입니다.

| 구역 | 역할 | 시작 파일 |
|---|---|---|
| `00-Start` | 읽기 순서·검증 기준·주제별 입구 | [[Macro-Economy-Research-MOC]], [[Macro-Financial-Crisis-MOC]] |
| `01-Events` | 금융위기·코로나·인플레이션 정상화의 사건 축 | [[Global-Financial-Crisis-2007-2009]], [[Covid-19-Global-Sudden-Stop]], [[Post-Pandemic-Inflation-and-Normalisation]] |
| `02-Mechanisms` | 신용, 유동성, 통화전파, 국제파급의 공통 경로 | [[Credit-Leverage-Risk-Pricing-Loop]], [[Sudden-Stop-and-Bridge-Finance]], [[Monetary-Policy-Transmission-and-International-Spillovers]], [[Central-Clearing-Model-Risk-and-Skin-in-the-Game]] |
| `03-Sources` | IMF·세계은행·BIS·NBER 핵심 문헌의 질문·방법·결과·한계 | [[IMF-WEO-2024-Policy-Pivot-Rising-Threats]], [[IMF-Fiscal-Monitor-2024-Public-Debt]], [[IMF-GFSR-2024-Uncertainty-Financial-Stability]], [[World-Bank-GEP-2024-06-Global-Outlook]] |
| `04-Reading-Process` | 출처 선택·직접 검토 범위·조사 로그 | [[Source-Selection-and-Reading-Log]] |
| `05-BIS-Working-Papers` | BIS Working Paper별 구조화 노트와 직접 심층검토 노트 | [[BIS_WP_849]], [[BIS_WP_867]], [[BIS_WP_873]], [[BIS_WP_874]], [[BIS_WP_875]] |
| `06-BIS-Archive-Catalog` | BIS WP 819–1371 구간 원문 탐색·주제 색인·수집 예외 기록 | [[BIS-Fulltext-Topic-Index]], [[BIS-Archive-Gap-Recovery-2026-08-14]], [[BIS-WP-1323-Withdrawn]] |
| `05-Primary-PDFs` | 2022–2023 핵심 원문 PDF 18건 + Fed FEDS Note HTML 1건 | [[2022-2023-Core-Source-Summary]] |

## 가져오기와 운영 원칙

압축을 풀어 원하는 Obsidian 볼트의 루트에 병합하면 내부 링크가 작동합니다. 동일한 제목의 파일이 기존 볼트에 있으면 먼저 이름 충돌을 확인하십시오. 이 묶음은 외부 플러그인·스크립트·자동화에 의존하지 않으며 Dataview 없이도 읽을 수 있습니다.

각 **사건 노트**는 ‘무슨 일이 있었나’와 ‘어떤 메커니즘으로 확대됐나’를 구분합니다. 각 **메커니즘 노트**는 단일 사건의 서술을 일반화합니다. 각 **문헌 노트**는 원문 URL, 문헌 유형, 검토 범위, 자료·방법, 핵심 결과와 한계를 병기합니다. 문헌 노트의 `reading_scope`는 실제로 이 노트가 직접 검토한 원문 범위를 표시하므로, 보고서 전체를 읽은 노트와 특정 장을 읽은 노트를 혼동하지 마십시오.

> **검증 규칙**: 검색 결과 요약, 제3자의 재인용, 원문 미열람 초록은 이 묶음의 사실 근거로 사용하지 않습니다. Working Paper는 동료심사 전 배포본일 수 있으므로, 해당 지위와 저자·기관의 견해임을 함께 보존합니다.

## BIS 전수 아카이브의 상태

BIS Working Papers 레코드 536건을 전수 대조했습니다. 이 중 **535건은 BIS 공식 PDF의 파일서명·최소용량·페이지수·텍스트 추출을 통과**하여 원문 아카이브에 보관했고, 1건(BIS WP 1323)은 저자 요청에 따른 BIS 공식 철회 상태여서 공개 PDF가 없습니다. 철회는 수집실패와 다르며, 그 예외와 공식 공지는 [[BIS-WP-1323-Withdrawn]]에 남겼습니다.

[[BIS-Fulltext-Topic-Index]]는 535건의 추출 전문에서 재현 가능한 키워드 규칙으로 만든 **탐색용 카탈로그**입니다. 이는 원문을 대체하는 실질 요약이나 품질평가가 아닙니다. `05-BIS-Working-Papers`의 구조화 노트 중 `reading_scope`가 명시된 심층 노트는 직접 전문 검토를 거친 문헌이고, 나머지 자동 구조화 노트는 원문 재확인을 위한 길잡이로 취급해야 합니다.

## 권장 탐색 순서

거시 전반을 보려면 [[Macro-Economy-Research-MOC]]에서 주제별 입구를 고른 뒤, IMF의 세계성장·물가·정책조합([[IMF-WEO-2024-Policy-Pivot-Rising-Threats]]), 세계은행의 EMDE 성장·부채·공공투자 제약([[World-Bank-GEP-2024-06-Global-Outlook]]), IMF의 공공부채 상방위험([[IMF-Fiscal-Monitor-2024-Public-Debt]]), 금융시장·NBFI 취약성([[IMF-GFSR-2024-Uncertainty-Financial-Stability]]) 순서로 읽으십시오. 이후 [[BIS-Fulltext-Topic-Index]]에서 같은 주제의 BIS 원문으로 내려가면, 기관 보고서의 종합진단과 Working Paper의 데이터·방법을 대조할 수 있습니다.

금융위기와 코로나 중심의 역사적 경로는 [[Macro-Financial-Crisis-MOC]]에서 시작하십시오. 사건을 읽은 뒤 [[Credit-Leverage-Risk-Pricing-Loop]]와 [[Sudden-Stop-and-Bridge-Finance]]으로 이동하면 충격의 유형은 달라도 신용·자금조달·위험프리미엄이라는 공통 취약성을 추적할 수 있습니다.

## 범위와 업데이트 기준

이 라이브러리는 살아 있는 연구 인프라입니다. 전망 보고서의 수치와 정책평가는 발간 시점의 정보·가정에 묶여 있으므로, 새 판이 나왔다고 기존 노트를 덮어쓰지 말고 발행월을 붙인 새 노트로 병존시키십시오. 특정 주장에 대해 표본·국가·식별전략이 다른 원문을 연결해 경쟁 가설을 만들고, 확정적 정책결론으로 격상시키기 전에는 원문상 한계를 확인하십시오.

## 이 볼트판에서 원본과 달라진 점

마누스가 보낸 두 묶음(`primary-source-library`, `financial-crisis-obsidian-notes-expanded`)은
포함관계가 아니라 서로 다른 내용을 담고 있어 손실 없이 병합했다. 그 위에 네 가지를 고쳤다.
전체 내역은 볼트 밖 `FIX-REPORT.md`에 있다.

1. **파일명 충돌 59건 해소.** `05`의 심층 노트와 `06`의 카탈로그 스텁이 같은 이름이라
   `[[BIS_WP_849]]`가 스텁으로 빨려가 심층 노트가 색인에서 고아가 됐다. 스텁을
   `BIS_WP_###-catalog.md`로 개명하고 양방향 링크를 걸었다.
2. **출처 축 신설.** `human_verified`로 사람 검증 5건과 `gpt-5-mini` 자동 생성 54건을
   분리했다. 자동 노트는 `status: llm-structured-unverified`이고 본문 최상단에 경고가 붙는다.
   **Dataview로 인용 가능 문헌을 거를 때는 `human_verified: true`를 쓸 것.**
3. **누락 17건 보완.** WP 820–835, 996을 공식 PDF로 수집해 `06/PDFs/`에 실물 보관했다.
4. **2022–2023 세트 보존.** 원 `primary-source-library`가 버렸던 노트 6건과
   PDF 19건을 되살렸다.

**작성 기준일**: 2026-08-14 (병합·정정 반영)
