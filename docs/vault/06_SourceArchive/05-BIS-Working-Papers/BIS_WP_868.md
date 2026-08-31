---
title: "BIS WP 868 — Debt De-risking"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 868
published: "June 2020"
authors: "Jannic Cutura , Gianpaolo Parise and Andreas Schrimpf"
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
  - "corporate-bond-funds"
  - "mutual-fund-incentives"
  - "liquidity-risk"
  - "flow-to-performance-sensitivity"
  - "swing-pricing"
  - "financial-stability"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 868 — Debt De-risking

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

저자들은 미국 기업채 오픈엔드 펀드의 분기별 보유데이터와 거래데이터를 이용해, 과거 성과가 낮은 펀드들이 유동성 리스크 노출을 줄이는 방식으로 'de‑risking'을 수행함을 실증적으로 보여준다. 이 행동은 신용·금리 리스크에는 거의 변화 없이 유동성 확보를 통해 향후 순유출을 줄이고 일부 성과손실을 만회하는 효과가 있었다. 토너먼트 유인은 일부 존재하나 평균적으로는 precautionary한 유동성 확보 동기가 우세하다. 다만 샘플·모형 선택, 파가중 사용의 해석범위, 환매 대 매매(선제적 판매 vs 유출충족) 구분, swing pricing 채택의 비외생성 등 한계가 있어 결과를 보다 넓은 제도·시스템 맥락에 일반화할 때는 신중을 기할 필요가 있다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 기업형(개방형) 채권 펀드에서 성과 악화가 펀드 매니저의 포트폴리오 위험조정(특히 유동성·신용·금리 노출 변경)에 어떤 영향을 미치는가? |
| 방법 | 미국 상장(집합투자) 채권펀드의 분기별 보유종목(eMAXX)과 CRSP 성과·유동성(TRACE, Mergent FISD) 자료를 결합하여, 파가액(par) 가중 포트폴리오 지표 기반의 '능동적 위험변화'를 종속변수로 패널회귀(기본식: 연-분기·펀드 고정효과 포함)를 추정하고, 개별 채권 거래수준 회귀(발행사×시점 고정효과 포함), IV 및 다양한 강건성 검정으로 인과성과 내생성 문제를 점검함. |
| 자료·범위 | 2004년 1월–2017년 12월 미국 소재 기업채 중심 오픈엔드 펀드(데이터에서 총 724개 펀드·2,288개 클래스). 포트폴리오 보유는 eMAXX(분기), 성과·AUM·클래스정보는 CRSP, 거래·유동성은 TRACE, 채권 기초정보 일부는 Mergent FISD. 리스크 지표로 Amihud, Roll, Bid–Ask, IQR(유동성), 신용등급(수치화), 듀레이션, 수익률 등을 사용. 성과(알파)는 주로 Vanguard Total Bond Index 대비 12개월 리스크조정 월별 평균으로 산출하되 대체 모형으로 강건성 확인. |
| 주제 | corporate bond funds, mutual fund incentives, liquidity risk, flow-to-performance sensitivity, swing pricing, financial stability |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저성과(해당 분기 기준 과거 12개월 리스크조정 성과가 교차분포 하위 50%) 펀드(이하 laggard)는 포트폴리오 리스크를 '감축(de-risking)'하며, 이 감축은 유동성 리스크 노출을 줄이는 방식으로 주로 이루어짐.
- laggard의 보유 신용노출(평균 등급)과 듀레이션(금리 민감도)은 유의하게 변화하지 않는 반면, 포트폴리오 평균 수익률(예: 잉여수익)은 하락(약 10bp 수준)하여 유동성을 위해 수익을 일부 포기함.
- 토너먼트(랭크 상승을 위한 위험증가) 유인은 채권펀드에서도 일부 관찰되나(상대적 성과에 대해 위험을 높이는 경향), 절대적(절대 성과 기준)로는 예비적 유동성 확보(precautionary de‑risking) 유인이 크고 정성적·양적 효과에서 우세함.
- 거래(트레이드) 수준 분석(발행사×시점 고정효과 포함)은 같은 발행사의 여러 채권을 대상으로 laggard가 특히 유동성이 낮고 고수익(저가) 채권을 줄이는 방향으로 거래함을 보여 자산기초충격(발행사 뉴스)에 의한 혼동을 부분적으로 배제함.
- de‑risking은 실증적으로 향후 순유출을 완화하고(예: 표준편차 단위의 유동성 증가가 향후 유출을 절반 가까이 감소시킴), laggard의 향후 초과수익·알파 손실을 상당부분 완화하여(대략 20–30% 수준) 결과적으로 실적 개선에 기여함.
- 시장상태·펀드특성에 따라 이 효과는 이질적임: 시장 스트레스(높은 VIX·TED), 포트폴리오가 비유동적일수록, 매니저 경력 짧음·리테일 고객 비중 높음·현금완충 낮음 등일수록 de‑risking이 강하게 발생함.
- 규제정책 관련 실증: 미국의 flexible NAV(선행적 swing pricing) 제도가 도입된 그룹의 경우 laggard가 오히려 위험을 증가시키는 경향을 보였으며, 저자들은 swing pricing이 precautionary 인센티브를 약화시켜 도덕적 해이(moral hazard)를 재도입할 수 있음을 제시함.

