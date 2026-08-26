"""유럽 — Eurostat 배포 API(JSON-stat 2.0) · ECB Data Portal(SDMX-JSON). 둘 다 키 불필요.

2026-08-26 실호출 검증 중 확인된 두 가지 파손 지점을 전제로 설계했다.
1) 유로존 집계 코드가 EA20 → EA21로 바뀌었다 (2026-01 불가리아 유로 가입).
   EA20/EA19 계열은 2025-12에서 끊긴다 → geo 필터는 EA21로 고정할 것.
2) HICP는 Eurostat prc_hicp_* 계열과 ECB ICP 계열이 모두 2025-12에서 멈췄다 (2025=100 개편).
   살아 있는 경로는 Eurostat ei_cphi_m (unit=RT12 전년비 / HICP2025 지수)뿐이다.
DBnomics 미러도 같은 파손을 그대로 물려받으므로 유럽 실물지표는 원천 API로 직접 친다.
"""
from __future__ import annotations

import urllib.parse
from typing import Any

from .base import get_json, result

N_OBS = 6
ES_BASE = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data"
ECB_BASE = "https://data-api.ecb.europa.eu/service/data"


def fetch_eurostat(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """Eurostat 배포 API — dataset: 데이터셋 코드, filters: 차원 필터(dict).

    필터는 time을 뺀 모든 차원을 값 1개로 좁혀야 한다(시리즈 1개). 안 좁혀지면
    JSON-stat의 평면 인덱스가 시간축과 어긋나므로 계산하지 않고 실패로 표시한다.
    """
    dataset = ind.get("dataset")
    if not dataset:
        return result(ind, "fail", error="dataset 미지정")
    filters = dict(ind.get("filters") or {})
    n = int(ind.get("n_obs", N_OBS))
    query = urllib.parse.urlencode({"format": "JSON", "lang": "en", **filters, "lastTimePeriod": n})
    url = f"{ES_BASE}/{dataset}?{query}"
    data = get_json(url)

    dims = data.get("dimension", {})
    if "time" not in dims:
        return result(ind, "fail", error=f"time 차원 없음 (데이터셋 코드 확인: {dataset})")
    periods = sorted(dims["time"]["category"]["index"].items(), key=lambda kv: kv[1])
    times = [p for p, _ in periods]
    wide = {k: len(v["category"]["index"]) for k, v in dims.items()
            if k != "time" and len(v["category"]["index"]) != 1}
    if wide:
        return result(ind, "fail", error=f"필터가 시리즈 1개로 안 좁혀짐: {wide}")

    values = data.get("value") or {}
    if not values:
        return result(ind, "fail", error=f"관측치 없음 (필터 조합 미게시 가능성: {filters})")
    label = ind.get("label") or dataset
    obs = []
    for k, v in sorted(values.items(), key=lambda kv: int(kv[0]), reverse=True):
        i = int(k)
        if i >= len(times) or not isinstance(v, (int, float)):
            continue
        obs.append({"date": times[i], "value": round(float(v), 3), "label": label})
    if not obs:
        return result(ind, "fail", error="수치 관측치 없음")
    return result(ind, "ok", observations=obs[:n],
                  source_url=f"https://ec.europa.eu/eurostat/databrowser/view/{dataset}/default/table")


def _ecb_one(key: str, n: int, label: str) -> tuple[list[dict[str, Any]], str]:
    url = f"{ECB_BASE}/{key}?lastNObservations={n}&format=jsondata"
    data = get_json(url)
    series = data["dataSets"][0]["series"]
    if not series:
        raise ValueError("시리즈 없음")
    if len(series) > 1:
        raise ValueError(f"키가 시리즈 {len(series)}개로 확장됨 — 차원을 더 좁힐 것")
    times = [t["id"] for t in data["structure"]["dimensions"]["observation"][0]["values"]]
    obs = []
    for k, v in sorted(list(series.values())[0]["observations"].items(),
                       key=lambda kv: int(kv[0]), reverse=True):
        i = int(k)
        if i >= len(times) or not isinstance(v[0], (int, float)):
            continue
        obs.append({"date": times[i], "value": round(float(v[0]), 3), "label": label})
    return obs, url


def fetch_ecb(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """ECB Data Portal — ecb_key: 'DATASET/SERIES_KEY' (str 또는 리스트). ecb_labels로 라벨 지정."""
    keys = ind.get("ecb_key")
    if not keys:
        return result(ind, "fail", error="ecb_key 미지정")
    if isinstance(keys, str):
        keys = [keys]
    labels = ind.get("ecb_labels") or []
    n = int(ind.get("n_obs", N_OBS))
    all_obs: list[dict[str, Any]] = []
    urls: list[str] = []
    errors: list[str] = []
    for i, key in enumerate(keys):
        label = labels[i] if i < len(labels) else key.split("/")[0]
        try:
            obs, url = _ecb_one(key, n, label)
            if not obs:
                errors.append(f"{key}: 관측치 없음(단종 가능성)")
            all_obs.extend(obs)
            urls.append(url)
        except Exception as e:
            errors.append(f"{key}: {type(e).__name__}: {e}")
    if not all_obs:
        return result(ind, "fail", error="; ".join(errors) or "관측치 없음")
    res = result(ind, "ok", observations=all_obs, source_url=" ".join(urls))
    if errors:
        res["error"] = "; ".join(errors)
    return res
