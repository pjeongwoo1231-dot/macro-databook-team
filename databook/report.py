"""주간 발표자료 **스캐폴드**를 만든다.

왜 이게 필요한가
    2026-08-30에 게이트를 통과하는 자료를 하나 만들었지만, 그건 임시 스크립트로
    만든 것이라 **다음 주에 재현할 수단이 없었다.** `audit`는 채점만 하지 생산을 돕지 않는다.
    채점표만 주고 답안 쓰는 법을 안 주면, 다음 사람은 또 지표 20개짜리를 낸다.

무엇이 자동이고 무엇이 사람 몫인가
    자동 — 축별 지표 수집·표 조판, 차트 10종, 기저율 계산, 문헌 계수 배치,
           백분위·잔차 같은 파생 계산, 게이트 자가검사
    사람 — **해석.** 각 절의 프로즈. 이건 주마다 다르므로 자동화 대상이 아니다.
           스캐폴드는 그 자리를 `WRITE:` 주석으로 남긴다.

    ⚠ **스캐폴드는 발표자료가 아니다.** 프로즈를 채우고 `databook audit`가 통과해야
    비로소 낼 수 있다. 볼트 「좋은 시황의 규칙」이 금지한 것 — 신선도표·자기검사·
    방법론을 본문에 남기는 것 — 도 프로즈 단계에서 지켜야 한다.

쓰는 법
    python -m databook report                        # as-of = 직전 세션(화)
    python -m databook report --asof 2026-08-28      # 시점 고정
    python -m databook report --out ~/Documents/주간.html
"""
from __future__ import annotations

import bisect
import csv
import datetime as dt
import json
import math
import statistics as st
from pathlib import Path
from typing import Any

from . import charts as C
from .core import OUTPUT_DIR

_TUE = 1
REPO = Path(__file__).resolve().parent.parent


# ─────────────────────────── 시점

def last_session(today: dt.date | None = None) -> dt.date:
    t = today or dt.date.today()
    back = (t.weekday() - _TUE) % 7
    return t - dt.timedelta(days=back or 7)


# ─────────────────────────── 자료

def _hist(name: str, sub: str = "") -> dict[dt.date, float]:
    p = (OUTPUT_DIR / "history" / sub / f"{name}.csv") if sub else (OUTPUT_DIR / "history" / f"{name}.csv")
    out: dict[dt.date, float] = {}
    if not p.exists():
        return out
    with p.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            k = list(r.keys())
            try:
                out[dt.date.fromisoformat(r[k[0]][:10])] = float(r[k[1]])
            except Exception:
                pass
    return out


def _snapshot(asof: dt.date) -> list[dict[str, Any]]:
    """as-of 이하의 가장 최근 **온전한** 스냅샷.

    ⚠ `run --only X --render-anyway`가 전체 스냅샷을 몇 건짜리로 덮어쓴 적이 있다.
    관측이 절반도 안 차 있으면 건너뛴다 — 그 상태로는 커버리지가 거짓 통과한다.
    """
    for p in sorted(OUTPUT_DIR.glob("snapshot_*.json"), reverse=True):
        if p.stem[len("snapshot_"):] > asof.isoformat():
            continue
        d = json.loads(p.read_text(encoding="utf-8"))
        items = d if isinstance(d, list) else next(
            (v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict)), [])
        if items and sum(1 for i in items if (i.get("observations") or [])) >= len(items) * 0.5:
            return items
    return []


def _papers() -> dict[str, list[dict[str, Any]]]:
    import yaml
    p = REPO / "papers.yaml"
    return yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else {}


# ─────────────────────────── 계산

def _chg(s, d, days):
    a = _at(s, d)
    b = _at(s, d - dt.timedelta(days=days))
    return None if (a is None or b is None) else (a - b) * 100


def _at(s, d):
    ks = [k for k in s if k <= d]
    return s[max(ks)] if ks else None


def _pct(s, d):
    v = {k: x for k, x in s.items() if k <= d}
    if not v:
        return None, None, 0
    cur = v[max(v)]
    vals = sorted(v.values())
    return cur, bisect.bisect_left(vals, cur) / len(vals) * 100, len(vals)


