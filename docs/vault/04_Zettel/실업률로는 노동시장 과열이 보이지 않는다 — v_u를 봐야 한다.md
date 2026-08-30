---
title: 실업률로는 노동시장 과열이 보이지 않는다 — v/u를 봐야 한다
type: atomic_note
created: 2026-08-12
status: seed
source: Bernanke & Blanchard(2023), NBER WP 31417
reliability: working-paper
tags: [type/atomic-note, domain/inflation, domain/policy, region/us]
concepts: [v/u 비율, 노동시장 과열, 지표 선택, JOLTS]
related: ["[[2023 What Caused the US Pandemic-Era Inflation (Bernanke & Blanchard)]]"]
---

# 실업률로는 노동시장 과열이 보이지 않는다 — v/u를 봐야 한다

## 1분 요약

2021년에 연준과 그 비판자들이 **똑같이** 틀린 지점이 있다. 둘 다 노동시장을 봤는데
**실업률과 총고용을 봤다.** 그 지표들로는 과열이 안 보였다. 실제로 과열을 드러낸 것은
**구인/실업자 비율(v/u)** 이었다. 같은 시장을 두 지표로 보면 정반대 결론이 나온다.

## 인과 사슬

```
실제 노동시장:  구인 폭증 · 이직률 낮음 · 채용률 지속불가능하게 높음  → **과열**
        ↓
**실업률**로 보면?  FOMC 전망치 근처에 머물렀다 → 과열 신호 **거의 없음**
**총고용**으로 보면?  팬데믹 손실 회복 중 → 과열 신호 **없음**
**v/u**로 보면?  급등 → **과열 명확**
```

저자 각주2 원문: *"the unemployment rate, which remained close to FOMC projections,
showed **fewer signs of labor market tightening**."*

본문: 정책당국은 *"in focusing on unemployment rates and total employment rather than the
vacancy-to-unemployment ratio they did **underestimate labor market tightness**."*

**왜 중요한가**: 이것은 **모형의 실패가 아니라 지표 선택의 실패다.** BB는 코로나 전후로
가격·임금·기대 방정식 계수가 **매우 유사**했음을 보인다 — 관계는 안 깨졌다.
깨진 것은 **어느 변수를 관계에 넣었느냐**였다.

**실업률이 과열을 못 잡는 구조적 이유**: 실업률은 **분모(경제활동인구)에 민감**하다.
노동공급이 줄면 실업률이 개선되므로, **노동공급 축소로 생긴 과열을 실업률은 완화로 읽는다.**
v/u는 수요(구인)와 공급(실업자)의 **비율**이라 이 함정을 피한다.

→ 이 볼트가 [[RegimeView 1.0 (2026-08-09)]]에서 실업률 4.2→4.1 하락을
"분모 축소 때문이라 좋은 뉴스가 아니다"라고 판정한 것과 **정확히 같은 구조**다.
그 판정은 맞았으나 **대안 지표를 제시하지 못했다.** 대안이 v/u다.

**운용 규칙**: 노동시장 과열을 물가와 연결할 때 [[실업률]] 단독 사용 금지.
**v/u = JOLTS 구인건수 ÷ 실업자 수**를 함께 본다.
(2001년 이전 구간은 Barnichon(2010) 보간 계열이 필요하다.)

**확신도: 중상.** 저자 진술이 명확하고 모형 계수 안정성으로 뒷받침된다.
**유보**: 동료심사 전 WP. 그리고 v/u 자체도 **JOLTS 구인건수의 측정 문제**(허수 공고 등)에서
자유롭지 않다 — 이 논문은 그 점을 다루지 않는다.

## 핵심 지표 · 연결고리

- **관련 노드**: [[실업률]] · [[핵심인플레이션]] · [[산출갭]] · [[GDP 성장률]]
- **같은 계열 — 지표 하나를 바꾸면 결론이 뒤집힌다**:
  [[물가지수를 주택가격으로 바꾸면 부호가 정상화된다 — 한은이 본 것은 자산가격이었다]] ·
  [[한국 인플레이션 동학은 CPI가 아니라 PPI로 봐야 정합적이다]] ·
  [[전력사용량은 조업일수를 걷어내야 경기 신호가 된다 — 상관 0.14에서 0.33으로]]
- **데이터북 조치 필요**: `JTSJOL`(구인건수)은 1팀 tier 2에 이미 있다.
  **실업자 수를 붙여 v/u 파생지표를 만들어야 한다** (`UNEMPLOY` 또는 UNRATE×경제활동인구).
