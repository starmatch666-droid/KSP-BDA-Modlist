#!/usr/bin/env python3
"""Build a branch-oriented BDA tech tree: weapons / armor / electronics / platforms."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from build_bda_custom_techtree import flags
from build_bda_techtree import MODERN, classify as classify_tier
from build_bda_techtree import clean_title, selector


ROOT = Path(__file__).resolve().parents[1]
KSP = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Kerbal Space Program")
SOURCE = ROOT / "data" / "bda-tech-parts.tsv"
PATCH_DIR = KSP / "GameData" / "ZZZ_BDA_CN" / "Patches"
LOC_DIR = KSP / "GameData" / "ZZZ_BDA_CN" / "Localization" / "UI"


def N(cost, parent, pos, icon, title, desc):
    return dict(cost=cost, parent=parent, pos=pos, icon=icon, title=title, desc=desc)


CT = "CommunityTechTree/UI/"
NODES = {
    "bda_foundations": N(15, "engineering101", (100, 1000), CT + "ctt_icon_enhancedSurvivability",
                         "BDA 军械基础", "弹药箱、通用挂架与基础工程部件。"),

    # Weapons
    "bda_w_root": N(20, "bda_foundations", (300, 1600), CT + "ctt_icon_subsonicFlight",
                    "武器系统", "BDA 武器研发总入口。"),
    "bda_w_guns_light": N(40, "bda_w_root", (500, 1700), CT + "ctt_icon_subsonicFlight",
                          "早期枪炮", "7–15 毫米机枪、.50 机枪与轻型炮塔。"),
    "bda_w_cannons_ww2": N(90, "bda_w_guns_light", (700, 1700), CT + "ctt_icon_specializedFlight",
                           "二战机炮", "20–40 毫米航空机炮与早期炮塔。"),
    "bda_w_autocannons": N(200, "bda_w_cannons_ww2", (900, 1700), CT + "ctt_icon_specializedFlight",
                           "现代机炮", "转管炮、链炮、自动炮与现代坦克炮。"),
    "bda_w_naval": N(400, "bda_w_autocannons", (1100, 1700), CT + "ctt_icon_highPowerElectricalSystems",
                     "舰炮与近防", "舰炮、CIWS、近程防空导弹与舰载发射系统。"),
    "bda_w_rockets": N(60, "bda_w_root", (500, 1500), CT + "ctt_icon_efficientFlight",
                       "火箭与无制导炸弹", "航空火箭弹、无制导炸弹与挂架。"),
    "bda_w_guided_bombs": N(200, "bda_w_rockets", (700, 1500), CT + "ctt_icon_efficientFlight",
                            "早期制导炸弹", "激光/GPS 制导炸弹与早期空地弹药。"),
    "bda_w_precision_bombs": N(500, "bda_w_guided_bombs", (900, 1500), CT + "ctt_icon_aerospaceComposites",
                               "现代精确炸弹", "JDAM、GBU、滑翔炸弹与钻地弹。"),
    "bda_w_heavy_bombs": N(1200, "bda_w_precision_bombs", (1100, 1500), CT + "ctt_icon_highEnergyNuclearPower",
                           "战略常规炸弹", "MOAB、FOAB、超重型与战略轰炸载荷。"),
    "bda_w_missiles_early": N(150, "bda_w_root", (500, 1300), CT + "ctt_icon_specializedFlight",
                              "早期导弹", "第一代红外/半主动雷达导弹与早期反坦克导弹。"),
    "bda_w_missiles_cold": N(350, "bda_w_missiles_early", (700, 1300), CT + "ctt_icon_specializedFlight",
                             "冷战导弹", "第二代空空、地空与反舰导弹。"),
    "bda_w_missiles_modern": N(600, "bda_w_missiles_cold", (900, 1300), CT + "ctt_icon_aerospaceComposites",
                               "现代导弹", "主动雷达、红外成像与反辐射导弹。"),
    "bda_w_missiles_advanced": N(1000, "bda_w_missiles_modern", (1100, 1300), CT + "ctt_icon_expElectricalSystems",
                                 "先进导弹", "AESA 导引、超视距与高超音速导弹。"),
    "bda_w_nuclear": N(1500, "bda_w_heavy_bombs", (1300, 1500), CT + "ctt_icon_highEnergyNuclearPower",
                       "核武器", "战术/战略核炸弹、核弹头与核火箭。"),
    "bda_w_railgun": N(1500, "bda_w_missiles_advanced", (1300, 1300), CT + "ctt_icon_experimentalElectrostaticPropulsion",
                       "轨道炮", "电磁轨道炮与超高速动能武器。"),
    "bda_w_laser": N(1800, "bda_w_railgun", (1500, 1300), CT + "ctt_icon_experimentalElectrostaticPropulsion",
                     "定向能武器", "机载/舰载激光、脉冲激光与高功率光束。"),
    "bda_w_exotic": N(2000, "bda_w_laser", (1700, 1300), CT + "ctt_icon_exoticElectricalSystems",
                      "实验性武器", "等离子、特斯拉、重力与末日级实验武器。"),

    # Armor
    "bda_a_root": N(20, "bda_foundations", (300, 1000), CT + "ctt_icon_enhancedSurvivability",
                    "装甲与载具", "装甲防护与地面载具炮塔研发总入口。"),
    "bda_a_plates": N(45, "bda_a_root", (500, 1100), CT + "ctt_icon_enhancedSurvivability",
                      "基础装甲", "钢板、复合板与基础结构装甲。"),
    "bda_a_reactive": N(200, "bda_a_plates", (700, 1100), CT + "ctt_icon_aerospaceComposites",
                        "反应与复合装甲", "爆炸反应装甲、陶瓷与复合装甲。"),
    "bda_a_ww2_tanks": N(120, "bda_a_plates", (500, 900), CT + "ctt_icon_specializedFlight",
                         "二战装甲", "二战坦克、自行火炮与坦克歼击车炮塔。"),
    "bda_a_cold_tanks": N(300, "bda_a_ww2_tanks", (700, 900), CT + "ctt_icon_specializedFlight",
                          "冷战装甲", "冷战主战坦克、步战车与自行防空炮。"),
    "bda_a_modern_tanks": N(600, "bda_a_cold_tanks", (900, 900), CT + "ctt_icon_aerospaceComposites",
                            "现代装甲", "四代主战坦克、现代步战车与复合装甲炮塔。"),

    # Electronics
    "bda_e_root": N(20, "bda_foundations", (300, 600), CT + "ctt_icon_specializedFlight",
                    "电子系统", "雷达、光电、对抗与 AI 研发总入口。"),
    "bda_e_radar_basic": N(150, "bda_e_root", (500, 700), CT + "ctt_icon_specializedFlight",
                           "基础雷达", "早期搜索雷达、测距仪与雷达告警。"),
    "bda_e_radar_advanced": N(400, "bda_e_radar_basic", (700, 700), CT + "ctt_icon_highTechElectricalSystems",
                              "高级雷达", "脉冲多普勒、TWS、IRST 与多目标跟踪。"),
    "bda_e_aesa": N(1000, "bda_e_radar_advanced", (900, 700), CT + "ctt_icon_expElectricalSystems",
                    "AESA 相控阵", "有源相控阵、预警雷达与高级火控。"),
    "bda_e_targeting": N(200, "bda_e_root", (500, 500), CT + "ctt_icon_efficientFlight",
                         "瞄准与数据链", "瞄准吊舱、摄像机、武器管理与数据链。"),
    "bda_e_countermeasures": N(120, "bda_e_root", (500, 350), CT + "ctt_icon_aerospaceComposites",
                               "对抗措施", "箔条、红外干扰弹与烟雾。"),
    "bda_e_ecm": N(600, "bda_e_countermeasures", (700, 350), CT + "ctt_icon_expElectricalSystems",
                   "电子战", "ECM 干扰、雷达压制与隐身装置。"),
    "bda_e_ai": N(1000, "bda_e_aesa", (1100, 700), CT + "ctt_icon_experimentalActuators",
                  "AI 与飞控", "AI 飞行员、舰船 AI、轨道 AI 与先进飞控。"),

    # Platforms
    "bda_p_root": N(20, "bda_foundations", (300, 200), CT + "ctt_icon_subsonicFlight",
                    "平台与发射系统", "发动机、挂架与模块化导弹平台。"),
    "bda_p_jets": N(120, "bda_p_root", (500, 300), CT + "ctt_icon_subsonicFlight",
                    "喷气动力", "早期喷气发动机与空战平台部件。"),
    "bda_p_launchers": N(60, "bda_p_root", (500, 150), CT + "ctt_icon_efficientFlight",
                         "挂架与发射器", "导弹挂架、火箭巢、发射管与弹舱。"),
    "bda_p_modular": N(400, "bda_p_launchers", (700, 150), CT + "ctt_icon_specializedFlight",
                       "模块化导弹", "程序化弹体、弹头、SRB 与模块化发射管。"),
}


def resolve_node(row: dict, tier: int) -> str:
    f = flags(row)
    pack = row["pack"]
    text = f"{row['name'].lower()} {clean_title(row)} {row['cat'].lower()}"

    # Armor and armoured vehicle turrets.
    tankish = pack == "FoxDefenseContracts" or (
        pack == "BDArmoryRefurbished"
        and any(w in text for w in ("tank", "bradley", "bmp", "challenger", "t-90", "m60", "m1a2"))
    )
    if f["armor"] or (f["gun"] and tankish):
        if f["armor"] and not f["gun"]:
            return "bda_a_plates" if tier <= 3 else "bda_a_reactive"
        if pack in {"FoxDefenseContracts", "BDArmoryRefurbished"} and any(w in text for w in MODERN):
            return "bda_a_modern_tanks"
        if tier <= 3:
            return "bda_a_ww2_tanks"
        if tier <= 5:
            return "bda_a_cold_tanks"
        return "bda_a_modern_tanks"

    # Electronics.
    if f["ai"]:
        return "bda_e_ai"
    if f["counter"]:
        return "bda_e_ecm" if any(w in text for w in ("ecm", "jammer", "cloak", "电子战", "干扰")) else "bda_e_countermeasures"
    if row["cat"].lower() in {"missile turrets", "rocket pods"}:
        return "bda_p_launchers"
    if f["radar"]:
        if tier <= 4:
            return "bda_e_radar_basic"
        if tier == 5:
            return "bda_e_radar_advanced"
        return "bda_e_aesa"
    if f["control"] or f["targeting"]:
        return "bda_e_targeting"

    # Platform / launch hardware.
    if f["rail"]:
        return "bda_w_railgun"
    if any(w in text for w in ("plasma", "tesla", "lightning", "gravity", "impulse", "等离子", "特斯拉", "重力", "零点")):
        return "bda_w_exotic"
    if f["laser"] and not (f["missile"] and any(w in text for w in ("laser guided", "laser-guided", "hellfire", "gsh"))):
        return "bda_w_laser"
    if pack == "BDModularMissileParts":
        return "bda_p_modular"
    if any(w in text for w in ("engine", "turbofan", "ej200", "saturn", "al-31")):
        return "bda_p_jets"
    if any(w in text for w in ("launcher", "rail", "tube", "pod", "bay", "rack", "mount", "发射管", "发射架", "挂架")):
        return "bda_p_launchers"

    # Weapons.
    if f["nuclear"]:
        return "bda_w_nuclear"
    if f["bomb"]:
        if any(w in text for w in ("moab", "foab", "gbu-57", "5000", "12000", "daisy cutter", "cloudmaker")):
            return "bda_w_heavy_bombs"
        if tier <= 3:
            return "bda_w_rockets"
        if tier == 4:
            return "bda_w_guided_bombs"
        return "bda_w_precision_bombs"
    if f["missile"]:
        if tier <= 3:
            return "bda_w_missiles_early"
        if tier == 4:
            return "bda_w_missiles_cold"
        if tier == 5:
            return "bda_w_missiles_modern"
        return "bda_w_missiles_advanced"
    if f["gun"]:
        if f["naval"]:
            return "bda_w_naval"
        if tier <= 2:
            return "bda_w_guns_light"
        if tier == 3:
            return "bda_w_cannons_ww2"
        return "bda_w_autocannons"
    if f["warhead"]:
        return "bda_w_guided_bombs" if tier <= 4 else "bda_w_missiles_modern"
    return "bda_foundations"


def line_dirs(parent, child):
    dx, dy = child[0] - parent[0], child[1] - parent[1]
    if abs(dx) >= abs(dy):
        return ("RIGHT", "LEFT") if dx >= 0 else ("LEFT", "RIGHT")
    return ("BOTTOM", "TOP") if dy >= 0 else ("TOP", "BOTTOM")


def main() -> None:
    rows = []
    for line in SOURCE.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        cols = line.split("\t")
        if len(cols) < 8:
            continue
        rows.append(dict(pack=cols[0], name=cols[1], title=cols[2], cat=cols[3],
                         tech=cols[4], mass=cols[5], cost=cols[6], modules=cols[7]))

    seen = set()
    assignments = []
    for row in rows:
        if row["name"] in seen:
            continue
        seen.add(row["name"])
        tier = classify_tier(row)
        if tier is None:
            continue
        text = f"{row['name'].lower()} {clean_title(row)} {row['cat'].lower()}"
        if any(w in text for w in ("moab", "foab", "gbu-57", "5000", "12000", "daisy cutter", "cloudmaker")):
            tier = 7
        if any(w in text for w in ("tesla", "plasma", "lightning", "gravity", "impulse", "等离子", "特斯拉", "重力", "零点")):
            tier = 8
        assignments.append((row, tier, resolve_node(row, tier)))

    PATCH_DIR.mkdir(parents=True, exist_ok=True)
    LOC_DIR.mkdir(parents=True, exist_ok=True)

    node_lines = [
        "// BDA 军械科技树：武器 / 装甲 / 电子 / 平台",
        "// 自动生成：tools/build_bda_branch_techtree.py",
        "",
        "@TechTree:AFTER[CommunityTechTree]",
        "{",
    ]
    for node_id, spec in NODES.items():
        parent_pos = NODES[spec["parent"]]["pos"] if spec["parent"] in NODES else (0, 0)
        line_from, line_to = line_dirs(parent_pos, spec["pos"])
        px, py = spec["pos"]
        node_lines += [
            "    RDNode",
            "    {",
            f"        id = {node_id}",
            f"        title = #LOC_BDA_TT_{node_id}_title",
            f"        description = #LOC_BDA_TT_{node_id}_description",
            f"        cost = {spec['cost']}",
            "        hideEmpty = False",
            f"        nodeName = {node_id}",
            "        anyToUnlock = False",
            f"        icon = {spec['icon']}",
            f"        pos = {px},{py},-1",
            "        scale = 0.6",
            "        Parent",
            "        {",
            f"            parentID = {spec['parent']}",
            f"            lineFrom = {line_from}",
            f"            lineTo = {line_to}",
            "        }",
            "    }",
        ]
    node_lines += ["}", ""]
    (PATCH_DIR / "BDA_TechTreeNodes.cfg").write_text("\n".join(node_lines), encoding="utf-8")

    part_lines = ["// BDA 部件科技树分配（按武器/装甲/电子/平台分支）", ""]
    for row, tier, node in assignments:
        part_lines += [
            f"// {NODES[node]['title']} | {row['pack']} | {row['name']}",
            selector(row["name"]),
            "{",
            f"    @TechRequired = {node}",
            "}",
            "",
        ]
    (PATCH_DIR / "BDA_TechTree.cfg").write_text("\n".join(part_lines), encoding="utf-8")

    loc_lines = ["// BDA 军械科技树节点名称", "", "Localization", "{", "    zh-cn", "    {"]
    for node_id, spec in NODES.items():
        loc_lines += [
            f"        #LOC_BDA_TT_{node_id}_title = {spec['title']}",
            f"        #LOC_BDA_TT_{node_id}_description = {spec['desc']}",
        ]
    loc_lines += ["    }", "}", ""]
    (LOC_DIR / "BDA_TechTree_zh.cfg").write_text("\n".join(loc_lines), encoding="utf-8")

    (ROOT / "data" / "bda-tech-assignment.tsv").write_text(
        "Tier\tNode\tPack\tName\tTitle\tCategory\n"
        + "\n".join(
            f"{tier}\t{node}\t{row['pack']}\t{row['name']}\t{row['title']}\t{row['cat']}".rstrip()
            for row, tier, node in assignments
        )
        + "\n",
        encoding="utf-8",
    )

    counts = Counter(node for _, _, node in assignments)
    print(f"Assigned {len(assignments)} unique parts to {len(NODES)} branch nodes")
    for node_id, spec in NODES.items():
        print(f"  {node_id:26s} {spec['cost']:4d}  {counts.get(node_id, 0):4d}")


if __name__ == "__main__":
    main()
