"""토스증권 Open API — OAuth2 Client Credentials. 2026-08-19 신설.

왜 필요한가 — 볼트의 한국 수급 계열은 지금까지 **네이버 페이지 스크랩**이었다.
토스증권 Open API는 같은 것을 **공식 REST**로 주고, 그 위에
**공매도·신용거래·대차거래·프로그램매매·기관 세부분류·외국인 지분율**처럼
**볼트에 아예 없던 계열**을 준다.
2026-08-19에 읽기 계열 전 엔드포인트를 실호출로 점검했다(2차 점검에서 8개 추가).

**인증**: `POST /oauth2/token` (grant_type=client_credentials).
토큰 수명 **86,399초(약 24시간)** — 프로세스 내 캐시한다.
`.env`에 `TOSSINVEST_CLIENT_ID` / `TOSSINVEST_CLIENT_SECRET`.

**⚠ 토큰은 동시에 하나만 산다(2026-08-19 실험으로 확인).**
새 토큰을 발급하면 **직전 토큰이 즉시 401**이 된다. 그래서:
- 이 수집기와 별도 스크립트를 **동시에 돌리면 서로 죽인다.** 백필은 수집이 끝난 뒤에 돌릴 것
- 실패가 `invalid-token`이면 키가 틀린 게 아니라 **다른 프로세스가 토큰을 가져간 것**이다

**⚠ 안전 경계 — 이 모듈은 읽기 전용이다.**
같은 토큰에 주문(`POST /api/v1/orders`)·조건주문 엔드포인트가 붙어 있지만
**이 모듈은 GET만 호출하며 주문 계열 경로를 아예 갖고 있지 않다.**
계좌·자산·주문·보유·수수료는 `X-Tossinvest-Account` 헤더가 추가로 필요한데
**그 헤더를 보내지 않는다** — 즉 내 계좌 잔고·보유종목은 원리적으로 못 읽는다.

**⚠ 그 밖의 한계 (yaml note에도 명시할 것)**
- **허용 IP 등록 필수.** 미등록 IP에서는 403 — 네트워크가 바뀌면 조용히 실패한다
- 응답이 **gzip**으로 올 수 있다(매직바이트로 판별해 해제)
- **429가 잦다**(엔드포인트군별 rate limit). 2초·4초·6초로 3회까지 재시도한다
- 수급 계열(`investor-trading` 등)의 **당일 값은 장중 갱신치**다. `updatedAt`을 같이 남긴다
- **장중 당일 레코드는 일부 투자자 구분이 `null`**로 온다(개인·기타법인이 특히 그렇다).
  값이 없으면 관측을 만들지 않는다 — 0으로 채우지 않는다
- Market Indicators 그룹은 **심볼 카탈로그 8종만** 받는다 —
  `KOSPI` · `KOSDAQ` · `KR_BOND_{2Y,3Y,5Y,10Y,20Y,30Y}`. 그 밖(KOSPI200 등)은 400 unsupported-symbol.
  **1차 점검에서 "KOSPI·KOSDAQ만"이라 적었던 것은 틀렸다** — 심볼 이름을 잘못 짚었을 뿐
  국고채 6개 만기가 실재한다(2026-08-19 스펙·실호출로 정정). 개별 종목 시세는 이 그룹이 아니라
  Market Data 그룹(`/api/v1/prices`, `/api/v1/candles`)을 쓴다
- 캔들 interval은 **`1m` / `1d`** 만 허용. 분봉은 지수만 — **국채는 일봉뿐**
- 페이지 크기 상한: 캔들 `count` **200**, 수급 계열 `count` **100**
- 이력 깊이(2026-08-19 실측): 캔들·수급 모두 **2020~2021년까지** 커서로 거슬러 올라간다.
  단 **신용거래(credit-trades)만 2023-04에서 커서가 끊긴다**
- `micro` 모드(호가·체결·상하한가)는 **스냅샷이라 일간 시계열이 아니다.** 장중에만 의미가 있다
"""
from __future__ import annotations

import gzip
import io as _io
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

from .base import result

