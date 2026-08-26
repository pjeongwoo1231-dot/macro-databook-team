"""출력 렌더 — Obsidian 네이티브 마크다운(frontmatter·콜아웃·위키링크) + 스냅샷 JSON.
해석 문구를 생성하지 않는다 (숫자·기준일·출처만). OBSIDIAN_VAULT_PATH가 설정되면 vault에도 동일 파일을 쓴다."""
from __future__ import annotations

import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .core import OUTPUT_DIR, TEAM_META
from .vaultlink import load_nodes, map_results

STATUS_LABEL = {"manual": "수동 입력", "stub": "미구현", "fail": "수집 실패"}

# 지표 노드를 소환하는 허브. 매 실행마다 덮어쓴다.
# 일별 노트가 각자 노드를 소환하면 1년 뒤 지표 노드의 백링크가 데이터 파일 수백 개로 덮인다.
# 소환은 이 노트 하나만 하고, 일별 노트는 여기로 연결만 한다 — 노드당 백링크 1개.
HUB_NAME = "DataBook 지표 소환"


def _fmt(v: float) -> str:
    if isinstance(v, str):
        return v
    a = abs(v)
    if a >= 1_000_000_000_000:
        return f"{v / 1e12:,.2f}조 달러" if a >= 1e12 else f"{v:,.0f}"
    if a >= 10_000:
        return f"{v:,.0f}"
    if a >= 100:
        return f"{v:,.1f}"
    if a and a < 0.01:
        # 소수 3자리 고정이면 구리/금 비율 같은 값이 0.001로 뭉개져 변화를 볼 수 없다.
        return f"{v:.4g}"
    return f"{v:,.3f}".rstrip("0").rstrip(".")


def _esc(s: str) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ")


def _obs_cell(r: dict[str, Any]) -> tuple[str, str]:
    """(최신값 셀, 직전 추이 셀) — label별로 묶는다."""
    by_label: dict[str, list[dict[str, Any]]] = {}
    for o in r["observations"]:
        by_label.setdefault(o.get("label") or "", []).append(o)
    latest_lines, trend_lines = [], []
    for label, obs in by_label.items():
        head = obs[0]
        prefix = f"{_esc(label)}: " if label and len(by_label) > 1 else ""
        latest_lines.append(f"{prefix}**{_fmt(head['value'])}** ({head['date']})")
        if len(obs) > 1:
            trend = " ← ".join(_fmt(o["value"]) for o in obs[1:5])
            trend_lines.append(f"{prefix}{trend}")
        if len(by_label) == 1 and label:
            latest_lines[-1] += f" — {_esc(label)}"
    return "<br>".join(latest_lines) or "—", "<br>".join(trend_lines) or "—"


def _team_note(team_key: str, team_rows: list[dict[str, Any]], run_ts: str, date_str: str) -> str:
    letter, title, _ = TEAM_META[team_key]
    ok = sum(1 for r in team_rows if r["status"] == "ok")
    lines = [
        "---",
        f"date: {date_str}",
        "type: databook",
        f"team: {letter}",
        f"team_name: {title}",
        f"collected_utc: {run_ts}",
        f"indicators_ok: {ok}",
        f"indicators_total: {len(team_rows)}",
        f"indicators_stale: {sum(1 for r in team_rows if r.get('stale'))}",
        "tags: [macro/databook]",
        "---",
        "",
        f"# Data Book — {letter}팀 {title}",
        "",
        f"> [!info] 자동 수집 {ok}/{len(team_rows)} · {run_ts} (UTC)",
        "> 해석 없음 — 숫자·기준일·출처만. 판단은 Interpretation 노트에서. 인덱스: [[DataBook_{0}]]".format(date_str),
        f"> 지표 노드로 가려면 [[{HUB_NAME}]] (문헌·제텔과 만나는 지점)",
        "",
        "| 지표 | 티어 | 최신값 (기준일) | 직전 추이 | 상태 / 출처 |",
        "|---|---|---|---|---|",
    ]
    for r in sorted(team_rows, key=lambda x: (x["tier"], x["status"] != "ok")):
        if r["status"] == "ok":
            latest, trend = _obs_cell(r)
            # 단위를 값 옆에 붙인다. 침체확률 0.6을 60%로 읽는 사고가 여기서 막힌다.
            meta_bits = [b for b in (r.get("unit"), r.get("seasonal_adjustment")) if b]
            if meta_bits:
                latest += f"<br><sub>{_esc(' · '.join(meta_bits))}</sub>"
            src = f"[출처]({r['source_url'].split()[0]})" if r["source_url"].startswith("http") else _esc(r["source_url"]) or "—"
            status = src + (f" ⚠ {_esc(r['error'])}" if r.get("error") else "")
            if r.get("stale"):
                status += f" ⛔ 갱신정지 의심 ({r['age_days']}일 전 관측, 주기 {r['gap_days']}일)"
        else:
            latest, trend = "—", "—"
            detail = r.get("error") or r.get("note") or ""
            status = f"{STATUS_LABEL.get(r['status'], r['status'])}" + (f" — {_esc(detail)}" if detail else "")
        lines.append(f"| {_esc(r['name'])} | {r['tier']} | {latest} | {trend} | {status} |")
    manual = [r for r in team_rows if r["status"] == "manual"]
    if manual:
        lines += ["", "## 수동 입력 슬롯 (담당자가 채울 것)", ""]
        for r in manual:
            note = f" — {_esc(r.get('note') or '')}" if r.get("note") else ""
            lines.append(f"- [ ] **{_esc(r['name'])}**{note}")
    lines.append("")
    return "\n".join(lines)


