# BDA+ 与多人联机安装记录

当前环境：KSP 1.12.5，138 个 GameData 顶层目录，146 个 CKAN 模块。
BDA 与联机部分**已经安装**。

## 为什么不是直接装 CKAN 的 BDArmoryForRunwayProject

CKAN 里的 `BDArmoryForRunwayProject` 就是 BDArmory Plus（BDA+），版本
`2:v1.13.1.0`，支持 KSP 1.9–1.12.999。但标准 BDA+ 不能和 Luna Multiplayer
同步武器；LMP 官方 wiki 明确写了 BDA/BDAc/BDA+ 不工作。

因此这里装的是社区分支 **BDA-MP-Renewed**：

- 基于 BDA+ 1.13.1.0
- 为最新 LMP 改写，加入 `LmpClient`/`LmpCommon` 引用
- 支持枪炮、导弹、雷达、隐身等 BDA+ 功能在多人中同步
- 版本 `v0.1`，属于 WIP；作者的 TODO 里记录“子弹不渲染，但仍能正常命中/击杀”

来源：<https://github.com/LVCKSTRiKE/BDA-MP-Renewed/releases/tag/BDA-MP-R_v0.1>

## 已安装组件

| 组件 | 版本 | 安装方式 |
|---|---|---|
| BDArmory Plus LMP edition | 1.13.1.0 | GitHub release，手动放进 `GameData\BDArmory` |
| Luna Multiplayer Client | 0.29.2 | CKAN |
| Physics Range Extender | 1.21.0 | CKAN |
| ModuleManager / Harmony | 已有 | 之前安装 |

`BDArmory` 的 DLL 里可以看到 `LmpClient`、`LmpCommon`、`LunaMultiplayerSystem`
等引用，确认是联机分支而不是普通 BDA+。

## 中文

BDA+ 自带 `localization-zh-cn.cfg` 和 `Localization/UI/zh-cn.cfg`，部件名/描述
以及大部分窗口已经是中文。1.13.x 新增的 AI 设置、轰炸、装甲工具等 186 个 UI 键
官方没有翻译，已由 `GameData\ZZZ_BDA_CN` 补齐。

如果仍有英文，通常是 BDA 的 DLL 里硬编码的字符串，cfg 词条覆盖不到；那种需要改
源码重编译。

## FAR 气动

已安装 **Ferram Aerospace Research Continued 0.16.1.2**：

- 替代原版部件气动，包含跨声速/高超声速、气动稳定性与失速模型
- 依赖已有：ModuleManager、ModularFlightIntegrator、TweakScale-Redist、KSPBurst
- 与 `WindTunnel` 冲突，CKAN 已移除 WindTunnel；FAR 自带气动分析
- BDA+ 对 FAR 有兼容处理：导弹/炸弹离机后改用 BDA 气动，程序化机翼的 HP/装甲计算也识别 FAR

`AtmosphereAutopilot` 仍保留，但它的飞控参数需要按 FAR 重新调；`CorrectCoL` 也保留，
不过 FAR 自己的稳定性分析更权威。

## 启动顺序

1. 先启动 LMP 服务器，见 [`MULTIPLAYER.md`](MULTIPLAYER.md)。
2. 启动 KSP。
3. 在主菜单点 Luna Multiplayer 按钮，连接服务器。
4. 进入 SPH/VAB 造带 BDA 武器/雷达的飞机，发射后打开 BDA 武器管理器。

单机测试时也可以先不启动服务器，直接在 KSP 里玩 BDA；但联机战斗必须让服务器
和所有客户端使用同一套 `GameData`。

## 可选扩展

先确认 BDA 本体和联机稳定，再考虑：

| 包 | 用途 | 注意 |
|---|---|---|
| `BDModularMissileParts` | 模块化导弹部件 | BDA 官方推荐 |
| `BDArmoryExtended` | 额外武器/部件 | 所有联机玩家都必须装同一版本 |
| `NorthKerbinDynamicRenewed` | 核武器/大型爆炸 | 主题很强，按需 |
| `KerbalAdvancedDefenseReborn` | 防空/雷达扩展 | 先看版本兼容 |

联机时**不要**只在一端装扩展包；LMP 会因为缺部件报错。

## 装完后的检查

1. 启动游戏，确认 `KSP.log` 里没有 `BDArmory` 的 `Exception`。
2. 进 VAB/SPH，确认有 BDA 的武器分类。
3. 发射一架带武器/雷达的飞机，确认右键菜单和 BDA 窗口能打开。
4. 连接 LMP 服务器，确认服务器列表/聊天可见。
5. 如果掉帧，优先降低 BDA 的物理范围/AI 数量；环境美化已经移除。
6. FAR 已安装；它会替换原版气动，`WindTunnel` 与其冲突已被移除。
