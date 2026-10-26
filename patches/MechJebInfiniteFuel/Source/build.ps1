$ErrorActionPreference = 'Stop'

$ksp = 'C:\Program Files (x86)\Steam\steamapps\common\Kerbal Space Program'
$managed = Join-Path $ksp 'KSP_x64_Data\Managed'
$csc = 'C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe'
$here = $PSScriptRoot
$patchRoot = Split-Path -Parent $here
$packageRoot = Join-Path $patchRoot 'GameData\MechJebInfiniteFuel'
$packagePlugins = Join-Path $packageRoot 'Plugins'
$out = Join-Path $packagePlugins 'MechJebInfiniteFuel.dll'

if (-not (Test-Path -LiteralPath $csc)) {
    throw "C# compiler not found: $csc"
}

New-Item -ItemType Directory -Path $packagePlugins -Force | Out-Null

& $csc /nologo /target:library /optimize+ /out:$out `
    (Join-Path $here 'MechJebInfiniteFuel.cs') `
    (Join-Path $here 'AssemblyInfo.cs') `
    /r:"$managed\Assembly-CSharp.dll" `
    /r:"$managed\UnityEngine.dll" `
    /r:"$managed\UnityEngine.CoreModule.dll" `
    /r:"$ksp\GameData\000_Harmony\0Harmony.dll" `
    /r:"$ksp\GameData\MechJeb2\Plugins\MechJeb2.dll" `
    /r:"$ksp\GameData\MechJeb2\Plugins\MechJebLib.dll" `
    /r:"$ksp\GameData\MechJeb2\Plugins\MechJebLibBindings.dll"

if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $out)) {
    throw 'Compilation failed.'
}

$deploy = Join-Path $ksp 'GameData\MechJebInfiniteFuel\Plugins'
New-Item -ItemType Directory -Path $deploy -Force | Out-Null
Copy-Item -LiteralPath $out -Destination (Join-Path $deploy 'MechJebInfiniteFuel.dll') -Force
Copy-Item -LiteralPath (Join-Path $packageRoot 'MechJebInfiniteFuel.version') -Destination (Join-Path (Split-Path -Parent $deploy) 'MechJebInfiniteFuel.version') -Force

"Built: $out"
"Deployed: $deploy\MechJebInfiniteFuel.dll"
