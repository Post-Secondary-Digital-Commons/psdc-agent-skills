[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$registry = Join-Path $root 'config/skill-registry.yaml'
$schema = Join-Path $root 'schemas/assessment-result.schema.json'
$consumerSchema = Join-Path $root 'schemas/consumer-manifest.schema.json'
$consumerValidator = Join-Path $root 'scripts/Validate-Consumer.py'
$manifest = Join-Path $root 'config/upstream-files.sha256'
$obsidianManifest = Join-Path $root 'config/obsidian-files.sha256'

if (-not (Test-Path -LiteralPath $registry)) { throw "Missing registry: $registry" }
if (-not (Test-Path -LiteralPath $schema)) { throw "Missing schema: $schema" }
if (-not (Test-Path -LiteralPath $consumerSchema)) { throw "Missing consumer schema: $consumerSchema" }
if (-not (Test-Path -LiteralPath $consumerValidator)) { throw "Missing consumer validator: $consumerValidator" }
if (-not (Test-Path -LiteralPath $manifest)) { throw "Missing upstream manifest: $manifest" }
if (-not (Test-Path -LiteralPath $obsidianManifest)) { throw "Missing Obsidian pilot manifest: $obsidianManifest" }

$json = Get-Content -LiteralPath $schema -Raw | ConvertFrom-Json
$consumerJson = Get-Content -LiteralPath $consumerSchema -Raw | ConvertFrom-Json
if ($json.'$schema' -ne 'https://json-schema.org/draft/2020-12/schema') {
    throw 'Assessment schema must use JSON Schema 2020-12.'
}
if ($consumerJson.'$schema' -ne 'https://json-schema.org/draft/2020-12/schema') {
    throw 'Consumer schema must use JSON Schema 2020-12.'
}

$registryText = Get-Content -LiteralPath $registry -Raw
$requiredSkills = @(
    'setup-matt-pocock-skills', 'grill-with-docs', 'domain-modeling', 'to-spec',
    'to-tickets', 'wayfinder', 'research', 'writing-for-agents',
    'psdc-project-assessment', 'psdc-evidence-audit', 'psdc-upstream-adoption',
    'psdc-engineering-quality',
    'psdc-workspace-health', 'psdc-obsidian-format'
)
foreach ($skill in $requiredSkills) {
    if ($registryText -notmatch [regex]::Escape("id: $skill")) {
        throw "Registry is missing skill: $skill"
    }
}

Get-ChildItem -LiteralPath (Join-Path $root 'skills') -Directory | ForEach-Object {
    $skillFile = Join-Path $_.FullName 'SKILL.md'
    if (-not (Test-Path -LiteralPath $skillFile)) { throw "Missing SKILL.md: $($_.FullName)" }
}

foreach ($line in Get-Content -LiteralPath $manifest, $obsidianManifest) {
    if ([string]::IsNullOrWhiteSpace($line) -or $line.StartsWith('#')) { continue }
    $parts = $line -split '\s+', 2
    $path = Join-Path $root $parts[1]
    if (-not (Test-Path -LiteralPath $path)) { throw "Missing vendored file: $($parts[1])" }
    $actual = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actual -ne $parts[0]) { throw "Vendored file differs from manifest: $($parts[1])" }
}
$obsidianListed = @(Get-Content -LiteralPath $obsidianManifest |
    Where-Object { -not [string]::IsNullOrWhiteSpace($_) -and -not $_.StartsWith('#') } |
    ForEach-Object { ($_ -split '\s+', 2)[1] } | Sort-Object)
$obsidianActual = @(Get-ChildItem -LiteralPath (Join-Path $root 'vendor/obsidian') -Recurse -File |
    ForEach-Object { $_.FullName.Substring($root.Length + 1).Replace('\', '/') } | Sort-Object)
if (Compare-Object $obsidianListed $obsidianActual) {
    throw 'Obsidian pilot contains files not accounted for in its hash manifest.'
}

python (Join-Path $root 'scripts/Validate-SkillRegistry.py')
if ($LASTEXITCODE -ne 0) { throw 'Skill registry validation failed.' }
python (Join-Path $root 'scripts/Validate-Adoption.py') --self-test
if ($LASTEXITCODE -ne 0) { throw 'Upstream adoption record self-test failed.' }
python (Join-Path $root 'scripts/Build-ApplicationScope.py') --check
if ($LASTEXITCODE -ne 0) { throw 'Skill application scope check failed.' }
python (Join-Path $root 'skills/psdc-obsidian-format/scripts/validate_canvas.py') --self-test
if ($LASTEXITCODE -ne 0) { throw 'Canvas format fixtures failed.' }

Write-Host "Agent skill structural checks passed ($($requiredSkills.Count) registered skills)."
