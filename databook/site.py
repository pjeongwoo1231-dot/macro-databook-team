"""시황 사이트 생성 — 매일 도는 수집 결과를 정적 HTML로 굳힌다.

**왜 필요한가** — `run`은 그날의 마크다운을 볼트에 쓴다. 그건 읽기 좋지만
**과거와 나란히 놓고 보기 어렵고**, 링크로 공유할 수도 없다.
이 모듈은 같은 데이터를 **정적 사이트**로 뱉는다 — 서버도 DB도 없고,
`site/` 폴더를 그대로 GitHub Pages·Netlify에 올리면 끝난다.

구조
- `index.html`      오늘 4축 대시보드 (성장·물가금리·유동성신용·지정학) + 한국
- `axis-*.html`     축별 전 지표 — 백분위 스파인 + 계열별 스파크라인
- `archive.html`    날짜별 목록
- `d/{날짜}.html`   그날의 스냅샷 — **매일 하나씩 쌓인다**

**축적 방식**: `output/snapshot_{날짜}.json`이 이미 날짜별로 쌓이고 있다.
이 모듈은 그 전부를 훑어 아카이브를 만든다 — 과거 파일이 남아 있는 한 소급 생성된다.

⚠ 백분위는 **각 계열 자체 표본** 기준이다(대부분 2016년 이후, 일부는 2000년/2023년).
표본 구간이 다른 지표를 나란히 놓고 "누가 더 극단인가"를 말하면 틀린다 — 각 카드에 표본 시작을 적는다.
⚠ 히스토리 CSV가 없는 계열은 **백분위 없이 값만** 보여준다. 없는 걸 추정하지 않는다.
"""
from __future__ import annotations

import csv
import io
import json
import shutil
import statistics as st
from datetime import datetime
from pathlib import Path
from typing import Any

from .core import OUTPUT_DIR

SITE = OUTPUT_DIR / "site"
HIST = OUTPUT_DIR / "history"
TOSS = HIST / "toss"

AXES = {
    "growth": ("성장", "team_1", "실물은 버티는가, 심리는 어디인가"),
    "rates": ("물가 · 금리", "team_2", "물가와 금리가 같은 말을 하는가"),
    "liquidity": ("유동성 · 신용", "team_3", "가격이 느슨해도 수량은 조일 수 있다"),
    "geo": ("지정학 · 무역", "team_4", "에너지와 전략광물의 자리"),
}

