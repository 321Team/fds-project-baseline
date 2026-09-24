# Read-only: fetch issue body edit history (userContentEdits) for the damaged issues.
# Windows PowerShell 5.1 compatible. ASCII only. Requires: gh (logged in). NO WRITES to GitHub.
#
# Usage (run inside this folder):
#   powershell -ExecutionPolicy Bypass -File .\fetch-edit-history.ps1
#
# Output (in .\edits\):
#   edits-<n>.json    raw GraphQL pages from gh (--paginate), bytes kept via cmd redirect
#   issue-<n>.json    current issue from REST (body, updated_at, title, state, labels)
#   SHA256SUMS.txt    SHA-256 of every output file
# Zip the edits folder and hand it to the session for analysis (analyze-edits.py).

$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$out = Join-Path $here 'edits'
if (-not (Test-Path $out)) { New-Item -ItemType Directory -Path $out | Out-Null }
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { Write-Host 'STOP gh not found'; exit 1 }

$owner = '321Team'
$repo = 'fds-project-baseline'
$numbers = @(9, 74, 75)
$q = 'query($o:String!,$r:String!,$n:Int!,$endCursor:String){repository(owner:$o,name:$r){issue(number:$n){number lastEditedAt updatedAt userContentEdits(first:50,after:$endCursor){totalCount pageInfo{hasNextPage endCursor} nodes{id createdAt editedAt deletedAt editor{login} diff}}}}}'

foreach ($n in $numbers) {
    $f = Join-Path $out "edits-$n.json"
    # cmd redirect writes gh stdout bytes as-is (PowerShell '>' would re-encode).
    cmd /c "gh api graphql --paginate -f query=""$q"" -F o=$owner -F r=$repo -F n=$n > ""$f"""
    if ($LASTEXITCODE -ne 0) { Write-Host "STOP #$n graphql read failed"; exit 1 }
    $g = Join-Path $out "issue-$n.json"
    cmd /c "gh api repos/$owner/$repo/issues/$n > ""$g"""
    if ($LASTEXITCODE -ne 0) { Write-Host "STOP #$n issue read failed"; exit 1 }
    Write-Host "READ #$n $((Get-Item $f).Length) bytes"
}

$sums = Join-Path $out 'SHA256SUMS.txt'
Get-ChildItem $out -File | Where-Object { $_.Name -ne 'SHA256SUMS.txt' } | Sort-Object Name | ForEach-Object {
    "$((Get-FileHash $_.FullName -Algorithm SHA256).Hash.ToLower())  $($_.Name)"
} | Set-Content -Path $sums -Encoding ASCII
Write-Host "DONE read-only. Zip the 'edits' folder and share it with the session."
