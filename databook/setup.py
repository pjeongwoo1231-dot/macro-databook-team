"""대화형 키 설정 마법사 — 다운받은 사람이 실행하면 필요한 API 키를 하나씩 물어보고 .env에 저장한다.

`python -m databook setup` 으로 단독 실행하거나, `run` 시 필수 키가 없고 터미널이 대화형이면 자동 호출된다.
전부 무료 키. 필수 4종(FRED·ECOS·KOSIS·data.go.kr)만 있으면 대부분 지표가 수집된다."""
from __future__ import annotations

import sys
from pathlib import Path

from .core import ROOT, load_env

# (환경변수, 라벨, 발급처, 필수여부, 도움말)
KEY_SPECS: list[tuple[str, str, str, bool, str]] = [
    ("FRED_API_KEY", "미국 지표(FRED, 45종+)", "https://fred.stlouisfed.org/docs/api/api_key.html", True, "무료 가입 후 즉시 발급"),
    ("ECOS_API_KEY", "한국은행 지표(ECOS)", "https://ecos.bok.or.kr/api/", True, "무료 인증키 신청"),
    ("KOSIS_API_KEY", "통계청 지표(KOSIS)", "https://kosis.kr/openapi/", True, "무료 활용신청"),
    ("DATA_GO_KR_KEY", "공공데이터포털(국토부·관세청·부동산원 공용)", "https://www.data.go.kr", True, "일반 인증키(Decoding) 사용"),
    ("EIA_API_KEY", "미 에너지정보청(원유·가스)", "https://www.eia.gov/opendata/register.php", False, "없으면 DEMO_KEY 폴백(제한적)"),
    ("OPINET_API_KEY", "오피넷 국내유가", "https://www.opinet.co.kr/user/custc/custceco.do", False, "없으면 해당 지표만 수동 안내"),
    ("NAVER_CLIENT_ID", "네이버 개발자센터 검색 — Client ID", "https://developers.naver.com/apps", False, "★NCP 아님. 앱 등록 후 '검색'+'데이터랩' 추가"),
    ("NAVER_CLIENT_SECRET", "네이버 개발자센터 검색 — Client Secret", "https://developers.naver.com/apps", False, "위 ID와 같은 앱에서 발급"),
    ("TOSSINVEST_CLIENT_ID", "토스증권 Open API — Client ID", "https://developers.tossinvest.com", False, "★WTS > 설정 > Open API에서 발급. 같은 화면의 허용 IP에 이 PC 공인 IP를 반드시 등록(미등록 시 403)"),
    ("TOSSINVEST_CLIENT_SECRET", "토스증권 Open API — Client Secret", "https://developers.tossinvest.com", False, "위 ID와 같은 앱. 토큰은 동시 1개만 유효해 다른 프로세스와 같이 돌리면 서로 401이 된다"),
]
REQUIRED = [k for k, _, _, req, _ in KEY_SPECS if req]

VAULT_SPEC = (
    "OBSIDIAN_VAULT_PATH",
    "Obsidian 공용 vault 경로 (설정하면 매 실행 시 vault의 Macro/에 바로 생성)",
    "예: C:\\Users\\me\\MacroVault  (비워두면 output/ 폴더에만 생성)",
)


def _mask(v: str) -> str:
    if len(v) <= 6:
        return "*" * len(v)
    return v[:3] + "*" * (len(v) - 6) + v[-3:]


def missing_required(env: dict[str, str]) -> list[str]:
    return [k for k in REQUIRED if not env.get(k)]


def write_env(values: dict[str, str]) -> Path:
    """KEY_SPECS + vault 값을 .env 파일로 (주석 포함) 기록. 빈 값은 빈 채로 남긴다."""
    dotenv = ROOT / ".env"
    lines = [
        "# macro-databook 설정 — python -m databook setup 이 생성/갱신.",
        "# 전부 무료 키. 이 파일은 .gitignore 대상 — 절대 커밋하지 말 것.",
        "",
    ]
    for k, label, url, req, _ in KEY_SPECS:
        tag = "필수" if req else "선택"
        lines.append(f"# [{tag}] {label} — 발급: {url}")
        lines.append(f"{k}={values.get(k, '')}")
    lines.append("")
    lines.append(f"# {VAULT_SPEC[1]}")
    lines.append(f"{VAULT_SPEC[0]}={values.get(VAULT_SPEC[0], '')}")
    lines.append("")
    dotenv.write_text("\n".join(lines), encoding="utf-8")
    return dotenv


def _ask(prompt: str) -> str:
    try:
        return input(prompt).strip()
    except EOFError:
        return ""


def run_wizard() -> int:
    """대화형으로 키를 채운다. 기존 값은 엔터로 유지. 반환 0=성공."""
    print("\n═══ macro-databook 키 설정 마법사 ═══")
    print("각 항목에 키를 붙여넣고 엔터. 이미 있는 값은 그냥 엔터=유지, 건너뛸 항목도 엔터.")
    print("전부 무료입니다. 필수 4종(FRED·ECOS·KOSIS·data.go.kr)만 있으면 대부분 수집됩니다.\n")

    env = load_env()
    values: dict[str, str] = {k: env.get(k, "") for k, *_ in KEY_SPECS}

    for k, label, url, req, help_ in KEY_SPECS:
        cur = values.get(k, "")
        tag = "필수" if req else "선택"
        print(f"── [{tag}] {label}")
        print(f"   발급: {url}  ({help_})")
        if cur:
            new = _ask(f"   현재값 {_mask(cur)} — 유지=엔터 / 새 값 입력: ")
            values[k] = new if new else cur
        else:
            values[k] = _ask(f"   {k} = ")
        print()

    k, label, hint = VAULT_SPEC
    cur = env.get(k, "")
    print(f"── [선택] {label}")
    print(f"   {hint}")
    new = _ask(f"   {k} = " + (f"(현재 {cur}) " if cur else ""))
    values[k] = new if new else cur

    path = write_env(values)
    still = missing_required(values)
    print(f"\n저장 완료 → {path}")
    if still:
        print(f"⚠ 아직 비어있는 필수 키: {', '.join(still)} — 해당 소스 지표는 수집 실패로 표시됩니다.")
    else:
        print("필수 키 모두 설정됨. 이제 `python -m databook run` 으로 수집하세요.")
    return 0


def ensure_keys_interactive(env: dict[str, str]) -> dict[str, str]:
    """run 진입 시 호출. 필수 키가 없고 터미널이 대화형이면 마법사를 돌리고 env를 다시 로드한다."""
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
        print("  → `python -m databook setup` 실행 또는 환경변수/.env로 키를 넣으세요. 없는 키의 지표는 실패로 표시됩니다.")
    return env


if __name__ == "__main__":
    sys.exit(run_wizard())
