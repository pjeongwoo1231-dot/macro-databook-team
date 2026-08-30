---
title: "Uncertainty and Exhaustible Resource Markets"
type: paper
journal: Journal of Political Economy 88(6), 1203-1225 (Dec 1980) · doi 10.1086/260935
date: 1980
author: Robert S. Pindyck (MIT)
url: https://web.mit.edu/rpindyck/www/Papers/UncertExhaustResourceJPE1980.pdf
tags: [type/paper, method/확률제어, domain/commodities]
concepts: [수요불확실성, 매장량불확실성, 비선형수요, 추출경로]
status: done
verification: full
reliability: academic
text_basis: human-fulltext
verified: "✔ 전문 판독(2026-08-18) — 저자 MIT 페이지 공개 PDF(24쪽, 텍스트층 있음) 초록·본문 직접 확인. 서지는 JPE(doi 10.1086/260935)·RePEc과 대조. ⚠ 05_Library의 JSTOR ID(1912938)는 확인하지 못했다"
promoted_from: "[[L223 Uncertainty and Exhaustible Resource Markets]]"
related: ["[[1978 The Optimal Exploration and Production of Nonrenewable Resources (Pindyck)]]", "[[1994 Investment under Uncertainty (Dixit & Pindyck)]]", "[[1984 The Welfare Effects of the Introduction of Storage (Wright & Williams)]]", "[[WTI (국제유가)]]"]
---

# 불확실성은 **기대 가격 경로가 아니라 생산 속도**를 바꾼다 (Pindyck, 1980)

> JPE 88(6) 1203-1225. **전문 판독 완료** — 인용 가능.

## 왜 중요한가 — 우리 문제와 직결

"불확실성이 커지면 가격이 오른다"는 말이 볼트 곳곳에서 느슨하게 쓰인다.
이 논문은 그 진술을 **정확히 갈라준다** — 불확실성이 무엇을 움직이고 무엇을 움직이지 않는지가
**모형의 비선형성에 달려 있다**고 말한다. [[VIX]] 노드의 "불확실성으로 읽을 때의 한계"와 같은 계열의 교정이다.

## 방법론

고갈성 자원 시장의 단순 모형에 **수요 함수와 매장량 수준이 연속시간 확률과정으로 변동**하도록 넣는다.
생산자는 **현재의 수요·매장량은 알지만 미래는 모른다.**

## 핵심 결과

**① 수요 불확실성은 기대 가격 동학에 영향이 없다**

> "demand uncertainty has **no effect on the expected dynamics of market price**"

**② 매장량 불확실성은 추출비용이 매장량에 대해 **비선형**일 때만 기대 가격 변화율을 움직인다**

**③ 그러나 수요함수가 비선형이면, 수요·매장량 불확실성 둘 다 생산(추출 속도)에 영향을 준다**

본문 논의: f'' > 0 이면 변동 자체가 q의 하락 속도를 **늦추고**, 초기 생산량을 낮추며 **초기 가격을 높인다.**
반대로 수요곡선이 시간에 따라 더 빨리 회전하면 q의 하락이 **빨라진다.**
독점의 경우도 유사하되 f''' 항이 추가로 들어간다.

→ **"불확실성 = 가격 상승"이 아니라, "불확실성 → (비선형성이 있을 때) 생산 경로 변화 → 초기 가격 수준 변화"** 가 정확한 진술이다.

## 저자가 밝힌 한계

- **단순 모형**이다(추출비용·수요의 함수형태에 결과가 걸린다 — 그것이 바로 논문의 요지이기도 하다)
- 생산자는 위험중립적 최적화 주체로 다뤄지며, 금융시장·헤지는 모형에 없다

## 우리 시스템에 적용

1. **"불확실성이 커져서 유가가 올랐다"는 서술을 쓸 때 경로를 명시한다** — 기대 가격 경로가 아니라
   **생산 결정을 통해서**다(①③). → [[WTI (국제유가)]] 실무 규칙에 추가 검토
2. **함수형태 가정을 밝히지 않은 불확실성 주장은 인용하지 않는다** — 이 논문에서는 그것이 결과의 부호를 정한다
3. [[1994 Investment under Uncertainty (Dixit & Pindyck)]]의 대기 옵션과 **다른 기제**임을 구분한다 —
   여기서는 옵션가치가 아니라 **확률과정 하의 최적 추출 경로**다

## Red Team

1. **부분균형·위험중립 모형**이다. 위험회피나 금융시장(선물·헤지)을 넣으면 결론이 달라질 수 있다
2. **①은 "기대 동학"에 대한 진술**이다. 실현 경로의 분산이 커지는 것과 혼동하면 안 된다
3. 1980년 모형이라 **셰일 이후 공급 탄력성 구조**는 반영되지 않는다
4. 스캔본 문제는 없었으나 **05_Library의 JSTOR ID는 검증하지 못했다** — 인용은 DOI로 한다

## 인과 사슬

```
수요·매장량이 확률적으로 변동
        ↓
 ┌─ 기대 가격 경로: 수요 불확실성은 **영향 없음** / 매장량 불확실성은 **추출비용이 비선형일 때만**
 └─ 생산(추출) 경로: **수요함수가 비선형이면 둘 다 영향**
        ↓
초기 생산량 q0 하락 → **초기 가격 p0 상승** (f'' > 0인 경우)
```

## 관련 노트

- [[1978 The Optimal Exploration and Production of Nonrenewable Resources (Pindyck)]] · [[WTI (국제유가)]] · [[Library MOC]]