# 축별 대표 계열 — (history CSV id, 표시명, 단위, 방향) 방향: hot=높을수록 과열/긴축, cold=낮을수록
SPINE = {
    "growth": [("INDPRO", "산업생산", "", "hot"), ("GDPNOW", "GDPNow", "%", "hot"),
               ("HG_F", "구리", "$/lb", "hot"), ("WEI", "주간경제지수", "", "hot"),
               ("JTSJOL", "JOLTS 구인", "천건", "mid"), ("UNRATE", "실업률", "%", "mid"),
               ("ICSA", "신규 실업수당", "건", "mid"), ("PAYEMS", "비농업 고용", "천명", "hot"),
               ("SAHMREALTIME", "Sahm Rule", "%p", "mid"),
               ("TEMPHELPS", "임시직 고용", "천명", "cold"), ("ISRATIO", "재고/판매", "", "cold"),
               ("UMCSENT", "미시간 소비자심리", "", "cold"),
               ("RECPROUSM156N", "침체확률", "%", "mid"), ("CIVPART", "경제활동참가율", "%", "mid")],
    "rates": [("DGS30", "미 국채 30Y", "%", "hot"), ("THREEFYTP10", "텀프리미엄 10Y", "%", "hot"),
              ("DFII10", "실질금리 10Y", "%", "hot"), ("DGS10", "미 국채 10Y", "%", "hot"),
              ("DGS2", "미 국채 2Y", "%", "hot"), ("MORTGAGE30US", "모기지 30Y", "%", "hot"),
              ("MICH", "기대인플레 서베이 1Y", "%", "mid"), ("T5YIFR", "5y5y 포워드", "%", "mid"),
              ("T10YIE", "BEI 10Y", "%", "mid"), ("T10Y3M", "커브 3m10y", "%p", "mid"),
              ("T10Y2Y", "커브 2s10s", "%p", "mid"),
              ("MEDCPIM158SFRBCLE", "중위 CPI", "%", "mid"),
              ("TRMMEANCPIM158SFRBCLE", "절사평균 CPI", "%", "mid"),
              ("DFEDTARU", "기준금리 상단", "%", "mid")],
    "liquidity": [("WTREGEN", "TGA", "$mn", "hot"), ("WALCL", "Fed 총자산", "$mn", "mid"),
                  ("WRESBAL", "은행 지준", "$mn", "cold"), ("RRPONTSYD", "RRP 잔고", "$bn", "cold"),
                  ("SOFR", "SOFR", "%", "mid"), ("IORB", "IORB", "%", "mid"),
                  ("VIXCLS", "VIX", "", "cold"), ("MOVE", "MOVE", "", "mid"),
                  ("SKEW", "SKEW", "", "mid"), ("NFCI", "NFCI", "", "cold"),
                  ("BAMLH0A0HYM2", "HY 스프레드", "%", "cold"),
                  ("BAMLC0A0CM", "IG 스프레드", "%", "cold"), ("BAA10Y", "Baa−10Y", "%p", "cold"),
                  ("DTWEXBGS", "DXY 광의", "", "mid"), ("DEXKOUS", "원/달러", "원", "hot"),
                  ("DEXJPUS", "엔/달러", "엔", "hot"), ("USEPUINDXD", "미 EPU", "", "hot"),
                  ("KS11", "코스피", "pt", "mid"), ("GC_F", "금", "$", "hot")],
    "geo": [("USDTRY_X", "리라/달러", "", "hot"), ("URA", "우라늄 ETF", "", "hot"),
            ("DCOILBRENTEU", "브렌트", "$", "hot"), ("LIT", "리튬 ETF", "", "hot"),
            ("DCOILWTICO", "WTI", "$", "hot"), ("BDRY", "건화물 운임", "", "mid"),
            ("REMX", "희토류 ETF", "", "mid"), ("PWHEAMTUSDM", "밀", "$/t", "mid"),
            ("DHHNGSP", "헨리허브 가스", "$", "mid"), ("DEXCHUS", "위안/달러", "", "cold")],
}


# ── 데이터 ──────────────────────────────────────────────────
def _csv(path: Path) -> list[tuple[str, float]]:
    if not path.exists():
        return []
    out = []
    for r in csv.DictReader(io.open(path, encoding="utf-8")):
        try:
            out.append((r["date"], float(r["value"])))
        except (ValueError, KeyError, TypeError):
            pass
    return out


def series(sid: str) -> list[tuple[str, float]]:
    return _csv(HIST / f"{sid}.csv") or _csv(TOSS / f"{sid}.csv")


def pctl(vals: list[float], v: float) -> float:
    return sum(1 for x in vals if x < v) / len(vals) * 100 if vals else 0.0


def stat(sid: str) -> dict[str, Any] | None:
    s = series(sid)
    if len(s) < 20:
        return None
    vals = [v for _, v in s]
    cur = vals[-1]
    m, sd = st.mean(vals), st.pstdev(vals)
    return {"id": sid, "d": s[-1][0], "v": cur, "pct": pctl(vals, cur),
            "z": (cur - m) / sd if sd else 0.0, "n": len(vals), "start": s[0][0],
            "chg20": cur - vals[-21] if len(vals) > 21 else None, "series": s[-260:]}


# ── SVG ─────────────────────────────────────────────────────
def spark(s: list[tuple[str, float]], w: int = 200, h: int = 40) -> str:
    if len(s) < 2:
        return ""
    vals = [v for _, v in s]
    lo, hi = min(vals), max(vals)
    rng = (hi - lo) or 1
    pts = " ".join(f"{i/(len(vals)-1)*w:.1f},{h-(v-lo)/rng*h:.1f}" for i, v in enumerate(vals))
    last_x, last_y = w, h - (vals[-1] - lo) / rng * h
    return (f'<svg class="spark" viewBox="0 0 {w} {h}" preserveAspectRatio="none" aria-hidden="true">'
            f'<polyline points="{pts}"/>'
            f'<circle cx="{last_x:.1f}" cy="{last_y:.1f}" r="2.5"/></svg>')


