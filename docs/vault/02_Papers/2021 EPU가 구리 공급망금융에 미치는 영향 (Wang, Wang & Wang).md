---
title: Research on the Influence of Economic Policy Uncertainty on the Supply Chain Finance
type: paper
journal: 학술대회 논문 (Jiangsu University of Science & Technology) — 게재지 미확인
date: 2021
author: Li Wang · Huimin Wang · Jian Wang
created: 2026-08-05
status: done
verification: full
reliability: research
verified: 원문 대조(2026-08-05, pymupdf 6p — 초록·서론 정독. GARCH-MIDAS 추정표 개별 계수는 미대조)
source_file: Research on the Influence of Economic Policy Uncer.pdf
tags: [type/paper, domain/commodity, domain/risk, method/GARCH-MIDAS, flag/needs-review]
concepts: [구리가격, EPU, 변동성, 공급망금융, 정제구리]
related: ["[[구리 가격]]", "[[2020 6대 비철금속 국제가격 변동요인 SVAR (최혜원·허은녕·김경아)]]", "[[2018 Do global factors impact bitcoin prices - wavelet approach (Das & Kannadhasan)]]"]
---

# EPU가 구리 가격 변동성에 미치는 영향 (Wang, Wang & Wang)

> 제목은 "공급망 금융"이지만 **실제 분석 대상은 구리 가격 변동성**이다.
> 본문에 `copper`가 **73회**, `supply chain`이 37회 등장한다.

## 핵심 주장 (초록 기준)

**GARCH-MIDAS** 모형으로 **글로벌 경제정책 불확실성(EPU)이 구리 가격 변동성에 미치는 영향**을 분석하고,
그 변동성이 정제구리 수급에 어떤 변화를 만드는지 본다.

1. **EPU 상승 → 구리의 장기 변동성 확대**
2. **강한 EPU 충격발 급격한 가격 변동 → 정제구리 시장의 수요 신뢰 약화 → 공급과잉**
3. **약한 EPU 충격발 완만한 변동 → 수요 신뢰 개선 → 공급부족**

즉 **변동성의 크기에 따라 수급 방향이 뒤집힌다**는 비선형 주장이다.

## 이 vault에서의 위치

[[2020 6대 비철금속 국제가격 변동요인 SVAR (최혜원·허은녕·김경아)]]이
**"상품별 수요충격(인플레·환율·투기·재고)이 가격에 가장 큰 영향"** 이라고 했을 때,
그 잔차 성분의 **한 후보를 구체적으로 지목**한 것이 이 논문이다 — **정책 불확실성**.

[[2018 Do global factors impact bitcoin prices - wavelet approach (Das & Kannadhasan)]]도
비트코인에 대해 **EPU와 원유가의 영향이 가장 뚜렷**하다고 보고했다.
[[2026 한국의 주요 환율 변동성과 글로벌 불확실성 (이은희)]]에서는 환율 공통요인과
**미 통화정책 EPU의 상관이 0.44로 VIX(0.33)보다 강했다.**
→ **EPU가 원자재·환율·위험자산 전반의 공통 변동 요인으로 반복 등장한다.**

## 검증 필요 · 반박 포인트 (Red Team)

**① 추정표를 대조하지 않았다** — `status: captured`. 초록의 세 주장은 확인했으나
GARCH-MIDAS 계수·유의성은 미대조다. **크기를 인용하려면 표를 먼저 볼 것.**

**② "수요 신뢰(demand confidence)"의 측정 방식이 불명확**
초록만으로는 이것이 관측 변수인지 저자의 해석인지 알 수 없다.

**③ 강/약 EPU 충격의 구분 기준**
"강한 충격 → 공급과잉 / 약한 충격 → 공급부족"이라는 **부호 반전 주장**은 강한 결론이다.
임계값을 데이터로 추정했는지 사후적으로 나눴는지 확인이 필요하다.
이 vault의 반복 원칙 — **사후적으로 구간을 나누면 원하는 결과가 나온다**
([[2023 글로벌 회사채 신용위험에 대한 시장지표의 선행성 (최재용)]]의 표본 선택 편의 참조).

**④ 게재 형태 미확인**
학술대회 논문으로 보이며 저널 심사 여부를 확인하지 못했다. → `reliability: research`

## 관련 개념

[[구리 가격]] · [[지정학적 리스크]] · [[글로벌 공급망]]

## 관련 MOC

- [[지표 MOC]] · [[원문검증 논문 MOC]]
