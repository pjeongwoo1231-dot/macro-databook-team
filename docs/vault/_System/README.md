---
title: Vault 사용법
type: system
created: 2026-07-18
status: working
author: Claude
source: Claude 생성
tags: [system]
related: ["[[CLAUDE.md]]", "[[OBSIDIAN.md]]", "[[GRAPHIFY.md]]"]
---

# MacroVault 사용법

이 Vault는 매크로 학회의 장기 기억이다.
규칙 전문은 루트의 CLAUDE.md와 docs/ 4개 문서에 있다.

## 세션 프로토콜 (Claude Code)

1. 세션 시작 : `graphify-out/GRAPH_REPORT.md`를 먼저 읽는다.
2. 작업 전 : 관련 노드를 graph에서 탐색한다 (파일 grep보다 먼저).
3. 노트 생성 : Templates 양식 + YAML + 내부 링크 3개 이상.
4. 세션 종료 : `/graphify .` 재실행으로 그래프를 갱신한다.

## 매주 흐름

DataKit 자동 갱신 → AI 해석(03_Research) → 체화 노트 →
Hermes 검증(새 세션) → Final → 세션 발표 → 레짐 뷰 갱신 →
매매일지(02_Journal) → graphify 재빌드.

## 양식 위치

00_System/Templates/ — DataKit · Interpretation · Embodiment ·
Final · RegimeView · Journal · Recommendation · Tracker
