"""대화형 키 설정 마법사 — `python -m databook setup`.

**설계 원칙 세 가지**

1. **먼저 전체를 보여주고 나서 묻는다.** 하나씩 물으면 발급 사이트를 왔다갔다 하게 된다.
   시작하자마자 *없는 키 + 발급 링크 + 그 키가 살리는 지표 수*를 표로 먼저 뿌리고,
   사용자가 탭을 한꺼번에 열어 키를 다 받아온 뒤 한 번에 붙여넣게 한다.
2. **없어도 되는 걸 없어도 된다고 말한다.** 전체 중 절반 이상은 키가 아예 필요 없다
   (정확한 수는 indicators.yaml에서 매번 실측한다 — 하드코딩하지 않는다).
   FRED 하나만 넣어도 289개가 돈다. 이걸 안 알려주면 팀원이 키 12개를 다 받아야 하는 줄 안다.
3. **모르는 키를 지우지 않는다.** 예전 구현은 `KEY_SPECS`에 없는 항목을 .env에서 **날렸다**
   (E_STAT_APP_ID·DATABOOK_OUTPUT_DIR이 그렇게 사라졌다). 이제 기존 .env를 파싱해
   **모르는 키는 그대로 보존**한다.

키를 넣은 뒤에는 실제로 호출해 **살아 있는 키인지 확인**한다(FRED·ECOS·e-Stat).
오타를 붙여넣고 수집이 다 끝난 뒤에야 알게 되는 일을 막는다.
"""
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from .core import ROOT, load_env

# ── 지표 수는 **indicators.yaml에서 실측한다.** 하드코딩하지 않는다 ──────────
# 예전엔 TOTAL_COUNT=328, FRED=105처럼 손으로 적어 뒀는데, 지표를 늘릴 때마다
# 같이 고쳐야 해서 실제로 드리프트했다(2026-09-04 시점 실측 333·110).
# 팀원에게 "328개 중 184개는 키가 필요 없다"고 말해 놓고 숫자가 틀리면
# 그 안내 전체의 신뢰가 깎인다. 그래서 yaml을 SSOT로 두고 매번 센다.
SOURCE_KEY: dict[str, str] = {
    "fred": "FRED_API_KEY",
    "ecos": "ECOS_API_KEY",
    "ecos_keystat": "ECOS_API_KEY",
    "kosis": "KOSIS_API_KEY",
    "data_go_kr": "DATA_GO_KR_KEY",
    "e_stat": "E_STAT_APP_ID",
    "tossinvest": "TOSSINVEST_CLIENT_ID",
    "eia": "EIA_API_KEY",
    "bls": "BLS_API_KEY",
    "lendborr": "DATA_GO_KR_LENDBORR_KEY",
    "opinet": "OPINET_API_KEY",
    "naver_datalab": "NAVER_CLIENT_ID",
}
# ⚠ 여기 없는 source는 **키가 필요 없다**는 뜻이다. 새 소스가 키를 요구하면
#    여기 추가해야 한다 — 안 하면 "키 없어도 된다"고 잘못 세게 된다.


def _measure() -> tuple[int, int, dict[str, int]]:
    from .core import all_indicators, load_registry
    inds = all_indicators(load_registry())
    per: dict[str, int] = {}
    n_keyed = 0
    for i in inds:
        k = SOURCE_KEY.get(i.get("source") or "")
        if k:
            per[k] = per.get(k, 0) + 1
            n_keyed += 1
    return len(inds), len(inds) - n_keyed, per


TOTAL_COUNT, NO_KEY_COUNT, KEY_COUNTS = _measure()

