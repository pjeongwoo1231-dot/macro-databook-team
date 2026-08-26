"""단위 정합성 검사 — 채워진 단위와 실제 값이 서로 모순되는지 본다.

staleness.py가 "값이 안 변하는 방식으로 죽은 계열"을 잡는다면, 이쪽은
**"단위를 잘못 읽어서 생기는 사고"**를 잡는다. 2026-08-26에 확인된 사례들이 대상이다.

  - 침체확률 0.6을 60%로 읽음        → 퍼센트 계열의 값 범위 검사
  - 구리/금 0.001로 뭉개짐            → 유효숫자 소멸 검사
  - 반도체 수출 10배 격차             → 계열 내 급변 검사(fetcher에도 있으나 전 지표로 확대)
  - 중국 CPI "전년동월=100" 지수      → 지수 계열을 증감률로 오독하는 것 방지

검사기는 **틀렸다고 단정하지 않는다.** 정상적으로 100을 넘는 퍼센트(누적 수익률 등)도 있고
음수인 지수도 있다. 그래서 결과는 "확인 필요" 목록이지 오류 목록이 아니다.
사람이 한 번 보고 넘어간 항목은 yaml에 `unit_check: skip`으로 끌 수 있다.
"""
from __future__ import annotations

from typing import Any

# 퍼센트로 표시되는 단위 문자열들. FRED units_short가 '%'를 쓴다.
PCT_UNITS = {"%", "% YoY", "percent", "Percent"}


def _numeric(obs: list[dict[str, Any]]) -> list[float]:
    return [o["value"] for o in obs if isinstance(o.get("value"), (int, float))]


def check(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """확인이 필요한 항목 목록. 각 항목: name·kind·detail."""
    out: list[dict[str, Any]] = []
    for r in results:
        if r.get("status") != "ok" or r.get("unit_check") == "skip":
            continue
        name = r.get("name", "")
        unit = (r.get("unit") or "").strip()
        vals = _numeric(r.get("observations", []))
        if not vals:
            continue

        # 1) 퍼센트인데 값이 상식 범위를 크게 벗어남 — 단위 오해 또는 지수 혼입
        if unit in PCT_UNITS:
            extreme = [v for v in vals if abs(v) > 100]
            if extreme:
                out.append({"name": name, "kind": "퍼센트 범위",
                            "detail": f"단위 '{unit}'인데 |값|>100 인 관측 {len(extreme)}개 "
                                      f"(예: {extreme[0]}) — 지수 계열이 섞였거나 단위 오기재 가능"})

        # 2) 단위 미확보 — 채우라는 뜻이지 오류는 아니다. tier1만 보고한다(전량은 소음).
        if not unit and r.get("tier") == 1:
            out.append({"name": name, "kind": "단위 없음",
                        "detail": "tier1인데 단위 미확보 — 발표에 인용되는 지표이므로 yaml에 unit을 적을 것"})

        # 3) 유효숫자 소멸 — 표시 반올림으로 변화를 못 보는 값
        tiny = [v for v in vals if v != 0 and abs(v) < 0.001]
        if tiny:
            out.append({"name": name, "kind": "유효숫자",
                        "detail": f"|값|<0.001 인 관측 {len(tiny)}개 (예: {tiny[0]}) — "
                                  f"비율 지표라면 지수화해서 볼 것"})

        # 4) 같은 라벨 안에서 10배 이상 급변 — 집계기준·단위 혼입 신호
        #
        # ⚠ 순진하게 a/b 비율을 쓰면 0 근처 값에서 폭주한다. 실제로 TFP(1.2↔0.08),
        #   절사평균 CPI(2.7↔0.13), 일본 소매판매(-0.05↔-1.42)가 전부 오탐으로 걸렸다 —
        #   전부 증감률 계열이라 0을 오가는 게 정상이다.
        #   그래서 계열 중앙값 대비 충분히 큰 값끼리만 비교한다. 이러면 반도체 수출
        #   (24억 ↔ 124만처럼 자릿수가 다른 진짜 사고)은 남고 0 근처 노이즈는 빠진다.
        by_label: dict[str, list[float]] = {}
        for o in r.get("observations", []):
            if isinstance(o.get("value"), (int, float)):
                by_label.setdefault(o.get("label") or "", []).append(o["value"])
        for label, series in by_label.items():
            mags = sorted(abs(v) for v in series if v)
            if len(mags) < 2:
                continue
            median = mags[len(mags) // 2]
            floor = median * 0.1
            for a, b in zip(series, series[1:]):
                if abs(a) < floor or abs(b) < floor or not (a and b):
                    continue
                if a / b > 10 or b / a > 10:
                    out.append({"name": name, "kind": "자릿수 불일치",
                                "detail": f"'{label[:30]}' 계열에서 {a:,.6g} ↔ {b:,.6g} — "
                                          f"집계기준(월중 누계 등)이 섞였을 가능성"})
                    break
    return out


def run(results: list[dict[str, Any]] | None = None) -> int:
    if results is None:
        import json
        from .core import OUTPUT_DIR
        snaps = sorted(OUTPUT_DIR.glob("snapshot_*.json"))
        if not snaps:
            print("스냅샷이 없다 — 먼저 python -m databook run 을 돌릴 것")
            return 1
        results = json.load(open(snaps[-1], encoding="utf-8"))["indicators"]
        print(f"검사 대상: {snaps[-1].name} ({len(results)}개 지표)")

    findings = check(results)
    if not findings:
        print("단위 정합성 확인 필요 항목 없음")
        return 0

    by_kind: dict[str, list[dict[str, Any]]] = {}
    for f in findings:
        by_kind.setdefault(f["kind"], []).append(f)
    print(f"\n확인 필요 {len(findings)}건 — 오류 목록이 아니라 사람이 한 번 봐야 할 목록이다")
    for kind, items in sorted(by_kind.items(), key=lambda x: -len(x[1])):
        print(f"\n[{kind}] {len(items)}건")
        for f in items[:8]:
            print(f"  {f['name'][:34]:36s} {f['detail'][:76]}")
        if len(items) > 8:
            print(f"  ... {len(items) - 8}건 더")
    print("\n확인 후 문제없는 항목은 indicators.yaml에 unit_check: skip 을 넣어 끌 것")
    return 0
