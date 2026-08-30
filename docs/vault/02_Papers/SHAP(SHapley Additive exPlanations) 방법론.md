---
title: SHAP(SHapley Additive exPlanations) 방법론
type: concept
category: [머신러닝 방법론, 모형해석]
tags: [type/paper, method/모형해석가능성, method/블랙박스모형]
concepts: [SHAP, Shapley value, 변수중요도, XAI]
related: [머신러닝 기반 회사채 신용스프레드·신용등급 예측 (비재무 데이터의 역할)]
difficulty: Intermediate
paper: [Wu2025]
status: done
verification: n-a
---

## 정의

**SHAP**
: 게임이론의 Shapley value에 기반해, 각 예측변수(feature)가 머신러닝 모형의 예측값에 기여한 정도를 정량적으로 분해하는 모형해석(explainability) 기법

- 특징(feature)을 "게임 참가자", 예측결과를 "총 보수(payoff)"로 간주하고 각 특징의 기여도(SHAP value)를 계산
- Random Forest·XGBoost 등 블랙박스 모형의 내부 의사결정 로직을 사후적으로 설명
- 공정성 공리(axiom of fairness) 충족, 전역적(global)·국소적(local) 해석 모두 가능, 모델 비의존적(model-agnostic)

---

## SHAP value 해석

**부호(+/-)**
: 해당 변수가 예측치를 증가시키는 방향인지(+) 감소시키는 방향인지(-)를 나타냄 → 변수와 종속변수 간 장기적 방향성(양/음의 상관관계) 판단

**절대값 크기 |SHAP value|**
: 예측에 대한 기여 강도(중요도)를 나타냄 → 변수중요도 순위 산정 기준

---

## 전체 표본기간 중요도 산출 절차

월별 검증셋(validation set)에서 SHAP value 및 |SHAP value|의 평균 계산
↓
전체 샘플기간에 대해 월별 결과를 재평균(aggregate)
↓
평균 SHAP value → 변수의 장기적 방향성(양/음의 상관관계) 판단 기준
평균 |SHAP value| → 변수의 전체 예측기여도(중요도 순위) 판단 기준

---

## 활용 사례

- Wu et al.(2025) 회사채 신용스프레드 예측모형: RF 모형 기준 상위 20개 변수 중 비재무지표(G-score, 소유성격, 정보공시평가, 최대주주 지분율 등)가 최상위를 차지함을 SHAP로 규명
- 롤링윈도우·재귀윈도우 등 학습방식이 달라져도 SHAP 기준 비재무지표의 중요도 순위는 상대적으로 안정적으로 유지됨 → 비재무지표가 특정 학습설정에 의존하지 않는 견고한 예측신호임을 시사

## 장점

- 이론적 엄밀성(Shapley value의 공정성 공리)과 직관적 이해가능성을 동시에 만족
- 예측 정확도가 높은 복잡한 앙상블 모형(RF, GBDT, XGBoost 등)에도 적용 가능해, "정확도-해석가능성"의 트레이드오프를 완화

## 인과 사슬

[[신용스프레드]] · [[통화정책]]

> 사슬 미작성. 위 링크를 **방향이 있는 문장**으로 다시 쓸 것 —
> 원인 노드 ↑ → 전달 경로 → 결과 노드 ↑ 형태로 화살표를 넣고,
> 그 아래 `**Comment**:` 줄에 현재 레짐에서 이 사슬이 갖는 의미를 적는다.
> 작성 예시는 _System/Templates/T_Paper.md 참조.
