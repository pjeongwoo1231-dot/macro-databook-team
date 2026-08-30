---
title: "R* in East Asia: business, financial cycles, and spillovers"
type: paper
series: BIS Working Papers No 1285
date: 2025
author: Pierre L. Siklos (WLU & BSIA), Dora Xia (BIS), Hongyi Chen (HKIMR)
url: https://www.bis.org/publ/work1285.pdf
tags: [type/paper, method/band-spectrum, domain/policy]
concepts: [중립금리, r-star, 경기순환, 금융순환, 국제 파급, 불확실성 밴드]
source_file: 06_SourceArchive/05-Primary-PDFs/2024-2026/BIS-WP-1285.pdf
status: done
verification: full
reliability: working-paper
text_basis: local-pdf
verified: 원문 대조 완료(2026-08-14). 로컬 PDF 판독 — 4개국·주파수영역·두 종류 r*·파급 방향 확인. 원문 초록에 'Kora' 오타 있음(Korea)
related: ["[[잠재성장률]]", "[[미국이 좋아서 올리는 금리도 한국에는 악재다]]", "[[Monetary-Policy-Transmission-and-International-Spillovers]]", "[[원문 아카이브 MOC]]"]
---

# 중립금리는 하나가 아니다 — 경기순환용과 금융순환용이 따로 논다 (Siklos, Xia & Chen, 2025)

> BIS Working Paper No 1285. 저자 견해이며 BIS 견해가 아니다.

## 왜 중요한가 — 우리 문제와 직결

**볼트에서 한국이 직접 등장하는 몇 안 되는 원문 대조 논문이다.**
중국·일본·한국·미국 4개국을 같은 틀에서 추정하고, **미국→동아시아 3국**과
**중국→한·일** 파급을 각각 식별한다. 볼트 제텔
[[미국이 좋아서 올리는 금리도 한국에는 악재다]]가 말하는 대외 종속을
**중립금리 수준에서** 확인해 준다.

두 번째로 중요한 것은 **r*가 하나가 아니라는 결과**다. 레짐 판단에서 "중립 대비 긴축/완화"를
말할 때 어떤 중립을 쓰는지에 따라 판정이 갈릴 수 있다는 뜻이고, 이건 RegimeView류 판단에
직접 걸린다.

## 방법과 자료

| 항목 | 내용 |
|---|---|
| 대상 | **중국·일본·한국·미국**, 분기 자료 |
| 방법 | **주파수영역 접근**의 밴드 스펙트럼 회귀. 순환 주기대별로 나눠 추정 |
| 산출 | **두 종류의 r***  — 하나는 **경기순환** 주기대에서, 다른 하나는 **금융순환** 주기대에서 성립 |
| 불확실성 | **thick modelling**으로 신뢰밴드 도출 |

## 원문에서 확인한 결과

**1. r*의 하락 추세는 확인되나, 불확실성 밴드를 넣으면 흐려진다.**
> *"a downward trend in r* is observed, although the trend becomes less obvious when
> uncertainty bands are factored in."*

**2. 두 r*가 항상 같이 움직이지 않는다.** 개별 국가에서 경기순환 r*와 금융순환 r*가
서로 따라가지 않는 구간이 있고, 이는 중앙은행이 정책금리를 정할 때
**경기순환 고려와 금융순환 고려 사이에서 상충(trade-off)에 직면**한다는 뜻이다.

**3. 파급은 방향이 있다.**
> *"we identify significant positive spillovers from the US to the three East Asia countries,
> as well as spillovers from China to Kora and Japan."*
(원문 표기 `Kora`는 Korea의 오타.)

즉 **미국 → 한·중·일**, 그리고 **중국 → 한·일**. 한국은 두 파급을 모두 받는 위치다.

## 한계와 적용 범위

- **사서(추가)**: r* 자체가 **관측 불가능한 추정치**다. 저자들이 thick modelling으로
  밴드를 낸 것은 정직하지만, 밴드가 넓으면 "지금 중립 위인가 아래인가"라는 실무 질문에
  단정적으로 답할 수 없다. **추세가 밴드에 먹힌다는 것이 이 논문의 솔직한 결과**다
- **사서(추가)**: 밴드 스펙트럼 회귀는 주기대 구분(경기 vs 금융)의 **경계 설정에 민감**하다.
  경계를 바꾸면 두 r*의 괴리 크기도 바뀔 수 있다
- **사서(추가)**: 4개국 표본이라 파급의 일반화 범위가 좁다. 또 파급 식별이
  **동시성 문제**(공통 글로벌 요인이 넷을 동시에 움직임)를 완전히 배제하는지 확인이 필요하다
- **사서(추가)**: 중국의 금리 자유화 정도가 시기별로 달라 중국 r* 해석에 주의가 필요하다

## 인과 사슬

미국 [[기준금리]]·r* 변화 → **한·중·일 중립금리 동반 이동**
+ 중국발 파급 → 한·일 추가 이동
→ 국내 정책금리가 국내 여건만으로 결정되지 않음
→ 경기순환 r* vs 금융순환 r* **괴리 구간에서 정책 상충**
→ [[원·달러 환율]]·[[신용사이클]] 압력과 [[잠재성장률]] 판단이 엇갈림

**Comment**: 레짐 판단에 쓸 실무 규칙 하나 — **"중립 대비"를 말할 때 어느 중립인지 명시할 것.**
경기순환 r*로는 완화적인데 금융순환 r*로는 긴축적인(또는 그 반대) 구간이 존재한다.
그리고 한국은 **미국과 중국 두 방향의 파급을 동시에 받는** 유일한 위치라,
대외 요인을 하나(미국)로만 두면 설명이 빈다.

## 관련 개념

- 한국으로의 파급 — [[미국이 좋아서 올리는 금리도 한국에는 악재다]]
- 전파 일반형 — [[Monetary-Policy-Transmission-and-International-Spillovers]]
- 지표 — [[잠재성장률]] · [[기준금리]] · [[원·달러 환율]]
- 국면 지도 — [[2024-2026-Comparative-Mechanism-Map]]

## References

[1]: https://www.bis.org/publ/work1285.pdf "Siklos, Xia and Chen (2025), R* in East Asia: business, financial cycles, and spillovers, BIS WP 1285"
