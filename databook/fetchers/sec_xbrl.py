"""SEC XBRL companyconcept — AI 캐펙스 기업의 부채·현금흐름. 키 불필요.

**왜 필요한가** — 볼트의 신용 블록(HY/IG OAS·EBP·GZ·BIS gap)은 전부 **시장이 매긴 가격**이다.
그런데 지금 미국 신용사이클의 중심에는 **AI 자본지출을 무엇으로 조달하는가**가 있고,
그건 가격이 아니라 **기업 재무제표**에 있다. 스프레드가 벌어지기 전에 대차대조표가 먼저 움직인다.

핵심 질문은 하나다: **자본지출을 영업현금흐름으로 대는가, 부채로 대는가.**
2026-08-26 실측(연간, 10-K 기준):

| 기업 | capex | 직전연도 | OCF−capex |
|---|---|---|---|
| MSFT | 115.9B | 64.6B | +67.0B |
| AMZN | 131.8B | 83.0B | — |
| GOOGL | 91.4B | 52.5B | +73.3B |
| META | 69.7B | 37.3B | +46.1B |
| **ORCL** | **55.7B** | 21.2B | **−23.7B** |

**오라클만 부호가 다르다.** 나머지는 벌어서 짓고 오라클은 빌려서 짓는다(총부채 129.5B).
이 구분이 "AI 캐펙스 = 신용 리스크"가 어디서 먼저 터지는지를 가른다.

**엔드포인트**: `https://data.sec.gov/api/xbrl/companyfacts/CIK<10자리>.json` (회사당 1회)

⚠ **`www.sec.gov`는 레이트리밋으로 막힌다**(Request Rate Threshold Exceeded).
  `data.sec.gov`만 쓴다. User-Agent는 반드시 설명형으로 보낸다.
⚠ **회사마다 XBRL 태그가 다르다.** 오라클엔 `LongTermDebtNoncurrent`가 아예 없고
  (404) `DebtLongtermAndShorttermCombinedAmount`를 쓴다. 아마존·엔비디아의 capex는
  `PaymentsToAcquireProductiveAssets`다.
⚠⚠ **"첫 번째로 값이 있는 태그"를 고르면 안 된다.** 아마존은 옛 태그에 2016년 값이,
  엔비디아는 2012년 값이 남아 있어서 그대로 최신값으로 실린다(실제로 겪었다).
  **각 태그의 최신 관측일을 비교해 가장 최신인 태그를 고른다.**
⚠⚠ **분기값을 쓰지 않는다.** 10-Q의 현금흐름표는 **연초누계**라 3분기 보고서의 capex는
  9개월치다. 차분 없이 쓰면 3배 부풀려진다. 그래서 여기서는 **10-K의 FY 값만** 쓰고,
  기간이 350~380일인 사실만 통과시킨다.
⚠ 부채 태그가 회사마다 달라 **정의가 완전히 같지 않다**(유동분 포함 여부 등).
  어떤 태그를 썼는지 라벨에 남긴다 — 기업 간 절대 수준 비교는 조심할 것.
"""
from __future__ import annotations

import datetime
from typing import Any

from .base import get_json, result

BASE = "https://data.sec.gov/api/xbrl/companyfacts"
_facts_cache: dict[int, dict[str, Any]] = {}   # 회사당 1회만 받는다(프로세스 캐시)
# 최신 관측이 이 일수 안이면 "현행 태그"로 보고 더 찾지 않는다(요청 수 절약)
_FRESH_DAYS = 500

