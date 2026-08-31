---
title: "BIS WP 859 — Post-crisis international financial regulatory reforms: a primer"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 859
published: "April 2020"
authors: "Claudio Borio , Marc Farag and Nikola Tarashev"
source_kind: "working-paper"
peer_reviewed: false
primary_text_read: true  # 추출 전문 기준. 사람 대조 아님
human_verified: false
analysis_model: "gpt-5-mini"
analysis_confidence: "not-calibrated"
relevance_score: 5
created: 2026-08-14
updated: 2026-08-14
archive_status: "llm-structured-unverified"
tags:
  - flag/partial-check
  - bis
  - working-paper
  - "bank-regulation"
  - "central-counterparties-(ccps)"
  - "basel-iii"
  - "tlac"
  - "macroprudential-policy"
  - "liquidity-regulation"
  - "leverage-ratio"
  - "expected-loss-provisioning"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 859 — Post-crisis international financial regulatory reforms: a primer

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

저자들은 포스트-위기 국제기준이 은행·CCP의 총체적 충격흡수능력을 크게 향상시켰지만, 기준들 간 상호작용·정책적 타협·모형·평가 불확실성으로 인해 일부 핵심 영역(자산평가·유동성 가정·CCP-은행 연결·비은행 중개 등)에 추가 연구와 보수적 접근이 필요하다고 결론지음. 논문은 정성적·정책적 분석에 초점을 두며 정량적 검증과 광범위한 비은행 부문 통합은 향후 과제로 남김.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 위기 이후 국제적 금융규제 개혁이 은행과 CCP의 충격흡수능력(SAC)에 어떻게 기여하는가, 기준들 간 상호작용은 어떠하며 남아있는 쟁점은 무엇인가? |
| 방법 | 정성적 분석틀을 제시: 충격흡수능력(SAC)을 노출(EtL)과 손실흡수자원(LAR; iLAR·nLAR)으로 분해하고, 국제적 기준(Basel III, TLAC, PFMI, IFRS9 등)의 설계·상호작용·공백을 문헌·정책문서를 바탕으로 종합 논의함. 정량적·계량적 실증분석은 수행하지 않음. |
| 자료·범위 | 공식 국제 기준과 표준문서, 관련 학술·정책문헌을 대상으로 한 이론적·정성적 고찰에 국한. 국제적 합의 수준의 은행·파생물 중앙결제소(CCP)에 초점, 국내 전용 개혁·광범위한 비은행 중개 전부는 범위 밖(자산운용부문은 부분적 시사점만 제시). |
| 주제 | bank regulation, central counterparties (CCPs), Basel III, TLAC, macroprudential policy, liquidity regulation, leverage ratio, expected loss provisioning, asset management (illustrative) |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장: 포스트-위기 국제 개혁은 은행과 CCP의 충격흡수능력(SAC)을 전반적으로 제고했다고 평가함(자원량·자원질·적시성 개선 및 위험측정 오류에 대한 보완 포함).
- 저자 주장: 충격흡수능력은 손실흡수자원(LAR) 확대와 손실노출(EtL) 축소로 나뉘며, 규제수단들은 이 두 축을 서로 보완적·중복적으로 다룸.
- 저자 주장: 주요 개혁수단은 CET1 등 자본정의 강화, 리스크 민감성 개선 및 모델·측정오류를 보완하는 레버리지 비율·출력플로어, TLAC(시스템중요은행용 nLAR), LCR·NSFR(유동성 리스크 축소), IFRS9(예상손실 충당) 등임.
- 저자 주장: 표준들 간 상호작용이 안정성 효과를 강화하는 경우가 많은 반면, 때로는 리스크를 다른 형태로 전환하거나 시스템 내 재분배하는 긴장이 발생할 수 있음(예: 중앙청산은 거래상대 신용리스크를 낮추지만 결제·담보 관련 유동성리스크를 높일 수 있음).
- 저자 주장: 개혁이 완결적이지 않은 잔여 쟁점들이 존재함(자산평가·충당금과 자본의 관계, FX스왑·리포의 규제·회계 불일치, 국채 노출의 우대 취급, 은행영업책임계정(은행북)의 금리리스크, 소형은행군의 집단적 시스템리스크, CCP-은행 연결고리·CCP의 충격흡수자원 한계 등).
- 저자 주장: CCP의 prefunded 자원은 본질적으로 내부적(mutualised)이며, 따라서 개별 CCP의 LAR은 곧바로 시스템 LAR로 이어지지 않음; CCP는 대부분 ‘inside positions’로 리스크를 재분배함.
- 저자 주장: 규제 불확실성(버퍼의 실사용 가능성·PONV의 불명확성·유동성 가정의 실패 가능성)과 규제 복잡성이 SAC의 실효성을 약화시킬 수 있음을 지적함.
- 저자 주장: 따라서 보수적 접근(여러 중첩된 백스톱·여러 지표 사용)이 바람직하며, 규제의 일관된 이행이 우선이라고 강조함.

