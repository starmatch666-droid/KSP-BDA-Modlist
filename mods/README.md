# 机器可读清单

| 文件 | 说明 |
|---|---|
| `installed-modules.csv` | CKAN 注册表里的 251 个模块，含标识、名称、版本、作者、英文摘要、安装时间 |
| `gamedata-inventory.csv` | `GameData` 222 个顶层目录，含体积、CKAN 标识、BDA 取舍与中文用途 |
| `modlist-current.ckan` | 用 `ckan list --export ckan` 导出的当前 CKAN 清单，可在 CKAN GUI/CLI 中导入 |

## 注意

- `.ckan` 只包含 CKAN 管理的模块；手工安装的 `Endurance`、`OPT`、`SXT`、
  `TundraSpaceCenter`、`KeridianDynamics` 等不在其中，需参照 `gamedata-inventory.csv`。
- 本目录是**删除前**的快照。删除完成后，应重新运行 `ckan list --export ckan`
  生成 `modlist-bda.ckan`，不要把旧清单当成 BDA 最终档案。
- `installed-modules.csv` 的摘要保留英文原文，便于和 CKAN/原作者页面核对；
  中文用途与取舍在 `gamedata-inventory.csv` 和 `MODLIST.md`。
