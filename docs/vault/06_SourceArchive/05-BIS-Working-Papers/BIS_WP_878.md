---
title: "BIS WP 878 — Which credit gap is better at predicting financial crises? A comparison of univariate filters"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 878
published: "August 2020"
authors: "Mathias Drehmann and James Yetman"
source_kind: "working-paper"
peer_reviewed: false
primary_text_read: true  # 추출 전문 기준. 사람 대조 아님
human_verified: false
analysis_model: "gpt-5-mini"
analysis_confidence: "not-calibrated"
relevance_score: 1
created: 2026-08-14
updated: 2026-08-14
archive_status: "llm-structured-unverified"
tags:
  - flag/partial-check
  - bis
  - working-paper
  - "credit-to-gdp-gap"
  - "early-warning-indicators"
  - "hp-filter"
  - "linear-projection"
  - "macroprudential-policy"
  - "roc/auc-forecast-evaluation"
  - "panel-vs-country-estimation"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 878 — Which credit gap is better at predicting financial crises? A comparison of univariate filters

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

저자들은 41개국(1970~2017) 분기자료를 이용해 일방향 HP갭, 선형투영갭(여러 지연구조) 및 20분기 성장률 갭을 실시간(확장표본)으로 비교했다. 주요 결과는 GDP로 정규화한 경우가 인구정규화보다 예측력이 높고, 선형투영은 국가별 실시간 추정 시 성능이 약하지만 패널로 계수를 공유하면 HP 갭보다 통계적으로 소폭 우수하다는 점이다. 그러나 이러한 통계적 개선은 실무적 의미는 작아 정책적 판단·다중지표 활용·불확실성 관리가 더 중요하다고 결론지었다. 분석은 단변량 지표에 국한되고 표본의 위기 수·실시간 데이터 빈티지 문제·패널 가정 등으로 일반화와 해석에 제약이 있다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 여러 단변량 방식(일방향 HP 필터, 선형투영(Projection), 20분기 성장률 등)으로 산출한 신용 갭 중 어느 것이 실물·금융 위기 예측에 더 유용한가? |
| 방법 | 분기별 자료의 확장표본(real-time expanding sample)을 사용해 국가별·패널 선형회귀로 투영오차(projection residual), 한쪽(실시간) HP 필터(λ=400000) 갭, 20분기 성장률 갭을 산출하고, ROC 곡선 아래 면적(AUC)으로 위기 예측능력을 평가함. 표준오차는 부트스트랩(1000회) 및 국가군 클러스터로 계산. |
| 자료·범위 | BIS의 민간 비금융부문 총신용(series of total credit to private non-financial sector), 국가별 명목 GDP, CPI, 인구(1970~2017 일부 국가에서 이용 가능). 표본은 41개국, 위기표본은 27건. 분석을 위해 각국별 갭은 최소 15년(60분기) 자료가 확보되는 시점부터 포함(최초 테스트 시점 ≈1985Q1). 위기일자는 ESRB 및 기존 문헌 데이터셋을 사용. |
| 주제 | credit-to-GDP gap, early warning indicators, HP filter, linear projection, macroprudential policy, ROC/AUC forecast evaluation, panel vs country estimation |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 결과: 신용을 GDP로 정규화하는 것이 인구로 정규화(1인당 실질신용)보다 위기 예측(AUC)에서 일관되게 우수함.
- 저자 결과: 선형투영 기반 갭은 국가별(개별회귀)로 실시간 추정할 경우 예측력이 약하고 종단(끝점) 문제에 민감함.
- 저자 결과: 동일한 선형투영식을 패널로 추정해 계수를 전체 국가에 동일하게 강제하면 실시간에서 성능이 크게 개선되어(패널 우월성) HP 기반 갭보다 AUC가 통계적으로 소폭 더 높음.
- 저자 결과: 선형투영의 지연구조(lag)와 h 값(예: 20~36분기)은 적절한 범위(약 5~9년)에서는 예측성능에 큰 영향을 주지 않음.
- 저자 결과: 선형투영 패널 GDP 갭의 성능 개선은 주로 2000년 이후 기간과 신흥시장국에서 더 두드러짐.
- 저자 결과: 통계적으로 유의한 차이가 가끔 관찰되나 실무적 중요성은 작음 — 평균적으로 여러 사양에서 신호의 약 30%는 오류이며, 패널 선형투영 GDP 갭이 HP GDP 갭보다 정상기(비위기)에서 오보를 2~3%포인트 줄이는 정도임.
- 저자 결과: 실무적 해석으로 보면 10년 동안 정책당국이 얻을 수 있는 개선은 평균적으로 오보 한 분기(또는 잘못된 결정 1회) 수준으로 제한적임.
- 저자 결과: 선형투영 방식은 표본의 희소성(위기 희귀성) 때문에 다른 국가의 경험을 차용하면 성능이 개선된다고 해석될 수 있음.

