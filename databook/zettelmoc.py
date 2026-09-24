"""판독 초안 → 축별 MOC 생성. **시황분석이 실제로 호출하는 유일한 경로.**

**왜 필요한가** — 볼트 규칙이 이미 답을 적어놨다:
「논문을 아무리 승격해도 02_Papers에 있는 것만으로는 시황에 반영되지 않는다.
 반영되는 경로는 하나뿐 — 지표 노드의 판정 규칙으로 옮겨진 것.」
초안 900건을 `07_Zettel/_drafts/`에 쌓아둔 것만으로는 **다음 세션의 에이전트가 존재를 모른다.**
축별로 묶어 MOC를 만들고 진입점 §1에 등재해야 비로소 불려 나온다.

**왜 손으로 안 쓰나** — 재판독·승격으로 초안 구성이 계속 바뀐다. 손으로 쓴 목록은
그 순간 낡기 시작하고, 낡은 목록은 **있는 것을 없다고 말한다.** 매번 다시 만든다.

**등급 규칙** — 여기 실린 것은 전부 기계 판독이다(`human_verified: false`).
유튜브 계층과 같은 취급을 한다: **포인터로 쓰고, 수치·인용은 원문 PDF를 확인한 뒤에만 쓴다.**
`cross-rejected`는 아예 싣지 않는다 — 검토 결과 전부 조건 탈락·범위 과장·인과 반전이었다.
"""
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

from .core import load_env

DRAFTS = "07_Zettel/_drafts"
SELFREAD = "07_Zettel/_drafts_selfread"
PDFDIR = "06_SourceArchive/06-BIS-Archive-Catalog/PDFs"
LOSSLOG = "07_Zettel/_drafts_소실_기록.md"
MOC = "03_MOC/BIS 판독 MOC.md"

AXES = [
    ("liquidity", "유동성·신용", "지준·QT·은행자본·NBFI·시장유동성"),
    ("inflation", "물가·정책금리", "인플레·기대·통화정책 전달·환율전가"),
    ("growth", "성장·경기", "생산성·노동시장·투자·금융사이클"),
    ("geopolitics", "지정학·무역", "제재·관세·공급망·원자재·주권위험"),
]


def _meta(t: str, k: str) -> str:
    m = re.search(rf"^{k}:\s*(.*)$", t, re.M)
    return m.group(1).strip().strip('"') if m else ""


