# KSP 删除后模组清单（BDA 当前状态）

- 快照时间：2026-10-19
- KSP：1.12.5（zh-cn，Steam）
- GameData 顶层目录：**155** 个
- CKAN 已记录模块：**165** 个
- GameData 总体积：**8.97 GB**
- 删除后仍存在的顶层目录：**155** 个
- 可选项（IVA/视觉/科学等，按需保留）：约 **111 MB**

> 这是“当前安装”的盘点，不是推荐安装顺序。BDA+ 标准单机版依赖
> ModuleManager 与 PhysicsRangeExtender；下面标为“必留”的多数是飞行、建造、
> 通信与 Near Future 推进等对空战/飞行有用的基础设施。

## 怎么读这张表

| 标记 | 含义 |
|---|---|
| ✅ 必留 | 框架/前置、BDA 直接相关，或对喷气机与空战有明显帮助 |
| ◻️ 可选 | 不影响 BDA 运行，按画面、IVA、科研或生涯偏好保留 |
| ❌ 建议删除 | 主题与 BDA 不符，或只是某个主题包的附属补丁 |
| ⏸️ 已禁用 | 目录还在，但当前不参与加载 |

“随上级删除”表示它本身是某个主题包的汉化/兼容补丁；上级包删掉后它也没有意义。

## 完整清单

### 基础框架与前置

