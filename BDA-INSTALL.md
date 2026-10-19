# BDA+ 单机安装记录

当前环境：KSP 1.12.5，136 个 GameData 顶层目录，145 个 CKAN 模块。

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

- `GameData\ZZZ_BDA_CN`：补齐 186 个 UI 键、VABOrganizer 子分类、
  硬编码部件文本（Mk1 Open Cockpit Type 2、BD 装甲板等）
- `BDA_CN_Categories.dll`：编辑器顶部分类按钮显示中文
- `BDA_CN_Info.dll`：武器/导弹 `GetInfo` 文本中文

FAR 自带 `zh-cn`，残留的 25 个英文 UI 字符串也已补译。

## 可以加装的 BDA 部件包

取消联机后，不再需要让所有客户端保持同一套 BDA 版本，可以按单机喜好加装。
建议先只装一两个，确认能进 VAB/SPH 再继续。

| CKAN 名称 | 内容 | 注意事项 |
|---|---|---|
| `BDArmoryExtended` | BDA+ 半官方扩展；补充武器、雷达、部件与功能示例 | 稳定版 1.5.3，依赖 BDA+ |
| `BDModularMissileParts` | 模块化导弹部件 | BDA+ 推荐扩展 |
| `AviatorArsenal` | 航空武器/挂架部件包 | 先确认 1.12.5 兼容 |
| `KerbalAdvancedDefenseReborn` | 更真实的防空武器、雷达与导弹 | 偏现代防空主题 |
| `NorthKerbinDynamicRenewed` | 核武器与大型爆炸 | 主题很强，按需 |
| `BDAUITeamIcons` | BDA 队伍/目标图标 UI | 纯 UI |
| `TURD-BDArmory` / `TURD-BDAssociated` | 坦克/地面载具 BDA 部件 | 地面战玩法 |
| `BKWeaponsPack` / `RefurbishedArmory` | 额外武器包 | 兼容性需逐个确认 |

不要一次把所有包都装上：BDA+ 本体已经有 60 多个部件目录，扩展包主要用于
特定玩法；出问题时也更难定位。

## 装扩展后的检查

1. 启动 KSP，`KSP.log` 里不应有 BDA 的 `TypeLoadException`。
2. 进 VAB/SPH，确认 BDA 分类和新增部件都出现。
3. 检查武器管理器能选中新武器、弹药匹配。
4. 如果某扩展导致 BDA 窗口或分类异常，先只移除最后装的那个。
