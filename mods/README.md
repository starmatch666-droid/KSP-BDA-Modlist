# 机器可读清单

| 文件 | 说明 |
|---|---|
| `installed-modules-before.csv` | 清理前 CKAN 注册表里的 251 个模块 |
| `installed-modules.csv` | 当前 CKAN 注册表里的 158 个模块 |
| `gamedata-inventory-before.csv` | 清理前 `GameData` 222 个顶层目录 |
| `gamedata-inventory.csv` | 当前 `GameData` 148 个顶层目录 |
| `modlist-before.ckan` | 清理前的 CKAN 导出清单 |
| `modlist-bda.ckan` | 清理后的 CKAN 导出清单（BDA 安装前） |
| `modlist-pre-bda-20261017.ckan` | 要恢复的 BDA 前完整状态：201 项，含精确版本 |

## 注意

- `.ckan` 只包含 CKAN 管理的模块；手工安装的 `Endurance`、`OPT`、`SXT`、
  `TundraSpaceCenter`、`KeridianDynamics` 等不在其中，需参照 CSV。
- `modlist-before.ckan` 是删除前快照；`modlist-bda.ckan` 是删除后、安装 BDA 前
  的当前状态。不要把旧清单当成 BDA 最终档案。
- 恢复“BDA 前一大堆模组”时使用 `modlist-pre-bda-20261017.ckan`；
  GitHub 原始文件 SHA256 为
  `09626AFFD6E2B0742D50F0857CFC24917CC4626494C07D07016EACB6F985060E`。
- `installed-modules.csv` 的摘要保留英文原文，便于和 CKAN/原作者页面核对；
  中文用途与取舍在 `gamedata-inventory.csv` 和 `MODLIST.md`。
