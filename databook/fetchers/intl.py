"""국제기구·해외 중앙은행 fetcher — DBnomics · BCB(브라질) · BOJ 통계 · Fed RSS · CBR(러시아) · PBOC LPR(중국).
전부 무료·키 불필요. 시리즈 코드는 2026-07-18~19 실호출로 검증됨."""
from __future__ import annotations

import datetime
import re
import urllib.request
from typing import Any

from .base import BROWSER_UA, get_json, get_text, result

N_OBS = 6


def _dbn_yoy(pairs: list[tuple[str, float]]) -> list[tuple[str, float]]:
    """레벨 → 전년비(%). 기간키를 직접 대조한다 — 결측이 섞여도 어긋나지 않게.
    DBnomics 기간 표기는 월차 'YYYY-MM' · 분기 'YYYY-Qn' · 연차 'YYYY'."""
    by = {str(p): v for p, v in pairs}
    out: list[tuple[str, float]] = []
    for p, v in pairs:
        s = str(p)
        if len(s) >= 7 and s[4] == "-":          # YYYY-MM · YYYY-Qn
            prev = f"{int(s[:4]) - 1:04d}{s[4:]}"
        elif len(s) == 4 and s.isdigit():        # YYYY
            prev = f"{int(s) - 1:04d}"
        else:
            continue
        base = by.get(prev)
        if base in (None, 0):
            continue
        out.append((p, round((v / base - 1) * 100, 2)))
    return out


