"""컨센서스 서프라이즈 — actual(이미 수집 중) − forecast(FairEconomy 무료 캘린더).

`surprise.py`가 "무료 컨센서스 없음"이라 판단해 ΔDGS2로 우회했던 지점을 정면으로 채운다.
FairEconomy 미러는 forecast·previous만 주고 actual은 안 주므로(fetchers/calendar.py 참조),
actual은 vintage.py가 이미 쌓아둔 리니지에서 가져온다. 두 소스를 합치는 게 이 모듈의 전부다.

## 왜 first_seen 값을 actual로 쓰는가
시장 컨센서스는 "최초 발표치(advance estimate)"를 겨냥해 형성된다. 나중에 개정된 값과
비교하면 서프라이즈가 아니라 개정 크기를 재게 된다. 그래서 vintage.csv에서 그 (지표, 관측월)
조합이 **처음 등장한 스냅샷의 값**을 actual로 쓴다.

## 왜 MAPPING이 작고 명시적인가
FairEconomy의 영문 이벤트명("Core PCE Price Index m/m")과 이 파이프라인의 FRED series_id를
잘못 짝지으면 조용히 틀린 서프라이즈가 나온다(예: NEWORDER는 "core capital goods"지 "Durable
Goods Orders m/m"이 아니다). 그래서 매핑은 정의가 실제로 일치한다고 확인한 것만 담는다.
indicators.yaml과 같은 원칙 — 없는 것보다 틀린 게 낫지 않다.

## 알려진 한계
- FairEconomy는 롤링 1주만 제공한다. 과거 주의 forecast는 이 소스로 복구 불가 — archive는
  이 모듈을 쓰기 시작한 시점부터만 쌓인다.
- 이 컨센서스는 Bloomberg/Refinitiv 서베이 패널과 다른 표본이다. 근사치로 취급할 것.
- 개정치(예: NFP 벤치마크 개정)와 최초 발표치를 vintage.py가 구분해주지만, 그 구분이
  스냅샷 파이프라인의 실행 주기(일 1회)보다 촘촘한 개정에는 못 미친다.
"""
from __future__ import annotations

import csv
import re
from datetime import datetime, timezone
from typing import Any

from .core import OUTPUT_DIR
from .vintage import _load as _load_vintage

CONSENSUS_CSV = OUTPUT_DIR / "consensus.csv"
FIELDS = ["ff_title", "event_date", "pull_date", "forecast_raw", "previous_raw",
          "forecast_value", "label", "transform"]

# FairEconomy 이벤트명 → (우리 FRED series_id(label), 변환방식, 배율)
# 배율: FF 원문을 자연단위로 파싱한 뒤(K=1e3 등) 이 값으로 나누면 우리 계열의 단위와 맞는다.
# transform: level(그대로 비교) · mom_pct(전월비 재계산) · yoy_pct(전년비 재계산) ·
#            diff_level(전월 대비 증감) · qoq_saar_pct(전기비 연율화)
MAPPING: dict[str, tuple[str, str, float]] = {
    "CPI m/m":                       ("CPIAUCSL",   "mom_pct",     1),
    "Core CPI m/m":                  ("CPILFESL",   "mom_pct",     1),
    "CPI y/y":                       ("CPIAUCSL",   "yoy_pct",     1),
    "Core CPI y/y":                  ("CPILFESL",   "yoy_pct",     1),
    "Core PCE Price Index m/m":      ("PCEPILFE",   "mom_pct",     1),
    "PCE Price Index m/m":           ("PCEPI",      "mom_pct",     1),
    "PPI m/m":                       ("PPIFIS",     "mom_pct",     1),
    "Retail Sales m/m":              ("RSAFS",      "mom_pct",     1),
    "Non-Farm Employment Change":    ("PAYEMS",     "diff_level",  1000),  # FF는 인원 단위, PAYEMS는 천 명 단위
    "Unemployment Rate":             ("UNRATE",     "level",       1),
    "Unemployment Claims":           ("ICSA",       "level",       1),
    "New Home Sales":                ("HSN1F",      "level",       1000),  # FF는 채, HSN1F는 천 채 단위
    "Prelim GDP q/q":                ("GDPC1",      "qoq_saar_pct", 1),
    "Final GDP q/q":                 ("GDPC1",      "qoq_saar_pct", 1),
    "Revised UoM Consumer Sentiment": ("UMCSENT",   "level",       1),
    "Prelim UoM Consumer Sentiment": ("UMCSENT",    "level",       1),
}

