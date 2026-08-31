---
title: "BIS WP 852 — Average inflation targeting and the interest rate lower bound"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 852
published: "April 2020"
authors: "Flora Budianto , Taisuke Nakata and Sebastian Schmidt"
source_kind: "working-paper"
peer_reviewed: false
primary_text_read: true  # 추출 전문 기준. 사람 대조 아님
human_verified: false
analysis_model: "gpt-5-mini"
analysis_confidence: "not-calibrated"
relevance_score: 1
created: 2026-08-14
updated: 2026-08-14
archive_status: "llm-structured-unverified"
tags:
  - flag/partial-check
  - bis
  - working-paper
  - "average-inflation-targeting-(ait)"
  - "price-level-targeting-(plt)"
  - "interest-rate-lower-bound-(ilb)"
  - "new-keynesian-model"
  - "boundedly-rational-expectations"
  - "policy-delegation-/-discretionary-central-bank"
  - "inflation-conservatism"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 852 — Average inflation targeting and the interest rate lower bound

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

저자들은 신케인지안 모형(일시적 제로하한)에서 평균물가목표(AIT)가 재량하의 중앙은행에 부여되면 합리적 기대하에서 복지를 상당히 개선하고, 최적의 평균창은 무한(즉 PLT와 동치)이라고 주장한다. 대부분의 이득은 유한하지만 충분히 긴 평균창으로도 확보될 수 있다. 그러나 기대형성이 제한적이면(AIT의 필수적 메커니즘인 미래정책약속의 내생적 효과가 약해지면) AIT의 이득이 작아지고 최적창이 짧아질 수 있다. 결과는 모형가정·보정값·정책의 신뢰성 등에 민감하다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 평균물가목표(AIT)를 재량(discretion)하의 중앙은행에 부여하면 명목금리 하방제약이 존재할 때 거시안정화와 사회적 복지(welfare)에 어떤 영향이 있는가? |
| 방법 | 무한내생 시차의 신케인지안 모델을 사용해 중앙은행이 지수평균(exp. moving average)으로 정의된 평균물가(π̂)를 목표로 재량적으로 정책금리(i_t)를 설정하는 문제를 풂. 기대형성은 (i) 합리적기대와 (ii) Gabaix(2019)식의 boundedly-rational 기대 두 가지로 비교. 비선형성과 occasionally binding lower bound(it≥0)을 고려해 전역(global) 수치해법(collocation · cubic splines)을 이용해 해를 구함. |
| 자료·범위 | 이론·수치모델 연구이며 실제 관측치 대신 문헌 기반의 보정(calibration)을 사용. 기준 보정값(table 1)은 Nakata & Schmidt(2019b) 계열 파라미터를 채용하고 자연실질금리 충격은 AR(1)로 모형화(논문은 해당 AR(1)를 미국 데이터로 추정했다고 명시). 복지는 2차 테일러 전개에 근거한 소비등가(perpetual consumption transfer)로 평가. |
| 주제 | average inflation targeting (AIT), price level targeting (PLT), interest rate lower bound (ILB), New Keynesian model, boundedly-rational expectations, policy delegation / discretionary central bank, inflation conservatism |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장: 합리적 기대 하에서는 AIT가 표준 물가목표(IT) 대비 복지를 상당히 개선하며, ω→0(무한 평균 창)은 최적이며 이 경우 AIT는 가격수준목표(PLT)와 동치이다.
- 저자 주장: 무한 평균이 최적이나 유한하더라도 충분히 긴 평균창(수년 수준)으로 PLT가 제공하는 대부분의 복지수익을 확보할 수 있다.
- 저자 주장: AIT의 핵심 작동 메커니즘은 (i) 과거 물가부족을 보상하기 위한 미래 인플레이션 초과(역사의존성)와 (ii) 향후 하방제약 발생 위험을 반영해 현재 인플레이션을 높이는(lower-bound risk) 두 동기이다.
- 저자 주장: 기대형성이 제한적(인지할인 m̄ 작음)인 경우 AIT의 효과가 약화되어 최적 평균창이 유한으로 이동하고, 매우 약한 인지능력에선 AIT(혹은 PLT)의 복지이득이 작거나 오히려 역효과를 낼 수 있다.
- 저자 주장: 중앙은행의 출력갭에 대한 상대적 가중치(λ_CB)를 낮추는 ‘인플레이션 보수성(inflation conservatism)’은 복지를 추가 개선하며, 충격원천이 자연실질금리뿐일 때는 λ_CB=0(출력갭 무시)이 사회적으로 최적일 수 있다.
- 저자 주장: AIT·PLT의 실효성은 에이전트가 미래 정책과 결과 간의 연계(정책의 메이크업 특성)를 얼마나 잘 이해하느냐에 크게 좌우된다.

