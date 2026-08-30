---
title: "Time-Varying Effects of Oil Supply Shocks on the US Economy"
type: paper
journal: American Economic Journal: Macroeconomics 5(4), 1–28 (2013)
date: 2013
author: Christiane Baumeister (Bank of Canada) · Gert Peersman (Ghent University)
url: https://doi.org/10.1257/mac.5.4.1
tags: [type/paper, method/TVP-VAR, method/부호제약, domain/commodities, domain/inflation]
concepts: [수요탄력성, 시변계수, 부호제약, 분산분해, 공급충격]
status: done
verification: full
reliability: academic
text_basis: human-fulltext
verified: "✔ 전문 판독(2026-08-18). 저자 페이지 공개본 PDF(users.ugent.be BP1_AEJ.pdf)에서 초록·본문·분산분해·결론 직접 확인. 서지는 AEA 페이지와 대조."
promoted_from: "[[L219 The Role of Time-Varying Oil Supply Shocks in Causing U.S. Macroeconomic Fluctuations]]"
related: ["[[2009 Causes and Consequences of the Oil Shock of 2007-08 (Hamilton)]]", "[[2009 Not All Oil Price Shocks Are Alike (Kilian)]]", "[[1996 This Is What Happened to the Oil Price-Macroeconomy Relationship (Hamilton)]]", "[[WTI (국제유가)]]", "[[RegimeView 1.0 (2026-08-09)]]"]
---

# 같은 공급 차질이 시간이 갈수록 더 큰 가격 반응을 만든다 — 수요곡선이 가팔라졌기 때문이다 (Baumeister & Peersman, 2013)

> AEJ: Macroeconomics 5(4) 1–28. 1974~2010 시변모수 구조VAR(부호제약).
> **전문 판독 완료** — 수치 인용 가능.

⚠ **서지 정정**: 05_Library의 제목 *"The Role of Time-Varying Oil Supply Shocks in Causing U.S. Macroeconomic Fluctuations"* 는
**존재하지 않는 제목**이다. 실제 제목은 위와 같고, 잘못된 제목은 같은 저자의 **다른 논문**
(*The Role of Time-Varying Price Elasticities…*, JAE 28(7) 1087–1109)과 **뒤섞인 형태**다.
URL은 옳았다 — **URL이 맞아도 제목이 틀릴 수 있다.**

## 왜 중요한가 — 우리 문제와 직결

[[WTI (국제유가)]] 노드는 "왜 올랐나를 먼저 붙인다"는 규칙을 갖고 있다.
이 논문은 그 규칙에 **시간 축**을 더한다 — **같은 종류의 충격이라도 시대에 따라 가격·실물 반응이 다르다.**

지금 국면과 정면으로 닿는다. 2026년은 전쟁발 공급 제약 국면이고, 한국 CPI는 석유류가 끌고 있다
([[핵심인플레이션]] · [[CPI (소비자물가지수)]]). 이 논문이 맞다면 **과거 공급충격의 계수로 지금을 추정하면 과소평가**한다.

## 문제의식

기존 연구는 모두 **시불변 회귀**였다. 공급충격의 효과가 40년간 같다고 가정한 것이다.
그런데 유가–거시 관계가 불안정하다는 증거는 이미 많았다(Edelstein-Kilian 2009, Blanchard-Galí 2010 등).
저자들의 질문: **불안정성이 "충격 구성의 변화" 때문인가, 아니면 "같은 충격에 대한 반응 자체의 변화" 때문인가.**

## 방법론

- **시변모수 구조VAR(TVP-VAR)** + 확률적 변동성. 임의의 표본 분할을 하지 않고 계수가 연속적으로 변하게 둔다
- 식별은 **동시적 배제제약이 아니라 부호제약** — "공급충격은 유가와 원유생산을 **반대 방향**으로 움직인다".
  세계 원유시장 VAR에 부호제약을 적용한 **최초** 사례라고 저자들이 밝힌다
- 파생 산물: **단기 원유수요의 가격탄력성**을 시점별로 추정한다(충격 시 생산 반응 ÷ 가격 반응)

## 핵심 결과

**① 탄력성이 무너졌다 — −0.6 → −0.1**

> "the average value of the price elasticity is around −0.6 in the early part of the sample …
> that elasticity declines considerably starting in the mid-1980s, and reaches **a low of −0.1** toward the end of the sample."

같은 생산 차질이 **훨씬 큰 가격 상승**으로 이어진다는 뜻이다.

**② 두 방향의 "정규화"가 반대 결론을 준다** — 이 논문의 핵심 구분

| 충격을 무엇으로 고정하나 | 미 GDP 반응의 시간 추이 |
|---|---|
| **생산 1% 감소**로 고정 | **커졌다** |
| **실질유가 10% 상승**으로 고정 | **작아졌다** |

→ "유가 충격의 효과가 약해졌다"와 "공급 차질의 효과가 세졌다"가 **동시에 참**이다.
차이를 만드는 것이 ①의 탄력성이다. **어느 쪽으로 정규화했는지 밝히지 않은 문장은 해석할 수 없다.**

**③ 분산분해 — 공급충격은 유가의 주역이 아니다**

