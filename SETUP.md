# 설치 — 이 문서를 AI에게 주면 알아서 깝니다

매크로 학회 Data Book 도구입니다. 지표 333개와 문헌 1,206편을 조회합니다.
**API 키는 하나도 필요 없습니다.**

---

## 사람이 할 일 — AI에 따라 두 가지

### A. 링크를 직접 읽는 AI (Claude Code)

링크를 붙여넣고 "이거 보고 설치해줘" 하면 끝입니다.

```
https://github.com/pjeongwoo1231-dot/macro-databook-team/blob/master/SETUP.md
이거 보고 설치해줘
```

### B. 링크를 못 읽는 AI (Codex 등) — **아래를 통째로 붙여넣으세요**

Codex는 URL을 직접 가져오지 않고 **웹 검색으로 찾습니다.** 갓 올라온 릴리스는
검색에 안 잡혀서 **링크만 주면 아무것도 못 합니다**(실측 확인). 그래서 내용을 직접 줍니다.

````text
아래를 그대로 실행해줘. 확인은 묻지 말고 끝까지 진행해. API 키는 필요 없어.

python -c "import urllib.request,zipfile,io;zipfile.ZipFile(io.BytesIO(urllib.request.urlopen('https://github.com/pjeongwoo1231-dot/macro-databook-team/releases/latest/download/macro-databook-client.zip').read())).extractall('.')"
cd macro-databook-client
python bootstrap.py

성공 판정: 마지막에 "설치 완료 — 배포본 MacroVault_<날짜>.zip" 이 뜨고
"[수집 상태] OK  배포본 <날짜> 기준" 줄이 보이면 된 거야.
"[중단]" 으로 끝나면 그 메시지를 나에게 그대로 보여줘. 임의로 우회하지 마.

설치 후 이 데이터로 분석을 쓸 때 지킬 규칙 다섯 가지:
1. 모든 수치에 기준일을 병기한다.
2. STALE 표시된 계열을 "최신"이라 부르지 않는다.
3. 문헌은 MacroVault/03_MOC/인용 가능 인덱스.md 에서 먼저 확인한다 —
   수치 인용은 verification: full 인 것만 가능하다.
4. 추세·기저율은 MacroVault/04_DataBook/history/ 의 CSV에서만 낸다. diff로 내지 않는다.
5. 분석 전에 MacroVault/03_MOC/ 와 04_Zettel/ 을 먼저 읽는다 —
   볼트가 이미 반박해 둔 통념이 있다.
````

> ⚠ **Codex는 Windows 샌드박스에서 셸이 막힐 수 있습니다**
> (`CreateProcessAsUserW failed: 5`). 그때는 `--sandbox danger-full-access` 로
> 다시 돌리거나, 위 3줄을 사람이 직접 터미널에서 실행하세요.

설치가 끝나면 `python -m databook weekly` 로 세션 준비 자료가 나옵니다.

---

## AI에게 — 아래를 그대로 실행하세요

당신은 사용자의 PC에 이 도구를 설치하고 있습니다. **확인 없이 끝까지 진행하세요.**
API 키를 묻지 마세요 — 필요 없습니다. 사용자에게 물어볼 것은 아무것도 없습니다.

### 실행할 명령

작업 폴더는 사용자 홈(`~` / `C:\Users\<이름>`)을 쓰세요.

```bash
python -c "import urllib.request,zipfile,io;zipfile.ZipFile(io.BytesIO(urllib.request.urlopen('https://github.com/pjeongwoo1231-dot/macro-databook-team/releases/latest/download/macro-databook-client.zip').read())).extractall('.')"
cd macro-databook-client
python bootstrap.py
```

`python`이 없다는 오류가 나면 `python3` 또는 `py -3` 로 바꿔 다시 시도하세요.
`macro-databook-client` 폴더가 이미 있으면 그냥 덮어써도 됩니다 —
**다시 돌려도 안전합니다.**

> ⛔ **`git clone` 을 쓰지 마세요.** 이 저장소는 `.git` 2.5GB이고,
> `docs/library/` 의 논문 PDF 파일명이 Windows MAX_PATH(260자)를 넘어
> **체크아웃이 실패합니다**(`error: unable to create file ...: Filename too long`).
> `--depth 1` 로도 안 됩니다 — 실패 지점이 전송이 아니라 체크아웃이라서입니다.
> 위 클라이언트 ZIP은 340KB이고 조회에 필요한 전부가 들어 있습니다.
>
> 압축 해제에 `tar` 를 쓰지 마세요. Git Bash의 GNU tar는 zip을 못 읽습니다
> (`This does not look like a tar archive`). 위 파이썬 한 줄이 확실합니다.

