---
title: 원문 아카이브 MOC
type: MOC
created: 2026-08-14
updated: 2026-08-14
status: working
author: Claude
source: 마누스 납품 2묶음(2026-08-14) 병합·정정본 + 누락 17건 보완
verification: n-a
reliability: secondary
tags: [type/MOC]
related: ["[[원문대조 감사 2026-08-14]]", "[[Library MOC]]", "[[원문검증 논문 MOC]]", "[[문헌군 지형도]]", "[[지표 MOC]]", "[[WHY_QUARANTINE_SECONDARY|왜 2차 요약본을 격리했는가]]"]
---

# 원문 아카이브 MOC — `06_SourceArchive/` 659편

> 이 MOC은 **목록이 아니라 검증 등급의 지도**다. 볼트 규칙대로 연결은 소환하는 쪽에서
> 만들어지므로 여기에 659편을 손으로 유지하지 않는다. 문헌 목록은
> [[BIS-Fulltext-Topic-Index]](주제별) 와 [[Macro-Economy-Research-MOC]](읽기 순서) 에 있다.

## ⚠ 이 아카이브는 **판정 경로가 아니다** *(2026-08-18 실측 후 명시)*

폴더 간 링크를 실측했다.

| | 값 |
|---|---:|
| 06_SourceArchive 노트 수 | **1,507** (볼트의 58%) |
| 내부 링크 | **7,061건** |
| **외부에서 인용된 노트** | **50 / 1,507 = 3.3%** |
| 판정 폴더(01·03·05)에서의 소환 | **51건** |

대조군: 05_Library 100% · 02_Papers 97.1% · 04_Zettel 99.4% · 01_Indicators 100%가 외부에서 인용된다.

**이것은 결함이 아니라 설계다.** 2026-08-14 통합 때 *"카탈로그 552편에는 의도적으로 소환을 붙이지 않는다 —
지표 노드 백링크 오염 방지"* 라고 정했다. 연결 수를 늘리는 것이 목적이 아니었다.

**그래서 성격을 못박는다**
- 이 폴더는 **검색용 창고**다. 시황·레짐 판정은 여기서 시작하지 않는다 → [[시황 분석 진입점]]
- 쓸 일이 생기면 **필요한 문헌만 02_Papers로 승격**해 판정 경로에 올린다(지금까지 9편 + BIS AER 3편)
- **꺼내는 경로를 2026-08-18에 만들었다** → [[1차 문헌 찾기 (아카이브 진입로)]].
  그전까지는 "안 건다"는 규칙만 있고 **꺼낼 방법이 없었다** — 그것이 3.3%의 진짜 원인이다
- **그래프 뷰에서는 숨긴다**(`.obsidian/graph.json`의 search 필터 `-path:"06_SourceArchive"`).
  숨긴다고 검색·백링크가 사라지지는 않는다 — **판정 경로를 보려는 그래프에서 시야를 막지 않으려는 것**이다

## 이게 뭔가

2026-08-14 마누스가 납품한 거시경제 원문 라이브러리 2묶음이다. BIS Working Papers
819–1371 구간과 IMF·World Bank·NBER·BOJ·Fed의 기관 문헌으로 구성된다.
[[Library MOC]]의 399편과 **출처가 같다(마누스)**. 따라서
[[WHY_QUARANTINE_SECONDARY|왜 2차 요약본을 격리했는가]]의 판단이 그대로 적용된다 — 다만 이번 묶음은
**등급이 균일하지 않아서** 폴더가 아니라 `verification` 필드로 갈랐다.

## 검증 등급과 인용 규칙 — 읽기 전에 이것부터

**이 묶음은 [[Library MOC]] 399편과 출처(마누스)는 같지만 생산 방식이 다르다.**
399편은 원문 없이 만들어졌고, 이 묶음은 공식 PDF를 실제로 받아 파일서명·페이지수·
SHA-256·텍스트추출을 검증한 뒤 **그 추출 전문 위에서** 구조화한 것이다.
표본 대조에서 오류가 나오지 않았다 — [[원문대조 감사 2026-08-14]] (**15편 / 대조 항목 64건 / 오류 0**).

