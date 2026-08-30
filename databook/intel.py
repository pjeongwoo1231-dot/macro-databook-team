"""정보 수집기 — **검색엔진을 치지 않는다.** API · 공개 CSV · RSS만 친다.

**왜 필요한가** — 볼트의 거시 축은 FRED를 직접 치는데
**지정학·원자재만 네이버·구글 뉴스를 긁고 있었다.** 검색엔진은 1차 자료의 3차 재탕을 물어온다.
같은 패턴(직접 API)을 지정학·물류 축에도 옮긴다.

**곁들여: 쿼리 언어가 소스 계층을 정한다.** "중국 원유 수입"으로 검색하면 연합뉴스가,
"China crude oil imports"로 검색하면 EIA가 나온다. 한국어로 긁는 한 1차 자료에 닿지 못한다.

3계층
1. **숫자** — EIA v2 · IMF PortWatch · UN Comtrade · FRED (API/정형)
2. **해석** — RSS (기관 발간물)
3. **촉매** — `intel_catalysts.yaml` (날짜가 박힌 이벤트. 손으로 유지)

**수집이 곧 검증이 되게 한다.** 모든 지표 노트에 `hypothesis`와 `direction`이 박히고,
직전 값과 비교해 지지/반박을 자동 판정한다. 판정할 수 없으면 `unset`으로 남겨
**대시보드의 "판정 대기"에 띄운다 — 조용히 넘기지 않는다.**

⚠ `verified` 필드는 **실호출로 확인한 것만** true다. 추정으로 적지 않는다.
"""
from __future__ import annotations

import csv
import io
import json
import re
import urllib.parse
import urllib.request
import gzip
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml

from .core import OUTPUT_DIR, ROOT, load_env

REG = ROOT / "intel_sources.yaml"
CAT = ROOT / "intel_catalysts.yaml"
STATE = OUTPUT_DIR / "intel_state.json"
UA = {"User-Agent": "MacroVault/1.0 (macro research)"}

PORTWATCH = ("https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services"
             "/Daily_Chokepoints_Data/FeatureServer/0/query")
EIA = "https://api.eia.gov/v2"
COMTRADE = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"
FRED = "https://api.stlouisfed.org/fred/series/observations"


def _get(url: str, timeout: int = 60) -> bytes:
    r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout)
    b = r.read()
    return gzip.decompress(b) if b[:2] == b"\x1f\x8b" else b


def _json(url: str, timeout: int = 60) -> Any:
    return json.loads(_get(url, timeout))


# ── 계층 1: 숫자 ────────────────────────────────────────────
def h_portwatch(s: dict, env: dict) -> list[dict]:
    """IMF PortWatch 일별 초크포인트 통항. 키 불필요.

    ⚠ **초크포인트 간 절대 수준을 비교하지 않는다.** 집계 방식 때문에
      호르무즈는 평상시에도 하루 평균 8.4건이다(2026-06~08 실측).
      자기 표본 대비 변화로만 읽는다.
    """
    q = urllib.parse.urlencode({
        "where": f"portid='{s['chokepoint']}'", "outFields": f"date,{s['field']},portname",
        "f": "json", "orderByFields": "date DESC", "resultRecordCount": 90})
    rows = [f["attributes"] for f in _json(f"{PORTWATCH}?{q}").get("features", [])]
    rows.sort(key=lambda a: a["date"], reverse=True)
    return [{"period": a["date"], "value": a.get(s["field"]), "meta": a.get("portname")}
            for a in rows if a.get(s["field"]) is not None]


def h_eia_v2(s: dict, env: dict) -> list[dict]:
    key = env.get("EIA_API_KEY", "")
    if not key:
        raise RuntimeError("EIA_API_KEY 없음 (.env 확인)")
    p = {"api_key": key, "data[0]": "value", "frequency": s.get("frequency", "monthly"),
         "sort[0][column]": "period", "sort[0][direction]": "desc", "length": "24"}
    q = urllib.parse.urlencode(p)
    for k, v in (s.get("facets") or {}).items():
        q += f"&facets[{k}][]={urllib.parse.quote(str(v))}"
    d = _json(f"{EIA}/{s['route']}/data/?{q}")
    rows = d.get("response", {}).get("data", [])
    out = []
    for r in rows:
        try:
            out.append({"period": r["period"], "value": float(r["value"]),
                        "meta": r.get("series-description") or r.get("product-name")})
        except (TypeError, ValueError, KeyError):
            continue
    return out


