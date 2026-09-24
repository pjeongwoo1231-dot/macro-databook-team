"""미국 자동차 — Manheim 도매 중고차지수(Cox Automotive)와 NY연은 가계부채 오토론.

왜 필요한가 — 볼트는 지금까지 미국 자동차를 **소매판매(RSAFS·RRSFS)와 헤드라인 CPI 안에
묻어서만** 봤다. 그런데 자동차는 물가 전달의 교과서적 경로가 통째로 관측되는 몇 안 되는
품목이다:

    도매 경매가(Manheim) ──2~3개월──> CPI 중고차 ──> 코어 CPI

2021~22 인플레의 상당 부분이 이 경로였는데, `indicators.yaml`의 절사평균 CPI note는
"2021~22 중고차·신차 급등은 식품도 에너지도 아니라 코어에 그대로 들어갔다"고 **논거로 쓰면서
정작 그 계열을 하나도 수집하지 않고 있었다**(2026-09-24 발견). 선행지표 없이 결과만 본 셈이다.

⚠ 한계 (yaml note에도 명시할 것):
- **Manheim은 도매다.** CPI 중고차는 소매다. 딜러 마진·재고회전이 사이에 끼므로 전달은
  기계적이지 않고, 전달 시차(통상 2~3개월)는 안정적인 상수가 아니다
- Manheim은 Cox Automotive의 **사유 지수**다. 산출 방법이 공개되어 있지 않고,
  2023-01 발표 때 전체 계열이 소급 재산출됐다(기준도 1995=100 → **1997-01=100**으로 변경).
  과거 보고서에 적힌 값과 지금 값이 다를 수 있다 — 시점 비교 시 같은 빈티지인지 확인할 것
- 월중 발표되는 mid-month 값은 **잠정치**다. 여기서는 확정 월값만 싣는다
- NY연은 오토론 연체율은 **분기**이고 참조분기 종료 후 약 1개월 시차가 있다.
  Equifax 소비자신용패널 표본 추정치이지 전수가 아니다
"""
from __future__ import annotations

import re
from datetime import date
from typing import Any

from .base import BROWSER_UA, N_OBS, get_bytes, get_text, result
from .xlsx import read_sheet

# ── Manheim ────────────────────────────────────────────────────────────
# site.manheim.com 쪽 랜딩은 2026-09-24 확인 시점에 **2025-12에서 멈춰 있었다**
# (첨부 xlsx도 Nov-2025판). 실제로 갱신되는 곳은 Cox Automotive 인사이트다.
COX_POST = ("https://www.coxautoinc.com/insights/"
            "manheim-used-vehicle-value-index-{month}-{year}-trends/")
MANHEIM_PAGE = "https://site.manheim.com/en/services/consulting/used-vehicle-value-index.html"

MONTH_NAMES = ["january", "february", "march", "april", "may", "june",
               "july", "august", "september", "october", "november", "december"]

# "Index (MUVVI) in August was 208.2" — 2026-09-24 실측한 문장 형태.
# 발표문 문구가 흔들려도 견디도록 'MUVVI' 이후 첫 3자리 지수값을 잡는다.
_MUVVI_VALUE = re.compile(r"MUVVI\)?[^.]{0,120}?\b(\d{3}(?:\.\d)?)\b")


def _plain(html: str) -> str:
    t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", html, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    for a, b in (("&nbsp;", " "), ("&amp;", "&"), ("&#8217;", "'"), ("&rsquo;", "'")):
        t = t.replace(a, b)
    return re.sub(r"\s+", " ", t)