| 目录 | 名称 | 用途 | 版本 | BDA 取舍 | 大小 |
|---|---|---|---|---|---:|
| `KSPCommunityFixes` | KSP Community Fixes | 社区维护的大量底层 bug 修复与性能改进，必留。 | 1:1.41.1 | ✅ 必留 | 955 MB |
| `000_KSPBurst` | KSPBurst | Burst 编译器与粒子/着色器优化库；体积大但属于性能基础设施。 | v1.7.4.11 | ✅ 必留 | 391 MB |
| `BDArmory` | BDArmory Plus | 标准单机 BDA+ 1.13.1.0；武器、雷达、导弹、炮塔与 AI。<br>注：CKAN 包 BDArmoryForRunwayProject；多人联机已取消。 | 2:v1.13.1.0 | ✅ 必留 | 57 MB |
| `Kopernicus` | Kopernicus | 行星模组框架；Kerbal Planet Emblems 仍需要它，行星包与 Parallax 删除后保留本体。<br>注：不再安装 Kcalbeloh/OPM/Parallax，但星球徽章依赖此框架。 | 2:release-1.12.1-251 | ✅ 必留 | 20 MB |
| `000_TexturesUnlimited` | Textures Unlimited | 金属度/贴图着色框架，Near Future 换色与 ReStock 外观会用到。 | 1.6.4.30 | ✅ 必留 | 11 MB |
| `WildBlueIndustries` | Kerbal Actuators（Mk-33 已删除） | Near Future Aeronautics 的作动器前置；Mk-33 太空飞机部件包已删除。<br>注：目录保留的是 001KerbalActuators，供 NFA 的螺旋桨/倾转发动机使用。 | v1.9.0 | ✅ 必留 | 5.2 MB |
| `KSPTextureLoader` | KSP Texture Loader | 运行时纹理加载库。 | 1.0.36 | ✅ 必留 | 2.1 MB |
| `000_Harmony` | Harmony2 | 运行时方法补丁库，大量插件的前置。 | 2.2.1.0 | ✅ 必留 | <1 MB |
| `000_AT_Utils` | AT Utils | Allista 系列模组的通用工具库（资源、动画、UI 辅助）。 | v1.10.1 | ✅ 必留 | <1 MB |
| `SpaceTuxLibrary` | SpaceTux Library | SpaceTux 系列模组的通用库。 | 0.0.9 | ✅ 必留 | <1 MB |
| `BahaSP` | BahamutoD Animation Modules | BDA/旧式部件动画模块库，供使用 BDAnimator 的部件播放动画。 | 1:v0.6.7.1 | ✅ 必留 | <1 MB |
| `B9PartSwitch` | B9 Part Switch | 部件模型/资源/节点切换框架，大量部件包的前置。 | v2.21.0.4 | ✅ 必留 | <1 MB |
| `KSPWheel` | KSPWheel | 轮子/悬挂物理库，Kerbal Foundries 等使用。 | 1:0.16.14.33 | ✅ 必留 | <1 MB |
| `CommunityCategoryKit` | Community Category Kit | 社区通用部件分类。 | v112.0.1 | ✅ 必留 | <1 MB |
| `SpaceTuxSA` | SpacetuxSA | SpaceTux 共享代码/工具。 | 0.3.13.1 | ✅ 必留 | <1 MB |
| `000_ClickThroughBlocker` | ClickThrough Blocker | 修复模组窗口点击穿透到场景的问题。 | 1:2.1.10.23 | ✅ 必留 | <1 MB |
| `CommunityResourcePack` | Community Resource Pack | 社区通用资源定义，Near Future/Cryo/USI 等共用。 | v112.0.1 | ✅ 必留 | <1 MB |
| `001_ToolbarControl` | Toolbar Controller | 统一管理 Blizzy/原版工具栏按钮。 | 1:0.1.9.14 | ✅ 必留 | <1 MB |
| `ROUtils` | ROUtils | RO 系列模组的通用工具库。 | v1.2.0.0 | ✅ 必留 | <1 MB |
| `KerbalJointReinforcement` | Kerbal Joint Reinforcement | 加固部件连接，减少大型飞行器抖动。 | v4.2.28 | ✅ 必留 | <1 MB |
| `PatchManager` | PatchManager | 在游戏内查看/管理 ModuleManager 补丁。 | 0.0.17.8 | ✅ 必留 | <1 MB |
| `KerbalChangelog` | Kerbal Changelog | 游戏内模组更新日志窗口。 | v1.4.2 | ✅ 必留 | <1 MB |
| `CustomPreLaunchChecks` | Custom Pre Launch Checks | 发射前检查 API，供其他模组挂接。 | 1.8.1.1 | ✅ 必留 | <1 MB |
| `PhysicsRangeExtender` | Physics Range Extender | 扩展物理范围，BDA 雷达/远距离交战需要。 | 1.21.0 | ✅ 必留 | <1 MB |
| `000_SerializationFix` | KSP Serialization Fix | 修复 KSP 配置序列化的兼容性问题，供 Aviator Arsenal 等模组使用。 | 1.0.1 | ✅ 必留 | <1 MB |
| `Shabby` | Shabby | 着色器资源包加载库。 | 0.4.2 | ✅ 必留 | <1 MB |
| `ModularFlightIntegrator` | Modular Flight Integrator | 气动/热集成框架，FAR 等模组使用。 | 1.2.10.0 | ✅ 必留 | <1 MB |
| `StagedAnimation` | Staged Animation | 分级时播放部件动画的插件。 | v2.0 | ✅ 必留 | <1 MB |
| `FireflyAPI` | Firefly API | Firefly 与其它模组通信的接口。 | 1.0.0.0 | ✅ 必留 | <1 MB |

### 飞行、导航与自动化

