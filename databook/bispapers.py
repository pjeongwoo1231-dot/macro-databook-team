"""BIS Working Papers 신규분 자동수집.

**왜 필요한가** — 볼트의 `06_SourceArchive/06-BIS-Archive-Catalog/Sources/`에 WP 1~1371이
이미 들어 있다(결번은 공식 철회된 1323 하나뿐). 그런데 **그건 2026-08-14 시점의 스냅샷이고
BIS는 계속 낸다.** 손으로 따라잡으면 또 몇 달치가 밀린다.

**어디가 열리나** (2026-09-16 실측)
    www.bis.org/publ/work{N}.htm  → 302 → /publications/working-paper-{N}-{슬러그}
    레거시 번호 URL이 살아 있어 **번호로 전수 열거가 된다.** 새 슬러그는 번호를 모르면 못 만든다.
    메타는 <meta name="citation_*">에 있고 PDF도 같은 슬러그 + .pdf 다.

⚠ **이 수집기는 초록까지만 신뢰한다.**
   기존 카탈로그 노트가 스스로 못박은 그대로다 — *"분석적 요약 노트가 아니며,
   저자의 주장·방법·한계를 인용하려면 원문 전문을 직접 확인해야 한다."*
   그래서 `human_verified: false`로 쓴다. **제텔은 여기서 자동 생성하지 않는다** —
   초록으로 주장을 만들면 볼트가 이미 겪은 실패(전수 판독 허위 주장)를 반복하는 것이다.
   전문 텍스트는 받아 두되(`fulltext_chars`), 판독은 사람이 한다.
"""
from __future__ import annotations

import hashlib
import html as _html
import re
import urllib.request
from datetime import date
from pathlib import Path
from typing import Any

from .core import load_env

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/131"}
LEGACY = "https://www.bis.org/publ/work{n}.htm"
SUB = "06_SourceArchive/06-BIS-Archive-Catalog/Sources"
PDFDIR = "06_SourceArchive/06-BIS-Archive-Catalog/PDFs"
PROBE_STOP = 4          # 연속 404 이만큼이면 최신에 도달한 것으로 본다


def _get(url: str, timeout: int = 45) -> tuple[bytes, str]:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read(), r.geturl()


def _meta(html: str, name: str) -> str:
    for pat in (r'<meta[^>]+name="' + name + r'"[^>]+content="([^"]*)"',
                r'<meta[^>]+content="([^"]*)"[^>]+name="' + name + r'"'):
        m = re.search(pat, html, re.I)
        if m:
            return m.group(1).strip()
    return ""


def _metas(html: str, name: str) -> list[str]:
    """**같은 name의 meta가 여러 개** 나온다 — citation_author가 저자 수만큼 반복된다.
    첫 개만 읽으면 3인 논문이 1인으로 기록된다(2026-09-16 WP 1373에서 실제로 그랬다).
    볼트 규칙 「서지는 조회한 것만, 공저자까지」에 정면으로 걸리는 결함이라 전부 모은다."""
    out, seen = [], set()
    for pat in (r'<meta[^>]+name="' + name + r'"[^>]+content="([^"]*)"',
                r'<meta[^>]+content="([^"]*)"[^>]+name="' + name + r'"'):
        for m in re.finditer(pat, html, re.I):
            v = m.group(1).strip()
            if v and v not in seen:
                seen.add(v)
                out.append(v)
    return out


def _plain(html: str) -> str:
    s = re.sub(r"(?s)<script.*?</script>|<style.*?</style>", " ", html)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def _abstract(html: str) -> str:
    """초록은 'Abstract' 뒤부터 'JEL'/'Keywords' 앞까지."""
    t = _plain(html)
    m = re.search(r"Abstract\s+(.{80,4000}?)(?:\s*JEL classification|\s*Keywords|\s*Download)", t, re.S)
    return m.group(1).strip() if m else ""


