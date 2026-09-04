"""인용 가능 인덱스 생성 — 팀원이 '이거 인용해도 되나'를 한 번에 판정하게 한다.

문헌이 1,200편인데 인용 규칙은 `verification` 프론트매터 하나에 걸려 있다.
그런데 그 필드는 노트를 **열어야** 보인다 — 팀원이 1,200번 열 수는 없다.
그래서 실측해서 목록으로 뽑는다. 규칙은 `_System/docs/FRONTMATTER_VOCAB.md`가 정본이고,
이 노트는 그 규칙을 **현재 볼트에 적용한 결과**다.
"""
from __future__ import annotations
import re
from datetime import date
from pathlib import Path

def _vault() -> Path:
    """볼트 위치. 예전엔 cwd를 볼트로 가정했는데, 이 스크립트가 저장소(`tools/`)로
    옮겨 오면서 그 가정이 깨졌다 — 저장소에서 돌리면 논문 폴더를 못 찾고 죽는다.
    `--vault` > `OBSIDIAN_VAULT_PATH` > cwd 순으로 찾는다.
    """
    import argparse
    import os
    ap = argparse.ArgumentParser(description="인용 가능 인덱스 생성")
    ap.add_argument("--vault", default="")
    a, _ = ap.parse_known_args()
    v = a.vault or os.environ.get("OBSIDIAN_VAULT_PATH", "").strip().strip('"')
    if not v:
        env = Path(__file__).resolve().parent.parent / ".env"
        if env.exists():
            for line in env.read_text(encoding="utf-8", errors="replace").splitlines():
                if line.strip().startswith("OBSIDIAN_VAULT_PATH") and "=" in line:
                    v = line.split("=", 1)[1].strip().strip('"')
                    break
    p = Path(v).expanduser().resolve() if v else Path(".").resolve()
    if not (p / "02_Papers").is_dir():
        raise SystemExit(f"[중단] 볼트가 아닙니다: {p}\n"
                         "       --vault <볼트경로> 를 주거나 OBSIDIAN_VAULT_PATH를 설정하세요.")
    return p


V = _vault()
FOLDERS = ["02_Papers", "05_Library", "04_Zettel"]


