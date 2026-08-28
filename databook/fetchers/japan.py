"""일본 재무성(MOF) 국채 금리 — 키 불필요.

**왜 필요한가** — [[일본 국채 (JGB)]] 노드는 판정 규칙을 갖췄는데
`mof_jgb` 소스가 **구현되지 않아** 매 실행 실패로 남아 있었다(2026-08-21 확인).
볼트의 일본 축은 *"커브가 이미 반영한 것을 먼저 뺀다"* 를 규칙으로 갖고 있어
**전 만기 커브**가 필요하다.

**출처**: `https://www.mof.go.jp/jgbs/reference/interest_rate/jgbcm.csv` (당월)
및 연도별 파일 `jgbcm{연도}.csv`. 만기 1·2·3·4·5·6·7·8·9·10·15·20·25·30·40년.

⚠ **인코딩이 Shift-JIS**다. UTF-8로 읽으면 깨진다.
⚠ **날짜가 일본 연호**다 — `R8.8.20` = 레이와 8년 = **2026년** 8월 20일.
  레이와 원년이 2019년이므로 서기 = 2018 + 연호년. 헤이세이(H)는 1988 + 연호년.
⚠ 값이 비어 있는 날이 있다(휴장). 빈 칸은 **건너뛴다** — 0으로 채우지 않는다.
"""
from __future__ import annotations

import csv
import html
import io
import re
from typing import Any

from .base import get_bytes, get_text, result, norm_key as _norm

BASE = "https://www.mof.go.jp/jgbs/reference/interest_rate"
CUR = f"{BASE}/jgbcm.csv"

# 헤더의 "10年" 같은 표기 → 만기 키
_TENOR = re.compile(r"^(\d+)年$")


def _jp_date(s: str) -> str | None:
    """R8.8.20 → 2026-08-20. 연호를 서기로 바꾼다."""
    m = re.match(r"^([RHS])(\d+)\.(\d+)\.(\d+)$", s.strip())
    if not m:
        return None
    era, y, mo, d = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))
    base = {"R": 2018, "H": 1988, "S": 1925}.get(era)
    if base is None:
        return None
    return f"{base + y:04d}-{mo:02d}-{d:02d}"


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """yaml 예시:
        method: api
        source: mof_jgb
        tenors: ["2年", "10年", "30年"]   # 없으면 2·10·30년
        points: 5
    """
    # yaml은 `maturities: ["2Y","10Y","30Y"]`를 쓰고 MOF 헤더는 `2年` 꼴이다. 둘 다 받는다
    raw_want = ind.get("tenors") or ind.get("maturities") or ["2Y", "10Y", "30Y"]
    want = [re.sub(r"(?i)^(\d+)\s*(?:Y|년|年)$", lambda m: m.group(1) + "年", str(x).strip())
            for x in raw_want]
    year = ind.get("year")
    url = f"{BASE}/jgbcm{year}.csv" if year else CUR
    try:
        raw = get_bytes(url, headers={"User-Agent": "MacroVault/1.0"})
    except Exception as e:
        return result(ind, "fail", error=f"MOF {type(e).__name__}: {e}", source_url=url)

    text = raw.decode("shift_jis", errors="replace")
    rows = list(csv.reader(io.StringIO(text)))
    # 헤더 행 찾기 — 첫 칸이 "基準日"
    hi = next((i for i, r in enumerate(rows) if r and r[0].strip() == "基準日"), None)
    if hi is None:
        return result(ind, "fail", error="헤더(基準日) 없음 — 포맷 변경 의심", source_url=url)
    header = [c.strip() for c in rows[hi]]
    idx = {h: i for i, h in enumerate(header)}
    missing = [w for w in want if w not in idx]
    if missing:
        return result(ind, "fail",
                      error=f"만기 없음: {missing} · 가능: {[h for h in header if _TENOR.match(h)]}",
                      source_url=url)

    obs: list[dict[str, Any]] = []
    for r in reversed(rows[hi + 1:]):          # 최신일부터
        if not r or not r[0].strip():
            continue
        d = _jp_date(r[0])
        if not d:
            continue
        for w in want:
            i = idx[w]
            if i >= len(r):
                continue
            v = r[i].strip()
            if not v:                          # 휴장·미고시 — 채우지 않는다
                continue
            try:
                obs.append({"date": d, "value": float(v), "label": f"JGB {w} 금리(%)"})
            except ValueError:
                continue
        if len({o["date"] for o in obs}) >= int(ind.get("points") or 5):
            break

    if not obs:
        return result(ind, "fail", error="파싱된 관측 없음", source_url=url)

    # 커브 스프레드도 같이 낸다 — 볼트 규칙이 "커브가 반영한 것"을 먼저 보라고 한다
    latest = obs[0]["date"]
    by = {o["label"]: o["value"] for o in obs if o["date"] == latest}
    for lo, hi_ in (("2年", "10年"), ("10年", "30年")):
        a, b = by.get(f"JGB {lo} 금리(%)"), by.get(f"JGB {hi_} 금리(%)")
        if a is not None and b is not None:
            obs.append({"date": latest, "value": round(b - a, 3),
                        "label": f"JGB {hi_}−{lo} 스프레드(%p)"})
    return result(ind, "ok", observations=obs, source_url=url, unit="%")