def _pdf_abstract(data: bytes) -> str:
    """초록은 **PDF에서 뽑는 게 맞다.**

    BIS 발간 페이지의 HTML 구조가 재편되면서 초록 블록을 못 잡는 경우가 생겼다
    (2026-09-16 WP 1372~1376 전부 실패). PDF 앞부분은 서식이 안정적이라
    `Abstract` ~ `JEL`/`Keywords` 구간이 그대로 잡힌다. 표지 다음 2~4쪽에 있다.
    ⚠ PDF 추출은 낱자 사이에 공백을 흘린다("c hanges", "high -frequency") — 그대로 둔다.
       임의로 붙이면 원문을 고치는 것이 된다. 인용할 때 사람이 원문을 본다.
    """
    import io
    try:
        import pypdf
        r = pypdf.PdfReader(io.BytesIO(data))
        # ⚠ **종결어를 필수로 두면 안 된다.** 초록이 쪽 경계에서 잘리면
        #    JEL/Keywords가 다음 쪽으로 넘어가고, 그러면 비탐욕 매칭이 통째로 실패한다
        #    (2026-09-16 WP 1372~1376 전부 이 이유로 빈 초록이 됐다).
        #    종결어가 있으면 거기서 끊고, 없으면 **앞에서부터 2,000자**를 취한다.
        for i in range(min(6, len(r.pages))):
            t = re.sub(r"\s+", " ", r.pages[i].extract_text() or "")
            head = re.search(r"\bAbstract\b[:.]?\s+", t, re.I)
            if not head:
                continue
            rest = t[head.end():]
            cut = re.search(r"\s*(?:JEL classification|JEL codes|JEL:|Keywords?|1\.?\s+Introduction)",
                            rest, re.I)
            body = rest[:cut.start()] if cut else rest[:2000]
            body = body.strip()
            if len(body) >= 120:
                return body
    except Exception:
        pass
    return ""


def _pdf_keywords(data: bytes) -> str:
    import io
    try:
        import pypdf
        r = pypdf.PdfReader(io.BytesIO(data))
        for i in range(min(5, len(r.pages))):
            t = re.sub(r"\s+", " ", r.pages[i].extract_text() or "")
            m = re.search(r"Keywords?[:.]?\s*([^.]{5,200})", t, re.I)
            if m:
                return m.group(1).strip()
    except Exception:
        pass
    return ""


def _pdf_text(data: bytes) -> tuple[int, int]:
    """전문 글자수만 센다. 본문 저장은 PDF 자체로 갈음한다(중복 보관하지 않는다)."""
    import io
    try:
        import pypdf
        r = pypdf.PdfReader(io.BytesIO(data))
        return sum(len(p.extract_text() or "") for p in r.pages), len(r.pages)
    except Exception:
        return 0, 0


def fetch_one(n: int) -> dict[str, Any] | None:
    try:
        raw, final = _get(LEGACY.format(n=n))
    except Exception:
        return None
    html = raw.decode("utf-8", "replace")
    title = _meta(html, "citation_title")
    if not title:
        return None
    pdf_url = ""
    m = re.search(r'href="([^"]*working-paper-' + str(n) + r'[^"]*\.pdf)"', html)
    if m:
        pdf_url = m.group(1)
        if pdf_url.startswith("/"):
            pdf_url = "https://www.bis.org" + pdf_url
    kw = ""
    mk = re.search(r"Keywords:\s*([^<]{0,200})", _plain(html))
    if mk:
        kw = mk.group(1).strip()
    # &#039; 같은 엔티티가 제목·저자에 그대로 남는다(WP 1376 실측) — 푼다
    unesc = _html.unescape
    return {"n": n, "url": final, "title": unesc(title),
            "authors": unesc(" · ".join(_metas(html, "citation_author")) or _meta(html, "author")),
            "date": _meta(html, "citation_date") or _meta(html, "citation_publication_date"),
            "abstract": _abstract(html), "keywords": kw, "pdf_url": pdf_url}


