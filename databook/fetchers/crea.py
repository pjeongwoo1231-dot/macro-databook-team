"""러시아 화석연료 수출수입 — CREA Russia Fossil Tracker.

`https://api.russiafossiltracker.com/v0/counter` 는 2022-02-24 이후 러시아 화석연료 수출의
일별 금액(EUR/USD)과 물량(톤)을 품목군(oil·gas·coal)별로 준다. 제재·유가가 실제로 크렘린
재정에 닿았는지를 보는 유일한 공개 기계판독 계열이라 지정학 축의 종속변수로 쓴다.

주의 둘:
  * **당월은 미완성이다.** 마지막 날짜가 그 달 말일이 아니면 그 달을 버린다 — 안 그러면
    월간 계열의 끝이 항상 급감한 것처럼 보인다.
  * 가격 시나리오가 여러 개 올 수 있다. `pricing_scenario == "default"` 만 쓴다.
"""
from __future__ import annotations

import calendar
from collections import defaultdict
from typing import Any

from .base import get_json, result

API = "https://api.russiafossiltracker.com/v0/counter"
DEFAULT_FROM = "2022-02-24"
_cache: dict[str, dict[str, list[tuple[str, float]]]] = {}

# 시리즈 키 → (품목군, 한국어 라벨). None 은 전 품목 합계.
SERIES = {
    "CREA_RU_FOSSIL_EUR": (None, "화석연료 전체"),
    "CREA_RU_OIL_EUR": ("oil", "원유·석유제품"),
    "CREA_RU_GAS_EUR": ("gas", "가스"),
    "CREA_RU_COAL_EUR": ("coal", "석탄"),
}


def _month_end(day: str) -> bool:
    y, m, d = (int(x) for x in day[:10].split("-"))
    return d >= calendar.monthrange(y, m)[1]


def load_crea_monthly(date_from: str = DEFAULT_FROM) -> dict[str, list[tuple[str, float]]]:
    """월간 수출수입(10억 유로). 시리즈 키 → [(YYYY-MM-01, value)] 오름차순.

    실행당 1회만 받아 캐시한다. 미완성 당월은 제외한다.
    """
    if date_from in _cache:
        return _cache[date_from]
    url = f"{API}?date_from={date_from}&aggregate_by=date,commodity_group&format=json"
    # base.get_json 은 20초 타임아웃·재시도 2회. 전 이력 요청은 느릴 수 있어 재시도를 넉넉히 준다.
    rows = (get_json(url, retries=3) or {}).get("data") or []
    if not rows:
        raise ValueError("CREA counter 응답에 data 없음 — 엔드포인트 변경 가능성")

    last_day = max(r["date"][:10] for r in rows)
    drop_month = None if _month_end(last_day) else last_day[:7]

    acc: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
    for r in rows:
        if r.get("pricing_scenario") not in (None, "", "default"):
            continue
        ym = r["date"][:7]
        if ym == drop_month:
            continue
        val = r.get("value_eur")
        if not isinstance(val, (int, float)):
            continue
        grp = r.get("commodity_group")
        acc["CREA_RU_FOSSIL_EUR"][ym] += float(val)
        for key, (want, _label) in SERIES.items():
            if want and want == grp:
                acc[key][ym] += float(val)

    out = {k: sorted(((f"{ym}-01", v / 1e9) for ym, v in months.items()))
           for k, months in acc.items()}
    _cache[date_from] = out
    return out


def series_labels() -> dict[str, str]:
    return {k: label for k, (_g, label) in SERIES.items()}


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """`run` 용 — crea_series 로 계열 지정, crea_points 로 최근 관측 수(기본 6개월)."""
    keys = ind.get("crea_series", "CREA_RU_FOSSIL_EUR")
    if isinstance(keys, str):
        keys = [keys]
    per = int(ind.get("crea_points", 6))
    try:
        series = load_crea_monthly(ind.get("crea_since", DEFAULT_FROM))
    except Exception as e:
        return result(ind, "fail", error=f"CREA 수집 실패: {type(e).__name__}: {e}")

    labels = series_labels()
    obs: list[dict[str, Any]] = []
    missing: list[str] = []
    for key in keys:
        pts = series.get(key)
        if not pts:
            missing.append(key)
            continue
        for d, v in pts[-per:]:
            obs.append({"date": d, "value": round(v, 2),
                        "label": f"러시아 수출수입 {labels.get(key, key)} (10억 유로/월)"})
    if not obs:
        return result(ind, "fail", error=f"계열 미발견: {', '.join(missing) or keys}")
    obs.sort(key=lambda o: (o["label"], o["date"]), reverse=True)
    return result(ind, "ok", observations=obs,
                  source_url="https://www.russiafossiltracker.com/",
                  note=("당월 미완성분 제외 · 값↑ = 제재에도 크렘린 수입 증가"
                        + (f" · 미발견 계열: {', '.join(missing)}" if missing else "")))
