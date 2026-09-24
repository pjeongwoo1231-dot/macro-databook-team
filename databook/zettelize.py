"""BIS 원문 판독 → 제텔 초안. **모델이 읽고, 다른 모델이 검증한다.**

**왜 외부 모델인가** — 논문 한 편이 평균 13만 자다. 1,375편이면 4,700만 토큰으로
대화형 에이전트가 직접 읽는 건 불가능하다. 외부 API에 읽히고 요약 한 장만 받아온다.

**왜 그대로 믿지 않는가** — 볼트가 이미 겪었다. 「마누스 원문 라이브러리 검수」에서
"전수 판독" 주장이 허위로 드러났고 등급 오판까지 나와 실측으로 정정해야 했다.

**그래서 관문을 셋 둔다. 셋 다 사람 손이 안 간다.**

    관문 A  인용 대조 (기계)   모델이 뽑은 근거 문장이 PDF 원문에 **문자열 그대로** 있는가.
                              없으면 지어낸 것이다. 의견이 아니라 문자열 비교라 100% 자동.
    관문 B  교차검증 (다른 모델) **판독한 모델과 다른 모델**이 같은 원문을 독립적으로 읽고,
                              그 주장이 논문에서 실제로 따라 나오는지 판정한다.
                              같은 모델에게 자기 답을 검토시키면 자기 확증만 한다.
    관문 C  사람               위 둘이 **엇갈린 것만** 본다. 전수가 아니라 잔여분이다.

셋 다 통과하면 `verification: machine-cross-verified`로 승격 후보가 된다.
**`human_verified`는 끝까지 false다** — 사람이 안 읽었으니까. 노동은 기계가 대신해도
기록은 사실대로 적는다. 볼트가 비싸게 배운 규칙이다.
"""
from __future__ import annotations

import http.client
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

from .core import load_env

SUB = "06_SourceArchive/06-BIS-Archive-Catalog/Sources"
PDFDIR = "06_SourceArchive/06-BIS-Archive-Catalog/PDFs"
DRAFTS = "07_Zettel/_drafts"

# 본문을 통째로 넣지 않는다. 앞(초록·서론)과 뒤(결론)가 주장을 담고
# 중간의 표·부록은 토큰만 먹는다. 놓친 게 있으면 관문 B에서 드러난다.
# 텍스트 층이 없는 스캔본을 거르는 하한.
# 초기 BIS 논문(WP 1~6 등, 1970~80년대)은 이미지 스캔이라 추출 결과가 30~50자다.
# 그걸 그대로 모델에 보내면 **빈 본문에서 인용문을 지어낸다** — 2026-09-16 WP 2에서 실측했다
# (본문 26자인데 인용 3개를 만들어냈고 관문 A에서 0/3으로 전부 걸렸다).
# 관문이 잡아주긴 하지만 호출 비용이 그냥 버려지므로 여기서 먼저 끊는다.
MIN_TEXT_CHARS = 3_000

# 관문 A의 합격선. **전건일치만 통과로 두면 멀쩡한 초안을 버린다** —
# 2026-09-16 첫 배치 실측: 불일치 7건 중 **6건이 2/3**이었다. 모델이 인용 두 개는
# 원문 그대로 가져오고 하나만 말을 바꾸는 패턴이다. 그건 환각이 아니라 부주의다.
# 그래서 2건 이상이면 **부분통과**로 교차검증까지 보내되 노트에 그대로 표기한다.
# 1건 이하는 본문을 안 봤다는 뜻이므로 거기서 끊는다(교차검증 호출도 아낀다).
QUOTES_MIN_PASS = 2

HEAD_CHARS = 60_000
TAIL_CHARS = 30_000

# 판독 모델과 **다른 계열**이어야 한다. 같은 모델은 자기 답을 검토시켜도 자기 확증만 한다.
# 2026-09-17 교체: 판독을 Gemini로 옮기면서 검증은 Qwen으로 내렸다.
# (같은 3편 실측에서 Gemini가 GPT-5.4-mini보다 t값·표본수·R²까지 더 잡아냈고 단가도 31원 vs 47원이었다)
DEFAULT_READ_MODEL = "gemini/gemini-flash-latest"
# ⚠ **Qwen을 쓰지 마라.** 2026-09-17 단발 지연 실측(같은 논문, 본문 18만 자):
#     gemini/gemini-flash-latest   23.3초  ✅
#     openai/gpt-5.4-mini          10.7초  ✅
#     qwen/qwen3.5-plus            253초 매달렸다가 RemoteDisconnected  ❌
# 관문 A를 통과한 논문은 전부 검증 모델을 부르므로, 검증이 느리면 **전체가 그 속도로 묶인다.**
# 실제로 Qwen을 물린 동안 편당 8분(1.2편/분)까지 떨어졌고, 워커를 10개로 올려도
# 4개일 때보다 느렸다 — 동시성을 올려도 막힌 파이프는 넓어지지 않는다.
DEFAULT_AUDIT_MODEL = "openai/gpt-5.4-mini"

