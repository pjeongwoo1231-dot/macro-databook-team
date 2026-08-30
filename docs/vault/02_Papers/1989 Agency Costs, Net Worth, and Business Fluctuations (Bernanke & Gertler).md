---
title: 1989 Agency Costs, Net Worth, and Business Fluctuations (Bernanke & Gertler)
type: paper
aliases:
  - "Bernanke & Gertler (1989) — Agency Costs, Net Worth, and Business Fluctuations"
  - "Bernanke & Gertler (1989)"
  - "BG 1989"
created: 2026-08-13
status: working
verification: full
author: Claude
source: "NBER WP 2015 (1986.9, 52p) — **WP 제목은 'Agency Costs, **Collateral**, and Business Fluctuations'**. 최종본 American Economic Review 79(1): 14–31 (1989)에서 'Net Worth'로 개제. ⚠ WP 대조본"
reliability: working-paper
tags: [type/paper, domain/credit, domain/growth, region/us, method/이론모형]
concepts: [금융가속기, 대리인비용, 순자산, 담보, 비대칭정보, 비용상태검증]
related: ["[[신용사이클]]", "[[기업 부도]]", "[[신용스프레드]]", "[[경기침체]]", "[[주택가격]]"]
---

> ⚠ **제목 변경 주의** — NBER WP(1986)는 *"Agency Costs, **Collateral**, and Business Fluctuations"*,
> AER 게재본(1989)은 *"...**Net Worth**..."*. **같은 논문이다.**
> 볼트 규칙([[같은 연구가 두 번 출판됐다 — 표본 숫자가 6개 셀 전부 다르다]])에 따라 버전을 명시한다.

# Agency Costs, Net Worth, and Business Fluctuations

## 1. 한 줄 명제

> **불황에 담보(순자산)가 줄면 차입의 대리인비용이 올라가고, 그것이 투자수요를 눌러
> 불황을 더 깊고 길게 만든다.** — 금융가속기(financial accelerator)의 원전.

## 2~3. 연구 질문 · 문헌 공백

관측: **불황은 재무적 곤경(도산·파산)의 높은 발생률을 동반한다.**
기존 거시모형은 이를 **결과**로만 취급했다. 이 논문은 **원인이자 전파 경로**로 다룬다.

## 4. 핵심 메커니즘

```
[미시] 비대칭정보 하 투자금융 (Townsend의 비용상태검증 확장)
        ↓
차입 기업의 **순자산(담보)이 많을수록** → 대리인비용(사중손실) **낮다**
        ↓
[거시로 이식]
불황 → 담보 가치 ↓ → 차입의 대리인비용 ↑ → 투자수요 ↓ → 산출 ↓
        ↓
   담보 가치 추가 ↓ → …  **증폭·지속**
```

저자 문장: *"when the entrepreneurs who borrow to finance projects are **more solvent
(have more 'collateral'), the deadweight agency costs of investment finance are lower**"* ·
*"since reductions in collateral in bad times increase the agency costs of borrowing,
which in turn depress the demand for investment"*

## 5. 충격 분류
**주 충격 = 신용충격.** 정확히는 **증폭기** — 이 논문의 신용은 충격의 **전파자**다.
(이 점이 훗날 비판 대상이 된다 → §13)

## 6. 전달경로

```
[[경기침체]] → 기업 순자산·[[주택가격]] 등 담보가치 ↓
   → 대리인비용 ↑ → [[신용스프레드]] ↑ → 투자 ↓ → 산출 ↓ → (되먹임)
```

## 7~9. 주요 결과

**① 미시 결과**: 순자산이 클수록 대리인비용이 낮다 — Townsend(1979) 비용상태검증 모형의 확장
**② 거시 결과**: 이 관계를 동태 거시모형에 이식하면 **충격이 증폭되고 지속된다**
**③ 함의**: 재무 상태가 **거시 상태변수**가 된다. 기술·선호만으로는 경기변동을 다 설명 못 한다

## 10. 레짐 의존성
**차입자 순자산 수준이 곧 레짐 변수**다. 순자산이 두터우면 같은 충격의 증폭이 작다.
→ 확장 말기(순자산 최대)와 불황 초기(순자산 급감)에서 **같은 충격이 다른 크기**로 전파된다.

## 11. 자산가격 함의
- **[논문 주장]** 담보가치 하락이 투자수요를 통해 실물로 전이된다
- **[우리의 추론]** [[주택가격]]·[[KOSPI]] 같은 자산가격이 **담보 채널**로 실물에 닿는다 —
  부의 효과와는 다른 경로다
- **[우리의 추론]** 볼트의 [[가계부채와 주택가격은 독립된 두 신호가 아니다 — 하나가 다른 하나를 흡수한다]]가
  이 이론과 정합적이다. 둘은 **하나의 담보 축**이다

## 12. 반증 조건
- **확증**: 순자산이 낮은 주체·시기에 충격의 실물 전파가 더 큼
- **반증**: 재무 상태를 통제해도 증폭 차이가 없음
- **감시**: 기업 순자산 · 담보가치 · [[신용스프레드]]

## 13~14. 연결
**보완**: [[2012 Credit Booms Gone Bust (Schularick & Taylor)]] — ST는 이 이론에 대한 비판
(*"금융가속기 모형에서 신용은 대체로 **수동적**이다 — 전파자이지 독립적 원천이 아니다"*, Borio 2008)을
인용하며 **신용이 독립 원천일 수 있는가**를 데이터로 묻는다. **BG는 전파자 쪽 이론**이다
**병렬**: [[1997 Credit Cycles (Kiyotaki & Moore)]] — 같은 담보 아이디어를 **자산가격 되먹임**으로 밀고 간다
**대비**: [[2010 Liquidity and Leverage (Adrian & Shin)]] — BG/KM은 **차입자** 순자산,
Adrian-Shin은 **대출자(중개기관)** 순자산. **가속기의 반대편**이다
**서베이**: 볼트의 `1995 Inside the Black Box (Bernanke & Gertler)` — 같은 저자의 신용경로 서베이

## 15. 원문 대조에서 발견한 것
- **네 층 정합.** 초록의 미시→거시 구조가 본문과 일치
- **⚠ 제목이 WP와 게재본에서 다르다** (Collateral → Net Worth). 인용 시 버전 명시
- **⚠ WP 날짜가 1986년 9월**이다. AER 게재는 1989년 — **3년 격차** 동안 개정됐을 수 있다.
  계수·모형 세부는 **게재본 확인 필수**
- ⚠ **순수 이론이다.** 실증 검정이 없다 — 실증은 후속 문헌 소관

## 16. 파생 제텔
- [[담보가 줄면 차입비용이 올라 불황이 깊어진다 — 금융가속기의 원전]]

## 17. 한 문장 · 확신도

> **불황이 깊어지는 이유 중 하나는 불황 자체가 담보를 깎아 돈 빌리기를 더 비싸게 만들기 때문이다.**

**확신도: 중.** 이론적 기여는 확립됐으나 **이 논문 자체는 실증이 없다.**
**유보**: ① WP(1986) 대조본, AER(1989) 게재본과 3년 격차 ② 제목 변경
③ 신용을 **전파자**로만 다룬다 — 독립 원천 여부는 이 논문 밖.
