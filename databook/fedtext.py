"""FOMC 성명서 코퍼스 — 중앙은행 커뮤니케이션 텍스트 분석용.

Crayton(2018)이 FOMC 성명서를 NMF 토픽모델링해 **수익률곡선의 곡률**과 연결한 방법론을
직접 돌려보려면 먼저 코퍼스가 있어야 한다. 이 모듈은 **수집까지만** 한다.
모델링(토픽 추출·회귀)은 별도 분석 스크립트의 몫이다.

수집 대상
- 1999년 이후 정례회의 직후 성명서 (`/newsevents/pressreleases/monetary{YYYYMMDD}a.htm`)
- 최근 ~5년은 `fomccalendars.htm`, 그 이전은 연도별 `fomchistorical{YYYY}.htm`에서 링크를 모은다

산출물 (`output/fedtext/`)
- `statements/{YYYYMMDD}.txt` — 본문 텍스트 (증분: 이미 있으면 건너뛴다)
- `index.csv` — 날짜 · 글자수 · 단어수 · URL

주의
- **성명서와 의사록(minutes)은 다르다.** 의사록은 3주 뒤 공개되므로 이벤트 시점이 어긋난다.
  이 모듈은 **성명서만** 받는다
- 본문 추출은 HTML 구조에 의존한다. 연도별로 마크업이 달라 실패할 수 있으므로
  글자수가 비정상적으로 짧은 건은 `index.csv`에서 걸러 볼 것
"""
from __future__ import annotations

import csv
import re
import urllib.request
from datetime import date
from pathlib import Path

from .core import OUTPUT_DIR
from .fetchers.base import BROWSER_UA, throttle

FED = "https://www.federalreserve.gov"
TEXT_DIR = OUTPUT_DIR / "fedtext"
STMT_DIR = TEXT_DIR / "statements"
LINK_RE = re.compile(r"/newsevents/pressreleases/monetary(\d{8})a\.htm")

# 본문만 남기기 위해 통째로 지울 블록
STRIP_BLOCKS = re.compile(
    r"<(script|style|nav|header|footer|form)\b.*?</\1>", re.S | re.I)


