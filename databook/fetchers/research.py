"""연구기관·싱크탱크 발간물 수집 — 키 불필요, 무료.

왜 필요한가 — 볼트가 승격하는 1차 문헌은 대부분 **이미 나온 뒤에** 발견된다.
발간 시점에 잡으려면 **발간 피드**가 필요하다. 2026-08-19에 주요 소스를 전수 점검했다.

**실측 결과 (2026-08-19)**

| 소스 | 방식 | 상태 |
|---|---|---|
| BIS 중앙은행 총재 연설 | RSS | ✔ 25건 |
| NBER 신규 워킹페이퍼 | RSS | ✔ 42건 |
| 연준 보도자료 | RSS | ✔ 20건 |
| NY Fed Liberty Street | RSS(Atom) | ✔ |
| **CSIS** | **HTML 스크랩** | ✔ — **RSS는 죽었다**(`rss.xml` 최신 항목이 2016-03) |
| PIIE · IMF · Brookings | — | ✘ 404/403 또는 항목 파싱 불가 |

⚠ 한계 (yaml note에도 명시할 것):
- **제목·링크·날짜만 가져온다.** 본문은 별도 판독이 필요하다 —
  볼트 규약상 **읽지 않은 문서를 승격하지 않는다**
- **피드는 큐일 뿐 판정 근거가 아니다.** 제목만 보고 규칙을 만들지 않는다
- HTML 스크랩은 **사이트 개편에 깨진다.** 실패 시 조용히 넘어가지 말고 fail로 남긴다
"""
from __future__ import annotations

import re
import urllib.parse
from typing import Any

from .base import get_text, result

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}

FEEDS = {
    "bis_speeches": ("https://www.bis.org/doclist/cbspeeches.rss", "BIS 중앙은행 총재 연설"),
    "nber_new": ("https://www.nber.org/rss/new.xml", "NBER 신규 워킹페이퍼"),
    "fed_press": ("https://www.federalreserve.gov/feeds/press_all.xml", "연준 보도자료"),
    "liberty_street": ("https://libertystreeteconomics.newyorkfed.org/feed/", "NY Fed Liberty Street"),
    # 2026-08-19 추가. ⚠ 기관 리서치가 아니라 **기고 논평 매체**다 — 저자가 매번 다르고 심사가 없다.
    # 갱신도 느리다(점검 시점 최신 항목이 2026-07-27, 약 3주 전). 지정학 축의 **큐**로만 쓰고
    # 판정 근거로 승격하지 않는다. 볼트 규칙: 등급은 출처가 아니라 근거로.
    "geopolitics": ("https://thegeopolitics.com/feed/", "The Geopolitics (기고 논평)"),
}

SCRAPES = {
    # CSIS: RSS가 2016년에 멈춰 있어 목록 페이지를 긁는다
    "csis": ("https://www.csis.org/analysis", r'href="(/analysis/[a-z0-9\-]+)"', "https://www.csis.org", "CSIS Analysis"),
}

# XML 사이트맵을 목록으로 쓰는 소스 — (사이트맵 URL, 라벨)
# RSS가 죽었거나 커스텀 포스트 타입이라 피드에 안 잡히는 사이트가 여기로 온다.
# 사이트맵은 <loc>과 <lastmod>만 주므로 **제목은 URL 슬러그에서 복원**한다.
SITEMAPS = {
    # politicsgeo.com — 조지아 발간 지정학 계간지 GEOpolitics.
    # ⚠ /feed/ 는 200을 주지만 **item이 0건**이다(기사가 커스텀 타입이라 기본 피드에 안 실린다).
    #   그래서 사이트맵을 쓴다. 2026-08-19 실측: 기사 221건 · 이슈 32호.
    "politicsgeo": ("https://politicsgeo.com/post-sitemap.xml", "GEOpolitics (조지아·남캅카스)"),
}


def _clean(s: str) -> str:
    s = re.sub(r"<!\[CDATA\[|\]\]>", "", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"')
    return re.sub(r"\s+", " ", s).strip()


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """yaml 예시:
        method: scrape
        source: research_feed
        feeds: [bis_speeches, nber_new, fed_press]
        keywords: ["Korea", "semiconductor", "tariff"]   # 있으면 제목 필터
        points: 5                                        # 소스별 최대 건수
    """
    names = ind.get("feeds") or ["bis_speeches"]
    kws = [k.lower() for k in (ind.get("keywords") or [])]
    points = int(ind.get("points") or 5)

    obs: list[dict[str, Any]] = []
    failed: list[str] = []
    for name in names:
        try:
            if name in FEEDS:
                url, label = FEEDS[name]
                raw = get_text(url, headers=UA)
                items = re.findall(r"<(?:item|entry)[ >].*?</(?:item|entry)>", raw, flags=re.S)
                if not items:
                    items = re.split(r"</item>|</entry>", raw)[:-1]
                rows = []
                for it in items:
                    tm = re.search(r"<title[^>]*>(.*?)</title>", it, flags=re.S)
                    dm = re.search(r"<(?:pubDate|updated|published|dc:date)>(.*?)</", it, flags=re.S)
                    if not tm:
                        continue
                    rows.append((_clean(dm.group(1))[:16] if dm else "", _clean(tm.group(1))))
            elif name in SITEMAPS:
                url, label = SITEMAPS[name]
                raw = get_text(url, headers=UA)
                pairs = re.findall(r"<loc>(.*?)</loc>\s*<lastmod>(.*?)</lastmod>", raw, flags=re.S)
                rows = []
                for loc, mod in pairs:
                    slug = loc.rstrip("/").rsplit("/", 1)[-1]
                    if not slug or slug in ("articles-archive", "about-us", "contact-us"):
                        continue
                    title = urllib.parse.unquote(slug).replace("-", " ").strip()
                    rows.append((mod[:10], title))
                rows.sort(key=lambda r: r[0], reverse=True)   # 사이트맵은 시간순이 아니다
            elif name in SCRAPES:
                url, pat, base, label = SCRAPES[name]
                raw = get_text(url, headers=UA)
                seen: list[str] = []
                for href in re.findall(pat, raw):
                    if href not in seen:
                        seen.append(href)
                rows = [("", href.rsplit("/", 1)[-1].replace("-", " ")) for href in seen]
            else:
                failed.append(f"{name}(미등록)")
                continue

            if kws:
                rows = [r for r in rows if any(k in r[1].lower() for k in kws)]
            if not rows:
                failed.append(f"{name}(해당 없음)")
                continue
            for date, title in rows[:points]:
                obs.append({"date": date or "-", "value": 1, "label": f"[{label}] {title[:120]}"})
        except Exception as e:  # 사이트 개편·차단은 조용히 넘기지 않는다
            failed.append(f"{name}({type(e).__name__})")

    if not obs:
        return result(ind, "fail", error=f"수집 실패: {', '.join(failed) or names}")
    err = f"실패: {', '.join(failed)}" if failed else ""
    return result(ind, "ok", observations=obs, source_url="https://www.bis.org/cbspeeches/",
                  unit="건", error=err)
