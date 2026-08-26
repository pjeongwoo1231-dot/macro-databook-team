"""scrape 소스 — 비공식 endpoint라 언제든 깨질 수 있다. 실패는 격리되므로 과감히 시도한다.
검증일 2026-07-16: yahoo chart API, CNN graphdata(Referer 필수), 네이버 투자자별 매매동향 iframe, Farside HTML."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from typing import Any

from .base import BROWSER_UA, get_bytes, get_text, result

YAHOO_CHART = "https://query1.finance.yahoo.com/v8/finance/chart/{sym}?range=1mo&interval=1d"
MONTH_CODES = "FGHJKMNQUVXZ"  # 1월~12월 선물 월물 코드


def _yahoo_closes(symbol: str) -> list[tuple[str, float]]:
    import urllib.parse

    body = get_text(YAHOO_CHART.format(sym=urllib.parse.quote(symbol)), headers={"Accept": "application/json"})
    res = json.loads(body)["chart"]["result"][0]
    ts = res.get("timestamp", [])
    closes = res["indicators"]["quote"][0].get("close", [])
    out = []
    for t, c in zip(ts, closes):
        if c is None:
            continue
        out.append((datetime.fromtimestamp(t, tz=timezone.utc).strftime("%Y-%m-%d"), float(c)))
    return out


def fetch_yahoo(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """symbol: 문자열 또는 리스트. 리스트면 심볼별 관측치를 label로 구분해 합친다."""
    symbols = ind.get("symbol", "")
    if isinstance(symbols, str):
        symbols = [symbols] if symbols else []
    if not symbols:
        return result(ind, "fail", error="symbol 미지정")
    all_obs: list[dict[str, Any]] = []
    urls: list[str] = []
    errors: list[str] = []
    for symbol in symbols:
        try:
            closes = _yahoo_closes(str(symbol))
            if not closes:
                errors.append(f"{symbol}: 종가 없음")
                continue
            n = 6 if len(symbols) == 1 else 3  # 다중 심볼이면 심볼당 3개로 압축
            for d, v in reversed(closes[-n:]):
                # 페그 통화(리얄·디르함) 등 저가 심볼은 소수 4자리로 이탈 모니터링
                all_obs.append({"date": d, "value": round(v, 4 if abs(v) < 100 else 2), "label": str(symbol)})
            urls.append(f"https://finance.yahoo.com/quote/{symbol}")
        except Exception as e:
            errors.append(f"{symbol}: {type(e).__name__}: {e}")
    if not all_obs:
        return result(ind, "fail", error="; ".join(errors) or "종가 없음")
    res = result(ind, "ok", observations=all_obs, source_url=" ".join(urls))
    if errors:
        res["error"] = "; ".join(errors)
    return res


def fetch_cboe_pcr(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """CBOE 일일 통계 페이지에서 Put/Call 비율 파싱 (검증일 2026-07-18)."""
    url = "https://www.cboe.com/us/options/market_statistics/daily/"
    txt = get_text(url)
    obs = []
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for pat, label in [
        (r"TOTAL PUT/CALL RATIO[^0-9]*([0-9.]+)", "전체 Put/Call"),
        (r"INDEX PUT/CALL RATIO[^0-9]*([0-9.]+)", "지수 Put/Call"),
        (r"EQUITY PUT/CALL RATIO[^0-9]*([0-9.]+)", "개별주 Put/Call"),
    ]:
        m = re.search(pat, txt, re.I)
        if m:
            obs.append({"date": today, "value": float(m.group(1)), "label": label})
    if not obs:
        return result(ind, "fail", error="Put/Call 비율 파싱 실패 (페이지 구조 변경 가능성)")
    return result(ind, "ok", observations=obs, source_url=url)


def fetch_fedfunds_futures(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """CME FedWatch 대용 — Fed 선물(ZQ) 가격에서 내재금리(100−가격) 직접 계산."""
    now = datetime.now(timezone.utc)
    obs = []
    errors = []
    for i in range(0, 7, 2):  # 현재월부터 격월로 4개 월물
        m = (now.month - 1 + i) % 12 + 1
        y = now.year + (now.month - 1 + i) // 12
        sym = f"ZQ{MONTH_CODES[m - 1]}{str(y)[2:]}.CBT"
        try:
            closes = _yahoo_closes(sym)
            if closes:
                d, price = closes[-1]
                obs.append({"date": d, "value": round(100 - price, 3), "label": f"{y}-{m:02d}월물 내재금리(%)"})
        except Exception as e:
            errors.append(f"{sym}: {type(e).__name__}")
    if not obs:
        return result(ind, "fail", error="; ".join(errors) or "월물 조회 실패")
    res = result(ind, "ok", observations=obs, source_url="https://finance.yahoo.com/quote/ZQ=F")
    if errors:
        res["error"] = "; ".join(errors)
    return res


def fetch_cnn_fng(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    body = get_text(
        "https://production.dataviz.cnn.io/index/fearandgreed/graphdata",
        headers={"Referer": "https://edition.cnn.com/markets/fear-and-greed", "Accept": "application/json"},
    )
    fg = json.loads(body)["fear_and_greed"]
    d = str(fg.get("timestamp", ""))[:10]
    obs = [
        {"date": d, "value": round(float(fg["score"]), 1), "label": fg.get("rating", "")},
        {"date": d, "value": round(float(fg["previous_1_week"]), 1), "label": "1주 전"},
        {"date": d, "value": round(float(fg["previous_1_month"]), 1), "label": "1개월 전"},
    ]
    return result(ind, "ok", observations=obs, source_url="https://edition.cnn.com/markets/fear-and-greed")


def fetch_naver_investor(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """KRX 외국인 수급 대용 — 네이버 투자자별 매매동향(KOSPI, 억원). 헤더를 파싱해 열을 매핑한다."""
    today = datetime.now(timezone.utc).strftime("%Y%m%d")
    html = get_text(
        f"https://finance.naver.com/sise/investorDealTrendDay.naver?bizdate={today}&sosok=",
        headers={"Referer": "https://finance.naver.com/sise/sise_trans_style.naver"},
        encoding="euc-kr",
    )
    headers = re.findall(r"<th[^>]*>\s*([가-힣A-Za-z]+)\s*</th>", html)
    try:
        fx_idx = headers.index("외국인")
        indiv_idx = headers.index("개인")
    except ValueError:
        return result(ind, "fail", error=f"헤더에서 외국인 열 미발견: {headers[:8]}")
    obs = []
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.S):
        tds = re.findall(r"<td[^>]*>\s*(?:<span[^>]*>)?\s*([^<]*?)\s*(?:</span>)?\s*</td>", tr)
        if not tds or not re.match(r"\d{2}\.\d{2}\.\d{2}", tds[0]):
            continue
        d = "20" + tds[0].replace(".", "-")
        try:
            # 날짜가 0번이므로 헤더 인덱스와 1 어긋남 없이 정렬됨 (헤더에도 날짜 없음 → +0/-0 검증: 값 열은 tds[1:])
            obs.append({"date": d, "value": float(tds[fx_idx].replace(",", "")), "label": "외국인 순매수(억원, KOSPI)"})
            obs.append({"date": d, "value": float(tds[indiv_idx].replace(",", "")), "label": "개인 순매수(억원, KOSPI)"})
        except (ValueError, IndexError):
            continue
        if len(obs) >= 10:
            break
    if not obs:
        return result(ind, "fail", error="표 파싱 실패 (구조 변경 가능성)")
    return result(ind, "ok", observations=obs, source_url="https://finance.naver.com/sise/sise_trans_style.naver")


def fetch_ici_flows(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """ICI(Investment Company Institute) 주간 펀드+ETF 합산 순유입 — 레거시 .xls(BIFF) 직배포.
    URL 패턴 https://www.ici.org/combined_flows_data_{연도}.xls 확인(2026-07-19). xlrd 필요(선택 의존성)."""
    try:
        import io
        import xlrd
    except ImportError:
        return result(ind, "fail", error="xlrd 미설치 — pip install xlrd 필요(선택 의존성)")
    year = datetime.now(timezone.utc).year
    url = f"https://www.ici.org/combined_flows_data_{year}.xls"
    try:
        raw = get_bytes(url)
        wb = xlrd.open_workbook(file_contents=raw)
    except Exception:
        # 연초 전환기 등 올해 파일이 아직 없으면 전년도 파일로 폴백
        year -= 1
        url = f"https://www.ici.org/combined_flows_data_{year}.xls"
        raw = get_bytes(url)
        wb = xlrd.open_workbook(file_contents=raw)
    sh = wb.sheet_by_index(0)
    rows = [sh.row_values(r) for r in range(sh.nrows)]
    start = next((i for i, row in enumerate(rows) if row and "weekly" in str(row[0]).lower()), None)
    if start is None:
        return result(ind, "fail", error="주간 섹션 헤더('Estimated weekly fund flows') 미발견 — 시트 구조 변경 가능성")
    obs = []
    for row in rows[start + 1:]:
        if not row or not row[0]:
            break
        date_str = str(row[0]).strip()
        try:
            d = datetime.strptime(date_str, "%m/%d/%Y").strftime("%Y-%m-%d")
            obs.append({"date": d, "value": float(row[1]), "label": "펀드+ETF 합산 순유입($mn, 주간, ICI)"})
        except (ValueError, IndexError):
            continue
    if not obs:
        return result(ind, "fail", error="주간 순유입 파싱 실패 (시트 구조 변경 가능성)")
    obs.sort(key=lambda o: o["date"], reverse=True)
    return result(ind, "ok", observations=obs[:6], source_url=url)


