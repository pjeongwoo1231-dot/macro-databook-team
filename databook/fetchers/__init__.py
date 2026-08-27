"""소스별 fetcher 디스패치. 반환 규격은 base.result() 참조 — 실패는 예외가 아니라 status로 표현한다."""
from __future__ import annotations

from typing import Any

from . import bis, bls, boj_api, cftc, china, crea, crypto, deribit, e_stat, europe, fred, frbsf, intl, japan, korea, nyfed, ofr, research, scrape, sec_xbrl, spreadsheet, tossinvest, us_gov, worldbank
from .base import result
from .news import fetch_news_indicator


def _lending_fetch(ind, env):
    from ..lending import fetch as f
    return f(ind, env)


def _sector_fetch(ind, env):
    from ..sectors import fetch as f
    return f(ind, env)

SCRAPE_DISPATCH = {
    "yahoo_finance": scrape.fetch_yahoo,
    "research_feed": research.fetch,
    "fedfunds_futures": scrape.fetch_fedfunds_futures,
    "cnn": scrape.fetch_cnn_fng,
    "naver_investor": scrape.fetch_naver_investor,
    "farside": scrape.fetch_farside,
    "cboe": scrape.fetch_cboe_pcr,
    "boj_stat": intl.fetch_boj_m2,
    "boj_policy_rate": intl.fetch_boj_rate,
    "ici": scrape.fetch_ici_flows,
    "gpr": scrape.fetch_gpr,
    "naver_sector": _sector_fetch,
    "yahoo_intraday": scrape.fetch_yahoo_intraday,
}

DISPATCH = {
    "crea": crea.fetch,
    "fred": fred.fetch,
    "ecos": korea.fetch_ecos,
    "ecos_keystat": korea.fetch_ecos_keystat,
    "kosis": korea.fetch_kosis,
    "data_go_kr": korea.fetch_data_go_kr,
    "fiscaldata": us_gov.fetch_fiscaldata,
    "treasury_auctions": us_gov.fetch_treasury_auctions,
    "treasurydirect": us_gov.fetch_treasurydirect,
    "cftc_socrata": us_gov.fetch_cftc,
    "coingecko": crypto.fetch_coingecko,
    "defillama": crypto.fetch_defillama,
    "alternative_me": crypto.fetch_alternative_me,
    "coinmetrics": crypto.fetch_coinmetrics,
    "upbit": crypto.fetch_upbit,
    "binance": crypto.fetch_binance,
    "worldbank": worldbank.fetch,
    "naver_datalab": korea.fetch_naver_datalab,
    "dbnomics": intl.fetch_dbnomics,
    "deribit": deribit.fetch,
    "eurostat": europe.fetch_eurostat,
    "ecb": europe.fetch_ecb,
    "bcb": intl.fetch_bcb,
    "fed_rss": intl.fetch_fed_rss,
    "cbr": intl.fetch_cbr_keyrate,
    "pboc_lpr": intl.fetch_pboc_lpr,
    "eia": us_gov.fetch_eia,
    "opinet": korea.fetch_opinet,
    "bls": bls.fetch,
    "lendborr": _lending_fetch,
    "spreadsheet": spreadsheet.fetch,
    "bis_credit_gap": bis.fetch,
    "bis_dsr": bis.fetch_dsr,
    "cftc_tff": cftc.fetch,
    "ofr_stfm": ofr.fetch,
    "mof_portfolio": intl.fetch_mof_portfolio,
    "mof_jgb": japan.fetch,
    "japan_customs": japan.fetch_customs,
    "e_stat": e_stat.fetch,
    "gacc": china.fetch_gacc,
    "pboc": china.fetch_pboc,
    "sec_xbrl": sec_xbrl.fetch,
    "boj_api": boj_api.fetch,
    "tossinvest": tossinvest.fetch,
    "frbsf_tfp": frbsf.fetch,
    "nyfed_pd": nyfed.fetch_pd,
    "nyfed_soma": nyfed.fetch_soma_maturity,
}


def fetch_indicator(ind: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    method = ind.get("method")
    if method == "manual":
        return result(ind, "manual", note=ind.get("note", "수동 입력 슬롯"))
    if method == "scrape":
        fn = SCRAPE_DISPATCH.get(ind.get("source", ""))
        if fn is None:
            return result(ind, "stub", error="scrape 미구현 소스", note=ind.get("note"))
        try:
            return fn(ind, env)
        except Exception as e:
            return result(ind, "fail", error=f"{type(e).__name__}: {e}")
    if method == "derived":
        return result(ind, "derived_pending")
    if method == "news":
        try:
            return fetch_news_indicator(ind, env)
        except Exception as e:
            return result(ind, "fail", error=f"{type(e).__name__}: {e}")
    fn = DISPATCH.get(ind.get("source", ""))
    if fn is None:
        return result(ind, "fail", error=f"미지원 소스: {ind.get('source')}")
    try:
        return fn(ind, env)
    except Exception as e:  # 실패 격리 — 지표 하나가 전체를 죽이지 않는다
        return result(ind, "fail", error=f"{type(e).__name__}: {e}")