# (환경변수, 라벨, 발급처, 필수, 도움말, 살리는 지표 수)
# ⚠ 지표 수는 indicators.yaml 실측(2026-08-28). 소스를 늘리면 같이 갱신할 것.
KEY_SPECS: list[tuple[str, str, str, bool, str, int]] = [
    ("FRED_API_KEY", "미국·글로벌 지표 (FRED)", "https://fred.stlouisfed.org/docs/api/api_key.html",
     True, "가입 후 즉시 발급. 이거 하나가 제일 큼", 105),
    ("ECOS_API_KEY", "한국은행 경제통계 (ECOS)", "https://ecos.bok.or.kr/api/",
     True, "무료 인증키 신청", 14),
    ("KOSIS_API_KEY", "통계청 (KOSIS)", "https://kosis.kr/openapi/",
     True, "무료 활용신청", 3),
    ("DATA_GO_KR_KEY", "공공데이터포털 (관세청 수출입 등)", "https://www.data.go.kr",
     True, "일반 인증키(Decoding) 사용. ★서비스별로 활용신청이 따로다", 3),
    ("E_STAT_APP_ID", "일본 e-Stat (기계수주·광공업생산·가계조사)", "https://www.e-stat.go.jp/api/",
     False, "★URL 칸에 localhost·사설IP는 거부된다. 공개 저장소 주소를 넣으면 통과", 3),
    ("TOSSINVEST_CLIENT_ID", "토스증권 Open API — Client ID", "https://developers.tossinvest.com",
     False, "★팀 공용 키가 없습니다 — 본인 앱을 만들고 본인 IP를 등록하세요(5분·무료)", 10),
    ("TOSSINVEST_CLIENT_SECRET", "토스증권 Open API — Client Secret", "https://developers.tossinvest.com",
     False, "위 ID와 같은 앱. 토큰이 동시 1개만 유효해 두 프로세스를 같이 돌리면 서로 401", 0),
    ("EIA_API_KEY", "미 에너지정보청 (원유·가스)", "https://www.eia.gov/opendata/register.php",
     False, "없으면 DEMO_KEY 폴백(레이트리밋)", 2),
    ("BLS_API_KEY", "미 노동통계국", "https://www.bls.gov/developers/api_signature_v2.html",
     False, "없어도 동작(일 25건 제한). 등록 시 일 500건", 1),
    ("DATA_GO_KR_LENDBORR_KEY", "금융위 주식대차정보", "https://www.data.go.kr",
     False, "위 공공데이터 키와 **활용신청이 별개**라 항목을 나눴다", 1),
    ("OPINET_API_KEY", "오피넷 국내유가", "https://www.opinet.co.kr/user/custc/custceco.do",
     False, "무료·즉시", 1),
    ("NAVER_CLIENT_ID", "네이버 검색·데이터랩 — Client ID", "https://developers.naver.com/apps",
     False, "★NCP 아님. 앱 등록 후 '검색'+'데이터랩' 추가", 1),
    ("NAVER_CLIENT_SECRET", "네이버 검색·데이터랩 — Client Secret", "https://developers.naver.com/apps",
     False, "위 ID와 같은 앱", 0),
]
# KEY_SPECS의 마지막 칸(지표 수)을 실측치로 덮는다 — 손으로 적힌 값은 무시한다
KEY_SPECS = [(k, l, u, r, h, KEY_COUNTS.get(k, n)) for k, l, u, r, h, n in KEY_SPECS]

REQUIRED = [k for k, _, _, req, _, _ in KEY_SPECS if req]
KEY_NAMES = {k for k, *_ in KEY_SPECS}

# ── 남에게 받아 쓸 수 없는 키 ────────────────────────────────────────────
# 자격증명에 **발급자의 환경**이 묶여 있어, 키를 그대로 넘겨받아도 내 자리에서는 실패한다.
# 그래서 이런 항목은 "팀원은 비워 두세요"가 아니라 **각자 자기 것을 발급**하는 게 정답이다.
# (예전 안내는 비워 두라고 했다 — 그러면 국내 수급 10개가 팀원 전원에게서 영원히 빈다.)
PERSONAL_KEYS: dict[str, str] = {
    "TOSSINVEST_CLIENT_ID":
        "앱에 **허용 IP를 등록**해야 하고 등록한 IP 밖에서 부르면 403이다. "
        "게다가 토큰이 계정당 동시에 하나뿐이라, 한 키를 둘이 쓰면 서로 401을 만든다.",
    "TOSSINVEST_CLIENT_SECRET": "위 Client ID와 같은 앱에서 함께 나온다.",
}
TOSS_LANDING = "https://developers.tossinvest.com"