def build(log=print) -> int:
    env = load_env()
    vault = Path(env.get("OBSIDIAN_VAULT_PATH") or ".")
    d = vault / DRAFTS
    if not d.is_dir():
        log(f"초안 폴더가 없다: {d}")
        return 1

    items: dict[str, list[dict]] = {a: [] for a, _, _ in AXES}
    skipped = {"rejected": 0, "unknown_axis": 0}
    for f in sorted(d.glob("*.md")):
        t = f.read_text(encoding="utf-8", errors="replace")
        ver = _meta(t, "verification")
        if ver not in ("machine-cross-verified", "machine-cross-verified-partial"):
            skipped["rejected"] += 1
            continue
        ax = _meta(t, "axis")
        if ax not in items:
            skipped["unknown_axis"] += 1
            continue
        num = _meta(t, "number") or (re.search(r"BIS_WP_(\d+)", f.stem) or [None, "?"])[1]
        try:
            num_i = int(num)
        except ValueError:
            num_i = 0
        items[ax].append({
            "n": num_i, "stem": f.stem, "claim": _meta(t, "title"),
            "partial": ver.endswith("partial"),
            "q": f"{_meta(t, 'quotes_verified')}/{_meta(t, 'quotes_total')}",
        })

    total = sum(len(v) for v in items.values())

    # **진도를 목록 안에 박아 둔다.** 이 MOC는 "판독이 끝난 것"이 아니라
    # "지금까지 읽힌 것 중 통과분"이다. 그 구분이 노트에 없으면 다음 세션의
    # 에이전트가 **없는 번호대를 '연구가 없다'로 읽는다** — 2026-09-17 초안
    # 730건이 소실됐을 때 MOC 링크 517개가 죽은 채 남아 실제로 그럴 뻔했다.
    # 진도는 **두 초안 폴더를 합쳐** 센다. 교차검증분(_drafts)만 세면 자체 판독분이
    # "안 읽힌 것"으로 보여, 이 배너가 막으려던 바로 그 오독이 다시 생긴다.
    # 다만 자체 판독분은 관문 B가 없어 이 MOC에 싣지 않으므로 배너에서 그 구분을 명시한다.
    def _nums(folder):
        return {m.group(1) for f in folder.glob("BIS_WP_*.md")
                if (m := re.match(r"BIS_WP_(\d+) ", f.name))}

    n_pdf = len(list((vault / PDFDIR).glob("BIS_WP_*.pdf")))
    crossed = _nums(d)
    self_dir = vault / SELFREAD
    uncrossed = (_nums(self_dir) - crossed) if self_dir.exists() else set()
    n_read = len(crossed) + len(uncrossed)
    self_note = (
        f" 이 가운데 **{len(uncrossed):,}편은 교차검증 없이 대화 에이전트가 직접 읽은 것**"
        f"이라 이 목록에 싣지 않는다 — 초안은 `{SELFREAD}/`에 있고 `flag/uncrossed`가 붙어 있다.\n"
        if uncrossed else "\n"
    )
    loss = (f"\n> 소실·재판독 경위는 [[{Path(LOSSLOG).stem}]]."
            if (vault / LOSSLOG).exists() else "")
    progress = (
        f"> [!danger] 이 목록은 아카이브 전체가 아니다 — 판독 진도 "
        f"**{n_read:,} / {n_pdf:,}편**\n"
        f"> 원문 {n_pdf:,}편 중 초안이 있는 것이 {n_read:,}편이고, 여기 실린 건 "
        f"교차검증을 통과한 승격후보 {total:,}건뿐이다.{self_note}"
        f"> **없는 번호대는 아직 안 읽힌 것이지 '그런 연구가 없는' 것이 아니다.** "
        f"없다는 말을 이 목록으로 하지 마라.{loss}\n"
    )
    secs = []
    for key, label, hint in AXES:
        rows = sorted(items[key], key=lambda r: -r["n"])
        lines = []
        for r in rows:
            flag = f" ⚠인용{r['q']}" if r["partial"] else ""
            lines.append(f"- **WP {r['n']}** — [[{r['stem']}|{r['claim']}]]{flag}")
        secs.append(
            f"## {label}  <small>{len(rows)}건</small>\n\n"
            f"> {hint}\n\n" + ("\n".join(lines) if lines else "_(없음)_") + "\n")

    p = vault / MOC
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(f"""---
title: BIS 판독 MOC
type: MOC
created: {date.today().isoformat()}
updated: {date.today().isoformat()}
status: working
verification: machine-cross-verified
human_verified: false
reliability: working-paper
source: "BIS Working Papers 전수 (아카이브 1~1376)"
tags: [type/MOC, domain/intel, source/bis, flag/needs-review]
related: ["[[시황 분석 진입점]]", "[[원문 아카이브 MOC]]", "[[제텔 MOC]]"]
---

# BIS 워킹페이퍼 전수 판독 — 축별 소환 인덱스

> [!warning] 여기 실린 것은 **기계 판독 초안**이다 — 사람이 읽지 않았다
> 외부 모델이 원문 PDF를 읽고 주장을 뽑은 뒤, **다른 계열 모델이 독립적으로 검증**한 것만 실었다.
> **쓰는 법**: 주장은 **포인터로** 쓴다. 수치·인용을 시황에 옮길 때는 **원문 PDF를 직접 확인한 뒤**에만 쓴다.
> ⚠인용 표시가 붙은 항목은 근거 인용 중 일부가 원문 대조에 실패했다 — **그 인용은 쓰지 않는다.**

> [!info] 무엇이 걸러졌나
> 교차검증에서 반려된 초안은 **여기 싣지 않는다.** 인용이 3/3이어도 주장은 틀릴 수 있다.
> 1차 판독(2026-08) 반려 79건은 **전건 검토했고 전부 실제 오류였다** — 조건 탈락("실업 갭이
> 0에 가까울 때"를 삭제), 범위 과장("이 비교군보다 낫다"→"가장 낫다"), **인과 반전**(논문은
> 8.9배 증가라는데 초안은 "늘지 않는다").
> ⚠ **2차 판독(2026-09-17) 반려분은 전건 검토하지 않았다.** 1차의 "전부 정당"을 이 배치에
> 그대로 옮기지 마라 — 2차에서는 내용이 아니라 **문장 구조** 때문에 반려된 사례가 실제로 나왔다
> (결과 둘을 한 문장에 접합하면 부품 하나가 약할 때 전체가 거짓 판정을 받는다).
> 반려분도 판정 근거째로 초안 파일에 남아 있으니, 필요하면 거기서 직접 확인한다.

{progress}
**수록 {total}건** · 축별로 논문 번호 내림차순(최신 우선).
초안 원본은 `{DRAFTS}/`, 원문 PDF는 `06_SourceArchive/06-BIS-Archive-Catalog/PDFs/`.

{chr(10).join(secs)}
---
자동 생성 {date.today().isoformat()} · `python -m databook zettelmoc` 로 재생성한다.
초안이 바뀌면 **반드시 다시 돌린다** — 낡은 목록은 있는 것을 없다고 말한다.
""", encoding="utf-8")

    log(f"수록 {total}건 (반려·미분류 {skipped['rejected'] + skipped['unknown_axis']}건 제외)")
    for key, label, _ in AXES:
        log(f"  {label:14} {len(items[key]):>4}건")
    log(f"  → {p}")
    return 0
