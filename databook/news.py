"""뉴스·이벤트 수집 모듈 (Phase 1.5) — macro-databook 드롭인.

배치 위치: databook/news.py  (render.py·core.py와 같은 레벨)
실행: python -m databook.news        (Data Book과 별개로 뉴스 다이제스트만 생성)

원칙:
- 본문 스크래핑 금지. RSS/뉴스 API가 주는 제목·매체·날짜·링크만.
- 판단 없음(해석 금지) — 취사선택도 없음. 각 소스가 주는 한도까지 전량 수집해 전부 기록한다.
  (사람이든 AI든 "몇 개만 골라오기"는 그 자체로 편향 주입이므로 금지 — 필터링은 소스단이 아니라
  독자가 다이제스트를 읽을 때 스스로 한다)
- 외부 의존성 없음(stdlib urllib + xml.etree). feedparser 있으면 자동 사용(더 견고).
- 실패 격리: 소스 하나가 죽어도 전체는 완주.

출력: <OUTPUT_DIR>/Macro/_News/NewsDigest_YYYY-MM-DD.md
      OBSIDIAN_VAULT_PATH 설정 시 vault에도 동일 저장 (render.py와 동일 패턴).
"""
from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

try:
    from .core import OUTPUT_DIR, load_env
except ImportError:  # 단독 실행/테스트 폴백
    OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

    def load_env() -> dict[str, str]:
        import os
        return {"OBSIDIAN_VAULT_PATH": os.environ.get("OBSIDIAN_VAULT_PATH", ""),
                "TEAM_VAULT_PATH": os.environ.get("TEAM_VAULT_PATH", "")}

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
TIMEOUT = 20
# 쿼리당 최대 헤드라인 — "취사선택 없음" 원칙상 각 소스가 허용하는 실제 상한까지 끌어온다.
# (2026-07-19: 기존 15는 임의 상한이었음 — 사용자 지적으로 소스별 진짜 한도로 상향)
RSS_MAX = 100        # Google News/고정 RSS — feedparser가 주는 만큼(대개 100건 내외), 인위적 컷 최소화
GDELT_MAXRECORDS = 250  # GDELT ArtList 모드 공식 상한
NAVER_DISPLAY = 100      # 네이버 뉴스검색 API 공식 상한(display 파라미터 최대값)

