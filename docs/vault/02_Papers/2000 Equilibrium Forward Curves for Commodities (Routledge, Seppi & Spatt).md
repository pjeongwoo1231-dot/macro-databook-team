---
title: "Equilibrium Forward Curves for Commodities"
type: paper
journal: The Journal of Finance 55(3), 1297–1338 (2000-06)
date: 2000
author: Bryan R. Routledge, Duane J. Seppi, Chester S. Spatt
doi: 10.1111/0022-1082.00248
url: https://doi.org/10.1111/0022-1082.00248
tags: [type/paper, domain/commodities, domain/derivatives, method/equilibrium-model]
concepts: [선물 기간구조, 재고 비음 제약, 내재된 타이밍 옵션, 새뮤얼슨 효과, 편의수익]
status: done
verification: full
reliability: academic
text_basis: full-text
verified: "✅ 2026-08-31 무료 사본 **전문 판독**(102,076자). 실제제목 대조 100% 일치. 서지 Crossref 확정(JF 55(3) 1297–1338, 2000-06)"
promoted_from: "[[Library MOC]]"
related: ["[[Library MOC]]", "[[1996 Competitive Storage and Commodity Price Dynamics (Deaton & Laroque)]]", "[[2014 Effects of Speculation and Interest Rates in a Carry Trade Model of Commodity Prices (Frankel)]]", "[[2014 The Role of Inventories and Speculative Trading in the Global Market for Crude Oil (Kilian & Murphy)]]", "[[선물 곡선 (Futures Curve)]]"]
---

# 선물곡선을 읽는 이론 (Routledge, Seppi & Spatt, 2000)

> *Journal of Finance* 55(3). 저장 가능 원자재의 **선물가격 기간구조**를 균형모형으로 도출한다.
> 우리 볼트에 [[선물 곡선 (Futures Curve)]] 지표 노드가 있는데 **그것을 해석할 이론이 없었다.**

## 핵심 메커니즘

> **재고에 **비음 제약**(재고는 음수가 될 수 없다)이 있기 때문에,
> 현물 원자재에는 선물계약에는 없는 **내재된 타이밍 옵션**이 붙는다.**

그 옵션의 가치는 두 가지로 변한다 — **내생적인 재고 수준**과 **외생적인 일시적 수급 충격**.

이게 편의수익(convenience yield)을 가정이 아니라 **모형에서 도출**한 것이다.
"재고가 바닥이면 현물이 프리미엄을 갖는다"가 왜 그런지를 옵션 가치로 설명한다.

## ★ 새뮤얼슨 효과의 조건부 위배

새뮤얼슨 효과 = **만기가 가까운 선물이 먼 선물보다 변동성이 크다**는 통념.

> **이 모형은 서로 다른 만기의 선물가격 변동성에 대해 예측을 내놓고,
> 새뮤얼슨 효과의 **조건부 위배**가 어떻게 발생하는지 보인다.**

즉 **재고 상태에 따라 통념이 뒤집힌다.** 저자들은 영구적 2번째 요인을 넣어 확장하고
**원유 선물 데이터로 캘리브레이션**한다.

## 우리 볼트에 쓰는 법

**선물곡선을 근거로 쓰는 방식이 바뀐다.**

- 우리는 콘탱고/백워데이션을 **수급 신호**로 읽어 왔다. 이 모형에 따르면
  곡선 모양은 **재고 수준 × 타이밍 옵션 가치**의 함수다
  → **"백워데이션이니 공급이 타이트하다"는 추론은 재고 수준을 명시해야 성립한다**
- **채점 규칙 23 후보: 선물곡선 형태를 근거로 든 claim은 동시점 재고 수준을 evidence에 함께 적는다.**
  우리 DataBook에 미국 원유재고(`us_crude_stocks`)가 있으므로 바로 실행 가능하다
- **만기별 변동성 통념(새뮤얼슨)을 무조건 적용하지 않는다** — 조건부로 뒤집힌다

## 원자재 이론 4편이 이제 하나로 이어진다

| 논문 | 층위 |
|---|---|
| [[1996 Competitive Storage and Commodity Price Dynamics (Deaton & Laroque)]] | 저장의 **기준선과 그 실패** |
| **이 논문 (2000)** | 저장 제약 → **선물곡선 형태**와 변동성 구조 |
| [[2014 Effects of Speculation and Interest Rates in a Carry Trade Model of Commodity Prices (Frankel)]] | 저장 결정에 **금리** |
| [[2014 The Role of Inventories and Speculative Trading in the Global Market for Crude Oil (Kilian & Murphy)]] | 재고를 **기대 식별 도구**로 |

## Red Team

1. **균형 이론 모형**이다. 캘리브레이션은 원유 한 품목이며, 추정된 실증 결과가 아니다.
2. **2000년 논문**으로 원자재 금융화(2004~) 이전이다.
   [[2014 The Financialization of Commodity Markets (Cheng & Xiong)]]이 다룬 지수투자·마진 채널이 없다.
3. 재고 비음 제약이 핵심 동력이므로, **저장이 사실상 무제한인 국면**(대규모 여유 저장능력)에서는
   메커니즘이 약해진다.
4. 전기·운임처럼 **저장 불가 상품에는 적용되지 않는다.**
