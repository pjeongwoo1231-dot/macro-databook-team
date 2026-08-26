"""환경설정(.env)·indicators.yaml 로딩. yaml이 SSOT — 지표를 코드에 하드코딩하지 않는다."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
YAML_PATH = ROOT / "indicators.yaml"


def _output_root() -> Path:
    """산출물 위치. 기본은 `<repo>/output`, `DATABOOK_OUTPUT_DIR`로 옮길 수 있다.

    **왜 옮길 수 있어야 하나** — 이 저장소가 OneDrive·Dropbox 안에 있으면
    산출물이 전부 클라우드로 동기화된다. 종목 패널만 CSV 4,300개이고
    원문 아카이브는 PDF 수백 MB다. **매일 바뀌는 대용량 산출물을 동기화 폴더에 두면
    업로드가 끊이지 않고, 파일 삭제마다 확인창이 뜬다**(2026-08-19에 실제로 겪었다).
    코드·yaml은 동기화하되 산출물은 로컬에 두는 편이 낫다.

    ⚠ 값을 바꾼 뒤에는 기존 `output/`을 **손으로 옮겨야 한다** — 자동으로 따라가지 않는다.
    """
    v = os.environ.get("DATABOOK_OUTPUT_DIR", "").strip()
    if not v:
        env_file = ROOT / ".env"
        if env_file.exists():
            for line in env_file.read_text(encoding="utf-8", errors="replace").splitlines():
                line = line.strip()
                if line.startswith("DATABOOK_OUTPUT_DIR") and "=" in line:
                    v = line.split("=", 1)[1].strip()
                    break
    return Path(v).expanduser() if v else ROOT / "output"


OUTPUT_DIR = _output_root()
CACHE_DIR = ROOT / "cache"

TEAM_META = {
    "team_1": ("1", "성장·경기 (Growth & Cycle)", "1_Growth"),
    "team_2": ("2", "물가·정책·금리 (Inflation·Policy·Rates)", "2_Inflation_Policy_Rates"),
    "team_3": ("3", "유동성·신용·심리 (Liquidity·Credit·Sentiment)", "3_Liquidity_Credit_Sentiment"),
    "team_4": ("4", "글로벌·지정학·무역 (Global·Geopolitics·Trade)", "4_Global_Geopolitics_Trade"),
}


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    dotenv = ROOT / ".env"
    if dotenv.exists():
        for line in dotenv.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            env[k.strip()] = v.strip()
    for k in ("FRED_API_KEY", "ECOS_API_KEY", "KOSIS_API_KEY", "DATA_GO_KR_KEY",
              "EIA_API_KEY", "OPINET_API_KEY", "E_STAT_APP_ID", "DATA_GO_KR_LENDBORR_KEY", "NAVER_CLIENT_ID", "NAVER_CLIENT_SECRET",
              "TOSSINVEST_CLIENT_ID", "TOSSINVEST_CLIENT_SECRET",
              "OBSIDIAN_VAULT_PATH"):
        env.setdefault(k, os.environ.get(k, ""))
    return env


def load_registry() -> dict[str, Any]:
    with open(YAML_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    for team_key in TEAM_META:
        for ind in data.get(team_key, []):
            ind["team"] = team_key
    return data


def all_indicators(registry: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for team_key in TEAM_META:
        out.extend(registry.get(team_key, []))
    return out
