---
title: A Reformulation of the Quantity Theory of Money — Globalization, Digitalization, and Exchange
type: paper
journal: Modern Economy, 16(9) (2025), pp. 1420-1436. DOI 10.4236/me.2025.169066 (SCIRP 오픈액세스)
date: 2025-09
author: Miguel Angel Temprano (Universidad Internacional de La Rioja, UNIR, Madrid)
created: 2026-08-04
status: done
verification: full
reliability: research
verified: 원문 대조(2026-08-04, pymupdf 전문 추출 17p — 초록·서론 정독. 추정표 개별 계수는 미대조)
source_file: me_7204071.pdf
tags: [type/paper, domain/inflation, domain/liquidity, region/us, method/GLS, method/NeweyWest, method/VAR, method/log-log]
concepts: [화폐수량설, REER, KOF지수, IDI, 화폐유통속도, SQTM, 연준대차대조표]
related: ["[[2022 What does machine learning say about the drivers of inflation (Kohlscheen, BIS WP 980)]]", "[[2019 On the Monetary Measures of Global Liquidity (Hashmi & Bhatti)]]", "[[2016 기대인플레이션을 이용한 미국 중장기 인플레이션 예측 (최준)]]"]
---

# A Reformulation of the Quantity Theory of Money (Temprano, 2025)

> ⚠ **게재지 주의.** Modern Economy(SCIRP)는 심사 강도가 낮은 것으로 알려진 오픈액세스 저널이다.
> 결과를 인용하기 전에 **재현 가능성과 데이터 출처를 직접 확인**해야 한다. `reliability: research`.

> 질문 자체는 이 vault의 관심사와 정확히 겹친다 —
> **"연준이 대차대조표를 그렇게 늘렸는데 왜 인플레이션이 오지 않았나."**

## 핵심 결과

**설계**
- 표본: **미국 분기 2000Q1 ~ 2024Q4**
- 고전적 화폐수량설(MV = PY)에 **21세기 구조 변수 3개**를 추가
  ① **실질실효환율(REER)** ② **세계화(KOF 지수)** ③ **디지털화(IDI 지수)**
- 추정: **log-log 모형 + GLS·Newey-West 보정**, 인과는 **VAR(3)** 로 검정
- 확장 모형을 **SQTM**(Structural/Expanded QTM)이라 명명

**① 인과 방향**
- **REER ↔ 인플레이션: 양방향**
- **M2 → 물가: 단방향** (역방향은 성립하지 않음)

**② 계수**
- **실질 1% 절하 → CPI +0.21%p**
- **세계화(KOF)·디지털화(IDI) 진전 → 지속적인 디스인플레이션 압력**

**③ 성능**
- 고전 QTM 및 **필립스 곡선 VAR** 대비 예측 **RMSE 40% 감소**, 조정 R² **0.87**

**④ 정책 함의(저자)**
중앙은행은 **REER · KOF · IDI · 화폐유통속도**를 함께 모니터링하고, **유연한 물가목표**를 채택하며,
환율 정책과 조율해야 한다.

## 모형 선택의 근거

저자의 문제의식은 **"통화량이 늘어도 물가가 오르지 않은 20년"** 이다.
고전 QTM은 유통속도(V)를 상수로 가정하는데, 세계화·디지털화가 V와 가격 전가를 구조적으로 바꿨다고 본다.
그래서 V를 상수로 두는 대신 **V에 영향을 주는 구조 변수(KOF·IDI)와 대외가격 경로(REER)를 명시적으로 넣는다.**

## 인과 사슬

[[M2 · Divisia 통화량]] ↑ → (단방향) → [[CPI (소비자물가지수)]] ↑
**단 세계화·디지털화가 동시에 진전되면** → 유통속도·가격전가 하락 → 물가 상승분이 상쇄

실질실효환율 절하(1%) → 수입물가 ↑ → [[CPI (소비자물가지수)]] **+0.21%p**
→ 그리고 물가가 오르면 다시 환율에 영향(**양방향**)

세계화(KOF) ↑ · 디지털화(IDI) ↑ → 경쟁 심화·거래비용 하락 → **지속적 디스인플레이션 압력**

**Comment**: 이 논문의 주장은 [[글로벌 유동성]]·[[M2 · Divisia 통화량]] 노드가 안고 있던 질문
— "통화량과 물가의 관계가 왜 끊겼나" — 에 **구조 변수로 답하려는 시도**다.
방향은 [[2022 What does machine learning say about the drivers of inflation (Kohlscheen, BIS WP 980)]]의
**글로벌 요인(유가·글로벌 PPI) 중요성**과 정합적이다.
다만 게재지 신뢰도와 아래 Red Team 항목 때문에 **이 vault에서는 "가설"로 취급**하고,
수치를 인용할 때는 반드시 재현 여부를 확인할 것.

## 저자가 밝힌 한계

초록·서론 범위에서는 **명시적 한계 서술이 확인되지 않는다.** 결론은 정책 권고로 마무리된다.

## 검증 필요 · 반박 포인트 (Red Team)

**① 게재지 신뢰도**
SCIRP 계열 저널은 **심사 강도와 편집 기준에 대한 비판**이 반복적으로 제기돼 왔다.
동일 결과가 주류 저널이나 중앙은행 워킹페이퍼에서 재현됐는지 확인 전에는 **근거로 인용하지 말 것.**

**② R² 0.87과 RMSE −40%는 과적합 신호일 수 있다**
분기 100개(2000~2024) 표본에 log-log + 구조 변수 다수를 넣으면 적합도는 쉽게 올라간다.
**표본외 검증 설계**(롤링/확장 윈도우)가 명시되지 않으면 "RMSE 40% 감소"는 표본내 개선일 가능성이 있다.
→ [[무작위 분할로 잰 out-of-sample은 시계열에서 성과가 아니다]]

**③ KOF·IDI는 저빈도·완만한 추세 변수다**
세계화·디지털화 지수는 **거의 단조 추세**를 그린다. 추세 변수를 넣으면 log-log 회귀에서
**공적분 없는 허구회귀(spurious regression)** 위험이 커진다. 단위근·공적분 검정 제시 여부 확인 필요.

**④ "디스인플레이션 압력"의 식별**
2000~2024년은 세계화·디지털화가 진전된 동시에 **중국 편입·기술 충격·인구구조 변화**가 겹친 기간이다.
KOF·IDI 계수가 그 셋을 **모두 흡수한 잔여물**일 수 있다.

**⑤ 필립스 곡선 VAR을 벤치마크로 삼은 방식**
비교 대상 필립스 VAR의 사양이 무엇인지에 따라 "40% 개선"의 의미가 완전히 달라진다.
[[2022 Advances in estimating the Phillips curve (Guirguis & Suen)]]가 보였듯 **필립스 곡선은 사양에 따라 성능이 크게 달라진다.**

## 관련 개념

[[M2 · Divisia 통화량]] · [[글로벌 유동성]] · [[CPI (소비자물가지수)]] · [[통화정책]] · [[DXY (달러지수)]]

## 관련 MOC

- [[지표 MOC]] · [[원문검증 논문 MOC]]
