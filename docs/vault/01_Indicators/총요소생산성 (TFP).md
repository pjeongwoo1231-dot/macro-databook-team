---
title: 총요소생산성 (TFP)
type: concept
created: 2026-08-12
updated: 2026-08-12
status: mapped
aliases: [TFP, 솔로우 잔차, Solow residual, 기술충격, technology shock, A(t)]
tags: [type/concept, domain/growth]
concepts: [growth-accounting, Solow-residual, labor-augmenting, Hicks-neutral]
---

# 총요소생산성 (TFP)

생산함수 `Y = A · F(K, L)` 에서 **자본과 노동으로 설명되지 않는 잔차 A**.
성장회계에서는 `Δlog A = Δlog Y − θ_L·Δlog L − θ_K·Δlog K` 로 측정되며, 이 정의 때문에 **솔로우 잔차(Solow residual)** 라고도 부른다.

## 왜 이 노드가 매크로 분석에서 중요한가

TFP는 **같은 계열이 두 문헌에서 정반대 지위**를 갖는다.

- **성장론에서 TFP는 "설명되지 않은 것"** — [[1956 A Contribution to the Theory of Economic Growth (Solow)]]에서 장기 1인당 성장률은 전적으로 외생 A(t)가 결정한다. 즉 성장 이론의 결론이 "우리가 모르는 것이 전부를 설명한다"였고, 이것이 [[1986 Increasing Returns and Long-Run Growth (Romer)]] · [[1988 On the Mechanics of Economic Development (Lucas)]] · [[1990 Endogenous Technological Change (Romer)]]가 A를 내생화하려 한 동기다.
- **경기변동론에서 TFP는 "충격 그 자체"** — [[1986 Theory Ahead of Business Cycle Measurement (Prescott)]]는 같은 잔차의 **분기 변동**을 실물 기술충격으로 읽고, 그 분산만으로 경기변동 대부분을 설명한다.

**같은 잔차를 성장론은 무지의 표시로, RBC는 관측된 충격으로 쓴다.** 이 이중성이 TFP 해석의 첫 번째 함정이다.

> ⚠ **원문 미대조**(`verification: none`) — 위 [[1986 Increasing Returns and Long-Run Growth (Romer)]]는
> [[원문검증 논문 MOC]] 「인용 규칙 개정」의 **① 명제 층위**로만 인용한다(내생적 성장의 *동기*).
> **수확체증 파라미터·성장률 계수는 쓰지 않는다.** 같은 문단의 Solow(1956)·Prescott(1986)·Romer(1990)은
> `verification: full`이라 수치 인용이 열려 있다 — **한 문단 안에서 층위가 다르다는 점에 주의.**
> *(2026-08-21 명제 연결)*

## 측정상의 함정 (실무)

1. **가동률 오염** — 자본서비스가 아니라 자본스톡을 쓰면 불황기에 놀리는 설비가 A의 하락으로 잡힌다. → [[설비가동률]] 보정 없는 TFP는 경기순응적으로 과대측정된다.
2. **노동의 질** — 인적자본 가중을 하지 않으면 [[인적자본]] 축적이 A로 흡수된다.
3. **교역조건** — Prescott(1986)은 유가 상승을 **음(−)의 기술충격**으로 명시적으로 취급한다. 즉 TFP 충격에는 [[WTI (국제유가)]]·[[무역분쟁·관세]] 같은 순수 기술이 아닌 것이 섞인다.
4. **마크업** — 불완전경쟁 하에서는 성장회계의 요소몫이 탄력성과 다르므로 잔차가 편의를 갖는다.

## 관측 대리지표

- 미국: BLS Total Factor Productivity(연간), Fernald(SF Fed) 가동률조정 TFP(분기)
- 한국: 한국은행 산업별 총요소생산성, KDI 잠재성장률 추계의 TFP 기여도
- 실무 근사: [[산업생산]] ÷ (가중 노동투입) — 단기 신호용

## 관련 노드

[[잠재성장률]] · [[GDP 성장률]] · [[산출갭]] · [[인적자본]] · [[설비가동률]] · [[경기침체]]


