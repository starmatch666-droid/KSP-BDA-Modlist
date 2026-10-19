param(
    [Parameter(Mandatory = $true)][string]$InputPath,
    [Parameter(Mandatory = $true)][string]$OutputPath
)

$lines = Get-Content -LiteralPath $InputPath -Encoding UTF8
$out = [System.Collections.Generic.List[string]]::new()
$out.Add("// Fox Defense Contracts / Kerbal Powers Armory 弹药类型中文")
$out.Add("// 由 tools/generate_bullet_zh.ps1 根据 tools/zh/bullets.tsv 生成。")
$out.Add("")

$count = 0
foreach ($line in $lines) {
    if ([string]::IsNullOrWhiteSpace($line) -or $line.StartsWith("#")) { continue }
    $cols = $line -split "`t"
    if ($cols.Count -lt 2) { throw "Invalid row: $line" }

    $english = $cols[0].Trim()
    $chinese = $cols[1].Trim()
    $pattern = $english -replace '\s', '?'

    $out.Add("@BULLET:HAS[#DisplayName[$pattern]]:FINAL")
    $out.Add("{")
    $out.Add("    @DisplayName = $chinese")
    $out.Add("}")
    $out.Add("")
    $count++
}

$encoding = [System.Text.UTF8Encoding]::new($false)
[System.IO.File]::WriteAllLines($OutputPath, $out, $encoding)
Write-Output "Generated $count bullet display-name patches -> $OutputPath"
