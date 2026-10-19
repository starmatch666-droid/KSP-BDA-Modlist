# BDArmory Plus 简体中文补充词条

BDA+ 1.13.x 自带 `zh-cn` 词条，但新增的 AI 设置、轰炸、装甲工具、横幅等
约 186 个 UI 键没有中文。这个目录只补这些缺失键，不修改 BDA 原文件。

另外包含：

- `Patches/VABOrganizer_zh.cfg`：BDA 的 VABOrganizer 子分类中文
- `Plugins/BDA_CN_Categories.dll`：把 BDA 编辑器顶部的分类按钮显示名
  （Guns/Gun turrets/Missiles 等）换成中文，但不改变过滤用的英文键

## 安装

整个 `ZZZ_BDA_CN` 放进 `GameData\`，游戏语言保持 `zh-cn`。

## 卸载

删除 `GameData\ZZZ_BDA_CN` 即可，不会影响 BDA 本体或存档。

## 说明

- 只补 UI 词条；BDA 部件名与描述由 BDA 自带的 `localization-zh-cn.cfg` 覆盖。
- 如果 BDA 更新后新增了更多键，重新运行
  `tools/build_bda_cn_patch.py` 检查并补充。
- BDA 的少数字符串硬编码在 DLL 里，词条文件覆盖不到；这类文本需要改源码重编译。
