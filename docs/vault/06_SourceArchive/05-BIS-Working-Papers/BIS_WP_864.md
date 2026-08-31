---
title: "BIS WP 864 — Global and domestic financial cycles: variations on a theme"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 864
published: "May 2020"
authors: "Iñaki Aldasoro , Stefan Avdjiev , Claudio Borio and Piti Disyatat"
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
  - "global-financial-cycle"
  - "domestic-financial-cycle"
  - "financial-cycle-duration"
  - "capital-flows"
  - "credit-and-property-prices"
  - "macroprudential-policy"
  - "business-cycle"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 864 — Global and domestic financial cycles: variations on a theme

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

이 논문은 국내금융주기(신용·주택가격 중심)와 글로벌금융주기(위험자산가격·국경간자본흐름 중심)를 비교·대조한다. 두 주기는 공통적 친주기성 메커니즘을 공유하지만 구성자산, 지속기간, 실물연계 주파수에서 차이가 크다: GFCy는 단기적(전통적 경기주기)이고 선진국 주도로 나타나며 DFC는 더 긴(중기) 주기이며 GDP의 중기 변동과 강하게 연계된다. 평상시에는 두 주기 연동이 약하나 금융·은행 위기 국면에서는 DFC가 먼저 고조되고 GFCy와 자본흐름이 뒤따라 폭발적 영향을 주며 위기를 증폭한다. 방법론은 밴드패스 필터, 요인·주성분 분석, 스펙트럼 분석, 국가별 회귀 등을 활용했으나 측정 선택·표본편중·식별제약 등으로 인과 추론과 일반화에는 제한이 있다. 정책적으로는 거시금융안정 프레임과 중기 시계열을 정책 목표에 더 반영할 필요가 있다는 결론을 제시한다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 국내 금융주기(DFC)와 글로벌 금융주기(GFCy)는 구조·경로·주기성 측면에서 어떻게 다른가, 그리고 두 주기는 실물활동과 어떻게 연결되는가? |
| 방법 | 저자들은 DFC를 Drehmann 등(2012) 방식으로 실질신용, 신용/GDP 비율, 실물주택가격의 밴드패스 필터(5–32·32–120분기)로 구성하고, GFCy는 Miranda‑Agrippino·Rey의 가격기반 동적요인과 IMF BoP의 국가별 총자본유입/GDP의 주성분을 결합한 혼합(단순평균)으로 측정함. 스펙트럼 분석(주기성), 주성분분석, 국가별 회귀(민감도 추정), 위기 전후 평균 비교 등을 사용. |
| 자료·범위 | 장기(1981Q1–2018Q4) 및 단기(1996Q1–2018Q4) 표본을 사용. 신용·주택가격 등 DFC 구성요소는 BIS 데이터베이스(국가소스), 자본유입은 IMF BoP, GFCy 가격요인은 Miranda‑Agrippino·Rey 데이터, 실질 GDP는 국가통계. 장기표본의 자본흐름 자료는 31개국(단기 49개국), 실질신용자료는 장기 30개국(단기 40개국). |
| 주제 | global financial cycle, domestic financial cycle, financial cycle duration, capital flows, credit and property prices, macroprudential policy, business cycle |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장: DFC와 GFCy는 공통의 분석적 기반(금융시스템의 친주기성, 자금조달·위험선호·자산가격 상호작용)을 공유하나 구성요소와 정책초점이 다르다(DFC: 신용·부동산·취약성 축적; GFCy: 국경간 자본흐름·위험자산가격·미국/선진국 영향).
- 저자 주장: 가격기반 GFCy와 규모(자본유입) 기반 GFCy는 서로 매우 유사해(서로 높은 상관), 이를 단순 평균한 복합지표를 벤치마크로 사용해도 무방하다.
- 저자 주장: GFCy는 지속기간이 짧아 전통적 경기순환(5–32분기)과 강하게 연동되며(예: GFCy가 2분기 지연될 때 상관 약 0.6), 주로 선진국 동향을 반영한다.
- 저자 주장: DFC 구성요소(실질신용·신용/GDP·실물주택가격)는 더 긴 주기를 보이며(스펙트럼 피크: 단기범위에서 약 6년대, 중기범위에서 ~20년 근처), GDP의 중기(32–120분기) 변동과 밀접히 연계된다(DFC는 GDP보다 후행하는 경향, 대략 4분기 지연).
- 저자 주장: 국가간 동기화 측면에서 GFCy는 설계상 전지구적 요인이나(공통요인 분산 비중 약 22%), 실제로는 선진국 자본흐름에 더 강하게 대표된다(선진국 표본의 1차 주성분 비중이 더 큼).
- 저자 주장: EMEs의 자본흐름은 1차 공통요인보다 2차 공통요인과 더 밀접하게 연동되며(EME 관련 2차성분의 중요성), EMEs는 환율·신용·주가 측면에서 GFCy 충격에 대해 더 큰 '영향력'(sensitivity)을 보인다.
- 저자 주장: 두 주기는 평상시엔 약하게 연동되지만 금융·은행 위기 국면에서는 함께 상승/하락하며(DFC가 먼저 상승하고 GFCy·자본흐름이 뒤따라 '터보차지'), 위기시 실물충격이 증폭된다.
- 정책결론(저자 주장): DFC와 GFCy를 억제하려면 통화·거시건전성·재정 정책을 결합한 거시금융안정 프레임워크가 필요하며, 중기 관점(32–120분기)을 정책설정에 더 반영해야 한다.

