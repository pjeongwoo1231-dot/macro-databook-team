---
title: "A Quarterly, Utilization-Adjusted Series on Total Factor Productivity"
type: paper
series: FRBSF Working Paper 2012-19 (2014-04)
date: 2014-04
author: John Fernald (Federal Reserve Bank of San Francisco)
doi: 10.24148/wp2012-19
url: https://www.frbsf.org/wp-content/uploads/wp12-19bk.pdf
data_url: https://www.frbsf.org/wp-content/uploads/quarterly_tfp.xlsx
tags: [type/paper, method/growth-accounting, domain/productivity]
concepts: [총요소생산성, 가동률 조정, 성장회계, 솔로우 잔차, 노동생산성]
status: done
verification: full
reliability: institutional
text_basis: human-fulltext
verified: "○ 공개 PDF 직접 판독(2026-08-14). 초록·서론에서 방법·구성·데이터 배포처 확인. 데이터 xlsx도 직접 받아 파싱해 DataBook 지표로 편입"
promoted_from: "[[L6 A Quarterly, Utilization-Adjusted Series on Total Factor Productivity]]"
related: ["[[2006 Are Technology Improvements Contractionary (Basu, Fernald & Kimball)]]", "[[총요소생산성 (TFP)]]", "[[RegimeView 1.0 (2026-08-09)]]", "[[DataBook 지표 소환]]"]
---

# 노동생산성이 오른다고 기술이 좋아진 건 아니다 (Fernald, 2014)

> FRBSF Working Paper 2012-19, 2014년 4월. `doi:10.24148/wp2012-19`
> **공개 PDF 전문 판독.** 데이터도 공개다 — 이 논문이 만든 계열을
> **DataBook에 `미국 TFP (Fernald, 가동률 조정)`로 편입했다**(2026-08-14).

## 왜 중요한가 — 우리 문제와 직결

[[RegimeView 1.0 (2026-08-09)]]의 레짐 이름이 **"공급제약형 생산성 확장"** 이고,
두 번째 기둥이 *"② 생산성이 모순을 해소한다"*(확신도 **상**)이다.
그런데 **DataBook에 생산성 지표가 하나도 없었다.** 판단이 근거 데이터 없이 돌고 있었다.

이 논문이 그 공백을 메우는 동시에, **뷰가 쓰는 "생산성"이 무엇인지를 되묻게 한다.**

## 논지 — 세 가지 개선

미국 business sector에 대한 **실시간 분기 성장회계 데이터베이스**를 만든다.
단순 솔로우 잔차 대비 세 가지가 낫다.

1. **투입 측정** — 자본·노동 모두 BLS·Jorgenson·EU-KLEMS 방식의 성장회계를 적용
2. **가동률 조정** — [[2006 Are Technology Improvements Contractionary (Basu, Fernald & Kimball)]] 방법으로
   **노동 노력(effort)과 자본 가동시간(workweek of capital)** 변동을 걷어낸다
3. **부문 분해** — 상대가격·투입산출 정보로 **장비투자**와 **소비** 부문 TFP를 분리

핵심 주장은 *"아무리 정교한 raw TFP도 분기 기술변화의 척도가 되지 못한다"* 는 것이다.
경기적 가동률 변동이 섞이기 때문이다.

## 실제 데이터가 지금 말하는 것 (2026-08-14 기준)

DataBook에 편입해 받아본 최신 값이다. **연율 %.**

| 분기 | dLP(노동생산성) | dk(자본투입) | dtfp(TFP) | **dtfp_util(가동률조정 TFP)** |
|---|---:|---:|---:|---:|
| 2025:Q3 | +4.55 | +2.94 | +3.52 | +2.35 |
| 2025:Q4 | +2.33 | +2.88 | +1.02 | +0.30 |
| 2026:Q1 | +0.08 | +2.88 | +0.18 | **−2.13** |
| 2026:Q2 | +1.20 | +3.19 | −0.34 | **−2.19** |
| **2026 상반기 평균** | **+0.64** | **+3.04** | **−0.08** | **−2.16** |

**노동생산성은 양(+)인데 가동률조정 TFP는 −2.16%다.**
격차를 메우는 것이 **자본투입 +3.04%**(자본심화)와 상승 중인 가동률이다.

## 한계와 적용 범위

- **저자(명시)**: *"This draft is updated intermittently as I make improvements in methodology"* —
  방법론이 계속 갱신된다. 시점별로 계열이 달라질 수 있다
- **사서(추가)**: **BEA 개정에 따라 과거치가 소급 수정**된다. 특정 분기 값을 고정된 사실로
  인용하면 안 되고, 인용 시 **다운로드 시점**을 함께 적어야 한다
- **사서(추가)**: 가동률 조정은 **BFK 모형 기반 추정**이다. 그 가정이 틀리면 조정도 틀린다.
  raw TFP와 조정 TFP가 크게 갈릴 때는 **둘 다 보고** 해석해야 한다
- **사서(추가)**: **business sector** 기준이라 BLS **비농업** 노동생산성과 정의가 다르다.
  RegimeView가 인용하는 "Q2 생산성 +1.4%"는 BLS 계열이고, 이 표의 dLP +1.20과 가깝지만 같지 않다.
  **섞어 쓰지 말 것**

## 인과 사슬

[[AI 자본지출]] 등 투자 확대 → **자본투입(dk) +3%대** → 노동생산성(dLP) 상승
→ **그러나 기술(dtfp_util)은 개선되지 않음**
→ 단위노동비용 하락 압력은 발생하되 **자본지출이 계속되는 동안만**
→ 동시에 가동률(dutil) 상승 = **여유(slack) 축소**

**Comment**: RegimeView §②에 직접 걸린다. 뷰의 사슬
`AI 자본지출 ↑ → 생산성 ↑ → 단위노동비용 ↓ → 핵심인플레 하방`은
**자본심화 경로로 읽으면 내부적으로는 정합적**이다. 다만 두 가지가 달라진다.

1. **지속성** — 기술 개선이면 영구적 공급 개선이지만, 자본심화면 **투자가 멈추면 끝난다.**
   "공급제약형 **생산성** 확장"이라는 이름이 기술 개선을 함의한다면 데이터가 뒷받침하지 않는다
2. **여유** — 가동률이 오르고 있다는 것은 **경제가 더 뜨겁게 돌고 있다**는 뜻이다.
   "동결 장기화"와는 결이 다른 신호다

→ 상세 대조는 [[RegimeView 1.0 (2026-08-09)]] 9차 개정에 적었다.

## 관련 개념

- 가동률 조정 방법의 원전 — [[2006 Are Technology Improvements Contractionary (Basu, Fernald & Kimball)]]
- 성장회계 원전 — [[1957 Technical Change and the Aggregate Production Function (Solow)]]
- 데이터 — [[DataBook 지표 소환]] · [[총요소생산성 (TFP)]] · [[AI 자본지출]]
- 레짐 판단 — [[RegimeView 1.0 (2026-08-09)]]

## References

[1]: https://www.frbsf.org/wp-content/uploads/wp12-19bk.pdf "Fernald (2014), A Quarterly, Utilization-Adjusted Series on Total Factor Productivity, FRBSF WP 2012-19"
[2]: https://www.frbsf.org/wp-content/uploads/quarterly_tfp.xlsx "분기 TFP 데이터 (xlsx, 공개)"
