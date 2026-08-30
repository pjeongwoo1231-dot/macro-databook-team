# OBSIDIAN.md

# ============================================================================
# Obsidian Long-term Memory Architecture
# ============================================================================

Version : 3.0 (삼위일체판)

---

# Purpose

Obsidian은 메모장이 아니다.
장기 기억(Long-term Memory)이다.

Claude의 기억은 Context Window에 제한된다.
Obsidian은 영구 기억이다.
Graphify는 이 기억을 Knowledge Graph로 연결한다.

---

# Philosophy

모든 노트는 미래의 나를 위해 작성한다.
AI가 읽기 쉬워야 한다.
사람도 읽기 쉬워야 한다.

모든 노트는 하나의 질문에 답한다.
하나의 노트에 여러 주제를 넣지 않는다.
Atomic Note를 지향한다.

---

# Vault Structure

```
Vault
│
├── 00_System          양식 · 운영 가이드 · 부록 · 자동화 설정
├── 01_Daily           자동 생성 Daily Note
├── 02_Journal         Journal + 개인 매매일지 (이름별)
├── 03_Research        AI Interpretation · 체화 노트 · Final
├── 04_DataBook        팀별 DataKit (자동수집 + 수동 슬롯)
├── 05_Regime          레짐 뷰 1.0 · ChangeLog · 2.0 · 검증 매트릭스
├── 06_Industries      산업 노트
├── 07_Companies       기업 노트
├── 08_Assets          자산 노트 (채권·원자재·환율·크립토·ETF)
├── 09_Countries       국가 노트
├── 10_Policies        정책 · 중앙은행 · 재정
├── 11_Reports         외부 리포트 + 리포트 해부 노트 (2~4주차)
├── 12_Papers          논문 · 자료
├── 13_Presentations   발표자료 + 발표 피드백
├── 14_Hypothesis      가설 · Thesis
├── 15_Recommendation  추천 (삭제 금지)
├── 16_Tracker         Recommendation Tracker (기수 인수인계)
├── 17_Meetings        회의록 · 이벤트 캘린더 · 플레이북
├── 18_Prompts         프롬프트 버전 관리 (Hermes · AI 위원회)
├── 19_AI              AI 산출물 로그 (Hermes 결과 · AI 위원회 회의록)
└── Attachments
```

폴더는 도메인이다.
지식이 쌓일 곳을 미리 마련해 둔다 —
빈 폴더는 부채가 아니라 그래프가 자랄 자리다.

---

# Naming Convention

파일명은 명확해야 한다.

예시 :
US CPI / Korea GDP / Fed Minutes / NVIDIA Analysis /
Oil Market / AI Semiconductor Thesis /
Interpretation_W5_Team2 / RegimeView_1.0

날짜를 파일명에 넣지 않는다. 날짜는 Metadata에 저장한다.
(주차 산출물은 W[N]으로 주차를 표기한다 — 스냅샷 버전 역할.)

---

# YAML (모든 노트 필수)

```yaml
---
title:
type:          # databook | interpretation | embodiment | final | regime |
               # journal | recommendation | tracker | report | company |
               # industry | country | asset | policy | hypothesis |
               # presentation | meeting | prompt | ai-log | daily
team:          # 1 | 2 | 3 | 4 | all | 개인
week:          # 1~10 (해당 시)
created:
updated:
status:        # draft | working | validated | archived | superseded
author:        # 사람 이름 | Claude | Hermes
source:        # FRED · ECOS · KRX · DART · 한은 · Reuters · 사용자 · Claude 생성
reliability:   # official | research | government | academic | media |
               # community | opinion | ai-generated
regime:        # 그 시점 레짐 뷰
trigger:       # 관련 무효화 트리거
tags:
related:       # 내부 링크 목록
---
```

---

# Status

Draft → Working → Validated → Archived / Superseded / Deprecated

과거 버전은 삭제하지 않고 superseded로 표시 + 새 버전 링크.

---

# Tag Rule

태그는 분류가 아니라 검색 보조이다. 남용하지 않는다.
예 : #macro #inflation #fed #bond #oil #semiconductor #china #usa #research

---

# Link Rule

모든 노트는 최소 3개의 내부 링크를 가진다.
고립된 노트를 만들지 않는다.

특히 강제되는 링크 :
- 매매일지 → 그 시점 레짐 뷰 또는 DataKit (논거 없는 기록 금지)
- AI Interpretation → 근거 DataKit
- 체화 노트 → 해당 AI Interpretation
- Final → Interpretation + Hermes 결과
- 레짐 뷰 수정 → 근거 데이터/이벤트 노트
- Recommendation → Regime + Trigger + Evidence
- Tracker → 당시 Data Book 스냅샷

---

# Daily Note (01_Daily — 자동 생성)

매일 자동 생성한다. 포함 :
오늘 뉴스 · 오늘 데이터 · 오늘 분석 · 오늘 질문 ·
오늘 아이디어 · 오늘 할 일 · 오늘 Journal.

자동수집기 결과 요약과 트리거 근접 경보를 자동 삽입한다.

---

# Research Note (03_Research)

구조 :
Summary → Evidence → AI Interpretations(복수 + 확신도)
→ 체화(재서술 · 질문 · AI 답변 · 선택 이유)
→ Counter Argument → Regime → Trigger
→ Conclusion → Journal → Next Action

---

# Regime Note (05_Regime)

현재 시장 상태 정의 + 근거 + 반례 + 무효 조건 +
가격 검증 상태 + 관련 Recommendation.
수정은 ChangeLog 누적으로만.

---

# Company / Industry / Country Note

기업 노트는 기업 설명보다 Investment Thesis를 우선한다 :
Business · Competitive Advantage · Risk · Catalyst ·
Macro Exposure · Valuation · Related Industry · Related Policy.

산업 노트는 Macro · 관련 기업 · 관련 국가와 연결된다.
국가 노트는 정치 · 경제 · 중앙은행 · 산업 · 지정학을 연결한다.

---

# Prompt (18_Prompts)

좋은 Prompt는 Knowledge이다.
Prompt도 버전 관리한다. Prompt끼리 관계를 만든다.

---

# AI Memory Rule

Claude가 새로운 정보를 생성하면 관련 노트를 먼저 찾는다.
새 노트를 만들기 전에 기존 노트 업데이트 가능 여부를 검사한다.
비슷한 노트가 있으면 병합을 제안한다.

새 노트는 기존 Graph를 풍부하게 만들어야 한다.
단순 저장을 목적으로 하지 않는다.

---

# Never Do

- 고아 노트 생성 금지
- 출처 없는 노트 금지
- YAML 없는 노트 금지
- 링크 없는 노트 금지
- 태그 남발 금지
- 중복 노트 생성 금지
- Journal · Tracker · ChangeLog 삭제 금지

---

# Success Criteria

좋은 Vault는 노트 수가 많은 것이 아니다.
서로 연결된 지식이 많은 것이다.

Obsidian은 Claude의 장기 기억이며,
Graphify는 그 기억을 하나의 Knowledge Graph로 이해한다.