## 메커니즘과 연결고리

- 공통메커니즘(저자 주장): 통화정책이 레버리지 가격을 설정하고 자금비용·위험선호를 통해 신용·자산가격·리스크테이킹을 친(증폭)주기적으로 움직이게 함.
- DFC 메커니즘: 은행·신용 확대와 주택가격 상승을 통해 중기적 취약성(부채 축적·담보·한계차주)을 쌓고, 이는 추후 붕괴 시 심각한 실물충격으로 이어짐.
- GFCy 메커니즘: 미국(선진국) 통화·위험자산가격 변화가 국제자본배분을 통해 자본유입/유출을 유발, 크로스보더 은행·투자 흐름이 전파 채널로 작동함.
- 위기상호작용: DFC가 먼저 팽창해 국내 취약성을 키우면 이후 글로벌 자본유입·가격 요인이 합류하여 부푼 거품을 '터보차지'하고 위기 시 동시에 축소되어 충격이 확대됨.
- EME 취약성 기여요인: 시장 얕음, 제도·거래기반 약화, 외국인 투자 기반의 변덕, 환위험(통화 불일치)이 동일 충격에 대한 EMEs의 영향 확대를 설명.

## 한계와 적용 범위

- 측정 관련: DFC 벤치마크는 Drehmann식(실질신용·신용/GDP·주택가격)으로 제한되어 다른 금융지표(예: 주식·금리·환율 결합지수)를 배제한다는 한계가 있다.
- 측정 관련: GFCy의 가격기반 측정치는 자산별(전세계 자산) 요인으로 국가별 이질성을 잡아내지 못하고, 규모기반 측정치는 총유입(또는 총유출) 선택에 따라 결과가 달라질 수 있다; 복합지표는 단순 평균이라는 임의성이 있다.
- 표본·대표성: 사용국가 표본은 선진국에 편중된 부분이 있어(특히 장기표본) 결과가 선진국 주도 현상을 과대평가할 가능성이 있다.
- 주파수·필터링 의존성: 밴드패스 필터(Christiano‑Fitzgerald)와 선택한 주파수대(5–32, 32–120분기) 및 스펙트럼 추정 파라미터에 민감할 수 있어 주기 추정치가 방법론에 의존한다.
- 인과식별의 부재: 상관·공동변동성 분석과 회귀 민감도 추정은 인과관계(예: GFCy가 DFC를 유발한다)를 확증하지 않으며 잠재적 내생성/오미션 문제가 남음.
- 단면·시계열 제약: 일부 분석은 가용한 균형패널(예: 16개국)로 제한되어 있고, 결과의 일반화에는 한계가 있다.
- 위기분석 한계: 위기 전후 평균 비교는 동시성과 타이밍을 보여주나 구조적 원인 규명에는 제약이 있다.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_864-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[GDP 성장률]]
- [[주택가격]]
- [[PPI (생산자물가지수)]]
- [[산업생산]]
- [[원·달러 환율]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work864.pdf](https://www.bis.org/publ/work864.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work864.htm](https://www.bis.org/publ/work864.htm)


## References

[1]: https://www.bis.org/publ/work864.pdf "BIS Working Paper 864: Global and domestic financial cycles: variations on a theme"