| 目录 | 名称 | 用途 | 版本 | BDA 取舍 | 大小 |
|---|---|---|---|---|---:|
| `MechJeb2` | MechJeb2 | 自动驾驶、轨道信息、交会/着陆辅助。 | 2.15.3.1 | ✅ 必留 | 8.7 MB |
| `RealChute` | RealChute Parachute Systems | 更真实的降落伞物理与配置。 | v1.4.9.5 | ✅ 必留 | 5.5 MB |
| `TriggerTech` | Kerbal Alarm Clock + Transfer Window Planner | 闹钟/时间提醒与转移窗口规划。 | 1:3.14.2.7 / v1.9.1.1 | ✅ 必留 | 2.4 MB |
| `PersistentRotation` | Persistent Rotation Upgraded | 时间加速/切换飞船时保持姿态与自转。 | 1.9.2.1 | ✅ 必留 | 1.9 MB |
| `FerramAerospaceResearch` | Ferram Aerospace Research Continued | 真实气动模型；替代原版部件气动，处理跨声速/高超声速与气动稳定性；自带中文，残留英文已补。<br>注：与 WindTunnel 冲突，已移除 WindTunnel。 | 3:0.16.1.2 | ✅ 必留 | 1.1 MB |
| `ThrottleControlledAvionics` | Throttle Controlled Avionics | 动态推力分配与姿态控制，垂直起降/悬停很有用。 | v3.8.0.1 | ✅ 必留 | <1 MB |
| `EasyVesselSwitch` | Easy Vessel Switch | 在飞行中快速切换附近飞船。 | 2.3 | ✅ 必留 | <1 MB |
| `Trajectories` | Trajectories | 考虑大气阻力/升力的再入与落点预测。 | v2.4.5.4 | ✅ 必留 | <1 MB |
| `AtmosphereAutopilot` | AtmosphereAutopilot | 大气层电传飞控，喷气机/战斗机保持姿态很好用。 | v1.6.1 | ✅ 必留 | <1 MB |
| `TrackingStationEvolved` | Tracking Station Evolved | 改进跟踪站飞船列表与筛选。 | 2:1.0.9.1 | ✅ 必留 | <1 MB |
| `WaypointManager` | Waypoint Manager | 飞行中显示/创建自定义航点。 | 2.8.4.7 | ✅ 必留 | <1 MB |
| `SpeedUnitAnnex` | Speed Unit Annex | 导航球速度单位与附加读数。 | 1.6.1 | ✅ 必留 | <1 MB |
| `BetterBurnTime` | BetterBurnTime | 点火、自杀式着陆与交会燃烧时间提示。 | 1.10 | ✅ 必留 | <1 MB |
| `NavHud` | NavHud | 把导航球信息投射到外部 HUD。 | 1.4.0.5 | ✅ 必留 | <1 MB |
| `PlanetInfoPlus` | Planet Info Plus | 跟踪站/地图显示行星详细数据。 | 1.4.3 | ✅ 必留 | <1 MB |
| `BetterTimeWarp` | BetterTimeWarpContinued | 更细的时间加速档位与物理加速控制。 | 2.3.14.2 | ✅ 必留 | <1 MB |
| `CorrectCOL` | CorrectCoL | 修正气动中心/升力中心显示，设计飞机时有用。 | 1.6.5.5 | ✅ 必留 | <1 MB |
| `KerbalFlightIndicators` | Kerbal Flight Indicators | 抬头显示速度、高度、迎角等飞行信息。 | R20 | ✅ 必留 | <1 MB |
| `FruitKocktail` | Vertikal Speed Indicator | 导航球垂直速度颜色/数值提示。 | 1:1.2.2 | ✅ 必留 | <1 MB |

### 建造与工程

| 目录 | 名称 | 用途 | 版本 | BDA 取舍 | 大小 |
|---|---|---|---|---|---:|
| `DockRotate` | Dock Rotate | 对接后原地旋转飞船，无需 RCS 反复调整。 | v1.12.1.57 | ✅ 必留 | <1 MB |
| `TweakScale` | TweakScale Rescaled | 在编辑器缩放部件尺寸。 | 3.3.2.1 | ✅ 必留 | <1 MB |
| `ConfigurableContainers` | Configurable Containers | 把油箱/货舱改为可切换资源类型。 | 2.6.2.1 | ✅ 必留 | <1 MB |
| `EditorExtensionsRedux` | Editor Extensions Redux | 编辑器对齐、对称、选根等增强。 | 3.4.7 | ✅ 必留 | <1 MB |
| `VABOrganizer` | VAB Organizer | 按尺寸/类别整理 VAB 部件列表。 | 1.2.0 | ✅ 必留 | <1 MB |
| `FShangarExtender` | Hangar Extender Extended | 扩大 VAB/SPH 建造空间，方便大型飞机/导弹。 | 3.6.1 | ✅ 必留 | <1 MB |

### 推进、电力与热控

