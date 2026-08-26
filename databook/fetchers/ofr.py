"""OFR(Office of Financial Research) Short-term Funding Monitor — 키 불필요, 무료. 일별.

왜 필요한가 — 볼트의 [[비은행 레버리지 (NBFI)]] 노드가 **레포 규모**를 관측 공백으로 적었다.
BIS AER 2023 Box D는 국채가 **레포를 통해 "준화폐"** 가 된다고 했고,
CFTC MRAC(2024)는 베이시스 거래의 세 다리 중 하나가 **레포 조달**이라고 했다.
그 시장의 크기를 재는 무료 일별 계열이 여기 있다.

주요 mnemonic:
  REPO-DVP_TV_TOT-P   DVP(인도결제) 레포 거래액 합계
  REPO-TRI_TV_TOT-P   삼자간(tri-party) 레포 거래액 합계
  REPO-GCF_TV_TOT-P   GCF 레포 거래액 합계
  REPO-DVP_AR_TOT-P   DVP 평균금리 (AR=average rate)

⚠ 한계 (yaml note에도 명시):
- **거래액(transaction volume)이지 잔액이 아니다.** 회전율이 섞인다
- 세 시장은 **참가자와 담보 관행이 다르다.** 단순 합산하면 중복·오독이 된다
- **헤어컷은 이 API에 없다** — OFR 공개 계열에 haircut mnemonic이 존재하지 않는다(2026-08-19 확인).
  담보 헤어컷은 여전히 **관측 공백**이다
"""
from __future__ import annotations

from typing import Any

from .base import get_json, result

BASE = "https://data.financialresearch.gov/v1/series/timeseries?mnemonic="
LANDING = "https://www.financialresearch.gov/short-term-funding-monitor/"


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """yaml 예시:
        method: api
        source: ofr_stfm
        mnemonics: ["REPO-DVP_TV_TOT-P", "REPO-TRI_TV_TOT-P", "REPO-GCF_TV_TOT-P"]
        scale: 1e9        # 나눌 값 (기본 1e9 = 십억 달러)
        points: 1
    """
    mns = ind.get("mnemonics") or ["REPO-DVP_TV_TOT-P"]
    scale = float(ind.get("scale") or 1e9)
    points = int(ind.get("points") or 1)

    obs: list[dict[str, Any]] = []
    missing: list[str] = []
    for mn in mns:
        try:
            rows = get_json(BASE + mn)
        except Exception as e:
            missing.append(f"{mn}({type(e).__name__})")
            continue
        pts = [r for r in rows if isinstance(r, list) and len(r) >= 2 and r[1] is not None]
        if not pts:
            missing.append(mn)
            continue
        for date, val in pts[-points:][::-1]:
            obs.append({"date": str(date)[:10],
                        "value": round(float(val) / scale, 1),
                        "label": mn})

    if not obs:
        return result(ind, "fail", error=f"OFR 계열 없음: {', '.join(missing) or mns}",
                      source_url=LANDING)
    err = f"계열 누락: {', '.join(missing)}" if missing else ""
    return result(ind, "ok", observations=obs, source_url=LANDING,
                  unit=ind.get("unit") or "$bn", error=err)
