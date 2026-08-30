---
title: Determination of Copper Price Expectations in the International Market - Some Important Variables
type: paper
journal: Open Journal of Business and Management 7(2), 2019, pp.348-373 (SCIRP, DOI 10.4236/ojbm.2019.72024)
date: 2019-02
author: Andre Assis de Salles · Raphael Sebastian Magrath · Matheus Manzani Malheiros (UFRJ, Brazil)
created: 2026-08-05
status: done
verification: full
reliability: research
verified: 원문 정독(2026-08-05, pymupdf 26p — 초록·서론·인과검정 서술·IRF 시차·결론 대조)
source_file: Determination of Copper Price Expectations in the .pdf
tags: [type/paper, domain/commodity, method/공적분, method/그랜저인과성, method/충격반응함수, flag/needs-review]
concepts: [구리가격, 산업생산, 알루미늄가격, 재고, 환율, 선행지표]
related: ["[[구리 가격]]", "[[2020 6대 비철금속 국제가격 변동요인 SVAR (최혜원·허은녕·김경아)]]", "[[산업생산]]"]
---

# 구리가격의 결정요인 (Salles et al., 2019)

> ⚠ **게재지 주의** — SCIRP 계열이다. 이 vault는 같은 출판사의
> [[2025 A Reformulation of the Quantity Theory of Money (Temprano)]]에도 동일한 경고를 달았다.
> `reliability: research` · 재현 확인 전 인용 금지.

## 이 논문이 중요한 이유 — Dr. Copper 통설을 스스로 전제한다

서론이 명시적으로 적는다:
> "copper price movements represent a relevant **global economy leading indicator**"

그런데 **정작 검증한 것은 반대 방향**이다 — 무엇이 구리 가격을 **결정하는가**.

## 핵심 결과

### ① 산업생산이 압도적으로 가장 중요하다

> "industrial production was **the most relevant variable**, presenting evidence in **all the tests**
> carried out that its impact on the copper price is significant"

알루미늄 가격과 구리 자신의 시차값도 유의하나 **"much weaker and more irregular"**.

### ② 그런데 이건 Dr. Copper와 방향이 반대다

**산업생산이 구리 가격을 설명한다**면, 구리는 산업생산을 **선행**하는 것이 아니라
**동행하거나 후행**한다는 뜻이 된다.
→ **"구리가 경기를 미리 알려준다"는 통설과 이 논문의 결과는 서로 맞물리지 않는다.**
논문은 이 긴장을 **명시적으로 다루지 않는다.**

### ③ 구리 생산량은 가격의 원인이 아니라 결과다

> "the copper production variable **did not present any evidence** to infer that this variable is relevant"
> "this variable is **caused by the price** while the reciprocal does not happen"

**생산 → 가격이 아니라 가격 → 생산.** 공급이 가격을 만드는 게 아니라 가격이 공급을 부른다.
→ [[2020 6대 비철금속 국제가격 변동요인 SVAR (최혜원·허은녕·김경아)]]의 **"공급충격 영향 0.1로 작다"** 와 정합적이다.

### ④ 유가는 그랜저 인과가 없어도 IRF에서는 반응한다

그랜저 검정에서는 무관했으나 **IRF에서는 브렌트 상승이 10개월 시차로 구리 가격을 올린다.**
환율은 그랜저·IRF 모두에서 유의하지 않았다(단 자료 확보에 한계가 있었다고 명시).

### ⑤ 방향은 73% 맞히지만 결정계수는 낮다

추정 회귀모형이 **구리 가격 변동의 방향을 73%의 경우에 맞혔다.**
그러나 저자 스스로 **"low coefficient of determination"** 이라고 적으며,
**선택한 변수들이 구리 가격 변동을 충분히 설명하지 못한다**고 인정한다.

## 인과 사슬

세계 [[산업생산]] ↑ → **구리 가격 ↑** (전 검정에서 유의, 가장 강함)
구리 가격 ↑ → **구리 생산량 ↑** (역방향은 성립하지 않음)
[[WTI (국제유가)]] ↑ → (10개월 시차) → 구리 가격 ↑ *(IRF에서만, 그랜저에서는 무관)*

**Comment**: 이 논문의 쓸모는 **자기 서론을 배반한다는 점**에 있다.
서론은 구리를 "글로벌 경기 선행지표"라 부르는데, 결과는 **산업생산이 구리를 설명한다**는 것이다.
→ 이 vault의 [[구리 가격]] 판정 규칙에 **"구리를 선행지표로 쓰지 말 것"** 의 근거로 쓴다.

## 검증 필요 · 반박 포인트 (Red Team)

**① SCIRP 게재지**
심사 강도가 낮은 것으로 알려진 출판사다. 결과 자체보다 **인용 시 게재지를 함께 밝힐 것.**

**② 서론의 전제와 결론이 충돌하는데 논의가 없다**
"구리는 선행지표"라고 써놓고 "산업생산이 구리를 결정한다"로 끝난다.
**선행/후행 관계를 직접 검정하지 않았다** — 시차 구조를 명시적으로 비교했어야 한다.

**③ 재고·환율 자료에 한계가 있다고 저자가 명시**
> "the time series of the stock and exchange rate variables, which were obtained with limitations"
→ 이 두 변수의 "비유의" 결과는 **부재의 증거가 아니라 자료의 한계**일 수 있다.

**④ 낮은 R²를 저자가 인정한다**
"선택한 변수들이 구리 가격 변동을 완전히 설명하지 못한다"
→ [[2020 6대 비철금속 국제가격 변동요인 SVAR (최혜원·허은녕·김경아)]]이
**설명되지 않는 성분(상품별 수요충격)이 가장 크다**고 한 것과 같은 이야기다.

## 관련 개념

[[구리 가격]] · [[산업생산]] · [[WTI (국제유가)]]

## 관련 MOC

- [[지표 MOC]] · [[원문검증 논문 MOC]]