# ───────────────────────── 설정 (여기만 수정하면 됨) ─────────────────────────
# 팀별 Google News RSS 키워드 쿼리. (q, lang) — lang: en=글로벌, ko=한국
TEAM_QUERIES: dict[str, list[tuple[str, str]]] = {
    "team_1": [("US jobs report OR GDP OR ISM PMI OR recession", "en"),
               ("한국 수출 OR 고용 OR 경기", "ko"),
               ("China economy growth", "en"),
               ("中国 经济 增长 OR 制造业 PMI", "zh"),
               ("日本 景気 OR GDP OR 鉱工業生産", "ja")],
    "team_2": [("Fed FOMC OR rate cut OR CPI inflation", "en"),
               ("한국은행 기준금리 OR 물가", "ko"),
               ("ECB OR BOJ policy rate", "en"),
               ("日銀 金融政策 OR 物価 OR 賃上げ", "ja"),
               ("中国 央行 OR LPR OR 物价", "zh")],
    "team_3": [("credit spreads OR liquidity OR dollar DXY", "en"),
               ("crypto bitcoin ETF OR stablecoin regulation", "en"),
               ("private credit OR CRE commercial real estate stress", "en"),
               ("외국인 수급 OR 원달러 환율", "ko")],
    "team_4": [("Middle East oil OR OPEC OR Russia Ukraine sanctions", "en"),
               ("US China tariff OR export controls OR trade war", "en"),
               ("中国 出口 OR 关税 OR 稀土", "zh"),
               ("日本 貿易統計 OR 輸出", "ja"),
               ("Taiwan strait OR North Korea", "en"),
               ("중동 유가 OR 지정학 OR 관세", "ko")],
}
TEAM_TITLE = {
    "team_1": "1팀 성장·경기", "team_2": "2팀 물가·정책·금리",
    "team_3": "3팀 유동성·신용·심리", "team_4": "4팀 글로벌·지정학·무역",
}
# 팀 4 지정학은 GDELT(이벤트 DB)도 병행
GDELT_QUERIES: dict[str, list[str]] = {
    "team_4": ["(sanctions OR tariff OR OPEC OR strait) sourcelang:english"],
}
# 네이버 뉴스 검색 API (한국어 뉴스 보강) — NAVER_CLIENT_ID/SECRET 있을 때만 작동, 없으면 자동 skip.
# Google News RSS는 한국 로컬 매체 커버가 약해, 국내 경제·정책 기사를 네이버로 두껍게 채운다.
NAVER_QUERIES: dict[str, list[str]] = {
    "team_1": ["한국 수출 반도체", "국내 고용 경기", "산업생산 소비"],
    "team_2": ["한국은행 기준금리", "소비자물가 CPI", "국고채 금리"],
    "team_3": ["원달러 환율", "외국인 순매수 코스피", "가계부채 신용"],
    "team_4": ["중동 유가 지정학", "미중 관세 무역", "방산 수출 조선 수주"],
}
# 고정 RSS 피드 (원문 이벤트 + 전문 분석) — team 태그. 전부 HTTP 200 확인됨(2026-07-17).
# 국제정세 싱크탱크·전문매체를 의도적으로 성향이 다른 곳까지 섞었다 — 뉴스 하나만
# 보면 편향되지만, 여러 소스를 무차별로 모으면 편향이 상쇄된다는 게 이 학회 뉴스
# 모듈의 설계 원칙이다 (매파 성향 vs 반개입주의 성향을 같이 넣은 것도 그래서다).
FIXED_FEEDS: list[tuple[str, str, str]] = [
    ("team_2", "Fed 보도자료", "https://www.federalreserve.gov/feeds/press_all.xml"),
    # 국제정세 종합 (중도·주류)
    ("team_4", "Foreign Affairs", "https://www.foreignaffairs.com/rss.xml"),
    ("team_4", "Foreign Policy", "https://foreignpolicy.com/feed/"),
    # 안보·전략 (다소 매파적 관점)
    ("team_4", "Atlantic Council", "https://www.atlanticcouncil.org/feed/"),
    ("team_4", "CSIS", "https://www.csis.org/rss.xml"),
    # 반개입주의·restraint 관점 (위 매파 시각의 균형추)
    ("team_4", "Responsible Statecraft", "https://responsiblestatecraft.org/feed/"),
    # 지역 전문 (아시아태평양 — 한중일·대만해협에 특화)
    ("team_4", "The Diplomat", "https://thediplomat.com/feed/"),
    ("team_4", "Lowy Institute", "https://www.lowyinstitute.org/the-interpreter/rss.xml"),
    # 북한 전문 (한국 학회 직결)
    ("team_4", "38 North", "https://www.38north.org/feed/"),
    ("team_4", "NK News", "https://www.nknews.org/feed/"),
    # 에너지·원자재 지정학
    ("team_4", "OilPrice.com", "https://oilprice.com/rss/main"),
    # Brookings 직접 피드는 봇에게 HTML을 반환 — Google News 사이트 한정 RSS로 우회
    ("team_4", "Brookings", "https://news.google.com/rss/search?q=site:brookings.edu&hl=en-US&gl=US&ceid=US:en"),
    # ── 각국 자국 매체 (그 나라 정부·여론이 스스로를 어떻게 말하는지) ──
    ("team_4", "Al Jazeera", "https://www.aljazeera.com/xml/rss/all.xml"),          # 카타르·범아랍권 시각
    ("team_4", "Global Times (China)", "https://www.globaltimes.cn/rss/outbrain.xml"),  # 중국 국영, 대외선전 톤
    ("team_4", "CGTN (China)", "https://www.cgtn.com/subscribe/rss/section/world.xml"),  # 중국 국영
    ("team_4", "TASS (Russia)", "https://tass.ru/rss/v2.xml"),                      # 러시아 국영
    ("team_4", "RT (Russia)", "https://www.rt.com/rss/"),                           # 러시아 국영
    ("team_4", "Moscow Times", "https://www.themoscowtimes.com/rss/news"),          # 러시아 독립·망명 매체 — 위 RT/TASS의 균형추
    ("team_4", "Japan Times", "https://www.japantimes.co.jp/feed/"),                # 일본, 영어
    ("team_4", "NHK", "https://www3.nhk.or.jp/rss/news/cat0.xml"),                  # 일본 공영, 일본어 원문
    ("team_4", "Times of India", "https://timesofindia.indiatimes.com/rssfeeds/296589292.cms"),  # 인도
    ("team_4", "Anadolu Agency (Turkey)", "https://www.aa.com.tr/en/rss/default?cat=guncel"),  # 튀르키예 국영
    ("team_4", "AllAfrica", "https://allafrica.com/tools/headlines/rdf/latest/headlines.rdf"),  # 범아프리카 — 약소국 시각 커버
    ("team_4", "Jerusalem Post", "https://www.jpost.com/rss/rssfeedsfrontpage.aspx"),  # 이스라엘 (중도우파)
    ("team_4", "Haaretz", "https://news.google.com/rss/search?q=site:haaretz.com&hl=en-US&gl=US&ceid=US:en"),  # 이스라엘 — 좌파·비판적, JPost 균형추. 직접 피드는 봇월이 HTML 반환하여 Google News 우회
    ("team_4", "+972 Magazine", "https://www.972mag.com/feed/"),                     # 이스라엘-팔레스타인, 더 비판적인 독립매체
    ("team_4", "Straits Times", "https://news.google.com/rss/search?q=site:straitstimes.com&hl=en-US&gl=US&ceid=US:en"),  # 싱가포르·동남아 시각. 직접 피드는 간헐적 봇월 — Google News 우회
    # ── 위 국영매체(Global Times·CGTN·TASS·RT)의 반대편 시각 ──
    ("team_4", "Radio Free Asia (Mandarin)", "https://www.rfa.org/mandarin/rss2.xml"),  # 중국어 원문, 반체제·서방자금, 중국 내 차단
    ("team_4", "Hong Kong Free Press", "https://hongkongfp.com/feed/"),              # 홍콩 독립매체, 베이징 비판적
    ("team_4", "Taipei Times", "https://www.taipeitimes.com/xml/index.rss"),         # 대만 시각의 양안·중국 문제
    ("team_4", "Meduza (Russia)", "https://meduza.io/rss/en/all"),                   # 러시아 독립매체, 라트비아 기반, 러시아 내 금지
    # ── 중앙아시아·코카서스 (4팀 담당 지역인데 기존엔 커버 없었음) ──
    ("team_4", "EurasiaNet", "https://eurasianet.org/rss"),                          # 중앙아시아+코카서스 전문
    ("team_4", "Astana Times (Kazakhstan)", "https://astanatimes.com/feed/"),        # 카자흐스탄 자체 매체
    # ── 걸프 국가 (카타르는 Al Jazeera로 이미 커버, 사우디 추가) ──
    ("team_4", "Arab News (Saudi Arabia)", "https://www.arabnews.com/rss.xml"),
    # ── 중남미 (기존엔 커버 없었음) ──
    ("team_4", "MercoPress", "https://en.mercopress.com/rss/"),                      # 남미 지역 전문, 영어
    ("team_4", "Folha de S.Paulo (Brazil)", "https://feeds.folha.uol.com.br/mundo/rss091.xml"),  # 브라질 최대지, 포르투갈어 원문
    ("team_4", "Buenos Aires Herald (Argentina)", "https://buenosairesherald.com/feed"),
    ("team_4", "Infobae (Argentina)", "https://www.infobae.com/arc/outboundfeeds/rss/"),  # 아르헨티나 최대 독자층, 스페인어 원문
    ("team_4", "Andina (Peru)", "https://andina.pe/ingles/rss/"),                    # 페루 국영
    ("team_4", "Prensa Latina (Cuba)", "https://www.prensa-latina.cu/feed"),         # 쿠바 국영 — 좌파 라틴아메리카 시각, 위 매체들의 균형추
    # ── 아프리카 심화 (프랑스의 아프리카 광산 이권 상실 등 사헬·자원 이슈 커버) ──
    ("team_4", "The Africa Report", "https://www.theafricareport.com/feed/"),        # 범아프리카, 정치·경제 심층
    ("team_4", "African Business", "https://african.business/feed"),                 # 범아프리카 경제
    ("team_4", "Premium Times (Nigeria)", "https://www.premiumtimesng.com/feed"),
    ("team_4", "Daily Maverick (South Africa)", "https://www.dailymaverick.co.za/rss/"),
    ("team_4", "RFI Afrique", "https://www.rfi.fr/fr/afrique/rss"),                  # 프랑스어 원문 — 사헬·프랑스 광산이권 이슈에 최적
    ("team_4", "Jeune Afrique", "https://www.jeuneafrique.com/feed/"),               # 프랑스어권 아프리카 정치·자원 최고 권위지
    # ── 북유럽 (기존엔 커버 없었음) ──
    ("team_4", "The Local Sweden", "https://www.thelocal.se/feeds/rss.php"),         # 영어
    ("team_4", "Aftenposten (Norway)", "https://www.aftenposten.no/rss"),            # 노르웨이어 원문
    ("team_4", "DR Nyheder (Denmark)", "https://www.dr.dk/nyheder/service/feeds/allenyheder"),  # 덴마크어 원문
    ("team_4", "SVT (Sweden)", "https://www.svt.se/nyheter/rss.xml"),                # 스웨덴어 원문, 공영
    ("team_4", "Helsingin Sanomat (Finland)", "https://www.hs.fi/rss/tuoreimmat.xml"),  # 핀란드어 원문, 최대지
    # ── EU 정책 (개별국이 아니라 EU 전체 정책 시각) ──
    ("team_4", "Politico Europe", "https://www.politico.eu/feed/"),
    ("team_4", "Euractiv", "https://news.google.com/rss/search?q=site:euractiv.com&hl=en-US&gl=US&ceid=US:en"),  # 직접 피드는 파이썬 요청에 403 — Google News 우회
    ("team_4", "EU Observer", "https://euobserver.com/rss"),
    # ── 동유럽 (기존엔 커버 없었음) ──
    ("team_4", "Notes from Poland", "https://notesfrompoland.com/feed/"),
    ("team_4", "Kyiv Post", "https://www.kyivpost.com/feed"),                        # 우크라이나
    ("team_4", "Balkan Insight", "https://balkaninsight.com/feed/"),                 # 발칸반도
    # ── OSINT 검증 매체 (주장을 공개출처로 교차검증) ──
    ("team_4", "Bellingcat", "https://www.bellingcat.com/feed/"),
    # 필요 시 ECB·BOK·언론 RSS·Substack RSS를 (team, 이름, url)로 추가
]
# ─────────────────────────────────────────────────────────────────────────────