def _base_rate(real, f5, kospi, asof):
    """지금 배열(1개월 실질↓ + 원거리 기대↑)이 과거에 있었을 때 코스피가 어땠나."""
    last = max(kospi) if kospi else asof
    days = sorted(set(real) & set(f5))

    def back(s, d, n):
        ks = [k for k in s if k <= d - dt.timedelta(days=n)]
        return s[max(ks)] if ks else None

    eps: list[dt.date] = []
    for d in days:
        r0, f0, f3 = back(real, d, 30), back(f5, d, 30), back(f5, d, 91)
        if None in (r0, f0, f3):
            continue
        if (real[d] - r0) * 100 <= -5 and (f5[d] - f0) * 100 >= 5 and (f5[d] - f3) * 100 >= 10:
            if not eps or (d - eps[-1]).days > 30:
                eps.append(d)

    def kv(d):
        ks = [k for k in kospi if k <= d]
        return kospi[max(ks)] if ks else None

    out = {}
    for hz, lab in ((30, "1개월"), (91, "3개월")):
        arr = []
        for d in eps:
            if d + dt.timedelta(days=hz) > last:       # 미완성 지평 제외 — 미래값이 없다
                continue
            a, b = kv(d), kv(d + dt.timedelta(days=hz))
            if a and b:
                arr.append((b / a - 1) * 100)
        out[lab] = arr
    return out


def _vix_resid(baa, vix, asof):
    """VIX가 설명하는 스프레드와 실제의 차 — '취약성'을 반증 가능하게 만드는 자리."""
    A = 1.6705                                          # papers.yaml: vix_repl
    smp = [d for d in sorted(set(baa) & set(vix))
           if dt.date(2008, 1, 1) <= d <= dt.date(2017, 12, 31)]
    if not smp:
        return None
    a0 = st.mean(baa[d] - A * math.log(vix[d]) for d in smp)
    both = [d for d in sorted(set(baa) & set(vix)) if d <= asof]
    if not both:
        return None
    cd = both[-1]
    resid = {d: baa[d] - (a0 + A * math.log(vix[d])) for d in sorted(set(baa) & set(vix))}
    rv = sorted(resid.values())
    return dict(A=A, a0=a0, d=cd, vix=vix[cd], pred=a0 + A * math.log(vix[cd]),
                act=baa[cd], resid=resid[cd], n=len(rv), smp=len(smp),
                pct=bisect.bisect_left(rv, resid[cd]) / len(rv) * 100, series=resid)


# ─────────────────────────── 축 정의

