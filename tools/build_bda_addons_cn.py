#!/usr/bin/env python3
"""Generate Chinese patches for the installed BDA add-on packs."""

from __future__ import annotations

import re
from pathlib import Path


KSP = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Kerbal Space Program")
GD = KSP / "GameData"
OUT = GD / "ZZZ_BDA_CN"

REFURB = {
    "LOC_BDRefurb_82jdam_description": "500 磅 GPS 制导炸弹",
    "LOC_BDRefurb_82jdam_title": "Mk82 JDAM 制导炸弹",
    "LOC_BDRefurb_83_description": "1000 磅无制导炸弹",
    "LOC_BDRefurb_83_title": "Mk83 炸弹",
    "LOC_BDRefurb_83brake_description": "带减速板的 1000 磅无制导炸弹，适合低空轰炸",
    "LOC_BDRefurb_83brake_title": "Mk83“蛇眼”减速炸弹",
    "LOC_BDRefurb_84_description": "2000 磅无制导炸弹",
    "LOC_BDRefurb_84_title": "Mk84 炸弹",
    "LOC_BDRefurb_84brake_description": "带减速板的 2000 磅无制导炸弹，适合低空轰炸",
    "LOC_BDRefurb_84brake_title": "Mk84“蛇眼”减速炸弹",
    "LOC_BDRefurb_84jdam_description": "2000 磅 GPS 制导炸弹",
    "LOC_BDRefurb_84jdam_title": "Mk84 JDAM 制导炸弹",
    "LOC_BDRefurb_AMRAAM_Variant_Cut": "切尖弹翼",
    "LOC_BDRefurb_AMRAAM_Variant_Uncut": "完整弹翼",
    "LOC_BDRefurb_Abrams_description": "与 Nujan Dynamics 合作授权的 M256 120 毫米滑膛炮，安装在装甲炮塔上。\\n\\n<color=orange>加农炮弹</color>",
    "LOC_BDRefurb_Abrams_title": "M1“艾布拉姆斯”炮塔",
    "LOC_BDRefurb_Abrams_weapon": "艾布拉姆斯",
    "LOC_BDRefurb_EJ_description": "高性能 0.625 米喷气发动机，固定喷管，带加力燃烧室。",
    "LOC_BDRefurb_EJ_title": "J-28“虎”加力涡扇发动机",
    "LOC_BDRefurb_ERATG_Weapon": "长矛",
    "LOC_BDRefurb_ERATG_description": "",
    "LOC_BDRefurb_ERATG_title": "AGM-65ER“长矛”导弹",
    "LOC_BDRefurb_ERRAAM_Weapon": "AIM-54",
    "LOC_BDRefurb_ERRAAM_description": "重型增程雷达制导空空导弹，采用高抛弹道攻击超远距离目标。",
    "LOC_BDRefurb_ERRAAM_title": "AIM-54“不死鸟”导弹",
    "LOC_BDRefurb_HATG_Weapon": "鹤嘴锄",
    "LOC_BDRefurb_HATG_description": "把标准“小牛”导弹的大部分燃料换成大型 GBU 弹头。",
    "LOC_BDRefurb_HATG_title": "AGM-65H“鹤嘴锄”火箭炸弹",
    "LOC_BDRefurb_Maverick_Weapon": "小牛",
    "LOC_BDRefurb_Maverick_description": "",
    "LOC_BDRefurb_Maverick_title": "AGM-65“小牛”导弹",
    "LOC_BDRefurb_Mavericks_Variant_Green": "绿色",
    "LOC_BDRefurb_Mavericks_Variant_Straight": "直弹翼",
    "LOC_BDRefurb_Mavericks_Variant_Tapered": "锥形弹翼",
    "LOC_BDRefurb_Mavericks_Variant_White": "白色",
    "LOC_BDRefurb_R9X_description": "小型高速激光制导导弹，使用带展开刀片的动能弹头，适合精确打击并减少附带损伤。",
    "LOC_BDRefurb_R9X_title": "AGM-114R-9X“地狱火砍刀”导弹",
    "LOC_BDRefurb_R9X_weapon": "砍刀",
    "LOC_BDRefurb_Saturn_description": "高性能喷气发动机，可变几何推力矢量喷管，带加力燃烧室。",
    "LOC_BDRefurb_Saturn_title": "J-606“美洲豹”加力涡扇发动机",
    "LOC_BDRefurb_SingleERA_description": "单块反应装甲，适合在现有装甲上增加一点额外防护。",
    "LOC_BDRefurb_SingleERA_title": "BD 0.3×0.25 轻型反应装甲",
    "LOC_BDRefurb_SmokeCmPod_description": "发射较少的烟幕对抗措施，用于遮蔽激光指示。",
    "LOC_BDRefurb_SmokeCmPod_title": "小型烟雾对抗吊舱",
    "LOC_BDRefurb_Variant_GreyHARM": "灰色",
    "LOC_BDRefurb_Variant_Inert": "惰性",
    "LOC_BDRefurb_Variant_Live": "实弹",
    "LOC_BDRefurb_Variant_WhiteHARM": "白色",
    "LOC_KPDynamics_Gladia_title": "格拉迪亚舰队工厂",
    "LOC_RU_agent_description": "普罗米修斯工业合作伙伴",
    "LOC_RU_agent_title": "克伦斯格勒拖拉机公社",
    "LOC_PEW_BMP_description": "轻快的高射速炮塔，发射 30×165 毫米高爆弹。车体较小，无法像同类那样内置弹药。\\n\\n<color=orange>30 毫米弹药</color>",
    "LOC_PEW_BMP_title": "BMP2 炮塔",
    "LOC_PEW_BMP_weapon": "BMP2",
    "LOC_PEW_mk19_description": "40 毫米榴弹发射器，对步兵和轻型装甲杀伤力很强。",
    "LOC_PEW_mk19_title": "Mk.19 榴弹发射器",
    "LOC_PEW_mk19_weapon": "Mk.19",
    "LOC_US_agent_description": "普罗米修斯工业合作伙伴",
    "LOC_US_agent_title": "联合帝国铸造厂",
    "LOC_PEW_Agent_title": "普罗米修斯工业",
    "LOC_PEW_Agent_description": "普罗米修斯工业不对任何人员或物品的损害承担责任；所有销售均为最终决定。",
    "LOC_PEW_GBU53_title": "GBU-53/B“风暴破坏者”小直径炸弹",
    "LOC_PEW_GBU53_description": "雷达制导小直径炸弹，带折叠弹翼，可远距离滑翔并精确命中目标。",
    "LOC_PEW_GBU53_weapon": "GBU-53",
    "LOC_PEW_GBU57_title": "GBU-57A/B Kerbin 钻地弹",
    "LOC_PEW_GBU57_description": "30000 磅钻地弹，弹体太宽，无法装入 Mk2 弹舱。",
    "LOC_PEW_GBU57_weapon": "GBU-57",
    "LOC_PEW_GBU43_title": "GBU-43/B MOAB",
    "LOC_PEW_GBU43_description": "大型空爆武器，绰号“炸弹之母”，重 22000 磅，是实战中使用过的最强常规炸弹。",
    "LOC_PEW_GBU43_weapon": "MOAB",
    "LOC_PEW_BLU82_title": "BLU-82“雏菊切刀”炸弹",
    "LOC_PEW_BLU82_description": "15000 磅无制导炸弹，内部装满炸药浆。",
    "LOC_PEW_BLU82_weapon": "BLU-82",
    "LOC_BDRefurb_Flogger_title": "R-3R“鞭挞者”导弹",
    "LOC_BDRefurb_Flogger_description": "轻型短程雷达制导导弹，适合大量挂载。",
    "LOC_BDRefurb_Flogger_weapon": "R-3R",
    "LOC_PEW_9M96E2_title": "9M96E2 拦截导弹",
    "LOC_PEW_9M96E2_description": "中程高速地对空导弹，用于 S-400“凯旋”防空系统。",
    "LOC_PEW_9M96E2_weapon": "9M96E2",
    "LOC_PEW_R77_title": "R-77“蝰蛇”导弹",
    "LOC_PEW_R77_description": "如果 AMRAAM 采用格栅尾翼会怎样？",
    "LOC_PEW_R77_weapon": "R-77",
    "LOC_MNWS_X51_title": "X51 乘波者导弹",
    "LOC_MNWS_X51_description": "",
    "LOC_MNWS_X51_weapon": "X51",
    "LOC_MalFunc_162_title": "RIM-162 改进型海麻雀导弹",
    "LOC_MalFunc_162_description": "中程雷达制导点防御导弹，可由 VLS 和 MK29 发射器发射。",
    "LOC_MalFunc_162_weapon": "RIM-162 ESSM",
    "LOC_Refurb_66_title": "RIM-66 标准导弹",
    "LOC_Refurb_66_description": "标准 SM-2 中程雷达制导防空导弹，可由 VLS 发射。",
    "LOC_Refurb_66_weapon": "RIM-66",
    "LOC_PEW_174_title": "RIM-174 标准 ERAM",
    "LOC_PEW_174_description": "标准 SM-6 增程主动雷达防空导弹，可由 VLS 发射。",
    "LOC_PEW_174_weapon": "RIM-174",
    "LOC_Refurb_174B_title": "RIM-174B“枪手”",
    "LOC_Refurb_174B_description": "",
    "LOC_Refurb_174B_weapon": "RIM-174B",
    "LOC_KerbalField_ASMP_title": "ASMP 导弹",
    "LOC_KerbalField_158_title": "AGM-158 JASSM 导弹",
    "LOC_KerbalField_158C_title": "AGM-158C LRASM 导弹",
    "LOC_KerbalField_158B_title": "AGM-158B JASSM-ER 导弹",
    "LOC_KerbalField_158VLS_title": "AGM-158 VLS 发射器",
}