| tier | 건수 | `verification` | `text_basis` | 인용 규칙 |
|---|---:|---|---|---|
| A | 5 | **`full`** | `human-fulltext` | **02_Papers로 승격 완료** — 인용은 승격 노트에서 |
| B | 54 | `partial` | `llm-fulltext` | 서술 가능, **수치·표는 원문 확인** |
| C | 17 | `n-a` | `local-pdf` | 출처 표기 후 인용. **PDF 실물을 볼트가 보유** |
| D | 535 | `partial` | `extracted-abstract` | 초록 범위 안에서만. 밖은 원문 확인 |
| E | 43 | `partial` | `cited-primary` | 서술 가능. 수치는 각주 원문 확인 |
| M | 4 | `n-a` | `index` | 색인 |

`verification` 값 5개로는 제약의 **종류**를 못 가르므로 `text_basis`를 신설했다.
필드 정의는 `_System/docs/FRONTMATTER_VOCAB.md`에 추가해 뒀다.

> ⚠ **주의**: B(54편)는 겉보기에 A와 똑같이 생겼다. 연구질문·방법·결과·한계가 전부
> 채워져 있고 표까지 있다. 납품 원본은 59편 전부에 `verified-primary-source`를 달아 놨었다.
> **본문을 보고 등급을 짐작하지 말고 `text_basis`를 볼 것.**
>
> 반대로, **출처가 같다는 이유만으로 격리하지도 말 것.** 이 묶음을 처음에 `none`
> (인용 금지)으로 매겼다가 실제 대조 후 정정했다. 그것도 감사 노트에 적혀 있다.

인용 가능한 것만 거르려면:

```dataview
TABLE verification, text_basis, verified
FROM "06_SourceArchive"
WHERE verification != "none"
SORT text_basis ASC
```

수치까지 쓸 수 있는 것만:

```dataview
LIST FROM "06_SourceArchive" WHERE verification = "full" OR text_basis = "local-pdf"
```


## 승격 완료 — tier A 5편 전량 (2026-08-14)

원문 대조 35개 항목 전부 일치. `02_Papers/`에서 `verification: full`로 운용한다.
**인용은 승격 노트에서** 한다 — 아카이브 원본에는 승격 표시와 역링크만 남겼다.

- [[2020 Effects of Fed Policy Rate Forecasts at the ZLB (Galati & Moessner)]] — 점도표가
  실질금리는 −6bp 움직이고 **5y5y 기대인플레는 안 건드렸다**. [[기관 예측 신뢰도 스코어카드]] 직결
- [[2020 Credit Risk Mispricing in the Subprime Boom (Kahn & Kay)]] — 평평한 보험료가
  교차보조·역선택을 만들었다. [[Credit-Leverage-Risk-Pricing-Loop]]의 "위험가격 압축"에 실체
- [[2020 Macroprudential Policies and Capital Controls against Volatile Inflows (Frost, Ito & van Stralen)]]
  — **자본통제는 효과 없고 FX 기반 거시건전성은 있었다**(83개국·PSM)
