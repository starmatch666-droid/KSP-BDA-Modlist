# BDA 化删除名单

> **2026-10-19 已执行。** 实际结果、CKAN 连带删除与恢复情况见
> [`DELETION-LOG.md`](DELETION-LOG.md)。执行后保留了 `Kopernicus` 与
> `WildBlueIndustries\001KerbalActuators`，因为 Parallax / Kerbal Planet Emblems
> 和 Near Future Aeronautics 仍分别依赖它们。

目标：保留 BDA 空战/飞行真正需要的东西，删掉“远未来、行星包、航天飞机、殖民地、
空间站、科幻太空飞机”等主题包及其专属补丁。

## 结论

- 建议删除的顶层目录：**54** 个
- 预计释放：**6.00 GB**（以实际磁盘占用为准）
- 当前 GameData：**16.82 GB**

BDArmory Continued 的 CKAN 依赖只有 **ModuleManager** 与 **PhysicsRangeExtender**；
因此下面这些包都不是运行 BDA 的必要条件。

## A. 明确删除（主题不符）

| 目录 | 名称 | 删除理由 | 大小 |
|---|---|---|---:|
| `KcalbelohTextures` | Kcalbeloh 4K Textures | Kcalbeloh 行星包 4K 纹理（约 1.2 GB）。 | 1.17 GB |
| `OuterParallax` | Outer Parallax | OPM/MPE 行星的视差地形与散射配置（约 690 MB）。 | 691 MB |
| `FarFutureTechnologies` | Far Future Technologies | 远未来聚变/反物质发动机与配套电力，主题与 BDA 不符。 | 455 MB |
| `WildBlueIndustries` | WildBlue Industries（Mk-33/Kerbal Actuators） | Mk-33 太空飞机与作动器部件包。 | 452 MB |
| `StationPartsExpansionRedux` | Stockalike Station Parts Expansion Redux | 大量原版风格空间站舱段与部件。 | 426 MB |
| `StationPartsExpansionReduxIVAs` | SSPX IVAs | SSPX 空间站舱段的 IVA 内饰。 | 373 MB |
| `OPT_Legacy` | OPT Legacy Spaceplane Parts | OPT 旧版太空飞机部件。 | 366 MB |
| `ModularLaunchPads` | Modular Launch Pads | 模块化发射台、服务塔与发射基础设施。 | 326 MB |
| `UniversalStorage2` | Universal Storage II | 模块化服务舱/通用储物部件。 | 313 MB |
| `OPT` | OPT Continued | 科幻风格太空飞机与部件包。 | 300 MB |
| `Benjee10_shuttleOrbiter` | Shuttle Orbiter Construction Kit | NASA 航天飞机轨道器部件包。 | 224 MB |
| `OPM` | Outer Planets Mod | 外行星行星包（Sarnus/Urlum/Neidon 等）。 | 116 MB |
| `SXT` | SXTContinued | 内存占用较低的原版风格部件扩展包。 | 97 MB |
| `PlanetaryBaseInc` | Kerbal Planetary Base Systems | 行星表面基地模块与配套系统。 | 96 MB |
| `TundraSpaceCenter` | Tundra's Space Center | 新一代发射台与航天中心建筑。 | 75 MB |
| `MarkIVSystem` | Mark IV Spaceplane System | Mk4 大型太空飞机部件。 | 67 MB |
| `KeridianDynamics` | Keridian Dynamics (KDVA) | 外星基地建造、3D 打印与资源加工部件。 | 60 MB |
| `RetroFuture` | RetroFuture | 复古风格飞机/太空飞机部件包。 | 58 MB |
| `Endurance` | Endurance Continued | 《星际穿越》永恒号/漫游者号部件包。 | 50 MB |
| `Cormorant Aeronology` | Shuttle Lifting Body | 航天飞机升力体、外储箱与助推器部件。 | 48 MB |
| `Mk2Expansion` | Mk2 Expansion | Mk2 机身扩展部件包。 | 42 MB |
| `UmbraSpaceIndustries` | Umbra Space Industries（Konstruction/USI-LS/Akita） | 殖民地建造、生命保障与物流体系。 | 41 MB |
| `KcalbelohSystem` | Kcalbeloh System | 异星系行星包，替换/扩展原版星系。 | 37 MB |
| `Mk3Expansion` | Mk3 Expansion | Mk3 机身扩展部件包。 | 36 MB |
| `OSSNTR` | Omega's Stockalike Structures: No Textures Required | 原版风格机场、跑道、发射场静态建筑。 | 34 MB |
| `StationScience` | MOAR Station Science | 空间站科学实验与模块。 | 23 MB |
| `HabTechProps` | HabTech Props | 空间站舱内道具与装饰。 | 23 MB |
| `GroundConstruction` | Global Construction | 在轨道/外星表面用建造包组装飞船。 | 18 MB |
| `htRobotics` | HabTech Robotics | 空间站机械臂与遥控关节。 | 14 MB |
| `ContractPacks` | Contract Packs（11 个合同包） | 探索、空间站、旅游、无人任务等生涯合同合集，偏探索主题。 | 5.0 MB |
| `FutureTechnologiesExpansion 0.3.1` | Future Technologies Expansion: Frontier Aeronautics | 聚变核热喷气发动机，属于远未来主题。 | 2.4 MB |
| `Space Shuttle Accessories` | Space Shuttle Accessories | SOCK 航天飞机的尾锥等配件。 | 2.0 MB |
| `SimpleConstruction` | SimpleConstruction! | 简易外星/轨道建造与发射台。 | 1.8 MB |
| `OPMFinalFrontierRibbons` | OPM Final Frontier Ribbons | OPM 行星包的 Final Frontier 绶带。 | 1.6 MB |
| `000_USITools` | USI Tools | Umbra Space Industries 系列（MKS/Konstruction/USI-LS）的前置库。 | 1.2 MB |
| `MPEFinalFrontierRibbons` | Minor Planets Expansion Ribbons | 已停用的 MPE 行星包的 Final Frontier 绶带。 | <1 MB |
| `KSCExtended` | KSC Extended | 扩建肯尼迪航天中心，增加发射台与建筑。 | <1 MB |
| `Singularity` | Singularity | 黑洞/引力透镜着色器，Kcalbeloh 相关。 | <1 MB |
| `ScattererOPM` | Scatterer OPM Config | OPM 行星包的大气散射配置。 | <1 MB |

