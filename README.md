# macro-databook

매크로 경제학회 운영방안 v4의 **4개 영역팀(1 성장·경기 / 2 물가·정책·금리 / 3 유동성·신용·심리 /
4 글로벌·지정학·무역) 핵심 커버리지 지표를 공개 API로 자동 수집**해서, Obsidian에 그대로 넣을 수
있는 **매크로 Data Book**(팀별 마크다운)·**뉴스 다이제스트**·**스냅샷 JSON**을 생성하는 애플리케이션.

- 원칙: **해석 문구 없음** — 숫자·기준일·출처 링크만 기록 (판단은 사람의 몫)
- 지표 목록·API 매핑의 단일 소스(SSOT)는 `indicators.yaml` — 지표 추가 시 코드 수정 불필요
- 문서의 지표 2티어제 반영 (1티어=해석 필수, 2티어=수치 인용)

## 실행 방법

```bash
# 요구사항: Python 3.11+ / pip install pyyaml requests feedparser / .env에 API 키
# 선택: pip install xlrd (ICI 펀드플로우 지표 — 없으면 해당 지표만 fail, 나머지는 정상)
python -m databook run            # 전체 수집 → output/에 팀별 md 4개 + 인덱스 + json
python -m databook run --dry-run  # 네트워크 없이 yaml·렌더 검증
python -m databook run --only fred  # 특정 소스만
python -m databook.news           # 뉴스만 따로 (run에 이미 포함 — 재생성할 때만)

python -m databook report --asof 2026-09-01   # ★ 발표자료 스캐폴드 (표·차트·문헌 자동)
python -m databook audit  <파일>              # ★ 게이트 19종. 미달이면 exit 1
python -m databook analog --asof 2026-09-01  # 과거 유사 국면 — 그때 무슨 일이 있었나
python -m databook weekly    # ★ 세션 준비 한 방 — 아래 5개를 한 덩어리로
                            #   ① 수집 상태 ② 기준 시점(as-of) 전체 상태
                            #   ③ 지난 한 주 변경분 ④ 장기 시계열 위치
                            #   ⑤ 새 기사 · 손댈 자리


# 조회 — 큰 산출물을 통째로 읽지 않기 위한 것 (실측 944,561 → 8,164 토큰)
python -m databook show 중국 PPI            # 지표 하나만 (20,837 → 225)
python -m databook diff                     # 어제 대비 값이 바뀐 지표만 (255,687 → 6,880)
python -m databook diff --since 2026-08-25  # 날짜 기준 (--back은 날짜가 아니라 스냅샷 개수다)
python -m databook diff --since A --until B # 구간을 양쪽 다 고정 — 매번 같은 자료가 나온다
python -m databook news --q 중국 --new      # 어제 없던 새 기사만 (668,037 → 1,059)
python -m databook todo                     # 에이전트가 채울 자리 (manual·STALE)

# 장기 시계열 (백테스트·회귀용) — FRED 계열 전체 히스토리를 CSV로 축적
python -m databook history                      # 전체, 2000-01-01~, 증분
python -m databook history --tier 1             # 1티어 지표의 계열만
python -m databook history --only DGS10,DGS2    # 특정 계열만
python -m databook history --since 1990-01-01 --full   # 전체 재수집
```

`history`는 `output/history/{SERIES_ID}.csv`(date,value)와 `_manifest.json`을 만든다.
FRED뿐 아니라 **`source: yahoo_finance` 지표의 심볼도 함께 받는다**(종가 기준) —
`^KS11` 코스피·`^KQ11` 코스닥·`HG=F` 구리·`GC=F` 금·`ES=F` S&P선물·`ZN=F` 국채선물.
파일명은 `KS11.csv`, `HG_F.csv`처럼 `^`를 떼고 `=`를 `_`로 바꾼다.
`run`이 최신 6개만 받는 것과 달리 전 구간을 받으며, 재실행 시 마지막 날짜의 400일 전부터
이어받아 **개정(revision)된 값을 덮어쓴다**. Obsidian에는 쓰지 않는다 — 분석 스크립트용 데이터다.