def _index_note(results: list[dict[str, Any]], run_ts: str, date_str: str) -> str:
    ok = sum(1 for r in results if r["status"] == "ok")
    manual = sum(1 for r in results if r["status"] == "manual")
    lines = [
        "---",
        f"date: {date_str}",
        "type: databook-index",
        f"collected_utc: {run_ts}",
        "tags: [macro/databook]",
        "---",
        "",
        f"# 매크로 Data Book — {date_str}",
        "",
        f"> [!summary] 자동 수집 {ok} · 수동 슬롯 {manual} · 전체 {len(results)} — {run_ts} (UTC)",
        *( [] if not [r for r in results if r.get("stale")] else
           ["", f"> [!warning] 갱신정지 의심 {len([r for r in results if r.get('stale')])}건 — 최신 관측이 관측주기 대비 오래됨. 인용 전 원천 확인"]
           + [f"> - {_esc(r['name'])}: 최신 {r['observations'][0]['date']} ({r['age_days']}일 전)"
              for r in sorted([r for r in results if r.get("stale")], key=lambda x: -x["age_days"])[:12]] ),
        "",
        "## 팀별 Data Book",
        "",
    ]
    for team_key, (letter, title, _) in TEAM_META.items():
        team_rows = [r for r in results if r["team"] == team_key]
        n_ok = sum(1 for r in team_rows if r["status"] == "ok")
        lines.append(f"- [[DataBook_{letter}_{date_str}|{letter}팀 {title}]] — 수집 {n_ok}/{len(team_rows)}")
    lines += ["", "## 1티어 하이라이트 (해석 필수 지표)", "",
              "| 팀 | 지표 | 최신값 (기준일) |", "|---|---|---|"]
    for team_key, (letter, _, _) in TEAM_META.items():
        for r in results:
            if r["team"] != team_key or r["tier"] != 1 or r["status"] != "ok":
                continue
            latest, _trend = _obs_cell(r)
            lines.append(f"| {letter} | {_esc(r['name'])} | {latest} |")
    lines += [
        "",
        f"## 지표 노드로 나가기\n\n[[{HUB_NAME}]] — 이 Data Book의 수치가 볼트의 지표 노드에서\n"
        "문헌·제텔과 만난다. 소환은 그 허브 하나만 한다(일별 노트가 각자 소환하면 백링크가 덮인다).",
        "",
        "> [!note] 이 노트는 macro-databook이 자동 생성. 스냅샷 JSON: `snapshot_" + date_str + ".json`",
        "> 출처 없는 수치는 발표에 쓸 수 없다 — 모든 인용은 위 표의 출처 링크 기준.",
        "",
    ]
    return "\n".join(lines)


def _hub_val(r: dict[str, Any], limit: int = 90) -> str:
    """허브 표는 요약이다. 뉴스형 지표는 값 셀이 RSS 링크 덩어리가 되므로 줄인다.
    전체 값과 출처는 일별 Data Book 표에 있다."""
    cell = _obs_cell(r)[0]
    cell = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", cell)   # 링크 → 텍스트
    cell = cell.replace("<br>", " · ")
    return cell if len(cell) <= limit else cell[:limit].rstrip() + "…"