# 교차검증에는 **전문을 보내지 않는다.** 검증의 일은 "주장이 과장됐나"를 보는 것이고
# 그건 초록·서론·결과·결론이면 판정된다. 전문을 두 번 보내면 비용이 정확히 두 배가 되는데
# 얻는 게 없다. 앞뒤를 남기고 가운데(표·부록)를 접는다.
AUDIT_HEAD = 30_000
AUDIT_TAIL = 20_000

READ_PROMPT = """당신은 거시경제 리서치 노트를 만든다. 아래 BIS 워킹페이퍼를 읽고 JSON만 출력한다.

**이 노트가 존재하는 이유를 먼저 알아라.**
읽는 사람은 시황을 쓰다가 "이 판단의 근거가 있나?"를 확인하러 온다. 그래서 필요한 것은
**"이 논문이 무슨 얘기를 한다"가 아니라 "무엇이 얼마만큼 측정됐고, 왜 그런가"** 다.
숫자 없는 요약은 초록의 재탕이고, 그건 쓸모가 없다. **수치를 못 찾으면 그 노트는 실패다.**

--- 좋은 노트가 어떤 것인지 (실제 예시) ---
claim   : "12개월 시계에서 Baa−Aaa 스프레드는 예측력이 없다"
numbers : ["Baa-Aaa 고용 예측 표준화계수 +0.054 [t=1.15] — 비유의이고 부호가 이론과 반대",
           "같은 표 GZ 스프레드는 −0.497 [t=13.4]", "표본 1973:M1–2010:M9 미국",
           "표준편차: Baa-Aaa 50bp / CP-Bill 67bp / GZ 약 100bp"]
mechanism: "Baa-Aaa는 만기·등급 구성이 고정된 총계 지수라 신용의 질적 변화를 흡수하지 못한다.
            GZ는 개별 채권 5,982종을 전 만기·전 등급에서 모아 구성이 움직인다."
so_what : "신용 스프레드로 경기를 판정할 때 Baa-Aaa를 근거로 쓰지 않는다. GZ나 CP-Bill을 본다."
--- 여기까지 예시 ---

**규칙**

1. `claim` — 가장 값나가는 주장 **한 문장**, 한국어, **단언**으로.
   나쁨: "지준 수요에 관한 연구"      좋음: "유동성 규제는 지준 수요를 늘리지 않는다"

   **단, 단언은 "조건을 떼어내라"는 뜻이 아니다.** 논문이 붙여놓은 기간·표본·범위·정도를
   문장 안에 그대로 남겨라. 조건을 떼면 문장은 세지지만 **논문이 하지 않은 말이 되고,
   교차검증에서 통째로 탈락한다.** 이건 이 파이프라인에서 가장 많이 나온 실패다
   (2026-09-17 실측: 탈락 179건 중 **156건이 내용이 아니라 이 과장 때문**이었다).

   논문에 그 말이 없으면 쓰지 마라 — **"영구히·전혀·항상·모든·절대·완전히·극복했다·해소한다"**.
   논문이 "5년까지 지속"이라 했으면 5년이라 쓰고, "크지 않다"면 "크지 않다"라고 쓴다.
   "줄인다"를 "없앤다"로, "진전을 이뤘다"를 "극복했다"로 올리지 마라.

   실제로 탈락한 문장들 (전부 발견 자체는 맞았는데 끝맺음이 논문을 넘었다):
     ✘ "...공간적 제약을 해소하여 고용률과 임금을 **장기적으로 영구히** 상승시킨다"
       ✔ "...이동수단 구매 신용은 공식 고용률과 임금을 높이고 그 효과가 **5년 후까지** 지속된다"
     ✘ "비은행은 ... 대출 관계의 완충 효과도 **전혀 제공하지 않는다**"
       ✔ "비은행은 ... 대출 관계가 있어도 그 격차가 **의미 있게 줄지 않는다**"
     ✘ "주요 신흥국은 ... 전통적 원죄를 **극복했으나**, ..."
       ✔ "주요 신흥국은 ... 원죄 극복에 **상당한 진전을 이뤘으나**, ..."
   핵심은 약하게 쓰라는 게 아니다. **논문이 잰 만큼 정확히 쓰라는 것이다.**

   **그리고 claim은 관계 하나다.** 결과 두세 개를 한 문장에 접합하지 마라. 수치 임계·계수·
   지연시간은 claim이 아니라 `numbers`에 넣는다. 접합하면 **그중 하나만 어긋나도 문장 전체가
   탈락한다** — 2026-09-17 실측에서 탈락 사유가 과장에서 이 접합으로 그대로 옮겨갔다.
     ✘ "AI 인프라 경쟁은 승자독식 유인으로 사회적 최적의 약 1.5배를 투자하게 하며,
        3조 달러를 넘으면 기대 순잉여가 음(−)으로 돌아선다"   ← 결과 두 개 + 임계 하나
     ✔ "AI 인프라 경쟁은 승자독식 유인 때문에 사회적 최적을 넘는 과잉투자를 낳는다"
        (1.5배도 3조 달러도 `numbers`로 내린다)
   맨 위 모범 예시를 다시 봐라 — "12개월 시계에서 Baa−Aaa 스프레드는 예측력이 없다".
   **조건 하나, 관계 하나, 수치 없음.** 그게 claim이고, 나머지는 전부 다른 필드의 몫이다.

2. `numbers` — **3~6개. 이게 이 노트의 핵심이다.** 각 항목에 반드시 담을 것:
   **값 + 단위 + 그 값이 무엇인지 + (있으면) 유의성·표본·기간.**
   계수·탄력성·효과크기·표본수·관측기간·임계값·백분율 등 **논문이 실제로 측정한 수**를 적는다.
   나쁨: "유의한 영향이 있었다" / "크게 증가했다" / "상관관계가 높다"  ← **숫자가 없으면 전부 실격**
   좋음: "정책금리 100bp 인상 시 대출 2.3% 감소 [t=4.1], 2003~2019 유로존 은행 1,842곳"
   논문에 수치가 정말 없으면(순수 이론모형 등) 빈 배열로 두고 `confidence`를 낮춰라. 지어내지 마라.

3. `mechanism` — **왜** 그 결과가 나오는가. 인과 사슬을 2~4문장으로.
   결과를 다시 말하는 게 아니라 **작동 원리**를 적는다.
   나쁨: "금리가 오르면 대출이 준다"   좋음: "금리 상승 → 은행 조달비용 상승 → 자본이 얇은 은행부터
   위험가중자산을 줄인다 → 담보가치 하락이 겹치면 신용제약 기업에 집중된다"

4. `so_what` — **시황에서 언제 이 논문을 부르는가.** 어느 지표를 판정할 때 쓰는가, 무엇을 하지 말라는 얘기인가.
   한두 문장. "참고가 된다" 같은 공허한 말 금지.

5. `contra` — 이 주장이 **깨지는 조건**. 저자가 밝힌 경계·예외·반대 방향이 나오는 구간.
   없으면 빈 배열.

6. `evidence` — 주장을 떠받치는 **원문 문장 3개**. 반드시 **영어 원문 그대로**.
   오타·이상한 띄어쓰기까지 **손대지 말고 글자 단위로 복사**하라. 고쳐 쓰면 대조에 실패한다.
   요약·번역·재구성 금지. 이 문자열을 원문과 기계 대조하며, 못 찾으면 이 노트는 폐기된다.
   가능하면 **수치가 들어간 문장**을 고를 것.

7. `limits` — **저자가 스스로 밝힌 한계**를 한국어 한 문장씩. 없으면 빈 배열.
   한계란 "이 결과를 믿으면 안 되는 조건"이다 — 표본 제약, 식별 실패, 모형 가정, 일반화 불가.
   **"우리 결과의 함의는…" 같은 자랑은 한계가 아니다.** 지어내지 마라.

8. `axis` — growth / inflation / liquidity / geopolitics 중 하나.

9. `confidence` — 확신이 없으면 낮게. 낮다고 불이익 없다. **틀린 확신이 해롭다.**

출력 형식 (JSON만, 다른 말 절대 금지)
{"claim":"...","axis":"...","summary":"3~5문장 한국어","numbers":["값+단위+무엇+표본"],"mechanism":"...","so_what":"...","contra":["..."],"evidence":["영어 원문 그대로","영어 원문 그대로","영어 원문 그대로"],"limits":["..."],"confidence":0.0}

--- 논문: BIS WP __N__ · __TITLE__ ---
__BODY__
"""

