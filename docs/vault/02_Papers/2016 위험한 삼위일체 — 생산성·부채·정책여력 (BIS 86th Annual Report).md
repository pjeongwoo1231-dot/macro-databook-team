---
title: "86th Annual Report — 'a risky trinity': low productivity growth, high global debt, narrow policy room"
type: report
journal: BIS 86th Annual Report, 1 April 2015 – 31 March 2016. Basel, 26 June 2016
date: 2016
author: Bank for International Settlements
url: https://www.bis.org/publ/arpdf/ar2016e.pdf
local_pdf: "[[BIS-AER-2016.pdf]]"
tags: [type/report, domain/macro-financial-stability, method/institutional-diagnosis]
concepts: [위험한 삼위일체, 금융사이클, doom loop, 정책여력, 생산성 둔화, 부채]
status: done
verification: full
reliability: institutional
text_basis: local-pdf
verified: "○ 공식 PDF를 볼트에서 직접 판독(2026-08-15). 아래 인용문은 추출 텍스트 그대로. `risky trinity` 6회 · `doom loop` 7회 · `financial cycle` 96회 실측"
promoted_from: "[[BIS-AER-2016]]"
related: ["[[BIS-AER-2017]]", "[[BIS-AER-2018]]", "[[총요소생산성 (TFP)]]", "[[신용사이클]]", "[[기준금리]]", "[[RegimeView 1.0 (2026-08-09)]]", "[[2014 A Quarterly, Utilization-Adjusted Series on Total Factor Productivity (Fernald)]]"]
---

# 위험한 삼위일체 (BIS, 2016)

> BIS 86th Annual Report, 2016년 6월 26일 바젤. **PDF가 볼트 안에 있다** — [[BIS-AER-2016.pdf]]
> 기관 진단서이지 인과 추정 논문이 아니다. **수치를 인과효과로 읽지 않는다.**

## 왜 이 노트가 지금 필요한가

**DataBook에 방금 넣은 지표 셋이 이 보고서의 세 축과 정확히 같다.**
우연이 아니라, BIS가 10년 전에 "이 셋을 함께 보라"고 말한 것을 이제야 실제로 함께 보게 된 것이다.

| BIS 2016의 축 | 볼트의 지표 | 최신값 |
|---|---|---|
| productivity growth **unusually low** | [[총요소생산성 (TFP)]] (Fernald `dtfp`) | 2026 H1 **−0.08** |
| global debt levels **historically high** | [[신용사이클]] (BIS credit-to-GDP gap) | 2025-Q4 JP **+6.8** / US −11.5 |
| room for policy manoeuvre **remarkably narrow** | [[기준금리]] · [[통화정책]] | — |

## 논지 — 저자의 문장

> *"One could speak of a 'risky trinity': productivity growth that is unusually low,
> casting a shadow over future improvements in living standards; global debt levels that are
> historically high, raising financial stability risks; and a room for policy manoeuvre that is
> remarkably narrow, leaving the global economy highly exposed."*

세 조건이 **각각** 나쁜 게 아니라 **함께 있을 때** 위험하다는 게 요지다.
성장이 약하면 부채 부담이 커지고, 부채가 크면 금리를 올리기 어렵고,
정책여력이 없으면 다음 충격을 흡수할 수단이 없다. **서로가 서로의 출구를 막는다.**

보고서는 이 상태의 증상으로 **이례적으로 낮은 금리의 지속**을 든다 —
낮은 금리가 원인이자 결과인 순환이다.

> *"A key sign of these discomforting conditions is the persistence of exceptionally low
> interest rates, which have actually fallen further since last year."*

## doom loop — 재정과 금융의 상호 오염

Chapter V를 통째로 이 문제에 할애한다.

> *"…one should not underestimate the risk of a doom loop, whereby weaknesses in public and
> private sector balance sheets feed into each other."*

은행이 자국 국채를 대량 보유하면 **국가 신용 악화 → 은행 자본 훼손 → 구제 필요 →
재정 악화**의 고리가 돈다. 재정정책 설계가 금융안정의 변수가 된다는 뜻이다.

## 한계와 적용 범위

- **사서(추가)**: 기관 진단서다. **단일 인과 식별 추정치로 인용하지 않는다** —
  [[2019 Structural Interpretation of VARs with Incomplete Identification (Baumeister & Hamilton)]]가
  경고한 "식별 없는 분해 인용"을 여기서도 피해야 한다
- **사서(추가)**: BIS는 **금융사이클 관점**의 기관이다. 저금리의 비용을 강조하는 편향이 구조적으로 있다.
  같은 시기 IMF·Fed 진단과 대조해 읽어야 한다
