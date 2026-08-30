"""표에 있는 값으로 **인라인 SVG**를 그린다.

왜 이 모듈이 있나 — 시황 자료가 숫자 표만 늘어놓으면 읽히지 않는다.
「좋은 시황의 규칙」이 요구하는 **추세**(어디서 어디로 갔나)는 그림이라야 전달된다.

원칙
 - **외부 의존 0.** matplotlib도 CDN도 쓰지 않는다. 순수 문자열로 SVG를 만든다.
   산출물이 단일 HTML에 그대로 박혀야 하기 때문이다(Artifact·오프라인 배포).
 - **데이터에 없는 것은 그리지 않는다.** 결측은 선을 끊고, 구간이 짧으면 그 사실을 라벨에 쓴다.
 - **다크모드에서 살아남게.** 색을 고정하지 않고 `currentColor`와 CSS 변수를 쓴다.
 - **음수는 색이 아니라 위치와 부호로** 구분한다(색각 이상 고려).
"""
from __future__ import annotations

import datetime as dt
from pathlib import Path

Num = float | int


def _esc(s: str) -> str:
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _fmt(v: Num, nd: int = 2) -> str:
    return f"{v:,.{nd}f}".rstrip("0").rstrip(".") if nd else f"{v:,.0f}"


def line(series: list[tuple[dt.date, float]], *, title: str, unit: str = "",
         w: int = 720, h: int = 220, mark_last: bool = True,
         bands: list[tuple[float, float, str]] | None = None) -> str:
    """시계열 선 그래프. `series`는 (날짜, 값) 오름차순.

    `bands`는 [(y0, y1, 라벨)] — 임계 구간을 음영으로 깔 때 쓴다.
    """
    if len(series) < 2:
        return f'<p class="chart-missing">{_esc(title)} — 점이 부족해 그리지 않는다({len(series)}개)</p>'
    pad_l, pad_r, pad_t, pad_b = 52, 58, 26, 26
    xs = [d.toordinal() for d, _ in series]
    ys = [v for _, v in series]
    x0, x1 = min(xs), max(xs)
    y0, y1 = min(ys), max(ys)
    if y1 == y0:
        y0, y1 = y0 - 1, y1 + 1
    m = (y1 - y0) * 0.12
    y0, y1 = y0 - m, y1 + m

    def px(x): return pad_l + (x - x0) / (x1 - x0) * (w - pad_l - pad_r)
    def py(y): return pad_t + (y1 - y) / (y1 - y0) * (h - pad_t - pad_b)

    out = [f'<figure class="chart"><svg viewBox="0 0 {w} {h}" role="img" '
           f'aria-label="{_esc(title)}" preserveAspectRatio="xMidYMid meet">']

    for by0, by1, lab in (bands or []):
        a, b = py(max(by0, by1)), py(min(by0, by1))
        out.append(f'<rect x="{pad_l}" y="{a:.1f}" width="{w-pad_l-pad_r}" '
                   f'height="{max(b-a,0.5):.1f}" class="chart-band"/>')
        out.append(f'<text x="{w-pad_r+4}" y="{(a+b)/2+3:.1f}" class="chart-band-lab">{_esc(lab)}</text>')

    # y축 눈금 3개
    for t in (0.0, 0.5, 1.0):
        yv = y0 + (y1 - y0) * t
        Y = py(yv)
        out.append(f'<line x1="{pad_l}" y1="{Y:.1f}" x2="{w-pad_r}" y2="{Y:.1f}" class="chart-grid"/>')
        out.append(f'<text x="{pad_l-6}" y="{Y+4:.1f}" class="chart-tick" text-anchor="end">{_fmt(yv)}</text>')

    pts = " ".join(f"{px(x):.1f},{py(y):.1f}" for x, y in zip(xs, ys))
    out.append(f'<polyline points="{pts}" class="chart-line"/>')

    # x축 양끝 날짜
    out.append(f'<text x="{pad_l}" y="{h-8}" class="chart-tick">{series[0][0]}</text>')
    out.append(f'<text x="{w-pad_r}" y="{h-8}" class="chart-tick" text-anchor="end">{series[-1][0]}</text>')

    if mark_last:
        lx, ly = px(xs[-1]), py(ys[-1])
        out.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="3.5" class="chart-dot"/>')
        out.append(f'<text x="{lx+6:.1f}" y="{ly-7:.1f}" class="chart-last">{_fmt(ys[-1])}{_esc(unit)}</text>')

    out.append("</svg>")
    out.append(f'<figcaption>{_esc(title)}</figcaption></figure>')
    return "".join(out)