> **1차 문헌이 더 필요하면** → [[1차 문헌 찾기 (아카이브 진입로)]] · BIS 주제 `labour-growth-and-productivity`
> (개별 카탈로그를 여기 걸지 않는다 — 다리 하나만 부른다)

## 관련 MOC

- [[지표 MOC]] · [[매크로 고전 논문 MOC]]

## '생산성'은 하나가 아니다 (2026-08-14)

**DataBook이 이제 Fernald 분기 TFP를 수집한다.** 네 계열이 서로 다른 것을 잰다.

| 계열 | 뜻 | 2026 상반기 |
|---|---|---:|
| `dLP` | 노동생산성 — **자본심화만으로도 오른다** | **+0.64%** |
| `dk` | 자본투입 | **+3.04%** |
| `dtfp` | TFP(솔로우 잔차) | **−0.08%** |
| `dtfp_util` | **가동률조정 TFP** — 기술에 가장 가까움 | **−2.16%** |

**부호까지 갈린다.** 노동생산성은 오르는데 기술은 안 좋아지고 있다.

### 읽는 순서

1. [[1957 Technical Change and the Aggregate Production Function (Solow)]] — 잔차 개념의 원전.
   **잔차는 측정된 것이 아니라 남은 것**이라 측정오차·가동률·규모수익이 전부 섞인다
2. [[2006 Are Technology Improvements Contractionary (Basu, Fernald & Kimball)]] — 그 성분을 걷어내는 방법.
   그리고 **기술이 좋아지면 단기엔 투입이 줄어든다**(답: Yes)
3. [[2014 A Quarterly, Utilization-Adjusted Series on Total Factor Productivity (Fernald)]] — 그 방법의 분기 구현체.
   DataBook이 받는 계열

> **실무 규칙**: 노트에 "생산성"이라고 쓸 때 **어느 계열인지 명시**할 것.
> BLS 비농업 노동생산성 ≠ Fernald `dLP` ≠ `dtfp` ≠ `dtfp_util`.
> [[RegimeView 1.0 (2026-08-09)]] 9차 개정이 이 구분으로 ②를 재검토한 사례다.

## 왜 낮은가 — 원인 문헌 (2026-08-15)

위까지는 **어떻게 재는가**였다. 이 절은 **왜 낮은가**다.
[[2016 위험한 삼위일체 — 생산성·부채·정책여력 (BIS 86th Annual Report)]]의 첫 축이 여기 걸린다.

**설명 후보가 셋이고, 정책 처방이 서로 다르다.**

| 설명 | 대표 문헌 | 뜻 | 처방 |
|---|---|---|---|
| **측정 문제** | [[1967 The Explanation of Productivity Change (Jorgenson & Griliches)]] | 투입의 질을 못 재서 잔차로 흘러든 것 | 통계 개선 |
| **배분 문제** | [[2009 Misallocation and Manufacturing TFP in China and India (Hsieh & Klenow)]] · [[2008 Policy Distortions and Aggregate Productivity with Heterogeneous Establishments (Restuccia & Rogerson)]] | 기술은 있는데 자원이 저생산성 기업에 묶임 | 왜곡 제거·구조조정 |
| **아이디어 고갈** | [[2020 Are Ideas Getting Harder to Find (Bloom, Jones, Van Reenen & Webb)]] | 같은 성장에 더 많은 연구자가 필요해짐 | R&D 확대(다만 수익체감) |

지형 전체는 [[2011 What Determines Productivity (Syverson)]]가 정리한다 —
기업 **내부**(경영·기술·인적자본)와 **외부**(경쟁·규제·재배분 유연성)로 갈라 읽는다.

> **실무 규칙 셋**
> **①** **TFP 둔화를 "혁신이 멈췄다"로 바로 읽지 말 것.** 위 세 설명이 같은 하락을 만들고
> 처방은 정반대다. 지표 하나로는 구분되지 않는다.
> **②** **오배분은 개도국만의 문제가 아니다.** Hsieh–Klenow는 완전 균등화 시 **미국도 30–43%**로 계산한다.
> **③** Hsieh–Klenow 수치를 인용하려면 **대체탄력성 σ 가정을 함께 적을 것** — 저자가
> σ=3에서 87%, σ=5에서 184%라고 직접 밝힌다. **가정이 결과의 두 배를 만든다.**

