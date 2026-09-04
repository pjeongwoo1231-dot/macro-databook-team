"""조회 도구 — 큰 산출물에서 필요한 부분만 뽑아 본다.

**왜 필요한가** — 산출물이 컨텍스트에 안 들어간다(2026-08-28 실측):

| 파일 | 대략 토큰 |
|---|---|
| 팀별 Data Book 1개 | 11,000 ~ 20,800 |
| 일별 인덱스 | 10,000 |
| 스냅샷 JSON 전체 | 255,000 |
| 뉴스 다이제스트 | **668,000** |

지표 하나를 확인하려고 20,000토큰을 읽는 건 낭비고, 뉴스는 아예 불가능하다.
여기 있는 세 명령이 그걸 수백 토큰으로 줄인다.

    python -m databook show 중국 원자재      # 이름으로 지표 찾아 값만
    python -m databook diff                  # 어제 대비 값이 바뀐 지표만
    python -m databook news --q 중국 --new   # 어제 없던 새 기사만

⚠ **뉴스는 "골라주지" 않는다.** news.py의 원칙(취사선택 금지 — 편향 주입이므로)을
지키려면 필터 조건을 **사람이 준다.** 이 도구는 검색일 뿐 요약·선별이 아니다.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from .core import OUTPUT_DIR, load_env


# ─────────────────────────── 공통 ───────────────────────────

def _snapshots() -> list[Path]:
    """최신순 스냅샷 목록.

    로컬 `output/`을 먼저 보고, **비어 있으면 볼트의 `04_DataBook/snapshots/`** 로 간다.

    왜 폴백이 필요한가 — 팀원은 수집을 직접 돌리지 않는다. 저장소만 clone하고
    데이터는 **Obsidian Sync로 볼트에서 받는다.** 그러면 `output/`은 비어 있어
    `diff`·`weekly`가 "스냅샷이 없다"로 끝난다(실제로 갓 클론한 환경에서 그랬다).
    볼트에는 같은 형식의 스냅샷이 들어 있으므로 그걸 쓰면 된다.
    """
    local = sorted(OUTPUT_DIR.glob("snapshot_*.json"), reverse=True)
    if local:
        return local
    v = (load_env().get("OBSIDIAN_VAULT_PATH") or "").strip().strip('"')
    if v:
        vs = Path(v) / "04_DataBook" / "snapshots"
        if vs.is_dir():
            return sorted(vs.glob("snapshot_*.json"), reverse=True)
    return []


def _no_snapshot_hint() -> str:
    """스냅샷이 없을 때 **왜 없는지**를 짚어 준다.

    ⚠ 2026-09-02부로 배포가 **주 1회 ZIP(GitHub Releases)**으로 바뀌었다. 그 전의
    옵시디언 싱크 안내("'기타 모든 파일 형식'을 켜세요")는 **이제 틀린 처방**이다 —
    켤 싱크가 없다. 지금 스냅샷이 없는 이유는 셋 중 하나다:
      ① .env에 OBSIDIAN_VAULT_PATH가 없다  ② ZIP에 snapshots/가 빠졌다  ③ 수집을 안 돌렸다
    """
    v = (load_env().get("OBSIDIAN_VAULT_PATH") or "").strip().strip('"')
    if not v:
        return ("볼트 경로가 없습니다 — 배포본을 받아 쓰는 사람은 `.env`에\n"
                "  OBSIDIAN_VAULT_PATH=<압축 푼 볼트 폴더>\n"
                "  를 적어야 합니다. (직접 수집한다면 `python -m databook run`)")
    if (Path(v) / "04_DataBook").is_dir():
        return ("볼트는 있는데 `04_DataBook/snapshots/*.json`이 없습니다 — "
                "스냅샷이 빠진 배포본입니다.\n"
                "  Releases에서 **최신 ZIP을 다시 받아** 통째로 덮어쓰세요\n"
                "  (github.com/pjeongwoo1231-dot/macro-databook-team/releases/latest).\n"
                "  (직접 수집한다면 `python -m databook run`)")
    return (f"OBSIDIAN_VAULT_PATH가 볼트를 가리키지 않습니다({v}) — "
            "`04_DataBook` 폴더가 있는 상위 폴더를 지정하세요.")


def _load(path: Path) -> list[dict[str, Any]]:
    d = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(d, dict):
        for v in d.values():
            if isinstance(v, list) and v and isinstance(v[0], dict) and "name" in v[0]:
                return v
        return []
    return d


def _match(ind: dict[str, Any], terms: list[str]) -> bool:
    """지표명·라벨·소스 어디든 모든 검색어가 들어 있으면 매치."""
    hay = (ind.get("name", "") + " " + ind.get("source", "") + " "
           + " ".join(str(o.get("label", "")) for o in ind.get("observations", []))).lower()
    return all(t.lower() in hay for t in terms)


def _fmt(v: Any) -> str:
    if isinstance(v, (int, float)):
        return f"{v:,.4g}"
    s = str(v)
    return s[:70] + "…" if len(s) > 70 else s


# ─────────────────────────── show ───────────────────────────

def cmd_show(terms: list[str], points: int) -> int:
    snaps = _snapshots()
    if not snaps:
        print(_no_snapshot_hint())
        return 1
    inds = _load(snaps[0])
    hits = [i for i in inds if _match(i, terms)]
    if not hits:
        print(f"'{' '.join(terms)}' 에 맞는 지표가 없습니다. (전체 {len(inds)}개)")
        return 1
    print(f"# {snaps[0].stem} — '{' '.join(terms)}' {len(hits)}건\n")
    for i in hits:
        head = f"## {i['name']}  [{i.get('status')}]"
        if i.get("error"):
            head += f"  ⚠ {i['error'][:60]}"
        print(head)
        by: dict[str, list] = {}
        for o in i.get("observations", []):
            by.setdefault(o.get("label") or "", []).append(o)
        for label, obs in by.items():
            vals = " ← ".join(f"{_fmt(o['value'])}({o['date']})" for o in obs[:points])
            print(f"   {label or '(라벨 없음)'}: {vals}")
        if i.get("note"):
            n = re.sub(r"\s+", " ", str(i["note"]))
            print(f"   ⓘ {n[:150]}{'…' if len(n) > 150 else ''}")
        print()
    return 0


# ─────────────────────────── diff ───────────────────────────

def _pick(snaps: list[Path], on_or_before: str) -> int | None:
    """그 날짜 **이하**의 가장 최근 스냅샷 인덱스. 그날 수집을 걸렀어도 직전 것으로 잡힌다."""
    for k, sp in enumerate(snaps):
        if sp.stem[len("snapshot_"):] <= on_or_before:
            return k
    return None


def _compare(cur: list[dict[str, Any]], prev: list[dict[str, Any]], terms: list[str]):
    """두 스냅샷을 견줘 (변경, 신규, 사라짐)을 돌려준다. 출력은 하지 않는다."""
    pmap = {i["name"]: i for i in prev}
    changed, new = [], []
    for i in cur:
        if terms and not _match(i, terms):
            continue
        q = pmap.get(i["name"])
        if q is None:
            new.append(i)
            continue
        # 관측이 빈 지표가 있다(수집 실패·수동 슬롯). `or [{}]`만으로는 부족하다 —
        # 리스트가 **존재하되 비어 있으면** [0] 접근에서 터진다(실제로 겪었다).
        a = (i.get("observations") or [{}]) or [{}]
        b = (q.get("observations") or [{}]) or [{}]
        a0 = a[0] if a else {}
        b0 = b[0] if b else {}
        if (a0.get("date"), a0.get("value")) != (b0.get("date"), b0.get("value")):
            changed.append((i, b0))
    cnames = {i["name"] for i in cur}
    return changed, new, [q for q in prev if q["name"] not in cnames]


def window_counts(since: str, until: str, terms: list[str] | None = None):
    """창 **밖** 변화량을 세는 용도. 개수만 돌려준다."""
    snaps = _snapshots()
    a, b = _pick(snaps, until), _pick(snaps, since)
    if a is None or b is None or a == b:
        return 0, 0, 0
    c, n, g = _compare(_load(snaps[a]), _load(snaps[b]), terms or [])
    return len(c), len(n), len(g)


def cmd_diff(days_back: int, terms: list[str], since: str | None = None,
             until: str | None = None) -> int:
    """두 스냅샷을 견줘 **값이 바뀐 지표만** 보여준다.

    ⚠ `--back`은 **날짜가 아니라 스냅샷 개수**다. 수집을 매일 돌리지 않으면
    `--back 7`이 7일 전을 가리키지 않는다(실제로 08-28 기준 7칸 뒤는 08-19였다).
    날짜로 자르려면 `--since`(시작) · `--until`(끝)을 쓴다.

    `--until`이 없으면 끝은 **최신 스냅샷**이다. 학회처럼 **닫힌 주간**으로 고정해야
    하면(지난 세션까지) `--until <지난 세션일>`을 함께 준다 — 그래야 준비 기간
    아무 날에 돌려도 **매번 같은 자료**가 나온다.
    """
    snaps = _snapshots()
    if len(snaps) < 2:
        print("비교할 스냅샷이 2개 이상 필요합니다. " + _no_snapshot_hint())
        return 1

    cur_i = 0
    if until:
        cur_i = _pick(snaps, until)
        if cur_i is None:
            print(f"{until} 이전 스냅샷이 없습니다.")
            return 1
    if since:
        idx = _pick(snaps, since)
        if idx is None:
            oldest = snaps[-1].stem[len("snapshot_"):]
            print(f"{since} 이전 스냅샷이 없습니다. 가장 오래된 것은 {oldest}입니다.")
            return 1
    else:
        idx = min(cur_i + days_back, len(snaps) - 1)
    if idx == cur_i:
        print(f"시작과 끝이 같은 스냅샷({snaps[idx].stem})입니다 — 비교할 것이 없습니다.")
        return 1

    cur, prev = _load(snaps[cur_i]), _load(snaps[idx])
    changed, new, gone = _compare(cur, prev, terms)

    print(f"# {snaps[idx].stem} → {snaps[cur_i].stem}\n")
    print(f"값 변경 {len(changed)} · 신규 {len(new)} · 사라짐 {len(gone)}\n")
    for i, old in changed:
        obs = i.get("observations") or []
        o = obs[0] if obs else {}
        arrow = ""
        if isinstance(o.get("value"), (int, float)) and isinstance(old.get("value"), (int, float)):
            d = o["value"] - old["value"]
            arrow = f"  ({d:+,.4g})"
        print(f"  {i['name'][:44]:44} {_fmt(old.get('value'))}({old.get('date') or '-'})"
              f" → {_fmt(o.get('value'))}({o.get('date') or '-'}){arrow}")
    for i in new:
        print(f"  [신규] {i['name']}")
    for p in gone:
        print(f"  [사라짐] {p['name']}")
    return 0


# ─────────────────────────── news ───────────────────────────

_ROW = re.compile(r"^\|\s*(?P<title>[^|]+?)\s*\|\s*(?P<src>[^|]*?)\s*\|"
                  r"\s*(?P<date>[^|]*?)\s*\|\s*\[[^\]]*\]\((?P<url>[^)]+)\)\s*\|\s*$")


def _digest_dir() -> Path:
    env = load_env()
    v = (env.get("OBSIDIAN_VAULT_PATH") or "").strip().strip('"')
    if v and (Path(v) / "04_DataBook" / "_News").is_dir():
        return Path(v) / "04_DataBook" / "_News"
    return OUTPUT_DIR / "Macro" / "_News"


def _parse_digest(path: Path) -> list[dict[str, str]]:
    """마크다운 표에서 기사 행만 뽑는다. 팀 섹션(`## …`)을 함께 기록한다."""
    out, team = [], ""
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("## "):
            team = line[3:].strip()
            continue
        m = _ROW.match(line)
        if not m or m.group("title") in ("제목", "---"):
            continue
        out.append({**m.groupdict(), "team": team})
    return out


def cmd_news(query: list[str], only_new: bool, limit: int, team: str | None) -> int:
    d = _digest_dir()
    files = sorted(d.glob("NewsDigest_*.md"), reverse=True)
    if not files:
        print(f"다이제스트가 없습니다: {d}")
        return 1
    rows = _parse_digest(files[0])
    label = files[0].stem

    if only_new:
        if len(files) < 2:
            print("비교할 이전 다이제스트가 없습니다.")
            return 1
        seen = {r["url"] for r in _parse_digest(files[1])}
        rows = [r for r in rows if r["url"] not in seen]
        label += f" (vs {files[1].stem} 신규분)"

    if team:
        rows = [r for r in rows if team in r["team"]]
    if query:
        rows = [r for r in rows if all(q.lower() in r["title"].lower() for q in query)]

    print(f"# {label} — {len(rows)}건"
          + (f" · 검색 '{' '.join(query)}'" if query else "")
          + (f" · {team}팀" if team else "") + "\n")
    for r in rows[:limit]:
        print(f"  {r['title'][:88]}")
        print(f"     {r['src'][:30]} · {r['date'][:22]} · {r['team'][:18]}")
    if len(rows) > limit:
        print(f"\n  … 외 {len(rows)-limit}건 (--limit 으로 더 보기)")
    return 0


# ─────────────────────────── CLI ───────────────────────────

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="databook query", description="산출물에서 필요한 부분만 조회")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("show", help="이름으로 지표를 찾아 값만 출력")
    s.add_argument("terms", nargs="+", help="검색어(여러 개면 AND)")
    s.add_argument("--points", type=int, default=4, help="라벨당 관측 수 (기본 4)")

    d = sub.add_parser("diff", help="이전 스냅샷 대비 값이 바뀐 지표만")
    d.add_argument("--back", type=int, default=1, help="몇 번째 이전 스냅샷과 비교 (기본 1)")
    d.add_argument("terms", nargs="*", help="특정 지표만 볼 때 검색어")

    n = sub.add_parser("news", help="뉴스 다이제스트 검색 (요약·선별 아님)")
    n.add_argument("--q", nargs="*", default=[], help="제목 검색어(AND)")
    n.add_argument("--new", action="store_true", help="이전 다이제스트에 없던 기사만")
    n.add_argument("--team", help="팀 섹션 필터 (예: 4팀)")
    n.add_argument("--limit", type=int, default=30)

    a = ap.parse_args(argv)
    if a.cmd == "show":
        return cmd_show(a.terms, a.points)
    if a.cmd == "diff":
        return cmd_diff(a.back, a.terms)
    return cmd_news(a.q, a.new, a.limit, a.team)


if __name__ == "__main__":
    sys.exit(main())
