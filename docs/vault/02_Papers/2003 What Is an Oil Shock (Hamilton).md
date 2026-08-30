---
title: "What Is an Oil Shock?"
type: paper
journal: Journal of Econometrics 113(2), 363–398 (2003)
date: 2003
author: James D. Hamilton (UC San Diego)
url: https://www.sciencedirect.com/science/article/abs/pii/S0304407602002075
tags: [type/paper, method/nonlinear, domain/commodities]
concepts: [비선형성, 순유가상승, 비대칭 반응, 유가-GDP 관계]
status: done
verification: partial
reliability: academic
text_basis: cited-primary
verified: "△ 서지 확정(2026-08-14). ScienceDirect PII S0304407602002075 형식 정상, 접속은 403(봇 차단)이라 미확인. 본문 미열람 — **수치 인용 금지**"
promoted_from: "[[L213 What Is an Oil Shock-]]"
related: ["[[1996 This Is What Happened to the Oil Price-Macroeconomy Relationship (Hamilton)]]", "[[2009 Not All Oil Price Shocks Are Alike (Kilian)]]", "[[WTI (국제유가)]]"]
---

# 유가 변화를 어떻게 변수로 만들 것인가 (Hamilton, 2003)

> Journal of Econometrics 113(2) 363–398, 2003.
> ⚠ **본문 미열람.** ScienceDirect가 403(봇 차단)이라 접속 확인도 못 했다.
> **수치는 인용하지 않는다.**

## 왜 중요한가 — 우리 문제와 직결

[[1996 This Is What Happened to the Oil Price-Macroeconomy Relationship (Hamilton)]]에서
제안한 **순유가상승** 아이디어를 계량적으로 밀고 나간 논문이다.
[[WTI (국제유가)]] 계보에서 **2단계와 3단계 사이**를 잇는다.

Ready(2018) 초고가 인용한 *"전후 11번의 경기하강 중 10번이 유의한 유가 상승 직후"* 라는
정식화도 Hamilton의 이 계열에서 나온다.

## 논지

유가와 실물의 관계는 **선형이 아니다.** 유가 **상승**은 GDP를 낮추지만
유가 **하락**은 대칭적으로 GDP를 높이지 않는다.

따라서 "유가 변화율"을 그대로 회귀에 넣으면 관계가 흐려진다.
**비선형 변환**(순유가상승 등)을 써야 역사적 관계가 드러난다.
제목이 곧 문제의식이다 — **"오일 쇼크란 무엇인가", 즉 어떤 변환이 진짜 충격인가.**

## 한계와 적용 범위

- **사서(추가)**: 비선형 변환의 **함수 형태 선택이 임의적**이라는 비판이 있다.
  기준 기간(1년/3년)을 바꾸면 결과가 달라질 수 있고, **데이터에 맞춰 고른 것 아닌가**라는
  의심이 [[2009 Not All Oil Price Shocks Are Alike (Kilian)]] 계열의 출발점이다
- **사서(추가)**: 본문 미열람이므로 **검정 통계량·모형 설정을 인용하지 않는다**
- **사서(추가)**: **변환으로 풀 것인가(Hamilton) 원인 분해로 풀 것인가(Kilian)** —
  두 해법이 경쟁한다. 이 노트가 판정하지 않는다

## 인과 사슬

유가 변화 → **상승과 하락의 비대칭** → 선형 변수로는 관계 소실
→ 순유가상승 등 **비선형 변환** → 유가-GDP 관계 복원
→ (경쟁 해법) 변환 대신 **충격 원인 분해**(Kilian)

**Comment**: DataBook 실무 후보 — `derived.py`에
**WTI의 "직전 12개월 최고치 대비 초과분"** 을 파생지표로 추가하면 이 계열의 변수를
직접 볼 수 있다. [[WTI (국제유가)]] 노드에 이미 후보로 적어 뒀다.

## 관련 개념

- 아이디어의 출발 — [[1996 This Is What Happened to the Oil Price-Macroeconomy Relationship (Hamilton)]] ·
  [[1983 Oil and the Macroeconomy Since World War II (Hamilton)]]
- 경쟁 해법 — [[2009 Not All Oil Price Shocks Are Alike (Kilian)]] · [[2008 Exogenous Oil Supply Shocks (Kilian)]]
- 계보 — [[WTI (국제유가)]]

## References

[1]: https://www.sciencedirect.com/science/article/abs/pii/S0304407602002075 "Hamilton (2003), What Is an Oil Shock?, Journal of Econometrics 113(2) 363–398"