## 메커니즘과 연결고리

- 투자자 흐름 대 성과(flow-to-performance) 관계의 오목성(하락 구간에서 과도한 유출)은 저성과 펀드에 대해 '하방 리스크(레퓨테이션·계약해지·대규모 환매)'를 크게 증가시켜 매니저가 선제적 유동성 확보를 통해 손실확산을 막으려는 인센티브를 제공함.
- 개방형 펀드의 '선출자 이익(first-mover advantage)'은 대규모 환매시 초동 투자자가 비용을 다른 투자자에게 전가할 수 있게 하므로, 매니저가 미리 비유동자산을 줄여 모든 투자자에게 비용을 균등화하려는 유인이 생김.
- 토너먼트(랭크 경쟁) 인센티브는 존재하나 채권펀드에서는 절대적 유출 위험의 비대칭성이 토너먼트 유인을 압도해 평균적으로 de‑risking을 유도함.
- flexible NAV(스윙프라이싱)는 환매시 비용을 환매자에게 일부 전가하여 환매압력을 낮추므로 매니저의 예비적 de‑risking 인센티브를 약화시키고 위험추구를 촉진할 수 있음(잠재적 도덕적 해이).

## 한계와 적용 범위

- 샘플은 미국 소재 기업채 중심 오픈엔드 펀드(2004–2017)로 연구결과의 국제적·시기적 일반화에는 제한이 있음(예: 유럽·아시아, 또는 2020년대 위기상황과 차이 가능).
- laggard 분류는 과거 12개월 리스크조정 성과의 하위 50% 기준을 사용했으며(대체 컷오프는 검토), 분류·알파 산출 방식에 따라 표본 내 개체가 달라질 수 있음(저자도 대체모형으로 강건성 점검).
- 포트폴리오 리스크 지표는 파가액(par) 가중을 사용해 가격변동에 따른 기계적 변화는 제거하였지만, 이 방식은 시장가치 기반 투자자 인지·행동(예: 표시된 NAV 변화)에 대한 효과를 직접 반영하지 못함.
- 펀드의 매매가 '유동성 확보를 위한 선제적 매도'인지 아니면 '유출 충족을 위한 매도(pecking order)'인지의 구별은 어려우며, 저자는 이에 대해 다양한 제어(동시 유출통제·유입만 있는 펀드 샘플 등)를 수행했으나 완전한 배제는 불가능하다고 밝힘.
- 트레이드 수준과 IV 분석으로 인과성(내생성) 문제를 어느 정도 처리했으나, swing pricing 채택은 대부분 자발적이고 표본 내 처리군이 매우 작아(small‑treated sample) 해당 결과의 인과해석은 제한적임(채택 비외생성).
- swing pricing 효과 분석은 eMAXX 보유 이후(2019) 포트폴리오 분기데이터가 부족해 실현변동성(리얼라이즈드 리스크)을 사용한 결과임; 즉 포트폴리오 구성 변경 자체를 직접 관찰한 것은 아님.
- 저자들은 aggregate(동시 다수 펀드의 동질적) de‑risking이 위기 시 집단적 유동성경색을 유발할 가능성을 언급하나, 본 연구는 주로 펀드단위 미시행동을 분석하므로 시스템 차원의 일반균형·피드백 효과는 충분히 규명하지 못함.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_868-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[글로벌 유동성]]
- [[통화정책]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work868.pdf](https://www.bis.org/publ/work868.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work868.htm](https://www.bis.org/publ/work868.htm)


## References

[1]: https://www.bis.org/publ/work868.pdf "BIS Working Paper 868: Debt De-risking"
