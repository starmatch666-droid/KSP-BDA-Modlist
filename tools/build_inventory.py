#!/usr/bin/env python3
"""Build the KSP mod inventory used by the BDA profile repository.

The script reads the live CKAN registry and GameData tree, merges a small
curated catalog (names, purposes, BDA decisions), and writes:

  MODLIST.md
  DELETION-PLAN.md
  mods/installed-modules.csv
  mods/gamedata-inventory.csv

It never modifies GameData.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


CATEGORY_ORDER = [
    ("core", "基础框架与前置"),
    ("flight", "飞行、导航与自动化"),
    ("engineering", "建造与工程"),
    ("propulsion", "推进、电力与热控"),
    ("aircraft", "飞机与地面载具"),
    ("comms", "通信"),
    ("science", "科学与探测"),
    ("career", "生涯、合同与科技"),
    ("iva", "IVA 与内饰"),
    ("visual", "视觉与音效"),
    ("parts", "部件包（主题内容）"),
    ("station", "空间站、基地与发射场"),
    ("planet", "行星包与行星框架"),
    ("localization", "第三方本地化"),
    ("local", "我们的自制补丁/插件"),
    ("stock", "原版与官方 DLC"),
    ("misc", "其它"),
]

ACTION_LABEL = {
    "keep": "✅ 必留",
    "optional": "◻️ 可选",
    "delete": "❌ 建议删除",
    "delete-with-parent": "❌ 随上级删除",
    "disabled": "⏸️ 已禁用",
}

ACTION_ORDER = {
    "keep": 0,
    "optional": 1,
    "delete": 2,
    "delete-with-parent": 3,
    "disabled": 4,
}


def load_registry(path: Path) -> dict:
    with path.open("r", encoding="utf-8-sig") as handle:
        return json.load(handle)


def build_folder_module_map(registry: dict) -> dict[str, set[str]]:
    mapping: dict[str, set[str]] = defaultdict(set)
    for file_path, module_id in registry.get("installed_files", {}).items():
        parts = file_path.replace("\\", "/").split("/")
        if len(parts) >= 2 and parts[0] == "GameData":
            mapping[parts[1]].add(module_id)
    return mapping


def folder_size(folder: Path) -> tuple[int, int]:
    files = 0
    total = 0
    for item in folder.rglob("*"):
        if item.is_file():
            files += 1
            try:
                total += item.stat().st_size
            except OSError:
                pass
    return files, total


def module_rows(registry: dict) -> list[dict]:
    rows = []
    for ident, payload in registry.get("installed_modules", {}).items():
        source = payload.get("source_module", {})
        authors = source.get("author", [])
        if isinstance(authors, str):
            authors = [authors]
        rows.append(
            {
                "identifier": ident,
                "name": source.get("name", ident),
                "version": str(source.get("version", "")),
                "authors": ", ".join(authors),
                "abstract": source.get("abstract", ""),
                "license": source.get("license", ""),
                "installed_time": payload.get("install_time", ""),
                "kind": source.get("kind", ""),
            }
        )
    rows.sort(key=lambda row: row["name"].lower())
    return rows


def fmt_mb(byte_count: int) -> str:
    mb = byte_count / (1024 * 1024)
    if mb >= 1024:
        return f"{mb / 1024:.2f} GB"
    if mb >= 10:
        return f"{mb:.0f} MB"
    if mb >= 1:
        return f"{mb:.1f} MB"
    return "<1 MB"


def version_for(folder: str, module_ids: set[str], by_id: dict[str, dict]) -> str:
    versions = []
    for ident in sorted(module_ids):
        row = by_id.get(ident)
        if row and row["version"]:
            versions.append(row["version"])
    if versions:
        # Collapse repeated versions of a metapackage and its dependencies.
        unique = []
        for version in versions:
            if version not in unique:
                unique.append(version)
        if len(unique) <= 2:
            return " / ".join(unique)
        return f"{unique[0]} 等 {len(unique)} 个"
    version_file = None
    for candidate in (Path(folder) / f"{Path(folder).name}.version",):
        if candidate.exists():
            version_file = candidate
            break
    return "手工"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ksp", required=True, help="KSP install directory")
    parser.add_argument("--repo", required=True, help="repository root")
    parser.add_argument(
        "--phase",
        choices=("before", "after"),
        default="before",
        help="before: write MODLIST.md + DELETION-PLAN.md; after: write MODLIST-AFTER.md and current CSVs",
    )
    args = parser.parse_args()

    ksp = Path(args.ksp)
    repo = Path(args.repo)
    gamedata = ksp / "GameData"
    registry_path = ksp / "CKAN" / "registry.json"

    registry = load_registry(registry_path)
    folder_modules = build_folder_module_map(registry)
    modules = module_rows(registry)
    by_id = {row["identifier"]: row for row in modules}
    catalog = json.loads((repo / "data" / "catalog.json").read_text(encoding="utf-8"))

    folders = sorted(
        (item for item in gamedata.iterdir() if item.is_dir()),
        key=lambda item: item.name.lower(),
    )

    inventory = []
    missing = []
    for folder in folders:
        meta = catalog.get(folder.name)
        if meta is None:
            missing.append(folder.name)
            meta = {
                "title": folder.name,
                "purpose": "未分类目录，请补充 catalog.json。",
                "category": "misc",
                "action": "optional",
            }
        file_count, byte_count = folder_size(folder)
        module_ids = folder_modules.get(folder.name, set())
        inventory.append(
            {
                "folder": folder.name,
                "title": meta["title"],
                "purpose": meta["purpose"],
                "category": meta["category"],
                "action": meta["action"],
                "note": meta.get("note", ""),
                "modules": ", ".join(sorted(module_ids)),
                "version": version_for(folder.name, module_ids, by_id)
                if module_ids
                else "手工",
                "files": file_count,
                "bytes": byte_count,
            }
        )

    if missing:
        print("WARNING: catalog entries missing for:")
        for name in missing:
            print("  -", name)

    # CSV: every CKAN module with official metadata.
    csv_path = repo / "mods" / "installed-modules.csv"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(modules[0].keys()))
        writer.writeheader()
        writer.writerows(modules)

    # CSV: top-level GameData inventory with our BDA decision.
    gd_csv = repo / "mods" / "gamedata-inventory.csv"
    with gd_csv.open("w", encoding="utf-8-sig", newline="") as handle:
        fields = [
            "folder",
            "title",
            "category",
            "action",
            "version",
            "modules",
            "files",
            "bytes",
            "purpose",
            "note",
        ]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(inventory)

    total_bytes = sum(row["bytes"] for row in inventory)
    delete_rows = [
        row
        for row in inventory
        if row["action"] in {"delete", "delete-with-parent"}
    ]
    delete_bytes = sum(row["bytes"] for row in delete_rows)
    optional_bytes = sum(
        row["bytes"] for row in inventory if row["action"] == "optional"
    )

    # MODLIST.md / MODLIST-AFTER.md
    title = (
        "# KSP 现有模组清单（BDA 取舍版）"
        if args.phase == "before"
        else "# KSP 删除后模组清单（BDA 当前状态）"
    )
    lines = [
        title,
        "",
        f"- 快照时间：2026-10-19",
        f"- KSP：1.12.5（zh-cn，Steam）",
        f"- GameData 顶层目录：**{len(inventory)}** 个",
        f"- CKAN 已记录模块：**{len(modules)}** 个",
        f"- GameData 总体积：**{total_bytes / (1024 ** 3):.2f} GB**",
        (
            f"- 建议删除（含随上级删除项）：**{len(delete_rows)}** 个顶层目录，约 **{fmt_mb(delete_bytes)}**"
            if args.phase == "before"
            else f"- 删除后仍存在的顶层目录：**{len(inventory)}** 个"
        ),
        f"- 可选项（IVA/视觉/科学等，按需保留）：约 **{fmt_mb(optional_bytes)}**",
        "",
        "> 这是“当前安装”的盘点，不是推荐安装顺序。BDArmory Continued 本体只依赖",
        "> ModuleManager 与 PhysicsRangeExtender；下面标为“必留”的多数是飞行、建造、",
        "> 通信与 Near Future 推进等对空战/飞行有用的基础设施。",
        "",
        "## 怎么读这张表",
        "",
        "| 标记 | 含义 |",
        "|---|---|",
        "| ✅ 必留 | 框架/前置、BDA 直接相关，或对喷气机与空战有明显帮助 |",
        "| ◻️ 可选 | 不影响 BDA 运行，按画面、IVA、科研或生涯偏好保留 |",
        "| ❌ 建议删除 | 主题与 BDA 不符，或只是某个主题包的附属补丁 |",
        "| ⏸️ 已禁用 | 目录还在，但当前不参与加载 |",
        "",
        "“随上级删除”表示它本身是某个主题包的汉化/兼容补丁；上级包删掉后它也没有意义。",
        "",
        "## 完整清单",
        "",
    ]

    for category, category_label in CATEGORY_ORDER:
        rows = [row for row in inventory if row["category"] == category]
        if not rows:
            continue
        rows.sort(
            key=lambda row: (
                ACTION_ORDER.get(row["action"], 9),
                -row["bytes"],
                row["folder"].lower(),
            )
        )
        lines.extend(
            [
                f"### {category_label}",
                "",
                "| 目录 | 名称 | 用途 | 版本 | BDA 取舍 | 大小 |",
                "|---|---|---|---|---|---:|",
            ]
        )
        for row in rows:
            note = f"<br>注：{row['note']}" if row["note"] else ""
            action = ACTION_LABEL.get(row["action"], row["action"])
            lines.append(
                "| `{folder}` | {title} | {purpose}{note} | {version} | {action} | {size} |".format(
                    folder=row["folder"],
                    title=row["title"].replace("|", "\\|"),
                    purpose=row["purpose"].replace("|", "\\|"),
                    note=note,
                    version=row["version"].replace("|", "\\|"),
                    action=action,
                    size=fmt_mb(row["bytes"]),
                )
            )
        lines.append("")

    lines.extend(
        [
            "## 说明",
            "",
            "- 体积按目录内所有文件求和；“<1 MB”并不代表没有文件。",
            "- 版本来自 CKAN 注册表；手工安装的包没有 CKAN 版本号时标为“手工”。",
            "- `Squad` 与 `SquadExpansion` 是原版与官方 DLC，不算第三方模组，但保留在表中以便核对。",
            "- `ScattererAtmosphereCache` 是自动生成的缓存；删除后首次进入游戏会重建。",
            "- 机器可读版本见 [`mods/installed-modules.csv`](mods/installed-modules.csv) 与",
            "  [`mods/gamedata-inventory.csv`](mods/gamedata-inventory.csv)。",
        ]
    )
    list_name = "MODLIST.md" if args.phase == "before" else "MODLIST-AFTER.md"
    (repo / list_name).write_text("\n".join(lines) + "\n", encoding="utf-8")

    # DELETION-PLAN.md
    plan = [
        "# BDA 化删除名单",
        "",
        "目标：保留 BDA 空战/飞行真正需要的东西，删掉“远未来、行星包、航天飞机、殖民地、",
        "空间站、科幻太空飞机”等主题包及其专属补丁。",
        "",
        "## 结论",
        "",
        f"- 建议删除的顶层目录：**{len(delete_rows)}** 个",
        f"- 预计释放：**{fmt_mb(delete_bytes)}**（以实际磁盘占用为准）",
        f"- 当前 GameData：**{total_bytes / (1024 ** 3):.2f} GB**",
        "",
        "BDArmory Continued 的 CKAN 依赖只有 **ModuleManager** 与 **PhysicsRangeExtender**；",
        "因此下面这些包都不是运行 BDA 的必要条件。",
        "",
        "## A. 明确删除（主题不符）",
        "",
        "| 目录 | 名称 | 删除理由 | 大小 |",
        "|---|---|---|---:|",
    ]
    tier_a = [row for row in delete_rows if row["action"] == "delete"]
    tier_a.sort(key=lambda row: -row["bytes"])
    for row in tier_a:
        plan.append(
            "| `{folder}` | {title} | {purpose} | {size} |".format(
                folder=row["folder"],
                title=row["title"].replace("|", "\\|"),
                purpose=row["purpose"].replace("|", "\\|"),
                size=fmt_mb(row["bytes"]),
            )
        )

    plan.extend(
        [
            "",
            "## B. 随上级删除（专属补丁/前置）",
            "",
            "| 目录 | 名称 | 删除原因 / 归属 | 大小 |",
            "|---|---|---|---:|",
        ]
    )
    tier_b = [row for row in delete_rows if row["action"] == "delete-with-parent"]
    tier_b.sort(key=lambda row: -row["bytes"])
    for row in tier_b:
        plan.append(
            "| `{folder}` | {title} | {purpose} | {size} |".format(
                folder=row["folder"],
                title=row["title"].replace("|", "\\|"),
                purpose=row["purpose"].replace("|", "\\|"),
                size=fmt_mb(row["bytes"]),
            )
        )

    plan.extend(
        [
            "",
            "## C. 默认保留（BDA 直接相关或普适）",
            "",
            "- **BDA 与前置**：ModuleManager、PhysicsRangeExtender（尚未安装）、Harmony、KSPCommunityFixes。",
            "- **飞行/空战**：AtmosphereAutopilot、B9 Procedural Wings、CorrectCoL、Trajectories、",
            "  MechJeb2、ThrottleControlledAvionics、RCS Build Aid、Docking Cam、DPAI、Wind Tunnel、",
            "  Kerbal Flight Indicators、NavHud、NavUtilities、Persistent Rotation。",
            "- **喷气机/载具**：Near Future Aeronautics、Firespitter、Kerbal Foundries、",
            "  Retractable Lifting Surface、B9 Part Switch、KSPWheel。",
            "- **推进/电力/热控**：Near Future 全套（Aeronautics/Construction/Electrical/Exploration/",
            "  LaunchVehicles/Propulsion/Rovers/Solar/Spacecraft）、Cryo Engines/Tanks、Kerbal Atomics、",
            "  System Heat 全套、Heat Control、Dynamic Battery Storage、Deployable Engines。",
            "- **工程/建造**：KIS、KAS、Ship Manifest、Configurable Containers、TweakScale、",
            "  Editor Extensions、VAB Organizer、Janitor's Closet、Hangar Extender、Dock Rotate。",
            "- **通信**：CommNet Antennas Extension/Consumptor/Info、RemoteTech Redev Antennas。",
            "- **视觉基础**：ReStock/ReStock+、Waterfall、Scatterer、EVE、Spectra、TUFX、PlanetShine、",
            "  Firefly、Rocket Sound Enhancement。",
            "",
            "## D. 可选项（不删也能玩 BDA）",
            "",
            "- **IVA/内饰**：ASET、MOARdV Avionics、JSI/RPM、FreeIva、Reviva、DE_IVA、",
            "  Probe Control Room、VesselView、Through The Eyes、Near Future Props、KSA IVA。",
            "  如果只看外部视角打空战，这些可以再省 200 MB 左右。",
            "- **生涯/合同**：Contract Configurator、Contract Packs、DMagic Utilities。",
            "  合同包偏探索/空间站主题，纯空战存档可以删。",
            "- **科学**：SCANsat、DMagic Orbital Science、Tarsier、SpaceDust、SpaceDust Next、ScienceAlert。",
            "  科学玩法本身是普适的，默认保留。",
            "- **视觉/性能**：Parallax Continued 三套纹理约 3.4 GB；如果 BDA 大规模空战掉帧，",
            "  这是第一个值得关掉的东西。KSPRC、TextureReplacer、Conformal Decals、Indicator Lights、",
            "  Chatterer、ZTheme、Benjee10 Suits 也都是纯外观。",
            "",
            "## E. 存档与回滚",
            "",
            "- 删除行星包（Kcalbeloh/OPM）会让依赖这些星球的存档无法正常加载；BDA 建议开新存档。",
            "- 本次操作会先把目录移到 `_disabled_mods/BDA_20261019/`，再按需要从 CKAN 注销。",
            "- `mods/gamedata-inventory.csv` 记录了每个目录的体积与 CKAN 标识，可用于恢复。",
            "- 不建议直接删除 `Squad`、`SquadExpansion`、`ModuleManager`、`KSPCommunityFixes`。",
        ]
    )
    if args.phase == "before":
        (repo / "DELETION-PLAN.md").write_text("\n".join(plan) + "\n", encoding="utf-8")

    print(f"Wrote {len(inventory)} GameData folders and {len(modules)} CKAN modules.")
    print(f"Delete tier size: {fmt_mb(delete_bytes)}")


if __name__ == "__main__":
    main()
