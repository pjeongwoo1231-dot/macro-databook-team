"""중국 국가통계국(NBS) 발표문 직접 수집.

**왜 필요한가.** 중국 계열은 DBnomics의 NBS 미러로 받고 있었는데
그 미러가 **2026-02에서 멈췄다**(2026-08-30 확인, 관측 13개가 끝). 그 사이
NBS 원문은 계속 나왔고, 두 값의 **부호가 반대**인 달까지 생겼다 —
미러 PPI는 2026-02 −0.9%인데 원문 2026-07은 **+3.5%** 다.
멈춘 미러를 그대로 인용하면 "중국이 디플레를 수출한다"는 판정이 통째로 뒤집힌다.

**어디가 막히고 어디가 열리나** (2026-08-30 실측)
    data.stats.gov.cn/easyquery.htm  → **403 Forbidden** (API는 막혔다)
    www.stats.gov.cn/sj/zxfb/        → **200** (발표 색인은 열린다)
    개별 발표문 t*.html              → **200** (본문·표 전부 읽힌다)

그래서 **발표문을 읽는다.** 제목에 이미 헤드라인 값이 들어 있고
(`2026年7月份工业生产者出厂价格同比上涨3.5%`), 본문에는 구성까지 있다.

**볼트 규칙이 요구하는 것은 전체 PPI가 아니라 구성이다.**
「디플레 수출은 소비재(生活资料) PPI로 판정한다」 — 2026-07은 전체 +3.5%지만
生产资料 +4.8% / **生活资料 −0.8%** 로, 플러스 전환은 상류가 만든 것이고
대외 디플레 압력은 살아 있다. 전체만 보면 정반대로 읽는다.

⚠ 함정
    ① 태그를 지우면 숫자 앞뒤에 공백이 낀다(`上涨 3.5 %`). 정규식에 `\\s*`를 넣는다.
    ② 같은 제목이 색인에 2~3번 반복된다. 최초 1건만 쓴다.
    ③ 발표 주기가 월 1회지만 "旬"(순) 단위 생산자재 가격 발표가 섞여 있다.
       제목에 `月份`이 있는 것만 월간 지표로 본다.
"""
from __future__ import annotations

import re
import ssl
import urllib.request
from typing import Any

from .base import result

INDEX = "https://www.stats.gov.cn/sj/zxfb/"          # 통계 속보
INDEX_JD = "https://www.stats.gov.cn/sj/sjjd/"       # 해설 — PMI는 여기에만 올라온다
_UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120",
       "Accept-Language": "zh-CN,zh;q=0.9"}
# 국가통계국 인증서 체인이 환경에 따라 검증에 실패한다 — 공개 통계라 본문 무결성만 보면 된다
_CTX = ssl.create_default_context()
_CTX.check_hostname = False
_CTX.verify_mode = ssl.CERT_NONE

_CACHE: dict[str, str] = {}