def h_comtrade(s: dict, env: dict) -> list[dict]:
    """UN Comtrade preview — 키 불필요, **연간만**.

    ⚠ 월별이 필요하면 각국 관세청을 쳐야 한다. 중국 해관은 봇 차단(412)이다.
    """
    # ⚠ preview API는 **연도를 하나씩만** 받는다(콤마로 여러 개 넣으면 400).
    #   게다가 rate limit이 빡빡해 429가 난다 — 호출 사이를 벌린다.
    import time
    out = []
    for i in range(int(s.get("years", 5))):
        yr = date.today().year - 1 - i
        q = urllib.parse.urlencode({
            "reporterCode": s["reporter"], "period": yr, "partnerCode": s.get("partner", 0),
            "cmdCode": s["cmd"], "flowCode": s.get("flow", "M")})
        try:
            d = _json(f"{COMTRADE}?{q}", 90)
        except Exception:
            time.sleep(6)          # 429면 한 번 더 쉬고 넘어간다 — 없는 해는 없는 대로 둔다
            continue
        for r in d.get("data", []):
            v = r.get("primaryValue") or r.get("fobvalue") or r.get("cifvalue")
            if v is None:
                continue
            out.append({"period": str(r.get("period")), "value": float(v),
                        "meta": r.get("cmdDesc") or s["cmd"]})
        time.sleep(3)
    out.sort(key=lambda x: x["period"], reverse=True)
    return out


def h_fred(s: dict, env: dict) -> list[dict]:
    key = env.get("FRED_API_KEY", "")
    if not key:
        raise RuntimeError("FRED_API_KEY 없음")
    today = date.today().isoformat()
    q = urllib.parse.urlencode({
        "series_id": s["series_id"], "api_key": key, "file_type": "json",
        "sort_order": "desc", "limit": 24, "observation_end": today})
    d = _json(f"{FRED}?{q}")
    return [{"period": o["date"], "value": float(o["value"]), "meta": s["series_id"]}
            for o in d.get("observations", []) if o.get("value") not in (".", "", None)]


def _sheet_names(raw: bytes) -> list[str]:
    """xlsx 워크북의 시트 이름을 순서대로. read_sheet가 인덱스만 받아서 필요하다."""
    import zipfile
    zf = zipfile.ZipFile(io.BytesIO(raw))
    xml = zf.read("xl/workbook.xml").decode("utf-8", "replace")
    return re.findall(r'<sheet[^>]*name="([^"]+)"', xml)


_XLSX_CACHE: dict[str, bytes] = {}


def h_xlsx_url(s: dict, env: dict) -> list[dict]:
    """공개 엑셀 직링크 → 한 컬럼의 시계열. World Bank Pink Sheet용.

    ⚠ **헤더 행을 "문자열 셀이 가장 많은 행"으로 찾으면 틀린다.** Pink Sheet는
      품목명 행 바로 아래에 단위 행(`($/bbl)`)이 있고, 단위는 전 컬럼에 다 차 있어서
      휴리스틱이 단위 행을 헤더로 잡는다 → 컬럼 조회가 전부 None이 된다(실측 2026-08-24).
      그래서 **찾으려는 컬럼명이 실제로 들어 있는 행**을 헤더로 삼는다.

    ⚠ URL에 판(edition) 코드가 박혀 있다. 연초에 아래에서 링크를 갱신할 것.
      https://www.worldbank.org/en/research/commodity-markets
    """
    from .fetchers.xlsx import read_sheet

    url = s["url"]
    if url not in _XLSX_CACHE:          # 같은 통합문서를 쓰는 계열이 여럿이다. 한 번만 받는다
        _XLSX_CACHE[url] = _get(url, 120)
    raw = _XLSX_CACHE[url]

    names = _sheet_names(raw)
    want_sheet = s.get("sheet")
    idx = names.index(want_sheet) if want_sheet in names else 0
    rows = read_sheet(raw, idx)
    col = str(s["column"]).strip().upper()

    hdr_i = next((i for i in range(min(15, len(rows)))
                  if any(isinstance(c, str) and c.strip().upper() == col for c in rows[i])), None)
    if hdr_i is None:
        raise RuntimeError(f"컬럼 '{s['column']}' 없음 (시트 {names[idx]})")
    header = [str(c).strip().upper() if c is not None else "" for c in rows[hdr_i]]
    ci = header.index(col)

    out = []
    for r in rows[hdr_i + 1:]:
        if not r or not isinstance(r[0], str) or ci >= len(r):
            continue
        period = r[0].strip()
        if not re.match(r"^\d{4}[MQ]\d{1,2}$", period):   # 단위 행·주석 행을 여기서 거른다
            continue
        try:
            out.append({"period": period, "value": float(r[ci]), "meta": s["column"]})
        except (TypeError, ValueError):
            continue                    # '…' = 결측
    out.sort(key=lambda x: x["period"], reverse=True)
    return out[:24]


