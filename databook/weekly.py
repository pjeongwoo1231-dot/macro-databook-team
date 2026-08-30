"""세션 준비 담당자가 치는 **단 하나의 명령**.

학회 리듬
    화(세션) → 수·목(준비 시작) → 금 → 월 → 화(다음 세션, 발표)

**기준 시점(as-of)을 직전 세션일로 고정한다.** 준비를 수요일에 하든 일요일에 하든
같은 자료가 나온다 — 시점이 움직이면 수요일에 쓴 문장이 월요일에 틀린 문장이 되고
글을 다시 써야 한다.

⚠ **as-of 고정은 "7일치만 본다"는 뜻이 아니다.**
   거시분석의 재료는 **그 시점까지의 전체 상태와 장기 시계열**이다.
   지표마다 2000년부터의 이력이 있고, 볼트 「좋은 시황의 규칙」이 요구하는
   「추세」와 「사례(기저율)」는 7일치로는 아예 낼 수 없다.
   `diff`는 **어디를 새로 볼지 고르는 길잡이**일 뿐 재료가 아니다.

그래서 세 층을 함께 준다
    1. 기준 시점의 **전체 상태** — DataBook_<as-of>.md (지표 328개, 각자 다른 기준일)
    2. 직전 세션 이후 **변경분** — 무엇을 새로 확인할지
    3. **장기 시계열** 위치      — 추세·기저율을 실제로 재는 곳

끝에 as-of 이후 변화 건수를 찍는다 — 발표 당일 한 절로 덧붙일 몫이다.
"""
from __future__ import annotations

import re
from datetime import date, timedelta
from pathlib import Path

from .core import OUTPUT_DIR

_TUE = 1  # date.weekday(): 월=0, 화=1


def last_session(today: date | None = None) -> date:
    """직전 세션일(화요일). 오늘이 화요일이면 **7일 전**을 준다(0일 전이 아니라)."""
    t = today or date.today()
    back = (t.weekday() - _TUE) % 7
    return t - timedelta(days=back or 7)


def next_session(today: date | None = None) -> date:
    """다음 세션일(발표일). 오늘이 화요일이면 오늘이다."""
    t = today or date.today()
    return t + timedelta(days=(_TUE - t.weekday()) % 7)


def _batch_ran_today(today: date | None = None) -> tuple[bool, str]:
    """daily.log 끝부분에서 오늘 날짜의 '종료' 줄을 찾는다."""
    log = OUTPUT_DIR / "daily.log"
    if not log.exists():
        return False, "daily.log가 없습니다 — 일일 배치가 한 번도 돌지 않았습니다."
    stamp = (today or date.today()).isoformat()
    tail = log.read_text(encoding="utf-8", errors="replace").splitlines()[-60:]
    for line in reversed(tail):
        if line.startswith(stamp) and "=== 종료" in line:
            m = re.search(r"실패 (INT)건(.*)$".replace("INT", r"\d+"), line)
            if m and m.group(1) != "0":
                return True, f"오늘 배치는 돌았으나 {m.group(1)}건 실패{m.group(2).strip()}"
            return True, "오늘 배치 정상 종료"
    return False, "오늘 일일 배치가 아직 안 끝났습니다 (`python -m databook daily`, 약 15~20분)"


def _databook_paths(asof: date) -> list[str]:
    """기준 시점의 Data Book 파일. 볼트본과 로컬본 둘 다 알려준다."""
    from .core import load_env
    out, v = [], (load_env().get("OBSIDIAN_VAULT_PATH") or "").strip().strip('"')
    for root, sub in ((Path(v) if v else None, "04_DataBook"), (OUTPUT_DIR, "Macro")):
        if root is None:
            continue
        f = root / sub / f"DataBook_{asof.isoformat()}.md"
        out.append(str(f) if f.exists() else f"{f}   ← 없음(그날 수집이 안 돌았다)")
    return out


def _print_history() -> None:
    """장기 시계열 CSV의 위치·규모·기간.

    **거시분석의 재료는 7일치 변경분이 아니다.** 볼트의 「좋은 시황의 규칙」은
    주장마다 「추세·사례·이론」 중 둘 이상을 요구하는데, 추세(어디서 어디로 갔나)와
    사례(같은 배열이 과거 몇 번, 그 뒤 무엇이 왔나)는 **여기서만 잴 수 있다.**
    """
    d = OUTPUT_DIR / "history"
    files = sorted(d.glob("*.csv")) if d.is_dir() else []
    if not files:
        print("  장기 시계열이 없습니다 — `python -m databook history` 를 한 번 돌리세요.")
        return
    print(f"  {d}")
    print(f"  계열 {len(files)}개 (FRED·Yahoo·GPR — 대체로 2000년부터)")
    print("  ⚠ **추세와 기저율은 여기서만 나온다.** §2의 변경분으로는 낼 수 없다.")
    print("     「좋은 시황의 규칙」의 근거 3축 중 추세·사례가 여기에 걸려 있다.")
    print("     예) '같은 배열이 과거 13번 있었고 그중 7번만 음수' → 이 CSV를 직접 세서 낸다.")
    for name in ("DGS10", "UNRATE", "CPIAUCSL", "VIXCLS"):
        f = d / f"{name}.csv"
        if not f.exists():
            continue
        rows = f.read_text(encoding="utf-8", errors="replace").splitlines()
        if len(rows) > 2:
            print(f"    {name:10} {len(rows) - 1:>6}행  "
                  f"{rows[1].split(',')[0]} → {rows[-1].split(',')[0]}")


