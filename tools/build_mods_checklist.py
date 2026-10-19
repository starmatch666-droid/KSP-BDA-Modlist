#!/usr/bin/env python3
"""Build MODS-CHECKLIST.md: clickable Markdown checkboxes for deletion review."""

from __future__ import annotations

import csv
import re
from pathlib import Path

from build_mods_table import CATEGORY_ORDER, NAMES


ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "mods" / "gamedata-inventory.csv"
OUT = ROOT / "MODS-CHECKLIST.md"

CATEGORY_LABEL = {
    "core": "基础框架 / 前置",
    "flight": "飞行 / 导航",
    "engineering": "工程 / 建造",
    "propulsion": "推进 / 电力 / 热控",
    "aircraft": "飞机 / 地面载具",
    "comms": "通信",
    "science": "科学 / 探测",
    "career": "生涯 / 合同",
    "iva": "舱内 / IVA",
    "visual": "视觉 / 音效",
    "parts": "部件包",
    "station": "空间站 / 发射场",
    "local": "自制补丁 / 插件",
    "localization": "第三方汉化",
    "stock": "原版 / 官方 DLC",
    "misc": "其它",
}


def main() -> None:
    rows = list(csv.DictReader(CSV.open(encoding="utf-8-sig")))
    rows.sort(key=lambda row: (CATEGORY_ORDER.index(row["category"]), row["folder"].lower()))

    lines = [
        "# 当前模组删除勾选表",
        "",
        "**勾选 = 想删。** 勾选不会立刻删除文件；把勾好的清单发给我，或直接告诉我勾了哪些，我再按名单执行。",
        "",
        f"当前共 **{len(rows)}** 个 GameData 顶层目录。",
        "",
    ]
    current_category = None
    for row in rows:
        if row["category"] != current_category:
            current_category = row["category"]
            lines.extend(["", f"## {CATEGORY_LABEL[current_category]}", ""])
        english = row["title"]
        if re.search(r"[\u4e00-\u9fff]", english):
            english = row["folder"]
        purpose = row["purpose"].strip()
        lines.append(f"- [ ] **{english}**（{NAMES[row['folder']]}）— {purpose}")

    lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT} with {len(rows)} checkboxes")


if __name__ == "__main__":
    main()
