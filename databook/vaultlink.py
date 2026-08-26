"""지표 → Obsidian 지표 노드 매칭.

이 모듈은 **볼트가 있을 때만** 동작한다. `OBSIDIAN_VAULT_PATH/01_Indicators/`를 읽어
노드 stem과 aliases를 모으고, 지표 이름에 그 토큰이 들어 있으면 노드로 잇는다.
볼트나 폴더가 없으면 빈 매핑을 돌려주고 렌더는 아무것도 바뀌지 않는다 —
이 도구를 볼트 없이 쓰는 사용자에게 영향이 없어야 하므로 노드 이름을 코드에 넣지 않는다.

지표별 수동 지정은 indicators.yaml 의 선택 필드로 한다.
    vault_node: 기준금리     # 이 노드로 강제
    vault_node: "-"          # 자동 매칭 끄기 (오매칭 차단)
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

ALIAS_RE = re.compile(r"^aliases:\s*\[(.*?)\]\s*$", re.M)
MIN_TOKEN = 2


def load_nodes(vault: str | Path) -> list[tuple[str, str]]:
    """(토큰, 노드명) 목록. 긴 토큰이 먼저 오도록 정렬 — 최장일치 우선."""
    folder = Path(vault) / "01_Indicators"
    if not folder.is_dir():
        return []
    out: list[tuple[str, str]] = []
    for p in sorted(folder.glob("*.md")):
        toks = {p.stem, re.sub(r"\s*\(.*?\)", "", p.stem).strip()}
        m = ALIAS_RE.search(p.read_text(encoding="utf-8", errors="replace"))
        if m:
            toks |= {a.strip().strip("\"'") for a in m.group(1).split(",")}
        out += [(t, p.stem) for t in toks if len(t) >= MIN_TOKEN]
    out.sort(key=lambda x: -len(x[0]))
    return out


def match_one(name: str, nodes: list[tuple[str, str]]) -> str | None:
    low = name.lower()
    for tok, node in nodes:
        if tok.lower() in low:
            return node
    return None


def map_results(results: list[dict[str, Any]], nodes: list[tuple[str, str]]) -> dict[str, list[dict[str, Any]]]:
    """노드 → 그 노드로 매칭된 지표 행들. `vault_node` 수동 지정이 자동 매칭을 이긴다."""
    by_node: dict[str, list[dict[str, Any]]] = {}
    if not nodes:
        return by_node
    valid = {n for _, n in nodes}
    for r in results:
        override = str(r.get("vault_node") or "").strip()
        if override == "-":
            continue
        node = override if override in valid else (None if override else match_one(r["name"], nodes))
        if node:
            by_node.setdefault(node, []).append(r)
    return by_node