BASE = "https://openapi.tossinvest.com"
LANDING = "https://developers.tossinvest.com"
_TOKEN: dict[str, Any] = {}


def _token(env: dict[str, str]) -> str:
    cid = env.get("TOSSINVEST_CLIENT_ID") or os.environ.get("TOSSINVEST_CLIENT_ID")
    sec = env.get("TOSSINVEST_CLIENT_SECRET") or os.environ.get("TOSSINVEST_CLIENT_SECRET")
    if not (cid and sec):
        raise RuntimeError("TOSSINVEST_CLIENT_ID/SECRET 미설정")
    if _TOKEN.get("v") and time.time() < _TOKEN.get("exp", 0):
        return _TOKEN["v"]
    body = urllib.parse.urlencode({"grant_type": "client_credentials",
                                   "client_id": cid, "client_secret": sec}).encode()
    req = urllib.request.Request(BASE + "/oauth2/token", data=body,
                                 headers={"Content-Type": "application/x-www-form-urlencoded",
                                          "User-Agent": "MacroVault/1.0"})
    d = json.loads(urllib.request.urlopen(req, timeout=40).read())
    _TOKEN["v"] = d["access_token"]
    _TOKEN["exp"] = time.time() + int(d.get("expires_in", 3600)) - 120
    return _TOKEN["v"]


def _get(path: str, env: dict[str, str], **q: Any) -> Any:
    url = BASE + path + ("?" + urllib.parse.urlencode(q) if q else "")

    def _req() -> urllib.request.Request:
        return urllib.request.Request(url, headers={
            "Authorization": "Bearer " + _token(env),
            "User-Agent": "MacroVault/1.0", "Accept": "application/json"})

    raw = b""
    refreshed = False
    for attempt in range(4):          # 429는 짧게 쉬고 재시도 — 전 엔드포인트를 한 번에 도는 구성이라 자주 걸린다
        try:
            raw = urllib.request.urlopen(_req(), timeout=60).read()
            break
        except urllib.error.HTTPError as e:
            body = e.read()
            if body[:2] == b"\x1f\x8b":
                body = gzip.decompress(body)
            msg = body.decode("utf-8", "replace")[:200]
            if e.code == 429 and attempt < 3:
                time.sleep(2.0 * (attempt + 1))
                continue
            # 401 invalid-token = 키 오류가 아니라 **다른 프로세스가 토큰을 가져간 것**이다.
            # 토큰은 동시에 하나만 사니까 캐시를 버리고 한 번만 새로 받아 재시도한다.
            # (한 번으로 제한하는 이유 — 두 프로세스가 계속 맞물리면 무한히 서로 뺏는다)
            if e.code == 401 and not refreshed:
                _TOKEN.clear()
                refreshed = True
                time.sleep(1.0)
                continue
            raise RuntimeError(f"HTTP {e.code}: {msg}")
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            # 오래 도는 백필에서 SSL 순단(TLSV1_ALERT_INTERNAL_ERROR)·타임아웃이 실제로 난다.
            # 종목 하나를 통째로 날리지 않도록 여기서 흡수한다
            if attempt < 3:
                time.sleep(1.5 * (attempt + 1))
                continue
            raise RuntimeError(f"네트워크 {type(e).__name__}: {e}")
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    d = json.loads(raw.decode("utf-8"))
    return d.get("result", d)


def _f(x: Any) -> float | None:
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _net(blk: Any, key: str = "netBuyVolume") -> float | None:
    """장중 레코드는 구분별로 통째 null이 온다 — 없으면 None을 돌려 관측을 만들지 않는다."""
    if not isinstance(blk, dict):
        return None
    return _f(blk.get(key))