def spine_svg(rows: list[tuple[str, float, str, str]]) -> str:
    W, PL, PR, STEP = 720, 176, 104, 26
    H = 18 + len(rows) * STEP
    def X(p: float) -> float:
        return PL + p / 100 * (W - PL - PR)
    body = []
    for i, (lab, pct, note, tone) in enumerate(rows):
        y = 8 + i * STEP
        body.append(
            f'<line class="sp-track" x1="{PL}" y1="{y+11}" x2="{W-PR}" y2="{y+11}"/>'
            f'<line class="sp-mid" x1="{X(50):.1f}" y1="{y+5}" x2="{X(50):.1f}" y2="{y+17}"/>'
            f'<circle class="sp-dot {tone}" cx="{X(pct):.1f}" cy="{y+11}" r="5"/>'
            f'<text class="sp-l" x="{PL-12}" y="{y+15}" text-anchor="end">{lab}</text>'
            f'<text class="sp-v" x="{W-PR+10}" y="{y+15}">{pct:.0f}% · {note}</text>')
    return (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="지표별 표본 백분위">'
            f'<text class="ax" x="{PL}" y="{H-1}">0</text>'
            f'<text class="ax" x="{X(50):.1f}" y="{H-1}" text-anchor="middle">50</text>'
            f'<text class="ax" x="{W-PR}" y="{H-1}" text-anchor="end">100 백분위</text>'
            f'{"".join(body)}</svg>')


def esc(s: Any) -> str:
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


