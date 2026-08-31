---
title: "BIS WP 873 — Effects of Fed policy rate forecasts on real yields and inflation expectations at the zero lower bound"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 873
published: "July 2020"
authors: "Gabriele Galati and Richhild Moessner"
source_kind: "working-paper"
peer_reviewed: false
primary_text_read: true
human_verified: true
reading_scope: "공식 PDF 전문·표·강건성 분석 직접 검토"
relevance_score: 5
created: 2026-08-14
updated: 2026-08-14
archive_status: "verified-primary-source"
tags:
  - flag/needs-review
  - bis
  - working-paper
  - "forward-guidance"
  - "zero-lower-bound"
  - "real-yields"
  - "inflation-expectations"
  - "event-study"
  - "monetary-policy-communication"
  - "term-premium"
  - "policy-credibility"
status: working
verification: full
reliability: working-paper
verified: "○ 원문 대조 완료(2026-08-14). 승격 노트로 이관됨 — 인용은 승격 노트를 쓸 것"
related: ["[[원문 아카이브 MOC]]"]
text_basis: human-fulltext
promoted_to: "[[2020 Effects of Fed Policy Rate Forecasts at the ZLB (Galati & Moessner)]]"
vault_tier: A
---

# BIS WP 873 — Effects of Fed policy rate forecasts on real yields and inflation expectations at the zero lower bound

> [!success] 원문 대조 완료 — 승격 노트 있음
> 이 노트는 마누스가 만든 원본이다. 2026-08-14 공식 PDF를 직접 대조해
> **[[2020 Effects of Fed Policy Rate Forecasts at the ZLB (Galati & Moessner)]]** 로 승격했다. **인용은 승격 노트에서 할 것.**

## 핵심 요약

저자들은 2012–2015년 SEP 공개일의 'lift-off' 시기 서프라이즈를 식별하여 이벤트스터디를 수행한 결과, Fed의 정책금리 전망이 ZLB 기간에 장기·중기 실질선행금리를 유의하게 낮추었으나 TIPS 기반의 장기 기대인플레이션(특히 5y/5y)은 유의미하게 변하지 않았다고 보고한다. 이는 SEP형 정량적 포워드가 실질금리 채널을 통해 경기에 영향을 줄 수 있었고, 동시에 통화정책 신뢰성에는 명백한 손상이 관찰되지 않았음을 시사하지만, 샘플·측정(프록시)·기간프리미엄·동시정책과의 식별 문제 등 해석상의 제한이 존재한다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 제로하한(ZLB) 상황에서 연방준비제도(Fed)의 정책금리 전망(SEP)이 장기 실질금리와 기대인플레이션에 어떤 영향을 미쳤는가? |
| 방법 | SEP 공개일의 '예상 인상 시기(days to lift-off)' 서프라이즈를 식별변수로 사용한 일별 차분(event-study) 회귀분석을 수행(종속변수: 2~10년 선행 실질 즉시 forward 금리 및 breake븐 인플레이션), 통제변수로 11개 거시지표 서프라이즈 포함, OLS 추정에 Newey‑West 표준오차 적용. 대체로 시장 기대의 프록시를 두 가지 방식으로 사용(구(式)와 가중합 방식). |
| 자료·범위 | 일별 샘플 2012-01-01~2015-07-31(SEP가 정책금리 전망을 게시하기 시작한 시점부터 금리 인상 직전까지). SEP의 중앙값이 37.5bp를 넘는 시점을 'lift-off'로 정의하여 SEPDAYS 산출. 시장 기대 프록시는 연방기금선물(fed funds futures)과 이전 SEP를 선형 보간/가중합하여 구성. 실질·breakeven은 미국 국채 및 TIPS로부터 즉시 forward율 산출(maturities 2~10년). |
| 주제 | forward guidance, zero lower bound, real yields, inflation expectations, event study, monetary policy communication |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장: SEP의 정책금리 전망 서프라이즈는 대체로 예상 방향으로 실질 선행금리에 유의미한 영향을 미침(대략 3~10년 선행에서 효과).
- 저자 주장: SEP에서 예상 인상 시기가 100일 늦춰진다는 서프라이즈는 3~6년 전방 실질 선행금리를 약 6bp(표준측정) 낮추었음; 대체 프록시 사용 시 2~4년 전방에서 약 9bp 낮아짐.
- 저자 주장: 반대로 선행 breakeven(물가보상)율은 전반적으로 거의 영향을 받지 않았고, 5년 후 5년 기대인플레이션(5y/5y)은 유의미한 변화가 관찰되지 않음 — 즉 신뢰도(credibility) 훼손 증거 없음.
- 저자 주장: 실질금리는 거시데이터 서프라이즈에도 반응하여 시장이 SEP 전망을 조건부 전망으로 인식했음을 시사.
- 저자 주장: 대체 프록시 분석에서는 단기(≤5년) breakeven이 소폭(약 2–4bp) 상승하는 결과가 일부 관찰됨.

