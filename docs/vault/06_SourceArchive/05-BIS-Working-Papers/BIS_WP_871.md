---
title: "BIS WP 871 — The Matthew effect and modern finance: on the nexus between wealth inequality, financial development and financial technology"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 871
published: "July 2020"
authors: "Jon Frost , Leonardo Gambacorta and Romina Gambacorta"
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
  - "wealth-inequality"
  - "financial-development"
  - "financial-technology-(fintech)"
  - "household-finance"
  - "quantile-regression"
  - "instrumental-variables"
  - "italy"
  - "shiw"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 871 — The Matthew effect and modern finance: on the nexus between wealth inequality, financial development and financial technology

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

이 논문은 이탈리아 SHIW(1991–2016)를 이용해 '매튜 효과'가 존재함을 실증적으로 보이고, 지방별 은행지점 수(금융발전)와 가구의 원격뱅킹 이용(금융기술)이 금융자산 규모와 수익률을 유의미하게 높인다고 주장한다. 그러나 이 영향은 분포의 상위(특히 최상위 10%)에서 훨씬 크고, 은행지점과 원격뱅킹은 IV 추정 시 상호대체 관계로 나타난다. 기술 확산이 진전된 후기(2004–2016)에는 효과 크기가 축소되어 기술의 광범위한 보급이 부유층 중심의 이득을 완화했을 가능성이 제시된다. 다만 금융수익률의 측정방법(자산유형별 고정수익률 적용, 자본이득 제외), 원격뱅킹 및 도구변수의 후향적 보간·측정오차, 그리고 단일국 자료로 인한 일반화 한계 등으로 인해 인과 해석은 도구변수의 타당성에 의존하며 장기적 부 축적 메커니즘을 완전 확증하지는 않는다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 금융발전(지방별 은행지점 수)과 금융기술(원격·온라인 뱅킹)이 가계의 재무자산 수준 및 재무수익률에 어떠한 영향을 미치며, 그 효과가 부유층과 다른 계층에서 어떻게 다른가? 또한 이러한 효과가 시간에 따라(기술 확산에 따라) 어떻게 변화하는가? |
| 방법 | 이탈리아 가계조사 SHIW(1991–2016)를 사용해 금융자산 및 자산수익률을 종속변수로 설정하고 표준화된 지방별 은행지점 수(FD)와 가계의 원격은행 이용 여부(FT)를 주요 설명변수로 하는 IV(도구변수) OLS 및 IV-분위수(quantile) 회귀를 추정. 도구변수는 1989년 지점수(지점용), 지역별 인터넷 이용률(원격뱅킹용, 결측은 Tobit으로 보간), EPO 특허 건수(상호작용용, 결측 보간) 등. 통제변수로 연도 더미·가구특성·소득/부(wealth)계층 등 포함. 신뢰구간은 MCMB 부트스트랩 사용. |
| 자료·범위 | Bank of Italy의 Survey on Household Income and Wealth(SHIW) 1991–2016 패널·단면 자료(관측치 103,007). 주요 변수: 가구별 재무자산(금융자산), 추정된 금융수익률(자본이득 제외, 자산별 고정수익률 적용), 지방(성)당 은행지점 수(인구 10,000명당), 가계의 원격뱅킹 이용 여부(2000년 이후 조사, 1995–1998은 회귀로 역추정, 1991–1994는 0으로 처리). |
| 주제 | wealth inequality, financial development, financial technology (fintech), household finance, quantile regression, instrumental variables, Italy, SHIW |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장: 고부유층이 다른 가구보다 더 높은 재무수익률을 얻는 '매튜 효과'가 SHIW 데이터에서 관찰된다.
- 저자 주장: 은행지점 수(금융발전)와 가계의 원격뱅킹 이용(금융기술)은 모두 가구의 금융자산 규모와 금융수익률과 유의한 양(+)의 관계를 갖는다.
- 저자 주장: 이러한 양(+) 효과는 분포의 모든 분위에서 존재하나 상위 분위(특히 최상위 10% 구간)로 갈수록 효과가 훨씬 커진다.
- 저자 주장(규모): 최상위 10% 가구의 경우 은행지점 수의 표준편차(1SD) 증가가 금융자산 약 €33,000·금융수익률 약 2.7%p 증가와 관련되고, 원격뱅킹 이용은 각각 약 €4,000·0.28%p 증가와 관련된다.
- 저자 주장: 은행지점 수와 원격뱅킹의 상호작용 계수는 음(-)으로 추정되어 두 요인은 대체관계(substitutes)로 해석된다(IV 추정 기준).
- 저자 주장: 분석기간을 1991–2002(초기)와 2004–2016(후기)로 나누면 두 요인의 긍정적 효과는 두 기간 모두 존재하지만, 경제적 크기는 초기 기간에 훨씬 크고 후기에는 축소되었다. 후기 축소는 원격뱅킹 확산과 지점수 감소와 일치한다.
- 저자 주장: 고위험·비예금 자산(채권·펀드·주식 등)에 대한 효과는 최상위 가구에 더 집중되어 있으며, 상위 90–95 분위에서 특히 두드러진다.
- 저자 주장: 은행 특성(규모·자본·유동성)을 추가 통제해도 결과는 정성적으로 유사하다.
- 저자 관찰: OLS(비도구변수) 추정에서는 상호작용 계수가 양(+)으로 나타나지만, IV로 보정하면 음(-)으로 바뀌어 내생성으로 인한 편향이 존재함을 시사한다.

