"""빈티지 인덱스 — 매일 쌓인 snapshot_YYYY-MM-DD.json을 데이터 리니지 테이블로 편다.

목적: "그 시점에 시장이 실제로 봤던 값"을 복원해 look-ahead bias 없이 되짚을 수 있게 한다.
새 수집이 아니다 — daily run이 이미 만들어 둔 스냅샷을 파싱만 한다.

핵심 개념 두 가지:
  first_seen  = 어떤 (지표, 관측일) 조합이 처음 등장한 스냅샷일 → "그 관측치가 언제 발표됐는가"의 근사치.
                실제 발표일보다 하루~며칠 늦을 수 있다(수집 파이프라인이 매일 도는 시차). 정밀한
                발표일이 필요하면 지표별 공식 캘린더와 대조해야 한다 — 이 인덱스는 근사 리니지다.
  revision    = 같은 관측일에 대해 나중 스냅샷에서 값이 바뀐 경우. 원계열 사후 개정(NFP 벤치마크
                개정 등)과 상대지수 재기준화(네이버 검색관심도 등)가 섞여 있으므로 구분 없이
                "값이 바뀌었다"만 보장한다 — 개정 사유 판정은 사람 몫이다.

CSV 하나(vintage.csv)에 append-only로 쌓는다. 매번 전체 스냅샷을 다시 훑지만(15개 기준 수 초),
스냅샷이 수백 개로 늘면 마지막 처리 스냅샷일을 커서로 남겨 증분 처리로 바꿀 것.
"""
from __future__ import annotations

import csv
import glob
import json
import os
from collections import defaultdict
from typing import Any

from .core import OUTPUT_DIR

VINTAGE_CSV = OUTPUT_DIR / "vintage.csv"
FIELDS = ["indicator", "label", "obs_date", "snapshot_date", "value", "team", "tier"]


def _snapshot_day(path: str) -> str:
    base = os.path.basename(path)
    return base[len("snapshot_"):-len(".json")]


def _iter_snapshots() -> list[str]:
    return sorted(glob.glob(str(OUTPUT_DIR / "snapshot_*.json")))


def build(out_path=None) -> tuple[int, int]:
    """전체 스냅샷을 훑어 vintage.csv를 새로 쓴다. (행 수, 스냅샷 수) 반환."""
    out_path = out_path or VINTAGE_CSV
    snaps = _iter_snapshots()
    rows: list[dict[str, Any]] = []
    for p in snaps:
        day = _snapshot_day(p)
        try:
            data = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        for r in data.get("indicators", []):
            if r.get("status") != "ok":
                continue
            for o in r.get("observations", []):
                v = o.get("value")
                if not isinstance(v, (int, float)):
                    continue  # 뉴스 헤드라인처럼 값이 문자열인 슬롯은 리니지 대상이 아니다
                rows.append({
                    "indicator": r["name"],
                    "label": o.get("label") or "",
                    "obs_date": o.get("date") or "",
                    "snapshot_date": day,
                    "value": v,
                    "team": r.get("team", ""),
                    "tier": r.get("tier", 2),
                })
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    return len(rows), len(snaps)


def _load() -> list[dict[str, Any]]:
    if not VINTAGE_CSV.exists():
        return []
    with open(VINTAGE_CSV, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def as_of(indicator: str, snapshot_date: str) -> dict[str, Any] | None:
    """그 스냅샷일 시점에 이 지표에 대해 실제로 알려져 있던 최신 관측치.
    백테스트에서 '그날 봤을 값'을 재구성할 때 쓴다."""
    rows = [r for r in _load() if r["indicator"] == indicator and r["snapshot_date"] <= snapshot_date]
    if not rows:
        return None
    rows.sort(key=lambda r: (r["obs_date"], r["snapshot_date"]))
    return rows[-1]


def revisions(indicator: str | None = None, min_change_pct: float = 0.5) -> list[dict[str, Any]]:
    """같은 관측일의 값이 스냅샷 간에 바뀐 사례. min_change_pct 미만은 부동소수 노이즈로 간주해 제외.

    첫 값이 0인 경우(그날 아직 값이 안 채워졌다가 다음 스냅샷에 채워진 경우)는 %변화가
    정의상 무한대라 순수 사후개정과 구분해 change_pct=None·filled_from_zero=True로 표시한다.
    이런 케이스는 대개 "발표 지연" 신호지 값 정정이 아니다.
    """
    by_key: dict[tuple[str, str, str], dict[str, float]] = defaultdict(dict)
    for r in _load():
        if indicator and r["indicator"] != indicator:
            continue
        key = (r["indicator"], r["label"], r["obs_date"])
        by_key[key][r["snapshot_date"]] = float(r["value"])

    out = []
    for (name, label, od), by_day in by_key.items():
        if len(by_day) < 2:
            continue
        days = sorted(by_day)
        v0, v1 = by_day[days[0]], by_day[days[-1]]
        if v0 == v1:
            continue
        filled_from_zero = (v0 == 0)
        pct = None if filled_from_zero else abs((v1 - v0) / v0 * 100)
        if pct is not None and pct < min_change_pct:
            continue
        out.append({
            "indicator": name, "label": label, "obs_date": od,
            "first_seen": days[0], "last_seen": days[-1],
            "first_value": v0, "last_value": v1,
            "change_pct": None if pct is None else round(pct, 1),
            "filled_from_zero": filled_from_zero,
            "n_snapshots": len(by_day),
        })
    out.sort(key=lambda r: (r["change_pct"] is None, -(r["change_pct"] or 0)))
    return out


def run(top: int = 20, like: str | None = None) -> int:
    n_rows, n_snaps = build()
    print(f"빈티지 인덱스 재구성: 스냅샷 {n_snaps}개 → {n_rows}행 → {VINTAGE_CSV}")

    revs = revisions()
    if like:
        revs = [r for r in revs if like in r["indicator"]]
    real = [r for r in revs if not r["filled_from_zero"]]
    filled = [r for r in revs if r["filled_from_zero"]]

    scope = f" ({like!r} 포함)" if like else ""
    print(f"\n사후개정 {len(real)}건{scope} (관측일 동일·값이 실제로 바뀜, 0.5%↑) "
          f"— 원계열 개정과 상대지수 재기준화가 섞여 있으므로 사유는 원문 대조 필요.\n"
          f"  퍼센트 정렬이라 값이 0에 가까운 소규모 계열이 상위를 채울 수 있다 — 특정 지표만 보려면 --like")
    for r in real[:top]:
        print(f"  {r['indicator'][:30]:32s} 관측 {r['obs_date']:12s} "
              f"{r['first_value']:>12,.2f} → {r['last_value']:>12,.2f} "
              f"({r['change_pct']:+.1f}%)  [{r['first_seen']} → {r['last_seen']}]")
    if len(real) > top:
        print(f"  ... {len(real) - top}건 더")

    print(f"\n0에서 채워짐 {len(filled)}건 — 개정이 아니라 발표 지연으로 그날은 값이 없었던 경우일 가능성")
    for r in filled[:5]:
        print(f"  {r['indicator'][:30]:32s} 관측 {r['obs_date']:12s} "
              f"0 → {r['last_value']:>12,.2f}  [{r['first_seen']} → {r['last_seen']}]")
    if len(filled) > 5:
        print(f"  ... {len(filled) - 5}건 더")

    print("\n조회: vintage.csv 직접 열거나 databook.vintage의 as_of()/revisions()를 코드에서 호출")
    return 0
