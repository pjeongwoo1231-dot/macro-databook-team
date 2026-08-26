"""e-Stat(政府統計の総合窓口) API — `E_STAT_APP_ID` 필요(무료, e-stat.go.jp/api).

**무엇을 채우는 자리인가** — BOJ API가 통화·물가·심리를 덮고 관세청이 무역을 덮은 뒤에도
**실물경제(생산·소비·설비투자 선행)**가 비어 있었다. FRED의 일본 광공업생산
(`JPNPROINDMISMEI`)은 OECD MEI 폐지로 2024-03에서 멈췄고, METI 자체 사이트는
파일 다운로드가 **HTTP 202 + 본문 0바이트**로 막힌다(2026-08-26 확인, 브라우저 UA·쿠키·리퍼러 모두 무효).
그래서 e-Stat이 유일한 자동 경로다.

⚠ **e-Stat이 최신인가는 부처마다 다르다.** 같은 API인데 갱신 주기가 제각각이라,
  **지표를 붙이기 전에 반드시 `getStatsList`로 UPDATED_DATE를 확인**할 것.
  2026-08-26 실측:

  | 통계 | statsCode | 상태 |
  |---|---|---|
  | 機械受注(기계수주) | 00100401 | ✅ 2026-08-19 갱신, 2026-06까지 |
  | 家計調査(가계소비) | 00200561 | ✅ 2026-08-07 갱신 |
  | 鉱工業指数(광공업생산) | 00550300 | ⚠ 2026-06-03 갱신, **2026-03까지(약 5개월 지연)** |
  | 商業動態統計(소매판매) | 00550030 | ✗ 2024년치까지 — 자동화 불가 |
  | 毎月勤労統計(임금) | 00450071 | ✗ **2021-10 이후 갱신 중단** — 자동화 불가 |

**엔드포인트**
    목록: https://api.e-stat.go.jp/rest/3.0/app/json/getStatsList?appId=..&statsCode=..
    메타: https://api.e-stat.go.jp/rest/3.0/app/json/getMetaInfo?appId=..&statsDataId=..
    데이터: https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData?appId=..&statsDataId=..&cdCat01=..

⚠ **분류코드를 추측하지 말 것.** 표마다 cat01·cat02의 의미가 다르다
  (같은 기계수주 안에서도 표 0003355268은 cat01=기종, 0003355222는 cat01=수요자다).
  `getMetaInfo`로 실제 코드를 확인한 뒤 yaml에 적는다.
⚠ **시간축 코드를 파싱하지 않는다**(`2026000606` 같은 내부 코드다).
  `metaGetFlg=Y`로 받은 `@name`("2026年6月")을 정규화해서 쓴다.
⚠ 값이 `-`·`***`·`X`인 칸이 있다(비공표·해당없음). **건너뛴다** — 0으로 채우지 않는다.
"""
from __future__ import annotations

import re
from typing import Any

from .base import get_json, result

BASE = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"
DEFAULT_POINTS = 6
_MISSING = {"-", "***", "X", "x", "…", "", "-  "}


def _period(name: str) -> str:
    """'2026年6月' → '2026-06' · '2026年4~6月期' → '2026-Q2' · '2026年度' → '2026년도'."""
    s = str(name).strip()
    m = re.match(r"^(\d{4})年(\d{1,2})月$", s)
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}"
    m = re.match(r"^(\d{4})年\s*(\d{1,2})\s*[~～-]\s*(\d{1,2})月期$", s)
    if m:
        return f"{m.group(1)}-Q{(int(m.group(3)) - 1) // 3 + 1}"
    m = re.match(r"^(\d{4})年度$", s)
    if m:
        return f"{m.group(1)}년도"
    m = re.match(r"^(\d{4})年$", s)
    if m:
        return m.group(1)
    m = re.match(r"^(\d{4})(\d{2})$", s)          # 표에 따라 '202607' 꼴로 오기도 한다
    if m and 1 <= int(m.group(2)) <= 12:
        return f"{m.group(1)}-{m.group(2)}"
    return s


# 정규화 결과가 이 꼴이어야 **기간**이다. 표에 따라 시간축에 기간이 아닌 행이 섞인다
# (鉱工業指数 표의 '付加生産ウエイト' = 가중치). 그냥 두면 사전순 정렬에서 맨 앞에 온다.
_PERIOD_RE = re.compile(r"^\d{4}(-\d{2}|-Q[1-4]|년도)?$")


def _class_names(stat: dict[str, Any]) -> dict[str, dict[str, str]]:
    """CLASS_INF → {'time': {코드: 이름}, 'cat01': {...}, ...}."""
    out: dict[str, dict[str, str]] = {}
    objs = ((stat.get("CLASS_INF") or {}).get("CLASS_OBJ")) or []
    if isinstance(objs, dict):
        objs = [objs]
    for cls in objs:
        items = cls.get("CLASS")
        items = items if isinstance(items, list) else [items]
        out[str(cls.get("@id"))] = {str(o.get("@code")): str(o.get("@name")) for o in items if o}
    return out


