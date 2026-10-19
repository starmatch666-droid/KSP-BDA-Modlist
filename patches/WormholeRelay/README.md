# WormholeRelay（虫洞通信中继）

让**虫洞两端的"中继卫星"之间建立通信链路**——一侧一个中继，就够把两边的通信网连成一张。

KSP 原版 CommNet 只按"直线距离 + 天线功率"判定连通，没有"隧道"概念，所以跨虫洞（271.8 Tm）
永远是断的。本插件在 CommNet 建网时挂钩 `CommNetwork.TryConnect`：当两个通信节点分别位于
配置里两个虫洞天体的 SOI（引力范围）内、且都具备中继天线时，把这次判定的距离当成 1000 m，
于是距离与信号强度都由 CommNet 自己算，链路自然成立。

## 用法

1. 把 `GameData/WormholeRelay/` 整个放进游戏（已装好）。
2. 在一侧虫洞的 SOI 里放一个**带中继天线**的飞船（例如你那颗 224Gm 级中继卫星，
   天线是 `RTLongDish2` / Reflectron KR-14，`antennaType = RELAY`）。
3. 另一侧虫洞的 SOI 里同样放一个中继。
4. 两边的网络就会连起来：Kcalbeloh 系里的飞船 → 当地中继 → 虫洞另一头的中继 → Kerbin。

## 怎么确认它在工作

- `KSP.log` 里应出现：`[WormholeRelay] Harmony 补丁已应用；sideA=WH3141A sideB=WH3141B`
- 进出虫洞 SOI 时会打印：`[WormholeRelay] 当前虫洞侧中继数: N，已请求重建通信网络`
- 地图视角的通信线会直接从一侧的中继连到另一侧的中继。

## 已知限制

- 只认"中继天线"（`RELAY` 型）。只有直连天线的飞船不算中继（按你的要求）。
- 两端之间如果刚好被某个天体挡住（连线和太阳相切那种），原版遮挡判定仍可能拦下链路；
  真遇到的话告诉我，我再加一层"绕开遮挡"的补丁。
- 需要 Harmony（你已装 `000_Harmony`）。

源码与构建脚本：工作目录 `wormhole-relay/`（`WormholeRelay.cs` + `build.ps1`）。
