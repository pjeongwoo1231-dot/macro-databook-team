"""공통 HTTP 헬퍼 + 결과 규격."""
from __future__ import annotations

import json
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