def _hub_note(results: list[dict[str, Any]], run_ts: str, date_str: str,
              by_node: dict[str, list[dict[str, Any]]]) -> str:
    """지표 노드를 소환하는 유일한 노트. 매 실행 덮어쓴다."""
    lines = [
        "---",
        "title: DataBook 지표 소환",
        "type: index",
        f"date: {date_str}",
        f"collected_utc: {run_ts}",
        "status: working",
        "verification: n-a",
        "reliability: primary",
        'verified: "○ 기관 원자료 자동 수집. 각 수치의 출처 링크는 일별 Data Book 표에 있다"',
        "tags: [macro/databook, type/index]",
        f'related: ["[[DataBook_{date_str}]]", "[[지표 MOC]]"]',
        "---",
        "",
        "# DataBook 지표 소환",
        "",
        f"> [!info] {date_str} 기준 · {run_ts} (UTC) · 매 실행 덮어씀",
        "> 볼트 규칙대로 **연결은 소환하는 쪽에서 만들어진다.** 이 노트가 Data Book을 대표해",
        "> 지표 노드를 부르고, 노드의 Backlinks에서 **최신 수치와 문헌·제텔이 만난다.**",
        "> 일별 Data Book은 여기로 연결만 한다 — 각자 소환하면 노드 백링크가 데이터로 덮인다.",
        "",
        f"최신 Data Book: [[DataBook_{date_str}]]",
        "",
    ]
    if not by_node:
        lines += ["", "> [!warning] 지표 노드를 찾지 못했다.",
                  "> `OBSIDIAN_VAULT_PATH/01_Indicators/`가 없거나 이름이 매칭되지 않았다.", ""]
        return "\n".join(lines)

    lines += [f"소환한 노드 **{len(by_node)}개** · 연결된 지표 "
              f"**{sum(len(v) for v in by_node.values())}개**", "",
              "| 지표 노드 | 최신값 | 연결된 수집 지표 |", "|---|---|---|"]
    for node in sorted(by_node, key=lambda n: (-len(by_node[n]), n)):
        rows = by_node[node]
        tier1 = [r for r in rows if r["tier"] == 1 and r["status"] == "ok"] or \
                [r for r in rows if r["status"] == "ok"]
        val = _hub_val(tier1[0]) if tier1 else "—"
        names = ", ".join(_esc(r["name"]) for r in rows[:4]) + (" 외" if len(rows) > 4 else "")
        lines.append(f"| [[{node}]] | {val} | {names} |")

    unmapped = [r for r in results
                if r["status"] == "ok" and not any(r in v for v in by_node.values())]
    lines += ["", "## 대응 노드가 없는 지표", "",
              f"수집은 되지만 볼트에 노드가 없는 지표 **{len(unmapped)}개**. "
              "볼트 규칙상 아무도 부르지 않는 노드는 만들지 않으므로, "
              "**논문·제텔이 실제로 이 개념을 쓰기 시작할 때** 노드를 만든다.", ""]
    for r in unmapped[:40]:
        lines.append(f"- {_esc(r['name'])}")
    if len(unmapped) > 40:
        lines.append(f"- … 외 {len(unmapped) - 40}개")
    lines.append("")
    return "\n".join(lines)


def render_markdown(results: list[dict[str, Any]], run_ts: str, env: dict[str, str] | None = None) -> list[Path]:
    date_str = run_ts[:10]
    written: list[Path] = []
    # (prefix가 붙기 전의) 상대경로 → 내용. prefix는 대상별로 다르다 —
    # 로컬 output/은 "Macro/"(이 프로젝트 자체 관례), 실제 Obsidian vault는 "04_DataBook/"(vault 관례)를 쓴다.
    files: dict[str, str] = {}
    for team_key, (letter, _, folder) in TEAM_META.items():
        team_rows = [r for r in results if r["team"] == team_key]
        files[f"{folder}/DataBook_{letter}_{date_str}.md"] = _team_note(team_key, team_rows, run_ts, date_str)
    files[f"DataBook_{date_str}.md"] = _index_note(results, run_ts, date_str)

    targets: list[tuple[Path, str]] = [(OUTPUT_DIR, "Macro")]
    vault = (env or {}).get("OBSIDIAN_VAULT_PATH", "").strip().strip('"')
    if vault:
        targets.append((Path(vault), "04_DataBook"))
        # 허브는 볼트의 노드 이름에 의존하므로 볼트가 있을 때만 만든다.
        by_node = map_results(results, load_nodes(vault))
        hub = _hub_note(results, run_ts, date_str, by_node)
        hub_path = Path(vault) / "04_DataBook" / f"{HUB_NAME}.md"
        hub_path.parent.mkdir(parents=True, exist_ok=True)
        hub_path.write_text(hub, encoding="utf-8")
        written.append(hub_path)
    for root, prefix in targets:
        for rel, content in files.items():
            path = root / prefix / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            written.append(path)
    return written


def render_snapshot(results: list[dict[str, Any]], run_ts: str, env: dict[str, str] | None = None) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / f"snapshot_{run_ts[:10]}.json"
    payload = {"generated_at_utc": run_ts, "indicator_count": len(results), "indicators": results}
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    vault = (env or {}).get("OBSIDIAN_VAULT_PATH", "").strip().strip('"')
    if vault:
        dest = Path(vault) / "04_DataBook" / "snapshots" / path.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, dest)
    return path


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
