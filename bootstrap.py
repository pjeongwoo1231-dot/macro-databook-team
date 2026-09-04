"""팀원 1인 설치기 — 이거 하나만 돌리면 `weekly`·`show`·`diff`가 된다.

    python bootstrap.py

**API 키는 하나도 필요 없다.** 이 스크립트가 하는 일은 넷뿐이다:

    1. 파이썬 버전 확인
    2. 의존성 설치 (PyYAML · feedparser — 조회에 필요한 건 이 둘뿐이다)
    3. 최신 배포본 ZIP을 GitHub Releases에서 받아 `~/MacroVault` 에 푼다
    4. `.env`에 볼트 경로를 적고, 실제로 `weekly`를 돌려 **되는지 확인한다**

**다시 돌려도 안전하다.** 매주 이걸 돌리면 배포본만 최신으로 갈린다(`--update`와 같다).
`.env`의 다른 항목은 건드리지 않는다 — 수집 담당자가 돌려도 키가 날아가지 않는다.

왜 스크립트인가 — 예전엔 안내 문서만 고치고 실제 수단을 안 붙여서 팀원 자료가 두 번
멈췄다(옵시디언 싱크 → 구글드라이브 → 실체 없음). 문서는 읽는 사람마다 다르게 실행되고,
틀렸을 때 아무도 모른다. 스크립트는 틀리면 그 자리에서 죽는다.

옵션
    --vault <경로>   볼트를 풀 위치 (기본: ~/MacroVault)
    --no-verify      마지막 확인 실행을 건너뛴다
    --full           requirements.txt 전부 설치 (수집까지 돌릴 사람만)
"""
from __future__ import annotations

import argparse
import io
import json
import os
import shutil
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = "pjeongwoo1231-dot/macro-databook-team"
API = f"https://api.github.com/repos/{REPO}/releases/latest"
QUERY_DEPS = ["PyYAML>=6.0", "feedparser>=6.0"]   # 조회 경로가 쓰는 전부
MIN_PY = (3, 10)


def say(step: str, msg: str) -> None:
    print(f"[{step}] {msg}", flush=True)


def die(msg: str, fix: str = "") -> None:
    print(f"\n[중단] {msg}", file=sys.stderr)
    if fix:
        print(f"       {fix}", file=sys.stderr)
    raise SystemExit(1)


# ── 1. 파이썬 ────────────────────────────────────────────────────────────
def check_python() -> None:
    if sys.version_info < MIN_PY:
        die(f"파이썬 {'.'.join(map(str, MIN_PY))} 이상이 필요합니다 "
            f"(지금 {sys.version.split()[0]}).",
            "https://www.python.org/downloads/ 에서 최신판을 설치하세요.")
    say("1/4", f"파이썬 {sys.version.split()[0]} OK")


# ── 2. 의존성 ────────────────────────────────────────────────────────────
def install_deps(full: bool) -> None:
    if full:
        req = ROOT / "requirements.txt"
        if not req.exists():
            die(f"{req} 가 없습니다.", "저장소 안에서 돌리고 있는지 확인하세요.")
        args = ["-r", str(req)]
        what = "requirements.txt 전부"
    else:
        args = QUERY_DEPS
        what = " · ".join(QUERY_DEPS)
    say("2/4", f"의존성 설치 — {what}")
    r = subprocess.run([sys.executable, "-m", "pip", "install", "-q", *args],
                       capture_output=True, text=True)
    if r.returncode != 0:
        die(f"pip 설치 실패:\n{r.stderr.strip()[-800:]}",
            "회사·학교망이면 프록시 때문일 수 있습니다. 개인 네트워크에서 다시 시도하세요.")


# ── 3. 배포본 ────────────────────────────────────────────────────────────
def fetch_release() -> tuple[str, bytes]:
    """최신 릴리스의 ZIP을 받는다. 공개 저장소라 토큰이 필요 없다."""
    say("3/4", "최신 배포본 확인 중…")
    try:
        with urllib.request.urlopen(API, timeout=30) as r:
            meta = json.load(r)
    except Exception as e:
        die(f"릴리스 정보를 못 받았습니다 ({type(e).__name__}: {e}).",
            f"브라우저로 https://github.com/{REPO}/releases/latest 가 열리는지 보세요.")
    # 릴리스에는 자산이 둘이다 — 볼트 배포본(`MacroVault_<날짜>.zip`)과
    # 이 스크립트가 들어 있던 클라이언트(`macro-databook-client.zip`).
    # **이름으로 골라야 한다.** 순서로 고르면 자산이 늘어날 때 조용히 엉뚱한 걸 받는다
    # (실제로 클라이언트를 추가한 날 그렇게 깨졌다).
    assets = [a for a in meta.get("assets", [])
              if a["name"].startswith("MacroVault_") and a["name"].endswith(".zip")]
    if not assets:
        names = [a["name"] for a in meta.get("assets", [])]
        die(f"릴리스에 볼트 배포본(MacroVault_*.zip)이 없습니다. 있는 자산: {names}",
            "수집 담당자에게 배포본이 올라갔는지 물어보세요.")
    a = sorted(assets, key=lambda x: x["name"])[-1]
    mb = a["size"] / 1048576
    say("3/4", f"{a['name']} ({mb:.1f} MB) 내려받는 중…")
    try:
        with urllib.request.urlopen(a["browser_download_url"], timeout=300) as r:
            blob = r.read()
    except Exception as e:
        die(f"내려받기 실패 ({type(e).__name__}: {e}).", "네트워크를 확인하고 다시 돌리세요.")
    return a["name"], blob


MARKER = ".databook-dist"   # 이 스크립트가 만든 배포본임을 표시한다