# ── 페이지 뼈대 ─────────────────────────────────────────────
CSS = """
:root{--paper:#F5F7FA;--card:#FFF;--ink:#14171D;--ink2:#3C434F;--mute:#6B7382;--rule:#DCE1E8;
--grid:#E7EBF0;--track:#E4E9F0;--hot:#C0102B;--mid:#8B7A55;--cold:#12459E;--line:#1A56C4;
--chip:#EEF2F8;--shadow:0 1px 2px rgba(16,24,40,.05),0 8px 24px -16px rgba(16,24,40,.22)}
@media(prefers-color-scheme:dark){:root:not([data-theme=light]){--paper:#0E1116;--card:#161A21;
--ink:#E9ECF2;--ink2:#B8C0CC;--mute:#8B94A3;--rule:#252B35;--grid:#222833;--track:#232A35;
--hot:#EF5C74;--mid:#C2A96B;--cold:#6E9BF2;--line:#7FA8F5;--chip:#1C222C;
--shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px -18px rgba(0,0,0,.8)}}
:root[data-theme=dark]{--paper:#0E1116;--card:#161A21;--ink:#E9ECF2;--ink2:#B8C0CC;--mute:#8B94A3;
--rule:#252B35;--grid:#222833;--track:#232A35;--hot:#EF5C74;--mid:#C2A96B;--cold:#6E9BF2;
--line:#7FA8F5;--chip:#1C222C;--shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px -18px rgba(0,0,0,.8)}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-weight:350;line-height:1.7;
font-family:"IBM Plex Sans KR","Malgun Gothic",system-ui,sans-serif}
a{color:inherit}
.nav{border-bottom:1px solid var(--rule);background:var(--card);position:sticky;top:0;z-index:9}
.nav-in{max-width:960px;margin:0 auto;padding:12px 22px;display:flex;gap:18px;align-items:baseline;flex-wrap:wrap}
.brand{font-family:"Gowun Batang",serif;font-weight:700;font-size:18px;text-decoration:none;margin-right:6px}
.nav a{font-size:13.5px;color:var(--mute);text-decoration:none;padding:3px 0;border-bottom:1.5px solid transparent}
.nav a:hover,.nav a.on{color:var(--ink);border-bottom-color:var(--line)}
.wrap{max-width:960px;margin:0 auto;padding:40px 22px 80px;display:flex;flex-direction:column;gap:38px}
.eyebrow{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.13em;
text-transform:uppercase;color:var(--mute);margin:0 0 10px}
h1{font-family:"Gowun Batang",serif;font-weight:700;font-size:clamp(30px,4.6vw,44px);line-height:1.24;
margin:0 0 14px;letter-spacing:-.015em;text-wrap:balance}
h2{font-family:"Gowun Batang",serif;font-weight:700;font-size:clamp(21px,2.6vw,26px);margin:0 0 4px;text-wrap:balance}
h3{font-size:15px;font-weight:600;margin:0 0 4px}
p{margin:0 0 12px;color:var(--ink2)}p:last-child{margin-bottom:0}
section{display:flex;flex-direction:column;gap:14px}
.lede{font-size:18px;color:var(--ink);line-height:1.62}
strong{color:var(--ink);font-weight:600}
.hr{height:1px;background:var(--rule);border:0;margin:0}
.card{background:var(--card);border:1px solid var(--rule);border-radius:10px;padding:18px 20px;
box-shadow:var(--shadow);display:flex;flex-direction:column;gap:12px}
.card svg{width:100%;height:auto;display:block;overflow:visible}
figure{margin:0;display:flex;flex-direction:column;gap:9px}
figcaption{font-size:12.5px;color:var(--mute);line-height:1.6}
.grid3{display:grid;grid-template-columns:repeat(auto-fill,minmax(232px,1fr));gap:12px}
.tile{background:var(--card);border:1px solid var(--rule);border-radius:9px;padding:13px 15px;
display:flex;flex-direction:column;gap:6px}
.tile .t{font-size:12.5px;color:var(--mute)}
.tile .v{font-family:"IBM Plex Mono",monospace;font-size:19px;font-weight:500;
font-variant-numeric:tabular-nums;letter-spacing:-.02em}
.tile .m{font-size:11.5px;color:var(--mute);font-family:"IBM Plex Mono",monospace;
font-variant-numeric:tabular-nums;display:flex;justify-content:space-between;gap:8px}
.spark{width:100%;height:38px;overflow:visible}
.spark polyline{fill:none;stroke:var(--line);stroke-width:1.6;vector-effect:non-scaling-stroke}
.spark circle{fill:var(--line)}
.pill{display:inline-block;padding:2px 7px;border-radius:999px;font-family:"IBM Plex Mono",monospace;
font-size:10.5px;background:var(--chip)}
.pill.hot{color:var(--hot)}.pill.cold{color:var(--cold)}.pill.mid{color:var(--mid)}
.stat-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(146px,1fr));gap:1px;
background:var(--rule);border:1px solid var(--rule);border-radius:10px;overflow:hidden}
.stat{background:var(--card);padding:14px 16px;display:flex;flex-direction:column;gap:3px}
.stat .k{font-size:11.5px;color:var(--mute)}
.stat .v{font-family:"IBM Plex Mono",monospace;font-size:22px;font-weight:500;
font-variant-numeric:tabular-nums;letter-spacing:-.02em}
.stat .s{font-size:11.5px;color:var(--mute);font-variant-numeric:tabular-nums}
.up{color:var(--hot)}.dn{color:var(--cold)}
table{border-collapse:collapse;width:100%;font-size:13.5px}
th,td{padding:8px 10px;text-align:right;border-bottom:1px solid var(--rule);white-space:nowrap}
th:first-child,td:first-child{text-align:left}
th{font-size:11px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--mute);
border-bottom:1px solid var(--ink2)}
td{font-family:"IBM Plex Mono",monospace;font-variant-numeric:tabular-nums}
td:first-child{font-family:"IBM Plex Sans KR",sans-serif}
.scroll{overflow-x:auto}
.ax{fill:var(--mute);font-family:"IBM Plex Mono",monospace;font-size:10.5px}
.sp-track{stroke:var(--track);stroke-width:6;stroke-linecap:round}
.sp-mid{stroke:var(--mute);stroke-width:1;opacity:.5}
.sp-dot.hot{fill:var(--hot)}.sp-dot.mid{fill:var(--mid)}.sp-dot.cold{fill:var(--cold)}
.sp-l{fill:var(--ink2);font-size:12.5px}
.sp-v{fill:var(--mute);font-family:"IBM Plex Mono",monospace;font-size:11px}
.arch{display:flex;flex-direction:column;gap:1px;background:var(--rule);border:1px solid var(--rule);
border-radius:10px;overflow:hidden}
.arch a{background:var(--card);padding:13px 17px;display:flex;justify-content:space-between;
gap:14px;text-decoration:none;align-items:baseline}
.arch a:hover{background:var(--chip)}
.arch .d{font-family:"IBM Plex Mono",monospace;font-size:14px}
.arch .m{font-size:12.5px;color:var(--mute)}
footer{font-size:12.5px;color:var(--mute);line-height:1.7;border-top:1px solid var(--rule);padding-top:20px}
@media(max-width:600px){.wrap{padding:26px 14px 56px;gap:28px}}
"""