| 目录 | 名称 | 用途 | 版本 | BDA 取舍 | 大小 |
|---|---|---|---|---|---:|
| `NearFutureLaunchVehicles` | Near Future Launch Vehicles | 近未来大型运载火箭部件。 | 2.2.2 | ✅ 必留 | 417 MB |
| `NearFutureSpacecraft` | Near Future Spacecraft | 近未来飞船指令舱、服务舱与发动机。 | 1.4.6 | ✅ 必留 | 212 MB |
| `NearFutureSolar` | Near Future Solar | 近未来高效太阳能板。 | 1.3.3 | ✅ 必留 | 138 MB |
| `NearFutureExploration` | Near Future Exploration | 近未来探测、着陆与深空任务部件。 | 1.1.3 | ✅ 必留 | 120 MB |
| `NearFutureElectrical` | Near Future Electrical | 近未来反应堆、电容、电力分配。 | 2.0.1 | ✅ 必留 | 87 MB |
| `NearFutureConstruction` | Near Future Construction | 近未来结构件、桁架与对接部件。 | 1.3.3 | ✅ 必留 | 86 MB |
| `NearFutureAeronautics` | Near Future Aeronautics | 近未来喷气发动机、螺旋桨与航空部件，BDA 飞机主力。 | 2.1.2 | ✅ 必留 | 70 MB |
| `NearFuturePropulsion` | Near Future Propulsion | 离子/等离子/霍尔推进与配套电力。 | 1.3.6 | ✅ 必留 | 66 MB |
| `KerbalAtomics` | Kerbal Atomics | 核热火箭与核动力推进部件。 | 1:1.3.4 | ✅ 必留 | 56 MB |
| `NearFutureRovers` | Near Future Rovers | 近未来漫游车底盘、轮组与部件。 | 手工 | ✅ 必留 | 39 MB |
| `HeatControl` | Heat Control | 高级散热器与热管理部件，Near Future/核推进常用。 | 0.6.2 | ✅ 必留 | 18 MB |
| `SystemHeat` | System Heat | 更完整的核/工业热管理系统。 | 0.9.1 | ✅ 必留 | 3.0 MB |
| `DynamicBatteryStorage` | Dynamic Battery Storage | 电力规划与动态电池管理，Near Future 电力系统常用。 | 2:2.3.7.0 | ✅ 必留 | <1 MB |
| `SystemHeatFissionReactors` | System Heat - Fission Reactors | 核反应堆的 SystemHeat 配置。 | 0.9.1 | ✅ 必留 | <1 MB |
| `SystemHeatConverters` | System Heat - Converters | 资源转换器的 SystemHeat 配置。 | 0.9.1 | ✅ 必留 | <1 MB |
| `SystemHeatFissionEngines` | System Heat - Fission Engines | 核热发动机的 SystemHeat 配置。 | 0.9.1 | ✅ 必留 | <1 MB |
| `SystemHeatIonEngines` | System Heat - Ion Engines | 离子发动机的散热配置。 | 0.9.1 | ✅ 必留 | <1 MB |
| `DeployableEngines` | Deployable Engines | 可展开喷管的动画/状态管理插件。 | 1.3.1 | ✅ 必留 | <1 MB |
| `SystemHeatHarvesters` | System Heat - Harvesters | 采集器的 SystemHeat 配置。 | 0.9.1 | ✅ 必留 | <1 MB |
| `KerbalAtomicsNTRsUseLF` | Kerbal Atomics - Liquid Fuel Only | 把 Kerbal Atomics 的液氢发动机改为只烧液体燃料，避免依赖 CryoTanks。 | 1.3.4 | ✅ 必留 | <1 MB |
| `SystemHeatBoiloff` | System Heat - Cryo Tanks | 低温储箱的零蒸发/制冷配置。 | 0.9.1 | ✅ 必留 | <1 MB |
| `OrbitalLFOEngines` | Orbital LFO Engines | Near Future Spacecraft 的轨道级 LFO 发动机。 | 1.4.6 | ✅ 必留 | <1 MB |

### 飞机与地面载具

| 目录 | 名称 | 用途 | 版本 | BDA 取舍 | 大小 |
|---|---|---|---|---|---:|
| `KerbalFoundries` | Kerbal Foundries | 高质量轮子、履带与着陆架，适合地面战斗载具。 | 2.4.8.18 | ✅ 必留 | 88 MB |
| `B9_Aerospace_ProceduralWings` | B9 Procedural Wings | 程序化机翼，自由设计战斗机/轰炸机翼型。 | 3:0.46.1 | ✅ 必留 | 3.5 MB |
| `Firespitter` | Firespitter | 螺旋桨、旋翼与起落架插件/资源库。 | v7.17 | ✅ 必留 | <1 MB |
| `RetractableLiftingSurface` | Retractable Lifting Surface | 可收放/折叠升力面控制。 | 0.2.1.2 | ✅ 必留 | <1 MB |

