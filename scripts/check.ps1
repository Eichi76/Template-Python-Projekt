Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

Write-Host "Running check script (PowerShell)..."

poetry env check
poetry run pytest -q
pre-commit run --all-files

if (Test-Path -Path "./package.json") {
    Write-Host "Found package.json — running npm run lint:md"
    npm run lint:md
} else {
    Write-Host "No package.json found — skipping npm lint"
}
