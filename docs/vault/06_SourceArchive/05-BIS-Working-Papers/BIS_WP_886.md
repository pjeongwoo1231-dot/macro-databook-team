---
title: "BIS WP 886 — Price search, consumption inequality, and expenditure inequality over the life-cycle"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 886
published: "September 2020"
authors: "Yavuz Arslan , Bulent Guler and Temel Taskin"
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
  - "consumption-vs.-expenditure"
  - "price-search"
  - "life-cycle-inequality"
  - "incomplete-markets"
  - "endogenous-labor-supply"
  - "partial-insurance"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 886 — Price search, consumption inequality, and expenditure inequality over the life-cycle

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

저자들은 가격검색을 생애주기 모형에 추가하면 지출 불평등이 소비 불평등보다 더 크게 증가하고(증가폭 차이 약 30%), 가격검색은 소비의 부분적 보험·복지 개선(신생아 소비등가 약 +3.9%)을 제공한다고 주장하나, 이 결과는 가격분포의 외생성, 검색수익률(θ1), 검색시간의 소비의존성(ψ) 등 몇몇 핵심 가정에 민감하여 일반화 시 주의가 필요하다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 가격 검색(choice of search effort)이 생애주기별 소비 불평등과 지출 불평등의 차이를 어떻게 발생시키며, 가격 검색이 가계의 보험(소비평활)과 복지에 어느 정도 기여하는가? |
| 방법 | 불완전시장(life-cycle) 이모형에 내생적 노동공급과 가격검색 시간을 추가하여 소비(ct)와 지출(et=pt ct)를 구분한 뒤, 로그선형 가격-검색 관계를 가정하고(로그(pt)=θ0t + θ1 log(st)), 외생적 임금과정 파라미터를 사용해 2단계(외부·내부) 보정으로 미국표준 모형을 수치해석. 보험효과는 공분산 기반 보험계수(φ = 1 − cov(Δc, shock)/var(shock))로 계산. |
| 자료·범위 | 모형은 미국을 대상으로 캘리브레이션(기간=1년, 취업시작 21세, 은퇴 65세, 사망 90세). 임금과정 파라미터는 선행연구(보고서에 인용된 Kaplan 등)에서 차용. 가격·검색 관련 경험적 정합성은 A.C. Nielsen Homescan(스캐너 거래) 자료의 가구별 가격지수와 쇼핑 행태(방문빈도·점포수·쿠폰사용 등 프록시)를 사용하여 점검. 가격검색의 수익성(θ1)은 Aguiar & Hurst의 식료품 기반 추정값을 출발점으로 사용. |
| 주제 | consumption vs. expenditure, price search, life-cycle inequality, incomplete markets, endogenous labor supply, partial insurance |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자들은 가격검색을 포함한 벤치마크 모형에서 생애주기 동안 로그 지출 분산이 약 13.6 로그포인트 증가하는 반면 로그 소비 분산은 약 9.5 로그포인트 증가하여 소비 불평등의 증가폭이 지출보다 약 30% 작다고 보고한다.
- 분해 결과 지출·소비 간 격차의 주된 원인은 소비와 임금의 공분산(cov(log c, log w))의 증가이며, 저자 계산에 따르면 이 요인이 격차 증가분의 약 85%를 차지한다고 주장한다.
- 모형은 가격 분산(가격에 대한 교차단면 분산)은 절대 수준에서 작지만(소비·지출 분산에 비해), 생애주기 동안 증가하며(A.C. Nielsen 자료의 쇼핑 프록시들 또한 검색 분산 증가를 보여) 이 점이 모델 예측과 정합한다고 보고한다.
- 가격검색은 부분적 보험효과를 제공하여 모형상 소비에 대한 영구(지속적) 충격의 보험계수를 소비 기준으로 0.42에서 0.54로(레벨 +0.12, 상대 약 +29%) 개선하고, 일시충격에서도 0.83→0.91로 개선된다고 계산한다.
- 가격검색 가능성은 균형에서 가계 효용을 높이며(신생아의 소비등가 보수로 약 3.9% 향상), 놀랍게도 가격검색이 존재할 때 자산보유(저축)가 약 14% 더 높아진다고 보고한다.
- 소득성장률이 다른 가구 집단 간에는, 가격 동학 때문에 지출이 소비보다 더 빠르게 증가하여 고성장 가구의 지출-소비 격차가 확대됨 — 저자 계산에서는 고/저 성장 대조에서 65세 시점의 평균 소비격차가 지출격차보다 약 15% 작게 나타난다.