def _get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.read()


def _norm(t: str) -> str:
    return re.sub(r"\s+", " ", (t or "")).strip()


def _parse_feed(raw: bytes, default_source: str = "") -> list[dict[str, str]]:
    """RSS 2.0 / Atom 최소 파서 (feedparser 없을 때 폴백)."""
    out: list[dict[str, str]] = []
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        return out
    # RSS 2.0: channel/item
    for item in root.iter("item"):
        title = _norm(item.findtext("title"))
        link = _norm(item.findtext("link"))
        date = _norm(item.findtext("pubDate"))
        src_el = item.find("source")
        source = _norm(src_el.text) if src_el is not None else default_source
        if title:
            out.append({"title": title, "link": link, "date": date, "source": source})
    if out:
        return out
    # Atom: entry
    ns = {"a": "http://www.w3.org/2005/Atom"}
    for entry in root.iter("{http://www.w3.org/2005/Atom}entry"):
        title = _norm(entry.findtext("a:title", namespaces=ns))
        link_el = entry.find("a:link", ns)
        link = link_el.get("href") if link_el is not None else ""
        date = _norm(entry.findtext("a:updated", namespaces=ns))
        if title:
            out.append({"title": title, "link": link, "date": date, "source": default_source})
    return out


def _fetch_feed(url: str, default_source: str = "") -> list[dict[str, str]]:
    try:
        raw = _get(url)
    except Exception as e:  # 실패 격리
        return [{"title": f"(수집 실패: {type(e).__name__})", "link": "", "date": "", "source": default_source}]
    try:
        import feedparser  # 있으면 더 견고
        feed = feedparser.parse(raw)
        rows = []
        for e in feed.entries[:RSS_MAX]:
            rows.append({
                "title": _norm(getattr(e, "title", "")),
                "link": getattr(e, "link", ""),
                "date": _norm(getattr(e, "published", "") or getattr(e, "updated", "")),
                "source": _norm(getattr(getattr(e, "source", None), "title", "")) or default_source,
            })
        return [r for r in rows if r["title"]]
    except ImportError:
        return _parse_feed(raw, default_source)[:RSS_MAX]