PATH_SPECS: list[tuple[str, str, str]] = [
    ("OBSIDIAN_VAULT_PATH", "Obsidian 볼트 경로 (설정하면 볼트에도 바로 출력)",
     r"예: C:\Users\<이름>\MacroVault  · 비우면 output/ 에만 생성"),
    ("DATABOOK_OUTPUT_DIR", "산출물 위치 (저장소 바깥 권장)",
     r"예: C:\Users\<이름>\macro-data\output  · OneDrive 안에 두면 매일 동기화가 돈다"),
]
PATH_NAMES = {k for k, *_ in PATH_SPECS}



def _mask(v: str) -> str:
    return "*" * len(v) if len(v) <= 6 else v[:3] + "*" * (len(v) - 6) + v[-3:]


def missing_required(env: dict[str, str]) -> list[str]:
    return [k for k in REQUIRED if not env.get(k)]


def _read_dotenv() -> tuple[dict[str, str], list[str]]:
    """기존 .env를 (값, 원본줄)로 읽는다. **모르는 키를 보존**하기 위해 필요하다."""
    path = ROOT / ".env"
    if not path.exists():
        return {}, []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    vals: dict[str, str] = {}
    for line in lines:
        t = line.strip()
        if not t or t.startswith("#") or "=" not in t:
            continue
        k, _, v = t.partition("=")
        vals[k.strip()] = v.strip()
    return vals, lines


def write_env(values: dict[str, str]) -> Path:
    """.env 기록. ⚠ **KEY_SPECS/PATH_SPECS에 없는 항목도 그대로 살린다.**"""
    existing, _ = _read_dotenv()
    lines = [
        "# macro-databook 설정 — `python -m databook setup`이 생성/갱신합니다.",
        "# 이 파일은 .gitignore 대상 — 절대 커밋하거나 메신저로 보내지 마세요.",
        "",
        "# ───── API 키 ─────",
    ]
    for k, label, url, req, _help, n in KEY_SPECS:
        tag = "필수" if req else "선택"
        extra = f" · 지표 {n}개" if n else ""
        lines.append(f"# [{tag}] {label}{extra} — {url}")
        lines.append(f"{k}={values.get(k, existing.get(k, ''))}")
    lines += ["", "# ───── 경로 ─────"]
    for k, label, hint in PATH_SPECS:
        lines.append(f"# {label}  ({hint})")
        lines.append(f"{k}={values.get(k, existing.get(k, ''))}")
    # 마법사가 모르는 키(다른 브랜치·수동 추가분)를 잃지 않는다
    unknown = {k: v for k, v in existing.items() if k not in KEY_NAMES and k not in PATH_NAMES}
    if unknown:
        lines += ["", "# ───── 마법사가 모르는 항목 (자동 보존) ─────"]
        lines += [f"{k}={v}" for k, v in sorted(unknown.items())]
    lines.append("")
    path = ROOT / ".env"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


# ─────────────────────────── 키 살아있는지 확인 ───────────────────────────

def _get(url: str, timeout: int = 12) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "macro-databook/0.1 (setup check)"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def public_ip(timeout: int = 5) -> str:
    """토스 앱에 등록할 **내 공인 IP**. 실패하면 빈 문자열 — 설정을 막지 않는다.

    공유기 뒤라 `ipconfig`가 보여주는 사설 IP(192.168.*)는 등록해도 소용이 없다.
    등록해야 하는 건 밖에서 보이는 주소라 외부에 한 번 물어봐야 안다.
    """
    for url in ("https://api.ipify.org", "https://ifconfig.me/ip"):
        try:
            ip = _get(url, timeout=timeout).strip()
        except Exception:
            continue
        if ip and len(ip) <= 45 and all(c in "0123456789abcdefABCDEF.:" for c in ip):
            return ip
    return ""