### 通信

| 目录 | 名称 | 用途 | 版本 | BDA 取舍 | 大小 |
|---|---|---|---|---|---:|
| `RemoteTechRedev` | RemoteTech Redev Antennas | RemoteTech 风格天线包，接入原版 CommNet。 | 0.1.1 | ✅ 必留 | 9.2 MB |
| `CommNetAntennasExtension` | CommNet Antennas Extension | 补充 5M/32M/7G 等档位的直连与中继天线。 | 2.1.9 | ✅ 必留 | <1 MB |
| `CommNetAntennasInfo` | CommNet Antennas Info | 在 VAB/SPH 显示天线距离与链路信息。 | 3.1.4 | ✅ 必留 | <1 MB |
| `CommNetAntennasConsumptor` | CommNet Antennas Consumptor | 让天线按功耗消耗电力，并支持静态天线开关。 | 3.5.8 | ✅ 必留 | <1 MB |

### 科学与探测

| 目录 | 名称 | 用途 | 版本 | BDA 取舍 | 大小 |
|---|---|---|---|---|---:|
| `SCANsat` | SCANsat | 扫描卫星、资源/地形测绘与科学数据。 | v21.1 | ✅ 必留 | 49 MB |

### 生涯、合同与科技

| 目录 | 名称 | 用途 | 版本 | BDA 取舍 | 大小 |
|---|---|---|---|---|---:|
| `ContractConfigurator` | Contract Configurator | 合同配置框架，KomUniMun 军事合同包的前置。 | v2.13.4.0 | ✅ 必留 | 18 MB |
| `ContractPacks` | KomUniMun Contractual Warfare | BDA+ 军事合同包：在 Kerbin、月球和轨道执行防空、对地、反舰、太空拦截与武器测试合同；自带部分中文。 | 1.0.0 | ✅ 必留 | 13 MB |
| `CommunityTechTree` | Community Tech Tree | 扩展科技树，给 Near Future 等模组提供节点。 | 1:3.4.5 | ✅ 必留 | 1.8 MB |
| `HideEmptyTechTreeNodes` | Hide Empty Tech Tree Nodes | 隐藏没有可用部件的科技树节点。 | 1.3.2 | ✅ 必留 | <1 MB |

### IVA 与内饰

| 目录 | 名称 | 用途 | 版本 | BDA 取舍 | 大小 |
|---|---|---|---|---|---:|
| `ASET` | ASET Consolidated | 高精度 IVA 道具、航空仪表、ALCOR 座舱与 Mk1/Mk12 座舱内饰。 | 1.0.1 等 7 个 | ✅ 必留 | 66 MB |
| `NearFutureProps` | Near Future Props | Near Future 系列 IVA 道具与内饰。 | 1:0.7.2 | ✅ 必留 | 63 MB |
| `MOARdV` | MOARdV's Avionics Systems | 高级 IVA 航电、MFD 页面与舱内交互。 | v1.3.7 | ✅ 必留 | 39 MB |
| `JSI` | JSI / RasterPropMonitor | RPM 舱内显示器、透明座舱与相关 IVA 工具。 | V0.1.24.0 / 1:v1.1.0.1 | ✅ 必留 | 6.4 MB |
| `ProbeControlRoom` | Probe Control Room | 无人飞船的地面控制室视角与界面。 | 1.4.0 | ✅ 必留 | 5.9 MB |
| `DE_IVAExtension` | DE_IVAExtension | 给原版座舱增加更完整的高级 IVA。 | v1.3.0 | ✅ 必留 | <1 MB |
| `KSA` | KSA IVA Upgrade | 原版座舱的高精度 IVA 内饰升级。 | v1.6.7 | ✅ 必留 | <1 MB |
| `VesselView` | Vessel Viewer Continued | 在 IVA 中显示飞船外部视图。 | 2:0.8.9 / 1:0.8.9 | ✅ 必留 | <1 MB |
| `ThroughTheEyes` | Through The Eyes | 第一人称/舱内视角增强。 | 手工 | ✅ 必留 | <1 MB |
| `Reviva` | Reviva | 在编辑器/飞行中切换多个 IVA。 | 1.0.2 | ✅ 必留 | <1 MB |