## 메커니즘과 연결고리

- 역사의존성(history dependence): 과거 평균물가(π̂)가 목표보다 낮으면 중앙은행은 미래에 초과인플레이션을 허용해 평균을 회복하려고 하며, 이 기대가 현재 수요·물가를 자극한다.
- 하방리스크 동기(lower-bound risk motive): 향후 하방제약에 대한 기대(Et φ_LB)가 존재하면 중앙은행은 제약 위험을 완화하기 위해 현재 인플레이션을 더 높이는 유인을 가진다.
- 디플레이션 바이어스(deflationary bias): 재량하의 정책에서 하방제약 가능성만으로도 평상시 기대인플레이션이 하락해 지속적 물가부족을 초래할 수 있음; AIT/PLT는 이를 상쇄함.
- 기대전달의 완화: boundedly-rational 기대(인지할인)는 미래정책 약속의 현재효과(포워드 가이던스)를 약화시켜 AIT의 메이크업 채널 효율을 떨어뜨림.
- 인플레이션 보수성: 중앙은행이 출력갭 가중치를 낮추면(λ_CB↓) 디플레이션 바이어스가 추가로 완화되어 복지 개선을 가져옴.

## 한계와 적용 범위

- 모형적 한계: 분석은 이론·수치모형에 기반하며 실증추정이나 관측자료로 직접 확인되지 않는다.
- 기대모델 특이성: boundedly-rational 기대는 Gabaix(2019) 방식 한 가지로만 다루며, 관련 파라미터(m̄)는 문헌에 따라 불확실하고 직접적으로 식별되지 않는다.
- 정책설정 가정: 중앙은행은 재량(discretion)만 허용되고 완전한 약속(commitment) 체계는 배제되어 있어 약속가능성·신뢰성 관련 채널(예: 완전한 forward guidance 신뢰성)이 고려되지 않는다.
- 평균 정의 근사: AIT를 지수평균으로 정의해 계산 편의를 확보했으며, 이는 보편적 산술(단순) 이동평균과는 수학적 차이가 있어 '유한 vs 무한' 윈도우 해석에서 근사적 해석을 수반한다.
- 하방제약 단순화: 하방제약은 it ≥ 0(제로 하한)으로 모델링되어 음수금리, 대규모 자산매입, 재정정책 등 실제 사용 가능한 비전통적 수단은 모형에 포함되지 않았다.
- 복지측정·근사: 복지는 가계효용의 2차 근사(쿼드러틱)로 평가되며, 높은차 비선형·분배·불평등 효과 등은 반영되지 않는다.
- 파라미터 민감도: 최적 ω와 복지이득은 m̄, rn(평상시 실질금리), ϕ(가격마찰), σ 등 보정값에 민감함(논문 자체의 민감도 분석에서 확인).
- 외생적제약: 정치적·제도적 제약(예: 중앙은행이 출력갭을 ‘무시’하는 λ_CB=0 정책을 채택 가능성)은 현실적 제약을 반영하지 않을 수 있다.
- 외부요인 미포함: 개방경제, 가계·기업 이질성, 금융 마찰, 재정정책 상호작용 등으로 결과가 달라질 여지가 있다.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_852-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[CPI (소비자물가지수)]]
- [[통화정책]]
- [[PMI (구매관리자지수)]]
- [[재정정책]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work852.pdf](https://www.bis.org/publ/work852.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work852.htm](https://www.bis.org/publ/work852.htm)


## References

[1]: https://www.bis.org/publ/work852.pdf "BIS Working Paper 852: Average inflation targeting and the interest rate lower bound"
