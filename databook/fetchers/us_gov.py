"""미 재무부 FiscalData·TreasuryDirect·CFTC Socrata — 전부 키 불필요."""
from __future__ import annotations

from typing import Any

from .base import BROWSER_UA, get_json, get_text, result

FISCAL_BASE = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"


def fetch_fiscaldata(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    endpoint = ind.get("endpoint", "")
    url = f"{FISCAL_BASE}{endpoint}"
    if "debt_to_penny" in endpoint:
        data = get_json(url, {"sort": "-record_date", "page[size]": 6})
        obs = [
            {"date": r["record_date"], "value": float(r["tot_pub_debt_out_amt"]), "label": "총 국가부채(USD)"}
            for r in data.get("data", [])
            if r.get("tot_pub_debt_out_amt") not in (None, "null")
        ]
        return result(ind, "ok", observations=obs, source_url=url) if obs else result(ind, "fail", error="데이터 없음", source_url=url)
    if "operating_cash_balance" in endpoint:
        # ⚠ 2026-09-27 수정 — 날짜마다 "Opening Balance"와 "Closing Balance" **두 행**이 온다.
        #   예전엔 둘 다 받아 "개장잔고"로 적었다 → 9/22 Data Book이 **9/18 개장잔고(= 9/17 마감)**를
        #   "최신"으로 싣고 있었다(실제 9/18 마감 985,932). **마감잔고 행만** 쓴다.
        #   API 특이점: 마감잔고 행도 값이 `open_today_bal` 칸에 있고 `close_today_bal`은 null이다.
        data = get_json(url, {"sort": "-record_date", "page[size]": 60,
                              "filter": "account_type:eq:Treasury General Account (TGA) Closing Balance"})
        obs = []
        for r in data.get("data", []):
            val = None
            for field in ("close_today_bal", "open_today_bal"):
                v = r.get(field)
                if v not in (None, "null", ""):
                    val = float(v)
                    break
            if val is not None:
                obs.append({"date": r["record_date"], "value": val, "label": "TGA 마감잔고($mn)"})
            if len(obs) >= 6:
                break
        return result(ind, "ok", observations=obs, source_url=url) if obs else result(ind, "fail", error="TGA 행 파싱 실패(필드 변경 가능성)", source_url=url)
    if "mts_table_9" in endpoint:
        # 월간 재무부 보고서 표9 = **수입 항목별** 실적. 관세(Customs Duties)가 여기 있다.
        # 볼트의 [[무역분쟁·관세]] 노드가 "계열이 없다"고 적어둔 그 계열이다(2026-08-21 신설).
        #
        # ⚠ **부호 규약 주의.** 필드명이 `rcpt_outly`(수입/지출 겸용)라 **환급이 크면 당월이 음수**가 된다.
        #   실측(2026-08-21): 2026-06 −256억달러 · 2026-07 −85억달러이고
        #   **회계연도 누계(FYTD)도 1,886억 → 1,545억으로 줄었다** — 대규모 환급이 일어났다는 뜻이다.
        #   따라서 **당월값만 보고 "관세가 줄었다"로 읽지 말 것.** 누계와 전년 누계를 함께 본다.
        want = [w.strip() for w in (ind.get("items") or ["Customs Duties"])]
        data = get_json(url, {"sort": "-record_date", "page[size]": 3000,
                              "filter": f"record_date:gte:{ind.get('since', '2024-10-01')}"})
        obs = []
        for r in data.get("data", []):
            desc = str(r.get("classification_desc", "")).strip()
            if desc not in want:
                continue
            d = r.get("record_date")
            for field, lab in (("current_month_rcpt_outly_amt", "당월"),
                               ("current_fytd_rcpt_outly_amt", "회계연도 누계"),
                               ("prior_fytd_rcpt_outly_amt", "전년 동기 누계")):
                v = r.get(field)
                if v in (None, "null", ""):
                    continue
                try:
                    obs.append({"date": d, "value": round(float(v) / 1e8, 1),
                                "label": f"{desc} {lab}(억달러)"})
                except ValueError:
                    pass
        obs = obs[:int(ind.get("points") or 18)]
        return (result(ind, "ok", observations=obs, source_url=url, unit="억달러")
                if obs else result(ind, "fail", error="해당 분류 없음", source_url=url))
    return result(ind, "fail", error=f"미지원 endpoint: {endpoint}")


UMICH_FILES = {
    # 미시간대 소비자조사 원본 표. **FRED의 MICH·UMCSENT는 라이선스 때문에 한 달 늦다**
    # (2026-09-25 기준 FRED 최종 = 8월, 원본 = 9월). 레짐 트리거 ⑦이 이 계열을 쓰는데
    # 09-13·09-22 시황 모두 「STALE」로 판정 불가였다 → 원본을 직접 읽는다(2026-09-27 신설).
    #  열: Month, YYYY, 값… (월 이름 영문)
    "sentiment": ("tbmics.csv", [(2, "소비자심리지수")]),
    "expectations": ("tbmpx1px5.csv", [(2, "기대인플레 1년(%)"), (3, "기대인플레 5~10년(%)")]),
}
_MONTHS = {m: i for i, m in enumerate(["January", "February", "March", "April", "May", "June", "July",
                                         "August", "September", "October", "November", "December"], 1)}


def load_umich(kind: str) -> dict[str, list[tuple[str, float]]]:
    """{라벨: [(YYYY-MM-01, 값), …]} — 원본 CSV 전 이력. history 수집에서도 재사용한다."""
    fname, cols = UMICH_FILES[kind]
    text = get_text(f"https://www.sca.isr.umich.edu/files/{fname}", headers={"User-Agent": BROWSER_UA})
    out: dict[str, list[tuple[str, float]]] = {lab: [] for _, lab in cols}
    for line in text.splitlines():
        parts = [x.strip() for x in line.split(",")]
        if len(parts) < 3 or parts[0] not in _MONTHS or not parts[1].isdigit():
            continue
        d = f"{int(parts[1]):04d}-{_MONTHS[parts[0]]:02d}-01"
        for idx, lab in cols:
            try:
                out[lab].append((d, float(parts[idx])))
            except (IndexError, ValueError):
                pass
    return out


def fetch_umich(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    kind = ind.get("kind", "expectations")
    url = f"https://www.sca.isr.umich.edu/files/{UMICH_FILES[kind][0]}"
    series = load_umich(kind)
    obs = []
    for lab, pts in series.items():
        for d, v in pts[-6:][::-1]:
            obs.append({"date": d, "value": v, "label": lab})
    # ⚠ 당월 값은 예비치(둘째 금요일)일 수 있다 — 원본 파일은 예비/확정을 구분해 표시하지 않는다.
    return (result(ind, "ok", observations=obs, source_url=url,
                   note=(ind.get("note", "") + " ⚠ 당월 값은 예비치일 수 있음(원본 미표시)").strip())
            if obs else result(ind, "fail", error="원본 표 파싱 실패", source_url=url))


def fetch_treasurydirect(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    url = "https://www.treasurydirect.gov/TA_WS/securities/auctioned?days=45&format=json"
    rows = get_json(url)
    obs = []
    for r in rows:
        btc = r.get("bidToCoverRatio")
        if btc in (None, ""):
            continue
        label = f"{r.get('securityTerm', '')} {r.get('securityType', '')} 응찰률"
        obs.append({"date": str(r.get("auctionDate", ""))[:10], "value": float(btc), "label": label.strip()})
        if len(obs) >= 8:
            break
    if not obs:
        return result(ind, "fail", error="최근 45일 입찰 결과에 응찰률 없음", source_url=url)
    return result(ind, "ok", observations=obs, source_url=url)


CFTC_MARKETS = {"JAPANESE YEN": "엔 비상업 순포지션", "E-MINI S&P 500": "S&P500 비상업 순포지션", "UST 10Y NOTE": "미 10Y 비상업 순포지션"}


def fetch_cftc(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    url = "https://publicreporting.cftc.gov/resource/6dca-aqww.json"
    rows = get_json(url, {"$order": "report_date_as_yyyy_mm_dd DESC", "$limit": 1500})
    obs = []
    for r in rows:
        market = str(r.get("market_and_exchange_names", "")).upper()
        for key, label in CFTC_MARKETS.items():
            if key in market:
                try:
                    net = float(r["noncomm_positions_long_all"]) - float(r["noncomm_positions_short_all"])
                except (KeyError, ValueError, TypeError):
                    continue
                obs.append({"date": str(r.get("report_date_as_yyyy_mm_dd", ""))[:10], "value": net, "label": label})
    seen: set[str] = set()
    dedup = []
    for o in obs:  # 최신 보고일만, 마켓별 1건
        if o["label"] not in seen:
            seen.add(o["label"])
            dedup.append(o)
    if not dedup:
        return result(ind, "fail", error="대상 마켓(엔·S&P·10Y) 미발견 — 마켓명 매칭 확인 필요", source_url=url)
    return result(ind, "ok", observations=dedup, source_url="https://publicreporting.cftc.gov")


def fetch_eia(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """EIA v2 API — eia_route(예: petroleum/stoc/wstk) + eia_series(예: WCESTUS1).
    EIA_API_KEY 미설정 시 DEMO_KEY 사용(레이트리밋 있음, 주 1회 실행이면 충분)."""
    key = env.get("EIA_API_KEY") or "DEMO_KEY"
    route = ind.get("eia_route", "")
    series = ind.get("eia_series", "")
    if not (route and series):
        return result(ind, "fail", error="eia_route/eia_series 미지정")
    url = (f"https://api.eia.gov/v2/{route}/data/?api_key={key}&frequency=weekly"
           f"&data[0]=value&facets[series][]={series}"
           f"&sort[0][column]=period&sort[0][direction]=desc&length=6")
    data = get_json(url)
    rows = data.get("response", {}).get("data", [])
    obs = []
    for r in rows:
        v = r.get("value")
        if v is None:
            continue
        unit = r.get("units", "")
        obs.append({"date": str(r.get("period", "")), "value": float(v),
                    "label": f"{series}({unit})" if unit else series})
    if not obs:
        return result(ind, "fail", error=f"EIA 관측치 없음 (route={route}, series={series})")
    note = ind.get("note", "")
    if key == "DEMO_KEY":
        note = (note + " · DEMO_KEY 사용 중 — eia.gov/opendata에서 무료 키 발급 권장").strip(" ·")
    return result(ind, "ok", observations=obs, note=note,
                  source_url=f"https://www.eia.gov/petroleum/supply/weekly/")

def fetch_treasury_auctions(ind: dict, env: dict) -> dict:
    """TreasuryDirect 입찰 결과 — 최근 낙찰금리·응찰배수(키 불필요).

    왜 필요한가: 장기물 수요를 재는 **직접 관측치**다. 시황이 흔히 인용하는
    "30년 입찰금리가 몇 년 만에 최고" 같은 문장을 우리가 검증하려면 이 계열이 필요하다.
    ⚠ high yield/rate는 증권 유형에 따라 필드가 다르다(Bill은 할인율).
    """
    from .base import result, get_json
    url = "https://www.treasurydirect.gov/TA_WS/securities/auctioned?format=json&pagesize=60"
    want = {str(t).lower() for t in (ind.get("terms") or ["10-year", "30-year"])}
    try:
        rows = get_json(url)
    except Exception as e:
        return result(ind, "fail", error=f"TreasuryDirect 수집 실패: {e}", source_url=url)
    obs = []
    for r in rows:
        term = str(r.get("securityTerm", "")).lower()
        if not any(w in term for w in want):
            continue
        d = str(r.get("auctionDate", ""))[:10]
        hy = r.get("highYield") or r.get("highDiscountRate") or r.get("interestRate")
        btc = r.get("bidToCoverRatio")
        try:
            if hy not in (None, ""):
                obs.append({"date": d, "value": float(hy),
                            "label": f"{r.get('securityTerm')} {r.get('securityType')} 낙찰금리(%)"})
            if btc not in (None, ""):
                obs.append({"date": d, "value": float(btc),
                            "label": f"{r.get('securityTerm')} 응찰배수"})
        except (TypeError, ValueError):
            continue
        if len(obs) >= 12:
            break
    if not obs:
        return result(ind, "fail", error=f"해당 만기 입찰 미발견({want})", source_url=url)
    return result(ind, "ok", observations=obs, source_url=url)