# 지표 → 후보 태그(우선순위). instant=잔액(기간 없음) · flow=기간값
_METRICS: dict[str, tuple[str, bool, list[str]]] = {
    "debt": ("총부채(십억$)", True, [
        "DebtLongtermAndShorttermCombinedAmount", "LongTermDebtNoncurrent",
        "LongTermNotesPayable", "LongTermDebt"]),
    "capex": ("자본지출(십억$)", False, [
        "PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets",
        "PaymentsToAcquirePropertyPlantAndEquipmentExcludingCapitalizedInterest"]),
    "ocf": ("영업현금흐름(십억$)", False, [
        "NetCashProvidedByUsedInOperatingActivities",
        "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"]),
    "interest": ("이자비용(십억$)", False, [
        "InterestExpense", "InterestExpenseDebt", "InterestExpenseNonoperating",
        "InterestIncomeExpenseNet"]),
    # ⚠ 회사마다 발행 태그가 딴판이다. 구글은 `ProceedsFromDebtNetOfIssuanceCosts`,
    # 오라클은 `...SeniorLongTermDebt`를 쓴다. MSFT는 **발행 자체가 없어서**
    # 0에 가까운 값이 정상이다(부채를 줄이는 중) — "태그 없음"과 구분할 것.
    "issuance": ("장기채 발행액(십억$)", False, [
        "ProceedsFromIssuanceOfSeniorLongTermDebt", "ProceedsFromIssuanceOfLongTermDebt",
        "ProceedsFromDebtNetOfIssuanceCosts", "ProceedsFromIssuanceOfDebt",
        "ProceedsFromNotesPayable", "ProceedsFromDebtMaturingInMoreThanThreeMonths"]),
}


def _facts(cik: int) -> dict[str, Any]:
    """companyfacts는 **회사당 1회**만 받는다.

    태그마다 companyconcept를 치면 지표 3개·기업 5곳에 요청이 60건까지 늘어
    2분을 넘겼다(실측). companyfacts는 4MB쯤이지만 요청이 회사당 1건이라 훨씬 빠르고,
    SEC 레이트리밋에도 안전하다."""
    if cik not in _facts_cache:
        _facts_cache[cik] = get_json(f"{BASE}/CIK{cik:010d}.json")
    return _facts_cache[cik]


def _pick_tag(gaap: dict[str, Any], tags: list[str]) -> str:
    """후보 태그 중 **가장 최신 관측을 가진 것**을 고른다.

    ⚠ "첫 번째로 값이 있는 태그"를 쓰면 폐기된 태그의 옛 값이 최신값으로 실린다
    (아마존 capex 2016년 6.7B · 엔비디아 2012년 0.1B를 실제로 겪었다)."""
    best: tuple[str, str] | None = None
    for t in tags:
        u = ((gaap.get(t) or {}).get("units") or {}).get("USD")
        if not u:
            continue
        ends = [x["end"] for x in u if x.get("form") in ("10-Q", "10-K")]
        if ends:
            cand = (max(ends), t)
            if best is None or cand > best:
                best = cand
    return best[1] if best else ""


def _fy_rows(cik: int, tag: str, instant: bool) -> list[dict[str, Any]]:
    """10-K의 FY 사실만. flow는 기간이 1년(350~380일)인 것만 — 누계 오염을 막는다."""
    try:
        gaap = (_facts(cik).get("facts") or {}).get("us-gaap") or {}
    except Exception:
        return []
    unit = ((gaap.get(tag) or {}).get("units") or {}).get("USD")
    if not unit:
        return []                                     # 그 회사엔 없는 태그 — 다음 후보로
    out: list[dict[str, Any]] = []
    for x in unit:
        if x.get("form") != "10-K" or x.get("fp") != "FY":
            continue
        if not instant:
            if not x.get("start"):
                continue
            try:
                span = (datetime.date.fromisoformat(x["end"])
                        - datetime.date.fromisoformat(x["start"])).days
            except ValueError:
                continue
            if not 350 <= span <= 380:
                continue
        out.append(x)
    # ⚠ **같은 회계연도가 여러 번 들어 있다.** FY2025 값은 2025년 10-K에도, 2026년 10-K의
    # 비교표시분에도 실린다(`accn`·`filed`만 다름). 그대로 두면 표에 같은 해가 두 줄로 나오고
    # `points: 3`이 실제로는 2개년만 보여준다(실제로 겪었다).
    # **기준일별로 가장 나중에 제출된 값만** 남긴다 — 수정 재작성(restatement)도 이쪽이 맞다.
    latest: dict[str, dict[str, Any]] = {}
    for x in out:
        cur = latest.get(x["end"])
        if cur is None or str(x.get("filed", "")) >= str(cur.get("filed", "")):
            latest[x["end"]] = x
    return sorted(latest.values(), key=lambda r: r["end"])


