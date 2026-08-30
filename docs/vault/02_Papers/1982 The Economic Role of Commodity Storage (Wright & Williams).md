---
title: "The Economic Role of Commodity Storage"
type: paper
journal: The Economic Journal 92(367), 596–614 (Sep 1982) · 초고 Yale Economic Growth Center Discussion Paper No. 385 (1981)
date: 1982
author: Brian D. Wright (UC Berkeley) · Jeffrey C. Williams
url: https://academic.oup.com/ej/article-abstract/92/367/596/5220325
tags: [type/paper, method/합리적기대, method/수치해석, domain/commodities]
concepts: [경쟁적저장, 재고 비음제약, 가격분포 비대칭, 안정화]
status: done
verification: partial
reliability: academic
text_basis: cited-primary
verified: "△ 서지 확정(2026-08-18) — RePEc(ecj/econjl/v92y1982i367p596-614)·Oxford Academic으로 권·호·면수 대조, Yale EGC DP #385(1981)가 초고임을 확인. **본문 미열람** — Oxford는 초록만 공개, Yale 원문 PDF는 403. **수치 인용 금지**"
promoted_from: "[[L232 The Economic Role of Commodity Storage]]"
related: ["[[1984 The Welfare Effects of the Introduction of Storage (Wright & Williams)]]", "[[1991 Storage and Commodity Markets (Williams & Wright)]]", "[[1992 On the Behaviour of Commodity Prices (Deaton & Laroque)]]", "[[1996 Competitive Storage and Commodity Price Dynamics (Deaton & Laroque)]]", "[[원자재 재고]]"]
---

# 저장은 안정화 장치가 아니라 **가격 분포를 비대칭으로 만드는 장치**다 (Wright & Williams, 1982)

> Economic Journal 92(367) 596–614.
> ⚠ **본문 미열람.** 서지·위치까지만 대조했다. **수치는 인용하지 않는다.**

## 왜 중요한가 — 우리 문제와 직결

이 논문은 볼트가 이미 갖고 있는 두 축의 **연결 고리**다.

- 아래쪽: [[1992 On the Behaviour of Commodity Prices (Deaton & Laroque)]] ·
  [[1996 Competitive Storage and Commodity Price Dynamics (Deaton & Laroque)]] — 경쟁적 저장 모형의 **추정·검정**
- 위쪽: [[1984 The Welfare Effects of the Introduction of Storage (Wright & Williams)]] — 같은 모형의 **후생·분배**

1982년 논문은 그 사이, 즉 **"저장이 시장에서 하는 일이 정확히 무엇인가"** 를 정식화한 자리에 있다.

## 논지 (초록·이차문헌 수준)

- 저장은 **공급과 소비의 시간 불일치를 흡수**한다. 그러나 **재고는 음수가 될 수 없다**
- 이 비음 제약 때문에 저장의 효과가 **비대칭**이 된다 — 재고가 넉넉할 때는 가격을 눌러주지만
  **재고가 고갈되면 완충이 사라져 가격이 튄다**
- 따라서 저장이 있는 시장의 가격은 **평시 낮은 변동 + 드문 급등**이라는 우편향 분포를 갖는다
- 저장 가능성은 **생산 결정 자체를 바꾼다** — 안정화 정책 평가에서 이 반응을 빼면 결과가 달라진다

⚠ 위 네 줄은 **본문이 아니라 초록·후속 문헌이 이 논문에 귀속시키는 내용**이다.
숫자·모수·정리 번호는 원문 확보 후에 채운다.

## 우리 시스템에 적용

1. **[[원자재 재고]]의 "재고는 증폭기다" 절에 이론적 근거를 붙인다** — 재고 수준이 낮을수록
   같은 공급 충격이 더 큰 가격 반응을 만든다는 서술의 출처가 이 계열이다
2. [[구리 가격]]·[[WTI (국제유가)]]의 **급락·급등 비대칭**을 "시장 심리"로 설명하지 않는다 —
   **비음 제약이라는 기술적 이유**가 먼저다
3. [[선물 곡선 (Futures Curve)]]의 백워데이션 논쟁과 연결된다 — 재고가 마르면 곡선이 뒤집힌다

## Red Team

1. **본문 미열람이다.** 이 노트의 서술은 후속 문헌이 이 논문에 부여한 표준적 요약이며,
   **원문이 실제로 어디까지 증명했는지는 확인하지 않았다.** 인용 시 "본문 미대조" 꼬리표를 붙인다
2. 초고(Yale EGC DP #385, 1981)와 게재본(1982) 사이에 **내용 차이가 있을 수 있다.** 둘을 같은 것으로 인용하지 않는다
3. 경쟁적 저장 모형은 **Deaton-Laroque가 실증적으로 부분 기각**했다(자기상관을 다 설명하지 못함) —
   이 논문의 기제를 현실 가격에 그대로 대응시키면 안 된다
4. **농산물 중심 문헌**이다. 금속·에너지는 저장비용 구조·창고 접근성이 달라 그대로 옮기기 어렵다

## 인과 사슬

```
확률적 공급 + 합리적 기대 + 경쟁적 저장
        ↓
재고 **비음 제약** (재고는 음수가 안 된다)
        ↓
   ┌─ 재고 충분 → 완충 작동 → 가격 변동 축소
   └─ 재고 고갈 → 완충 소멸 → **가격 급등**
        ↓
가격 분포의 **비대칭(우편향)** + 자기상관
        ↓
저장 가능성이 **생산 결정**에 되먹임
```

## Comment

**다음 배치의 재작업 1순위 후보**다 — 원문을 구하면 ① 비음 제약의 정식화 ② 생산 반응의 처리
③ Deaton-Laroque가 이 모형의 무엇을 검정했는지 세 가지를 확인해 `full`로 올린다.
현재 등급으로는 **기제 서술까지만 인용 가능**하다.

## 관련 노트

- [[1984 The Welfare Effects of the Introduction of Storage (Wright & Williams)]]
- [[1991 Storage and Commodity Markets (Williams & Wright)]]
- [[원자재 재고]] · [[Library MOC]]
