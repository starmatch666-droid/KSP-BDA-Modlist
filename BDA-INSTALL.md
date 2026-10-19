# 安装 BDArmory Continued

当前环境已经清到 170 个顶层目录、195 个 CKAN 模块，BDA 本体尚未安装。

## 版本选择

CKAN 里唯一支持 KSP 1.12.x 的 BDArmory Continued 是：

| 版本 | 支持 KSP | 状态 |
|---|---|---|
| `1:v1.3.5_beta` | 1.9.0–1.12.999 | testing |
| `1:v1.3.4` | 1.9.0–1.9.999 | stable，但不支持 1.12 |

所以 1.12.5 只能装 `1:v1.3.5_beta`。它自带 `zh-cn` 词条，依赖只有
`ModuleManager` 和 `PhysicsRangeExtender`。

## 命令

```powershell
cd "C:\Program Files (x86)\Steam\steamapps\common\Kerbal Space Program"
.\ckan1.36.exe install --headless BDArmoryContinued
```

如果 CKAN 没有自动选中 1.12 兼容版本，显式指定：

```powershell
.\ckan1.36.exe install --headless BDArmoryContinued=1:v1.3.5_beta
```

装完确认：

```powershell
.\ckan1.36.exe list | Select-String "BDArmory|PhysicsRange"
```

## 可选扩展

先只装 BDA 本体，确认游戏能进、能发射、能打开 BDA 窗口，再考虑：

| 包 | 用途 | 注意 |
|---|---|---|
| `BDModularMissileParts` | 模块化导弹部件 | BDA 官方推荐 |
| `BDArmoryExtended` | 额外武器/部件 | 先看是否支持 1.12 |
| `NorthKerbinDynamicRenewed` | 核武器/大型爆炸 | 主题很强，按需 |
| `KerbalAdvancedDefenseReborn` | 防空/雷达扩展 | 先看版本兼容 |

不要一次性把所有 BDA 扩展都装上；BDA 本身部件已经很多，扩展包主要用于特定玩法。

## 装完后的检查

1. 启动游戏，确认 `KSP.log` 里没有 `BDArmory` 的 `Exception`。
2. 进 VAB/SPH，确认有 BDA 的武器分类。
3. 发射一架带武器/雷达的飞机，确认右键菜单和 BDA 窗口能打开。
4. 如果掉帧，优先考虑关闭 Parallax（约 3.4 GB 纹理）或降低 BDA 的物理范围/AI 数量。