AUDIT_PROMPT = """당신은 심사자다. 다른 조수가 아래 논문을 읽고 주장을 하나 뽑았다.
**그 주장이 이 논문에서 실제로 따라 나오는지** 당신이 직접 원문을 읽고 판정하라.

주의
- 조수의 주장에 끌려가지 말 것. 당신은 반대 증거를 찾는 사람이다.
- 논문이 말하지 않은 것을 말했다고 하면 supported=false 다.
- 논문이 말했지만 **조건·범위를 떼어내 과장**했으면 그것도 supported=false 다.
- 주장이 사실이긴 하나 **이 논문의 핵심이 아니라 곁가지**면 is_central=false 다.

출력 형식 (JSON만, 다른 말 금지)
{"supported":true,"is_central":true,"verdict":"한국어 한두 문장 판정 근거","overreach":"과장·왜곡이 있으면 지적, 없으면 빈 문자열","confidence":0.0}

--- 조수가 뽑은 주장 ---
__CLAIM__

--- 논문: BIS WP __N__ · __TITLE__ ---
__BODY__
"""


def _settings() -> tuple[str, str, str]:
    env = load_env()

    def pick(name: str, default: str = "") -> str:
        # .env가 환경변수를 이긴다 — 옛 환경변수가 새 키를 가려 한참 헤맨 전례가 있다(2026-09-16)
        return env.get(name) or os.environ.get(name) or default

    key = pick("RUNYOUR_API_KEY")
    if not key:
        sys.exit("RUNYOUR_API_KEY가 없다 — .env 확인")
    return (pick("RUNYOUR_API_BASE", "https://api.runyour.ai/v1"), key,
            pick("ZETTEL_READ_MODEL") or DEFAULT_READ_MODEL)


