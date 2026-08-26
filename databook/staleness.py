"""갱신 정지 탐지 — "값이 안 변하는 방식으로 죽은 시리즈"를 자동으로 잡는다.

2026-08 유럽 개편(EA20→EA21, HICP 계열 이전)에서 확인된 실패 모드: 미러(FRED·DBnomics)를
쓰면 단종된 계열도 status=ok에 옛 값이 그대로 실려 조용히 통과한다. 그래서 관측 간격을
데이터에서 직접 추정하고, 최신 관측이 그 간격 대비 지나치게 오래됐으면 stale로 표시한다.
임계는 '중앙 간격 × 2.5 + 10일' — 발표 지연은 통과시키고 분기 이상 정지는 잡는 수준.
"""
from __future__ import annotations

import calendar
import re
from datetime import date, datetime, timezone
from typing import Any

_D = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")
_M = re.compile(r"^(\d{4})[-.](\d{1,2})$")
_Q = re.compile(r"^(\d{4})[-]?Q([1-4])$", re.I)
_W = re.compile(r"^(\d{4})[-]?W(\d{1,2})$", re.I)
_Y = re.compile(r"^(\d{4})$")


def period_end(s: str) -> date | None:
    """관측 라벨을 그 기간의 마지막 날로 변환 — 월간 '2026-07'은 2026-07-31로 본다."""
    s = str(s).strip()
    if m := _D.match(s):
        try:
            return date(int(m[1]), int(m[2]), int(m[3]))
        except ValueError:
            return None
    if m := _M.match(s):
        y, mo = int(m[1]), int(m[2])
        if not 1 <= mo <= 12:
            return None
        return date(y, mo, calendar.monthrange(y, mo)[1])
    if m := _Q.match(s):
        mo = int(m[2]) * 3
        return date(int(m[1]), mo, calendar.monthrange(int(m[1]), mo)[1])
    if m := _W.match(s):
        try:
            return date.fromisocalendar(int(m[1]), int(m[2]), 7)
        except ValueError:
            return None
    if m := _Y.match(s):
        return date(int(m[1]), 12, 31)
    return None


def _median(xs: list[float]) -> float:
    xs = sorted(xs)
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def annotate(results: list[dict[str, Any]], today: date | None = None,
             overrides: dict[str, int] | None = None) -> list[dict[str, Any]]:
    """status=ok 결과에 age_days·gap_days·stale을 붙인다. 판단 불가면 조용히 건너뛴다.

    발표 지연이 구조적으로 긴 지표(케이스-실러는 2개월 지연 발표)는 지표명 → 허용일수로
    overrides를 주거나 indicators.yaml에 max_age_days를 넣어 임계를 따로 정할 수 있다.
    """
    today = today or datetime.now(timezone.utc).date()
    overrides = overrides or {}
    for r in results:
        if r.get("status") != "ok" or not r.get("observations"):
            continue
        by_label: dict[str, list[date]] = {}
        for o in r["observations"]:
            d = period_end(o.get("date", ""))
            if d:
                by_label.setdefault(o.get("label") or "", []).append(d)
        groups = [sorted(v, reverse=True) for v in by_label.values() if len(v) >= 2]
        if not groups:
            continue
        # 가장 오래 밀린 계열 기준 — 다계열 지표에서 한 계열만 죽는 경우를 놓치지 않는다
        worst = max(groups, key=lambda g: (today - g[0]).days)
        age = (today - worst[0]).days
        gap = _median([(worst[i] - worst[i + 1]).days for i in range(len(worst) - 1)]) or 1.0
        limit = overrides.get(r.get("name", "")) or r.get("max_age_days")
        r["age_days"] = age
        r["gap_days"] = round(gap, 1)
        r["stale"] = age > (int(limit) if limit else gap * 2.5 + 10)
    return results
