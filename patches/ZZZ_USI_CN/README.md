# USI 简体中文补丁

适用于 KSP 1.12.5 + USI 112.0.1（Konstruction / Akita / USI-LS）。

## 安装

把整个 `ZZZ_USI_CN` 文件夹放进：

`Kerbal Space Program\GameData\ZZZ_USI_CN`

游戏语言保持 `zh-cn`。本补丁不修改 USI 原文件，USI 更新后通常仍可继续使用。

## 卸载

删除 `GameData\ZZZ_USI_CN` 即可，不会影响 USI 本体或存档。

## 覆盖内容

- Konstruction / Akita：所有部件的标题、描述、制造商
- Konstructor 轨道建造界面：标题栏、步骤提示、按钮、错误信息
- 资源转移界面：目标选择、距离提示、错误信息
- USI-LS：所有部件的标题、描述、制造商，以及温室/回收/居住模块在 PAW 中的名称
- Konstruction 资源显示名、阿基塔动画名、燃料电池与工坊转换器名称

## 已知限制

- USI-LS 本体没有自带 `Localization` 目录；本补丁只做了 cfg 层能覆盖的部件名、
  描述和右键菜单。KSC 设置窗口和状态面板的文字硬编码在 `USILifeSupport.dll`
  里，cfg 层改不了。网上有一个第三方完整补丁
  `linshix/USI-LS-ChineseLocalization`（基于 112.0.1，含修改过的 DLL），
  如果需要设置/状态面板也中文，可以改用那个补丁；本补丁没有擅自替换 DLL。
- Konstruction 的 PAL 磁铁/活塞/对接端口右键菜单里，还有少量标签（如
  Magnet Strength、Port Force）硬编码在 `Konstruction.dll`，同样需要插件层处理。
- CommunityResourcePack 自带的中文把 `Supplies` 译作“资源”；`Mulch` 已经被
  `KISA_Fixes/MulchRename.cfg` 改成“残渣”，本补丁不再重复处理。

## 文件结构

```
ZZZ_USI_CN/
├─ Localization/
│  ├─ Konstruction_zh-cn.cfg
│  ├─ Konstructor_zh-cn.cfg
│  ├─ LifeSupport_zh-cn.cfg
│  ├─ ResourceTransfers_zh-cn.cfg
│  └─ USI_CN_en-us.cfg
└─ Patches/
   ├─ Konstruction_Localization.cfg
   ├─ LifeSupport_Localization.cfg
   ├─ Resources_Localization.cfg
   └─ UI_Localization.cfg
```
