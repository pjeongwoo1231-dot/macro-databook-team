---
title: "BIS WP 837 — Bad bank resolutions and bank lending"
type: paper
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: 837
published: "January 2020"
authors: "Michael Brei , Leonardo Gambacorta , Marcella Lucchetta and Bruno Maria Parigi"
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
  - "bad-banks"
  - "non-performing-loans-(npls)"
  - "bank-lending"
  - "recapitalisation"
  - "asset-segregation"
  - "bank-resolution-design"
  - "legal-environment"
status: working
verification: partial
reliability: working-paper
verified: "△ 공식 PDF(해시 검증) 추출 전문을 gpt-5-mini가 구조화. 2026-08-14 5편 감사에서 구체 주장 8/8 일치 — 서술 인용 가능, 수치·표는 원문 확인"
related: ["[[원문 아카이브 MOC]]"]
text_basis: llm-fulltext
vault_tier: B
---

# BIS WP 837 — Bad bank resolutions and bank lending

> [!info] 자동 구조화 노트 — 서술은 쓰되 수치는 원문에서 확인
> 요약·결과·한계 항목은 **공식 PDF(파일서명·페이지수·SHA-256 검증) 추출 전문**을
> `gpt-5-mini`가 구조화한 것이다. 사람이 대조하지는 않았다.
> 2026-08-14 표본 감사(5편, 검증 가능한 구체 주장 8건)에서 **오류 0건**이 나왔으므로
> 격리 대상은 아니다. 다만 표본 5편의 결과이므로 **수식·표의 숫자를 인용할 때는**
> 하단 공식 PDF를 직접 확인할 것. 감사 기록: [[원문대조 감사 2026-08-14]]

## 핵심 요약

이 논문은 2000–2016 유럽·스위스 주요 은행 패널을 이용해 bad bank(자산분리)와 공적 재자본화의 은행대출 및 NPL 영향(원인-효과)을 분석했다. 주요 결론은 자산분리 또는 공적 재자본화 단독으로는 대출 회복을 이루기 어렵고(공적 재자본화는 주로 NPL 정리에 사용됨), 두 조치를 결합할 때에만 대출 회복과 향후 NPL 축소가 관찰된다는 점이다. 민간자금 주도의 BB, 이전 자산비중이 작은 경우, 법집행이 효율적인 국가에서 효과가 더 크다. 다만 BB 지표의 내생성, GMM의 소표본·도구문제, NPL 측정 이질성, BB-only 사례의 소수성 등으로 인과추정의 완전한 확정에는 제약이 있으며 결과는 유럽·스위스 맥락에 대한 해석으로 제한된다.

| 항목 | 내용 |
|---|---|
| 연구 질문 | 자산분리(이른바 bad bank)와(또는) 공적 재자본화가 원은행(originating/good bank)의 대출 회복과 향후 부실대출(NPL) 축소에 미치는 영향은 무엇이며, 자산분리 설계의 어떤 특징들이 효과를 좌우하는가? |
| 방법 | 유럽·스위스 은행의 연단위 은행레벨 패널(2000–2016)을 구축(135개 은행, 15개국, 38개 자산분리 사건 포함). 종속변수는 대출증가율과 NPL 비율의 로지트 변환. 동적 패널(System GMM) 추정이 주 분석기법이며, 보완적으로 은행 고정효과 OLS와 자산분리 지표에 대한 IV(자산분리 발생 확률을 로짓으로 예측한 값)를 사용해 내생성 문제에 대응. 은행특성(규모·유동성·자기자본 등)과 거시통제(실질GDP성장·정책금리·중앙은행자산증가 등)를 포함. |
| 자료·범위 | 대상: 2000–2016 기간의 135개 주요 은행(15개국: EU 일부 및 스위스). 관찰된 자산분리 사건 38건(대다수는 공적 재자본화 병행), 총 이전된 자산 약 EUR 444.2bn, 총 공적 재자본화액 약 EUR 297.2bn. 자산분리는 공적/사적 자금 비중, 이전된 자산비중, BB 목적(처분 vs 재구조화), 국가 법·집행 효율성 등으로 이질성 구분. |
| 주제 | bad banks, non-performing loans (NPLs), bank lending, recapitalisation, asset segregation, bank resolution design, legal environment |
| 문헌 위상 | BIS Working Paper; 원문 표지상 저자 견해이며 동료심사 논문이 아님 |

## 원문에서 확인한 결과