def fetch_dbnomics(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """DBnomics 애그리게이터 — db_series: 'PROVIDER/DATASET/SERIES' (str 또는 리스트).

    `yoy: true`를 주면 레벨 계열을 **전년비(%)로 환산**한다. 지수 계열(예: STATJP CPI)은
    원본이 지수 레벨뿐이라 그대로 쓰면 "113.6"만 남고 2% 목표와 대조할 수 없다.
    계산분임을 라벨에 남긴다 — 기관 공표 전년비와 반올림에서 갈릴 수 있다.
    """
    series = ind.get("db_series")
    if not series:
        return result(ind, "fail", error="db_series 미지정")
    if isinstance(series, str):
        series = [series]
    labels = ind.get("db_labels") or []
    yoy = bool(ind.get("yoy"))
    all_obs: list[dict[str, Any]] = []
    urls: list[str] = []
    errors: list[str] = []
    for i, sid in enumerate(series):
        try:
            d = get_json(f"https://api.db.nomics.world/v22/series/{sid}?observations=1")
            doc = d["series"]["docs"][0]
            label = labels[i] if i < len(labels) else str(doc.get("series_name", sid))[:40]
            pairs = [(p, v) for p, v in zip(doc.get("period", []), doc.get("value", []))
                     if isinstance(v, (int, float))]
            if yoy:
                pairs = _dbn_yoy(pairs)
                label = f"{label} 전년비(%) — 계산"
                if not pairs:
                    errors.append(f"{sid}: 전년비 계산 불가(1년 전 관측 부족)")
                    continue
            for p, v in pairs[-N_OBS:][::-1]:
                all_obs.append({"date": str(p), "value": round(float(v), 2), "label": label})
            urls.append(f"https://db.nomics.world/{sid}")
        except Exception as e:
            errors.append(f"{sid}: {type(e).__name__}: {e}")
    if not all_obs:
        return result(ind, "fail", error="; ".join(errors) or "관측치 없음")
    res = result(ind, "ok", observations=all_obs, source_url=" ".join(urls))
    if errors:
        res["error"] = "; ".join(errors)
    return res


def fetch_bcb(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """브라질중앙은행 SGS API — sgs: 시리즈 번호 (432 = Selic 목표금리)."""
    sgs = ind.get("sgs", 432)
    rows = get_json(f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{sgs}/dados/ultimos/{N_OBS}?formato=json")
    obs = []
    for r in reversed(rows):
        d, m, y = str(r["data"]).split("/")
        obs.append({"date": f"{y}-{m}-{d}", "value": float(r["valor"]), "label": f"BCB SGS {sgs}"})
    if not obs:
        return result(ind, "fail", error="관측치 없음")
    return result(ind, "ok", observations=obs,
                  source_url=f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{sgs}/dados")


def fetch_boj_m2(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """일본은행 stat-search 월보 페이지 — M2 전년비(%) 스크레이프."""
    url = "https://www.stat-search.boj.or.jp/ssi/mtshtml/md02_m_1_en.html"
    txt = get_text(url)
    rows = re.findall(r"(20\d\d/\d\d)[^0-9\-]*(-?[0-9][0-9,]*\.?\d*)", txt)
    if not rows:
        return result(ind, "fail", error="M2 표 파싱 실패 (페이지 구조 변경 가능성)")
    obs = []
    for period, val in rows[-N_OBS:][::-1]:
        obs.append({"date": period.replace("/", "-"), "value": float(val.replace(",", "")),
                    "label": "일본 M2 전년비(%)"})
    return result(ind, "ok", observations=obs, source_url=url)


def fetch_boj_rate(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """일본은행 stat-search 기준대출금리(Basic Loan Rate, 舊공정할인율) 월보 스크레이프.
    BOJ의 실제 정책금리(무담보콜금리 목표)는 stat-search에 깔끔한 시계열 페이지가 없어,
    정책 변경 시 함께 조정되는 기준대출금리를 프록시로 쓴다 (SONIA를 BOE 정책금리 프록시로 쓰는 것과 동일 패턴).
    FRED(OECD MEI)가 2023-12에서 갱신 중단된 것을 대체."""
    url = "https://www.stat-search.boj.or.jp/ssi/mtshtml/ir01_m_1_en.html"
    txt = get_text(url)
    rows = re.findall(r"(20\d\d/\d\d)[^0-9\-]*(-?[0-9][0-9,]*\.?\d*)", txt)
    if not rows:
        return result(ind, "fail", error="기준대출금리 표 파싱 실패 (페이지 구조 변경 가능성)")
    obs = []
    for period, val in rows[-N_OBS:][::-1]:
        obs.append({"date": period.replace("/", "-"), "value": float(val.replace(",", "")),
                    "label": "일본 기준대출금리(%) — BOJ 정책금리 프록시"})
    return result(ind, "ok", observations=obs, source_url=url,
                  note="기준대출금리(Basic Loan Rate) — 정책금리 변경과 연동되는 공식 BOJ 프록시. 정밀 값은 boj.or.jp 성명 참조")


def fetch_cbr_keyrate(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """러시아중앙은행(CBR) 기준금리 — DailyInfo SOAP(KeyRate). 무료·키 불필요.
    2026-07-19 실호출 검증(최신 14.25%). 제재 이후 FRED/OECD 경로 단종분 대체."""
    today = datetime.date.today()
    start = today - datetime.timedelta(days=120)
    body = (
        '<?xml version="1.0" encoding="utf-8"?>'
        '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body>'
        '<KeyRate xmlns="http://web.cbr.ru/">'
        f"<fromDate>{start:%Y-%m-%d}</fromDate><ToDate>{today:%Y-%m-%d}</ToDate>"
        "</KeyRate></soap:Body></soap:Envelope>"
    ).encode()
    req = urllib.request.Request(
        "https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx",
        data=body,
        headers={"User-Agent": BROWSER_UA, "Content-Type": "text/xml; charset=utf-8",
                 "SOAPAction": "http://web.cbr.ru/KeyRate"},
    )
    with urllib.request.urlopen(req, timeout=25) as resp:
        txt = resp.read().decode("utf-8", "replace")
    dates = re.findall(r"<DT>([^<]+)</DT>", txt)
    rates = re.findall(r"<Rate>([\d.]+)</Rate>", txt)
    pairs = sorted(((d[:10], float(r)) for d, r in zip(dates, rates)), reverse=True)  # 최신순
    if not pairs:
        return result(ind, "fail", error="KeyRate 파싱 실패(SOAP 응답 구조 변경 가능성)")
    obs = [{"date": d, "value": v, "label": "CBR 기준금리(%)"} for d, v in pairs[:N_OBS]]
    return result(ind, "ok", observations=obs, source_url="https://www.cbr.ru/eng/hd_base/keyrate/")


def fetch_pboc_lpr(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """중국 대출우대금리(LPR) 1Y·5Y — 전국은행간자금센터(chinamoney) 공식 JSON. 무료·키 불필요.
    2026-07-19 실호출 검증(1Y 3.00 / 5Y 3.50). OECD MEI에 중국 정책금리 시계열 없어 수동이던 항목 대체."""
    url = ("https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/LprHis"
           "?lang=CN&startDate=&endDate=&pageNum=1&pageSize=6")
    data = get_json(url, headers={"Referer": "https://www.chinamoney.com.cn/english/bmklpr/"})
    records = data.get("records") or []
    obs: list[dict[str, Any]] = []
    for rec in records[:N_OBS]:
        date = str(rec.get("showDateCN", ""))[:10]
        for term in ("1Y", "5Y"):
            val = rec.get(term)
            if val not in (None, "", "---"):
                obs.append({"date": date, "value": float(val), "label": f"LPR {term}(%)"})
    if not obs:
        return result(ind, "fail", error="LPR 레코드 없음(응답 구조 변경 가능성)")
    return result(ind, "ok", observations=obs,
                  source_url="https://www.chinamoney.com.cn/english/bmklpr/")


def fetch_fed_rss(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """연준 RSS — feed: press_monetary(FOMC 통화정책 보도자료) | speeches(연설).
    수치가 아니라 최신 제목·날짜·링크를 자동 수집한다. 스탠스 해석은 사람 몫."""
    feed = ind.get("feed", "press_monetary")
    url = f"https://www.federalreserve.gov/feeds/{feed}.xml"
    txt = get_text(url)
    items = re.findall(r"<item>(.*?)</item>", txt, re.S)
    obs = []
    months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
              "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    def _cdata(tag: str, src: str) -> str:
        m = re.search(rf"<{tag}>\s*(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?\s*</{tag}>", src, re.S)
        return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""

    for item in items[:3]:
        title = _cdata("title", item).replace("&#39;", "'").replace("&amp;", "&") or "(제목 없음)"
        link = _cdata("link", item)
        d = re.search(r"(\d+)\s+(\w+)\s+(\d{4})", _cdata("pubDate", item))
        date = f"{d.group(3)}-{months.get(d.group(2), '01')}-{int(d.group(1)):02d}" if d else ""
        obs.append({"date": date, "value": title, "label": link})
    if not obs:
        return result(ind, "fail", error="RSS 항목 없음")
    return result(ind, "ok", observations=obs, source_url=url,
                  note=(ind.get("note", "") + " — 링크는 각 항목 label 참조").strip(" —"))

def fetch_mof_jgb(ind: dict, env: dict) -> dict:
    """일본 재무성 공개 CSV — JGB 만기별 유통수익률(일별, 1Y~40Y).

    왜 필요한가: 볼트에 **일본 국채 슬롯이 0개**였다(2026-08-18 실측).
    엔·BOJ 정책을 읽을 때 10Y·30Y가 없으면 "시장이 이미 반영했는지"를 못 잰다.
    CSV는 당월분만 담기므로 최근 6영업일만 취한다.
    """
    from .base import result, get_text
    url = "https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv"
    want = [str(x) for x in (ind.get("maturities") or ["2Y", "10Y", "30Y"])]
    try:
        text = get_text(url)
    except Exception as e:
        return result(ind, "fail", error=f"MOF CSV 수집 실패: {e}", source_url=url)
    rows = [r.split(",") for r in text.splitlines() if r.strip()]
    hdr = None
    for r in rows:
        if r and r[0].strip().lower() == "date":
            hdr = [c.strip() for c in r]
            break
    if not hdr:
        return result(ind, "fail", error="헤더(Date 행) 미발견 — CSV 구조 변경", source_url=url)
    idx = {m: hdr.index(m) for m in want if m in hdr}
    if not idx:
        return result(ind, "fail", error=f"만기 열 미발견: {want} / 가용 {hdr[1:6]}...", source_url=url)
    data = [r for r in rows if r and re.match(r"\d{4}/\d{1,2}/\d{1,2}", r[0].strip())]
    obs = []
    for r in data[-6:][::-1]:
        d = r[0].strip().replace("/", "-")
        for m, i in idx.items():
            try:
                obs.append({"date": d, "value": float(r[i]), "label": f"JGB {m}"})
            except (ValueError, IndexError):
                continue
    if not obs:
        return result(ind, "fail", error="값 파싱 실패", source_url=url)
    return result(ind, "ok", observations=obs, source_url=url)


# ── 일본 대외·대내 증권투자 (MOF 주간) ──────────────────────────────
# 왜 필요한가 — 볼트 [[일본 국채 (JGB)]] 노드가 "일본 대외증권투자"를 관측 공백으로 적었다.
# BIS AER 2025 Ch.II는 일본 투자자가 FX 스왑으로 헤지해 해외채권을 사고,
# **목적지 통화 단기금리가 오르거나 커브가 평탄해지면 그 수요가 줄어든다**고 했다.
# 이 계열이 그 수요를 주간으로 관측한다. 단위는 억엔(100 million yen).
MOF_WEEK = ("https://www.mof.go.jp/policy/international_policy/reference/"
            "itn_transactions_in_securities/week.csv")
MOF_LANDING = ("https://www.mof.go.jp/english/policy/international_policy/reference/"
               "itn_transactions_in_securities/index.htm")

# 열 인덱스 (2026-08-19 실측): 0=기간
#  대외(거주자 취득): 1~3 주식 취·처·순 · 4~6 중장기채 · 7 소계순 · 8~10 단기채 · 11 합계순
#  대내(비거주자):   12~14 주식 · 15~17 중장기채 · 18 소계순 · 19~21 단기채 · 22 합계순
_MOF_COL = {
    "out_equity": 3, "out_ltdebt": 6, "out_sub": 7, "out_stdebt": 10, "out_total": 11,
    "in_equity": 14, "in_ltdebt": 17, "in_sub": 18, "in_stdebt": 21, "in_total": 22,
}
_MOF_CACHE: dict[str, Any] = {}


def fetch_mof_portfolio(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """yaml 예시:
        method: api
        source: mof_portfolio
        fields: [out_ltdebt, out_total, in_ltdebt]
        points: 4          # 최신부터 몇 주
    """
    import csv
    import io as _io

    from .base import get_bytes

    if "rows" not in _MOF_CACHE:
        raw = get_bytes(MOF_WEEK)
        text = raw.decode("cp932", errors="replace")
        rows = list(csv.reader(_io.StringIO(text)))
        _MOF_CACHE["rows"] = [r for r in rows if r and r[0].strip() and "～" in r[0]]
    rows = _MOF_CACHE["rows"]
    if not rows:
        return result(ind, "fail", error="MOF 주간 CSV 파싱 실패", source_url=MOF_LANDING)

    fields = ind.get("fields") or ["out_total", "in_total"]
    points = int(ind.get("points") or 1)

    obs: list[dict[str, Any]] = []
    bad: list[str] = []
    for f in fields:
        col = _MOF_COL.get(f)
        if col is None:
            bad.append(f)
            continue
        for r in rows[-points:][::-1]:
            cell = (r[col] if col < len(r) else "").replace(",", "").strip()
            if not cell:
                continue
            try:
                oku = float(cell)
            except ValueError:
                continue
            # 억엔 → 조엔
            obs.append({"date": r[0].strip(), "value": round(oku / 10000.0, 2),
                        "label": f"{f} (조엔, 주간 순액)"})

    if not obs:
        return result(ind, "fail", error=f"MOF 필드 없음: {', '.join(bad) or fields}",
                      source_url=MOF_LANDING)
    err = f"미지원 필드: {', '.join(bad)}" if bad else ""
    return result(ind, "ok", observations=obs, source_url=MOF_LANDING, unit="조엔", error=err)