_FARSIDE = {
    "btc": ("https://farside.co.uk/btc/", "BTC ETF 순유입($mn)"),
    # 2026-08-21 추가. BTC만 받고 ETH는 안 받는 비대칭이 있었다 —
    # [[시황 2026-08-20]]에서 "ETH 현물 ETF 순유입 미수집"으로 기록된 그 결측이다.
    "eth": ("https://farside.co.uk/ethereum-etf-flow-all-data/", "ETH ETF 순유입($mn)"),
}


def fetch_farside(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """현물 ETF 일별 순유입 — farside.co.uk 표의 마지막 열(Total, $mn).

    ⚠ **표의 마지막 열이 Total이라는 가정**에 의존한다. 운용사가 추가·제거되면 열이 바뀌므로
    값이 갑자기 이상해지면 이 가정을 먼저 의심한다.
    ⚠ Cloudflare가 걸리면 통째로 실패한다 — 조용히 빈 값을 넣지 않는다.
    """
    asset = str(ind.get("asset", "btc")).lower()
    if asset not in _FARSIDE:
        return result(ind, "fail", error=f"미지원 asset: {asset} (가능: {list(_FARSIDE)})")
    url, label = _FARSIDE[asset]
    html = get_text(url, headers={"Accept": "text/html"})
    obs = []
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.S):
        cells = [re.sub(r"<[^>]+>", "", c).strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)]
        if not cells or not re.match(r"\d{1,2} [A-Z][a-z]{2} \d{4}", cells[0]):
            continue
        raw = cells[-1].replace(",", "").replace("(", "-").replace(")", "")
        try:
            d = datetime.strptime(cells[0], "%d %b %Y").strftime("%Y-%m-%d")
            obs.append({"date": d, "value": float(raw), "label": label})
        except ValueError:
            continue
    obs.sort(key=lambda o: o["date"], reverse=True)
    if not obs:
        return result(ind, "fail", error="표 파싱 실패 (Cloudflare 차단 또는 구조 변경)")
    return result(ind, "ok", observations=obs[:6], source_url=url)


