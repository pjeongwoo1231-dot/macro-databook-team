"""시리즈 메타데이터 — 단위·주기·계절조정을 원천에서 받아 캐시한다.

## 왜 필요한가
`result()` 스키마에는 `unit` 필드가 처음부터 있었는데 316개 지표 중 30개(9.5%)만 채워져 있었고,
indicators.yaml에 명시된 건 2개뿐이었다. 그 공백이 2026-08-26에 확인된 판독 사고 전부의 원인이다.

  - 침체확률 0.6 → 60%인지 0.6%인지 알 수 없었다 (실제로는 0.6%)
  - 구리/금 0.001 → 무슨 단위의 비율인지 표시가 없었다
  - NBS 중국 CPI → "전년동월=100 지수"라 100을 빼야 하는데 그 사실이 note 본문에만 있었다

단위를 사람이 316줄 적는 게 아니라, **원천이 이미 갖고 있는 메타를 긁어온다.**
FRED는 `/fred/series`가 units·frequency·seasonal_adjustment를 준다.

## 설계
- 캐시는 `cache/series_meta.json` 하나. 갱신은 `python -m databook seriesmeta`.
- fetcher는 이 캐시를 읽어 `result()`의 unit 등을 채운다 — 수집 때마다 메타를 다시 받지 않는다.
- **FRED가 아닌 소스는 자동으로 못 채운다.** 그건 빈 채로 두고 `--report`가 목록을 뽑아준다.
  빈 것을 그럴듯하게 추측해 채우면 위 사고가 되풀이된다.
"""
from __future__ import annotations

import json
import time
from typing import Any

from .core import CACHE_DIR, YAML_PATH, load_env

META_PATH = CACHE_DIR / "series_meta.json"
FRED_SERIES = "https://api.stlouisfed.org/fred/series"


def _yaml_indicators() -> list[dict[str, Any]]:
    import yaml
    d = yaml.safe_load(open(YAML_PATH, encoding="utf-8"))
    out = []
    for k, v in d.items():
        if k == "sources":
            continue
        out.extend(v)
    return out


def fred_series_ids() -> list[str]:
    ids: set[str] = set()
    for ind in _yaml_indicators():
        if ind.get("source") != "fred":
            continue
        sid = ind.get("series_id")
        for x in ([sid] if isinstance(sid, str) else (sid or [])):
            if x:
                ids.add(str(x))
    return sorted(ids)


def load() -> dict[str, dict[str, Any]]:
    if not META_PATH.exists():
        return {}
    try:
        return json.load(open(META_PATH, encoding="utf-8"))
    except Exception:
        return {}


def refresh(sleep: float = 0.35) -> tuple[int, int, list[str]]:
    """FRED 시리즈 메타를 받아 캐시를 갱신. (성공, 실패, 실패ID) 반환."""
    from .fetchers.base import get_json

    env = load_env()
    key = env.get("FRED_API_KEY", "")
    if not key:
        raise RuntimeError("FRED_API_KEY 없음 (.env 확인)")

    meta = load()
    ok = fail = 0
    failed: list[str] = []
    for sid in fred_series_ids():
        try:
            d = get_json(f"{FRED_SERIES}?series_id={sid}&api_key={key}&file_type=json")
            s = d["seriess"][0]
            meta[sid] = {
                "source": "fred",
                "title": s.get("title", ""),
                "unit": s.get("units_short") or s.get("units", ""),
                "unit_long": s.get("units", ""),
                "frequency": s.get("frequency_short") or s.get("frequency", ""),
                "seasonal_adjustment": s.get("seasonal_adjustment_short", ""),
                "last_updated": s.get("last_updated", ""),
            }
            ok += 1
        except Exception as e:
            fail += 1
            failed.append(f"{sid}: {type(e).__name__}")
        time.sleep(sleep)

    META_PATH.parent.mkdir(parents=True, exist_ok=True)
    json.dump(meta, open(META_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return ok, fail, failed


def for_series(series_id: str) -> dict[str, Any]:
    return load().get(str(series_id), {})


def coverage_report() -> dict[str, Any]:
    """소스별로 메타를 자동 취득할 수 있는지/없는지 집계. 못 채우는 것을 드러내는 게 목적이다."""
    meta = load()
    by_source: dict[str, dict[str, int]] = {}
    missing: list[str] = []
    for ind in _yaml_indicators():
        src = ind.get("source") or ind.get("method") or "(미지정)"
        row = by_source.setdefault(src, {"total": 0, "covered": 0})
        row["total"] += 1
        sid = ind.get("series_id")
        sids = [sid] if isinstance(sid, str) else (sid or [])
        if sids and all(str(x) in meta for x in sids):
            row["covered"] += 1
        elif ind.get("unit"):
            row["covered"] += 1
        else:
            missing.append(f"[{src}] {ind['name']}")
    return {"by_source": by_source, "missing": missing, "cached": len(meta)}


def run(report: bool = False) -> int:
    if not report:
        ok, fail, failed = refresh()
        print(f"FRED 시리즈 메타 갱신: 성공 {ok} · 실패 {fail} → {META_PATH}")
        for f in failed[:10]:
            print(f"  FAIL {f}")

    rep = coverage_report()
    print(f"\n메타 캐시 {rep['cached']}건 · 소스별 커버리지")
    for src, row in sorted(rep["by_source"].items(), key=lambda x: -x[1]["total"]):
        pct = row["covered"] / row["total"] * 100 if row["total"] else 0
        print(f"  {src:16s} {row['covered']:3d}/{row['total']:3d}  ({pct:5.1f}%)")

    miss = rep["missing"]
    print(f"\n메타 미확보 {len(miss)}건 — 자동 취득 경로가 없다. "
          f"추측해 채우지 말고 yaml에 unit을 직접 적을 것")
    for m in miss[:15]:
        print(f"  {m[:74]}")
    if len(miss) > 15:
        print(f"  ... {len(miss) - 15}건 더")
    return 0
