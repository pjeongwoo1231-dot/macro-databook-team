# 읽을거리 무인 판독 — databook daily(18:30) 뒤에 실행된다.
#
#   테스트:  powershell -ExecutionPolicy Bypass -File "<이 파일>" -Force
#   특정일:  ... -Date 2026-08-29
#
# 무인 실행이라 '조용한 실패'와 '무한 대기'가 가장 위험하다. 그래서
#   ① 타임아웃을 걸고 ② 결과를 status.tsv 에 한 줄씩 남긴다.
[CmdletBinding()]
param(
    [string]$Date = (Get-Date).ToString('yyyy-MM-dd'),
    [switch]$Force,                  # 판독본이 있어도 덮어쓴다 (기존본은 .bak-<시각> 보존)
    [int]$TimeoutMin = 45            # 이 시간을 넘기면 죽인다
                                     # 2026-08-30 25→45: 상한 없이 통과분을 전부 읽게 바꿔서
                                     # 본문 fetch가 8건에서 20~30건으로 늘었다
)

$ErrorActionPreference = 'Stop'
# 코드는 이 저장소(=$PSScriptRoot), 로그·상태는 볼트.
# 런타임 산출물을 git에 넣지 않으려고 나눠 둔 것이다 — 둘을 다시 합치지 말 것.
$Here   = $PSScriptRoot
$Vault  = if ($env:OBSIDIAN_VAULT_PATH) { $env:OBSIDIAN_VAULT_PATH }
          else { 'C:\Users\test\Documents\MacroVault' }
$RunDir = Join-Path $Vault '_System\readingpilot'
$LogDir = Join-Path $RunDir 'logs'
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$Log    = Join-Path $LogDir "$Date.log"
$Status = Join-Path $RunDir 'status.tsv'

function W($m) { "$((Get-Date).ToString('HH:mm:ss')) $m" | Tee-Object -FilePath $Log -Append }
function S($state, $note) {
    if (-not (Test-Path $Status)) { "date`tstate`tnote" | Set-Content $Status -Encoding UTF8 }
    "$Date`t$state`t$note" | Add-Content $Status -Encoding UTF8
}

$Src = Join-Path $Vault "15-reading\$Date.md"
$Out = Join-Path $Vault "15-reading\판독\$Date-판독.md"

if (-not (Test-Path $Src)) { W "SKIP 읽을거리 없음"; S 'SKIP' 'no-source'; exit 0 }

if (Test-Path $Out) {
    if (-not $Force) { W "SKIP 판독본 이미 있음 (덮어쓰려면 -Force)"; S 'SKIP' 'exists'; exit 0 }
    $Bak = "$Out.bak-$((Get-Date).ToString('HHmmss'))"
    Move-Item $Out $Bak
    W "기존 판독본 보존 -> $(Split-Path $Bak -Leaf)"
}

# 프롬프트를 임시파일로 — stdin 리다이렉트에 파일이 필요하다
$Tmp = Join-Path $env:TEMP "triage-$Date-$PID.txt"
((Get-Content (Join-Path $Here 'TRIAGE_PROMPT.md') -Raw) -replace '\{DATE\}', $Date) |
    Set-Content $Tmp -Encoding UTF8

$OutFile = Join-Path $LogDir "$Date.stdout"
$ErrFile = Join-Path $LogDir "$Date.stderr"
W "START 판독 $Date (타임아웃 ${TimeoutMin}분)"

# 플래그 근거 — code.claude.com/docs/en/headless · /cli-reference (2026-08-30 확인)
#
# --permission-mode acceptEdits
#     -p 의 기본 모드는 **Manual**이라 반드시 명시해야 한다. acceptEdits 는 파일 쓰기를 통과시키지만
#     "네트워크 요청은 여전히 --allowedTools 항목이 필요하다"고 문서에 못박혀 있다 → WebFetch 를 넣은 이유.
# --strict-mcp-config (--mcp-config 없이)
#     ⚠ 이게 없으면 -p 세션이 이 사용자 환경의 MCP 서버를 **전부 연결한다**(Canva·Gmail·Notion·
#     Lucid·Higgsfield·크롬 등). 판독에 하나도 안 쓰는데 서버당 MCP_TIMEOUT 30초까지 잡아먹고
#     매달릴 수 있다. 이 플래그로 --mcp-config 에 준 것만 쓰게 하고, 아무것도 안 주면 0개가 된다.
# --disallowedTools mcp__*
#     위와 겹치는 안전장치. MCP 툴을 컨텍스트에서 아예 제거한다.
# --output-format json
#     결과에 total_cost_usd 가 들어온다 → 매일 비용을 status.tsv 에 남긴다.
#
# --bare 는 쓰지 않는다: 시작은 빨라지지만 CLAUDE.md·자동메모리·볼트 규칙을 안 읽고,
# OAuth 대신 ANTHROPIC_API_KEY 를 요구해 구독이 아닌 별도 과금이 된다.
$sw = [Diagnostics.Stopwatch]::StartNew()
$p = Start-Process -FilePath 'claude' `
        -ArgumentList '-p','--permission-mode','acceptEdits',
                      '--allowedTools','Read,Write,Edit,Glob,Grep,WebFetch',
                      '--disallowedTools','mcp__*',
                      '--strict-mcp-config',
                      '--output-format','json' `
        -WorkingDirectory $Vault `
        -RedirectStandardInput $Tmp `
        -RedirectStandardOutput $OutFile `
        -RedirectStandardError  $ErrFile `
        -NoNewWindow -PassThru

if (-not $p.WaitForExit($TimeoutMin * 60 * 1000)) {
    try { $p.Kill($true) } catch {}
    W "TIMEOUT ${TimeoutMin}분 초과 — 프로세스 종료함"
    S 'TIMEOUT' "${TimeoutMin}min"
    Remove-Item $Tmp -ErrorAction SilentlyContinue
    exit 1
}
$sw.Stop(); $rc = $p.ExitCode
Remove-Item $Tmp -ErrorAction SilentlyContinue
Get-Content $ErrFile -ErrorAction SilentlyContinue | Select-Object -Last 20 | Add-Content $Log

$mins = [math]::Round($sw.Elapsed.TotalMinutes,1)

# --output-format json 의 결과에서 비용을 뽑는다. 실패해도 판정에는 영향 없다.
$cost = '?'
try {
    $j = Get-Content $OutFile -Raw -ErrorAction Stop | ConvertFrom-Json
    if ($null -ne $j.total_cost_usd) { $cost = '$' + [math]::Round($j.total_cost_usd, 3) }
} catch { }

if (Test-Path $Out) {
    $kb = [math]::Round((Get-Item $Out).Length/1KB,1)
    W "OK 판독본 생성 ${kb}KB / ${mins}분 / $cost / exit=$rc"
    S 'OK' "${kb}KB ${mins}min $cost"
} else {
    # exit 143 = SIGTERM (Task Scheduler 한도 초과 등). 문서상 그 턴은 미완으로 남는다.
    $why = if ($rc -eq 143) { 'SIGTERM(외부 종료)' } else { "exit=$rc" }
    W "FAIL 판독본 미생성 ($why, ${mins}분, $cost) — $ErrFile 확인"
    S 'FAIL' "$why ${mins}min $cost"
    exit 1
}