def page(title: str, body: str, depth: int = 0, active: str = "") -> str:
    up = "../" * depth
    nav = [("index.html", "오늘", "index"), ("axis-growth.html", "성장", "growth"),
           ("axis-rates.html", "물가·금리", "rates"), ("axis-liquidity.html", "유동성·신용", "liquidity"),
           ("axis-geo.html", "지정학·무역", "geo"), ("archive.html", "아카이브", "archive")]
    links = "".join(f'<a href="{up}{h}" class="{"on" if k == active else ""}">{t}</a>'
                    for h, t, k in nav)
    return f'''<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=IBM+Plex+Sans+KR:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{up}style.css">
</head><body>
<nav class="nav"><div class="nav-in"><a class="brand" href="{up}index.html">시황판</a>{links}</div></nav>
<div class="wrap">{body}
<footer>매크로 Data Book 자동수집 · 백분위는 각 계열 자체 표본 기준(표본 시작은 카드에 표기).
생성 {datetime.now().strftime('%Y-%m-%d %H:%M')}</footer>
</div></body></html>'''


def tile(s: dict, label: str, unit: str, tone: str) -> str:
    pill = f'<span class="pill {tone}">{s["pct"]:.0f}%</span>'
    chg = (f'20기간 {s["chg20"]:+,.2f}' if s["chg20"] is not None else "")
    v = f'{s["v"]:,.2f}' if abs(s["v"]) < 10000 else f'{s["v"]:,.0f}'
    return (f'<div class="tile"><div class="t">{esc(label)} {pill}</div>'
            f'<div class="v">{v}<span style="font-size:12px;color:var(--mute)"> {esc(unit)}</span></div>'
            f'{spark(s["series"])}'
            f'<div class="m"><span>{s["d"]}</span><span>{chg}</span></div>'
            f'<div class="m"><span>z {s["z"]:+.2f}</span><span>{s["start"][:7]}~ {s["n"]:,}</span></div></div>')


# ── 축 페이지 ───────────────────────────────────────────────
def build_axis(key: str) -> tuple[str, list[dict]]:
    name, team, sub = AXES[key]
    stats, rows, tiles = [], [], []
    for sid, lab, unit, tone in SPINE[key]:
        s = stat(sid)
        if not s:
            continue
        stats.append(s)
        note = f'{s["v"]:,.2f}{unit}' if abs(s["v"]) < 10000 else f'{s["v"]:,.0f}{unit}'
        rows.append((lab, s["pct"], note, tone))
        tiles.append(tile(s, lab, unit, tone))
    rows.sort(key=lambda r: -r[1])
    body = f'''<section><div><p class="eyebrow">축 · {esc(name)}</p>
<h1>{esc(name)}</h1><p class="lede">{esc(sub)}</p></div>
<figure class="card">{spine_svg(rows)}
<figcaption>표본 백분위. 붉은 점은 높은 자리, 푸른 점은 낮은 자리 — <strong>색은 방향이지 좋고 나쁨이 아니다.</strong>
각 계열의 표본 구간이 달라 서로 다른 지표의 백분위를 직접 비교하지 않는다.</figcaption></figure>
</section>
<section><h2>계열별</h2><div class="grid3">{"".join(tiles)}</div></section>'''
    return page(f"{name} — 시황판", body, 0, key), stats


