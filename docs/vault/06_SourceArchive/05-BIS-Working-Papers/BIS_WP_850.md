---
title: "BIS WP 850 — The impact of unconventional monetary policies on retail lending and deposit rates in the euro area"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 850
published: "March 2020"
authors: "Boris Hofmann , Anamaria Illes , Marco Jacopo Lombardi and Paul Mizen"
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
  - "unconventional-monetary-policy"
  - "retail-lending-rates"
  - "deposit-rates"
  - "pass-through"
  - "ecb"
  - "euro-area-heterogeneity"
  - "event-study"
  - "ardl-/-sur"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 850 — The impact of unconventional monetary policies on retail lending and deposit rates in the euro area

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

이 논문은 일별 이벤트 스터디로 UMP 발표가 EURIBOR·국가별 은행채에 미친 누적효과를 추정하고, 월별 ARDL/SUR로 소매금리 패스스루를 계산해 무(無)UMP 반사실을 시뮬레이션하였다. 결과는 UMP가 소매대출·예금금리를 실질적으로 낮췄고(효과 집중 시점: 2012 OMT·2014 이후 APP), 효과는 이탈리아에서 특히 컸으며 은행 중개마진 영향은 독일·이탈리아에서만 유의하게 축소되었다는 것이다. 다만 이벤트 식별·프록시 측정·내생성 등 방법론적 한계와 발표 전후의 비가시적 채널 미포착으로 결과가 보수적일 가능성이 있음을 저자도 지적한다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | ECB의 2008–2019 기간 비전통적 통화정책(UMP)이 주요 유로지역(독일·프랑스·이탈리아·스페인)의 가계 및 비금융법인 대상 소매대출·예금금리에 어떤 영향을 미쳤는가? |
| 방법 | 두 단계 분석: (1) ECB UMP 주요 발표일을 이용한 일별 이벤트 스터디로 EURIBOR(3·12개월) 및 국가별 단기·장기 은행채(스왑요율+금융 CDS) 누적 발표효과 추정, (2) 월별 ARDL(시스템은 SUR로 추정)를 통해 소매대출·예금금리에 대한 EURIBOR·은행채의 장기 패스스루 산정 및 발표효과를 반영한 무(無)UMP 반사실(counterfactual) 시뮬레이션. |
| 자료·범위 | 기간: 2007–2019. 대상국: 독일·프랑스·이탈리아·스페인. 일별: 3·12개월 EURIBOR, 단기(1년)·장기(5년) 은행채(1·5년 스왑 + 각국 금융 CDS) 프록시. 월별: ECB MFI 통계의 신규 단기·장기 대출·예금 금리(가계·비금융법인). 원자료 출처로 Bloomberg, Markit, Datastream, ECB 사용. |
| 주제 | Unconventional monetary policy, Retail lending rates, Deposit rates, Pass-through, ECB, Euro area heterogeneity, Event study, ARDL / SUR |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장: ECB의 UMP는 네 개 주요국의 소매대출·예금금리를 경제적·통계적으로 유의하게 낮추었다.
- 저자 주장: 효과의 대부분은 2012년 OMT 발표와 2014년 중반 이후 대규모 자산매입(APP) 이후에 집중되었다.
- 저자 주장: 국가별 이질성 존재 — 독일·프랑스·스페인의 대출금리는 대체로 100–200bp 하락, 예금금리는 50–150bp 하락; 이탈리아에서는 대출 250–450bp, 예금 150–250bp 수준의 하락을 보였다.
- 저자 주장: 이벤트 스터디 결과 EURIBOR에 대한 UMP의 누적 영향은 제한적(약 0.5%포인트)인 반면 은행채(프록시) 수익률에는 더 큰 하락이 관측되어(국가별로 수%포인트, 이탈리아에서 가장 큼) 소매금리 하락에 기여했다.
- 저자 주장: 소매금리의 가격결정에서 국가별 차이 — 이탈리아·독일·프랑스의 장기 소매금리는 은행채 영향력이 크고 스페인은 단기·장기에서 EURIBOR의 영향이 비교적 큰 편이었다.
- 저자 주장: 은행의 중개마진(대출-예금 스프레드)에 대한 UMP의 영향은 명확하지 않으며 통계적으로 유의한 스프레드 축소는 독일과 이탈리아에서만 관찰된다(독일: 50–150bp 더 높았을 것, 이탈리아: 100–250bp 축소 추정).
- 저자 주장: 월별 ARDL(장기 승수) 추정치는 EURIBOR 및 은행채의 장기 패스스루가 많은 경우에선 상당히 크거나 완전한 수준임을 시사한다(국가·상품별 이질적).