def extract(blob: bytes, vault: Path) -> Path:
    """ZIP을 푼다. 최상위는 항상 `MacroVault/` 로 고정돼 있다.

    ⚠ **지우기 전에 우리가 만든 것인지 확인한다.** 배포본은 읽기용 사본이라 통째로
    갈아끼우는 게 맞지만, `--vault`를 잘못 준 사람의 폴더까지 지우면 안 된다.
    그래서 `.databook-dist` 표시가 있을 때만 지운다. 표시가 없는 폴더가 이미 있으면
    **아무것도 지우지 않고 멈춘다** — 이 경우 사람이 판단해야 한다.

    (섞어서 풀지 않는 이유: 지난주에 삭제된 노트가 남아 '있는데 왜 안 보이지'가 된다.)
    """
    z = zipfile.ZipFile(io.BytesIO(blob))
    tops = {n.split("/")[0] for n in z.namelist()}
    if tops != {"MacroVault"}:
        die(f"ZIP 최상위가 예상과 다릅니다: {sorted(tops)}",
            "배포본이 잘못 만들어졌습니다 — 수집 담당자에게 알려주세요.")

    if vault.exists():
        if any(vault.iterdir()) and not (vault / MARKER).exists():
            die(f"{vault} 에 이미 내용이 있는데 배포본 표시({MARKER})가 없습니다.",
                "실수로 다른 폴더를 지정했을 수 있어 **아무것도 지우지 않았습니다.**\n"
                "       비어 있는 새 폴더를 --vault 로 주거나, 이 폴더가 정말 배포본이면\n"
                "       직접 지운 뒤 다시 돌리세요.")
        say("3/4", f"기존 배포본을 지우고 다시 풉니다 — {vault}")
        shutil.rmtree(vault)

    vault.parent.mkdir(parents=True, exist_ok=True)
    # 임시 폴더에 풀고 마지막에 옮긴다 — 중간에 끊겨도 반쪽 볼트가 남지 않는다.
    staging = vault.parent / f".{vault.name}.part"
    if staging.exists():
        shutil.rmtree(staging)
    z.extractall(staging)
    (staging / "MacroVault" / MARKER).write_text(
        "이 폴더는 bootstrap.py가 만든 배포본 사본입니다. 여기서 고친 내용은\n"
        "다음 실행에서 사라집니다. 작성한 것은 제출함에 올리세요.\n",
        encoding="utf-8")
    (staging / "MacroVault").rename(vault)
    shutil.rmtree(staging, ignore_errors=True)
    return vault


# ── 4. .env ──────────────────────────────────────────────────────────────
def write_env(vault: Path) -> None:
    """OBSIDIAN_VAULT_PATH만 갱신한다. **다른 줄은 그대로 둔다.**

    수집 담당자가 이걸 돌려도 API 키가 날아가면 안 된다.
    """
    p = ROOT / ".env"
    lines = p.read_text(encoding="utf-8", errors="replace").splitlines() if p.exists() else []
    key = "OBSIDIAN_VAULT_PATH"
    new = f"{key}={vault}"
    for i, line in enumerate(lines):
        if line.strip().startswith(key) and "=" in line:
            lines[i] = new
            break
    else:
        if lines and lines[-1].strip():
            lines.append("")
        lines.append("# 배포본 볼트 — bootstrap.py 가 적었습니다")
        lines.append(new)
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    say("4/4", f".env 에 볼트 경로 기록 — {vault}")


# ── 확인 ─────────────────────────────────────────────────────────────────
def verify() -> int:
    """실제로 돌려 본다. **설치했다고 말하려면 되는 걸 봐야 한다.**"""
    print("\n" + "─" * 60)
    print("확인 — `python -m databook weekly` 앞부분")
    print("─" * 60)
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    r = subprocess.run([sys.executable, "-m", "databook", "weekly"],
                       cwd=str(ROOT), capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=env)
    out = (r.stdout or "") + (r.stderr or "")
    for line in out.splitlines()[:10]:
        print("  " + line)
    if "[수집 상태]" not in out:
        print("\n[경고] weekly가 정상 출력을 내지 않았습니다. 전체 출력:", file=sys.stderr)
        print(out[-1500:], file=sys.stderr)
        return 1
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="macro-databook 팀원 설치기")
    ap.add_argument("--vault", default=str(Path.home() / "MacroVault"),
                    help="배포본을 풀 위치 (기본: ~/MacroVault)")
    ap.add_argument("--no-verify", action="store_true", help="확인 실행 생략")
    ap.add_argument("--full", action="store_true",
                    help="requirements.txt 전부 설치 (직접 수집까지 돌릴 사람)")
    a = ap.parse_args()

    print("macro-databook 설치 — API 키는 필요 없습니다\n")
    check_python()
    install_deps(a.full)
    name, blob = fetch_release()
    vault = extract(blob, Path(a.vault).expanduser().resolve())
    write_env(vault)

    rc = 0 if a.no_verify else verify()
    print("\n" + "═" * 60)
    if rc == 0:
        print(f"설치 완료 — 배포본 {name}")
        print(f"  볼트    : {vault}")
        print(f"  Obsidian: '다른 폴더를 볼트로 열기' → {vault}")
        print(f"            열리면 '팀 안내 (먼저 읽기).md' 부터 보세요")
        print("\n  자주 쓰는 것")
        print("    python -m databook weekly            세션 준비 자료 한 번에")
        print("    python -m databook show 중국 PPI     지표 하나 찾아보기")
        print("    python -m databook diff              지난 스냅샷 대비 바뀐 것")
        print("\n  다음 주에는 `python bootstrap.py` 를 다시 돌리면 배포본만 갱신됩니다.")
    else:
        print("설치는 됐지만 확인 실행이 이상합니다 — 위 출력을 그대로 담당자에게 보내세요.")
    print("═" * 60)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
