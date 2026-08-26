# Macro Data Book 자동 최신화 애플리케이션 — 스펙 v1

## 목적
학회 운영방안 v4 문서의 "팀 구성 핵심 커버리지" (A·B·C팀, **D팀 제외**)에 해당하는
거시경제 지표들을 공개 API에서 자동 수집하여, 항상 최신 상태의 **매크로 Data Book**을
생성·갱신하는 애플리케이션.

- 원문 규칙 준수: Data Book은 **해석 문구 금지, 숫자·원문·출처 링크만** 기록한다.
- 각 지표는 최신값 + 직전 추이(최근 N개 관측치) + 출처 링크 + 수집 시각을 포함한다.
- 지표 2티어제 반영: 1티어(해석 필수)·2티어(수치 인용만)를 메타데이터로 구분한다.

## 범위 (v2 — 학회 4팀 재편 반영)
- **포함**: 1팀 성장·경기 / 2팀 물가·정책·금리 / 3팀 유동성·신용·심리 / 4팀 글로벌·지정학·무역
  (v1은 A·B·C 3팀에 D 제외였으나, v2에서 4팀 전면 재편 + 원자재·글로벌·뉴스 모듈 추가)
- 전체 지표 목록과 API 매핑은 `indicators.yaml`이 단일 소스(SSOT)다.

## 산출물 (앱이 만들어야 하는 것)
1. **수집 코어**: `indicators.yaml`을 읽어 소스별 fetcher(FRED, ECOS, KOSIS, FiscalData,
   TreasuryDirect, CoinGecko, DefiLlama, CFTC Socrata, 거래소 공개 API 등)로 시계열을 수집.
2. **Data Book 출력 (필수)**: 팀별 마크다운 파일 생성 — Obsidian vault에 그대로 넣을 수 있는 형식.
   - 경로 예: `output/Macro/1_Growth/DataBook_1_YYYY-MM-DD.md`
   - 각 지표: 이름 / 최신값·기준일 / 직전 3~6개 값 / 전기 대비 변화 / 출처 URL / 티어
3. **스냅샷 JSON (필수)**: `output/snapshot_YYYY-MM-DD.json` — 전체 지표의 기계가독 스냅샷
   (Recommendation Tracker의 "당시 Data Book 스냅샷 링크" 용도).
4. **파생 지표 계산 (필수)**:
   - 순유동성 = Fed B/S(WALCL) − RRP(RRPONTSYD) − TGA
   - 2s10s = DGS10 − DGS2, 한미 금리차 = Fed 상단 − 한은 기준금리
   - 김치프리미엄 = (업비트 KRW-BTC ÷ 바이낸스 BTCUSDT × USDKRW) − 1
5. **대시보드 (선택, 2차)**: 스냅샷 JSON을 읽는 간단한 웹 대시보드 (정적 HTML 또는 Streamlit).

## 아키텍처 가이드 (권장, 강제 아님)
- Python 3.11+, 의존성 최소화 (`httpx`/`requests`, `pyyaml`, `pandas` 선택).
- 구조: `fetchers/` (소스별 1모듈) · `core/` (스케줄·캐시·파생계산) · `render/` (md/json 출력).
- 실패 격리: 지표 하나가 실패해도 전체 실행이 죽지 않는다. 실패 지표는 Data Book에
  "수집 실패 (사유)"로 표기하고 exit code는 0 유지, 로그에 경고.
- 캐시: 소스별 호출 결과를 로컬 캐시(예: `cache/`)에 저장, 재실행 시 당일 캐시 재사용.
- 레이트리밋 준수: FRED 120 req/min, ECOS/KOSIS 키별 일일 한도. fetcher에 간단한 스로틀.

## 필요한 API 키 (.env)
| 변수 | 발급처 | 비고 |
|---|---|---|
| `FRED_API_KEY` | https://fred.stlouisfed.org/docs/api/api_key.html | 무료, 즉시 발급 |
| `ECOS_API_KEY` | https://ecos.bok.or.kr/api/ | 무료, 회원가입 필요 |
| `KOSIS_API_KEY` | https://kosis.kr/openapi/ | 무료 |
| `DATA_GO_KR_KEY` | https://www.data.go.kr/ | 관세청 수출입 등 공공데이터포털 |
| `BLS_API_KEY` | https://www.bls.gov/developers/api_signature_v2.html | 선택. 무키로도 동작(일 25건 제한); 등록 시 일 500건·20년치로 상승 |

CoinGecko·DefiLlama·업비트·바이낸스 공개 endpoint·CFTC Socrata·FiscalData·TreasuryDirect는 키 불필요.

## 수집 방법 구분 (indicators.yaml의 `method` 필드)
- `api`: 공식 API로 안정 수집 가능 — 1차 구현 대상
- `scrape`: 공식 API 없음, 공개 페이지/CSV 파싱 필요 (예: CME FedWatch, MOVE, ETF 플로우) — 2차
- `manual`: 유료·비정형 소스 (ISM PMI 본값, 컨퍼런스보드 LEI/심리, AAII, ICI 플로우, HY 부도율 등)
  — 앱은 수집하지 않고 Data Book에 "수동 입력" 슬롯만 생성

## 수용 기준 (Definition of Done)
1. `python -m databook run` 1회 실행으로 A·B·C팀 Data Book md 3개 + 스냅샷 JSON 1개 생성.
2. `method: api` 지표 전부가 실제 최신값을 담고, 각 값에 관측 기준일과 출처 URL이 붙는다.
3. 파생 지표 4종(순유동성·2s10s·한미 금리차·김치프리미엄)이 계산되어 포함된다.
4. 네트워크 차단 상태에서 실행해도 크래시 없이 "수집 실패" 표기로 완주한다.
5. `indicators.yaml`에 지표를 추가하면 코드 수정 없이 Data Book에 반영된다 (소스가 기존 fetcher인 경우).

