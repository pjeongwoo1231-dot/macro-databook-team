# DATA_CONNECTORS.md

# ============================================================================
# Data Connector Architecture
# ============================================================================

Version : 3.0 (삼위일체판 — 자동화 전면 확대)

---

# Purpose

MR-OS의 가장 중요한 기능은 자동 데이터 수집이다.

Claude는 데이터를 직접 기억하지 않는다.
Data Connector를 통해 현실 세계와 연결된다.

새로운 Data Source는 쉽게 추가할 수 있어야 한다.
Connector는 Plugin Architecture를 따른다 —
한 파일만 추가하면 동작한다.

자동화는 제한하지 않는다.
사람이 수동으로 반복하는 수집이 보이면 커넥터로 만든다.

---

# Data Flow

```
External Source
↓
Connector        (수집)
↓
Raw Data         (원본 보존)
↓
Normalizer       (단위 · 시간 · 국가코드 · 통화 · 숫자형식 · 언어 표준화)
↓
Knowledge Parser (Raw → Knowledge 변환)
↓
Obsidian         (Markdown 자동 저장 + 관련 노트 자동 연결)
↓
Graphify         (자동 Index + 관련 Node 자동 연결)
↓
Claude           (해석 · 요약 · Daily 생성)
```

---

# Data Principles

모든 데이터는 원본을 유지한다.
모든 데이터는 출처를 가진다.
모든 데이터는 시간을 가진다.
모든 데이터는 Version을 가진다.
모든 데이터는 Graph에 연결된다.

같은 데이터는 중복 저장하지 않는다. Version만 추가한다.

---

# Priority

1. Official Source
2. Academic
3. Research Institute
4. News
5. Community
6. SNS (반드시 교차 검증 — 단독 근거 금지)

---

# 현재 가동 (Core — macro-databook)

주 1회 GitHub Actions 자동 실행, 약 130개 지표 → 팀별 DataKit.

- FRED — 미국 매크로 전반
- ECOS — 한국 매크로
- KOSIS — 한국 통계
- 관세청 — 20일 수출, 품목별 수출입
- KRX — 외국인 수급 · 지수 · 공매도
- DART — 공시
- Yahoo Finance — 가격 (지수 · 환율 · 원자재 · 크립토)
- CME FedWatch — 금리 선물 내재 확률
- CFTC — 포지셔닝

---

# Connector Targets (확장 로드맵)

## Macro
OECD · IMF · World Bank · BIS · Trading Economics · UN Data

## Central Bank
Federal Reserve · ECB · BOJ · BOE · PBOC · BOK · RBA · SNB · BOC · RBNZ
→ Statement · Minutes · Speech · Projection · Dot Plot · Balance Sheet

## Government
미국 · 한국 · 중국 · 일본 · EU
→ 법안 · 예산 · 규제 · 행정명령 · 관세 · 제재 · 산업정책

## Financial Market
Alpha Vantage · Polygon · IEX · NASDAQ · NYSE · CBOE · CME · ICE
→ 주가 · 거래량 · 옵션 · 선물 · 금리 · ETF · Index · Market Breadth

## Commodity
WTI · Brent · 천연가스 · 구리 · 금 · 은 · 철광석 ·
리튬 · 니켈 · 우라늄 · 곡물 (옥수수 · 대두 · 밀)

## Fixed Income
US Treasury · KTB · HY/IG 스프레드 · CDS · Yield Curve

## Company
SEC EDGAR · Earnings Call · IR · Annual/Quarterly Report
→ 재무제표 · 가이던스 · 자본배분 · 배당 · M&A

## News
Reuters · Bloomberg · WSJ · FT · CNBC · 연합 · Nikkei · The Economist

## Research
IMF Paper · OECD Report · McKinsey · Brookings · CSIS · RAND · BIS · 학술논문

## Alternative Data
Satellite · AIS · Google Trends · Job Posting ·
Shipping (BDI · SCFI) · Flight · Weather · Energy Grid