def _toss_http_msg(code: int) -> tuple[bool | None, str]:
    """토스 응답 코드를 사람이 고칠 수 있는 말로 바꾼다.

    **403과 401을 구분하는 것이 핵심**이다 — 403은 키가 맞는데 IP가 틀린 것이라
    키를 다시 발급받으면 시간만 버린다.
    """
    if code == 403:
        ip = public_ip()
        where = f" · 지금 이 PC의 공인 IP: {ip}" if ip else ""
        return False, (f"허용 IP 미등록 — 키는 맞고 **IP가 안 맞습니다**. "
                       f"{TOSS_LANDING} 앱 설정에서 허용 IP를 등록하세요{where}")
    if code in (400, 401):
        return False, f"인증 실패(HTTP {code}) — Client ID/Secret을 다시 확인하세요"
    return None, f"확인 못 함(HTTP {code})"


def _verify_toss(cid: str, sec: str) -> tuple[bool | None, str]:
    """토큰을 실제로 발급하고 GET까지 한 번 해 본다.

    토큰만 받아 보고 끝내면 안 된다 — **IP 검사는 호출 단계에서** 걸리므로
    토큰이 나와도 실제 조회에서 403이 난다.

    ⚠ 토큰은 계정당 동시에 하나뿐이라, 여기서 발급하면 돌고 있던 수집의 토큰이 죽는다.
      그래서 수집이 잡고 있는 락을 존중하고, 못 잡으면 확인을 건너뛴다.
    """
    if not sec:
        return None, "Client Secret이 없어 확인 못 함 — 같은 앱의 Secret도 넣으세요"
    from .tosslock import toss_lock
    with toss_lock("setup 키 확인", wait=0, quiet=True) as held:
        if not held:
            return None, "다른 작업이 토스 API를 쓰는 중 — 확인 건너뜀"
        body = urllib.parse.urlencode({"grant_type": "client_credentials",
                                       "client_id": cid, "client_secret": sec}).encode()
        req = urllib.request.Request(
            "https://openapi.tossinvest.com/oauth2/token", data=body,
            headers={"Content-Type": "application/x-www-form-urlencoded",
                     "User-Agent": "macro-databook/0.1 (setup check)"})
        try:
            tok = json.loads(urllib.request.urlopen(req, timeout=30).read()).get("access_token")
        except urllib.error.HTTPError as e:
            return _toss_http_msg(e.code)
        except Exception as e:
            return None, f"확인 못 함({type(e).__name__})"
        if not tok:
            return False, "토큰이 오지 않았습니다 — Client ID/Secret을 다시 확인하세요"
        try:
            probe = urllib.request.Request(
                "https://openapi.tossinvest.com/api/v1/market-indicators/prices?symbols=KOSPI",
                headers={"Authorization": "Bearer " + tok, "Accept": "application/json",
                         "User-Agent": "macro-databook/0.1 (setup check)"})
            urllib.request.urlopen(probe, timeout=30).read()
        except urllib.error.HTTPError as e:
            return _toss_http_msg(e.code)
        except Exception as e:
            return None, f"토큰은 받았으나 호출 확인 못 함({type(e).__name__})"
    return True, "정상 — 토큰 발급 + 실호출까지 확인"


