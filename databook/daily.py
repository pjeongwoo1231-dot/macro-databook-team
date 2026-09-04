"""일일 배치 — 스냅샷 성격 데이터를 매일 쌓는다.

**왜 필요한가**: `sectors`와 `lending`은 그날 상태만 준다. 과거를 소급해 받을 수 없으므로
**돌리지 않은 날은 영영 빈칸으로 남는다.** FRED 계열처럼 나중에 몰아 받는 게 불가능하다.

실행 순서와 이유
1. `run`     — Data Book 214개 지표 + Obsidian vault 출력
2. `sectors` — 업종 등락·시총가중 외국인 지분율 (스냅샷, 소급 불가)
3. `lending` — 대차잔고 (T+1 공개라 어제치를 받는다)
4. `history` — FRED·Yahoo 증분 + GPR 전이력 (소급 가능하지만 매일 받아두면 빠르다)
5. `tossback` — 토스 시장계열 증분. **1분봉이 여기 걸려 있는 게 핵심이다** —
   토스 1분봉은 보관이 약 8영업일뿐이라 **안 돌린 날은 영영 빈칸**이다(sectors·lending과 같은 성격).
   지수·국채 일봉과 환율은 소급되지만 같이 받아둔다. 종목 패널(4,300개)은 여기 넣지 않는다 —
   수 시간짜리라 일일 배치를 막는다. 그건 `tossback --what stocks`로 따로 돌린다.

`events`·`fedtext`·`topics`·`earnings`는 매일 돌릴 필요가 없어 제외했다.
"""
from __future__ import annotations

import time
from datetime import datetime
from pathlib import Path

from .core import OUTPUT_DIR

LOG = OUTPUT_DIR / "daily.log"

STEPS: list[tuple[str, str, list[str]]] = [
    # consensus는 run보다 먼저 — FairEconomy는 롤링 1주만 제공하므로 forecast는 발표 전에
    # 적립해둬야 한다. 이번 주 값을 놓치면 그 주 서프라이즈는 영영 계산할 수 없다.
    ("consensus", "컨센서스 캘린더 적립 (발표 전 forecast 확보)", []),
    ("run", "Data Book 전체 수집", []),
    ("sectors", "업종 등락·외국인 지분율", []),
    ("lending", "대차잔고", ["--days", "5"]),
    ("history", "FRED·Yahoo 증분 + GPR 전이력", []),
    ("tossback", "토스 시장계열 증분(1분봉 포함)", ["--what", "market"]),
    ("intel", "정보 수집 (API·RSS, 검색엔진 미사용)", []),
    ("vintage", "빈티지 인덱스 재구성 (개정 이력)", []),
    ("unitcheck", "단위 정합성 검사", []),
    ("site", "시황 사이트 재생성", []),
    # 배포본은 **월요일에만** 싼다 — 세션이 화요일이라 그 전날 것이 그 주의 정본이 된다.
    # 매일 싸면 팀원이 어느 ZIP을 봐야 할지 몰라 기준일이 갈린다(그게 인용 사고의 씨앗이다).
    ("package", "주간 배포본 ZIP (월요일만)", []),   # 항상 마지막 — 위 단계 결과를 굳힌다
]


