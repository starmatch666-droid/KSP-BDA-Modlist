#!/usr/bin/env python3
"""Translate the remaining English FAR UI strings in Localization_zh-cn.cfg."""

from __future__ import annotations

import re
from pathlib import Path


KSP = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Kerbal Space Program")
SOURCE = KSP / "GameData" / "FerramAerospaceResearch" / "Localization" / "Localization_zh-cn.cfg"
PATCH = Path(__file__).resolve().parents[1] / "patches" / "ZZZ_FAR_CN" / "Localization_zh-cn.cfg"

REPLACEMENTS = {
    "FAREditorStabDerivLoopButton": "运行导出扫描",
    "FAREditorStabDerivSaveErrorExp": "无法导出稳定性导数。可能需要先删除之前导出的数据。",
    "FARFlightGUIFltLogging": "飞行日志",
    "FARFlightGUIFltLogPeriod": "记录周期",
    "FARFlightGUIFltLogFlushPeriod": "刷新周期",
    "FARFlightGUIFltDebug": "FAR 调试",
    "FARDebugWindowLabel": "调试选项",
    "FARDebugExposureLabel": "暴露分析",
    "FARDevicePreferGPU": "优先使用 GPU",
    "FARDeviceNone": "禁用",
    "FARDrawBoundsLabel": "显示载具边界",
    "FARExposureWidthLabel": "宽度",
    "FARExposureHeightLabel": "高度",
    "FARExposureDirectionAirstream": "气流方向",
    "FARExposureDirectionSun": "太阳方向",
    "FARExposureDirectionBody": "天体方向",
    "FARExposureEnableLabel": "启用当前方向",
    "FARExposureArrowLabel": "显示相机箭头",
    "FARExposureShaderLabel": "在相机中可视化",
    "FARExposureShowLabelsLabel": "显示部件面积",
    "FARCtrlShowDynamicDeflection": "动态偏转",
    "FARCtrlDynamicDeflection": "切换动态偏转",
    "FARCtrlDynamicStartSpeed": "起始速度",
    "FARCtrlDynamicExponent": "衰减指数",
    "FARCtrlDynamicMinControl": "最小控制量",
}


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8-sig")
    found = set()
    lines = []
    for line in text.splitlines():
        match = re.match(r"^(\s*)([A-Za-z0-9_]+)(\s*=\s*)(.*)$", line)
        if match and match.group(2) in REPLACEMENTS:
            key = match.group(2)
            found.add(key)
            line = f"{match.group(1)}{key} = {REPLACEMENTS[key]}"
        lines.append(line)
    missing = sorted(set(REPLACEMENTS) - found)
    if missing:
        raise SystemExit("Keys not found: " + ", ".join(missing))
    result = "\n".join(lines) + "\n"
    SOURCE.write_text(result, encoding="utf-8")
    PATCH.parent.mkdir(parents=True, exist_ok=True)
    PATCH.write_text(result, encoding="utf-8")
    print(f"Updated {len(found)} FAR strings; wrote {PATCH}")


if __name__ == "__main__":
    main()
