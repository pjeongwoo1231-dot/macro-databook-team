"""뉴스 기반 지표 자동 채움 — databook/news.py(다이제스트)가 이미 구현한 네이버 뉴스검색·
Google News 수집 함수를 재사용해, 지금까지 수동 슬롯이던 지정학/정책 지표를 DataBook 표
안에 최신 헤드라인 N건으로 직접 채운다.

원칙(DATA_CONNECTORS.md와 동일): 해석 없음 — 제목·매체·기준일·링크만. 판단은 사람 몫.
"""
from __future__ import annotations

from email.utils import parsedate_to_datetime
from typing import Any

from ..news import _dedupe, _google_news, _naver_news
from .base import result

MAX_HEADLINES = 3


def _is_korean(q: str) -> bool:
    return any("가" <= ch <= "힣" for ch in q)


def _sort_key(row: dict[str, str]):
    try:
        dt = parsedate_to_datetime(row.get("date", ""))
        if dt.tzinfo is None:
            return dt
        return dt.replace(tzinfo=None)
    except Exception:
        from datetime import datetime
        return datetime.min


def _date_str(row: dict[str, str]) -> str:
    try:
        return parsedate_to_datetime(row.get("date", "")).strftime("%Y-%m-%d")
    except Exception:
        return row.get("date", "") or "-"


def fetch_news_indicator(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    queries: list[str] = ind.get("news_queries") or []
    if not queries:
        return result(ind, "fail", error="news_queries 미설정")

    rows: list[dict[str, str]] = []
    for q in queries:
        try:
            rows += _google_news(q, "ko" if _is_korean(q) else "en")
        except Exception:
            pass

    cid = env.get("NAVER_CLIENT_ID", "").strip()
    sec = env.get("NAVER_CLIENT_SECRET", "").strip()
    if cid and sec:
        for q in queries:
            if _is_korean(q):
                try:
                    rows += _naver_news(q, cid, sec)
                except Exception:
                    pass

    rows = [r for r in _dedupe(rows) if r["title"] and not r["title"].startswith("(")]
    if not rows:
        return result(ind, "fail", error="헤드라인 수집 실패(0건) — 쿼리 확인 필요")

    rows.sort(key=_sort_key, reverse=True)

    # 오래된 기사 차단 — 쿼리가 빈약하면 몇 년 전 기사가 최신인 척 지표 슬롯을 채운다.
    # 실제로 1팀 ISM 항목에 2023-02 기사가 앉아 있었다. 옛 기사는 "수치 없음"보다 나쁘다.
    from datetime import datetime, timedelta
    max_age = int(ind.get("news_max_age_days", 60))
    cutoff = datetime.now() - timedelta(days=max_age)
    fresh = [r for r in rows if _sort_key(r) >= cutoff]
    dropped = len(rows) - len(fresh)
    if not fresh:
        return result(ind, "fail",
                      error=f"최근 {max_age}일 내 헤드라인 없음 (가장 최신 {_date_str(rows[0])}) — 쿼리 재검토 필요")
    picked = fresh[:MAX_HEADLINES]

    observations = []
    for r in picked:
        title = r["title"].replace("|", "\\|").replace("[", "(").replace("]", ")")
        link = r.get("link", "")
        value = f"[{title}]({link})" if link.startswith("http") else title
        observations.append({"date": _date_str(r), "value": value, "label": r.get("source") or ""})

    return result(
        ind, "ok", observations=observations,
        source_url="네이버뉴스 · Google News (자동 헤드라인, 판단은 사람 몫)",
        note=(ind.get("note") or "") + (f" · 오래된 기사 {dropped}건 제외({max_age}일 초과)" if dropped else ""),
    )
