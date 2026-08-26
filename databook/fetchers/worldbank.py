"""World Bank Open Data API — 키 불필요, 무료. FRED/OECD 커버리지가 없는 비OECD
국가(사우디·UAE·나이지리아·카자흐스탄·튀르키예 등)의 GDP·CPI를 표준화된 형태로 제공한다.

⚠ 한계 (yaml note에도 명시할 것):
- 연간 데이터만 제공 (월/분기 아님) — 매주 갱신되는 지표가 아니라 연간 배경 지표로 취급
- 최신값도 1년 이상 지연될 수 있음 (mrnev=1로 최신 유효값 요청)
- 서버가 간헐적으로 500(Request Error)을 반환 — 재시도 로직 필수
"""
from __future__ import annotations

import time
from typing import Any

from .base import get_json, result

BASE = "https://api.worldbank.org/v2/country"
RETRIES = 3
RETRY_DELAY = 2.0


def fetch_indicator(country_iso3: str, indicator_code: str) -> tuple[str, float, str]:
    url = f"{BASE}/{country_iso3}/indicator/{indicator_code}?format=json&per_page=1&mrnev=1"
    last_err: Exception | None = None
    for attempt in range(RETRIES):
        try:
            data = get_json(url)
            rows = data[1] if isinstance(data, list) and len(data) > 1 else None
            if not rows:
                raise ValueError(f"데이터 없음 ({country_iso3}/{indicator_code})")
            row = rows[0]
            return row["date"], float(row["value"]), url
        except Exception as e:  # World Bank가 간헐적으로 HTML 에러페이지 반환 — 재시도
            last_err = e
            if attempt < RETRIES - 1:
                time.sleep(RETRY_DELAY)
    raise last_err  # type: ignore[misc]


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    country_iso3 = ind.get("country_iso3")
    indicator_code = ind.get("indicator_code")
    if not country_iso3 or not indicator_code:
        return result(ind, "fail", error="country_iso3/indicator_code 미지정")
    try:
        date, value, url = fetch_indicator(country_iso3, indicator_code)
    except Exception as e:
        return result(ind, "fail", error=f"World Bank {type(e).__name__}: {e}")
    obs = [{"date": date, "value": round(value, 2), "label": f"{indicator_code} (연간, World Bank)"}]
    return result(ind, "ok", observations=obs, source_url=url)
