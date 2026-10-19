# GroundConstruction 简体中文补丁

对应 GroundConstruction / Global Construction 2.7.1（KSP 1.12.x）。

## 内容

- `Localization/GroundConstruction_zh-cn.cfg`：部件标题、描述、制造商的中文
- `Localization/GroundConstruction_en-us.cfg`：新增键的英文回退
- `Patches/GroundConstruction_Localization.cfg`：把硬编码的部件文本接到本地化键
- `Plugins/GroundConstruction_CN.dll`：Harmony 文本替换插件，汉化 GroundConstruction 的窗口/按钮/提示
- `Plugins/GroundConstruction_CN.cs`：插件源码，方便后续补充词条

## 安装

把整个 `ZZZ_GC_CN` 文件夹放进 `GameData`。需要已安装：

- GroundConstruction 2.7.1
- GroundConstruction-Core 2.7.1
- Harmony 2（已有 `000_Harmony`）

## 卸载

删除 `GameData/ZZZ_GC_CN` 即可；不会影响 GroundConstruction 本体或存档。

## 已知限制

插件只替换 GroundConstruction 的固定界面短语；如果某个按钮/提示仍是英文，
把原文发我，我可以往字典里补。插件不会替换其他 mod 的界面文本。