def _google_news(query: str, lang: str) -> list[dict[str, str]]:
    # 원어 우선 규칙(AGENTS.md) — 그 나라 기사는 그 나라 언어로 검색해야 잡힌다.
    # 영어 쿼리만 쓰면 현지 매체가 통째로 빠진다(중국 재경·일경 등).
    _LOC = {
        "ko": ("ko", "KR", "KR:ko"),
        "ja": ("ja", "JP", "JP:ja"),
        "zh": ("zh-CN", "CN", "CN:zh-Hans"),
        "en": ("en-US", "US", "US:en"),
    }
    hl, gl, ceid = _LOC.get(lang, _LOC["en"])
    q = urllib.parse.quote(query)
    url = f"https://news.google.com/rss/search?q={q}&hl={hl}&gl={gl}&ceid={ceid}"
    return _fetch_feed(url)


def _gdelt(query: str) -> list[dict[str, str]]:
    q = urllib.parse.quote(query)
    url = (f"https://api.gdeltproject.org/api/v2/doc/doc?query={q}"
           f"&mode=ArtList&maxrecords={GDELT_MAXRECORDS}&timespan=7d&format=json&sort=DateDesc")
    try:
        data = json.loads(_get(url).decode("utf-8", "replace"))
    except Exception as e:
        return [{"title": f"(GDELT 실패: {type(e).__name__})", "link": "", "date": "", "source": "GDELT"}]
    rows = []
    for a in data.get("articles", [])[:GDELT_MAXRECORDS]:
        rows.append({"title": _norm(a.get("title")), "link": a.get("url", ""),
                     "date": a.get("seendate", ""), "source": a.get("domain", "") or "GDELT"})
    return [r for r in rows if r["title"]]