def fetch_manheim(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """Manheim 중고차 가치지수(MUVVI). 월간, 1997-01 = 100. 키 불필요.

    yaml 예시:

        method: scrape
        source: manheim

    발표월을 현재 달부터 거꾸로 짚는다. 확정 월값은 다음 달 초에 올라오므로
    현재 달은 대개 404다 — 결측이 아니라 **아직 안 나온 것**이라 조용히 건너뛴다.
    """
    want = int(ind.get("points") or 4)
    today = date.today()
    y, m = today.year, today.month

    obs: list[dict[str, Any]] = []
    errors: list[str] = []
    urls: list[str] = []
    # 원하는 개수 + 2달치를 훑는다. 발표 지연 한 달은 정상이므로 여유를 준다.
    for _ in range(want + 2):
        if len(obs) >= want:
            break
        url = COX_POST.format(month=MONTH_NAMES[m - 1], year=y)
        try:
            # 미발표 달은 404가 정상이라 재시도하지 않는다(retries=0) — 헛되이 느려진다
            body = get_text(url, retries=0)
        except Exception as e:
            # 404는 "아직 미발표"라 정상이다. 그 외 오류만 기록한다.
            if "404" not in str(e):
                errors.append(f"{y}-{m:02d}: {type(e).__name__}")
            m = 12 if m == 1 else m - 1
            y = y - 1 if m == 12 else y
            continue
        mt = _MUVVI_VALUE.search(_plain(body))
        if mt:
            obs.append({"date": f"{y}-{m:02d}-01", "value": float(mt.group(1)),
                        "label": "Manheim 중고차지수 (1997-01=100)"})
            urls.append(url)
        else:
            errors.append(f"{y}-{m:02d}: 지수값 파싱 실패(발표문 서식 변경 의심)")
        m = 12 if m == 1 else m - 1
        y = y - 1 if m == 12 else y

    if not obs:
        return result(ind, "fail",
                      error="; ".join(errors) or "발표문을 찾지 못했다",
                      source_url=MANHEIM_PAGE)
    res = result(ind, "ok", observations=obs, source_url=urls[0] if urls else MANHEIM_PAGE)
    if errors:
        res["error"] = "; ".join(errors)
    return res


# ── NY연은 가계부채·신용 보고서 (HHDC) ──────────────────────────────────
HHDC_XLSX = ("https://www.newyorkfed.org/medialibrary/interactives/"
             "householdcredit/data/xls/HHD_C_Report_{q}.xlsx")
HHDC_PAGE = "https://www.newyorkfed.org/microeconomics/hhdc"

# 같은 실행에서 지표 여러 개가 같은 워크북을 쓴다. 1MB짜리를 지표 수만큼 받지 않는다.
_wb_cache: dict[str, bytes] = {}


def _latest_workbook() -> tuple[bytes, str]:
    """최신 분기 보고서를 찾아 내려받는다. 현재 분기부터 최대 4분기 거슬러 올라간다."""
    today = date.today()
    y, q = today.year, (today.month - 1) // 3 + 1
    last_err = ""
    for _ in range(5):
        tag = f"{y}Q{q}"
        if tag in _wb_cache:
            return _wb_cache[tag], tag
        try:
            raw = get_bytes(HHDC_XLSX.format(q=tag), headers={"User-Agent": BROWSER_UA})
            # ⚠ 미발표 분기는 404가 아니라 **302로 HTML 안내 페이지**를 돌려준다(2026-09-24 실측).
            #   상태코드만 믿으면 HTML을 워크북으로 열다 BadZipFile로 죽는다. 매직바이트로 거른다.
            if not raw.startswith(b"PK"):
                last_err = f"{tag}: 미발표(HTML 응답)"
                raise ValueError(last_err)
            _wb_cache[tag] = raw
            return raw, tag
        except Exception as e:
            last_err = f"{tag}: {type(e).__name__}" if not last_err.startswith(tag) else last_err
        q -= 1
        if q == 0:
            q, y = 4, y - 1
    raise RuntimeError(f"HHDC 워크북을 찾지 못했다 ({last_err})")


def _quarter_to_date(s: str) -> str | None:
    """'26:Q2' → '2026-04-01'. 분기 시작일로 맞춘다(FRED 분기 계열과 같은 규약)."""
    mt = re.match(r"^\s*(\d{2}):Q([1-4])\s*$", str(s))
    if not mt:
        return None
    yy, qq = int(mt.group(1)), int(mt.group(2))
    year = 2000 + yy if yy < 80 else 1900 + yy
    return f"{year}-{(qq - 1) * 3 + 1:02d}-01"


def fetch_hhdc(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """NY연은 가계부채·신용 보고서의 한 표. 분기, 키 불필요.

    yaml 예시:

        method: api
        source: nyfed_hhdc
        sheet: "Page 12 Data"
        columns: [AUTO, CC, ALL]
        labels:
          AUTO: 오토론 90+ 연체 비중(%)

    첫 열이 '26:Q2' 형태의 분기 라벨이고 헤더행에 열 이름이 있다. 열은 **이름으로** 고른다 —
    위치로 잡으면 원본이 열을 하나 끼워 넣을 때 조용히 다른 계열을 싣게 된다.
    """
    sheet = str(ind.get("sheet") or "Page 12 Data")
    cols = ind.get("columns") or ["AUTO"]
    if isinstance(cols, str):
        cols = [cols]
    labels = ind.get("labels") or {}

    raw, tag = _latest_workbook()
    rows = read_sheet(raw, sheet)
    if not rows:
        return result(ind, "fail", source_url=HHDC_PAGE,
                      error=f"시트 '{sheet}' 없음 — {tag} 워크북 서식이 바뀌었다")

    # 헤더행 = 요청한 열 이름을 담은 첫 행.
    want = {str(c).strip().upper() for c in cols}
    hdr_i, idx = -1, {}
    for i, row in enumerate(rows[:12]):
        names = {str(c).strip().upper(): j for j, c in enumerate(row) if c not in (None, "")}
        if want & set(names):
            hdr_i, idx = i, names
            break
    if hdr_i < 0:
        return result(ind, "fail", source_url=HHDC_PAGE,
                      error=f"열 {sorted(want)} 를 헤더에서 못 찾았다 (시트 '{sheet}')")

    missing = sorted(want - set(idx))
    obs: list[dict[str, Any]] = []
    for row in rows[hdr_i + 1:]:
        if not row:
            continue
        d = _quarter_to_date(row[0])
        if not d:
            continue
        for c in cols:
            j = idx.get(str(c).strip().upper())
            if j is None or j >= len(row) or row[j] in (None, ""):
                continue
            try:
                v = float(row[j])
            except (TypeError, ValueError):
                continue
            obs.append({"date": d, "value": round(v, 2),
                        "label": labels.get(c, str(c))})

    if not obs:
        return result(ind, "fail", source_url=HHDC_PAGE,
                      error=f"분기 행을 파싱하지 못했다 (시트 '{sheet}')")
    # 최신 N분기만 남긴다 — 날짜 기준으로 잘라야 다중 열일 때 한 열이 밀려나지 않는다.
    keep = sorted({o["date"] for o in obs})[-int(ind.get("points") or N_OBS // 2 or 3):]
    # ⚠ 최신이 앞이다. __main__의 STALE 출력이 observations[0]을 "최신"으로 찍기 때문에
    #   오래된 것부터 담으면 경고문에 엉뚱한 날짜가 나온다(2026-09-24에 실제로 그랬다).
    obs = sorted((o for o in obs if o["date"] in keep), key=lambda o: o["date"], reverse=True)

    res = result(ind, "ok", observations=obs, source_url=HHDC_PAGE)
    if missing:
        res["error"] = f"헤더에 없는 열: {missing}"
    return res