## 메커니즘과 연결고리

- GDP로 정규화하면 신용-산출의 공변성 때문에 위기 신호가 산출 변동에 영향을 받는 반면, 실증적으로는 GDP 정규화가 예측력에서 우수함.
- HP 필터(특히 큰 λ)는 중·장기 신용주기를 포착하지만 끝점과 통계적 성질(스푸리어스 다이내믹스) 문제를 초래할 수 있음.
- 선형투영의 잔차는 관측시점에서 향후(h분기) 신용수준을 선형예측한 뒤의 편차로서 '과도한 신용' 신호로 해석됨.
- 패널추정은 위기 사례가 드문 상황에서 다른 국가의 경험으로 계수를 안정화시켜 예측력(특히 실시간시나리오)을 향상시킴.
- 실시간(확장표본) 추정 시에는 경기부양기(붐) 동안 회귀계수가 갱신되어 잔차가 억제되는 방식으로 선형투영에 자체 끝점 문제가 발생할 수 있음.
- 20분기(5년) 성장률 방식은 필터를 사용하지 않고 중기 신용가속을 직접 측정하는 간단한 대안으로 기능함.

## 한계와 적용 범위

- 저자 자체 설명: 모든 갭 측정치는 본질적으로 지표(indicator)에 불과하며 명확한 이론적 기반이 없음.
- 저자 자체 설명: 사용한 실시간 추정은 'quasi real time'으로서 실제 시점의 데이터 빈출(vintage) 문제(진정한 리얼타임 데이터의 불완전성)를 완전히 반영하지 않음.
- 저자 자체 설명: 표본에 포함된 위기 수가 27건으로 제한적이며, 이로 인해 통계적 파워와 일반화 가능성에 제약이 있음.
- 방법론적 한계(명시·암시): 패널 추정은 국가들에 동일한 동역학 계수를 강제하므로 국가별 이질성이 존재할 경우 오차를 낳을 수 있음.
- 방법론적 한계(명시): HP 필터 및 선형투영 모두 끝점(end-point) 문제와 사후-실시간 차이(특히 HP의 경우)에 민감함; 선형투영도 작은 표본에서 끝점 문제 발생을 보고함.
- 범위 한계: 본문은 단변량 갭 지표들만 비교하며, 다변량(예: VAR, 금융 사이클 다중지표, 머신러닝 결합지표 등)은 분석 대상에서 제외됨.
- 실무 해석 한계: 갭의 임계값 설정과 행동 규칙(예: 66% 신호 임계값)은 자의적 선택이며 정책비용·편익을 반영한 최적의 규칙을 제시하지 않음.
- 측정 이슈: 1인당 실질신용의 축척 문제로 로그변환을 사용했으며 이는 비교가능성 확보를 위한 조치이나 해석 차이를 낳음.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_878-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[GDP 성장률]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work878.pdf](https://www.bis.org/publ/work878.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work878.htm](https://www.bis.org/publ/work878.htm)


## References

[1]: https://www.bis.org/publ/work878.pdf "BIS Working Paper 878: Which credit gap is better at predicting financial crises? A comparison of univariate filters"