# ── 모드별 처리 ──────────────────────────────────────────────
def _index(ind, env, obs):
    """지수 현재가 + 일봉 종가"""
    syms = ind.get("symbols") or ["KOSPI", "KOSDAQ"]
    for row in _get("/api/v1/market-indicators/prices", env, symbols=",".join(syms)) or []:
        v = _f(row.get("lastPrice"))
        if v is not None:
            obs.append({"date": (row.get("timestamp") or "")[:10] or "-", "value": v,
                        "label": f"{row.get('symbol')} 현재가"})
    for s in syms:
        c = _get(f"/api/v1/market-indicators/{s}/candles", env,
                 interval="1d", count=int(ind.get("points") or 3)) or {}
        for k in (c.get("candles") or []):
            v = _f(k.get("closePrice"))
            if v is None:
                continue
            date = (k.get("timestamp") or "")[:10]
            obs.append({"date": date, "value": v, "label": f"{s} 종가"})
            hi, lo = _f(k.get("highPrice")), _f(k.get("lowPrice"))
            if hi and lo and v:
                # 종가만 보면 장중에 −7%까지 갔다 되돌아온 날을 구분하지 못한다
                obs.append({"date": date, "value": round((hi - lo) / v * 100, 2),
                            "label": f"{s} 일중 변동폭(%)"})


def _index_flow(ind, env, obs):
    """지수 투자자별 매매대금 — 순매수(억원)"""
    for s in (ind.get("symbols") or ["KOSPI"]):
        d = _get(f"/api/v1/market-indicators/{s}/investor-trading", env,
                 interval="1d", count=int(ind.get("points") or 3)) or {}
        for r in (d.get("records") or []):
            for who, ko in (("individual", "개인"), ("foreigner", "외국인"),
                            ("institution", "기관"), ("otherCorporation", "기타법인")):
                blk = r.get(who) or {}
                b, s2 = _f(blk.get("buyAmount")), _f(blk.get("sellAmount"))
                if b is None or s2 is None:
                    continue
                obs.append({"date": r.get("date"), "value": round((b - s2) / 1e8, 0),
                            "label": f"{s} {ko} 순매수(억원)"})
            br = ((r.get("institution") or {}).get("breakdown") or {})
            for who, ko in (("pensionFund", "연기금"), ("financialInvestment", "금융투자"),
                            ("trust", "투신"), ("insurance", "보험")):
                blk = br.get(who) or {}
                b, s2 = _f(blk.get("buyAmount")), _f(blk.get("sellAmount"))
                if b is None or s2 is None:
                    continue
                obs.append({"date": r.get("date"), "value": round((b - s2) / 1e8, 0),
                            "label": f"{s} 기관·{ko} 순매수(억원)"})


_STOCK_FLOW = {
    "investor": ("investor-trading", "투자자별"),
    "program": ("program-trades", "프로그램"),
    "short": ("short-selling", "공매도"),
    "credit": ("credit-trades", "신용"),
    "lending": ("securities-lending", "대차"),
}