# ── 오늘 ────────────────────────────────────────────────────
def build_index(snap: dict) -> str:
    parts = []
    heads = []
    for key in AXES:
        name, _, sub = AXES[key]
        rows = []
        for sid, lab, unit, tone in SPINE[key]:
            s = stat(sid)
            if s:
                note = f'{s["v"]:,.2f}{unit}' if abs(s["v"]) < 10000 else f'{s["v"]:,.0f}{unit}'
                rows.append((lab, s["pct"], note, tone))
        if not rows:
            continue
        rows.sort(key=lambda r: -r[1])
        top = rows[:6]
        parts.append(f'''<section><div><p class="eyebrow">축 · {esc(name)}</p>
<h2>{esc(sub)}</h2></div>
<figure class="card">{spine_svg(top)}
<figcaption>백분위 상위 6개만. <a href="axis-{key}.html">{esc(name)} 전체 보기 →</a></figcaption></figure></section>''')
        heads.append((name, rows[0]))

    # 한국 수급
    kr = ""
    ks = series("TOSS_KOSPI_CLOSE")
    if len(ks) > 2:
        rets = [(b[0], (b[1] / a[1] - 1) * 100) for a, b in zip(ks, ks[1:]) if a[1]]
        rv = [r for _, r in rets]
        last_d, last_r = rets[-1]
        fo = series("TOSS_KOSPI_FLOW_FOREIGNER")
        ind = series("TOSS_KOSPI_FLOW_INDIVIDUAL")
        cells = [("코스피", f"{ks[-1][1]:,.0f}", f"{last_r:+.2f}% · 백분위 {pctl(rv, last_r):.1f}%",
                  "dn" if last_r < 0 else "up")]
        if fo:
            fv = [v for _, v in fo]
            cells.append(("외국인 순매수", f"{fo[-1][1]/10000:+.2f}조",
                          f"백분위 {pctl(fv, fo[-1][1]):.1f}%", "dn" if fo[-1][1] < 0 else "up"))
        if ind:
            iv = [v for _, v in ind]
            cells.append(("개인 순매수", f"{ind[-1][1]/10000:+.2f}조",
                          f"백분위 {pctl(iv, ind[-1][1]):.1f}%", "up" if ind[-1][1] > 0 else "dn"))
        b3, b10 = series("TOSS_KR_BOND_3Y"), series("TOSS_KR_BOND_10Y")
        if b3 and b10:
            m3 = dict(b3); m10 = dict(b10)
            common = sorted(set(m3) & set(m10))
            spd = {d: m10[d] - m3[d] for d in common}
            sv = list(spd.values())
            cur = spd[common[-1]]
            cells.append(("국고 10Y−3Y", f"{cur:+.3f}%p", f"백분위 {pctl(sv, cur):.1f}%", "up"))
        kr = ('<section><div><p class="eyebrow">한국</p><h2>수급과 커브</h2></div><div class="stat-row">'
              + "".join(f'<div class="stat"><span class="k">{esc(k)}</span>'
                        f'<span class="v {c}">{esc(v)}</span><span class="s">{esc(s)}</span></div>'
                        for k, v, s, c in cells) + '</div>'
              f'<p>기준일 {esc(last_d)}. 한국 수급은 2014-07 이후 {len(rv):,}일 표본.</p></section>')

    hl = " · ".join(f'<strong>{esc(n)}</strong> {r[0]} {r[1]:.0f}%' for n, r in heads)
    head = f'''<section><div><p class="eyebrow">시황판 · {esc(snap.get("generated_at_utc", "")[:10])} · 지표 {snap.get("indicator_count", 0)}개</p>
<h1>오늘의 네 축</h1>
<p class="lede">각 축에서 가장 높은 자리에 있는 계열 — {hl}</p></div></section>'''
    return page("시황판 — 오늘의 네 축", head + kr + "".join(parts) + '''
<section class="card"><h3>읽는 법</h3>
<p><strong>백분위는 그 계열 자체의 표본 안에서의 위치</strong>다. 90%는 "과거 대비 높은 자리"라는 뜻이지
"위험하다"가 아니다. 표본 구간이 계열마다 달라 <strong>서로 다른 지표의 백분위를 직접 비교하지 않는다</strong>.</p>
<p>스파크라인은 최근 260관측이다. 일별 계열은 약 1년, 주별은 5년, 월별은 20년을 가리킨다 —
<strong>같은 폭이 같은 기간을 뜻하지 않는다.</strong></p></section>''', 0, "index")


