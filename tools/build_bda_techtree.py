#!/usr/bin/env python3
"""Assign BDA/add-on parts to a tiered tech-tree progression.

Reads data/bda-tech-parts.tsv, applies era/category rules, and writes:
  GameData/ZZZ_BDA_CN/Patches/BDA_TechTree.cfg
  data/bda-tech-assignment.tsv

The patch only changes TechRequired; it never touches part stats.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KSP = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Kerbal Space Program")
SOURCE = ROOT / "data" / "bda-tech-parts.tsv"
OUT_PATCH = KSP / "GameData" / "ZZZ_BDA_CN" / "Patches" / "BDA_TechTree.cfg"
OUT_REPORT = ROOT / "data" / "bda-tech-assignment.tsv"

NODES = {
    1: "enhancedSurvivability",
    2: "subsonicFlight",
    3: "efficientFlightSystems",
    4: "specializedFlightSystems",
    5: "aerospaceComposites",
    6: "advEMSystems",
    7: "highPowerElectricalSystems",
    8: "experimentalElectricalSystems",
}

LABELS = {
    1: "基础装甲/弹药",
    2: "二战航空武器",
    3: "早期喷气/早期导弹",
    4: "冷战导弹/雷达",
    5: "现代精确制导",
    6: "AESA/先进电子战",
    7: "核武/高能武器",
    8: "实验性激光/轨道炮",
}

WW2 = (
    "sherman", "churchill", "tiger", "panther", "panzer", "stug", "jagd",
    "t-34", "kv-1", "kv-2", "is-1", "is-2", "m4", "m10", "m18", "m22",
    "m24", "m26", "m36", "m3 stuart", "crusader", "cromwell", "comet",
    "valentine", "tortoise", "tog", "char", "renault", "ft", "m13",
    "m14", "m41m", "semovente", "turan", "zrinyi", "chi-ha", "chi-he",
    "chi-nu", "chi-ri", "o-i", "type-97", "7tp", "bt-7", "t-26", "su-85",
    "su-100", "isu-152", "su-14", "su-5", "zis-30", "flak", "wirbelwind",
    "kugelblitz", "brummbar", "hummel", "wespe", "marder", "dicker",
    "sturer", "waffentrager", "m6a1", "t95", "t34", "t57", "t92", "m8",
)

COLD = (
    "m60", "m103", "m48", "m551", "mbt-70", "t-54", "t-55", "t-62",
    "t-64", "t-72", "t-80", "chieftain", "conqueror", "centurion",
    "leopard 1", "amx-30", "amx-13", "amx 50", "arl 44", "batignolles",
    "ebr", "m41", "m42", "m109", "m163", "m113", "bmp-1", "bmp-2",
    "btr", "zsu", "shilka", "gepard", "marksman", "falcon", "za-35",
    "type-74", "type-87", "strv 103", "strv 74", "ikv", "pvkv", "bkan",
    "elden", "luft42", "luft9040",
)

MODERN = (
    "m1a2", "abrams", "leopard 2", "challenger 2", "t-90", "t-80bvm",
    "t-72b3", "ztz99", "type 10", "type 16", "leclerc", "ariete",
    "centauro", "stridsvagn 122", "strv 122", "k2", "bmp-3", "btr-90",
    "puma", "boxer", "bradley", "lav-25", "lav ad", "otomatic", "pgz09",
    "ztl11", "wma301", "ptz89", "type 89", "type 90", "type 87",
    "m109a6", "paladin", "m1 howitzer", "m198", "mk45",
)

EARLY_MISSILES = (
    "aim-9b", "aim-9c", "aim-9d", "aim-9e", "aim-9g", "aim-9h",
    "aim-9j", "r-3s", "r-3r", "r-13", "aim-7d", "aim-7e", "r-530",
    "sidewinder", "sparrow",
)

MID_MISSILES = (
    "aim-9l", "aim-9m", "aim-7f", "aim-7m", "r-60", "r-23", "r-24",
    "r-27t", "agm-65", "maverick", "hellfire", "agm-114", "tow",
)

MODERN_MISSILES = (
    "aim-120", "r-27et", "r-73", "aim-132", "asraam", "harm",
    "anti-rad", "anti_rad", "meteor", "cuda", "brimstone", "siaw",
    "agm-88", "kh-58", "cm-102", "searam", "rim-116",
    "rim-162", "9m96", "mim-104", "patriot", "aster", "iris-t",
)

ADV_MISSILES = (
    "aim-120", "meteor", "cuda", "siaw", "asn4g", "scalp", "mdcn",
    "harm", "agm-88", "kh-58", "cm-102", "patriot", "mim-104",
    "s-300", "s-400", "iris-t", "rim-162", "9m96", "pl-15",
    "super 530d", "r-40", "r-27et", "r-73", "aim-132", "asraam",
)

ADVANCED_ELECTRONICS = (
    "aesa", "phased", "awacs", "snoop", "simpson", "smart-s", "apar",
    "tws", "locking radar", "irist", "irst", "electronic warfare",
    "jammer", "cloak",
)


def clean_title(row: dict) -> str:
    title = row["title"].strip()
    if "//" in title:
        title = title.rsplit("//", 1)[1].strip()
    if title.startswith("#"):
        title = row["name"]
    return title.lower()


def has_any(text: str, words: tuple[str, ...]) -> bool:
    return any(word in text for word in words)


def classify(row: dict) -> int | None:
    pack = row["pack"]
    name = row["name"].lower()
    title = clean_title(row)
    cat = row["cat"].lower()
    modules = row["modules"].lower()
    text = f"{name} {title} {cat}"

    # Hidden/legacy parts keep their original unresearcheable flag.
    if row["tech"].lower().startswith("unresearcheable"):
        return None

    # AI flight/ship computers are a late electronics branch.
    if "artificialintelligence" in modules or any(
        word in text for word in ("pilotai", "shipai", "vtolai", "orbitalai", "ai pilot", "autopilot")
    ):
        return 6

    # Other control parts: weapon manager is early, guidance/core is mid.
    if cat == "control" or "guidance" in text or "missilecore" in text:
        if "missilecontroller" in name or "weapon manager" in title:
            return 2
        if "cockpit" in title or "opencockpit" in name:
            return 2
        if "bdammguidance" in name or "proceduralmissilecore" in name:
            return 4
        return 3

    # Nuclear and strategic weapons.
    if any(word in text for word in ("nuclear", "nuke", "thermo", "tsar", "castle bravo", "b-83", "w88", "核", "氢弹", "原子")):
        return 7

    # Directed energy / railguns.
    if any(word in text for word in ("laser", "railgun", "microwave", "beam", "激光", "轨道炮", "微波", "radiation cannon")) and not any(
        word in text for word in ("laser guided", "laser-guided", "hellfire", "gsh")
    ):
        return 8

    # Radars and electronic warfare.
    if "moduleradar" in modules or cat == "radars" or "radar" in title or "雷达" in title:
        if pack == "AviatorArsenal":
            return 2
        if any(word in text for word in ADVANCED_ELECTRONICS):
            return 6
        return 4 if pack in {"BDArmory", "BDArmoryExtended"} else 5

    # Countermeasures.
    if cat == "countermeasures" or any(word in text for word in ("flare", "chaff", "ecm", "jammer", "干扰", "诱饵")):
        return 2 if pack == "AviatorArsenal" else 3

    # Cameras and targeting pods.
    if cat == "targeting" or any(word in text for word in ("camera", "targeting", "相机", "瞄准")):
        return 4

    # Ammunition and armor.
    if cat == "ammo" or "ammo" in title or "ammunition" in title or "弹药" in title or "弹鼓" in title:
        if pack == "AviatorArsenal":
            return 2
        if pack == "BDArmory":
            return 1
        if pack == "FoxDefenseContracts":
            return 2
        return 3

    if cat == "armor" or "armor" in title or "armour" in title or "装甲" in title or "plate" in title:
        if pack == "BDArmory" and "reactive" not in text:
            return 1
        return 4

    # Bombs.
    is_bomb = cat == "bombs" or "bomb" in title or "炸弹" in title or "航弹" in title
    if is_bomb:
        if any(word in text for word in ("moab", "foab", "gbu-57", "5000", "12000", "daisy cutter", "cloudmaker")):
            return 6
        if any(word in text for word in ("jdam", "gbu-", "paveway", "stormbreaker", "glide", "guided")):
            return 5
        if pack == "AviatorArsenal":
            return 2
        if pack == "FoxDefenseContracts":
            return 3
        return 4

    # Missiles and rockets.
    is_missile = (
        "missilelauncher" in modules
        or cat in {"missiles", "missile turrets", "rocket pods", "torpedoes"}
        or any(word in title for word in ("missile", "rocket", "torpedo", "导弹", "火箭", "鱼雷"))
    )
    if is_missile:
        if has_any(text, ADV_MISSILES):
            return 6
        if has_any(text, MODERN_MISSILES):
            return 5
        if has_any(text, MID_MISSILES):
            return 4
        if has_any(text, EARLY_MISSILES):
            return 3
        if pack == "AviatorArsenal":
            return 2
        if pack == "fishy_weapons_dev":
            return 4
        if pack == "FoxDefenseContracts":
            return 3
        if pack in {"KerbalAdvancedDefenseReborn", "KerbalPowers", "NKDR"}:
            return 5
        return 4

    # Guns and turrets.
    is_gun = (
        "moduleweapon" in modules
        or "moduleturret" in modules
        or cat in {"guns", "gun turrets", "laser turrets", "rocket turrets"}
        or any(word in title for word in ("gun", "cannon", "turret", "炮", "机枪"))
    )
    if is_gun:
        if pack == "AviatorArsenal":
            return 3
        if pack == "FoxDefenseContracts":
            if any(word in text for word in MODERN):
                return 6
            if any(word in text for word in COLD):
                return 4
            return 3
        if any(word in text for word in ("ciws", "goalkeeper", "millennium")):
            return 4
        if any(word in text for word in ("abrams", "120mm", "120 mm", "rh120")):
            return 6
        if any(word in text for word in ("machine gun", "browning", ".50cal", "50cal", ".50 cal")):
            return 2
        if any(word in text for word in ("100mm", "120mm", "130mm", "155mm", "183mm", "203mm", "240mm", "280mm", "380mm", "howitzer", "naval gun", "舰炮", "榴弹炮")):
            return 5
        if any(word in text for word in ("20mm", "25mm", "30mm", "37mm", "40mm", "50cal", ".50", "57mm", "76mm")):
            return 4
        if pack in {"KerbalAdvancedDefenseReborn", "KerbalPowers", "NKDR"}:
            return 5
        return 3

    # Pack defaults.
    return {
        "AviatorArsenal": 3,
        "FoxDefenseContracts": 4,
        "fishy_weapons_dev": 4,
        "BDArmory": 3,
        "BDArmoryExtended": 4,
        "BDArmoryRefurbished": 5,
        "KerbalAdvancedDefenseReborn": 5,
        "KerbalPowers": 5,
        "NKDR": 5,
        "BilikermanIndustry": 2,
        "BDModularMissileParts": 5,
    }.get(pack, 4)


def selector(name: str) -> str:
    if re.search(r"\s", name):
        pattern = re.sub(r"\s", "?", name)
        if "(" in pattern:
            pattern = pattern[: pattern.index("(")] + "*"
        return f"@PART:HAS[#name[{pattern}]]:NEEDS[CommunityTechTree]:FINAL"
    return f"@PART:HAS[#name[{name}]]:NEEDS[CommunityTechTree]:FINAL"


def main() -> None:
    rows = []
    for line in SOURCE.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        cols = line.split("\t")
        if len(cols) < 8:
            continue
        rows.append(
            dict(
                pack=cols[0],
                name=cols[1],
                title=cols[2],
                cat=cols[3],
                tech=cols[4],
                mass=cols[5],
                cost=cols[6],
                modules=cols[7],
            )
        )

    seen: set[str] = set()
    assignments = []
    for row in rows:
        if row["name"] in seen:
            continue
        seen.add(row["name"])
        tier = classify(row)
        if tier is None:
            continue
        assignments.append((row, tier, NODES[tier]))

    OUT_PATCH.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "// BDA 部件科技树代际分布",
        "// 自动生成：tools/build_bda_techtree.py",
        "// 只改 TechRequired，不改部件属性。",
        "",
    ]
    for row, tier, node in assignments:
        lines.extend(
            [
                f"// {LABELS[tier]} | {row['pack']} | {row['name']}",
                selector(row["name"]),
                "{",
                f"    @TechRequired = {node}",
                "}",
                "",
            ]
        )
    OUT_PATCH.write_text("\n".join(lines), encoding="utf-8")

    OUT_REPORT.write_text(
        "Tier\tNode\tPack\tName\tTitle\tCategory\n"
        + "\n".join(
            f"{tier}\t{node}\t{row['pack']}\t{row['name']}\t{row['title']}\t{row['cat']}"
            for row, tier, node in assignments
        )
        + "\n",
        encoding="utf-8",
    )

    counts = Counter(tier for _, tier, _ in assignments)
    print(f"Assigned {len(assignments)} unique parts -> {OUT_PATCH}")
    for tier in sorted(counts):
        print(f"  T{tier} {NODES[tier]:35s} {counts[tier]:4d}")


if __name__ == "__main__":
    main()
