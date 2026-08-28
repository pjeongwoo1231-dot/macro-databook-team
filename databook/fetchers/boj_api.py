"""일본은행(BOJ) 시계열통계 검색사이트 공식 API — 키 불필요.

**왜 필요한가** — 볼트의 일본 축은 지금까지 `boj_stat`(M2)·`boj_policy_rate`(기준대출금리)
**HTML 스크레이프 2개**로만 서 있었다. 둘 다 페이지 구조가 바뀌면 죽고, 정책금리는
실제 정책금리가 아니라 **기준대출금리 프록시**였다.

BOJ가 **2026-02-18** 시계열통계 검색사이트에 공식 API를 열었다(JSON·CSV, 키 불필요).
이제 무담보콜 O/N(=실제 정책금리 조작목표)·마네터리베이스·BOJ 대차대조표·PPI·SPPI·
단칸·국제수지·실효환율을 **원본 그대로** 받는다.

- 공고: https://www.boj.or.jp/statistics/outline/notice_2026/not260218a.htm
- 매뉴얼: https://www.stat-search.boj.or.jp/info/api_manual.pdf

**엔드포인트** (3종 중 코드 API만 쓴다)
    https://www.stat-search.boj.or.jp/api/v1/getDataCode?format=json&lang=en&db=<DB>&code=<계열코드,...>

⚠ **한 요청의 계열은 期種(frequency)가 전부 같아야 한다.** 월차와 분기를 섞으면 에러다.
⚠ **계열코드에 `%`가 들어가는 것들이 있다**(전년비 계열). URL 인코딩(%25) 필수 —
  `params`로 넘기면 `urlencode`가 처리한다. 코드를 URL에 직접 붙이지 말 것.
⚠ **고빈도 접근 금지**(매뉴얼 명시, 차단될 수 있음). 그래서 한 지표의 여러 계열은
  **콤마로 묶어 1회 요청**한다. `base.throttle`이 호스트당 0.6초를 추가로 깐다.
⚠ 값이 `null`인 기간이 있다(휴장·미공표). **건너뛴다** — 0으로 채우지 않는다.
⚠ BOJ는 **전년비 계열을 일부만 제공**한다(PPI·수출입물가는 있고, 마네스톡·은행대출 잔액은 없다).
  없는 건 `yoy: true`로 레벨에서 계산하고 라벨에 "(계산)"을 남긴다 — 원본과 구분하기 위해서다.

계열 코드는 전부 **메타데이터 API 실호출로 확인**했다(2026-08-26).
"""
from __future__ import annotations

import datetime
import json
from typing import Any
from urllib.error import HTTPError

from .base import N_OBS, get_json, result, yoy as _yoy_calc

BASE = "https://www.stat-search.boj.or.jp/api/v1/getDataCode"

# 전년비를 만들 수 있는 期種. 일차·주차는 1년 전 관측이 정의되지 않아 제외한다.
_YOY_OK = {"M", "Q", "CY", "FY"}


def _months_ago(n: int) -> datetime.date:
    d = datetime.date.today().replace(day=1)
    y, m = d.year, d.month - n
    while m <= 0:
        m += 12
        y -= 1
    return datetime.date(y, m, 1)


def _start_date(freq: str, points: int, yoy: bool) -> str:
    """응답 크기를 줄이는 개시기. 期種별 포맷이 다르다(매뉴얼 Ⅱ.3)."""
    today = datetime.date.today()
    if freq in ("D", "W"):
        # 일차·주차도 **월차 포맷(YYYYMM)**으로 지정한다. 휴장일이 있으니 넉넉히 잡는다
        return f"{_months_ago(max(2, points // 15 + 2)):%Y%m}"
    if freq == "M":
        return f"{_months_ago(points + 2 + (12 if yoy else 0)):%Y%m}"
    if freq == "Q":
        back_q = points + 1 + (4 if yoy else 0)
        d = _months_ago(back_q * 3)
        return f"{d.year:04d}{(d.month - 1) // 3 + 1:02d}"
    # CY·FY
    return f"{today.year - (points + (1 if yoy else 0)):04d}"