def h_sdmx_json(s: dict, env: dict) -> list[dict]:
    """SDMX-JSON. BIS · ECB 공용.

    ⚠ **두 서버의 Accept 요구가 정반대다**(실측 2026-08-24).
      BIS  — sdmx-json Accept를 줘야 JSON이 온다. 없으면 200이지만 XML이라 파싱이 깨진다
      ECB  — 그 Accept를 주면 **406**. generic json을 써야 한다
    그래서 accept는 소스별로 yaml에서 지정한다.
    """
    url = s["url"]
    if s.get("params"):
        url += ("&" if "?" in url else "?") + urllib.parse.urlencode(s["params"])
    hdr = dict(UA)
    hdr["Accept"] = s.get("accept", "application/json")
    r = urllib.request.urlopen(urllib.request.Request(url, headers=hdr), timeout=60)
    b = r.read()
    if b[:2] == b"\x1f\x8b":
        b = gzip.decompress(b)
    j = json.loads(b)

    root = j.get("data", j)
    series = list(root["dataSets"][0]["series"].values())[0]["observations"]
    dims = root["structure"]["dimensions"]["observation"][0]["values"]
    out = []
    for k in sorted(series, key=int, reverse=True):
        v = series[k][0]
        if v in (None, "NaN", ""):
            continue
        period = dims[int(k)]["id"] if int(k) < len(dims) else k
        out.append({"period": str(period), "value": float(v), "meta": s.get("label")})
    return out


def h_socrata(s: dict, env: dict) -> list[dict]:
    """Socrata Open Data API. CFTC COT(투기적 순포지션)용. 키 불필요.

    "가격이 어디로 가나"가 아니라 "누가 어느 쪽에 서 있나"를 보는 공개 데이터다.
    ⚠ 순포지션 극단치는 **반전 신호로 읽히지만 타이밍을 주지는 않는다.**
      볼트 규칙대로 자기 표본 백분위로 읽고, 수준만으로 방향을 부르지 않는다.
    """
    q = {"$limit": s.get("limit", 24), "$order": f"{s['date_field']} DESC"}
    for field, val in (s.get("filter_contains") or {}).items():
        q["$where"] = f"{field} like '%{val}%'"
    rows = _json(f"{s['url']}?{urllib.parse.urlencode(q)}", 60)

    expr = s.get("compute")
    m = re.match(r"^\s*(\w+)\s*([-+])\s*(\w+)\s*$", expr) if expr else None
    if expr and not m:
        raise RuntimeError(f"compute 형식 오류: {expr}")

    out = []
    for r in rows:
        try:
            if m:
                a, b2 = float(r[m.group(1)]), float(r[m.group(3)])
                v = a - b2 if m.group(2) == "-" else a + b2
            else:
                v = float(r[s["value_field"]])
            out.append({"period": str(r[s["date_field"]])[:10], "value": v,
                        "meta": r.get("market_and_exchange_names", "")[:48]})
        except (TypeError, ValueError, KeyError):
            continue
    return out


HANDLERS = {"portwatch": h_portwatch, "eia_v2": h_eia_v2,
            "comtrade": h_comtrade, "fred": h_fred,
            "xlsx_url": h_xlsx_url, "sdmx_json": h_sdmx_json, "socrata": h_socrata}