def _get(url: str) -> str:
    throttle("www.federalreserve.gov", 0.5)
    req = urllib.request.Request(url, headers={"User-Agent": BROWSER_UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


MEETING_RE = re.compile(r"/monetarypolicy/files/FOMC(\d{8})meeting\.pdf")


def list_dates(since_year: int = 1999) -> dict[str, str]:
    """YYYYMMDD → 성명서 URL.

    URL 체계가 2011년을 전후로 다르다.
    - 2011~ : `/newsevents/pressreleases/monetary{YYYYMMDD}a.htm`
    - ~2010 : `/boarddocs/press/monetary/{YYYY}/{YYYYMMDD}/default.htm`
    구형 구간은 연도별 historical 페이지가 성명서를 직접 링크하지 않으므로
    회의자료 PDF 링크(`FOMC{YYYYMMDD}meeting.pdf`)에서 **회의 날짜를 얻어** URL을 조립한다.
    """
    out: dict[str, str] = {}
    this_year = date.today().year
    try:
        html = _get(f"{FED}/monetarypolicy/fomccalendars.htm")
        for d in LINK_RE.findall(html):
            if int(d[:4]) >= since_year:
                out[d] = f"{FED}/newsevents/pressreleases/monetary{d}a.htm"
    except Exception:
        pass

    for y in range(since_year, this_year - 4):
        try:
            html = _get(f"{FED}/monetarypolicy/fomchistorical{y}.htm")
        except Exception:
            continue
        for d in LINK_RE.findall(html):          # 신형 링크가 있으면 그대로
            if int(d[:4]) >= since_year:
                out.setdefault(d, f"{FED}/newsevents/pressreleases/monetary{d}a.htm")
        for d in MEETING_RE.findall(html):       # 구형: 회의일에서 조립
            if int(d[:4]) >= since_year and d not in out:
                out[d] = ""                      # URL은 candidates()가 순차 시도
    return out


def candidates(d: str) -> list[str]:
    """성명서 URL 체계가 시대별로 세 가지다. 오래된 것부터 순서대로 시도한다.

    - 2011~      `/newsevents/pressreleases/monetary{YYYYMMDD}a.htm`
    - 2006~2010  `/newsevents/press/monetary/{YYYYMMDD}a.htm`
    - ~2005      `/boarddocs/press/monetary/{YYYY}/{YYYYMMDD}/default.htm`
                 (1999~2001은 `general`)
    회의가 이틀이면 성명서는 **둘째 날**에 나오므로 +1일도 함께 시도한다.
    """
    from datetime import datetime, timedelta
    days = [d]
    try:
        days.append((datetime.strptime(d, "%Y%m%d") + timedelta(days=1)).strftime("%Y%m%d"))
    except ValueError:
        pass
    urls: list[str] = []
    for x in days:
        y = x[:4]
        urls += [
            f"{FED}/newsevents/pressreleases/monetary{x}a.htm",
            f"{FED}/newsevents/press/monetary/{x}a.htm",
            f"{FED}/boarddocs/press/monetary/{y}/{x}/default.htm",
            f"{FED}/boarddocs/press/general/{y}/{x}/default.htm",
        ]
    return urls


def extract_text(html: str) -> str:
    html = STRIP_BLOCKS.sub(" ", html)
    # 본문 영역이 있으면 그 안만
    m = re.search(r'<div[^>]*class="[^"]*col-xs-12[^"]*"[^>]*>(.*?)</div>\s*</div>', html, re.S)
    body = m.group(1) if m else html
    body = re.sub(r"<[^>]+>", " ", body)
    body = (body.replace("&nbsp;", " ").replace("&amp;", "&")
                .replace("&#39;", "'").replace("&quot;", '"')
                .replace("&ldquo;", '"').replace("&rdquo;", '"'))
    return re.sub(r"\s+", " ", body).strip()


def collect(since_year: int = 1999, dry_run: bool = False) -> int:
    print(f"FOMC 성명서 코퍼스 — {since_year}년 이후")
    try:
        dates = list_dates(since_year)
    except Exception as e:
        print(f"  [FAIL] 링크 수집: {type(e).__name__}: {e}")
        return 1
    print(f"  링크 {len(dates)}건 ({min(dates) if dates else '-'} ~ {max(dates) if dates else '-'})")
    if dry_run:
        return 0

    STMT_DIR.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    new = skipped = failed = 0
    for i, (d, url) in enumerate(sorted(dates.items()), 1):
        f = STMT_DIR / f"{d}.txt"
        if f.exists() and f.stat().st_size > 200:
            txt = f.read_text(encoding="utf-8")
            skipped += 1
        else:
            txt = ""
            tried = [url] if url else []
            tried += [u for u in candidates(d) if u != url]
            for u in tried:
                try:
                    cand = extract_text(_get(u))
                except Exception:
                    continue
                if len(cand) >= 200:      # 마크업이 달라 본문을 못 잡은 경우 다음 후보로
                    txt, url = cand, u
                    break
            if not txt:
                failed += 1
                continue
            f.write_text(txt, encoding="utf-8")
            new += 1
        rows.append({"date": f"{d[:4]}-{d[4:6]}-{d[6:]}", "chars": len(txt),
                     "words": len(txt.split()), "url": url})
        if i % 40 == 0:
            print(f"    {i}/{len(dates)} …")

    idx = TEXT_DIR / "index.csv"
    with idx.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["date", "chars", "words", "url"])
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: str(r["date"])))

    if rows:
        wc = sorted(int(r["words"]) for r in rows)  # type: ignore[arg-type]
        print(f"\n완료: 신규 {new} · 기존 {skipped} · 실패 {failed} · 총 {len(rows)}건")
        print(f"  단어수 중앙값 {wc[len(wc) // 2]} (최소 {wc[0]} / 최대 {wc[-1]})")
        print(f"  → {STMT_DIR}")
        print(f"  → {idx}")
        print("\n⚠ 단어수가 유난히 짧은 건은 본문 추출 실패 가능성 — index.csv에서 확인할 것.")
    return 0