## 메커니즘과 연결고리

- SEP의 정책금리 경로(예상 인상 지연) 신호가 장래 실질금리에 대한 시장의 기대를 낮춤 → 장기 실질금리 하락(수요·투자 채널을 통해 경기부양 가능).
- 시장참가자는 SEP 전망을 조건부 전망으로 해석한 듯하며, 거시데이터 뉴스에는 계속 반응하여 SEP가 전면적 헌신(commitment)이 아님을 반영.
- 장기 금리의 일부 변화는 기대 실질금리 변동이 아닌 기간 프리미엄(term premia) 조정에 의해 발생할 수 있음.
- SEP 서프라이즈가 기대인플레이션(특히 5y/5y)에 유의미한 변화를 주지 않아 통화정책 신뢰도에는 부정적 영향이 관찰되지 않음.

## 한계와 적용 범위

- 샘플 기간이 2012~2015년으로 제한되어 있으며, 분석은 금리 인상 직전까지의 SEP 공개일에만 적용됨(외삽 제한).
- SEP의 'lift-off'를 37.5bp 기준으로 정의하고 연간 중앙값을 선형보간한 SEPDAYS에 의존하는 측정상 결정(임계값·보간방법이 결과에 민감할 수 있음).
- 시장 기대의 프록시(FEDFDAYS 및 대체 가중합)는 기간 프리미엄(term premia) 변화의 영향을 받을 수 있어 '진정한' 시장 기대를 정확히 반영하지 못할 가능성을 저자들이 직접 지적함.
- 일별 event-study는 자산가격이 '서프라이즈'에만 반응한다는 합리적 기대 가정을 전제로 함; 비관찰적 정보·유동성·프리미엄 변화 등은 완전 통제 불가.
- 장기 실질금리 반응에는 기간 프리미엄 변화가 일부 기여했을 수 있음(저자들도 가능성을 제시).
- TIPS 기반 breakeven은 기대인플레이션뿐 아니라 유동성·인플레이션 리스크 프리미엄 등 복합요인에 의해 결정되므로, '정책 신뢰도'를 직접적으로 측정하는 한계가 있음.
- SEP 공개 외에 동시기에 작동한 다른 비정형 수단(양적완화, 질적 가이던스 등)과의 분리 식별이 완전하지 않음.


## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[CPI (소비자물가지수)]]
- [[기준금리]]
- [[통화정책]]
- [[BEI (기대인플레이션)]]
- [[산업생산]]
- [[글로벌 유동성]]

## 연결

- 국제 파급과 포워드가이던스: [[Monetary-Policy-Transmission-and-International-Spillovers]]
- 코로나 이후 정상화: [[Post-Pandemic-Inflation-and-Normalisation]]
- 정책 신뢰와 물가: [[BIS-Fulltext-Topic-Index]]

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_873-catalog]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work873.pdf](https://www.bis.org/publ/work873.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work873.htm](https://www.bis.org/publ/work873.htm)

## References

[1]: https://www.bis.org/publ/work873.pdf "BIS Working Paper 873: Effects of Fed policy rate forecasts on real yields and inflation expectations at the zero lower bound"