def _best_tag(cik: int, tags: list[str], instant: bool) -> tuple[str, list[dict[str, Any]]]:
    """★ 가장 **최신 관측을 가진** 태그를 고른다 — 첫 태그를 그냥 쓰면 폐기된 태그의
    옛날 값(아마존 2016·엔비디아 2012)을 최신값으로 싣게 된다."""
    today = datetime.date.today()
    cands: list[tuple[str, str, list[dict[str, Any]]]] = []
    for tag in tags:
        rows = _fy_rows(cik, tag, instant)
        if not rows:
            continue
        last = rows[-1]["end"]
        try:
            age = (today - datetime.date.fromisoformat(last)).days
        except ValueError:
            age = 10**6
        if age <= _FRESH_DAYS:
            return tag, rows                          # 현행 태그를 찾았으면 즉시 채택
        cands.append((last, tag, rows))
    if not cands:
        return "", []
    cands.sort(reverse=True)
    return cands[0][1], cands[0][2]


def _quarters(cik: int, tags: list[str]) -> tuple[str, dict[str, float], dict[str, float]]:
    """분기값 복원 + 자체검증용 연간값.

    **왜 필요한가** — 10-K만 쓰면 갱신이 연 1회다. AI 자본지출은 분기마다 수십억 달러씩
    움직여서 대부분의 기간 동안 낡은 값을 보게 된다. 분기값은 6개월가량 최신이다.

    **복원 규칙** — SEC의 기간 사실을 `start`가 같은 것끼리 묶어 `end` 순으로 **연속 차분**한다.
    회사에 따라 3개월 개별값을 직접 태깅하기도 하고(MSFT의 10~12월), 누계만 내기도 하는데
    두 경우가 같은 사슬에 들어가므로 한 규칙으로 처리된다.

    ⚠⚠ **누계에서 앞 분기를 빼지 않으면 6월 분기가 2배로 부푼다.** 1~6월 누계를 그대로
    2분기로 쓰면 그렇게 된다(실제로 겪었다 — 구글 39.6B, 메타 29.5B로 나왔다).
    ⚠ **아마존은 10-Q에 TTM(12개월) 열을 태깅한다.** 연간 기준값으로 섞이면 안 되므로
    검증용 연간은 **10-K·FY만** 쓴다.
    """
    try:
        gaap = (_facts(cik).get("facts") or {}).get("us-gaap") or {}
    except Exception:
        return "", {}, {}
    tag = _pick_tag(gaap, tags)
    if not tag:
        return "", {}, {}

    latest: dict[tuple[str, str], dict[str, Any]] = {}
    for x in gaap[tag]["units"]["USD"]:
        if not x.get("start") or x.get("form") not in ("10-Q", "10-K"):
            continue
        k = (x["start"], x["end"])
        if k not in latest or str(x.get("filed", "")) >= str(latest[k].get("filed", "")):
            latest[k] = x
    facts = list(latest.values())

    def span(a: str, b: str) -> int:
        return (datetime.date.fromisoformat(b) - datetime.date.fromisoformat(a)).days

    fy = {x["end"]: float(x["val"]) for x in facts
          if x.get("form") == "10-K" and x.get("fp") == "FY" and 350 <= span(x["start"], x["end"]) <= 380}

    by_start: dict[str, list[tuple[str, float]]] = {}
    for x in facts:
        by_start.setdefault(x["start"], []).append((x["end"], float(x["val"])))
    q: dict[str, float] = {}
    for st, items in by_start.items():
        prev_end, prev_val = st, 0.0
        for end, val in sorted(set(items)):
            if 80 <= span(prev_end, end) <= 100:
                q[end] = val - prev_val
            prev_end, prev_val = end, val
    return tag, q, fy


