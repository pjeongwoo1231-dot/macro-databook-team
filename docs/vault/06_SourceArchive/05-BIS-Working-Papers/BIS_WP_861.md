---
title: "BIS WP 861 — Dealers' insurance, market structure, and liquidity"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 861
published: "May 2020"
authors: "Francesca Carapella and Cyril Monnet"
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
  - "liquidity"
  - "dealers-/-market-makers"
  - "central-counterparties-(ccp)"
  - "counterparty-risk"
  - "market-structure-/-entry-exit"
  - "bid-ask-spreads"
  - "search-models"
  - "innovation-/-investment-incentives"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 861 — Dealers' insurance, market structure, and liquidity

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

본 논문은 검색균형 모형을 통해 중앙청산 등 상대방위험 완화가 단순히 '안전성 증가→유효성 개선'으로만 연결되지 않음을 보인다. 상대방위험 축소는 직접적으로는 딜러의 재고비용을 낮춰 스프레드를 줄이지만, 균형상 더 많은(덜 효율적인) 딜러의 진입을 촉발해 기존 효율딜러의 이윤·혁신유인을 약화시킬 수 있다. 결과적으로 평균 호가·후생의 순효과는 시장참여자 분포·혁신비용·위험크기 등 구체적 조건에 따라 양(이득)·음(손실) 모두 가능하다. 모형은 정상시의 비체계적 위험을 전제로 하고 재판매·담보·시스템리스크 등 실무적 요소를 단순화했으므로 정책적 해석시 이 점들을 함께 고려해야 한다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 상대방(결제)위험을 낮추는 규제(예: 중앙청산)가 장외(OTC) 중개시장에서 딜러의 진입·퇴출, 경쟁구조, 호가(스프레드), 딜러의 기술투자(혁신) 유인 및 사회적 후생에 어떠한 영향을 미치는가? |
| 방법 | 동형(monopolistic competition) 이질적 딜러들이 이끌어가는 정적·정상균형 이론모형을 사용. 딜러는 거래비용(k) 분포를 가지며 진입결정·호가(매수·매도) 게시·(사전)효율성투자(ρ)를 선택. 상대방위험은 매수자 결제 실패의 이질적 충격 ε로 모델링(중앙청산은 ε 축소). 분석은 무위험(ε=0) 대비 균형해석, ε>0 경우의 해석, 혁신선택의 일반균형 효과, 수치예제로 보강, 검색옵션을 둔 확장모형으로 견고성 점검. |
| 자료·범위 | 이론·수치모형 연구로 실증데이터 분석은 포함하지 않음. 수치예제는 가정한 분포와 비용함수(예: piecewise, quadratic γ(ρ))를 사용한 시뮬레이션 수준임. 관심은 정상시(normal times)의 비(비시스템적) 위험(아이디오신크라틱) 효과에 한정됨. |
| 주제 | liquidity, dealers / market makers, central counterparties (CCP), counterparty risk, market structure / entry-exit, bid-ask spreads, search models, innovation / investment incentives, welfare analysis |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자들은 중앙청산처럼 상대방위험(모형의 ε)을 낮추면 딜러의 개별 재고(인벤토리)비용이 줄어들어 직·간접 경로로 평균 호가(스프레드)가 좁아질 수 있다고 주장한다.
- 직접효과: ε 감소는 딜러의 재고위험을 완화해 거래당 마크업을 낮추게 하고, 같은 비용조건에서 거래량을 늘려 스프레드를 축소한다.
- 진입(경쟁)효과: ε 감소는 진입한 딜러 수를 늘려(덜 효율적 딜러의 진입) 경쟁을 심화시키고 이는 스프레드를 추가로 낮추지만 기존의 효율적 딜러들의 시장점유와 이윤을 감소시킨다.
- 혁신유인 약화: 경쟁심화로 인한 기존 효율딜러의 이윤 감소는 사전투자(더 낮은 거래비용 분포를 얻는 혁신) 유인을 약화시켜 균형상 혁신률(ρ̄)이 사회적 최적(ρ*)보다 낮아질 수 있다.
- 후생(총잉여)은 모수·분포 조건에 따라 불확정적이며, 혁신저하로 인한 손실이 충분히 크면 ε 감소(즉 중앙청산)는 거래관련 후생을 감소시킬 수 있다.
- 평균 스프레드는 ε의 직접효과(상승)와 진입·혁신을 통한 간접효과(감소)가 상충해 비단조적으로 반응할 수 있으며, 분절적 도입 단계(대상 참여자별 단계적 중앙청산)에서 관찰된 실증패턴과 일관된 결과가 도출될 수 있다.
- 정책적 함의: 규제입안자는 중앙청산의 금융안정 효과(위험공유·상대방위험 축소)를 혁신유인 약화와 균형구조변화로 인한 효율손실과 비교 고려해야 한다고 저자들은 결론지음.
- 모형 확장(검색옵션 포함)에서도 정성적 결과는 유지되며, 검색옵션이 있을 때 경쟁효과·혁신효과는 더 강화되는 경향을 보인다.

