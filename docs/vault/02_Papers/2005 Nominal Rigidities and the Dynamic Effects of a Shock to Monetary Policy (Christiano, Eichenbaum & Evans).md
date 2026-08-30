---
title: 2005 Nominal Rigidities and the Dynamic Effects of a Shock to Monetary Policy (Christiano, Eichenbaum & Evans)
type: paper
aliases:
  - "Christiano, Eichenbaum & Evans (2005) — Nominal Rigidities and the Dynamic Effects of a Shock to Monetary Policy"
  - "Christiano, Eichenbaum & Evans (2005)"
  - "CEE 2005"
created: 2026-08-13
status: working
verification: partial
author: Claude
source: "NBER WP 8403 (2001, 48p). 최종본 Journal of Political Economy 113(1): 1–45 (2005). ⚠ WP 대조본 — **OCR 복원**(TeX 폰트 ToUnicode 부재, Tesseract 5.4 250dpi)"
reliability: working-paper
tags: [type/paper, domain/policy, domain/inflation, region/us, method/DSGE, method/VAR, method/최소거리추정]
concepts: [명목경직성, 임금 시차계약, 가변 자본가동률, 한계비용, 물가 관성, 산출 지속성]
related: ["[[통화정책]]", "[[기준금리]]", "[[핵심인플레이션]]", "[[설비가동률]]", "[[산업생산]]"]
---

> ⚠ **OCR 복원 노트.** 원 PDF는 TeX 폰트에 ToUnicode 맵이 없어 일반 추출이 불가능했다.
> Tesseract 5.4 · 250dpi 복원. 본문 서술은 양호하나 **수식·표의 계수는 인용하지 않는다.**

# Nominal Rigidities and the Dynamic Effects of a Shock to Monetary Policy

## 1. 한 줄 명제

> **물가는 왜 천천히 움직이고 산출은 왜 오래 지속되는가.**
> 답은 "명목경직성을 얼마나 크게 넣느냐"가 아니라,
> **확장적 통화충격 뒤 한계비용이 급등하지 않게 막는 마찰이 무엇이냐**다.

## 2~3. 연구 질문 · 문헌 공백

관측 사실 두 가지: **물가의 관성(inertia)** 과 **산출의 지속성(persistence)**.
표준 모형은 이를 재현하려면 **비현실적으로 큰 명목경직성**을 요구했다.

CEE의 접근: 경직성을 키우는 대신, **한계비용이 왜 안 오르는지**를 묻는다.
가격이 끈적한 이유는 기업이 못 고쳐서가 아니라 **고칠 이유가 약해서**일 수 있다.

## 4. 핵심 메커니즘

```
확장적 통화충격
        ↓
수요 ↑ → 통상 **한계비용 급등** → 가격 인상 압력 → 물가가 빠르게 반응
        ↓
[CEE의 마찰들이 이 경로를 막는다]
   ① **평균 3분기 시차 임금계약(staggered wage contracts)** → 임금이 안 뛴다
   ② **가변 자본가동률(variable capital utilization)** → 자본을 더 돌려 산출을 늘림. 비용 완만
        ↓
   한계비용이 완만 → 가격 인상 유인 약함 → **물가 관성 + 산출 지속성**
```

저자 문장: *"The key features of our model are those that **prevent a sharp rise in marginal
costs** after an expansionary shock to monetary policy. Of these features, the most important are
**staggered wage contracts of average duration three quarters**, and **variable capital utilization**."*

## 5. 충격 분류
**주 충격 = 통화충격.** 기여는 충격이 아니라 **전달을 늦추는 마찰의 특정**이다.

## 6. 전달경로

```
[[통화정책]] 확장 충격 → 수요 ↑
   → (임금 시차계약 + 가변 [[설비가동률]]) → 한계비용 완만
   → [[핵심인플레이션]] 반응 **지연** · [[산업생산]] 반응 **지속**
```

## 7~9. 실증 전략 · 주요 결과

| | |
|---|---|
| 모형 | 동태 일반균형 + **시차 임금·가격 계약** |
| 방법 | VAR로 통화충격의 동태 반응을 추정 → 모형이 그 반응을 맞추도록 **추정(최소거리)** |
| 설계 원칙 | *"For this exercise to be well defined, we must characterize inertia and persistence **precisely**"* |

