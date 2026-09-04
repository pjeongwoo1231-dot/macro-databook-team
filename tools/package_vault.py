"""주간 배포본(ZIP) 빌더 — 팀 안내가 약속한 '주 1회 ZIP 스냅샷'을 실제로 만든다.

2026-09-02에 배포 채널이 **옵시디언 싱크 → 주 1회 ZIP(구글드라이브)**로 바뀌었는데
만드는 쪽이 없었다. 그래서 팀원은 자료가 갱신되지 않았고, `weekly`는 스냅샷을 못 찾아
"배치가 한 번도 돌지 않았다"를 띄웠다. 이 스크립트가 그 빈자리다.

**무엇을 넣고 무엇을 빼나 — 용량이 아니라 쓸모로 정한다.**

넣는다
    04_DataBook/           지표 333개 · 스냅샷 .json · 팀별 노트      18MB
    04_DataBook/history/   장기 시계열 180계열 (추세·기저율의 유일한 출처)  9.9MB
    02_Papers 05_Library 04_Zettel 03_MOC 01_Indicators …  노트 전부  14MB
    06_SourceArchive/**.md 원문 정리 노트 1,509건                    5.6MB
    _System/docs _System/Prompts _System/Templates  운영 규칙·프롬프트

뺀다
    history/toss/          593MB — 종목 패널 4,300개. 허용 IP 문제로 수집도 안 된다
    06_SourceArchive/*.pdf 원문 PDF 95건 — 구글드라이브 별도 폴더로 간다(안내대로)
    _System/backup _System/Analysis  백업·분석 스크립트 221MB 대부분
    Attachments/           57MB
    .obsidian/ .git/ __pycache__/

기준일은 **볼트의 최신 스냅샷 날짜**로 박는다 — 빌드한 날이 아니라. 팀원이 파일명만
보고 "언제 자료인가"를 알 수 있어야 하고, 그게 인용 기준일이 된다.

사용:  python _System/package_vault.py            # 볼트 옆에 dist/ 로 만든다
       python _System/package_vault.py --out D:/드라이브/제출함
"""
from __future__ import annotations

import argparse
import fnmatch
import shutil
import sys
import zipfile
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _default_vault() -> Path:
    """볼트 위치. **이 스크립트는 저장소에 산다**(버전관리를 받아야 하니까).

    예전엔 볼트 안(`_System/`)에만 있어서 볼트가 날아가면 빌드 수단도 같이 날아갔다.
    지금은 저장소가 정본이고, 빌드할 때 자기 자신을 ZIP의 `_System/`에 넣어 준다 —
    배포본을 받은 사람도 다시 쌀 수 있다.
    """
    import os
    v = os.environ.get("OBSIDIAN_VAULT_PATH", "").strip().strip('"')
    if not v:
        env = HERE.parent / ".env"
        if env.exists():
            for line in env.read_text(encoding="utf-8", errors="replace").splitlines():
                if line.strip().startswith("OBSIDIAN_VAULT_PATH") and "=" in line:
                    v = line.split("=", 1)[1].strip().strip('"')
                    break
    if v:
        return Path(v).expanduser()
    # 옛 자리(볼트 안 `_System/`)에서 돌린 경우
    return HERE.parent


VAULT = _default_vault()

# 통째로 빼는 경로 (볼트 루트 기준, 접두사 일치)
EXCLUDE_DIRS = (
    "Attachments",
    "_System/backup",
    "_System/Analysis",
    "_System/paper-autopilot",
    "_System/readingpilot",
    "04_DataBook/_archive",
    "graphify-out",
    # 볼트 안에 볼트가 들어앉는 경우가 실제로 있다(2026-09-04: OneDrive가 클라우드의
    # 중복본을 `MacroVault/MacroVault/`로 내려받는 중이었다). 걸러내지 않으면
    # 배포본이 두 배가 되고, 받은 사람은 어느 쪽이 진짜인지 알 수 없다.
    "MacroVault",
    "MacroVault_dist",
    # `DATABOOK_OUTPUT_DIR`이 볼트를 가리킨 채 `run`이 돌면 수집 산출물이 볼트 안에
    # `Macro/`로 떨어진다. 발행 가드(publish.py)는 `04_DataBook/`만 지키므로 이 경로는
    # 그냥 통과한다 — 2026-09-04에 키 없는 런의 168/333짜리가 실제로 여기 남아 있었다.
    "Macro",
)
# 어디에 있든 빼는 폴더명
EXCLUDE_ANY = {".obsidian", ".git", ".trash", "__pycache__", ".DS_Store",
               ".smart-env", ".smart-connections", ".makemd", ".space"}
# 확장자로 빼는 것 (노트가 아니라 원문·바이너리)
EXCLUDE_EXT = {".pdf", ".epub", ".mobi", ".zip", ".7z", ".mp4", ".xlsx", ".pptx",
               ".ajson"}  # .ajson = Smart Connections 임베딩 캐시 545MB — 받는 쪽에서 다시 만든다

HISTORY_SRC_HINT = "DATABOOK_OUTPUT_DIR"


def _excluded(rel: Path) -> bool:
    parts = rel.parts
    if any(p in EXCLUDE_ANY for p in parts):
        return True
    s = rel.as_posix()
    if any(s == d or s.startswith(d + "/") for d in EXCLUDE_DIRS):
        return True
    if rel.suffix.lower() in EXCLUDE_EXT:
        return True
    return False