def run(since: str | None = None, limit: int = 30, asof: str | None = None) -> int:
    from .query import cmd_diff, cmd_news, window_counts
    from .todo import cmd_todo

    today = date.today()
    # 기준 시점은 기본이 **직전 세션**이다. 다만 세션 전에 최신까지 당겨보고 싶을 때가 있다
    # (as-of 이후에 금통위 같은 큰 사건이 있었던 주). 그때만 --asof로 옮긴다.
    end = date.fromisoformat(asof) if asof else last_session(today)
    start = date.fromisoformat(since) if since else end - timedelta(days=7)
    nxt = next_session(today)
    dday = (nxt - today).days
    ok, msg = _batch_ran_today()

    print("=" * 68)
    print(f"세션 준비 자료  ·  오늘 {today.isoformat()}")
    tag = "직전 세션" if not asof else "**수동 지정 — 준비 중 바뀔 수 있다**"
    print(f"  기준 시점 : {end.isoformat()} (as-of · {tag})")
    print(f"  발표      : {'오늘' if dday == 0 else nxt.isoformat() + f' (D-{dday})'}")
    print("=" * 68)
    print(f"[수집 상태] {'OK ' if ok else '! '} {msg}")

    # 요청한 창과 **실제로 잡히는 스냅샷**이 다를 수 있다 — 그날 수집을 걸렀으면
    # 그 이전 것으로 대체된다. 말없이 넘어가면 "일주일치"인 줄 알고 더 긴 구간을 읽는다.
    from .query import _pick, _snapshots
    snaps = _snapshots()
    for label, want in (("시작", start), ("끝", end)):
        k = _pick(snaps, want.isoformat())
        if k is None:
            print(f"[창 경고] {label} {want} 이전 스냅샷이 없습니다.")
            continue
        got = date.fromisoformat(snaps[k].stem[len("snapshot_"):])
        if got != want:
            print(f"[창 경고] {label} {want} 스냅샷이 없어 {got}로 대체됩니다"
                  f" ({(want - got).days}일 차이 — 그날 수집이 안 돌았습니다).")

    if asof:
        print("⚠ --asof로 기준 시점을 옮겼습니다. 준비 중 자료가 **바뀔 수 있습니다** —")
        print("   다시 돌릴 때 같은 --asof를 주지 않으면 다른 자료가 나옵니다.")
        print("   보고서 첫 줄에 이 기준 시점을 반드시 적으세요.")
    else:
        print("기준 시점은 준비를 언제 하든 바뀌지 않습니다 — 수·목에 쓴 문장이 월요일에도 그대로 섭니다.")
    print()

    # ── 1. 본 재료는 '그 시점의 전체 상태'다. 변경분이 아니다
    print("─" * 68 + f"\n## 1. 기준 시점({end})의 전체 상태 — 본 재료\n" + "─" * 68)
    for line in _databook_paths(end):
        print(f"  {line}")
    print("  → 지표 328개의 값·기준일·출처·note가 전부 여기 있다. 분석은 여기서 시작한다.")
    print("     각 지표는 **저마다 다른 기준일**을 갖는다(GDP는 분기, CPI는 월, 유가는 일).")
    print("     수치를 인용할 땐 그 지표의 기준일을 반드시 함께 적는다.")

    # ── 2. 변경분은 재료가 아니라 '어디를 새로 볼지' 고르는 길잡이다
    print("\n" + "─" * 68 + f"\n## 2. 지난 한 주({start} → {end})에 바뀐 것 — 길잡이\n" + "─" * 68)
    print("# 무엇을 새로 확인할지 고르는 용도다. **이 목록만으로 글을 쓰지 않는다.**\n")
    cmd_diff(1, [], start.isoformat(), end.isoformat())

    # ── 3. 추세와 기저율은 여기서만 나온다
    print("\n" + "─" * 68 + "\n## 3. 장기 시계열 — 추세 · 기저율\n" + "─" * 68)
    _print_history()

    print("\n" + "─" * 68 + "\n## 4. 새로 뜬 기사\n" + "─" * 68)
    cmd_news([], True, limit, None)

    print("\n" + "─" * 68 + "\n## 5. 손댈 자리 (manual 슬롯 · STALE 계열)\n" + "─" * 68)
    cmd_todo("all", False, 15)

    # 창 밖 — 발표 당일 덧붙일 몫. 창을 고정한 대가를 숫자로 보여준다
    c, n, _ = window_counts(end.isoformat(), today.isoformat())
    print("\n" + "=" * 68)
    if c or n:
        print(f"[창 이후] {end} 이후 지표 {c}건 변경 · {n}건 신규 — **이번 자료엔 없습니다.**")
        print(f"  발표 당일 아침에 `python -m databook diff --since {end}` 를 돌려")
        print("  「세션 이후 변화」 한 절로 맨 앞에 덧붙이세요. 본문은 고치지 않습니다.")
    else:
        print(f"[창 이후] {end} 이후 새 변화 없음 — 덧붙일 것이 없습니다.")
    print("다음: 볼트 `_System/Prompts/시황 요청 프롬프트 (팀원용)` E-1을 붙여넣으세요.")
    print("=" * 68)
    return 0 if ok else 1