def _unescape(s: str) -> str:
    """네이버 응답의 HTML 엔티티 해제 후 <b> 강조태그 제거 (리터럴·이스케이프 모두 처리)."""
    s = s or ""
    for a, b in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&#39;", "'"), ("&apos;", "'")):
        s = s.replace(a, b)
    s = re.sub(r"</?b>", "", s)
    return _norm(s)


def _naver_news(query: str, cid: str, sec: str) -> list[dict[str, str]]:
    """네이버 뉴스 검색 API — 최신순 헤드라인. 인증/네트워크 실패는 격리."""
    url = ("https://openapi.naver.com/v1/search/news.json?"
           + urllib.parse.urlencode({"query": query, "display": NAVER_DISPLAY, "sort": "date"}))
    req = urllib.request.Request(url, headers={
        "X-Naver-Client-Id": cid, "X-Naver-Client-Secret": sec, "User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            data = json.loads(r.read().decode("utf-8", "replace"))
    except Exception as e:
        code = getattr(e, "code", "")
        return [{"title": f"(네이버 수집 실패: {type(e).__name__} {code})", "link": "", "date": "", "source": "네이버뉴스"}]
    rows = []
    for it in data.get("items", []):
        rows.append({
            "title": _unescape(it.get("title", "")),
            "link": it.get("originallink") or it.get("link", ""),
            "date": _norm(it.get("pubDate", "")),
            "source": "네이버뉴스",
        })
    return [r for r in rows if r["title"]]


def _dedupe(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[str] = set()
    out = []
    for r in rows:
        key = re.sub(r"[^\w가-힣]", "", r["title"].lower())[:60]
        if key and key not in seen:
            seen.add(key)
            out.append(r)
    return out


def collect(env: dict[str, str] | None = None) -> dict[str, list[dict[str, str]]]:
    env = env or {}
    by_team: dict[str, list[dict[str, str]]] = {t: [] for t in TEAM_QUERIES}
    for team, queries in TEAM_QUERIES.items():
        for q, lang in queries:
            by_team[team] += _google_news(q, lang)
    for team, queries in GDELT_QUERIES.items():
        for q in queries:
            by_team.setdefault(team, [])
            by_team[team] += _gdelt(q)
    # 네이버 뉴스 검색 — 개발자센터 검색 API 키(X-Naver-Client-Id/Secret)가 있을 때만.
    cid = env.get("NAVER_CLIENT_ID", "").strip()
    sec = env.get("NAVER_CLIENT_SECRET", "").strip()
    if cid and sec:
        for team, queries in NAVER_QUERIES.items():
            by_team.setdefault(team, [])
            for q in queries:
                by_team[team] += _naver_news(q, cid, sec)
    for team, name, url in FIXED_FEEDS:
        by_team.setdefault(team, [])
        by_team[team] += _fetch_feed(url, name)
    return {t: _dedupe(rows) for t, rows in by_team.items()}


def _esc(s: str) -> str:
    return _norm(s).replace("|", "\\|")


def render_digest(by_team: dict[str, list[dict[str, str]]], run_ts: str) -> str:
    date_str = run_ts[:10]
    total = sum(len(v) for v in by_team.values())
    lines = [
        "---", f"date: {date_str}", "type: news-digest",
        f"collected_utc: {run_ts}", "tags: [macro/news]", "---", "",
        f"# 뉴스·이벤트 다이제스트 — {date_str}", "",
        f"> [!summary] 헤드라인 {total}건 (RSS·GDELT·네이버, 취사선택 없이 전량) — {run_ts} (UTC)",
        "> 해석 없음, 사전 필터링 없음 — 제목·매체·날짜·링크만 소스 상한까지 전부 수집. "
        "4팀 이벤트캘린더·무효화트리거·주간스캔 작성 시 참고자료로 활용.",
        f"> 같은 날 수치: [[DataBook_{date_str}]] · 지표 노드: [[DataBook 지표 소환]]", "",
    ]
    for team in ("team_1", "team_2", "team_3", "team_4"):
        rows = by_team.get(team, [])
        lines += [f"## {TEAM_TITLE[team]} ({len(rows)})", "",
                  "| 제목 | 매체 | 날짜 | 링크 |", "|---|---|---|---|"]
        for r in rows:
            link = f"[열기]({r['link']})" if r["link"].startswith("http") else "—"
            lines.append(f"| {_esc(r['title'])} | {_esc(r['source']) or '—'} | {_esc(r['date']) or '—'} | {link} |")
        lines.append("")
    return "\n".join(lines)


def write_digest(content: str, run_ts: str, env: dict[str, str]) -> list[Path]:
    rel = f"_News/NewsDigest_{run_ts[:10]}.md"
    # 로컬 output/은 "Macro/"(이 프로젝트 자체 관례), 실제 Obsidian vault는 "04_DataBook/"(vault 관례).
    targets: list[tuple[Path, str]] = [(OUTPUT_DIR, "Macro")]
    vault = (env or {}).get("OBSIDIAN_VAULT_PATH", "").strip().strip('"')
    # 팀 볼트에도 같이 쓴다 — render.py와 동일 규칙
    team = (env or {}).get("TEAM_VAULT_PATH", "").strip().strip('"')
    if team and team != vault:
        targets.append((Path(team), "04_DataBook"))
    if vault:
        targets.append((Path(vault), "04_DataBook"))
    written = []
    for root, prefix in targets:
        path = root / prefix / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        written.append(path)
    return written


def run_news(env: dict[str, str] | None = None) -> list[Path]:
    env = env or load_env()
    run_ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    by_team = collect(env)
    content = render_digest(by_team, run_ts)
    paths = write_digest(content, run_ts, env)
    n = sum(len(v) for v in by_team.values())
    print(f"뉴스 다이제스트 생성: {n}건 → " + " · ".join(str(p) for p in paths))
    return paths


if __name__ == "__main__":
    run_news()
