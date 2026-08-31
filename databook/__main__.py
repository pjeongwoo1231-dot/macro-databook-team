"""CLI: python -m databook run [--only SOURCE] [--dry-run] | history | setup"""
from __future__ import annotations

import argparse
import sys

from . import derived, staleness
from .core import all_indicators, load_env, load_registry
from .fetchers import fetch_indicator
from .render import now_utc, render_markdown, render_snapshot


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="databook")
    sub = ap.add_subparsers(dest="cmd", required=True)
    run = sub.add_parser("run", help="전체 수집 → Data Book md + 스냅샷 JSON 생성")
    run.add_argument("--only", help="특정 소스만 수집(확인용). 볼트·스냅샷은 덮어쓰지 않는다")
    run.add_argument("--render-anyway", action="store_true",
                     help="--only 실행에서도 산출물을 덮어쓴다 (그날 노트가 그 소스만 남는다)")
    run.add_argument("--dry-run", action="store_true", help="네트워크 호출 없이 yaml 파싱·렌더 경로만 검증")
    run.add_argument("--no-setup", action="store_true", help="필수 키가 없어도 설정 마법사를 띄우지 않음")
    run.add_argument("--no-news", action="store_true",
                     help="뉴스 다이제스트를 건너뛴다 (기본은 수집 끝에 자동 생성)")
    sub.add_parser("setup", help="대화형 키 설정 마법사 (.env 생성/갱신)")

    # 조회 3종 — 큰 산출물을 통째로 읽지 않기 위한 것. databook/query.py 참조
    q1 = sub.add_parser("show", help="이름으로 지표를 찾아 값만 출력")
    q1.add_argument("terms", nargs="+")
    q1.add_argument("--points", type=int, default=4)
    q2 = sub.add_parser("diff", help="이전 스냅샷 대비 값이 바뀐 지표만")
    q2.add_argument("terms", nargs="*")
    q2.add_argument("--back", type=int, default=1,
                    help="N번째 이전 **스냅샷**과 비교(날짜 아님). 수집을 거른 날이 있으면 어긋난다")
    q2.add_argument("--since", help="이 날짜(YYYY-MM-DD) 시점과 비교. 주간 분석은 이쪽을 쓴다")
    q2.add_argument("--until", help="끝 시점(YYYY-MM-DD). 생략하면 최신. 닫힌 주간을 볼 때 쓴다")
    ik = sub.add_parser("intake", help="원문 인테이크 — 무엇이 아직 안 읽혔나")
    ik.add_argument("--limit", type=int, default=10, help="보여줄 편수 (기본 10)")
    ik.add_argument("--detail", action="store_true", help="본문을 읽어 실증/이론을 판정")
    ik.add_argument("--dir", action="append", dest="dirs", help="추가로 훑을 폴더 (반복 가능)")
    an = sub.add_parser("analog", help="과거 유사 국면 탐색 — 그때 무슨 일이 있었나")
    an.add_argument("--asof", help="기준 시점 YYYY-MM-DD")
    an.add_argument("--top", type=int, default=6, help="이웃 개수 (기본 6)")
    rp = sub.add_parser("report", help="주간 발표자료 스캐폴드 생성 (차트·표·문헌 자동 배치)")
    rp.add_argument("--asof", help="기준 시점 YYYY-MM-DD (기본: 직전 세션 화요일)")
    rp.add_argument("--out", help="출력 경로 (기본: output/report_<asof>.html)")
    au = sub.add_parser("audit", help="발표자료 강제 검사 — 미달이면 exit 1")
    au.add_argument("target", help="검사할 .html 또는 .md")
    au.add_argument("--json", action="store_true", dest="as_json")
    au.add_argument("--unused", type=int, default=0, help="쓰지 않은 지표를 N개까지 보여준다")
    wk = sub.add_parser("weekly", help="주간 통합분석 자료 한 번에 (신선도+diff+news+todo)")
    wk.add_argument("--since", help="비교 기준일 YYYY-MM-DD (기본: 직전 화요일 자동)")
    wk.add_argument("--limit", type=int, default=30, help="기사 최대 건수")
    wk.add_argument("--asof", help="기준 시점을 직전 세션이 아닌 다른 날로 (세션 전 최신 반영용)")
    q0 = sub.add_parser("todo", help="에이전트가 처리할 자리 (manual 슬롯·STALE 계열)")
    q0.add_argument("--kind", choices=["all","manual","stale"], default="all")
    q0.add_argument("--json", action="store_true", dest="as_json")
    q0.add_argument("--limit", type=int, default=15)
    q3 = sub.add_parser("news", help="뉴스 다이제스트 검색 (요약·선별 아님)")
    q3.add_argument("--q", nargs="*", default=[])
    q3.add_argument("--new", action="store_true")
    q3.add_argument("--team")
    q3.add_argument("--limit", type=int, default=30)
    hist = sub.add_parser("history", help="장기 시계열(FRED) CSV 수집 — 백테스트·회귀용")
    hist.add_argument("--since", default="2000-01-01", help="시작일 YYYY-MM-DD (기본 2000-01-01)")
    hist.add_argument("--tier", type=int, help="해당 티어 지표의 계열만 수집")
    hist.add_argument("--only", help="특정 series_id만 (쉼표 구분, 예: DGS10,DGS2)")
    hist.add_argument("--full", action="store_true", help="증분이 아니라 전체 재수집")
    hist.add_argument("--dry-run", action="store_true", help="네트워크 없이 대상·시작일만 출력")
    ev = sub.add_parser("events", help="이벤트 캘린더 + 코스피 갭/장중 수익률 분해")
    ev.add_argument("--since", default="2000-01-01", help="시작일 YYYY-MM-DD")
    ev.add_argument("--symbol", default="^KS11", help="지수 심볼 (기본 ^KS11 코스피)")
    ev.add_argument("--dry-run", action="store_true", help="대상만 출력")
    ea = sub.add_parser("earnings", help="빅테크 실적 캘린더 (MANGOS / Fab 10)")
    ea.add_argument("--basket", choices=["mangos", "fab10"], help="특정 바스켓만")
    ea.add_argument("--ahead", type=int, default=120, help="향후 며칠까지 스캔 (기본 120)")
    ea.add_argument("--dry-run", action="store_true", help="대상 종목만 출력")
    se = sub.add_parser("sectors", help="업종별 등락 스냅샷 (78개 업종)")
    se.add_argument("--no-foreign", action="store_true", help="외국인 지분율 계산 생략(빠름)")
    se.add_argument("--dry-run", action="store_true")
    ft = sub.add_parser("fedtext", help="FOMC 성명서 코퍼스 수집 (텍스트 분석용)")
    ft.add_argument("--since", type=int, default=1999, help="시작 연도 (기본 1999)")
    ft.add_argument("--dry-run", action="store_true")
    ln = sub.add_parser("lending", help="주식 대차잔고 (공매도 압력 대리지표)")
    ln.add_argument("--days", type=int, default=60, help="최근 N영업일 (기본 60)")
    ln.add_argument("--no-sector", action="store_true", help="업종별 집계 생략")
    ln.add_argument("--dry-run", action="store_true")
    tp = sub.add_parser("topics", help="FOMC 성명서 NMF 토픽모델링 + 수익률곡선 반응")
    tp.add_argument("--kmin", type=int, default=2)
    tp.add_argument("--kmax", type=int, default=12)
    tp.add_argument("--seed", type=int, default=0)
    tp.add_argument("--k", type=int, help="토픽 수 고정 (미지정 시 일관성으로 자동선택)")
    tp.add_argument("--since", type=int, default=0, help="해당 연도 이후 성명서만")
    tp.add_argument("--ns", action="store_true", help="Nelson-Siegel 요인 사용(기본: 버터플라이 프록시)")
    sub.add_parser("eventreg", help="이벤트 → 코스피 반응 회귀 (갭/장중 분해)")
    it = sub.add_parser("intel", help="정보 수집 (EIA·PortWatch·Comtrade·RSS) → 볼트 노트")
    it.add_argument("--only", choices=["indicators","reading","catalysts"], default="")
    it.add_argument("--dry-run", action="store_true")
    sm = sub.add_parser("sectormap", help="종목↔업종 매핑 + 파생 지표 + 업종 수급 집계")
    sm.add_argument("--remap", action="store_true", help="업종 매핑을 다시 받는다 (약 80회 요청)")
    st = sub.add_parser("site", help="시황 사이트 생성 (output/site/, 정적 HTML)")
    st.add_argument("--quiet", action="store_true")
    tb = sub.add_parser("tossback", help="토스증권 장기 백필 (지수·국채·수급 전 이력 → CSV)")
    tb.add_argument("--what", choices=["all", "market", "stocks", "fx", "calendar", "intraday"],
                    default="all",
                    help="market=지수·국채·수급·환율·캘린더·1분봉, stocks=종목 패널 (기본 all)")
    tb.add_argument("--since", default="2000-01-01", help="이 날짜보다 과거는 안 받는다 (기본: API가 주는 데까지)")
    tb.add_argument("--top", type=int, default=100, help="시총 상위 N종목 (0이면 전 종목, 기본 100)")
    tb.add_argument("--symbols", help="종목 직접 지정 (쉼표 구분). 지정하면 --top 무시")
    tb.add_argument("--kinds", help="수급 종류 (기본 전부: short,credit,lending,investor,program)")
    tb.add_argument("--no-close", action="store_true", help="종목 일봉 종가 생략 (호출 절약)")
    tb.add_argument("--full", action="store_true", help="증분이 아니라 전체 재수집")
    tb.add_argument("--no-resume", action="store_true", help="체크포인트 무시하고 처음부터")
    tb.add_argument("--interval", type=float, default=0.18, help="호출 간격 초 (기본 0.18)")
    tb.add_argument("--workers", type=int, default=8, help="종목 병렬 워커 수 (기본 8)")
    tb.add_argument("--dry-run", action="store_true", help="네트워크 없이 대상만 출력")
    dy = sub.add_parser("daily", help="일일 배치 (run+sectors+lending+history)")
    dy.add_argument("--skip", nargs="*", default=[], help="건너뛸 단계")
    sub.add_parser("surprise", help="금리 기반 서프라이즈 → 코스피 방향 회귀")
    dt = sub.add_parser("dyntopics", help="동태적 NMF (창별 토픽 → 2차 NMF)")
    dt.add_argument("--windows", type=int, default=5)
    dt.add_argument("--kwin", type=int, default=4, help="창 내부 토픽 수")
    dt.add_argument("--kdyn", type=int, default=4, help="동태적 토픽 수")
    dt.add_argument("--since", type=int, default=0)
    dt.add_argument("--ns", action="store_true", help="Nelson-Siegel 요인 사용")
    sub.add_parser("curve", help="Nelson-Siegel 3요인 추정 (Diebold-Li)")
    vt = sub.add_parser("vintage", help="빈티지 인덱스 재구성 — 스냅샷 이력 → vintage.csv + 개정 리포트")
    vt.add_argument("--top", type=int, default=20, help="개정 리포트에 출력할 건수")
    vt.add_argument("--like", help="지표명 부분일치 필터 (예: --like GDPNow)")
    sub.add_parser("consensus", help="컨센서스 서프라이즈 — FairEconomy 캘린더 적립 + actual 대조")
    sm2 = sub.add_parser("seriesmeta", help="시리즈 메타(단위·주기·계절조정) 캐시 갱신 + 커버리지 리포트")
    sm2.add_argument("--report", action="store_true", help="갱신 없이 커버리지만 출력")
    sub.add_parser("unitcheck", help="단위 정합성 검사 — 최신 스냅샷에서 단위/값 모순 탐지")
    args = ap.parse_args()

    if args.cmd == "todo":
        from .todo import cmd_todo
        return cmd_todo(args.kind, args.as_json, args.limit)
    if args.cmd in ("show", "diff", "news"):
        from .query import cmd_diff, cmd_news, cmd_show
        if args.cmd == "show":
            return cmd_show(args.terms, args.points)
        if args.cmd == "diff":
            return cmd_diff(args.back, args.terms, args.since, args.until)
        return cmd_news(args.q, args.new, args.limit, args.team)
    if args.cmd == "setup":
        from .setup import run_wizard
        return run_wizard()

    if args.cmd == "surprise":
        from .surprise import run as run_sur
        return run_sur()

    if args.cmd == "intake":
        from .intake import cmd_intake
        return cmd_intake(args.limit, args.detail, args.dirs)

    if args.cmd == "analog":
        from .analog import cmd_analog
        return cmd_analog(args.asof, args.top)

    if args.cmd == "report":
        from .report import cmd_report
        return cmd_report(args.asof, args.out)

    if args.cmd == "audit":
        from .audit import cmd_audit
        return cmd_audit(args.target, args.as_json, args.unused)

    if args.cmd == "weekly":
        from .weekly import run as run_weekly
        return run_weekly(args.since, args.limit, args.asof)

    if args.cmd == "daily":
        from .daily import run as run_daily
        return run_daily(skip=args.skip)

    if args.cmd == "eventreg":
        from .eventreg import run as run_ereg
        return run_ereg()

    if args.cmd == "curve":
        from .nelsonsiegel import run as run_curve
        return run_curve()

    if args.cmd == "vintage":
        from .vintage import run as run_vintage
        return run_vintage(top=args.top, like=args.like)

    if args.cmd == "consensus":
        from .consensus import run as run_consensus
        return run_consensus()

    if args.cmd == "seriesmeta":
        from .seriesmeta import run as run_meta
        return run_meta(report=args.report)

    if args.cmd == "unitcheck":
        from .unitcheck import run as run_uc
        return run_uc()

    if args.cmd == "dyntopics":
        from .dyntopics import run as run_dyn
        return run_dyn(n_win=args.windows, k_win=args.kwin, k_dyn=args.kdyn,
                       since_year=args.since, use_ns=args.ns)

    if args.cmd == "topics":
        from .topics import run as run_topics
        return run_topics(kmin=args.kmin, kmax=args.kmax, seed=args.seed,
                          k_fixed=args.k, since_year=args.since, use_ns=args.ns)

    if args.cmd == "fedtext":
        from .fedtext import collect as collect_fedtext
        return collect_fedtext(since_year=args.since, dry_run=args.dry_run)

    if args.cmd == "lending":
        from .lending import collect as collect_lending
        return collect_lending(days=args.days, with_sector=not args.no_sector, dry_run=args.dry_run)

    if args.cmd == "sectors":
        from .sectors import collect as collect_sectors
        return collect_sectors(dry_run=args.dry_run, with_foreign=not args.no_foreign)

    if args.cmd == "earnings":
        from .earnings import collect as collect_earnings
        return collect_earnings(basket=args.basket, ahead=args.ahead, dry_run=args.dry_run)

    if args.cmd == "events":
        from .events import collect as collect_events
        return collect_events(since=args.since, symbol=args.symbol, dry_run=args.dry_run)

    if args.cmd == "sectormap":
        from .sectormap import collect as collect_sm
        return collect_sm(remap=args.remap)

    if args.cmd == "intel":
        from .intel import collect as collect_intel
        return collect_intel(only=args.only, dry_run=args.dry_run)

    if args.cmd == "site":
        from .site import build
        return build(quiet=args.quiet)

    if args.cmd == "tossback":
        from .tossback import collect as collect_toss
        syms = [s.strip() for s in args.symbols.split(",")] if args.symbols else None
        kinds = [k.strip() for k in args.kinds.split(",")] if args.kinds else None
        return collect_toss(what=args.what, since=args.since, top=args.top, symbols=syms,
                            kinds=kinds, full=args.full, with_close=not args.no_close,
                            dry_run=args.dry_run, resume=not args.no_resume,
                            interval=args.interval, workers=args.workers)

    if args.cmd == "history":
        from .history import collect
        only = [s.strip() for s in args.only.split(",")] if args.only else None
        return collect(since=args.since, tier=args.tier, only=only,
                       full=args.full, dry_run=args.dry_run)

    registry = load_registry()
    env = load_env()
    if not args.dry_run and not args.no_setup:
        from .setup import ensure_keys_interactive
        env = ensure_keys_interactive(env)
    indicators = all_indicators(registry)
    print(f"지표 {len(indicators)}개 로드 (indicators.yaml)")

    results = []
    derived_queue = []
    for ind in indicators:
        if args.dry_run:
            from .fetchers.base import result
            results.append(result(ind, "stub", error="dry-run"))
            continue
        if args.only and ind.get("source") != args.only and ind.get("method") not in ("manual",):
            from .fetchers.base import result
            results.append(result(ind, "stub", error=f"--only {args.only} 로 skip"))
            continue
        res = fetch_indicator(ind, env)
        if res["status"] == "derived_pending":
            derived_queue.append(ind)
            continue
        icon = {"ok": "OK  ", "fail": "FAIL", "manual": "MAN ", "stub": "SKIP"}.get(res["status"], "?   ")
        print(f"  [{icon}] {ind['name']}" + (f" — {res['error']}" if res["status"] == "fail" else ""))
        results.append(res)

    if not args.dry_run:
        for ind in derived_queue:
            res = derived.compute(ind, results)
            icon = "OK  " if res["status"] == "ok" else "FAIL"
            print(f"  [{icon}] (파생) {ind['name']}" + (f" — {res['error']}" if res["status"] == "fail" else ""))
            results.append(res)
        results.extend(derived.extra_derived(results))

    staleness.annotate(results)
    _stale = [r for r in results if r.get("stale")]
    if _stale:
        print(f"\n[갱신정지 의심 {len(_stale)}건] 최신 관측이 관측주기 대비 오래됨 — 코드 개편·단종 확인 필요")
        for r in sorted(_stale, key=lambda x: -x["age_days"]):
            print(f"  [STALE] {r['name']} — 최신 {r['observations'][0]['date']} ({r['age_days']}일 전, 주기 {r['gap_days']}일)")

    ts = now_utc()
    # --only 는 나머지를 전부 skip 처리한다. 그 결과를 그대로 렌더하면
    # **볼트의 그날 노트와 스냅샷이 한 소스만 남은 상태로 덮인다**(2026-08-19에 두 번 겪었다).
    # 부분 실행은 확인용이지 산출물 갱신이 아니므로, 렌더를 건너뛴다.
    if args.only and not args.render_anyway:
        ok = sum(1 for r in results if r["status"] == "ok")
        print(f"\n확인 실행(--only {args.only}): 성공 {ok} — 볼트·스냅샷은 덮어쓰지 않았다")
        print("  산출물까지 갱신하려면 --only 없이 전량 실행하거나 --render-anyway 를 붙일 것")
        return 0
    md_paths = render_markdown(results, ts, env)
    snap = render_snapshot(results, ts, env)
    if env.get("OBSIDIAN_VAULT_PATH"):
        print(f"Obsidian vault에도 출력: {env['OBSIDIAN_VAULT_PATH']}")
    ok = sum(1 for r in results if r["status"] == "ok")
    fail = sum(1 for r in results if r["status"] == "fail")
    manual = sum(1 for r in results if r["status"] == "manual")
    print(f"\n완료: 성공 {ok} / 실패 {fail} / 수동 {manual} / 전체 {len(results)}")
    for p in md_paths:
        print(f"  → {p}")
    print(f"  → {snap}")

    # 뉴스는 원래 `python -m databook.news` 별도 명령이었는데, run만 돌리는 습관 탓에
    # **2026-07-20 이후 5주간 갱신이 멈춰 있었다**(경로 문제가 아니라 실행을 안 한 것).
    # 그래서 run 끝에 붙인다. 실패해도 Data Book은 이미 기록됐으므로 exit code를 바꾸지 않는다.
    if not args.no_news:
        try:
            from .news import run_news
            for p in run_news(env):
                print(f"  → {p}")
        except Exception as e:
            print(f"  ⚠ 뉴스 생성 실패({type(e).__name__}: {e}) — Data Book은 정상 기록됨")
    return 0


if __name__ == "__main__":
    sys.exit(main())