BDAEXT = {
    "loc_BDArmory_part_bahaRocketBoxRS_title": "可缩放火箭弹药箱",
    "loc_BDArmory_part_bahaRocketBoxRS_desc": "可缩放的火箭弹药箱，最多容纳 100 枚火箭弹。",
}

NKDR = [
    ("harp12kBomb", "12000 磅常规炸弹", "12000 磅无制导炸弹。"),
    ("b83Nuke", "B-83 核炸弹", "可由普通战斗机投放的无制导核炸弹，当量 1.2 百万吨。"),
    ("harpCastleBravo", "城堡行动“喝彩”氢弹", "重 10.7 吨、当量 1500 万吨的大型氢弹。"),
    ("FAB-100Bomb", "FAB-100 炸弹", "100 千克无制导俄式炸弹。"),
    ("FAB-250Bomb", "FAB-250 炸弹", "250 千克无制导俄式炸弹，对应 Mk-82。"),
    ("FAB-5000Bomb", "FAB-5000 炸弹", "5000 千克无制导俄式炸弹，体积巨大。"),
    ("foabBomb", "FOAB 温压弹", "比 MOAB 小但更致命，爆炸半径约为 MOAB 的两倍。"),
    ("GBU39", "GBU-39 小直径炸弹", "可以大量挂载在飞机上的小直径炸弹。"),
    ("GBU44", "GBU-44“毒蛇”小直径炸弹", "适合轻型飞机的微型小直径炸弹。"),
    ("k12Cloudmaker", "K-12“造云者”炸弹", "非常老旧、重达 44000 磅的大型炸弹。"),
    ("harpKineticBombarder", "动能轰炸武器", "重型钨棒，用动能撞击目标。"),
    ("paveWayIV", "Paveway IV 制导炸弹", "激光制导反坦克炸弹。"),
    ("moabBomb", "MOAB 大型空爆弹", "常规炸弹中威力极大的一种，爆炸半径约 180 米。"),
    ("thermoMIRV", "W88 热核多弹头导弹", "0.625 米级 GPS 制导多弹头导弹，可分别指定目标。"),
    ("tsarBomba", "沙皇炸弹", "人类制造过的最大氢弹。"),
    ("harpBahaCmPod", "细长热诱弹吊舱", "更小更细的对抗吊舱，热诱弹数量较少。"),
    ("harpGSH301Pod", "GSh-301 机炮吊舱", "单管 30 毫米机炮吊舱。"),
    ("harpGSHPod", "GSh-23 机炮吊舱", "双管 14.5 毫米 GSh-23 机炮吊舱。"),
    ("harpM129Pod", "M129 榴弹发射器吊舱", "40 毫米 M129 榴弹发射器吊舱。"),
    ("harpVulcanPod", "M61“火神”机炮吊舱", "20 毫米 M61 六管机炮，射速约 6000 发/分。"),
    ("harpAtomAnnieR", "M65“核瓦伦蒂娜”径向炮", "280 毫米核炮弹炮，径向安装版，重 65 吨。"),
    ("harpRailgunR", "原型轨道炮（径向）", "原型轨道炮，可把炮弹加速到约 7 马赫。"),
    ("harpAK230", "AK-230 近防炮", "双管 30 毫米俄式近防炮。"),
    ("harpGSHTurret", "GSh-23 直升机炮塔", "双管 14.5 毫米 GSh-23 直升机炮塔。"),
    ("harpKarl", "卡尔臼炮 041", "540 毫米超重型攻城迫击炮。"),
    ("harpKompensator", "2A3“补偿器”406 毫米核榴弹炮", "巨大的 406 毫米核榴弹炮。"),
    ("harpKV2", "旧 KV-2 炮塔", "从南 Kerbin 岛屿找到的老式 KV-2 炮塔，火炮口径很大。"),
    ("harpLAVADTurret", "LAV-AD 防空炮塔", "装有 GAU-12/U 机炮和两具毒刺发射器的短程防空炮塔。"),
    ("harpLAV25", "LAV-25 炮塔", "25 毫米 Bushmaster 机炮加两具 TOW 发射器。"),
    ("harpM1Howitzer", "M1 203 毫米榴弹炮", "大型 203 毫米榴弹炮。"),
    ("harpM198Howitzer", "M198 155 毫米榴弹炮", "射速较快的中型 155 毫米榴弹炮。"),
    ("harpMk45", "Mk45 舰炮炮塔", "127 毫米舰炮，可对空和对地。"),
    ("harpAtomAnnie", "M65“核瓦伦蒂娜”", "83 吨、280 毫米核炮弹炮，射程约 30 千米。"),
    ("harpPaladinTurret", "M109“帕拉丁”炮塔", "155 毫米自行榴弹炮炮塔，射速快、射程远。"),
    ("harpRailgun", "原型轨道炮", "原型轨道炮，炮弹约 7 马赫，但耗电很大。"),
    ("harpAAD", "AAD 反导导弹", "高速反导拦截弹，用于击落来袭导弹。"),
    ("agm158", "AGM-158B 巡航导弹", "远程亚音速空射巡航导弹，适合打击坚固目标。"),
    ("harpDavyCrockett", "W54“戴维克罗克特”核弹头", "当量约 10 到 20 吨的最小核弹头之一。"),
    ("harpExocet", "MM-40“飞鱼”反舰导弹", "主动雷达制导远程反舰导弹。"),
    ("harpM26", "M-26 火箭弹", "中程无制导火箭弹，适合大面积火力覆盖。"),
    ("harpM30", "M-30 火箭弹", "M-26 的 GPS 制导增程型。"),
    ("harpMGM", "MGM-140 ATACMS 导弹", "远程战术导弹，通常由 MLRS 发射。"),
    ("harpOhka", "樱花 MXY7 特攻机", "短程自杀式飞机，机内保留了制导系统。"),
    ("harpScud", "飞毛腿导弹（常规）", "GPS 坐标制导的远程火炮导弹。"),
    ("harpScudNuclear", "飞毛腿导弹（核）", "GPS 坐标制导的远程核导弹。"),
    ("harpStinger", "毒刺导弹", "短程防空导弹，可由 LAV-AD 炮塔发射。"),
    ("harpTomahawkConv", "战斧巡航导弹（常规）", "远程亚音速空射巡航导弹的常规型号。"),
    ("harpV1", "V-1 飞行炸弹", "在岛屿跑道下发现的古老飞行炸弹，射程很远但精度一般。"),
    ("chaparralTurret", "“小槲树”导弹炮塔", "可装 4 枚响尾蛇导弹的紧凑防空炮塔。"),
    ("davyCrockettLauncher", "戴维克罗克特发射器", "155 毫米无后坐力炮，用于发射戴维克罗克特核弹头。"),
    ("launcherMLRSTurret", "MLRS 火箭炮塔", "可装 12 枚 M26 GPS 火箭弹的多管火箭炮塔。"),
    ("scudLauncher", "飞毛腿发射车", "飞毛腿导弹的发射平台。"),
    ("Slow", "Kerbalie 降落伞", "用于径向安装在炸弹上的小型降落伞，可减缓炸弹速度。"),
    ("harpMGMCap", "MGM 发射管盖", "MGM 发射管的盖子。"),
    ("harpMGMTube", "MGM 发射管", "用来装火箭弹的管子。"),
    ("harpPod", "模块化机炮吊舱", "空机炮吊舱，可安装 GSh-23、GSh-301、20 毫米火神或 M129 榴弹发射器。"),
    ("harpRocketTube", "火箭发射管", "用来装火箭弹的管子。"),
]

