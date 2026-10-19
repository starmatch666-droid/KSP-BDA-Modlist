# 多人联机（Luna Multiplayer）

> **已取消（2026-10-19）。** LMP 客户端已从 GameData 移除，0.29.2/0.30.0
> 服务端已移到 `C:\Users\STARM\Documents\KSP-BDA-Work\_disabled_multiplayer\`。
> 当前是标准单机 BDA+；以下内容仅作历史记录。

## 已安装

| 组件 | 版本 | 位置 |
|---|---|---|
| LMP 客户端 | 已移除 | 历史版本 0.29.2 |
| LMP 服务端 | 已归档 | `C:\Users\STARM\Documents\KSP-BDA-Work\_disabled_multiplayer\LMP-Server-0.29.2\LMPServer` |
| BDA+ LMP 分支 | 1.13.1.0 | `GameData\BDArmory` |
| Physics Range Extender | 1.21.0 | `GameData\PhysicsRangeExtender` |
| FAR Continued | 0.16.1.2 | `GameData\FerramAerospaceResearch` |

服务端要求 **.NET 6 Runtime**；本机已安装 `Microsoft.NETCore.App 6.0.33`。

## 启动服务器

双击：

`C:\Users\STARM\Documents\KSP-BDA-Work\LMP-Server-0.29.2\LMPServer\StartLunaServer.bat`

或在 PowerShell 里：

```powershell
cd "C:\Users\STARM\Documents\KSP-BDA-Work\LMP-Server-0.29.2\LMPServer"
.\StartLunaServer.bat
```

看到 `All systems up and running. Поехали!` 就是启动成功。服务器监听 **UDP 8800**；
网站/管理端口是 **TCP 8900**。UPnP 已开启，日志里出现 `UPnP active` 表示端口映射成功。

停止服务器请用 `Ctrl+C`，让 LMP 正常保存宇宙备份。

## 客户端连接

1. 启动 KSP。
2. 主菜单点 **Luna Multiplayer** 按钮。
3. 从服务器列表选择 `BDA Combat Server`，或直接连接：

```text
127.0.0.1:8800
```

外网朋友连接时，用服务器的公网 IP + 8800；如果路由器/防火墙没放行，优先依赖
UPnP 或手动转发 UDP 8800。服务器已注册到 LMP 主服务器，通常可以直接在列表里搜到。

## 服务器配置

配置文件在：

`C:\Users\STARM\Documents\KSP-BDA-Work\LMP-Server-0.29.2\LMPServer\Config\`

已改的关键项：

| 文件 | 项 | 值 | 原因 |
|---|---|---|---|
| `GeneralSettings.xml` | `ServerName` | `BDA Combat Server` | 服务器列表显示名 |
| `GeneralSettings.xml` | `Description` | `KSP 1.12.5 / BDArmory Plus LMP edition` | 说明 |
| `GeneralSettings.xml` | `ModControl` | `false` | 允许 BDA 自定义部件；否则默认白名单只放行原版 |
| `GeneralSettings.xml` | `MaxVesselParts` | `500` | BDA 战斗机制造部件较多 |
| `GeneralSettings.xml` | `GameMode` | `Sandbox` | BDA 空战不需要生涯进度 |
| `ConnectionSettings.xml` | `Port` | `8800` | 默认端口 |
| `ConnectionSettings.xml` | `Upnp` | `true` | 自动开端口 |

### 设置密码

如果不想让陌生人进服，在 `GeneralSettings.xml` 里填：

```xml
<Password>你的密码</Password>
```

`AdminPassword` 也建议设置，否则别人可以在游戏里执行管理命令。

## 联机规则

- **所有玩家必须使用完全相同的 `GameData`**，尤其是 BDA 版本和 BDA 扩展包。
- `ModControl=false` 是为了让 BDA 部件能进服；代价是服务器不会帮你检查客户端是否缺件。
- BDA-MP-Renewed 是 WIP：已知子弹不渲染，但伤害/击杀逻辑正常。
- 双方都要装 `BDArmory`、`LunaMultiplayer`、`PhysicsRangeExtender` 和同版本 FAR。
- FAR 已替换原版气动；所有客户端必须使用同一 FAR 版本，否则气动表现会不一致。

## 为什么锁定 0.29.2

BDA-MP-Renewed 的 `BDArmory.dll` 引用的是 `LmpClient 0.29.2.0`。使用
LMP 0.30.0-Draft 会在 `BDArmory.Multiplayer.LunaMultiplayerSystem.Update()`
每帧抛出 `TypeLoadException`，并导致 BDA 武器逻辑无法正常更新。客户端和
服务端都必须使用 0.29.2。
- 当前服务器密码为空，公网开服前建议先设密码。

## 恢复到单机 BDA+

如果只想单机玩标准 BDA+，把 `GameData\BDArmory` 换回 CKAN 的
`BDArmoryForRunwayProject` 即可；两者都提供 `BDArmory`，不能同时安装。