_NUM_RE = re.compile(r"^(-?[\d,.]+)\s*([KMB%])?$")


def parse_ff_number(raw: str) -> float | None:
    """'0.2%' -> 0.2 · '150K' -> 150000.0(자연단위) · '-100.8B' -> -1.008e11 · '' -> None."""
    raw = (raw or "").strip()
    if not raw:
        return None
    m = _NUM_RE.match(raw)
    if not m:
        return None
    val = float(m.group(1).replace(",", ""))
    suf = m.group(2)
    if suf == "K":
        val *= 1_000
    elif suf == "M":
        val *= 1_000_000
    elif suf == "B":
        val *= 1_000_000_000
    # '%'와 접미사 없음은 배율 1 — 퍼센트는 이미 percent-point 단위로 쓰는 게 이 파이프라인 관례
    return val


def _read_archive() -> list[dict[str, Any]]:
    if not CONSENSUS_CSV.exists():
        return []
    with open(CONSENSUS_CSV, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def archive_calendar() -> tuple[int, int]:
    """이번 주 캘린더에서 MAPPING에 있는 이벤트만 추려 archive에 append.
    같은 (제목,이벤트일,오늘) 조합이 이미 있으면 forecast를 최신값으로 덮어쓴다
    (같은 날 여러 번 돌려도 중복이 쌓이지 않게). 반환: (신규추가, 갱신)"""
    from .fetchers.calendar import fetch_usd_events

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    rows = _read_archive()
    index = {(r["ff_title"], r["event_date"], r["pull_date"]): i for i, r in enumerate(rows)}

    added = updated = 0
    for ev in fetch_usd_events():
        title = ev.get("title", "")
        if title not in MAPPING:
            continue
        label, transform, scale = MAPPING[title]
        fc_raw = ev.get("forecast", "")
        fc_natural = parse_ff_number(fc_raw)
        fc_value = None if fc_natural is None else fc_natural / scale
        event_date = (ev.get("date") or "")[:10]
        key = (title, event_date, today)
        row = {
            "ff_title": title, "event_date": event_date, "pull_date": today,
            "forecast_raw": fc_raw, "previous_raw": ev.get("previous", ""),
            "forecast_value": "" if fc_value is None else fc_value,
            "label": label, "transform": transform,
        }
        if key in index:
            rows[index[key]] = row
            updated += 1
        else:
            rows.append(row)
            added += 1

    CONSENSUS_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(CONSENSUS_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    return added, updated


def _level_history(label: str) -> list[tuple[str, float, str]]:
    """label의 (관측일, 최초발표값, 최초등장 스냅샷일) 목록을 관측일 오름차순으로.
    최초발표값 = 그 obs_date가 vintage.csv에 처음 등장한 스냅샷의 값 — 나중 개정치가 아니라
    시장이 그때 봤던 원래 발표치. 세 번째 원소(first_seen)가 look-ahead 차단에 쓰인다."""
    by_obs: dict[str, list[tuple[str, float]]] = {}
    for r in _load_vintage():
        if r["label"] != label:
            continue
        by_obs.setdefault(r["obs_date"], []).append((r["snapshot_date"], float(r["value"])))
    out = []
    for od, seen in by_obs.items():
        seen.sort(key=lambda x: x[0])
        out.append((od, seen[0][1], seen[0][0]))
    out.sort(key=lambda x: x[0])
    return out


def _actual_for(label: str, transform: str, event_date: str) -> float | None:
    """event_date(YYYY-MM-DD)에 발표된 값으로 actual을 계산.

    ⚠ 이 함수의 첫 구현은 event_date의 앞 7자(YYYY-MM)로 관측을 찾았다. 그래서
    2026-08-27에 발표될 실업수당청구에 이미 수집된 8월 초 주간 관측이 붙어
    "발표 전에 서프라이즈가 계산되는" look-ahead가 났다. 주간 계열에서 특히 위험하다.

    지금은 vintage의 first_seen(그 관측이 처음 등장한 스냅샷일)을 써서
    **발표일 당일 또는 그 이후에 처음 나타난 관측**만 actual로 인정한다.
    아직 안 나온 발표는 None을 돌려주고, 그 이벤트는 서프라이즈 계산에서 빠진다.
    """
    hist = _level_history(label)
    # 발표일 이후 처음 등장한 관측 중 가장 이른 것 = 그 발표가 내놓은 값
    idx = next((i for i, (_, _, first_seen) in enumerate(hist) if first_seen >= event_date), None)
    if idx is None:
        return None
    _, v_t, _ = hist[idx]
    if transform == "level":
        return v_t
    if transform == "mom_pct":
        if idx == 0:
            return None
        v_prev = hist[idx - 1][1]
        return (v_t / v_prev - 1) * 100 if v_prev else None
    if transform == "yoy_pct":
        if idx < 12:
            return None
        v_prev = hist[idx - 12][1]
        return (v_t / v_prev - 1) * 100 if v_prev else None
    if transform == "diff_level":
        if idx == 0:
            return None
        return v_t - hist[idx - 1][1]
    if transform == "qoq_saar_pct":
        if idx == 0:
            return None
        v_prev = hist[idx - 1][1]
        return ((v_t / v_prev) ** 4 - 1) * 100 if v_prev else None
    return None


def surprises() -> list[dict[str, Any]]:
    """archive에 쌓인 이벤트 중 actual이 이미 수집된 것들의 서프라이즈(actual − forecast)."""
    out = []
    for r in _read_archive():
        if not r.get("forecast_value"):
            continue
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        if r["event_date"] > today:
            continue  # 아직 발표 전 — actual이 존재할 수 없다
        actual = _actual_for(r["label"], r["transform"], r["event_date"])
        if actual is None:
            continue
        forecast = float(r["forecast_value"])
        out.append({
            "title": r["ff_title"], "event_date": r["event_date"], "label": r["label"],
            "forecast": round(forecast, 3), "actual": round(actual, 3),
            "surprise": round(actual - forecast, 3), "pull_date": r["pull_date"],
        })
    # 같은 이벤트가 여러 pull_date로 archive됐으면 이벤트일에 가장 가까운(마지막) forecast만 남긴다
    latest: dict[tuple[str, str], dict[str, Any]] = {}
    for row in out:
        key = (row["title"], row["event_date"])
        if key not in latest or row["pull_date"] > latest[key]["pull_date"]:
            latest[key] = row
    return sorted(latest.values(), key=lambda r: r["event_date"], reverse=True)


def run() -> int:
    try:
        added, updated = archive_calendar()
        print(f"컨센서스 캘린더 적립: 신규 {added}건 · 갱신 {updated}건 → {CONSENSUS_CSV}")
    except Exception as e:
        # 실패 격리 — 캘린더 하나 못 받는다고 daily 배치 전체가 죽으면 안 된다.
        # FairEconomy는 무료 미러라 레이트리밋(429)이 흔하다. 이번 회차 적립만 건너뛴다.
        print(f"컨센서스 캘린더 수집 실패({type(e).__name__}: {e}) — 이번 회차는 건너뜀. "
              f"기존 archive와 서프라이즈 계산은 계속 진행")
    print(f"매핑된 이벤트 {len(MAPPING)}종 — 목록: {', '.join(sorted(MAPPING))[:200]}")

    sur = surprises()
    if not sur:
        print("\n서프라이즈 계산 가능한 건 아직 없음 — forecast를 적립한 이벤트가 실제로 "
              "발표돼 actual이 vintage에 들어와야 계산된다. 이 소스는 롤링 1주뿐이라 "
              "과거분은 복구 불가 — 오늘부터 쌓인다.")
        return 0
    print(f"\n서프라이즈 {len(sur)}건")
    for r in sur[:20]:
        sign = "+" if r["surprise"] >= 0 else ""
        print(f"  {r['event_date']}  {r['title']:32s} 실제 {r['actual']:>10} "
              f"vs 예상 {r['forecast']:>10}  서프라이즈 {sign}{r['surprise']}")
    return 0
