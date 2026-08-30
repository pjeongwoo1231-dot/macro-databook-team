---
title: 1997 Credit Cycles (Kiyotaki & Moore)
type: paper
aliases:
  - "Kiyotaki & Moore (1997) — Credit Cycles"
  - "Kiyotaki & Moore (1997)"
  - "KM 1997"
created: 2026-08-13
status: working
verification: partial
author: Claude
source: "NBER WP 5083 (1995, 63p). 최종본 Journal of Political Economy 105(2): 211–248 (1997). ⚠ WP 대조본 — **OCR 복원**(스캔본, Tesseract 5.4 250dpi)"
reliability: working-paper
tags: [type/paper, domain/credit, domain/asset, region/global, method/이론모형]
concepts: [담보제약, 신용순환, 자산가격 되먹임, 증폭, 지속성, 파급]
related: ["[[신용사이클]]", "[[주택가격]]", "[[경기침체]]", "[[신용스프레드]]", "[[1989 Agency Costs, Net Worth, and Business Fluctuations (Bernanke & Gertler)]]"]
---

> ⚠ **OCR 복원 노트.** 원 PDF가 스캔본이라 일반 추출 불가. Tesseract 5.4 · 250dpi 복원.
> 본문 서술은 양호하나 **수식·숫자는 인용하지 않는다.**

# Credit Cycles

> 📎 **Library 중복**: [[L422 Credit Cycles]]에 같은 논문의 2차 요약(Manus AI 생성)이 있다.
> **이 노트가 정본이며, 수치는 여기서만 가져온다.**

## 1. 한 줄 명제

> **내구자산은 생산요소이면서 동시에 담보다.** 신용한도가 자산가격에 영향받고,
> 자산가격이 다시 신용한도에 영향받는 **되먹임** 때문에,
> **작고 일시적인 충격이 크고 지속적인 변동을 만든다.**

## 2~3. 연구 질문 · 문헌 공백

전제: **대출자는 담보 없이는 상환을 강제할 수 없다.**
그러면 토지·건물·기계 같은 내구자산이 **이중 역할**을 한다 —
① 생산요소 ② 대출 담보. 이 이중성이 거시 동학을 바꾼다.

## 4. 핵심 메커니즘

```
작은 일시적 충격 (기술 or 소득분배)
        ↓
차입자의 순자산 ↓
        ↓
담보자산 매각 → **자산가격 ↓**
        ↓
   담보가치 ↓ → **신용한도 ↓**  ─┐
        ↓                        │  되먹임
   투자·생산 ↓ → 순자산 추가 ↓  ─┘
        ↓
   **증폭(amplify) · 지속(persist) · 파급(spill over to other sectors)**
```

저자 문장: *"Borrowers' credit limits are affected by the prices of the collateralized assets.
And at the same time, **these prices are affected by the size of the credit limits.**"* ·
*"**small, temporary shocks** to technology or income distribution can generate
**large, persistent fluctuations** in output and asset prices."*

## 5. 충격 분류
**주 충격 = 신용충격(증폭기).** 원 충격은 기술·분배지만, **크기를 만드는 것은 담보 되먹임**이다.

## 6. 전달경로

```
충격 → 차입자 순자산 ↓ → 담보자산 매각 → [[주택가격]]·자산가격 ↓
   → 신용한도 ↓ → 투자 ↓ → [[경기침체]] 심화 → (되먹임) → 타 부문 파급
```

## 7~9. 주요 결과

**① 담보-가격 되먹임이 강력한 전달 메커니즘이다** — 증폭·지속·파급 세 가지를 동시에 만든다
**② 충격 크기와 반응 크기가 비례하지 않는다** — 작은 충격 → 큰 변동
**③ 부문 간 파급** — 담보를 공유하는 부문으로 충격이 번진다

## 10. 레짐 의존성
**담보제약이 구속(binding)될 때만 작동**한다. 순자산이 풍부하면 제약이 안 걸리고 메커니즘도 잠든다.
→ **비선형**이다. 평상시엔 조용하다가 임계를 넘으면 급격해진다.

## 11. 자산가격 함의
- **[논문 주장]** 자산가격과 신용은 **양방향**으로 서로를 움직인다
- **[우리의 추론]** 자산가격을 **결과**로만 보는 분석은 이 되먹임을 놓친다.
  [[주택가격]]은 거시의 결과이자 **원인**이다
- **[우리의 추론]** 볼트의 [[가계부채와 주택가격은 독립된 두 신호가 아니다 — 하나가 다른 하나를 흡수한다]]가
  **왜 그런지**를 이 모형이 설명한다 — 둘은 되먹임 고리의 양 끝이라 통계적으로 분리되지 않는다

## 12. 반증 조건
- **확증**: 담보제약이 구속되는 국면에서 충격 전파가 비선형적으로 커짐
- **반증**: 순자산 수준과 무관하게 전파 크기가 일정
- **감시**: 담보가치 · LTV · 신용한도 · [[주택가격]]

## 13~14. 연결
**병렬**: [[1989 Agency Costs, Net Worth, and Business Fluctuations (Bernanke & Gertler)]] —
BG는 **대리인비용**(정보 마찰) 경로, KM은 **담보제약**(계약 집행 불가) 경로.
**둘 다 차입자 순자산이 상태변수**라는 점에서 같은 계열이나 마찰의 종류가 다르다
**대비**: [[2014 Procyclical Leverage and Value-at-Risk (Adrian & Shin)]] —
KM은 **차입자** 담보, Adrian-Shin은 **대출자** 위험한도. **가속기의 양쪽 끝**
**실증 대응**: [[2013 When Credit Bites Back (Jorda, Schularick & Taylor)]] —
"신용집약적 확장 뒤 침체가 깊다"는 이 모형이 예측하는 바와 정합
**인용처**: GZ(2012)가 EBP를 금융가속기의 가격 측 대리변수로 제시하며 이 논문을 인용한다

## 15. 원문 대조에서 발견한 것
- **네 층 정합.** 초록의 "이중 역할 → 되먹임 → 증폭·지속·파급"이 본문 구조와 일치
- **강점: 결론의 크기를 명시**했다 — "small, temporary" → "large, persistent"라는 **비례 파괴**가 핵심 주장이고
  초록에서 그대로 밝힌다
- ⚠ **OCR 복원본**(수식·숫자 인용 금지) · WP(1995) 대조본, JPE(1997) 최종본 미확인
- ⚠ **순수 이론.** 실증 검정 없음 — 정량적 크기는 이 논문에서 인용할 수 없다
- ⚠ 모형의 자산은 **토지**(공급 고정)다. 공급 탄력적인 자산에는 되먹임이 약해진다 — 일반화 주의

## 16. 파생 제텔
- [[담보가 줄면 차입비용이 올라 불황이 깊어진다 — 금융가속기의 원전]] (BG와 공유)
- [[자산가격과 신용한도는 서로를 움직인다 — 그래서 작은 충격이 크게 증폭된다]]

## 17. 한 문장 · 확신도

> **담보는 빌리기 위한 조건이면서 동시에 빌린 돈이 만드는 결과다.**

**확신도: 중.** 이론적 기여는 확립됐으나 **실증이 없다.**
**유보**: ① OCR 복원본 ② WP 대조본 ③ **순수 이론** ④ 토지(공급 고정) 가정.