AXES: list[tuple[str, str, list[str]]] = [
    ("01", "성장 · 경기", [
        "GDPNow", "실질 GDP", "산업생산", "소매판매", "설비투자", "기업이익", "미국 TFP",
        "지역 연준 제조업지수", "미시간 소비자심리", "주택 착공", "신규 / 기존주택",
        "케이스-실러", "모기지 30Y", "재고 사이클", "설비가동률", "주간경제지수 WEI",
        "NFP", "실업률", "v/u 비율", "JOLTS", "실업자 수", "경제활동참가율",
        "신규 실업수당", "Sahm", "임시직 고용", "고용비용지수", "침체확률",
        "유로존 실질GDP", "일본 실질GDP", "일본 단칸", "중국 실물", "독일 산업생산"]),
    ("02", "한국", [
        "한국은행 기준금리", "국고채 3Y", "CD 91일", "한미 시장금리차", "한미 금리차",
        "한국 품목별 수출", "한국 20일 수출", "한국 20일 수입", "한국 산업활동동향",
        "국내 소비", "한국 CPI", "한국 기대인플레이션", "한국 M2", "원/달러"]),
    ("03", "미 채권", [
        "미 국채 2Y", "미 국채 10Y", "미 국채 30Y", "실질금리", "BEI 10Y",
        "5y5y", "텀프리미엄", "커브 2s10s", "커브 3m10y", "미 기준금리"]),
    ("04", "유동성 · 신용", [
        "초과채권프리미엄", "GZ 신용스프레드", "HY 스프레드", "IG 스프레드",
        "신용스프레드 장기 대용", "시카고연준", "은행 대출태도", "BIS 부채상환비율",
        "카드 연체율", "VIX", "MOVE", "SKEW", "Put/Call", "CNN Fear"]),
    ("05", "물가", [
        "근원 PCE 물가", "PCE (헤드라인", "절사평균 PCE", "중위 CPI", "CPI 서비스ex",
        "PPI (최종수요", "기대인플레 서베이", "유로존 HICP", "유로존 근원 HICP",
        "일본 CPI (코어", "일본 서비스물가", "중국 CPI", "중국 PPI"]),
    ("06", "지정학 · 무역", [
        "유가 WTI", "유가 Brent", "금 (실질금리", "천연가스", "유럽 TTF", "EU 천연가스",
        "지정학위험지수 GPR", "지정학위험지수 GPRC", "GSCPI", "해운 운임",
        "러시아 화석연료", "미 원유재고", "미 원유생산", "농산물", "니치 원자재",
        "미 관세 수입", "중국 국가별 무역", "일본 무역수지", "국내 유가", "구리"]),
    ("07", "유동성 수량", [
        "RRP 잔고", "은행 지준", "순유동성", "TGA 잔고 (주간", "EFFR - IORB",
        "SOFR−IORB", "연준 레포", "미국 M2 증가율", "글로벌 M2",
        "국채선물 레버리지펀드 숏", "Fed 대차대조표"]),
    ("08", "수급 · 가격", [
        "코스피·코스닥 지수", "외국인 수급", "주식 대차잔고", "김치프리미엄",
        "DXY", "엔/달러", "유로/달러", "위안/달러", "BIS 실질실효환율",
        "S&P500 선물", "나스닥100 선물", "러셀2000 선물", "AI 캐펙스"]),
]


# ─────────────────────────── 조판 조각

def _tbl(rows: list[tuple], head: list[str]) -> str:
    th = "".join(f'<th class="n">{h}</th>' if i else f"<th>{h}</th>" for i, h in enumerate(head))
    body = []
    for r in rows:
        tds = "".join(f'<td class="n">{c}</td>' if i else f"<td>{c}</td>" for i, c in enumerate(r))
        body.append(f"<tr>{tds}</tr>")
    return (f'<div class="scroll"><table><thead><tr>{th}</tr></thead>'
            f'<tbody>{"".join(body)}</tbody></table></div>')


def _fmt(v, nd=2):
    if isinstance(v, (int, float)):
        return f"{v:,.{nd}f}"
    s = str(v)
    return s[:44] + "…" if len(s) > 46 else s


def _paper_box(p: dict[str, Any]) -> str:
    return (f'<div class="paper"><b>{p["claim"]}</b><br>{p["coef"]}<br>'
            f'<span style="opacity:.85">적용 — {p["apply"]}</span><br>'
            f'<span style="opacity:.85">⚠ {p["caveat"]}</span>'
            f'<cite>{p["cite"]}</cite></div>')