# ── 계층 2: 해석 (RSS) ──────────────────────────────────────
def h_rss(s: dict) -> list[dict]:
    raw = _get(s["url"], 45).decode("utf-8", "replace")
    items = re.findall(r"<(?:item|entry)[ >].*?</(?:item|entry)>", raw, re.S)
    out = []
    for it in items[:int(s.get("limit", 12))]:
        t = re.search(r"<title[^>]*>(.*?)</title>", it, re.S)
        l = re.search(r"<link[^>]*>(.*?)</link>", it, re.S) or re.search(r'<link[^>]*href="(.*?)"', it)
        dt = re.search(r"<(?:pubDate|updated|published)>(.*?)</", it, re.S)
        if not t:
            continue
        clean = lambda x: re.sub(r"<!\[CDATA\[|\]\]>|<[^>]+>", "", x).strip()
        out.append({"title": clean(t.group(1))[:200],
                    "link": clean(l.group(1)) if l else "",
                    "date": clean(dt.group(1))[:25] if dt else ""})
    return out



def num(v: float) -> str:
    """사람이 읽는 수 표기.

    `,.4g`를 쓰면 13543이 `1.354e+04`가 된다 — **가격을 지수표기로 적으면 못 읽는다.**
    크기에 따라 소수 자릿수만 줄이고 지수표기는 쓰지 않는다.
    """
    a = abs(v)
    if a >= 1000:
        return f"{v:,.0f}"
    if a >= 10:
        return f"{v:,.2f}".rstrip("0").rstrip(".")
    return f"{v:,.4f}".rstrip("0").rstrip(".")


def feed_age(items: list[dict]) -> int | None:
    """피드에서 가장 최신 항목이 며칠 전인가. 날짜를 못 읽으면 None.

    ⚠ **HTTP 200은 살아 있다는 뜻이 아니다.** 실측 사례:
      CSIS(최신 2016-03) · VoxEU/CEPR(최신 2024-04, 게다가 항목이 주제 분류명)
      둘 다 200을 주고 항목 수도 정상이라 **성공으로 집계됐다.**
      최신 항목 날짜를 보지 않으면 죽은 피드를 매일 성공으로 센다.
    """
    from email.utils import parsedate_to_datetime
    best = None
    for it in items:
        raw = (it.get("date") or "").strip()
        if not raw:
            continue
        d = None
        try:
            d = parsedate_to_datetime(raw).date()          # RFC822 (pubDate)
        except Exception:
            m = re.match(r"(\d{4})-(\d{2})-(\d{2})", raw)   # ISO8601 (Atom)
            if m:
                d = date(*map(int, m.groups()))
        if d and (best is None or d > best):
            best = d
    return None if best is None else (date.today() - best).days


# ── 판정 ────────────────────────────────────────────────────
def judge(s: dict, cur: float, prev: float | None) -> str:
    """직전 값 대비 방향이 가설을 지지하는가.

    **판정할 수 없으면 unset을 돌려준다.** 억지로 supports/contra를 만들지 않는다.
    """
    if not s.get("hypothesis"):
        return "neutral"
    if prev is None:
        return "unset"
    if cur > prev:
        return s.get("direction_if_up", "unset")
    if cur < prev:
        return s.get("direction_if_down", "unset")
    return "neutral"