> ⚠ **FRED 라이선스 제약**: ICE BofA 계열(`BAMLH0A0HYM2`·`BAMLC0A0CM`)은 API가 **약 3년 롤링만** 제공한다.
> 장기 신용스프레드 분석에는 Moody's 기반 `BAA10Y`·`AAA10Y`(1986~)를 쓸 것.

```bash
# 이벤트 캘린더 + 코스피 갭/장중 수익률 분해
python -m databook events --since 2005-01-01
python -m databook events --symbol ^KQ11        # 코스닥
```

`events`는 **FRED 릴리스 일정 API**에서 미국 주요 지표(CPI·고용·GDP·PCE·PPI·소매판매·산업생산·JOLTS)의
**실제 발표일**을 받고, Yahoo에서 지수 OHLC를 받아 `output/events/`에 3개 CSV를 만든다.

- `calendar.csv` — 발표일 · 이벤트 코드 · **반응일**(발표일 다음 한국 거래일)
- `{SYMBOL}_returns.csv` — 갭 / 장중 / 종가-종가 로그수익률(%)과 `suspect` 플래그
- `event_panel.csv` — 회귀용 조인 테이블(반응일 기준 이벤트 더미 wide)

> **왜 갭과 장중을 나누는가**: 미국 지표는 한국시간 밤에 나오므로 반응은 **다음 거래일 시가**에 대부분 실린다.
> 종가-종가 하나로 뭉치면 두 효과가 상쇄되어 계수가 0으로 보인다.
> `suspect=1`(일중 변동폭 0)은 휴장 플레이스홀더/데이터 결손이므로 회귀에서 제외할 것.

```bash
# 빅테크 실적 캘린더 (MANGOS / Fab 10)
python -m databook earnings                    # 두 바스켓 전부
python -m databook earnings --basket mangos --ahead 60
```

**MANGOS** = Meta·Anthropic·Nvidia·Google·OpenAI·SpaceX
**Fab 10** (Vanda Research) = Magnificent 7 + SpaceX + OpenAI + Anthropic

`output/earnings/`에 `surprise.csv`(최근 4분기 EPS·컨센서스·서프라이즈%),
`upcoming.csv`(향후 일정), `earnings_reaction.csv`(발표일 → 다음 한국 거래일 코스피 갭/장중)를 만든다.

> ⚠ **Anthropic·OpenAI는 비상장**이라 실적발표가 없다. `SPCX`는 2026-06 상장이라 이력이 없다.
> Nasdaq API는 **최근 4분기만** 제공하므로 장기 이벤트 스터디는 이 소스로 불가능하다.
> 같은 날 여러 종목이 발표하면 코스피 반응 행이 중복된다 — **회귀에서 독립 관측치로 취급하지 말 것.**

```bash
# 업종별 등락 스냅샷 (79개 업종)
python -m databook sectors
```

`output/sectors/sectors_YYYY-MM-DD.csv` — 업종명·등락률·상승/보합/하락 종목수.
"외국인 비중 높은 업종이 지수를 주도한다"는 통념을 검증하려면 업종 데이터가 있어야 한다.

> ⚠ **업종별 외국인 지분율은 수집하지 못한다.** 네이버가 해당 컬럼을 세션 옵션으로 숨겨두고 있고
> (GET/POST 모두 실패), KRX 정보데이터시스템 비공개 API는 bld 코드가 바뀌었으며,
> 공공데이터포털 금융위 지수시세 API는 **별도 활용신청**이 필요하다(현재 키는 관세청 전용 → 403).
> 부정확한 대용치를 넣는 대신 비워뒀다.
> ⚠ 스냅샷이다. 시계열을 만들려면 매일 실행해 쌓아야 한다.

```bash
# 주식 대차잔고 (공매도 압력 대리지표)
python -m databook lending --days 60
python -m databook lending --days 20 --no-sector   # 업종 집계 생략(빠름)
```

`output/lending/`에 `market_daily.csv`(시장 전체 대차잔고 조원·신규·상환),
`by_stock_YYYYMMDD.csv`, `by_sector_YYYYMMDD.csv`를 만든다.

