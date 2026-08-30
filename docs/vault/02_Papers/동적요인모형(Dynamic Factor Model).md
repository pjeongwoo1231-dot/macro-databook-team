---
title: 동적요인모형(Dynamic Factor Model, DFM)
type: concept
category: [계량경제모형, 거시경제]
tags: [type/paper, method/DFM, method/PCA, method/VAR 대안, method/칼만필터링, method/팩터모형]
concepts: [차원의 저주, EM알고리즘]
related: [Nowcasting(경기 적시예측), K-SuperCast, MIDAS 혼합주기 회귀모형, 공식발표 통계지표의 적시성 확보를 위한 대안 데이터 파이프라인 구축제안]
difficulty: Intermediate
paper: [Choi2019]
status: done
verification: n-a
---

## 정의

**동적요인모형(DFM)**
: 다수의 거시경제 시계열을 소수의 관측 불가능한 공통 팩터(factor)로 압축하고, 그 팩터를 통해 관심 변수(GDP 등)를 설명·예측하는 계량모형
- Stock & Watson(1999, 2011)이 제안, Giannone·Reichlin·Small(2008, GRS)이 GDP nowcasting에 도입하며 'Nowcasting'이라는 이름을 붙임

---

## 등장 배경 — VAR의 한계

- VAR(다변량 자기회귀)는 시계열 변수가 많아지면 추정할 모수 대비 자료가 부족 → 차원의 저주(curse of dimensionality)
- 변수를 줄이면 누락변수 편의(bias) 발생 → 모수 추정치가 일치성(consistency) 상실
- BVAR(베이지안 VAR)는 사전분포로 정보를 보완하지만, 사전분포 설정에 대한 의존도가 큼

---

## 모형 구조

```
Yt = μ + ΛFt + εt   (관측방정식: n개 거시변수 = 팩터의 선형결합 + 고유오차)
Ft = AFt-1 + But    (전이방정식: 팩터의 자기회귀)
```
- Yt: n×1 관측 가능한 거시변수 벡터
- Ft: r×1 관측 불가능한 잠재 팩터 (r ≪ n)
- Λ: 팩터적재행렬(factor loading), 각 변수와 팩터의 상관관계

---

## 추정 흐름 (Two-step 업데이팅 접근법)

```
① PCA로 다수 거시변수 → 소수 팩터 추출 (동조성 높은 변수 묶음)
↓
② 팩터-관심변수(GDP) 관계를 회귀로 추정 (일치성 있는 모수, Doz et al. 2005)
↓
③ 칼만필터링으로 신규 발표자료를 팩터에 실시간 반영(업데이트)
↓
GDP 성장률 nowcast 산출
```

---

## 장점

- 정보손실을 최소화하며 혼합주기·ragged-edge 문제를 결측 형태로 자연스럽게 처리
- 다중공선성·차원의 저주 완화 (수십~수백 개 변수를 3~4개 팩터로 압축)
- 팩터적재값으로 어떤 경제부문이 GDP를 움직이는지 해석 가능 → 정책적 시사점 도출 용이

---

## 대안 추정법: EM 알고리즘

- Two-step(PCA + 회귀 + 칼만필터링) vs EM알고리즘(Banbura et al. 2011) 비교
- EM알고리즘: 관측 안 된 변수를 우회한 최우추정, 신규 자료 반영 시 과거 팩터값도 재추정하는 **칼만 스무딩(Kalman smoothing)** 특성
- Two-step: 더 많은 자료를 활용 가능, 변수 개수가 늘어나도 상대적으로 안정적 → K-SuperCast는 Two-step을 기본 모형, EM을 보조 검증 수단으로 채택

---

## 실제 사례 — K-SuperCast의 팩터 해석 (2018년 기준)

- 팩터1(17%): 기업의 전망과 현재상황 (수출입, 가동률, BSI)
- 팩터2(13%): 건설 및 부동산 (전세/매매비율, 정부지출)
- 팩터3(12%): 임금 및 노동

2019.5월 갱신판에서는 China PMI, 미국 신규실업청구건수 등 해외변수가 팩터1·2에 새롭게 편입됨.

---

## 관련 노트
- [[Nowcasting(경기 적시예측)]]
- [[K-SuperCast]]
- [[MIDAS 혼합주기 회귀모형]]

## 인과 사슬

[[BSI (기업경기실사지수)]] · [[GDP 성장률]] · [[PMI (구매관리자지수)]] · [[통화정책]]

> 사슬 미작성. 위 링크를 **방향이 있는 문장**으로 다시 쓸 것 —
> 원인 노드 ↑ → 전달 경로 → 결과 노드 ↑ 형태로 화살표를 넣고,
> 그 아래 `**Comment**:` 줄에 현재 레짐에서 이 사슬이 갖는 의미를 적는다.
> 작성 예시는 _System/Templates/T_Paper.md 참조.