def _stock_flow(ind, env, obs):
    """종목 수급 5종 — 공매도·신용·대차·프로그램(차익/비차익)·투자자별(+외국인 지분율)"""
    kinds = ind.get("kinds") or ["short", "credit", "lending"]
    pts = int(ind.get("points") or 2)
    for sym in (ind.get("stocks") or ["005930"]):
        for kind in kinds:
            ep, _ko = _STOCK_FLOW[kind]
            d = _get(f"/api/v1/stocks/{sym}/{ep}", env, count=pts) or {}
            for r in (d.get("records") or []):
                date = r.get("date")
                if kind == "short":
                    v = _f(r.get("shortSellingVolumeRate"))
                    if v is not None:
                        obs.append({"date": date, "value": round(v * 100, 3),
                                    "label": f"{sym} 공매도 비중(%)"})
                    amt = _f(r.get("shortSellingAmount"))
                    if amt is not None:
                        obs.append({"date": date, "value": round(amt / 1e8, 0),
                                    "label": f"{sym} 공매도 대금(억원)"})
                elif kind == "credit":
                    m = r.get("marginLoan") or {}
                    v = _f(m.get("balanceQuantity"))
                    if v is not None:
                        obs.append({"date": date, "value": v,
                                    "label": f"{sym} 신용융자 잔고(주)"})
                    rate = _f(m.get("balanceRate"))
                    if rate is not None:
                        obs.append({"date": date, "value": round(rate * 100, 3),
                                    "label": f"{sym} 신용융자 잔고율(%)"})
                elif kind == "lending":
                    v = _f(r.get("balanceQuantity"))
                    if v is not None:
                        obs.append({"date": date, "value": v,
                                    "label": f"{sym} 대차잔고(주)"})
                    amt = _f(r.get("balanceAmount"))
                    if amt is not None:
                        obs.append({"date": date, "value": round(amt / 1e12, 2),
                                    "label": f"{sym} 대차잔고 금액(조원)"})
                elif kind == "program":
                    # 차익과 비차익은 성격이 다르다 — 차익은 선물 베이시스, 비차익은 바스켓 방향성
                    for key, ko2 in (("nonArbitrage", "비차익"), ("arbitrage", "차익")):
                        v = _net(r.get(key))
                        if v is not None:
                            obs.append({"date": date, "value": v,
                                        "label": f"{sym} 프로그램 {ko2} 순매수(주)"})
                else:  # investor
                    for who, ko2 in (("foreigner", "외국인"), ("institution", "기관"),
                                     ("individual", "개인"), ("otherCorporation", "기타법인")):
                        v = _net(r.get(who))
                        if v is not None:
                            obs.append({"date": date, "value": v, "label": f"{sym} {ko2} 순매수(주)"})
                    # 외국인 지분율 — 수급 흐름(플로우)이 아니라 잔량(스톡). 볼트에 없던 계열이다
                    fh = r.get("foreignerHolding") or {}
                    hr = _f(fh.get("holdingRate"))
                    if hr is not None:
                        obs.append({"date": date, "value": round(hr * 100, 2),
                                    "label": f"{sym} 외국인 지분율(%)"})
                    hq, lq = _f(fh.get("holdingQuantity")), _f(fh.get("limitQuantity"))
                    if hq and lq:
                        # 한도소진율 — 지분율과 다르다. 한도가 낮은 규제업종(통신·항공)에서만 의미가 커진다
                        obs.append({"date": date, "value": round(hq / lq * 100, 2),
                                    "label": f"{sym} 외국인 한도소진율(%)"})


def _stock_info(ind, env, obs):
    """종목 기본정보 + 현재가 → 시가총액(조원)·상장주식수·거래정지 여부"""
    syms = ind.get("stocks") or ["005930", "000660"]
    info = {r.get("symbol"): r for r in (_get("/api/v1/stocks", env, symbols=",".join(syms)) or [])}
    price = {r.get("symbol"): r for r in (_get("/api/v1/prices", env, symbols=",".join(syms)) or [])}
    for sym in syms:
        i, p = info.get(sym) or {}, price.get(sym) or {}
        nm = i.get("name") or sym
        sh, px = _f(i.get("sharesOutstanding")), _f(p.get("lastPrice"))
        date = (p.get("timestamp") or "")[:10] or "-"
        if sh and px:
            obs.append({"date": date, "value": round(sh * px / 1e12, 2),
                        "label": f"{nm}({sym}) 시가총액(조원)"})
        if px:
            obs.append({"date": date, "value": px, "label": f"{nm}({sym}) 주가"})
        if sh:
            obs.append({"date": date, "value": sh, "label": f"{nm}({sym}) 상장주식수"})
        kd = i.get("koreanMarketDetail") or {}
        if kd:
            # 거래정지·정리매매는 사건이다. 0/1로 남겨야 나중에 시계열에서 눈에 띈다
            flag = 1.0 if (kd.get("krxTradingSuspended") or kd.get("liquidationTrading")) else 0.0
            obs.append({"date": date, "value": flag,
                        "label": f"{nm}({sym}) 거래정지·정리매매 플래그"})


_RANK_KO = {
    "MARKET_TRADING_AMOUNT": "시장 거래대금",
    "MARKET_TRADING_VOLUME": "시장 거래량",
    "TOP_GAINERS": "급상승",
    "TOP_LOSERS": "급하락",
    "TOSS_SECURITIES_TRADING_AMOUNT": "토스 거래대금",
    "TOSS_SECURITIES_TRADING_VOLUME": "토스 거래량",
}


