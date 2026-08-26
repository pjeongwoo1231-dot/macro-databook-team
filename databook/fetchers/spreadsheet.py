"""스프레드시트로 배포되는 지표 — NY연은 GSCPI, policyuncertainty.com EPU.

FRED에 없거나(GSCPI) FRED판이 갱신이 끊긴 계열을 원천에서 직접 받는다.

포맷 주의:
- GSCPI는 확장자가 `.xlsx`인데 실제 내용은 **구형 .xls(OLE2)** 다. xlrd로 읽는다.
- policyuncertainty.com은 진짜 xlsx라 의존성 없는 자체 리더(`xlsx.py`)로 읽는다.
- 두 파일 모두 **말미에 출처·주석 행이 붙어 있어** 숫자로 파싱되지 않는 행은 버려야 한다.
"""
from __future__ import annotations

import re
from datetime import date
from typing import Any

from .base import BROWSER_UA, get_bytes, result
from .xlsx import read_sheet

MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}

SOURCES: dict[str, dict[str, Any]] = {
    "gscpi": {
        "url": "https://www.newyorkfed.org/medialibrary/research/interactives/gscpi/downloads/gscpi_data.xlsx",
        "kind": "xls",
        "sheet": "GSCPI Monthly Data",   # 2026-08 개편으로 1번 시트가 안내문이 됐다
        "page": "https://www.newyorkfed.org/research/policy/gscpi",
    },
    "epu_korea": {
        "url": "https://www.policyuncertainty.com/media/Korea_Policy_Uncertainty_Data.xlsx",
        "kind": "xlsx",
        "page": "https://www.policyuncertainty.com/korea_monthly.html",
    },
    "epu_us": {
        "url": "https://www.policyuncertainty.com/media/US_Policy_Uncertainty_Data.xlsx",
        "kind": "xlsx",
        "page": "https://www.policyuncertainty.com/us_monthly.html",
    },
    # Gilchrist-Zakrajšek(2012) GZ 스프레드·초과채권프리미엄. 연준이 월 단위로 갱신한다.
    # 헤더: date,gz_spread,ebp,est_prob — 날짜가 M/D/YYYY라 _parse_date에 해당 패턴이 필요하다.
    "ebp": {
        "url": "https://www.federalreserve.gov/econres/notes/feds-notes/ebp_csv.csv",
        "kind": "csv",
        "page": "https://www.federalreserve.gov/econres/notes/feds-notes/updating-the-recession-risk-and-the-excess-bond-premium-20161006.html",
    },
}


def _parse_date(v: Any) -> str | None:
    """'30-Apr-2026' · '4/1990' · 엑셀 시리얼 → 'YYYY-MM-DD'. 실패하면 None."""
    if v is None or v == "":
        return None
    if isinstance(v, (int, float)):
        from .xlsx import serial_to_date
        d = serial_to_date(v)
        return d.isoformat() if d else None
    s = str(v).strip()
    m = re.match(r"^(\d{1,2})-([A-Za-z]{3})-(\d{4})$", s)          # 30-Apr-2026
    if m:
        mo = MONTHS.get(m.group(2).lower())
        return f"{m.group(3)}-{mo:02d}-{int(m.group(1)):02d}" if mo else None
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})$", s)               # 1/1/1973 (EBP csv, M/D/YYYY)
    if m:
        return f"{m.group(3)}-{int(m.group(1)):02d}-{int(m.group(2)):02d}"
    m = re.match(r"^(\d{1,2})/(\d{4})$", s)                         # 4/1990
    if m:
        return f"{m.group(2)}-{int(m.group(1)):02d}-01"
    m = re.match(r"^(\d{4})-(\d{1,2})(?:-(\d{1,2}))?$", s)          # 2026-04(-30)
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3) or 1):02d}"
    return None


