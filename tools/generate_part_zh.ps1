param(
    [Parameter(Mandatory = $true)][string]$InputPath,
    [Parameter(Mandatory = $true)][string]$OutputPath,
    [Parameter(Mandatory = $true)][string]$Header
)

$lines = Get-Content -LiteralPath $InputPath -Encoding UTF8
$out = [System.Collections.Generic.List[string]]::new()
$out.Add("// $Header")
$out.Add("// 由 tools/generate_part_zh.ps1 根据 tools/zh/*.tsv 生成。")
$out.Add("")

$count = 0
foreach ($line in $lines) {
    if ([string]::IsNullOrWhiteSpace($line) -or $line.StartsWith("#")) { continue }
    $cols = $line -split "`t"
    if ($cols.Count -lt 3) { throw "Invalid row: $line" }

    $name = $cols[0].Trim()
    $title = $cols[1].Trim()
    $description = $cols[2].Trim()
    $manufacturer = if ($cols.Count -ge 4) { $cols[3].Trim() } else { "" }

    if ($name -match '\s') {
        $selectorName = $name -replace '\s', '?'
        if ($selectorName.Contains('(')) {
            $selectorName = $selectorName.Substring(0, $selectorName.IndexOf('(')) + '*'
        }
        $out.Add("@PART:HAS[#name[$selectorName]]:FINAL")
    }
    else {
        $out.Add("@PART:HAS[#name[$name]]:FINAL")
    }
    $out.Add("{")
    $out.Add("    @title = $title")
    $out.Add("    @description = $description")
    if ($manufacturer -ne "") { $out.Add("    @manufacturer = $manufacturer") }
    $out.Add("}")
    $out.Add("")
    $count++
}

$encoding = [System.Text.UTF8Encoding]::new($false)
[System.IO.File]::WriteAllLines($OutputPath, $out, $encoding)
Write-Output "Generated $count part patches -> $OutputPath"