CSS = """
:root{--paper:#FBFCFC;--raise:#F2F5F5;--ink:#101C24;--muted:#566672;
 --rule:#DCE3E5;--hair:#EBEFF0;--accent:#0F6B6B;--warn:#9A4A2C;--bg:#FBFCFC}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
 --paper:#0E1417;--raise:#161F24;--ink:#E4ECEE;--muted:#8FA0A8;
 --rule:#223038;--hair:#1A252B;--accent:#4FC3B8;--warn:#E08A63;--bg:#0E1417}}
:root[data-theme="dark"]{--paper:#0E1417;--raise:#161F24;--ink:#E4ECEE;--muted:#8FA0A8;
 --rule:#223038;--hair:#1A252B;--accent:#4FC3B8;--warn:#E08A63;--bg:#0E1417}
*{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);margin:0;word-break:keep-all;
 font:400 16px/1.75 "IBM Plex Sans KR",-apple-system,"Segoe UI","Malgun Gothic",sans-serif}
.wrap{max-width:1080px;margin:0 auto;padding:clamp(2rem,5vw,4.5rem) clamp(1.1rem,4vw,2.5rem) 5rem}
.col{max-width:64ch}
h1,h2,h3{font-family:"Noto Serif KR",Georgia,serif;text-wrap:balance;margin:0}
h1{font-weight:700;font-size:clamp(1.9rem,4.4vw,3rem);line-height:1.24;letter-spacing:-.015em}
h2{font-weight:700;font-size:clamp(1.2rem,2.4vw,1.5rem);margin:0 0 .5rem}
h3{font-weight:500;font-size:1.02rem;margin:2rem 0 .4rem}
p{margin:0 0 1.05rem}
.eyebrow{font:500 .72rem/1.5 "IBM Plex Mono",monospace;letter-spacing:.14em;
 text-transform:uppercase;color:var(--muted)}
header{border-bottom:2px solid var(--ink);padding-bottom:2rem;margin-bottom:2.6rem}
.meta{display:flex;flex-wrap:wrap;gap:.4rem 1.6rem;margin-top:1.6rem;
 font:400 .82rem/1.6 "IBM Plex Mono",monospace;color:var(--muted)}
.meta b{color:var(--ink);font-weight:500}
section{margin:3.4rem 0 0}
section>.num{font:500 .72rem/1 "IBM Plex Mono",monospace;color:var(--accent);
 letter-spacing:.1em;display:block;margin-bottom:.55rem}
table{border-collapse:collapse;width:100%;font-size:.88rem;
 font-variant-numeric:tabular-nums;margin:1.4rem 0}
.scroll{overflow-x:auto}
th,td{padding:.5rem .7rem;border-bottom:1px solid var(--hair);text-align:left;vertical-align:top}
thead th{border-bottom:1.5px solid var(--rule);font-weight:500;font-size:.78rem;
 letter-spacing:.05em;text-transform:uppercase;color:var(--muted);white-space:nowrap}
td.n,th.n{text-align:right;font-family:"IBM Plex Mono",monospace;white-space:nowrap}
.paper{border-left:2px solid var(--accent);padding:.15rem 0 .15rem 1.05rem;margin:1.5rem 0;
 font-size:.92rem;color:var(--muted)}
.paper b{color:var(--ink);font-weight:500}
.paper cite{display:block;font-style:normal;font-size:.78rem;margin-top:.4rem;
 font-family:"IBM Plex Mono",monospace}
.slot{border:1px dashed var(--warn);background:color-mix(in srgb,var(--warn) 6%,transparent);
 padding:.9rem 1.1rem;margin:1.4rem 0;font-size:.9rem;color:var(--warn);border-radius:2px}
.slot b{display:block;margin-bottom:.3rem}
.wide{margin-left:calc(-1*clamp(0px,3vw,90px));margin-right:calc(-1*clamp(0px,3vw,90px))}
figure.chart{margin:1.8rem 0}
.kv{font-family:"IBM Plex Mono",monospace;font-variant-numeric:tabular-nums;font-weight:500}
@media print{body{background:#fff}.wide{margin:0}table,figure{break-inside:avoid}}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""


def _slot(what: str, hint: str) -> str:
    return (f'<div class="slot"><b>WRITE: {what}</b>{hint}</div>'
            f'<!-- WRITE: {what} — {hint} -->')


# ─────────────────────────── 본체

def build(asof: dt.date, out: Path) -> dict[str, Any]:
    items = _snapshot(asof)
    if not items:
        raise SystemExit(f"{asof} 이하의 온전한 스냅샷이 없습니다 — `python -m databook run`을 먼저 돌리세요.")

    S: dict[str, tuple] = {}
    TEAM: dict[str, str] = {}
    for i in items:
        obs = i.get("observations") or []
        if obs:
            S[i["name"]] = (obs[0].get("value"), obs[0].get("date"),
                            obs[1].get("value") if len(obs) > 1 else None,
                            (obs[0].get("label") or ""))
            TEAM[i["name"]] = i.get("team") or "?"

    def q(key: str):
        for n in S:
            if key in n:
                return (n,) + S[n]
        return None

    nom, real = _hist("DGS10"), _hist("DFII10")
    bei, f5 = _hist("T10YIE"), _hist("T5YIFR")
    vix, baa = _hist("VIXCLS"), _hist("BAA10Y")
    nfci, hy = _hist("NFCI"), _hist("BAMLH0A0HYM2")
    kospi = _hist("KS11")
    fx = _hist("TOSS_KOSPI_FLOW_FOREIGNER", "toss")
    ind = _hist("TOSS_KOSPI_FLOW_INDIVIDUAL", "toss")
    kpx = _hist("TOSS_KOSPI_CLOSE", "toss")
    try:
        from .fetchers.spreadsheet import fetch_history
        ebp = {dt.date.fromisoformat(d): v for d, v in fetch_history("ebp", column="ebp")}
    except Exception:
        ebp = {}

    papers = _papers()
    base = _base_rate(real, f5, kospi, asof)
    vr = _vix_resid(baa, vix, asof)

    # ── 차트
    ch: dict[str, str] = {}
    rows = []
    for lab, dd in (("1주", 7), ("1개월", 30), ("3개월", 91)):
        for nm, s in (("명목 10Y", nom), ("실질 10Y", real), ("BEI 10Y", bei), ("5y5y", f5)):
            c = _chg(s, asof, dd)
            if c is not None:
                rows.append((f"{lab} · {nm}", round(c, 1)))
    ch["bond"] = C.diverging(rows, title="미 10년 금리의 분해 — 창별 변화", unit="bp")
    bond_rows = dict(rows)

    pc = []
    for lab, s in (("실질 10Y", real), ("BEI 10Y", bei), ("5y5y 기대", f5), ("미 10Y", nom),
                   ("HY OAS", hy), ("EBP", ebp), ("VIX", vix), ("NFCI", nfci)):
        cur, p, n = _pct(s, asof)
        if cur is None:
            continue
        pc.append((lab, cur, p, f"{min(k for k in s if k <= asof).year}~ n={n:,}"))
    ch["pct"] = C.percentile(pc, title="수준이 아니라 위치 — 자기 역사 안에서 어디인가")

    if ebp:
        ch["ebp"] = C.line([(d, v) for d, v in sorted(ebp.items()) if d >= dt.date(2005, 1, 1)],
                           title="초과채권프리미엄 EBP — 0 아래는 위험을 싸게 판다는 뜻",
                           unit="%p", bands=[(-0.6, 0.0, "0 이하")])
    if vr:
        ch["vixr"] = C.line([(d, v) for d, v in sorted(vr["series"].items()) if d >= dt.date(2015, 1, 1)],
                            title="Baa−10Y 잔차 — VIX로 설명되고 남은 부분", unit="%p",
                            bands=[(-1.2, 0.0, "VIX보다 좁다")])
    for lab, key in (("1개월", "1개월"), ("3개월", "3개월")):
        if base.get(key):
            ch["base_" + key] = C.dotplot(base[key], title=f"같은 배열 이후 코스피 {lab} 수익률", unit="%")

    wd = [d for d in sorted(fx) if asof - dt.timedelta(days=8) <= d <= asof]
    if wd:
        ch["flow"] = C.mirror([(f"{d:%m/%d}", fx.get(d, 0), ind.get(d, 0)) for d in wd],
                              title="코스피 수급 — 외국인(위) vs 개인(아래)",
                              labels=("외국인 순매수", "개인 순매수"))

    def _delta_chart(pairs, title, unit="%"):
        out = []
        for lab, key in pairs:
            r = q(key)
            if r and isinstance(r[1], (int, float)) and isinstance(r[3], (int, float)) and r[3]:
                out.append((lab, round((r[1] / r[3] - 1) * 100, 2)))
        return C.diverging(out, title=title, unit=unit) if out else ""

    ch["grow"] = _delta_chart(
        [("GDPNow", "GDPNow"), ("지역 연준 제조업", "지역 연준 제조업지수"),
         ("미시간 심리", "미시간 소비자심리"), ("설비투자", "설비투자"), ("산업생산", "산업생산"),
         ("소매판매", "소매판매"), ("주택 착공", "주택 착공"), ("주택 판매", "신규 / 기존주택"),
         ("JOLTS 구인", "JOLTS"), ("실업자 수", "실업자 수")],
        "성장 지표 — 직전 관측 대비 변화")
    ch["geo"] = _delta_chart(
        [("WTI", "유가 WTI"), ("Brent", "유가 Brent"), ("금", "금 (실질금리"), ("VIX", "VIX"),
         ("유럽 TTF", "유럽 TTF"), ("해운 운임", "해운 운임"), ("원/달러", "원/달러"),
         ("DXY", "DXY"), ("농산물", "농산물"), ("국내 유가", "국내 유가"),
         ("니치 원자재", "니치 원자재")],
        "지정학 — 지수가 아니라 가격으로 본다 (직전 대비)")

    # ── 문서
    P = [f"<title>주간 매크로 {asof.isoformat()} (스캐폴드)</title>",
         '<link rel="preconnect" href="https://fonts.googleapis.com">',
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Noto+Serif+KR:wght@500;700&family=IBM+Plex+Sans+KR:wght@300;400;500;600'
         '&family=IBM+Plex+Mono:wght@400;500&display=swap">',
         "<style>" + CSS + C.CSS + "</style>", '<div class="wrap">']

    filled = sum(1 for i in items if (i.get("observations") or []))
    P.append(f"""<header>