def diverging(rows: list[tuple[str, float]], *, title: str, unit: str = "bp",
              w: int = 720, row_h: int = 26) -> str:
    """0을 기준으로 좌우로 뻗는 막대. **부호가 갈리는 것**을 보이려고 쓴다."""
    if not rows:
        return f'<p class="chart-missing">{_esc(title)} — 값이 없다</p>'
    pad_l, pad_r, pad_t = 132, 56, 22
    h = pad_t + row_h * len(rows) + 12
    span = max(abs(v) for _, v in rows) or 1.0
    mid = pad_l + (w - pad_l - pad_r) / 2
    half = (w - pad_l - pad_r) / 2

    out = [f'<figure class="chart"><svg viewBox="0 0 {w} {h}" role="img" '
           f'aria-label="{_esc(title)}" preserveAspectRatio="xMidYMid meet">']
    out.append(f'<line x1="{mid}" y1="{pad_t-6}" x2="{mid}" y2="{h-8}" class="chart-zero"/>')
    for k, (lab, v) in enumerate(rows):
        y = pad_t + row_h * k + row_h / 2
        L = abs(v) / span * (half - 8)
        x = mid if v >= 0 else mid - L
        cls = "chart-bar-pos" if v >= 0 else "chart-bar-neg"
        out.append(f'<text x="{pad_l-10}" y="{y+4:.1f}" class="chart-tick" text-anchor="end">{_esc(lab)}</text>')
        out.append(f'<rect x="{x:.1f}" y="{y-7:.1f}" width="{L:.1f}" height="14" class="{cls}"/>')
        tx = mid + L + 6 if v >= 0 else mid - L - 6
        anc = "start" if v >= 0 else "end"
        out.append(f'<text x="{tx:.1f}" y="{y+4:.1f}" class="chart-val" text-anchor="{anc}">'
                   f'{v:+,.1f}{_esc(unit)}</text>')
    out.append(f"</svg><figcaption>{_esc(title)}</figcaption></figure>")
    return "".join(out)


def percentile(rows: list[tuple[str, float, float, str]], *, title: str,
               w: int = 720, row_h: int = 34) -> str:
    """0~100 백분위 띠 위에 현재 위치를 점으로. rows=(라벨, 값, 백분위, 표본설명)."""
    if not rows:
        return f'<p class="chart-missing">{_esc(title)} — 값이 없다</p>'
    pad_l, pad_r, pad_t = 148, 118, 24
    h = pad_t + row_h * len(rows) + 14
    bw = w - pad_l - pad_r
    out = [f'<figure class="chart"><svg viewBox="0 0 {w} {h}" role="img" '
           f'aria-label="{_esc(title)}" preserveAspectRatio="xMidYMid meet">']
    for k, (lab, val, p, note) in enumerate(rows):
        y = pad_t + row_h * k + row_h / 2
        out.append(f'<text x="{pad_l-10}" y="{y+4:.1f}" class="chart-tick" text-anchor="end">{_esc(lab)}</text>')
        out.append(f'<rect x="{pad_l}" y="{y-6:.1f}" width="{bw}" height="12" rx="6" class="chart-track"/>')
        for q in (25, 50, 75):
            X = pad_l + bw * q / 100
            out.append(f'<line x1="{X:.1f}" y1="{y-6:.1f}" x2="{X:.1f}" y2="{y+6:.1f}" class="chart-qtick"/>')
        X = pad_l + bw * max(0.0, min(100.0, p)) / 100
        out.append(f'<circle cx="{X:.1f}" cy="{y:.1f}" r="6" class="chart-dot"/>')
        out.append(f'<text x="{w-pad_r+8}" y="{y+4:.1f}" class="chart-val">'
                   f'{_fmt(val)} · {p:.0f}%ile</text>')
        out.append(f'<text x="{w-pad_r+8}" y="{y+15:.1f}" class="chart-note">{_esc(note)}</text>')
    out.append(f'<text x="{pad_l}" y="{h-4}" class="chart-tick">0</text>')
    out.append(f'<text x="{pad_l+bw}" y="{h-4}" class="chart-tick" text-anchor="end">100</text>')
    out.append(f"</svg><figcaption>{_esc(title)}</figcaption></figure>")
    return "".join(out)


