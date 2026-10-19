# KSP 1.12.5 → BDA 空战档案

这个仓库做三件事：

1. 把当前 KSP 1.12.5 安装里的模组完整列成表，写清名称、用途、版本与体积；
2. 按“BDA 空战”主题给出保留/删除名单；
3. 收纳我们自己写的补丁与插件，方便恢复或迁移到另一台机器。

> 当前状态：**BDA+ LMP 版、Luna Multiplayer、PhysicsRangeExtender 已安装**。
> 本仓库同时保留了“清理前”和“清理后”两份清单，方便回滚与继续调整。

## 环境

| 项 | 值 |
|---|---|
| 游戏 | Kerbal Space Program 1.12.5（Steam） |
| 语言 | zh-cn |
| 路径 | `C:\Program Files (x86)\Steam\steamapps\common\Kerbal Space Program` |
| GameData 顶层目录 | 清理前 222 → 当前 170 |
| CKAN 已记录模块 | 清理前 251 → 当前 187 |
| GameData 体积 | 清理前 16.82 GB → 当前 6.69 GB |
| 已释放 | **约 10.13 GB** |

## 文件

| 路径 | 内容 |
|---|---|
| [`MODLIST.md`](MODLIST.md) | **清理前**全量清单：名称、用途、版本、BDA 取舍、体积 |
| [`MODLIST-AFTER.md`](MODLIST-AFTER.md) | **当前**清单（170 个目录） |
| [`MODS-TABLE.md`](MODS-TABLE.md) | 当前 170 个模组的中英对照表：英文名 / 中文名 / 作用简述 |
| [`MODS-CHECKLIST.md`](MODS-CHECKLIST.md) | 可勾选的删除清单；勾选代表想删 |
| [`DELETION-PLAN.md`](DELETION-PLAN.md) | 删除名单、保留名单、可选项与回滚说明 |
| [`DELETION-LOG.md`](DELETION-LOG.md) | 实际执行记录、CKAN 连带删除与恢复情况 |
| [`BDA-INSTALL.md`](BDA-INSTALL.md) | BDA+ LMP 版的版本选择、安装记录与扩展建议 |
| [`MULTIPLAYER.md`](MULTIPLAYER.md) | LMP 服务器启动、客户端连接、配置与联机注意事项 |
| [`mods/installed-modules-before.csv`](mods/installed-modules-before.csv) | 清理前 CKAN 的 251 个模块 |
| [`mods/installed-modules.csv`](mods/installed-modules.csv) | 当前 CKAN 的 185 个模块 |
| [`mods/gamedata-inventory-before.csv`](mods/gamedata-inventory-before.csv) | 清理前 222 个顶层目录 |
| [`mods/gamedata-inventory.csv`](mods/gamedata-inventory.csv) | 当前 170 个顶层目录 |
| [`patches/README.md`](patches/README.md) | 我们自己的补丁一览、依赖与安装方法 |
| [`patches/`](patches/) | 可直接放进 `GameData\` 的补丁目录 |
| [`tools/build_inventory.py`](tools/build_inventory.py) | 重新生成清单的脚本（只读 GameData，不改游戏文件） |
| [`data/catalog.json`](data/catalog.json) | 人工维护的中文名称/用途/BDA 取舍 |

## BDA 与联机

当前安装的是 **BDArmory Plus LMP edition 1.13.1.0**（BDA-MP-Renewed v0.1）：

- 基础是 BDA+ 1.13.1.0，包含武器、雷达、导弹、炮塔、AI、战斗管理界面
- 为 Luna Multiplayer 增加了武器同步
- 依赖：`ModuleManager`、`PhysicsRangeExtender`
- 语言：自带多语言词条（含中文）

标准 BDA+ 不能和 LMP 同步武器，所以这里用 LMP 分支；详见
[`BDA-INSTALL.md`](BDA-INSTALL.md) 和 [`MULTIPLAYER.md`](MULTIPLAYER.md)。

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
- **部件/引擎外观**：ReStock/ReStock+、Waterfall、Restock Waterfall Expansion、Firefly。

## 已经删除的主题

完整表格见 [`DELETION-PLAN.md`](DELETION-PLAN.md)，执行结果见
[`DELETION-LOG.md`](DELETION-LOG.md)。这里只列大类：

- 远未来：Far Future Technologies、Future Technologies Expansion
- 行星包：Kcalbeloh（含 4K 纹理）、OPM、Outer Parallax、Scatterer OPM
- 科幻/复古太空飞机：OPT、OPT Legacy、RetroFuture、Mk4 Expansion
- 航天飞机：SOCK、Cormorant、Space Shuttle Accessories、Benjee10 sharedAssets
- 殖民地/基地：USI、Planetary Base、Ground Construction、SimpleConstruction、Keridian
- 空间站：SSPX、Station Science、Universal Storage 2、HabTech
- 发射场：Modular Launch Pads
- 探索合同包：11 个 Contract Packs
- 环境美化：Parallax Continued 及三套纹理、Scatterer、EVE、Spectra、KSPRC、
  TUFX、PlanetShine

**后来恢复：** Mk2/Mk3 Expansion、SXT、KSC Extended，以及 KSC Extended 需要的
Kerbal Konstructs、Tundra Space Center、OSSNTR；全部 IVA 相关包也保留。
体积云（Low End Volumetric Clouds）也已单独恢复。

这些目录已经移出 `GameData`，原件在 `_disabled_mods\BDA_20261019\`；仍可随时搬回。
清单里保留了每个包的标识与版本。

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
