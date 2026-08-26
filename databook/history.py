"""장기 시계열 수집 — 백테스트·회귀 분석용.

`run`은 '오늘 상태'를 보려고 최신 6개 관측치만 받는다. 이 모듈은 반대로
**전체 히스토리를 CSV로 축적**한다. 산출물은 사람이 읽는 노트가 아니라
분석 스크립트가 먹는 데이터라, Obsidian이 아니라 `output/history/`에 쓴다.

증분 수집: CSV가 이미 있으면 마지막 날짜 이후만 받아 이어붙인다.
FRED는 개정(revision)이 잦으므로 겹치는 구간은 **새로 받은 값으로 덮어쓴다**.
"""
from __future__ import annotations

import csv
import json
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

from .core import OUTPUT_DIR, all_indicators, load_env, load_registry
from .fetchers.base import get_json

BASE = "https://api.stlouisfed.org/fred/series/observations"
HISTORY_DIR = OUTPUT_DIR / "history"
DEFAULT_SINCE = "2000-01-01"

# 개정 반영을 위해 이어받기 시작점을 이만큼 앞당긴다
REVISION_LOOKBACK_DAYS = 400


def _series_ids(ind: dict[str, Any]) -> list[str]:
    ids = ind.get("series_id")
    if not ids:
        return []
    return [ids] if isinstance(ids, str) else list(ids)


def fred_targets(indicators: list[dict[str, Any]], tier: int | None = None,
                 only: list[str] | None = None) -> dict[str, dict[str, Any]]:
    """series_id → 메타. 같은 계열이 여러 지표에 걸쳐 있으면 첫 지표 기준으로 기록한다."""
    out: dict[str, dict[str, Any]] = {}
    for ind in indicators:
        if ind.get("source") != "fred" or ind.get("method") != "api":
            continue
        if tier is not None and int(ind.get("tier", 2)) != tier:
            continue
        for sid in _series_ids(ind):
            if only and sid not in only:
                continue
            out.setdefault(sid, {
                "series_id": sid,
                "name": ind["name"],
                "team": ind.get("team", ""),
                "tier": ind.get("tier", 2),
                "units": str(ind.get("units", "")),
            })
    return out


def gpr_targets(indicators: list[dict[str, Any]], tier: int | None = None,
                only: list[str] | None = None) -> dict[str, dict[str, Any]]:
    """GPR 컬럼 → 메타. `method: scrape` + `source: gpr` 지표의 `gpr_series` 를 그대로 쓴다.

    FRED·Yahoo 와 달리 원본이 한 파일에 전 컬럼을 담고 있어, 대상이 몇 개든 다운로드는 1회다.
    """
    out: dict[str, dict[str, Any]] = {}
    for ind in indicators:
        if ind.get("method") != "scrape" or ind.get("source") != "gpr":
            continue
        if tier is not None and int(ind.get("tier", 2)) != tier:
            continue
        cols = ind.get("gpr_series", "GPR")
        if isinstance(cols, str):
            cols = [cols]
        for col in cols:
            if only and col not in only:
                continue
            out.setdefault(col, {
                "series_id": col,
                "name": ind["name"],
                "team": ind.get("team", ""),
                "tier": ind.get("tier", 2),
                "units": "index",
            })
    return out


def crea_targets(indicators: list[dict[str, Any]], tier: int | None = None,
                 only: list[str] | None = None) -> dict[str, dict[str, Any]]:
    """CREA 계열 키 → 메타. `source: crea` 지표의 `crea_series` 를 읽는다."""
    out: dict[str, dict[str, Any]] = {}
    for ind in indicators:
        if ind.get("source") != "crea":
            continue
        if tier is not None and int(ind.get("tier", 2)) != tier:
            continue
        keys = ind.get("crea_series", "CREA_RU_FOSSIL_EUR")
        if isinstance(keys, str):
            keys = [keys]
        for key in keys:
            if only and key not in only:
                continue
            out.setdefault(key, {
                "series_id": key,
                "name": ind["name"],
                "team": ind.get("team", ""),
                "tier": ind.get("tier", 2),
                "units": "EUR bn/month",
            })
    return out


