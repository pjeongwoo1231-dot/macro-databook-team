"""미 재무부 FiscalData·TreasuryDirect·CFTC Socrata — 전부 키 불필요."""
from __future__ import annotations

from typing import Any

from .base import get_json, result

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
        data = get_json(url, {"sort": "-record_date", "page[size]": 40})
        obs = []
        for r in data.get("data", []):
            if "Treasury General Account" not in str(r.get("account_type", "")):
                continue
            val = None
            for field, label in (("close_today_bal", "TGA 마감잔고($mn)"), ("open_today_bal", "TGA 개장잔고($mn)")):
                v = r.get(field)
                if v not in (None, "null", ""):
                    val, lab = float(v), label
                    break
            if val is not None:
                obs.append({"date": r["record_date"], "value": val, "label": lab})
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