## B. 随上级删除（专属补丁/前置）

| 目录 | 名称 | 删除原因 / 归属 | 大小 |
|---|---|---|---:|
| `CTTP` | Community Terrain Texture Pack | 行星模组用的社区地形纹理。 | 21 MB |
| `Kopernicus` | Kopernicus | 行星模组框架，只有行星包需要。 | 19 MB |
| `Benjee10_sharedAssets` | Benjee10 sharedAssets | Benjee10 航天飞机与舱外活动包的共享资源。 | 15 MB |
| `KerbalKonstructs` | Kerbal Konstructs | 静态建筑/发射场框架，服务 Tundra、KSCExtended 等。 | 9.9 MB |
| `OPT_Reconfig` | OPT Reconfig | OPT 的兼容/平衡重配置补丁。 | 7.3 MB |
| `KopernicusExpansion` | Kopernicus Expansion Continueder | Kopernicus 的行星效果扩展。 | <1 MB |
| `001_DuckweedUtils` | Duckweed Utils | Kopernicus 行星 PQS 工具，只服务行星包。 | <1 MB |
| `Endurance_适配` | Endurance 适配补丁 | 自制：Endurance 漫游者号电力、热控、USI 兼容与零件调整。 | <1 MB |
| `MLP_CN` | Modular Launch Pads 中文补丁 | 自制：模块化发射台部件简体中文。 | <1 MB |
| `ZZZ_USI_CN` | USI 中文补丁 | 自制：Konstruction/USI-LS/Akita 部件与界面简体中文。 | <1 MB |
| `ZZZ_GC_CN` | GroundConstruction 中文补丁 | 自制：GroundConstruction 部件与界面简体中文。 | <1 MB |
| `Endurance_CN` | Endurance 中文补丁 | 自制：Endurance 部件与 PAW 文本简体中文。 | <1 MB |
| `WormholeRelay` | Wormhole Relay | 自制：让虫洞两端的中继卫星互相连通 CommNet；只对 Kcalbeloh 虫洞有意义。 | <1 MB |
| `000_NiakoUtils` | Niako Utils | Kopernicus 行星着色/地形工具，只服务行星包。 | <1 MB |
| `ZZZ_KONSTRUCTION_INDEPENDENCE` | KS-500 本地工业补丁 | 自制：给 Konstruction KS-500 船坞增加本地资源缓冲与合成。 | <1 MB |