## 메커니즘과 연결고리

- 가격검색은 검색시간 증가→지불가격 감소(로그선형 관계)로 동일한 소비량에서 실제 구매가능한 소비(실질소비)를 늘리는 통로다.
- 검색시간은 여가·노동시간과 시간예산을 공유하므로 검색은 여가·노동의 대체로 작용해 가계의 선택을 변경한다.
- 이론적으로(해당모형) 저소득·저자산 가구가 더 많이 검색하여 더 낮은 가격을 지불하는 경향이 발생(특정 조건하에서), 따라서 지출 불평등이 소비 불평등보다 크게 된다.
- 임금과 소비의 양(또는 분포)의 공분산이 생애주기 동안 증가하면(고소득자일수록 소비가 커지는 구조) 가격검색 효과를 통해 지출·소비의 격차가 확대된다.
- 가격검색이 존재하면 경기악화 시점에 검색을 통해 실질구매력을 회복할 수 있어 소비의 부분적 보험 역할을 하며, 이로 인해 위험무관자산(무위험채권)의 수익 구간이 소득상태별로 달라져 자산수요가 오히려 증가한다.

## 한계와 적용 범위

- 본 연구는 소매가격 분포 자체를 외생적(기업부문 비내생화)으로 가정하여, 가격분산의 발생원(공급측·시장구조 변화)이 모형 내부적으로 설명되지 않는다.
- 가격검색 기술의 핵심 파라미터 θ1(검색의 수익률)는 Aguiar & Hurst의 식료품 거래 기반 추정치를 사용했는데, 이는 비식료품·온라인 등 다른 범주로 일반화 가능성에 제약이 있다(저자도 이 점을 명시).
- 검색시간의 소비규모 의존성 ψ(검색시간이 소비규모에 비례하는지 여부)는 결과에 민감한 파라미터이며, 논문은 ψ=1을 보수적으로 채택했으나 ψ의 실제값은 불확실하고 결과에 큰 영향을 준다.
- 검색행동을 직접 관찰할 수 없으므로 A.C. Nielsen의 쇼핑 빈도·점포방문수·쿠폰사용 등은 검색의 불완전한 프록시이며 측정오차 가능성이 있다.
- 모형은 가격-검색 관계를 로그선형의 단순한 축약식으로 쓴다(로그(pt)=θ0t+θ1 log(st)); 이 축약식과 통계적 식별은 실물 데이터의 범주별·시장별 이질성을 충분히 포착하지 못할 수 있다.
- 복수의 보정(targeting)으로 파라미터를 맞추는 특성상 일부 결과는 특정 타깃(부의 소득비율, 연령별 평균시간·가격 등)에 민감할 수 있어 외삽(다른 국가·시기·정책문맥)에는 제약이 있다.
- 모형의 자산시장·대출제약 설정(예: at+1 ≥ 0 등)과 연간 기간 설계는 보험계수·저축결정에 영향; 다른 융통성(차입허용 등)에서는 크기가 달라질 수 있다.
- 저자들이 제시한 ‘가격검색 없음’ 반사실(counterfactual)은 모든 가구의 지불가격을 평균(1)으로 고정하는 방식인데, 이는 공급·균형 반응(기업의 가격설정)까지 반영한 일반균형 반사실이 아니어서 비교 해석에 제한이 있다.
- 모형은 상품별 상이한 검색수익이나 시장별(오프라인·온라인) 차이를 내생적으로 다루지 않아 카테고리별 불평등 해석에는 한계가 있다.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_886-catalog]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work886.pdf](https://www.bis.org/publ/work886.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work886.htm](https://www.bis.org/publ/work886.htm)

## References

[1]: https://www.bis.org/publ/work886.pdf "BIS Working Paper 886: Price search, consumption inequality, and expenditure inequality over the life-cycle"
