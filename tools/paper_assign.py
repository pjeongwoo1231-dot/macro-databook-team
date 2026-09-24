# -*- coding: utf-8 -*-
"""논문 배정 — 누가 어느 논문을 맡았는지, 파일명까지 미리 확정한다.

**왜 표가 아니라 파일 하나씩인가.**
옵시디언 싱크는 양방향이라 팀원이 모두 같은 볼트를 쓴다. 배정 현황을 표 하나로 두면
그 표가 유일한 동시편집 지점이 된다 — 12명이 같은 줄 근처를 고치면 싱크 충돌이
바로 거기서 난다. 그래서 청구는 `03_MOC/논문배정/<파일명>.md` 로 **1건 1파일**이다.
서로 다른 논문을 맡는 한 두 사람이 같은 파일을 건드릴 일이 없고, 같은 논문을 집었다면
그건 막아야 할 충돌이므로 **파일 충돌로 드러나는 게 맞다.**

`03_MOC/논문 배정 큐.md` 는 그 청구들을 모아 **자동 생성**한다. 손으로 고치지 말 것 —
`sync` 를 돌리면 덮어쓴다.

    python tools/paper_assign.py claim --paper "제목" --year 1956 --author "Solow" --who 홍길동
    python tools/paper_assign.py start "1956 제목 (Solow)"
    python tools/paper_assign.py status
    python tools/paper_assign.py sync

볼트 경로는 `--vault` > `.env` 의 `OBSIDIAN_VAULT_PATH` > `~/MacroVault` 순으로 찾는다.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CLAIM_DIR = "03_MOC/논문배정"
QUEUE_NOTE = "03_MOC/논문 배정 큐.md"
PAPERS_DIR = "02_Papers"
TEMPLATE = "_System/Templates/T_Paper.md"

STATUSES = ("claimed", "drafting", "review", "done")
GENERATED = "<!-- 자동 생성 — paper_assign.py sync 가 덮어쓴다. 손으로 고치지 말 것 -->"

# 파일명에 못 쓰는 문자. 논문 제목에 콜론·물음표가 흔해서 실제로 걸린다.
BAD_CHARS = r'<>:"/\\|?*'


def die(msg: str, fix: str = "") -> None:
    print(f"[중단] {msg}", file=sys.stderr)
    if fix:
        print(f"       {fix}", file=sys.stderr)
    raise SystemExit(2)


# ── 볼트 찾기 ────────────────────────────────────────────────────────────
def find_vault(explicit: str | None) -> Path:
    if explicit:
        return Path(explicit).expanduser().resolve()
    env = os.environ.get("OBSIDIAN_VAULT_PATH", "").strip()
    if not env:
        p = ROOT / ".env"
        if p.exists():
            for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
                if line.startswith("OBSIDIAN_VAULT_PATH") and "=" in line:
                    env = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
    if env:
        return Path(env).expanduser().resolve()
    return (Path.home() / "MacroVault").resolve()


def require_vault(v: Path) -> Path:
    if not v.exists():
        die(f"볼트를 찾을 수 없습니다: {v}",
            "--vault 로 경로를 주거나 .env 의 OBSIDIAN_VAULT_PATH 를 채우세요.")
    return v


# ── 파일명 ───────────────────────────────────────────────────────────────
def note_name(year: str, paper: str, author: str) -> str:
    """볼트의 기존 관례를 그대로 따른다: `1956 제목 (저자).md`"""
    base = f"{year} {paper} ({author})".strip()
    for ch in BAD_CHARS:
        base = base.replace(ch, "-")
    return re.sub(r"\s+", " ", base).strip()


def norm(s: str) -> str:
    """중복 판정을 위한 정규화 — 공백·대소문자·문장부호를 지운다."""
    return re.sub(r"[^0-9a-z가-힣]", "", s.lower())


# ── 청구 파일 ────────────────────────────────────────────────────────────
def read_claim(p: Path) -> dict[str, str]:
    """frontmatter 만 읽는다. PyYAML 없이도 돌게 단순 파서를 쓴다."""
    out: dict[str, str] = {"_file": p.name, "_path": str(p)}
    txt = p.read_text(encoding="utf-8", errors="replace")
    if not txt.startswith("---"):
        return out
    body = txt.split("---", 2)
    if len(body) < 3:
        return out
    for line in body[1].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def all_claims(vault: Path) -> list[dict[str, str]]:
    d = vault / CLAIM_DIR
    if not d.exists():
        return []
    return sorted((read_claim(p) for p in d.glob("*.md")),
                  key=lambda c: (c.get("status", ""), c.get("claimed", ""), c.get("_file", "")))


def write_claim(vault: Path, name: str, data: dict[str, str]) -> Path:
    d = vault / CLAIM_DIR
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{name}.md"
    lines = ["---", "type: paper-claim"]
    for k in ("paper", "year", "author", "assignee", "note_filename",
              "claimed", "due", "status"):
        lines.append(f'{k}: "{data.get(k, "")}"')
    lines += [
        "---",
        "",
        f"# 배정 — {data.get('paper', '')}",
        "",
        f"- 담당: **{data.get('assignee', '')}**",
        f"- 노트: [[{data.get('note_filename', '')}]]",
        f"- 마감: {data.get('due', '') or '미정'}",
        "",
        "## 진행 메모",
        "",
        "<!-- 원문을 어디까지 봤는지, 막힌 곳이 어딘지 여기에. -->",
        "",
        "> [!warning] 확인한 것만 적는다",
        "> 저널·권호·DOI·공저자는 **실제로 조회한 것만** 채운다.",
        "> 확인 못 한 칸은 지어내지 말고 `미확인` 으로 비워 둔다.",
        "",
    ]
    p.write_text("\n".join(lines), encoding="utf-8")
    return p


# ── 명령 ─────────────────────────────────────────────────────────────────
def cmd_claim(a: argparse.Namespace) -> int:
    vault = require_vault(find_vault(a.vault))
    name = note_name(str(a.year), a.paper, a.author)

    existing = vault / PAPERS_DIR / f"{name}.md"
    if existing.exists():
        die(f"이미 노트가 있습니다: {PAPERS_DIR}/{name}.md",
            "같은 논문이 이미 정리돼 있습니다. 먼저 읽어보고, 보강이면 그 노트를 이어서 쓰세요.")

    claim_path = vault / CLAIM_DIR / f"{name}.md"
    if claim_path.exists():
        c = read_claim(claim_path)
        die(f"이미 배정된 논문입니다 — 담당 {c.get('assignee', '?')} ({c.get('claimed', '?')})",
            "다른 논문을 고르거나, 담당자와 이야기하세요.")

    key = norm(f"{a.year}{a.paper}")
    for c in all_claims(vault):
        if norm(f"{c.get('year','')}{c.get('paper','')}") == key:
            die(f"제목이 같은 청구가 있습니다: {c.get('_file')} — 담당 {c.get('assignee','?')}",
                "표기만 다른 같은 논문일 수 있습니다. 확인하세요.")

    today = dt.date.today().isoformat()
    due = a.due or (dt.date.today() + dt.timedelta(days=a.days)).isoformat()
    p = write_claim(vault, name, {
        "paper": a.paper, "year": str(a.year), "author": a.author,
        "assignee": a.who, "note_filename": name,
        "claimed": today, "due": due, "status": "claimed",
    })
    print(f"배정 완료 — {a.who}")
    print(f"  논문  : {a.paper} ({a.year}, {a.author})")
    print(f"  노트명: {name}.md   ← 이 이름은 선점됐습니다")
    print(f"  청구  : {p.relative_to(vault)}")
    print(f"  마감  : {due}")
    print(f"\n  다음: python tools/paper_assign.py start \"{name}\"")
    rebuild(vault)
    return 0


def cmd_start(a: argparse.Namespace) -> int:
    vault = require_vault(find_vault(a.vault))
    name = a.name[:-3] if a.name.endswith(".md") else a.name
    claim_path = vault / CLAIM_DIR / f"{name}.md"
    if not claim_path.exists():
        die(f"청구가 없습니다: {CLAIM_DIR}/{name}.md",
            "먼저 claim 으로 배정을 받으세요.")
    c = read_claim(claim_path)

    out = vault / PAPERS_DIR / f"{name}.md"
    if out.exists():
        die(f"노트가 이미 있습니다: {PAPERS_DIR}/{name}.md", "이어서 쓰면 됩니다.")

    tpl = vault / TEMPLATE
    if tpl.exists():
        body = tpl.read_text(encoding="utf-8", errors="replace")
        body = body.replace("{{논문 제목}}", c.get("paper", ""))
        body = body.replace("{{발표연도}}", c.get("year", ""))
        body = body.replace("{{저자(소속)}}", c.get("author", ""))
        body = body.replace("{{date:YYYY-MM-DD}}", dt.date.today().isoformat())
    else:
        body = "\n".join([
            "---", f'title: {c.get("paper","")}', "type: paper",
            'journal: 미확인', f'date: {c.get("year","")}',
            f'author: {c.get("author","")}',
            f"created: {dt.date.today().isoformat()}",
            "status: captured", "reliability: 미확인", "verified: 미대조",
            "related: []", "---", "", f'# {c.get("paper","")}', "",
        ])

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(body, encoding="utf-8")
    set_status(claim_path, "drafting")
    print(f"노트 생성 — {out.relative_to(vault)}")
    print(f"  담당: {c.get('assignee','')}  ·  상태: claimed → drafting")
    print("\n  ⚠ journal·DOI·공저자는 실제로 조회한 것만 채우세요. 확인 못 하면 `미확인`.")
    rebuild(vault)
    return 0


def set_status(claim_path: Path, status: str) -> None:
    txt = claim_path.read_text(encoding="utf-8", errors="replace")
    txt = re.sub(r'^status:.*$', f'status: "{status}"', txt, count=1, flags=re.M)
    claim_path.write_text(txt, encoding="utf-8")


def cmd_status(a: argparse.Namespace) -> int:
    vault = require_vault(find_vault(a.vault))
    claims = all_claims(vault)
    if not claims:
        print(f"배정된 논문이 없습니다. ({vault / CLAIM_DIR})")
        return 0
    today = dt.date.today().isoformat()
    print(f"배정 {len(claims)}건 — {vault}\n")
    print(f"  {'상태':<9} {'담당':<10} {'마감':<12} 논문")
    print("  " + "─" * 66)
    for c in claims:
        late = "  ⚠지연" if (c.get("due", "") and c.get("due", "") < today
                            and c.get("status") != "done") else ""
        print(f"  {c.get('status','?'):<9} {c.get('assignee','?'):<10} "
              f"{c.get('due','-'):<12} {c.get('paper','?')[:38]}{late}")
    n_done = sum(1 for c in claims if c.get("status") == "done")
    print(f"\n  완료 {n_done} / {len(claims)}")
    return 0


def cmd_set(a: argparse.Namespace) -> int:
    vault = require_vault(find_vault(a.vault))
    name = a.name[:-3] if a.name.endswith(".md") else a.name
    p = vault / CLAIM_DIR / f"{name}.md"
    if not p.exists():
        die(f"청구가 없습니다: {CLAIM_DIR}/{name}.md")
    if a.status not in STATUSES:
        die(f"모르는 상태: {a.status}", f"쓸 수 있는 값: {', '.join(STATUSES)}")
    set_status(p, a.status)
    print(f"{name} → {a.status}")
    rebuild(vault)
    return 0


def rebuild(vault: Path) -> Path:
    """청구 파일들을 모아 배정 큐 노트를 다시 만든다."""
    claims = all_claims(vault)
    today = dt.date.today().isoformat()
    lines = [
        "---", "type: moc", "title: 논문 배정 큐",
        f"updated: {today}", "tags: [type/moc, team/assignment]", "---", "",
        "# 논문 배정 큐", "", GENERATED, "",
        "> [!info] 한 논문에 한 사람, 파일명까지 미리 확정한다.",
        "> 청구는 `03_MOC/논문배정/` 에 1건 1파일로 들어간다 — 이 표는 그걸 모은 것이다.",
        "> 이 노트를 손으로 고치지 말 것. `paper_assign.py sync` 가 덮어쓴다.", "",
    ]
    if not claims:
        lines += ["아직 배정이 없습니다.", ""]
    else:
        lines += ["| 상태 | 담당 | 논문 | 연도 | 노트 | 배정일 | 마감 |",
                  "|---|---|---|---|---|---|---|"]
        for c in claims:
            late = " ⚠" if (c.get("due", "") and c.get("due", "") < today
                            and c.get("status") != "done") else ""
            lines.append(
                f"| {c.get('status','?')}{late} | {c.get('assignee','?')} "
                f"| {c.get('paper','?')} | {c.get('year','')} "
                f"| [[{c.get('note_filename','')}]] "
                f"| {c.get('claimed','')} | {c.get('due','')} |")
        n_done = sum(1 for c in claims if c.get("status") == "done")
        lines += ["", f"완료 **{n_done}** / 전체 **{len(claims)}**", ""]
    lines += [
        "## 규칙", "",
        "1. **claim 없이 노트를 만들지 않는다.** 파일명이 겹치면 싱크가 둘 중 하나를 덮는다.",
        "2. **확인한 것만 적는다.** 저널·권호·DOI·공저자는 조회한 것만. 못 하면 `미확인`.",
        "3. **배포본(`bootstrap.py`)과 싱크 볼트를 같이 쓰지 않는다.** 배포본은 매번 볼트를 지운다.",
        "",
    ]
    out = vault / QUEUE_NOTE
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def cmd_sync(a: argparse.Namespace) -> int:
    vault = require_vault(find_vault(a.vault))
    p = rebuild(vault)
    print(f"배정 큐 갱신 — {p.relative_to(vault)} ({len(all_claims(vault))}건)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="논문 배정 (한 논문 한 사람)")
    ap.add_argument("--vault", help="볼트 경로 (기본: .env 의 OBSIDIAN_VAULT_PATH)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("claim", help="논문을 맡는다 (파일명 선점)")
    c.add_argument("--paper", required=True, help="논문 제목")
    c.add_argument("--year", required=True, help="발표 연도")
    c.add_argument("--author", required=True, help="저자 (성만 써도 된다)")
    c.add_argument("--who", required=True, help="담당자 이름")
    c.add_argument("--due", help="마감일 YYYY-MM-DD")
    c.add_argument("--days", type=int, default=7, help="마감까지 일수 (기본 7)")
    c.set_defaults(func=cmd_claim)

    s = sub.add_parser("start", help="템플릿으로 논문 노트를 만든다")
    s.add_argument("name", help="노트명 (claim 이 알려준 이름)")
    s.set_defaults(func=cmd_start)

    t = sub.add_parser("set", help="상태를 바꾼다")
    t.add_argument("name")
    t.add_argument("status", help=" | ".join(STATUSES))
    t.set_defaults(func=cmd_set)

    sub.add_parser("status", help="현황").set_defaults(func=cmd_status)
    sub.add_parser("sync", help="배정 큐 노트 재생성").set_defaults(func=cmd_sync)

    a = ap.parse_args()
    return a.func(a)


if __name__ == "__main__":
    raise SystemExit(main())