# 지표별: (제목에서 찾을 말, 본문에서 뽑을 항목들)
# 지표별: (제목에서 찾을 말, [(라벨, 정규식)])
# ⚠ 본문은 「一、同比변동」→「二、环比변동」 순서라 **같은 문구가 두 번** 나온다.
#   그래서 같은 문구를 쓰는 항목은 아래 _YOY_CUT으로 同比 구간만 잘라 찾는다.
_REPORTS = {
    "ppi": ("工业生产者出厂价格", [
        ("PPI 전체", r"工业生产者出厂价格同比\s*(上涨|下降)\s*([\d.]+)\s*%"),
        ("PPI 생산자재 生产资料", r"生产资料价格(?:同比)?\s*(上涨|下降)\s*([\d.]+)\s*%"),
        ("PPI 생활자재 生活资料", r"生活资料价格(?:同比)?\s*(上涨|下降)\s*([\d.]+)\s*%"),
        ("PPI 채굴 采掘", r"采掘工业价格\s*(上涨|下降)\s*([\d.]+)\s*%"),
        ("PPI 원재료 原材料", r"原材料工业价格\s*(上涨|下降)\s*([\d.]+)\s*%"),
        ("PPI 가공 加工", r"加工工业价格\s*(上涨|下降)\s*([\d.]+)\s*%"),
        ("PPI 식품 食品", r"食品价格\s*(上涨|下降)\s*([\d.]+)\s*%"),
        ("PPI 구매가격 购进", r"工业生产者购进价格同比\s*(上涨|下降)\s*([\d.]+)\s*%"),
    ]),
    "cpi": ("居民消费价格", [
        ("CPI 전체", r"居民消费价格同比\s*(上涨|下降)\s*([\d.]+)\s*%"),
        ("CPI 소비재 消费品", r"消费品价格\s*(上涨|下降)\s*([\d.]+)\s*%"),
        ("CPI 서비스 服务", r"服务价格\s*(上涨|下降)\s*([\d.]+)\s*%"),
        ("CPI 식품·주류 食品烟酒", r"食品烟酒[^%]{0,12}?价格同比\s*(上涨|下降)\s*([\d.]+)\s*%"),
        ("CPI 돼지고기 猪肉", r"猪肉价格\s*(上涨|下降)\s*([\d.]+)\s*%"),
    ]),
    "activity": ("国民经济", [
        ("규모이상 공업증가치 (전년비)", r"规模以上工业增加值(?:同比)?(?:实际)?\s*(增长|下降)\s*([\d.]+)\s*%"),
        ("소매판매 社会消费品零售总额 (전년비)", r"社会消费品零售总额[^%]{0,20}?(增长|下降)\s*([\d.]+)\s*%"),
        ("고정자산투자 (누계 전년비)", r"固定资产投资[^%]{0,26}?(增长|下降)\s*([\d.]+)\s*%"),
        ("부동산개발투자 (누계 전년비)", r"房地产开发投资[^%]{0,26}?(增长|下降)\s*([\d.]+)\s*%"),
        ("도시조사실업률", r"城镇调查失业率[^%\d]{0,24}?([\d.]+)\s*%"),
        ("서비스업생산지수 (전년비)", r"服务业生产指数(?:同比)?\s*(增长|下降)\s*([\d.]+)\s*%"),
    ]),
    # ⚠ PMI 해설문은 세 지수를 **한 문장에 나열**한다:
    #   「制造业采购经理指数、非制造业商务活动指数和综合PMI产出指数分别为 49.2% 、 49.0% 和 49.3% 」
    #   그래서 지수별로 따로 찾을 수 없고 나열 문장을 통째로 잡아 순서대로 배정한다.
    "pmi": ("采购经理指数", [
        ("제조업 PMI", _PMI_TRIPLE := (
            r"制造业采购经理指数[^。]{0,40}?分别为\s*([\d.]+)\s*%[^。]{0,20}?"
            r"([\d.]+)\s*%[^。]{0,20}?([\d.]+)\s*%", 1)),
        ("비제조업 PMI", (_PMI_TRIPLE[0], 2)),
        ("종합 PMI 산출지수", (_PMI_TRIPLE[0], 3)),
    ]),
}

# PMI 발표문 제목은 「…2026年7月中国采购经理指数」 — '月份'이 아니라 '月'이다
_PMI_YM = re.compile(r"(\d{4})\s*年\s*(\d{1,2})\s*月")

# 同比 구간의 끝 — 여기부터는 环比라 같은 문구가 다시 나온다
_YOY_CUT = re.compile(r"二、[^。]{0,20}?环比")

def _get(url: str) -> str:
    if url in _CACHE:
        return _CACHE[url]
    raw = urllib.request.urlopen(
        urllib.request.Request(url, headers=_UA), timeout=30, context=_CTX).read()
    _CACHE[url] = raw.decode("utf-8", "replace")
    return _CACHE[url]


def _plain(html: str) -> str:
    """태그를 지우고 공백을 하나로. 숫자 앞뒤 공백은 정규식이 흡수한다."""
    s = re.sub(r"(?s)<script.*?</script>|<style.*?</style>", " ", html)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", s)


