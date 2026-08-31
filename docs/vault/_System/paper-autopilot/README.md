# paper-autopilot

기관 리포트를 수집해 **골격(skeleton) 노트**로 vault에 축적하는 파이프라인.
[[databook-autopilot]]이 *숫자*를 담당하고, 이쪽이 *해석 방식*을 담당한다.

## 목적 — "학습"의 정확한 의미

모델 가중치는 바뀌지 않는다. 실제로 작동하는 경로는 이것이다.

```
리포트 → 골격으로 분해 저장 → 세션 시작 시 골격 3~5개 소환
       → few-shot 예시 + 명시적 템플릿으로 주입 → 분석 문체·구조 재현
```

즉 **점진적 학습이 아니라 매 세션 명시적 주입**이다. 그래서 내용 노트와 골격을
분리해야 하고, 골격이 소환 가능한 단위로 인덱싱돼야 한다. 뭉뚱그리면 소환이 안 된다.

## 3층 구조

| 층 | 대상 | 방식 | 상태 |
|---|---|---|---|
| **L1 캘린더** | S급 정기간행물 (연 50~60건) | 발간일 + URL 조립 | `l1_fetch.py` 실가동 |
| **L2 피드** | NBER·Fed WP·Liberty Street·ECB WP·World Bank | RSS/API + **키워드 필터** | `l2_feeds.py` 실가동 |
| **L3 크롬** | IMF, 운용사 Outlook, KDI | claude-in-chrome | IMF 개통 |

### L2의 본체는 수집이 아니라 **버리는 규칙**이다

NY Fed Liberty Street 피드 하나가 100건이다. 필터 없이 붙이면 큐가 쓰레기로 찬다.
`l2_feeds.py`는 2단 필터를 쓴다.

- **PRIORITY** (1개만 걸려도 통과) — 지금 레짐 판단에 직접 쓰이는 주제
  (monetary policy, term premium, private credit, nonbank, tariff, repo …)
- **GENERAL** (**2개 이상** 필요) — 단일 일반어로는 거의 모든 경제 논문이 통과한다

실측 통과율: NY Fed 5/100 · ECB WP 9/15 · FRED Blog 1/10.
필터가 곧 이 파이프라인의 **편집 방침**이다. 넓히거나 좁히려면 그 두 리스트만 고치고,
`--show-skipped` 로 무엇이 버려졌는지 확인한다.

L1이 우선인 이유: 건수가 적고, 가장 중요하고, **가장 안 깨진다.**
Beige Book은 RSS가 아예 없고 BIS는 RSS 경로 4종이 전부 404다 — 이 소스들은
피드 폴링으로는 애초에 못 잡는다. 반면 URL은 `r_qt{YYMM}`, `beigebook{YYYYMM}`으로
정확히 떨어진다(실측 확인).

## 파이프라인

```
[1] 수집   자동  — calendar.yaml → probe → Attachments/
[2] 인덱스 자동  — 03_MOC/리포트 수집 큐.md 갱신 (= 다음 세션의 작업 지시서)
[3] 해석   반자동 — 세션에서 T_ReportSkeleton.md 로 분해 → 02_Reports/
[4] 등록   수동  — 03_MOC/리포트 골격 MOC.md 배치 등록 + state.json noted:true
```

**3단계는 자동화되지 않는다.** Red Team, 인과 사슬, 트레이드오프 추출은 LLM 추론이라
셸 스크립트 단독으로 못 쓴다. 대신 1·2가 자동이면 세션에서는
"큐에서 N건 처리해" 한 줄로 끝난다.

### 소환은 graphify가 아니라 옵시디언으로

graphify는 토큰 소모가 커서 쓰지 않는다. 대신 **MOC 노트 + 백링크**가 인덱스다.

- `03_MOC/리포트 수집 큐.md` — 스크립트가 갱신. 미처리 항목 체크박스
- `03_MOC/리포트 골격 MOC.md` — 사람이 갱신. 배치 + 교차 논점
- SessionStart 훅은 그래프 상태 대신 **큐 미처리 건수 / 사후채점 대기 건수**만 알린다

골격을 few-shot으로 쓸 때는 MOC에서 3~5개를 직접 골라 읽으면 된다.
그래프 질의보다 싸고, 무엇이 주입됐는지 눈에 보인다.

## 스키마 — report_class 분기

파일럿에서 확인: **단일 스키마는 절반이 빈칸이 된다.**

- `forecast` → 사후 채점 중심 (WEO, OECD EO, GEP, MPR)
- `structural` → 트레이드오프 중심 (BIS QR, Fed WP)
- `diagnostic` → 지표 연결 + 인과 사슬 (GFSR, FSR, Beige Book)
- `commentary` → 출발 질문 + 반대 시나리오 (Liberty Street, Oaktree)

## 사후 채점 — 이 시스템의 최종 산출물

리포트는 논문과 달리 **날짜 박힌 예측**을 한다. 채점 이력이 쌓이면
기관별 신뢰도가 감이 아니라 **데이터**로 나온다. 규칙:

