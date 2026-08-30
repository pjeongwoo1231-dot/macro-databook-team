---
title: "Households' Medium- to Long-Term Inflation Expectations Formation: The Role of Past Experience and Inflation Regimes"
type: paper
series: Bank of Japan Working Paper No.25-E-6
date: 2025
author: Go Fujii, Shogo Nakano (Bank of Japan)
url: https://www.boj.or.jp/en/research/wps_rev/
tags: [type/paper, method/microdata, domain/inflation]
concepts: [기대인플레이션, 경험 인플레이션, 세대효과, 인플레이션 레짐, 후향적 기대]
source_file: 06_SourceArchive/05-Primary-PDFs/2024-2026/BOJ-WP-25e06.pdf
status: done
verification: full
reliability: working-paper
text_basis: local-pdf
verified: 원문 대조 완료(2026-08-14). 로컬 PDF 판독 — 경험 +1%p → 기대 +0.357%p, BOJ 생활의식 설문 마이크로데이터, 상하위 절단 확인
related: ["[[BEI (기대인플레이션)]]", "[[2023 인플레이션 기대와 주택가격 - 한국 미국 비교 (이명수)]]", "[[2014 NKPC Closed Form - Korean Manufacturing (Bae, Hong, Kang & Yoon)]]", "[[원문 아카이브 MOC]]"]
---

# 살아온 물가가 앞으로의 물가 기대를 만든다 — 계수 0.357 (Fujii & Nakano, BOJ 2025)

> Bank of Japan Working Paper No.25-E-6. 저자 견해이며 일본은행 견해가 아니다.

## 왜 중요한가 — 우리 문제와 직결

볼트의 [[원문검증 논문 MOC]]에 **"한국의 기대 형성은 후향적이다 — 두 논문이 서로 보강"**
이라는 교차 논점이 있다. [[2023 인플레이션 기대와 주택가격 - 한국 미국 비교 (이명수)]]의
"금리 인상이 기대를 못 잡는다"와 [[2014 NKPC Closed Form - Korean Manufacturing (Bae, Hong, Kang & Yoon)]]의
"제조업 40~50%가 후향적 가격설정"이 서로 다른 방법으로 같은 방향을 가리킨다는 것.

**이 논문은 그 후향성의 미시적 기제를 마이크로데이터로 계량한다.**
가계가 **자기 생애에 겪은 인플레이션**을 기준으로 미래를 예상한다는 것이고,
계수까지 제시한다. 한국 논의에 세 번째 다리를 놓는다.

또 하나 — 볼트 제텔은 **[[BEI (기대인플레이션)]]의 한국판이 유동성 프리미엄 과다로
쓸 수 없다**고 기록한다(최준 2016). 시장 기반 지표가 막혔다면 **서베이 기반 기대**를
어떻게 읽을지가 남는데, 이 논문이 그 읽는 법을 준다.

## 방법과 자료

| 항목 | 내용 |
|---|---|
| 자료 | **일본은행 「생활의식에 관한 앙케이트」 마이크로데이터**(Opinion Survey on the General Public's Views and Behavior) |
| 설명변수 | ① 개인의 **생애 경험 인플레이션**(past inflation experience) ② 시점별 **인플레이션 레짐**(물가 추세) |
| 종속변수 | 가계의 **중장기** 기대인플레이션 |
| 처리 | 각 설문 라운드에서 분포 상·하위 극단치를 이상치로 절단 |

## 원문에서 확인한 결과

**1. 생애 경험이 기대를 움직인다 — 계수 0.357.**
> *"when past experience increases by 1 percentage point, household inflation expectations
> increase by 0.357 percentage points."*

**2. 세대 효과.** 생애 평균 경험 인플레가 낮은 가계일수록 통계적으로 유의하게 낮은 기대를
형성한다. 특히 **생애 대부분을 디플레 환경에서 보낸 젊은 세대**가 그렇다.

**3. 함의.** 일본의 장기 디플레·저인플레가 **개인의 경험을 통해 기대에 각인**돼 있으며,
이는 물가목표 달성이 단순히 현재 물가를 올리는 문제가 아님을 시사한다.

## 한계와 적용 범위

- **사서(추가)**: 서베이 기대는 **응답자가 실제 지출·임금협상에서 쓰는 기대와 다를 수 있다.**
  이 논문은 기대의 형성만 다루고 행동으로의 전달은 다루지 않는다
- **사서(추가)**: 경험 인플레와 연령은 **거의 완전히 얽혀 있다.** "세대 효과"가 경험 때문인지
  생애주기(소득·자산 구성) 때문인지 분리하려면 추가 식별이 필요하다
- **사서(추가)**: **일본은 극단 사례다.** 30년 디플레라는 조건이 계수를 키웠을 수 있어
  0.357을 다른 나라에 그대로 옮기면 안 된다. 한국은 일본만큼 긴 디플레가 없다 —
  **같은 회귀를 한국 서베이(한은 소비자동향조사)로 돌리면 계수가 얼마인지가 곧 검증 과제**다
- **사서(추가)**: 인플레이션 레짐 변수는 구성 방식에 민감하다

## 인과 사슬

장기 저인플레 환경 → 세대별 **생애 경험 인플레** 낮음
→ 중장기 [[BEI (기대인플레이션)]]·서베이 기대 하향(경험 +1%p당 +0.357%p)
→ 임금·가격 설정의 **후향성** 강화
→ [[통화정책]]의 기대경로 약화 → 현재 [[CPI (소비자물가지수)]]를 올려도 기대가 늦게 따라옴

**Comment**: 정책 함의가 무겁다 — **기대는 발표로 바뀌지 않고 경험으로 바뀐다.**
[[2020 Effects of Fed Policy Rate Forecasts at the ZLB (Galati & Moessner)]]가 보인
"점도표가 실질금리는 움직이는데 기대인플레는 안 움직인다"의 **가계 쪽 이유**가 여기 있을 수 있다.
커뮤니케이션이 시장 가격은 움직여도 **살아온 경험은 못 덮는다.**

한국 적용의 관문: 한은 소비자동향조사로 같은 회귀를 돌려 계수를 비교하는 것.
그 결과가 [[2023 인플레이션 기대와 주택가격 - 한국 미국 비교 (이명수)]]의 후향성 주장을
독립적으로 검증하거나 반증한다.

## 관련 개념

- 한국의 후향적 기대 — [[2023 인플레이션 기대와 주택가격 - 한국 미국 비교 (이명수)]] ·
  [[2014 NKPC Closed Form - Korean Manufacturing (Bae, Hong, Kang & Yoon)]]
- 시장 기반 기대의 한계 — [[2016 기대인플레이션을 이용한 미국 중장기 인플레이션 예측 (최준)]]
- 커뮤니케이션 쪽 — [[2020 Effects of Fed Policy Rate Forecasts at the ZLB (Galati & Moessner)]] ·
  [[2025 Monetary Policy, Uncertainty, and Communications (Garga et al, FEDS 2025-074)]]
- 지표 — [[BEI (기대인플레이션)]] · [[CPI (소비자물가지수)]] · [[핵심인플레이션]]

## References

[1]: https://www.boj.or.jp/en/research/wps_rev/wps_2025/data/wp25e06.pdf "Fujii and Nakano (2025), Households' Medium- to Long-Term Inflation Expectations Formation, BOJ WP 25-E-6"
