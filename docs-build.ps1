param(
    [string]$SourceDir = "source",
    [string]$BuildDir = "/build",
    [string]$Builder = "html"
)

if (-not (Get-Command sphinx-build -ErrorAction SilentlyContinue)) {
    Write-Host "sphinx-build not found. Install requirements with: pip install -r requirements.txt" -ForegroundColor Yellow
    exit 1
}

sphinx-build -b $Builder $SourceDir $BuildDir
Write-Host "Build complete: $BuildDir" -ForegroundColor Green
