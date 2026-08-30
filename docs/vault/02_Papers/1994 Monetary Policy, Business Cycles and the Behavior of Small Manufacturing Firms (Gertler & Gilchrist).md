---
title: "Monetary Policy, Business Cycles, and the Behavior of Small Manufacturing Firms"
type: paper
journal: Quarterly Journal of Economics 109(2), 309–340 (1994) · 판독본은 NBER WP 3892 (1991)
date: 1994
author: Mark Gertler, Simon Gilchrist
doi: 10.2307/2118465
url: https://www.nber.org/papers/w3892
tags: [type/paper, domain/monetary, domain/credit, method/time-series, method/firm-size]
concepts: [신용시장 불완전성, 금융가속기, 통화정책 전달경로, 기업규모별 반응, 은행대출 채널]
status: done
verification: full
reliability: academic
text_basis: full-text
verified: "✅ 2026-08-28 NBER WP 3892 공개본 **전문 판독**(약 7.8만 자). 서지 Crossref 확정(10.2307/2118465). **판독본은 QJE 최종본이 아니라 1991년 WP본**. 1991년 스캔본이라 OCR 오탈자가 있다"
promoted_from: "[[Library MOC]]"
related: ["[[Library MOC]]", "[[2020 The Housing Boom and Bust - Model Meets Evidence (Kaplan, Mitman & Violante)]]", "[[통화정책]]"]
---

# 긴축은 작은 기업부터 때린다 (Gertler & Gilchrist, 1994)

> QJE 109(2). **금융가속기 문헌의 출발점** 중 하나다.
> 제조업을 대·소기업으로 나눠, 통화정책 충격에 대한 반응 차이를 본다.

## 네 가지 발견

1. **긴축 이후 소기업 매출이 대기업보다 빠르게 감소**하며, 그 상태가 **2년 이상** 지속된다
2. **★ 은행 대출이 소기업에는 축소되는 반면, 대기업에는 오히려 증가한다**
3. **M2처럼 은행 성과와 연동된 통화정책 지표는 대기업보다 소기업에 대해 상대적으로 예측력이 크다**
4. 소기업이 대기업보다 **GNP의 시차 움직임에 더 민감**하다

소기업이 경제에서 결코 작지 않은 비중을 차지한다는 점을 고려하면,
저자들은 이를 **신용시장 불완전성의 거시적 중요성**을 시사하는 증거로 해석한다.

## 우리 볼트에 쓰는 법

이건 **유동성 축을 읽는 방법**에 관한 논문이다.

1. **★ 총량으로는 긴축 효과가 안 보인다.** 대기업 대출이 늘고 소기업 대출이 줄면
   **총 대출은 별로 안 변한다.** 그래서 "대출이 안 줄었으니 긴축이 안 먹혔다"는 판정은 틀린다
   → **채점 규칙 13 후보: 긴축·완화의 효과를 채점할 때 총량이 아니라 **분포(규모별·신용등급별)** 를 본다.**
   우리 DataBook에 **기업규모별/신용등급별 대출·스프레드 계열**이 있는지 점검할 것
2. **시차가 2년 이상**이다. 우리 코퍼스의 통화정책 관련 forecast에서 `horizon`이 6개월~1년이면
   **이 논문의 기저율보다 짧다** — 미실현을 실패로 채점하지 않도록 주의해야 한다
3. 이 구조는 [[2020 The Housing Boom and Bust - Model Meets Evidence (Kaplan, Mitman & Violante)]]와 대조하면 흥미롭다 —
   그쪽은 **가계** 신용조건이 가격을 움직이지 못한다고 했고, 이쪽은 **기업** 신용조건이 실물을 움직인다고 한다.
   **모순이 아니다. 대체 수단(임대시장)이 있느냐 없느냐가 갈랐다.**
   → 일반 원칙: **신용채널의 강도는 차입자가 가진 대안의 수에 반비례한다**

## Red Team

1. **1991년 집필, 미국 제조업 자료**다. 금융구조가 크게 바뀌었다 —
   회사채 시장 확대, 사모대출, 핀테크 대출은 이 표본에 없다.
2. **기업규모를 신용제약의 대리변수**로 쓴다. 규모가 작다고 반드시 제약이 큰 것은 아니며,
   이후 문헌은 **연령·레버리지·등급**을 더 나은 대리변수로 본다.
3. 식별이 **VAR/예측회귀 기반**이며, 현대적 통화정책 충격 식별(고빈도 서프라이즈)을 쓰지 않는다.
4. M2의 예측력은 **1990년대 이후 크게 약화**됐다 — 이 결과를 현재 지표 선택의 근거로 쓰면 안 된다.
5. 판독본이 **WP본**이라 QJE 최종본과 표·수치가 다를 수 있다.