**API 메모** — 공개 문서에 영문 오퍼레이션명이 없어 탐색으로 찾았다.
```
https://apis.data.go.kr/1160100/GetStocLendBorrInfoService_V2/getStLendAndBorrItemRank_V2
  ?serviceKey=...&resultType=json&numOfRows=5000&basDt=YYYYMMDD
```
- `/service/` 경로가 **없다**(다른 1160100 서비스와 다르다)
- `basDt`로 하루씩만 받는다. **`beginBasDt`/`endBasDt`는 먹지 않는다**(전체 807만건이 그대로 온다)
- 키는 `.env`의 `DATA_GO_KR_LENDBORR_KEY`. **서비스별로 활용신청이 분리**돼 있어 다른 금융위 API에는 쓸 수 없다
- `isinCd`가 최신은 6자리 단축코드, 과거는 12자리 ISIN으로 **혼용**된다 — 장기 조인 시 주의

> ⚠ **대차 ≠ 공매도.** 차익거래·헤지·의결권 목적이 섞인다.
> **수준보다 변화**를, **절대액보다 시가총액 대비 비율**을 볼 것.

### 일일 배치 · 자동 실행

```bash
python -m databook daily                      # run + sectors + lending + history
python -m databook daily --skip run history   # 스냅샷만 (빠름)
python -m databook eventreg                   # 이벤트 → 코스피 반응 회귀
python -m databook surprise                   # 금리 기반 서프라이즈 → 코스피 방향
python -m databook curve                       # Nelson-Siegel 3요인 (Diebold-Li)
python -m databook topics --k 3 --since 2009 --ns   # FOMC 토픽모델링 (NS 요인)
python -m databook dyntopics --ns             # 동태적 NMF (창별→2차 NMF)
```

`sectors`·`lending`은 **그날 상태만** 주고 소급 수집이 불가능하다 —
돌리지 않은 날은 영영 빈칸이다. 그래서 일일 배치로 묶었다. 로그는 `output/daily.log`.

**Windows 작업 스케줄러 등록** (평일 18:30, KRX 마감 후):

```powershell
$py   = "<venv>\Scripts\python.exe"
$repo = "<이 리포 경로>"
Register-ScheduledTask -TaskName "macro-databook-daily" -Force `
  -Action  (New-ScheduledTaskAction -Execute $py -Argument "-m databook daily" -WorkingDirectory $repo) `
  -Trigger (New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday,Tuesday,Wednesday,Thursday,Friday -At 18:30) `
  -Settings (New-ScheduledTaskSettingsSet -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Hours 2))