# ═══════════════════════ 일본 관세청(Japan Customs) 무역통계 속보 ═══════════════════════
"""**왜 필요한가** — BOJ 국제수지(BP01)는 재화수지 총액만 준다. 어느 나라와, 무엇을
얼마나 주고받았는지는 **관세청 속보**에만 있다. 원유·LNG·석탄 수입은 **수량까지** 나와서
"금액이 늘어난 게 가격 때문인가 물량 때문인가"를 그 자리에서 가른다.

**출처**: 색인 https://www.customs.go.jp/toukei/shinbun/happyou_e.htm
        속보 XML https://www.customs.go.jp/toukei/shinbun/trade-st_e/<연도>/<파일>.xml

⚠ **파일명 규칙을 추측하지 않는다.** 월별 파일명이 `2026074e` · `2025_216e`처럼 불규칙해서
  색인 페이지의 링크를 읽고, 각 XML의 `<taishoymtonen>`(대상 월)으로 실제 기간을 확인한다.
⚠ **금액 단위는 百万円**이다. XML 어디에도 안 적혀 있어(XSL에만 있다) 2026-06 수출을
  BOJ 국제수지 재화수출과 대조해 확인했다 — 관세청 10.93조엔 / BOP 10.48조엔(BOP는
  FOB·소유권 기준 조정분만큼 낮다). 조엔 = 원값 ÷ 1,000,000.
⚠ **음수 표기가 두 가지다**: 총액 페이지는 `△634,500`, 국가별 페이지는 `-634,500`.
⚠ 속보(Provisional)라 이후 확보치로 개정된다.
"""

CUSTOMS_INDEX = "https://www.customs.go.jp/toukei/shinbun/happyou_e.htm"
CUSTOMS_BASE = "https://www.customs.go.jp/toukei/shinbun/"
_MONTHS = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
           "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12}
_releases_cache: list[dict[str, Any]] | None = None      # 프로세스당 1회만 받는다


def _cnum(s: str | None) -> float | None:
    """'11,511,798' → 11511798.0 · '△634,500' → -634500.0 · '' → None."""
    if s is None:
        return None
    t = str(s).strip().replace(",", "").replace("\u2206", "-").replace("\u25b3", "-").replace("\u2212", "-")
    if not t or t in ("-", "..."):
        return None
    try:
        return float(t)
    except ValueError:
        return None


def _tag(src: str, name: str) -> str:
    m = re.search(rf"<{name}>(.*?)</{name}>", src, re.S)
    return m.group(1).strip() if m else ""


def _period_key(text: str) -> str:
    """'July 2026' → '2026-07'."""
    m = re.search(r"([A-Za-z]+)\s+(\d{4})", text or "")
    if not m:
        return text or ""
    mon = _MONTHS.get(m.group(1).lower())
    return f"{m.group(2)}-{mon:02d}" if mon else text


def _load_customs(months: int) -> list[dict[str, Any]]:
    """최신 월보부터 months개. 색인 링크 순서를 믿되 대상 월은 XML에서 읽어 확인한다."""
    global _releases_cache
    if _releases_cache is not None and len(_releases_cache) >= months:
        return _releases_cache[:months]
    idx = get_text(CUSTOMS_INDEX, encoding="utf-8")
    links: list[str] = []
    for href in re.findall(r'href="([^"]*trade-st_e/[^"]+\.xml)"', idx):
        url = CUSTOMS_BASE + href.lstrip("./")
        if url not in links:
            links.append(url)
    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    for url in links[: months * 3]:                       # 반기보 등 다른 발표가 섞여 있다
        if len(out) >= months:
            break
        try:
            xml = get_bytes(url).decode("utf-8", "replace")
        except Exception:
            continue
        head = _tag(xml, "sogakutsuki") or xml
        period = _period_key(_tag(xml, "taishoymtonen"))
        if not re.match(r"^\d{4}-\d{2}$", period) or period in seen:
            continue
        seen.add(period)
        out.append({"period": period, "url": url, "xml": xml,
                    "title": _tag(xml, "title"), "released": _tag(xml, "kohyoymd")})
    _releases_cache = out
    return out


