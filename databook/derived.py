"""파생 지표 계산 — fetch 결과(1차 패스) 위에서 2차 패스로 계산한다.
지표 이름의 키워드로 핸들러를 매칭한다 (yaml의 formula는 사람용 설명)."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .fetchers.base import get_json, result


def _latest(results: list[dict[str, Any]], label_or_name: str) -> tuple[str, float] | None:
    """label(FRED series id 등) 또는 지표명으로 최신 관측치 검색."""
    for r in results:
        if r["status"] != "ok":
            continue
        if label_or_name in r["name"]:
            o = r["observations"][0]
            return o["date"], o["value"]
        for o in r["observations"]:
            if o.get("label") == label_or_name:
                return o["date"], o["value"]
    return None


def _obs_series(results: list[dict[str, Any]], label_or_name: str) -> list[dict[str, Any]]:
    """관측치 전체를 최신순 리스트로. _latest는 최신 1개만 주므로 전월 대비 분해에는 이게 필요하다."""
    for r in results:
        if r["status"] != "ok":
            continue
        if label_or_name in r["name"]:
            return r["observations"]
        hits = [o for o in r["observations"] if o.get("label") == label_or_name]
        if hits:
            return hits
    return []


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def compute(ind: dict[str, Any], results: list[dict[str, Any]]) -> dict[str, Any]:
    name = ind["name"]
    try:
        if "순유동성" in name:
            walcl, rrp, tga = _latest(results, "WALCL"), _latest(results, "RRPONTSYD"), _latest(results, "WTREGEN")
            if not (walcl and rrp and tga):
                return result(ind, "fail", error="구성요소 미수집 (WALCL/RRPONTSYD/WTREGEN 필요 — FRED 키 확인)")
            net = walcl[1] / 1000 - rrp[1] - tga[1] / 1000  # WALCL·WTREGEN은 $mn, RRPONTSYD는 $bn
            obs = [{"date": walcl[0], "value": round(net, 1), "label": "순유동성($bn) = B/S − RRP − TGA"}]
            return result(ind, "ok", observations=obs, source_url="FRED WALCL−RRPONTSYD−WTREGEN")
        if "v/u" in name or "구인/실업자" in name:
            # 2026-08-21 신설. 원계열(JTSJOL·UNEMPLOY)은 진작 수집하고 있었는데
            # 파생 핸들러가 없어 매 실행 fail로 남아 있었다 — [[실업률]] 노드의 "못 보는 것"이 이것이었다.
            # 둘 다 천명 단위라 그대로 나눈다.
            v, u = _latest(results, "JTSJOL"), _latest(results, "UNEMPLOY")
            if not (v and u):
                return result(ind, "fail", error="구성요소 미수집 (JTSJOL 구인·UNEMPLOY 실업자 필요)")
            if u[1] <= 0:
                return result(ind, "fail", error="실업자 수가 0 이하 — 계산 불가")
            ratio = v[1] / u[1]
            # ⚠ 두 계열의 기준월이 다를 수 있다(JOLTS가 한 달 늦다). 어긋나면 라벨에 남긴다
            gap = "" if v[0] == u[0] else f" ⚠ 기준월 불일치 (구인 {v[0]} · 실업 {u[0]})"
            obs = [{"date": min(v[0], u[0]), "value": round(ratio, 3),
                    "label": f"v/u 비율 (구인 {v[1]:,.0f}천 ÷ 실업 {u[1]:,.0f}천){gap}"}]
            return result(ind, "ok", observations=obs, source_url="FRED JTSJOL ÷ UNEMPLOY")
        if "한미 금리차" in name:
            us, kr = _latest(results, "DFEDTARU"), _latest(results, "한국은행 기준금리")
            if not (us and kr):
                return result(ind, "fail", error="구성요소 미수집 (Fed 상단 + 한은 기준금리 필요)")
            obs = [{"date": max(us[0], kr[0]), "value": round(us[1] - kr[1], 2), "label": "Fed 상단 − 한은 기준금리(%p)"}]
            return result(ind, "ok", observations=obs)
        if "김치프리미엄" in name:
            krw = _latest(results, "DEXKOUS")
            if not krw:
                return result(ind, "fail", error="원/달러(DEXKOUS) 미수집 — FRED 키 확인")
            upbit = get_json("https://api.upbit.com/v1/ticker?markets=KRW-BTC")[0]["trade_price"]
            usdt = float(get_json("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")["price"])
            prem = (float(upbit) / (usdt * krw[1]) - 1) * 100
            obs = [{"date": _today(), "value": round(prem, 2), "label": f"김치프리미엄(%) @USDKRW {krw[1]:,.0f}({krw[0]})"}]
            return result(ind, "ok", observations=obs, source_url="업비트/바이낸스/FRED")
        if "구리/금" in name:
            cu, au = _latest(results, "HG=F"), _latest(results, "GC=F")
            if not (cu and au):
                return result(ind, "fail", error="구성요소 미수집 (구리 HG=F·금 GC=F 필요)")
            obs = [{"date": max(cu[0], au[0]), "value": round(cu[1] / au[1], 5),
                    "label": "구리/금 비율 (상승=성장·리스크온, 하락=둔화 공포)"}]
            return result(ind, "ok", observations=obs, source_url="Yahoo HG=F ÷ GC=F")
        if "시장금리차" in name:
            kr, us = _latest(results, "국고채(10년)"), _latest(results, "DGS10")
            if not (kr and us):
                return result(ind, "fail", error="구성요소 미수집 (국고채(10년)·DGS10 필요)")
            obs = [{"date": max(str(kr[0]), us[0]), "value": round(kr[1] - us[1], 3),
                    "label": "국고10Y − 미국채10Y(%p, 음수 확대 시 외국인 자금이탈 압력)"}]
            return result(ind, "ok", observations=obs, source_url="ECOS 817Y002 − FRED DGS10")
        if "지역 연준 제조업 평균" in name:
            parts = [("GACDFSA066MSFRBPHI", "필라델피아"), ("GACDISA066MSFRBNY", "엠파이어"),
                     ("BACTSAMFRBDAL", "댈러스")]
            series = {lab: {o["date"]: o["value"] for o in _obs_series(results, sid)}
                      for sid, lab in parts}
            missing = [lab for lab, m in series.items() if not m]
            if missing:
                return result(ind, "fail", error=f"구성요소 미수집: {', '.join(missing)}")
            # 댈러스가 한 달 늦게 나오는 일이 잦다. 최신월을 강제하면 매달 실패하므로
            # 세 계열이 모두 가진 가장 최근 월로 맞춘다 — 서로 다른 시점을 평균하는 것만 막으면 된다.
            common = set.intersection(*(set(m) for m in series.values()))
            if not common:
                detail = " · ".join(f"{lab} {max(m)}" for lab, m in series.items())
                return result(ind, "fail", error=f"공통 기준월 없음 ({detail})")
            month = max(common)
            avg = sum(m[month] for m in series.values()) / len(series)
            newest = max(max(m) for m in series.values())
            obs = [{"date": month, "value": round(avg, 2),
                    "label": "지역연준 3종 평균 (0=중립, ISM 50 기준선과 다름)"}]
            res = result(ind, "ok", observations=obs, source_url="FRED 필라델피아·엠파이어·댈러스 평균")
            if newest != month:
                res["error"] = f"공통월 {month} 기준 — 일부 계열은 {newest}까지 나와 있다(발표 시차)"
            return res
        if "실업률 변화 분해" in name:
            clf = _obs_series(results, "CLF16OV")
            cnp = _obs_series(results, "CNP16OV")
            une = _obs_series(results, "UNEMPLOY")
            if not (len(clf) >= 2 and len(cnp) >= 2 and len(une) >= 2):
                return result(ind, "fail",
                              error="구성요소 부족 (CLF16OV·CNP16OV·UNEMPLOY 각 2개월 이상 필요)")
            # t = 최신, p = 직전. 세 계열의 기준월이 어긋나면 분해가 무의미하므로 먼저 막는다.
            if not (clf[0]["date"] == cnp[0]["date"] == une[0]["date"]):
                return result(ind, "fail",
                              error=f"기준월 불일치 (CLF {clf[0]['date']} · CNP {cnp[0]['date']} · U {une[0]['date']})")
            clf_t, clf_p = clf[0]["value"], clf[1]["value"]
            cnp_t, cnp_p = cnp[0]["value"], cnp[1]["value"]
            u_t, u_p = une[0]["value"], une[1]["value"]
            if not (clf_t and clf_p and cnp_t and cnp_p):
                return result(ind, "fail", error="0 또는 결측값 포함")
            rate_t = u_t / clf_t * 100
            rate_p = u_p / clf_p * 100
            emp_t = clf_t - u_t                      # 취업자 = 경활인구 − 실업자
            part_p = clf_p / cnp_p                   # 전월 참가율
            clf_cf = cnp_t * part_p                  # 참가율이 전월 그대로였다면의 경활인구
            u_cf = clf_cf - emp_t                    # 취업자는 실측 그대로 두고 실업자만 재계산
            rate_cf = u_cf / clf_cf * 100
            actual_chg = rate_t - rate_p             # 실제 실업률 변화(%p)
            cf_chg = rate_cf - rate_p                # 참가율 고정 시 변화(%p)
            part_effect = actual_chg - cf_chg        # 참가율 변동이 만든 부분
            obs = [
                {"date": clf[0]["date"], "value": round(actual_chg, 3),
                 "label": "실제 실업률 변화(%p, 전월비)"},
                {"date": clf[0]["date"], "value": round(cf_chg, 3),
                 "label": "참가율 고정 반사실 변화(%p) — 취업만으로 설명되는 부분"},
                {"date": clf[0]["date"], "value": round(part_effect, 3),
                 "label": "참가율 기여(%p) — 음수면 이탈이 실업률을 끌어내린 것"},
            ]
            return result(ind, "ok", observations=obs,
                          source_url="FRED CLF16OV·CNP16OV·UNEMPLOY")
        if "파편화 스프레드" in name:
            allb, aaa = _latest(results, "전체등급 10Y(%)"), _latest(results, "AAA 10Y(%)")
            if not (allb and aaa):
                return result(ind, "fail", error="구성요소 미수집 (ECB YC AAA·전체등급 10Y 필요)")
            obs = [{"date": max(allb[0], aaa[0]), "value": round(allb[1] - aaa[1], 3),
                    "label": "전체등급 10Y − AAA 10Y(%p, 일별 유로존 파편화 게이지)"}]
            return result(ind, "ok", observations=obs, source_url="ECB YC G_N_C − G_N_A")
        if "이탈리아-독일" in name:
            it, de = _latest(results, "이탈리아 10Y(%)"), _latest(results, "독일 10Y(%)")
            if not (it and de):
                return result(ind, "fail", error="구성요소 미수집 (ECB IRS 독일·이탈리아 10Y 필요)")
            obs = [{"date": max(it[0], de[0]), "value": round(it[1] - de[1], 3),
                    "label": "이탈리아 10Y − 독일 10Y(%p, 확대 = 유로존 재정·국가신용 파편화)"}]
            return result(ind, "ok", observations=obs, source_url="ECB IRS M.IT − M.DE")
        if "텀스트럭처" in name:
            v3, v1 = _latest(results, "^VIX3M"), _latest(results, "VIXCLS")
            if not (v3 and v1):
                return result(ind, "fail", error="구성요소 미수집 (^VIX3M·VIXCLS 필요)")
            obs = [{"date": max(v3[0], v1[0]), "value": round(v3[1] / v1[1], 3),
                    "label": "VIX3M/VIX (1 미만 = 백워데이션·단기 패닉 신호)"}]
            return result(ind, "ok", observations=obs, source_url="Yahoo ^VIX3M ÷ FRED VIXCLS")
        if "엔캐리" in name:
            jpy = _latest(results, "엔 비상업 순포지션")
            if not jpy:
                return result(ind, "fail", error="CFTC 엔 순포지션 미수집 (CFTC 선물 포지셔닝 지표 필요)")
            obs = [{"date": jpy[0], "value": jpy[1],
                    "label": "CFTC 엔 비상업 순포지션(계약수) — 음수 클수록 캐리 확대, 급격한 양전환=청산 신호"}]
            return result(ind, "ok", observations=obs, source_url="https://publicreporting.cftc.gov")
        if "글로벌 M2" in name:
            parts = [
                ("미국 M2 증가율", "미국 M2 YoY(%)"),  # 지표명 매칭 — 레벨(M2SL) 지표와 라벨 충돌 방지
                ("유로존 M3 YoY(%)", "유로존 M3 YoY(%)"),
                # ⚠ 이 키는 **fetcher가 실제로 만드는 라벨과 글자 단위로 같아야** 한다.
                # 2026-08-26에 일본 M2를 스크레이프→BOJ API로 옮기며 라벨이 바뀌었는데
                # 여기를 안 고쳐서 **대시보드에서 일본만 조용히 빠졌다**(4개 중 3개면 통과라 실패로 안 잡힌다).
                ("일본 M2 전년비(%) — 계산", "일본 M2 YoY(%)"),
                ("중국 M2 YoY(%)", "중국 M2 YoY(%)"),
            ]
            obs = []
            missing = []
            for key, label in parts:
                hit = _latest(results, key)
                if hit:
                    obs.append({"date": hit[0], "value": hit[1], "label": label})
                else:
                    missing.append(label)
            if len(obs) < 3:
                return result(ind, "fail", error=f"구성요소 부족 (수집됨 {len(obs)}/4, 누락: {', '.join(missing)})")
            note = "증가율(YoY%) 취합 — 레벨 USD 합산은 단위·환율 리스크로 하지 않음(환각 차단 원칙)"
            if missing:
                note += f" · 누락: {', '.join(missing)}"
            return result(ind, "ok", observations=obs, note=note)
        if "위험충격 종류" in name:
            # §1 규칙: VIX 하나로 위험을 대리하지 않는다. 충격 종류를 먼저 분류한다.
            # 임계는 2006~2026 전 표본(5,108일) 5영업일 변화의 p90에서 뽑았다.
            def _span(label: str) -> tuple[str, float, float] | None:
                for r in results:
                    if r["status"] != "ok":
                        continue
                    o = [x for x in r["observations"] if x.get("label") == label]
                    if len(o) >= 2:
                        return o[0]["date"], float(o[0]["value"]), float(o[-1]["value"])
                return None
            vx, rr, jp = _span("VIXCLS"), _span("DFII10"), _span("DEXJPUS")
            if not (vx and rr and jp):
                missing = [n for n, v in (("VIXCLS", vx), ("DFII10", rr), ("DEXJPUS", jp)) if not v]
                return result(ind, "fail", error=f"구성요소 미수집: {', '.join(missing)} (각 2관측 이상 필요)")
            d_vix = vx[1] - vx[2]
            d_real = (rr[1] - rr[2]) * 100          # bp
            d_jpy = (jp[1] / jp[2] - 1) * 100       # +면 엔 절하
            risk_off, rate_led = d_vix >= 3.5, d_real >= 13.0
            label = ("복합" if risk_off and rate_led else
                     "리스크오프" if risk_off else
                     "미 금리 주도" if rate_led else "평시")
            guide = {
                "리스크오프": "엔 절상·원 절하 (전표본 70%/73%). 한국은 이중타격",
                "미 금리 주도": "엔도 원도 절하 (엔 절상은 19%뿐). 안전통화 기능 꺼짐",
                "복합": "원 절하 88%. 표본 74일뿐 — 해석 주의",
                "평시": "엔·원 방향에 정보 없음 (47%/46% = 동전던지기). 환율 움직임을 매크로로 설명하지 말 것",
            }[label]
            obs = [
                {"date": vx[0], "value": label, "label": f"충격 종류 — {guide}"},
                {"date": vx[0], "value": round(d_vix, 2), "label": "VIX 5일 변화(pt, 임계 +3.5 = p90)"},
                {"date": rr[0], "value": round(d_real, 1), "label": "실질금리 5일 변화(bp, 임계 +13 = p90)"},
                {"date": jp[0], "value": round(d_jpy, 2), "label": "엔/달러 5일 변화(%, +면 엔 절하)"},
            ]
            return result(ind, "ok", observations=obs, source_url="FRED VIXCLS·DFII10·DEXJPUS")
        if "레포 스트레스" in name:
            sofr, iorb = _latest(results, "SOFR"), _latest(results, "IORB")
            if not (sofr and iorb):
                return result(ind, "fail", error="구성요소 미수집 (SOFR·IORB 필요 — FRED 키 확인)")
            obs = [{"date": sofr[0], "value": round(sofr[1] - iorb[1], 3),
                    "label": "%p (T14: 0 이상 5영업일 연속 = 준비금 희소화 발동 · 월말·FOMC일 제외)"}]
            return result(ind, "ok", observations=obs, source_url="FRED SOFR − IORB")
        if "무담보 시장 압력" in name:
            # T14(SOFR−IORB)의 무담보 짝. 임계 +3bp는 2019-06~10 준비금 희소화 국면 실측치에서 잡았다.
            # ⚠ _latest는 지표명 부분일치를 먼저 본다 — "EFFR"은 슬롯명 "…(EFFR·OBFR)"에 걸려
            #    EFFRVOL을 집어온다. 라벨 정확일치로만 찾는다.
            def _by_label(lab: str) -> tuple[str, float] | None:
                for r in results:
                    if r["status"] != "ok":
                        continue
                    for o in r["observations"]:
                        if o.get("label") == lab:
                            return o["date"], o["value"]
                return None
            effr, iorb = _by_label("EFFR"), _by_label("IORB")
            if not (effr and iorb):
                return result(ind, "fail", error="구성요소 미수집 (EFFR·IORB 필요 — FRED 키 확인)")
            obs = [{"date": effr[0], "value": round((effr[1] - iorb[1]) * 100, 1),
                    "label": "bp (임계 +3 = 2019-09 레포 발작 구간. 거래량이 아니라 이 스프레드가 신호다)"}]
            return result(ind, "ok", observations=obs, source_url="FRED EFFR − IORB")
        if "반감기" in name:
            h = int(get_json("https://mempool.space/api/blocks/tip/height"))
            next_halving = (h // 210_000 + 1) * 210_000
            remain = next_halving - h
            obs = [
                {"date": _today(), "value": h, "label": "현재 블록 높이"},
                {"date": _today(), "value": remain, "label": f"다음 반감기(#{next_halving})까지 블록 수 (~{remain * 10 / 60 / 24:,.0f}일)"},
            ]
            return result(ind, "ok", observations=obs, source_url="https://mempool.space")
    except Exception as e:
        return result(ind, "fail", error=f"{type(e).__name__}: {e}")
    return result(ind, "fail", error=f"파생 핸들러 없음: {name}")


def extra_derived(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """yaml 밖의 추가 파생을 넣는 자리. 현재 비어 있다.

    2026-08-15: SOFR−IORB 스프레드가 여기 하드코딩돼 있었다. tier가 코드에 박혀 있어
    yaml에서 조정할 수 없었고(CLAUDE.md 5조 — Hard Coding 최소화), T14 트리거로
    승격하면서 indicators.yaml의 정식 파생 항목으로 옮겼다(tier 1, compute() 처리).
    호출부(__main__.py·daily.py)를 건드리지 않으려고 함수는 남겨 둔다.
    """
    return []