def write_note(vault: Path, rec: dict[str, Any], sha: str, chars: int, pages: int) -> Path:
    p = vault / SUB / f"BIS_WP_{rec['n']}-catalog.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    esc = lambda s: (s or "").replace('"', "'")
    kw_tags = [re.sub(r"[^a-z0-9-]+", "-", w.strip().lower()).strip("-")
               for w in (rec.get("keywords") or "").split(",") if w.strip()][:6]
    tag_lines = "".join(f"\n  - {t}" for t in kw_tags if t)
    body = rec["abstract"] or "_(초록을 페이지에서 추출하지 못했다 — 원문 PDF를 확인할 것)_"
    p.write_text(f"""---
title: "BIS WP {rec['n']} — {esc(rec['title'])}"
type: primary_source
institution: "Bank for International Settlements"
series: "BIS Working Papers"
number: {rec['n']}
published: "{esc(rec.get('date'))}"
authors: "{esc(rec.get('authors'))}"
source_kind: "working-paper"
peer_reviewed: false
primary_text_available: {str(bool(sha)).lower()}
fulltext_verified: false
pages: {pages}
fulltext_chars: {chars}
sha256: "{sha}"
catalog_filename: "BIS_WP_{rec['n']}-catalog.md"
human_verified: false
catalog_method: "automated-bis-fetch"
created: {date.today().isoformat()}
updated: {date.today().isoformat()}
archive_status: "auto-collected-abstract"
tags:
  - flag/partial-check
  - bis
  - working-paper{tag_lines}
status: working
verification: partial
reliability: working-paper
verified: "△ BIS 공식 페이지에서 자동 수집한 서지·초록. **초록 범위 밖 주장은 원문 확인 필요** — 이 노트로 제텔을 만들지 않는다"
related: ["[[원문 아카이브 MOC]]"]
text_basis: extracted-abstract
vault_tier: D
---

# BIS WP {rec['n']} — {rec['title']}

> 자동 수집한 **원문 카탈로그 노트**다. 분석적 요약이 아니며,
> 저자의 주장·방법·한계를 인용하려면 **원문 전문을 직접 확인해야 한다.**

| 항목 | 내용 |
|---|---|
| 저자 | {rec.get('authors') or '—'} |
| 발행 | {rec.get('date') or '—'} |
| 원문 | [{rec['url']}]({rec['url']}) |
| PDF | {f"[내려받기]({rec['pdf_url']})" if rec.get('pdf_url') else '—'} |
| 전문 | {f"{pages}쪽 · {chars:,}자 (로컬 PDF 보관)" if sha else '미확보'} |
| 키워드 | {rec.get('keywords') or '—'} |

## 초록 (원문 그대로)

{body}
""", encoding="utf-8")
    return p