**① 적당한(moderate) 명목경직성만으로 관성과 지속성이 설명된다**
초록: *"a model embodying **moderate amounts of nominal rigidities** which accounts for the
observed inertia in inflation and persistence in output"*
→ 비현실적으로 큰 경직성이 필요하지 않다.

**② 가장 중요한 마찰은 가격이 아니라 임금이다**
**평균 3분기 시차 임금계약**이 첫 번째 요인으로 지목된다.
→ 뉴케인지언 문헌의 무게중심이 **가격 경직성에서 임금 경직성으로** 옮겨간 계기.

**③ 두 번째는 가변 자본가동률** — 실물 마진이 명목 마찰을 보완한다.

## 10. 레짐 의존성
마찰의 크기(계약 기간·가동률 탄력성)가 곧 레짐 변수다.
노동시장 계약 관행이 바뀌면 통화정책 전달 속도도 바뀐다.

## 11. 자산가격 함의
- **[논문 주장]** 통화충격의 물가 반응은 **지연**되고 산출 반응은 **지속**된다
- **[우리의 추론]** 정책 변경 직후 물가 반응이 없다고 "정책이 안 먹힌다"고 읽으면 안 된다.
  **관성은 모형이 예측하는 정상 반응**이다
- **[우리의 추론]** [[설비가동률]]이 통화정책 전달의 **완충재**로 작동한다 —
  가동률 여유가 없으면 같은 충격이 더 빨리 물가로 간다

## 12. 반증 조건
- **확증**: 임금계약 기간이 긴 경제에서 물가 관성이 더 큼
- **반증**: 임금 경직성을 통제해도 관성이 남거나, 가격 경직성만으로 충분
- **감시**: 임금 계약 구조 · [[설비가동률]] 여유

## 13~14. 연결
**보완**: [[2007 Real Wage Rigidities and the New Keynesian Model (Blanchard & Galí)]] —
CEE는 **명목** 임금 경직성(계약 시차), BG는 **실질** 임금 경직성. **다른 종류의 임금 마찰**이며
BG는 그것이 **정책 상충**을 낳는다는 규범적 함의까지 간다
**연결**: [[2021 The Transmission of Monetary Policy Shocks (Miranda-Agrippino & Ricco)]] —
CEE는 VAR 통화충격의 동태반응을 **모형이 맞추는 대상**으로 삼는다.
MAR이 그 **VAR 충격 자체의 식별**을 문제 삼으므로, **CEE의 타깃이 흔들리면 추정치도 흔들린다.**
→ 인용 시 이 의존성을 밝힐 것
**보완**: [[2011 When Is the Government Spending Multiplier Large (Christiano, Eichenbaum & Rebelo)]] — 같은 저자군의 후속

## 15. 원문 대조에서 발견한 것
- **네 층 정합.** 초록의 세 요소(적당한 경직성 / 한계비용 억제 / 임금계약+가동률)가 본문과 일치
- **강점: 설계 원칙을 명시했다** — *"For this exercise to be well defined, we must characterize
  inertia and persistence precisely."* 무엇을 맞출지 먼저 정의하고 들어간다
- ⚠ **모형이 VAR 반응을 타깃으로 추정된다.** 즉 *"모형이 사실을 재현했다"*는 것은
  **캘리브레이션 제약이지 독립 예측이 아니다** →
  [[RBC의 산출 변동성은 예측이 아니라 캘리브레이션 제약이다]]와 같은 계열의 유보
- ⚠ **OCR 복원본**(계수 인용 금지) · WP(2001) 대조본, JPE 최종본(2005) 미확인

## 16. 파생 제텔
- [[물가 관성의 열쇠는 가격 경직성이 아니라 임금 경직성이다]]

## 17. 한 문장 · 확신도

> **물가가 천천히 움직이는 이유는 가격표를 못 고쳐서가 아니라 임금이 안 올라 한계비용이 안 뛰기 때문이다.**

**확신도: 중상.** 메커니즘이 명확하고 설계 원칙이 명시적이다.
**유보**: ① OCR 복원본 ② WP 대조본 ③ **VAR 타깃 의존** — 통화충격 식별이 바뀌면 결과도 바뀐다
④ 모멘트 매칭이라 **독립 예측 검정이 아니다.**
