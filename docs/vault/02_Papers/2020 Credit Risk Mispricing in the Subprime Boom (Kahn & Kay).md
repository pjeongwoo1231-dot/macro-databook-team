---
title: The impact of credit risk mispricing on mortgage lending during the subprime boom
type: paper
series: BIS Working Papers No 875
date: 2020-08
author: James A Kahn (Yeshiva University), Benjamin S Kay (Federal Reserve Board)
url: https://www.bis.org/publ/work875.pdf
tags: [type/paper, method/structural-estimation, domain/credit]
concepts: [서브프라임, 모기지보험, 역선택, 신용위험 오가격, 교차보조, FICO, 신용할당]
status: done
verification: full
reliability: working-paper
text_basis: human-fulltext
verified: 원문 대조 완료(2026-08-14). 표본기간·FICO 임계·결론부 직접 확인. tier A 승격
related: ["[[1997 Credit Cycles (Kiyotaki & Moore)]]", "[[2012 Credit Booms Gone Bust (Schularick & Taylor)]]", "[[Credit-Leverage-Risk-Pricing-Loop]]", "[[원문 아카이브 MOC]]"]
---

# 위험을 안 나눈 보험료가 역선택을 만들었다 (Kahn & Kay, 2020)

> BIS Working Paper No 875, 2020년 8월. JEL: G21, E44, E32

## 왜 중요한가 — 우리 문제와 직결

볼트의 위기 문헌은 **총량**으로 말한다 — [[2012 Credit Booms Gone Bust (Schularick & Taylor)]]는
신용붐이 위기를 예고한다고 하고, 볼트 제텔은 그 판별력이 [[금융위기는 잘못 끝난 신용붐이다 — 단 판별력은 AUROC 0.72에 그친다|AUROC 0.72에 그친다]]고 단서를 단다.
**총량으로는 왜 0.72에서 멈추는지 설명이 안 된다.**

이 논문은 **가격 구조**를 본다. 같은 신용 증가라도 위험이 제대로 가격화됐는지에 따라
결과가 갈린다는 것. [[Credit-Leverage-Risk-Pricing-Loop]]의 "위험가격 압축" 고리에
**측정 가능한 실체**를 준다 — 모기지보험료라는 관측 가능한 가격이다.

## 방법과 자료

| 항목 | 내용 |
|---|---|
| 원자료 | 정부·민간 **모기지보험료를 직접 수집**, **1999–2016**. CoreLogic Loan-Level Market Analytics(LLM 2.0) 병용 |
| 핵심 관찰 | **2008년 이전에는 관측 가능한 특성이 크게 다른 대출들 사이에 보험료 차이가 없었다.** 그 특성들은 실제로 부도를 예측했다 |
| 식별 | **위기 이후** 보험료로 부도행태 모형을 적합시키고, 주택가격 상승 기대를 시변으로 허용해 2008년 이전 오가격 규모를 역산 |

## 원문에서 확인한 결과

**1. 고위험 모기지 붐은 두 가지가 함께 만들었다** — 위험의 **오가격**과 주택가격에 대한
**낙관적 기대**. 저자들은 둘 중 하나로 환원하지 않는다.

**2. 오가격의 정체는 풀링이다.** FICO 점수로 측정한 **크게 다른 신용위험을 한 풀에 묶어**
평평한 보험료를 매겼고, 그 결과 **안전한 모기지가 위험한 모기지를 교차보조**했다.
이것이 풀 내부의 **역선택**을 낳았다.

**3. 정부 보험이 위험을 더 낮게 매겼다.** 가장 위험한 모기지가 매력적이었던 이유가 여기 있다.
그리고 **2008년 이후에도 정부는 계속 위험을 저가로 매겼다** — 주택시장 가정을 덜 낙관적으로
바꿔 보험료를 올렸지만 여전히 낮았다.

**4. 위기 후 축소는 가격이 아니라 할당으로 일어났다.** 보험료 인상이 **FICO 640 미만**
차입자의 차입을 줄이기는 했다. 그러나 이 상품군의 시장점유율 붕괴는
> *"appears primarily due to rationing rather than as a response to price changes."*

## 한계와 적용 범위

- **저자(명시)**: 2008년 이전에는 다수 차입자가 PMI 대신 **piggyback 2차 담보대출**을 썼다.
  고FICO 차입자에게는 PMI가 과대가격이었을 수 있어, **오가격 추정이 보수적**일 수 있다
- **저자(명시)**: 결과는 Adelino et al.(2016)·Kaplan et al.(2017)의 **신념 변화 중심 해석과
  양립한다.** 신용공급 요인을 인정하되 그것만으로 환원하지 않는다
- **사서(추가)**: 미국 모기지보험 제도(PMI·정부보증)에 특화된 식별이다. 한국처럼 보험 대신
  **LTV·DSR 규제**로 위험을 나누는 제도에는 그대로 이식되지 않는다. 다만 "규제가 위험을
  균일하게 취급하면 교차보조와 역선택이 생긴다"는 논리는 이전 가능하다

## 인과 사슬
평평한 보험료(위험 미차등) → 안전→위험 **교차보조** → 풀 내 **역선택**
→ 고위험 [[주택가격]] 연계 대출 확대 + 낙관적 기대 → [[신용사이클]] 팽창
→ 부도 현실화 → [[기업 부도]]·차압 → 위기 후 **가격이 아닌 할당**으로 축소(FICO 640 절벽)

**Comment**: 총량 지표는 이 사슬의 어디쯤인지 말해주지 못한다. **같은 신용 증가라도
위험이 차등 가격화됐는지**를 봐야 한다 — 스프레드의 *수준*이 아니라 *분산*을 보라는 뜻이다.
볼트의 [[가계부채와 주택가격은 독립된 두 신호가 아니다 — 하나가 다른 하나를 흡수한다]]와
합치면, 두 신호가 겹치는 이유의 후보 하나가 여기 있다 — 둘 다 같은 가격 왜곡의 결과일 수 있다.

## 관련 개념

- 메커니즘 일반형 — [[Credit-Leverage-Risk-Pricing-Loop]] · [[Global-Financial-Crisis-2007-2009]]
- 총량 접근의 한계 — [[2012 Credit Booms Gone Bust (Schularick & Taylor)]] ·
  [[금융위기는 잘못 끝난 신용붐이다 — 단 판별력은 AUROC 0.72에 그친다]]
- 담보·순자산 증폭 이론 — [[1997 Credit Cycles (Kiyotaki & Moore)]] ·
  [[1989 Agency Costs, Net Worth, and Business Fluctuations (Bernanke & Gertler)]]
- 신용공급 충격의 정량 모형 — [[BIS_WP_885]] (tier B, 은행 레버리지 충격 → 붐버스트)

## References

[1]: https://www.bis.org/publ/work875.pdf "Kahn and Kay (2020), The impact of credit risk mispricing on mortgage lending during the subprime boom, BIS WP 875"