## 메커니즘과 연결고리

- 저자 주장: 유동성공급은 은행의 유동성·신용위험을 낮춰 은행 자금조달비용과 국채·은행채 스프레드를 축소한다.
- 저자 주장: 대규모 자산매입은 포트폴리오·지속시간(duration)·신용프리미엄 채널 및 신호(signalling)를 통해 장기금리·기간프리미엄·신용스프레드를 낮춘다.
- 저자 주장: 유로존의 강한 소버린-은행(sovreign-bank) 연계로 은행의 위험완화는 국채수익률 하락으로도 연결된다.
- 저자 주장: 최종적으로 은행은 소매대출·예금금리를 자금비용(또는 기회비용)인 benchmark(예: EURIBOR, 은행채)에 마크업/마크다운으로 가격화하므로 benchmark 하락은 지연을 동반하여 소매금리 하락으로 전달된다.

## 한계와 적용 범위

- 저자(명시): 추정치는 ECB의 UMP 효과만을 반영하며 정책금리 인하(통상적 완화)의 효과는 포함하지 않는다.
- 저자(명시): 이벤트 스터디는 발표일 즉시·완전한 시장가격화를 가정하므로 발표 전 선(anticipation)효과나 발표 이후의 구현(implementation)·신뢰감(confidence) 채널 등은 포착하지 못해 추정치가 하방편향(상수치의 하한)일 수 있다.
- 저자(명시): 본 연구는 UMP가 신용·실물에 미친 효과(대출량·성장·물가)를 직접 평가하지 않으며 그 점은 별도 문헌에서 다루어져야 한다.
- 사서(추가): 이벤트 스터디 식별은 '발표가 외생적'이라는 가정에 의존하며 발표와 동시 다수 경제·정책 뉴스의 상호작용으로 인해 개별 발표효과 분리에 한계가 있다.
- 사서(추가): 은행채 수익률을 스왑금리 + 금융 CDS 평균으로 근사한 것은 발행종류·만기·시장유동성 차이를 무시하는 간단화로, 실제 발행비용과 괴리가 있을 수 있다(프록시 측정오차).
- 사서(추가): ARDL/SUR 패스스루 추정은 내생성(예: 소매금리와 은행채·EURIBOR의 동시 결정), 누락변수(예: 은행별 자본·유동성정책) 가능성을 완전히 제거하지 못한다.
- 사서(추가): 분석대상 국가는 4개 주요국에 한정되어 있어 유로존 전체(소수국·비주요국)에 대한 일반화에 제약이 있다.
- 사서(추가): 반사실 시뮬레이션은 발표효과의 선형·가법적 누적을 전제로 하며 구조적 상호작용·비선형성(예: 한계수익률·역전이자율 등)은 반영하지 않는다.
- 사서(추가): 2020년 이후 코로나 대응 성격의 UMP/정책(논문 작성 시점 이후)은 본 연구 범위에서 제외된다.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_850-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[통화정책]]
- [[글로벌 유동성]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work850.pdf](https://www.bis.org/publ/work850.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work850.htm](https://www.bis.org/publ/work850.htm)


## References

[1]: https://www.bis.org/publ/work850.pdf "BIS Working Paper 850: The impact of unconventional monetary policies on retail lending and deposit rates in the euro area"
