"""ECOS·KOSIS·공공데이터포털. 코드가 'verify'인 지표는 추측 호출하지 않고,
키가 있으면 목록 API로 후보를 조회해 에러 메시지에 담아준다 (하네스/사용자가 확정 후 yaml 갱신)."""
from __future__ import annotations

from datetime import date, timedelta
from typing import Any

from .base import get_json, result

ECOS_BASE = "https://ecos.bok.or.kr/api"


def _ecos_search(key: str, stat: str, cycle: str, item: str) -> list[dict[str, Any]]:
    today = date.today()
    if cycle == "D":
        start, end = (today - timedelta(days=45)).strftime("%Y%m%d"), today.strftime("%Y%m%d")
    elif cycle == "M":
        start = (today - timedelta(days=400)).strftime("%Y%m")
        end = today.strftime("%Y%m")
    elif cycle == "Q":
        start, end = f"{today.year - 2}Q1", f"{today.year}Q4"
    else:
        start, end = str(today.year - 5), str(today.year)
    url = f"{ECOS_BASE}/StatisticSearch/{key}/json/kr/1/500/{stat}/{cycle}/{start}/{end}/{item}"
    data = get_json(url)
    block = data.get("StatisticSearch")
    if not block or "row" not in block:
        return []
    return block["row"]