### 视觉与音效

| 目录 | 名称 | 用途 | 版本 | BDA 取舍 | 大小 |
|---|---|---|---|---|---:|
| `ReStock` | ReStock | 原版部件模型/纹理重制，不改变数值。 | 1.5.1 | ✅ 必留 | 687 MB |
| `TURD` | TURD BD Recolours | BD Armory 及相关扩展的 Textures Unlimited 换色配置。 | v1.9.2 | ✅ 必留 | 385 MB |
| `RocketSoundEnhancementDefault` | RSE Default Config | 原版发动机/轮子/分离器的 RSE 音效配置。 | 1.3.1 | ✅ 必留 | 108 MB |
| `Waterfall` | Waterfall Core | 可编程发动机尾焰/羽流核心。 | 0.11.0 | ✅ 必留 | 11 MB |
| `RestockWaterfallExpansion` | Restock Waterfall Expansion | ReStock 引擎的 Waterfall 尾焰配置。 | 3.1.1 | ✅ 必留 | 8.5 MB |
| `Firefly` | Firefly | 再入等离子体、气动加热与相关视觉/音效。 | 1.0.6 | ✅ 必留 | 1.8 MB |
| `StockWaterfallEffects` | Stock Waterfall Effects | 原版发动机的 Waterfall 尾焰配置。 | 3.1.1 | ✅ 必留 | 1.7 MB |
| `LowEndVolumetricCloudsMod` | Low End Volumetric Clouds | 低配体积云插件/着色器；按用户要求恢复。<br>注：用 CKAN 1.0.3 重新安装，包含 Plugins 与 Shaders，不是旧的手工纹理目录。 | v1.0.3 | ✅ 必留 | <1 MB |
| `RocketSoundEnhancement` | Rocket Sound Enhancement | 分层发动机音效框架。 | 0.9.13 | ✅ 必留 | <1 MB |
| `WaterfallRestock` | Waterfall Restock | ReStock 发动机的 Waterfall 配置。 | 3.1.1 | ✅ 必留 | <1 MB |
| `Chatterer` | Chatterer | 乘员无线电闲聊、SSTV 与提示音。 | 0.9.99 / 0.6.2 | ◻️ 可选 | 45 MB |
| `TextureReplacer` | TextureReplacer | 乘员/宇航服纹理替换。 | v4.5.3 | ◻️ 可选 | 30 MB |
| `ConformalDecals` | Conformal Decals | 在任意曲面贴贴花/机徽。 | 0.4.2 | ◻️ 可选 | 24 MB |
| `ZTheme` | ZTheme | 深色 UI 主题。 | v1.2.2 | ◻️ 可选 | 1.7 MB |
| `KerbalPlanetEmblems` | Kerbal Planet Emblems | 任务徽章/星球标志贴花。 | V2.3 | ◻️ 可选 | <1 MB |
| `IndicatorLights` | Indicator Lights | 部件状态指示灯（电力、资源、对接口等）。 | 1.8.3 | ◻️ 可选 | <1 MB |
| `KerbalShipEmblems2D` | Kerbal Ship Emblems 2D | 飞船 2D 徽章/贴花。 | V1.1 | ◻️ 可选 | <1 MB |
| `TU_NearFutureSpacecraft` | Recolor Collection - NF Spacecraft | Near Future Spacecraft 部件的 Textures Unlimited 换色。 | v1.4.1 | ◻️ 可选 | <1 MB |
| `TU_NearFuturePropulsion` | Recolor Collection - NF Propulsion | Near Future Propulsion 部件的 Textures Unlimited 换色。 | v1.3 | ◻️ 可选 | <1 MB |
| `HUDReplacer` | HUDReplacer | 替换/美化飞行 HUD 贴图。 | 1.4.2 | ◻️ 可选 | <1 MB |
| `SoundtrackEditorForked` | Soundtrack Editor Forked | 自定义游戏背景音乐播放列表。 | 手工 | ◻️ 可选 | <1 MB |
| `IndicatorLightsCommunityExtensions` | IndicatorLights Community Extensions | 给更多模组部件补指示灯配置。 | 1.6.2 | ◻️ 可选 | <1 MB |
| `UJModlets` | Slim Navball Markers | 更细的导航球标记。 | 1.0.2 | ◻️ 可选 | <1 MB |
| `Sigma` | Sigma Replacements | 部件外观/纹理替换。 | 手工 | ◻️ 可选 | <1 MB |

