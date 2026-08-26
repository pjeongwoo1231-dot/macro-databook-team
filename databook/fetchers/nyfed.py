"""NY Fed Markets API — 1차 딜러 통계(레포)와 SOMA 만기분포. 키 불필요, 무료.

왜 필요한가 — 볼트의 유동성·신용 지표는 전부 **가격**이다.
EBP·HY OAS·SOFR−IORB 모두 "얼마에 거래되나"만 말하고 "얼마나 쌓였나"를 말하지 않는다.

- **딜러 레포**: Adrian & Shin(2010)은 중개기관의 위험한도가 대차대조표 **수량**으로 먼저 드러나며,
  딜러 레포 변화가 VIX 혁신을 **예측**한다고 보고한다. 가격 지표(EBP)만 보면 늦을 수 있다.
  → 제텔 `금융가속기는 차입자 쪽과 대출자 쪽 두 개다` · RegimeView 8차 개정의 숙제.
- **SOMA 만기분포**: D'Amico & King(2013)의 핵심은 금리를 낮추는 것이 매입 플로우가 아니라
  **보유 스톡**이고 효과가 10~15년 구간에 몰린다는 것이다. 시장이 실제로 소화할 듀레이션은
  (재무부 발행 구성) − (연준 보유 구성)이므로 **연준 쪽 만기 구성 없이는 계산이 반쪽**이다.
  → 제텔 `QE 효과는 사는 동안이 아니라 들고 있는 동안 지속된다 — 스톡이 플로우를 압도한다`.

⚠ 한계 (yaml note에도 명시할 것):
- 1차 딜러 통계는 **주간**이고 공표까지 약 **2주 시차**가 있다. 일별 트리거로 쓸 수 없다
- 값이 `*`인 주가 있다 — 결측이 아니라 **개별 딜러 노출 방지를 위한 비공개**다.
  최근 24주 중 절반 이상이 비공개인 구간도 있으므로 **이동평균·연속성 판정에 쓰지 말 것**.
  비공개 건수는 매 실행 note에 기록된다
- 딜러 포지션은 **자기자본이 아니라 총잔액**이다. 레버리지 자체가 아니라 그 대용이다
- SOMA `parValue`는 **액면**이다. 시가도 듀레이션(수정듀레이션)도 아니다.
  여기서 내는 것은 **잔존만기 가중평균(WAM)** 이며 볼록성·쿠폰을 반영하지 않는다
- SOMA 국채 보유에는 TIPS·FRN이 섞여 있다. 액면 합산이라 인플레보상은 빠진다
"""
from __future__ import annotations

from datetime import date
from typing import Any

from .base import get_json, result

BASE = "https://markets.newyorkfed.org/api"
N_OBS = 6
LANDING_PD = "https://www.newyorkfed.org/markets/counterparties/primary-dealers-statistics"
LANDING_SOMA = "https://www.newyorkfed.org/markets/soma-holdings"

# 잔존만기 버킷 — D'Amico & King의 효과 구간(10~15년)이 마지막 버킷에 들어가도록 잡았다
BUCKETS: list[tuple[str, float, float]] = [
    ("1년 이하", 0.0, 1.0),
    ("1~5년", 1.0, 5.0),
    ("5~10년", 5.0, 10.0),
    ("10년 초과", 10.0, 1e9),
]


def _to_float(v: Any) -> float | None:
    try:
        return float(str(v).replace(",", ""))
    except (TypeError, ValueError):
        return None


