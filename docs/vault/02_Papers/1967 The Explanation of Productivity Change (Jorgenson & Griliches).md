---
title: "The Explanation of Productivity Change"
type: paper
journal: Review of Economic Studies 34(3), 249–283 (1967-07)
date: 1967
author: Dale W. Jorgenson (Berkeley / Harvard), Zvi Griliches (Chicago / Harvard)
url: https://ideas.repec.org/a/oup/restud/v34y1967i3p249-283..html
tags: [type/paper, method/growth-accounting, domain/productivity]
concepts: [성장회계, 요소서비스, 자본서비스, 질 조정, 잔차의 해석, 측정오차]
status: done
verification: partial
reliability: academic
text_basis: cited-primary
verified: "○ RePEc 공식 페이지에서 제목·저자·권호·페이지 대조 확인(2026-08-15, REStud 34(3) 249–283 일치. URL의 이중 마침표는 RePEc 정상 형식). 본문 미열람, **수치 인용 금지**"
promoted_from: "[[L162 The Explanation of Productivity Change]]"
related: ["[[1957 Technical Change and the Aggregate Production Function (Solow)]]", "[[2014 A Quarterly, Utilization-Adjusted Series on Total Factor Productivity (Fernald)]]", "[[2011 What Determines Productivity (Syverson)]]", "[[총요소생산성 (TFP)]]"]
---

# 잔차의 대부분은 측정을 잘못해서 생긴 것이다 (Jorgenson & Griliches, 1967)

> Review of Economic Studies 34(3) 249–283, 1967년 7월.
> ⚠ **본문 미열람.** 서지만 확정했다. **수치는 인용하지 않는다.**

## 왜 중요한가 — Solow 잔차에 대한 정면 반론

[[1957 Technical Change and the Aggregate Production Function (Solow)]]이 남긴 **잔차**를
사람들은 "기술진보"라고 불렀다. 이 논문은 그 해석을 공격한다.

**주장: 잔차의 상당 부분은 기술이 아니라 투입 측정의 실패다.**

노동 1시간과 노동 1시간은 같지 않다(교육·숙련이 다르다).
자본 1달러와 1달러도 같지 않다(내용연수·자산 구성이 다르다).
**투입을 질까지 반영해 제대로 재면 설명되지 않는 잔차가 크게 줄어든다.**

## 논지

핵심 개념이 **요소서비스(factor services)** 다. 자본 **스톡**이 아니라 그 스톡이 제공하는 **서비스 흐름**을
측정해야 하고, 자산 종류별 서비스 가격으로 가중해야 한다.
노동도 마찬가지로 교육·연령·직종별로 나눠 질 조정을 한다.

이 접근이 이후 **성장회계의 표준**이 됐고, KLEMS류 데이터베이스와
[[2014 A Quarterly, Utilization-Adjusted Series on Total Factor Productivity (Fernald)]]의
가동률 조정도 같은 계보다.

## 한계와 적용 범위

- **사서(추가)**: **"잔차가 0이 될 수 있다"까지 밀면 반대편 극단**이다. 후속 문헌은
  질 조정 후에도 유의미한 잔차가 남는다고 본다. 논쟁의 결론이 아니라 **논쟁의 한쪽 끝**이다
- **사서(추가)**: 질 조정은 **가정이 많이 들어간다.** 무엇을 질로 볼지, 어떤 가격으로 가중할지에
  따라 결과가 달라진다. **측정 개선이 곧 객관성 증가는 아니다**
- **사서(추가)**: 본문 미열람이므로 **잔차 축소 폭을 인용하지 않는다**

## 인과 사슬

투입을 총량으로만 측정 → 질 변화가 투입 증가로 안 잡힘
→ **그만큼이 잔차로 흘러들어감** → "기술진보"로 오독
→ 요소서비스·질 조정 도입 → **잔차 축소**
→ [[총요소생산성 (TFP)]]는 **측정 방식에 의존하는 양**임이 드러남

**Comment**: 실무 규칙 — **TFP 수치를 인용할 때 어떤 계열인지 반드시 밝힌다.**
질 조정·가동률 조정 여부에 따라 같은 시기 값이 달라진다.
DataBook이 쓰는 것은 [[2014 A Quarterly, Utilization-Adjusted Series on Total Factor Productivity (Fernald)]]의
**가동률 조정 계열**(`dtfp_util`)과 비조정(`dtfp`)이고, **둘의 차이가 곧 이 논문이 제기한 문제**다.

실제로 2026 H1에 `dtfp` −0.08과 `dtfp_util` −2.16이 크게 벌어져 있다.
**"생산성이 얼마나 나빴나"의 답이 계열 선택으로 갈린다** — 이 논문이 60년 전에 경고한 그것이다.

## 관련 개념

- 반론 대상 — [[1957 Technical Change and the Aggregate Production Function (Solow)]]
- 현대적 구현 — [[2014 A Quarterly, Utilization-Adjusted Series on Total Factor Productivity (Fernald)]]
- 기술충격 해석 — [[2006 Are Technology Improvements Contractionary (Basu, Fernald & Kimball)]]
- 서베이 — [[2011 What Determines Productivity (Syverson)]]
- 지표 — [[총요소생산성 (TFP)]]

## References

[1]: https://ideas.repec.org/a/oup/restud/v34y1967i3p249-283..html "Jorgenson and Griliches (1967), The Explanation of Productivity Change, REStud 34(3) 249–283"
