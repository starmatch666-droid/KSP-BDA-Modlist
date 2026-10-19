# 删除执行记录（2026-10-19）

## 结果

| 项 | 删除前 | 删除后（第二轮结束时） |
|---|---:|---:|
| GameData 顶层目录 | 222 | 148 |
| CKAN 记录模块 | 251 | 158 |
| GameData 体积 | 16.82 GB | 7.27 GB |
| 释放空间 | — | **约 9.55 GB** |

上表是第二轮清理结束时的快照。后续取消联机并补装全部兼容 BDA 部件包后，
当前为 **154 个顶层目录、164 个 CKAN 模块、8.96 GB**；详见文末第四轮。

最初名单 54 个顶层目录。经过两轮调整，相对原始 222 个目录实际移除了 58 个，
并新增了 Final Frontier 的 `STMRibbons`，当时为 165 个。`Kopernicus`、
`WildBlueIndustries\001KerbalActuators` 以及后来恢复的 Mk2/Mk3/SXT/KSCExtended
及其配套建筑都在。CKAN 管理的部分已用 `ckan remove` 注销，手工安装的部分已移出
`GameData`。目录没有直接永久删除：原件都在
`_disabled_mods\BDA_20261019\` 下，可随时搬回。

## 第一轮删掉的主题（后续部分已恢复）

- 远未来：Far Future Technologies、Future Technologies Expansion
- 行星包：Kcalbeloh System/4K Textures、OPM、Outer Parallax、Scatterer OPM、
  Kopernicus Expansion、Kcalbeloh/MPE/OPM 绶带、Singularity
- 科幻/复古太空飞机：OPT、OPT Legacy、OPT Reconfig、RetroFuture、Mk4 Expansion
- 航天飞机：SOCK、Cormorant、Space Shuttle Accessories、Benjee10 sharedAssets
- 殖民地/基地：USI（Konstruction/USI-LS/Akita）、Planetary Base、Ground Construction、
  SimpleConstruction、Keridian Dynamics、Planetside MMSEV、HabTech Props
- 空间站：SSPX、SSPX IVAs、Station Science、Universal Storage 2、HabTech Robotics
- 发射场：Modular Launch Pads
- 探索合同包：11 个 Contract Packs
- 主题部件/补丁：Endurance、WildBlue Mk-33、MLP_CN、ZZZ_GC_CN、
  ZZZ_USI_CN、ZZZ_KONSTRUCTION_INDEPENDENCE、WormholeRelay

## 第二轮调整（用户指定）

**恢复并标为必留：**

- Mk2Expansion、Mk3Expansion、SXT
- KSCExtended，以及它的配套建筑依赖 KerbalKonstructs、Tundra Space Center、OSSNTR
- 全部 IVA 相关：ASET、MOARdV Avionics、JSI/RPM、FreeIva、Reviva、DE_IVAExtension、
  Probe Control Room、VesselView、Through The Eyes、KSA IVA、Near Future Props
  （这些原本就没有被删，只是从“可选”改为“必留”）

**删除环境美化：**

- Parallax Continued + Planet/Scatter/Terrain 三套纹理
- Scatterer + 默认配置/太阳耀斑 + 大气缓存
- EVE、Spectra、KSPRC 城市灯光、TUFX 及其配置、PlanetShine

这些环境包已移到 `_disabled_mods\BDA_20261019\env_beautify_20261019\`。
ReStock、Waterfall、Rocket Sound Enhancement、Firefly 等部件/引擎外观或音效保留。

**体积云恢复：** `LowEndVolumetricCloudsMod` 已用 CKAN 1.0.3 重新安装，
包含 `Plugins`、`Shaders` 与版本文件；旧的手工目录只有一张纹理，已在备份里保留。

## BDA 安装与联机取消

- 标准单机 BDA+ `1.13.1.0`：CKAN `BDArmoryForRunwayProject`
- Physics Range Extender `1.21.0`
- Ferram Aerospace Research Continued `0.16.1.2`（WindTunnel 因冲突移除）
- 原 BDA-MP-Renewed 备份在 `_disabled_mods\BDA_20261019\BDA-MP-Renewed_20261019`
- LMP 客户端已移除；服务端归档在 `KSP-BDA-Work\_disabled_multiplayer`
- 已安装 BDA 扩展：BDArmoryExtended、BDModularMissileParts、AviatorArsenal、
  KerbalAdvancedDefenseReborn、NorthKerbinDynamicsRenewedExtended、BDAUITeamIcons、
  TURD 两套、BKWeaponsPack、RefurbishedArmory
- `BDAUITeamIcons` 因引用旧 BDA 1.3.6.4 的 `MissileFire`、在 BDA+ 1.13 下
  加载失败，已移除并备份到 `_disabled_mods\BDA_20261019\BDAUITeamIcons_incompatible_20261019`

详见 [`BDA-INSTALL.md`](BDA-INSTALL.md) 与 [`MULTIPLAYER.md`](MULTIPLAYER.md)。

## 第三轮：勾选删除（2026-10-19）

按 `MODS-CHECKLIST-APPLIED-20261019.md` 勾选的 33 项执行，备份在
`_disabled_mods\BDA_20261019\checked_20261019\`（约 489 MB）：

Astrogator、Docking Cam、NavUtilities、DPAI、Filter Extensions 及默认配置、
Janitor's Closet、KAS、KIS、Moar Filter Configs、QuickMods 五项、RCS Build Aid、
Ship Manifest、RemoteTech 过滤器补丁、Cryo Engines、Cryo NFAero、Cryo Tanks、
Decaying RTGs、Xenon Hall Thrusters、DMagic Orbital Science、ScienceAlert、
Space Dust/Next、Tarsier、Custom Barn Kit、DMagic Utilities、Final Frontier/
绶带、ReStrategia、Benjee10 Suits、Crew Light、REPOSoftTech/DeepFreeze、
Resupply Network。

另外按用户要求删除 **FreeIva 0.2.20.2**：它在 IVA 里会锁住飞船控制，
导致 Z（满油门）、X（油门归零）等键失效。备份在
`_disabled_mods\BDA_20261019\FreeIva_removed_20261019\`。

CKAN 因 `CryoTanks` 依赖顺手移除了未勾选的 **Kerbal Atomics**；已用
`KerbalAtomics-NTRsUseLF` 补丁把它装回，保留核推进，但不再依赖 CryoTanks。

## 保留但原本在“随上级删除”里的东西

- **Kopernicus**：Kerbal Planet Emblems 仍然依赖它。行星包与 Parallax 已删，
  但框架本身保留。
- **KerbalActuators**（`WildBlueIndustries\001KerbalActuators`）：Near Future
  Aeronautics 的硬依赖，保留。Mk-33 本体已删。
- **Benjee10 sharedAssets**：删除 Planetside/HabTech 后已无依赖，最终已移除。

## CKAN 批量删除的连带问题

CKAN 在 `--headless` 下把“依赖被删后失去依赖”的模组也一并删了，包括：

- Near Future Aeronautics
- Firespitter Core / Firespitter Resources
- Parallax Continued 与三套纹理
- ModularFlightIntegrator
- KSP Texture Loader
- Kerbal Planet Emblems
- Retractable Lifting Surface
- SpacetuxSA
- Planetside Exploration Technologies

这些已经重新安装；其中 Planetside、HabTech Props、Mark IV 和 Benjee10 sharedAssets
随后作为主题包再次移除。Near Future Aeronautics、Firespitter、Kopernicus、
KSP Texture Loader、Kerbal Planet Emblems、ModularFlightIntegrator、
Retractable Lifting Surface、SpacetuxSA 和 KerbalActuators 当前都在；
Parallax 与三套纹理已在第二轮按要求删除。
- Final Frontier 与三个角色绶带包在连带删除后也已重新安装，`Nereid` 与
  `STMRibbons` 目录已恢复。

## 第四轮：取消联机后补装全部兼容 BDA 部件（2026-10-19）

- 补装 `KerbalPowersArmory` + `KerbalPowersCore`：32 个现代舰炮、导弹、雷达与
  弹道武器；CKAN 元数据明确依赖 `BDArmoryForRunwayProject`。
- 补装 `FishyAntiMissileSpam` + `Fishy-Mod-Core`：105 个机炮、导弹、炸弹、
  雷达、激光与核武器部件。
- 补装 `FoxDefenseContracts` + `FDC_Armor`：209 个二战至现代坦克/自行火炮
  炮塔、机炮、炸弹、地雷与装甲兼容配置。
- 补装 `BDAnimationModules`，供旧式 BDA 部件播放动画。
- 中文补丁：Kerbal Powers 146 个词条、Fishy 104 个部件、Fox 209 个部件、
  65 种弹药类型显示名与 5 种 Fox 弹药资源名；`ZZZ_BDA_CN` 同步到仓库。
- `BDArmoryContinued`、`NorthKerbinDynamicRenewed` 与 BDA+ 冲突；
  `BDArmoryMultiplayer` 随联机取消；`BDAUITeamIcons` 引用旧 BDA 1.3.6.4，
  仍不安装。
- `KISA_Fixes\VABOrganizer_SubcategoryFix.cfg` 中两个部件名列表含制表符，
  已清除；ModuleManager 最近一次完整启动为 **32191 个补丁、0 错误、1 个警告**。

当前 GameData：**154 个顶层目录、164 个 CKAN 模块、8.96 GB**。

## 回滚

1. 手工包：把 `_disabled_mods\BDA_20261019\<目录>` 复制回 `GameData\`。
2. CKAN 包：在 CKAN 里按标识重新安装，或导入 `mods/modlist-before.ckan`。
3. 旧存档如果用了 Kcalbeloh/OPM，回滚后才能正常加载；BDA 建议开新存档。

备份清单与每个目录的大小见 `mods/gamedata-inventory-before.csv`。