## C. 默认保留（BDA 直接相关或普适）

- **BDA 与前置**：ModuleManager、PhysicsRangeExtender（尚未安装）、Harmony、KSPCommunityFixes。
- **飞行/空战**：AtmosphereAutopilot、B9 Procedural Wings、CorrectCoL、Trajectories、
  MechJeb2、ThrottleControlledAvionics、RCS Build Aid、Docking Cam、DPAI、Wind Tunnel、
  Kerbal Flight Indicators、NavHud、NavUtilities、Persistent Rotation。
- **喷气机/载具**：Near Future Aeronautics、Firespitter、Kerbal Foundries、
  Retractable Lifting Surface、B9 Part Switch、KSPWheel。
- **推进/电力/热控**：Near Future 全套（Aeronautics/Construction/Electrical/Exploration/
  LaunchVehicles/Propulsion/Rovers/Solar/Spacecraft）、Cryo Engines/Tanks、Kerbal Atomics、
  System Heat 全套、Heat Control、Dynamic Battery Storage、Deployable Engines。
- **工程/建造**：KIS、KAS、Ship Manifest、Configurable Containers、TweakScale、
  Editor Extensions、VAB Organizer、Janitor's Closet、Hangar Extender、Dock Rotate。
- **通信**：CommNet Antennas Extension/Consumptor/Info、RemoteTech Redev Antennas。
- **视觉基础**：ReStock/ReStock+、Waterfall、Scatterer、EVE、Spectra、TUFX、PlanetShine、
  Firefly、Rocket Sound Enhancement。

## D. 可选项（不删也能玩 BDA）

- **IVA/内饰**：ASET、MOARdV Avionics、JSI/RPM、FreeIva、Reviva、DE_IVA、
  Probe Control Room、VesselView、Through The Eyes、Near Future Props、KSA IVA。
  如果只看外部视角打空战，这些可以再省 200 MB 左右。
- **生涯/合同**：Contract Configurator、Contract Packs、DMagic Utilities。
  合同包偏探索/空间站主题，纯空战存档可以删。
- **科学**：SCANsat、DMagic Orbital Science、Tarsier、SpaceDust、SpaceDust Next、ScienceAlert。
  科学玩法本身是普适的，默认保留。
- **视觉/性能**：Parallax Continued 三套纹理约 3.4 GB；如果 BDA 大规模空战掉帧，
  这是第一个值得关掉的东西。KSPRC、TextureReplacer、Conformal Decals、Indicator Lights、
  Chatterer、ZTheme、Benjee10 Suits 也都是纯外观。

## E. 存档与回滚

- 删除行星包（Kcalbeloh/OPM）会让依赖这些星球的存档无法正常加载；BDA 建议开新存档。
- 本次操作会先把目录移到 `_disabled_mods/BDA_20261019/`，再按需要从 CKAN 注销。
- `mods/gamedata-inventory.csv` 记录了每个目录的体积与 CKAN 标识，可用于恢复。
- 不建议直接删除 `Squad`、`SquadExpansion`、`ModuleManager`、`KSPCommunityFixes`。