```

해제: `Unregister-ScheduledTask -TaskName "macro-databook-daily" -Confirm:$false`

> ⚠ `.cmd` 래퍼를 거치지 말고 **python.exe를 직접 지정**할 것.
> 경로에 비ASCII 문자가 있으면 배치 파일 인코딩에서 깨진다(실제로 겪었다).
> ⚠ 전체 배치는 약 **14분** 걸린다(run 10분 + 나머지 4분). 실행시간 제한을 넉넉히 둘 것.

### ECOS 100대 통계지표

한국은행이 직접 선정·관리하는 101개 대표지표를 **한 번의 API 호출**로 받는다
(`source: ecos_keystat`). 개별 `stat_code`를 몰라도 되고, `CLASS_NAME` 28종으로 분류돼 있어
`class_filter`로 잘라 쓴다 — 시장금리 / 물가 / 실물·고용 / 대외 / 통화·금융 / 부동산·심리·가계.

```bash
# FOMC 성명서 코퍼스 (텍스트 분석용)
python -m databook fedtext                # 1999~ 전체, 증분
python -m databook fedtext --since 2015
```

`output/fedtext/statements/{YYYYMMDD}.txt` + `index.csv`(날짜·글자수·단어수·URL).
2026-08 기준 **225건(1999~2026)**, 단어수 중앙값 371.

> 성명서 URL 체계가 시대별로 셋이라(2011~ / 2006~2010 / ~2005, 1999~2001은 `general`)
> 후보를 순차 시도한다. 회의가 이틀이면 성명서는 둘째 날이므로 +1일도 시도한다.
> ⚠ **성명서만** 받는다. 의사록(minutes)은 3주 뒤 공개라 이벤트 시점이 어긋난다.

산출물 (Obsidian 네이티브 마크다운 — frontmatter·콜아웃·위키링크):
- `output/Macro/DataBook_YYYY-MM-DD.md` — **인덱스 노트**: 팀별 노트 위키링크 + 1티어 하이라이트 표
- `output/Macro/1_Growth/DataBook_1_YYYY-MM-DD.md` (2_Inflation·3_Liquidity·4_Global 동일) —
  팀별 전체 지표 표 + 수동 입력 슬롯 체크리스트 (담당자가 채움)
- `output/Macro/_News/NewsDigest_YYYY-MM-DD.md` — 뉴스 헤드라인 다이제스트 (팀별 분류)
- `output/snapshot_YYYY-MM-DD.json` — Recommendation Tracker용 기계가독 스냅샷

**Obsidian 공용 vault 직접 출력**: `.env`에 `OBSIDIAN_VAULT_PATH=<vault 경로>`를 설정하면
매 실행 시 vault의 `Macro/` 아래에 동일 노트 + `Macro/snapshots/`에 JSON이 함께 생성된다.
설정하지 않으면 `output/` 폴더를 통째로 vault에 복사해도 된다 (구조 동일).

## API 키 (.env)

`.env.example`을 `.env`로 복사해 채운다. **전부 무료.**

| 변수 | 발급처 | 용도 |
|---|---|---|
| `FRED_API_KEY` | fred.stlouisfed.org | 미국 지표 45종 |
| `ECOS_API_KEY` | ecos.bok.or.kr | 한국은행 지표 9종 |
| `KOSIS_API_KEY` | kosis.kr/openapi | 통계청·국토부 4종 |
| `DATA_GO_KR_KEY` | data.go.kr | 관세청 수출입 3종 |

data.go.kr는 키 발급 후 **활용신청 필요**: 품목별 수출입실적(15101609),
수출/수입 주요품목별 10일 단위 잠정치. 계정당 키 1개가 승인된 모든 API에 공용.

## 현재 상태 (2026-07-16)

**총 110개 지표 — 성공 90 / 실패 0 / 수동 슬롯 19 / scrape 미구현 1**

| 분류 | 상태 |
|---|---|
| FRED 45종 (금리·커브·M2·순유동성 구성·HY/IG·VIX·환율·고용·물가·주택 등) | ✅ live 검증 |
| ECOS 9종 (한은 기준금리·국고채 3Y/10Y·한국 M2·CPI·가계신용·연체율·수출입총괄) | ✅ live 검증 |
| 관세청 3종 (반도체 HS8542 월별, 20일 수출 총액+반도체, 20일 수입) | ✅ live 검증 |
| KOSIS 4종 (전산업·광공업생산, 소매판매, 취업자·실업률, 미분양 전국합산) | ✅ live 검증 |
| 미 재무부 (국가부채·TGA·국채 입찰 응찰률), CFTC 포지셔닝(엔·S&P·10Y) | ✅ live 검증 |
| 크립토 (시총 상위 10 시세·도미넌스·F&G·MVRV·스테이블코인·펀딩·미결제·반감기) | ✅ live 검증 |
| 파생 5종 (순유동성, 2s10s, 한미 금리차, 김치프리미엄, SOFR−IORB) | ✅ 계산 검증 |
| scrape 6종 (Fed 선물 내재금리, MOVE·SKEW, CNN F&G, 외국인 수급, BTC ETF 플로우) | ✅ live 검증 |
| 수동 슬롯 19 (FOMC 문서·ISM·컨퍼런스보드·AAII·Put/Call·부동산 PF 등) | 설계상 수동 |
| scrape 미구현 1 (신용융자·예탁금 — KOFIA freesis 별도 키 필요) | ⏳ 보류 |

## 진행 이력 (확정 과정에서 알아낸 것들)

1. **설계** — 운영방안 문서에서 A·B·C팀 커버리지 + 부록 B 체크리스트를 109개 지표로
   변환, `indicators.yaml`에 소스·티어·수집방법(`api`/`scrape`/`manual`/`derived`) 매핑.
   크립토는 BTC·ETH 하드코딩 대신 **시총 상위 10 동적 수집**(스테이블 제외)으로 설계.
2. **코어 구현** — yaml 레지스트리 → 소스별 fetcher(13개) → 파생 계산 → md/json 렌더.
   실패 격리(지표 1개 실패해도 완주), 재시도, 소스별 스로틀 포함.
3. **ECOS 코드 확정** — 전부 목록 API 실호출로 확인 (추측 금지 원칙):
   기준금리 `722Y001/0101000`, 국고채 `817Y002/010200000·010210000`,
   M2는 구계열(101Y004)이 비어 있어 **현행 `161Y006/BBHA00`으로 교체**,
   CPI `901Y009/0`, 가계신용 `151Y001/1000000`, 연체율 `901Y054/MO3AB`,
   수출입총괄 `901Y118/T002·T004` (관세청 GW 총괄 API 대신 동일 수치 ECOS 사용).
4. **관세청 확정** — 품목별 `Itemtrade/getItemtradeList` (HS 8542 반도체).
   10일 단위 잠정치는 endpoint 경로(`prlstMmUtPrviExpAcrs/getPrlstMmUtPrviExpAcrs`)와
   파라미터(`strtYymm`/`endYymm`)를 실호출 탐색으로 확정. **Exp=수출, Imp=수입**
   (안내 문서와 라벨이 반대였음). 단위 천 USD, `itemUsdAmt00`=총액, `01`=반도체
   (KDI 보도자료 수치와 교차 검증).
5. **KOSIS 확정** — 통계표 검색 API(`statisticsSearch.do`)로 4개 표 확정.
   미분양은 전국 행이 없어 시도별 "계"를 기간별 합산.

## 구조

```
indicators.yaml        # SSOT — 지표 정의·API 매핑 (수정은 여기서)
databook/
  __main__.py          # CLI (run / --only / --dry-run)
  core.py              # .env·yaml 로딩
  derived.py           # 파생 지표 계산 (이름 키워드 매칭)
  render.py            # 팀별 md + 스냅샷 json
  fetchers/
    base.py            # HTTP·재시도·스로틀·결과 규격
    fred.py            # FRED
    korea.py           # ECOS·KOSIS·관세청(data.go.kr)
    us_gov.py          # 재무부 FiscalData·TreasuryDirect·CFTC
    crypto.py          # CoinGecko·DefiLlama·alternative.me·CoinMetrics·업비트·바이낸스
