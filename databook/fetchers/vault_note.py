"""볼트의 `11_AutoIndicators/` 노트를 읽어 팀 Data Book에 싣는다 (재수집 없음).

**왜 이게 있나** — 볼트에는 수집기가 둘이다.

  * `databook/daily.py`  → `indicators.yaml` 을 읽고 **팀별 DataKit**(`04_DataBook/1~4`)을 만든다
  * `databook/intel.py`  → 자체 소스(portwatch·comtrade·eia_v2·sdmx·socrata·xlsx)를 받아
                            **`11_AutoIndicators/<id>.md`** 24개를 만든다

둘이 분리돼 있어서 `intel.py` 산출물이 **팀 DataKit에 한 번도 실린 적이 없었다.**
학회원은 `04_DataBook/1~4`만 보고 공부하므로, 매일 갱신되는 24개가 통째로 사각지대였다
(2026-09-09 확인. 그 전까지 볼트 어디서도 링크조차 되지 않는 고아였다).

**설계 판단** — 같은 값을 `daily.py`가 다시 받아오게 하지 않는다. portwatch·comtrade 등은
`databook/fetchers/` 에 대응 fetcher가 없어 포팅 비용이 크고, 같은 API를 하루 두 번 때리는 것도
이유가 없다. 대신 **이미 디스크에 있는 노트를 읽는다.** 그래서 이 fetcher는 네트워크를 쓰지 않는다.

**따라서 순서 의존이 있다**: `intel.py` 가 먼저 돌아야 값이 최신이다.
안 돌았으면 노트의 `retrieved` 가 오래됐을 뿐 실패하지는 않는다 — `max_age_days` 로 걸러진다.

yaml 사용법:

    - name: 호르무즈 통항 (일별)
      tier: 1
      method: api
      source: vault_note
      series_id: hormuz_transits      # 11_AutoIndicators/<series_id>.md
      max_age_days: 14
"""
from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

from .base import result

FOLDER = "11_AutoIndicators"


def _vault_dir(env: dict[str, str]) -> Path:
    p = env.get("OBSIDIAN_VAULT_PATH") or os.environ.get("OBSIDIAN_VAULT_PATH") or ""
    return Path(p) / FOLDER


def _frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    out: dict[str, str] = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return out


def _to_date(period: str) -> str:
    """intel 계열의 period 표기가 제각각이라 YYYY-MM-DD 로 맞춘다.

    일별 `2026-09-01` · 월별 `2026-06` · World Bank `2026M08` · 연간 `2024` 가 섞여 있다.
    월·연 단위는 **해당 기간의 첫날**로 내린다(끝날로 올리면 아직 오지 않은 날짜가 생긴다).
    """
    p = (period or "").strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", p):
        return p
    m = re.fullmatch(r"(\d{4})M(\d{2})", p)          # 2026M08
    if m:
        return f"{m.group(1)}-{m.group(2)}-01"
    if re.fullmatch(r"\d{4}-\d{2}", p):              # 2026-06
        return p + "-01"
    if re.fullmatch(r"\d{4}", p):                    # 2024
        return p + "-01-01"
    return p


def _num(v: str) -> Any:
    try:
        f = float(str(v).replace(",", ""))
        return int(f) if f.is_integer() else f
    except (TypeError, ValueError):
        return v


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    ids = ind.get("series_id")
    if isinstance(ids, str):
        ids = [ids]
    if not ids:
        return result(ind, "fail", error="vault_note: series_id 없음")

    base = _vault_dir(env)
    if not base.is_dir():
        return result(ind, "fail",
                      error=f"vault_note: {FOLDER} 폴더를 못 찾음 (OBSIDIAN_VAULT_PATH 확인)")

    obs: list[dict[str, Any]] = []
    unit = ""
    src_url = ""
    missing: list[str] = []
    unverified: list[str] = []

    for sid in ids:
        p = base / f"{sid}.md"
        if not p.is_file():
            missing.append(sid)
            continue
        fm = _frontmatter(p.read_text(encoding="utf-8", errors="ignore"))
        val = fm.get("value", "")
        if val in ("", "null", "None"):
            missing.append(sid)
            continue
        label = fm.get("label") or sid
        obs.append({"date": _to_date(fm.get("period", "")), "value": _num(val), "label": label})
        unit = unit or (fm.get("unit") or "")
        src_url = src_url or fm.get("source_url", "")
        if (fm.get("verified_source") or "").lower() not in ("true", "yes", "1"):
            unverified.append(sid)

    if not obs:
        return result(ind, "fail",
                      error="vault_note: 값을 못 읽음 — " + ", ".join(missing or ids)
                            + " (intel.py 를 먼저 돌렸는지 확인)")

    notes = [ind.get("note", "")] if ind.get("note") else []
    notes.append(f"`{FOLDER}/` 노트를 읽어 실었다 — 재수집 아님. 값 갱신은 `intel.py` 담당.")
    if missing:
        notes.append(f"⚠ 못 읽은 계열: {', '.join(missing)}")
    if unverified:
        notes.append(f"⚠ `verified_source: false`: {', '.join(unverified)}")

    return result(ind, "ok", observations=obs, unit=unit,
                  source_url=src_url or f"obsidian://{FOLDER}",
                  note=" / ".join(n for n in notes if n))