## 메커니즘과 연결고리

- 저자 제시: 은행지점 증가는 지역 내 금융서비스 접근성 증가·경쟁 심화로 더 나은 상품·조건을 제공해 저축·투자 기회를 확대하고 고수익 자산 접근성을 높인다.
- 저자 제시: 원격(온라인) 뱅킹은 지리적 제약을 완화해 투자상품 접근을 용이하게 하고 거래비용을 낮추어 참여와 효율을 높인다.
- 저자 제시: 부유층은 복잡·고위험·비표준 자산에 더 쉽게 접근하고 포트폴리오 다각화가 잘 되어 있어 동일한 금융발전·기술진전에서 더 큰 초과수익을 얻는 경향이 있다.
- 저자 주장: 초기에는 기술 도입 비용·기술·문해력의 차이 때문에 기술혜택이 부유층으로 집중되지만, 기술이 널리 확산되면 격차가 줄어드는 경로가 작동한다.
- 저자 해석: 은행지점과 원격뱅킹은 일부 조건에서 대체 관계로 작동할 수 있어 한 쪽의 발달이 다른 쪽의 한계를 완화시키는 방식으로 수익 격차에 영향을 준다.

## 한계와 적용 범위

- 단일국(이탈리아) 연구로서 결과는 은행중심 금융구조를 가진 선진국에 가깝게 일반화될 수 있으나 다른 제도·시장구조 국가로의 외삽에는 한계가 있다(저자도 명시).
- 금융수익률은 설문상 보고된 연말 보유잔액에 대해 자산유형별 '고정 수익률'을 적용해 추정한 값으로, 같은 자산유형 내 실제 수익률 차이(개별 종목·타이밍·거래내역 등)를 반영하지 못해 수익률 이질성·변동성을 과소평가할 가능성이 있다(자본이득은 제외).
- 원격뱅킹 변수는 2000년 이후 직접 수집되며 1995–1998년은 로지스틱 예측으로 보간, 1991–1994년은 0으로 설정하는 등 후향적 재구성이 있어 초기기간 측정오차 가능성이 존재한다(저자 설명).
- 도구변수들의 결측 연도는 Tobit으로 보간(인터넷 보급률, 특허건수 등)했으며 이 보간 자체가 도구의 측정오차/약화로 이어질 수 있고, 도구의 배제제약(exclusion restriction)이 완전히 만족된다고 확정하기 어렵다(예: 특허·1989년 지점수는 지역 경제구조·부에 직접적인 영향을 줄 수 있음).
- IV-분위수 추정의 식별은 도구의 강건성·정당성에 크게 의존하므로 도구가 약하거나 배제제약을 위반할 경우 원인추론이 제한된다(저자도 내생성 검정으로 IV 필요성 제시).
- 관측 가능한 통제변수(예: 재무문해력, 투자경험, 위험선호 등)로 완전히 통제되지 않은 잠재적 교란변수(예: 기술수용성·금융문해력)가 남아 있을 수 있으며, 이는 원격뱅킹 이용과 수익의 동시결정 문제를 남긴다.
- 연구 설계는 가구 수준의 단면·패널 혼합자료로 단기간 내의 관계를 분석하였으나, 장기적 복리(compounding)를 통한 부의 축적 경로를 완전하게 인과적으로 추적·증명하지는 못한다.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_871-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[통화정책]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work871.pdf](https://www.bis.org/publ/work871.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work871.htm](https://www.bis.org/publ/work871.htm)


## References

[1]: https://www.bis.org/publ/work871.pdf "BIS Working Paper 871: The Matthew effect and modern finance: on the nexus between wealth inequality, financial development and financial technology"