def _log(msg: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    line = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  {msg}"
    print(line)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def run(skip: list[str] | None = None) -> int:
    skip = skip or []
    _log(f"=== 일일 배치 시작 (건너뜀: {skip or '없음'}) ===")
    failed = []
    for cmd, label, extra in STEPS:
        if cmd in skip:
            _log(f"[SKIP] {cmd} — {label}")
            continue
        t0 = time.time()
        try:
            rc = _dispatch(cmd, extra)
        except Exception as e:
            rc = 1
            _log(f"[FAIL] {cmd} — {type(e).__name__}: {e}")
        dt = time.time() - t0
        if rc == 0:
            _log(f"[OK  ] {cmd:9s} {label} ({dt:.0f}초)")
        else:
            failed.append(cmd)
            _log(f"[FAIL] {cmd:9s} {label} (rc={rc}, {dt:.0f}초)")
    _log(f"=== 종료 · 실패 {len(failed)}건 {failed or ''} ===")
    return 1 if failed else 0


def _dispatch(cmd: str, extra: list[str]) -> int:
    """하위 프로세스를 띄우지 않고 직접 호출한다 — venv 경로 문제를 피한다."""
    if cmd == "run":
        import sys

        from . import derived
        from .core import all_indicators, load_env, load_registry
        from .fetchers import fetch_indicator
        from .render import now_utc, render_markdown, render_snapshot
        registry, env = load_registry(), load_env()
        results, queue = [], []
        for ind in all_indicators(registry):
            res = fetch_indicator(ind, env)
            if res["status"] == "derived_pending":
                queue.append(ind)
                continue
            results.append(res)
        for ind in queue:
            results.append(derived.compute(ind, results))
        results.extend(derived.extra_derived(results))
        ts = now_utc()
        render_markdown(results, ts, env)
        render_snapshot(results, ts, env)
        ok = sum(1 for r in results if r["status"] == "ok")
        _log(f"       수집 성공 {ok}/{len(results)}")
        return 0
    if cmd == "package":
        # 볼트를 통째로 싸서 팀원에게 줄 ZIP을 만든다. 월요일이 아니면 아무것도 안 한다.
        # (`DATABOOK_PACKAGE_ALWAYS=1`이면 요일 무시 — 급히 다시 배포할 때 쓴다)
        import os
        from datetime import date
        if date.today().weekday() != 0 and not os.environ.get("DATABOOK_PACKAGE_ALWAYS"):
            _log("       월요일이 아니라 건너뜀 (강제: DATABOOK_PACKAGE_ALWAYS=1)")
            return 0
        from .core import load_env
        v = (load_env().get("OBSIDIAN_VAULT_PATH") or "").strip().strip('"')
        if not v:
            _log("       OBSIDIAN_VAULT_PATH가 없어 건너뜀 — 배포본을 만들 볼트가 없다")
            return 0
        script = Path(v) / "_System" / "package_vault.py"
        if not script.exists():
            _log(f"       {script} 없음 — 볼트에 패키저가 없다")
            return 1
        import runpy
        import sys
        dist = os.environ.get("DATABOOK_DIST_DIR", "").strip() or str(Path(v).parent / "MacroVault_dist")
        argv = sys.argv
        sys.argv = [str(script), "--out", dist]
        try:
            runpy.run_path(str(script), run_name="__main__")
        except SystemExit as e:
            if e.code not in (0, None):
                return int(e.code or 1)
        finally:
            sys.argv = argv
        _log(f"       배포본 → {dist}")
        return 0

    if cmd == "consensus":
        from .consensus import run as f
        return f()

    if cmd == "vintage":
        from .vintage import run as f
        return f(top=8)

    if cmd == "unitcheck":
        from .unitcheck import run as f
        return f()

    if cmd == "sectors":
        from .sectors import collect
        return collect()
    if cmd == "lending":
        from .lending import collect
        days = int(extra[1]) if len(extra) > 1 else 5
        return collect(days=days)
    if cmd == "history":
        from .history import collect
        return collect()
    if cmd == "intel":
        from .intel import collect
        return collect()
    if cmd == "site":
        from .site import build
        return build(quiet=True)
    if cmd == "tossback":
        from .tossback import collect
        what = extra[1] if len(extra) > 1 else "market"
        # 종목 백필이 돌고 있으면 락에 막혀 rc=1이 온다 — 그건 실패가 아니라 '나중에'다
        rc = collect(what=what)
        if rc != 0:
            _log("       토스 건너뜀 — 백필이 토큰을 쓰는 중(락). 백필 종료 후 따로 돌릴 것")
            return 0
        return 0
    return 1
