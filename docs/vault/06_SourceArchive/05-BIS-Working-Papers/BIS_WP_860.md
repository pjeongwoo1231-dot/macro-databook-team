---
title: "BIS WP 860 — Dollar invoicing, global value chains, and the business cycle dynamics of international trade"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 860
published: "April 2020"
authors: "David Cook and Nikhil Patel"
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
  - "dollar-invoicing"
  - "global-value-chains-(gvcs)"
  - "open-economy-new-keynesian-dsge"
  - "exchange-rates"
  - "monetary-policy-spillovers"
  - "value-added-trade-decomposition"
  - "local-projection-estimation"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 860 — Dollar invoicing, global value chains, and the business cycle dynamics of international trade

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

저자들은 달러 중심의 청구체계와 글로벌 가치사슬을 동시에 고려한 3국 DSGE 모형을 통해, 미국(글로벌 통화) 금리·환율 충격이 지역 간 최종재 교역과 가치사슬(중간재) 교역에 서로 다른 영향을 준다고 보여준다. 실증적으로는 WIOD와 Wang–Wei–Zhu의 부문별 가치부가 분해를 이용한 패널 추정에서 비미국향 거래가 미국향 거래보다 상대적으로 더 크게 줄어드는 등 모형 예측과 일치하는 패턴을 관찰했다. 다만 모형의 단순화·데이터 보간·식별 한계로 정량적 일반화는 신중해야 한다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 달러(국제 통화)로 청구되는 거래와 글로벌 가치사슬이 국제무역의 경기 변동성과 통화·환율 충격에 어떻게 영향을 미치는가? |
| 방법 | 이론: 3개국(미국(글로벌 통화 발행국) + 두 지역 소규모 경제) 뉴케인즈 DSGE 모형을 설정하여 달러(DCP)로의 가격표시, 중간재로 구성된 수출 플랫폼(GVC)과 가격경직을 도입하고 외부(미국) 금리 충격 및 지역별 통화 충격을 시뮬레이션함. 실증: WIOD(1995–2011, 40개국·35개업종)와 Wang–Wei–Zhu의 가치부가·8항목 분해를 사용, US 정책금리(그림자금리)를 충격으로 한 로컬 프로젝션(지역 패널)추정, 라그드 종속변수 포함으로 차분 GMM(아렐라노–본드) 이용. |
| 자료·범위 | 연간 WIOD 1995–2011, 40개국·35개업종; 실증분해는 Wang–Wei–Zhu(양방향·부문별 가치부가·간접·직접 분해) 사용; 미국 정책금리 대리치는 Lombardi·Zhu의 그림자금리; 유럽 국가는 표본에서 제외한 분석도 보고. |
| 주제 | dollar invoicing, global value chains (GVCs), open-economy New Keynesian DSGE, exchange rates, monetary policy spillovers, value-added trade decomposition, local projection estimation |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장 — 모형 예측: 미국(글로벌 통화) 금리 상승에 따른 달러 실질 강세(지역 통화의 달러 대비 평가절하)는 비(미국) 지역 간의 직접적인 최종재 교역을 크게 축소시키는 반면, 미국의 최종수요를 위한 글로벌 가치사슬 관련 중간재 교역은 더 덜 축소되거나 경우에 따라 확대될 수 있다.
- 저자 주장 — 모형 동학: 외부 금리 상승(달러 강세) 시 두 지역의 대미 수출(글로벌 수출)은 증가하고 지역 간 상호 수출(지역 내 최종재)은 감소하는 경향을 보이며, 지역의 부가가치 수출은 미국향보다 지역향에서 더 크게 줄어든다.
- 저자 주장 — 정책 효과: 통화정책 체계에 따라(고정환율·CPI·PPI 표적) 환율·물가·생산·무역의 조정 경로가 달라지며, 고정환율은 내수·고용에 더 큰 실물손실을 유발한다는 예비적 시사.
- 실증 주장: Wang–Wei–Zhu의 부문·양자별 가치부가 분해를 이용한 패널 로컬프로젝션 추정에서, 미국 긴축(그림자금리 상승) 후 비미국행 대비 미국행 가치부가 비율(r_x)이 유의하게 하락 — 즉 비미국 최종소비로 흡수되는 가치부가가 미국향보다 더 크게 감소하여 모형 예측과 일치하는 패턴이 관찰된다.
- 실증 추가: 단순한 중간재/최종재 이분법이나 총수출(거시 총계)으로는 모형 예측을 포착하기 어렵고, 다단계 국경횡단을 반영한 미시적 가치부가 분해가 필요하다고 보고됨.
- 상세 실증: 직접·간접 가치부가(VAF, VAB, IVAF, IVAB) 모두에 대해 비미국/미국 비율이 지속적으로 하락하는 결과를 보고함; 업종별로는 1차(원자재) 섹터에서 차별적 동학이 뚜렷하지 않음(데이터 측정·보간 문제 가능성).

