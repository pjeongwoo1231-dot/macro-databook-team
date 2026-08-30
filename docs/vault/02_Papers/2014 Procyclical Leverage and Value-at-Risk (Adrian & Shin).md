---
title: 2014 Procyclical Leverage and Value-at-Risk (Adrian & Shin)
type: paper
aliases:
  - "Adrian & Shin (2014) — Procyclical Leverage and Value-at-Risk"
  - "Adrian & Shin (2014)"
created: 2026-08-13
status: working
verification: full
author: Claude
source: "NY연준 Staff Report 338 (2008.7, 2013.8 개정, 42p). 최종본 Review of Financial Studies 27(2): 373–403 (2014)"
reliability: working-paper
tags: [type/paper, domain/liquidity, domain/credit, domain/risk, region/us, method/계약이론, method/극단값이론]
concepts: [VaR, 경기순응적 레버리지, 일정 부도확률, 극단값이론, 디레버리징, 담보부차입]
related: ["[[글로벌 유동성]]", "[[신용사이클]]", "[[신용스프레드]]", "[[VIX]]", "[[2010 Liquidity and Leverage (Adrian & Shin)]]"]
---

# Procyclical Leverage and Value-at-Risk

## 1. 한 줄 명제

> **중개기관 레버리지는 VaR와 음(−)으로 정렬된다.**
> 이유는 중개기관이 **부도확률을 일정하게 유지**하기 때문이며,
> 그래서 위험이 커지는 국면에 **대규모 디레버리징**이 강제된다.

## 2~3. 연구 질문 · 문헌 공백

[[2010 Liquidity and Leverage (Adrian & Shin)]]이 **"레버리지가 순응적이다"** 는 사실을 기록했다.
이 논문은 **왜 그런가** — 계약이론으로 답한다.

## 4. 핵심 메커니즘

```
중개기관이 **일정한 부도확률**을 유지하려 한다 (계약 균형의 성질)
        ↓
자산 위험(VaR) ↑  →  같은 부도확률을 지키려면 자기자본 대비 자산을 줄여야 함
        ↓
   **레버리지 ↓**  → 자산 매각 → 가격 ↓ → 위험 추가 ↑ →  **되먹임**
        ↓
불황에 **대규모 디레버리징**

(호황: VaR ↓ → 같은 부도확률에서 레버리지 ↑ → 자산 매입 → …)
```

저자 문장: *"intermediary leverage is **negatively aligned with the banks' value-at-risk (VaR)**"* ·
*"intermediaries maintain a **constant probability of default** to shifts in the outcome
distribution, implying **substantial deleveraging during downturns**."*

## 5. 충격 분류
**주 충격 = 금융충격.** 위험 인식 변화가 신용공급을 움직인다.

## 6. 전달경로

```
자산 위험(VaR) ↑ → 일정 부도확률 제약 → 레버리지 ↓ → 신용공급 ↓
   → [[신용스프레드]] ↑ · [[글로벌 유동성]] ↓
```

## 7~9. 주요 결과

**① 실증: 레버리지와 VaR의 음(−) 정렬**

**② 이론: 극단값이론(EVT) 하의 일반 조건**
결과분포에 대한 EVT 조건 하에서 중개기관은 **부도확률을 일정하게 유지**한다.
→ 이것이 순응적 레버리지의 **미시적 근거**다.

**③ VaR 임계확률의 내생화**
일부 파라미터 영역에서 모형을 명시적으로 풀어 **VaR 문턱 확률 자체를 계약문제에서 도출**한다.
→ VaR 규제가 **외생적으로 부과된 제약이 아니라 최적계약의 결과**일 수 있다.

## 10. 레짐 의존성
**담보부차입(collateralized borrowing) 구조가 전제**다. 무담보·관계금융 중심 시스템에서는 약해진다.
그리고 **위험이 급변하는 국면일수록 메커니즘이 강해진다** — 평상시엔 조용하다.

## 11. 자산가격 함의
- **[논문 주장]** 불황기 디레버리징은 규모가 크고 강제적이다
- **[우리의 추론]** **VaR 기반 위험관리가 보편화될수록 시스템 전체가 동조화**된다.
  모두가 같은 신호에 같은 방향으로 반응 → 개별적으로 합리적인 위험관리가 **총량적으로 불안정**을 만든다
- **[우리의 추론]** [[VIX]] 상승이 **그 자체로** 신용공급을 줄인다 — 심리가 아니라 **제약**을 통해서다

## 12. 반증 조건
- **확증**: VaR 상승 국면에 레버리지가 유의하게 축소
- **반증**: 레버리지가 VaR와 무관하거나 양(+)으로 정렬
- **감시**: 딜러 레버리지 · [[VIX]] · 담보 헤어컷

## 13~14. 연결
**직계 선행**: [[2010 Liquidity and Leverage (Adrian & Shin)]] — 사실 → 이 논문이 이유
**보완**: [[2012 Credit Spreads and Business Cycle Fluctuations (Gilchrist & Zakrajsek)]] —
GZ가 2007–09에 **브로커-딜러 CDS 프리미엄 상승 → EBP 거의 1:1 동반 상승**을 보고한다.
**이 논문이 그 연결고리의 메커니즘**이다: 딜러 위험 ↑ → VaR ↑ → 디레버리징 → 위험가격 ↑ = EBP ↑
**이론 배경**: 담보제약 문헌(Kiyotaki-Moore) — 단 그쪽은 **차입자** 담보, 이쪽은 **대출자** 위험한도

## 15. 원문 대조에서 발견한 것
- **네 층 정합.** 초록의 실증(음의 정렬) → 이론(EVT, 일정 부도확률) → 내생화 순서가 본문과 일치
- **강점: 실증에서 출발해 모형으로 갔다** — *"Motivated by the evidence, we explore a contracting model"*.
  모형이 먼저가 아니다
- **강점: 해석 가능한 특수해를 제시**했다 — 일부 파라미터에서 명시적 풀이를 제공해 내생화를 보였다
- ⚠ **NY연준 SR(2013.8 개정) 대조본**. RFS 최종본(2014)과 다를 수 있다
- ⚠ **"일정 부도확률"은 EVT 조건 하의 결과**다. 조건이 안 맞으면 성립하지 않는다 —
  일반 명제가 아니라 **조건부 명제**로 인용할 것

## 16. 파생 제텔
- [[중개기관은 부도확률을 일정하게 유지하려다 불황에 디레버리징한다]]

## 17. 한 문장 · 확신도

> **개별 은행의 합리적 위험관리가 시스템 전체의 경기순응성을 만든다.**

**확신도: 중상.** 실증→이론 순서가 건전하고 조건을 명시했다.
**유보**: ① SR 대조본 ② **EVT 조건부** 결과 ③ 담보부차입 구조 전제.