def _state() -> dict:
    if STATE.exists():
        try:
            return json.loads(STATE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def _fm(v: Any) -> str:
    if v is None:
        return "null"
    if isinstance(v, str) and (":" in v or v.startswith("[")):
        return f'"{v}"'
    return str(v)


def write_indicator(vault: Path, s: dict, obs: list[dict], prev: float | None) -> Path:
    cur = obs[0]
    direction = judge(s, cur["value"], prev)
    hyp = s.get("hypothesis")
    body_hist = "\n".join(f"| {o['period']} | {num(o['value'])} |" for o in obs[:12])
    chg = (("+" if cur['value'] >= prev else "-") + num(abs(cur['value'] - prev))) if prev is not None else "—"
    # f-string 안에 백슬래시를 못 쓰므로 밖에서 만든다
    wait_box = ("> [!warning] 판정 대기\n"
                "> 직전 값이 없어 방향을 정할 수 없다. 다음 수집에서 판정된다.\n"
                if direction == "unset" else "")
    p = vault / "10-indicators" / f"{s['id']}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(f"""---
type: indicator
source: {s['handler']}
metric: {s['id']}
label: {_fm(s.get('label'))}
value: {cur['value']}
unit: {_fm(s.get('unit'))}
period: {_fm(cur['period'])}
retrieved: {date.today().isoformat()}
hypothesis: {f'"[[{hyp}]]"' if hyp else 'null'}
direction: {direction}
prev_value: {prev if prev is not None else 'null'}
verified_source: {str(s.get('verified', False)).lower()}
tags: [type/indicator, domain/intel]
---

# {s.get('label', s['id'])}

**{num(cur['value'])} {s.get('unit', '')}** ({cur['period']}) · 직전 대비 **{chg}**
{f"→ 가설 **[[{hyp}]]** 에 대해 **{direction}**" if hyp else "→ 가설 미연결 (백본 계열)"}

{wait_box}
{s.get('note', '')}

## 최근 관측

| 기간 | 값 |
|---|---:|
{body_hist}

---
`{s['handler']}` · 수집 {datetime.now():%Y-%m-%d %H:%M} · 이 노트는 자동 생성된다.
""", encoding="utf-8")
    return p


def write_reading(vault: Path, feeds: dict[str, list[dict]],
                  headline_only: set[str] | None = None) -> Path:
    """읽을거리 노트를 쓴다.

    headline_only: 본문을 확보할 수 없는 피드의 label 집합.
    그런 피드는 배너로 명시한다 — 표시하지 않으면 '수집됐다'는 착시만 남는다
    (2026-08-30: Reuters 20건이 전부 판독 불가였는데 목록상으로는 정상으로 보였다).
    """
    headline_only = headline_only or set()
    p = vault / "15-reading" / f"{date.today().isoformat()}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    secs, n_read, n_head = [], 0, 0
    for label, items in feeds.items():
        rows = "\n".join(f"- [{i['title']}]({i['link']}) <small>{i['date']}</small>" for i in items)
        if label in headline_only:
            n_head += len(items)
            secs.append(f"## {label}\n\n"
                        f"> ⚠ **본문 판독 불가 — 헤드라인 신호로만 쓴다.** 링크를 열어도 본문이 안 나온다.\n"
                        f"> 여기 항목으로 주장을 세우지 말 것. 같은 사건은 다른 피드에서 본문을 찾는다.\n\n"
                        f"{rows or '_(항목 없음)_'}\n")
        else:
            n_read += len(items)
            secs.append(f"## {label}\n\n{rows or '_(항목 없음)_'}\n")
    p.write_text(f"""---
type: reading
retrieved: {date.today().isoformat()}
readable: {n_read}
headline_only: {n_head}
tags: [type/reading, domain/intel]
---

# 읽을거리 {date.today().isoformat()}

> 기관 1차·2차 발간물 RSS. **검색엔진 결과가 아니다.**
> **본문 판독 가능 {n_read}건 · 헤드라인 전용 {n_head}건** — 뒤쪽은 섹션마다 배너로 표시했다.
> 트리아지 대기 — 읽고 값어치가 있으면 가설 노트나 지표 노트로 옮긴다.

{chr(10).join(secs)}
""", encoding="utf-8")
    return p


def write_catalysts(vault: Path) -> Path | None:
    if not CAT.exists():
        return None
    cats = yaml.safe_load(CAT.read_text(encoding="utf-8")) or {}
    items = cats.get("catalysts", [])
    today = date.today()
    rows = []
    for c in sorted(items, key=lambda x: str(x.get("date", ""))):
        try:
            dd = datetime.strptime(str(c["date"]), "%Y-%m-%d").date()
        except (ValueError, KeyError):
            continue
        left = (dd - today).days
        if left < -7:
            continue
        tag = "**지남**" if left < 0 else (f"**D-{left}**" if left <= 30 else f"D-{left}")
        hyp = f"[[{c['hypothesis']}]]" if c.get("hypothesis") else "—"
        rows.append(f"| {c['date']} | {tag} | {c.get('label','')} | {hyp} | {c.get('why','')} |")
    p = vault / "00-dashboard" / "촉매 캘린더.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(f"""---
type: dashboard
updated: {today.isoformat()}
tags: [type/dashboard, domain/intel]
---

# 촉매 캘린더

> **날짜가 박힌 이벤트만** 모은다. 유예 만료·예산 확정·정례 회의처럼
> **검색엔진 스크래핑으로는 안 나오는 층위**이고, 실제로 포지션을 잡게 해주는 건 이쪽이다.
> `intel_catalysts.yaml`을 손으로 유지한다 — **이 시스템에서 가장 값나가는 파일이다.**

| 날짜 | | 이벤트 | 가설 | 왜 중요한가 |
|---|---|---|---|---|
{chr(10).join(rows)}

---
자동 생성 {datetime.now():%Y-%m-%d %H:%M} · 원본 `intel_catalysts.yaml`
""", encoding="utf-8")
    return p


def collect(only: str = "", dry_run: bool = False, log=print) -> int:
    env = load_env()
    vault = Path(env.get("OBSIDIAN_VAULT_PATH") or (OUTPUT_DIR / "vault"))
    reg = yaml.safe_load(REG.read_text(encoding="utf-8"))
    st = _state()
    ok = fail = 0
    unset = []
    stale = []

    if only in ("", "indicators"):
        log(f"[지표] {len(reg.get('indicators', []))}개")
        for s in reg.get("indicators", []):
            fn = HANDLERS.get(s["handler"])
            if not fn:
                log(f"  ✘ {s['id']}: 미지원 handler {s['handler']}")
                fail += 1
                continue
            try:
                obs = fn(s, env)
            except Exception as e:
                log(f"  ✘ {s['id']}: {type(e).__name__} {str(e)[:70]}")
                fail += 1
                continue
            if not obs:
                log(f"  ✘ {s['id']}: 관측 없음")
                fail += 1
                continue
            prev = st.get(s["id"], {}).get("value")
            d = judge(s, obs[0]["value"], prev)
            if not dry_run:
                write_indicator(vault, s, obs, prev)
                st[s["id"]] = {"value": obs[0]["value"], "period": obs[0]["period"],
                               "retrieved": date.today().isoformat()}
            if d == "unset" and s.get("hypothesis"):
                unset.append(s["id"])
            log(f"  ✔ {s['id']:24} {num(obs[0]['value']):>14} {s.get('unit',''):10} {obs[0]['period']:11} → {d}")
            ok += 1

    if only in ("", "reading"):
        feeds, headline_only = {}, set()
        for s in reg.get("reading", []):
            try:
                items = h_rss(s)
                feeds[s["label"]] = items
                if s.get("headline_only"):
                    headline_only.add(s["label"])
                age = feed_age(items)
                # 날짜를 못 읽는 피드(NBER 등)는 신선도를 판정할 수 없다 — 그것도 표시한다
                tag = "날짜없음" if age is None else f"{age}일 전"
                limit = int(s.get("stale_days", 60))
                if age is not None and age > limit:
                    log(f"  ⚠ RSS {s['id']:20} {len(items):>3}건  최신 {tag} — **정체된 피드다**")
                    stale.append(f"{s['id']}({tag})")
                else:
                    log(f"  ✔ RSS {s['id']:20} {len(items):>3}건  최신 {tag}")
                ok += 1
            except Exception as e:
                log(f"  ✘ RSS {s['id']}: {type(e).__name__} {str(e)[:60]}")
                fail += 1
        if feeds and not dry_run:
            write_reading(vault, feeds, headline_only)

    if only in ("", "catalysts") and not dry_run:
        p = write_catalysts(vault)
        if p:
            log(f"  ✔ 촉매 캘린더 → {p.name}")

    if not dry_run:
        STATE.parent.mkdir(parents=True, exist_ok=True)
        STATE.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")

    log(f"\n완료: 성공 {ok} / 실패 {fail}")
    if unset:
        log(f"⚠ 판정 대기 {len(unset)}건 (직전 값 없음): {', '.join(unset)}")
    if stale:
        log(f"⚠ 정체된 피드 {len(stale)}건 — 200을 주지만 새 글이 없다: {', '.join(stale)}")
    log(f"  → {vault}")
    return 1 if fail and not ok else 0
