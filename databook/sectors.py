"""업종별 등락 — "어느 업종이 지수를 끄는가"를 검증하기 위한 데이터.

**왜 만드는가**: "외국인 보유비중이 높은 반도체가 지수를 주도한다"는 서술이 흔하지만,
그건 **노출(exposure)** 이지 **인과**가 아니다. 검증하려면 최소한 업종별 수익률이 필요하다.
(외국인 비중까지 붙이는 것은 아래 한계 참조 — 현재 불가)

**출처와 한계**
- 네이버 금융 업종별 시세(원천 KRX). 79개 업종, 일별 등락률
- ⚠ **업종별 외국인 지분율은 수집하지 못한다.** 네이버는 해당 컬럼을 세션 기반 옵션으로 숨겨두고
  있어 GET/POST 어느 쪽으로도 안정적으로 켤 수 없다(2026-08-05 확인). 부정확한 대용치를 넣느니
  비워둔다. 확보하려면 KRX 정보데이터시스템 또는 공공데이터포털 금융위 API의 활용신청이 필요하다
- KRX 정보데이터시스템(data.krx.co.kr) 비공개 API는 2026-08 기준 세션·bld 코드가 바뀌어 접근 불가.
  공공데이터포털 금융위 지수시세 API는 **별도 활용신청**이 필요하다(현재 키는 관세청 전용 → 403)
- 스냅샷 성격이다. **과거 시계열이 아니다** — 매일 실행해 쌓아야 시계열이 된다
"""
from __future__ import annotations

import csv
import re
from datetime import date
from typing import Any

from .core import OUTPUT_DIR
from .fetchers.base import BROWSER_UA, get_text, result

SECTOR_DIR = OUTPUT_DIR / "sectors"
LIST_URL = "https://finance.naver.com/sise/sise_group.naver?type=upjong"

ROW_RE = re.compile(
    r'<a href="/sise/sise_group_detail\.naver\?type=upjong&no=(\d+)">([^<]+)</a>\s*</td>\s*'
    r'<td class="number">\s*<span[^>]*>\s*([-+][\d.]+)%',
    re.S)
COUNT_RE = re.compile(r'<td class="number">(\d+)</td>')


def fetch_list() -> list[dict[str, Any]]:
    html = get_text(LIST_URL, headers={"User-Agent": BROWSER_UA}, encoding="euc-kr")
    out: list[dict[str, Any]] = []
    # 업종 단위로 잘라 등락률과 상승/보합/하락 개수를 함께 읽는다
    for block in re.split(r"<tr>", html):
        m = ROW_RE.search(block)
        if not m:
            continue
        counts = COUNT_RE.findall(block)
        out.append({
            "no": m.group(1),
            "sector": m.group(2).strip(),
            "change_pct": float(m.group(3)),
            "n_total": int(counts[0]) if len(counts) > 0 else None,
            "n_up": int(counts[1]) if len(counts) > 1 else None,
            "n_flat": int(counts[2]) if len(counts) > 2 else None,
            "n_down": int(counts[3]) if len(counts) > 3 else None,
        })
    return out


SUM_URL = "https://finance.naver.com/sise/sise_market_sum.naver?sosok={sosok}&page={page}"
DETAIL_URL = "https://finance.naver.com/sise/sise_group_detail.naver?type=upjong&no={no}"
CODE_RE = re.compile(r"/item/main\.naver\?code=(\d{6})")


def fetch_market_caps(sosok: int = 0, max_pages: int = 40) -> dict[str, dict[str, float]]:
    """시가총액 페이지에서 종목코드 → {시총(억), 외국인비율(%)}.

    이 페이지는 **외국인비율이 기본 컬럼**이라 업종 상세와 달리 세션 옵션 문제가 없다.
    sosok: 0=코스피, 1=코스닥
    """
    out: dict[str, dict[str, float]] = {}
    for page in range(1, max_pages + 1):
        html = get_text(SUM_URL.format(sosok=sosok, page=page),
                        headers={"User-Agent": BROWSER_UA}, encoding="euc-kr")
        found = 0
        for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.S):
            m = CODE_RE.search(tr)
            if not m:
                continue
            tds = [re.sub(r"<[^>]+>", " ", t).strip()
                   for t in re.findall(r'<td class="number">(.*?)</td>', tr, re.S)]
            # 열: 현재가·전일비·등락률·액면가·시가총액(억)·상장주식수·외국인비율·거래량·PER·ROE
            if len(tds) < 7:
                continue
            try:
                cap = float(tds[4].replace(",", ""))
                frgn = float(tds[6].replace(",", ""))
            except ValueError:
                continue
            out[m.group(1)] = {"cap": cap, "foreign_pct": frgn}
            found += 1
        if found == 0:          # 마지막 페이지를 지나면 빈 표가 온다
            break
    return out


