# 删除执行记录（2026-10-19）

## 结果

| 项 | 删除前 | 删除后 |
|---|---:|---:|
| GameData 顶层目录 | 222 | 170 |
| CKAN 记录模块 | 251 | 195 |
| GameData 体积 | 16.82 GB | 10.83 GB |
| 释放空间 | — | **约 5.99 GB** |

目标名单共 54 个顶层目录。最终移除了 53 个原有目录（保留 `Kopernicus` 与
`WildBlueIndustries\001KerbalActuators`，并新增了 Final Frontier 的 `STMRibbons`）。
CKAN 管理的部分已用 `ckan remove` 注销，手工安装的部分已移出 `GameData`。
目录没有直接永久删除：原件都在
`_disabled_mods\BDA_20261019\` 下，可随时搬回。

## 实际删掉的主题

- 远未来：Far Future Technologies、Future Technologies Expansion
- 行星包：Kcalbeloh System/4K Textures、OPM、Outer Parallax、Scatterer OPM、
  Kopernicus 行星包工具、Kcalbeloh/MPE/OPM 绶带、Singularity
- 科幻/复古太空飞机：OPT、OPT Legacy、OPT Reconfig、RetroFuture、Mk2/Mk3/Mk4 Expansion
- 航天飞机：SOCK、Cormorant、Space Shuttle Accessories、Benjee10 sharedAssets
- 殖民地/基地：USI（Konstruction/USI-LS/Akita）、Planetary Base、Ground Construction、
  SimpleConstruction、Keridian Dynamics、OSSNTR、Planetside MMSEV、HabTech Props
- 空间站：SSPX、SSPX IVAs、Station Science、Universal Storage 2、HabTech Robotics
- 发射场：Modular Launch Pads、Tundra、KSC Extended、Kerbal Konstructs
- 探索合同包：11 个 Contract Packs
- 主题部件/补丁：SXT、Endurance、WildBlue Mk-33、MLP_CN、ZZZ_GC_CN、
  ZZZ_USI_CN、ZZZ_KONSTRUCTION_INDEPENDENCE、WormholeRelay

## 保留但原本在“随上级删除”里的东西

- **Kopernicus**：Parallax Continued 与 Kerbal Planet Emblems 仍然依赖它。
  行星包已删，但框架本身保留。
- **KerbalActuators**（`WildBlueIndustries\001KerbalActuators`）：Near Future
  Aeronautics 的硬依赖，保留。Mk-33 本体已删。
- **Benjee10 sharedAssets**：删除 Planetside/HabTech 后已无依赖，最终已移除。

## CKAN 批量删除的连带问题

CKAN 在 `--headless` 下把“依赖被删后失去依赖”的模组也一并删了，包括：

- Near Future Aeronautics
- Firespitter Core / Firespitter Resources
- Parallax Continued 与三套纹理
- ModularFlightIntegrator
- KSP Texture Loader
- Kerbal Planet Emblems
- Retractable Lifting Surface
- SpacetuxSA
- Planetside Exploration Technologies

这些已经重新安装；其中 Planetside、HabTech Props、Mark IV 和 Benjee10 sharedAssets
随后作为主题包再次移除。Near Future Aeronautics、Firespitter、Parallax、Kopernicus、
KSP Texture Loader、Kerbal Planet Emblems、ModularFlightIntegrator、
Retractable Lifting Surface、SpacetuxSA 和 KerbalActuators 当前都在。
- Final Frontier 与三个角色绶带包在连带删除后也已重新安装，`Nereid` 与
  `STMRibbons` 目录已恢复。

## 当前需要补的东西

- **BDArmory Continued 尚未安装**。
- BDA 的 CKAN 依赖 `ModuleManager` 已有；`PhysicsRangeExtender` 尚未安装，
  安装 BDA 时 CKAN 会自动带上。
- 如果还要装 BDA 的扩展包（BDArmoryExtended、BDModularMissileParts 等），
  再按需安装，不要一次把旧的主题包全装回来。

## 回滚

1. 手工包：把 `_disabled_mods\BDA_20261019\<目录>` 复制回 `GameData\`。
2. CKAN 包：在 CKAN 里按标识重新安装，或导入 `mods/modlist-before.ckan`。
3. 旧存档如果用了 Kcalbeloh/OPM，回滚后才能正常加载；BDA 建议开新存档。

备份清单与每个目录的大小见 `mods/gamedata-inventory-before.csv`。