def _rows(key: str) -> tuple[list[list[Any]], str]:
    cfg = SOURCES[key]
    raw = get_bytes(cfg["url"], headers={"User-Agent": BROWSER_UA})
    if cfg["kind"] == "csv":
        import csv as _csv
        import io
        text = raw.decode("utf-8-sig", errors="replace")
        return [r for r in _csv.reader(io.StringIO(text)) if r], cfg["page"]
    if cfg["kind"] == "xls":
        import xlrd  # .xls(OLE2) 전용. xlsx는 자체 리더가 처리한다
        wb = xlrd.open_workbook(file_contents=raw)
        # ⚠ **첫 시트가 데이터 시트라는 보장이 없다.** 2026-08에 GSCPI가 시트를 둘로 쪼개면서
        #   1번 시트가 안내문("GSCPI Overview")이 됐고 수집이 조용히 실패했다.
        #   설정에 sheet가 있으면 그 이름으로, 없으면 **데이터가 가장 많은 시트**를 고른다.
        want = cfg.get("sheet")
        if want and want in wb.sheet_names():
            sh = wb.sheet_by_name(want)
        else:
            sh = max((wb.sheet_by_index(i) for i in range(wb.nsheets)),
                     key=lambda s: s.nrows * s.ncols)
        return [[c.value for c in sh.row(i)] for i in range(sh.nrows)], cfg["page"]
    return read_sheet(raw), cfg["page"]


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    key = str(ind.get("dataset", ""))
    if key not in SOURCES:
        return result(ind, "fail", error=f"알 수 없는 dataset: {key}")
    try:
        rows, page = _rows(key)
    except Exception as e:
        return result(ind, "fail", error=f"{type(e).__name__}: {e}")

    # 열 선택: column 지정이 있으면 헤더에서 찾고, 없으면 두 번째 열
    header = [str(c or "").strip() for c in (rows[0] if rows else [])]
    want = str(ind.get("column", "")).lower()
    col = 1
    if want:
        for i, h in enumerate(header):
            if want in h.lower():
                col = i
                break
        else:
            return result(ind, "fail",
                          error=f"열 '{ind['column']}' 없음. 헤더: {header[:8]}")
    label = header[col] if col < len(header) else key

    obs: list[dict[str, Any]] = []
    for r in rows[1:]:
        if col >= len(r):
            continue
        d = _parse_date(r[0] if r else None)
        if not d:
            continue                      # 말미 주석·빈 행
        try:
            val = float(str(r[col]).strip())
        except (TypeError, ValueError):
            continue
        obs.append({"date": d, "value": val, "label": label})
    if not obs:
        return result(ind, "fail", error="파싱된 관측치 없음(포맷 변경 의심)")

    obs.sort(key=lambda o: o["date"], reverse=True)
    latest = obs[0]["date"]
    note = ind.get("note", "")
    # 6개월 넘게 갱신이 없으면 경고를 붙인다 — 원천이 조용히 멈추는 일이 잦다
    try:
        y, m, _ = (int(x) for x in latest.split("-"))
        today = date.today()
        stale = (today.year - y) * 12 + (today.month - m)
        if stale > 6:
            note = (note + " | " if note else "") + f"⚠ 최신값 {latest} — {stale}개월째 갱신 없음"
    except Exception:
        pass
    return result(ind, "ok", observations=obs[:6], source_url=page, note=note)


def fetch_history(key: str, column: str = "") -> list[tuple[str, float]]:
    """history 모듈에서 쓰는 전 구간 반환."""
    rows, _ = _rows(key)
    header = [str(c or "").strip() for c in (rows[0] if rows else [])]
    col = 1
    if column:
        for i, h in enumerate(header):
            if column.lower() in h.lower():
                col = i
                break
    out: list[tuple[str, float]] = []
    for r in rows[1:]:
        if col >= len(r):
            continue
        d = _parse_date(r[0] if r else None)
        if not d:
            continue
        try:
            out.append((d, float(str(r[col]).strip())))
        except (TypeError, ValueError):
            continue
    return sorted(out)