def verify_key(name: str, value: str, peer: dict[str, str] | None = None) -> tuple[bool | None, str]:
    """(성공?, 메시지). None = 확인 수단 없음 — 형식만 보고 넘어간다."""
    if not value:
        return None, "비어 있음"
    try:
        if name == "TOSSINVEST_CLIENT_ID":
            return _verify_toss(value, (peer or {}).get("TOSSINVEST_CLIENT_SECRET", ""))
        if name == "FRED_API_KEY":
            d = json.loads(_get("https://api.stlouisfed.org/fred/series?series_id=DGS10"
                                f"&api_key={urllib.parse.quote(value)}&file_type=json"))
            return (True, "정상") if d.get("seriess") else (False, "응답에 계열 없음")
        if name == "E_STAT_APP_ID":
            # ⚠ 검색어에 일본어를 그대로 넣으면 URL 인코딩 단계에서 깨진다 — ASCII 코드로 조회한다
            d = json.loads(_get("https://api.e-stat.go.jp/rest/3.0/app/json/getStatsList"
                                f"?appId={urllib.parse.quote(value)}&statsCode=00100401&limit=1"))
            st = d.get("GET_STATS_LIST", {}).get("RESULT", {}).get("STATUS")
            # 0=정상, 1=조건에 맞는 데이터 없음(인증은 통과), 100=인증 실패
            return (True, "정상") if st in (0, 1) else (False, f"STATUS {st} — 인증 실패")
        if name == "ECOS_API_KEY":
            t = _get(f"https://ecos.bok.or.kr/api/KeyStatisticList/{urllib.parse.quote(value)}/json/kr/1/1")
            if "KeyStatisticList" in t and "RESULT" not in t[:200]:
                return True, "정상"
            return False, "인증 실패(응답에 오류 코드)"
    except urllib.error.HTTPError as e:
        # ⚠ 틀린 키를 "확인 못 함"으로 넘기면 오타를 못 잡는다.
        # FRED는 잘못된 키에 **400**을 준다 — 인증 실패로 단정해야 한다.
        if e.code in (400, 401, 403):
            return False, f"인증 실패(HTTP {e.code}) — 키를 다시 확인하세요"
        return None, f"확인 못 함(HTTP {e.code})"
    except Exception as e:
        return None, f"확인 못 함({type(e).__name__})"
    return None, "확인 수단 없음(형식만)"


VERIFIABLE = ("FRED_API_KEY", "E_STAT_APP_ID", "ECOS_API_KEY", "TOSSINVEST_CLIENT_ID")


# ─────────────────────────── 마법사 ───────────────────────────

def _ask(prompt: str) -> str:
    try:
        return input(prompt).strip()
    except EOFError:
        return ""


def _print_plan(env: dict[str, str]) -> list[tuple]:
    """지금 없는 키를 발급 링크와 함께 **한 번에** 보여준다. 반환 = 물어볼 항목."""
    have = [s for s in KEY_SPECS if env.get(s[0])]
    miss = [s for s in KEY_SPECS if not env.get(s[0])]
    live = NO_KEY_COUNT + sum(s[5] for s in have)

    print("\n═══ macro-databook 키 설정 ═══")
    print(f"전체 지표 {TOTAL_COUNT}개 중 **{NO_KEY_COUNT}개는 키가 전혀 필요 없습니다**")
    print("  (관세청·일본은행·중국인민은행·SEC·DBnomics 등)")
    print(f"현재 설정된 키로 도는 지표: 약 {live}개\n")

    if have:
        print("── 이미 설정됨")
        for k, label, _u, _r, _h, n in have:
            print(f"   ✓ {label} ({_mask(env[k])})")
        print()
    if not miss:
        print("모든 키가 설정돼 있습니다.\n")
        return []

    def _row(spec: tuple) -> None:
        k, label, url, req, help_, n = spec
        tag = "필수" if req else "선택"
        cnt = f"{n}개" if n else "—"
        print(f"   [{tag}] {label}")
        print(f"        {cnt:>8}   {url}")
        if help_:
            print(f"        └ {help_}")

    shared = sorted([x for x in miss if x[0] not in PERSONAL_KEYS], key=lambda x: not x[3])
    personal = [x for x in miss if x[0] in PERSONAL_KEYS]

    if shared:
        print("── 아직 없는 키 — 아래 링크를 한꺼번에 열어 발급받은 뒤 붙여넣으세요")
        for spec in shared:
            _row(spec)
        print("\n   ※ 지금 다 받을 필요 없습니다. 엔터로 건너뛰면 그 지표만 '수집 실패'로 표시되고")
        print("      나머지는 정상 동작합니다. 나중에 `python -m databook setup`으로 다시 채우면 됩니다.\n")

    # 남의 것을 받아 쓸 수 없는 키는 **따로 세워** 안내한다.
    # 위 목록에 섞어 두면 "선택"으로 보여서 아무도 안 받고, 국내 수급이 팀 전체에서 빈다.
    if personal:
        print("── 본인 것만 통하는 키 — 남에게 받아 쓸 수 없습니다")
        for spec in personal:
            _row(spec)
        ip = public_ip()
        print()
        print("   토스 앱은 **허용 IP에 묶여** 있습니다. 남의 Client ID/Secret을 그대로 넣으면")
        print("   키가 맞아도 403이 납니다. 각자 앱을 만들고 자기 IP를 등록하세요 (무료·즉시).")
        print(f"     1) {TOSS_LANDING} 로그인 → 앱 생성")
        if ip:
            print(f"     2) 허용 IP에 지금 이 PC의 공인 IP를 등록:  {ip}")
        else:
            print("     2) 허용 IP에 지금 이 PC의 **공인 IP**를 등록")
            print("        (자동 조회 실패 — https://api.ipify.org 를 브라우저로 열면 나옵니다)")
        print("     3) 발급된 Client ID / Secret을 아래에 붙여넣기")
        print("   ※ 공유기·회사망·핫스팟은 IP가 바뀝니다. 바뀌면 다시 등록해야 403이 풀립니다.")
        print("   ※ 안 넣어도 나머지는 정상입니다 — 국내 수급 지표 10개만 비어 있게 됩니다.\n")

    return shared + personal


