---
title: 2010 Liquidity and Leverage (Adrian & Shin)
type: paper
aliases:
  - "Adrian & Shin (2010) — Liquidity and Leverage"
  - "Adrian & Shin (2010)"
created: 2026-08-13
status: working
verification: full
author: Claude
source: "NY연준 Staff Report 328 (2008.5, 2010.12 개정, 39p). 최종본 Journal of Financial Intermediation 19(3): 418–437 (2010)"
reliability: working-paper
tags: [type/paper, domain/liquidity, domain/credit, domain/risk, region/us, method/시계열회귀]
concepts: [경기순응적 레버리지, 시가평가, 딜러 레포, 총유동성, VIX]
related: ["[[글로벌 유동성]]", "[[신용사이클]]", "[[VIX]]", "[[신용스프레드]]", "[[2012 Credit Spreads and Business Cycle Fluctuations (Gilchrist & Zakrajsek)]]"]
---

# Liquidity and Leverage

## 1. 한 줄 명제

> **시가평가 체제에서 자산가격 변화는 즉시 순자산 변화가 되고, 중개기관은 대차대조표 크기로 반응한다.**
> 그 결과 **레버리지가 경기순응적**이 되고, **딜러 레포 변화가 VIX 혁신을 예측한다.**

## 2~3. 연구 질문 · 문헌 공백

기존 관점: 레버리지는 역(逆)순응적이어야 한다 — 자산가격이 오르면 자기자본이 늘어 레버리지가 **떨어져야** 한다.
**데이터는 정반대다.** 중개기관이 대차대조표를 **능동적으로 관리**하기 때문이다.

## 4. 핵심 메커니즘

```
자산가격 ↑  → (시가평가) → 순자산 즉시 ↑ → 레버리지 일시 하락
        ↓
중개기관이 **목표 레버리지를 맞추려 자산을 더 산다** (대차대조표 확대)
        ↓
자산가격 ↑ 압력 → 순자산 ↑ → …  **양(+)의 되먹임**
        ↓
   호황엔 레버리지 높고 불황엔 낮다 = **경기순응적 레버리지**

※ 하락 국면에서는 같은 고리가 반대로 돈다 → 강제 축소 → 가격 추가 하락
```

저자 문장: *"leverage is high during booms and low during busts. That is, **leverage is procyclical**."*
그리고 이는 *"a consequence of the **active management of balance sheets**"* 다.

## 5. 충격 분류
**주 충격 = 금융충격.** 신용의 **공급 측 증폭기**를 다룬다.

## 6. 전달경로

```
자산가격 → 중개기관 순자산 → **딜러 레포**(조정의 주 마진) → 총 대차대조표
   → [[글로벌 유동성]] → 위험자산 가격 · [[VIX]]
```

## 7~9. 주요 결과

**① 시가평가 레버리지는 강하게 경기순응적이다**

**② 딜러 레포가 조정의 **주 마진**이다** — 총 대차대조표가 움직이는 통로

**③ 딜러 레포 변화가 금융시장 위험을 예측한다**
*"Changes in dealer repos... **forecast changes in financial market risk** as measured by the
innovations in the CBOE Volatility Index (**VIX**)."*
→ **레포가 VIX를 선행한다.** 수량이 가격 변동성을 앞선다.

**④ 총유동성의 정의**
*"Aggregate liquidity can be seen as **the rate of change of the aggregate balance sheet** of
the financial intermediaries."*
→ 유동성은 **수준이 아니라 변화율**이다. 통화량이 아니라 **중개기관 대차대조표의 증가율**.

## 10. 레짐 의존성
**시가평가 회계와 위험관리 모형(VaR)이 전제**다. 이 제도가 없으면 메커니즘이 약해진다.
→ 은행 중심 시스템보다 **딜러·시장기반 금융**에서 강하게 작동한다.

## 11. 자산가격 함의
- **[논문 주장]** 딜러 레포가 VIX를 선행한다
- **[우리의 추론]** [[VIX]]를 위험의 **원인**처럼 쓰면 안 된다. 레포·레버리지가 앞선다 →
  볼트의 "리스크를 단일 지표로 대리하지 않는다" 원칙의 구체적 확장
- **[우리의 추론]** 이것이 [[2012 Credit Spreads and Business Cycle Fluctuations (Gilchrist & Zakrajsek)]]의
  **EBP를 관측 가능하게 만드는 대리변수**다. GZ는 EBP를 "중개기관의 실효 위험부담능력"이라 해석하는데,
  **그 능력의 직접 관측치가 딜러 레버리지·레포**다

## 12. 반증 조건
- **확증**: 딜러 레포 축소가 VIX 상승·스프레드 확대에 선행
- **반증**: 레버리지가 역순응적이거나, 레포가 VIX를 선행하지 않음
- **감시**: **1차 딜러 레포 잔액** · 중개기관 총자산 증가율

## 13~14. 연결
**직계 후속**: [[2014 Procyclical Leverage and Value-at-Risk (Adrian & Shin)]] — **왜** 순응적인지의 계약이론
**보완**: [[2012 Credit Spreads and Business Cycle Fluctuations (Gilchrist & Zakrajsek)]] — 같은 대상의 **가격** 측정
**이론 배경**: Bernanke-Gertler(1989) · Kiyotaki-Moore(1997) — 단 이들은 **차입자** 순자산, 이 논문은 **대출자(중개기관)** 순자산

## 15. 원문 대조에서 발견한 것
- **네 층 정합.** 초록의 세 요소(순응적 레버리지 / 레포가 VIX 예측 / 유동성=변화율)가 본문과 일치
- **강점: 통념과 반대 방향임을 명시**하고 그 이유(능동적 관리)를 제시했다
- **강점: 유동성을 조작적으로 재정의**했다 — "변화율"이라는 정의는 측정 가능하다
- ⚠ **NY연준 Staff Report(2010.12 개정) 대조본**. JFI 최종본과 다를 수 있다
- ⚠ 표본이 **금융위기 전후**에 집중된다. 위기 국면 특수성 가능성

## 16. 파생 제텔
- [[유동성은 수준이 아니라 중개기관 대차대조표의 변화율이다]]

## 17. 한 문장 · 확신도

> **레버리지는 위험이 줄어서 오르는 게 아니라, 오르기 때문에 위험이 줄어 보인다.**

**확신도: 중상.** 사실 기록이 명확하고 조작적 정의를 제시했다.
**유보**: ① SR 대조본 ② 표본의 위기 편중 ③ 레포–VIX 선행이 **예측**이지 인과 식별은 아니다.
