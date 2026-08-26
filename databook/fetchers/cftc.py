"""CFTC Traders in Financial Futures (TFF) — 키 불필요, 무료. 주간.

왜 필요한가 — 볼트가 2026-08-18에 [[비은행 레버리지 (NBFI)]] 축을 만들면서
"헤지펀드 레버리지·국채 선물 미결제약정·현·선물 베이시스"를 **관측 공백**으로 적었다.
그 공백을 메우는 가장 표준적인 무료 계열이 TFF의 **레버리지 펀드(lev money) 포지션**이다.

**왜 이것이 베이시스 트레이드의 대리지표인가.**
CFTC MRAC(2024)에 따르면 현·선물 베이시스 거래는 일반적으로
**인도 가능 현물을 사고 선물을 판다.** 따라서 이 거래가 커지면
**레버리지 펀드의 국채선물 순숏이 커진다.** 순숏 자체가 거래 규모는 아니지만
**같은 방향으로 움직이는 관측 가능한 흔적**이다.

⚠ 한계 (yaml note에도 반드시 명시):
- **순숏 ≠ 베이시스 트레이드 규모.** 방향성 베팅·헤지도 같은 칸에 들어간다.
  "베이시스 거래가 얼마다"라고 쓰지 말고 **"레버리지 펀드 순숏이 얼마다"** 라고 쓸 것
- **화요일 기준, 금요일 공표**로 3일 지연. 급변 국면에 늦다
- 계약 수 기준이라 **듀레이션 가중이 아니다.** 2Y와 30Y 계약을 더하면 안 된다
- TFF의 'leveraged money'는 헤지펀드·CTA·CPO를 포함하는 **범주**이며 헤지펀드만이 아니다
"""
from __future__ import annotations

import urllib.parse
from typing import Any

from .base import get_json, result

BASE = "https://publicreporting.cftc.gov/resource/gpe5-46if.json"
LANDING = "https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm"


def _rows(contract: str, limit: int) -> list[dict[str, Any]]:
    q = urllib.parse.urlencode({
        "$where": f"contract_market_name='{contract}'",
        "$order": "report_date_as_yyyy_mm_dd DESC",
        "$limit": str(limit),
    })
    return get_json(f"{BASE}?{q}")


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """yaml 예시:
        method: api
        source: cftc_tff
        contracts: ["UST 2Y NOTE", "UST 5Y NOTE", "UST 10Y NOTE", "UST BOND"]
        mode: net          # net=순숏(계약, 음수가 순숏) · pct_short=미결제 대비 숏 비중(%)
        points: 1          # 계약별 최신 몇 주
    """
    contracts = ind.get("contracts") or ["UST 10Y NOTE"]
    mode = str(ind.get("mode") or "net").lower()
    points = int(ind.get("points") or 1)

    obs: list[dict[str, Any]] = []
    missing: list[str] = []
    for c in contracts:
        try:
            rows = _rows(c, points)
        except Exception as e:  # 네트워크·쿼리 실패는 계약 단위로 건너뛴다
            missing.append(f"{c}({type(e).__name__})")
            continue
        if not rows:
            missing.append(c)
            continue
        for r in rows:
            try:
                lng = float(r["lev_money_positions_long"])
                sht = float(r["lev_money_positions_short"])
                oi = float(r["open_interest_all"])
            except (KeyError, TypeError, ValueError):
                missing.append(c)
                break
            date = str(r["report_date_as_yyyy_mm_dd"])[:10]
            if mode == "pct_short":
                val = round(100.0 * sht / oi, 1) if oi else 0.0
                label = f"{c} 레버리지펀드 숏/미결제 (롱 {lng:,.0f} · 숏 {sht:,.0f})"
            else:
                val = round(lng - sht, 0)
                label = f"{c} 레버리지펀드 순포지션 (숏비중 {100.0 * sht / oi:.1f}%)" if oi else c
            obs.append({"date": date, "value": val, "label": label})

    if not obs:
        return result(ind, "fail", error=f"CFTC TFF 없음: {', '.join(missing) or contracts}",
                      source_url=LANDING)
    err = f"계약 누락: {', '.join(missing)}" if missing else ""
    unit = "%" if mode == "pct_short" else "계약"
    return result(ind, "ok", observations=obs, source_url=LANDING, unit=unit, error=err)
