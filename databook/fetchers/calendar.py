"""경제 캘린더 — FairEconomy(ForexFactory 데이터 파트너)의 무료 공개 JSON.
키 불필요. https://nfs.faireconomy.media/ff_calendar_thisweek.json

`surprise.py`가 "무료 컨센서스가 없다"고 판단해 금리 대리로 우회했던 지점을 다시 확인했다.
결론: 이 엔드포인트는 forecast(컨센서스)·previous는 주지만 **actual은 주지 않는다**
(2026-08-26 확인, 69건 전수 actual 필드 자체가 없음). 하지만 actual은 이미 이 파이프라인이
FRED/BLS로 직접 수집 중이므로, 두 소스를 결합하면 서프라이즈(actual − forecast)가 나온다.
Bloomberg/Refinitiv 패널과 다른 표본이므로 "시장 컨센서스"의 근사치로만 쓸 것.

`thisweek` 하나만 안정적으로 존재한다(`nextweek`는 404, `lastweek`도 404 — 이 미러는 롤링 1주만
제공한다). 그래서 이 파일은 매일 실행 시점의 forecast를 archive에 적립하는 방식으로 쓴다 —
지나간 주의 forecast는 이 엔드포인트에서 복구할 수 없다.
"""
from __future__ import annotations

from typing import Any

from .base import get_json

FF_URL = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"


def fetch_calendar_raw() -> list[dict[str, Any]]:
    """FairEconomy JSON을 그대로 반환. 실패 시 예외를 던진다(호출부가 처리)."""
    data = get_json(FF_URL, headers={"Accept": "application/json"})
    if not isinstance(data, list):
        raise ValueError("예상치 못한 응답 형식 (list가 아님)")
    return data


def fetch_usd_events() -> list[dict[str, Any]]:
    """USD 표시 이벤트만 추린다 — 이 파이프라인이 실제 actual을 갖고 있는 게 미국 지표뿐이라서.
    각 행: title, country, impact, date(ISO, 로컬 오프셋 포함), forecast(원문 문자열), previous(원문 문자열)."""
    rows = fetch_calendar_raw()
    return [r for r in rows if r.get("country") == "USD"]