def _ranking(ind, env, obs):
    """랭킹 6종 × KR/US. 값은 등락률(%), 라벨에 거래대금을 남긴다.

    ⚠ TOP_GAINERS/TOP_LOSERS는 duration=realtime 미지원(400). 기본 1d를 쓴다.
    ⚠ TOSS_SECURITIES_* 는 토스증권 체결 기준 — 시장 전체가 아니라 **개인 리테일 쏠림의 대리**로 읽을 것.
    """
    types = ind.get("ranking_types") or ["MARKET_TRADING_AMOUNT", "TOP_GAINERS", "TOP_LOSERS"]
    country = ind.get("market_country") or "KR"
    dur = ind.get("duration") or "1d"
    n = int(ind.get("points") or 5)
    for t in types:
        d = _get("/api/v1/rankings", env, type=t, marketCountry=country, duration=dur, count=n) or {}
        date = (d.get("rankedAt") or "")[:10] or "-"
        ko = _RANK_KO.get(t, t)
        rows = d.get("rankings") or []
        total = 0.0
        for r in rows:
            ch = _f((r.get("price") or {}).get("changeRate"))
            amt = _f(r.get("tradingAmount"))
            total += amt or 0.0
            # 순위별 라벨은 종목이 매일 바뀐다 — 시계열이 아니라 그날의 명단이다
            obs.append({"date": date, "value": round((ch or 0) * 100, 2),
                        "label": f"[{ko}·{country}] #{r.get('rank')} {r.get('symbol')} 등락률(%)"})
        if total and "TRADING_AMOUNT" in t:
            # 이쪽이 진짜 시계열이다 — 상위 N종목에 대금이 얼마나 몰렸나(집중도)
            obs.append({"date": date, "value": round(total / 1e12, 2),
                        "label": f"[{ko}·{country}] 상위 {len(rows)}종목 거래대금 합계(조원)"})


_BOND = {"KR_BOND_2Y": "2Y", "KR_BOND_3Y": "3Y", "KR_BOND_5Y": "5Y",
         "KR_BOND_10Y": "10Y", "KR_BOND_20Y": "20Y", "KR_BOND_30Y": "30Y"}
_SPREADS = (("KR_BOND_10Y", "KR_BOND_3Y"), ("KR_BOND_10Y", "KR_BOND_2Y"),
            ("KR_BOND_30Y", "KR_BOND_10Y"))


def _bonds(ind, env, obs):
    """국고채 금리 커브 — 2·3·5·10·20·30년 + 장단기 스프레드.

    왜 중요한가 — 볼트의 커브 계열은 ECOS(817Y002)인데 **하루 늦다.**
    금통위처럼 날짜가 박힌 판정에서 그 하루는 곧 오판이다. 이건 장중 값이다.

    ⚠ **ECOS와 값이 다를 수 있다.** 민평 기준·시각이 다르므로 **대체가 아니라 교차검증**이다.
      장기 시계열·공식 인용은 계속 ECOS를 쓴다.
    ⚠ 국채는 **일봉(1d)만** 지원한다(분봉 400).
    ⚠ 현재가 응답의 `timestamp`는 국채에서 **null로 온다** — 기준일을 알 수 없으므로 '-'로 남긴다.
    """
    syms = ind.get("symbols") or list(_BOND)
    cur: dict[str, float] = {}
    for row in _get("/api/v1/market-indicators/prices", env, symbols=",".join(syms)) or []:
        v = _f(row.get("lastPrice"))
        sym = row.get("symbol")
        if v is None or sym not in _BOND:
            continue
        cur[sym] = v
        obs.append({"date": (row.get("timestamp") or "")[:10] or "-", "value": v,
                    "label": f"국고채 {_BOND[sym]} 금리(%)"})
    for long, short in _SPREADS:
        if long in cur and short in cur:
            obs.append({"date": "-", "value": round(cur[long] - cur[short], 3),
                        "label": f"국고채 {_BOND[long]}−{_BOND[short]} 스프레드(%p)"})
    for s in (ind.get("history") or []):     # 이력이 필요한 만기만 골라 받는다(호출 절약)
        c = _get(f"/api/v1/market-indicators/{s}/candles", env,
                 interval="1d", count=int(ind.get("points") or 5)) or {}
        for k in (c.get("candles") or []):
            v = _f(k.get("closePrice"))
            if v is not None:
                obs.append({"date": (k.get("timestamp") or "")[:10], "value": v,
                            "label": f"국고채 {_BOND.get(s, s)} 금리 종가(%)"})


