---
title: "BIS WP 866 — Model risk at central counterparties: Is skin-in-the-game a game changer?"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 866
published: "May 2020"
authors: "Wenqian Huang and Előd Takáts"
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
  - "central-counterparties-(ccps)"
  - "model-risk"
  - "initial-margin-(im)"
  - "skin-in-the-game-(sitg)"
  - "capital-and-incentives"
  - "panel-regression"
  - "back-testing-/-margin-breaches"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 866 — Model risk at central counterparties: Is skin-in-the-game a game changer?

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

저자들의 주장: 공개 정량공시(2015 Q3–2018 Q4) 기반 패널분석에서 CCP의 skin-in-the-game(SITG) 규모가 클수록 포트폴리오 수준의 초기마진(IM) 모델 성과(마진 브리치 빈도·달성커버리지·브리치 평균·최대치)가 더 양호하게 나타난다. 반면 운영자본(기타자본)은 일관된 보수성 신호를 주지 않으며, 이윤은 소유구조·수익성에 따라 '프랜차이즈 가치' 채널 또는 '위험수익' 채널로 상반된 효과를 보인다. 범위·식별성 관련 주의사항: 표본기간이 제한적이고(극단적 스트레스 사건 부족), 마진 브리치 지표는 프록시에 불과하며 이윤 변수의 내생성 등 인과 도출에 제약이 있다. 따라서 결과는 'SITG와 더 보수적 모델링의 상관관계'를 제시하지만, 정책적 최적치나 확정적 인과관계 규명을 제공하지는 못한다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | CCP의 고유자본(특히 skin-in-the-game)·영업자본·이윤이 포트폴리오 수준의 초기마진(IM) 모델링(모델 리스크)에 어떤 영향을 미치는가? |
| 방법 | CCP 정량공시(Clarus CCPView) 기반 패널회귀 분석. 종속변수는 5개 모델리스크 프록시(분기별 증거기반: 마진 브리치 건수·달성커버리지·달성-목표 커버리지 차이, 연간: 브리치 평균·최대 크기). 핵심 설명변수는 SITG, 기타자본(영업자본), 이윤이며 IM 및 자산을 통제. 개체·시점 고정효과 적용. 이윤의 경로를 식별하기 위해 소유구조·이윤 수준에 따른 상호작용(subsample/interaction) 분석을 수행. |
| 자료·범위 | 공시기한: 2015 Q3–2018 Q4(분기패널), 표본: 39 CCP 그룹(120개 제품라인), 자료원: 공개 정량공시(Clarus FT CCPView). 마진 브리치 관련 보고는 '과거 12개월' 기준으로 제공되어 일부 변수는 연단위 처리하거나 분기 증가분으로 환산함. |
| 주제 | Central counterparties (CCPs), Model risk, Initial margin (IM), Skin-in-the-game (SITG), Capital and incentives, Panel regression, Back-testing / margin breaches |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장: 더 높은 CCP skin-in-the-game(SITG)는 포트폴리오 수준 IM 모델의 보수성 증가와 일관되게 연관되어 있음(브리치 빈도·달성커버리지·브리치 평균·최대치에서 더 나은 성과).
- 저자 주장: 기타 영업자본(운영자본)은 신용리스크 모델링의 보수성 향상과 일관된 양(positive) 관계를 보이지 않음(대체로 무관하거나 혼재된 결과).
- 저자 주장: 이윤(profit)과 모델리스크의 관계는 양면적임. 평균적으로 명확한 단일 효과가 관찰되지 않으나, 소유구조·수익성에 따라 채널이 달라짐.
- 저자 주장: 사용자(회원) 소유이면서 저수익(CCP)군에서는 이윤이 더 높은 경우 더 보수적인 모델링(프랜차이즈 가치 채널)이 관찰되는 반면, 영리법인·고수익 CCP에서는 이윤과 리스크완화가 역관계(위험추구 → 단기 이윤)로 나타나 위험영업 채널이 우세함.
- 저자 주장: 결과는 5개 프록시와 여러 사양에서 비교적 일관되며 SITG의 인센티브 역할을 지지함.

## 메커니즘과 연결고리

- SITG 인센티브 메커니즘: CCP가 자신들의 SITG 자본을 손실로 잃을 가능성이 클수록(IM 모델 실패 시) 주주·운영자들이 모델을 보수적으로 설계·보완할 유인이 커짐 (‘자본위험 내재화’).
- 기타자본(non-SITG) 불연계: 운영자본·영업자본은 신용 손실에 노출되지 않는 경우가 많아(SITG와 법적·운영상 분리), 동일한 인센티브 효과를 제공하지 않음.
- 이윤의 양면채널: (1) 프랜차이즈 가치 채널 – 지속적 이윤은 사업가치(주주손실 위험)를 증가시켜 더 보수적 행동 유인; (2) 위험수익 채널 – 높은 이윤이 리스크완화의 포기로부터 기인할 경우 이윤이 높을수록 더 무모한 모델링 유인 발생.
- 소유구조 조절: 사용자(회원) 소유 CCP는 멤버의 손실을 부분적으로 내부화해 '위험수익' 채널이 약화되고, 영리 CCP는 단기이윤 추구로 인해 위험수익 채널이 강하게 작동할 가능성.

## 한계와 적용 범위

- 저자 표명·암시된 제한: SITG 금액은 전체 IM·DF에 비해 매우 작음(샘플 평균 수십만 달러 수준), 따라서 SITG의 손실흡수능력 자체는 제한적이며 주된 발견은 '인센티브 효과'에 관한 연관성임.
- 마진 브리치 지표는 모델리스크의 프록시일 뿐이며, 분기 단위로 관찰되는 브리치가 곧 CCP 실패를 의미하지는 않음(대부분의 브리치는 정산으로 해결됨).
- 마진 브리치 보고는 '과거 12개월' 누적치로 제공되어 시계열 자가상관성이 존재하고, 저자들이 보정(연단위 사용·분기증분 추정)을 했으나 측정오차 가능성은 남음.
- 이윤 변수의 내생성(endogeneity)을 완전히 제거하지 못함(이윤이 리스크선택의 결과일 수 있어 인과관계 역방향 가능).
- 표본기간(2015 Q3–2018 Q4)은 대형 스트레스 사건을 포함하지 않아 극단적 충격하의 행동(예: 위기시 리스크관리 변화)을 관찰하기 어려움.
- 회귀 설명력(R-squared)이 전반적으로 낮음과 일부 규격에서 표본수가 작아(특히 연간 규모 지표) 통계적 검정력 제약이 존재함.
- 소유구조·거버넌스·규제상 차이 등 잠재적 누락변수(예: 리스크문화, 모델리스크 거버넌스)로 인한 편향 가능성.
- 본 연구는 규범적 최적 SITG 수준을 제시하지 않음(정책적 함의는 있으나 최적화·복잡한 균형 고려 불포함).
- 표본은 '거의 모든 국제적 관련 CCP'를 포함한다고 하나 지역적·소규모 CCP나 비공개 자료는 포함되지 않을 수 있음.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_866-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[통화정책]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work866.pdf](https://www.bis.org/publ/work866.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work866.htm](https://www.bis.org/publ/work866.htm)


## References

[1]: https://www.bis.org/publ/work866.pdf "BIS Working Paper 866: Model risk at central counterparties: Is skin-in-the-game a game changer?"
