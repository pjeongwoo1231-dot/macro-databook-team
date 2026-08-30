---
title: CPI (소비자물가지수)
aliases: ["CPI", "소비자물가지수", "미국 CPI", "한국 CPI", "소비자물가", "인플레이션", "물가상승률"]
type: indicator
category: 물가
created: 2026-07-27
status: linked
series_id: [CPIAUCSL, CPILFESL]
data_source: fred
updated: 2026-08-05
author: Claude (02_Papers 자동 추출)
source: vault 내 논문·뷰 노트 19건에서 언급 추출
tags: [type/indicator, domain/inflation]
---

# CPI (소비자물가지수)

> `type: indicator` — 논문(02_Papers)과 데이터(04_DataBook)가 만나는 접점 노트.
> 데이터 계열은 Data Book(`indicators.yaml`)의 정의와 연결돼 있다 — 아래 `## 데이터` 참조.

## 데이터

- 출처 : FRED `CPIAUCSL` (헤드라인) · `CPILFESL` (코어)
- 갱신 : 월간
- Data Book tier : 1
- 스냅샷 : `04_DataBook/` (최신) · `04_DataBook/snapshots/*.json`

## 판정 규칙

**한국 인플레 동학을 볼 때 CPI는 이론적으로 정합적이지 않다**

[[2014 NKPC Closed Form - Korean Manufacturing (Bae, Hong, Kang & Yoon)]] — 한국 제조업 하이브리드 NKPC를 CPI와 PPI로 각각 추정했다.
- **CPI 기준으로는 한계비용 기울기 λ가 비내구재(0.0513)·내구재(0.0089) 모두 비유의**
- **PPI 기준으로는 3개 산업 모두 유의**하고 부호도 이론과 부합
- 축약형 정합성 검증(6개 조합)에서 **오직 "제조업 + PPI"만** 이론적 관계를 만족

**한국에서 CPI가 유효한 곳** : [[2023 Dissipation of Relation between Inflation and Business Cycles in Korea (Huh In)]]에서 **GDP갭 × CPI는 유의**(R² 0.125)했다.
반면 **GDP 디플레이터는 CPI와 상관 0.19로 무관**하며 어떤 경기 지표와도 유의하지 않다.
→ **한국 물가 3종은 서로 대체 가능하지 않다.**

**금지**
- CPI로 필립스 곡선·NKPC를 추정하고 "이론과 다르다"고 결론짓는 것 → **지표 선택의 문제**일 수 있다
- CPI와 GDP 디플레이터를 같은 "물가"로 묶는 것

**교차 확인** : [[핵심인플레이션]]의 판정 기준 3가지(공적분·슬랙 관계·Theil U)를 함께 볼 것.


### 디플레이터와의 괴리 *(2026-08-21 제텔 연결)*

[[CPI와 GDP 디플레이터의 괴리가 수입물가의 크기다]] —
두 지표의 차이는 오차가 아니라 **수입물가 성분**이다.

**규칙에 더하는 것**: CPI와 디플레이터가 벌어질 때 *"통계가 안 맞는다"* 로 쓰지 않는다.
**교역조건 변화의 크기**로 읽는다.

## 이 지표를 다룬 노트

왼쪽 **Backlinks** 창을 볼 것 — 이 노드를 소환한 논문·뷰가 전부 잡힌다 (재편 시점 19건).
논문 쪽 `## 인과 사슬` 섹션이 링크를 만든다. 여기에 목록을 손으로 유지하지 않는다.


## 관련 MOC

- [[지표 MOC]]
