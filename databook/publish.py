"""볼트 발행 가드 — **망가진 런이 팀 볼트를 덮어쓰지 못하게 한다.**

2026-09-01에 실제로 벌어진 일: `.env`가 없는 저장소에서 `run`이 돌았다.
키가 필요한 지표가 전부 "수집 실패 — FRED_API_KEY 없음"으로 바뀌었고,
그 상태 그대로 볼트에 쓰여 **옵시디언 싱크를 타고 팀원 전원에게 퍼졌다.**
전날 311개가 들어 있던 Data Book이 168개짜리로 바뀌었다.

수집이 실패한 것 자체는 사고가 아니다. 네트워크는 끊기고 키는 만료된다.
**사고는 그 결과를 공유 볼트에 발행한 것**이다 — 로컬 `output/`에만 남았으면
다음 날 정상 런이 덮고 아무도 몰랐다.

그래서 규칙은 하나다 — **직전에 발행된 것보다 크게 나빠진 결과는 볼트에 쓰지 않는다.**
로컬 `output/`에는 그대로 쓴다(무엇이 깨졌는지 봐야 하니까). 정말 발행해야 하면 `--force-publish`.

기준선은 상태파일이 아니라 **볼트에 이미 있는 최신 인덱스 노트**에서 읽는다.
상태파일은 체크아웃마다 다른데, 이번 사고가 정확히 **다른 체크아웃에서 돌린 것**이었다.
볼트 자신에게 물어봐야 체크아웃이 몇 개든 같은 답이 나온다.
"""
from __future__ import annotations

import re
from pathlib import Path

# 인덱스 노트의 요약 줄: "> [!summary] 자동 수집 311 · 수동 슬롯 3 · 전체 331 — ..."
SUMMARY_RE = re.compile(r"자동 수집\s+(\d+)")
INDEX_RE = re.compile(r"^DataBook_\d{4}-\d{2}-\d{2}\.md$")

# 이 비율 밑으로 떨어지면 발행하지 않는다. 하루치 정상 변동(토스 IP 403 10개,
# 네트워크 순단 2~3개)은 전체의 5% 안쪽이라 20%는 넉넉한 여유다.
MIN_RATIO = 0.8
MAX_DROP_PCT = 20          # 표시용 — int(1-0.8)*100 은 부동소수 탓에 19가 나온다


def baseline(root: Path, prefix: str) -> tuple[str, int] | None:
    """볼트에 마지막으로 발행된 (날짜, 자동 수집 수). 없으면 None."""
    folder = Path(root) / prefix
    if not folder.is_dir():
        return None
    cands = [p for p in folder.iterdir() if p.is_file() and INDEX_RE.match(p.name)]
    if not cands:                       # 전부 아카이브로 밀렸을 수 있다
        arch = folder / "_archive"
        if arch.is_dir():
            cands = [p for p in arch.rglob("DataBook_*.md") if INDEX_RE.match(p.name)]
    if not cands:
        return None
    # 최신 하나가 아니라 **최근 5회 중 최댓값**을 기준선으로 쓴다.
    # 망가진 발행이 한 번 들어가면 기준선이 그만큼 내려가고, 그 다음 망가진 런은
    # 무사통과한다 — 2026-09-01 노트(168)가 실제로 그 상태였다.
    best: tuple[str, int] | None = None
    for p in sorted(cands, key=lambda p: p.name, reverse=True)[:5]:
        m = SUMMARY_RE.search(p.read_text(encoding="utf-8", errors="replace")[:2000])
        if not m:
            continue
        n = int(m.group(1))
        if best is None or n > best[1]:
            best = (p.name[len("DataBook_"):-len(".md")], n)
    return best


def allowed(root: Path, prefix: str, ok: int, env: dict[str, str] | None = None) -> tuple[bool, str]:
    """이 결과를 이 볼트에 발행해도 되나. (허용?, 사람이 읽을 이유)"""
    if (env or {}).get("DATABOOK_FORCE_PUBLISH"):
        return True, "--force-publish"
    if ok == 0:
        return False, "성공한 지표가 0개다 — 수집이 통째로 실패한 런이다"
    base = baseline(root, prefix)
    if base is None:
        return True, "볼트에 기준선 없음(첫 발행)"
    prev_date, prev_ok = base
    floor = int(prev_ok * MIN_RATIO)
    if ok >= floor:
        return True, f"최근 발행 최대 {prev_ok}개({prev_date}) 대비 {ok}개 — 정상 범위"
    return False, (f"최근 발행 최대 {prev_ok}개({prev_date}) → 이번 {ok}개. "
                   f"{MAX_DROP_PCT}% 넘게 줄었다")


def _key_hint(env: dict[str, str] | None) -> str:
    """왜 줄었는지 짚어 준다. 키 누락이 가장 흔한 원인이다(2026-09-01이 그랬다)."""
    from .setup import missing_required
    miss = missing_required(env or {})
    if miss:
        return ("  원인 후보: 필수 키가 비어 있다 — " + ", ".join(miss) +
                "\n           이 저장소에 .env가 없거나 다른 폴더에서 돌린 것은 아닌지 확인 "
                "(`python -m databook setup`)")
    return "  원인 후보: 네트워크·원천 API 장애. 잠시 뒤 다시 돌려 보고, 계속되면 로그의 실패 사유를 볼 것"


def filter_targets(targets: list[tuple[Path, str]], ok: int, env: dict[str, str] | None,
                   quiet: bool = False, dry: bool = False) -> list[tuple[Path, str]]:
    """볼트 대상만 검사해 통과한 것만 남긴다. 로컬 output/은 항상 통과시킨다.

    로컬을 막지 않는 이유 — 무엇이 깨졌는지 보려면 결과물이 남아 있어야 한다.
    막아야 하는 건 **남에게 퍼지는 경로**뿐이다.
    """
    from .core import OUTPUT_DIR
    keep: list[tuple[Path, str]] = []
    for root, prefix in targets:
        if Path(root) == OUTPUT_DIR:
            keep.append((root, prefix))
            continue
        ok_to, why = allowed(Path(root), prefix, ok, env)
        if ok_to:
            keep.append((root, prefix))
            continue
        if quiet:
            continue
        if dry:
            # --dry-run은 수집을 안 하므로 성공 0이 정상이다. 경고할 일이 아니다.
            print(f"  (dry-run: 볼트 {Path(root) / prefix} 는 건드리지 않았다)")
            continue
        print(f"\n⚠ 볼트 발행 중단: {Path(root) / prefix}")
        print(f"  {why}")
        print(_key_hint(env))
        print("  → 로컬 output/ 에는 그대로 썼다. 확인 후 정말 발행하려면 "
              "`python -m databook run --force-publish`")
    return keep
