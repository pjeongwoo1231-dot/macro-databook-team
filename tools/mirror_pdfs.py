"""원문 PDF 미러 — 볼트의 PDF를 구글드라이브 폴더로 복사한다.

주간 ZIP(GitHub Releases)은 노트만 싣고 PDF를 전부 뺀다(16MB vs 1.6GB). 그 빠진 절반이
여기로 간다. 2026-09에 "PDF는 구글드라이브 별도 폴더로"라고 문서에만 쓰고 만들지 않아
팀원이 원문을 못 받았다 — 이 스크립트가 그 실체다.

**경로를 볼트와 똑같이 둔다.** 드라이브 폴더 안이
    06_SourceArchive/06-BIS-Archive-Catalog/PDFs/xxx.pdf
    Attachments/KIEP/yyy.pdf
처럼 볼트 상대경로 그대로라서, 팀원이 받아 MacroVault 폴더에 **덮어 합치기만 하면**
노트의 PDF 링크가 그대로 열린다.

무엇을 보내나
    06_SourceArchive/**.pdf   BIS 1,373편 + 1차 원문 · 기사캡처
    Attachments/**.pdf        KIEP · 고전 등 노트 첨부
안 보낸다
    _System/**                backup(중복본)·Analysis 캐시 — 원문이 아니다

**드라이브 쪽은 지우지 않는다.** 볼트에서 파일을 옮기거나 지워도 미러에는 남는다.
볼트 규약이 "삭제 대신 이동"이고, 미러가 뭔가를 지우면 팀원 쪽에서 복구할 길이 없다.

사용:  python tools/mirror_pdfs.py --vault C:/Users/test/Documents/MacroVault
       python tools/mirror_pdfs.py --vault ... --dest "G:/내 드라이브/MacroVault-PDF" --dry-run
환경변수 DATABOOK_PDF_MIRROR 로 대상 폴더를 바꿀 수 있다.
"""
from __future__ import annotations

import argparse
import csv
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

DEFAULT_DEST = Path("G:/내 드라이브/MacroVault-PDF")
INCLUDE = ("06_SourceArchive", "Attachments")
EXT = {".pdf"}

README = """# MacroVault 원문 PDF

매크로 학회 공용 볼트의 **원문 PDF**입니다. 노트(주간 ZIP)와 짝입니다.

- 노트 ZIP: https://github.com/pjeongwoo1231-dot/macro-databook-team/releases/latest
- 이 폴더: 노트에 링크된 PDF 원본 ({n:,}편 · {mb:,.0f} MB · {stamp} 갱신)

## 쓰는 법

이 폴더의 하위 폴더(`06_SourceArchive`, `Attachments`)를 **MacroVault 폴더에 그대로 덮어 합치세요.**
경로가 볼트와 똑같아서 Obsidian 노트의 PDF 링크가 바로 열립니다.
전부 받을 필요는 없습니다 — 필요한 하위 폴더만 받아도 그 부분 링크는 동작합니다.

- `06_SourceArchive/06-BIS-Archive-Catalog/PDFs` — BIS 워킹페이퍼 원문 (공개 자료)
- `06_SourceArchive/05-Primary-PDFs` — 1차 원문 (학술지 PDF 포함 — **외부 재배포 금지**)
- `Attachments` — 노트 첨부 (KIEP · 거시 고전 등)

PDF가 있다고 인용해도 되는 것은 아닙니다. 인용 가능 여부는 노트 ZIP의
`03_MOC/인용 가능 인덱스.md`(릴리스의 `citation-index.md`)가 정합니다.

목록: `manifest.csv` · 이 폴더는 매주 월요일 배치가 자동으로 갱신합니다.
"""


def collect(vault: Path) -> list[tuple[Path, str]]:
    out: list[tuple[Path, str]] = []
    for top in INCLUDE:
        base = vault / top
        if not base.is_dir():
            continue
        for f in base.rglob("*"):
            try:
                if f.is_file() and f.suffix.lower() in EXT:
                    out.append((f, f.relative_to(vault).as_posix()))
            except OSError:
                pass   # Obsidian이 열려 있으면 스캔 중 사라지는 파일이 있다
    return sorted(out, key=lambda t: t[1])


def mirror(vault: Path, dest: Path, dry: bool = False) -> int:
    if not vault.is_dir():
        print(f"[중단] 볼트가 없습니다 — {vault}")
        return 1
    # 드라이브가 안 붙어 있으면(앱 꺼짐·다른 PC) 조용히 건너뛴다 — 배치를 깨지 않는다
    if not dest.parent.exists():
        print(f"[건너뜀] 구글드라이브가 연결돼 있지 않습니다 — {dest.parent}")
        return 0
    files = collect(vault)
    new = upd = same = fail = 0
    total = 0
    rows = []
    for src, rel in files:
        try:
            st = src.stat()
        except OSError:
            fail += 1
            continue
        total += st.st_size
        rows.append((rel, st.st_size, datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d")))
        dst = dest / rel
        try:
            if dst.exists():
                if dst.stat().st_size == st.st_size:
                    same += 1
                    continue
                upd += 1
            else:
                new += 1
            if not dry:
                dst.parent.mkdir(parents=True, exist_ok=True)
                tmp = dst.with_name(dst.name + ".part")
                shutil.copy2(src, tmp)
                tmp.replace(dst)
        except OSError as e:
            fail += 1
            print(f"  [실패] {rel} — {e}")
    print(f"PDF {len(files):,}편 · {total / 1048576:,.0f} MB → {dest}")
    print(f"  신규 {new:,} · 갱신 {upd:,} · 동일 {same:,} · 실패 {fail:,}" + ("  (dry-run)" if dry else ""))
    if not dry:
        dest.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now().strftime("%Y-%m-%d")
        (dest / "README.md").write_text(
            README.format(n=len(rows), mb=total / 1048576, stamp=stamp), encoding="utf-8")
        with open(dest / "manifest.csv", "w", newline="", encoding="utf-8-sig") as fh:
            w = csv.writer(fh)
            w.writerow(["path", "bytes", "modified"])
            w.writerows(rows)
    return 1 if fail and not (new or upd or same) else 0


def main() -> int:
    ap = argparse.ArgumentParser(description="볼트 원문 PDF → 구글드라이브 미러")
    ap.add_argument("--vault", default=os.environ.get("OBSIDIAN_VAULT_PATH", ""))
    ap.add_argument("--dest", default=os.environ.get("DATABOOK_PDF_MIRROR", "") or str(DEFAULT_DEST))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if not a.vault:
        print("[중단] --vault 또는 OBSIDIAN_VAULT_PATH 가 필요합니다")
        return 1
    return mirror(Path(a.vault.strip('"')).expanduser(), Path(a.dest).expanduser(), a.dry_run)


if __name__ == "__main__":
    sys.exit(main())
