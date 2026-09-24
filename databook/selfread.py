"""BIS 원문 **자체 판독** — 대화 에이전트가 직접 읽고 쓴다.

`zettelize`는 외부 모델에 원문을 보내 판독시키고 **다른 계열 모델**에게 교차검증(관문 B)을
받는다. 그 경로가 막히면(크레딧 소진 등) 판독 자체가 멈춘다. 이 모듈은 그때의 우회로다.

**무엇이 빠지는가 — 관문 B다.** 판독자와 검증자가 같으면 자기 확증이라 교차검증이 아니다.
그래서 산출물은 `_drafts_selfread/`에 따로 쌓고 `verification: self-read-uncrossed`로 적으며
**`BIS 판독 MOC`에 싣지 않는다.** 크레딧이 복구되면 같은 논문을 교차검증에 다시 넣는다.

**관문 A는 그대로 건다.** 인용문이 원문에 문자열로 있는지는 읽은 주체가 누구든 기계가 센다.
그게 이 파이프라인에서 유일하게 반박 불가능한 검사다.

    selfread --next N      다음 N편의 원문을 앞·뒤로 잘라 텍스트로 떨군다 (읽을 거리)
    selfread --commit J    내가 쓴 판독 JSON을 받아 관문 A를 걸고 초안 파일로 확정한다
"""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

from .core import load_env
from .zettelize import (DRAFTS, HEAD_CHARS, MIN_TEXT_CHARS, PDFDIR, SUB,
                        TAIL_CHARS, pdf_text, verify_quotes)

SELF = "07_Zettel/_drafts_selfread"
# "none"은 **거시 4축 어디에도 안 붙는 논문**을 위한 자리다. BIS 워킹페이퍼에는
# 통계 인프라·암호학·측정방법론처럼 시황에 축으로 걸리지 않는 편이 섞여 있다.
# 가장 가까운 축을 억지로 붙이면 그 축을 소환했을 때 관계없는 논문이 딸려 나온다 —
# 읽었다는 사실만 남기고 축은 비운다(어차피 selfread는 MOC에 싣지 않는다).
AXES = ("liquidity", "inflation", "growth", "geopolitics", "none")


def _vault() -> Path:
    return Path(load_env().get("OBSIDIAN_VAULT_PATH") or ".")


def _workdir() -> Path:
    out = load_env().get("DATABOOK_OUTPUT_DIR") or "."
    d = Path(out) / "selfread"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _title(vault: Path, n: int) -> str:
    """카탈로그 노트에서 논문 제목만 꺼낸다 — 판독 전에 무엇을 읽는지는 알아야 한다."""
    f = vault / SUB / f"BIS_WP_{n}-catalog.md"
    if not f.is_file():
        return ""
    t = f.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^title:\s*(.*)$", t, re.M)
    return m.group(1).strip().strip('"') if m else ""


def _done(vault: Path) -> set[int]:
    """**두 폴더를 다 센다.** 외부 배치가 읽은 것을 내가 또 읽으면 돈이 아니라 시간을 버린다."""
    seen = set()
    for sub in (DRAFTS, SELF):
        for f in (vault / sub).glob("BIS_WP_*.md"):
            if m := re.match(r"BIS_WP_(\d+) ", f.name):
                seen.add(int(m.group(1)))
    return seen


def pick(limit: int, log=print) -> int:
    vault = _vault()
    done = _done(vault)
    BIG = 8 * 1024 * 1024
    pdfs = sorted((vault / PDFDIR).glob("BIS_WP_*.pdf"),
                  key=lambda f: (f.stat().st_size >= BIG,
                                 -int(re.search(r"(\d+)", f.stem).group(1))))
    todo = [f for f in pdfs
            if int(re.search(r"(\d+)", f.stem).group(1)) not in done][:limit]
    w = _workdir()
    log(f"판독 완료 {len(done):,}편 · 이번에 {len(todo)}편 → {w}")
    for f in todo:
        n = int(re.search(r"(\d+)", f.stem).group(1))
        try:
            full = pdf_text(f)
        except Exception as e:
            log(f"  WP {n:<5} ✘ 추출 실패 {type(e).__name__} {str(e)[:50]}")
            continue
        if len(full) < MIN_TEXT_CHARS:
            # 스캔본이다. 사람이 읽든 모델이 읽든 텍스트 층이 없으면 **없는 문장을 짓게 된다.**
            log(f"  WP {n:<5} ⏭ 스캔본 (추출 {len(full)}자) — OCR 없이는 판독 불가")
            continue
        body = full[:HEAD_CHARS] + (
            "\n\n===== [중간 생략] =====\n\n" + full[-TAIL_CHARS:]
            if len(full) > HEAD_CHARS + TAIL_CHARS else "")
        (w / f"WP_{n}.txt").write_text(
            f"# BIS WP {n} — {_title(vault, n)}\n"
            f"# 추출 {len(full):,}자 (앞 {HEAD_CHARS:,} + 뒤 {TAIL_CHARS:,})\n\n{body}",
            encoding="utf-8")
        (w / f"WP_{n}.full.txt").write_text(full, encoding="utf-8")
        log(f"  WP {n:<5} {len(full):>8,}자 → WP_{n}.txt")
    return 0