- [[2020 Demographic Origins of the Decline in Labor's Share (Glover & Short)]] —
  노동소득분배율 하락의 **59%가 고령화**. 노조 산업에서는 관계가 사라진다
- [[2020 Reserve Management and Sustainability - Green Bonds (Fender, McMorrow, Sahakyan & Zulaica)]]
  — 그린본드는 **투자 트랜치엔 되고 유동성 트랜치엔 안 된다**


## 2024–2026 확장분 (2026-08-14 2차 납품)

마누스 3차 묶음. **증분만 반영했다** — 21편은 이전 납품과 바이트 동일이라 건드리지 않았고
(볼트본에는 프론트매터·소환·직접링크 작업이 얹혀 있다), 실제 신규는 아래다.

| 구분 | 수 |
|---|---:|
| 신규 노트 | 3 (Mechanism Map · Core Source Summary · WB GEP Jan-2025 페이지) |
| 원문 파일 | **33** (BIS·BOJ·Fed·IMF·NBER·OECD·World Bank, 2024–2026) |
| 기존 노트 이식 | 2 (MOC 1개 절 · Reading Log 4개 배치) |

**PDF 33건 전부 실물 신원을 확인했다** — 표지 추출로 파일명·기관·판본이 전부 일치.
수치 3건 표본 대조도 통과:

- OECD Interim Sep 2025 — 노트 "2025년 3.2% → 2026년 2.9%" ↔ 원문 *"3.2% in 2025 and 2.9% in 2026"*
- World Bank GEP Jan 2026 — 노트 "2026년 2.6%" ↔ *"global growth is projected to edge down to 2.6 percent"*
- BIS WP 1285 — 노트 "미국→동아시아 3국, 중국→한·일 파급" ↔ *"significant positive spillovers from the US
  to the three East Asia countries, as well as spillovers from China to Kora and Japan"*

### 이번 납품에서 개선된 것

수집 실패를 **명시했다** — IMF WP 2024/196이 404라 집계에서 뺐다고 적혀 있다.
`MANUS-REQUEST.md` 2번(실패 로그) 항목이 반영됐다.

### 남은 문제

- **`.SHA256`이 또 안 왔다.** 무결성 검증 불가 (요청서 6번)
- **로그 집계와 실제 수록이 어긋난다.** 로그는 29건인데 Core Summary는 34개 문헌·34개 각주다.
  빠진 5건: OECD Interim(2024-09·2025-09·2026-03), OECD Outlook 2024 Issue 1, WB GEP Jan 2025.
  **과소집계**라 인용 안전성 문제는 아니지만 로그가 기록인 이상 맞아야 한다.
  볼트 측 정정은 [[Source-Selection-and-Reading-Log]]에 적어 뒀다


### 2024–2026 승격 5편 (2026-08-14)

로컬 PDF를 직접 판독해 `02_Papers/`로 승격했다. 선정 기준은 **기존 볼트 자료와 충돌하거나
보완하는지**였다.

- [[2025 Navigating the 2022 Inflation Surge - IT vs Non-IT (Imam et al, IMF WP 25-212)]] —
  IT 33국 vs non-IT 37국, 양쪽 다 ~9% 정점. **IT가 더 세게 올렸는데 결과는 안 나았다**
- [[2025 Post-Pandemic Global Inflation and Disinflation (Clarida, NBER W33885)]] —
  반사실: 일찍 올렸어도 **물가 −1%p 미만, 실업 +2%p**. 단 SOMC 발표문 개정판이고 저자가 당사자
- [[2026 Limited Effects of Post-Pandemic US Monetary Tightening (BOJ WP 26-E-6)]] —
  **정책이 약해진 게 아니라 경제 구성이 바뀌었다.** EBP를 전이변수로 쓴 ST-LP
- [[2025 Monetary Policy, Uncertainty, and Communications (Garga et al, FEDS 2025-074)]] —
  **불확실성이 크다고 점진주의가 정답은 아니다.** 출처와 모형에 의존
- [[2025 R-star in East Asia - Business, Financial Cycles and Spillovers (Siklos, Xia & Chen, BIS WP 1285)]] —
  경기순환 r*와 금융순환 r*가 따로 논다. **미국→한중일, 중국→한일** 파급


**2차 배치 (4편)**

- [[2025 From Banks to Nonbanks - Macroprudential and Monetary Policy Effects on Corporate Lending (Albuquerque et al, IMF WP 25-96)]] —
  긴축하면 신용이 사라지는 게 아니라 **비은행으로 옮겨간다**(은행 대비 +4.6%). 규제도 같은 방향으로 샌다
- [[2024 Global Demand and Supply of International Reserves (Mendoza & Quadrini, NBER W32810)]] —
  **구성의 오류.** 혼자 쌓으면 안전해지고 다 같이 쌓으면 위험해진다. 안 쌓는 나라가 최대 피해
- [[2025 Unconventional Monetary Policies in Small Open Economies (Kolasa, Laseen & Linde, IMF WP 25-66)]] —
  **환율이 비전통정책은 키우고 재정정책은 깎는다.** 대국 문헌을 소규모 개방경제로 옮기면 틀린다
- [[2025 Households' Inflation Expectations - Past Experience and Regimes (Fujii & Nakano, BOJ WP 25-E-6)]] —
  생애 경험 +1%p → 기대 **+0.357%p**. 기대는 발표가 아니라 경험으로 바뀐다


## 4차·5차 납품 반영 (2026-08-14) — WP 1–1371 + 2019–2021

| 구분 | 내용 |
|---|---|
| **BIS WP 1–818 카탈로그 818건** | 요청서 A-1(819 이전 확장) 반영. 그중 **34건은 스캔본**이라 텍스트 추출 불가 → `text_basis: scan-limited`, `verification: unknown` |
| **연결 노트 3건** | [[Macro-Research-Relations-Map]] · [[Macro-Economy-Connection-Map]] · [[Macro-Economy-Learning-Paths]] |
| **2019–2021 세트** | [[2019-2021-Core-Source-Summary]](10문헌) · [[2019-2021-Comparative-Mechanism-Map]] · 원문 10건 |
| **WP 870·876·890** | 부분 직접검토(1–8쪽/1–4쪽) → `text_basis: human-partial`, tier A2 |
| **Topic Index** | WP 1–1371 기준 재생성본 채택 + ⟨심층⟩ 표시·보완 17건 절 재적용 |

### 마누스 CHANGELOG의 병합 지침은 따르지 않았다

CHANGELOG는 *"동일 경로 파일이 있으면 이 릴리스의 파일로 교체한다"*고 지시한다.
**그대로 하면 지금까지의 작업이 전부 사라진다** — tier·`text_basis` 프론트매터, 소환 노드,
인과 사슬, 직접 링크, 승격 배지 9건, 그리고 마누스가 `not_attempted`로 남긴
**WP 820–835·996 보완 17건(로컬 PDF 포함)**까지.
또 그들 패키지에는 **05 vs 06 파일명 충돌 59건이 그대로 재발**해 있다.
→ 511편은 손대지 않고 **증분만** 넣었다.

### 이번 납품에서 개선된 것

- **범위 정정** — "전수" 표현을 스스로 철회하고 WP 1–818을 실제로 수집(요청서 A-1)
- **매니페스트 상태 구분** — `ok 1,353` / `not_attempted 17` / `withdrawn 1`(요청서 A-2)
- **CHANGELOG 동봉**(체크리스트 C)
- **스캔본 34건을 스스로 표기**(`text_quality: scanned_or_text_limited`)

### 아직 안 된 것

- **`.SHA256` 5번째 누락.** 무결성 검증 여전히 불가
- **원문 PDF·텍스트·코드 아카이브 미수신** — CHANGELOG가 언급한
  `bis-wp-1-1371-full-archive-2026-08-14.zip`이 안 왔다. 카탈로그 1,336건은 **여전히 해시만 있고 대조 불가**
- **파일명 충돌 59건 미수정** — 매 납품마다 이쪽에서 다시 고쳐야 한다


### 2019–2021 승격 4편 (2026-08-14)

코로나 국면. 로컬 PDF 직접 판독.

- [[2021 Fed Dollar Liquidity Lines and Spillovers in COVID (NBER W28585)]] —
  스왑라인 접근권은 **미국과의 연계 강도**로 갈렸다. 막은 것은 **미국채 투매**(집중 시 10년물 +98bp)
- [[2021 Capital Flows-at-Risk in Emerging Economies (Norimasa, Ueda & Watanabe, BOJ WP 21-E-5)]] —
  자본흐름을 **평균이 아니라 꼬리로**. RegimeView **T8의 심각도 축**에 해당
- [[2021 Domestic Lending and the Pandemic - Cross-Border Spillovers to US Credit (Temesvary & Wei, FEDS 2021-056)]] —
  **해외 충격이 국내 대출을 6~7%p 줄인다.** 저자본 은행은 효과 2배
- [[2022 The Monetary-Fiscal Policy Nexus in the Wake of the Pandemic (BIS Papers 122)]] —
  EME가 경기대응할 수 있었던 것은 **선진국이 동시에 완화했기 때문.** 긴축 국면엔 성립 안 함


### 05_Library 승격 1호 — 실업 변동성 4부작 (2026-08-14)

마누스 2차 요약 라이브러리에서 처음으로 `02_Papers`에 올린 것.
Shimer(2005) → Hall(2005) → Hagedorn & Manovskii(2008) → Elsby et al.(2009).
**서지만 확정했고 본문은 유료라 미열람** → `verification: partial`, 수치 인용 금지.
[[RegimeView 1.0 (2026-08-09)]]의 `low-hire-low-fire` 판단이 서 있는 이론적 지반이다.
경위: [[05_Library 중복 판별 (2026-08-14)]]

## 그래프 연결도 (2026-08-14 실측)

[[문헌군 지형도]] 7절의 조치 결과. 숫자는 재실행하면 바뀌므로 스냅샷으로 읽을 것.

| | 지표 노드로 향하는 링크 |
|---|---:|
| 05_Library (399편) | 1,900 |
| 02_Papers (240편) | 1,406 |
| 04_Zettel (177편) | 925 |
| **06_SourceArchive (660편)** | **267** |

아카이브 수치가 낮은 것은 **의도된 것**이다. 552편 카탈로그 스텁에는 소환을 붙이지 않았다 —
초록 키워드로 지표 백링크를 덮으면 신호가 죽는다. 실질 분모는 108편이다.

- 아카이브가 부른 지표 노드 **38/46**. 안 부른 8개(구리·김치프리미엄·제련수수료·동행종합지수
  ·PCE·소비자신뢰지수·무역분쟁·관세)는 **어휘 구멍이 아니라 주제 부재**다 — 억지로 잇지 않았다
- 아카이브 → `02_Papers`/`04_Zettel` **직접 링크 34개**. 기계 매칭이 아니라 내용을 읽고 고른 것
- 볼트 1,586편 중 **98%가 단일 연결요소**. 아카이브발 고립 노트 **0**

> 이 통합 과정에서 [[에너지 전환]]·[[잠재성장률]]·[[KOSPI]]·[[AI 자본지출]] 네 노드에
> **별칭을 추가**했다. 아카이브 19편이 그린본드·ESG·기후를 말하는데 노드 별칭에 그 단어가
> 없어 매칭이 실패하고 있었다. 2026-08-13에 [[문헌군 지형도]]가 쓴 것과 같은 처방이다.

## 어디서 시작하나

- 거시 전반 — [[Macro-Economy-Research-MOC]]
- 금융위기·코로나 역사 — [[Macro-Financial-Crisis-MOC]]
- 메커니즘 — [[Credit-Leverage-Risk-Pricing-Loop]] · [[Sudden-Stop-and-Bridge-Finance]]
  · [[Monetary-Policy-Transmission-and-International-Spillovers]]
  · [[Central-Clearing-Model-Risk-and-Skin-in-the-Game]]
- 2022–2023 긴축·인플레 — [[2022-2023-Comparative-Mechanism-Map]] · [[2022-2023-Core-Source-Summary]]
- **2024–2026 무역분절·불확실성·NBFI — [[2024-2026-Comparative-Mechanism-Map]] · [[2024-2026-Core-Source-Summary]]**
- BIS 전 구간 탐색 — [[BIS-Fulltext-Topic-Index]]
- 수집 경위·누락 — [[BIS-Archive-Collection-Status]] · [[BIS-Archive-Gap-Recovery-2026-08-14]]

## 지표 노드와의 연결

[[문헌군 지형도]]가 기록한 사고(05_Library 399편이 영문 어휘를 써서 그래프가 갈라진 일)를
반복하지 않기 위해, 신규 문헌도 **한글 지표 노드를 소환**하도록 만들었다.

- 서사·메커니즘 8편 — 손으로 쓴 `## 인과 사슬` (실제 인과 주장)
- 분석 보유 80편 — `## 소환한 노드` (별칭 기계 매칭. **인과 주장 아님**, 탐색용)
- 카탈로그 552편 — 소환 없음. 초록 키워드로 지표 노드 백링크를 덮으면 신호가 죽는다

가장 많이 불린 노드: [[통화정책]] 43 · [[글로벌 유동성]] 20 · [[CPI (소비자물가지수)]] 19
· [[원·달러 환율]] 14 · [[산업생산]] 13 · [[GDP 성장률]] 11

## 원본 대비 고친 것

납품본에는 세 가지 결함이 있었고 임포트 전에 고쳤다. 전체 기록은 볼트 밖
`macro-source-library-clean/FIX-REPORT.md`.

1. **"전수 536건" 주장이 사실과 달랐다.** 실제 범위는 WP 819–1371이고 그 안에서 18개가
   비어 있었다. 문서화된 예외는 철회 1건뿐, 나머지 17건은 사유 없이 누락됐고 전부
   bis.org에 공개 PDF가 살아 있었다. → 직접 수집해 tier C로 넣었다.
   경위는 [[BIS-Archive-Gap-Recovery-2026-08-14]]
2. **파일명 충돌 59건.** 심층 노트와 카탈로그 스텁이 같은 이름이라 위키링크가 스텁으로
   빨려가 심층 노트가 색인에서 고아가 되는 구조였다. 스텁을 `-catalog` 접미사로 개명.
   **2026-08-15 상류에서 해결됐다** — 마누스가 카탈로그 전량에 같은 접미사를 붙여 납품했다.
   다만 안내된 적용 절차(삭제 후 복사)를 그대로 따랐으면 검증 등급이 전부 지워졌을 것이라
   개명 병합으로 적용했다 — [[카탈로그 개명 병합 2026-08-15]].
   이제 `[[BIS_WP_###]]`는 **항상 심층 노트**, `[[BIS_WP_###-catalog]]`는 **항상 원문 카탈로그**다
3. **사람 검증본과 LLM 생성본이 프론트매터상 구분 불가.** 위 tier 표로 분리했다.
   다만 이 분리를 처음엔 과하게 해서 tier B·E를 `none`(인용 금지)으로 격리했었다.
   출처가 마누스로 같다는 연상이 근거였고, 실제 대조 결과 틀린 판단이었다 —
   [[원문대조 감사 2026-08-14]]

## 남은 부채

- tier D 535편은 PDF가 없어 **해시 대조 자체가 불가능**하다. 마누스에게 원문 또는
  추출 텍스트를 요청해 둔 상태(`MANUS-REQUEST.md`).
  2026-08-15 CHANGELOG가 `bis-wp-1-1371-text-archive-2026-08-15.zip`을 **이름으로 명시**했으나
  **파일은 오지 않았다.** 만들어져 있을 가능성이 높으니 이것만 받으면 된다
- tier C 17편은 주제색인이 없다. 마누스의 키워드 규칙을 못 받아 재현 불가.
  게다가 마누스 매니페스트에서 여전히 `not_attempted`라 **색인이 재생성될 때마다 사라진다** —
  2026-08-15에도 사라져서 되살렸고, 이번엔 ⟨자체수집⟩ 표시를 붙여 다음 유실이 보이게 했다
- tier B 54편 중 통화정책 전파·글로벌 금융사이클·재정–금융안정 쪽은
  원문 대조 후 `verification: full`로 승격할 후보다
- 카탈로그 초록 13건에 fi/fl 합자 깨짐 (`…nancial`)
