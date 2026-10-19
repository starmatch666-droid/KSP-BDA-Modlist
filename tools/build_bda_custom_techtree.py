#!/usr/bin/env python3
"""Build a dedicated BDA military tech-tree branch.

This replaces the coarse 8-node mapping with 23 custom RDNode entries under
an independent BDA branch. Existing part classification is reused, then split
by role (guns, missiles, radar, armor, bombs, etc.).
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from build_bda_techtree import classify as classify_tier
from build_bda_techtree import clean_title, selector


ROOT = Path(__file__).resolve().parents[1]
KSP = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Kerbal Space Program")
SOURCE = ROOT / "data" / "bda-tech-parts.tsv"
PATCH_DIR = KSP / "GameData" / "ZZZ_BDA_CN" / "Patches"
LOC_DIR = KSP / "GameData" / "ZZZ_BDA_CN" / "Localization" / "UI"

NODES = {
    "bda_armor_basics": dict(
        cost=25, parent="engineering101", pos=(200, 900),
        icon="CommunityTechTree/UI/ctt_icon_enhancedSurvivability",
        title="BDA 军械基础", desc="装甲板、弹药箱与基础挂架。",
    ),
    "bda_early_guns": dict(
        cost=40, parent="bda_armor_basics", pos=(400, 1050),
        icon="CommunityTechTree/UI/ctt_icon_subsonicFlight",
        title="早期枪炮", desc="7–15 毫米机枪、.50 机枪与轻型炮塔。",
    ),
    "bda_ww2_ordnance": dict(
        cost=60, parent="bda_armor_basics", pos=(400, 750),
        icon="CommunityTechTree/UI/ctt_icon_efficientFlight",
        title="二战航空弹药", desc="无制导炸弹、火箭弹与挂架。",
    ),
    "bda_ww2_cannons": dict(
        cost=90, parent="bda_early_guns", pos=(600, 1050),
        icon="CommunityTechTree/UI/ctt_icon_specializedFlight",
        title="二战机炮", desc="20–40 毫米航空机炮、炮塔与早期对地武器。",
    ),
    "bda_ww2_tanks": dict(
        cost=120, parent="bda_ww2_cannons", pos=(600, 750),
        icon="CommunityTechTree/UI/ctt_icon_enhancedSurvivability",
        title="二战装甲", desc="二战坦克、自行火炮与坦克歼击车炮塔。",
    ),
    "bda_early_jets": dict(
        cost=120, parent="bda_ww2_cannons", pos=(800, 1050),
        icon="CommunityTechTree/UI/ctt_icon_subsonicFlight",
        title="早期喷气", desc="早期喷气发动机与空战平台部件。",
    ),
    "bda_early_missiles": dict(
        cost=150, parent="bda_early_jets", pos=(1000, 1050),
        icon="CommunityTechTree/UI/ctt_icon_specializedFlight",
        title="早期导弹", desc="第一代红外/半主动雷达空空导弹与早期反坦克导弹。",
    ),
    "bda_radar_basics": dict(
        cost=150, parent="bda_early_jets", pos=(1000, 900),
        icon="CommunityTechTree/UI/ctt_icon_specializedFlight",
        title="基础雷达", desc="早期搜索雷达、测距仪、雷达告警与瞄准吊舱。",
    ),
    "bda_countermeasures": dict(
        cost=120, parent="bda_early_jets", pos=(800, 900),
        icon="CommunityTechTree/UI/ctt_icon_aerospaceComposites",
        title="对抗措施", desc="箔条、红外干扰弹、烟雾与早期电子干扰。",
    ),
    "bda_early_guided": dict(
        cost=200, parent="bda_ww2_ordnance", pos=(800, 750),
        icon="CommunityTechTree/UI/ctt_icon_efficientFlight",
        title="早期精确制导", desc="激光/GPS 制导炸弹、早期空地导弹与制导组件。",
    ),
    "bda_cold_war_tanks": dict(
        cost=300, parent="bda_ww2_tanks", pos=(1000, 750),
        icon="CommunityTechTree/UI/ctt_icon_specializedFlight",
        title="冷战装甲", desc="冷战主战坦克、步战车与自行防空炮。",
    ),
    "bda_cold_war_missiles": dict(
        cost=350, parent="bda_early_missiles", pos=(1200, 1050),
        icon="CommunityTechTree/UI/ctt_icon_specializedFlight",
        title="冷战导弹", desc="第二代红外/雷达制导空空、地空与反舰导弹。",
    ),
    "bda_advanced_radar": dict(
        cost=400, parent="bda_radar_basics", pos=(1200, 900),
        icon="CommunityTechTree/UI/ctt_icon_highTechElectricalSystems",
        title="高级雷达", desc="脉冲多普勒、TWS、IRST 与多目标跟踪雷达。",
    ),
    "bda_modern_tanks": dict(
        cost=600, parent="bda_cold_war_tanks", pos=(1400, 750),
        icon="CommunityTechTree/UI/ctt_icon_aerospaceComposites",
        title="现代装甲", desc="四代主战坦克、现代步战车与复合装甲炮塔。",
    ),
    "bda_modern_missiles": dict(
        cost=600, parent="bda_cold_war_missiles", pos=(1400, 1050),
        icon="CommunityTechTree/UI/ctt_icon_aerospaceComposites",
        title="现代导弹", desc="主动雷达、红外成像、反辐射与远程巡航导弹。",
    ),
    "bda_modern_ordnance": dict(
        cost=500, parent="bda_early_guided", pos=(1200, 650),
        icon="CommunityTechTree/UI/ctt_icon_efficientFlight",
        title="现代制导炸弹", desc="JDAM、GBU、滑翔炸弹与精确对地弹药。",
    ),
    "bda_naval_ciws": dict(
        cost=600, parent="bda_advanced_radar", pos=(1400, 900),
        icon="CommunityTechTree/UI/ctt_icon_highPowerElectricalSystems",
        title="舰载近防", desc="舰炮、CIWS、近程防空导弹与舰载发射系统。",
    ),
    "bda_aesa_ew": dict(
        cost=1000, parent="bda_advanced_radar", pos=(1600, 1000),
        icon="CommunityTechTree/UI/ctt_icon_expElectricalSystems",
        title="AESA 与电子战", desc="有源相控阵雷达、数据链、电子压制与先进 AI。",
    ),
    "bda_strategic_bombs": dict(
        cost=1200, parent="bda_modern_ordnance", pos=(1600, 650),
        icon="CommunityTechTree/UI/ctt_icon_highEnergyNuclearPower",
        title="战略轰炸", desc="超重型常规炸弹、钻地弹与战略轰炸载荷。",
    ),
    "bda_nuclear": dict(
        cost=1500, parent="bda_strategic_bombs", pos=(1800, 650),
        icon="CommunityTechTree/UI/ctt_icon_highEnergyNuclearPower",
        title="核武器", desc="战术/战略核炸弹、核弹头与核火箭。",
    ),
    "bda_railgun": dict(
        cost=1500, parent="bda_aesa_ew", pos=(1800, 900),
        icon="CommunityTechTree/UI/ctt_icon_experimentalElectrostaticPropulsion",
        title="轨道炮", desc="电磁轨道炮与超高速动能武器。",
    ),
    "bda_laser": dict(
        cost=1800, parent="bda_aesa_ew", pos=(1800, 1100),
        icon="CommunityTechTree/UI/ctt_icon_experimentalElectrostaticPropulsion",
        title="定向能武器", desc="机载/舰载激光、脉冲激光与高功率光束。",
    ),
    "bda_exotic": dict(
        cost=2000, parent="bda_laser", pos=(2000, 1000),
        icon="CommunityTechTree/UI/ctt_icon_exoticElectricalSystems",
        title="实验性武器", desc="等离子、特斯拉、重力与末日级实验武器。",
    ),
}


def flags(row: dict) -> dict[str, bool]:
    title = clean_title(row)
    text = f"{row['name'].lower()} {title} {row['cat'].lower()}"
    cat = row["cat"].lower()
    modules = row["modules"].lower()
    return {
        "ammo": cat == "ammo" or "ammo" in title or "ammunition" in title or "弹药" in title or "弹鼓" in title,
        "armor": cat == "armor" or "armor" in title or "armour" in title or "装甲" in title or "plate" in title,
        "radar": cat == "radars" or "moduleradar" in modules or "radar" in title or "雷达" in title,
        "counter": cat == "countermeasures" or any(w in text for w in ("flare", "chaff", "ecm", "jammer", "干扰", "诱饵")),
        "bomb": cat == "bombs" or "bomb" in title or "炸弹" in title or "航弹" in title,
        "missile": "missilelauncher" in modules or cat in {"missiles", "missile turrets", "rocket pods", "torpedoes"} or any(w in title for w in ("missile", "rocket", "torpedo", "导弹", "火箭", "鱼雷")),
        "gun": "moduleweapon" in modules or "moduleturret" in modules or cat in {"guns", "gun turrets", "laser turrets", "rocket turrets"} or any(w in title for w in ("gun", "cannon", "turret", "炮", "机枪")),
        "laser": any(w in text for w in ("laser", "beam", "microwave", "激光", "光束", "微波")),
        "rail": any(w in text for w in ("railgun", "轨道炮")),
        "nuclear": any(w in text for w in ("nuclear", "nuke", "thermo", "tsar", "castle bravo", "b-83", "w88", "核", "氢弹", "原子")),
        "ai": any(w in text for w in ("pilotai", "shipai", "vtolai", "orbitalai", "ai pilot", "autopilot")),
        "control": cat == "control",
        "targeting": cat == "targeting" or any(w in text for w in ("camera", "targeting", "瞄准", "相机")),
        "warhead": cat == "warheads",
        "naval": any(w in text for w in ("naval", "ciws", "goalkeeper", "phalanx", "sea ram", "mk45", "舰炮", "近防")),
        "early_mg": any(w in text for w in ("7mm", "8mm", "12mm", "13mm", "15mm", "machine gun", "browning", ".50", "shkas", "berezin", "breda", "mg131", "mg 131", "mg34", "m2 ")),
    }


def resolve_node(row: dict, tier: int) -> str:
    f = flags(row)
    pack = row["pack"]
    text = f"{row['name'].lower()} {clean_title(row)} {row['cat'].lower()}"

    if tier == 1:
        return "bda_armor_basics"
    if tier == 2:
        if f["ammo"] or f["armor"]:
            return "bda_armor_basics"
        if f["bomb"] or (f["missile"] and pack == "AviatorArsenal"):
            return "bda_ww2_ordnance"
        if f["gun"]:
            return "bda_early_guns" if f["early_mg"] else "bda_ww2_cannons"
        return "bda_ww2_ordnance"
    if tier == 3:
        if f["ammo"] or f["armor"]:
            return "bda_armor_basics"
        if f["radar"]:
            return "bda_radar_basics"
        if f["counter"]:
            return "bda_countermeasures"
        if f["bomb"]:
            return "bda_ww2_ordnance"
        if f["missile"]:
            return "bda_early_missiles"
        if f["gun"]:
            if pack == "FoxDefenseContracts":
                return "bda_ww2_tanks"
            if pack == "AviatorArsenal":
                return "bda_ww2_cannons"
            return "bda_early_guns" if f["early_mg"] else "bda_ww2_cannons"
        if f["warhead"]:
            return "bda_early_guided"
        if pack == "BDArmory" and any(w in text for w in ("engine", "ej200", "saturn", "al-31", "turbofan")):
            return "bda_early_jets"
        if pack == "FoxDefenseContracts":
            return "bda_ww2_tanks"
        return "bda_early_jets"
    if tier == 4:
        if f["radar"]:
            return "bda_radar_basics"
        if f["counter"]:
            return "bda_countermeasures"
        if f["bomb"]:
            return "bda_early_guided"
        if f["missile"]:
            return "bda_cold_war_missiles"
        if f["gun"]:
            return "bda_cold_war_tanks"
        if f["warhead"]:
            return "bda_early_guided"
        return "bda_cold_war_tanks"
    if tier == 5:
        if f["radar"]:
            return "bda_advanced_radar"
        if f["bomb"]:
            return "bda_modern_ordnance"
        if f["missile"]:
            return "bda_modern_missiles"
        if f["gun"]:
            if pack == "FoxDefenseContracts":
                return "bda_modern_tanks"
            if f["naval"]:
                return "bda_naval_ciws"
            return "bda_modern_tanks"
        if f["counter"]:
            return "bda_countermeasures"
        if f["warhead"]:
            return "bda_modern_ordnance"
        return "bda_modern_tanks"
    if tier == 6:
        if f["missile"]:
            return "bda_modern_missiles"
        if f["gun"]:
            return "bda_modern_tanks"
        return "bda_aesa_ew"
    if tier == 7:
        return "bda_nuclear" if f["nuclear"] else "bda_strategic_bombs"
    if tier == 8:
        if f["rail"]:
            return "bda_railgun"
        if any(w in text for w in ("plasma", "tesla", "lightning", "gravity", "impulse", "等离子", "特斯拉", "重力", "零点")):
            return "bda_exotic"
        return "bda_laser"
    return "bda_armor_basics"


def line_dirs(parent: tuple[int, int], child: tuple[int, int]) -> tuple[str, str]:
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

    seen: set[str] = set()
    assignments = []
    for row in rows:
        if row["name"] in seen:
            continue
        seen.add(row["name"])
        tier = classify_tier(row)
        if tier is None:
            continue
        # Heavy conventional bombs are strategic, not ordinary guided bombs.
        text = f"{row['name'].lower()} {clean_title(row)} {row['cat'].lower()}"
        if any(w in text for w in ("moab", "foab", "gbu-57", "5000", "12000", "daisy cutter", "cloudmaker")):
            tier = 7
        if any(w in text for w in ("tesla", "plasma", "lightning", "gravity", "impulse", "等离子", "特斯拉", "重力", "零点")):
            tier = 8
        node = resolve_node(row, tier)
        assignments.append((row, tier, node))

    PATCH_DIR.mkdir(parents=True, exist_ok=True)
    LOC_DIR.mkdir(parents=True, exist_ok=True)

    node_lines = [
        "// BDA 专属军械科技树支线",
        "// 自动生成：tools/build_bda_custom_techtree.py",
        "",
        "@TechTree:AFTER[CommunityTechTree]",
        "{",
    ]
    for node_id, spec in NODES.items():
        px, py = spec["pos"]
        parent = spec["parent"]
        parent_pos = NODES[parent]["pos"] if parent in NODES else (0, 0)
        line_from, line_to = line_dirs(parent_pos, spec["pos"])
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
            f"            parentID = {parent}",
            f"            lineFrom = {line_from}",
            f"            lineTo = {line_to}",
            "        }",
            "    }",
        ]
    node_lines += ["}", ""]
    (PATCH_DIR / "BDA_TechTreeNodes.cfg").write_text("\n".join(node_lines), encoding="utf-8")

    part_lines = [
        "// BDA 部件科技树分配",
        "// 自动生成：tools/build_bda_custom_techtree.py",
        "",
    ]
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

    loc_lines = [
        "// BDA 军械科技树节点名称",
        "",
        "Localization",
        "{",
        "    zh-cn",
        "    {",
    ]
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
            f"{tier}\t{node}\t{row['pack']}\t{row['name']}\t{row['title']}\t{row['cat']}"
            for row, tier, node in assignments
        )
        + "\n",
        encoding="utf-8",
    )

    counts = Counter(node for _, _, node in assignments)
    print(f"Assigned {len(assignments)} unique parts to {len(NODES)} custom nodes")
    for node_id, spec in NODES.items():
        print(f"  {node_id:24s} {spec['cost']:4d}  {counts.get(node_id, 0):4d}")


if __name__ == "__main__":
    main()
