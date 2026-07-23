$ErrorActionPreference = 'Stop'

$projectRoot = Split-Path -Parent $PSScriptRoot
$dataDir = Join-Path $projectRoot 'data'
$datasetSlug = 'mashlyn/online-retail-ii-uci'

if (-not (Get-Command kaggle -ErrorAction SilentlyContinue)) {
    throw "Kaggle CLI is not installed. Install it with 'pip install kaggle' and configure your API token before running this script."
}

New-Item -ItemType Directory -Path $dataDir -Force | Out-Null

$zipPath = Join-Path $dataDir 'online-retail-ii-uci.zip'

Write-Host "Downloading dataset $datasetSlug into $dataDir ..."
kaggle datasets download -d $datasetSlug -p $dataDir -o

if (-not (Test-Path $zipPath)) {
    throw "Dataset download did not produce $(Split-Path $zipPath -Leaf) in $dataDir."
}

Write-Host "Extracting dataset ..."
Expand-Archive -Path $zipPath -DestinationPath $dataDir -Force

Write-Host 'Files available in data/:'
Get-ChildItem -Path $dataDir -File | Select-Object -ExpandProperty Name

if (-not (Test-Path (Join-Path $dataDir 'online_retail_II.csv'))) {
    Write-Warning "online_retail_II.csv was not found after extraction. Check the extracted filenames and adjust notebook paths if needed."
}