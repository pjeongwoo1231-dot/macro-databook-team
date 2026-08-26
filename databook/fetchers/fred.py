"""FRED — series_id가 리스트면 시리즈별 관측치를 label로 구분해 합친다."""
from __future__ import annotations

from typing import Any

from .base import get_json, result

import datetime as _dt

BASE = "https://api.stlouisfed.org/fred/series/observations"
N_OBS = 6


def fetch_series(series_id: str, api_key: str, units: str = "") -> tuple[list[dict[str, Any]], str]:
    # ⚠ CBO 계열(GDPPOT·NROU 등)은 **미래 전망치를 포함**한다. limit이 최신 N개만 가져오므로
    #   그냥 받으면 2036년 전망만 담겨 온다(2026-08-21 실측). **API 단에서 오늘까지로 자른다.**
    today = _dt.date.today().isoformat()
    url = (f"{BASE}?series_id={series_id}&api_key={api_key}&file_type=json"
           f"&sort_order=desc&limit={N_OBS}&observation_end={today}")
    if units:  # 예: pc1 = 전년동기비 %
        url += f"&units={units}"
    data = get_json(url)
    obs = []
    # ⚠ **CBO 계열(GDPPOT·NROU 등)은 미래 전망치를 포함한다.** 정렬이 최신순이라
    #   그대로 두면 2036년 전망이 "최신값"으로 표시된다(2026-08-21에 실제로 그랬다).
    #   실적치만 남기고, 전망 구간은 잘라낸다 — **없는 관측을 있는 것처럼 보이지 않게 한다.**
    for row in data.get("observations", []):
        if row.get("value") in (".", "", None):
            continue
        obs.append({"date": row["date"], "value": float(row["value"]), "label": series_id})
    public_url = f"https://fred.stlouisfed.org/series/{series_id}"
    return obs, public_url


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    key = env.get("FRED_API_KEY", "")
    if not key:
        return result(ind, "fail", error="FRED_API_KEY 없음 (.env 확인)")
    ids = ind["series_id"]
    if isinstance(ids, str):
        ids = [ids]
    all_obs: list[dict[str, Any]] = []
    urls: list[str] = []
    errors: list[str] = []
    units = str(ind.get("units", ""))
    for sid in ids:
        try:
            obs, url = fetch_series(sid, key, units)
            if not obs:
                errors.append(f"{sid}: 관측치 없음(단종 가능성)")
            all_obs.extend(obs)
            urls.append(url)
        except Exception as e:
            errors.append(f"{sid}: {type(e).__name__}: {e}")
    if not all_obs:
        return result(ind, "fail", error="; ".join(errors) or "관측치 없음")
    res = result(ind, "ok", observations=all_obs, source_url=" ".join(urls))
    if errors:
        res["error"] = "; ".join(errors)  # 부분 실패 병기

    # 단위·주기·계절조정을 메타 캐시에서 붙인다. yaml의 unit이 있으면 그쪽이 우선 —
    # 사람이 명시한 것을 자동 취득분이 덮어쓰면 안 된다.
    # units=pc1 같은 변환을 걸면 FRED 원단위가 더 이상 맞지 않으므로 그때는 변환 단위를 쓴다.
    try:
        from ..seriesmeta import for_series
        metas = [for_series(sid) for sid in ids]
        metas = [m for m in metas if m]
        if metas and not ind.get("unit"):
            if units == "pc1":
                res["unit"] = "% YoY"
            elif units:
                res["unit"] = f"FRED units={units}"
            else:
                uniq = {m.get("unit", "") for m in metas if m.get("unit")}
                res["unit"] = uniq.pop() if len(uniq) == 1 else " / ".join(sorted(uniq))
        if metas:
            res["frequency"] = "/".join(sorted({m.get("frequency", "") for m in metas if m.get("frequency")}))
            res["seasonal_adjustment"] = "/".join(sorted({m.get("seasonal_adjustment", "") for m in metas if m.get("seasonal_adjustment")}))
    except Exception:
        pass  # 메타는 부가정보다 — 없다고 수집을 실패시키지 않는다
    return res
