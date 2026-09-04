"""조회용 클라이언트 ZIP 빌더 — 팀원이 `git clone` 없이 받게 한다.

**왜 필요한가.** 이 저장소는 `.git` 2.5GB · `docs/` 857MB(PDF 575개)다. 팀원은
그걸 받을 이유가 하나도 없는데, 더 나쁜 건 **Windows에서 clone 자체가 실패한다**는 것이다:

    error: unable to create file docs/library/... .pdf: Filename too long

`docs/library/`의 논문 PDF 파일명이 260자(MAX_PATH)를 넘어 체크아웃이 깨진다.
`--depth 1`도 소용없다 — 실패 지점이 전송이 아니라 **체크아웃**이라서다.
즉 SETUP.md가 시키던 `git clone`은 팀원 전원의 1단계에서 막혔다.

그래서 조회에 필요한 것만 따로 싼다 — 약 1MB, git도 긴 경로도 필요 없다.

    python tools/package_client.py --out <폴더>

담당자(수집까지 돌리는 1명)는 여전히 전체 clone이 필요하다. 그 사람은
`git config --global core.longpaths true` 를 먼저 켜야 한다.
"""
from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOP = "macro-databook-client"

# 조회 경로(`weekly`·`show`·`diff`·`todo`)가 실제로 쓰는 것만.
# 수집용 fetcher까지 포함하는 이유는 `databook` 패키지가 통째로 import되기 때문이다 —
# 코드는 다 합쳐 1MB 미만이라 쪼개서 얻는 게 없다.
INCLUDE_FILES = ("indicators.yaml", "requirements.txt", "bootstrap.py", "SETUP.md")
INCLUDE_DIRS = ("databook",)
SKIP_PARTS = {"__pycache__", ".git"}


def collect() -> list[tuple[Path, str]]:
    out: list[tuple[Path, str]] = []
    for name in INCLUDE_FILES:
        p = ROOT / name
        if p.exists():
            out.append((p, name))
        else:
            print(f"[경고] {name} 없음 — 클라이언트가 불완전해집니다.")
    for d in INCLUDE_DIRS:
        base = ROOT / d
        for f in sorted(base.rglob("*")):
            if not f.is_file() or set(f.parts) & SKIP_PARTS:
                continue
            # 수집 PC에는 손으로 고치며 남긴 `.bak-<날짜>` 사본이 쌓여 있다(17건 실측).
            # 팀원에게 나갈 이유가 없고, 나가면 어느 게 진짜인지 헷갈린다.
            if f.suffix in (".pyc", ".pyo") or ".bak" in f.name:
                continue
            out.append((f, f.relative_to(ROOT).as_posix()))
    return out


def build(out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    zip_path = out_dir / f"{TOP}.zip"
    files = collect()
    total = sum(f.stat().st_size for f, _ in files)
    tmp = zip_path.with_suffix(".zip.part")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for f, arc in files:
            z.write(f, f"{TOP}/{arc}")
    tmp.replace(zip_path)
    print(f"클라이언트 {len(files)}개 · 원본 {total / 1024:.0f} KB "
          f"→ {zip_path} ({zip_path.stat().st_size / 1024:.0f} KB)")
    return zip_path


def main() -> int:
    ap = argparse.ArgumentParser(description="조회용 클라이언트 ZIP 빌더")
    ap.add_argument("--out", default=str(ROOT.parent / "MacroVault_dist"),
                    help="ZIP을 놓을 폴더 (기본: 저장소 옆 MacroVault_dist)")
    build(Path(ap.parse_args().out).expanduser())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