def _reconcile(q: dict[str, float], fy: dict[str, float]) -> str:
    """분기합 = 연간인지 스스로 검사한다. 어긋나면 사유를 문자열로 돌려준다."""
    if not fy or not q:
        return ""
    fe = max(fy)
    quarters = [v for e, v in sorted(q.items()) if e <= fe][-4:]
    if len(quarters) < 4 or not fy[fe]:
        return ""
    gap = abs(sum(quarters) - fy[fe]) / abs(fy[fe]) * 100
    return "" if gap < 2 else f"분기합이 연간과 {gap:.1f}% 어긋남(FY {fe}) — 복원 규칙 재확인 필요"


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """yaml 예시:
        method: api
        source: sec_xbrl
        companies:
          - {ticker: MSFT, cik: 789019}
          - {ticker: ORCL, cik: 1341439}
        metrics: [capex, ocf, fcf]        # debt · capex · ocf · interest · issuance · fcf
        freq: quarterly                    # annual(기본) | quarterly — 잔액(debt)은 항상 연간
        points: 3                          # 최근 기간 N개
    """
    companies = ind.get("companies") or []
    if not companies:
        return result(ind, "fail", error="companies 미지정")
    metrics = [str(m).lower() for m in (ind.get("metrics") or ["capex", "ocf", "fcf"])]
    points = int(ind.get("points") or 3)
    quarterly = str(ind.get("freq") or "annual").lower().startswith("q")

    obs: list[dict[str, Any]] = []
    errors: list[str] = []
    for c in companies:
        tk = str(c.get("ticker") or "?")
        try:
            cik = int(c["cik"])
        except Exception:
            errors.append(f"{tk}: cik 없음")
            continue
        cache: dict[str, list[dict[str, Any]]] = {}
        for m in metrics:
            if m == "fcf":
                continue                              # 아래에서 파생 계산
            spec = _METRICS.get(m)
            if not spec:
                errors.append(f"{tk}: 알 수 없는 metric {m}")
                continue
            label, instant, tags = spec
            if quarterly and not instant:
                tag, q, fy = _quarters(cik, tags)
                if not q:
                    errors.append(f"{tk}/{m}: 분기 복원 실패")
                    continue
                warn = _reconcile(q, fy)
                if warn:
                    errors.append(f"{tk}/{m}: {warn}")
                cache[m] = [{"end": e, "val": v} for e, v in sorted(q.items())]
                for e, v in sorted(q.items())[-points:][::-1]:
                    obs.append({"date": e, "value": round(v / 1e9, 1),
                                "label": f"{tk} {label} [{tag}]"})
                continue
            tag, rows = _best_tag(cik, tags, instant)
            if not rows:
                errors.append(f"{tk}/{m}: 해당 태그 없음")
                continue
            cache[m] = rows
            for r in rows[-points:][::-1]:
                obs.append({"date": r["end"], "value": round(r["val"] / 1e9, 1),
                            "label": f"{tk} {label} [{tag}]"})
        if "fcf" in metrics:
            # ⚠ **두 계열의 주기가 같아야 한다.** 분기 capex에서 연간 OCF를 빼면
            # MSFT가 +147B, 오라클은 부호까지 뒤집힌다(실제로 겪었다).
            def _series(key: str) -> list[dict[str, Any]] | None:
                if cache.get(key):
                    return cache[key]
                if quarterly:
                    _t, qq, _f = _quarters(cik, _METRICS[key][2])
                    return [{"end": e, "val": v} for e, v in sorted(qq.items())] or None
                _t, rows = _best_tag(cik, _METRICS[key][2], False)
                return rows or None

            oc, cx = _series("ocf"), _series("capex")
            if oc and cx:
                by_end = {r["end"]: r["val"] for r in cx}
                pairs = [(r["end"], r["val"] - by_end[r["end"]]) for r in oc if r["end"] in by_end]
                for end, v in pairs[-points:][::-1]:
                    obs.append({"date": end, "value": round(v / 1e9, 1),
                                "label": f"{tk} 영업현금흐름−자본지출(십억$)"})
            else:
                errors.append(f"{tk}/fcf: 구성요소 부족")

    if not obs:
        return result(ind, "fail", error="; ".join(errors) or "관측치 없음")
    res = result(ind, "ok", observations=obs, unit="십억 달러",
                 source_url="https://data.sec.gov/api/xbrl/companyfacts/")
    if errors:
        res["error"] = "; ".join(errors)
    return res