def fetch_ecos(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    key = env.get("ECOS_API_KEY", "")
    if not key:
        return result(ind, "fail", error="ECOS_API_KEY 없음 (.env 확인)")
    stat = str(ind.get("stat_code", ""))
    raw_item = ind.get("item_code", "verify")
    items = [str(i) for i in raw_item] if isinstance(raw_item, list) else [str(raw_item)]
    if stat in ("", "verify", "None"):
        return result(ind, "fail", error="stat_code 미확정 — ECOS StatisticTableList로 통계표 확인 후 yaml 갱신 필요")
    if items == ["verify"]:
        # 항목 후보를 조회해서 알려준다
        try:
            data = get_json(f"{ECOS_BASE}/StatisticItemList/{key}/json/kr/1/20/{stat}")
            rows = (data.get("StatisticItemList") or {}).get("row", [])
            cand = ", ".join(f"{r.get('ITEM_CODE')}={r.get('ITEM_NAME')}" for r in rows[:8])
            return result(ind, "fail", error=f"item_code 미확정. {stat} 후보: {cand or '조회 실패'}")
        except Exception as e:
            return result(ind, "fail", error=f"item_code 미확정 (후보 조회 실패: {e})")
    obs = []
    errors = []
    for item in items:
        rows = []
        for cycle in ("M", "D", "Q", "A"):
            try:
                rows = _ecos_search(key, stat, cycle, item)
            except Exception:
                rows = []
            if rows:
                break
        if not rows:
            errors.append(f"{stat}/{item} 관측치 없음")
            continue
        for r in rows[-6:][::-1]:
            try:
                obs.append({"date": r.get("TIME", ""), "value": float(r["DATA_VALUE"]), "label": r.get("ITEM_NAME1", item)})
            except (KeyError, ValueError, TypeError):
                continue
    if not obs and errors:
        return result(ind, "fail", error="; ".join(errors) + " — 주기/코드 확인 필요")
    url = f"https://ecos.bok.or.kr (통계표 {stat})"
    if not obs:
        return result(ind, "fail", error="값 파싱 실패", source_url=url)
    return result(ind, "ok", observations=obs, source_url=url)


def fetch_kosis(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    key = env.get("KOSIS_API_KEY", "")
    if not key:
        return result(ind, "fail", error="KOSIS_API_KEY 없음 (.env 확인)")
    org, tbl = str(ind.get("org_id", "")), str(ind.get("tbl_id", ""))
    if not org or not tbl:
        return result(ind, "fail", error="KOSIS org_id/tbl_id 미확정 — statisticsSearch API로 확인 후 yaml 갱신 필요")
    params = {
        "method": "getList", "apiKey": key, "itmId": "ALL", "objL1": "ALL",
        "format": "json", "jsonVD": "Y", "prdSe": str(ind.get("prd_se", "M")),
        "newEstPrdCnt": 6, "orgId": org, "tblId": tbl,
    }
    if ind.get("obj_levels", 1) >= 2:
        params["objL2"] = "ALL"
    rows = get_json("https://kosis.kr/openapi/Param/statisticsParameterData.do", params)
    if isinstance(rows, dict):
        return result(ind, "fail", error=f"KOSIS 오류: {rows.get('errMsg', rows)}")
    flt = ind.get("filter", {}) or {}

    def keep(r: dict[str, Any]) -> bool:
        for field, allowed in flt.items():
            key_map = {"itm_id": "ITM_ID", "itm_nm": "ITM_NM", "c1": "C1", "c1_nm": "C1_NM", "c2_nm": "C2_NM"}
            val = str(r.get(key_map.get(field, field), ""))
            # 코드 필드(_id, c1)는 정확일치, 이름 필드(_nm)는 부분일치
            if field.endswith("_nm"):
                if not any(str(a) in val for a in allowed):
                    return False
            elif not any(str(a) == val for a in allowed):
                return False
        return True

    kept = [r for r in rows if keep(r)]
    url = f"https://kosis.kr/statHtml/statHtml.do?orgId={org}&tblId={tbl}"
    obs: list[dict[str, Any]] = []
    if ind.get("aggregate") == "sum_by_period":
        sums: dict[str, float] = {}
        for r in kept:
            try:
                sums[r["PRD_DE"]] = sums.get(r["PRD_DE"], 0.0) + float(r["DT"])
            except (KeyError, ValueError, TypeError):
                continue
        label = ind.get("agg_label", "합계")
        obs = [{"date": d, "value": v, "label": label} for d, v in sorted(sums.items(), reverse=True)]
    else:
        for r in kept:
            try:
                label = r.get("ITM_NM", "")
                if r.get("C1_NM") and r.get("C1_NM") != r.get("ITM_NM"):
                    label = f"{r['C1_NM']} {label}".strip()
                obs.append({"date": r["PRD_DE"], "value": float(r["DT"]), "label": f"{label}({r.get('UNIT_NM', '')})"})
            except (KeyError, ValueError, TypeError):
                continue
        obs.sort(key=lambda o: o["date"], reverse=True)
    if not obs:
        return result(ind, "fail", error=f"필터 결과 없음 (원본 {len(rows)}행) — filter 설정 확인", source_url=url)
    return result(ind, "ok", observations=obs[:12], source_url=url)


def fetch_data_go_kr(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    if not env.get("DATA_GO_KR_KEY"):
        return result(ind, "fail", error="DATA_GO_KR_KEY 없음 (.env 확인)")
    endpoint = ind.get("endpoint", "")
    if not endpoint or endpoint == "verify":
        return result(ind, "fail", error="관세청 API endpoint 미확정 — 활용신청 승인 후 참고문서의 요청주소를 yaml에 기입 필요")
    if "Itemtrade" in endpoint:
        return _fetch_itemtrade(ind, env, endpoint)
    if "prlstMmUtPrvi" in endpoint:
        return _fetch_prlst_10day(ind, env, endpoint)
    return result(ind, "fail", error=f"미지원 endpoint: {endpoint}")


def _fetch_prlst_10day(ind: dict[str, Any], env: dict[str, str], endpoint: str) -> dict[str, Any]:
    """관세청 10일 단위 잠정치 (수출 Exp / 수입 Imp). 단위 천 USD, itemUsdAmt00=총액."""
    import urllib.parse
    import urllib.request
    import xml.etree.ElementTree as ET

    today = date.today()
    start = (today.replace(day=1) - timedelta(days=95)).strftime("%Y%m")
    params = {"serviceKey": env["DATA_GO_KR_KEY"], "strtYymm": start, "endYymm": today.strftime("%Y%m")}
    url = endpoint + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "macro-databook/0.1"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        root = ET.fromstring(resp.read())
    if root.findtext(".//resultCode") != "00":
        return result(ind, "fail", error=f"응답 오류: {root.findtext('.//resultMsg')}")
    is_export = "ExpAcrs" in endpoint
    kind = "수출" if is_export else "수입"

    # 이 API는 같은 달에 대해 10일·20일·월전체 행을 함께 준다(priodDt로 구분).
    # 이걸 한 계열에 섞으면 20일 잠정치(55B) 옆에 월전체(99B)가 붙어 "전월비 급증"으로 읽힌다.
    # 실제로 Data Book에서 그 상태였다. 기간구분을 라벨에 넣어 서로 다른 계열로 분리한다.
    def _span(dt: str) -> str:
        d = (dt or "").replace(" ", "")
        if d.endswith("~10"):
            return "10일"
        if d.endswith("~20"):
            return "20일"
        return "월전체"

    by_span: dict[str, list[dict[str, Any]]] = {}
    for item in root.iter("item"):
        mon, dt = item.findtext("priodMon") or "", item.findtext("priodDt") or ""
        total = (item.findtext("itemUsdAmt00") or "").replace(",", "").strip()
        if not (mon and total):
            continue
        span = _span(dt)
        d = f"{mon[:4]}-{mon[4:6]} {dt}"
        by_span.setdefault(span, []).append(
            {"date": d, "value": float(total) * 1000, "label": f"{kind} 총액(USD, {span})"})
        if is_export:
            semi = (item.findtext("itemUsdAmt01") or "").replace(",", "").strip()
            if semi:
                by_span.setdefault(span, []).append(
                    {"date": d, "value": float(semi) * 1000, "label": f"반도체 수출(USD, {span})"})

    # 기간구분을 못 나눈 경우까지 포함해 계열별로 최신 4개씩만 싣는다.
    obs = []
    warn = []
    for span, rows in by_span.items():
        rows.sort(key=lambda o: o["date"], reverse=True)
        by_label: dict[str, list[dict[str, Any]]] = {}
        for r in rows:
            by_label.setdefault(r["label"], []).append(r)
        for label, series in by_label.items():
            obs.extend(series[:4])
            # 같은 기간구분 안에서 10배 이상 튀면 집계기준이 섞였다는 뜻 — 조용히 내보내지 않는다.
            for a, b in zip(series, series[1:]):
                if b["value"] and (a["value"] / b["value"] > 10 or b["value"] / a["value"] > 10):
                    warn.append(f"{label} {a['date']}↔{b['date']} 10배 이상 격차")
                    break
    if not obs:
        return result(ind, "fail", error="관측치 없음")
    res = result(ind, "ok", observations=obs, source_url="https://tradedata.go.kr")
    if warn:
        res["error"] = "집계기준 확인 필요 — " + "; ".join(warn[:3])
    return res


def _fetch_itemtrade(ind: dict[str, Any], env: dict[str, str], endpoint: str) -> dict[str, Any]:
    import urllib.parse
    import urllib.request
    import xml.etree.ElementTree as ET

    today = date.today()
    start = (today.replace(day=1) - timedelta(days=200)).strftime("%Y%m")
    params = {
        "serviceKey": env["DATA_GO_KR_KEY"],
        "strtYymm": start,
        "endYymm": today.strftime("%Y%m"),
        "hsSgn": str(ind.get("hs_code", "")),
    }
    url = endpoint + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "macro-databook/0.1"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        root = ET.fromstring(resp.read())
    code = root.findtext(".//resultCode")
    if code != "00":
        return result(ind, "fail", error=f"관세청 응답 오류: {code} {root.findtext('.//resultMsg')}")
    obs = []
    for item in root.iter("item"):
        ym = (item.findtext("year") or "").replace(".", "-")
        # 이 API는 월별 행 사이에 연간·누계 행을 섞어 준다. 그대로 넣으면 월 24억 달러 옆에
        # 연간 135억 달러가 붙어 "전월비 5배"로 읽힌다(실제 Data Book에서 그 상태였다).
        # YYYY-MM 형태가 아닌 행은 전부 버린다.
        import re as _re
        if not ym or "총계" in ym or not _re.fullmatch(r"\d{4}-\d{2}", ym):
            continue
        exp, imp = item.findtext("expDlr"), item.findtext("impDlr")
        if exp is not None:
            obs.append({"date": ym, "value": float(exp), "label": f"HS{ind.get('hs_code')} 수출(USD)"})
        if imp is not None:
            obs.append({"date": ym, "value": float(imp), "label": f"HS{ind.get('hs_code')} 수입(USD)"})
    obs.sort(key=lambda o: o["date"], reverse=True)
    if not obs:
        return result(ind, "fail", error="관세청 응답에 관측치 없음")
    res = result(ind, "ok", observations=obs[:12], source_url="https://tradedata.go.kr")
    # 월별 행만 남긴 뒤에도 10배 이상 튀면 단위·집계기준 문제다. 조용히 내보내지 않는다.
    by_label: dict[str, list[float]] = {}
    for o in obs[:12]:
        by_label.setdefault(o.get("label", ""), []).append(o["value"])
    jumps = [lab for lab, vs in by_label.items()
             if any(b and (a / b > 10 or b / a > 10) for a, b in zip(vs, vs[1:]))]
    if jumps:
        res["error"] = "집계기준 확인 필요 — " + ", ".join(jumps[:2]) + " 계열에 10배 이상 격차"
    return res


def fetch_naver_datalab(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """네이버 데이터랩 검색어트렌드 — 매크로 키워드의 대중 검색 관심도(리테일 심리 프록시).
    개발자센터 검색앱 키(NAVER_CLIENT_ID/SECRET, 데이터랩 API 추가) 필요. 없으면 안내.
    비율은 조회기간 내 상대값(최대=100) — 그룹 간·주간 추세 비교용."""
    import json
    import urllib.request

    cid = env.get("NAVER_CLIENT_ID", "").strip()
    sec = env.get("NAVER_CLIENT_SECRET", "").strip()
    if not (cid and sec):
        return result(ind, "fail",
                      error="NAVER_CLIENT_ID/SECRET 없음 — developers.naver.com에서 검색앱 등록 후 '데이터랩(검색어트렌드)' API 추가, .env에 입력")
    groups = ind.get("keyword_groups") or []
    if not groups:
        return result(ind, "fail", error="keyword_groups 미지정")
    today = date.today()
    body = {
        "startDate": (today - timedelta(days=90)).strftime("%Y-%m-%d"),
        "endDate": today.strftime("%Y-%m-%d"),
        "timeUnit": ind.get("time_unit", "week"),
        "keywordGroups": [{"groupName": g["name"], "keywords": g["keywords"]} for g in groups[:5]],
    }
    req = urllib.request.Request(
        "https://openapi.naver.com/v1/datalab/search",
        data=json.dumps(body).encode("utf-8"),
        headers={"X-Naver-Client-Id": cid, "X-Naver-Client-Secret": sec,
                 "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read().decode("utf-8", "replace"))
    obs: list[dict[str, Any]] = []
    for grp in data.get("results", []):
        name = grp.get("title", "")
        for pt in grp.get("data", [])[-6:][::-1]:
            try:
                obs.append({"date": pt["period"], "value": round(float(pt["ratio"]), 1),
                            "label": f"{name} 검색관심도"})
            except (KeyError, ValueError, TypeError):
                continue
    if not obs:
        return result(ind, "fail", error="데이터랩 응답에 관측치 없음")
    return result(ind, "ok", observations=obs,
                  source_url="https://datalab.naver.com/keyword/trendSearch.naver")


def fetch_opinet(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """오피넷 전국 평균 유가 — OPINET_API_KEY 필요 (opinet.co.kr 무료 즉시 발급)."""
    key = env.get("OPINET_API_KEY", "")
    if not key:
        return result(ind, "fail",
                      error="OPINET_API_KEY 없음 — opinet.co.kr > 오픈API에서 무료 발급 후 .env에 추가")
    data = get_json(f"https://www.opinet.co.kr/api/avgAllPrice.do?out=json&certkey={key}")
    oils = data.get("RESULT", {}).get("OIL", [])
    obs = []
    from datetime import datetime, timezone
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    wanted = {"B027": "보통휘발유(원/L)", "D047": "자동차경유(원/L)"}
    for o in oils:
        code = o.get("PRODCD", "")
        if code in wanted:
            try:
                raw_date = str(o.get("TRADE_DT") or "")
                date = f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:8]}" if len(raw_date) == 8 else today
                obs.append({"date": date, "value": float(o.get("PRICE")),
                            "label": wanted[code]})
            except (TypeError, ValueError):
                continue
    if not obs:
        return result(ind, "fail", error="오피넷 응답에 유가 없음 (키 유효성 확인)")
    return result(ind, "ok", observations=obs, source_url="https://www.opinet.co.kr")

def fetch_ecos_keystat(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """ECOS 100대 통계지표 — 한 번의 호출로 101건을 전부 받는다.

    한국은행이 직접 선정·관리하는 대표 지표 묶음이라 개별 stat_code를 몰라도 된다.
    CLASS_NAME(시장금리·물가·국민계정 등)으로 분류돼 있어 그대로 그룹핑에 쓴다.
    `class_filter`를 주면 해당 분류만 싣는다.
    """
    key = env.get("ECOS_API_KEY", "")
    if not key:
        return result(ind, "fail", error="ECOS_API_KEY 없음 (.env 확인)")
    url = f"https://ecos.bok.or.kr/api/KeyStatisticList/{key}/json/kr/1/200"
    data = get_json(url)
    root = data.get("KeyStatisticList") or {}
    rows = root.get("row") or []
    if not rows:
        err = (data.get("RESULT") or {}).get("MESSAGE", "응답에 row 없음")
        return result(ind, "fail", error=str(err))

    want = ind.get("class_filter")
    wants = [want] if isinstance(want, str) else (want or [])
    obs: list[dict[str, Any]] = []
    for r in rows:
        cls = str(r.get("CLASS_NAME", "")).strip()
        if wants and not any(w in cls for w in wants):
            continue
        try:
            val = float(str(r.get("DATA_VALUE", "")).replace(",", ""))
        except (TypeError, ValueError):
            continue
        cyc = str(r.get("CYCLE", "")).strip()
        if len(cyc) == 8:
            d = f"{cyc[:4]}-{cyc[4:6]}-{cyc[6:]}"
        elif len(cyc) == 6:
            d = f"{cyc[:4]}-{cyc[4:6]}-01"
        elif len(cyc) == 4:
            d = f"{cyc}-01-01"
        else:
            continue
        unit = str(r.get("UNIT_NAME", "")).strip()
        name = str(r.get("KEYSTAT_NAME", "")).strip()
        obs.append({"date": d, "value": val,
                    "label": f"[{cls}] {name}" + (f" ({unit})" if unit else "")})
    if not obs:
        return result(ind, "fail", error=f"필터 '{want}'에 맞는 항목 없음")
    obs.sort(key=lambda o: o["label"])
    return result(ind, "ok", observations=obs,
                  source_url="https://ecos.bok.or.kr/api/#/DevGuide/StatisticalCodeSearch")
