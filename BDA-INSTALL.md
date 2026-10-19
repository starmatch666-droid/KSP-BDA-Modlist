# BDA+ 单机安装记录

当前环境：KSP 1.12.5，155 个 GameData 顶层目录，165 个 CKAN 模块，8.97 GB。

**多人联机已取消。** LMP 客户端已移除，服务端移到
`C:\Users\STARM\Documents\KSP-BDA-Work\_disabled_multiplayer\`；
当前安装的是标准单机 BDA+。

## 当前 BDA

| 组件 | 版本 | 安装方式 |
|---|---|---|
| BDArmory Plus | 1.13.1.0 | CKAN `BDArmoryForRunwayProject` |
| Physics Range Extender | 1.21.0 | CKAN |
| FAR Continued | 0.16.1.2 | CKAN |

BDA+ 依赖 `ModuleManager` 和 `PhysicsRangeExtender`；标准单机版不再引用
`LmpClient`，因此不会再出现之前每帧 `TypeLoadException` 的问题。

## 中文

- `GameData\ZZZ_BDA_CN`：补齐 BDA+ 的 UI 键、VABOrganizer 子分类、
  硬编码部件文本（Mk1 Open Cockpit Type 2、BD 装甲板等）
- `BDA_CN_Categories.dll`：编辑器顶部分类按钮显示中文
- `BDA_CN_Info.dll`：武器/导弹 `GetInfo` 文本中文
- `KerbalPowers_zh.cfg`：Kerbal Powers Armory 146 个本地化键
- `Fishy_zh.cfg`：Fishy Weapons Pack 104 个部件标题/说明
- `FoxDefense_zh.cfg`：Fox Defense Contracts 209 个部件标题/说明
- `KerbalPowers_Agencies_zh.cfg`：Kerbal Powers 机构与制造商名称
- `Bullets_zh.cfg`：Fox / Kerbal Powers 的 65 种弹药类型显示名
- `FoxAmmo_zh.cfg`：Fox 的五种弹药资源名

FAR 自带 `zh-cn`，残留的 25 个英文 UI 字符串也已补译。

ModuleManager 最近一次完整启动：**38276 个补丁、0 错误、1 个 TURD 换色警告**；
`BDA_CN_Info` 成功替换 23 个武器/导弹信息方法。

## 已安装的 BDA 部件包

取消联机后，不再需要让所有客户端保持同一套 BDA 版本，已按要求安装以下扩展。

| CKAN 名称 | 内容 | 状态 |
|---|---|---|
| `BDArmoryExtended` | BDA+ 半官方扩展；补充武器、雷达、部件与功能示例 | 已安装 |
| `BDModularMissileParts` | 模块化导弹部件 | 已安装 |
| `AviatorArsenal` | 二战航空武器/挂架部件包 | 已安装 |
| `KerbalAdvancedDefenseReborn` | 现代防空武器、雷达与导弹 | 已安装 |
| `NorthKerbinDynamicsRenewedExtended` | 核武器、重型火炮、巡航导弹 | 已安装（BDA+ 兼容版） |
| `BDAUITeamIcons` | BDA 队伍/目标图标 UI | 已移除：引用旧 BDA 1.3.6.4，BDA+ 1.13 加载失败 |
| `TURD-BDArmory` / `TURD-BDAssociated` | BD 部件 Textures Unlimited 换色 | 已安装 |
| `BKWeaponsPack` / `RefurbishedArmory` | 额外武器与重制旧武器包 | 已安装 |
| `KerbalPowersArmory` / `KerbalPowersCore` | 现代舰炮、导弹、雷达、弹道武器 | 已安装；明确依赖 BDA+ |
| `FishyAntiMissileSpam` / `Fishy-Mod-Core` | 机炮、导弹、炸弹、雷达、激光与核武器 | 已安装 |
| `FoxDefenseContracts` / `FDC_Armor` | 二战至现代坦克炮塔、机炮、炸弹、地雷与装甲兼容 | 已安装 |
| `BDAnimationModules` | 旧式部件动画模块库 | 已安装 |

注意：旧的 `NorthKerbinDynamicRenewed` 依赖 `BDArmoryContinued`，不能和标准
BDA+ 共存；已改用 `NorthKerbinDynamicsRenewedExtended`。

以上为当前可用的 BDA+ 兼容部件包全集。`BDArmoryContinued`、
`NorthKerbinDynamicRenewed` 与 BDA+ 冲突，`BDArmoryMultiplayer` 随联机取消，
`BDAUITeamIcons` 引用旧 BDA 1.3.6.4 的 `MissileFire`，均不安装。

已知非致命日志：Aviator Arsenal、NKDR 与 Near Future Aeronautics 的少量旧
PartModule（`BDACategoryModule`、`BDALookConstraintUp`、`AnimatedIntake`）
在 BDA+ 1.13 中不存在，部件仍会加载；这些是旧包残留，不影响新装的三个部件包。

## 军事合同包

已安装 **KomUniMun Contractual Warfare 1.0.0**（CKAN `KomUniMunCW`），
位于 `GameData\ContractPacks\KUM`。它明确依赖 BDA+ 与 Contract Configurator，
在 Kerbin、月球和轨道提供防空、对地、反舰、太空拦截与武器测试合同。
自带 `zh-cn`；其对地、反舰、太空和测试合同残留的 99 个英文键已由
`ZZZ_BDA_CN/Localization/UI/KomUniMun_zh.cfg` 补全。

原包的普通战斗合同 `science = 0`，只有测试合同给 0.5–2.5 科研点。
`ZZZ_BDA_CN/Patches/KUM_MilitaryScience.cfg` 已给全部 60 个合同追加：

```text
rewardScience = 原科研 + 合同资金 / 300 + 5
```

例如 5500 资金合同约给 23.3 科研点，9000 资金约给 35，14000 资金约给 51.7；
测试合同会在此之上再加原本的 0.5–2.5。想更快把 `300` 改成 `200`，
想更慢改成 `500`。

## BDA 科技树：四条大方向 + 36 个节点

`ZZZ_BDA_CN/Patches/BDA_TechTreeNodes.cfg` 在科技树右侧新建了一条 BDA
专属支线；`BDA_TechTree.cfg` 把 724 个 BDA/扩展部件分配到 36 个节点。
不再借用 Community Tech Tree 的少数大节点：

| 大方向 | 子节点 | 部件数 |
|---|---|---:|
| 军械基础 | 基础弹药、挂架与工程部件 | 51 |
| 武器 | 早期枪炮 40、二战机炮 90、现代机炮 200、舰炮/近防 400、火箭/无制导炸弹 60、早期制导炸弹 200、现代精确炸弹 500、战略常规炸弹 1200、早期导弹 150、冷战导弹 350、现代导弹 600、先进导弹 1000、核武 1500、轨道炮 1500、定向能 1800、实验武器 2000 | 330 |
| 装甲与载具 | 基础装甲 45、反应/复合装甲 200、二战坦克 120、冷战坦克 300、现代坦克 600 | 207 |
| 电子系统 | 基础雷达 150、高级雷达 400、AESA 1000、瞄准与数据链 200、对抗措施 120、电子战 600、AI 与飞控 1000 | 77 |
| 平台与发射 | 喷气动力 120、挂架/发射器 60、模块化导弹 400 | 59 |

44 个原本标记为 `Unresearcheable` 的隐藏/遗留部件保持原样。
这次调整会改变已有存档的解锁状态；建议开新档，或先备份存档再进 R&D 查看。
完整的 724 条部件分档记录见
`data/bda-tech-assignment.tsv`，生成脚本为
`tools/build_bda_branch_techtree.py`。

旧的 **Defense Combat Advisors (DCA)** 依赖 `BDArmoryContinued`，与 BDA+ 冲突，
因此没有安装。

## 装扩展后的检查

1. 启动 KSP，`KSP.log` 里不应有 BDA 的 `TypeLoadException`。
2. 进 VAB/SPH，确认 BDA 分类和新增部件都出现。
3. 检查武器管理器能选中新武器、弹药匹配。
4. 如果某扩展导致 BDA 窗口或分类异常，先只移除最后装的那个。
