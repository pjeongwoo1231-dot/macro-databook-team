---
title: "BIS WP 854 — Bank Funding Cost and Liquidity Supply Regimes"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 854
published: "April 2020"
authors: "Eric Jondeau , Benoit Mojon and Jean-Guillaume Sahuc"
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
  - "bank-funding-risk"
  - "forward-funding-spread"
  - "liquidity-regimes"
  - "multicurve-yield-construction"
  - "macroeconomic-predictability"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 854 — Bank Funding Cost and Liquidity Supply Regimes

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

저자들은 OIS 할인곡선과 테너별 포워딩 곡선을 다중곡선 방식으로 일별 구성해 은행의 롤오버·조달리스크를 반영하는 Forward Funding Spread(FFS)를 제시했다. FFS는 중앙은행의 유동성 레짐(위기·풍부·중간)을 구별하는 데 유용하며, 특히 풍부유동성기에는 스팟 SFS보다 정책·시장 기대의 변화를 더 잘 드러낸다. 실증적으로 FFS는 미국·유로지역의 실물지표와 은행대출의 향후 변동을 SFS·CDS·은행채 스프레드보다 우수하게 예측했고, 레짐별 차이가 코로나19 초반 양대권의 스프레드 반응 격차를 설명한다. 다만 분석은 예측회귀와 단순 Markov-Switching 모형에 의존하며 인과식별·외삽성·곡선 추정 파라미터 선택에 따른 제약이 존재한다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 시장 기대(선도금리)를 이용한 은행의 장래 조달비용 지표(FFS)가 현행 스팟 SFS와 비교해 유동성 상황·통화정책 태도·거시예측에 대해 어떤 정보를 제공하는가? |
| 방법 | 달러·유로 단기금융시장의 예금·FRA·OIS·IRS·기초스왑 시세를 바탕으로 OIS 할인곡선과 테너별 포워딩 곡선을 다중곡선 방식으로 일별 보트스트랩·최적화(평활성 제약 포함)해 선도금리에서 FFS를 계산하고, Markov-Switching(3상)으로 통계적 유동성 레짐을 탐지하며, 통제변수(실질 단기금리·턴프리미엄·지연 변수)를 둔 예측회귀로 실물·대출 예측력을 비교함. |
| 자료·범위 | 일별 인터뱅크 시세(2005.01–2020.09 기준으로 USD·EUR 중심; JPY·GBP용 시계열도 제공)로 1·3·6·12개월 테너 곡선 구축; CDS(5년)·은행회사채 스프레드(GZ·GM)와 분기별 실질 GDP·소비·투자·실업률·은행 대출(세부항목 포함)을 사용해 예측회귀(분기단위)는 2005.01–2019.12 표본으로 수행(2020은 예측회귀에서 제외). |
| 주제 | bank funding risk, forward funding spread, liquidity regimes, multicurve yield construction, macroeconomic predictability |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- FFS는 시장참가자의 장래 조달비용 기대를 반영하는 일별 지표로 구현 가능하며 3·6개월 곡선의 시장가격과 매우 근접하게 적합됨(일반적으로 상대오차 수bp 수준).
- FFS는 중앙은행의 잉여유동성 수준과 일치하는 세 가지 레짐(위기·풍부·중간)을 식별하는 데 유용하며 Markov-Switching 결과와 서술적 사건(예: QE, LTRO, OMT)과의 대응성이 높음.
- 위기기에는 FFS와 SFS가 모두 급등해 유동성과 신용리스크가 결합되는 반면, 풍부유동성기에는 SFS가 압축되고 FFS가 보다 정보 제공력이 있어 기대(지속성)가 중요해짐.
- 미·유로 지역 실증에서 FFS는 SFS·CDS·은행 채권스프레드보다 GDP·소비·투자·실업률의 향후 변동을 더 잘 설명(조정 R2 기준)함—특히 유로지역에서 3개월 FFS의 예측력이 강함.
- 은행대출 예측에서는 장기 기대(예: 12개월 FFS)가 중요해, 대출 예측에는 보다 먼 시작일자·긴 테너의 FFS가 더 우수한 성과를 보임(미국에서 두드러짐).
- 코로나19 초기에 미국과 유로지역의 FFS·SFS 반응 차이는 사전 유동성 레짐의 차이로 설명 가능하며, 통화당국의 신속한 유동성 공급(다채널 조치)이 스프레드 진정에 기여함.

## 메커니즘과 연결고리

- 단기 조달의 만기불일치로 인한 롤오버 리스크는 은행의 신용공급 의사결정에 영향을 주며, 그 핵심 신호는 장래 조달비용 기대(FFS)임.
- 중앙은행의 대규모 유동성 공급(QE·LTRO·TLTRO·PEPP 등)은 유동성 레짐을 풍부 상태로 이동시켜 SFS를 억압하지만 시장은 FFS(지속성)를 통해 통화정책 태도의 변화를 반영함.
- FFS 상승은 은행의 자금조달 여건 악화를 통해 은행대출 축소로 이어지고, 이는 실물변수(소비·투자·GDP·고용)에 하방압력을 가함(자금조달 채널).
- 정책 충격에 대해 SFS는 즉각적 현황을, FFS는 시장의 기대·지속성 판단을 보여 중앙은행의 대응 시점·규모 결정에 보완적 정보를 제공함.

## 한계와 적용 범위

- 논문은 인과관계를 주장하지 않고 주로 예측력·상관관계 분석을 제공함(예측회귀는 인과 식별을 보장하지 않음).
- 예측회귀 표본은 2005–2019년 단일 경기주기(그리고 의도적으로 2020년 팬데믹 충격은 제외)로 구성되어 있어 외삽에 제약이 있음.
- FFS 구성은 깊은 거래시장(주로 대형은행·국채·파생상품 유동성)에 의존하므로 소형은행·지역별 비시장 조달은 포착하지 못함.
- 곡선 보간·평활(예: 목적함수 가중치 w=0.25, 3개월 전도율 기준 N=120 등)과정에서 선택된 파라미터·보정이 측정오차를 유발할 수 있음(추정값 민감도 존재).
- FFS가 '시장 기대'를 반영한다고 해도 선도금리에 내재된 위험프리미아와 기대(효율적예측가설 불완전성)을 완전히 분리하지 못함.
- CDS·회사채 기반 신용지표는 표본·유동성·집계 방식의 제한(데이터 소스별 차이)을 저자 스스로 지적함.
- Markov-Switching 모형은 3상 단순 모형으로 레짐의 동학·다변량 상호작용을 완전하게 포착하지 못할 수 있음.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_854-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[글로벌 유동성]]
- [[GDP 성장률]]
- [[실업률]]
- [[통화정책]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work854.pdf](https://www.bis.org/publ/work854.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work854.htm](https://www.bis.org/publ/work854.htm)


## References

[1]: https://www.bis.org/publ/work854.pdf "BIS Working Paper 854: Bank Funding Cost and Liquidity Supply Regimes"
