# Evidence Path update for 321Team/fds-project-baseline #9 (2026-09-25, after body repair; same logic as 2026-09-23 batch).
# Windows PowerShell 5.1 compatible. ASCII only. Requires: gh (logged in).
#
# Usage (run inside this folder):
#   .\apply-evidence-path.ps1            # dry run: file hash + drift check only, no writes
#   .\apply-evidence-path.ps1 -Apply     # write issue bodies, one by one
#
# Per issue:
#   1. body file SHA-256 must equal plan.json file_sha256   (else STOP)
#   2. issue updated_at must equal plan.json updated_at      (else STOP: edited after plan)
#   3. PATCH body from file (gh reads file bytes directly)
#   4. record number in applied.txt; reruns skip recorded numbers
# Any error stops the run. Issues already written stay written; nothing is rolled back.

param([switch]$Apply)
$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$plan = Get-Content -Raw -Encoding UTF8 (Join-Path $here 'plan.json') | ConvertFrom-Json
$repo = $plan.repo
$log = Join-Path $here 'applied.txt'
$done = @()
if (Test-Path $log) { $done = Get-Content $log | ForEach-Object { $_.Split(' ')[0] } }

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { Write-Host 'STOP gh not found'; exit 1 }

$count = 0
foreach ($it in $plan.issues) {
    $n = [string]$it.number
    if ($done -contains $n) { Write-Host "SKIP #$n already applied"; continue }

    $f = Join-Path $here $it.file
    if (-not (Test-Path $f)) { Write-Host "STOP #$n body file missing: $f"; exit 1 }
    $h = (Get-FileHash $f -Algorithm SHA256).Hash.ToLower()
    if ($h -ne $it.file_sha256) { Write-Host "STOP #$n body file hash mismatch ($h)"; exit 1 }

    $u = gh api "repos/$repo/issues/$n" --jq '.updated_at'
    if ($LASTEXITCODE -ne 0) { Write-Host "STOP #$n read failed"; exit 1 }
    if ($u.Trim() -ne $it.updated_at) {
        Write-Host "STOP #$n edited after plan: now $u, plan $($it.updated_at). Ask for a new plan."
        exit 1
    }

    if (-not $Apply) { Write-Host "READY #$n $($it.record_ids -join ',')"; $count++; continue }

    $r = gh api -X PATCH "repos/$repo/issues/$n" -F "body=@$f" --jq '.updated_at'
    if ($LASTEXITCODE -ne 0) { Write-Host "STOP #$n PATCH failed"; exit 1 }
    Add-Content -Path $log -Value "$n $($r.Trim())" -Encoding ASCII
    Write-Host "OK #$n $($r.Trim())"
    $count++
    Start-Sleep -Seconds 1
}

if ($Apply) { Write-Host "DONE applied=$count" } else { Write-Host "DRY RUN ready=$count (no writes). Run with -Apply to write." }
