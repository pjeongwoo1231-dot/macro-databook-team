---
title: 2011 A Model of Unconventional Monetary Policy (Gertler & Karadi)
type: paper
aliases:
  - "Gertler & Karadi (2011) — A Model of Unconventional Monetary Policy"
  - "Gertler & Karadi (2011)"
  - "GK 2011"
created: 2026-08-13
status: working
verification: partial
author: Claude
source: "저자 원고 (NYU, 2009.4, 33p). 최종본 Journal of Monetary Economics 58(1): 17–34 (2011). ⚠ 2009 원고 대조본 — ScienceDirect 접근 불가로 Berkeley 미러 사용"
reliability: working-paper
tags: [type/paper, domain/policy, domain/credit, domain/liquidity, region/us, method/DSGE]
concepts: [비전통적 통화정책, 중앙은행 신용정책, 내생적 대차대조표 제약, 금융중개, 위기 시뮬레이션]
related: ["[[통화정책]]", "[[신용사이클]]", "[[신용스프레드]]", "[[글로벌 유동성]]", "[[2014 Procyclical Leverage and Value-at-Risk (Adrian & Shin)]]"]
---

> ⚠ **2009년 4월 저자 원고** 대조본(Berkeley 미러). JME 최종본(2011)과 다를 수 있다.

# A Model of Unconventional Monetary Policy

## 1. 한 줄 명제

> **금융중개기관이 내생적 대차대조표 제약에 묶인 정량적 DSGE**를 세우고,
> **중앙은행이 민간대출을 직접 중개하는 정책**(연준이 서브프라임 위기에 개발한 비전통적 정책의 본질)이
> 위기를 얼마나 완화하는지를 **수치적으로** 평가한다.

## 2~3. 연구 질문 · 문헌 공백

2008년 연준은 전례 없는 일을 했다 — **민간신용을 직접 매입·중개**했다.
표준 모형에는 이 정책이 들어갈 자리가 없다. 금융중개가 마찰 없이 가정되기 때문이다.
→ **중개기관을 명시적으로 넣고, 그 제약을 내생화**해야 정책을 평가할 수 있다.

## 4. 핵심 메커니즘

```
금융중개기관이 **내생적 대차대조표 제약**에 직면
   (자기자본 대비 얼마나 자산을 들 수 있는지가 균형에서 정해짐)
        ↓
위기 충격 → 중개기관 순자산 ↓ → 제약 강화 → 신용공급 ↓ → 스프레드 ↑
        ↓
   실물 투자 ↓ → 순자산 추가 ↓ →  **되먹임**
        ↓
[정책] **중앙은행이 직접 중개** — 중앙은행은 이 제약에 안 묶인다
        ↓
   민간 중개 능력 부족분을 대체 → 스프레드 ↓ → 위기 완화
```

저자 문장: *"a quantitative monetary DSGE model that allows for financial intermediaries that
face **endogenous balance sheet constraints**"* ·
*"the effect of **direct central bank intermediation of private lending**, which is the essence
of the unconventional monetary policy that the Federal Reserve has developed"*

## 5. 충격 분류
**주 충격 = 금융충격.** 정책 도구는 **신용정책(credit policy)** — 금리정책과 구분된다.

## 6. 전달경로

```
위기 → 중개기관 순자산 ↓ → 대차대조표 제약 ↑ → [[신용스프레드]] ↑ → 투자 ↓
   [정책 개입] 중앙은행 직접 중개 → 실효 중개능력 ↑ → 스프레드 ↓ → 완화
```

## 7~9. 주요 결과

**① 위기 시뮬레이션이 실제 침체의 기본 특징을 재현한다**
**② 중앙은행 신용정책이 시뮬레이션된 위기를 **수치적으로** 완화한다**
**③ 정책의 작동 원리**: 중앙은행은 민간 중개기관과 달리 **대차대조표 제약이 없다** —
그래서 민간 중개능력이 붕괴한 국면에서만 **비교우위**를 갖는다