def commit(jpath: str, log=print) -> int:
    """판독 JSON → 초안 파일. **관문 A는 여기서 기계가 건다 — 내 판단이 아니다.**"""
    vault = _vault()
    recs = json.loads(Path(jpath).read_text(encoding="utf-8"))
    if isinstance(recs, dict):
        recs = [recs]
    w = _workdir()
    ok = bad = 0
    for r in recs:
        n = int(r["n"])
        fullf = w / f"WP_{n}.full.txt"
        if not fullf.is_file():
            log(f"  WP {n:<5} ✘ 원문 텍스트가 없다 — selfread --next 로 먼저 떨군다")
            bad += 1
            continue
        checks = verify_quotes(list(r.get("quotes") or []), fullf.read_text(encoding="utf-8"))
        got = sum(1 for c in checks if c["found"])
        claim = (r.get("claim") or "").strip()
        ax = r.get("axis", "")
        if ax not in AXES:
            log(f"  WP {n:<5} ✘ axis가 {AXES} 중에 없다: {ax!r}")
            bad += 1
            continue
        if got < 2:
            # 인용 둘이 원문에 없으면 본문을 안 본 것이다. 초안을 만들지 않는다.
            log(f"  WP {n:<5} ✘ 관문 A {got}/{len(checks)} — 초안 미작성")
            for c in checks:
                if not c["found"]:
                    log(f"           불일치: {c['quote'][:90]}")
            bad += 1
            continue

        safe = re.sub(r'[\/:*?"<>|]', "", claim)[:70]
        p = vault / SELF / f"BIS_WP_{n} — {safe}.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        part = "" if got == len(checks) else (
            f"\n> ⚠ 인용 {got}/{len(checks)}만 일치했다 — **불일치 인용은 쓰지 않는다.**")
        rows = "\n".join(
            ("- ✅ 원문 확인\n  > " + c["quote"]) if c["found"]
            else ("- ❌ **원문에 없음**" + (f" — {c['why']}" if c["why"] else "")
                  + "\n  > " + c["quote"])
            for c in checks)
        axtag = "flag/no-macro-axis, " if ax == "none" else f"domain/{ax}, "
        bul = lambda k, alt: "\n".join(f"- {x}" for x in (r.get(k) or [])) or alt
        p.write_text(f"""---
title: "{claim.replace('"', "'")}"
type: zettel_draft
status: draft
human_verified: false
source: "BIS Working Paper {n}"
source_note: "[[BIS_WP_{n}-catalog]]"
axis: {ax}
read_model: claude-opus-5 (대화 에이전트 직접 판독)
audit_model: "없음 — 교차검증 미실시"
quotes_total: {len(checks)}
quotes_verified: {got}
cross_supported: null
cross_is_central: null
verification: self-read-uncrossed
created: {date.today().isoformat()}
tags: [type/zettel-draft, {axtag}flag/needs-review, flag/uncrossed]
---

# {claim}

> [!warning] 교차검증을 받지 않은 초안이다
> 외부 모델 배치와 달리 **판독자와 검증자가 같다** — 다른 계열 모델의 독립 판정(관문 B)이 없다.
> 자기 확증을 배제할 장치가 빠져 있으므로 **`BIS 판독 MOC`에 싣지 않는다.**
> 관문 A(인용 원문 문자열 대조)는 그대로 걸었다 — 인용 {got}/{len(checks)}건 일치.{part}
> 크레딧이 복구되면 이 논문은 **교차검증을 다시 받아야 한다.**

## 핵심 수치

{bul("numbers", "_⚠ **수치를 뽑지 못했다** — 순수 이론모형이거나 판독이 얕았다. 원문 확인 전에는 쓰지 말 것_")}

## 메커니즘 — 왜 그렇게 되는가

{r.get("mechanism", "_(기재 없음)_")}

## 시황에서 언제 부르는가

{r.get("when", "_(기재 없음)_")}

## 이 주장이 깨지는 조건

{bul("contra", "_(기재 없음)_")}

## 요약

{r.get("summary", "_(기재 없음)_")}

## 관문 A — 근거 인용의 원문 대조

{rows}

## 저자가 밝힌 한계

{bul("limits", "_(논문에 명시된 한계 없음 — 그래서 더 조심해서 읽을 것)_")}

---
`BIS WP {n}` · {_title(vault, n)}
자체 판독 {date.today().isoformat()} · 교차검증 없음
""", encoding="utf-8")
        log(f"  WP {n:<5} ✅ 인용 {got}/{len(checks)} · {claim[:60]}")
        ok += 1

    # 볼트 밖 사본 — 2026-09-17 초안 730건이 원인 미상으로 사라진 뒤의 규칙이다.
    from .zettelize import _mirror
    _mirror(vault / SELF, load_env(), log)
    log(f"\n확정 {ok}건 · 반려 {bad}건")
    return 0 if ok else 1