BDMOD = [
    ("proceduralHighExplosive", "程序化高爆模块", "用于 BDA 自定义导弹的高爆模块。", "Carto 军事科技"),
    ("proceduralMissileCore", "程序化导弹核心", "用于 BDA 自定义导弹的程序化核心系统。", "Carto 军事科技"),
    ("proceduralMissileSRB", "程序化固体助推器", "用于 BDA 自定义导弹的程序化固体火箭发动机。", "Carto 军事科技"),
    ("MMmk1Tube", "Mk1 模块化导弹发射管", "Mk1 模块化导弹发射管，未缩放尺寸 1.5×7 米。", "SM 海军"),
]


def main() -> None:
    # localization keys
    all_loc = {**REFURB, **BDAEXT}
    lines = [
        "// BDA 扩展包简体中文补充",
        "// 覆盖 Refurbished Armory、BDArmoryExtended 等缺失词条。",
        "",
        "Localization",
        "{",
        "    zh-cn",
        "    {",
    ]
    for key, value in all_loc.items():
        lines.append(f"        #{key} = {value}")
    lines.extend(["    }", "}", ""])
    loc_path = OUT / "Localization" / "UI" / "Addons_zh.cfg"
    loc_path.parent.mkdir(parents=True, exist_ok=True)
    loc_path.write_text("\n".join(lines), encoding="utf-8")

    # NKDR hardcoded parts
    lines = ["// North Kerbin Dynamics Renewed-Extended 部件文本中文", ""]
    for part, title, desc in NKDR:
        lines.extend(
            [
                f"@PART[{part}]:FINAL",
                "{",
                f"\t@title = {title}",
                "\t@manufacturer = 北坎巴拉动力",
                f"\t@description = {desc}",
                "}",
                "",
            ]
        )
    nkdr_path = OUT / "Patches" / "NKDR_zh.cfg"
    nkdr_path.parent.mkdir(parents=True, exist_ok=True)
    nkdr_path.write_text("\n".join(lines), encoding="utf-8")

    # BD Modular hardcoded parts
    lines = ["// BD Modular Missile Parts 部件文本中文", ""]
    for part, title, desc, manufacturer in BDMOD:
        lines.extend(
            [
                f"@PART[{part}]:FINAL",
                "{",
                f"\t@title = {title}",
                f"\t@manufacturer = {manufacturer}",
                f"\t@description = {desc}",
                "}",
                "",
            ]
        )
    bdmod_path = OUT / "Patches" / "BDModular_zh.cfg"
    bdmod_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {len(all_loc)} localization keys, {len(NKDR)} NKDR parts, {len(BDMOD)} BD Modular parts")


if __name__ == "__main__":
    main()
