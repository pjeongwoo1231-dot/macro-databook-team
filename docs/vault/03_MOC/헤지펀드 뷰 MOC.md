---
title: 헤지펀드 뷰 MOC
type: MOC
created: 2026-07-22
updated: 2026-07-27
status: working
author: Claude
source: Claude 생성
tags: [type/MOC]
related: ["[[지정학 코멘터리 MOC]]", "[[README]]", "[[2026-07-05_Super-Cycle-Thesis]]"]
---

# 헤지펀드 뷰 MOC — 글로벌 매크로 헷지펀드 운용가 유튜브 학습 노트

> **성격**: 매크로 판단에 직접 투입되는 입력이다. 논문·지표와 **같은 파이프라인**에 있고, 다른 것은 트랙이 아니라 **신뢰도 등급**이다.
> 여기 모인 것은 운용가·애널리스트의 **1인칭 견해(view)** — CLAUDE.md §6 신뢰도 사다리에서 Opinion 층이다. 논문(Academic)보다 낮고, 대신 **훨씬 빠르다**.
> 그래서 쓰임이 다르다: 논문은 "이 지표를 믿어도 되는가"에 답하고, 뷰는 "지금 시장이 무엇을 가격에 넣고 있는가"에 답한다. 레짐 판단에는 둘 다 필요하다.
> 모든 노트에 "검증 필요 / 반박 포인트(Red Team)" 섹션을 필수로 넣어 AI Constitution(신뢰도 평가·반례 생성)을 그대로 적용한다.

## 사용법

1. 사용자가 스크립트(.txt)를 `OneDrive/Desktop/AI먹일 지식들/`에 쌓으면, 세션마다 새 파일을 이 폴더 구조로 구조화한다.
2. 파일명 규칙: `YYYY-MM-DD_화자-주제.md`, 화자별 하위 폴더(현재: Raoul_Pal, RealVision_Guests — 새 화자 등장 시 하위 폴더 추가).
3. 각 노트 필수 섹션: 핵심 요지 / 프레임워크·개념 / 배경지식 / 트레이딩 시사점 / **검증 필요·반박 포인트** / 활용 방향.
4. 신뢰도(reliability) 필드에 이해상충·홍보성 여부를 반드시 명시 (예: Real Vision 게스트 영상은 대부분 구독 판매 목적 티저).
5. 세션 종료 시 `/graphify .` 재실행으로 그래프 갱신.

## 수록 화자

| 화자 | 소속/배경 | 이해상충 주의사항 |
|---|---|---|
| Raoul Pal | 전 Goldman/헤지펀드, Real Vision 공동창업자 | SUI Foundation 연계 공개 — 레이어1 강세론에 편향 |
| Jordi Visser | 전 Weiss Multi-Strategy CIO, GMI 운영 | AI/테크 롱 포지션, Pal과 상호 에코챔버 |
| Tarek Mansour | Kalshi CEO | 자사 인터뷰, 홍보성 |
| Malia Bengali | MB Commodities Capital | 원자재 트레이더, 지정학 해석은 본인도 편향 인정 |
| Rekt Capital | 익명 크립토 TA | "4년 주기설" 프레임 자체가 논쟁적 |
| Warren Buffett | Berkshire Hathaway 회장 | 즉흥 인터뷰 발언, 수치는 본인 기억 의존 |
| Michael Howell | CrossBorder Capital/GL Indexes 창업자 | 65개월 주기설 방법론 비공개(재현 불가) |
| 김영지 (SP 리서치) | 증권사 애널리스트 추정 | 실시간 시황 코멘트, 데이터 근거 제시 양호 |

## 노트 목록 (시간순)

