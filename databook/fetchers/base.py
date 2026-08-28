"""공통 HTTP 헬퍼 + 결과 규격."""
from __future__ import annotations

import html
import html
import json
import re
import time
import urllib.parse
import urllib.request
from typing import Any

UA = "macro-databook/0.1 (study-group data pipeline)"
TIMEOUT = 20
_last_call: dict[str, float] = {}


def throttle(host: str, min_interval: float = 0.6) -> None:
    now = time.monotonic()
    prev = _last_call.get(host, 0.0)
    wait = prev + min_interval - now
    if wait > 0:
        time.sleep(wait)
    _last_call[host] = time.monotonic()


def get_json(url: str, params: dict[str, Any] | None = None, retries: int = 2,
             headers: dict[str, str] | None = None) -> Any:
    if params:
        sep = "&" if "?" in url else "?"
        url = url + sep + urllib.parse.urlencode(params)
    host = urllib.parse.urlparse(url).netloc
    last_err: Exception | None = None
    for attempt in range(retries + 1):
        throttle(host)
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": UA, "Accept": "application/json", **(headers or {})})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:  # 일시 오류(RemoteDisconnected, 5xx 등) 재시도
            last_err = e
            time.sleep(1.5 * (attempt + 1))
    raise last_err  # type: ignore[misc]


def get_text(url: str, headers: dict[str, str] | None = None, encoding: str = "utf-8", retries: int = 1) -> str:
    host = urllib.parse.urlparse(url).netloc
    last_err: Exception | None = None
    for attempt in range(retries + 1):
        throttle(host)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": BROWSER_UA, **(headers or {})})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                return resp.read().decode(encoding, "replace")
        except Exception as e:
            last_err = e
            time.sleep(1.0 * (attempt + 1))
    raise last_err  # type: ignore[misc]


def get_bytes(url: str, headers: dict[str, str] | None = None, retries: int = 1) -> bytes:
    """바이너리 다운로드(엑셀 등) — get_text와 달리 디코딩하지 않고 원본 바이트를 반환."""
    host = urllib.parse.urlparse(url).netloc
    last_err: Exception | None = None
    for attempt in range(retries + 1):
        throttle(host)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": BROWSER_UA, **(headers or {})})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                return resp.read()
        except Exception as e:
            last_err = e
            time.sleep(1.0 * (attempt + 1))
    raise last_err  # type: ignore[misc]


BROWSER_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"


_UNIT_PAT = None


def unit_from_labels(observations: list[dict[str, Any]]) -> str:
    """라벨 끝의 괄호에서 단위를 뽑는다 — "유로존 HICP YoY(%)" -> "%".

    eurostat·ecb·dbnomics 지표는 db_labels/label에 이미 단위를 적어두는 관례라
    사람이 yaml에 unit을 또 쓰는 대신 여기서 재사용한다. 못 뽑으면 빈 문자열이고,
    그건 "미확보"로 남아 unitcheck가 보고한다 — 추측해서 채우지 않는다.
    """
    global _UNIT_PAT
    if _UNIT_PAT is None:
        import re
        _UNIT_PAT = re.compile(r"[（(]([^()（）]{1,24})[)）]\s*$")
    found = set()
    for o in observations:
        lab = str(o.get("label") or "").strip()
        m = _UNIT_PAT.search(lab)
        if m:
            found.add(m.group(1).strip())
    if len(found) == 1:
        return found.pop()
    return ""


def result(
    ind: dict[str, Any],
    status: str,
    observations: list[dict[str, Any]] | None = None,
    source_url: str = "",
    error: str = "",
    note: str | None = None,
    unit: str = "",
) -> dict[str, Any]:
    """status: ok | fail | manual | stub | derived_pending"""
    return {
        "name": ind["name"],
        "team": ind.get("team", ""),
        "tier": ind.get("tier", 2),
        "method": ind.get("method", ""),
        "source": ind.get("source", ""),
        "status": status,
        "observations": observations or [],  # [{"date": "YYYY-MM-DD", "value": float|str, "label": str?}]
        # yaml에 사람이 적은 unit을 fetcher가 전달하지 않아도 실리게 한다.
        # 이게 없어서 indicators.yaml의 unit이 스냅샷에 전혀 반영되지 않고 있었다(2026-08-26).
        "unit": unit or ind.get("unit", "") or unit_from_labels(observations or []),
        "unit_check": ind.get("unit_check", ""),
        "max_age_days": ind.get("max_age_days"),
        "source_url": source_url,
        "error": error,
        "note": note if note is not None else ind.get("note", ""),
        # Obsidian 지표 노드 수동 지정(선택). 빈 값이면 이름으로 자동 매칭, "-"면 매칭 안 함.
        "vault_node": ind.get("vault_node", ""),
    }

# ─────────────────── 공통 헬퍼 (2026-08-28 통합) ───────────────────
# fetcher를 하나씩 붙이면서 같은 코드를 매번 새로 썼다. ponytail-audit에서
# 전년비 3벌·_norm 2벌·N_OBS 8벌이 잡혀 여기로 모았다.

N_OBS = 6                       # 기본 표시 관측 수. 지표별로 points/n_obs로 덮어쓴다


def prev_year_key(period: str) -> str | None:
    """기간키의 **앞 4자리 연도만 1 줄인다.** 포맷을 안 가리는 게 요점이다:
    '202607'→'202507' · '2026-06'→'2025-06' · '2026-Q2'→'2025-Q2' · '2026'→'2025'.
    분기·월·연차가 섞여 들어와도 같은 규칙으로 처리된다."""
    s = str(period)
    if len(s) < 4 or not s[:4].isdigit():
        return None
    return f"{int(s[:4]) - 1:04d}{s[4:]}"


def yoy(pairs: list[tuple[str, float]]) -> list[tuple[str, float]]:
    """레벨 → 전년비(%). **기간키로 1년 전을 직접 찾는다** — 인덱스로 세면
    결측이 섞였을 때 어긋난다. 1년 전 값이 없거나 0이면 그 기간은 버린다."""
    by = {str(p): v for p, v in pairs}
    out: list[tuple[str, float]] = []
    for p, v in pairs:
        prev = prev_year_key(p)
        base_v = by.get(prev) if prev else None
        if base_v in (None, 0):
            continue
        out.append((p, round((v / base_v - 1) * 100, 2)))
    return out


def norm_key(s: str) -> str:
    """항목 매칭용 정규화. 매칭은 **정확일치**로 한다 — 부분일치로 두면
    'EU'가 'WESTERN EUROPE'을, 'Copper ores'가 'Unwrought copper'를 끌어온다."""
    return re.sub(r"[^A-Z0-9]", "", html.unescape(str(s)).upper())


def clean_html(s: str) -> str:
    """태그·CDATA·엔티티를 걷어내고 공백을 하나로."""
    s = re.sub(r"<!\[CDATA\[|\]\]>", "", str(s))
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()
