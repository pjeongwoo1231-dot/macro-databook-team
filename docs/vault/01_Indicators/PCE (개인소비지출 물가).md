---
title: PCE (개인소비지출 물가)
aliases: ["PCE", "개인소비지출 물가", "PCE 물가", "코어 PCE"]
type: indicator
category: 물가
created: 2026-07-27
status: linked
series_id: [PCEPI, PCEPILFE]
data_source: fred
updated: 2026-08-05
author: Claude (02_Papers 자동 추출)
source: vault 내 논문·뷰 노트 4건에서 언급 추출
tags: [type/indicator, domain/inflation]
---

# PCE (개인소비지출 물가)

> `type: indicator` — 논문(02_Papers)과 데이터(04_DataBook)가 만나는 접점 노트.
> 데이터 계열은 Data Book(`indicators.yaml`)의 정의와 연결돼 있다 — 아래 `## 데이터` 참조.

## 데이터

- 출처 : FRED `PCEPI` (헤드라인) · `PCEPILFE` (코어)
- 갱신 : 월간
- Data Book tier : 1
- 스냅샷 : `04_DataBook/` (최신) · `04_DataBook/snapshots/*.json`

## 판정 규칙

**Core PCE로 잰 필립스 곡선은 순진한 예측보다 못하다**

[[Core PCE로 잰 필립스 곡선은 1995년 이후 순진한 예측보다 못하다]] — [[2022 Advances in estimating the Phillips curve (Guirguis & Suen)]] 기준

| 물가 지표 | 표본내 R²_adj | 표본외 **Theil U** | 실업갭 |
|---|---|---|---|
| **Core PCE** | 0.132 | **1.244~1.329** | 6개 사양 **전부 비유의** |
| UIG | 0.946 | 0.066~0.071 | 대부분 유의 |
| CPIM | 0.610 | 0.306~0.341 | 가장 가파름 |

**Theil U > 1은 순진한 벤치마크보다 못하다는 뜻**이다.

**기대인플레 계수마저 지표에 따라 뒤집힌다** — Core PCE 0.081(비유의) / UIG −0.018(음, 비유의) / **CPIM 0.408\*\*\***.
→ **"기대가 물가를 만든다"는 명제조차 어떤 물가를 재느냐에 조건부다.**

**금지** : Core PCE 하나로 "필립스 곡선이 평탄해졌다"고 결론짓는 것 — **곡선이 아니라 지표의 성질**일 수 있다

**연준 관점에서는 여전히 공식 지표**다. **정책 반응함수를 볼 때와 물가-슬랙 관계를 볼 때 쓰는 지표가 달라야 한다.**

## 이 지표를 다룬 노트

왼쪽 **Backlinks** 창을 볼 것 — 이 노드를 소환한 논문·뷰가 전부 잡힌다 (재편 시점 4건).
논문 쪽 `## 인과 사슬` 섹션이 링크를 만든다. 여기에 목록을 손으로 유지하지 않는다.


## 관련 MOC

- [[지표 MOC]]