def _latest_link(keyword: str, index: str = INDEX) -> tuple[str, str, str] | None:
    """색인에서 `…年…月份…<keyword>…` 제목의 **최신 1건**을 찾는다."""
    html = _get(index)
    seen: set[str] = set()
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>\s*([^<]{6,80}?)\s*</a>', html):
        href, title = m.group(1), m.group(2).strip()
        if keyword not in title or "月份" not in title:
            continue
        if href in seen:                       # 같은 제목이 색인에 2~3번 반복된다
            continue
        seen.add(href)
        ym = re.search(r"(\d{4})\s*年\s*(?:\d{1,2}\s*[—–-]\s*)?(\d{1,2})\s*月份", title)
        if not ym:
            # 「1—7月份国民经济…」처럼 연도가 제목에 없는 경우 — 링크 경로의 202608에서 연을 얻는다
            ym2 = re.search(r"(?:\d{1,2}\s*[—–-]\s*)?(\d{1,2})\s*月份", title)
            ymd = re.search(r"/(\d{4})(\d{2})/", href)
            if not (ym2 and ymd):
                continue
            period = f"{ymd.group(1)}-{int(ym2.group(1)):02d}"
            url = href if href.startswith("http") else index + href.lstrip("./")
            return url, period, title
        period = f"{ym.group(1)}-{int(ym.group(2)):02d}"
        url = href if href.startswith("http") else index + href.lstrip("./")
        return url, period, title
    return None


def _pmi_link() -> tuple[str, str, str] | None:
    """PMI는 해설(sjjd) 페이지에만 올라오고 제목이 「…2026年7月中国采购经理指数」 형식이다."""
    html = _get(INDEX_JD)
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>\s*([^<]{6,90}?)\s*</a>', html):
        href, title = m.group(1), m.group(2).strip()
        if "采购经理指数" not in title:
            continue
        ym = _PMI_YM.search(title)
        if not ym:
            continue
        url = href if href.startswith("http") else INDEX_JD + href.lstrip("./")
        return url, f"{ym.group(1)}-{int(ym.group(2)):02d}", title
    return None


def fetch_nbs(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """yaml 예시:
        method: api
        source: nbs
        report: ppi          # ppi | cpi | pmi
    """
    key = (ind.get("report") or "").lower()
    if key not in _REPORTS:
        return result(ind, "fail", error=f"report는 {list(_REPORTS)} 중 하나여야 한다: {key!r}",
                      source_url=INDEX)
    keyword, fields = _REPORTS[key]
    try:
        if key == "pmi":
            found = _pmi_link()
        else:
            found = _latest_link(keyword)
        if not found:
            return result(ind, "fail", error=f"색인에서 '{keyword}' 월간 발표를 찾지 못했다",
                          source_url=INDEX)
        url, period, title = found
        text = _plain(_get(url))
        # 同比 구간만 남긴다 — 안 자르면 环比 값을 同比로 착각한다
        if key not in ("activity", "pmi"):          # activity 발표문은 环比 절이 따로 없다
            cut = _YOY_CUT.search(text)
            if cut:
                text = text[:cut.start()]
    except Exception as exc:                                   # noqa: BLE001
        return result(ind, "fail", error=f"{type(exc).__name__}: {exc}", source_url=INDEX)

    obs, missing = [], []
    for label, spec in fields:
        # spec은 정규식이거나 (정규식, 그룹번호) — 후자는 한 문장에 여러 값이 나열될 때 쓴다
        pat, grp = spec if isinstance(spec, tuple) else (spec, None)
        m = re.search(pat, text)
        if not m:
            missing.append(label)
            continue
        if grp is not None:                                     # 수준값, 지정한 그룹
            v = float(m.group(grp))
        elif len(m.groups()) == 2:                              # (上涨|下降, 값)
            v = float(m.group(2)) * (-1 if m.group(1) in ("下降", "下降") else 1)
        else:
            v = float(m.group(1))
        obs.append({"date": period, "value": v, "label": label})

    if not obs:
        return result(ind, "fail", error=f"본문에서 값을 못 뽑았다 — 서식이 바뀌었는지 확인: {title[:40]}",
                      source_url=url)
    err = f"못 뽑은 항목: {', '.join(missing)}" if missing else ""
    return result(ind, "ok", observations=obs, source_url=url,
                  unit="%", error=err,
                  note=(ind.get("note", "") + f" — 원문 제목: {title}").strip(" —"))