## 메커니즘과 연결고리

- 달러(지배 통화) 청구(DCP): 수출가격은 달러로 표기되면 환율 변동이 수출가격에 즉각 전체적으로 전가되지 않아 수출 통화전달(passthrough)이 약화되고, 반대로 수입가격은 달러 표시이므로 환율 변동이 즉시 소비자 물가·수입가격에 강하게 전가된다.
- 대체효과: 지역 통화의 달러 대비 평가절하(달러 강세)는 지역 소비자 입장에서 달러표시 수입을 비싸게 만들어 국내품으로의 대체를 촉진하고 지역 간 최종재 교역을 축소한다.
- GVC(수출 플랫폼): 지역 간 중간재(플랫폼용 소재)는 최종수요(특히 글로벌 수요)에 더 민감하므로, 미국(글로벌) 수요가 상대적으로 강화되는 경우(예: 달러 강세에 따른 글로벌 가격·수요 변화)에는 GVC 관련 중간재 수요가 덜 위축되거나 증가할 수 있다.
- 가격경직·일반균형: 수출가격의 경직성과 환율·정책금리의 일반균형 조정으로 특정 통화정책(고정환율 vs CPI/PPI 표적)에 따라 수출·수입·내수의 조정 경로가 달라짐(예: 고정환율은 내수·생산에 더 큰 실물 충격을 유발).
- 경로종속성: 동일한 환율 변동이라도 청구통화(누가 청구하는가)와 무역거래의 성격(최종재 vs 중간재, 재수출여부)이 다르면 교역 반응의 크기와 방향이 달라짐.

## 한계와 적용 범위

- 저자 경고 — 충격 해석: 모형의 '미국 금리 상승' 충격은 외생적으로 가정되어 있으며, 실제로 미국 금리 상승이 미국의 수요 위축을 동반하면 실증 결과는 모형과 반대로 편향될 수 있으나 본 분석은 이점을 감안해도 결과가 일관됨을 주장함.
- 저자 경고 — 모형 단순화: 모형은 정량적 추정보다 질적 메커니즘 제시에 초점을 둔 단순화된 구조(금융마찰·다양한 조정메커니즘·자본·국제부채·금융채무 통화표시 등 미포함)여서 수치적 크기나 복합채널의 상호작용을 완전히 재현하지 못함.
- 데이터 제한: WIOD와 Wang–Wei–Zhu 분해는 업종·국가간 보간·추정이 포함되어 있어 원자재(상품) 부문의 측정오차 가능성 존재, 또한 연간 패널·1995–2011 기간으로 최근 변화(예: 2010s 후반)의 반영이 제한적임.
- 식별 한계 및 계량: 실증은 미국 그림자금리를 외생충격으로 사용하고 로컬 프로젝션+차분GMM을 적용하나 내생성·동학적 상호작용(예: 동시 수요충격, 정책예고효과) 완전 제거는 어려움.
- 모형 가정: 모든 대외거래를 달러로 청구(DCP 전제)하고 지역 내 거래에서 자국통화 사용 등 단순화된 청구 통화 규칙을 가정하므로 실제 청구통화의 이질성(부분적 PCP/LCP 혼재)을 완전히 반영하지 못함.
- 표본 선택: 유럽 국가들을 분석에서 제외한 결과를 주로 제시하였고 이 제외·포함에 따른 민감도 및 결과 일반화 가능성은 한계.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_860-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[원·달러 환율]]
- [[통화정책]]
- [[DXY (달러지수)]]
- [[기준금리]]
- [[CPI (소비자물가지수)]]
- [[PPI (생산자물가지수)]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work860.pdf](https://www.bis.org/publ/work860.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work860.htm](https://www.bis.org/publ/work860.htm)


## References

[1]: https://www.bis.org/publ/work860.pdf "BIS Working Paper 860: Dollar invoicing, global value chains, and the business cycle dynamics of international trade"
