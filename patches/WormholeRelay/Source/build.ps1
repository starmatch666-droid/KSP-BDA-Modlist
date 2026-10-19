# 用 KSP 自带的程序集编译 WormholeRelay.dll（需要 Windows 自带的 csc.exe，无需 SDK）
$ErrorActionPreference = 'Stop'
$ksp   = 'C:\Program Files (x86)\Steam\steamapps\common\Kerbal Space Program'
$m     = Join-Path $ksp 'KSP_x64_Data\Managed'
$csc   = 'C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe'
$here  = $PSScriptRoot
$out   = Join-Path $here 'WormholeRelay.dll'

& $csc /nologo /target:library /out:$out (Join-Path $here 'WormholeRelay.cs') `
    /r:"$m\Assembly-CSharp.dll" /r:"$m\Assembly-CSharp-firstpass.dll" `
    /r:"$m\UnityEngine.dll" /r:"$m\UnityEngine.CoreModule.dll" /r:"$m\UnityEngine.UI.dll" `
    /r:"$ksp\GameData\000_Harmony\0Harmony.dll"

if (Test-Path $out) {
    $dst = Join-Path $ksp 'GameData\WormholeRelay\Plugins'
    New-Item -ItemType Directory -Path $dst -Force | Out-Null
    Copy-Item -LiteralPath $out -Destination $dst -Force
    "编译并部署完成: $dst\WormholeRelay.dll  ($((Get-Item $out).Length) 字节)"
} else { "编译失败，见上面的错误" }
