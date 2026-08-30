---
title: 2018 High-Frequency Identification of Monetary Non-Neutrality — The Information Effect (Nakamura & Steinsson)
type: paper
aliases:
  - "Nakamura & Steinsson (2018) — High-Frequency Identification of Monetary Non-Neutrality"
  - "Nakamura & Steinsson (2018)"
  - "NS 2018"
created: 2026-08-13
status: working
verification: full
author: Claude
source: "NBER WP 19260 (2013.7, 2018.1 개정, 74p). 최종본 QJE 133(3): 1283–1330 (2018). ⚠ WP 대조본"
reliability: working-paper
tags: [type/paper, domain/policy, region/us, method/고빈도식별, method/구조모형]
concepts: [정보효과, 통화 비중립성, 실질금리, BEI, 기간구조, 30분 창]
related: ["[[기준금리]]", "[[통화정책]]", "[[BEI (기대인플레이션)]]", "[[장단기 금리차]]", "[[2021 The Transmission of Monetary Policy Shocks (Miranda-Agrippino & Ricco)]]"]
---

> ⚠ NBER WP 19260(2018.1 개정) 대조본. QJE 최종본과 수치가 다를 수 있다.

# High-Frequency Identification of Monetary Non-Neutrality: The Information Effect

## 1. 한 줄 명제

> **연준 발표는 정책에 대한 정보만 전달하는 게 아니라 경제 펀더멘털에 대한 믿음까지 바꾼다.**
> 그 증거는 **긴축 발표 후 산출 전망이 오히려 올라간다**는 것이다 — 표준 모형이 예측하는 것의 정반대.

## 2~3. 연구 질문 · 문헌 공백

식별 가정: **예정된 연준 발표 전후 30분 창의 예상 밖 금리 변화 = 통화정책 뉴스.**
그런데 그 "뉴스"가 무엇에 관한 뉴스인지는 가정하지 않는다. 이 논문은 **그 안에 무엇이 들어 있는지**를 묻는다.

## 4. 핵심 메커니즘

```
연준 발표
   ├─ ① 정책 충격 → 실질금리 ↑ → 산출 ↓   (표준 경로)
   └─ ② **경제 펀더멘털에 대한 연준의 믿음** 전달 → 민간의 산출 전망 ↑
                    ↓
관측: 긴축 후 **산출 성장 전망이 오른다** ← ②가 ①을 압도하는 부분이 있다
```

## 5. 충격 분류
**주 충격 = 통화충격 + 기대충격(정보효과).** 둘이 **분리되지 않은 채** 발표에 실려 있다.

## 6~9. 실증 · 주요 결과

| | |
|---|---|
| 식별 | 예정 FOMC 발표 전후 **30분 창** 금리 변화 |
| 관측 대상 | **실질금리 · 기대인플레(BEI) · 기대 산출성장** |

**① 명목·실질금리가 거의 1:1로 함께 오른다 — 기간구조상 수년 뒤까지**
*"nominal and real interest rates increase roughly **one-for-one, several years out into the
term structure**"*

**② 기대인플레 반응은 작다**
*"the response of expected inflation is **small**"*
→ 실질금리가 움직이는 것이므로 **통화 비중립성**이 확인된다. 이 논문 제목의 절반이 이것이다.

**③ 실질금리 효과는 약 2년에서 정점, 이후 10년까지 단조 감소해 0으로**
*"The effect on real rates peaks at around **2 years** and then falls monotonically to zero at **10 years**."*

**④ 그런데 산출 성장 전망이 함께 오른다 — 표준 모형과 정반대**
*"forecasts about output growth also increase—**the opposite of what standard models imply**
about a monetary tightening."*
→ 이것이 **정보효과의 직접 증거**다. 긴축이 성장을 올릴 리 없으므로,
발표가 **"연준이 경제를 좋게 본다"**는 신호를 함께 보낸 것이다.

**⑤ 모형화**: 연준 발표가 정책뿐 아니라 **다른 경제 펀더멘털에 대한 믿음**에도 영향을 주는 모형을 세운다.
결론: *"information effects play an **important role** in the overall causal effect of monetary
policy shocks on output."*

## 10. 레짐 의존성
정보효과의 크기는 **중앙은행의 정보우위**에 비례한다. 연준이 민간보다 아는 게 많을수록 커진다.
→ 커뮤니케이션이 투명해지고 예측이 공개될수록 정보효과는 **줄어야** 한다(이 논문이 검정한 바는 아니다).

## 11. 자산가격 함의
- **[논문 주장]** 실질금리는 2년 부근에서 가장 크게 반응하고 10년에서 0으로 수렴
- **[우리의 추론]** FOMC 발표일 커브 반응을 **정책 효과로만** 읽으면 안 된다.
  산출 전망 개선분이 섞여 있다

## 12. 반증 조건
- **확증**: 긴축 발표 후 산출 전망 상승이 반복 관측
- **반증**: 연준 사적정보를 통제하면 산출 전망 상승이 사라짐

## 13~14. 연결

**⚠ 볼트 내 기존 서술의 정정** — [[2005 Do Actions Speak Louder Than Words (Gürkaynak, Sack & Swanson)]]
노트(원문 미대조 임포트)는 NS(2018)을 **"정보 효과 통제 후에도 path factor 유의미"** 라며
**GSS를 옹호하는 근거**로 인용한다. **원문 대조 결과 그 성격 규정은 과하다.**
이 논문의 주 기여는 path factor의 생존이 아니라 **정보효과가 실재하고 중요하다는 것**이다.
→ 오히려 [[2021 The Transmission of Monetary Policy Shocks (Miranda-Agrippino & Ricco)]]의
비판을 **지지하는 쪽**에 가깝다.

**SUPPORTS**: MAR(2021)의 정보경직성·정보효과 문제 제기
**CRITIQUES**: 고빈도 서프라이즈를 순수 정책충격으로 쓰는 관행
**EXTENDS**: GSS(2005) 고빈도 식별 — 같은 창을 쓰되 **무엇이 들어 있는지**를 판다

## 15. 원문 대조에서 발견한 것
- **네 층 정합.** 초록의 세 사실(1:1 · 기대인플레 반응 작음 · 산출 전망 상승)이 본문과 일치
- **강점: 반직관적 결과를 숨기지 않았다.** "산출 전망이 오른다"는 표준 모형에 불리한 결과인데
  **그것을 핵심 증거로 전면에 세웠다**
- ⚠ **WP(2018.1) 대조본.** QJE 최종본 미확인
- ⚠ **정보효과의 크기를 이 노트에서 수치로 인용하지 않는다** — 해당 표를 직접 대조하지 않았다

## 16. 파생 제텔
- [[긴축 발표 뒤 산출 전망이 오른다 — 정보효과의 직접 증거]]

## 17. 한 문장 · 확신도

> **연준이 금리를 올리면 시장은 "긴축이다"와 "연준이 경제를 좋게 본다"를 동시에 듣는다.**

**확신도: 중상.** 식별이 명확하고 반직관적 결과를 정면으로 다뤘다.
**유보**: ① WP 대조본 ② 정보효과 크기의 구체 수치 미대조 ③ 30분 창 가정 자체는 이 논문도 유지한다.