def _fmt_date(raw: str, freq: str) -> str:
    s = str(raw)
    if len(s) == 8:
        return f"{s[:4]}-{s[4:6]}-{s[6:]}"
    if len(s) == 6:
        if freq == "Q":
            return f"{s[:4]}-Q{int(s[4:])}"
        if freq in ("CH", "FH"):
            return f"{s[:4]}-H{int(s[4:])}"
        return f"{s[:4]}-{s[4:]}"
    return s


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """yaml 예시:
        method: api
        source: boj_api
        db: FM01                       # 매뉴얼 Ⅱ.3(2)의 DB명
        codes: [STRDCLUCON]            # 계열코드(DB명 접두 없이). code: 단일 문자열도 받는다
        labels: ["무담보콜 O/N 평균(%)"]  # 없으면 API의 영문 계열명
        freq: D                        # D W M Q CY FY (기본 M) — 한 지표 안에서는 동일해야 한다
        points: 6
        yoy: true                      # 레벨 계열을 전년비(%)로 환산
        scale: 0.0001                  # 값 배율 (억엔 → 조엔)
    """
    db = str(ind.get("db") or "").strip()
    codes = ind.get("codes") or ind.get("code")
    if not db or not codes:
        return result(ind, "fail", error="db 또는 codes 미지정")
    if isinstance(codes, str):
        codes = [codes]
    codes = [str(c).strip() for c in codes if str(c).strip()]
    labels = ind.get("labels") or []
    freq = str(ind.get("freq") or "M").upper()
    points = int(ind.get("points") or N_OBS)
    yoy = bool(ind.get("yoy"))
    scale = float(ind.get("scale") or 1)

    params = {
        "format": "json",
        "lang": "en",
        "db": db,
        "code": ",".join(codes),
        "startDate": _start_date(freq, points, yoy),
    }
    try:
        data = get_json(BASE, params=params)
    except HTTPError as e:
        # BOJ는 잘못된 계열코드에 400을 주고 **사유는 본문 JSON에만** 담는다.
        # 그대로 두면 "HTTP Error 400"만 남아 어떤 코드가 틀렸는지 알 수 없다.
        try:
            body = json.loads(e.read().decode("utf-8", "replace"))
            msg = f"{body.get('STATUS')} {body.get('MESSAGE')}"
        except Exception:
            msg = str(e)
        return result(ind, "fail", error=f"BOJ API {msg} — db={db} code={','.join(codes)}")
    if data.get("STATUS") != 200:
        return result(ind, "fail",
                      error=f"BOJ API {data.get('STATUS')}: {data.get('MESSAGE')}",
                      source_url="https://www.stat-search.boj.or.jp/")

    rows = data.get("RESULTSET") or []
    if not rows:
        return result(ind, "fail", error=f"계열 없음 — db={db} code={','.join(codes)}")

    obs: list[dict[str, Any]] = []
    unit = ""
    errors: list[str] = []
    for i, row in enumerate(rows):
        vals = row.get("VALUES") or {}
        periods = vals.get("SURVEY_DATES") or []
        values = vals.get("VALUES") or []
        pairs = [(str(p), float(v)) for p, v in zip(periods, values)
                 if isinstance(v, (int, float))]          # null = 휴장·미공표 → 버린다
        if not pairs:
            errors.append(f"{row.get('SERIES_CODE')}: 관측치 없음")
            continue
        label = str(labels[i]) if i < len(labels) else str(row.get("NAME_OF_TIME_SERIES") or "")[:60]
        if yoy:
            # 期種가 일차·주차면 전년비를 만들지 않는다(1년 전 관측이 정의되지 않음)
            pairs = _yoy_calc(pairs) if freq in _YOY_OK else []
            if not pairs:
                errors.append(f"{row.get('SERIES_CODE')}: 전년비 계산 불가(1년 전 관측 부족)")
                continue
            label = f"{label} 전년비(%) — 계산"
            row_unit = "%"
        else:
            row_unit = str(row.get("UNIT") or "")
        unit = unit or row_unit
        for period, val in pairs[-points:][::-1]:          # 최신순
            obs.append({"date": _fmt_date(period, freq),
                        "value": round(val * scale, 4) if scale != 1 else val,
                        "label": label})

    if not obs:
        return result(ind, "fail", error="; ".join(errors) or "파싱된 관측 없음")

    src = f"{BASE}?db={db}&code={','.join(codes)}&format=json&lang=en"
    res = result(ind, "ok", observations=obs, source_url=src, unit=unit)
    if errors:
        res["error"] = "; ".join(errors)                   # 부분 실패 병기
    return res
