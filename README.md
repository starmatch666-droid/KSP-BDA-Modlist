# KSP 1.12.5 → BDA 空战档案

这个仓库做三件事：

1. 把当前 KSP 1.12.5 安装里的模组完整列成表，写清名称、用途、版本与体积；
2. 按“BDA 空战”主题给出保留/删除名单；
3. 收纳我们自己写的补丁与插件，方便恢复或迁移到另一台机器。

> 当前状态：**BDArmory Continued 还没有安装**。本仓库是安装前的清理档案，
> 不是已经装好 BDA 的成品整合包。

## 环境

| 项 | 值 |
|---|---|
| 游戏 | Kerbal Space Program 1.12.5（Steam） |
| 语言 | zh-cn |
| 路径 | `C:\Program Files (x86)\Steam\steamapps\common\Kerbal Space Program` |
| GameData 顶层目录 | 222 个 |
| CKAN 已记录模块 | 251 个 |
| GameData 体积 | 约 16.82 GB |
| 建议删除 | 53 个顶层目录，约 6.00 GB |

## 文件

| 路径 | 内容 |
|---|---|
| [`MODLIST.md`](MODLIST.md) | 全量清单：名称、用途、版本、BDA 取舍、体积 |
| [`DELETION-PLAN.md`](DELETION-PLAN.md) | 删除名单、保留名单、可选项与回滚说明 |
| [`mods/installed-modules.csv`](mods/installed-modules.csv) | CKAN 的 251 个模块（标识/名称/版本/作者/摘要） |
| [`mods/gamedata-inventory.csv`](mods/gamedata-inventory.csv) | 222 个顶层目录的机器可读盘点 |
| [`patches/README.md`](patches/README.md) | 我们自己的补丁一览、依赖与安装方法 |
| [`patches/`](patches/) | 可直接放进 `GameData\` 的补丁目录 |
| [`tools/build_inventory.py`](tools/build_inventory.py) | 重新生成清单的脚本（只读 GameData，不改游戏文件） |
| [`data/catalog.json`](data/catalog.json) | 人工维护的中文名称/用途/BDA 取舍 |

## BDA 需要什么

CKAN 当前稳定通道里的 **BDArmory Continued 1:v1.3.5_beta**：

- 依赖：`ModuleManager`、`PhysicsRangeExtender`
- 自带：武器、雷达、导弹、炮塔、AI、战斗管理界面
- 语言：自带 `zh-cn` 词条

也就是说，下面这些被删掉的主题包都不是 BDA 的运行前提。真正需要优先保证的是
`ModuleManager`、`Harmony`、`KSPCommunityFixes`、物理/气动辅助，以及 Near Future
这类能给战斗机提供喷气发动机与电力/热控的包。

## 保留的核心

- **飞行/空战**：AtmosphereAutopilot、B9 Procedural Wings、CorrectCoL、Trajectories、
  MechJeb2、ThrottleControlledAvionics、RCS Build Aid、Docking Cam、DPAI、Wind Tunnel。
- **喷气机**：Near Future Aeronautics、Firespitter、Kerbal Foundries、Retractable Lifting Surface。
- **推进/电力/热控**：Near Future 全套、Cryo Engines/Tanks、Kerbal Atomics、System Heat、
  Heat Control、Dynamic Battery Storage。
- **工程/通信**：KIS、KAS、Ship Manifest、Configurable Containers、TweakScale、
  CommNet Antennas、RemoteTech Redev。
- **视觉基础**：ReStock/ReStock+、Waterfall、Scatterer、EVE、Spectra、TUFX。

## 建议删除的主题

完整表格见 [`DELETION-PLAN.md`](DELETION-PLAN.md)，这里只列大类：

- 远未来：Far Future Technologies、Future Technologies Expansion
- 行星包：Kcalbeloh（含 4K 纹理）、OPM、Outer Parallax、Scatterer OPM、Kopernicus 及其工具
- 科幻/复古太空飞机：OPT、OPT Legacy、RetroFuture、Mk2/Mk3/Mk4 Expansion
- 航天飞机：SOCK、Cormorant、Space Shuttle Accessories、Benjee10 sharedAssets
- 殖民地/基地：USI、Planetary Base、Ground Construction、SimpleConstruction、Keridian、OSSNTR
- 空间站：SSPX、Station Science、Universal Storage 2、HabTech
- 发射场：Modular Launch Pads、Tundra、KSC Extended、Kerbal Konstructs
- 探索合同包：11 个 Contract Packs

删除后仍可随时从 CKAN 或原发布页装回；清单里保留了每个包的标识与版本。

## 我们自己的补丁

仓库中的 `patches/` 包含：

- `KISA_Fixes`、`KISA_Flags`、`KISA_FlagsAgency`
- `RealChute_CN`（含 C# 源码）
- `ResupplyNetwork`
- `DSH_Plugins`（Engine Thrust Reverser）
- `Endurance_适配`、`Endurance_CN`
- `MLP_CN`、`ZZZ_GC_CN`、`ZZZ_USI_CN`、`ZZZ_KONSTRUCTION_INDEPENDENCE`
- `WormholeRelay`（含 C# 源码）
- 未安装的 `ArcjetXeArPatch`

其中 `Endurance_*`、`MLP_CN`、`ZZZ_GC_CN`、`ZZZ_USI_CN`、`ZZZ_KONSTRUCTION_INDEPENDENCE`
和 `WormholeRelay` 会随对应主题包一起停用；补丁本身仍保留在仓库，方便以后装回。

## 重新生成清单

```powershell
python tools\build_inventory.py `
  --ksp "C:\Program Files (x86)\Steam\steamapps\common\Kerbal Space Program" `
  --repo "C:\Users\STARM\Documents\KSP-BDA-Work\KSP-BDA-Modlist"
```

脚本只读取 `GameData` 与 `CKAN\registry.json`，不会删除或移动任何模组。

## 相关仓库

- [ResupplyNetwork](https://github.com/starmatch666-droid/ResupplyNetwork)
- [Endurance-Compat](https://github.com/starmatch666-droid/Endurance-Compat)
- [Endurance-CN](https://github.com/starmatch666-droid/Endurance-CN)
- [RealChute-CN](https://github.com/starmatch666-droid/RealChute-CN)
- [ModularLaunchPads-CN](https://github.com/starmatch666-droid/ModularLaunchPads-CN)

## 注意

- 删除行星包（Kcalbeloh/OPM）会让依赖这些星球的旧存档无法正常加载；BDA 建议开新存档。
- 本仓库不包含第三方模组本体、存档或游戏本体文件。
- 补丁目录中的第三方美术资源（如 KISA 旗子）仅用于个人存档；再分发前请确认原作者许可证。
