"""FRBSF Fernald 분기 TFP — 가동률 조정 총요소생산성. 키 불필요, 무료.

왜 필요한가 — DataBook에 **생산성 지표가 하나도 없었다.** 그런데 RegimeView의 두 번째
기둥("생산성이 모순을 해소한다", 확신도 상)이 생산성 위에 서 있다. 근거 데이터가
수집되지 않은 채로 판단이 돌아가고 있었다.

그리고 **노동생산성과 TFP는 다르다.** 노동생산성은 자본심화(자본투입 증가)만으로도 오른다.
기술이 좋아졌는지 보려면 TFP를, 경기적 가동률 변동을 걷어내려면 **가동률 조정 TFP**를 봐야 한다.
Fernald(2014)가 Basu-Fernald-Kimball(2006) 방법으로 그 조정을 구현한 표준 계열이다.

⚠ 한계 (yaml note에도 명시):
- **분기 데이터**이고 BEA 개정에 따라 **과거치가 소급 수정**된다. 주간 트리거 불가
- 가동률 조정은 **모형 기반 추정**이다. BFK 방법의 가정에 의존한다
- 저자가 "This draft is updated intermittently"라 밝힌 대로 방법론이 갱신된다
- 미국 **business sector** 기준. BLS 비농업 노동생산성과 정의가 다르다 — 섞지 말 것

열: dLP=노동생산성 · dk=자본투입 · dtfp=TFP · dutil=가동률 · dtfp_util=가동률조정 TFP
(전부 연율 %)
"""
from __future__ import annotations

import re
from typing import Any

from .base import get_bytes, result
from .xlsx import read_sheet

XLSX = "https://www.frbsf.org/wp-content/uploads/quarterly_tfp.xlsx"
LANDING = "https://www.frbsf.org/research-and-insights/data-and-indicators/total-factor-productivity-tfp/"
QUARTER_RE = re.compile(r"^(19|20)\d\d:Q?\d$")
_CACHE: dict[str, Any] = {}


def _load() -> tuple[dict[str, int], list[list[Any]]]:
    if "rows" not in _CACHE:
        rows = read_sheet(get_bytes(XLSX), 1)          # 시트 1 = quarterly
        hdr = next(r for r in rows if r and str(r[0]).strip() == "date")
        _CACHE["hdr"] = {str(h).strip(): i for i, h in enumerate(hdr) if h}
        _CACHE["rows"] = [r for r in rows
                          if r and r[0] and QUARTER_RE.match(str(r[0]).strip())]
    return _CACHE["hdr"], _CACHE["rows"]


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """yaml 예시:
        method: api
        source: frbsf_tfp
        columns: [dLP, dtfp, dtfp_util, dk]   # 기본값도 이것
        points: 4
    """
    hdr, rows = _load()
    cols = ind.get("columns") or ["dLP", "dtfp", "dtfp_util", "dk"]
    points = int(ind.get("points") or 4)

    missing = [c for c in cols if c not in hdr]
    obs: list[dict[str, Any]] = []
    for r in reversed(rows[-points:]):
        period = str(r[0]).strip()
        for c in cols:
            if c not in hdr:
                continue
            v = r[hdr[c]]
            if isinstance(v, (int, float)):
                obs.append({"date": period, "value": round(float(v), 2), "label": c})

    if not obs:
        return result(ind, "fail", error="FRBSF TFP 파싱 실패", source_url=LANDING)
    err = f"열 없음: {', '.join(missing)}" if missing else ""
    return result(ind, "ok", observations=obs, source_url=LANDING, unit="% 연율", error=err)