def run_wizard() -> int:
    env = load_env()
    values: dict[str, str] = {k: env.get(k, "") for k, *_ in KEY_SPECS}
    values.update({k: env.get(k, "") for k, *_ in PATH_SPECS})

    ask_list = _print_plan(env)   # 이미 필수 → 선택 → 토스 순으로 정렬돼 있다
    if ask_list:
        ans = _ask("링크를 열어 키를 받아오셨나요? 지금 입력하려면 엔터 (나중에 하려면 s) : ")
        if ans.lower().startswith("s"):
            print("건너뜁니다. 나중에 `python -m databook setup`을 다시 실행하세요.")
            return 0
        print()
        for k, label, url, req, help_, _n in ask_list:
            mark = "  ← 본인 앱에서 발급한 값" if k in PERSONAL_KEYS else ""
            v = _ask(f"{label}{mark}\n   {k} = ")
            if v:
                values[k] = v
            print()

    print("── 경로 (엔터=유지/생략)")
    for k, label, hint in PATH_SPECS:
        cur = env.get(k, "")
        print(f"   {label}")
        print(f"   {hint}")
        v = _ask(f"   {k} = " + (f"(현재 {cur}) " if cur else ""))
        values[k] = v if v else cur
        print()

    path = write_env(values)
    print(f"저장 완료 → {path}\n")

    # 넣은 키가 실제로 동작하는지 확인 — 오타를 수집 후에 알게 되는 일을 막는다
    checks = [(k, values.get(k, "")) for k in VERIFIABLE if values.get(k)]
    if checks:
        print("── 키 확인 중…")
        for k, v in checks:
            ok, msg = verify_key(k, v, values)
            mark = "✓" if ok else ("✗" if ok is False else "?")
            print(f"   {mark} {k}: {msg}")
        print()

    still = missing_required(values)
    if still:
        print(f"⚠ 아직 비어 있는 필수 키: {', '.join(still)}")
        print("  해당 지표만 '수집 실패'로 표시되고 나머지는 정상입니다.")
    print("이제 `python -m databook run` 으로 수집하세요.")
    return 0


def ensure_keys_interactive(env: dict[str, str]) -> dict[str, str]:
    """run 진입 시 호출. 필수 키가 없고 대화형 터미널이면 마법사를 권한다."""
    miss = missing_required(env)
    if not miss:
        return env
    if sys.stdin.isatty():
        print(f"\n필수 API 키가 없습니다: {', '.join(miss)}")
        ans = _ask("지금 설정 마법사를 실행할까요? [Y/n] ")
        if ans.lower() not in ("n", "no"):
            run_wizard()
            return load_env()
    else:
        print(f"\n⚠ 필수 키 없음({', '.join(miss)}). 대화형이 아니라 마법사를 건너뜁니다.")
        print("  → `python -m databook setup` 또는 환경변수/.env로 넣으세요.")
    return env


if __name__ == "__main__":
    sys.exit(run_wizard())