def pdf_text(p: Path) -> str:
    import pypdf
    r = pypdf.PdfReader(str(p))
    return " ".join(re.sub(r"\s+", " ", (pg.extract_text() or "")) for pg in r.pages)


def _norm(s: str) -> str:
    """대조용 정규화.

    PDF 추출은 낱자 사이에 공백을 흘리고("c hanges", "high -frequency") 따옴표를 바꾼다.
    그 잡음까지 불일치로 세면 멀쩡한 인용이 전부 탈락한다 — 공백·인용부호만 지운다.
    """
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-")):
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]", "", s.lower())


def verify_quotes(quotes: list[str], full: str) -> list[dict]:
    """관문 A — 인용문이 원문에 실제로 있는가. 기계적이고 반박 불가능한 검사."""
    hay = _norm(full)
    out = []
    for q in quotes:
        n = _norm(q)
        if len(n) < 25:
            out.append({"quote": q, "found": False, "why": "너무 짧아 검증 불가"})
        else:
            out.append({"quote": q, "found": n in hay, "why": ""})
    return out


# 일시 장애로 보는 상태코드. 429는 속도 제한, 5xx는 업스트림 장애다 —
# 둘 다 **논문 탓이 아니라 그 순간의 사정**이라 조금 쉬었다 다시 부르면 대개 된다.
RETRY_CODES = (408, 429, 500, 502, 503, 504)
MAX_RETRY = 3


def call_model(base: str, key: str, model: str, prompt: str,
               timeout: int = 300) -> tuple[dict, dict]:
    """일시 장애는 재시도한다.

    2026-09-16 실측: 30편 배치에서 WP 1337이 **HTTP 503 한 번으로 통째로 날아갔다.**
    1,300편을 무인으로 돌리는데 한 번의 업스트림 딸꾹질로 논문을 잃으면,
    나중에 무엇이 왜 빠졌는지 추적할 수 없다. 여기서 흡수한다.
    """
    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "response_format": {"type": "json_object"},
    }).encode("utf-8")
    last: Exception | None = None
    for attempt in range(MAX_RETRY + 1):
        req = urllib.request.Request(
            f"{base}/chat/completions", data=body,
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                d = json.loads(r.read().decode("utf-8"))
            ch = (d.get("choices") or [{}])[0]
            txt = (ch.get("message") or {}).get("content")
            if not txt:
                # **빈 응답도 일시 장애로 본다.** 2026-09-17 WP 957 실측:
                # content가 None으로 와서 정규식이 TypeError로 터졌다 — 원인이 논문인지
                # 그 순간의 사정인지 로그만 보고는 알 수 없는 형태로 죽는다.
                # 여기서 사유(finish_reason)를 붙여 다시 부르고, 끝까지 비면 그렇게 적는다.
                why = ch.get("finish_reason") or "사유 없음"
                if attempt == MAX_RETRY:
                    raise RuntimeError(f"모델이 빈 응답 (finish_reason={why})")
                last = RuntimeError(f"빈 응답 {why}")
                time.sleep(2.0 * (attempt + 1))
                continue
            m = re.search(r"\{.*\}", txt, re.S)   # 모델이 앞뒤에 말을 붙이는 경우가 있다
            return json.loads(m.group(0) if m else txt), d.get("usage", {})
        except urllib.error.HTTPError as e:
            last = e
            if e.code not in RETRY_CODES or attempt == MAX_RETRY:
                raise
            time.sleep(2.0 * (attempt + 1))       # 2s → 4s → 6s
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError,
                ConnectionError, http.client.HTTPException) as e:
            # **RemoteDisconnected를 반드시 여기서 잡아야 한다.**
            # 2026-09-17 실측: 동시 3워커로 Gemini를 부르자 3건 모두
            # `RemoteDisconnected: Remote end closed connection without response`로
            # 토큰 0인 채 죽었다. 이건 URLError가 아니라 http.client.HTTPException 계열이라
            # 기존 except 절을 빠져나가 재시도 없이 그대로 실패했다.
            # 서버가 동시 연결을 끊는 것은 **그 순간의 사정**이지 논문 탓이 아니다.
            last = e
            if attempt == MAX_RETRY:
                raise
            time.sleep(2.0 * (attempt + 1))
    raise last  # type: ignore[misc]


