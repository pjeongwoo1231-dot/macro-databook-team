"""BIS 공식 통계 — credit-to-GDP gap (WS_CREDIT_GAP). 키 불필요, 무료.

왜 필요한가 — 기존 신용 지표(EBP·HY OAS·신용스프레드)는 전부 **신용의 가격**이고
"지금 실물이 꺾이나"(3~12개월)만 답한다. Jordà·Schularick·Taylor(2013)의
"확장기 신용집약도가 높을수록 그 뒤 침체가 깊다"는 **심각도** 축을 채우려면
**신용의 양**이 필요하다. BIS gap = 총신용/GDP 비율의 장기추세 이탈분이 그 표준 지표다.

⚠ 한계 (yaml note에도 반드시 명시):
- **분기 데이터**이며 BIS 갱신이 2~3분기 지연된다. 주간 트리거로 쓸 수 없다
- 단측 HP필터(λ=400,000) 기반이라 **표본 끝단 추정이 불안정**하다. BIS 자신이 경고한다
- 추세는 통계적 산물이지 균형 수준이 아니다. "gap<0이니 안전"으로 읽으면 안 된다
- **총신용(비은행 포함) 기준**이다. 은행 신용만 보는 지표와 섞지 말 것

CG_DTYPE: A=credit-to-GDP 비율 · B=추세 · C=**gap(actual−trend)**
"""
from __future__ import annotations

import csv
import io
import zipfile
from typing import Any

from .base import get_bytes, result

BULK = "https://data.bis.org/static/bulk/WS_CREDIT_GAP_csv_col.zip"
LANDING = "https://www.bis.org/statistics/c_gaps.htm"
_CACHE: dict[str, list[list[str]]] = {}


def _load(env: dict[str, str]) -> tuple[list[str], list[list[str]]]:
    """벌크 CSV 1회 다운로드 후 프로세스 내 캐시 — 국가별 지표가 여럿이어도 1회만 받는다."""
    if "rows" not in _CACHE:
        raw = get_bytes(BULK)
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            name = next(n for n in z.namelist() if n.lower().endswith(".csv"))
            text = z.read(name).decode("utf-8-sig", errors="replace")
        rd = csv.reader(io.StringIO(text))
        _CACHE["hdr"] = next(rd)
        _CACHE["rows"] = list(rd)
    return _CACHE["hdr"], _CACHE["rows"]


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """yaml 예시:
        method: api
        source: bis_credit_gap
        countries: [US, KR]          # BIS 2자리 국가코드
        dtype: C                     # 기본 C(gap). A=비율, B=추세
        points: 4                    # 최신부터 몇 분기
    """
    hdr, rows = _load(env)
    dtype = str(ind.get("dtype") or "C").upper()
    countries = ind.get("countries") or ["US"]
    points = int(ind.get("points") or 4)

    obs: list[dict[str, Any]] = []
    missing: list[str] = []
    for cty in countries:
        hit = next((r for r in rows if r[2] == cty and r[8] == dtype), None)
        if hit is None:
            missing.append(cty)
            continue
        series = [(hdr[i], r) for i, r in enumerate(hit) if i >= 14 and r.strip()]
        if not series:
            missing.append(cty)
            continue
        for period, val in reversed(series[-points:]):
            obs.append({"date": period, "value": round(float(val), 2), "label": cty})

    if not obs:
        return result(ind, "fail", error=f"BIS gap 없음: {', '.join(missing) or countries}",
                      source_url=LANDING)
    err = f"국가 누락: {', '.join(missing)}" if missing else ""
    return result(ind, "ok", observations=obs, source_url=LANDING, unit="%p", error=err)


# ── 부채상환비율(DSR) ────────────────────────────────────────────────
# BIS AER 2018 Ch.I Graph I.9가 쓴 지표. "금리가 오르면 부담이 는다"로 끝내지 않고
# **DSR이 자국 장기평균에서 몇 %p 벗어났는가**로 묻기 위해 붙였다.
# 벌크 CSV 구조: [2]=국가, [4]=차입주체(H 가계 / N 비금융기업 / P 민간 전체), [10:]=분기 관측
DSR_BULK = "https://data.bis.org/static/bulk/WS_DSR_csv_col.zip"
DSR_LANDING = "https://www.bis.org/statistics/dsr.htm"
_DSR: dict[str, Any] = {}


def _load_dsr() -> tuple[list[str], list[list[str]]]:
    if "rows" not in _DSR:
        raw = get_bytes(DSR_BULK)
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            name = next(n for n in z.namelist() if n.lower().endswith(".csv"))
            text = z.read(name).decode("utf-8-sig", errors="replace")
        rd = csv.reader(io.StringIO(text))
        _DSR["hdr"] = next(rd)
        _DSR["rows"] = list(rd)
    return _DSR["hdr"], _DSR["rows"]


def fetch_dsr(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """yaml 예시:
        method: api
        source: bis_dsr
        countries: [KR, US, JP]
        sector: P                 # H=가계 · N=비금융기업 · P=민간 전체(기본)
        mode: deviation           # deviation=장기평균 이탈(%p, 기본) · level=수준(%)
    """
    hdr, rows = _load_dsr()
    sector = str(ind.get("sector") or "P").upper()
    countries = ind.get("countries") or ["KR", "US"]
    mode = str(ind.get("mode") or "deviation").lower()

    obs: list[dict[str, Any]] = []
    missing: list[str] = []
    for cty in countries:
        hit = next((r for r in rows if r[2] == cty and r[4] == sector), None)
        if hit is None:
            missing.append(cty)
            continue
        ser = [(hdr[i], float(v)) for i, v in enumerate(hit) if i >= 10 and v.strip()]
        if not ser:
            missing.append(cty)
            continue
        period, level = ser[-1]
        vals = [v for _, v in ser]
        avg = sum(vals) / len(vals)
        val = round(level - avg, 2) if mode == "deviation" else round(level, 2)
        obs.append({"date": period, "value": val,
                    "label": f"{cty} {sector} (수준 {level:.1f}% · {hdr[10][:4]}~평균 {avg:.1f}%)"})

    if not obs:
        return result(ind, "fail", error=f"BIS DSR 없음: {', '.join(missing) or countries}",
                      source_url=DSR_LANDING)
    err = f"국가 누락: {', '.join(missing)}" if missing else ""
    unit = "%p" if mode == "deviation" else "%"
    return result(ind, "ok", observations=obs, source_url=DSR_LANDING, unit=unit, error=err)
