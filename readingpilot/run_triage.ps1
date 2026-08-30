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

$sw = [Diagnostics.Stopwatch]::StartNew()
$p = Start-Process -FilePath 'claude' `
        -ArgumentList '-p','--permission-mode','acceptEdits',
                      '--allowedTools','Read,Write,Edit,Glob,Grep,WebFetch' `
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
if (Test-Path $Out) {
    $kb = [math]::Round((Get-Item $Out).Length/1KB,1)
    W "OK 판독본 생성 ${kb}KB / ${mins}분 / exit=$rc"
    S 'OK' "${kb}KB ${mins}min"
} else {
    W "FAIL 판독본 미생성 (exit=$rc, ${mins}분) — $ErrFile 확인"
    S 'FAIL' "exit=$rc ${mins}min"
    exit 1
}
