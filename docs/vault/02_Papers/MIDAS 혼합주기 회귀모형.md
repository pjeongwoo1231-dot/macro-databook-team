---
title: MIDAS 혼합주기 회귀모형(Mixed Data Sampling)
type: concept
category: [계량경제모형, 거시경제]
tags: [type/paper, method/LASSO, method/MIDAS, method/벌점화회귀, method/커널분위수회귀]
concepts: [혼합주기, 교량방정식, 가중치함수, SCAD]
related: [Nowcasting(경기 적시예측), 빅데이터를 이용한 실시간 민간소비 예측, 공식발표 통계지표의 적시성 확보를 위한 대안 데이터 파이프라인 구축제안, 동적요인모형(Dynamic Factor Model)]
difficulty: Intermediate
paper: [Shin2024]
status: done
verification: n-a
---

## 정의

**MIDAS(Mixed Data Sampling) 회귀모형**
: 종속변수보다 관측주기가 빠른(고빈도) 설명변수를, 별도의 분기화(집계) 없이 시차-가중치함수를 통해 직접 회귀모형에 포함시키는 부분모형(partial model)
- Ghysels, Santa-Clara & Valkanov(2004) 제안
- 교량방정식(bridge equation)의 확장형: 교량방정식은 고빈도 자료를 단순평균해 주기를 맞추지만, MIDAS는 평균의 가중치 자체를 자료로부터 학습

---

## 왜 필요한가 — 혼합주기 문제

```
GDP·민간소비(분기 관측) vs 카드소비·검색량(월/일 관측)
↓
단순 평균·집계 시 고빈도 자료의 정보 손실
↓
MIDAS: 시차별 가중치 w(j; β)를 모수화하여 정보 손실 최소화
```

---

## 모형 구조 (개념)

```
φ(L)yt = ρ0 + Σk ψ(L^(1/mk); θk) xt,k + εt
```
- xt,k: yt보다 mk배 빠른 고빈도 공변량
- θj,k = w((j-1)/mk; βk): 기저함수(constant / linear / harmonic 등)로 표현된 가중치함수
- 최종적으로 yt = bᵀzt + εt 형태의 선형모형으로 재표현 가능 → 다양한 추정법 적용 가능

---

## 고차원 확장과 기계학습 결합

- Babii, Ghysels & Striaukas(2022): 고차원 MIDAS-회귀 + 벌점화 최소제곱(LASSO/SCAD)
- yt = f(zt) + εt 로 확장하면 비선형 함수 f를 다양한 ML 기법으로 추정 가능
  - 벌점화 선형모형: LASSO, elastic net, SCAD(편향 감소)
  - 단일지표모형 + 충분차원축약(SDR)
  - 커널분위수회귀(KQR) — 데이터 바깥쪽 끝부분(nowcasting 대상)을 예측하는 데 상대적으로 강건
  - 랜덤포레스트 등 비선형 앙상블

---

## 실무적 유의점

- 가중치함수 복잡도(기저함수 개수 D)를 높이면, 공변량이 많을 때 오히려 모형 분산이 커져 nowcasting 성능이 저하될 수 있음
- 초고차원(변수 ≫ 표본)에서는 **변수선별(feature screening)**을 MIDAS 적합 전에 선행해야 성능이 크게 개선됨
  - 근거: Fan & Lv(2008)의 sure screening property — 종속변수와 개별 공변량의 주변연관성만으로도 신호변수를 제거할 확률이 0으로 수렴

---

## 결합모형(DFM) 대비 장단점

- 장점: 계산이 효율적이고 대용량 빅데이터로 확장하기 쉬움 (결합모형은 계산비용이 커짐)
- 단점: ragged-edge 문제 해결을 위해 별도의 결측 대체가 필요, 변수-종속변수 관계의 정량화가 DFM보다 어려움

---

## 관련 노트
- [[Nowcasting(경기 적시예측)]]
- [[동적요인모형(Dynamic Factor Model)]]
- [[빅데이터를 이용한 실시간 민간소비 예측]]