def read_csv(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    rows: dict[str, str] = {}
    with path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if row.get("date"):
                rows[row["date"]] = row.get("value", "")
    return rows


def write_csv(path: Path, rows: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "value"])
        for d in sorted(rows):
            w.writerow([d, rows[d]])


def fetch_history(series_id: str, api_key: str, start: str, units: str = "") -> list[tuple[str, str]]:
    """limit 없이 요청하면 FRED가 전체 구간을 오름차순으로 준다."""
    url = (f"{BASE}?series_id={series_id}&api_key={api_key}&file_type=json"
           f"&observation_start={start}&sort_order=asc")
    if units:
        url += f"&units={units}"
    data = get_json(url)
    out: list[tuple[str, str]] = []
    # ⚠ CBO 계열(GDPPOT·NROU)은 **미래 전망치를 포함**한다. 실적 시계열에 섞으면
    #   백분위·z가 오염된다(2026-08-21 실측: 2036년까지 값이 들어왔다). 오늘까지만 남긴다.
    today = date.today().isoformat()
    for row in data.get("observations", []):
        v = row.get("value")
        if v in (".", "", None):  # FRED 결측 표기
            continue
        if row["date"] > today:
            continue
        out.append((row["date"], v))
    return out


def _resume_from(existing: dict[str, str], since: str) -> str:
    if not existing:
        return since
    last = max(existing)
    try:
        d = datetime.strptime(last, "%Y-%m-%d").date() - timedelta(days=REVISION_LOOKBACK_DAYS)
    except ValueError:
        return since
    return max(d, datetime.strptime(since, "%Y-%m-%d").date()).isoformat()


def yahoo_targets(indicators: list[dict[str, Any]], tier: int | None = None,
                  only: list[str] | None = None) -> dict[str, dict[str, Any]]:
    """yahoo_finance 스크레이프 지표의 심볼. FRED가 못 주는 한국·원자재 가격이 여기 있다."""
    out: dict[str, dict[str, Any]] = {}
    for ind in indicators:
        if ind.get("source") != "yahoo_finance":
            continue
        if tier is not None and int(ind.get("tier", 2)) != tier:
            continue
        syms = ind.get("symbol")
        if not syms:
            continue
        for s in ([syms] if isinstance(syms, str) else syms):
            if only and s not in only:
                continue
            out.setdefault(s, {"series_id": s, "name": ind["name"],
                               "team": ind.get("team", ""), "tier": ind.get("tier", 2),
                               "units": ""})
    return out


