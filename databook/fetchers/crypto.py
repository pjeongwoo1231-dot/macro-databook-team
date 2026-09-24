"""크립토 소스 — CoinGecko·DefiLlama·alternative.me·CoinMetrics·업비트·바이낸스. 전부 키 불필요."""
from __future__ import annotations

import re
import time

from datetime import datetime, timezone
from typing import Any

from .base import get_json, result

STABLES = {"tether", "usd-coin", "dai", "ethena-usde", "first-digital-usd", "paypal-usd", "true-usd", "binance-usd", "usds", "usdtb", "usd1", "frax", "usdd"}


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def fetch_coingecko(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    endpoint = ind.get("endpoint", "")
    url = f"https://api.coingecko.com/api/v3{endpoint}"
    if "/coins/markets" in endpoint:
        rows = get_json(url)
        obs = []
        for r in rows:
            if r.get("id") in STABLES:
                continue
            obs.append({"date": _today(), "value": float(r["current_price"]), "label": f"{str(r.get('symbol', '')).upper()} (USD)"})
            if len(obs) >= 10:
                break
        return result(ind, "ok", observations=obs, source_url="https://www.coingecko.com") if obs else result(ind, "fail", error="응답 비어있음", source_url=url)
    if "/global" in endpoint:
        data = get_json(url).get("data", {})
        mcap = float(data["total_market_cap"]["usd"])
        obs = [
            {"date": _today(), "value": mcap, "label": "전체 시총(USD)"},
            {"date": _today(), "value": round(float(data["market_cap_percentage"]["btc"]), 2), "label": "BTC 도미넌스(%)"},
        ]
        # 거래량은 가격과 다른 정보를 담는다(회전율 = 유동성 상태). 볼트 [[글로벌 유동성]] 규칙 참조
        vol = data.get("total_volume", {}).get("usd")
        if vol:
            obs.append({"date": _today(), "value": float(vol), "label": "전체 24h 거래량(USD)"})
            if mcap:
                obs.append({"date": _today(), "value": round(100.0 * float(vol) / mcap, 2), "label": "회전율(거래량/시총, %)"})
        return result(ind, "ok", observations=obs, source_url="https://www.coingecko.com/en/global-charts")
    return result(ind, "fail", error=f"미지원 endpoint: {endpoint}")


def fetch_defillama(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    url = "https://stablecoins.llama.fi/stablecoins?includePrices=false"
    data = get_json(url)
    total = 0.0
    top = []
    for a in data.get("peggedAssets", []):
        circ = (a.get("circulating") or {}).get("peggedUSD")
        if circ:
            total += float(circ)
            top.append((float(circ), a.get("symbol", "?")))
    if total <= 0:
        return result(ind, "fail", error="circulating 파싱 실패", source_url=url)
    top.sort(reverse=True)
    obs = [{"date": _today(), "value": total, "label": "스테이블코인 총 시총(USD)"}]
    obs += [{"date": _today(), "value": v, "label": f"{s} 시총(USD)"} for v, s in top[:3]]
    return result(ind, "ok", observations=obs, source_url="https://defillama.com/stablecoins")


def fetch_alternative_me(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    data = get_json("https://api.alternative.me/fng/?limit=6")
    obs = []
    for r in data.get("data", []):
        d = datetime.fromtimestamp(int(r["timestamp"]), tz=timezone.utc).strftime("%Y-%m-%d")
        obs.append({"date": d, "value": float(r["value"]), "label": r.get("value_classification", "")})
    return result(ind, "ok", observations=obs, source_url="https://alternative.me/crypto/fear-and-greed-index/") if obs else result(ind, "fail", error="데이터 없음")


def fetch_coinmetrics(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    url = "https://community-api.coinmetrics.io/v4/timeseries/asset-metrics"
    data = get_json(url, {"assets": "btc", "metrics": "CapMVRVCur", "frequency": "1d", "page_size": 6})
    rows = data.get("data", [])
    obs = [
        {"date": str(r.get("time", ""))[:10], "value": round(float(r["CapMVRVCur"]), 3), "label": "BTC MVRV"}
        for r in rows
        if r.get("CapMVRVCur") is not None
    ][::-1]
    if not obs:
        return result(ind, "fail", error="CapMVRVCur 커뮤니티 API 미제공 — manual 강등 검토", source_url=url)
    return result(ind, "ok", observations=obs, source_url="https://coinmetrics.io/community-network-data/")


def fetch_upbit(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    rows = get_json("https://api.upbit.com/v1/ticker?markets=KRW-BTC")
    r = rows[0]
    obs = [{"date": _today(), "value": float(r["trade_price"]), "label": "KRW-BTC"}]
    return result(ind, "ok", observations=obs, source_url="https://upbit.com")


def fetch_binance(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """펀딩레이트·미결제약정. **BTC만 보던 것을 symbols 목록으로 넓혔다**(2026-09-16) —
    ETH가 BTC와 갈리는 구간이 레버리지 사이클의 국면 전환인데 BTC만으로는 안 보인다."""
    obs = []
    errors = []
    for sym in (ind.get("symbols") or ["BTCUSDT"]):
        coin = sym.replace("USDT", "")
        try:
            p = get_json(f"https://fapi.binance.com/fapi/v1/premiumIndex?symbol={sym}")
            obs.append({"date": _today(), "value": float(p["lastFundingRate"]) * 100,
                        "label": f"{coin} 펀딩레이트(%, 8h)"})
        except Exception as e:
            errors.append(f"{coin} 펀딩레이트: {e}")
        try:
            oi = get_json(f"https://fapi.binance.com/fapi/v1/openInterest?symbol={sym}")
            obs.append({"date": _today(), "value": float(oi["openInterest"]),
                        "label": f"{coin} 미결제약정({coin})"})
        except Exception as e:
            errors.append(f"{coin} 미결제약정: {e}")
    if not obs:
        return result(ind, "fail", error="; ".join(errors) or "실패", source_url="https://www.binance.com")
    res = result(ind, "ok", observations=obs, source_url="https://www.binance.com")
    if errors:
        res["error"] = "; ".join(errors)
    return res


# ================================================= 크립토 다각화 (2026-09-16)
# **왜 늘리나**: 기존 10개는 가격·시총·심리에 몰려 있었다. 매크로 축에서 크립토가 값을 하려면
# 가격이 아니라 **레버리지·캐리·생산비용·온체인 유동성**을 봐야 한다 — 그게 달러 유동성과
# 위험선호의 고빈도 대리이기 때문이다. 아래 넷은 전부 무료·키 불필요 (2026-09-16 실호출 200 확인).
#
# ⚠ 크립토는 24시간 거래라 기준시각이 흔들린다. 값은 **호출 시점 스냅샷**이다 —
#   일별 비교는 같은 시각에 받은 것끼리만 한다.

def fetch_mempool(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """비트코인 채굴 경제 — 해시레이트·난이도.

    **왜 매크로인가**: 해시레이트는 **생산비용의 하한**을 만들고, 급락은 채굴자 항복
    (보유분 매도)의 선행 신호다. 반감기 카운트다운만으로는 이걸 못 본다.
    """
    obs, errors = [], []
    try:
        d = get_json("https://mempool.space/api/v1/mining/hashrate/3m")
        hr = d.get("hashrates") or []
        if hr:
            last = hr[-1]
            obs.append({"date": _today(),
                        "value": float(last["avgHashrate"]) / 1e18,
                        "label": "해시레이트 (EH/s)"})
        diff = d.get("difficulty") or []
        if diff:
            obs.append({"date": _today(),
                        "value": float(diff[-1]["difficulty"]) / 1e12,
                        "label": "채굴 난이도 (T)"})
    except Exception as e:
        errors.append(f"해시레이트: {e}")
    if not obs:
        return result(ind, "fail", error="; ".join(errors) or "실패",
                      source_url="https://mempool.space")
    res = result(ind, "ok", observations=obs, source_url="https://mempool.space")
    if errors:
        res["error"] = "; ".join(errors)
    return res


def fetch_defillama_chains(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """체인별 DeFi TVL — 온체인 유동성이 어디에 있나.

    스테이블코인 시총이 '얼마나'라면 이건 '어디에'다. 체인 간 이동은
    수익률 추종이라 **위험선호의 방향**을 보여준다.
    """
    chains = ind.get("chains") or ["Ethereum", "Solana", "Base", "Arbitrum", "BSC"]
    obs, errors = [], []
    try:
        rows = get_json("https://api.llama.fi/v2/chains")
        by = {r.get("name"): r for r in rows if isinstance(r, dict)}
        for c in chains:
            r = by.get(c)
            if not r or r.get("tvl") is None:
                errors.append(f"{c}: 없음")
                continue
            obs.append({"date": _today(), "value": float(r["tvl"]) / 1e9,
                        "label": f"{c} TVL (십억$)"})
    except Exception as e:
        errors.append(str(e))
    if not obs:
        return result(ind, "fail", error="; ".join(errors) or "실패",
                      source_url="https://defillama.com/chains")
    res = result(ind, "ok", observations=obs, source_url="https://defillama.com/chains")
    if errors:
        res["error"] = "; ".join(errors)
    return res


def fetch_coinbase_premium(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """코인베이스 프리미엄 — 미국 기관 수요의 대리지표.

    **김치프리미엄의 반대편이다.** 김프가 한국 자본통제·차익거래 실패를 재는 것처럼,
    코인베이스 프리미엄은 **미국 쪽 매수 강도**를 잰다. 둘을 같이 보면
    어느 지역이 밀고 있는지 갈린다.
    ⚠ 두 거래소 호가를 **각각 따로** 받으므로 몇 초의 시차가 낀다. 소수점 둘째 자리는 믿지 않는다.
    """
    obs, errors = [], []
    cb = bn = None
    try:
        d = get_json("https://api.exchange.coinbase.com/products/BTC-USD/ticker")
        cb = (float(d["bid"]) + float(d["ask"])) / 2
        obs.append({"date": _today(), "value": cb, "label": "Coinbase BTC-USD (중간가)"})
    except Exception as e:
        errors.append(f"coinbase: {e}")
    try:
        d = get_json("https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT")
        bn = (float(d["bidPrice"]) + float(d["askPrice"])) / 2
        obs.append({"date": _today(), "value": bn, "label": "Binance BTCUSDT (중간가)"})
    except Exception as e:
        errors.append(f"binance: {e}")
    if cb and bn:
        obs.append({"date": _today(), "value": (cb / bn - 1) * 100,
                    "label": "코인베이스 프리미엄 (%, USDT 기준)"})
    if not obs:
        return result(ind, "fail", error="; ".join(errors) or "실패",
                      source_url="https://exchange.coinbase.com")
    res = result(ind, "ok", observations=obs, source_url="https://exchange.coinbase.com")
    if errors:
        res["error"] = "; ".join(errors)
    return res


def fetch_deribit_basis(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """선물 베이시스와 연율 캐리 — 크립토판 달러 캐리.

    선물이 현물보다 비싸면(콘탱고) 현물매수+선물매도로 캐리를 먹을 수 있다.
    그 **연율 캐리가 달러 조달금리 대비 얼마인가**가 레버리지 수요의 가격이다.
    베이시스 축소는 디레버리징 신호 — 가격이 빠지기 전에 먼저 움직이는 경우가 많다.
    ⚠ 만기가 가까울수록 연율화가 불안정해진다. 잔존 7일 미만은 버린다.
    """
    cur = ind.get("currency", "BTC")
    obs, errors = [], []
    try:
        idx = get_json(f"https://www.deribit.com/api/v2/public/get_index_price?index_name={cur.lower()}_usd")
        spot = float(idx["result"]["index_price"])
        obs.append({"date": _today(), "value": spot, "label": f"{cur} 현물 지수 ($)"})
        rows = get_json(f"https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency={cur}&kind=future")
        best = None
        for r in rows.get("result", []):
            name = r.get("instrument_name", "")
            if name.endswith("PERPETUAL") or not r.get("mark_price"):
                continue
            # ⚠ book_summary 응답에는 expiration_timestamp가 **없다**(2026-09-16 실측).
            #    만기는 종목명에서 뽑는다 — "BTC-30OCT26" 형식이다.
            mm = re.match(r"^[A-Z]+-(\d{1,2})([A-Z]{3})(\d{2})$", name)
            if not mm:
                continue
            try:
                exp_dt = datetime.strptime(
                    f"{mm.group(1)}{mm.group(2)}20{mm.group(3)}", "%d%b%Y")
            except ValueError:
                continue
            days = (exp_dt - datetime.utcnow()).total_seconds() / 86400
            if days < 7:                       # 만기 임박분은 연율화가 튄다
                continue
            if best is None or days < best[0]:
                best = (days, name, float(r["mark_price"]))
        if best:
            days, name, mark = best
            basis = (mark / spot - 1) * 100
            obs.append({"date": _today(), "value": basis, "label": f"{name} 베이시스 (%)"})
            obs.append({"date": _today(), "value": basis * 365 / days,
                        "label": f"연율 캐리 (%, 잔존 {days:.0f}일)"})
        else:
            errors.append("잔존 7일 이상 선물이 없다")
    except Exception as e:
        errors.append(str(e))
    if not obs:
        return result(ind, "fail", error="; ".join(errors) or "실패",
                      source_url="https://www.deribit.com")
    res = result(ind, "ok", observations=obs, source_url="https://www.deribit.com")
    if errors:
        res["error"] = "; ".join(errors)
    return res