**AI 논쟁의 반증 기준** — [[2020 Are Ideas Getting Harder to Find (Bloom, Jones, Van Reenen & Webb)]]가
검증 가능한 형태를 준다: *연구자 1인당 아이디어 산출이 반등하는가.*
반등하지 않으면 AI는 하락을 **늦추는** 것이지 뒤집는 것이 아니다.

## 시황에서 생산성을 판정하는 법 — 세 진영과 눈금 *(2026-08-18 신설)*

생산성은 시황에서 가장 자주 **결론 없이 언급되는** 항목이다. 문헌을 좌표로 깔고 **관측치로 판정**한다.

| 진영 | 대표 문헌 | 현재 자료에서 기대되는 모습 |
|---|---|---|
| **A. 자본심화형** (기술이 아니라 투자가 끈다) | [[2008 A Retrospective Look at the U.S. Productivity Growth Resurgence (Jorgenson, Ho & Stiroh)]] | dk ↑ · dLP ↑ · **dtfp ≈ 0** |
| **B. 구조적 둔화** (아이디어 고갈·역풍) | [[2012 Is U.S. Economic Growth Over - Faltering Innovation Confronts the Six Headwinds (Gordon)]] · [[2020 Are Ideas Getting Harder to Find (Bloom, Jones, Van Reenen & Webb)]] | dtfp 장기 하향 · dLP도 둔화 |
| **C. 과제 재편형** (AI·자동화) | [[2018 Artificial Intelligence, Automation, and Work (Acemoglu & Restrepo)]] · [[2015 Why Are There Still So Many Jobs (Autor)]] | dk ↑ + **고용 구성 변화**(신규 과제) 동반 여부가 관건 |

**판정 규칙 (시황 작성 시)**

1. **dLP(노동생산성)와 dtfp(기술)를 반드시 갈라 쓴다.** 둘이 갈리면 그 자체가 결론이다
2. dk ↑ · dLP ↑ · dtfp ≈ 0 이면 **A**로 적는다 — *"생산성이 좋아졌다"가 아니라 "자본을 더 넣었다"*
3. **A로 판정되면 지속성 단서를 붙인다**: 투자가 멈추면 끝난다(T13 dk < +1.5 감시)
4. **C를 주장하려면 자본지출만으로 부족하다** — 신규 과제·고용 구성 변화를 함께 제시한다 → [[AI 자본지출]]
5. **B는 분기 자료로 판정하지 않는다.** Gordon의 주장은 10년 단위이므로 시황에서는 **배경 가설**로만 쓴다

**현재 판정 (2026 상반기 Fernald 기준, DataBook `frbsf` 수집)**

| 계열 | 값 |
|---|---:|
| dLP (노동생산성) | **+0.64** |
| dk (자본투입) | **+3.04** |
| dtfp | **−0.08** |
| dtfp_util (가동률조정) | **−2.16** ← T12 발동 중 |

→ **A(자본심화형)로 판정.** *"생산성 개선"이라고 쓰지 않는다.*
[[RegimeView 1.0 (2026-08-09)]] ②번 기둥은 이 판정 위에서만 성립하며,
**지속성(투자 지속)과 여유(가동률 상승 = slack 축소)** 두 단서를 항상 함께 적는다.


**⚖ 기관 진단과의 대조 (2026-08-18)**

- [[2026 Monetary Policy Report July 2026 (Federal Reserve)]] — 연준도 **"자본투자는 상당히 증가, 가계소비는 아주 소폭"**,
  **"노동생산성 증가율이 강하다"** 고 서술한다. **A(자본심화) 판정과 정합적**이다.
  ⚠ 단 연준이 말한 것은 **노동생산성**이지 TFP가 아니다 — 그대로 옮기면 A와 C를 혼동한다
- [[2026 OECD Economic Outlook Interim March 2026 — Testing Resilience]] — **"미국에서 AI 채택이 높은 부문의 생산성 증가가 더 빨랐다"**.
  이것은 **C(과제 재편) 쪽 대립 증거 후보**다. 부문별 자료로 검증하기 전까지 **판정을 바꾸지 않는다**