<span class="eyebrow">스캐폴드 · 프로즈를 채운 뒤 audit를 통과해야 낼 수 있다</span>
<h1>주간 매크로 {asof.isoformat()}</h1>
{_slot("결론 한 줄 (H1을 이 문장으로 교체)",
       "이번 주에 실제로 일어난 일 중 가장 큰 것 하나. 축 이름이 아니라 사건으로 쓴다.")}
<div class="meta">
 <span><b>기준</b> {asof.isoformat()}</span>
 <span><b>지표</b> {len(items)}개 중 {filled}개 수집</span>
 <span><b>기저율</b> n={len(base.get('1개월', []))}</span>
 <span><b>등재 문헌</b> {sum(len(v) for v in papers.values())}편</span>
</div></header>""")

    # 축별 절
    used_keys: set[str] = set()
    for num, title, keys in AXES:
        P.append(f'<section><span class="num">{num}</span><h2>{title}</h2>')
        if num == "01" and ch.get("grow"):
            P.append(f'<div class="wide">{ch["grow"]}</div>')
        if num == "03":
            P.append(f'<div class="wide">{ch["bond"]}</div><div class="wide">{ch["pct"]}</div>')
        if num == "04":
            for k in ("vixr", "ebp"):
                if ch.get(k):
                    P.append(f'<div class="wide">{ch[k]}</div>')
        if num == "06" and ch.get("geo"):
            P.append(f'<div class="wide">{ch["geo"]}</div>')
        if num == "08" and ch.get("flow"):
            P.append(f'<div class="wide">{ch["flow"]}</div>')

        rows = []
        for key in keys:
            r = q(key)
            if not r:
                rows.append((key, "관측 없음", "—", "—", "—"))
                continue
            name, cur, date_, prev, label = r
            used_keys.add(name)
            d = ""
            if isinstance(cur, (int, float)) and isinstance(prev, (int, float)) and prev:
                d = f"{(cur/prev-1)*100:+.1f}%"
            rows.append((name[:38], _fmt(prev), _fmt(cur), date_ or "—", d))
        P.append(_tbl(rows, ["지표", "직전", "현재", "기준일", "변화"]))

        for p in papers.get({"01": "labor", "02": "korea", "03": "rates", "04": "credit",
                             "05": "prices", "06": "geopolitics", "07": "liquidity",
                             "08": "korea"}.get(num, ""), []):
            P.append(_paper_box(p))
        P.append(_slot(f"{title} 해석",
                       "표에서 무엇이 어긋나는지, 그것이 무엇을 뜻하는지. "
                       "근거는 추세·사례·이론 중 최소 둘. 방향을 말하려면 기저율을 먼저."))
        P.append("</section>")

    # 기저율
    P.append('<section><span class="num">09</span><h2>기저율 — 이 배열이 방향을 말하는가</h2>')
    for k in ("base_1개월", "base_3개월"):
        if ch.get(k):
            P.append(f'<div class="wide">{ch[k]}</div>')
    br = []
    for lab in ("1개월", "3개월"):
        a = base.get(lab) or []
        if a:
            neg = sum(1 for v in a if v < 0)
            br.append((lab, len(a), f"{st.median(a):+.1f}%",
                       f"{neg}/{len(a)} ({neg/len(a)*100:.0f}%)",
                       f"{min(a):+.1f}%", f"{max(a):+.1f}%"))
    P.append(_tbl(br, ["지평", "n", "중앙값", "음(−)", "최악", "최선"]))
    P.append(_slot("기저율 해석", "동전던지기인가 편향이 있는가. 방향을 말할 수 있는지 없는지를 명시."))
    P.append("</section>")

    # 유사 국면 — 「좋은 시황의 규칙」의 '사례' 축
    try:
        from .analog import find as _analog
        ana = _analog(asof, top=6)
    except Exception:
        ana = None
    if ana:
        P.append('<section><span class="num">10</span>'
                 '<h2>과거 유사 국면 — 그때는 이랬다</h2>')
        head = ["시점", "거리"] + [f"코스피 {h}" for _, h in
                                 (("", "1개월"), ("", "3개월"), ("", "6개월"))]
        rows = []
        for x in ana["rows"]:
            rows.append((str(x["date"]), f"{x['dist']:.2f}",
                         *[("—" if x.get(f"코스피·{h}") is None else f"{x[f'코스피·{h}']:+.1f}%")
                           for h in ("1개월", "3개월", "6개월")]))
        P.append(_tbl(rows, head))
        srow = []
        for lab, _n, unit in (("코스피", "", "%"), ("금", "", "%"), ("WTI", "", "%"),
                              ("미 10Y", "", "bp"), ("Baa 스프레드", "", "bp")):
            cells = [lab]
            for h in ("1개월", "3개월", "6개월"):
                st_ = ana["stats"].get(f"{lab}·{h}")
                cells.append("—" if not st_ else
                             f"{st_['median']:+.1f}{'%' if unit == '%' else 'bp'} "
                             f"(음 {st_['neg']}/{st_['n']})")
            srow.append(tuple(cells))
        P.append(_tbl(srow, ["자산", "1개월 중앙값", "3개월", "6개월"]))
        P.append('<div class="paper"><b>이웃이 가깝다는 것은 관측된 축들만 가깝다는 뜻이다.</b><br>'
                 '정책 국면·제도·전쟁 유무처럼 상태 벡터에 없는 것은 비교되지 않았다. '
                 'n=6은 방향을 부르기에 작다.<br>'
                 '<span style="opacity:.85">적용 — 결과를 옮겨 쓰지 말고 '
                 '「이번과 다른 점」을 먼저 쓴다.</span>'
                 '<cite>databook analog · 상태 8축, 2003~ 후보 {:,}일</cite></div>'.format(ana["pool"]))
        P.append(_slot("이번과 다른 점",
                       "각 이웃에서 지금과 가장 갈리는 축을 짚는다. "
                       "`python -m databook analog --asof <날짜>` 출력의 「이번과 다른 점」을 근거로."))
        P.append("</section>")

    # 투자자 함의 — 방향이 아니라 조건
    P.append('<section><span class="num">11</span><h2>투자자에게 무엇을 뜻하나</h2>')
    P.append('<div class="paper"><b>규칙 — 방향을 부르지 않는다. 조건을 쓴다.</b><br>'
             '「X가 Y를 넘으면 Z가 유리하다」 형태로 쓰고, 각 항목에 <b>시계·근거·무효화</b>를 붙인다.'
             '<br><span style="opacity:.85">시계는 지표의 실제 선행 기간에 맞춘다 — '
             '신용스프레드의 유의 시차는 −10영업일이라 <b>2주 안에 실행 가능한 행동</b>과만 짝짓는다.'
             '</span><br><span style="opacity:.85">⚠ 최종 실행과 승인은 사람이 한다. '
             '이 절은 추천이 아니라 <b>조건부 판단의 재료</b>다.</span>'
             '<cite>최재용(2023) 신용스프레드 유효기간 · 볼트 Human Principle</cite></div>')
    P.append(_slot("함의 3~4개",
                   "각 항목: ① 조건(숫자) ② 그러면 무엇이 유리/불리 ③ 시계 ④ 근거(기저율 n 또는 이웃 결과) "
                   "⑤ 무효화(어떤 값이 나오면 이 함의를 버리나). 다섯이 다 없으면 쓰지 않는다."))
    P.append(_slot("지금 하지 말아야 할 것",
                   "기저율이 동전던지기인 배열로 방향을 부르는 것 같은, 이번 자료가 지지하지 않는 행동."))
    P.append("</section>")

    # 판정
    P.append('<section><span class="num">12</span><h2>트리거 · 레짐 판정</h2>')
    P.append(_slot("트리거 전수 점검 표",
                   "05_Regime 최신 RegimeView의 트리거를 하나씩 대조. 발동/미발동/관측없음과 남은 거리를 숫자로."))
    P.append(_slot("레짐 유지 여부", "바꿀 근거가 없으면 '유지'라고 명시. 매주 새 서사를 만들지 않는다."))
    P.append(_slot("무효화 조건", "숫자로. 현재값과 임계를 나란히. 몇 개가 충족되면 개정하는지."))
    P.append(_slot("다음 세션까지 볼 것 3개", "무엇이 어떻게 나오면 판단이 바뀌는지."))
    P.append("</section>")

    P.append('<details><summary>수치의 한계</summary><div class="col">')
    P.append(_slot("한계", "미검증 주장 · 짧은 표본 · 계수 전용 · 계산 불가 · 단위 함정. "
                          "본문이 아니라 여기에만 쓴다."))
    P.append("</div></details></div>")

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(P), encoding="utf-8")
    unused = [n for n in S if n not in used_keys]
    return {"out": out, "asof": asof, "items": len(items), "filled": filled,
            "charts": len(ch), "papers": sum(len(v) for v in papers.values()),
            "base_n": len(base.get("1개월", [])), "unused": unused, "teams": TEAM,
            "used": used_keys}


def cmd_report(asof: str | None, out: str | None) -> int:
    a = dt.date.fromisoformat(asof) if asof else last_session()
    path = Path(out).expanduser() if out else (OUTPUT_DIR / f"report_{a.isoformat()}.html")
    r = build(a, path)

    print(f"\n스캐폴드 생성  {r['out']}")
    print("=" * 68)
    print(f"  기준 시점(as-of)  {r['asof']}   {'(직전 세션 자동)' if not asof else '(수동 지정)'}")
    print(f"  지표              {r['items']}개 중 {r['filled']}개 수집 · 본문 배치 {len(r['used'])}개")
    print(f"  차트              {r['charts']}개")
    print(f"  문헌 계수         {r['papers']}편 (papers.yaml)")
    print(f"  기저율 표본       n={r['base_n']}")
    print("=" * 68)
    print("  다음: `WRITE:` 슬롯을 채운 뒤")
    print(f"        python -m databook audit {r['out']}")
    print("        게이트를 통과해야 낼 수 있다. 미달이면 exit 1이다.")

    from collections import Counter
    c = Counter(r["teams"].get(n, "?") for n in r["used"])
    print(f"\n  팀 배치  " + " · ".join(f"{k} {v}개" for k, v in sorted(c.items())))
    if r["unused"]:
        print(f"  아직 안 쓴 지표 {len(r['unused'])}개 — `--unused`로 audit에서 확인")
    return 0
