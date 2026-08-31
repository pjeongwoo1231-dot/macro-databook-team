---
title: "BIS WP 862 — On the instability of banking and other financial intermediation"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 862
published: "May 2020"
authors: "Chao Gu , Cyril Monnet , Ed Nosal and Randall Wright"
source_kind: "working-paper"
peer_reviewed: false
primary_text_read: true  # 추출 전문 기준. 사람 대조 아님
human_verified: false
analysis_model: "gpt-5-mini"
analysis_confidence: "not-calibrated"
relevance_score: 2
created: 2026-08-14
updated: 2026-08-14
archive_status: "llm-structured-unverified"
tags:
  - flag/partial-check
  - bis
  - working-paper
  - "banking-instability"
  - "financial-intermediation"
  - "multiple-equilibria"
  - "sunspot-equilibria-and-cycles"
  - "search-and-otc-markets"
  - "money-and-payment-instruments"
  - "dynamic-general-equilibrium"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 862 — On the instability of banking and other financial intermediation

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

저자들은 네 가지 상이한 동적 이론모형을 통해 금융중개가 본질적으로 불안정성을 확대시킬 수 있음을 논리적으로 보였다. 평판·고정비·딜러 재고·은행발 지급수단이라는 서로 다른 현실적 기능들이 각기 다른 경로로 다중 균형·주기·혼돈·선샤인(사인스팟) 균형을 만들어낼 수 있음을 수학적으로 증명하고 예시적 파라미터로 시뮬레이션했다. 동시에 저자들은 중개가 일반적으로 복지를 개선할 수 있음을 강조하며, 불안정성이 중개가 무조건 나쁘다는 결론으로 직결되지는 않는다고 명시한다. 다만 모든 결과는 이론적 논증과 특정 가정·파라미터에 의존하므로 경험적 확인과 정책적 적용은 추가 연구가 필요하다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 금융중개(은행·딜러·지급수단 발행 등)가 동일한 기초환경에서 중개가 없을 때보다 다중 균형·주기·확률적 변동성(자기충족적 변동)을 일으키기 쉬운가, 그렇다면 어떤 메커니즘을 통해 그런 불안정성이 발생하는가? |
| 방법 | 이론모형 분석. 네 가지 동적 무한-기간 모형을 명시적으로 구축(1: 신뢰·평판을 포함한 확장된 Diamond–Dybvig; 2: 고정비·위임투자형 Diamond 계열; 3: OTC 자산시장 내 딜러·재고 모델; 4: 지급수단으로서 은행부채를 포함한 CM–DM 모형). 각 모형에서 균형 경로·정상상태·주기·선샤인(사인스팟) 균형·혼돈 가능성을 수학적으로 분석하고 예시적 파라미터로 동적 궤적을 제시. |
| 자료·범위 | 실증데이터 없음. 모두 이론·수학적·수치 예시(매개변수화)로 논증. 캘리브레이션은 아니며 논의는 논리적 가능성(logical possibility)에 초점. |
| 주제 | banking instability, financial intermediation, multiple equilibria, sunspot equilibria and cycles, search and OTC markets, money and payment instruments, dynamic general equilibrium |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장: 여러 이질적 모형에서 금융중개가 존재하면 동일한 기초환경에서 중개가 없을 때보다 다중·비안정적 균형(순환·혼돈·확률적 변동)을 가질 가능성이 넓게 확장된다.
- 저자 주장: 네 모형별 핵심 결과는 다음과 같다 — Model 1(보험·평판): 평판·현금횡령 위험이 있을 때 동적계에서 2주기·태양표(선샤인)·혼돈적 궤적이 가능하다; Model 2(고정비·위임투자): 규모의 경제와 유인문제로 인해 0을 포함한 여러 정적평형이 존재하고 정태적 다중균형 주변에서 선샤인 균형이 가능하다; Model 3(자산시장 중개): 딜러의 재고·교섭·시장구성의 내생성이 가격·유동성·거래량의 주기적·확률적 변동을 일으킬 수 있다; Model 4(안전성·비밀성): 은행부채가 더 안전하거나 정보적으로 둔감하면 거래매개체로서 역할이 강화되어 평형의 비선형성을 도입하고 순환·선샤인 가능성을 확대한다.
- 저자 주장: 불안정성이 생기더라도 중개활동은 대체로 (특히 Model 1·2 근처 정상상태에서) 복지 개선을 제공할 수 있으며, 중개가 반드시 나쁘다고 단정할 수는 없다.
- 저자 주장: 불안정성의 발생은 모델별로 다른 수학적·경제적 작동원리(예: f'의 부호 변화, 대리인의 프랜차이즈 가치 감소, 내생적 시장구성)가 핵심적 역할을 한다.
- 사서 주의: 논문은 이론적 가능성을 보여주는 데 집중하며, 제시된 비안정성은 특정 파라미터·제약·가정(유틸리티 형태, 재난확률, 협상 규칙, 만남 기술 등)에 의존함을 명확히 한다.
- 사서 주의: 제시된 다중·주기·선샤인 균형들 중 어떤 균형이 현실에서 선택되는지는 모델이 밝히지 않으며, 선호·정책·소음 등 추가 요소가 균형선택에 영향을 줄 수 있다.
- 사서 주의: 실증타당성(데이터 부합성)이나 정책적 유효성은 본문에서 칼리브레이션·검증 없이 논리적·수학적 결과로만 제시되어 있다.

## 메커니즘과 연결고리

- 평판·프랜차이즈 메커니즘: 은행의 미래가치(프랜차이즈)가 낮으면 현재 유인으로 인해 횡령 유혹이 커지고, 이로 인해 계약·예금구조가 변하여 동적비안정이 발생할 수 있음.
- 규모의 경제·고정비와 위임투자: 고정비를 공유하기 위해 적은 수의 큰 은행을 구성하면 은행 당 인센티브 문제가 악화되어 다중정상상태와 선샤인 균형을 초래함.
- 딜러 재고·교섭 피드백: 딜러가 재고를 보유하고 매매확률·교섭력·진입자수를 통해 유동성과 가격에 영향을 주면 가격·유동성·진입의 상호작용이 자기충족적 변동을 일으킴.
- 지급수단의 안전성·비밀성: 은행부채가 더 안전하거나 정보적으로 둔감하면 매매매개성분이 강화되어 자산의 교환수단 역할이 변화하고 비선형적 동학(f의 비단조성)을 유발함.
- 내생적 시장구성: 서비스 공급자(판매자·딜러·입장자) 수가 균형에서 결정되면 그 수가 거래확률·가격·유동성에 되돌아와 다중성·변동을 증폭함.

## 한계와 적용 범위

- 모형은 모두 이론모형이며 실증자료·계량추정이 제공되지 않아 경험적 적용성은 논문 범위 밖이다.
- 다수 결과는 특정 유틸리티·비용함수, 만남기술, 협상해법(예: 프로포셔널·Nash) 및 수치 파라미터에 의존한다; 다른 규격에서는 다른 동학이 나올 수 있다고 저자들이 명시함.
- 평판·평가·불법행위 탐지 확률 등 핵심 변수가 외생적으로 주어지거나 단순화되어 있어 현실의 복잡한 정보구조를 완전히 반영하지 못함.
- 균형 선택 문제와 조기정책(예: 규제·보호예금)이 균형을 제거 또는 선호하는 균형을 선택할 수 있으나 본문은 정책실험을 상세히 다루지 않음.
- 내생적 시장구성(예: 입장·퇴장 결정) 가정이 결과 핵심인 경우가 있어 해당 가정의 타당성에 따라 결과가 달라질 수 있음.
- 모형별 가정(무한시간, 일부 단기체류자·영구체류자의 혼합, 자산의 이산 재고 등)이 결과의 일반성에 제한을 둠.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_862-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[원자재 재고]]
- [[글로벌 유동성]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work862.pdf](https://www.bis.org/publ/work862.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work862.htm](https://www.bis.org/publ/work862.htm)


## References

[1]: https://www.bis.org/publ/work862.pdf "BIS Working Paper 862: On the instability of banking and other financial intermediation"