# ── GPR 지정학위험지수 (Caldara & Iacoviello, matteoiacoviello.com) ──────────────
# 월간 .xls 직배포(안정 URL) → xlrd 파싱. GeoSwap이 쓰던 지정학 데이터의 라이브 원본.
# 헤드라인 GPR + 국가별 GPRC_*(산유국·핵심국). team_4의 정성 지정학 헤드라인에 정량 수치를 더한다.
_GPR_URL = "https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls"
_GPR_PUBLIC = "https://www.matteoiacoviello.com/gpr.htm"
_gpr_cache: dict[str, list[tuple[str, float]]] | None = None
_GPR_LABELS = {
    "GPR": "글로벌(헤드라인)", "GPRC_RUS": "러시아", "GPRC_SAU": "사우디",
    "GPRC_VEN": "베네수엘라", "GPRC_USA": "미국", "GPRC_UKR": "우크라이나",
    "GPRC_ISR": "이스라엘", "GPRC_CHN": "중국", "GPRC_KOR": "한국",
}


def _load_gpr() -> dict[str, list[tuple[str, float]]]:
    """GPR export.xls를 실행당 1회 다운로드·파싱해 컬럼별 (YYYY-MM-DD, value) 시계열(최신순)로 캐시."""
    global _gpr_cache
    if _gpr_cache is not None:
        return _gpr_cache
    import xlrd

    raw = get_bytes(_GPR_URL, headers={"User-Agent": BROWSER_UA})
    wb = xlrd.open_workbook(file_contents=raw)
    sh = wb.sheet_by_index(0)
    header = [str(sh.cell_value(0, c)).strip() for c in range(sh.ncols)]
    idx = {name: i for i, name in enumerate(header)}
    month_i = idx.get("month")
    if month_i is None:
        raise ValueError("'month' 컬럼 미발견 — 파일 구조 변경 가능성")
    series: dict[str, list[tuple[str, float]]] = {}
    for r in range(1, sh.nrows):
        row = sh.row_values(r)
        try:
            d = xlrd.xldate.xldate_as_datetime(float(row[month_i]), wb.datemode).strftime("%Y-%m-%d")
        except Exception:
            continue
        for name, i in idx.items():
            if name in ("month", "var_name", "var_label"):
                continue
            v = row[i]
            if isinstance(v, (int, float)) and v != "":
                series.setdefault(name, []).append((d, float(v)))
    for name in series:
        series[name].sort(key=lambda t: t[0], reverse=True)
    _gpr_cache = series
    return series