### 部件包（主题内容）

| 目录 | 名称 | 用途 | 版本 | BDA 取舍 | 大小 |
|---|---|---|---|---|---:|
| `FoxDefenseContracts` | Fox Defense Contracts | 209 个二战至现代坦克/自行火炮炮塔、机炮、炸弹与地雷部件。 | 2.2.1 | ✅ 必留 | 1.43 GB |
| `NKDR` | North Kerbin Dynamics Renewed-Extended | 核武器、重型火炮、巡航导弹与大型爆炸物。 | 0.1.2 | ✅ 必留 | 262 MB |
| `fishy_weapons_dev` | Fishy Weapons Pack | 105 个机炮、导弹、炸弹、雷达、激光与核武器部件。 | 1:0.10.0 | ✅ 必留 | 108 MB |
| `SXT` | SXTContinued | 内存占用较低的原版风格部件扩展包。 | 2:0.3.31.1 | ✅ 必留 | 96 MB |
| `ReStockPlus` | ReStock+ | 补充原版缺口的部件。 | 1.5.1 | ✅ 必留 | 65 MB |
| `BDArmoryRefurbished` | Refurbished Armory | 重制 BDArmory、Malfunc、PEW 等旧武器包，加入现代 BDA+ 兼容部件。 | v1.2.2 | ✅ 必留 | 57 MB |
| `BDArmoryExtended` | BDArmory Extended | BDA+ 半官方扩展，补充武器、雷达、部件与功能示例。 | 1:1.5.3 | ✅ 必留 | 56 MB |
| `KerbalPowers` | Kerbal Powers Armory + Core | 32 个现代舰炮、导弹、雷达与弹道武器部件；含 Kerbal Powers Core 机构与本地化。 | v1.2.3 / v1.1 | ✅ 必留 | 49 MB |
| `Mk2Expansion` | Mk2 Expansion | Mk2 机身扩展部件包。 | 2:1.9.1.4 | ✅ 必留 | 42 MB |
| `Mk3Expansion` | Mk3 Expansion | Mk3 机身扩展部件包。 | 1.6.1.4 | ✅ 必留 | 36 MB |
| `ProceduralParts` | Procedural Parts | 程序化油箱、SRB 与结构件。 | v2.8.0.0 | ✅ 必留 | 34 MB |
| `AviatorArsenal` | Aviator Arsenal Continued | 二战风格航空机炮、炸弹、火箭与挂架部件包。 | 1.5.5 | ✅ 必留 | 31 MB |
| `KerbalAdvancedDefenseReborn` | Kerbal Advanced Defense Reborn | 现代防空导弹、雷达与防空系统部件包。 | V0.4 | ✅ 必留 | 18 MB |
| `BDModularMissileParts` | BD Modular Missile Parts | BDA 自定义导弹的程序化弹体、弹头、SRB 与发射管。 | v3.0 | ✅ 必留 | 5.6 MB |
| `Fishy-Mod-Core` | Fishy Mod Core | Fishy 武器包的共享模型、贴图、音效与资源。 | 1.1.5a | ✅ 必留 | 3.6 MB |
| `FDC_Armor` | FDC Armor | Fox Defense Contracts 的装甲与伤害兼容配置，为坦克部件提供 BDA 装甲和碰撞数据。 | 2.2.1 | ✅ 必留 | 1.4 MB |
| `BilikermanIndustry` | BK Weapons Pack | Bilikerman 工业武器包，含额外机炮与弹药。 | Pre_0.1.2 | ✅ 必留 | 1.3 MB |
| `LithobrakeExplorationTechnologies` | Lithobrake Exploration Technologies | 原版风格着陆腿、梯子、居住舱等探索部件。 | 0.6.2 | ◻️ 可选 | 8.5 MB |

