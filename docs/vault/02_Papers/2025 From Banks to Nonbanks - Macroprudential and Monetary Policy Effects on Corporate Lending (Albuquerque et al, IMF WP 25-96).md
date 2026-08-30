---
title: "From Banks to Nonbanks: Macroprudential and Monetary Policy Effects on Corporate Lending"
type: paper
series: IMF Working Paper WP/25/96
date: 2025-05
author: Bruno Albuquerque, Eugenio Cerutti, Nanyu Chen, Melih Firat (IMF)
url: https://www.imf.org/en/Publications/WP
tags: [type/paper, method/high-frequency-identification, method/panel, domain/credit]
concepts: [비은행금융, NBFI, 거시건전성정책, 신디케이트론, 규제차익, 충격흡수, 신용질]
source_file: 06_SourceArchive/05-Primary-PDFs/2024-2026/IMF-WP-2025-096.pdf
status: done
verification: full
reliability: working-paper
text_basis: local-pdf
verified: 원문 대조 완료(2026-08-14). 로컬 PDF 판독 — 표본 2000Q1–2019Q4·5,904 대출자·22개국·43→49%·4.6%/2.5% 효과크기 확인
related: ["[[2020 Macroprudential Policies and Capital Controls against Volatile Inflows (Frost, Ito & van Stralen)]]", "[[2024-2026-Comparative-Mechanism-Map]]", "[[신용사이클]]", "[[원문 아카이브 MOC]]"]
---

# 긴축하면 신용이 사라지는 게 아니라 비은행으로 옮겨간다 (Albuquerque 외, IMF 2025)

> IMF Working Paper WP/25/96, 2025년 5월. 동료심사 전 배포본이며 IMF 견해가 아니다.

## 왜 중요한가 — 우리 문제와 직결

[[2020 Macroprudential Policies and Capital Controls against Volatile Inflows (Frost, Ito & van Stralen)]]는
**FX 기반 거시건전성정책이 자본유입 규모를 줄인다**고 했다. 이 논문은 같은 도구의
**국내 신용 쪽 부작용**을 본다 — 은행을 규제하면 신용이 줄어드는 게 아니라 **비은행으로 새어나간다.**

두 논문을 붙이면 거시건전성정책의 손익계산서가 완성된다.
**대외 취약성은 줄지만 국내 신용은 감독 밖으로 이동한다.**

[[2024-2026-Comparative-Mechanism-Map]]의 "4. 금융중개 증폭 — NBFI" 슬롯에 실증을 넣는 논문이기도 하다.

## 방법과 자료

| 항목 | 내용 |
|---|---|
| 자료 | **글로벌 신디케이트론** 대출자 단위 데이터 |
| 표본 | **2000Q1–2019Q4**, 대출자 **5,904곳**(그중 **48%가 비은행**), **22개국**(선진 20 · 신흥 2) |
| 식별 | Drechsel & Miura(2025)의 **고빈도 식별 + 부호제약**으로 통화정책(MP)·거시건전성(MaPP) 충격 추출 |
| 배경 | 비은행의 글로벌 금융자산 비중 **2008년 43% → 2023년 49%**(FSB 2024). 신디케이트론 기업대출 조성에서 비은행 비중은 GFC 당시 30%대 초반 → **현재 약 50%** |

## 원문에서 확인한 결과

**1. 비은행이 충격흡수 장치로 작동한다.** 긴축 국면에서 **기존에 비은행과 거래관계가 있던
기업**이 특히 완충된다.

**2. 효과 크기.** 1 표준편차 긴축 통화정책 충격에 대해 비은행은 기업대출을
**은행 대비 4.6%**, **절대 기준 2.5%** 늘린다.

**3. 이동의 방향이 문제다.** 이 충격들은 **약한 은행**으로부터 비은행으로 신용을 밀어내며,
이는 **신용 질(credit quality)에 대한 우려**를 낳는다.

**4. 거시건전성정책도 같은 방향으로 샌다.** 은행에 대한 MaPP는 은행 — **특히 약한 은행** —
이 비은행으로 대출을 이전하게 만들 수 있다.

## 한계와 적용 범위

- **사서(추가)**: 표본이 **2019Q4에서 끝난다.** 2022~23년 급속 긴축 국면이 없다.
  하필 비은행 비중이 가장 커진 시기가 빠져 있어, 효과 크기는 **하한**일 가능성이 있다
- **사서(추가)**: **신디케이트론은 대기업 시장**이다. 중소기업 신용이나 한국의 은행 중심
  기업금융에 그대로 옮기기 어렵다. 한국은 비은행이 가계·부동산 쪽에 몰려 있어
  "어디로 새는가"의 답이 다를 수 있다
- **사서(추가)**: 고빈도 식별의 외생성 가정은 볼트의
  [[고빈도 통화 서프라이즈는 충격의 자격을 갖추지 못했다 — 자기상관되고 예측 가능하다]]가
  제기한 문제를 그대로 받는다
- **사서(추가)**: "충격흡수"와 "규제차익"은 같은 현상의 두 이름이다. 저자들은 신용질 우려를
  달지만, **완충이 좋은 것인지 위험 이전인지는 이 데이터로 판정되지 않는다**

## 인과 사슬

[[기준금리]] 인상 또는 은행 대상 거시건전성 규제
→ 은행(특히 약한 은행) 기업대출 축소
→ **비은행이 대체 공급** (은행 대비 +4.6%, 절대 +2.5%)
→ 총량 [[신용사이클]]은 덜 줄지만 **위험이 감독 밖으로 이동**
→ 신용 질 저하 → [[신용스프레드]]에 뒤늦게 반영될 위험

**Comment**: 실무 함의는 **은행 신용 총량으로 긴축 강도를 재면 과대평가**한다는 것이다.
같은 취지로 [[2026 Limited Effects of Post-Pandemic US Monetary Tightening (BOJ WP 26-E-6)]]는
**수요 구성**이 민감도를 낮췄다고 했는데, 이 논문은 **공급 주체 구성**이 같은 일을 한다고 말한다.
둘을 합치면 "2022년 이후 그렇게 올렸는데 왜 안 무너졌나"의 답 두 조각이 된다.

## 관련 개념

- 거시건전성의 대외 효과 — [[2020 Macroprudential Policies and Capital Controls against Volatile Inflows (Frost, Ito & van Stralen)]]
- 수요 구성 쪽 설명 — [[2026 Limited Effects of Post-Pandemic US Monetary Tightening (BOJ WP 26-E-6)]]
- 메커니즘 슬롯 — [[2024-2026-Comparative-Mechanism-Map]]
- 지표 — [[신용사이클]] · [[신용스프레드]] · [[기준금리]]

## References

[1]: https://www.imf.org/-/media/Files/Publications/WP/2025/English/wpiea2025096-print-pdf.ashx "IMF WP/25/96, From Banks to Nonbanks"