def _hm(ts: str) -> int:
    """ISO 시각 문자열에서 분 단위 시각 — '2026-08-19T09:00:00.000+09:00' → 540"""
    return int(ts[11:13]) * 60 + int(ts[14:16])


def _calendar(ind, env, obs):
    """장 운영 정보 — 오늘이 영업일인가. 수집 실패와 휴장을 구분하려면 이게 있어야 한다."""
    for mk in (ind.get("markets") or ["KR", "US"]):
        d = _get(f"/api/v1/market-calendar/{mk}", env) or {}
        for key, ko in (("today", "당일"), ("previousBusinessDay", "직전영업일")):
            blk = d.get(key) or {}
            date = blk.get("date")
            if not date:
                continue
            body = blk.get("integrated") or blk
            reg = (body.get("regularMarket") or {})
            st, en = reg.get("startTime"), reg.get("endTime")
            obs.append({"date": date, "value": 1.0 if st else 0.0,
                        "label": f"{mk} {ko} 정규장 개장(1=개장)"})
            if st and en:
                # 조기 폐장(수능일 등)은 개장 여부로는 안 잡힌다 — 운영 분수로 잡는다
                mins = (_hm(en) - _hm(st)) % 1440
                obs.append({"date": date, "value": float(mins),
                            "label": f"{mk} {ko} 정규장 운영시간(분)"})


def _micro(ind, env, obs):
    """호가 스프레드 · 상하한가 대비 위치 · 최근 체결가 — 장중 스냅샷.

    ⚠ 일간 시계열이 아니다. 장 마감 후에 돌리면 직전 스냅샷이 굳은 값이 온다.
    """
    for sym in (ind.get("stocks") or ["005930"]):
        ob = _get("/api/v1/orderbook", env, symbol=sym) or {}
        date = (ob.get("timestamp") or "")[:10] or "-"
        asks, bids = ob.get("asks") or [], ob.get("bids") or []
        if asks and bids:
            a, b = _f(asks[0].get("price")), _f(bids[0].get("price"))
            if a and b:
                mid = (a + b) / 2
                obs.append({"date": date, "value": round((a - b) / mid * 10000, 2),
                            "label": f"{sym} 최우선호가 스프레드(bp)"})
                av = sum(_f(x.get("volume")) or 0 for x in asks)
                bv = sum(_f(x.get("volume")) or 0 for x in bids)
                if av + bv:
                    obs.append({"date": date, "value": round(bv / (av + bv) * 100, 1),
                                "label": f"{sym} 매수호가 잔량비중(%) — 50 초과면 매수 우위"})
        pl = _get("/api/v1/price-limits", env, symbol=sym) or {}
        up, lo = _f(pl.get("upperLimitPrice")), _f(pl.get("lowerLimitPrice"))
        tr = _get("/api/v1/trades", env, symbol=sym, count=1) or []
        last = _f(tr[0].get("price")) if tr else None
        if up and lo and last:
            obs.append({"date": date, "value": round((last - lo) / (up - lo) * 100, 1),
                        "label": f"{sym} 상하한 밴드 내 위치(%)"})
        wn = _get(f"/api/v1/stocks/{sym}/warnings", env)
        if isinstance(wn, list):
            obs.append({"date": date, "value": float(len(wn)),
                        "label": f"{sym} 매수 유의사항 건수"})


_FX_OK = {"KRW", "USD"}     # 실호출 확인(2026-08-19) — allowedValues가 딱 둘이다