# ≈ 100K 토큰. **판독 모델의 컨텍스트를 모를 때는 낮게 잡는다.**
# 처음엔 90만 자(≈225K 토큰)로 뒀다. GPT-5.4-mini의 400K 컨텍스트 기준이었는데,
# 판독을 Gemini로 옮기면서 **콘솔에 컨텍스트 표기가 없는 모델**을 쓰게 됐다.
# 그 상태로 돌리자 최신순 첫 논문(WP 1371, 전문 554만 자)에서 워커가 통째로 묶였다 —
# 거대한 PDF 파싱 + 감당 못 할 요청이 겹친 것이다.
# 전문 p99가 40만 자이므로 이 상한이면 **99%는 그대로 들어간다.**
MAX_BODY_CHARS = 400_000


def _body_of(full: str) -> str:
    """**자르지 않는 것이 기본이다.**

    처음엔 앞 6만 자 + 뒤 3만 자만 보냈다. 그게 치명적이었다 —
    **계수와 표는 논문 한가운데(결과 절)에 있다.** 숫자가 있는 부분을 통째로 잘라내고
    모델에게 숫자를 달라고 한 셈이라, 초안이 전부 "밀접하게 연동되며" 같은 맹물이 됐다.

    실측하면 자를 이유도 거의 없다 — 전문 중앙값 29.6K 토큰, p99가 101K 토큰이고
    판독 모델 컨텍스트는 400K다. **99.8%는 통째로 들어간다.**
    상한을 넘는 극소수(3편)만 앞뒤를 남기고 가운데를 접는다.
    """
    if len(full) <= MAX_BODY_CHARS:
        return full
    head = int(MAX_BODY_CHARS * 0.6)
    tail = MAX_BODY_CHARS - head
    return full[:head] + "\n...(분량 초과로 중략)...\n" + full[-tail:]


def _fill(tpl: str, **kw) -> str:
    for k, v in kw.items():
        tpl = tpl.replace(f"__{k}__", str(v))
    return tpl


