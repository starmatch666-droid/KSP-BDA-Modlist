# 删除执行记录（2026-10-19）

## 结果

| 项 | 删除前 | 删除后 |
|---|---:|---:|
| GameData 顶层目录 | 222 | 138 |
| CKAN 记录模块 | 251 | 146 |
| GameData 体积 | 16.82 GB | 6.21 GB |
| 释放空间 | — | **约 10.61 GB** |

最初名单 54 个顶层目录。经过两轮调整，相对原始 222 个目录实际移除了 58 个，
并新增了 Final Frontier 的 `STMRibbons`，当前 165 个。`Kopernicus`、
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

## BDA 与联机安装

- BDA+ LMP 版 `1.13.1.0`：`GameData\BDArmory`（来自 BDA-MP-Renewed v0.1）
- Luna Multiplayer Client `0.30.0-Draft`
- Physics Range Extender `1.21.0`
- Ferram Aerospace Research Continued `0.16.1.2`（WindTunnel 因冲突移除）
- LMP 服务端在 `C:\Users\STARM\Documents\KSP-BDA-Work\LMP-Server-0.30.0\LMPServer`

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

## 当前需要补的东西

- **BDArmory Continued 尚未安装**。
- BDA 的 CKAN 依赖 `ModuleManager` 已有；`PhysicsRangeExtender` 尚未安装，
  安装 BDA 时 CKAN 会自动带上。
- 如果还要装 BDA 的扩展包（BDArmoryExtended、BDModularMissileParts 等），
  再按需安装，不要一次把旧的主题包全装回来。

## 回滚

1. 手工包：把 `_disabled_mods\BDA_20261019\<目录>` 复制回 `GameData\`。
2. CKAN 包：在 CKAN 里按标识重新安装，或导入 `mods/modlist-before.ckan`。
3. 旧存档如果用了 Kcalbeloh/OPM，回滚后才能正常加载；BDA 建议开新存档。

备份清单与每个目录的大小见 `mods/gamedata-inventory-before.csv`。
