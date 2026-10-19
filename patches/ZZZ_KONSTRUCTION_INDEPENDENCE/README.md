# KS-500-O 本地工业补丁

适用于 Konstruction 112.0.1 + KSP 1.12.x。

## 作用

Konstruction 的 KS-500-O 船坞在建造飞船时会消耗：

- `MaterialKits`（主体质量）
- `SpecializedParts`（模块成本）
- `Alloys` / `Electronics` / `Synthetics` / `Robotics`（成本抵扣）
- `Prototypes`（成本溢出）

本补丁不删除这些成本，而是在 KS-500-O 内部补：

1. `USI_ModuleResourceWarehouse`：让船坞能找到自己船上的资源；
2. 7 种资源缓冲：MaterialKits、SpecializedParts、Alloys、Synthetics、Robotics、Electronics、Prototypes；
3. 5 个本地合成转换器：用 MaterialKits + EC 生产高级资源。

比例按资源 `unitCost` 做价值等价，不产生免费资源。船坞仍需要从 Duna 地表接收 MaterialKits。

## 合成配方

| 输出 | 输出速率 | MaterialKits/s | EC/s |
|---|---:|---:|---:|
| Alloys | 0.01/s | 3.0 | 30 |
| Electronics | 0.01/s | 1.91 | 30 |
| Synthetics | 0.01/s | 3.5 | 30 |
| Robotics | 0.01/s | 17.5 | 60 |
| Prototypes | 0.01/s | 150 | 300 |

全部同时运行约 450 EC/s；建议分批运行，或配大型反应堆/太阳能阵列。工程师在船坞上可提高效率。

## 使用

1. 在 Duna 轨道组装/停靠 KS-500-O；
2. 从地表运 MaterialKits 到船坞（USI 资源转移或对接口）；
3. 在船坞 PAW 中启动需要的合成转换器；
4. 等高级资源进入船坞缓冲后，再用 Konstructor 建船。

## 平衡说明

- 没有修改 Konstruction 的全局成本，也没有把 Prototypes 从配方里删掉；
- 1 单位 Prototypes 需要 15000 MaterialKits，仍是很重的后期资源；
- 船坞缓冲装满约 54 t，建议按实际船型增减 `maxAmount`。

## 卸载

删除 `GameData/ZZZ_KONSTRUCTION_INDEPENDENCE` 即可。