def backfill_pdfs(log=print, sleep_s: float = 1.0) -> int:
    """카탈로그 노트는 있는데 **로컬 PDF가 없는** 건들의 원문을 받아 온다.

    **왜 필요한가** — 카탈로그 1,375건은 초록까지만 갖고 있다(`text_basis: extracted-abstract`).
    노트 자체가 "주장을 인용하려면 원문 전문을 확인해야 한다"고 못박고 있어서,
    **PDF가 없으면 제텔을 만들 수 없다.** 판독의 전제 조건이다.

    ⚠ BIS 서버에 예의를 지킨다 — 요청 사이에 쉰다(기본 1초). 1,353건이면 한 시간쯤 걸린다.
    ⚠ **중단해도 안전하다.** 이미 받은 파일은 건너뛰므로 다시 돌리면 이어서 받는다.
    """
    import time
    env = load_env()
    vault = Path(env.get("OBSIDIAN_VAULT_PATH") or ".")
    src, pdfdir = vault / SUB, vault / PDFDIR
    pdfdir.mkdir(parents=True, exist_ok=True)

    nums = sorted(int(m.group(1)) for f in src.glob("BIS_WP_*-catalog.md")
                  if (m := re.search(r"BIS_WP_(\d+)-catalog", f.name)))
    todo = [n for n in nums if not (pdfdir / f"BIS_WP_{n}.pdf").exists()]
    # **최신부터 받는다.** 초기 번호대(WP 1~6 등, 1970~80년대)는 이미지 스캔이라
    # 텍스트 층이 없어 판독에 못 쓴다(2026-09-16 실측: 본문 추출이 26~51자).
    # 오름차순으로 받으면 쓸모없는 것부터 한 시간을 쓰고 그동안 판독기는 논다.
    # 내림차순이면 받는 즉시 판독이 붙는다. 어차피 전부 받지만 **순서가 처리량을 정한다.**
    todo.sort(reverse=True)
    log(f"카탈로그 {len(nums):,}건 · 이미 보유 {len(nums) - len(todo):,}건 → "
        f"받을 것 {len(todo):,}건 (최신 {todo[0] if todo else '-'}번부터 내림차순)")

    ok = fail = 0
    for i, n in enumerate(todo, 1):
        try:
            rec = fetch_one(n)
            if not rec or not rec.get("pdf_url"):
                log(f"  ✘ WP {n}: PDF 링크 없음")
                fail += 1
                continue
            data, _ = _get(rec["pdf_url"], timeout=120)
            if not data.startswith(b"%PDF"):
                log(f"  ✘ WP {n}: PDF가 아니다 ({len(data):,}B)")
                fail += 1
                continue
            (pdfdir / f"BIS_WP_{n}.pdf").write_bytes(data)
            ok += 1
            if i % 25 == 0 or i == len(todo):
                log(f"  … {i:,}/{len(todo):,}  성공 {ok:,} 실패 {fail:,}")
        except Exception as e:
            log(f"  ✘ WP {n}: {type(e).__name__} {str(e)[:60]}")
            fail += 1
        time.sleep(sleep_s)
    log(f"\n완료: 성공 {ok:,} / 실패 {fail:,} → {pdfdir}")
    return 0


def collect(start: int | None = None, end: int | None = None,
            with_pdf: bool = True, log=print) -> int:
    env = load_env()
    vault = Path(env.get("OBSIDIAN_VAULT_PATH") or ".")
    src = vault / SUB
    have = {int(m.group(1)) for f in src.glob("BIS_WP_*-catalog.md")
            if (m := re.search(r"BIS_WP_(\d+)-catalog", f.name))}
    if start is None:
        start = (max(have) + 1) if have else 1
    log(f"보유 {len(have)}건 (최대 {max(have) if have else 0}) → {start}번부터 확인")

    n, miss, got = start, 0, 0
    while True:
        if end is not None and n > end:
            break
        if end is None and miss >= PROBE_STOP:
            log(f"연속 404 {PROBE_STOP}회 — 최신에 도달했다 (마지막 확인 {n - 1})")
            break
        rec = fetch_one(n)
        if not rec:
            miss += 1
            n += 1
            continue
        miss = 0
        sha, chars, pages = "", 0, 0
        if with_pdf and rec.get("pdf_url"):
            try:
                data, _ = _get(rec["pdf_url"], timeout=90)
                sha = hashlib.sha256(data).hexdigest()
                chars, pages = _pdf_text(data)
                if not rec.get("abstract"):
                    rec["abstract"] = _pdf_abstract(data)
                if not rec.get("keywords"):
                    rec["keywords"] = _pdf_keywords(data)
                pd = vault / PDFDIR
                pd.mkdir(parents=True, exist_ok=True)
                (pd / f"BIS_WP_{n}.pdf").write_bytes(data)
            except Exception as e:
                log(f"    ⚠ PDF 실패 {n}: {type(e).__name__}")
        write_note(vault, rec, sha, chars, pages)
        log(f"  ✔ WP {n:<5} {rec['title'][:58]}"
            + (f"  [{pages}쪽 {chars:,}자]" if sha else "  [PDF 미확보]"))
        got += 1
        n += 1
    log(f"\n완료: 신규 {got}건 → {src}")
    return 0
