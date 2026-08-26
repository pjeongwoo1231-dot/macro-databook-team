"""중국 — 해관총서(GACC) 무역통계 속보 + 인민은행(PBoC) 월간 금융통계. 키 불필요.

**왜 이 경로인가** — 중국 실물 데이터의 자동 경로는 대부분 막혀 있다(2026-08-26 실측):

| 경로 | 결과 |
|---|---|
| NBS 공식 API(`data.stats.gov.cn/easyquery.htm`) | **403 WAF(UrlACL)** — IP 차단 |
| GACC 통계포털(`stats.customs.gov.cn`) | **412** — 안티봇 |
| PBoC `.../116319/`(통계데이터) 색인 | **JS 렌더** — 링크 안 잡힘 |
| **PBoC `.../116225/`(데이터해석) 색인** | **2026-07까지 정상** ← 월간 TSF는 여기서 나온다(`fetch_pboc`) |
| DBnomics NBS 미러 | 살아 있으나 **2026-02까지(6개월 지연)** |
| **GACC 영문 속보(여기)** | **2026-07까지 정상** ← 중국에서 가장 최신인 자동 경로 |

그래서 이 모듈이 중국 파트에서 **유일하게 당월에 가까운 실측치**를 준다.
게다가 원유·철광석·구리·석탄·가스를 **물량과 금액으로 함께** 주기 때문에
"수입액이 는 게 가격 때문인가 물량 때문인가"를 그 자리에서 가른다 —
중국이 글로벌 원자재 수요의 본체라 이 구분이 곧 원자재 판정이 된다.

**출처**: 색인 http://english.customs.gov.cn/statics/report/preliminary.html
        각 월보 http://english.customs.gov.cn/Statics/<GUID>.html

⚠ **월별 파일명이 GUID다.** 규칙이 없으니 색인 표의 링크를 읽어야 한다.
⚠ **색인의 `<a href=...>`가 따옴표 없이** 나온다(`href=http://...`). 인용부호 있는 형태만
  잡는 정규식으로는 하나도 못 찾는다.
⚠ **표마다 단위가 다르다**: 총액표는 `USD 100 Million`(억달러), 국가별·품목별은
  `USD1 Million`(백만달러). 섞으면 100배 틀린다 — 여기서는 전부 **억달러로 통일**한다.
⚠ 품목표의 물량 단위는 열에 적혀 있다(`10,000 Tons`·`Ton`·`10,000 CBM` 등). 라벨에 그대로 싣는다.
⚠ 속보(preliminary)라 이후 개정된다.
"""
from __future__ import annotations

import html
import re
from typing import Any

from .base import get_text, result

INDEX = "http://english.customs.gov.cn/statics/report/preliminary.html"
_MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
           "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}

# report 키 → 색인 표의 제목에서 찾을 패턴
_REPORTS = {
    "totals": r"\(1\)\s*China's Total Export & Import Values",
    "country": r"\(4\).*by Country/Region",
    "exports": r"\(5\).*Major Exports",
    "imports": r"\(6\).*Major Imports",
}
_index_cache: str | None = None
_page_cache: dict[str, str] = {}