def _commodity_page(xml: str, direction: str) -> str:
    """'Imports by Principal Commodity(WORLD)' 페이지 블록. pg 번호를 믿지 않고 제목으로 찾는다."""
    for blk in re.findall(r"<shuyochiikikunihin [^>]*>(.*?)</shuyochiikikunihin>", xml, re.S):
        title = _tag(blk, "title").upper().replace(" ", "")
        if title.startswith(direction.upper()) and "WORLD" in title:
            return blk
    return ""


def fetch_customs(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """yaml 예시:
        method: api
        source: japan_customs
        section: total | country | import_commodity | export_commodity
        items: ["CHINA", "U.S.A."]      # country·commodity 절에서 고를 항목(대소문자 무시, 부분일치)
        months: 3
        quantity: true                   # commodity 절에서 수량(원유 TKL·LNG TMT 등)도 함께
    """
    section = str(ind.get("section") or "total").lower()
    months = int(ind.get("months") or 3)
    items = {_norm(x) for x in (ind.get("items") or [])}
    want_qty = bool(ind.get("quantity"))

    rels = _load_customs(months)
    if not rels:
        return result(ind, "fail", error="관세청 색인에서 월보 XML을 찾지 못함",
                      source_url=CUSTOMS_INDEX)

    obs: list[dict[str, Any]] = []
    for rel in rels:
        d, xml = rel["period"], rel["xml"]
        if section == "total":
            blk = re.search(r"<sogakutsuki [^>]*>(.*?)</sogakutsuki>", xml, re.S)
            if not blk:
                continue
            b = blk.group(1)
            for key, name in (("export", "수출액(조엔)"), ("import", "수입액(조엔)"),
                              ("sashihiki", "무역수지(조엔)")):
                part = re.search(rf"<{key}>(.*?)</{key}>", b, re.S)
                if not part:
                    continue
                v = _cnum(_tag(part.group(1), "sogakutonen"))
                if v is None:
                    continue
                obs.append({"date": d, "value": round(v / 1e6, 3), "label": name})
            ex = re.search(r"<export>(.*?)</export>", b, re.S)
            im = re.search(r"<import>(.*?)</import>", b, re.S)
            for part, name in ((ex, "수출 전년비(%)"), (im, "수입 전년비(%)")):
                v = _cnum(_tag(part.group(1), "nobiritsu")) if part else None
                if v is not None:
                    obs.append({"date": d, "value": v, "label": name})

        elif section == "country":
            for info in re.findall(r"<chiikikunisogakuinfo>(.*?)</chiikikunisogakuinfo>", xml, re.S):
                nm = html.unescape(_tag(info, "chiikikuni")).upper()
                if items and _norm(nm) not in items:
                    continue
                for key, suffix in (("exportkagakue", "수출액(조엔)"), ("importkagakue", "수입액(조엔)")):
                    v = _cnum(_tag(info, key))
                    if v is not None:
                        obs.append({"date": d, "value": round(v / 1e6, 3),
                                    "label": f"{nm} {suffix}"})
                v = _cnum(_tag(info, "sashihikikagakue"))
                if v is not None:
                    obs.append({"date": d, "value": round(v / 1e6, 3), "label": f"{nm} 수지(조엔)"})

        elif section in ("import_commodity", "export_commodity"):
            direction = "Imports" if section.startswith("import") else "Exports"
            blk = _commodity_page(xml, f"{direction}byPrincipalCommodity")
            if not blk:
                continue
            for info in re.findall(r"<shuyochiikikunihininfo>(.*?)</shuyochiikikunihininfo>", blk, re.S):
                nm = html.unescape(_tag(info, "shuyoshohin")).upper().strip()
                if items and _norm(nm) not in items:
                    continue
                v = _cnum(_tag(info, "kagaku"))
                if v is not None:
                    obs.append({"date": d, "value": round(v / 1e6, 3), "label": f"{nm} 금액(조엔)"})
                y = _cnum(_tag(info, "kagakunobiritsu"))
                if y is not None:
                    obs.append({"date": d, "value": y, "label": f"{nm} 금액 전년비(%)"})
                if want_qty:
                    q, unit_ = _cnum(_tag(info, "suryo")), _tag(info, "tani").strip()
                    if q is not None:
                        obs.append({"date": d, "value": q, "label": f"{nm} 수량({unit_ or 'n/a'})"})
                    qy = _cnum(_tag(info, "suryonobiritsu"))
                    if qy is not None:
                        obs.append({"date": d, "value": qy, "label": f"{nm} 수량 전년비(%)"})
        else:
            return result(ind, "fail", error=f"알 수 없는 section: {section}")

    if not obs:
        return result(ind, "fail",
                      error=f"항목을 찾지 못함(section={section}, items={sorted(items)}) — 이름은 XML 표기와 정확히 일치해야 한다",
                      source_url=rels[0]["url"])
    return result(ind, "ok", observations=obs, source_url=rels[0]["url"],
                  note=(ind.get("note") or ""))
