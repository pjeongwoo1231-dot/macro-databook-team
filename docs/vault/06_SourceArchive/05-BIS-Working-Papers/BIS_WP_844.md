---
title: "BIS WP 844 — Variability in risk-weighted assets: what does the market think?"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 844
published: "February 2020"
authors: "Edson Bastos e Santos , Neil Esho , Marc Farag and Christopher Zuin"
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
  - "risk-weighted-assets"
  - "bank-internal-models"
  - "basel-iii"
  - "output-floor"
  - "market-implied-risk"
  - "bank-funding-costs"
  - "cross-country-regulation"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 844 — Variability in risk-weighted assets: what does the market think?

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

저자들은 Moody's KMV EDF를 F-IRB 공식에 대입해 계산한 시장기반 RWA와 은행이 보고한 규제 RWA의 비율(VR)을 제안·측정하고, 2001–2016년 대형 국제은행 패널을 통해 VR의 결정요인과 은행 비용에 미치는 영향을 분석했다. 주요 결과는 시장기반 RWA가 규제 RWA보다 지속적으로 높고 중앙 VR이 약 2이며, 파생상품 등 불투명자산 비중·자본제약(게임 유인)·관할권 요인이 VR을 유의하게 설명하고 VR이 WACC·CDS를 상승시킨다는 점이다. 또한 바젤3의 output floor는 국가단위로 VR을 줄이는 효과를 보였다. 다만 결과는 KMV·F-IRB 가정, 레버리지 보정 방식, QIS의 집계 한계 및 표본(대형국제은행) 제약 등으로 해석상 주의가 필요하며, '게임'의 인과적 확정에는 추가적 식별전략이 요구된다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 시장(모델·투자자)은 은행이 보고한 규제용 RWA와 비교해 은행별 RWA의 차이를 어떻게 보고 있으며, 그 차이(VR)의 결정요인과 은행 비용 및 바젤3 개혁(특히 output floor)이 그 차이에 미치는 영향은 무엇인가? |
| 방법 | Moody's KMV EDF(일별)를 연평균화하여 F-IRB 공식에 대입해 시장기반 RWA를 산출하고(기본 LGD 45%), 시장레버리지 효과를 회귀보정 및 KMV내부조정으로 제거한 뒤 'Variability Ratio = Market RWA / Regulatory RWA'를 계산함. 은행·연도·국가 패널(비정형, 연간)에서 VR의 결정요인과 VR이 WACC 및 CDS에 미치는 영향을 랜덤효과 패널회귀(강건 표준오차)와 고정효과(CDS 분석)에 따라 추정함. 바젤3 QIS(국가 집계, 2015년 잔고 기준)를 이용해 다양한 output-floor 보정이 VR 분포에 미치는 영향을 비교함. |
| 자료·범위 | 분석표본은 2001–2016년 연간 비정형 패널로 초기 91개(2016년 기준 총자산>2000억달러)에서 5년 이상 시계열 조건으로 76개 은행·21개국으로 축소. 주요 원자료는 FitchConnect(재무·규제), Moody's KMV(CreditEdge EDF), IHS Markit·Bloomberg(CDS·WACC) 및 BIS·BCBS(QIS 국가집계)이며 CDS·기타 시장자료는 연간평균으로 사용. BCBS QIS 데이터는 기밀·은행별 식별 불가하여 국가집계(샘플 17개국)로만 사용. |
| 주제 | risk-weighted assets, bank internal models, Basel III, output floor, market-implied risk, bank funding costs, cross-country regulation |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장: 제안된 Variability Ratio(VR)의 중앙값은 대체로 약 2로, 시장이 추정한 RWA가 많은 은행에서 규제보고 RWA보다 대략 두 배 높게 나타남.
- 저자 주장: 규제(RWA)보다 시장기반 RWA가 지속적으로 높고, 규제 RWA는 시장기반 RWA·자산변동성보다 덜 경기적(덜 변동적)임.
- 저자 주장: VR은 은행포트폴리오 구성에 따라 큰 차이를 보이며, 특히 파생상품 등 '불투명(복잡)' 자산 비중이 높은 은행에서 VR이 유의하게 높음(시장에 의한 'opaqueness premium' 가능성).
- 저자 주장: 2006년 기준 자본이 취약(하위 분위)했던 은행들은 이후 규제 RWA를 크게 낮춘 반면 시장기반 리스크는 덜 하락하여 VR이 높아졌고, 이는 자본제약이 있는 은행의 내부모형 '게임'(incentive to game) 가능성을 시사함.
- 저자 주장: 국가(관할권) 고유효과가 VR을 설명하는 데 강하게 유의미하며, 같은 은행특성·리스크 통제 후에도 국가별 차이가 남음(중국·인도·러시아 등은 시장·규제 간 차이가 상이).
- 저자 주장: VR 증가(시장·규제 불일치 확대)는 은행의 조달비용(가중평균자본비용 WACC 및 CDS 스프레드)을 유의하게 상승시키며 은행수익성에 직·간접적 영향이 있음.
- 저자 주장: 바젤3 최종안의 output floor(예: 72.5% 등) 적용 시 국가단위 VR 분포가 왼쪽으로 이동하며 과도한 VR(특히 상위 꼬리)가 완화됨; 75% 근방에서 마찰 완화 효과가 상당함.
- 저자 주장: 규제 RWA와 시장기반 리스크(자산변동성)가 위기기 일부 구간에서 역(-) 상관을 보이는데, 이는 내부모형 조작 또는 시장평가기법의 한계 가능성을 시사함(저자들은 'gaming' 및 정보비대칭을 원인으로 제시).
- 검토자 유의: 저자들은 위 결과들을 서술적·회귀분석으로 제시하며, '게임' 혹은 인과관계 주장에는 모델적·식별상의 한계가 있음을 논문 자체에서도 인정함.

