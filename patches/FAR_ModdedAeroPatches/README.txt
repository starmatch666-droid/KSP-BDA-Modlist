================================================================================
 FAR 第三方气动部件适配补丁（Modded Aero Patches for FAR）
 位置：GameData/FAR_ModdedAeroPatches/
 依赖：FerramAerospaceResearch（FAR 0.16.x）+ 对应部件 mod
================================================================================

【这个补丁解决什么问题】
FAR 只自带原版部件的气动配置。第三方 mod 的机翼/舵面如果没有 FAR 配置，
在 FAR 下就不会被当作真正的机翼或操纵面，表现为升力系数不对、舵面没有
FAR 舵效。安装本补丁后：

  * SpikeX 的 4 个可动舵面（Wing1 / Wing1e / Wing2 / Wing3）→ FARControllableSurface
  * SpikeX 的固定翼面（Wing1f）→ FARWingAerodynamicModel
  * BDA/Fishy “improved wings” 的 gliderWingB、structuralWing10 → FARWingAerodynamicModel
  * 一批第三方座舱/适配器/脊线等部件上残留的原版 ModuleLiftingSurface 会被清理，
    避免原版升力和 FAR 升力叠加（做法与 FAR 处理原版部件一致）。

【哪些 mod 不用管：它们本来就自带 FAR 兼容】
  * AirplanePlus      —— Compatibility/FAR.cfg
  * SXT               —— Patches/ModCompatibility/FAR/
  * RetroFuture       —— Aero/… 自带 FAR 模块
  * Mk3Expansion      —— Patches/M3X_FAR_Compatibility.cfg
  * B9 程序化机翼     —— 部件自带 FAR 模块（其“结构面板”版本由 BDA 补丁故意禁用升力）
  * 原版 DLC 热盾等    —— FAR 自带配置
  这些部件的机翼/舵面本来就能正常参与 FAR 计算，本补丁不会重复处理。

【几何参数的来源】
SpikeX 没有提供 FAR 数据，所以 b_2 / MAC / TaperRatio / MidChordSweep
是根据它的 .mu 模型平面形状测量得到的（展开为平面后量翼展、根/梢弦长、
中弦线后掠角），并按 FAR 自身的关系 S = b_2 * MAC 与模型面积核对过。
测得这些机翼都是约 40° 后掠、梢根比约 0.3，与 SpikeX 的“超音速项目”
定位一致。fishy 的两个部件直接复用原版模型，所以沿用了 FAR 对相应原版
部件（sweptWing2 / R8winglet）的几何参数。

这些数值是“合理近似”而不是官方数据。实飞如果发现：
  * 舵效太强/太弱 → 调整对应舵面的 ctrlSurfFrac 或 maxdeflect
  * 升力/诱导阻力不对 → 调整 FARWingAerodynamicModel 的 b_2 / MAC
    （保持 b_2*MAC≈实际翼面积）
  * 配平/气动中心位置不对 → 微调 MidChordSweep 或 TaperRatio
改完 cfg 直接重新进游戏即可（ModuleManager 会重新打补丁）。

【如何验证补丁生效】
  1. 进 SPH/VAB，右键 SpikeX 舵面 → 部件菜单里应出现 FAR 的标准控制面滑块
     （俯仰/偏航/滚转 %、Max Deflect 等）。
  2. 打开 FAR 气动分析窗口，静态分析里把“俯仰设置”分别填 1 和 -1 再点
     “攻角扫描”：黄线（Cm）现在会明显整体平移，说明这些舵面已经参与 FAR 计算。
  3. 飞行中观察 FAR 飞行数据：舵面偏转应该带来对应的俯仰/滚转响应。

【特例与有意不处理的部件】
  * SpikeX 的减速板（NesdSpX_Brake1 / ModuleAeroSurface）：FAR 对原版减速板
    也是按减速板处理，不需要转成 FAR 控制面。
  * NearFutureAeronautics 的升力风扇（nfa-liftfan-*）：靠 ModuleLiftingSurface
    产生升力，FAR 没有对应替代模型，保留原样。
  * Mk2Expansion / Mk3Expansion 的 VTOL 升力风扇（ModuleControlSurface 驱动）：
    属于推进部件而不是气动操纵面，保留原样。
  * Breaking Ground 的螺旋桨/旋翼叶片（SquadExpansion 中的 blades）：
    FAR 不模拟旋翼，保留原样。
  * fishy 的 AV-R9_1：cfg 里没有可用的 .mu 模型文件，部件本身无法正常加载，
    未做处理。

【如何卸载】
直接删除整个 GameData/FAR_ModdedAeroPatches 文件夹即可。
已保存的飞行器不需要重建，重新载入后 ModuleManager 会按新配置处理。
================================================================================