# ── 아카이브 ────────────────────────────────────────────────
def build_archive() -> tuple[str, list[tuple[str, str]]]:
    snaps = sorted(OUTPUT_DIR.glob("snapshot_*.json"), reverse=True)
    items, pages = [], []
    for p in snaps:
        date = p.stem.replace("snapshot_", "")
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        inds = d.get("indicators", [])
        ok = sum(1 for i in inds if i.get("status") == "ok")
        items.append(f'<a href="d/{date}.html"><span class="d">{date}</span>'
                     f'<span class="m">지표 {len(inds)}개 · 수집 성공 {ok}</span></a>')
        pages.append((date, build_day(date, d)))
    body = f'''<section><div><p class="eyebrow">아카이브</p><h1>날짜별 스냅샷</h1>
<p class="lede">수집이 돌 때마다 하루가 하나씩 쌓인다. 현재 <strong>{len(items)}일</strong>.</p></div>
<div class="arch">{"".join(items)}</div></section>'''
    return page("아카이브 — 시황판", body, 0, "archive"), pages


def build_day(date: str, snap: dict) -> str:
    secs = []
    for key, (name, team, _) in AXES.items():
        rows = [i for i in snap.get("indicators", [])
                if i.get("team") == team and i.get("status") == "ok" and i.get("observations")]
        if not rows:
            continue
        trs = []
        for i in rows:
            o = i["observations"][0]
            v = o.get("value")
            lab = str(o.get("label", ""))
            if "http" in lab:
                lab = "(헤드라인)"
            vs = f"{v:,.3f}" if isinstance(v, (int, float)) else esc(str(v)[:44])
            trs.append(f'<tr><td>{esc(i["name"])}</td><td>{vs}</td>'
                       f'<td>{esc(o.get("date", ""))}</td><td>{esc(lab[:34])}</td></tr>')
        secs.append(f'<section><h2>{esc(name)}</h2><div class="scroll card"><table>'
                    f'<thead><tr><th>지표</th><th>값</th><th>기준일</th><th>계열</th></tr></thead>'
                    f'<tbody>{"".join(trs)}</tbody></table></div></section>')
    body = (f'<section><div><p class="eyebrow">스냅샷</p><h1>{esc(date)}</h1>'
            f'<p class="lede">수집 지표 {snap.get("indicator_count", 0)}개. '
            f'<a href="../archive.html">← 아카이브</a></p></div></section>' + "".join(secs))
    return page(f"{date} — 시황판", body, 1, "archive")


# ── 진입 ────────────────────────────────────────────────────
def build(quiet: bool = False) -> int:
    snaps = sorted(OUTPUT_DIR.glob("snapshot_*.json"))
    if not snaps:
        print("스냅샷이 없다 — `python -m databook run` 을 먼저 돌릴 것")
        return 1
    snap = json.loads(snaps[-1].read_text(encoding="utf-8"))

    SITE.mkdir(parents=True, exist_ok=True)
    (SITE / "d").mkdir(exist_ok=True)
    (SITE / "style.css").write_text(CSS, encoding="utf-8")

    (SITE / "index.html").write_text(build_index(snap), encoding="utf-8")
    n_ax = 0
    for key in AXES:
        html, stats = build_axis(key)
        (SITE / f"axis-{key}.html").write_text(html, encoding="utf-8")
        n_ax += len(stats)
    arch_html, days = build_archive()
    (SITE / "archive.html").write_text(arch_html, encoding="utf-8")
    for date, html in days:
        (SITE / "d" / f"{date}.html").write_text(html, encoding="utf-8")

    if not quiet:
        print(f"사이트 생성: {SITE}")
        print(f"  index + 축 4개(계열 {n_ax}개) + 아카이브 {len(days)}일")
        print(f"  → file:///{str(SITE / 'index.html').replace(chr(92), '/')}")
    return 0
