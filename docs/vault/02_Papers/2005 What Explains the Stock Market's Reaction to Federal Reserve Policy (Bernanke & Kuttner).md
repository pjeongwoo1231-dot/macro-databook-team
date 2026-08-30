---
title: What Explains the Stock Market's Reaction to Federal Reserve Policy
type: paper
journal: Journal of Finance, Vol. 60, No. 3, pp. 1221-1257
date: 2005
author: Ben S. Bernanke, Kenneth N. Kuttner
created: 2026-08-12
updated: 2026-08-12
status: done
verification: none
reliability: academic
verified: "❌ 원문 미대조. 카카오톡 수신 노트(2026-08-12 임포트)를 볼트 규약으로 정규화한 것 — 수치·표현은 원문 확보 후 재검증 필요"
source_file: 없음 (외부 작성 노트 수신)
tags: [type/paper, domain/asset, domain/policy, region/us, method/이벤트스터디, method/고빈도식별, flag/unverified]
concepts: [monetary-policy-surprise, equity-premium, Fed-funds-futures, event-study]
import_origin: 카카오톡 수신 — Macro Paper Notes / 원본 파일명 'Bernanke & Kuttner (2005) — What Explains the Stock Market's Reaction to the Federal Reserve.md'
duplicate_of: "[[2005 What Explains the Stock Market's Reaction to Federal Reserve Policy (Bernanke & Kuttner) — 정본]]"
---

