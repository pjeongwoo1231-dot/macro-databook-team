---
title: 매크로 고전 논문 MOC
type: MOC
created: 2026-08-12
updated: 2026-08-12
tags: [type/MOC, domain/growth, domain/policy, domain/inflation, domain/labor]
---

# 매크로 고전 논문 MOC

거시경제학의 정전(canon) 29편. **2026-08-12에 두 경로로 들어왔다.**

- **원문 PDF 대조본 7편** — 이 세션에서 원문을 내려받아 전문 정독하고 작성
- **외부 수신본 22편** — 카카오톡으로 받은 노트를 볼트 규약(파일명·닫힌 태그·frontmatter)으로 정규화해 임포트

두 경로는 **신뢰도가 다르다.** 아래 표의 검증 열이 그 구분이며, 이 볼트의 AI Constitution에 따라
**미검증 노트의 수치는 다른 노트의 근거로 인용하지 않고 제텔로도 분해하지 않는다.**

---

## 0. 검증 상태 요약

| 상태 | 편수 | 의미 |
|---|---|---|
| ✅ **verified** | 7 | 원문 PDF 전문 정독·대조 완료. 인용 가능. PDF는 `Attachments/macro_classics/` |
| ❌ **unverified** | 22 | 원문 미확보 또는 미대조. `flag/unverified` 부착 |

**verified 7편**: Solow(1956) · Lucas(1988) · Romer(1990) · Kydland-Prescott(1982) · Long-Plosser(1983) · Prescott(1986) · Barro(1990)
⚠ Barro는 **JPE 1990 최종판이 아니라 NBER WP #2588(1988) 판본**을 읽었다 — `flag/needs-review` 부착.

---

## 1. 성장이론 — 외생에서 내생으로

이 계열은 **하나의 논쟁**으로 읽어야 한다: *장기 성장률을 정하는 것이 무엇인가.*

| 논문 | 검증 | 성장률을 정하는 것 |
|---|---|---|
| [[1956 A Contribution to the Theory of Economic Growth (Solow)]] | ✅ | **외생 기술진보 g**. 저축률은 수준만 바꾼다 |
| [[1956 Economic Growth and Capital Accumulation (Swan)]] | ❌ | 동상동몽 — 같은 해 독립 발견 |
| [[1986 Increasing Returns and Long-Run Growth (Romer)]] | ❌ | 지식 스필오버. **단 저자가 1990년에 스스로 정정** |
| [[1988 On the Mechanics of Economic Development (Lucas)]] | ✅ | 인적자본의 **증가율** ν |
| [[1990 Endogenous Technological Change (Romer)]] | ✅ | 인적자본의 **수준** H_A |
| [[1990 Government Spending in a Simple Model of Endogenous Growth (Barro)]] | ✅ | 생산적 정부지출 비중 g/y (역U자, 정점 τ=α) |
| [[1992 A Contribution to the Empirics of Economic Growth (Mankiw, Romer & Weil)]] | ❌ | (실증) 확장 솔로우로 조건부 수렴 |
| [[1982 An Evolutionary Theory of Economic Change (Nelson & Winter)]] | ❌ | 루틴의 탐색·선택 (비균형 접근) |

**이 계열에서 반드시 구분할 것 — 원문 대조로 확인된 것**

- **Lucas(1988)와 Romer(1990)는 같은 편이 아니다.** 전자는 인적자본의 *증가율*, 후자는 *수준*이 성장률을 정한다고 본다. 정책 함의가 갈린다 — 전자는 "교육에 시간을 더 써라", 후자는 "숙련인력 총량을 늘려라".
- **Romer(1986) → Romer(1990)은 계승이 아니라 정정이다.** 1990년 원문에서 저자가 직접 쓴다: 1986년 모형은 "A의 성장률을 K의 성장률과 같도록 **가정으로 강제**했다"고. 따라서 1986년 논문을 "투자 촉진이 기술진보를 낳는다"의 근거로 쓰면 안 된다.
- **Lucas의 γ=0.417은 추정치가 아니라 역산 잔차다.** 저자 본인이 "솔로우 모형과 정확히 동일한 정도로 데이터를 설명한다"고 적는다. 집계자료로는 γ=0과 구별 불가.

**연결 노드**: [[총요소생산성 (TFP)]] · [[인적자본]] · [[잠재성장률]] · [[GDP 성장률]]

---

## 2. 실물경기변동(RBC) — 솔로우 모형에 확률을 넣다

**RBC는 솔로우의 반박이 아니라 솔로우의 확률적 확장이다.** 이 점을 놓치면 1·2절을 별개 문헌으로 오해한다.

| 논문 | 검증 | 핵심 장치 |
|---|---|---|
| [[1982 Time to Build and Aggregate Fluctuations (Kydland & Prescott)]] | ✅ | 건설기간(J=4분기, 각 25%) + 비시점분리 여가 효용 |
| [[1983 Real Business Cycles (Long & Plosser)]] | ✅ | 투입산출 행렬 A만으로 공행·지속성 생성 |
| [[1986 Theory Ahead of Business Cycle Measurement (Prescott)]] | ✅ | 솔로우 잔차를 기술충격으로 직접 사용 |
| [[1988 Production Growth and Business Cycles I - The Basic Neoclassical Model (King, Plosser & Rebelo)]] | ❌ | 균형성장경로 정합 선호 + 로그선형화 |

