---
title: "Technical Change and the Aggregate Production Function"
type: paper
journal: Review of Economics and Statistics 39(3), 312–320 (1957)
date: 1957
author: Robert M. Solow (MIT)
url: https://www.jstor.org/stable/1926047
tags: [type/paper, method/growth-accounting, domain/productivity]
concepts: [솔로우 잔차, 성장회계, 총요소생산성, 기술변화, 생산함수]
status: done
verification: partial
reliability: academic
text_basis: cited-primary
verified: "△ 서지 확정(2026-08-14). JSTOR 링크 생존 확인(HTTP 200). 본문 유료라 미열람 — **수치 인용 금지**"
promoted_from: "[[L161 Technical Change and the Aggregate Production Function]]"
related: ["[[1956 A Contribution to the Theory of Economic Growth (Solow)]]", "[[2014 A Quarterly, Utilization-Adjusted Series on Total Factor Productivity (Fernald)]]", "[[총요소생산성 (TFP)]]"]
---

# 잔차가 곧 기술이다 — 그리고 그게 문제다 (Solow, 1957)

> Review of Economics and Statistics 39(3) 312–320, 1957.
> ⚠ **본문 미열람**(JSTOR 유료). 서지만 확정했다. **수치는 인용하지 않는다.**

## 왜 중요한가 — 우리 문제와 직결

볼트에 [[1956 A Contribution to the Theory of Economic Growth (Solow)]](성장 **모형**)은 있는데
**1957(성장 회계)이 없었다.** 둘은 다른 논문이고, 실무에서 쓰는 건 후자다.

DataBook이 이제 받는 `dtfp`·`dtfp_util`이 전부 **이 논문이 만든 개념의 후손**이다.
그리고 볼트 제텔에 `솔로우 잔차`가 [[총요소생산성 (TFP)]] 노드의 별칭으로 등록돼 있다 —
그 출처가 여기다.

## 논지

총생산함수와 요소투입(자본·노동)의 성장률을 알면, **산출 성장 중 투입 증가로 설명되지 않는
나머지**를 계산할 수 있다. 그 **잔차(residual)** 를 기술변화로 해석한다.

```
산출 성장 = (자본 몫 × 자본 성장) + (노동 몫 × 노동 성장) + 잔차
                                                          └─ 솔로우 잔차 = TFP
```

이 단순한 회계 항등식이 이후 성장·경기 연구의 **공통 언어**가 됐다.

## 한계와 적용 범위

이 논문의 한계가 곧 후속 문헌 전체의 출발점이라 특히 중요하다.

- **잔차는 측정된 것이 아니라 남은 것이다.** 기술 개선뿐 아니라 **측정오차, 가동률 변동,
  규모수익, 불완전경쟁, 집계 문제**가 전부 여기 들어간다.
  → [[2006 Are Technology Improvements Contractionary (Basu, Fernald & Kimball)]]가
  그 성분들을 하나씩 걷어내려 한 작업이다
- **요소 몫을 관측 가능한 소득 몫으로 대체**하는 것은 완전경쟁·규모수익불변을 전제한다.
  → [[2020 Demographic Origins of the Decline in Labor's Share (Glover & Short)]]가 보인
  **수요독점 쐐기**가 있으면 이 전제가 깨진다
- **사서(추가)**: 본문 미열람이므로 **원논문의 추정치(예: 미국 성장의 몇 %가 기술)를 인용하지 않는다**

## 인과 사슬

산출·자본·노동 관측 → 요소 몫으로 가중 → **잔차 = TFP**
→ (잔차에 가동률·측정오차가 섞임) → 가동률 조정 필요
→ [[2014 A Quarterly, Utilization-Adjusted Series on Total Factor Productivity (Fernald)]]의 `dtfp_util`

**Comment**: 볼트 실무 규칙 — **"생산성"이라는 말이 나오면 어느 것인지 먼저 묻는다.**
노동생산성(`dLP`) · 잔차 TFP(`dtfp`) · 가동률조정 TFP(`dtfp_util`)는 다른 물건이고,
2026 상반기에는 **부호까지 갈린다**(+0.64 / −0.08 / −2.16).
[[RegimeView 1.0 (2026-08-09)]]처럼 생산성을 논지의 기둥으로 쓰는 노트에서는
**어느 계열인지 명시**해야 한다.

## 관련 개념

- 같은 저자, 다른 논문 — [[1956 A Contribution to the Theory of Economic Growth (Solow)]]
- 잔차를 정제하려는 시도 — [[2006 Are Technology Improvements Contractionary (Basu, Fernald & Kimball)]] ·
  [[2014 A Quarterly, Utilization-Adjusted Series on Total Factor Productivity (Fernald)]]
- 요소 몫 전제의 균열 — [[2020 Demographic Origins of the Decline in Labor's Share (Glover & Short)]]
- 지표 — [[총요소생산성 (TFP)]] · [[잠재성장률]]

## References

[1]: https://www.jstor.org/stable/1926047 "Solow (1957), Technical Change and the Aggregate Production Function, REStat 39(3) 312–320"
