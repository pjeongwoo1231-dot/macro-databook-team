---
title: "BIS WP 855 — Does the liquidity trap exist?"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 855
published: "April 2020"
authors: "Stéphane Lhuissier , Benoit Mojon and Juan Rubio-Ramírez"
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
  - "liquidity-trap"
  - "effective-lower-bound"
  - "monetary-policy-transmission"
  - "svar"
  - "unconventional-monetary-policy"
  - "credit-spread"
  - "quantitative-easing"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 855 — Does the liquidity trap exist?

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

저자들은 월별 SVAR(부호·영 제약과 통화정책 반응계수 제약)을 이용해 미국·유로지역·일본에서 ELB 시기에도 통화완화 충격이 신용스프레드 축소·통화량 증가를 통해 생산과 물가를 자극했다고 보고한다. 다만 이 결과는 ELB 정의, 정책지표(2년물 사용), 식별제약, 분할표본 방식 등 일련의 방법론적 선택에 민감하며 표본별 불확실성과 Lucas 비판 같은 일반적 한계가 존재한다. 결론적으로 논문은 '실증적으로 관찰된 기간 동안' 전통적 의미의 힉스형 유동성함정이 보편적으로 실현되지는 않았음을 제시하지만, 그 해석은 식별·측정·표본 한계 아래 신중히 다루어야 한다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 단기금리가 유효하한선(ELB) 근처에 있을 때에도 통화정책 충격이 실질경제(생산)과 물가에 유의미한 영향을 미치는가? |
| 방법 | 월별 5변수 SVAR(산업생산·CPI·정책금리·통화(M1)·금융지표)에서 베이지안 추정. 충격 식별은 (i) 충격의 즉시 반응에 대한 부호·영(0) 제약(sign/zero restrictions)과 (ii) 통화정책의 체계적(반응)항에 대한 부호제약을 결합. 표본을 '정상기'와 'ELB기'로 분할하여 각각 별도 SVAR을 추정하고 충격반응과 분산분해를 비교. 정책지표로는 2년 명목금리 사용(ELB 동안 단기금리 정체로 인한 선택). |
| 자료·범위 | 미국(1990M01–2015M12), 유로지역(1999M01–2018M12), 일본(1980M01–2018M12) 월별 자료. 내생변수: 산업생산(지수), 소비자물가(CPI/HICP), 2년 국채수익률, M1, 금융지표(미·유로: 비금융기업 신용스프레드, 일: 닛케이지수). ELB 시기는 금리수준과 표준편차가 역사적 저점인 시점으로 정의(예: 미국 2009.01–2015.12 등). |
| 주제 | liquidity trap, effective lower bound, monetary policy transmission, SVAR, unconventional monetary policy, credit spread, quantitative easing |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 추정 결과, 미국·유로지역·일본 모두에서 통화완화 충격은 ELB 시기에도 생산과 물가를 상승시키는 것으로 나타남.
- 정상기와 비교할 때 IRF의 부호(방향성)는 대체로 변하지 않음(ELB에서도 신용스프레드 하락·통화량 상승 등 재무적 반응 유지).
- 미국의 경우 ELB 기간에 통화정책 충격이 생산·물가 변동성에서 차지하는 비중이 정상기보다 커졌음(장기에서 약 40% 수준까지 보고).
- 유로지역과 일본은 국가별로 기여도 변화가 달랐음: 유로지역과 일본에서는 ELB 기간에 통화충격 기여도가 오히려 낮아지거나 불확실성이 확대된 경우 관찰됨.
- 통화정책의 체계적 반응계수(정책금리의 동시 반응)는 ELB 기간에 물가·산출에 대한 민감도가 전반적으로 축소된 것으로 추정됨(예: ψ_p, ψ_y 감소).
- 모델이 포착한 주요 완화시점들은 QE·OMT·QQE·마이너스금리 등 대규모 비전통정책의 발표·집행 시점과 일치함.

## 메커니즘과 연결고리

- 신용채널/금융촉진(financial accelerator): 금리·자산가치 변화가 차주 대차대조표를 개선시켜 외부자금프리미엄을 축소하고 크레딧 공급을 확대.
- 자산가격(주가·채권) 채널: 중앙은행의 대규모 자산매입·포워드 가이던스가 기대·기간·위험프리미엄을 조정해 장기·중기금리를 하락시키고 자산가치를 상승.
- 유동성공급·대출지원(credit easing, liquidity provision): 비전통정책이 직접적 유동성·신용 여건을 완화하여 경기·물가를 지원.
- 기대채널(forward guidance): 향후 정책경로 약속이 현재의 장단기 금리 및 물가·산출 기대에 영향을 미침.

## 한계와 적용 범위

- 식별방법에 의존: 부호·영 제약과 통화정책 반응계수 제약이 결과에 중요하므로 다른 식별 가정 하에서는 결과가 달라질 수 있음.
- ELB 정의는 경험적 기준(금리 수준·표준편차 저점)에 따름 — 이 정의와 분할시점 선택이 결과에 영향 가능.
- 정책지표로 2년물 금리를 사용한 선택은 ELB 기간 단기금리 정체 문제를 완화하지만 '그림자금리(shadow rate)'를 사용하지 않아 비전통정책의 완전한 동등환산을 수행하지 않음(저자도 shadow rate 불확실성 지적).
- 샘플 길이·시기 제약: 미국은 ELB 샘플이 2009–2015로 종료(이후 금리인상으로 ELB 해제), 유로지역 ELB 표본은 상대적으로 짧아 불확실성 큼.
- 모델은 각 시기에 대해 별도 SVAR을 추정(시간가변모형 미사용) — 연속적 구조변화·적응적 기대 형성 등은 포착하기 어렵다.
- 통화량(M1), 신용스프레드 및 주가 등의 측정 선택이 결과에 영향을 줄 수 있음(변수선택에 따른 민감도 존재).
- 충격 크기(2년물 즉시 10bp 하락으로 규모 표준화)가 작아 비선형·대규모 완화효과를 직접적으로 보여주지는 않음.
- 결과는 SVAR 구조와 데이터에 기반한 경험적 추정이며 '엘리어스적' 결론(ELB 무의미화)을 일반화하기엔 한계가 있음(저자도 Lucas 비판 등 언급).

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_855-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[통화정책]]
- [[신용스프레드]]
- [[CPI (소비자물가지수)]]
- [[M2 · Divisia 통화량]]
- [[글로벌 유동성]]
- [[기준금리]]
- [[산업생산]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work855.pdf](https://www.bis.org/publ/work855.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work855.htm](https://www.bis.org/publ/work855.htm)


## References

[1]: https://www.bis.org/publ/work855.pdf "BIS Working Paper 855: Does the liquidity trap exist?"
