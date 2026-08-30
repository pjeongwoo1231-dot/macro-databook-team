---
title: "Measuring Economic Policy Uncertainty"
type: paper
journal: Quarterly Journal of Economics 131(4), 1593–1636 (2016)
date: 2016
author: Scott R. Baker, Nicholas Bloom, Steven J. Davis
url: https://academic.oup.com/qje/article-abstract/131/4/1593/2468873
tags: [type/paper, method/text-analysis, domain/uncertainty]
concepts: [정책 불확실성, EPU 지수, 신문 텍스트, 지수 구축, 대용지표]
status: done
verification: partial
reliability: academic
text_basis: cited-primary
verified: "△ 서지 확정(2026-08-14, QJE 131(4) 1593). 본문 유료라 미열람 — **수치 인용 금지**"
promoted_from: "[[L21 Measuring Economic Policy Uncertainty]]"
related: ["[[2015 Measuring Uncertainty (Jurado, Ludvigson & Ng)]]", "[[2009 The Impact of Uncertainty Shocks (Bloom)]]", "[[지정학적 리스크]]", "[[RegimeView 1.0 (2026-08-09)]]"]
---

# DataBook이 매일 받는 EPU 지수, 그 원논문 (Baker, Bloom & Davis, 2016)

> Quarterly Journal of Economics 131(4) 1593–1636, 2016.
> ⚠ **본문 미열람**(유료). 서지만 확정했다. **수치는 인용하지 않는다.**

## 왜 중요한가 — 우리 문제와 직결

**DataBook이 수집하는 지표의 원논문이다.**

- `미국 경제정책 불확실성 EPU (일별)` — FRED `USEPUINDXD`
- `미국 통화정책 불확실성 EPU (범주별)` — FRED `EPUMONETARY`
- `한국 경제정책 불확실성 EPU (월간)`

셋 다 이 논문이 만든 지수다. **매일 숫자를 받으면서 그게 어떻게 만들어졌는지
볼트에 기록이 없었다.** 지수의 구축 방식을 모르면 한계도 모른다.

## 논지

정책 불확실성을 **신문 텍스트**로 측정한다. 주요 신문에서
**"경제(economy)" + "불확실(uncertain)" + "정책(policy 관련어)"** 세 범주의 단어가
함께 등장하는 기사의 **빈도**를 세어 지수화한다. 신문 발행량 변화를 보정하고 표준화한다.

이렇게 만든 EPU 지수가 걸프전·9·11·리먼·재정절벽·유로위기 같은 **정책 사건에서 급등**하고,
지수 상승이 **투자·산출·고용의 하락**과 동태적으로 연관된다는 것을 보인다.

**범주별 하위 지수**(통화정책·재정정책·무역정책 등)도 함께 제공하는데,
DataBook이 받는 `EPUMONETARY`가 그중 하나다.

## 한계와 적용 범위

- **사서(추가)**: **신문 지면이 곧 불확실성은 아니다.** 언론 관심·편집 방침·매체 구성 변화가
  지수를 움직인다. 같은 사건도 보도량이 다르면 지수가 다르게 나온다
- **사서(추가)**: [[2015 Measuring Uncertainty (Jurado, Ludvigson & Ng)]]가 정면으로 반박한다 —
  **예측 가능한 정책 이벤트도 기사 빈도를 올린다.** FOMC 회의처럼 일정이 정해진 사건은
  불확실성이 아니라 **관심**을 재는 것일 수 있다
- **사서(추가)**: **한국 EPU는 특히 조심해야 한다.** 매체 수가 적고 정치 보도 비중이 커서
  경제 정책 불확실성이 아니라 **정치 뉴스량**을 잡을 수 있다. 미국 지수와 같은 해석을 적용하기 전에
  급등 시점이 실제 정책 사건과 맞는지 눈으로 확인할 것
- **사서(추가)**: 본문 미열람이므로 **회귀계수·충격반응 크기를 인용하지 않는다**

## 인과 사슬

정책 사건 → 신문 기사에 "경제+불확실+정책" 동시 출현 증가 → **EPU 지수 상승**
→ (Bloom 2009 기제라면) 기업 대기행동 → 투자·고용 위축
→ **단, 지수 상승이 관심 증가일 뿐이면 실물 반응이 없다** (JLN 2015)

**Comment**: DataBook 실무 규칙 — **EPU 급등을 보면 먼저 "무슨 기사였나"를 확인**한다.
지수 자체는 원인을 말해주지 않는다. 다행히 DataBook은 뉴스 다이제스트를 같이 수집하므로
같은 날 [[DataBook 지표 소환]]과 `_News/NewsDigest`를 대조하면 확인된다.

그리고 [[지정학적 리스크]] 노드(GPR 지수)와 **측정 방식이 같은 계열**이다 —
둘 다 텍스트 빈도 기반이므로 **같은 한계를 공유**한다. 하나가 오르면 다른 하나도
오르는 것이 실체 때문인지 보도량 때문인지 구분되지 않는다.

## 관련 개념

- 측정 비판 — [[2015 Measuring Uncertainty (Jurado, Ludvigson & Ng)]]
- 전파 기제 — [[2009 The Impact of Uncertainty Shocks (Bloom)]]
- 같은 텍스트 기반 지표 — [[지정학적 리스크]]
- 정책 설계 — [[2025 Monetary Policy, Uncertainty, and Communications (Garga et al, FEDS 2025-074)]]
- 데이터 — [[DataBook 지표 소환]] · [[RegimeView 1.0 (2026-08-09)]]

## References

[1]: https://academic.oup.com/qje/article-abstract/131/4/1593/2468873 "Baker, Bloom and Davis (2016), Measuring Economic Policy Uncertainty, QJE 131(4) 1593–1636"
[2]: https://www.policyuncertainty.com/ "Economic Policy Uncertainty Index — 지수 공식 배포처"