## 메커니즘과 연결고리

- 충격흡수능력(SAC) 분해: 손실흡수자원(LAR)과 손실노출(EtL)로 구분하고 LAR을 going-concern(iLAR)·gone-concern(nLAR)으로 재분류함.
- 자본 측면 메커니즘: 자본정의 개선(CET1 강화, AT1/Tier2 규정), 리스크 민감성 개선, 출력플로어로 모델오류 보완, 레버리지 비율로 비위험감응 보완.
- 버퍼 메커니즘: 자본보전버퍼, G-SIB 추가버퍼(교차단면적 기여 반영), 경기대응자본(CCyB)을 통해 시계열·교차단면적 외부효과 내재화.
- 유동성 메커니즘: LCR(단기 유동성), NSFR(구조적 자금조달)로 유동성 노출(EtL) 축소 및 해산·해결 시 유동성 관리 지원.
- CCP 기본 메커니즘: novation으로 상대방 신용노출 축소·투명성·다자간 넷팅 증대 → prefunded 구조(초기증거금 IM, 디폴트펀드 DF, CCP 자본(SITG) 등)로 기본 손실흡수; 그러나 내부화(inside positions)로 시스템LAR으로의 직접적 이전 제한.
- 상호작용·전이 메커니즘: 자본·유동성 규제가 상호 보완·악화(예: LCR이 양호해도 NSFR 취약 가능), CCP 마진요구는 멤버의 유동성 수요·EtL를 증대시켜 은행 리스크로 전이.
- 프로시클리시티 메커니즘: 예상손실 회계(IFRS9)·마진 재조정·자산가격 하락이 경기확장기의 약한 충당과 경기후퇴기의 과도한 손실인식으로 연결될 수 있음.

## 한계와 적용 범위

- 논문이 밝힌 범위제한: 비은행 중개와 광범한 자본시장부문, 국내 전용 개혁 대부분은 분석 범위 밖이며 이들로의 위험이동·상호작용은 정량분석 대상이 아님.
- 방법론 한계: 정성적·정책적 평가에 중점하고 있어 규제효과의 정량적·인과적 추정(비용·효과 분석)은 수행하지 않음.
- 가정의 명시적 제약: CCP 분석에서 대부분 회원을 은행으로 가정하고 내부 포지션만 고려하는 단순화가 있음(현실은 비은행 회원·다중 CCP 복잡성 존재).
- 식별·제도적 불확실성: PONV(비실현성 지점), 해산·해결 시점의 감독·시장반응이 애매해 nLAR·iLAR의 실효성·규모 추정이 모호함.
- 데이터·모형 한계: 제시된 스트레스·상호작용 논의는 표준·지침·사례·이론에 기반한 질적 분석으로 실물·계량자료에 의한 검증이 필요함.
- 시계열 관련 한계: 논문은 코로나19 발생 이전 작성됨(단, 저자들은 본문에서 그 점을 명기하며 논문의 논리가 위기 대응에도 함의가 있음을 언급).
- 정책 타협·조정의 한계: 국제 합의 과정에서의 정치적 타협(예: 주권채권 취급, 레버리지 조정 등)이 규범의 이론적 최적성과 다를 수 있음을 인정함.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_859-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[글로벌 유동성]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work859.pdf](https://www.bis.org/publ/work859.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work859.htm](https://www.bis.org/publ/work859.htm)


## References

[1]: https://www.bis.org/publ/work859.pdf "BIS Working Paper 859: Post-crisis international financial regulatory reforms: a primer"