## 10. 레짐 의존성
**결정적이다.** 중앙은행 신용정책의 편익은 **민간 중개 제약이 구속될 때만** 발생한다.
정상 국면에서는 중앙은행이 민간보다 중개를 잘할 이유가 없다 → **위기 한정 도구**다.

## 11. 자산가격 함의
- **[논문 주장]** 신용정책이 스프레드를 낮춰 위기를 완화한다
- **[우리의 추론]** **금리정책과 신용정책은 다른 도구**다. 정책금리가 하한에 없어도
  중개 제약이 구속되면 신용정책이 유효할 수 있다 — **두 축을 따로 봐야 한다**
- **[우리의 추론]** 이 모형이 [[2012 Credit Spreads and Business Cycle Fluctuations (Gilchrist & Zakrajsek)]]의
  **EBP를 이론적으로 정당화**한다. EBP = 중개기관 실효 위험부담능력의 가격 측 측정치이고,
  GK의 대차대조표 제약이 **그 능력의 모형 대응물**이다

## 12. 반증 조건
- **확증**: 중개 제약이 구속된 국면에서 신용정책이 스프레드를 유의하게 낮춤
- **반증**: 제약 유무와 무관하게 효과가 동일하거나 없음
- **감시**: 딜러 레버리지 · **EBP** · 중개기관 자기자본

## 13~14. 연결
**미시 기초 공급**: [[2014 Procyclical Leverage and Value-at-Risk (Adrian & Shin)]] —
GK의 "내생적 대차대조표 제약"의 **관측 대응물**이 VaR 제약과 딜러 레버리지다
**이론 계보**: [[1989 Agency Costs, Net Worth, and Business Fluctuations (Bernanke & Gertler)]] —
같은 저자(Gertler)의 가속기를 **차입자 → 중개기관**으로 옮긴 것
**실증 짝**: [[2011 The Effects of Quantitative Easing on Interest Rates (Krishnamurthy & Vissing-Jorgensen)]] ·
[[2013 Flow and Stock Effects of Large-Scale Treasury Purchases (D'Amico & King)]] —
GK는 **모형**, 저 둘은 **실증**. 세 편이 QE 3부작을 이룬다
**통화 쪽 대비**: [[2003 The Zero Bound on Interest Rates and Optimal Monetary Policy (Eggertsson & Woodford)]] —
EW는 **기대 관리**로, GK는 **대차대조표 개입**으로 하한 문제에 답한다. **다른 도구**

## 15. 원문 대조에서 발견한 것
- **네 층 정합.** 초록의 세 단계(모형 → 위기 시뮬 → 정책 평가)가 본문 구조와 일치
- **강점: 정책의 본질을 특정**했다 — 비전통적 정책을 "돈 풀기"가 아니라
  **"중앙은행의 직접 중개"** 로 정의하고 그 조건(민간 제약 구속)을 명시했다
- ⚠ **2009년 4월 원고**다. JME 게재는 2011년 — **2년 격차** 동안 개정됐을 가능성.
  **계수·시뮬레이션 수치 인용 시 최종본 확인 필수**
- ⚠ **정량 모형이지만 캘리브레이션 기반**이다. "위기의 기본 특징을 재현했다"는 것은
  **독립 예측이 아니라 맞춘 결과**일 수 있다 →
  [[RBC의 산출 변동성은 예측이 아니라 캘리브레이션 제약이다]] 계열의 유보
- ⚠ ScienceDirect 접근 불가로 **Berkeley 미러**를 썼다. 출처 경로를 기록해둔다

## 16. 파생 제텔
- [[중앙은행 신용정책은 민간 중개가 막혔을 때만 비교우위를 갖는다]]

## 17. 한 문장 · 확신도

> **비전통적 통화정책의 본질은 돈을 푸는 것이 아니라, 중앙은행이 은행을 대신해 직접 중개하는 것이다.**

**확신도: 중.** 정책 정의와 조건이 명확하다.
**유보**: ① **2009 원고 대조본**(2년 격차) ② **캘리브레이션 기반**이라 독립 검증 아님
③ 미러 소스 사용.