## 메커니즘과 연결고리

- 시장 참가자는 파생상품·Level3 자산 등 복잡·불투명 자산에 대해 'opaqueness premium'을 부과하여 시장기반 RWA가 높아짐.
- 자본이 취약한 은행은 내부모형 사용으로 규제 RWA를 낮추려는 유인이 커져 규제·시장 간 괴리가 발생(모형 'gaming').
- 국가별 법·감독·회계·시장구조 차이가 규제 RWA·시장평가 간 불일치에 기여.
- 시장기반 리스크(EDF)는 레버리지·자산변동성의 결합 효과를 반영하므로 단순 RWA와의 비교를 위해 레버리지 보정 필요(회귀·KMV 내 보정 적용).
- 출력바닥(output floor)과 같은 규제제한은 내부모형으로부터의 하향편향을 제한해 VR의 과도한 상향편차를 축소.

## 한계와 적용 범위

- 본 연구의 '시장기반 RWA'는 Moody's KMV EDF와 F-IRB 공식(기본 LGD 45%)에 의존하므로 KMV·Merton모형과 F-IRB 가정(예: LGD·상관구조)에 민감함(저자도 LGD 40%·50% 민감도 제시).
- 레버리지 보정은 회귀 기반과 KMV 내 퍼핏(Within) 보정 두 방식으로 수행했으나 두 방식 모두 가정(평균 레버리지 대체, KMV DD↔EDF 매핑 등)에 의존하며 측정오차 가능성이 존재함.
- BCBS QIS 데이터는 은행단위 비식별·국가집계만 사용 가능하여 output-floor 효과 분석은 국가수준(샘플 17개국)이고 은행별 이질성 식별이 불가함.
- 표본은 대형 국제은행(총자산 임계치 기준)으로 국한되어 결과를 중·소형 은행이나 비국제은행군에 일반화할 수 없음.
- 시장지표(EDF·CDS)는 경기적·프로사이클릭 성질을 가지며 연간평균 처리로 단기정보는 흐려짐. 또한 시장과 규제 간 차이는 관측되지 않는 감독·회계·법률 요인이나 공개정보의 차이에서 기인할 수 있고, 이는 완전하게 통제되기 어려움.
- VR과 WACC/CDS의 관계는 통제변수를 포함한 회귀분석으로 제시되지만 내생성(endogeneity, 예: 높은 비용이 VR에 영향을 줄 수 있음) 문제가 완전히 해결되지는 않음(식별을 위한 자연실험·도구변수 부족).
- 파생상품·Level3자산 등 '불투명성' 지표는 표준화되어 있으나 측정오차·국가별 회계처리 차이가 있어 결과 해석에 제약이 있음.
- 랜덤효과 선택은 저자들이 통계검정을 제시했으나 고정효과나 패널 동적요인 등 대체식별전략 결과가 잠재적으로 다를 수 있음.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_844-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[통화정책]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work844.pdf](https://www.bis.org/publ/work844.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work844.htm](https://www.bis.org/publ/work844.htm)


## References

[1]: https://www.bis.org/publ/work844.pdf "BIS Working Paper 844: Variability in risk-weighted assets: what does the market think?"