def fetch_yahoo_history(symbol: str, start: str) -> list[tuple[str, str]]:
    """Yahoo chart API — 종가만. OHLC 분해가 필요하면 events 모듈을 쓴다."""
    import json
    import urllib.parse
    import urllib.request
    from datetime import datetime as _dt

    from .fetchers.base import BROWSER_UA
    p1 = int(_dt.strptime(start, "%Y-%m-%d").timestamp())
    p2 = int(_dt.utcnow().timestamp())
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(symbol)}"
           f"?period1={p1}&period2={p2}&interval=1d")
    req = urllib.request.Request(url, headers={"User-Agent": BROWSER_UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read().decode("utf-8"))
    res = data["chart"]["result"][0]
    closes = res["indicators"]["quote"][0]["close"]
    out: list[tuple[str, str]] = []
    for i, ts in enumerate(res["timestamp"]):
        c = closes[i]
        if c in (None, 0):
            continue
        out.append((_dt.utcfromtimestamp(ts).strftime("%Y-%m-%d"), repr(float(c))))
    return out


def collect(since: str = DEFAULT_SINCE, tier: int | None = None,
            only: list[str] | None = None, full: bool = False,
            dry_run: bool = False) -> int:
    env = load_env()
    key = env.get("FRED_API_KEY", "")
    if not key and not dry_run:
        print("FRED_API_KEY 없음 (.env 확인) — `python -m databook setup` 으로 설정")
        return 1

    inds = all_indicators(load_registry())
    targets = fred_targets(inds, tier=tier, only=only)
    ytargets = yahoo_targets(inds, tier=tier, only=only)
    gtargets = gpr_targets(inds, tier=tier, only=only)
    ctargets = crea_targets(inds, tier=tier, only=only)
    if not targets and not ytargets and not gtargets and not ctargets:
        print("대상 계열이 없다. --tier/--only 조건을 확인할 것")
        return 1
    print(f"FRED {len(targets)}개 · Yahoo {len(ytargets)}개 · GPR {len(gtargets)}개 · CREA {len(ctargets)}개 · 시작 {since}" + (" · 전체 재수집" if full else " · 증분"))

    manifest: list[dict[str, Any]] = []
    ok = fail = 0
    for i, (sid, meta) in enumerate(sorted(targets.items()), 1):
        path = HISTORY_DIR / f"{sid}.csv"
        existing = {} if full else read_csv(path)
        start = since if full else _resume_from(existing, since)
        if dry_run:
            print(f"  [{i:3d}/{len(targets)}] {sid:22s} start={start} (dry-run)")
            continue
        try:
            fetched = fetch_history(sid, key, start, meta["units"])
        except Exception as e:
            print(f"  [{i:3d}/{len(targets)}] {sid:22s} FAIL {type(e).__name__}: {e}")
            fail += 1
            continue
        before = len(existing)
        existing.update(dict(fetched))  # 겹치는 구간은 새 값으로 덮어쓴다(개정 반영)
        write_csv(path, existing)
        added = len(existing) - before
        ok += 1
        print(f"  [{i:3d}/{len(targets)}] {sid:22s} {len(existing):>6,}행 (+{added}) "
              f"{min(existing) if existing else '-'} ~ {max(existing) if existing else '-'}  {meta['name'][:26]}")
        manifest.append({
            **meta,
            "rows": len(existing),
            "start": min(existing) if existing else None,
            "end": max(existing) if existing else None,
            "csv": f"history/{sid}.csv",
            "fetched_at": date.today().isoformat(),
        })

    for i, (sym, meta) in enumerate(sorted(ytargets.items()), 1):
        path = HISTORY_DIR / f"{sym.lstrip('^').replace('=', '_')}.csv"
        existing = {} if full else read_csv(path)
        start = since if full else _resume_from(existing, since)
        if dry_run:
            print(f"  [Y{i:2d}/{len(ytargets)}] {sym:22s} start={start} (dry-run)")
            continue
        try:
            fetched = fetch_yahoo_history(sym, start)
        except Exception as e:
            print(f"  [Y{i:2d}/{len(ytargets)}] {sym:22s} FAIL {type(e).__name__}: {e}")
            fail += 1
            continue
        before = len(existing)
        existing.update(dict(fetched))
        write_csv(path, existing)
        ok += 1
        print(f"  [Y{i:2d}/{len(ytargets)}] {sym:22s} {len(existing):>6,}행 (+{len(existing)-before}) "
              f"{min(existing) if existing else '-'} ~ {max(existing) if existing else '-'}  {meta['name'][:26]}")
        manifest.append({**meta, "rows": len(existing),
                         "start": min(existing) if existing else None,
                         "end": max(existing) if existing else None,
                         "csv": f"history/{path.name}", "source": "yahoo_finance",
                         "fetched_at": date.today().isoformat()})

    if gtargets:
        # GPR 은 월간이라 증분이 의미가 없다. 한 번 받아 전 이력(1900~)을 덮어쓴다.
        try:
            from .fetchers.scrape import gpr_labels, load_gpr_series
            gseries = load_gpr_series() if not dry_run else {}
        except Exception as e:
            print(f"  [GPR] 다운로드/파싱 실패 {type(e).__name__}: {e}")
            gseries = None
            fail += 1
        if gseries is not None:
            labels = gpr_labels() if not dry_run else {}
            for i, (col, meta) in enumerate(sorted(gtargets.items()), 1):
                if dry_run:
                    print(f"  [G{i:2d}/{len(gtargets)}] {col:22s} 전 이력 (dry-run)")
                    continue
                pts = gseries.get(col)
                if not pts:
                    print(f"  [G{i:2d}/{len(gtargets)}] {col:22s} FAIL 컬럼 미발견 — 원본 구조 변경 확인")
                    fail += 1
                    continue
                rows = {d: f"{v:.2f}" for d, v in pts}
                path = HISTORY_DIR / f"{col}.csv"
                before = len(read_csv(path))
                write_csv(path, rows)
                ok += 1
                print(f"  [G{i:2d}/{len(gtargets)}] {col:22s} {len(rows):>6,}행 (+{len(rows)-before}) "
                      f"{min(rows)} ~ {max(rows)}  GPR {labels.get(col, col)}")
                manifest.append({**meta, "rows": len(rows), "start": min(rows), "end": max(rows),
                                 "csv": f"history/{col}.csv", "source": "gpr",
                                 "source_url": "https://www.matteoiacoviello.com/gpr.htm",
                                 "fetched_at": date.today().isoformat()})

    if ctargets:
        # CREA 도 월간이라 증분이 무의미하다. 전 이력(2022-02~)을 한 번 받아 덮어쓴다.
        try:
            from .fetchers.crea import load_crea_monthly, series_labels
            cseries = load_crea_monthly() if not dry_run else {}
        except Exception as e:
            print(f"  [CREA] 수집 실패 {type(e).__name__}: {e}")
            cseries = None
            fail += 1
        if cseries is not None:
            clabels = series_labels() if not dry_run else {}
            for i, (key, meta) in enumerate(sorted(ctargets.items()), 1):
                if dry_run:
                    print(f"  [C{i:2d}/{len(ctargets)}] {key:22s} 전 이력 (dry-run)")
                    continue
                pts = cseries.get(key)
                if not pts:
                    print(f"  [C{i:2d}/{len(ctargets)}] {key:22s} FAIL 계열 미발견")
                    fail += 1
                    continue
                rows = {d: f"{v:.3f}" for d, v in pts}
                path = HISTORY_DIR / f"{key}.csv"
                before = len(read_csv(path))
                write_csv(path, rows)
                ok += 1
                print(f"  [C{i:2d}/{len(ctargets)}] {key:22s} {len(rows):>6,}행 (+{len(rows)-before}) "
                      f"{min(rows)} ~ {max(rows)}  {clabels.get(key, key)}")
                manifest.append({**meta, "rows": len(rows), "start": min(rows), "end": max(rows),
                                 "csv": f"history/{key}.csv", "source": "crea",
                                 "source_url": "https://www.russiafossiltracker.com/",
                                 "fetched_at": date.today().isoformat()})

    if dry_run:
        return 0
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    mpath = HISTORY_DIR / "_manifest.json"
    prev = {}
    if mpath.exists():
        try:
            prev = {m["series_id"]: m for m in json.loads(mpath.read_text(encoding="utf-8")).get("series", [])}
        except Exception:
            prev = {}
    prev.update({m["series_id"]: m for m in manifest})
    mpath.write_text(json.dumps({
        "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "series_count": len(prev),
        "series": sorted(prev.values(), key=lambda m: m["series_id"]),
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n완료: 성공 {ok} / 실패 {fail} / 전체 {len(targets) + len(ytargets) + len(gtargets) + len(ctargets)}")
    print(f"  → {HISTORY_DIR}")
    print(f"  → {mpath}")
    return 0