## Social
X · Reddit · YouTube · Podcast · Substack
(신뢰도 낮음 — 교차 검증 필수)

## User Data
Journal · Meeting · Presentation · Idea · Prompt ·
Markdown · CSV · Excel · PDF

우선순위는 "학회원이 매주 실제로 쓰는 것"부터.
그러나 위시리스트를 지우지 않는다 — 자동화가 목표다.

---

# Metadata

모든 데이터는
Source · Author · Collected · Published · Updated ·
Reliability · Language · License
를 가진다.

---

# Refresh Policy

실시간 · 일간 · 주간 · 월간 · 분기 · 연간 업데이트를 지원한다.
지표별 주기는 커넥터 설정 파일에 선언한다.

---

# Retry & Error Handling

실패한 Connector는 자동 재시도한다. 실패 로그를 기록한다.
데이터 누락 · API 제한 · 형식 오류 · 네트워크 오류 · 권한 오류를
명확히 기록한다. 오류를 숨기지 않는다.

수집 실패 시 DataKit에 실패 표시를 남겨
Daily Note에 자동 경보로 올린다.

---

# Graphify / Obsidian / Claude Integration

새로운 데이터는 Markdown으로 자동 저장하고
관련 Note를 자동 연결한다.
Graphify에 자동 Index되고 관련 Node와 자동 연결된다.

Claude는 Connector를 직접 구현하지 않는다.
Connector를 호출하고 결과를 해석한다 —
해석은 여러 개, 추론 과정 포함 (RESEARCH_METHOD.md STEP 4).

---

# Never Do

- HTML만 저장하지 않는다.
- 원본 링크를 버리지 않는다.
- 출처를 삭제하지 않는다.
- 뉴스만으로 결론을 내리지 않는다.
- SNS만으로 분석하지 않는다.

---

# Success Criteria

좋은 Connector는 많은 데이터를 가져오는 것이 아니다.

신뢰할 수 있는 데이터를 일관된 형식으로 자동 수집하고
Knowledge Graph와 Long-term Memory에 즉시 연결하는 것이다.

그리고 사람의 시간이 수집이 아니라
학습과 체화에 쓰이게 만드는 것이다.

# ============================================================================
# EIA 원유 커넥터 (2026-08-25 신설) — **API 키 불필요**
# ============================================================================

FRED의 원유생산·재고 계열이 전부 폐지됐다(`MCRFPUS2`·`WCESTUS1` 등 404, 2026-08-25 확인).
**EIA의 공개 dnav 엔드포인트는 키 없이 열린다.** 이걸로 우회한다.

| 용도 | URL | 형식 |
|---|---|---|
| 미국 원유생산 (월, 천b/d) | `https://www.eia.gov/dnav/pet/hist_xls/MCRFPUS2m.xls` | .xls |
| 미국 원유재고 (주, 천배럴) | `https://www.eia.gov/dnav/pet/hist_xls/WCESTUS1w.xls` | .xls |
| WTI 현물 (일) | `https://www.eia.gov/dnav/pet/hist_xls/RWTCd.xls` | .xls |

**FRED에서 아직 살아 있는 것**: `DCOILWTICO`(WTI) · `DCOILBRENTEU`(브렌트).
→ 브렌트-WTI 스프레드는 FRED만으로 계산된다.

**파싱 주의**: 구형 `.xls`라 `xlrd>=2.0`으로 읽는다(openpyxl 불가).
데이터는 **두 번째 시트**(`sheet_by_index(1)`)에 있고 첫 열이 Excel 날짜 serial이다.

**실행기**: `_System/Analysis/oil_supply_monitor.py`
→ 생산 증가율 · 재고 vs 5년평균 · 브렌트-WTI 스프레드를 한 번에 출력한다.

**아직 못 뚫은 것**: CME 선물 곡선(프런트 스프레드) · 케플러 호르무즈 통항 · 중국 PPI(NBS 수동).