def fetch_pd(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """1차 딜러 통계. yaml 예시:

        method: api
        source: nyfed_pd
        keyid: ["PDSORA-UTSETTOT", "PDSIRRA-UTSETTOT"]
        labels:
          PDSORA-UTSETTOT: 딜러 레포 잔액(국채 ex-TIPS, $bn)
    """
    raw = ind.get("keyid")
    if not raw:
        return result(ind, "fail", error="keyid 미지정 — /api/pd/list/timeseries.json 에서 확인")
    keyids = [str(k) for k in raw] if isinstance(raw, list) else [str(raw)]
    labels = ind.get("labels") or {}

    obs: list[dict[str, Any]] = []
    errors: list[str] = []
    suppress_notes: list[str] = []
    for kid in keyids:
        try:
            data = get_json(f"{BASE}/pd/get/{kid}.json")
        except Exception as e:  # 시리즈 하나가 전체를 죽이지 않는다
            errors.append(f"{kid}: {type(e).__name__}")
            continue
        rows = sorted((data.get("pd") or {}).get("timeseries") or [],
                      key=lambda r: str(r.get("asofdate", "")))
        # NY Fed는 개별 딜러 포지션 노출을 막으려고 일부 주를 '*'로 비공개 처리한다.
        # 계열이 성기다는 사실 자체가 해석에 들어가야 하므로 비공개 건수를 세어 note에 남긴다.
        recent = rows[-24:]
        suppressed = sum(1 for r in recent if _to_float(r.get("value")) is None)
        valid = [r for r in rows if _to_float(r.get("value")) is not None]
        if not valid:
            errors.append(f"{kid}: 유효 관측치 없음(전부 비공개 '*')")
            continue
        label = labels.get(kid, kid)
        for r in valid[-N_OBS:][::-1]:
            val = _to_float(r.get("value"))
            assert val is not None
            obs.append({"date": r.get("asofdate", ""), "value": round(val / 1000, 1), "label": label})
        if suppressed:
            suppress_notes.append(f"{label.split(' =')[0]} 최근 24주 중 {suppressed}주 비공개(*)")

    if not obs:
        return result(ind, "fail", error="; ".join(errors) or "관측치 없음")
    extra = suppress_notes + (["일부 실패: " + "; ".join(errors)] if errors else [])
    note = ind.get("note", "")
    if extra:
        note = (note + " · " if note else "") + " · ".join(extra)
    return result(ind, "ok", observations=obs, source_url=LANDING_PD, note=note)


def fetch_soma_maturity(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """SOMA 국채 보유의 잔존만기 분포와 가중평균만기(WAM).

        method: api
        source: nyfed_soma
    """
    latest = get_json(f"{BASE}/soma/asofdates/latest.json")
    dates = (latest.get("soma") or {}).get("asOfDates") or []
    if not dates:
        return result(ind, "fail", error="asofdates 응답에 날짜 없음 — API 포맷 변경 의심")
    asof_str = str(dates[0])
    asof = date.fromisoformat(asof_str)

    data = get_json(f"{BASE}/soma/tsy/get/asof/{asof_str}.json")
    holdings = (data.get("soma") or {}).get("holdings") or []
    if not holdings:
        return result(ind, "fail", error=f"{asof_str} 보유내역 없음")

    sums = {name: 0.0 for name, _, _ in BUCKETS}
    total = 0.0
    weighted = 0.0
    skipped = 0
    for h in holdings:
        par = _to_float(h.get("parValue"))
        mat = h.get("maturityDate")
        if par is None or not mat:
            skipped += 1
            continue
        try:
            yrs = (date.fromisoformat(str(mat)[:10]) - asof).days / 365.25
        except ValueError:
            skipped += 1
            continue
        yrs = max(yrs, 0.0)
        total += par
        weighted += par * yrs
        for name, lo, hi in BUCKETS:
            if lo <= yrs < hi:
                sums[name] += par
                break

    if total <= 0:
        return result(ind, "fail", error="parValue 합계가 0 — 필드명 변경 의심")

    obs = [{"date": asof_str, "value": round(sums[name] / 1e9, 1),
            "label": f"{name} ($bn, 액면)"} for name, _, _ in BUCKETS]
    obs.append({"date": asof_str, "value": round(sums["10년 초과"] / total * 100, 1),
                "label": "10년 초과 비중(%)"})
    obs.append({"date": asof_str, "value": round(weighted / total, 2),
                "label": "가중평균 잔존만기 WAM(년)"})

    note = ind.get("note", "")
    if skipped:
        note = (note + " · " if note else "") + f"만기·액면 결측 {skipped}건 제외"
    return result(ind, "ok", observations=obs, source_url=LANDING_SOMA, note=note)
