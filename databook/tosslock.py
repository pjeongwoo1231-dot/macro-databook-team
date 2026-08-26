"""토스증권 API 단일 사용자 락 — 두 프로세스가 토큰을 서로 뺏지 않게 한다.

왜 필요한가 — 토스 토큰은 **동시에 하나만 산다.** 새로 발급하면 직전 토큰이 즉시 401이다.
그래서 `databook run`(10분)과 `databook tossback`(수 시간)이 겹치면 서로 토큰을 뺏는다.
`_get`이 401을 만나면 한 번 재발급해 복구하지만, 그건 **낭비를 줄일 뿐 없애지 못한다.**

이 모듈은 그 조율을 **사람의 기억에서 파일로 옮긴다.** 먼저 잡은 쪽이 돌고,
나중 쪽은 누가 왜 잡고 있는지 보고 즉시 물러난다.

⚠ 락은 **토스를 쓰는 구간만** 감싼다. 토스 없이 도는 다른 수집은 막지 않는다.
⚠ 죽은 프로세스가 남긴 락은 자동으로 회수한다(PID 생존 확인 + 만료 시각).
"""
from __future__ import annotations

import json
import os
import time
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

from .core import OUTPUT_DIR

LOCK = OUTPUT_DIR / ".tossinvest.lock"
DEFAULT_TTL = 6 * 3600      # 이보다 오래된 락은 죽은 것으로 본다


def _alive(pid: int) -> bool:
    """PID가 아직 살아 있나. Windows·POSIX 둘 다에서 동작하는 최소한의 확인."""
    if pid <= 0:
        return False
    if os.name == "nt":
        import subprocess
        try:
            out = subprocess.run(["tasklist", "/FI", f"PID eq {pid}", "/NH"],
                                 capture_output=True, text=True, timeout=10).stdout
            return str(pid) in out
        except Exception:
            return True      # 확인 실패 시엔 살아 있다고 본다 — 남의 작업을 뺏는 쪽이 더 나쁘다
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def read_lock() -> dict | None:
    if not LOCK.exists():
        return None
    try:
        return json.loads(LOCK.read_text(encoding="utf-8"))
    except Exception:
        return None


def _stale(info: dict, ttl: int) -> bool:
    if time.time() - float(info.get("ts", 0)) > ttl:
        return True
    return not _alive(int(info.get("pid", 0)))


@contextmanager
def toss_lock(owner: str, ttl: int = DEFAULT_TTL, wait: float = 0.0, quiet: bool = False):
    """토스 API 사용 구간을 감싼다.

    성공하면 True, 남이 쓰고 있으면 False를 넘긴다 — **예외를 던지지 않는다.**
    호출자가 "건너뛰고 나머지는 계속"을 고를 수 있어야 하기 때문이다.

    wait > 0이면 그 초만큼 기다려 본 뒤 포기한다.
    """
    deadline = time.monotonic() + wait
    held = False
    while True:
        info = read_lock()
        if info is None or _stale(info, ttl):
            LOCK.parent.mkdir(parents=True, exist_ok=True)
            LOCK.write_text(json.dumps({
                "owner": owner, "pid": os.getpid(), "ts": time.time(),
                "started": datetime.now().isoformat(timespec="seconds"),
            }, ensure_ascii=False), encoding="utf-8")
            # 경합 시 마지막에 쓴 쪽이 이긴다 — 내 것이 맞는지 되읽어 확인한다
            back = read_lock() or {}
            if back.get("pid") == os.getpid():
                held = True
                break
        if time.monotonic() >= deadline:
            break
        time.sleep(1.0)

    if not held and not quiet:
        info = read_lock() or {}
        print(f"  [토스 건너뜀] 다른 작업이 토스 API를 쓰는 중 — "
              f"{info.get('owner', '?')} (pid {info.get('pid', '?')}, {info.get('started', '?')} 시작)")
        print(f"              끝난 뒤 다시 돌리거나, 확실히 죽었으면 {LOCK} 삭제")
    try:
        yield held
    finally:
        if held:
            try:
                cur = read_lock() or {}
                if cur.get("pid") == os.getpid():
                    LOCK.unlink(missing_ok=True)
            except Exception:
                pass
