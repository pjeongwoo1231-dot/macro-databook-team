---
title: M2 · Divisia 통화량
aliases: ["M2", "통화량", "Divisia", "Divisia 통화량", "광의통화"]
type: indicator
category: 유동성
created: 2026-07-27
status: linked
series_id: [M2SL]
data_source: fred+ecos
updated: 2026-08-05
author: Claude (02_Papers 자동 추출)
source: vault 내 논문·뷰 노트 8건에서 언급 추출
tags: [type/indicator, domain/liquidity]
---

# M2 · Divisia 통화량

> `type: indicator` — 논문(02_Papers)과 데이터(04_DataBook)가 만나는 접점 노트.
> 데이터 계열은 Data Book(`indicators.yaml`)의 정의와 연결돼 있다 — 아래 `## 데이터` 참조.

## 데이터

- 출처 : FRED `M2SL` (미, **단순합산**) · ECOS `161Y006/BBHA00` (한국 M2)
- 갱신 : 월간
- Data Book tier : 1
- 스냅샷 : `04_DataBook/` (최신) · `04_DataBook/snapshots/*.json`

> ⚠ `M2SL`은 **단순합산(simple-sum) M2**다. 이 노트 제목의 **Divisia 통화량은 별도 계열**(세인트루이스 연은 MSI/CFS Divisia)이며 아직 수집 대상이 아니다.

## 판정 규칙

**집계 방식을 밝히지 않은 "유동성" 판단은 무효**

- [[2019 On the Monetary Measures of Global Liquidity (Hashmi & Bhatti)]] — 이론 기반(Divisia·Currency Equivalent)과 비이론 기반(단순합산) 집계는 **서로 다른 동학**을 보인다
- 이 노트가 연결한 `M2SL`은 **단순합산**이다. Divisia가 아니다

**금지** : `M2SL` 증가율 하나로 "유동성이 풀렸다/조였다"를 판정하는 것

**같이 볼 것** : **순유동성**(Fed B/S `WALCL` − RRP `RRPONTSYD` − TGA `WTREGEN`)이 단기 시장 유동성에는 더 직접적이다. M2는 느리다.

## 이 지표에 대해 vault가 아는 것

- [[2019 On the Monetary Measures of Global Liquidity (Hashmi & Bhatti)]] — 글로벌 통화량 집계 5가지 비교. **이론 기반(Divisia·Currency Equivalent)이 비이론 기반(단순합·GDP가중·PCA)을 압도.** 단 모든 측정치 상관 0.85+
- [[2025 스테이블코인 규제 방안 - 금융안정·지급결제·통화정책 (권태율)]] — 스테이블코인은 **통화지표 밖에서 만들어지는 유동성**. "무엇을 통화로 셀 것인가"의 다음 질문

## 이 지표를 다룬 노트

왼쪽 **Backlinks** 창을 볼 것 — 이 노드를 소환한 논문·뷰가 전부 잡힌다 (재편 시점 8건).
논문 쪽 `## 인과 사슬` 섹션이 링크를 만든다. 여기에 목록을 손으로 유지하지 않는다.


## 관련 MOC

- [[지표 MOC]]
