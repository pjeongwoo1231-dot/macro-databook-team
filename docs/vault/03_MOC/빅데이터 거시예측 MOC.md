---
title: 빅데이터 거시예측 MOC
type: MOC
tags: [type/MOC]
concepts: [빅데이터, nowcasting, 거시예측]
---

# 빅데이터 거시예측 MOC

정우형님자료2/3 폴더의 논문·리포트 13건을 지식카드형 노트(부모 13 + 자식 10 = 23건)로 변환한 모음. 다섯 갈래 — ① GDP·경기 nowcasting, ② 심리지수·센티먼트, ③ 인플레이션·통화정책·원자재, ④ 신용시장, ⑤ 채권시장 리포트 — 로 묶인다.

## 1. GDP·경기 Nowcasting

- [[K-SuperCast]] — 금융감독원 빅데이터 GDP 적시예측 시스템 (Choi 2019)
- [[딥러닝 시계열 모형을 이용한 당분기 GDP 예측 성능 분석]] — ETRI GRU 앙상블 딥러닝 GDP 예측 (Lee et al. 2022)
- [[빅데이터를 이용한 실시간 민간소비 예측]] — 한국은행/고려대 MIDAS+ML 민간소비 nowcasting (Shin & Seo 2024)
- [[공식발표 통계지표의 적시성 확보를 위한 대안 데이터 파이프라인 구축제안]] — 실시간 대안데이터 파이프라인 제안 서베이 (Cho & Kim 2023)
- 자식 개념: [[Nowcasting(경기 적시예측)]] · [[동적요인모형(Dynamic Factor Model)]] · [[MIDAS 혼합주기 회귀모형]] · [[대안데이터 파이프라인 구조]]

## 2. 심리지수·센티먼트

- [[한국 경제심리지수(ESI) 구축 (Moon 2011)]] — 한국 경제 ESI 구축
- 자식 개념: [[경제심리지수(ESI) 구축방법론]]

## 3. 인플레이션·통화정책·원자재

- [[부문별 인플레이션을 이용한 테일러 준칙 추정]] — 한국은행 주현도 (2024)
- [[핵심인플레이션(Core Inflation) 지표 개발 (Lee, Lee & Kim, 2003)]]
- [[통화정책-원자재 가격 연계성 서베이 (Bohl, Humann & Siklos 2025)]]
- [[중앙은행 커뮤니케이션과 수익률곡선 (NMF 토픽모델링, Crayton 2018)]]
- 자식 개념: [[테일러 준칙(Taylor Rule)]] · [[핵심인플레이션(Core Inflation) 추정방법 개관]] · [[비음수행렬분해(NMF) 토픽모델링 방법론]]

## 4. 신용시장

- [[The Impact of Credit Market Sentiment Shocks]] — Boeck & Zörner (2023/2024), JMCB
- [[머신러닝 기반 회사채 신용스프레드·신용등급 예측 (비재무 데이터의 역할)]] — Wu et al. (2025)
- 자식 개념: [[진단적 기대(Diagnostic Expectations)]] · [[SHAP(SHapley Additive exPlanations) 방법론]]

## 5. 채권시장 리포트

- [[채권 잔혹기, 시장에 머물러야 하는 이유]] — SC제일은행 박순현
- [[Weekly Market (2024년 6월 4주 국내외 증시 동향)]] — 더스쿠프 주간 시황

## 주제 간 연결

- **빅데이터·대체정보 방법론**: [[Nowcasting(경기 적시예측)]] ↔ [[동적요인모형(Dynamic Factor Model)]] ↔ [[MIDAS 혼합주기 회귀모형]] ↔ [[비음수행렬분해(NMF) 토픽모델링 방법론]] ↔ [[SHAP(SHapley Additive exPlanations) 방법론]] — 모두 "구조화되지 않은/고빈도 데이터를 어떻게 경제지표로 압축하는가"라는 공통 문제의식
- **심리·기대의 시장 영향**: [[경제심리지수(ESI) 구축방법론]] ↔ [[진단적 기대(Diagnostic Expectations)]] — 심리·기대 변수가 실물·신용시장에 선행지표로 작용
- **통화정책 파급경로**: [[테일러 준칙(Taylor Rule)]] ↔ [[통화정책-원자재 가격 연계성 서베이 (Bohl, Humann & Siklos 2025)]] ↔ [[핵심인플레이션(Core Inflation) 추정방법 개관]] ↔ [[중앙은행 커뮤니케이션과 수익률곡선 (NMF 토픽모델링, Crayton 2018)]] — 정책금리 결정(테일러 준칙)부터 커뮤니케이션 효과까지 통화정책의 파급 경로
- **자본시장연구원 심리지수와의 연결**: [[The Impact of Credit Market Sentiment Shocks]] ↔ [[26-01 자본시장 심리지수 시리즈1 - 구축과 활용]] — 신용시장 심리 vs 자본시장 심리지수, 유사한 텍스트/데이터 기반 심리지수 구축 방법론