| 대상 | 전반부 | 후반부 |
|---|---|---|
| 실질유가 변동 기여 | 30~35% | **20~25%** |
| 세계 원유생산 변동 기여 | 25~35% | ~30% |
| **미 GDP 성장·CPI 인플레 분산 기여** | **15~20%** | **15~20%(꾸준)** |

CPI 쪽 기여는 **2000년대 초 이후 점진적으로 상승**했다.

**④ 역사적 분해 — 공급충격이 실물에 확실히 걸린 건 두 번뿐**

> "oil supply disruptions mattered for real economic activity mainly during two episodes.
> They contributed to the **1991 recession** and they **slowed the ongoing boom at the end of the millennium**."

1980년대 초·2001·2008 침체는 공급충격으로 설명되지 않고, **1970년대 Great Inflation도 설명하지 못한다.**

## 저자가 밝힌 한계

- 탄력성 하락의 원인(오일집약도 하락·수송 비중 상승·신흥국 비중 상승·연료보조금)은 **논문이 검정한 것이 아니라 §III에서 제시한 해석**이다
- 부호제약은 집합 식별이라 개별 충격의 크기를 점추정으로 못 준다. Fry-Pagan(2011) 비판이 그대로 적용된다
- 표본이 1974년 시작이라 1973년 1차 오일쇼크가 **표본 밖**이다

## 우리 시스템에 적용

1. **[[WTI (국제유가)]]의 실무규칙에 "언제의 계수인가"를 추가한다.** 1980년대 추정치로 지금을 재면 **가격 반응은 과소, GDP 반응은 과대**로 틀린다
2. **공급충격 국면의 물가 전이는 커졌다** — CPI 분산 기여가 2000년대 이후 상승했다는 ③은
   현재 한국·미국 물가가 유가에 민감한 것과 정합적이다 → [[핵심인플레이션]] 물가 축 해석에 사용
3. **"유가가 올랐는데 침체가 안 왔다"를 레짐 변화의 증거로 쓰지 않는다** — ②에 따르면 정규화 차이일 수 있다
4. ④는 **경고**다. 공급충격은 물가를 움직이지만 **침체를 부르는 힘은 생각보다 약하다** →
   [[RegimeView 1.0 (2026-08-09)]] 성장 축에 유가를 직접 넣지 않는 현 설계와 일치한다

## Red Team

1. **탄력성 −0.1은 모형이 만든 값이다.** 부호제약 집합식별에서 impact ratio로 유도한 것이라
   식별 가정이 바뀌면 값이 달라진다. **"현재 원유 수요탄력성은 −0.1"이라고 단정 인용하면 안 된다** — 이 모형 안에서의 값이다
2. **③의 15~20%는 20분기 지평 값이다.** 단기(1~4분기) 기여는 다를 수 있고, 논문은 그 표를 전면에 두지 않는다
3. **④는 "공급충격만"의 기여다.** Kilian식 분해에서 수요충격으로 잡히는 부분이 실제로는 공급 우려(예비적 수요)일 수 있다 →
   [[2009 The Impact of Oil Price Shocks on the U.S. Stock Market (Kilian & Park)]]의 3분해와 함께 읽어야 한다
4. **표본이 2010년 전후에서 끝난다.** 셰일 혁명 이후 미국이 순수출국이 된 구조 변화가 빠져 있다.
   **지금 국면에 그대로 외삽하면 안 된다** — 저자들의 논리(구조는 계속 변한다)가 이 논문 자신에게도 적용된다

## 인과 사슬

```
오일집약도↓ · 수송 비중↑ · 신흥국 비중↑ · 연료보조금
        ↓
단기 원유수요 가격탄력성 **−0.6 → −0.1** (수요곡선이 가팔라짐)
        ↓
같은 생산 차질(−1%) → **더 큰 유가 상승**
        ↓
   ┌─ 가격 기준 정규화 시: 미 GDP 반응 **축소**
   └─ 수량 기준 정규화 시: 미 GDP·물가 반응 **확대**
        ↓
분산 기여: 실질유가 30~35% → 20~25% / 미 GDP·CPI 15~20%
        ↓
침체 설명력은 제한적 (1991 · 1990년대 말 두 번)
```

## Comment

이 논문의 진짜 기여는 탄력성 숫자가 아니라 **"충격을 무엇으로 고정해 말하는가"를 분리한 것**이다.
같은 데이터에서 상반된 두 문장이 모두 참일 수 있다는 걸 보여줬고, 그것이 유가–거시 문헌의 오랜 혼선을 정리한다.

우리 볼트에는 같은 유형의 교훈이 이미 있다 — [[1996 This Is What Happened to the Oil Price-Macroeconomy Relationship (Hamilton)]]의
"관계가 사라진 게 아니라 변수 정의가 틀렸다". **1996년은 변수 정의, 2013년은 정규화 기준.** 둘 다 측정의 문제였다.

## 관련 노트

- [[2009 Causes and Consequences of the Oil Shock of 2007-08 (Hamilton)]] — 같은 탄력성 붕괴를 사건 분석으로 보여준다
- [[2015 Speculation in the Oil Market (Juvenal & Petrella)]] — 남은 변동을 금융 수요가 설명하는지
- [[WTI (국제유가)]] · [[핵심인플레이션]] · [[Library MOC]]