- 검증 가능한 명제만 적는다. "성장세 둔화" 같은 건 채점 불가 → 적지 않는다
- `실제 결과`는 공란으로 두고 대상 시점 도래 후 채운다
- `scored: 미채점` 인 노트를 주기적으로 훑는 것이 배치 작업의 일부다

## ⚠ 저작권

원문 PDF는 **vault 로컬에만** 둔다. `github.com/pjeongwoo1231-dot/macro-databook`은
공개 저장소이므로 원문이나 장문 발췌가 올라가면 문제가 된다.
BIS 판권면 실측: *"Brief excerpts may be reproduced or translated provided the source is stated."*

골격 노트는 원문을 담지 않으므로 이 문제를 구조적으로 회피한다.

## 사용법

```bash
python _System/paper-autopilot/l1_fetch.py                 # 올해 신규 확인·수집
python _System/paper-autopilot/l1_fetch.py --year 2025     # 과거 소급
python _System/paper-autopilot/l1_fetch.py --dry-run       # 존재 확인만
python _System/paper-autopilot/l1_fetch.py --only fed_beige_book
```

요청 간 1.5초 지연. `state.json` 이 중복을 막으므로 반복 실행해도 안전하다.

### 수집 중 걸러낸 실제 함정

- **BIS가 `.pdf` 요청에 HTML을 돌려주는 경우가 있다**(r_qt2603 실측). 확장자만 믿으면
  PDF인 줄 아는 HTML이 쌓인다 → 매직바이트(`%PDF-`)로 검증하고 내용에 맞는 확장자로 저장
- **Beige Book `beigebook{YYYYMM}.htm` 은 12개 지역 링크만 있는 껍데기**(본문 13K 중 대부분 네비게이션)
  → 전국 요약 `-summary.htm` 을 받는다(실측 17,877자 본문 확인). PDF는 `BeigeBook_{발표일}.pdf` 라
  날짜를 따로 알아내야 해서 쓰지 않는다
- **FOMC 의사록은 피드의 `<link>` 가 보도자료 URL**이다. 본문은 `fomcminutes{회의종료일}.htm`
  → 제목에서 회의 날짜를 뽑아 조립하되 `June 16-17` 의 **종료일 17**을 써야 한다
- **BIS Papers는 고정 개수 probe로는 놓친다**(155 기준 172까지 존재, 171 결번)
  → 연속 3회 404까지 전진

## 수집이 아니라 검증까지 — 분석 스크립트

골격에서 뽑은 **검증 가능한 명제**를 실제로 계산하는 층. `_System/Analysis/`

| 스크립트 | 검증 대상 | 결과 |
|---|---|---|
| `stock_bond_corr.py` | GFSR 증폭 경로 ⑥ (주식-채권 헤지 약화) | **적중** — 전쟁 이전 +0.273 → 이후 −0.584 |
| `kr_cpi_decomp.py` | RegimeView v1.2의 한국 가설 | **기각** — 중국발 디스인플레 흔적 없음 |

둘 다 **API 키 불필요**(FRED) 또는 기존 ECOS 키 재사용이며, 월간 재실행용이다.
리포트를 읽는 것과 그 주장을 확인하는 것은 다른 작업이고, 이 층이 없으면
[[RegimeView_2026-08]]은 의견에 머문다.

## 현재 상태 (2026-08-09)

- [x] `_System/Templates/T_ReportSkeleton.md` — report_class 분기 + 사후 채점
- [x] 골격 노트 **6건** — BIS QR / FOMC Minutes / ECB EB / Beige Book / IMF WEO / IMF GFSR
- [x] `03_MOC/리포트 골격 MOC.md` — 4차 배치, 교차 논점 19개
- [x] `calendar.yaml` — 20소스, 실측 기반
- [x] **`l1_fetch.py` 실가동** (33건) · **`l2_feeds.py` 실가동** (45건, 2단 필터)
- [x] **L3 크롬 개통** — IMF WEO·GFSR (curl 403 우회)
- [x] SessionStart 훅을 graphify → 큐 상태 알림으로 교체
- [x] **출력층** — `_System/Prompts/매크로 분석 작성 프롬프트.md` + `05_Regime/RegimeView_2026-08.md` (v1.4)
- [x] **검증층** — `stock_bond_corr.py`(적중) · `kr_cpi_decomp.py`(가설 기각)
- [x] 파생 제텔 3건
- [ ] 큐 75건 골격 분해 — **비우는 것이 목표가 아니다.** 레짐 판단에 필요한 것만 꺼내 쓴다
- [ ] World Bank **GEP**: WDS 색인이 2022년까지뿐 → 수동/크롬
- [ ] OECD Economic Outlook: 랜딩 파싱 미구현
- [ ] 한국은행 경제전망보고서 게시판 ID 재확인 (`bbs/P0002359`는 "콘텐츠 준비중" 빈 페이지)
- [ ] 한국은행 통방 **개별 문서**(결정문·의사록)는 뷰어 뒤 — 캘린더까지만 자동화됨
- [ ] KDI 봇 차단 → 크롬 경로
- [ ] 자본시장연구원·KIEP JS 렌더링 → 크롬 경로