def _misc(ind, env, obs):
    """환율 · 랭킹 · 종목 마스터 규모

    ⚠ 환율은 **USD/KRW 한 쌍뿐**이다. 엔·유로는 여기서 못 받는다(FRED·ECOS를 쓸 것).
    """
    what = ind.get("what") or ["fx"]
    if "fx" in what:
        for pair in (ind.get("fx_pairs") or ["USD/KRW"]):
            b, q = pair.split("/")
            if b not in _FX_OK or q not in _FX_OK:
                # 실호출 확인(2026-08-19): KRW·USD 외 통화는 400. 한 쌍 때문에 지표 전체를 죽이지 않는다
                obs.append({"date": "-", "value": 0.0,
                            "label": f"{pair} 미지원 — 토스증권 환율은 KRW·USD만"})
                continue
            d = _get("/api/v1/exchange-rate", env, baseCurrency=b, quoteCurrency=q) or {}
            date = (d.get("validFrom") or "")[:10]
            v = _f(d.get("rate"))
            if v is not None:
                obs.append({"date": date, "value": v, "label": pair})
            mid = _f(d.get("midRate"))
            if mid is not None:
                obs.append({"date": date, "value": mid, "label": f"{pair} 중간환율"})
    if "ranking" in what:
        _ranking(ind, env, obs)
    if "universe" in what:
        for mk in ("KOSPI", "KOSDAQ"):
            d = _get("/api/v1/stocks/all", env, market=mk)
            if isinstance(d, list):
                obs.append({"date": "-", "value": len(d), "label": f"{mk} 상장 종목 수"})
                n_sus = sum(1 for x in d if ((x.get("koreanMarketDetail") or {}).get("krxTradingSuspended")))
                if n_sus:
                    obs.append({"date": "-", "value": float(n_sus), "label": f"{mk} 거래정지 종목 수"})


_MODES = {"index": _index, "index_flow": _index_flow, "stock_flow": _stock_flow,
          "stock_info": _stock_info, "bonds": _bonds, "ranking": _ranking,
          "calendar": _calendar, "micro": _micro, "misc": _misc}


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """yaml 예시:
        method: api
        source: tossinvest
        mode: index_flow           # index · index_flow · stock_flow · stock_info
                                   # bonds · ranking · calendar · micro · misc
        symbols: [KOSPI, KOSDAQ]           # index / index_flow / bonds
        history: [KR_BOND_3Y, KR_BOND_10Y] # bonds — 이력까지 받을 만기
        stocks: ["005930","000660"]        # stock_flow / stock_info / micro
        kinds: [short, credit, lending, program, investor]   # stock_flow
        ranking_types: [MARKET_TRADING_AMOUNT, TOP_GAINERS]  # ranking
        market_country: KR                 # ranking (KR·US)
        duration: 1d                       # ranking (realtime·1d·1w·1mo·3mo·6mo·1y)
        markets: [KR, US]                  # calendar
        what: [fx, ranking, universe]      # misc
        fx_pairs: ["USD/KRW"]              # misc
        points: 3
    """
    mode = str(ind.get("mode") or "index")
    fn = _MODES.get(mode)
    if fn is None:
        return result(ind, "fail", error=f"미지원 mode: {mode}", source_url=LANDING)
    obs: list[dict[str, Any]] = []
    # 토큰은 동시에 하나만 산다 — 백필이 돌고 있으면 뺏지 않고 물러난다(그 지표만 skip)
    from ..tosslock import toss_lock
    try:
        with toss_lock("databook run", wait=3.0, quiet=True) as got:
            if not got:
                return result(ind, "fail",
                              error="다른 작업이 토스 API 사용 중 — 건너뜀(백필 종료 후 재실행)",
                              source_url=LANDING)
            fn(ind, env, obs)
    except Exception as e:
        return result(ind, "fail", error=f"토스증권 {type(e).__name__}: {e}", source_url=LANDING)
    if not obs:
        return result(ind, "fail", error="관측 없음", source_url=LANDING)
    return result(ind, "ok", observations=obs, source_url=LANDING)