### 空间站、基地与发射场

| 目录 | 名称 | 用途 | 版本 | BDA 取舍 | 大小 |
|---|---|---|---|---|---:|
| `TundraSpaceCenter` | Tundra's Space Center | 新一代发射台与航天中心建筑；KSC Extended 的配套建筑。 | 2.0.2 | ✅ 必留 | 75 MB |
| `OSSNTR` | Omega's Stockalike Structures: No Textures Required | 原版风格机场、跑道、发射场静态建筑；KSC Extended 的配套建筑。 | 0.0.12 | ✅ 必留 | 34 MB |
| `KerbalKonstructs` | Kerbal Konstructs | 静态建筑/发射场框架，KSC Extended 的前置。 | v1.12.3.0 | ✅ 必留 | 9.9 MB |
| `KSCExtended` | KSC Extended | 扩建肯尼迪航天中心，增加发射台与建筑。 | 3.0.3 | ✅ 必留 | <1 MB |

### 第三方本地化

| 目录 | 名称 | 用途 | 版本 | BDA 取舍 | 大小 |
|---|---|---|---|---|---:|
| `0000Tinygrox_CNPatches` | Chinese Mod Patches | 第三方简体中文补丁合集，覆盖大量部件与界面。 | v1.8.5 | ✅ 必留 | 18 MB |

### 我们的自制补丁/插件

| 目录 | 名称 | 用途 | 版本 | BDA 取舍 | 大小 |
|---|---|---|---|---|---:|
| `KISA_Flags` | KISA Flags | 自制：KISA 机构任务旗与 EVE 任务特别版。 | 手工 | ✅ 必留 | 5.4 MB |
| `KISA_FlagsAgency` | KISA Flags Agency | 自制：KISA 机构徽章与方形贴花。 | 手工 | ✅ 必留 | 2.9 MB |
| `ZZZ_BDA_CN` | BDA+ 中文补充 | 自制：补 BDA+ 1.13.x 官方 zh-cn 尚未覆盖的 186 个 UI 键。 | 手工 | ✅ 必留 | <1 MB |
| `KISA_Fixes` | KISA Fixes | 自制：生涯存档用的杂项修复（USI 资源、CapCom、VAB 分类、Endurance 移除等）。 | 手工 | ✅ 必留 | <1 MB |
| `RealChute_CN` | RealChute 中文补丁 | 自制：RealChute 界面与预设的简体中文 Harmony 插件。 | 手工 | ✅ 必留 | <1 MB |
| `DSH_Plugins` | Engine Thrust Reverser | 自制插件：为喷气发动机提供反推/换向控制。 | 手工 | ✅ 必留 | <1 MB |

### 原版与官方 DLC

| 目录 | 名称 | 用途 | 版本 | BDA 取舍 | 大小 |
|---|---|---|---|---|---:|
| `Squad` | Squad（原版） | 游戏原版部件、资源与场景。 | 手工 | ✅ 必留 | 1.15 GB |
| `SquadExpansion` | Squad Expansion（官方 DLC） | Making History 与 Breaking Ground 官方 DLC 内容。 | 手工 | ✅ 必留 | 1.05 GB |

### 其它

| 目录 | 名称 | 用途 | 版本 | BDA 取舍 | 大小 |
|---|---|---|---|---|---:|
| `Custom` | Custom（用户目录） | KSP 的用户自定义目录，目前只有空的 Flags 子目录。 | 手工 | ✅ 必留 | <1 MB |

## 说明

- 体积按目录内所有文件求和；“<1 MB”并不代表没有文件。
- 版本来自 CKAN 注册表；手工安装的包没有 CKAN 版本号时标为“手工”。
- `Squad` 与 `SquadExpansion` 是原版与官方 DLC，不算第三方模组，但保留在表中以便核对。
- `ScattererAtmosphereCache` 是自动生成的缓存；删除后首次进入游戏会重建。
- 机器可读版本见 [`mods/installed-modules.csv`](mods/installed-modules.csv) 与
  [`mods/gamedata-inventory.csv`](mods/gamedata-inventory.csv)。