def _clean(s: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def _norm(s: str) -> str:
    """항목 매칭은 **정확일치**로 한다 — 부분일치면 'Copper ores'가
    'Unwrought copper'까지 끌어오거나 그 반대가 된다."""
    return re.sub(r"[^A-Z0-9]", "", html.unescape(str(s)).upper())


def _num(s: str) -> float | None:
    t = str(s).strip().replace(",", "")
    if not t or t in ("-", "—", "…"):
        return None
    try:
        return float(t)
    except ValueError:
        return None


def _index() -> str:
    global _index_cache
    if _index_cache is None:
        _index_cache = get_text(INDEX, encoding="utf-8")
    return _index_cache


def _page(url: str) -> str:
    if url not in _page_cache:
        _page_cache[url] = get_text(url, encoding="utf-8")
    return _page_cache[url]


def _month_links(report: str, currency: str) -> list[str]:
    """색인 표에서 해당 리포트 행을 찾아 월별 링크를 **오래된 달 → 최신 달** 순으로."""
    pat = _REPORTS.get(report)
    if not pat:
        return []
    body = _index()
    body = body[body.find("<table"):]
    want_cur = f"(in {currency.upper()})"
    for row in re.findall(r"<tr>(.*?)</tr>", body, re.S):
        cells = re.findall(r"<td>(.*?)</td>", row, re.S)
        if len(cells) < 2:
            continue
        title = _clean(cells[0])
        if not re.search(pat, title) or want_cur not in title:
            continue
        # ⚠ href에 따옴표가 없다
        return [h for h in re.findall(r"href=[\"']?([^\"'\s>]+)", cells[1])]
    return []


def _period(page: str) -> str:
    """페이지 제목의 'Jul 2026' → '2026-07'."""
    head = _clean(page[:page.find("window.dataLayer")] if "window.dataLayer" in page else page[:2000])
    m = re.search(r"([A-Za-z]{3})[a-z]*\.?\s+(\d{4})", head)
    if not m:
        return ""
    mon = _MONTHS.get(m.group(1).lower())
    return f"{m.group(2)}-{mon:02d}" if mon else ""


def _rows(page: str) -> list[list[str]]:
    out = []
    for r in re.findall(r"<tr[^>]*>(.*?)</tr>", page, re.S):
        cells = [_clean(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, re.S)]
        if cells:
            out.append(cells)
    return out


def fetch_gacc(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """yaml 예시:
        method: api
        source: gacc
        report: imports          # totals | country | imports | exports
        currency: USD            # USD | CNY (기본 USD)
        items: ["Crude petroleum oils", "Iron ores and concentrates"]   # 표기와 정확일치
        months: 3
        quantity: true           # 품목표에서 물량도 함께
    """
    report = str(ind.get("report") or "totals").lower()
    currency = str(ind.get("currency") or "USD").upper()
    months = int(ind.get("months") or 3)
    items = {_norm(x) for x in (ind.get("items") or [])}
    want_qty = bool(ind.get("quantity"))

    links = _month_links(report, currency)
    if not links:
        return result(ind, "fail", error=f"색인에서 리포트를 못 찾음(report={report}, {currency})",
                      source_url=INDEX)
    links = links[-months:][::-1]                      # 최신 달부터

    obs: list[dict[str, Any]] = []
    errors: list[str] = []
    for url in links:
        try:
            page = _page(url)
        except Exception as e:
            errors.append(f"{url[-20:]}: {type(e).__name__}")
            continue
        d = _period(page)
        if not d:
            errors.append(f"{url[-20:]}: 기간 파싱 실패")
            continue
        for cells in _rows(page):
            name = cells[0]
            if not name or name.startswith("("):
                continue
            if report == "totals":
                # [항목, 당월액, 누계액, 전월비%, 전년동월비%, 누계 전년비%] — 단위 억달러
                if len(cells) < 5 or _norm(name) not in {
                        _norm(x) for x in ("Total Export & Import", "Total Export",
                                           "Total Import", "Export-Import Balance")}:
                    continue
                v = _num(cells[1])
                if v is not None:
                    obs.append({"date": d, "value": round(v, 1), "label": f"{name} (억달러)"})
                yoy = _num(cells[4]) if len(cells) > 4 else None
                if yoy is not None:
                    obs.append({"date": d, "value": yoy, "label": f"{name} 전년동월비(%)"})
            elif report == "country":
                # [국가, 당월 수출입, 누계 수출입, 당월 수출, 누계 수출, 당월 수입, 누계 수입,
                #  누계YoY 수출입%, 수출%, 수입%] — 단위 백만달러 → 억달러
                if len(cells) < 10 or (items and _norm(name) not in items):
                    continue
                for idx, tag in ((3, "수출"), (5, "수입")):
                    v = _num(cells[idx])
                    if v is not None:
                        obs.append({"date": d, "value": round(v / 100, 1),
                                    "label": f"{name} {tag}(억달러)"})
                for idx, tag in ((8, "수출"), (9, "수입")):
                    v = _num(cells[idx])
                    if v is not None:
                        obs.append({"date": d, "value": v,
                                    "label": f"{name} {tag} 누계 전년비(%)"})
            else:
                # [품목, 물량단위, 당월물량, 당월금액, 누계물량, 누계금액,
                #  전년누계물량, 전년누계금액, 누계YoY 물량%, 누계YoY 금액%] — 금액 백만달러
                if len(cells) < 10 or (items and _norm(name) not in items):
                    continue
                unit = cells[1]
                val = _num(cells[3])
                if val is not None:
                    obs.append({"date": d, "value": round(val / 100, 1),
                                "label": f"{name} 금액(억달러)"})
                qv = _num(cells[8])
                if qv is not None:
                    obs.append({"date": d, "value": qv, "label": f"{name} 물량 누계 전년비(%)"})
                vv = _num(cells[9])
                if vv is not None:
                    obs.append({"date": d, "value": vv, "label": f"{name} 금액 누계 전년비(%)"})
                if want_qty:
                    q = _num(cells[2])
                    if q is not None:
                        obs.append({"date": d, "value": q,
                                    "label": f"{name} 물량({unit or 'n/a'})"})

    if not obs:
        return result(ind, "fail",
                      error=f"항목을 찾지 못함(report={report}, items={sorted(items)}) — "
                            f"표기와 정확일치해야 한다" + ("; " + "; ".join(errors) if errors else ""),
                      source_url=links[0] if links else INDEX)
    res = result(ind, "ok", observations=obs, source_url=links[0])
    if errors:
        res["error"] = "; ".join(errors)
    return res


# ═══════════════════ 중국인민은행(PBoC) 월간 금융통계 — 사회융자총량(TSF) ═══════════════════
"""**왜 이게 중요한가** — TSF(社会融资规模)는 중국 신용사이클의 본체이고, 글로벌 원자재·성장의
선행 재료다. 그런데 **2026-07 시점 판정은 "자동화 불가"였다** — PBoC가 매월 URL이 바뀌는
리포트로만 낸다는 이유였다.

**그 판정은 색인 페이지를 잘못 본 결과였다.** `.../116219/116319/`(통계데이터)는 JS로 그려져
링크가 안 잡히지만, **`.../116219/116225/`(데이터해석)는 서버 렌더**라 월보 링크가 그대로 있다.
2026-08-26 재검증에서 2026-07 보고까지 정상 수집됨을 확인했다.

**출처**: https://www.pbc.gov.cn/diaochatongjisi/116219/116225/index.html

⚠ **http는 302로 튕긴다. https만 쓴다.**
⚠ **월 이름이 분기·반기로 바뀐다**: 3월분은 「一季度」, 6월분은 「上半年」, 9월분은 「三季度」,
  12월분은 「2025年金融统计数据报告」(월 표기 없음)로 나온다. 제목을 그대로 믿고 파싱한다.
⚠ **문장에서 숫자를 뽑는다.** 표가 아니라 산문이라, 앵커 문구를 정확히 잡아야 한다.
  특히 `人民币贷款余额`는 **두 번** 나온다 — 앞의 것은 TSF 하위항목
  (`对实体经济发放的人民币贷款余额`), 뒤의 것이 총잔액(`月末人民币贷款余额`)이다.
  앵커 없이 첫 매치를 쓰면 **다른 지표를 그 이름으로 싣게 된다**(실제로 겪었다).
⚠ `同比增长`(증가)과 `同比下降`(감소)이 둘 다 나온다 — 부호를 뒤집어야 한다.
"""

PBOC_INDEX = "https://www.pbc.gov.cn/diaochatongjisi/116219/116225/index.html"
PBOC_BASE = "https://www.pbc.gov.cn"
_pboc_cache: dict[str, str] = {}

# (라벨, 정규식) — 값과 전년비를 함께 뽑는다. 그룹: (금액, 增长|下降, 전년비)
_PBOC_PATS: list[tuple[str, str, str]] = [
    ("사회융자총량 TSF 존량", "조위안", r"社会融资规模存量为([\d.]+)万亿元[，,]\s*同比(增长|下降)([\d.]+)%"),
    ("M2", "조위안", r"广义货币[（(]M2[）)]余额([\d.]+)万亿元[，,]\s*同比(增长|下降)([\d.]+)%"),
    ("M1", "조위안", r"狭义货币[（(]M1[）)]余额([\d.]+)万亿元[，,]\s*同比(增长|下降)([\d.]+)%"),
    ("실체경제 위안화대출", "조위안", r"对实体经济发放的人民币贷款余额([\d.]+)万亿元[，,]\s*同比(增长|下降)([\d.]+)%"),
    ("위안화대출 총잔액", "조위안", r"月末人民币贷款余额([\d.]+)万亿元[，,]\s*同比(增长|下降)([\d.]+)%"),
    ("정부채권 잔액", "조위안", r"政府债券余额([\d.]+)万亿元[，,]\s*同比(增长|下降)([\d.]+)%"),
]
_PBOC_FLOW = r"社会融资规模增量累计为([\d.]+)万亿元"
_PBOC_TITLE = re.compile(r"(\d{4})年(上半年|一季度|三季度|\d{1,2}月|)金融统计数据报告")


def _pboc_period(title: str) -> str:
    m = _PBOC_TITLE.search(title)
    if not m:
        return ""
    year, part = m.group(1), m.group(2)
    if part.endswith("月"):
        return f"{year}-{int(part[:-1]):02d}"
    return {"一季度": f"{year}-03", "上半年": f"{year}-06",
            "三季度": f"{year}-09", "": f"{year}-12"}.get(part, "")


def _pboc_text(url: str) -> str:
    if url not in _pboc_cache:
        raw = get_text(url, encoding="utf-8")
        raw = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
        _pboc_cache[url] = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    return _pboc_cache[url]


def fetch_pboc(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """yaml 예시:
        method: api
        source: pboc
        months: 4          # 최근 보고 N개 (월보 1건 = 1회 요청)
    """
    months = int(ind.get("months") or 4)
    try:
        idx = get_text(PBOC_INDEX, encoding="utf-8")
    except Exception as e:
        return result(ind, "fail", error=f"PBoC 색인 {type(e).__name__}: {e}", source_url=PBOC_INDEX)

    reports: list[tuple[str, str]] = []          # (기간, url)
    for href, label in re.findall(r"<a[^>]+href=[\"']?([^\"'\s>]+)[^>]*>(.*?)</a>", idx, re.S):
        title = _clean(label)
        d = _pboc_period(title)
        if d and not any(d == p for p, _ in reports):
            reports.append((d, href if href.startswith("http") else PBOC_BASE + href))
    if not reports:
        return result(ind, "fail", error="색인에서 금융통계 보고를 못 찾음(페이지 구조 변경 의심)",
                      source_url=PBOC_INDEX)
    reports.sort(reverse=True)
    reports = reports[:months]

    obs: list[dict[str, Any]] = []
    errors: list[str] = []
    for d, url in reports:
        try:
            txt = _pboc_text(url)
        except Exception as e:
            errors.append(f"{d}: {type(e).__name__}")
            continue
        for label, unit, pat in _PBOC_PATS:
            m = re.search(pat, txt)
            if not m:
                continue
            val, direction, yoy = m.group(1), m.group(2), m.group(3)
            obs.append({"date": d, "value": float(val), "label": f"{label}({unit})"})
            sign = -1 if direction == "下降" else 1
            obs.append({"date": d, "value": round(sign * float(yoy), 1),
                        "label": f"{label} 전년비(%)"})
        mf = re.search(_PBOC_FLOW, txt)
        if mf:
            obs.append({"date": d, "value": float(mf.group(1)),
                        "label": "TSF 연초누계 증량(조위안)"})
    if not obs:
        return result(ind, "fail",
                      error="본문에서 수치를 못 뽑음(문구 변경 의심) — " + "; ".join(errors),
                      source_url=reports[0][1])
    res = result(ind, "ok", observations=obs, source_url=reports[0][1])
    if errors:
        res["error"] = "; ".join(errors)
    return res