**원문 정독으로 확정한 대조 포인트 — 4편 모두 노트 본문에 반영 완료**

- **Prescott(1986)의 정책 결론은 흔히 인용되는 것보다 훨씬 세다** — 원문: *"이 연구의 정책 함의는 값비싼 안정화 노력이 역효과일 가능성이 크다는 것이다. 경기변동은 기술변화율의 불확실성에 대한 **최적 반응**이다."*
- **Prescott은 유가 상승을 명시적으로 "음(−)의 기술충격"으로 취급한다.** 즉 RBC의 "기술충격"은 순수 기술이 아니다 → [[총요소생산성 (TFP)]] 측정 함정과 직결.
- **KP(1982)는 산출 분산을 맞춘 것이지 예측한 것이 아니다.** 원문: 세 충격 분산의 합을 "모형의 순환적 산출 분산이 미국 경제의 그것과 같아지도록" 제약했다. 모형 σ(Y)=1.80 vs 미국 1.8은 **적합도가 아니라 캘리브레이션 결과**다.
- **KP(1982)의 노동시간 변동성은 데이터의 절반이다** — 모형 1.05 vs 미국 2.0. 저자들도 인정하며 측정오차로 설명을 시도한다.
- **Long-Plosser는 충격을 iid로 두고도 공행·지속성을 만든다** — 상관된 공통충격 없이 **투입산출 구조만으로**. [[글로벌 공급망]] 논의의 이론적 원형.

**연결 노드**: [[총요소생산성 (TFP)]] · [[산업생산]] · [[설비가동률]] · [[경기침체]] · [[글로벌 공급망]]

---

## 3. 통화정책 — 준칙 대 재량

| 논문 | 검증 | 기여 |
|---|---|---|
| [[1963 Inflation - Causes and Consequences (Friedman)]] | ❌ | 화폐수량설 |
| [[1968 The Role of Monetary Policy (Friedman)]] | ❌ | 자연실업률 · 수직 필립스곡선 |
| [[1976 Econometric Policy Evaluation - A Critique (Lucas)]] | ❌ | 루카스 비판 — 축약형 계수는 정책에 불변이 아니다 |
| [[1977 Rules Rather than Discretion - The Inconsistency of Optimal Plans (Kydland & Prescott)]] | ❌ | 동태적 비일관성 |
| [[1983 Rules Discretion and Reputation in a Model of Monetary Policy (Barro & Gordon)]] | ❌ | 평판으로 준칙을 지지 |
| [[1993 Discretion versus Policy Rules in Practice (Taylor)]] | ❌ | 테일러 준칙 |
| [[1999 The Science of Monetary Policy - A New Keynesian Perspective (Clarida, Galí & Gertler)]] | ❌ | NK 3방정식 · Divine Coincidence |

**연결 노드**: [[통화정책]] · [[기준금리]] · [[핵심인플레이션]] · [[BEI (기대인플레이션)]] · [[실업률]]

---

## 4. 정책 전달경로 — 금리 채널 너머

