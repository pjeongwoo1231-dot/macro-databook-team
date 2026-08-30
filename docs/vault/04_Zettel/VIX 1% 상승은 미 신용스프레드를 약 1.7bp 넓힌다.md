---
title: VIX 1% 상승은 미 신용스프레드를 약 1.7bp 넓힌다
type: atomic_note
created: 2026-07-28
status: verified
source: 자체 재현 (2026-07) — FRED 원자료, 코드 _System/Analysis/vix_default_premium_replication.py
reliability: ai-generated
tags: [type/atomic-note, domain/risk, region/us]
related: ["[[2022 Global Risk Aversion and US Corporate Default Risk Premium (Jiawei Yuan)]]"]
---

# VIX 1% 상승은 미 신용스프레드를 약 1.7bp 넓힌다

## 1분 요약

논문의 해석은 틀렸지만 **추정치 자체는 쓸 수 있다.** 올바르게 재계산하고
종속변수를 진짜 신용스프레드로 바꾸면 이 vault가 쓸 수 있는 숫자가 나온다.

## 인과 사슬

`Baa−국채10년 = α₀ + α₁·log(VIX)`, 2008.01~2017.12 월별

  **α₁ = 1.6705** (SE 0.1025) · **R² = 0.693**

→ [[VIX]] **1% 상승** → 미 Baa [[신용스프레드]] **약 +1.7bp**
→ 위기 국면 (VIX 12 → 80, log 차 1.897) → 누적 **+3.17%p (317bp)**

⚠ 단변량이므로 인과가 아니라 **동시 상관**이다. 통제변수 없음

**왜 중요한가**: 이 vault의 [[VIX]] 노드에 **신용 경로**가 추가된다.
지금까지 VIX의 전달 경로로 확인된 것:

- **주식** → [[2014 The Impact of Global Volatility on Asian Financial Markets (Kang·Choi·Yoon)]]
  (VIX↑ → 한국 −0.0993, 일본 −0.0767)
- **환율** → 같은 논문 (엔 절상 −0.0061 / 원 절하 +0.0212)
- **신용** → 여기 (Baa 스프레드 +1.7bp per 1%)

세 경로가 모두 같은 방향으로 작동한다 — 리스크오프 시
한국은 [[KOSPI]] 하락 + [[원·달러 환율]] 상승 + 조달비용 상승이 **동시에** 온다.

⚠ 인용 시 반드시 명시: **원 논문의 서술(2.3802%p)이 아니라 재계산값**이며,
   단변량 상관이라 인과 해석 불가.

**확신도: 중하.** 단변량 회귀에 통제변수가 전혀 없어 계수가 식별되지 않는다. 노트 본인도 '동시 상관이지 인과 아님'을 명시한다. 크기 감각용으로만 쓴다

## 핵심 지표 · 연결고리

- **관련 노드**: [[VIX]] · [[신용스프레드]] · [[KOSPI]] · [[원·달러 환율]] · [[신용사이클]]
- **리서치 관점**: 틀린 해석의 논문에서도 추정치는 건질 수 있다 — 단, 재현하고 재계산한 뒤에만.