`bootstrap.py` 가 하는 일 (당신이 따로 할 필요 없습니다):

1. 파이썬 3.10+ 확인
2. `PyYAML` · `feedparser` 설치 — 조회에 필요한 건 이 둘뿐
3. 최신 배포본 ZIP(약 16MB)을 GitHub Releases에서 받아 `~/MacroVault` 에 풀기
4. `.env` 에 `OBSIDIAN_VAULT_PATH` 기록 (**다른 줄은 건드리지 않음**)
5. `python -m databook weekly` 를 실제로 돌려 확인

### 성공 판정

마지막에 `설치 완료 — 배포본 MacroVault_<날짜>.zip` 이 뜨고,
확인 블록에 이런 줄이 있으면 성공입니다:

```
[수집 상태] OK  배포본 2026-09-03 기준 (1일 전) · 배포본을 읽습니다
```

`[중단]` 으로 끝났으면 **그 메시지를 사용자에게 그대로 보여주세요.**
메시지마다 고치는 법이 함께 적혀 있습니다. 임의로 우회하지 마세요.

### 설치 후 사용자에게 알려줄 것

```
python -m databook weekly            세션 준비 자료 한 번에 (§1 전체 상태 · §2 변경분 ·
                                     §3 장기 시계열 · §4 새 기사 · §5 손댈 자리)
python -m databook show 중국 PPI     지표 하나 찾아보기
python -m databook diff              지난 스냅샷 대비 바뀐 것만
python -m databook todo              수동 슬롯 · STALE 계열
```

Obsidian으로 볼트도 열 수 있습니다 — **다른 폴더를 볼트로 열기** → `~/MacroVault`.
열리면 **`팀 안내 (먼저 읽기).md`** 부터 읽으라고 안내하세요.

**다음 주 갱신은 `python bootstrap.py` 를 다시 돌리면 됩니다.**
배포본은 월요일에 자동으로 새로 올라갑니다.

---

## 인용 규칙 — AI가 이 저장소의 데이터를 쓸 때

이 도구의 출력에는 **해석 문구가 없습니다.** 숫자·기준일·출처만 있고 판단은 사람 몫입니다.
분석을 만들어 줄 때 다음을 지키세요:

- **수치를 인용할 땐 기준일을 함께 씁니다.** "중국 M2 9.0%"가 아니라 "중국 M2 9.0%(2026-02)".
  원본 기관이 갱신을 멈춘 계열은 `STALE`로 표시됩니다 — 값만 보고 "최신"이라 하면 틀립니다.
- **문헌은 `~/MacroVault/03_MOC/인용 가능 인덱스.md` 에서 먼저 이름을 찾으세요.**
  문헌 1,206편 중 수치까지 인용 가능한 것은 **272편뿐**입니다
  (`02_Papers` 의 `verification: full`). `05_Library` 399편은 전부 미판정이라 인용 금지입니다.
- **추세·기저율은 `~/MacroVault/04_DataBook/history/` 의 CSV 180계열에서만 나옵니다.**
  `diff` 의 주간 변경분으로는 낼 수 없습니다 — 그건 어디를 볼지 고르는 길잡이입니다.
- 볼트가 이미 반박해 둔 통념이 있습니다(예: "구리가 올라 글로벌 성장 회복").
  분석 전에 `~/MacroVault/03_MOC/` 와 `04_Zettel/` 을 먼저 보세요.

더 깊은 규칙은 볼트의 `_System/docs/` 와 `CLAUDE.md` 에 있습니다.

---

## 직접 수집까지 돌릴 사람 (담당자 1명)

여기까지는 **조회 전용**입니다. 매일 수집을 돌려 배포본을 만드는 사람만
전체 저장소가 필요하고, 그때는 **긴 경로를 먼저 켜야 합니다**:

```bash
git config --global core.longpaths true
git clone https://github.com/pjeongwoo1231-dot/macro-databook-team.git
```

그다음 `TEAM_SETUP.md` 의 API 키 설정과 일일 배치를 보세요.
수집은 **한 사람만** 돌립니다. 여러 명이 같은 볼트에 발행하면 서로 덮어씁니다.