1. [[2026-06-04_Agentic-Economy-Invisible-Economy|2026-06-04 — Agentic Economy]] (Raoul Pal 단독)
2. [[2026-06-12_Jordi-Visser-Compute-vs-Energy|2026-06-12 — Compute vs Energy 병목]] (Pal × Jordi Visser)
3. [[2026-07-02_Tarek-Mansour-Kalshi-Prediction-Markets|2026-07-02 — 예측시장·퍼페추얼]] (Pal × Tarek Mansour)
4. [[2026-07-05_Super-Cycle-Thesis|2026-07-05 — 슈퍼사이클 논제]] (Raoul Pal 단독) ★ 가장 밀도 높음
5. [[2026-07-12_Rekt-Capital-Bitcoin-Cycle-TA|2026-07-12 — 비트코인 4년 주기]] (Rekt Capital) — ④와 상반된 시간축, 대조 필독
6. [[2026-07-22_Malia-Bengali-Oil-Fed-Geopolitics|2026-07-22 — 유가·Fed·지정학]] (Malia Bengali)
7. [[2026-07-22_Economic-Singularity-Revisit|2026-07-22 — 경제적 특이점 재방문]] (Raoul Pal 단독)
8. [[2026-07_Buffett-CNBC-Alphabet-Warsh-AI-Capex|2026-07 — 버핏의 알파벳·워시·AI capex]] (Warren Buffett)
9. [[2026-Michael-Howell-Global-Liquidity-Cycle|2026 — 글로벌 유동성 65개월 사이클·GFC2]] (Michael Howell) — ④와 정면 대조(같은 메커니즘, 반대 결론)
10. [[2026_Nasdaq-Selloff-AI-Credit-Spread-Rolling-Rotation|2026 — 나스닥 급락·AI 신용스프레드·롤링 로테이션]] (김영진)
11. [[2026_SK-Hynix-ADR-Oil-Fed-Rate-Trading|2026 — 하이닉스 ADR·유가·GSCPI·10년물 트레이딩]] (김영진)
12. [[2026_AI-4Layer-Rolling-Recession-Deepening|2026 — AI 4층구조·롤링리세션 심화(JP모건·키미·삼성전자)]] (김영진, 3편 종합)
13. [[2026_Yen-Won-Weakness-BOJ-Fed-Tariff-301|2026 — 엔화·원화 약세·BOJ·관세301조]] (김영진, 3편 종합)
14. [[2026_Fed-Liquidity-Mechanism-Warsh-Stock-Ownership|2026 — Fed 유동성메커니즘·워시 실제노선·주식비중 논쟁]] (김영진)

> 참고: 김영진(SP 리서치)의 실명은 외부방송 출연분(딜사이트 경제TV)에서 "김영진 투자리서치 대표"로 확인됨. 다른 노트의 "김영지"는 STT 오기(誤記)로 동일인.

## 교차 읽기 추천

- **④ vs ⑤**: 같은 크립토 자산에 대해 "구조적 슈퍼사이클"(Pal) vs "전형적 4년 약세장"(Rekt Capital) — 정반대 시간축 비교.
- **④ vs ⑨**: "부채가 유동성을 강제한다"는 동일한 메커니즘에서 Pal은 "위기 없음", Howell은 "GFC2(2030년경)"이라는 정반대 결론 — Red Team 워크샵 최적 소재.
- **②·④**: "병목이 곧 더 많은 capex를 부른다"는 동일 논리가 반복 사용됨 — Pal 진영 내부의 핵심 순환논리, 검증 시 이 지점을 우선 공격할 것.
- **⑥**: 학회 4팀(지정학) DataBook과 가장 직접적으로 연결되는 회차 — 유가/OPEC/Fed 인사 관련 배경지식 소스로 우선 활용.
- **⑧ vs 13_Geopolitics_Commentary/US_Politics_Fed**: 버핏의 케빈 워시 호평과 하원 청문회에서 제기된 Fed 독립성 논란을 나란히 볼 것.

## 학회 파이프라인과의 관계

- 이 노트들은 [[README]]의 "AI 해석 → 사람 체화" 흐름 **안에** 있다. 레짐 판단·트리거 설정의 1차 입력이다.
- 인용할 때는 신뢰도만 명시한다 — "운용가 견해, 미검증". 등급 표기가 필요한 것이지 격리가 필요한 게 아니다.
- 뷰가 지표를 거론하면 해당 지표 노트([[지표 MOC]])에서 그 뷰가 역링크로 잡힌다. 논문의 "이 지표는 못 믿는다"와 뷰의 "시장은 이걸 본다"가 같은 화면에 서게 하는 것이 목적이다.
- 순수 지정학/정책 원문(청문회, 싱크탱크 웨비나, 국제정세 유튜브)은 성격이 달라 [[지정학 코멘터리 MOC]]가 따로 묶는다.