- 저자 주장: 자산분리(BB)만 단독으로 시행될 경우 원은행의 대출 성장과 향후 NPL 감소에 유의미한 효과가 관찰되지 않음.
- 저자 주장: 공적 재자본화만 단독으로 시행될 경우 은행은 우선 대차대조표 정리에 자본을 사용하여 NPL이 감소하지만(인식·정리 효과) 대출 회복은 나타나지 않음.
- 저자 주장: 자산분리와 공적 재자본화가 결합될 때에만(동시에 또는 선행·동시) 대출 회복과 향후 NPL 축소라는 ‘원하는’ 효과가 통계적으로 유의하게 관찰됨.
- 저자 주장: 자산분리 사건의 이질성을 이용한 분석에서, 자산매입 자금이 대부분 민간으로 충당된 경우(majority private) 원은행의 대출 회복 및 NPL 축소 효과가 더 크도록 나타남.
- 저자 주장: 원은행이 BB로 이전한 자산의 비중이 상대적으로 작을수록(샘플 하위분위에 해당) 대출 회복과 향후 NPL 감소가 더 강하게 관찰됨.
- 저자 주장: 국가의 법적·집행 체계가 효율적(채권 실현·집행이 빠른 경우)일수록 자산분리 이후 대출 회복과 NPL 축소가 더 뚜렷하게 나타남.
- 저자 관찰: BB 생성 연도에는 NPL이 일시적으로 증가(대출 재평가·인식 강화 또는 조치시점의 NPL 급증 반영)한 뒤 다음 연도에 유의한 감소로 전환되는 패턴이 관찰됨.
- 저자 비지지 결과: BB가 자산처분(disposition) 목적인지 재구조화(restructuring) 목적인지의 구분에서는 대체로 유의한 차이를 찾지 못했음.

## 메커니즘과 연결고리

- 저자 제시 메커니즘: 자산분리는 원은행의 대차대조표에서 불확실성과 위험을 제거(혹은 축소)해 자본비율·신용등급·시장·예금자 신뢰를 개선하고 대출 공급 제약을 완화할 수 있음.
- 저자 제시 메커니즘: 자산분리로 손실실현(haircut)이 발생하면 재자본화가 병행되지 않으면 은행의 자본부족이 남아 대출 확대 여력이 제한됨(따라서 재자본화 필요).
- 저자 제시 메커니즘: 민간자금 중심 BB는 더 큰 시장 규율(높은 haircut·손실조기인식)을 유도해 좀비대출 연장의 억제와 자원 재배치에 더 유리할 수 있음.
- 저자 제시 메커니즘: 법·집행 효율성이 높을수록 채권 회수·자산처분이 예측가능하고 신속해져 자산분리의 효과가 증대됨.
- 저자 제시 메커니즘: 이전한 자산의 범위가 크면 처리의 복잡성·정책비용·공적자금 필요성이 증가하고, 반대로 소규모 이전은 문제의 경미함을 의미해 회복이 빠를 수 있음.

## 한계와 적용 범위

- 저자 지적: 자산분리(BB) 지정 변수는 내생적일 수 있음(예: NPL 증가가 BB 창설을 유발). 이를 완화하기 위해 BB 지표를 로짓으로 예측한 확률을 이용한 IV 검정을 실시했으나 완전한 무내생성 보장은 어려움.
- 저자 지적: 동적 System GMM은 표본의 관측기간이 짧고(패널 특성) 계측수(instrument) 과다 문제에 민감하므로 도구변수 수를 절제하고 Windmeijer 보정을 적용했음. 그럼에도 소표본 바이어스 가능성이 존재함.
- 저자 지적: BB-only(재자본화 없는 자산분리) 사례가 소수여서(샘플 파워) 해당 범주 효과 추정의 신뢰성이 낮음.
- 저자 지적: NPL 정의와 회계·보고 관행은 완전히 횡단국가적으로 일치하지 않아 NPL 측정의 이질성이 결과 해석에 영향 가능.
- 추가적 유의사항(참고): 표본은 유럽 및 스위스에 한정되므로 다른 제도·시장(예: 미국·아시아)으로 외삽할 때 제도차 영향을 고려해야 함.
- 추가적 유의사항(참고): 자산분리와 재자본화가 대부분 동시 또는 근접시기에 시행되므로 순인과관계(즉 어떤 조치가 주된 효과를 낳는지)를 완전히 분리해 해석하기 어렵다.

- 원문 카탈로그(PDF 해시·페이지수): [[BIS_WP_837-catalog]]

## 소환한 노드

> 본문 어휘를 볼트 지표 노드 별칭에 기계 매칭한 결과다(빈도 2회 이상, 상위 7개).
> **인과 주장이 아니라 탐색용 연결**이며, 사슬의 방향은 원문을 읽고 직접 써야 한다.

- [[설비가동률]]
- [[통화정책]]

## 원문

공식 PDF 전문: [https://www.bis.org/publ/work837.pdf](https://www.bis.org/publ/work837.pdf)  
공식 랜딩페이지: [https://www.bis.org/publ/work837.htm](https://www.bis.org/publ/work837.htm)


## References

[1]: https://www.bis.org/publ/work837.pdf "BIS Working Paper 837: Bad bank resolutions and bank lending"
