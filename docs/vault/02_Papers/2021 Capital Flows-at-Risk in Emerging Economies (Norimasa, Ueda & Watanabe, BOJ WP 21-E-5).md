---
title: "Emerging Economies' Capital Flows-at-Risk"
type: paper
series: Bank of Japan Working Paper No.21-E-5
date: 2021
author: Yoshihiko Norimasa, Kazuki Ueda (Bank of Japan), Tomohiro Watanabe (Nissay)
url: https://www.boj.or.jp/en/research/wps_rev/
tags: [type/paper, method/quantile-regression, domain/capital-flows]
concepts: [자본흐름 위험, CFaR, 분위회귀, 꼬리위험, 신흥국, 정부부채]
source_file: 06_SourceArchive/05-Primary-PDFs/2019-2021/BOJ-WP-21E05.pdf
status: done
verification: full
reliability: working-paper
text_basis: local-pdf
verified: 원문 대조 완료(2026-08-14). 로컬 PDF 판독 — 16개 신흥국·패널 분위회귀·CFaR5/CFaR10·왜곡 t분포 확인
related: ["[[2020 Macroprudential Policies and Capital Controls against Volatile Inflows (Frost, Ito & van Stralen)]]", "[[Sudden-Stop-and-Bridge-Finance]]", "[[RegimeView 1.0 (2026-08-09)]]", "[[원문 아카이브 MOC]]"]
---

# 자본흐름을 평균이 아니라 꼬리로 본다 — CFaR (Norimasa, Ueda & Watanabe, 2021)

> Bank of Japan Working Paper No.21-E-5. 저자 견해이며 일본은행 견해가 아니다.

## 왜 중요한가 — 우리 문제와 직결

**방법론이 본체다.** 이 논문은 자본흐름의 **평균**이 아니라 **하위 꼬리**를 추정한다 —
Capital Flows-at-Risk(CFaR). Growth-at-Risk·Debt-at-Risk와 같은 계열이다.

[[RegimeView 1.0 (2026-08-09)]]가 6차 개정에서 자인한 결함이 정확히 이것이었다 —
*"현재 트리거 10개는 전부 '언제/무엇이 바뀌나'를 묻는다. **'바뀌면 얼마나 아픈가'를 묻는
트리거가 하나도 없다.**"* 8차 개정에서 BIS credit-to-GDP gap으로 신용 쪽 심각도 축을 채웠는데,
**자본흐름 쪽 심각도 축이 이것**이다. 특히 **T8(원·달러 1,480)**은 임계 하나뿐인데,
CFaR는 그 임계가 얼마나 깊게 뚫릴 수 있는지를 분포로 답한다.

[[2020 Macroprudential Policies and Capital Controls against Volatile Inflows (Frost, Ito & van Stralen)]]가
"어떤 도구가 유입 **규모**를 줄이나"를 물었다면, 이 논문은 "유출의 **꼬리**가 무엇에 반응하나"를 묻는다.

## 방법과 자료

| 항목 | 내용 |
|---|---|
| 대상 | **신흥 16개국** |
| 방법 | **패널 분위회귀**. 자본흐름 분포에 **왜곡 t분포**를 적합시키고 하위 분위를 추정 |
| 지표 정의 | **CFaR** = 자본흐름이 해당 백분위 아래로 떨어질 꼬리위험. **CFaR5**(5%)·**CFaR10**(10%) 두 종 |
| 설명변수 | 선진국 **금융여건**, **미국 통화정책 스탠스**, 그리고 구조적 취약성 대용으로 **정부부채** |

## 원문에서 확인한 결과

**1. 선진국 금융여건과 미국 통화정책 스탠스 변화가 일부 국가의 대규모 유출 위험을 움직인다.**

**2. 상호작용이 핵심이다.** 특히 **미국 통화정책 스탠스가 크게 변하는 국면에서**
선진국 금융여건이 긴축되면 신흥국 CFaR에 유의한 영향을 준다.
→ 두 변수를 따로 보면 안 되고 **국면 조건부로** 봐야 한다.

**3. 정부부채를 구조적 취약성 지표로 넣으면** 국가별 CFaR 차이가 설명된다.

## 한계와 적용 범위

- **사서(추가)**: 분위회귀는 **조건부 분포**를 추정할 뿐 인과가 아니다. "선진국 여건이
  꼬리를 만든다"가 아니라 "꼬리가 그 변수와 함께 움직인다"까지가 정확하다
- **사서(추가)**: 왜곡 t분포 적합은 **분포 가정**이다. 표본이 짧은 신흥국에서 꼬리 모수 추정은
  불안정하다 — 하필 가장 알고 싶은 부분이 가장 부정확하다
- **사서(추가)**: 표본이 **2021년 이전**이다. 2022년 미국 급속 긴축기의 유출은 안 들어 있다.
  이 논문의 "미국 스탠스 변화 국면" 상호작용을 **검증할 최적 표본이 그 이후**에 있다
- **사서(추가)**: 16개국에 한국이 포함되는지는 원문 국가목록에서 확인 필요. 포함되지 않으면
  한국 적용은 재추정이 전제다

## 인과 사슬

선진국 [[신용스프레드]]·금융여건 긴축 + **미국 [[통화정책]] 스탠스 전환 국면**
→ 신흥국 자본흐름 **하위 꼬리** 확대(CFaR5/CFaR10)
→ (정부부채가 높을수록 꼬리가 더 두꺼움) → [[재정정책]] 여력이 완충을 결정
→ [[원·달러 환율]] 압력 → [[Sudden-Stop-and-Bridge-Finance]] 진입 조건

**Comment**: 실무 번역은 이렇다 — **T8을 임계 하나로 두지 말고 분포로 보라.**
"1,480을 넘느냐"가 아니라 "지금 국면에서 하위 5%가 어디냐"를 물어야 한다.
그리고 이 논문의 상호작용 결과대로면, **미국 스탠스 전환 국면에서는 같은 금융여건 긴축도
꼬리를 더 크게 벌린다.** 평온기 임계를 전환기에 그대로 쓰면 늦는다.

## 관련 개념

- 심각도 축 — [[RegimeView 1.0 (2026-08-09)]] 6차·8차 개정
- 도구 쪽 — [[2020 Macroprudential Policies and Capital Controls against Volatile Inflows (Frost, Ito & van Stralen)]]
- 메커니즘 — [[Sudden-Stop-and-Bridge-Finance]] · [[2019-2021-Comparative-Mechanism-Map]]
- 지표 — [[원·달러 환율]] · [[신용스프레드]] · [[재정정책]]

## References

[1]: https://www.boj.or.jp/en/research/wps_rev/wps_2021/data/wp21e05.pdf "Norimasa, Ueda and Watanabe (2021), Emerging Economies' Capital Flows-at-Risk, BOJ WP 21-E-5"