## 메커니즘과 연결고리

- 재고위험(직접) 채널: 상대방결제 실패확률 ε↑ → 딜러가 보유해야 할 안전재고 증대 → 거래당 마크업·스프레드 상승.
- 진입(경쟁) 채널: ε↓ → 진입기준(k̄) 완화 → 비효율 딜러 진입 → 경쟁심화 → 스프레드 하락·효율딜러 이윤 감소.
- 집약·광범위 마진(intensive vs extensive): 비효율 딜러 퇴출 시 남은 딜러당 거래량 증가(intensive), 반면 ε 변화는 모든 딜러의 이윤을 직접 낮춤(extensive); 균형은 두 마진의 합으로 결정.
- 혁신유인 채널: 경쟁심화로 인한 기대이윤 하락 → 사전혁신(거래비용 분포 개선)에 대한 사적유인 약화 → 평균딜러효율 저하.
- 정책수단 채널: 사회최적(플래너)은 직접위험감축과 혁신유도 사이 균형을 고려; 딜러의 사적 저투자를 보정하기 위한 보조금·규제설계 필요 가능.

## 한계와 적용 범위

- 이론모형 연구로서 실증식별·계량추정은 제공하지 않음; 정책효과의 정량적 크기는 제시된 수치예제·가정에 민감함.
- 모형의 상대방위험은 아이디오신크라틱(딜러별 비체계적) 충격 ε로만 다룸; 시스템적(상관된) 위험·위기시 거동은 배제되어 있어 CCP의 시스템리스크 완화 가치는 반영되지 않음(저자들도 명시).
- 딜러의 재고는 최종적으로 무가치(또는 처분비용이 매우 큼)로 가정되어 있어 실무의 재매도·재헤지·차입조달 메커니즘을 단순화함; 결과는 재고의 회수가능가치가 높으면 달라질 수 있음.
- 딜러·거래상대방의 전략적 디폴트, 정보 비대칭, 담보·증거금·자본제약, 상호딜러간 재매매·다자간 네팅(일부문헌과 대조)은 모형에 포함되지 않아 현실의 복합채널은 누락됨.
- 혁신(ρ) 모형화는 비용함수 γ(ρ)와 분포변화 가정에 의존함(특정 조건들(예: 식(16),(23))이 결과 판단에 중요하므로 가정민감성 존재).
- 균형·후생 계산은 정적·단기적 잉여 합산 방식에 의존; 장기적 역학·자본배분·금융안전망 외부효과는 누락됨.
- 수치 예제에서 사용된 분포는 사례적(설명적)이며 실제 시장의 거래비용·딜러구조와 차이가 있을 수 있음.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_861-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[원자재 재고]]
- [[통화정책]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work861.pdf](https://www.bis.org/publ/work861.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work861.htm](https://www.bis.org/publ/work861.htm)


## References

[1]: https://www.bis.org/publ/work861.pdf "BIS Working Paper 861: Dealers' insurance, market structure, and liquidity"