def write_draft(vault: Path, n: int, title: str, res: dict, checks: list[dict],
                audit: dict, models: dict, usage: dict) -> Path:
    claim = (res.get("claim") or "(주장 없음)").strip()
    safe = re.sub(r'[\\/:*?"<>|]', "", claim)[:70]
    p = vault / DRAFTS / f"BIS_WP_{n} — {safe}.md"
    p.parent.mkdir(parents=True, exist_ok=True)

    ok = sum(1 for c in checks if c["found"])
    full_pass = bool(checks) and ok == len(checks)
    part_pass = ok >= QUOTES_MIN_PASS
    a_sup = bool(audit.get("supported"))
    a_cen = bool(audit.get("is_central"))

    if not part_pass:
        verdict, vtag = "❌ **관문 A 실패(인용 대부분 불일치) — 폐기 대상**", "quote-mismatch"
    elif not a_sup:
        verdict, vtag = "❌ **관문 B 실패(교차검증 반대) — 사람 확인 필요**", "cross-rejected"
    elif not a_cen:
        verdict, vtag = "⚠ **핵심 주장이 아니라는 판정 — 사람 확인 필요**", "not-central"
    elif full_pass:
        verdict, vtag = "✅ **관문 A·B 통과 — 승격 후보**", "machine-cross-verified"
    else:
        verdict, vtag = (f"✅ **통과(인용 부분일치 {ok}/{len(checks)}) — 승격 후보, "
                         f"불일치 인용은 쓰지 말 것**", "machine-cross-verified-partial")

    rows = []
    for c in checks:
        mark = "✅ 원문 확인" if c["found"] else (
            "❌ **원문에 없음**" + (f" — {c['why']}" if c["why"] else ""))
        rows.append(f"- {mark}\n  > {c['quote']}")
    lim = "\n".join(f"- {x}" for x in (res.get("limits") or [])) or \
        "_(논문에 명시된 한계 없음 — 그래서 더 조심해서 읽을 것)_"
    nums = "\n".join(f"- {x}" for x in (res.get("numbers") or [])) or \
        "_⚠ **수치를 뽑지 못했다** — 순수 이론모형이거나 판독이 얕았다. 원문 확인 전에는 쓰지 말 것_"
    contra = "\n".join(f"- {x}" for x in (res.get("contra") or [])) or \
        "_(기재 없음)_"
    over = audit.get("overreach") or ""

    p.write_text(f"""---
title: "{claim.replace('"', "'")}"
type: zettel_draft
status: draft
human_verified: false
source: "BIS Working Paper {n}"
source_note: "[[BIS_WP_{n}-catalog]]"
axis: {res.get('axis', '')}
read_model: {models.get('read', '')}
audit_model: {models.get('audit', '')}
read_confidence: {res.get('confidence', '')}
audit_confidence: {audit.get('confidence', '')}
quotes_total: {len(checks)}
quotes_verified: {ok}
cross_supported: {str(a_sup).lower()}
cross_is_central: {str(a_cen).lower()}
verification: {vtag}
created: {date.today().isoformat()}
tags: [type/zettel-draft, domain/{res.get('axis', 'unsorted')}, flag/needs-review]
---

# {claim}

> [!warning] 기계 판독 초안이다 — 사람이 읽지 않았다
> **{verdict}**
> 판독 `{models.get('read','')}` → 교차검증 `{models.get('audit','')}` (서로 다른 계열).
> 인용 {ok}/{len(checks)}건이 원문과 **문자열 대조**로 일치.

## 핵심 수치

{nums}

## 메커니즘 — 왜 그렇게 되는가

{res.get('mechanism') or '_(메커니즘 미기재 — 원문 확인 필요)_'}

## 시황에서 언제 부르는가

{res.get('so_what') or '_(용도 미기재)_'}

## 이 주장이 깨지는 조건

{contra}

## 요약

{res.get('summary', '—')}

## 관문 A — 근거 인용의 원문 대조

{chr(10).join(rows) if rows else '_(인용 없음)_'}

## 관문 B — 다른 모델의 독립 판정

- **주장이 논문에서 따라 나오는가**: {'예' if a_sup else '**아니오**'}
- **이 논문의 핵심 주장인가**: {'예' if a_cen else '**아니오 — 곁가지**'}
- 판정 근거: {audit.get('verdict', '—')}
{f"- ⚠ 과장·왜곡 지적: {over}" if over else ""}

## 저자가 밝힌 한계

{lim}

---
`BIS WP {n}` · {title}
판독 {date.today().isoformat()} · 토큰 입력 {usage.get('in', 0):,} / 출력 {usage.get('out', 0):,}
""", encoding="utf-8")
    return p


# 길이 관문만으로는 **깨진 텍스트 층을 못 거른다.**
# 2026-09-17 WP 957 실측: 글리프 번호가 `/0/1/2/2/3/4...` 형태로 46만 자 추출됐다.
# MIN_TEXT_CHARS를 가볍게 통과하고, 모델은 그 쓰레기를 받아 **빈 응답(content=None)**을 돌려줬다.
# 그 논문은 그렇게 두 번(RemoteDisconnected → TypeError) 호출만 태우고 죽었다.
# 세는 검사 둘이면 충분하다 — 영문자 비율과 흔한 단어의 존재. 판단이 들어가지 않는다.
# 같은 방식으로 전수 검사한 결과 아카이브에서 5편(WP 957·121·109·102·96)이 걸렸다.
ALPHA_MIN = 0.55
THE_MIN = 20


def unreadable(full: str) -> str:
    """읽을 수 있는 텍스트가 아니면 사유를, 멀쩡하면 빈 문자열을 돌려준다."""
    ns = re.sub(r"\s", "", full)
    if not ns:
        return "텍스트 0자"
    alpha = sum(ch.isalpha() for ch in ns) / len(ns)
    the = len(re.findall(r"\bthe\b", full[:200_000], re.I))
    if alpha < ALPHA_MIN or the < THE_MIN:
        return f"텍스트층 손상 — 글자비율 {alpha:.2f} · the {the}회 (OCR 필요)"
    return ""


