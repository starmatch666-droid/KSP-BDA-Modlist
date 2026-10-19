# BDArmory Plus 简体中文补充词条

BDA+ 1.13.x 自带 `zh-cn` 词条，但新增的 AI 设置、轰炸、装甲工具、横幅等
约 186 个 UI 键没有中文。这个目录只补这些缺失键，不修改 BDA 原文件。

另外包含：

- `Patches/VABOrganizer_zh.cfg`：BDA 的 VABOrganizer 子分类中文
- `Patches/PartText_zh.cfg`：Mk1 Open Cockpit Type 2、BD 装甲板等硬编码部件文本
- `Patches/NKDR_zh.cfg`：North Kerbin Dynamics Renewed-Extended 的 57 个硬编码部件
- `Patches/BDModular_zh.cfg`：BD Modular Missile Parts 的 4 个硬编码部件
- `Patches/Fishy_zh.cfg`：Fishy Weapons Pack 的 104 个硬编码部件
- `Patches/FoxDefense_zh.cfg`：Fox Defense Contracts 的 209 个硬编码部件
- `Localization/UI/Addons_zh.cfg`：Refurbished Armory / BDArmoryExtended 缺失词条
- `Localization/UI/KerbalPowers_zh.cfg`：Kerbal Powers Armory 的 146 个词条
- `Localization/UI/KerbalPowers_Agencies_zh.cfg`：Kerbal Powers 机构与制造商名称
- `Plugins/BDA_CN_Categories.dll`：把 BDA 编辑器顶部的分类按钮显示名
  （Guns/Gun turrets/Missiles 等）换成中文，但不改变过滤用的英文键
- `Plugins/BDA_CN_Info.dll`：替换武器/导弹部件信息里硬编码的
  `Rounds Per Minute`、`Estimated Penetration`、`Air detonation` 等英文

## 安装

整个 `ZZZ_BDA_CN` 放进 `GameData\`，游戏语言保持 `zh-cn`。

## 卸载

删除 `GameData\ZZZ_BDA_CN` 即可，不会影响 BDA 本体或存档。

## 说明

- 只补 UI 词条；BDA 部件名与描述由 BDA 自带的 `localization-zh-cn.cfg` 覆盖。
- 如果 BDA 更新后新增了更多键，重新运行
  `tools/build_bda_cn_patch.py` 检查并补充。
- BDA 的少数字符串硬编码在 DLL 里，词条文件覆盖不到；这类文本需要改源码重编译。