def _yoy(rows: list[tuple[str, float]]) -> list[tuple[str, float]]:
    """레벨 → 전년비(%). 정규화한 기간키('2026-06'·'2026-Q2'·'2026')로 1년 전을 직접 찾는다."""
    by = dict(rows)
    out: list[tuple[str, float]] = []
    for p_, v in rows:
        if len(p_) >= 7 and p_[4] == "-":          # YYYY-MM · YYYY-Qn
            prev = f"{int(p_[:4]) - 1:04d}{p_[4:]}"
        elif len(p_) == 4 and p_.isdigit():        # YYYY
            prev = f"{int(p_) - 1:04d}"
        else:
            continue
        base = by.get(prev)
        if base in (None, 0):
            continue
        out.append((p_, round((v / base - 1) * 100, 2)))
    return out


def _fetch_one(app_id: str, sid: str, filters: dict[str, str], points: int,
               scale: float, label: str, yoy: bool = False) -> tuple[list[dict[str, Any]], str, str]:
    # ⚠ **limit으로 자른 뒤 정렬하면 안 된다.** e-Stat은 반환 순서를 보장하지 않아서,
    # 60건만 받아 정렬했더니 100개 기간 중 앞쪽만 잡혀 "최신"이 2022-11로 나왔다(실제로 겪었다).
    # 필터를 건 슬라이스는 보통 수백 건이라 넉넉히 받고 **기간으로 정렬**한다.
    params = {"appId": app_id, "statsDataId": sid, "metaGetFlg": "Y",
              "cntGetFlg": "N", "limit": int(max(points * 10, 500)), **filters}
    d = get_json(BASE, params=params)
    root = d.get("GET_STATS_DATA") or {}
    res = root.get("RESULT") or {}
    if str(res.get("STATUS")) not in ("0", "1"):
        raise RuntimeError(f"e-Stat {res.get('STATUS')}: {res.get('ERROR_MSG')}")
    stat = root.get("STATISTICAL_DATA") or {}
    values = ((stat.get("DATA_INF") or {}).get("VALUE")) or []
    if isinstance(values, dict):
        values = [values]
    names = _class_names(stat)
    times = names.get("time", {})

    rows: list[tuple[str, float]] = []
    unit = ""
    for v in values:
        raw = str(v.get("$", "")).strip().replace(",", "")
        if raw in _MISSING:
            continue
        try:
            num = float(raw)
        except ValueError:
            continue
        tcode = str(v.get("@time", ""))
        unit = unit or str(v.get("@unit") or "")
        period = _period(times.get(tcode, tcode))
        if not _PERIOD_RE.match(period):          # 가중치·주기 등 기간이 아닌 행은 버린다
            continue
        rows.append((period, num))
    if not rows:
        return [], unit, ""

    # 정규화한 기간('2026-06'·'2026-Q2')으로 정렬한다 — 원본 이름('2026年6月')은
    # 사전순이 12月 < 6月이라 뒤집힌다
    rows.sort(key=lambda r: r[0], reverse=True)
    if yoy:
        rows = _yoy(rows)
        if not rows:
            return [], "%", ""
        label = f"{label} 전년비(%) — 계산"
        unit = "%"
        scale = 1
    obs = [{"date": p, "value": round(n * scale, 4) if scale != 1 else n, "label": label}
           for p, n in rows[:points]]
    tbl = (stat.get("TABLE_INF") or {})
    title = tbl.get("TITLE")
    title = title.get("$") if isinstance(title, dict) else title
    return obs, unit, str(title or "")


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """yaml 예시:
        method: api
        source: e_stat
        stats_data_id: "0003355222"
        series:                          # 여러 계열이면 목록으로 (계열당 1회 요청)
          - label: "민수(선박·전력 제외, 조엔)"
            filters: {cdCat01: "160", cdCat02: "100"}
        points: 6
        scale: 0.000001                  # 百万円 → 조엔

      단일 계열이면 series 없이 filters·label을 바로 써도 된다.
    """
    app_id = env.get("E_STAT_APP_ID", "")
    if not app_id:
        return result(ind, "fail", error="E_STAT_APP_ID 없음 (.env 확인 · e-stat.go.jp/api 무료 발급)")
    sid = str(ind.get("stats_data_id") or "").strip()
    if not sid:
        return result(ind, "fail", error="stats_data_id 미지정")

    series = ind.get("series")
    if not series:
        series = [{"label": ind.get("label") or ind["name"], "filters": ind.get("filters") or {}}]
    points = int(ind.get("points") or DEFAULT_POINTS)
    scale = float(ind.get("scale") or 1)
    yoy = bool(ind.get("yoy"))       # 레벨만 있는 표(家計調査 금액 등)를 전년비로 환산

    obs: list[dict[str, Any]] = []
    errors: list[str] = []
    unit = ""
    for s in series:
        filters = {str(k): str(v) for k, v in (s.get("filters") or {}).items()}
        label = str(s.get("label") or ind["name"])
        try:
            got, u, _title = _fetch_one(app_id, sid, filters, points, scale, label, yoy)
        except Exception as e:
            errors.append(f"{label}: {type(e).__name__}: {e}")
            continue
        if not got:
            errors.append(f"{label}: 관측치 없음(분류코드 확인 — getMetaInfo)")
            continue
        unit = unit or u
        obs.extend(got)

    if not obs:
        return result(ind, "fail", error="; ".join(errors) or "관측치 없음")
    src = f"https://www.e-stat.go.jp/dbview?sid={sid}"
    res = result(ind, "ok", observations=obs, source_url=src, unit=unit)
    if errors:
        res["error"] = "; ".join(errors)                        # 부분 실패 병기
    return res
