"""발표자료 강제 검사기 — 통과 못 하면 **exit 1**로 끝난다.

왜 프로그램인가
    규칙을 문서로 써두는 방식은 이미 실패했다. 볼트 자신이 그 실패를
    「결정과 규칙문서의 표류」로 기록해 두었고, 2026-08-30 세션에서도
    지표 300여 개 중 10여 개만 쓰고 "분석했다"고 내놓는 일이 반복됐다.
    **작성자가 멈추고 싶을 때 멈출 수 있으면 반드시 거기서 멈춘다.**
    그래서 판정을 사람의 성실성이 아니라 **종료 코드**에 건다.

무엇을 강제하나 (기본값은 아래 GATES)
    1. 커버리지 — 팀별로 최소 몇 개 지표를 실제로 인용했는가
    2. 축 균형  — 한 축에서만 긁어오는 것을 막는다(토스 수급만 쓰는 행태)
    3. 문헌     — 계수를 가진 논문을 최소 몇 편 인용했는가
    4. 그림     — 축마다 그림이 있는가
    5. 기저율   — 방향을 말하는 문장이 있으면 표본 수가 함께 있어야 한다
    6. 금지문장 — 볼트 「시황 분석 진입점」 §2 목록
    7. 한계     — 미검증·표본한계를 부록에 적었는가

쓰는 법
    python -m databook audit <보고서.html 또는 .md>
    python -m databook audit <파일> --json
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

from .core import OUTPUT_DIR

# ── 통과 기준. 낮추려면 근거를 커밋 메시지에 남긴다.
GATES = {
    "min_indicators": 40,       # 본문이 실제로 인용한 서로 다른 지표 수
    "min_per_team": {"team_1": 8, "team_2": 8, "team_3": 8, "team_4": 3},
    "max_team_share": 0.45,     # 한 팀이 인용의 45%를 넘으면 편식
    "min_papers": 5,            # 저자·연도가 붙은 문헌
    "min_coefficients": 3,      # 계수·통계량이 실제 숫자로 등장한 횟수
    "min_charts": 4,
    "min_baserate_n": 20,       # 기저율 표본 하한
    "min_dates": 25,            # 기준일 병기 횟수
    "min_prose": 2500,          # 표·차트를 뺀 **실제 문장** 글자 수
    "required": ["Red Team", "무효화", "다음"],   # 반드시 있어야 하는 절
    "min_implications": 3,      # 투자자 함의 — 조건부 문장 최소 개수
    "min_analogs": 3,           # 과거 유사 국면 — 날짜가 붙은 사례 최소 개수
}

# 볼트 「시황 분석 진입점」 §2 — 실제로 저지른 오류만 들어 있다
BANNED = [
    (r"구리가?\s*(올라|상승).{0,14}(성장|경기).{0,8}(회복|개선)",
     "구리 완만한 등락을 성장 신호로 쓰지 않는다 — 게이트(12개월 최고 대비 −35%)를 먼저 확인"),
    (r"외국인이?\s*(사서|팔아서|순매수로|순매도로).{0,18}(환율|주가|지수)",
     "외국인 수급을 가격의 원인으로 쓰지 않는다 — 크기(F=9.03, 작음)를 병기할 것"),
    (r"생산성이\s*(개선|향상)",
     "dtfp가 아니라 dk가 오른 것이면 '자본심화'로 쓴다"),
    (r"(임금|기대인플레)[가이]?\s*오를?\s*테니.{0,12}물가",
     "임금·기대는 따라오는 변수다"),
    (r"리쇼어링.{0,14}(위험|리스크)[이가]?\s*(줄|감소)",
     "재배치일 뿐이다"),
    (r"투기\s*때문에\s*가격이\s*(올랐|상승)",
     "재고가 늘었는지 먼저 본다"),
    (r"선행지수가\s*돌아섰",
     "CLI 선행성은 6개 조합 전부 기각됐다"),
    (r"한은이?\s*올렸으니.{0,16}(과열|긴축)",
     "환율 제약의 뒤늦은 반응 + 생산 바닥 통과로 읽는다"),
    (r"스프레드가?\s*(낮|좁).{0,20}(스트레스|위험)[이가]?\s*없",
     "수준과 반전 위험은 다른 축이다"),
    (r"위험이\s*없다",
     "'지금까지 억제됐다'로 쓴다"),
]

_PAPER = re.compile(
    r"[A-Z][A-Za-z’'\-]+(?:\s*(?:&|and|·)\s*[A-Z][A-Za-z’'\-]+)*\s*\(\s*(?:19|20)\d{2}"
    r"|[가-힣]{2,4}(?:\s*[·,]\s*[가-힣]{2,4})*\s*\(\s*(?:19|20)\d{2}")
_COEF = re.compile(
    r"(?:α|β|γ|계수|coefficient)\s*[₀-₉0-9]*\s*[=＝]\s*[-−+]?\d"
    r"|\bR²\s*[=＝]?\s*0?\.\d"
    r"|\bF\s*[=＝]\s*\d"
    r"|\bt\s*[=＝]\s*\d"
    r"|\bSE\s*\d?\.\d"
    r"|[-−+]?\d+(?:\.\d+)?\s*%p\b"
    r"|\bn\s*[=＝]\s*\d{2,}")
_DATE = re.compile(r"(?:19|20)\d{2}[-./]\d{1,2}(?:[-./]\d{1,2})?|\b20\d{4}\b|\d{4}[-–]Q[1-4]|\d{4}:Q[1-4]")
_NBASE = re.compile(r"\bn\s*[=＝]\s*(\d{1,4})")
_DIRECTION = re.compile(r"(오른다|내린다|빠진다|상승한다|하락한다|오를\s*것|내릴\s*것|반등한다)")
# 스캐폴드가 남긴 미작성 슬롯 — 하나라도 있으면 아직 자료가 아니다
_SLOT = re.compile(r"WRITE\s*:")


def _prose(raw: str) -> str:
    """**작성자가 쓴 문장만** 센다.

    빼는 것: 표·차트·코드는 물론 **슬롯 안내문(.slot)과 문헌 인용 박스(.paper)** 도 뺀다.
    스캐폴드 안내문이 분량으로 세어지면 아무것도 안 쓰고 통과한다(실제로 그랬다).
    문헌 박스는 남의 문장이라 내 해석의 분량이 아니다.
    """
    # ⚠ <style> 안의 CSS가 문장으로 세어져 11,864자가 잡힌 적이 있다 — 먼저 지운다
    # ⚠ <style> 안의 CSS가 문장으로 세어져 11,864자가 잡힌 적이 있다 — 먼저 지운다.
    #    역참조를 쓰면 편집 과정에서 이스케이프가 벗겨져 조용히 무력화된다 — 태그별로 돈다.
    s = raw
    for _tag in ('script', 'style', 'svg', 'table'):
        s = re.sub(rf'(?is)<{_tag}[^>]*>.*?</{_tag}[^>]*>', ' ', s)
    s = re.sub(r"(?is)<link[^>]*>|<title[^>]*>.*?</title>", " ", s)
    s = re.sub(r'(?is)<div class="(slot|paper)".*?</div>', " ", s)
    s = re.sub(r"(?s)<!--.*?-->", " ", s)
    s = re.sub(r"(?is)<figure.*?</figure>", " ", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = unicodedata.normalize("NFKC", s)
    return re.sub(r"\s+", " ", s).strip()


def _text(raw: str) -> str:
    """HTML 태그·스크립트·스타일을 걷어낸 본문."""
    s = re.sub(r"(?is)<(script|style|svg)\b.*?</\1>", " ", raw)
    s = re.sub(r"(?s)<!--.*?-->", " ", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = unicodedata.normalize("NFKC", s)
    return re.sub(r"[ \t ]+", " ", s)


# HTML 구조 — 태그가 어긋나면 브라우저가 페이지를 못 그린다.
# ⚠ 게이트 18종을 다 통과한 자료가 <div> 하나가 안 닫혀 열리지 않은 적이 있다(2026-08-30).
#   내용 검사만으로는 이걸 못 잡는다.
_VOID = {"br", "hr", "img", "input", "link", "meta", "source", "col", "area", "base", "wbr",
         "circle", "rect", "line", "path", "polyline", "polygon", "text", "use", "stop",
         "ellipse", "g", "defs", "title"}


def _structure(raw: str) -> list[str]:
    """열고 닫힌 태그가 맞는지. 어긋난 지점을 사람이 찾을 수 있게 주변 글자와 함께 돌려준다."""
    stack: list[tuple[str, int]] = []
    errs: list[str] = []
    for m in re.finditer(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)([^>]*?)(/?)>", raw):
        close, tag, _attrs, selfclose = m.group(1), m.group(2).lower(), m.group(3), m.group(4)
        if tag in _VOID or selfclose == "/":
            continue
        if not close:
            stack.append((tag, m.start()))
        elif not stack:
            errs.append(f"짝 없는 </{tag}> (문서 시작 부분)")
        elif stack[-1][0] != tag:
            near = re.sub(r"\s+", " ", raw[max(0, m.start() - 70):m.start()])[-60:]
            errs.append(f"<{stack[-1][0]}>가 열린 채 </{tag}>로 닫힘 — …{near}")
            for k in range(len(stack) - 1, -1, -1):
                if stack[k][0] == tag:
                    del stack[k:]
                    break
        else:
            stack.pop()
    for tag, pos in stack[:5]:
        near = re.sub(r"\s+", " ", raw[max(0, pos - 70):pos])[-60:]
        errs.append(f"안 닫힌 <{tag}> — …{near}")
    return errs


def _snapshot() -> list[dict[str, Any]]:
    """가장 최근 스냅샷. **온전한 것**만 쓴다.

    ⚠ 2026-08-30에 `run --only <소스> --render-anyway`로 돌려 전체 스냅샷을
    2개짜리로 덮어쓴 적이 있다. 그 상태로 검사하면 "부를 지표가 2개뿐"이라
    커버리지 게이트가 **거짓 통과**한다. 관측이 절반도 안 차 있으면 그 파일을
    건너뛰고 이전 스냅샷으로 내려간다.
    """
    for p in sorted(OUTPUT_DIR.glob("snapshot_*.json"), reverse=True):
        d = json.loads(p.read_text(encoding="utf-8"))
        items = d if isinstance(d, list) else next(
            (v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict)), [])
        if not items:
            continue
        filled = sum(1 for i in items if (i.get("observations") or []))
        if filled >= len(items) * 0.5:
            return items
        print(f"  ⚠ {p.name}은 {len(items)}개 중 {filled}개만 차 있다 — 건너뛴다"
              f" (부분 수집이 전체를 덮어쓴 흔적)", file=sys.stderr)
    return []


def _mentions(text: str, items: list[dict[str, Any]]) -> dict[str, str]:
    """본문이 실제로 부른 지표 → 팀. 이름 전체가 아니라 **식별 가능한 조각**으로 센다."""
    hit: dict[str, str] = {}
    flat = re.sub(r"[\s·,()\[\]{}]", "", text)
    for i in items:
        name = i.get("name") or ""
        if not name:
            continue
        # 괄호 앞 본체를 키로 삼는다: "구리 (Dr.Copper, …)" → "구리"
        head = re.split(r"[(（]", name)[0].strip()
        key = re.sub(r"[\s·,]", "", head)
        if len(key) < 2:
            continue
        if key in flat:
            hit[name] = i.get("team") or "?"
    return hit


def audit(path: Path, gates: dict | None = None) -> dict[str, Any]:
    g = {**GATES, **(gates or {})}
    raw = path.read_text(encoding="utf-8", errors="replace")
    text = _text(raw)
    items = _snapshot()

    hits = _mentions(text, items)
    per_team: dict[str, int] = {}
    for t in hits.values():
        per_team[t] = per_team.get(t, 0) + 1
    total = len(hits)
    share = (max(per_team.values()) / total) if total else 1.0
    top_team = max(per_team, key=per_team.get) if per_team else "-"

    papers = sorted(set(m.group(0).strip() for m in _PAPER.finditer(text)))
    coefs = _COEF.findall(text)
    charts = len(re.findall(r"<figure[^>]*class=\"[^\"]*chart", raw)) or raw.count("<svg")
    dates = _DATE.findall(text)
    ns = [int(x) for x in _NBASE.findall(text)]
    max_n = max(ns) if ns else 0
    directions = _DIRECTION.findall(text)

    checks: list[tuple[str, bool, str]] = []

    def chk(name, ok, detail):
        checks.append((name, bool(ok), detail))

    chk("지표 커버리지", total >= g["min_indicators"],
        f"본문이 부른 지표 {total}개 / 최소 {g['min_indicators']}개")
    for t, need in g["min_per_team"].items():
        chk(f"팀 균형 {t}", per_team.get(t, 0) >= need,
            f"{per_team.get(t,0)}개 / 최소 {need}개")
    chk("한 축 편식 금지", share <= g["max_team_share"],
        f"최다 팀 {top_team} 비중 {share*100:.0f}% / 상한 {g['max_team_share']*100:.0f}%")
    chk("문헌 인용", len(papers) >= g["min_papers"],
        f"{len(papers)}편 / 최소 {g['min_papers']}편 — {', '.join(papers[:4])}")
    chk("계수 사용", len(coefs) >= g["min_coefficients"],
        f"계수·통계량 {len(coefs)}회 / 최소 {g['min_coefficients']}회")
    chk("그림", charts >= g["min_charts"], f"{charts}개 / 최소 {g['min_charts']}개")
    chk("기준일 병기", len(dates) >= g["min_dates"],
        f"{len(dates)}회 / 최소 {g['min_dates']}회")
    chk("기저율 표본", (not directions) or max_n >= g["min_baserate_n"],
        (f"방향 서술 {len(directions)}회 · 최대 n={max_n} / 최소 {g['min_baserate_n']}"
         if directions else "방향 서술 없음 — 면제"))
    chk("한계 명시", any(k in text for k in ("미검증", "표본", "관측 없음", "계산 불가", "한계")),
        "미검증·표본한계·못 보는 것 중 하나 이상")

    slots = _SLOT.findall(raw)
    chk("미작성 슬롯 없음", not slots,
        f"WRITE 슬롯 {len(slots)}개 남음 — 스캐폴드는 자료가 아니다" if slots else "0개")

    prose = _prose(raw)
    chk("해석 분량", len(prose) >= g["min_prose"],
        f"표·차트를 뺀 문장 {len(prose):,}자 / 최소 {g['min_prose']:,}자")

    miss = [k for k in g["required"] if k not in text]
    chk("필수 절", not miss,
        f"빠짐: {', '.join(miss)}" if miss else "Red Team · 무효화 조건 · 다음 세션 확인")

    # 투자자 함의 — **조건부**여야 한다. "오른다"가 아니라 "X를 넘으면 Y가 유리하다".
    # 볼트 Human Principle: 최종 실행과 승인은 사람이고 AI는 조건부 판단의 재료를 만든다.
    impl = re.findall(r"(?:넘으면|상회하면|하회하면|아래면|위면|충족되면|나오면)"
                      r"[^.。]{0,60}?(?:유리|불리|우위|약해|강해|바뀐다|버린다)", text)
    chk("투자자 함의", len(impl) >= g["min_implications"],
        f"조건부 문장 {len(impl)}개 / 최소 {g['min_implications']}개 — "
        f"'X를 넘으면 Y가 유리하다' 형태로 쓴다")

    # 과거 사례 — 「좋은 시황의 규칙」 근거 3축의 '사례'. 날짜가 붙어야 사례다
    # 과거 사례 — 「좋은 시황의 규칙」 근거 3축의 '사례'.
    #   날짜 뒤 60자 안에 결과를 말하는 말이 있어야 사례다. 날짜만 나열한 표는 사례가 아니다.
    # 과거 사례 — 「좋은 시황의 규칙」 근거 3축의 '사례'.
    #   날짜 뒤 80자 안에 결과를 말하는 말이 있어야 사례다. 날짜만 나열한 표는 사례가 아니다.
    #   ⚠ 마침표로 문장을 끊으면 "(거리 0.56)" 같은 소수점에서 잘린다 — 길이로만 자른다.
    ana = re.findall(
        r"(?:19|20)\d{2}[-./]\d{1,2}[-./]\d{1,2}.{0,80}?"
        r"(?:그때|당시|이후|그 뒤|직후|였다|갔다|겪|기록)",
        text)
    chk("과거 사례", len(ana) >= g["min_analogs"],
        f"날짜가 붙은 사례 {len(ana)}개 / 최소 {g['min_analogs']}개 — "
        f"`databook analog`로 이웃을 찾는다")

    struct = _structure(raw)
    chk("HTML 구조", not struct,
        "; ".join(struct[:2]) if struct else "태그 짝 맞음")

    banned_hits = []
    for pat, why in BANNED:
        m = re.search(pat, text)
        if m:
            banned_hits.append((m.group(0)[:40], why))
    chk("금지문장 없음", not banned_hits,
        "; ".join(f"'{a}' → {b}" for a, b in banned_hits) or "0건")

    failed = [c for c in checks if not c[1]]
    return {"path": str(path), "checks": checks, "failed": len(failed),
            "indicators": total, "per_team": per_team, "papers": papers,
            "charts": charts, "coefs": len(coefs), "max_n": max_n,
            "slots": len(slots), "prose": len(prose),
            "implications": len(impl), "analogs": len(ana), "struct": len(struct),
            "unused": [i["name"] for i in items if i.get("name") not in hits][:400]}


def cmd_audit(target: str, as_json: bool = False, show_unused: int = 0) -> int:
    p = Path(target)
    if not p.exists():
        print(f"파일이 없습니다: {target}")
        return 2
    r = audit(p)
    if as_json:
        print(json.dumps({k: v for k, v in r.items() if k != "checks"} |
                         {"checks": [{"name": n, "ok": o, "detail": d} for n, o, d in r["checks"]]},
                         ensure_ascii=False, indent=1))
        return 1 if r["failed"] else 0

    print(f"\n검사 대상  {p.name}")
    print("=" * 72)
    for name, ok, detail in r["checks"]:
        print(f"  {'PASS' if ok else 'FAIL'}  {name:16} {detail}")
    print("=" * 72)
    if r["failed"]:
        print(f"  {r['failed']}건 미달 — 이 자료는 아직 낼 수 없다.")
        print("  기준을 낮추려면 GATES를 고치고 **왜 낮췄는지 커밋에 남긴다.**")
    else:
        print("  전 항목 통과.")
    if show_unused:
        print(f"\n쓰지 않은 지표 {len(r['unused'])}개 중 앞 {show_unused}개:")
        for n in r["unused"][:show_unused]:
            print(f"    {n}")
    return 1 if r["failed"] else 0
