"""Runyour API 최소 실행 예시 — 모델에게 한 마디 묻고 답을 받는다.

실행:  python tools/runyour_example.py "질문"

**키는 코드에 쓰지 않는다.** 저장소 루트 `.env`의 RUNYOUR_API_KEY에서만 읽는다.
키를 소스에 박으면 그 파일을 공유하는 순간 키가 새고, git에 한 번 올라가면 지우기 어렵다.
환경변수/.env는 그걸 막는 가장 싼 방법이다.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def settings() -> tuple[str, str, str]:
    """.env → 환경변수 순으로 찾는다. 키가 없으면 친절히 멈춘다."""
    env: dict[str, str] = {}
    f = ROOT / ".env"
    if f.exists():
        for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            env[k.strip()] = v.strip().strip('"').strip("'")

    def pick(name: str, default: str = "") -> str:
        """**.env를 환경변수보다 우선한다.**

        반대로 짰다가 하루를 날렸다(2026-09-16). OS 환경변수에 예전 RUNYOUR_API_KEY가
        남아 있었고, 그게 .env의 새 키를 가려서 계속 402(크레딧 없음)가 났다.
        콘솔에는 크레딧이 멀쩡히 10만 있는데 API만 거부하니 계정 문제로 오진했다.
        .env는 이 프로젝트에 대해 **명시적으로** 적어둔 값이므로 그쪽이 이긴다.
        둘이 다르면 조용히 넘기지 않고 경고한다 — 조용한 우선순위가 사고의 씨앗이다.
        """
        envv, osv = env.get(name), os.environ.get(name)
        if envv and osv and envv != osv:
            print(f"  ⚠ {name}: OS 환경변수와 .env 값이 다르다 → .env를 쓴다 "
                  f"(환경변수 {osv[:12]}… 무시)", file=sys.stderr)
        return envv or osv or default

    key = pick("RUNYOUR_API_KEY")
    if not key:
        sys.exit("RUNYOUR_API_KEY가 없다 — .env에 넣었는지 확인할 것 (키를 코드에 쓰지 말 것)")
    return (pick("RUNYOUR_API_BASE", "https://api.runyour.ai/v1"),
            key,
            pick("RUNYOUR_MODEL", "openai/gpt-5.4-mini"))


def ask(question: str) -> str:
    base, key, model = settings()
    body = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": "한국어로 간결하게 답한다."},
            {"role": "user", "content": question},
        ],
        "max_completion_tokens": 300,
    }).encode("utf-8")

    req = urllib.request.Request(
        f"{base}/chat/completions",
        data=body,
        headers={"Authorization": f"Bearer {key}",      # ← Bearer 토큰 방식
                 "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            d = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        # 본문에 진짜 원인이 들어 있다. 상태코드만 보면 못 고친다.
        sys.exit(f"HTTP {e.code}\n{e.read().decode('utf-8', 'replace')[:500]}")

    usage = d.get("usage", {})
    print(f"[모델] {d.get('model', model)}")
    print(f"[토큰] 입력 {usage.get('prompt_tokens', '?')} · "
          f"출력 {usage.get('completion_tokens', '?')}")
    return d["choices"][0]["message"]["content"]


if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "BIS 워킹페이퍼가 무엇인지 두 문장으로 설명해줘."
    print(ask(q))
