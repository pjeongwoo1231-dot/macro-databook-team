"""BLS Public API v2 — registrationkey 없이도 조회 가능(무키: 일 25건, 데이터 3년치 제한).
BLS_API_KEY 설정 시 자동으로 실어 보내 한도 상승(일 500건, 20년치, 시리즈 배치)."""
from __future__ import annotations

from typing import Any

from .base import get_json, result

BASE = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
N_OBS = 6


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    series_id = ind.get("series_id", "")
    if not series_id:
        return result(ind, "fail", error="series_id 미지정")
    key = env.get("BLS_API_KEY", "")
    url = BASE + series_id
    data = get_json(url, {"registrationkey": key} if key else None)
    if data.get("status") != "REQUEST_SUCCEEDED":
        msg = "; ".join(data.get("message", [])) or data.get("status", "알 수 없는 오류")
        return result(ind, "fail", error=f"BLS: {msg}", source_url=url)
    series = data.get("Results", {}).get("series", [])
    if not series or not series[0].get("data"):
        return result(ind, "fail", error="관측치 없음", source_url=url)
    rows = []
    for r in series[0]["data"]:
        period = r.get("period", "")
        val = r.get("value")
        if not period.startswith("M") or period == "M13" or val in (None, ""):
            continue  # M13=연평균 등 월별 아닌 행 제외
        try:
            fval = float(val)
        except ValueError:
            continue  # "-" 등 결측(예: 셧다운으로 인한 데이터 공백) 스킵
        rows.append((r["year"], period[1:], fval))
    rows.sort(reverse=True)
    obs = [{"date": f"{y}-{m}-01", "value": v, "label": series_id} for y, m, v in rows[:N_OBS]]
    if not obs:
        return result(ind, "fail", error="월별 관측치 없음", source_url=url)
    note = ind.get("note", "")
    if not key:
        note = (note + " · 무키 접속(BLS_API_KEY 미설정, 일 25건 제한) — bls.gov/developers 등록 시 한도 상승").strip(" ·")
    return result(ind, "ok", observations=obs, note=note,
                  source_url=f"https://data.bls.gov/timeseries/{series_id}")
