"""원문 인테이크 — **무엇이 아직 안 읽혔나**를 알려준다.

왜 필요한가
    `paper-autopilot`은 **수집**만 한다. 분해는 사람이 프롬프트로 수동으로 했고,
    그래서 다운로드 폴더에 원문이 계속 쌓이기만 했다(2026-08-31 기준 399편).
    **"읽을 것"과 "이미 읽은 것"을 가르는 장치가 없으면 쌓이는 것을 막을 수 없다.**

    이 모듈은 분해를 대신하지 않는다. 분해는 읽고 판단하는 일이라 AI가 한다.
    여기서 하는 것은 그 앞의 세 가지다 —
      ① 새 원문을 찾고
      ② **이미 볼트에 노트가 있는지** 대조하고
      ③ 실증이냐 이론이냐를 갈라 **어느 프롬프트를 쓸지** 지정한다

왜 ③이 중요한가
    볼트 CLAUDE.md §14-3이 정한 갈림길이다. 실증용 절차를 이론 논문에 그대로 돌리면
    대조할 수치가 없어 *"저자가 이렇게 주장했다"* 요약만 남는다.
    **2026-08-21 기준 이론 고전 12편이 정확히 이 이유로 제텔 0건이었다** —
    원문이 없어서가 아니라 축이 없어서였다. 그래서 자동으로 갈라준다.

쓰는 법
    python -m databook intake                      # 미분해 목록
    python -m databook intake --limit 5 --detail   # 다음 5편을 프롬프트까지
    python -m databook intake --dir ~/Downloads    # 다른 폴더도 함께
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from typing import Any

from .core import load_env

# 볼트에서 이미 분해된 것을 찾는 곳
NOTE_DIRS = ("02_Papers", "04_Zettel", "05_Library", "06_SourceArchive")
# 읽은 원문 대장 — 파일명↔노트 제목 매칭이 실패하는 경우를 사람이 직접 기록한다
READ_LEDGER = "reading_log.yaml"
# 원문이 쌓이는 곳 (저장소 기준 상대 + 홈 기준 절대)
#
# ⚠ 2026-09-01 확장 — **스캔 범위가 좁아 미분해 편수를 크게 과소보고하고 있었다.**
#   종전 목록은 저장소 안(docs/*)만 봤다. 그런데 사용자가 실제로 논문을 받는 곳은
#   `~/Downloads`와 **`~/OneDrive/Desktop/새 폴더*`** 다.
#   Desktop 267편이 통째로 빠진 채 "미분해 370편"으로 보고돼 왔다 — 실제로는 694편이었다.
#   **받는 곳을 스캔하지 않으면 대장은 진실을 말하지 않는다.**
SCAN_DIRS = (
    "docs/library",
    "docs/vault/06_SourceArchive",
    "docs/vault/Attachments",
    "~/Downloads",
    "~/OneDrive/Desktop",
    "~/Documents/MacroVault/Attachments",
    "~/Documents/MacroVault/06_SourceArchive",
    "~/OneDrive/ドキュメント/카카오톡 받은 파일",
)
# 세지 않는 곳 — 백업·캐시·미러. 경로에 이 조각이 있으면 건너뛴다.
SKIP_PARTS = ("backup", ".pdfcache", "sep_cache", "macro-source-library-clean")

# 실증 논문의 흔적 — 표·계수·표본기간이 본문에 있다
_EMPIRIC = [
    (r"\bTable\s+\d", 3), (r"표\s*\d", 3),
    (r"\bt-statistic|\bt-stat|\(t\s*=", 3),
    (r"\bstandard error|표준오차|\bS\.?E\.?\s*[=(]", 3),
    (r"\bR\s*\^?2\b|\bR²|adjusted R", 3),
    (r"\bregression|회귀분석|\bOLS\b|\bGMM\b|\bVAR\b|\bIV\b", 2),
    (r"\bsample period|표본기간|observations\s*[:=]|\bN\s*=\s*\d{2,}", 2),
    (r"\*{1,3}\s*p\s*<|significant at the", 2),
]
# 이론 논문의 흔적 — 모형·증명·명제
_THEORY = [
    (r"\bProposition\s+\d|\bLemma\s+\d|\bTheorem\s+\d", 4),
    (r"\bProof\b|증명\b", 3),
    (r"\bfirst-order condition|오일러 방정식|\bEuler equation", 3),
    (r"\bequilibrium\b.{0,40}\bdefinition|균형의 정의", 2),
    (r"\bcalibrat", 2),
]

_STOP = re.compile(r"[^0-9A-Za-z가-힣]+")


def _norm(s: str) -> str:
    """제목 대조용 정규화 — 확장자·판본 표기·구두점을 지운다."""
    s = unicodedata.normalize("NFKC", s).lower()
    s = re.sub(r"\.(pdf|md)$", "", s)
    s = re.sub(r"\(\d+\)$|\s-\s?main$|_v\d+$|-v\d+$", "", s)
    return _STOP.sub(" ", s).strip()


def _tokens(s: str) -> set[str]:
    return {t for t in _norm(s).split() if len(t) > 2}


def _key(stem: str) -> str:
    """대장 조회용 키. 브라우저가 붙이는 ` (1)` 사본 접미사를 같은 원문으로 본다."""
    return _norm(stem)


def _ledger(repo: Path) -> dict[str, str]:
    """읽은 원문 대장을 읽는다 — `파일명 stem: 남긴 노트 제목` 매핑.

    ⚠ 왜 필요한가
        `_matched()`는 **파일명 토큰과 노트 제목의 겹침**으로 판정한다.
        그런데 제텔 제목은 파일명이 아니라 **주장 문장**이다
        (`ssrn-2244796.pdf` → "원자재 가격의 지배 요인은 시계에 따라 갈린다").
        겹치는 토큰이 0이라 **분해를 끝낸 논문이 계속 미분해로 뜬다.**
        2026-08-31에 29편을 분해했는데 목록이 전혀 줄지 않아 드러났다.

        자동 매칭을 더 똑똑하게 만드는 대신 **사람이 적는 대장**을 둔다 —
        느슨한 추론보다 명시적 기록이 낫다. 파일이 없으면 조용히 건너뛴다.
    """
    f = repo / READ_LEDGER
    if not f.is_file():
        return {}
    try:
        import yaml
        raw = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
    except Exception:
        return {}
    out: dict[str, str] = {}
    for e in (raw.get("read") or []):
        if isinstance(e, dict) and e.get("file"):
            out[_key(str(e["file"]))] = str(e.get("note") or "대장 기록")
    return out


def _text(pdf: Path, sample: int = 16) -> str:
    """문서 **전체에 걸쳐** 표본을 뽑는다.

    ⚠ 앞쪽만 읽으면 판정이 어긋난다. 표·계수는 중반에, 명제·증명은 부록 직전에
    몰린다. 실제로 앞 12쪽만 읽었을 때 King et al.(RBC 이론 고전)이
    '판정불가'로 나왔다. 앞 5·중간·뒤쪽을 고르게 집는다.
    """
    def pick(n: int) -> list[int]:
        if n <= sample:
            return list(range(n))
        head = list(range(5))
        rest = sample - 5
        step = max(1, (n - 5) // rest)
        return head + list(range(5, n, step))[:rest]

    try:
        import pypdf
        r = pypdf.PdfReader(str(pdf))
        idx = pick(len(r.pages))
        return "\n".join((r.pages[i].extract_text() or "") for i in idx)
    except Exception:
        try:
            import fitz
            with fitz.open(str(pdf)) as d:
                return "\n".join(d[i].get_text() for i in pick(d.page_count))
        except Exception:
            return ""


def classify(text: str) -> tuple[str, int, int]:
    """(종류, 실증점수, 이론점수). 점수가 비슷하면 실증으로 본다 — 계수가 있으면 대조가 가능하다."""
    e = sum(w for pat, w in _EMPIRIC if re.search(pat, text, re.I))
    t = sum(w for pat, w in _THEORY if re.search(pat, text, re.I))
    if e == 0 and t == 0:
        return "판정불가", e, t
    return ("이론" if t > e + 2 else "실증"), e, t


def _vault() -> Path | None:
    v = (load_env().get("OBSIDIAN_VAULT_PATH") or "").strip().strip('"')
    p = Path(v) if v else None
    return p if p and p.is_dir() else None


def _existing_notes(vault: Path) -> list[tuple[str, set[str]]]:
    out = []
    for d in NOTE_DIRS:
        base = vault / d
        if not base.is_dir():
            continue
        for f in base.rglob("*.md"):
            out.append((f.stem, _tokens(f.stem)))
    return out


def _matched(name: str, notes: list[tuple[str, set[str]]]) -> str | None:
    """파일명 토큰이 노트 제목과 충분히 겹치면 '이미 분해됨'으로 본다.

    ⚠ 느슨한 대조다. 파일명이 `w16385.pdf`처럼 코드뿐이면 못 잡는다 —
    그런 것은 미분해로 뜨고, 실제로 읽어보면 중복일 수 있다. **놓치는 쪽보다
    중복으로 뜨는 쪽이 낫다**(읽으면 바로 안다).
    """
    t = _tokens(name)
    if len(t) < 2:
        return None
    for title, nt in notes:
        if not nt:
            continue
        inter = len(t & nt)
        if inter >= 3 or (inter >= 2 and inter / min(len(t), len(nt)) >= 0.6):
            return title
    return None


def scan(extra: list[Path] | None = None, repo: Path | None = None) -> dict[str, Any]:
    repo = repo or Path(__file__).resolve().parent.parent
    vault = _vault()
    notes = _existing_notes(vault) if vault else []

    seen: set[Path] = set()
    dupkeys: set[str] = set()
    pdfs: list[Path] = []
    for d in list(SCAN_DIRS) + [str(p) for p in (extra or [])]:
        # ⚠ expanduser 를 **먼저** 한다. `~/Downloads`는 is_absolute()가 False라서
        #   순서를 바꾸면 `repo/~/Downloads`가 되어 조용히 사라진다(2026-09-01 실제로 그랬다).
        base = Path(d).expanduser()
        if not base.is_absolute():
            base = repo / base
        if not base.is_dir():
            continue
        for f in base.rglob("*.pdf"):
            if any(sp in str(f) for sp in SKIP_PARTS):
                continue
            rp = f.resolve()
            if rp in seen:
                continue
            seen.add(rp)
            # 같은 원문이 여러 위치에 있으면 한 번만 센다(대장 키 기준)
            k = _key(f.stem)
            if k in dupkeys:
                continue
            dupkeys.add(k)
            pdfs.append(f)

    ledger = _ledger(repo)
    # 판정을 **세 상태**로 가른다 — 2026-09-01 개정.
    #   done   : 대장에 있다. **확인된 사실**
    #   maybe  : 제목이 겹친다. **추측일 뿐이다**
    #   todo   : 아무 근거도 없다
    #
    # ⚠ 왜 갈랐나
    #   종전에는 `ledger or _matched` 로 묶어 하나의 "분해됨"으로 셌다.
    #   그 결과 **가짜 분해됨이 대량 생산**됐다 — 실측 표본:
    #     Basak "A Model of Financialization of Commodities" -> "2012 Index Investment..."(다른 논문)
    #     amiti-et-al-2019 관세 논문 -> "2003 Melitz"(완전히 무관)
    #   788편 중 "분해됨 392"로 보고됐으나 **대장 근거는 94편뿐**이었다.
    #   **추측을 사실과 같은 칸에 세면 백로그가 사라진 것처럼 보인다.**
    done, maybe, todo = [], [], []
    for f in sorted(pdfs):
        led = ledger.get(_key(f.stem))
        if led:
            done.append((f, led))
            continue
        hit = _matched(f.stem, notes)
        (maybe if hit else todo).append((f, hit))
    return {"vault": vault, "notes": len(notes), "total": len(pdfs), "ledger": len(ledger),
            "done": done, "maybe": maybe, "todo": [f for f, _ in todo]}


def cmd_intake(limit: int, detail: bool, extra_dirs: list[str] | None) -> int:
    extra = [Path(d).expanduser() for d in (extra_dirs or [])]
    r = scan(extra)
    if not r["vault"]:
        print("OBSIDIAN_VAULT_PATH 가 없습니다 — 볼트 노트와 대조할 수 없습니다.")
    print(f"\n원문 {r['total']}편 · 볼트 노트 {r['notes']}개와 대조"
          + (f" · 대장 {r['ledger']}건" if r.get("ledger") else " · **대장 없음**"))
    print("=" * 70)
    print(f"  ✅ 분해 확인 (대장 근거)   : {len(r['done'])}편")
    print(f"  ❓ 제목만 겹침 (추측)      : {len(r.get('maybe', []))}편  ← 확인 전까지 읽은 것이 아니다")
    print(f"  ⬜ 근거 없음               : {len(r['todo'])}편")
    print(f"  ── 실제 남은 일           : {len(r.get('maybe', [])) + len(r['todo'])}편")
    print("=" * 70)
    if not r["todo"]:
        print("  읽을 것이 없습니다.")
        return 0

    print(f"\n다음 {min(limit, len(r['todo']))}편 — 읽고 분해할 순서\n")
    for i, f in enumerate(r["todo"][:limit], 1):
        txt = _text(f) if detail else ""
        kind, e, t = classify(txt) if txt else ("미판정", 0, 0)
        mb = f.stat().st_size / 1048576
        print(f"  [{i}] {f.name[:66]}")
        print(f"      {mb:.1f}MB · {f.parent}")
        if detail:
            prompt = {"실증": "_System/Prompts/제텔 분해 프롬프트.md",
                      "이론": "_System/Prompts/이론논문 분해 프롬프트.md"}.get(kind)
            print(f"      판정: **{kind}** (실증 {e} / 이론 {t})"
                  + (f" → {prompt}" if prompt else " → 본문을 열어 직접 판단"))
            head = re.sub(r"\s+", " ", txt[:180]).strip()
            if head:
                print(f"      첫머리: {head[:150]}…")
        print()

    print("=" * 70)
    print("  분해 절차는 볼트 CLAUDE.md §14-3 — 2단계로 나눈다.")
    print("    1단계 뼈대만 뽑는다(노트를 만들지 않는다)")
    print("    2단계 제텔로 쪼갠다 — 노트 하나 = 인과관계 하나")
    print("  실증·이론에 따라 **프롬프트가 다르다.** 위 판정을 따른다.")
    return 0