def dotplot(values: list[float], *, title: str, unit: str = "%",
            marks: list[tuple[float, str]] | None = None,
            w: int = 720, h: int = 150) -> str:
    """기저율 분포를 점으로 뿌린다. 중앙값과 0선을 함께 긋는다."""
    if not values:
        return f'<p class="chart-missing">{_esc(title)} — 표본이 없다</p>'
    pad_l, pad_r, pad_t, pad_b = 46, 46, 30, 34
    lo, hi = min(values), max(values)
    if hi == lo:
        lo, hi = lo - 1, hi + 1
    m = (hi - lo) * 0.08
    lo, hi = lo - m, hi + m

    def px(v): return pad_l + (v - lo) / (hi - lo) * (w - pad_l - pad_r)

    srt = sorted(values)
    med = srt[len(srt) // 2] if len(srt) % 2 else (srt[len(srt)//2-1] + srt[len(srt)//2]) / 2
    neg = sum(1 for v in values if v < 0)

    out = [f'<figure class="chart"><svg viewBox="0 0 {w} {h}" role="img" '
           f'aria-label="{_esc(title)}" preserveAspectRatio="xMidYMid meet">']
    band = h - pad_t - pad_b
    # 점을 세로로 흩어 겹침을 줄인다(결정적 배치 — 난수를 쓰지 않는다)
    for k, v in enumerate(values):
        y = pad_t + band * (0.5 + 0.34 * ((k % 7) - 3) / 3)
        cls = "chart-pt-neg" if v < 0 else "chart-pt-pos"
        out.append(f'<circle cx="{px(v):.1f}" cy="{y:.1f}" r="3" class="{cls}"/>')
    if lo < 0 < hi:
        out.append(f'<line x1="{px(0):.1f}" y1="{pad_t-6}" x2="{px(0):.1f}" y2="{h-pad_b+6}" class="chart-zero"/>')
        out.append(f'<text x="{px(0):.1f}" y="{pad_t-10}" class="chart-tick" text-anchor="middle">0</text>')
    out.append(f'<line x1="{px(med):.1f}" y1="{pad_t-2}" x2="{px(med):.1f}" y2="{h-pad_b+2}" class="chart-med"/>')
    out.append(f'<text x="{px(med):.1f}" y="{h-pad_b+20}" class="chart-val" text-anchor="middle">'
               f'중앙값 {med:+.1f}{_esc(unit)}</text>')
    for mv, ml in (marks or []):
        out.append(f'<line x1="{px(mv):.1f}" y1="{pad_t-2}" x2="{px(mv):.1f}" y2="{h-pad_b+2}" class="chart-mark"/>')
        out.append(f'<text x="{px(mv):.1f}" y="{pad_t-10}" class="chart-val" text-anchor="middle">{_esc(ml)}</text>')
    out.append(f'<text x="{pad_l}" y="{h-6}" class="chart-tick">{_fmt(lo)}{_esc(unit)}</text>')
    out.append(f'<text x="{w-pad_r}" y="{h-6}" class="chart-tick" text-anchor="end">{_fmt(hi)}{_esc(unit)}</text>')
    out.append(f"</svg><figcaption>{_esc(title)} · n={len(values)} · "
               f"음(−) {neg}/{len(values)} ({neg/len(values)*100:.0f}%)</figcaption></figure>")
    return "".join(out)


def mirror(rows: list[tuple[str, float, float]], *, title: str,
           labels: tuple[str, str] = ("위", "아래"), w: int = 720, h: int = 210) -> str:
    """방향이 반대인 두 계열을 위아래 대칭 막대로. rows=(라벨, 위값, 아래값)."""
    if not rows:
        return f'<p class="chart-missing">{_esc(title)} — 값이 없다</p>'
    pad_t, pad_b, pad_l, pad_r = 26, 40, 40, 20
    mid = pad_t + (h - pad_t - pad_b) / 2
    span = max(max(abs(a), abs(b)) for _, a, b in rows) or 1.0
    bw = (w - pad_l - pad_r) / len(rows)
    half = (h - pad_t - pad_b) / 2 - 6
    out = [f'<figure class="chart"><svg viewBox="0 0 {w} {h}" role="img" '
           f'aria-label="{_esc(title)}" preserveAspectRatio="xMidYMid meet">']
    out.append(f'<line x1="{pad_l}" y1="{mid:.1f}" x2="{w-pad_r}" y2="{mid:.1f}" class="chart-zero"/>')
    for k, (lab, a, b) in enumerate(rows):
        cx = pad_l + bw * (k + 0.5)
        for v, cls in ((a, "chart-bar-pos"), (b, "chart-bar-neg")):
            L = abs(v) / span * half
            y = mid - L if v >= 0 else mid
            out.append(f'<rect x="{cx-bw*0.3:.1f}" y="{y:.1f}" width="{bw*0.6:.1f}" '
                       f'height="{max(L,0.5):.1f}" class="{cls}"/>')
        out.append(f'<text x="{cx:.1f}" y="{h-14}" class="chart-tick" text-anchor="middle">{_esc(lab)}</text>')
    out.append(f'<text x="{pad_l}" y="{pad_t-8}" class="chart-note">{_esc(labels[0])}</text>')
    out.append(f'<text x="{pad_l}" y="{h-26}" class="chart-note">{_esc(labels[1])}</text>')
    out.append(f"</svg><figcaption>{_esc(title)}</figcaption></figure>")
    return "".join(out)


CSS = """
.chart{margin:1.4rem 0;overflow-x:auto}
.chart svg{width:100%;height:auto;display:block}
.chart figcaption{font-size:.82rem;color:var(--muted,#667);margin-top:.35rem}
.chart-missing{font-size:.85rem;color:var(--muted,#667);font-style:italic}
.chart-line{fill:none;stroke:var(--ink,#123);stroke-width:1.8}
.chart-grid{stroke:var(--rule,#d8dde3);stroke-width:1;stroke-dasharray:2 3}
.chart-zero{stroke:var(--ink,#123);stroke-width:1.2}
.chart-med{stroke:var(--ink,#123);stroke-width:1.4;stroke-dasharray:4 3}
.chart-mark{stroke:var(--accent,#a33);stroke-width:1.6}
.chart-tick,.chart-note{font-size:11px;fill:var(--muted,#667)}
.chart-val,.chart-last{font-size:12px;fill:var(--ink,#123);font-variant-numeric:tabular-nums}
.chart-band{fill:var(--rule,#d8dde3);opacity:.35}
.chart-band-lab{font-size:10px;fill:var(--muted,#667)}
.chart-track{fill:var(--rule,#d8dde3);opacity:.5}
.chart-qtick{stroke:var(--bg,#fff);stroke-width:1}
.chart-dot{fill:var(--ink,#123)}
.chart-bar-pos{fill:var(--ink,#123);opacity:.85}
.chart-bar-neg{fill:var(--ink,#123);opacity:.4}
.chart-pt-pos{fill:var(--ink,#123);opacity:.7}
.chart-pt-neg{fill:var(--ink,#123);opacity:.7;stroke:var(--accent,#a33);stroke-width:1.4}
"""


def demo_out(html_body: str, title: str, out: Path) -> Path:
    """만든 그림을 눈으로 확인하려고 단일 HTML로 떨군다(검수용)."""
    out.write_text(
        "<!doctype html><meta charset='utf-8'>"
        f"<title>{_esc(title)}</title><style>"
        ":root{--bg:#fff;--ink:#14202c;--muted:#5b6874;--rule:#d8dde3;--accent:#a3302c}"
        "@media(prefers-color-scheme:dark){:root{--bg:#12161a;--ink:#e6ecf2;"
        "--muted:#93a1ad;--rule:#2a323b;--accent:#e0736c}}"
        "body{background:var(--bg);color:var(--ink);font:15px/1.7 -apple-system,"
        "'Segoe UI','Malgun Gothic',sans-serif;max-width:820px;margin:2rem auto;padding:0 1rem}"
        + CSS + "</style>" + html_body, encoding="utf-8")
    return out