SPEC.md                # 앱 스펙·수용 기준
AGENTS.md              # AI 하네스 작업 지침
```

## scrape 구현 노트 (2026-07-16 검증)

- **FedWatch 대용**: CME 직접 접근은 봇차단(403) → Fed 선물(ZQ) 월물 가격을 Yahoo에서 받아
  내재금리(100−가격)를 직접 계산. 격월 4개 월물로 인하 경로 제공
- **KRX 외국인 수급**: data.krx.co.kr 직접 조회 400 차단 → 네이버 투자자별 매매동향
  (원천 KRX, 억원) 파싱. 헤더 인덱스 매핑으로 열 순서 변경에 대비
- **CNN F&G**: Referer 헤더 필수 (없으면 418)
- **CBOE (Put/Call)**: cdn 차단(403) — SKEW는 Yahoo로 대체, P/C는 수동 슬롯

## 남은 작업

- [ ] 신용융자·예탁금 (KOFIA freesis OpenAPI — 별도 키 신청 필요)
- [ ] CPI 슈퍼코어 (BLS API 세부 항목)
- [ ] 글로벌 M2 합산 (미+유로존+일+중)
- [ ] 스케줄 실행 (주간 배치) + Obsidian vault 경로 직접 출력 옵션
- [ ] 대시보드 (스냅샷 JSON 기반, 선택)

## 볼트 노트도 여기 있다

`docs/vault/` — 연구 노트 **2,707개 + 원문 PDF 210편**.
제텔 188 · 논문 450 · 문헌 399 · 원문 아카이브 1,509 · 지표 노드 52 · MOC 33.
Obsidian Sync가 본선이고 이건 사본이지만, **원문까지 있어 이것만으로도 공부가 된다.**

먼저 읽을 것: `docs/vault/03_MOC/시황 분석 진입점.md` · `좋은 시황의 규칙.md`

⚠ PDF 때문에 저장소가 약 290MB다. 노트만 받으려면 sparse checkout —
자세한 것은 `docs/vault/README.md`.