> ⚠ **이 노트는 [[2005 What Explains the Stock Market's Reaction to Federal Reserve Policy (Bernanke & Kuttner) — 정본]]으로 대체됐다.**
> 이 문서는 2026-08-12 카카오톡으로 수신한 외부 노트를 정규화한 것이고 **원문 대조가 안 돼 있다**(verification: none).
> 2026-08-13에 Wiley 게재본 37쪽 전문을 대조한 **정본이 따로 있으므로 판정에는 정본만 쓴다.**
> 이 노트는 **수신 이력 보존용**으로만 남긴다 (2026-08-19 확인).


> 🔴 **정본이 생겼다 (2026-08-13). 이 카드를 인용하지 말 것.**
> **정본**: [[2005 What Explains the Stock Market's Reaction to Federal Reserve Policy (Bernanke & Kuttner) — 정본]]
> (`verification: full` · J. of Finance 60(3) 게재본 37p 전문 대조, Free Access)
>
> **원문 대조 결과 — 이 카드의 핵심 주장은 정확했다.** 오류는 없고 **누락**이 있다.
>
> | 누락 항목 | 원문 |
> |---|---|
> | 표본기간 | **1989년 6월(첫 이벤트: 25bp 인하) ~ 2002년 12월 FOMC** |
> | 주가지수 | **CRSP 가치가중지수**, 1일 수익률 |
> | 핵심 보조결과 | **"예상된 부분에는 시장이 거의 반응하지 않는다"** — 서프라이즈 측정의 자체 타당성 검증 |
> | 이벤트 정의 | 목표금리 변경일 ∪ FOMC 회의일. **2001-09-17 관측치 별도 취급** |
> | 강건성 | **월별 단위**에서도 유사한 반응 |
> | 분해 출처 | Campbell(1991) · **Campbell & Ammer(1993)** VAR |


﻿---
tags:
  - macro/monetary-policy
  - asset-prices
  - stock-market
  - event-study
  - high-frequency
aliases:
  - "Bernanke Kuttner 2005"
  - "Fed Stock Market"
year: 2005
author: "Bernanke & Kuttner"
---

# What Explains the Stock Market's Reaction to the Federal Reserve

## 1. Bibliographic Information

- **Title:** What Explains the Stock Market's Reaction to Federal Reserve Policy?
- **Authors:** Ben S. Bernanke, Kenneth N. Kuttner
- **Year:** 2005
- **Journal / Working Paper:** Journal of Finance, Vol. 60, No. 3, pp. 1221-1257
- **Research Field:** Financial Economics, Monetary Economics
- **Keywords:** monetary policy surprise, stock market, equity premium, event study, Fed funds futures, high-frequency identification, asset pricing

### One-Sentence Thesis
이 논문은 **Fed funds futures로 측정한 예상치 못한 통화 정책 완화 25bp**가 **주식 위험 프리미엄 감소 채널**을 통해 **약 1%의 주가 상승**을 초래함을 이벤트 스터디로 보여준다.

---

## 2. Research Question

- **Question 1:** 예상치 못한 통화 정책 변화가 주식 시장에 미치는 효과는 얼마인가?
- **Question 2:** 어떤 채널(기대 배당, 실질 금리, 위험 프리미엄)을 통해 주가가 반응하는가?

---

## 3. Literature Gap

**Existing Literature**
- 통화 정책-주가 관계 이론: 현금흐름 할인 모형; 실질 금리 채널; 기대 배당 채널
- 기존 실증: 통화 정책과 주가의 단순 상관관계; 내생성 문제

**Limitation**
- 예측된 통화 정책과 예상치 못한 변화를 구분하지 않음; 인과 식별 어려움

**Contribution of This Paper**
- Fed funds futures를 사용한 예상치 못한(surprise) 통화 정책 충격 식별; 채널 분해 (기대 배당 vs. 실질 금리 vs. 위험 프리미엄)

---

## 4. Core Mechanism

```
Cause / Shock: 예상치 못한 Fed funds rate 인하 (25bp 완화 surprise)
      ↓
Expected Dividends Channel: 낮은 금리 → 기업 투자 확대 → 미래 기대 이익 상승
      ↓
Real Interest Rate Channel: 낮은 할인율 → 미래 현금흐름의 현재 가치 상승
      ↓
Equity Risk Premium Channel: (주요 채널) 낮은 금리 → 경제 불확실성 감소 → 위험 프리미엄 하락 → 주가 상승
      ↓
Stock Market: 약 1% 주가 상승 (25bp surprise 당)
```

**Economic Logic**
- P = sum D_t / (1+r+rp)^t; r 하락 또는 rp 하락 또는 D_t 상승 → P 상승
- 실증: 기대 배당 채널이 아닌 위험 프리미엄 감소가 주된 메커니즘

---

## 5. Shock Classification

- [ ] Demand Shock
- [ ] Supply Shock
- [x] Monetary Shock
- [ ] Fiscal Shock
- [ ] Credit Shock
- [x] Financial Shock
- [ ] Commodity Shock
- [ ] Technology Shock
- [ ] Productivity Shock
- [ ] Trade Shock
- [ ] Capital Flow Shock
- [ ] Expectation Shock

**Primary Shock:** 예상치 못한 통화 정책 충격 (Fed funds futures surprise)

---

## 6. Transmission Mechanism

```
Shock: 예상치 못한 25bp 금리 인하
  ↓
Signal Channel: 연준이 경기에 대해 긍정적 신호 (또는 완화적 입장)
  ↓
Risk Premium Channel: 경제 불확실성 감소 → 투자자 위험 회피 하락 → 주식 위험 프리미엄 하락
  ↓
Discount Rate Effect: 실질 금리 하락 + 위험 프리미엄 하락 → 할인율 하락 → 주가 상승
  ↓
Real Economy: [추론] 높은 주가 → Tobin's q 상승 → 기업 투자 증가 (대차대조표 채널)
```

---

## 7. Key Variables

**Macroeconomic**
- 통화 정책 surprise: Fed funds futures (당월물) 기반 측정
- 실질 GDP 성장률, 기업 이익 성장률

**Financial**
- S&P 500 및 섹터별 주가; CRSP 포트폴리오
- 기대 배당 성장률, 실질 이자율, 주식 위험 프리미엄 (Campbell-Shiller 분해)
- Fed funds futures rate (예상치 못한 변화 식별)

**Leading / Coincident / Lagging**
- 주가 반응: 즉각 (당일, 고빈도)
- 실물 효과: lagging

---

## 8. Empirical Strategy

- **Data:** FOMC 발표일 주가 데이터; Fed funds futures 가격; 1989-2002
- **Sample Period:** 1989-2002 (38 FOMC 회의)
- **Country / Region:** 미국
- **Frequency:** 일별 (event study); 고빈도 (30분 창)
- **Method:** 이벤트 스터디; OLS 회귀; Campbell-Shiller 분산 분해
- **Identification Strategy:** Fed funds futures로 예상치 못한 충격 분리 (Kuttner 2001)
- **Main Model:** DELTA_S = alpha + beta*DELTA_i_surprise + epsilon

**Correlation or Causality?**
- 고빈도 이벤트 스터디 → 인과 관계 식별 (단기 창 내 역인과 없음)

---

## 9. Main Findings

1. [논문 직접] 예상된 통화 정책 변화는 주가에 유의미한 영향 없음; 예상치 못한 완화만 유의
2. [논문 직접] 예상치 못한 25bp 금리 인하 → 약 1% 주가 상승 (OLS 추정)
3. [논문 직접] 주된 채널: 기대 배당이나 실질 금리가 아니라 주식 위험 프리미엄 감소
4. [논문 직접] 섹터별 반응: 경기 민감 섹터 (기술주, 소비재) 반응 더 강함; 유틸리티 약함
5. [논문 직접] FOMC 발표 당일 주가 변동의 상당 부분이 통화 정책 surprise로 설명

---

## 10. Regime Dependency

**When is the effect stronger?**
- 경기 불확실성이 높을 때: 위험 프리미엄 채널 더 강하게 작동
- 기대 인플레이션이 낮고 통화 정책이 순환적 반응에 집중할 때

**When is the effect weaker?**
- ZLB 환경: 금리 surprise의 분산 자체가 작아짐 → 신호 채널이 중요해짐
- 정보 효과(information effect): 연준의 긍정 신호 → 주가 상승, 부정 신호 → 하락 (방향 혼재)

**Does the conclusion change across regimes?**
- 이후 연구: [[Miranda-Agrippino & Ricco (2021) — The Transmission of Monetary Policy Shocks]]에서 정보 효과 통제 후 더 명확한 인과 확인; [[2005 Do Actions Speak Louder Than Words (Gürkaynak, Sack & Swanson)]]에서 forward guidance 효과 추가

---

## 11. Asset-Price Implications

**Bonds**
- [추론] 예상치 못한 금리 인하 → 단기 채권 가격 상승; 기대 경기 개선 → 장기 채권 반응 혼재 (성장 기대 상승 vs. 할인율 하락)

**Equities**
- [논문 직접] 예상치 못한 25bp 완화 → ~1% 주가 상승; 주된 채널은 위험 프리미엄
- [논문 직접] 경기 민감 섹터가 더 강하게 반응 (베타 높은 섹터)

**FX**
- [추론] 예상치 못한 완화 → 달러 약세 (금리 차익 감소); 단기 환율 반응

**Credit**
- [추론] 위험 프리미엄 감소 → 크레딧 스프레드 축소 (주식 위험 프리미엄과 동방향)

> 반드시 [논문에서 직접 주장한 내용]과 [우리의 추론]을 구분한다.

---

## 12. Falsification Conditions

**What would confirm the hypothesis?**
- 고빈도 창에서 예상치 못한 완화와 주가 상승의 강한 양의 상관관계
- Campbell-Shiller 분해에서 위험 프리미엄 항이 통화 충격에 더 강하게 반응

**What would falsify the hypothesis?**
- 예상치 못한 통화 정책이 주가에 유의미한 영향 없음; 위험 프리미엄 채널 통계적 비유의

**Variables to monitor**
- VIX (위험 프리미엄 proxy), Fed funds futures surprise, S&P 500 당일 반응, TIPS yield

---

## 13. Contradictory / Alternative Literature

**Supporting Papers**
- Kuttner (2001): Fed funds futures 기반 통화 정책 surprise 측정 방법 제시
- Gürkaynak, Sack & Swanson (2005): path factor (forward guidance)까지 확장

**Contradictory Papers**
- [[Miranda-Agrippino & Ricco (2021) — The Transmission of Monetary Policy Shocks]]: 정보 효과 통제 전 surprise 측정이 편향 → 수정 필요
- Cieslak & Vissing-Jorgensen (2021): 연준의 정보가 주가에 미치는 영향 재검토

---

## 14. Connections to Other Papers

**SUPPORTS**
- [[1995 Inside the Black Box - The Credit Channel of Monetary Policy Transmission (Bernanke & Gertler)]]: 자산 가격 채널 (대차대조표 채널) 실증
- [[2005 Do Actions Speak Louder Than Words (Gürkaynak, Sack & Swanson)]]: forward guidance 효과 추가

**EXTENDS**
- Kuttner (2001): Fed funds futures 방법론을 주식 시장으로 확장

**APPLIES**
- 주식 시장의 통화 정책 민감도 측정; 중앙은행 커뮤니케이션 효과 분석

---

## 15. Zettelkasten Atomic Notes

### ZK Note 1
**Claim:** 예상된 통화 정책이 아닌 예상치 못한 surprise만이 자산 가격에 영향을 준다.
**Mechanism:** 효율적 시장 가설: 예측 가능한 정책 → 이미 가격에 반영 → 발표 시 추가 영향 없음; 오직 surprise만이 가격 조정 유발
**Evidence:** [직접] 예상된 Fed 정책 변화와 주가 간 상관관계 통계적 비유의; surprise와는 유의한 양의 상관
**Implication:** 중앙은행 커뮤니케이션의 중요성: 정책 예측 가능성 높이면 발표 시 시장 충격 감소; 그러나 동시에 정책 신호 가치 상승
**Connected Notes:** [[2005 Do Actions Speak Louder Than Words (Gürkaynak, Sack & Swanson)]], [[Miranda-Agrippino & Ricco (2021) — The Transmission of Monetary Policy Shocks]]

### ZK Note 2
**Claim:** 통화 정책의 주가 영향 주요 채널은 기대 배당이나 실질 금리가 아니라 주식 위험 프리미엄이다.
**Mechanism:** Campbell-Shiller 분산 분해: 주가 변동 = 기대 배당 변동 + 실질 금리 변동 + 위험 프리미엄 변동; 통화 충격 → 위험 프리미엄 항이 지배적
**Evidence:** [직접] 분산 분해 분석; 위험 프리미엄 채널이 통계적으로 가장 유의미
**Implication:** 통화 정책은 금리 채널뿐 아니라 투자자 위험 선호 변화를 통해 주가에 영향; QE의 "risk-taking channel" 이론적 근거
**Connected Notes:** [[1999 The Science of Monetary Policy - A New Keynesian Perspective (Clarida, Galí & Gertler)]]

### ZK Note 3
**Claim:** 섹터별 통화 정책 민감도는 경기 민감도(beta)와 양의 관계이다.
**Mechanism:** 완화 → 위험 프리미엄 감소 → 고베타 섹터 더 수혜; 긴축 → 반대
**Evidence:** [직접] 기술주, 소비재: 강한 반응; 유틸리티, 필수소비재: 약한 반응
**Implication:** 통화 정책 사이클과 섹터 로테이션 전략: 완화 → 성장주·경기민감주 매수; 긴축 → 방어주·가치주 이동
**Connected Notes:** [[1995 Inside the Black Box - The Credit Channel of Monetary Policy Transmission (Bernanke & Gertler)]]

---

## 16. One-Sentence Takeaway

이 논문을 한 문장으로 기억한다면: **연준이 예상치 못하게 금리를 0.25%포인트 내리면 주가가 약 1% 오르는데, 이는 기업 이익 기대보다는 투자자들의 위험 회피 감소(주식 위험 프리미엄 하락) 때문이다.**

---

## Quality Control

- [x] 논문의 핵심 주장을 정확하게 이해했는가?
- [x] 기존 연구와 무엇이 다른지 설명했는가?
- [x] Shock을 분류했는가?
- [x] Transmission mechanism을 화살표로 표현했는가?
- [x] 인과관계와 상관관계를 구분했는가?
- [x] 논문의 실증 결과와 우리의 해석을 구분했는가?
- [x] Regime dependency를 검토했는가?
- [x] Asset-price implication을 도출했는가?
- [x] Falsification condition을 제시했는가?
- [x] 반대되는 연구를 확인했는가?
- [x] 다른 논문과 연결했는가?
- [x] Atomic note로 분해했는가?
- [x] 한 문장으로 핵심을 설명할 수 있는가?

---

## 관련 MOC

- [[매크로 고전 논문 MOC]] · [[리포트 수집 큐]]