| 논문 | 검증 | 채널 |
|---|---|---|
| [[1995 Inside the Black Box - The Credit Channel of Monetary Policy Transmission (Bernanke & Gertler)]] | ❌ | 은행대출 · 대차대조표 채널 |
| [[2005 What Explains the Stock Market's Reaction to Federal Reserve Policy (Bernanke & Kuttner)]] | ❌ | 주식 위험프리미엄 채널 |
| [[2005 Do Actions Speak Louder Than Words (Gürkaynak, Sack & Swanson)]] | ❌ | 목표요인 vs 경로요인(포워드 가이던스) |
| [[2007 Market-Based Measures of Monetary Policy Expectations (Gürkaynak, Sack & Swanson)]] | ❌ | 정책기대의 기간구조 측정 |
| [[1967 Tax Policy and Investment Behavior (User Cost of Capital) (Hall & Jorgenson)]] | ❌ | 자본의 사용자비용 |

**연결 노드**: [[신용스프레드]] · [[신용사이클]] · [[KOSPI]] · [[장단기 금리차]] · [[미국→한국 증시 전이 MOC]]

---

## 5. 노동시장 · 이질적 주체

| 논문 | 검증 | 기여 |
|---|---|---|
| [[1982 Aggregate Demand Management in Search Equilibrium (Diamond)]] | ❌ | 복수균형 · 조정실패 |
| [[1984 Equilibrium Unemployment as a Worker Discipline Device (Shapiro & Stiglitz)]] | ❌ | 효율임금 · 비자발적 실업 |
| [[1994 Job Creation and Job Destruction in the Theory of Unemployment (Mortensen & Pissarides)]] | ❌ | 매칭함수 · 베버리지 곡선 |
| [[1986 Stationary Monetary Equilibrium with a Continuum of Independently Fluctuating Consumers (Bewley)]] | ❌ | 불완전시장 정상균형 |
| [[1994 Uninsured Idiosyncratic Risk and Aggregate Saving (Aiyagari)]] | ❌ | 예비적 저축 · 부의 분포 |

**연결 노드**: [[실업률]] · [[주택가격]] · [[CSI (소비자심리지수)]]

---

## 6. 다음 작업 (우선순위 순)

1. ✅ **제텔 분해 완료 (2026-08-13).** verified 7편의 §15 원자 노트 **28개**를 `04_Zettel/`의 개별 파일로 승격했다. 미해결 링크 0, [[제텔 소환 인덱스]] §1에 11개 규칙·§2에 신설 섹션 반영, §3 확신도 집계 재산출(상 13→34).
   - 지표 노드 Backlinks 생성 확인: [[GDP 성장률]] 19개 · [[총요소생산성 (TFP)]] 18개 · [[잠재성장률]] 16개 · [[인적자본]] 11개 · [[재정정책]] 10개 제텔
2. **Barro JPE 1990 최종판 확보** — 현재 노트는 NBER WP #2588(1988) 기준이다. 식 번호·수치 예시가 다를 수 있어 `flag/needs-review` 상태다.
3. **유료 3편 확보** — Swan(1956, Wiley) · Romer(1986, JPE) · KPR(1988, Elsevier). Unpaywall 조회 결과 셋 다 OA 사본이 없다. 도서관/RISS 경로 필요. **KPR(1988)이 우선순위** — RBC 4부작 중 유일하게 미확보이고, 균형성장경로 정합 선호(KPR preferences)는 이후 모든 DSGE의 표준 사양이 됐다.
4. **미검증 22편 태그 유지** — `flag/unverified`를 임의로 떼지 않는다. 원문을 읽은 뒤에만 승격한다.
5. **아직 노트가 없는 인용 대상 8편** — 임포트본이 링크만 걸어둔 상태다: Miranda-Agrippino & Ricco(2021) · Eggertsson & Woodford(2003) · Blanchard & Galí(2007) · Christiano, Eichenbaum & Evans(2005) · Hazell 외(2022) · Woodford(1995, 2001) · Bernanke & Blanchard(2023). 링크는 향후 작성 대상 표시로 그대로 두었다.

---

## 이 컬렉션을 실무에 쓰는 법

이 29편은 뉴스에 직접 대응하지 않는다. **판단의 자(尺)로 쓴다.**

- **"이 정책이 성장률을 몇 %p 올린다"는 주장을 만나면** → Lucas(1988)의 산술을 먼저 대입한다. *산출을 5% 줄이는 비효율을 10년에 걸쳐 제거해도 연 0.5%p다.* 대부분의 성장률 주장은 사실 수준 효과다.
- **"AI 설비투자가 잠재성장률을 올린다"는 주장을 만나면** → Romer(1990)의 구분을 대입한다. 물적자본 보조는 성장 효과가 모호하고, 연구인력만이 g를 올린다. [[AI 자본지출]] 이 어디로 가는지가 갈림길이다.
- **TFP 하락을 기술 후퇴로 읽기 전에** → Prescott(1986)이 유가 상승을 음의 기술충격으로 취급했음을 기억한다. 잔차에는 순수 기술이 아닌 것이 섞인다.
- **레짐이 바뀌었다고 판단할 때** → Solow §VII(가격경직 레짐)과 §I~VI(신축 레짐)의 결론이 정반대임을 확인한다. 어느 쪽 세계인지 먼저 정한다.
- **"지표들이 같이 움직이니 공통 요인이 있다"는 추론을 만나면** → Long-Plosser(1983)를 대입한다. 충격을 완전 독립 iid로 두고도 공행이 나온다. **동조는 공통충격의 증거가 아니다.** 팩터모형으로 뽑은 "공통 요인"이 네트워크 전파의 축약일 수 있고, 자료만으로는 구분되지 않는다.
- **정책변수와 성과의 국가 간 회귀를 만나면** → Barro(1990) 초록을 대입한다. 정부가 최적화하면 g/y와 성장률의 상관이 **음(−)으로 뒤집힌다**. 정책변수가 최적화의 산물이면 회귀계수는 구조가 아니라 반응함수를 잰다 — 이 볼트가 한은 반응함수 계열에서 반복 확인한 바로 그 문제다.
- **"모형이 사실을 재현했다"는 주장을 만나면** → 두 가지를 확인한다. ① **맞춘 것인가 예측한 것인가** (KP 1982는 산출 분산을 제약으로 걸었고, Prescott 1986은 잔차 분산을 외부에서 측정해 넣었다 — 강도가 다르다). ② **그 사실을 재현하는 파라미터가 독립적으로 측정됐는가** (KP의 α₀·η는 "노동경제학 문헌에서 못 찾아" 자유 파라미터로 뒀다).

---

## 관련 MOC

- [[지표 MOC]] · [[원문검증 논문 MOC]] · [[제텔 MOC]] · [[매크로 해석 프레임]] · [[리포트 수집 큐]]