## Obsidian 지표 노드 소환 (2026-08-14 추가)

`OBSIDIAN_VAULT_PATH`가 설정돼 있고 볼트에 `01_Indicators/`가 있으면,
매 실행마다 **`04_DataBook/DataBook 지표 소환.md` 허브 하나**를 덮어쓴다.
이 허브가 지표 노드를 `[[...]]`로 부르고, 노드의 Backlinks에서
**최신 수치와 논문·제텔이 만난다.**

### 왜 허브 하나인가

일별 노트가 각자 지표 노드를 소환하면 1년 뒤 `[[통화정책]]` 백링크가
Data Book 파일 수백 개로 덮여 문헌 신호가 죽는다. 그래서
**소환은 허브만 하고 일별 노트는 허브로 연결만 한다** — 노드당 백링크 1개.

### 매칭 규칙

`databook/vaultlink.py`가 볼트의 `01_Indicators/*.md`에서 파일명(stem)과
`aliases:`를 읽어 토큰 사전을 만들고, 지표 이름에 그 토큰이 들어 있으면 잇는다.
**최장일치 우선**, 토큰 2자 이상. 볼트나 폴더가 없으면 빈 매핑을 돌려주고
출력은 아무것도 바뀌지 않는다 — 노드 이름을 코드에 넣지 않는 이유다.

수동 지정은 `indicators.yaml`의 선택 필드로 한다.

```yaml
  - name: 재고 사이클 (재고/판매 비율)
    vault_node: "-"        # 자동 매칭 끄기 (오매칭 차단)
  - name: 어떤 지표
    vault_node: 기준금리    # 이 노드로 강제
```

실제로 `재고 사이클 (재고/판매 비율)`이 별칭 `재고` 때문에 `[[원자재 재고]]`
(LME 구리 등 실물 재고)로 잘못 붙어서 `-`로 막았다. 오매칭을 발견하면 같은 방식으로 처리한다.

### 커버리지 (2026-08-13 스냅샷 기준)

지표 224개 중 **104개가 29개 노드**에 연결됐다. 나머지는 볼트에 대응 노드가 없다
(NFP·JOLTS·Sahm Rule·소매판매 등). 허브의 "대응 노드가 없는 지표" 절에 전부 나열된다.
볼트 규칙상 **아무도 부르지 않는 노드는 만들지 않으므로**, 논문·제텔이 그 개념을
실제로 쓰기 시작할 때 노드를 만든다.

## BIS credit-to-GDP gap (2026-08-14 추가)

`databook/fetchers/bis.py` · `source: bis_credit_gap`. 키 불필요.
BIS 벌크 CSV(`WS_CREDIT_GAP`)를 **프로세스당 1회만** 받아 캐시한다(국가별 지표가 여럿이어도 1회).

```yaml
  - name: BIS credit-to-GDP gap (총신용·비은행 포함)
    method: api
    source: bis_credit_gap
    countries: [US, KR, CN, JP]   # BIS 2자리 코드, 44개국 지원
    dtype: C                      # C=gap(actual-trend) · A=비율 · B=추세
    points: 4                     # 최신부터 몇 분기
```

**왜 넣었나** — 기존 신용 지표(EBP·HY OAS·신용스프레드)는 전부 신용의 **가격**이고
"지금 실물이 꺾이나"(3~12개월)만 답한다. JST(2013)의 심각도 축("확장기 신용집약도가
높을수록 침체가 깊다")을 채우려면 신용의 **양**이 필요하다. RegimeView 6차 개정이
"볼트에 지표 없음"으로 남긴 구멍이었다.

**한계 (yaml note에도 있음)** — 분기 데이터이고 BIS 갱신이 2~3분기 지연된다.
단측 HP필터(λ=400,000)라 표본 끝단이 불안정하다. 추세는 통계적 산물이지 균형 수준이 아니다.
**주간 트리거로 쓰지 말고 배경 조건으로만 쓴다.**

## FRBSF Fernald 분기 TFP (2026-08-14 추가)

`databook/fetchers/frbsf.py` · `source: frbsf_tfp`. 키 불필요.
FRBSF 공개 xlsx(`quarterly_tfp.xlsx`)의 `quarterly` 시트를 의존성 없는 자체 리더로 읽는다.

```yaml
  - name: 미국 TFP (Fernald, 가동률 조정)
    method: api
    source: frbsf_tfp
    columns: [dLP, dtfp, dtfp_util, dk]   # 기본값
    points: 4
```

| 열 | 뜻 |
|---|---|
| `dLP` | 노동생산성 |
| `dk` | 자본투입 |
| `dtfp` | TFP |
| `dutil` | 가동률 |
| `dtfp_util` | **가동률 조정 TFP** |

**왜 넣었나** — DataBook에 생산성 지표가 하나도 없었다. 그리고 **노동생산성과 TFP는 다르다** —
노동생산성은 자본심화만으로도 오른다. 실제로 2026:Q2 기준 `dLP +1.20`인데
`dtfp_util −2.19`, `dk +3.19`다. 노동생산성 상승이 기술 개선이 아니라
자본투입·가동률에서 오고 있다는 뜻이며, 이 구분이 정책 함의를 가른다.

**한계** — 분기 데이터이고 **BEA 개정으로 과거치가 소급 수정**된다. 가동률 조정은 모형 기반이다.
미국 business sector 기준이라 BLS 비농업 노동생산성과 정의가 다르다.
