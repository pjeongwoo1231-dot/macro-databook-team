"""크립토 소스 — CoinGecko·DefiLlama·alternative.me·CoinMetrics·업비트·바이낸스. 전부 키 불필요."""
from __future__ import annotations

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
    obs = []
    errors = []
    try:
        p = get_json("https://fapi.binance.com/fapi/v1/premiumIndex?symbol=BTCUSDT")
        obs.append({"date": _today(), "value": float(p["lastFundingRate"]) * 100, "label": "BTC 펀딩레이트(%, 8h)"})
    except Exception as e:
        errors.append(f"펀딩레이트: {e}")
    try:
        oi = get_json("https://fapi.binance.com/fapi/v1/openInterest?symbol=BTCUSDT")
        obs.append({"date": _today(), "value": float(oi["openInterest"]), "label": "BTC 미결제약정(BTC)"})
    except Exception as e:
        errors.append(f"미결제약정: {e}")
    if not obs:
        return result(ind, "fail", error="; ".join(errors) or "실패", source_url="https://www.binance.com")
    res = result(ind, "ok", observations=obs, source_url="https://www.binance.com")
    if errors:
        res["error"] = "; ".join(errors)
    return res
