# GRAPHIFY.md

# ============================================================================
# Graphify Knowledge Graph Architecture
# ============================================================================

Version : 3.0 (삼위일체판)

---

# Purpose

Graphify는 검색 도구가 아니다. Vector Database도 아니다.
Vault 전체를 Knowledge Graph로 변환하는 Core Engine이다.

Claude는 Graphify를 통해 프로젝트를 이해한다.
파일은 지식이 아니다. 파일은 Knowledge의 표현 방식이다.
Graphify는 파일을 이해하지 않는다. 관계를 이해한다.

---

# Graph Scope (2026-07-27 확정)

Graphify는 Vault 전체가 아니라 **연구 운영 계층**을 그래프화한다.

포함 :
CLAUDE.md · _System/** · 01_Indicators/** · 03_MOC/**

제외 :
02_Papers/** (논문·리포트·뷰 128개) · Attachments/** (원문 PDF 39개)

논문 연결은 Graphify가 아니라 **Obsidian Smart Connections**가 담당한다.
논문 ↔ 논문, 논문 ↔ 산출물 노트 연결은 임베딩 의미 검색으로 수행한다.

역할 분담 :
Graphify        = 구조 (커뮤니티 · god node · 경로 · 왜 연결됐는지)
Smart Connections = 근접성 (지금 보는 노트에 의미상 가까운 논문)

이유 :
논문 145개를 semantic 추출에 넣으면 재빌드 비용이 그래프 가치를 넘는다.
논문에 필요한 답은 "커뮤니티 구조"가 아니라
"지금 쓰는 노트와 얼마나 가까운가"이고, 그건 임베딩이 더 잘 답한다.

주의 : graphify에는 ignore 설정 기능이 없다.
`/graphify --update` 나 재빌드 시 제외 경로가 스캔에 다시 잡히면,
그 산출물을 채택하지 않고 포함 경로만 대상으로 다시 실행한다.

---

# 삼위일체 동작 구조 (구현)

```
Obsidian Vault  (Long-term Memory — 파일이 곧 원장)
↓  graphify 재빌드 (자동 : 주 1회 + 대량 변경 시 온디맨드)
graph.json / graph.html / GRAPH_REPORT.md
↓  세션 시작 시
Claude  (Brain)
  ① GRAPH_REPORT.md를 먼저 읽는다
  ② graphify query / path / explain으로 관련 노드를 탐색한다
  ③ 작업을 수행한다 (해석 · 검증 · 노트 생성)
  ④ 새 노트는 Link Rule대로 연결한다
  ⑤ 작업 종료 시 graphify를 재실행해 그래프를 갱신한다
```

이 루프가 삼위일체다.
Obsidian이 기억하고, Graphify가 연결하고, Claude가 추론한다.

재빌드는 자동화한다 :
스케줄러(주 1회) + 세션 훅(작업 종료 시).
사람이 수동으로 돌리는 것을 전제하지 않는다.

---

# Knowledge Graph Priority

항상
Relationship → Context → History → Source → Content
순으로 탐색한다.

파일명을 우선하지 않는다.
Keyword Search만 사용하지 않는다.

---

# Search Rule

Claude는 검색보다 Graph Traversal을 우선한다.
관련 Node를 계속 확장한다.

예시 :
CPI → Inflation → Federal Reserve → Bond
→ NASDAQ → Semiconductor → NVIDIA → AI Theme

검색은 연결 탐색이다.

---

# Node Types

산출물 노드 :
DataKit · Interpretation · 체화노트 · Final ·
RegimeView · 검증매트릭스 · 자산매트릭스 ·
Journal · 매매일지 · Recommendation · Tracker ·
Report · ReportAutopsy · Paper · Presentation ·
Hypothesis · Thesis · Meeting · EventPlaybook ·
Prompt · AI위원회 회의록 · Daily

도메인 노드 :
Country · Region · Institution · Government · Central Bank ·
Macro Indicator · Economic Indicator ·
Company · Sector · Industry ·
Commodity · Currency · Bond · Stock · ETF · Crypto ·
Policy · Law · War · Conflict · Election · Speech ·
Regime · Trigger · Signal ·
Person · Organization · Team

시스템 노드 :
Code · API · Dataset · CSV · PDF · Image · Video ·
Markdown · Workflow · Project · Module · Class · Function

---

# Relationship Types

related_to · belongs_to · depends_on ·
causes · affects · supports · contradicts ·
updates · superseded_by · extends · references · mentions · contains ·
generated_by · stored_in · derived_from ·
validated_by · invalidated_by ·
tracks · implements · uses · calls · imports ·
summarizes · explains · questions · confirms

확장 가능하게 설계하되,
새 관계를 만들기 전에 기존 관계로 표현되는지 먼저 확인한다.

---

# Time / Source / Reliability / Metadata

모든 Node는 생성일 · 수정일 · 이벤트 날짜를 가진다.
모든 Node는 Source를 가진다
(FRED · ECOS · Reuters · OECD · IMF · DART · 사용자 작성 · Claude 생성 ...).
모든 Node는 신뢰도를 가진다
(Official > Research > Government > Academic > Media > Community > Opinion > AI Generated).
모든 Node는 ID · Title · Summary · Author · Created · Updated ·
Tags · Aliases · Source · Reliability · Status · Version을 가진다.

---

# Knowledge Expansion

새로운 Node는 기존 Node와 연결된다.
고립된 Node를 생성하지 않는다.

Connection Strategy (새 뉴스/데이터 유입 시) :
국가 연결 → 산업 연결 → 기업 연결 → 자산 연결
→ Regime 연결 → Journal 연결 → Recommendation 연결
→ Trigger 연결 → Presentation 연결

이 연결은 Claude가 자동으로 수행한다 (자동 링크).

---

# Memory Strategy

과거 Knowledge를 삭제하지 않는다.
새로운 버전을 추가한다. History를 보존한다.

---

# Research / Recommendation / Journal / Presentation Graph

모든 Research는
Data → Evidence → Interpretation → Regime → Recommendation → Journal
관계를 가진다.

Recommendation은 Regime · Evidence · Trigger · 성과와 연결된다.
Journal은 관련 연구 · 발표 · Recommendation · Trigger · 실패 · 성공과 연결된다.
발표자료는 Research · Journal · Evidence와 연결되고, 발표 후 피드백도 연결한다.

---

# Code Philosophy

코드는 프로그램이 아니다. Knowledge이다.
Function도 Graph의 Node이다.
Python · SQL · Shell · YAML · JSON · Markdown 모두 Node로 관리한다.

---

# AI Rule

Claude는 새로운 작업을 시작하기 전에 Graph를 탐색한다.
관련 Node를 최대한 찾는다.
Graph를 이해하지 못하면 코드를 작성하지 않는다.

---

# 운영 체크 (자동)

GRAPH_REPORT.md의 고아 노트 목록을 매주 확인하고
Claude가 연결 후보를 제안·적용한다.

중복 의심 노드(같은 지표 다른 이름)를 병합 제안한다.

god nodes(최다 연결 개념)의 변화를 주간 요약에 포함한다 —
학회의 관심이 어디로 이동하는지 보여주는 지표다.

---

# Never Do

- 파일명만으로 판단하지 않는다.
- Keyword Search만 사용하지 않는다.
- 고립된 Node를 생성하지 않는다.
- 관계 없는 Markdown을 만들지 않는다.
- 중복 Node를 생성하지 않는다.
- History를 삭제하지 않는다.

---

# Success Criteria

좋은 Graph란 Node가 많은 것이 아니다.
관계가 풍부한 Graph이다.

Claude는 항상 Graph를 먼저 이해하고
그 이후 분석 · 설계 · 구현 · 리팩토링 · 문서화를 수행한다.
