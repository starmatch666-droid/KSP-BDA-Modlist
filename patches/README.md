# 我们自己的补丁与插件

这里只放**我们自己写的**内容：ModuleManager 配置、汉化词条、Harmony 插件与
小型 KSP 插件。第三方模组本体不随仓库分发；需要时通过 CKAN 或原作者发布页安装。

每个目录都可以直接放进 `Kerbal Space Program\GameData\`。目录名前的 `ZZZ_`
只是为了让补丁在 ModuleManager 中最后执行，不是必需前缀。

## 一览

| 目录 | 类型 | 作用 | 依赖 | BDA 档案中的处理 |
|---|---|---|---|---|
| `KISA_Fixes` | MM 配置 + 小插件 | KISA 生涯存档的杂项修复：USI 资源、CapCom、VAB 分类、Endurance 零件移除等 | 视具体文件而定；多数只对已装模组生效 | **保留**（其中针对已删模组的文件会自动失效） |
| `KISA_Flags` | 旗子 PNG | KISA 机构任务旗、EVE 任务特别版 | 无 | **保留** |
| `KISA_FlagsAgency` | 机构徽章 PNG | KISA 机构徽章与方形贴花 | 无 | **保留** |
| `RealChute_CN` | Harmony 插件 + 源码 | RealChute 界面/预设简体中文 | RealChute、Harmony | **保留** |
| `ResupplyNetwork` | 独立插件 | 付费定时补给任意飞船资源 | Harmony、ToolbarController | **保留**；源码另见 GitHub `starmatch666-droid/ResupplyNetwork` |
| `DSH_Plugins` | 独立插件 | 喷气发动机反推/换向控制 | 无额外依赖 | **保留**（适合 BDA 喷气机） |
| `Endurance_适配` | MM 配置 | Endurance 漫游者号电力、热控、USI/Cryo 兼容 | Endurance、USI-LS、CryoTanks | **随 Endurance 删除** |
| `Endurance_CN` | MM 配置 | Endurance 部件与 PAW 简体中文 | Endurance | **随 Endurance 删除** |
| `MLP_CN` | MM 配置 | Modular Launch Pads 简体中文 | ModularLaunchPads | **随 MLP 删除** |
| `ZZZ_GC_CN` | MM 配置 + Harmony 插件 | GroundConstruction 部件与界面简体中文 | GroundConstruction、Harmony | **随 GroundConstruction 删除** |
| `ZZZ_USI_CN` | MM 配置 | Konstruction / USI-LS / Akita 简体中文 | USI 系列 | **随 USI 删除** |
| `ZZZ_KONSTRUCTION_INDEPENDENCE` | MM 配置 | 给 Konstruction KS-500 船坞增加本地资源缓冲与合成 | Konstruction | **随 USI 删除** |
| `WormholeRelay` | Harmony 插件 + 源码 | 让 Kcalbeloh 虫洞两端的中继卫星连通 CommNet | Kcalbeloh、Harmony | **随 Kcalbeloh 删除** |
| `ZZZ_BDA_CN` | 本地化 cfg + Harmony 插件 | 补 186 个 UI 键、VABOrganizer 子分类和 BDA 顶部分类按钮的中文 | BDArmory Plus、Harmony | **保留** |
| `ZZZ_FAR_CN` | 本地化 cfg | 修正 FAR 自带 zh-cn 中残留的 25 个英文 UI 字符串 | FAR Continued | **保留** |
| `optional-not-installed/ArcjetXeArPatch-2026-10-15` | MM 配置 | 电弧喷射发动机氙/氩燃料补丁；当前未安装 | Near Future Propulsion 相关部件 | 备用，未进入当前档案 |

## 安装顺序

1. 先装模组本体与前置（Harmony、ModuleManager、B9PartSwitch 等）。
2. 把上表对应的补丁目录整体复制到 `GameData\`。
3. 启动游戏，检查 `KSP.log` 里是否有 ModuleManager 的 `Skipping a patch subnode`
   或 Harmony 的 `patch failed`。
4. 补丁不修改模组原文件；卸载时删除对应目录即可。

## 说明

- `KISA_Fixes` 里的 `zz_RemoveEnduranceShip.cfg` 会在 Endurance 仍安装时移除
  永恒号船体/登陆舱零件；如果 Endurance 已经删除，这个文件不会造成额外影响。
- `KISA_Fixes\Mk33LifeSupport.cfg`、`AgroponicsFertilizer.cfg`、`MulchRename.cfg`
  分别针对 Mk-33、USI-LS 等模组；对应模组删除后，这些配置不会被任何部件匹配。
- `DSH_Plugins` 目前只有编译好的 DLL，源码暂未找到；如果后续要维护，建议补一份
  `.cs` 与构建脚本。
- 所有补丁按“原样提供”分发；第三方模组本体与其美术资源仍遵循各自许可证。
