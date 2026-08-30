---
title: 선물 곡선 (Futures Curve)
type: concept
created: 2026-08-13
updated: 2026-08-25
status: mapped
aliases: [Futures Curve, Convenience Yield, 편의수익, 백워데이션, 콘탱고, contango, backwardation, Commodity financialization, Commodity Macro Transmission, Inventory channel]
tags: [type/concept, domain/commodity, domain/energy]
concepts: [contango, backwardation, convenience-yield, term-structure, roll-yield, financialization]
---

# 선물 곡선 (Futures Curve)

원자재 선물의 만기별 가격 구조. **현물가격 하나로는 안 보이는 정보가 곡선의 모양에 들어 있다.**

## 왜 이 노드가 필요한가 — 가격보다 곡선이 재고를 말한다

원자재 분석에서 반복되는 실수는 **현물가격만 보는 것**이다. 곡선의 기울기가 담는 정보는 다르다.

| 곡선 형태 | 조건 | 읽는 법 |
|---|---|---|
| **백워데이션** (근월 > 원월) | 재고 부족, 편의수익 ↑ | **현물 수급 타이트.** 지금 손에 쥐는 것에 프리미엄 |
| **콘탱고** (근월 < 원월) | 재고 풍부, 보관비용 지배 | 현물 여유. 깊은 콘탱고는 저장능력 한계 신호 |

**편의수익(convenience yield)** 이 이 구조를 만든다 — 현물을 보유하면 생산 중단을 피할 수 있다는 옵션 가치이며, 재고가 낮을수록 커진다. 즉 **곡선의 기울기는 관측되지 않는 재고 타이트니스의 대리지표**다.

## 거시로 올릴 때의 주의

**가격 수준과 곡선 형태는 다른 것을 잰다.**

[[구리 가격]]이 오르는 국면에서도 곡선이 콘탱고면 그 상승은 현물 부족이 아니라 **금융 수요·기대**일 수 있다. 이 볼트가 반복 확인해온 논점과 직접 이어진다 —
[[Dr. Copper는 급락기에만 경기를 말한다]]는 구리 가격의 지배 성분이 경기가 아니라 인플레·환율·투기·재고임을 보였다. **곡선은 그 성분을 분리하는 도구**다.

**금융화(financialization)** — 지수 투자자 유입 이후 곡선이 수급이 아니라 자금흐름을 반영하는 구간이 생겼다는 문헌이 있다. 곡선을 재고 신호로 읽을 때 이 오염을 함께 고려한다.

### 금융화 논쟁 — **결론이 나지 않았다**

이 노드가 "문헌이 있다"고만 적어두었던 자리를 채운다(2026-08-15). **양쪽이 팽팽하고, 볼트는 판정하지 않는다.**

| 입장 | 논문 | 근거 |
|---|---|---|
| **자금이 움직였다** | [[2012 Index Investment and the Financialization of Commodities (Tang & Xiong)]] | 지수 편입 상품끼리 **상관이 올랐다** — 펀더멘털로 설명 안 됨 |
| " | [[2014 Investor Flows and the 2008 Boom-Bust in Oil Prices (Singleton)]] | 2008년 유가에서 **자금흐름이 수익을 예측** |
| **증거가 없다** | [[2015 Effects of Index-Fund Investing on Commodity Futures Prices (Hamilton & Wu)]] | 위험프리미엄 경로 검정 — 농산물 예측력 없음, 유가는 **표본 외에서 붕괴** |
| " | [[2016 The Simple Economics of Commodity Price Speculation (Knittel & Pindyck)]] | 투기로 올랐으면 **재고에 흔적**이 남아야 한다 |

**읽는 순서** — 자금이 왜 들어왔는지([[2006 Facts and Fantasies about Commodity Futures (Gorton & Rouwenhorst)]])
→ 어떻게 굴렸는지([[2006 The Strategic and Tactical Value of Commodity Futures (Erb & Harvey)]])
→ 무슨 일이 생겼는지(위 논쟁 4편).

> **실무 규칙 셋**
> **①** "투기 때문"이라고 말하려면 **어떤 경로인지** 밝힌다 — 상관 구조인가, 위험프리미엄인가, 현물 재고인가.
> 경로마다 증거가 다르고, Hamilton–Wu가 기각한 것은 **위험프리미엄 경로뿐**이다.
> **②** 재고를 먼저 본다([[원자재 재고]]). Knittel–Pindyck의 회계 제약이 가장 빠른 점검이다.
> **③** [[2006 Facts and Fantasies about Commodity Futures (Gorton & Rouwenhorst)]]의 표본은 **2004년까지**다.
> 금융화 이전 데이터로 금융화를 정당화한 문헌이므로 **분산 효과를 현재형으로 인용하면 안 된다.**

### 곡선을 재고 대용으로 쓸 때 — 상품별로 신뢰도가 다르다

[[1993 The Present Value Model of Rational Commodity Pricing (Pindyck)]]이 편의수익을
**현물–선물 가격에서 직접 측정**할 수 있음을 보인 논문이다. 다만 상품 4종 검정 결과가 갈렸다 —
**난방유는 모형에 부합하고 구리·목재·금은 부합하지 않는다.**

→ **에너지에서는 곡선을 재고 신호로 써도 되지만 [[구리 가격]]에서는 조심한다.**
[[Dr. Copper는 급락기에만 경기를 말한다]]가 관측으로 말한 것과 같은 방향이다.

비대칭의 근거는 [[1992 On the Behaviour of Commodity Prices (Deaton & Laroque)]]에 있다 —
**시장 전체가 음(-)의 재고를 가질 수 없어서** 가격이 아래로는 눌리고 위로는 열린다.
**원자재 시나리오를 대칭으로 잡으면 상방을 과소평가한다.**

## 인과 사슬

재고 ↓ → 편의수익 ↑ → **선물 곡선 백워데이션** → 롤수익(+) → 지수 투자 유입
→ (금융화 경로) 곡선이 수급과 분리될 수 있음

[[글로벌 공급망]] 병목 → 현물 확보 경쟁 → 백워데이션 심화 → [[구리 가격]]·[[WTI (국제유가)]] 현물 프리미엄

## 실측 프런트 스프레드 (2026-08-25 추가)

2개월물 − 근월물 월평균. **+ = 콘탱고 / − = 백워데이션.**
2008~2020-04은 월 +0.50(연 약 9%)를 **12년간 매달** 냈고, 2021년에 부호가 뒤집혀 현재까지 유지 중이다.
전체 표와 해석: [[2026-08-25_원유-선물곡선-캐리-대담]]
판정 장치: [[선물 곡선의 부호가 레짐을 말한다 — 백워데이션 지속은 공급 비탄력의 가격이다]] ·
[[원자재 ETF의 성과를 정하는 건 가격 방향이 아니라 롤 캐리다]]

⚠ 수치 출처는 STT 전사본의 화자 자체 집계다. **CME WTI 선물로 재현 전까지 ③ 수치 층위 인용 금지.**

## 관측

- LME/COMEX 구리 선물 기간구조(cash-3M 스프레드)
- WTI 1개월-12개월 스프레드
- 재고: LME·SHFE·COMEX 창고 재고

## 관련 노드

[[구리 가격]] · [[WTI (국제유가)]] · [[글로벌 공급망]] · [[에너지 전환]] · [[VIX]]

## 관련 MOC

- [[지표 MOC]] · [[Library MOC]]