def load_gpr_series() -> dict[str, list[tuple[str, float]]]:
    """GPR 전체 월간 시계열(컬럼별, 최신순). `history` 모듈이 CSV 축적에 쓴다.

    `run` 은 최신 몇 점만 보지만 백테스트는 전 이력이 필요하다. 원본이 한 번의
    .xls 다운로드로 1900년대부터 전부 주므로, 증분 없이 매번 통째로 받아 덮어쓴다.
    """
    return _load_gpr()


def gpr_labels() -> dict[str, str]:
    return dict(_GPR_LABELS)


def fetch_gpr(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """지정학위험지수 GPR. gpr_series로 헤드라인(GPR)/국가별(GPRC_*) 컬럼 지정, gpr_points로 시리즈당 관측 수."""
    try:
        import xlrd  # noqa: F401
    except ImportError:
        return result(ind, "fail", error="xlrd 미설치 — pip install xlrd 필요(선택 의존성)")
    cols = ind.get("gpr_series", "GPR")
    if isinstance(cols, str):
        cols = [cols]
    per = int(ind.get("gpr_points", 2))
    try:
        series = _load_gpr()
    except Exception as e:
        return result(ind, "fail", error=f"GPR 다운로드/파싱 실패: {type(e).__name__}: {e}")
    obs: list[dict[str, Any]] = []
    missing: list[str] = []
    for col in cols:
        pts = series.get(col)
        if not pts:
            missing.append(col)
            continue
        label = _GPR_LABELS.get(col, col)
        for d, v in pts[:per]:
            obs.append({"date": d, "value": round(v, 1), "label": f"GPR {label}"})
    if not obs:
        return result(ind, "fail", error=f"GPR 컬럼 미발견: {', '.join(missing) or cols}")
    res = result(ind, "ok", observations=obs, source_url=_GPR_PUBLIC)
    if missing:
        res["error"] = f"미발견 컬럼: {', '.join(missing)}"
    return res

def fetch_yahoo_intraday(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """장중 스냅샷 — 현재가와 전일 종가 대비 등락률.

    왜 필요한가: 볼트는 **일별 종가 배치**뿐이라 장중 상태를 못 본다(2026-08-18 실측).
    ⚠ 이 값은 **실행 시점 스냅샷**이며 소급 수집이 불가능하다 — daily 배치와 같은 성격이다.
    """
    syms = ind.get("symbol") or []
    if isinstance(syms, str):
        syms = [syms]
    obs = []
    for s in syms:
        u = ("https://query1.finance.yahoo.com/v8/finance/chart/"
             f"{__import__('urllib.parse', fromlist=['quote']).quote(str(s))}?range=1d&interval=5m")
        try:
            import urllib.parse, json as _json
            d = _json.loads(get_text(u, headers={"Accept": "application/json"}))
            r = d["chart"]["result"][0]
            meta = r.get("meta", {})
            price = meta.get("regularMarketPrice")
            prev = meta.get("chartPreviousClose") or meta.get("previousClose")
            ts = meta.get("regularMarketTime")
            when = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC") if ts else _today()
            if price is None:
                continue
            obs.append({"date": when, "value": round(float(price), 2), "label": f"{s} 현재가"})
            if prev:
                obs.append({"date": when, "value": round(100.0 * (float(price) / float(prev) - 1.0), 2),
                            "label": f"{s} 전일 대비(%)"})
        except Exception:
            continue
    if not obs:
        return result(ind, "fail", error="장중 스냅샷 수집 실패(심볼·시장 개장 여부 확인)")
    return result(ind, "ok", observations=obs, source_url="https://finance.yahoo.com")
