"""사람이 아니라 **에이전트가 처리할 작업 목록**을 뽑는다.

볼트 원칙이 "사람이 먼저 해석하는 구조 금지 · AI 해석 선제시"인데, 정작
수집기는 손이 필요한 자리를 알려주지 않았다. 어디를 채워야 하는지 코드가 모르면
AI에게 넘길 수도 없다. 이 명령이 그 목록을 만든다.

두 종류가 나온다.

1. **manual 슬롯** — 자동 경로가 없어 비어 있는 지표.
   (예: 일본 임금 — e-Stat이 2021-10에 멈췄고 춘투는 애초에 統計가 아니라 連合 집계)
   note에 적힌 출처 URL과 "채울 값"을 함께 뽑아준다.

2. **STALE 계열** — 원본 기관이 갱신을 멈춰 값이 낡은 지표.
   (예: 중국 NBS 미러는 약 6개월 지연)
   값 자체는 맞지만 **"최신"이라고 인용하면 틀린다.** 원문에서 최신치를 확인해야 한다.

⚠ **트리거 판정은 여기 없다.** 그건 이미 `derived.py`가 코드로 한다(17종, 임계값 포함).
   사람도 AI도 손댈 필요가 없는 자리다.

    python -m databook todo            # 전체
    python -m databook todo --kind manual
    python -m databook todo --json     # 에이전트가 파싱하기 좋게
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from .core import OUTPUT_DIR, all_indicators, load_registry
from .staleness import annotate

# note에서 출처 URL을 뽑는다 — manual 슬롯은 "어디서 채우나"가 핵심 정보다
_URL = re.compile(r"https?://[^\s)>'\"]+")
# "채울 값: A · B · C" 형태를 note에 적어두는 관례
_FILL = re.compile(r"채울 값[:：]\s*([^.⚠]+)")


def _latest_snapshot() -> list[dict[str, Any]]:
    snaps = sorted(OUTPUT_DIR.glob("snapshot_*.json"), reverse=True)
    if not snaps:
        return []
    d = json.loads(snaps[0].read_text(encoding="utf-8"))
    if isinstance(d, dict):
        for v in d.values():
            if isinstance(v, list) and v and isinstance(v[0], dict) and "name" in v[0]:
                return v
        return []
    return d


def collect(kind: str = "all") -> dict[str, list[dict[str, Any]]]:
    """(manual, stale) 작업 목록. 스냅샷이 없으면 manual만 yaml에서 뽑는다."""
    reg = load_registry()
    inds = all_indicators(reg)
    by_name = {i["name"]: i for i in inds}

    manual: list[dict[str, Any]] = []
    for i in inds:
        if i.get("method") != "manual":
            continue
        note = re.sub(r"\s+", " ", str(i.get("note") or ""))
        manual.append({
            "name": i["name"],
            "team": i.get("team", ""),
            "tier": i.get("tier"),
            "sources": _URL.findall(note)[:4],
            "fill": (_FILL.search(note).group(1).strip()[:160] if _FILL.search(note) else ""),
            "note": note[:300],
        })

    stale: list[dict[str, Any]] = []
    results = _latest_snapshot()
    if results:
        annotate(results)
        for r in results:
            if not r.get("stale"):
                continue
            src = by_name.get(r["name"], {})
            note = re.sub(r"\s+", " ", str(src.get("note") or r.get("note") or ""))
            obs = r.get("observations") or [{}]
            stale.append({
                "name": r["name"],
                "team": r.get("team", ""),
                "latest": obs[0].get("date", "?"),
                "age_days": r.get("age_days"),
                "gap_days": r.get("gap_days"),
                "source_url": r.get("source_url", "").split()[0] if r.get("source_url") else "",
                "sources": _URL.findall(note)[:3],
                "note": note[:300],
            })
        stale.sort(key=lambda x: -(x["age_days"] or 0))

    out = {}
    if kind in ("all", "manual"):
        out["manual"] = manual
    if kind in ("all", "stale"):
        out["stale"] = stale
    return out


def cmd_todo(kind: str, as_json: bool, limit: int) -> int:
    data = collect(kind)
    if as_json:
        print(json.dumps(data, ensure_ascii=False, indent=1))
        return 0

    if not _latest_snapshot() and kind in ("all", "stale"):
        print("⚠ 스냅샷이 없어 STALE 판정을 못 합니다 — 먼저 `python -m databook run`\n")

    m = data.get("manual", [])
    if m:
        print(f"# 수동 입력 슬롯 {len(m)}건 — 자동 경로가 없어 비어 있는 자리\n")
        for x in m:
            print(f"## {x['name']}  (tier {x['tier']} · {x['team']})")
            if x["fill"]:
                print(f"   채울 값: {x['fill']}")
            for u in x["sources"]:
                print(f"   출처: {u}")
            if not x["sources"]:
                print(f"   ⚠ note에 출처 URL이 없다 — 먼저 출처를 찾아 note에 적을 것")
            print()

    s = data.get("stale", [])
    if s:
        print(f"# 갱신 정지 의심 {len(s)}건 — 값은 맞지만 낡았다. 원문에서 최신치 확인 필요\n")
        for x in s[:limit]:
            print(f"## {x['name']}  ({x['team']})")
            print(f"   최신 {x['latest']} · {x['age_days']}일 전 · 정상 주기 {x['gap_days']}일")
            if x["source_url"]:
                print(f"   수집 URL: {x['source_url'][:110]}")
            for u in x["sources"][:2]:
                print(f"   note 출처: {u[:110]}")
            print()
        if len(s) > limit:
            print(f"  … 외 {len(s)-limit}건 (--limit 으로 더 보기)\n")

    if not m and not s:
        print("처리할 자리가 없습니다.")
        return 0

    print("─" * 68)
    print("에이전트가 처리하는 방법")
    print("  manual : 출처 URL을 열어 '채울 값'의 수치를 찾고, indicators.yaml의 해당")
    print("           지표 note에 값과 **확인일·출처**를 적는다. 추측으로 채우지 않는다.")
    print("  stale  : 원문 기관 발표에서 최신치를 확인한다. 원본이 정말 멈춘 것이면")
    print("           note에 '기준월 ○○○○-○○, ○○개월 지연'을 갱신하고, 다시 나오기")
    print("           시작했으면 수집 경로를 고친다.")
    return 0
