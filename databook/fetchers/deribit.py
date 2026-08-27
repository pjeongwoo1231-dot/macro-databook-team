"""Deribit DVOL — 암호자산 내재변동성 지수. 공개 API, 키 불필요.

DVOL은 BTC/ETH 옵션의 30일 내재변동성을 VIX와 같은 방식으로 산출한 지수다.
크립토 층에 가격·온체인은 있었지만 **옵션이 가격하는 위험**은 없었다 — 그 공백을 메운다.

⚠ VIX와 스케일이 비슷해 보여도 같은 자산이 아니다. BTC DVOL 40은 주식 VIX 40과
같은 의미의 "패닉"이 아니라 크립토의 평시 수준에 가깝다. 절대수준이 아니라
자기 이력 대비 위치로 읽을 것.
"""
from __future__ import annotations

import time
from typing import Any

from .base import get_json, result

BASE = "https://www.deribit.com/api/v2/public/get_volatility_index_data"
N_OBS = 6


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """currency: BTC | ETH (리스트 가능). resolution 43200 = 12시간봉."""
    cur = ind.get("currency", "BTC")
    currencies = [cur] if isinstance(cur, str) else list(cur)
    now = int(time.time() * 1000)
    start = now - 15 * 86400 * 1000  # 15일치면 12시간봉 30개 — N_OBS를 채우고 남는다

    all_obs: list[dict[str, Any]] = []
    errors: list[str] = []
    for c in currencies:
        try:
            d = get_json(f"{BASE}?currency={c}&start_timestamp={start}"
                         f"&end_timestamp={now}&resolution=43200")
            rows = d.get("result", {}).get("data", [])
            if not rows:
                errors.append(f"{c}: 관측치 없음")
                continue
            # 각 행: [timestamp, open, high, low, close]
            for row in rows[-N_OBS:][::-1]:
                ts, close = row[0], row[4]
                if not isinstance(close, (int, float)):
                    continue
                date = time.strftime("%Y-%m-%d %H:%M", time.gmtime(ts / 1000))
                all_obs.append({"date": date, "value": round(float(close), 2),
                                "label": f"{c} DVOL (30일 내재변동성)"})
        except Exception as e:
            errors.append(f"{c}: {type(e).__name__}: {e}")

    if not all_obs:
        return result(ind, "fail", error="; ".join(errors) or "관측치 없음")
    res = result(ind, "ok", observations=all_obs,
                 source_url="https://www.deribit.com/api/v2/public/get_volatility_index_data",
                 unit="%")
    if errors:
        res["error"] = "; ".join(errors)
    return res
