---
title: "The Limited Effects of Post-Pandemic U.S. Monetary Policy Tightening"
type: paper
series: Bank of Japan Working Paper No.26-E-6
date: 2026-04
author: Bank of Japan 조사통계국
url: https://www.boj.or.jp/en/research/wps_rev/
tags: [type/paper, method/FAVAR, method/local-projection, domain/policy]
concepts: [통화정책 전달, 수요구성, 신용경로, 초과채권프리미엄, 구성효과, 무형자산투자]
source_file: 06_SourceArchive/05-Primary-PDFs/2024-2026/BOJ-WP-26e06.pdf
status: done
verification: full
reliability: working-paper
text_basis: local-pdf
verified: 원문 대조 완료(2026-08-14). 로컬 PDF 판독 — FAVAR·ST-LP·EBP(Favara et al 2016) 전이변수·구성효과 결론 확인
related: ["[[2012 Credit Spreads and Business Cycle Fluctuations (Gilchrist & Zakrajsek)]]", "[[신용스프레드의 정보는 기대부도가 아니라 잔차에 있다]]", "[[Monetary-Policy-Transmission-and-International-Spillovers]]", "[[원문 아카이브 MOC]]"]
---

# 통화정책이 약해진 게 아니라 경제의 구성이 바뀌었다 (BOJ, 2026)

> Bank of Japan Working Paper Series No.26-E-6, 2026년 4월.
> 저자 견해이며 일본은행의 견해가 아니다.

## 왜 중요한가 — 우리 문제와 직결

**볼트의 신용스프레드 라인과 정면으로 이어진다.**
[[2012 Credit Spreads and Business Cycle Fluctuations (Gilchrist & Zakrajsek)]]가
초과채권프리미엄(EBP)을 만들었고, 볼트 제텔
[[신용스프레드의 정보는 기대부도가 아니라 잔차에 있다]]가 그 핵심을 정리해 뒀다.
이 논문은 **그 EBP를 국면 전이변수로 써서** 통화정책 효과가 언제 강하고 언제 약한지를 가른다.
제텔이 "잔차에 정보가 있다"고 했다면, 이 논문은 **그 잔차로 정책 효과를 조건화한다.**

두 번째 이유 — "2022년 이후 그렇게 올렸는데 왜 미국이 안 무너졌나"는 지난 2년의 핵심 퍼즐이고,
[[2024-2026-Comparative-Mechanism-Map]]의 "긴축 이후 구조 변화" 슬롯에 실증을 넣는다.

## 방법과 자료

| 항목 | 내용 |
|---|---|
| 질문 | 2022년 이후 급속·대폭 긴축에도 미국 실물 하방압력이 제한적이었던 이유 |
| 방법 1 | **FAVAR** — GDP 수요항목별 통화정책 충격 반응의 이질성 |
| 방법 2 | **평활전이 국면회귀(ST-LP)** — Favara et al.(2016)의 **초과채권프리미엄(EBP)을 전이변수**로 써서 금융환경에 따른 시변 효과 추정 |
| 변수 처리 | 금리 등 퍼센트 표시 변수를 제외하고 전부 자연로그 |

## 원문에서 확인한 결과

**1. 수요항목별로 반응이 뚜렷이 다르다.**
- **눌리는 항목**: 내구재 소비, 주택투자, 비주거 유형자산 투자
- **거의 안 눌리는 항목**: **서비스 소비, 무형자산 투자**

**2. 구성효과(composition effect)가 답이다.** 최근 미국 경제에서 서비스 소비와
무형자산 투자의 비중이 커졌고, 그것이 거시 전체의 통화정책 민감도를 낮췄다.

> 정책 **효과 자체가 약해진 것이 아니라**, 눌리지 않는 항목의 몫이 커진 것이다.

**3. 신용경로가 작동하는 국면에서만 강하게 눌린다.** ST-LP 결과, **차입의존도가 높은
수요항목**은 신용경로가 잘 작동하는 국면(EBP 기준)에서 긴축 효과가 유의하게 더 강했다.
반대로 서비스 소비·무형자산 투자처럼 **차입의존도가 낮은 항목은 금융환경 국면과 무관하게**
반응이 작았다.

## 한계와 적용 범위

- **사서(추가)**: FAVAR의 통화정책 충격 식별은 표준 가정에 의존한다. 볼트의
  [[고빈도 통화 서프라이즈는 충격의 자격을 갖추지 못했다 — 자기상관되고 예측 가능하다]]가
  제기한 식별 문제가 여기에도 적용될 수 있다
- **사서(추가)**: **구성효과와 정책효력 약화는 관측적으로 구분하기 어렵다.** 저자는 전자로
  결론짓지만, 항목별 계수 자체가 시간에 따라 변했을 가능성을 완전히 배제하려면
  항목별 시변 추정이 더 필요하다
- **사서(추가)**: 미국 데이터다. 한국은 **가계부채·변동금리 비중과 주택 익스포저가 커서**
  차입의존 항목의 몫이 다르다. 같은 논리를 쓰면 **한국의 정책 민감도는 미국보다 높다**는
  예측이 나오고, 그것 자체가 검증 대상이다
- **사서(추가)**: 무형자산 투자가 정말 금리에 둔감한지는 자금조달 구조(내부유보·주식)에
  달려 있다. 조달환경이 바뀌면 둔감성도 바뀔 수 있다

## 인과 사슬

[[기준금리]] 급속 인상 → 차입의존 항목(내구재·[[주택가격]] 연계 투자) 위축
→ **그러나** 서비스 소비·무형자산 투자는 무반응
→ 두 항목의 경제 내 비중 상승 = **구성효과**
→ 거시 전체 민감도 하락 → [[산업생산]]·[[GDP 성장률]] 하방압력 제한
→ 단, [[신용스프레드]](EBP)가 벌어진 국면에서는 차입의존 항목이 더 크게 눌림

**Comment**: 실무적 함의는 **"금리 몇 %p 올렸다"로 긴축 강도를 재지 말라**는 것이다.
같은 인상폭이라도 **경제의 구성**과 **EBP 국면**에 따라 실물 효과가 달라진다.
[[Monetary-Policy-Transmission-and-International-Spillovers]]가 "정책금리만으로 스탠스를
판단하지 말라"고 한 것의 정량판이며, 판단에 쓸 조건변수를 하나 준다 —
[[신용스프레드]]를 수준이 아니라 **국면 스위치**로 읽을 것.

## 관련 개념

- EBP의 원전 — [[2012 Credit Spreads and Business Cycle Fluctuations (Gilchrist & Zakrajsek)]]
- 잔차에 정보가 있다 — [[신용스프레드의 정보는 기대부도가 아니라 잔차에 있다]]
- 예측 시계 — [[신용스프레드의 예측 시계는 2주가 아니라 12개월이다 — 무엇을 예측하느냐에 달렸다]]
- 전파 메커니즘 — [[Monetary-Policy-Transmission-and-International-Spillovers]] · [[2024-2026-Comparative-Mechanism-Map]]

## References

[1]: https://www.boj.or.jp/en/research/wps_rev/wps_2026/data/wp26e06.pdf "Bank of Japan WP 26-E-6, The Limited Effects of Post-Pandemic U.S. Monetary Policy Tightening"