def _one(f: Path, vault: Path, src: Path, base: str, key: str,
         read_model: str, audit_model: str) -> dict:
    """논문 한 편. **워커 하나가 통째로 처리한다** — 공유 상태가 없어야 병렬이 안전하다.

    각 워커는 자기 PDF를 읽고, 자기 API 호출을 하고, 자기 파일을 쓴다.
    파일명이 논문 번호로 갈리므로 워커끼리 같은 파일을 건드릴 일이 없다.
    """
    n = int(re.search(r"(\d+)", f.stem).group(1))
    out = {"n": n, "kind": "", "got": 0, "total": 0, "claim": "",
           "in": 0, "out": 0, "err": ""}
    title = ""
    cat = src / f"BIS_WP_{n}-catalog.md"
    if cat.exists():
        m = re.search(r'^title:\s*"(.*)"',
                      cat.read_text(encoding="utf-8", errors="replace"), re.M)
        if m:
            title = m.group(1)
    try:
        full = pdf_text(f)
        if len(full) < MIN_TEXT_CHARS:
            out["kind"] = "scanned"
            out["err"] = f"텍스트 {len(full)}자"
            return out
        why = unreadable(full)
        if why:
            out["kind"] = "scanned"
            out["err"] = why
            return out
        body = _body_of(full)

        res, u1 = call_model(base, key, read_model,
                             _fill(READ_PROMPT, N=n, TITLE=title, BODY=body))
        checks = verify_quotes(res.get("evidence") or [], full)
        got = sum(1 for c in checks if c["found"])

        if got >= QUOTES_MIN_PASS:
            abody = (full if len(full) <= AUDIT_HEAD + AUDIT_TAIL else
                     full[:AUDIT_HEAD] + "\n...(중략)...\n" + full[-AUDIT_TAIL:])
            audit, u2 = call_model(base, key, audit_model,
                                   _fill(AUDIT_PROMPT, CLAIM=res.get("claim", ""),
                                         N=n, TITLE=title, BODY=abody))
        else:
            audit, u2 = {"supported": None, "is_central": None,
                         "verdict": "관문 A 실패로 교차검증 생략"}, {}

        usage = {"in": u1.get("prompt_tokens", 0) + u2.get("prompt_tokens", 0),
                 "out": u1.get("completion_tokens", 0) + u2.get("completion_tokens", 0)}
        write_draft(vault, n, title, res, checks, audit,
                    {"read": read_model, "audit": audit_model}, usage)

        out.update(got=got, total=len(checks), claim=(res.get("claim") or "")[:40],
                   **{"in": usage["in"], "out": usage["out"]})
        if got < QUOTES_MIN_PASS:
            out["kind"] = "quote_fail"
        elif audit.get("supported") and audit.get("is_central"):
            out["kind"] = "pass"
        else:
            out["kind"] = "cross_fail"
    except urllib.error.HTTPError as e:
        out["kind"] = "error"
        out["err"] = f"HTTP {e.code} {e.read().decode('utf-8', 'replace')[:70]}"
    except Exception as e:
        out["kind"] = "error"
        out["err"] = f"{type(e).__name__} {str(e)[:60]}"
    return out