def _asof(vault: Path) -> str:
    """배포본 기준일 = 볼트 최신 스냅샷 날짜. 빌드일이 아니다."""
    snaps = sorted((vault / "04_DataBook" / "snapshots").glob("snapshot_*.json"))
    if not snaps:
        sys.exit("[중단] 04_DataBook/snapshots 가 비어 있습니다 — 배포할 기준일이 없습니다.")
    return snaps[-1].stem[len("snapshot_"):]


def _history_dir() -> Path | None:
    """장기 시계열 원본. 수집기의 OUTPUT_DIR/history 를 찾는다."""
    import os
    v = os.environ.get(HISTORY_SRC_HINT, "").strip()
    if not v:
        env = VAULT.parent / "macro-databook-team" / ".env"
        for cand in (env,):
            if cand.exists():
                for line in cand.read_text(encoding="utf-8", errors="replace").splitlines():
                    if line.strip().startswith(HISTORY_SRC_HINT) and "=" in line:
                        v = line.split("=", 1)[1].strip()
    if not v:
        v = str(Path.home() / "macro-data" / "output")
    d = Path(v).expanduser() / "history"
    return d if d.is_dir() else None


def build(vault: Path, out_dir: Path, dry: bool = False) -> Path:
    asof = _asof(vault)
    out_dir.mkdir(parents=True, exist_ok=True)
    zip_path = out_dir / f"MacroVault_{asof}.zip"

    # **볼트는 살아 있는 폴더다.** Obsidian이 열려 있거나 플러그인이 캐시를 쓰는 중이면
    # rglob이 준 경로가 stat 시점엔 이미 사라져 있을 수 있다(2026-09-04에 실제로 겪었다).
    # 그때 죽으면 월요일 배치 전체가 멈춘다 — 배포본은 사라진 파일 하나보다 중요하다.
    files: list[tuple[Path, str, int]] = []
    vanished = 0
    for f in vault.rglob("*"):
        try:
            if not f.is_file():
                continue
            rel = f.relative_to(vault)
            if _excluded(rel):
                continue
            files.append((f, rel.as_posix(), f.stat().st_size))
        except OSError:
            vanished += 1

    # 장기 시계열은 볼트 밖에 있다 — 04_DataBook/history/ 로 끌어온다 (toss/ 제외)
    hist = _history_dir()
    n_hist = 0
    if hist:
        for f in sorted(hist.glob("*.csv")):
            try:
                files.append((f, f"04_DataBook/history/{f.name}", f.stat().st_size))
                n_hist += 1
            except OSError:
                vanished += 1
    else:
        print("[경고] history/ 를 못 찾았습니다 — §3(추세·기저율)이 빠진 배포본이 됩니다.")

    # 빌드 도구를 배포본 안에 같이 넣는다 — 받은 사람도 다시 쌀 수 있어야 한다.
    # (저장소가 정본이므로 볼트에 낡은 사본이 남아 있어도 이게 덮는다.)
    for tool in ("package_vault.py", "build_citation_index.py"):
        t = HERE / tool
        if t.exists():
            files = [e for e in files if e[1] != f"_System/{tool}"]
            files.append((t, f"_System/{tool}", t.stat().st_size))

    total = sum(sz for _, _, sz in files)
    print(f"기준일 {asof} · 파일 {len(files):,}개 · 원본 {total / 1048576:.1f} MB "
          f"(장기 시계열 {n_hist}계열 포함)")
    if vanished:
        print(f"[알림] 스캔 중 사라진 파일 {vanished}개를 건너뛰었습니다 "
              f"(Obsidian이 열려 있으면 정상입니다).")
    if dry:
        for _, arc, _ in files[:15]:
            print("   ", arc)
        print(f"    … 외 {len(files) - 15:,}개")
        return zip_path

    # ZIP 안의 최상위 폴더는 **날짜 없이 고정**한다. 날짜를 넣으면 압축 푼 폴더명이
    # 매주 바뀌고, 팀원이 `.env`의 OBSIDIAN_VAULT_PATH를 매주 고쳐야 한다.
    # 기준일은 ZIP 파일명과 `04_DataBook/snapshots/`가 이미 들고 있다 —
    # `weekly`도 거기서 읽어 "배포본 <날짜> 기준"으로 찍어 준다.
    tmp = zip_path.with_suffix(".zip.part")
    skipped = 0
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for f, arc, _ in files:
            try:
                z.write(f, f"MacroVault/{arc}")
            except OSError:
                skipped += 1   # 목록을 만든 뒤에도 사라질 수 있다
    if skipped:
        print(f"[알림] 쓰는 중 사라진 파일 {skipped}개를 건너뛰었습니다.")
    tmp.replace(zip_path)
    print(f"→ {zip_path}  ({zip_path.stat().st_size / 1048576:.1f} MB)")
    return zip_path


def main() -> int:
    ap = argparse.ArgumentParser(description="주간 배포본 ZIP 빌더")
    ap.add_argument("--out", default=str(VAULT.parent / "MacroVault_dist"),
                    help="ZIP을 놓을 폴더 (기본: 볼트 옆 MacroVault_dist)")
    ap.add_argument("--dry-run", action="store_true", help="넣을 목록만 보고 만들지 않는다")
    a = ap.parse_args()
    build(VAULT, Path(a.out).expanduser(), a.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