- **사서(추가)**: 2016년 시점의 "정책여력 부족"은 **그 뒤 2020년에 반증됐다.**
  코로나 때 재정·통화가 훨씬 크게 움직였다. **"여력이 없다"는 진단은 정치적 제약의 서술이지
  기술적 상한이 아니었다.** 이 오판을 기록해 둔다

## 인과 사슬

생산성 둔화([[총요소생산성 (TFP)]]↓) → 성장으로 부채를 줄일 수 없음
→ 부채 누적([[신용사이클]]↑) → 금리 인상이 부채 부담을 통해 실물을 때림
→ 정책여력 축소([[기준금리]] 하한 근접) → **다음 충격의 흡수 수단 부재**
→ 낮은 금리 지속 → 수익률 추구 → 자산가격·부채 재누적 → **처음으로 돌아감**

**Comment**: RegimeView 실무 규칙 하나가 여기서 나온다 —
**세 축을 따로 읽지 말 것.** TFP가 마이너스인데 신용갭이 플러스인 나라(현재 일본)와
TFP가 마이너스인데 신용갭도 마이너스인 나라(현재 미국)는 **같은 생산성 부진이라도 위험도가 다르다.**
[[RegimeView 1.0 (2026-08-09)]]의 T11(BIS gap)·T12(TFP)를 **개별 트리거가 아니라 조합**으로
설계해야 한다는 근거다.

다만 위 한계 셋째를 잊지 말 것 — **BIS는 2016년에 "여력이 없다"고 했고 2020년에 틀렸다.**
정책여력 축을 트리거로 쓸 때는 **기술적 여력과 정치적 의지를 구분**해야 한다.

## 관련 개념

- 후속 진단 — [[BIS-AER-2017]](금융사이클 전환·정상화) · [[BIS-AER-2018]](좁은 정상화 경로)
- 생산성 측정 — [[2014 A Quarterly, Utilization-Adjusted Series on Total Factor Productivity (Fernald)]] ·
  [[1957 Technical Change and the Aggregate Production Function (Solow)]]
- 부채와 위기 — [[2012 Credit Booms Gone Bust (Schularick & Taylor)]] ·
  [[2013 When Credit Bites Back (Jorda, Schularick & Taylor)]]
- 지표 — [[총요소생산성 (TFP)]] · [[신용사이클]] · [[기준금리]]
- 묶음 — [[2016-2018-Comparative-Mechanism-Map]] · [[2016-2018-Core-Source-Summary]]

## References

[1]: https://www.bis.org/publ/arpdf/ar2016e.pdf "BIS (2016), 86th Annual Report, Basel, 26 June 2016 — 볼트 내 PDF 대조본 있음"

## 2026-08-18 재판독 — Ch.I에서 추가로 건진 것

**① 문장 규칙: 수치는 수사만큼 나쁘지 않다.**
BIS는 Ch.I을 이렇게 연다 — *"표준 지표로 보면 거시경제 성과는 수사가 시사하는 만큼 나쁘지 않다."*
성장 전망은 GFC 이후 **매번 하향 조정**됐지만 성장률 자체는 역사적 평균에서 멀지 않고,
**인구구조를 조정한 생산가능인구당 성장은 장기 추세를 약간 웃돈다**.
→ **성장 판단 전에 인구구조 조정을 한다.** *"경기가 나쁘다"* 를 수사가 아니라 지표로 확인한다.

**② 이 보고서의 결론 문장이 볼트 전체의 계보가 됐다.**

> *"부채가 너무 오랫동안 소득 증가의 **정치적·사회적 대체재** 노릇을 해 왔다."*
> *"**시점간 상충(intertemporal trade-offs)이 본질이다.**"*

2026-08-18에 승격한 두 문헌이 **정확히 이 문장의 형식화**다 —
[[2022 Monetary Policy and the Intertemporal Risk-Taking Tradeoff (NBER W30751)]](선진국 신용시장)과
[[2022 EME Monetary Policy under Sudden Stops (BIS WP 1032)]](신흥국 자본유출).
→ **2016 문장 → 2022 모형 → 2026 관측**의 계보로 기록한다.

**③ 당시 관측(역사로만)**: 인플레 조정 정책금리가 전후 최장 마이너스 구간,
BOJ가 ECB·릭스방크·덴마크·SNB에 합류해 마이너스 명목금리 채택,
**2016년 5월 말 약 $8조 국채가 마이너스 수익률**(당시 기록).

**④ 대립 학파를 병기한다.** Ch.I의 절 제목이 *"Secular stagnation – or financial booms gone wrong?"* 이다.
**BIS의 금융사이클 해석은 하나의 학파**이며 장기정체론과 경쟁 관계다 — 볼트는 양측을 병기한다.
