$ErrorActionPreference = 'Stop'

$ksp = 'C:\Program Files (x86)\Steam\steamapps\common\Kerbal Space Program'
$managed = Join-Path $ksp 'KSP_x64_Data\Managed'
$csc = 'C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe'
$here = $PSScriptRoot
$patchRoot = Split-Path -Parent $here
$packageRoot = Join-Path $patchRoot 'GameData\ScienceLabAutoTransmit'
$packagePlugins = Join-Path $packageRoot 'Plugins'
$out = Join-Path $packagePlugins 'ScienceLabAutoTransmit.dll'

if (-not (Test-Path -LiteralPath $csc)) {
    throw "C# compiler not found: $csc"
}

New-Item -ItemType Directory -Path $packagePlugins -Force | Out-Null

& $csc /nologo /target:library /optimize+ /out:$out `
    (Join-Path $here 'ScienceLabAutoTransmit.cs') `
    (Join-Path $here 'AssemblyInfo.cs') `
    /r:"$managed\Assembly-CSharp.dll" `
    /r:"$managed\UnityEngine.dll" `
    /r:"$managed\UnityEngine.CoreModule.dll" `
    /r:"$managed\UnityEngine.IMGUIModule.dll" `
    /r:"$managed\UnityEngine.UI.dll"

if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $out)) {
    throw 'Compilation failed.'
}

$deploy = Join-Path $ksp 'GameData\ScienceLabAutoTransmit'
New-Item -ItemType Directory -Path (Join-Path $deploy 'Plugins') -Force | Out-Null
Copy-Item -LiteralPath $out -Destination (Join-Path $deploy 'Plugins\ScienceLabAutoTransmit.dll') -Force
Copy-Item -LiteralPath (Join-Path $packageRoot 'ScienceLabAutoTransmit.cfg') -Destination $deploy -Force
Copy-Item -LiteralPath (Join-Path $packageRoot 'ScienceLabAutoTransmit.version') -Destination $deploy -Force

"Built: $out"
"Deployed: $deploy"