def fetch_sector_members(no: str) -> list[str]:
    """업종 상세에서 구성 종목코드."""
    html = get_text(DETAIL_URL.format(no=no), headers={"User-Agent": BROWSER_UA}, encoding="euc-kr")
    return sorted(set(CODE_RE.findall(html)))


def fetch(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """일일 수집용 — 등락률 상하위 업종만 요약해 Data Book에 싣는다(요청 1건)."""
    try:
        rows = fetch_list()
    except Exception as e:
        return result(ind, "fail", error=f"{type(e).__name__}: {e}")
    if not rows:
        return result(ind, "fail", error="업종 표 파싱 실패(구조 변경 의심)")
    rows.sort(key=lambda r: r["change_pct"], reverse=True)
    today = date.today().isoformat()
    obs = [{"date": today, "value": r["change_pct"], "label": f"▲ {r['sector']}"} for r in rows[:3]]
    obs += [{"date": today, "value": r["change_pct"], "label": f"▼ {r['sector']}"} for r in rows[-3:]]
    return result(ind, "ok", observations=obs,
                  source_url="https://finance.naver.com/sise/sise_group.naver?type=upjong",
                  note=(ind.get("note", "") or "") +
                       f" | 업종 {len(rows)}개 중 상하위 3개. 전체는 `python -m databook sectors`")


def collect(dry_run: bool = False, with_foreign: bool = True) -> int:
    print("업종별 시세 수집 (네이버 금융, 원천 KRX)")
    if dry_run:
        print("  dry-run — 요청하지 않음")
        return 0
    try:
        rows = fetch_list()
    except Exception as e:
        print(f"  [FAIL] {type(e).__name__}: {e}")
        return 1
    print(f"  [OK  ] 업종 {len(rows)}개")

    if with_foreign:
        print("\n시가총액·외국인비율 수집 (코스피+코스닥)")
        caps: dict[str, dict[str, float]] = {}
        for sosok, nm in [(0, "코스피"), (1, "코스닥")]:
            try:
                c = fetch_market_caps(sosok)
                caps.update(c)
                print(f"  [OK  ] {nm} {len(c):,}종목")
            except Exception as e:
                print(f"  [FAIL] {nm}: {type(e).__name__}: {e}")
        print(f"\n업종별 시총가중 외국인 지분율 — {len(rows)}개 업종")
        for i, r in enumerate(rows, 1):
            try:
                members = fetch_sector_members(r["no"])
            except Exception:
                r["foreign_pct_wavg"] = None
                r["mktcap_bn"] = None
                r["n_matched"] = 0
                continue
            tot = num = 0.0
            n = 0
            for code in members:
                c = caps.get(code)
                if not c:
                    continue
                tot += c["cap"]
                num += c["cap"] * c["foreign_pct"]
                n += 1
            r["foreign_pct_wavg"] = round(num / tot, 2) if tot > 0 else None
            r["mktcap_bn"] = round(tot / 10, 1) if tot > 0 else None   # 억 → 십억
            r["n_matched"] = n
            if i % 20 == 0:
                print(f"    {i}/{len(rows)} …")

    SECTOR_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    p = SECTOR_DIR / f"sectors_{today}.csv"
    cols = ["date", "no", "sector", "change_pct", "n_total", "n_up", "n_flat", "n_down",
            "foreign_pct_wavg", "mktcap_bn", "n_matched"]
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in sorted(rows, key=lambda x: x["change_pct"], reverse=True):
            w.writerow({"date": today, **r})

    up = [r for r in rows if r["change_pct"] > 0]
    print(f"\n완료: 업종 {len(rows)}개 (상승 {len(up)} / 하락 {len(rows) - len(up)})")
    print(f"  → {p}")
    print("\n⚠ 이건 스냅샷이다. 시계열을 만들려면 매일 실행해 쌓아야 한다.")
    if with_foreign:
        got = [r for r in rows if r.get("foreign_pct_wavg") is not None]
        if got:
            got.sort(key=lambda r: r["foreign_pct_wavg"], reverse=True)
            print(f"\n외국인 지분율 상위 (시총가중, {len(got)}개 업종)")
            for r in got[:5]:
                print(f"  {r['sector'][:20]:22s} {r['foreign_pct_wavg']:5.2f}%  "
                      f"시총 {r['mktcap_bn']:>10,.0f}십억  등락 {r['change_pct']:+.2f}%")
    print("\n⚠ 시총가중 외국인비율은 네이버 시가총액 페이지 기준. 우선주·중복상장 처리는 하지 않았다.")
    return 0