def run(limit: int = 0, sleep_s: float = 0.4, audit_model: str = "",
        workers: int = 1, log=print) -> int:
    base, key, read_model = _settings()
    audit_model = audit_model or DEFAULT_AUDIT_MODEL
    if audit_model.split("/")[0] == read_model.split("/")[0]:
        log(f"⚠ 판독({read_model})과 교차검증({audit_model})이 같은 계열이다 — "
            f"자기 확증이 된다. --audit-model로 다른 계열을 지정할 것")
    env = load_env()
    vault = Path(env.get("OBSIDIAN_VAULT_PATH") or ".")
    pdfdir, drafts = vault / PDFDIR, vault / DRAFTS
    drafts.mkdir(parents=True, exist_ok=True)

    done = {int(m.group(1)) for f in drafts.glob("BIS_WP_*.md")
            if (m := re.match(r"BIS_WP_(\d+) ", f.name))}
    # 최신부터 판독한다. 초기 번호대는 스캔본이라 어차피 건너뛰고,
    # 최신 연구가 시황에 바로 쓰인다 — 먼저 처리된 것이 먼저 쓸모가 있다.
    # 최신부터 판독하되, **거대 PDF는 맨 뒤로 민다.**
    # 2026-09-17: 최신순 첫 논문이 하필 5.5MB짜리라 워커 하나가 통째로 묶였고,
    # 4워커 중 하나가 죽은 채 2분간 산출이 0이었다. 큰 파일은 파싱만으로도 분 단위를 먹는다.
    # 작은 것부터 흘려보내면 **전체 처리량이 훨씬 안정된다** — 큰 것은 마지막에 몰아서 처리한다.
    BIG = 8 * 1024 * 1024
    pdfs = sorted(pdfdir.glob("BIS_WP_*.pdf"),
                  key=lambda f: (f.stat().st_size >= BIG,
                                 -int(re.search(r"(\d+)", f.stem).group(1))))
    todo = [f for f in pdfs
            if int(re.search(r"(\d+)", f.stem).group(1)) not in done]
    if limit:
        todo = todo[:limit]
    log(f"PDF {len(pdfs):,}건 · 판독 완료 {len(done):,}건 → 이번에 {len(todo):,}건")
    log(f"  판독 {read_model} · 교차검증 {audit_model}")

    src = vault / SUB
    stat = {"pass": 0, "quote_fail": 0, "cross_fail": 0, "error": 0, "scanned": 0}
    tin = tout = 0
    MARK = {"pass": "통과", "quote_fail": "A✘", "cross_fail": "B✘",
            "scanned": "⏭", "error": "✘"}

    def _record(i: int, r: dict) -> None:
        nonlocal tin, tout
        stat[r["kind"]] = stat.get(r["kind"], 0) + 1
        tin += r["in"]
        tout += r["out"]
        mark = MARK.get(r["kind"], "?")
        if r["kind"] == "pass" and r["got"] != r["total"]:
            mark = "부분"
        if r["kind"] == "scanned":
            log(f"  [{i:>4}/{len(todo)}] WP {r['n']:<5} ⏭ 스캔본 — {r['err']}, "
                f"OCR 없이는 판독 불가 (호출 생략)")
        elif r["kind"] == "error":
            log(f"  [{i:>4}/{len(todo)}] WP {r['n']:<5} ✘ {r['err']}")
        else:
            log(f"  [{i:>4}/{len(todo)}] WP {r['n']:<5} {mark} "
                f"인용{r['got']}/{r['total']}  {r['claim']}")

    if workers <= 1:
        for i, f in enumerate(todo, 1):
            _record(i, _one(f, vault, src, base, key, read_model, audit_model))
            time.sleep(sleep_s)
    else:
        # **워커는 완전히 독립이다** — 각자 자기 PDF를 읽고 자기 파일을 쓴다.
        # 공유되는 건 집계 카운터뿐이고 그건 메인 스레드에서만 만진다(as_completed).
        # 워커를 너무 올리면 429가 나고 메모리도 워커 수만큼 든다 — 3~4가 적당하다.
        from concurrent.futures import ThreadPoolExecutor, as_completed
        log(f"  동시 {workers}워커로 돌린다")
        with ThreadPoolExecutor(max_workers=workers) as ex:
            futs = {ex.submit(_one, f, vault, src, base, key,
                              read_model, audit_model): f for f in todo}
            for i, fut in enumerate(as_completed(futs), 1):
                try:
                    _record(i, fut.result())
                except Exception as e:                       # 워커가 통째로 죽은 경우
                    stat["error"] += 1
                    log(f"  [{i:>4}/{len(todo)}] 워커 오류 {type(e).__name__} {str(e)[:60]}")

    log(f"\n완료 — 승격후보 {stat['pass']:,} · 인용불일치 {stat['quote_fail']:,} · "
        f"교차검증탈락 {stat['cross_fail']:,} · 스캔본건너뜀 {stat['scanned']:,} · "
        f"오류 {stat['error']:,}")
    log(f"토큰 입력 {tin:,} / 출력 {tout:,}")
    log(f"  → {drafts}")
    _mirror(drafts, env, log)
    return 0


def _mirror(drafts: Path, env: dict, log=print) -> None:
    """초안을 볼트 **밖에** 한 벌 더 둔다.

    2026-09-17에 `_drafts` 925건 중 730건이 원인 미상으로 사라졌다. 볼트 `.trash`에도
    윈도우 휴지통에도 없었고 그 시각 볼트에 쓰기도 프로세스도 없었다. 원인은 끝내 못 찾았다.
    **원인을 모르는 손실은 막을 수 없으니 복제본으로 값을 줄인다** — 판독 한 편이 실제 돈이라
    다시 읽는 비용이 복사 비용보다 몇 자릿수 비싸다. 볼트가 아닌 곳에 둬야 의미가 있다.
    """
    import shutil
    out = env.get("DATABOOK_OUTPUT_DIR")
    if not out:
        return
    # 원본 폴더 이름을 그대로 달고 간다 — `_drafts`와 `_drafts_selfread`는 같은 논문에
    # 같은 파일명을 쓸 수 있어서, 한 곳에 섞으면 교차검증본이 미검증본에 덮인다.
    dst = Path(out) / "zettel-drafts-mirror" / drafts.name
    try:
        dst.mkdir(parents=True, exist_ok=True)
        n = 0
        for f in drafts.glob("*.md"):
            tgt = dst / f.name
            if not tgt.exists() or tgt.stat().st_mtime < f.stat().st_mtime:
                shutil.copy2(f, tgt)
            n += 1
        log(f"  사본 {n:,}건 → {dst}")
    except Exception as e:                                   # 사본 실패가 배치를 죽이면 안 된다
        log(f"  ⚠ 사본 실패 {type(e).__name__} {str(e)[:60]} — 판독 결과는 볼트에 있다")