def fm(p: Path) -> dict[str, str]:
    t = p.read_text(encoding="utf-8", errors="replace")
    if not t.startswith("---"):
        return {}
    end = t.find("\n---", 3)
    if end < 0:
        return {}
    d = {}
    for line in t[3:end].splitlines():
        m = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
        if m:
            d[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return d


rows: dict[str, list[tuple[str, str, str]]] = {}
counts: dict[str, dict[str, int]] = {}
for folder in FOLDERS:
    counts[folder] = {}
    for p in sorted((V / folder).glob("*.md")):
        f = fm(p)
        ver = f.get("verification", "").lower() or "(필드없음)"
        rel = f.get("reliability", "") or "-"
        counts[folder][ver] = counts[folder].get(ver, 0) + 1
        rows.setdefault(f"{folder}/{ver}", []).append((p.stem, rel, f.get("type", "")))

L: list[str] = []
A = L.append
A("---")
A("title: 인용 가능 인덱스")
A("type: MOC")
A(f"created: {date.today().isoformat()}")
A("status: done")
A("tags: [type/MOC, team/guide]")
A('related: ["[[팀 안내 (먼저 읽기)]]", "[[Library MOC]]"]')
A("---")
A("")
A("# 인용 가능 인덱스")
A("")
A("> **문헌을 인용하기 전에 여기서 이름을 찾으세요.** 목록에 없으면 인용하지 않습니다.")
A("> 규칙 정본은 `_System/docs/FRONTMATTER_VOCAB.md` — 이 노트는 그걸 현재 볼트에 적용한 결과입니다.")
A(f"> 실측일 {date.today().isoformat()}. 배포본이 갱신되면 이 노트도 다시 생성됩니다.")
A("")
A("## 판정 규칙 — 세 줄")
A("")
A("| 가져올 것 | 필요한 `verification` | 예 |")
A("|---|---|---|")
A("| ③ **수치**(표·계수·통계량) | `full` **만** | \"실업률 1%p↑ 시 −0.4\" |")
A("| ② **서술**(저자의 주장·결론) | `full` 또는 `partial` | \"저자는 전이가 비대칭이라고 본다\" |")
A("| ① **명제**(수치 없는 일반 주장) | `none`이어도 `reliability: academic` 이상이면 통과 | \"신용스프레드는 경기에 선행한다\" |")
A("")
A("`n-a`는 기관 리포트·1차 사료 — 그 자체가 원문이므로 출처만 밝히고 인용합니다.")
A("**`(필드없음)`은 '아마 괜찮다'가 아니라 '판정 안 됨'입니다 — 인용하지 마세요.**")
A("")
A("## 현황 — 실측")
A("")
A("| 폴더 | " + " | ".join(sorted({k for c in counts.values() for k in c})) + " | 합계 |")
allk = sorted({k for c in counts.values() for k in c})
A("|---|" + "---|" * (len(allk) + 1))
for folder in FOLDERS:
    c = counts[folder]
    A(f"| `{folder}` | " + " | ".join(str(c.get(k, 0)) for k in allk) + f" | {sum(c.values())} |")
A("")
# 표만 보면 "제텔 대부분이 못 쓰는 것"으로 읽힌다 — 제텔은 규칙이 다르다.
# 오독을 뒤 절까지 미루지 않고 표 바로 아래서 끊는다.
z_none = counts["04_Zettel"].get("(필드없음)", 0)
if z_none:
    A(f"> **제텔의 `(필드없음)` {z_none}개는 결격이 아닙니다.** 제텔은 자기 필드가 아니라 "
      "`source`가 가리키는 원문 노트의 등급을 따릅니다 — 판정법은 이 문서 맨 아래에 있습니다.")
    A("> 위 경고가 적용되는 것은 `02_Papers`와 `05_Library`입니다.")
    A("")

lib_none = counts["05_Library"].get("(필드없음)", 0)
if lib_none:
    A(f"> ⚠ **`05_Library` {lib_none}편은 전부 `verification` 미판정입니다 — 인용 금지.**")
    A("> 원문 대조(DOI로 디스크 PDF 확인)를 거쳐야 승격됩니다. 「[[05_Library 중복 판별 (2026-08-14)]]」 참조.")
    A("")

A("## ③ 수치까지 인용 가능 — `verification: full`")
A("")
full = rows.get("02_Papers/full", [])
A(f"`02_Papers` **{len(full)}편**. 이 목록에 있는 것만 표·계수·통계량을 옮길 수 있습니다.")
A("")
for name, rel, _ in full:
    A(f"- [[{name}]] · `{rel}`")
A("")

A("## ② 서술만 — `verification: partial` (수식·표 숫자 금지)")
A("")
part = rows.get("02_Papers/partial", [])
A(f"`02_Papers` **{len(part)}편**. OCR 복원·미러 소스·부분 판독이라 **숫자는 못 씁니다.**")
A("")
for name, rel, _ in part:
    A(f"- [[{name}]] · `{rel}`")
A("")

A("## 출처 표기 후 인용 — `verification: n-a` (기관 리포트·1차 사료)")
A("")
na = rows.get("02_Papers/n-a", [])
A(f"`02_Papers` **{len(na)}편**. 그 자체가 원문입니다.")
A("")
for name, rel, _ in na:
    A(f"- [[{name}]] · `{rel}`")
A("")

A("## ⛔ 수치 인용 금지 — `verification: none`")
A("")
none = rows.get("02_Papers/none", [])
A(f"`02_Papers` **{len(none)}편**. 원문 미확보(2차 자료). ")
A("`reliability: academic` 이상이면 **① 명제 층위만** 허용됩니다(2026-08-21 개정). "
  "`secondary`·`media`는 ①도 금지.")
A("")
for name, rel, _ in none:
    mark = " — **①도 금지**" if rel in ("secondary", "media") else ""
    A(f"- [[{name}]] · `{rel}`{mark}")
A("")

A("## 제텔(`04_Zettel`)은 어떻게 판정하나")
A("")
z = counts["04_Zettel"]
A(f"제텔 {sum(z.values())}개 중 `verification`이 붙은 것은 **{sum(v for k, v in z.items() if k != '(필드없음)')}개**뿐입니다.")
A("나머지는 `reliability`만 있습니다. **제텔의 인용 가능 여부는 제텔 자신이 아니라 "
  "`source`가 가리키는 원문 노트에서 옵니다.**")
A("")
A("판정 순서: 제텔의 `source`를 본다 → 그 논문을 위 목록에서 찾는다 → 그 등급을 따른다.")
A("찾을 수 없으면 인용하지 않습니다.")
A("")
A("> 제텔은 **주장 단위**라 그 자체로는 ① 명제입니다. 제텔에 적힌 **숫자**를 옮기려면 "
  "원문이 `full`이어야 합니다 — 제텔이 요약하며 반올림했을 수 있습니다.")

out = V / "03_MOC" / "인용 가능 인덱스.md"
out.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"→ {out}  ({len(L)}줄)")
for folder in FOLDERS:
    print(f"   {folder}: {counts[folder]}")
