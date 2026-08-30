---
title: 소비자신뢰지수 (CCI)
aliases: ["소비자신뢰지수", "consumer confidence", "소비자신뢰"]
type: indicator
category: 심리·서베이
created: 2026-07-27
status: linked
series_id: [UMCSENT]
data_source: fred
updated: 2026-08-05
author: Claude (02_Papers 자동 추출)
source: vault 내 논문·뷰 노트 2건에서 언급 추출
tags: [type/indicator, domain/sentiment]
---

# 소비자신뢰지수 (CCI)

> `type: indicator` — 논문(02_Papers)과 데이터(04_DataBook)가 만나는 접점 노트.
> 데이터 계열은 아래 `## 데이터` 참조.

## 데이터

- 출처 : FRED `UMCSENT` (미시간 소비자심리)
- 갱신 : 월간
- Data Book tier : 2
- 스냅샷 : `04_DataBook/` (최신) · `04_DataBook/snapshots/*.json`

> **결정 근거**: Data Book이 수집하는 소비자 심리 계열은 미시간 `UMCSENT` 하나다. 이 노트를 **미국 쪽**으로 확정했다.
> Conference Board CCI는 별개 계열이며 수집 대상이 아니다. 한국 쪽은 [[CSI (소비자심리지수)]]로 분리한다.

## 판정 규칙

*(판정 규칙 미작성 — 근거 부족)*

이 노트는 **미시간 소비자심리(`UMCSENT`)** 로 확정했다(Data Book이 수집하는 유일한 미국 소비심리 계열).
그러나 **vault에 미시간 지수를 직접 검증한 문헌이 없다.**

한국 대응 지표 [[CSI (소비자심리지수)]]에는 판정 규칙이 있다 —
**GDP 예측 회귀에서 계수가 비유의**하다는 결과다. 미국에서도 같은지는 **확인되지 않았다.**
→ **한국 결과를 미국에 그대로 옮기지 말 것.**

## 이 지표에 대해 vault가 아는 것

- [[2013 중국 경제 선행지표의 유효성에 관한 연구 (김동하)]] — 중국 CCI는 **구조적으로 신뢰도가 낮다.** 20개 도시 표본이 6.65억 도시민을 대표하지 못하고, SARS 때 6개월 만에 오판을 회복
- ⚠ 한국의 동행종합지수(CCI=Composite Coincident Index)와 **약어만 같고 전혀 다른 지표**다. 인용 시 원어 전체명을 먼저 확인할 것

## 이 지표를 다룬 노트

왼쪽 **Backlinks** 창을 볼 것 — 이 노드를 소환한 논문·뷰가 전부 잡힌다 (재편 시점 2건).
논문 쪽 `## 인과 사슬` 섹션이 링크를 만든다. 여기에 목록을 손으로 유지하지 않는다.


## 관련 MOC

- [[지표 MOC]]
