<!-- zhtw:disable -->
# Blind-v2 Source Classification 010

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-010.json`
Cases: 100
Seed: `20260719`
Selection: `equal-source-deterministic-sha256-v1`
Selection round: 1

## Rules

- Read only the input and provenance shown in this packet.
- Do not run zhtw, OpenCC, zhconv, Gemini, or another converter.
- Mark `eligible = no` for malformed, unclear, non-Mandarin, or unsuitable text.
- Script: `simplified`, `mixed`, `traditional`, or `uncertain`.
- Domain: `it_api_cli`, `ui_i18n`, `llm_generated`, `formal_news`, `social_daily`, or `high_stakes`.
- Risk: `candidate_gap`, `over_conversion_guard`, or `baseline_guard`.
- Confidence: `high`, `medium`, or `low`; do not guess when context is insufficient.
- This packet is advisory input classification, not expected-output annotation.

## Cases

### osha-chainsaw-safety-simplified-v1/sentence-001

- Source: `osha-chainsaw-safety-simplified-v1`
- Source case: `sentence-001`
- Split: `document`

Input:

```text
操作链锯存在危险，使用适当的个人防护装备和遵守安全操作程序可以最大限度地减少潜在的伤害。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-chainsaw-safety-simplified-v1/sentence-003

- Source: `osha-chainsaw-safety-simplified-v1`
- Source case: `sentence-003`
- Split: `document`

Input:

```text
确保链条始终锋利且油箱已加满。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-chainsaw-safety-simplified-v1/sentence-004

- Source: `osha-chainsaw-safety-simplified-v1`
- Source case: `sentence-004`
- Split: `document`

Input:

```text
在地面或其他稳固的支撑物上启动锯；严禁悬空启动。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-chainsaw-safety-simplified-v1/sentence-005

- Source: `osha-chainsaw-safety-simplified-v1`
- Source case: `sentence-005`
- Split: `document`

Input:

```text
在距离加油区至少 10 英尺（3米）的地方启动，并开启链锯制动器。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-chainsaw-safety-simplified-v1/sentence-006

- Source: `osha-chainsaw-safety-simplified-v1`
- Source case: `sentence-006`
- Split: `document`

Input:

```text
使用经认可的容器给链锯加油。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-chainsaw-safety-simplified-v1/sentence-007

- Source: `osha-chainsaw-safety-simplified-v1`
- Source case: `sentence-007`
- Split: `document`

Input:

```text
进行加油操作时，需要在距离所有火源至少 10 英尺（3米）的地方进行；加油时禁止吸烟。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-chainsaw-safety-simplified-v1/sentence-008

- Source: `osha-chainsaw-safety-simplified-v1`
- Source case: `sentence-008`
- Split: `document`

Input:

```text
将燃料倒入链锯中时使用漏斗或软管。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-chainsaw-safety-simplified-v1/sentence-010

- Source: `osha-chainsaw-safety-simplified-v1`
- Source case: `sentence-010`
- Split: `document`

Input:

```text
清除链锯导板上的污垢、碎片、小树枝和石块。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-chainsaw-safety-simplified-v1/sentence-011

- Source: `osha-chainsaw-safety-simplified-v1`
- Source case: `sentence-011`
- Split: `document`

Input:

```text
砍伐树木之前，请检查树上是否有钉子、尖刺或其他金属。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-chainsaw-safety-simplified-v1/sentence-013

- Source: `osha-chainsaw-safety-simplified-v1`
- Source case: `sentence-013`
- Split: `document`

Input:

```text
用双手握持锯柄，并在操作链锯时保持平衡。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-chainsaw-safety-simplified-v1/sentence-014

- Source: `osha-chainsaw-safety-simplified-v1`
- Source case: `sentence-014`
- Split: `document`

Input:

```text
操作链锯时必须佩戴适当的个人防护装备，包括手、脚、腿、眼睛、面部、听力和头部的保护装置。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-chainsaw-safety-simplified-v1/sentence-015

- Source: `osha-chainsaw-safety-simplified-v1`
- Source case: `sentence-015`
- Split: `document`

Input:

```text
不要穿宽松的衣服。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-chainsaw-safety-simplified-v1/sentence-017

- Source: `osha-chainsaw-safety-simplified-v1`
- Source case: `sentence-017`
- Split: `document`

Input:

```text
留意受压的树枝，切割时它们可能会崩出。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-chainsaw-safety-simplified-v1/sentence-018

- Source: `osha-chainsaw-safety-simplified-v1`
- Source case: `sentence-018`
- Split: `document`

Input:

```text
汽油链锯必须配备保护装置，以最大限度地减少链锯反冲。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-chainsaw-safety-simplified-v1/sentence-019

- Source: `osha-chainsaw-safety-simplified-v1`
- Source case: `sentence-019`
- Split: `document`

Input:

```text
为避免反冲，请勿使用端头进行切割。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-cleanup-simplified-v1/sentence-005

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-005`
- Split: `document`

Input:

```text
如果您是参与清理和重建活动的雇主、工人、房主或市民，请务必在参与这些活动之前评估危险性和（或）遇到危险的可能性。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-cleanup-simplified-v1/sentence-008

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-008`
- Split: `document`

Input:

```text
被洪水淹没的工业和废弃矿场的有毒物质。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-cleanup-simplified-v1/sentence-009

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-009`
- Split: `document`

Input:

```text
空气中的霉菌和真菌。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-cleanup-simplified-v1/sentence-010

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-010`
- Split: `document`

Input:

```text
对封闭空间用新鲜空气进行通风。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-cleanup-simplified-v1/sentence-024

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-024`
- Split: `document`

Input:

```text
树木的修剪与杂物清除与倒下的电力线相连接的电线或树枝有带电的危险，与之接触会导致触电。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-cleanup-simplified-v1/sentence-026

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-026`
- Split: `document`

Input:

```text
链锯和切割机等设备造成的伤害。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-cleanup-simplified-v1/sentence-030

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-030`
- Split: `document`

Input:

```text
做出清晰的标记，以标示出树木残片可能落到工人身上的危险区域。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-cleanup-simplified-v1/sentence-036

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-036`
- Split: `document`

Input:

```text
如果不可行，请使用更多的工人和适当的举升方式。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-cleanup-simplified-v1/sentence-041

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-041`
- Split: `document`

Input:

```text
遵从适当的用梯安全（如：梯子架设在坚固稳定的地方，上下梯时保持“三点”接触，不要站在最上面的梯级上）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-cleanup-simplified-v1/sentence-043

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-043`
- Split: `document`

Input:

```text
便携发电机燃气或柴油发电机导致的电击和触电。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-cleanup-simplified-v1/sentence-047

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-047`
- Split: `document`

Input:

```text
检查电线以确保它们状况良好且没有破损；使用接地故障断路器 (GFCI)。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-cleanup-simplified-v1/sentence-048

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-048`
- Split: `document`

Input:

```text
确保发电机运行的地方通风良好。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-cleanup-simplified-v1/sentence-062

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-062`
- Split: `document`

Input:

```text
相关的详细信息请参阅29 CFR 1910.146。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-cleanup-simplified-v1/sentence-070

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-070`
- Split: `document`

Input:

```text
OSHA还向工人和雇主提供信息、进行培训和协助。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-cleanup-simplified-v1/sentence-075

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-075`
- Split: `document`

Input:

```text
这些信息将根据要求提供给有视听障碍的人。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-falls-simplified-v1/sentence-001

- Source: `osha-disaster-falls-simplified-v1`
- Source case: `sentence-001`
- Split: `document`

Input:

```text
应急救援人员在应对自然和人为灾难时，会面临因滑倒、绊倒和跌倒而受伤甚至死亡的风险。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-falls-simplified-v1/sentence-002

- Source: `osha-disaster-falls-simplified-v1`
- Source case: `sentence-002`
- Split: `document`

Input:

```text
雇主必须采取的、确保工人安全的步骤包括：制定事前灾难响应方案并确保应急救援人员了解该方案。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-falls-simplified-v1/sentence-003

- Source: `osha-disaster-falls-simplified-v1`
- Source case: `sentence-003`
- Split: `document`

Input:

```text
评估作业场地，以确定其是否存在或可能存在危险。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-falls-simplified-v1/sentence-004

- Source: `osha-disaster-falls-simplified-v1`
- Source case: `sentence-004`
- Split: `document`

Input:

```text
提供防护装备以防止滑倒、绊倒和跌倒，它们包括：防滑鞋（例如橡胶鞋底）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-falls-simplified-v1/sentence-005

- Source: `osha-disaster-falls-simplified-v1`
- Source case: `sentence-005`
- Split: `document`

Input:

```text
手套，工人可以牢固地抓住栏杆 / 梯子以稳定自己。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-falls-simplified-v1/sentence-006

- Source: `osha-disaster-falls-simplified-v1`
- Source case: `sentence-006`
- Split: `document`

Input:

```text
头部防护装置个人跌落保护培训员工们识别危险——包括需要防护装备的危险，以及如何防止受伤。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-falls-simplified-v1/sentence-007

- Source: `osha-disaster-falls-simplified-v1`
- Source case: `sentence-007`
- Split: `document`

Input:

```text
尽量避免在湿滑的地方行走；将湿掉的鞋底擦干。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-falls-simplified-v1/sentence-008

- Source: `osha-disaster-falls-simplified-v1`
- Source case: `sentence-008`
- Split: `document`

Input:

```text
使用手电筒或头盔灯，以避开洞口或地板开口、潮湿或光滑的表面、以及碎片或设备。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-falls-simplified-v1/sentence-009

- Source: `osha-disaster-falls-simplified-v1`
- Source case: `sentence-009`
- Split: `document`

Input:

```text
在目视检查以确保没有孔洞或薄弱处、并且可以支撑工人及其设备的重量之前，请勿踏上任何表面。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-falls-simplified-v1/sentence-010

- Source: `osha-disaster-falls-simplified-v1`
- Source case: `sentence-010`
- Split: `document`

Input:

```text
攀爬梯子时切勿手持设备或工具。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-falls-simplified-v1/sentence-011

- Source: `osha-disaster-falls-simplified-v1`
- Source case: `sentence-011`
- Split: `document`

Input:

```text
使用背包和工具带以固定设备、解放双手。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-falls-simplified-v1/sentence-012

- Source: `osha-disaster-falls-simplified-v1`
- Source case: `sentence-012`
- Split: `document`

Input:

```text
在高空未受保护的边缘附近移动或执行应急救援时，使用防坠落保护装置。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-falls-simplified-v1/sentence-013

- Source: `osha-disaster-falls-simplified-v1`
- Source case: `sentence-013`
- Split: `document`

Input:

```text
将滑倒、绊倒和跌倒的危险用通讯设备——尤其是免提设备——通知雇主/救援主管和其他工人。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-disaster-falls-simplified-v1/sentence-014

- Source: `osha-disaster-falls-simplified-v1`
- Source case: `sentence-014`
- Split: `document`

Input:

```text
当您对某项任务的安全性有疑问时，请停止并通知主管。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-electrical-safety-simplified-v1/sentence-001

- Source: `osha-electrical-safety-simplified-v1`
- Source case: `sentence-001`
- Split: `document`

Input:

```text
电会导致灼伤、电击甚至触电（死亡）等危险。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-electrical-safety-simplified-v1/sentence-002

- Source: `osha-electrical-safety-simplified-v1`
- Source case: `sentence-002`
- Split: `document`

Input:

```text
所有架空电线都可能已通电且为致命电压。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-electrical-safety-simplified-v1/sentence-003

- Source: `osha-electrical-safety-simplified-v1`
- Source case: `sentence-003`
- Split: `document`

Input:

```text
永远不要认为电线是安全的，即使它是垂下的或看起来是绝缘的。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-electrical-safety-simplified-v1/sentence-004

- Source: `osha-electrical-safety-simplified-v1`
- Source case: `sentence-004`
- Split: `document`

Input:

```text
切勿接触掉落的架空电线，通知电力公司该掉落的电线。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-electrical-safety-simplified-v1/sentence-005

- Source: `osha-electrical-safety-simplified-v1`
- Source case: `sentence-005`
- Split: `document`

Input:

```text
在清理和其他活动期间，与架空电线保持至少 10英尺（3米）的距离。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-electrical-safety-simplified-v1/sentence-006

- Source: `osha-electrical-safety-simplified-v1`
- Source case: `sentence-006`
- Split: `document`

Input:

```text
如果您在高处工作或处理长物体，请在工作开始前核实该区域是否存在架空电线。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-electrical-safety-simplified-v1/sentence-007

- Source: `osha-electrical-safety-simplified-v1`
- Source case: `sentence-007`
- Split: `document`

Input:

```text
如果在您驾车时，架空电线掉落至您的车辆上，请留在车内并继续驶离电线；如果发动机熄火，请勿离开车辆。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-electrical-safety-simplified-v1/sentence-008

- Source: `osha-electrical-safety-simplified-v1`
- Source case: `sentence-008`
- Split: `document`

Input:

```text
警告其他人不要触摸该车辆或电线。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-electrical-safety-simplified-v1/sentence-009

- Source: `osha-electrical-safety-simplified-v1`
- Source case: `sentence-009`
- Split: `document`

Input:

```text
致电或请人致电当地电力公司和紧急服务中心。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-electrical-safety-simplified-v1/sentence-010

- Source: `osha-electrical-safety-simplified-v1`
- Source case: `sentence-010`
- Split: `document`

Input:

```text
站在水中时切勿操作电气设备。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-electrical-safety-simplified-v1/sentence-011

- Source: `osha-electrical-safety-simplified-v1`
- Source case: `sentence-011`
- Split: `document`

Input:

```text
除非有相关资质和授权，切勿修理插线板或电气设备。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-electrical-safety-simplified-v1/sentence-012

- Source: `osha-electrical-safety-simplified-v1`
- Source case: `sentence-012`
- Split: `document`

Input:

```text
在通电前，让有资质的电工检查曾经受潮的电气设备。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-electrical-safety-simplified-v1/sentence-013

- Source: `osha-electrical-safety-simplified-v1`
- Source case: `sentence-013`
- Split: `document`

Input:

```text
如果在潮湿的地方工作，检查电线和设备以确保它们状况良好且没有缺陷，并使用接地故障断路器(GFCI)。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-electrical-safety-simplified-v1/sentence-014

- Source: `osha-electrical-safety-simplified-v1`
- Source case: `sentence-014`
- Split: `document`

Input:

```text
在靠近通电的地方工作时，一定要谨慎小心。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-fallen-workers-family-simplified-v1/sentence-002

- Source: `osha-fallen-workers-family-simplified-v1`
- Source case: `sentence-002`
- Split: `document`

Input:

```text
我在 2009 年的一次职业事故中失去了一位亲人，因此我了解并理解你们所遭受的直接打击。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-fallen-workers-family-simplified-v1/sentence-004

- Source: `osha-fallen-workers-family-simplified-v1`
- Source case: `sentence-004`
- Split: `document`

Input:

```text
我希望通过帮助您解决有关您亲人的事故、检查过程、工人纪念日和/或 OSHA 的任何问题，来减轻您的一些担忧。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-fallen-workers-family-simplified-v1/sentence-007

- Source: `osha-fallen-workers-family-simplified-v1`
- Source case: `sentence-007`
- Split: `document`

Input:

```text
哀伤的常见阶段：否认、愤怒、纠结、抑郁、接受照顾好自己。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-fallen-workers-family-simplified-v1/sentence-008

- Source: `osha-fallen-workers-family-simplified-v1`
- Source case: `sentence-008`
- Split: `document`

Input:

```text
分享/创建纪念物品或活动。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-fallen-workers-family-simplified-v1/sentence-011

- Source: `osha-fallen-workers-family-simplified-v1`
- Source case: `sentence-011`
- Split: `document`

Input:

```text
OSHA 设立了一个虚拟的工人纪念墙，以纪念在工作中失去生命的同事。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-fallen-workers-family-simplified-v1/sentence-013

- Source: `osha-fallen-workers-family-simplified-v1`
- Source case: `sentence-013`
- Split: `document`

Input:

```text
其他 7 个州计划（康涅狄格州、伊利诺伊州、缅因州、马萨诸塞州、新泽西州、纽约州和维尔京群岛）仅涵盖州和地方政府工作人员。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-fallen-workers-family-simplified-v1/sentence-014

- Source: `osha-fallen-workers-family-simplified-v1`
- Source case: `sentence-014`
- Split: `document`

Input:

```text
须知和期望 OSHA 将对您亲人的事故进行调查，以确定是否违反了 OSHA 规定。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-fallen-workers-family-simplified-v1/sentence-015

- Source: `osha-fallen-workers-family-simplified-v1`
- Source case: `sentence-015`
- Split: `document`

Input:

```text
我们在六个月内完成调查，希望你理解。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-fallen-workers-family-simplified-v1/sentence-016

- Source: `osha-fallen-workers-family-simplified-v1`
- Source case: `sentence-016`
- Split: `document`

Input:

```text
所有罚金将直接上缴美国财政部；它们不会被当做OSHA 预算或收入。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-fallen-workers-family-simplified-v1/sentence-017

- Source: `osha-fallen-workers-family-simplified-v1`
- Source case: `sentence-017`
- Split: `document`

Input:

```text
OSHA 不会仅仅因为工作场所发生死亡事故就发出违规通知。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-fallen-workers-family-simplified-v1/sentence-020

- Source: `osha-fallen-workers-family-simplified-v1`
- Source case: `sentence-020`
- Split: `document`

Input:

```text
检查结束后，地区主管将回答你的问题并解释处理方案。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-fallen-workers-family-simplified-v1/sentence-021

- Source: `osha-fallen-workers-family-simplified-v1`
- Source case: `sentence-021`
- Split: `document`

Input:

```text
OSHA 将在结案时通知你。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-fallen-workers-family-simplified-v1/sentence-022

- Source: `osha-fallen-workers-family-simplified-v1`
- Source case: `sentence-022`
- Split: `document`

Input:

```text
《信息自由法案》（FOIA）规定了 OSHA 事故检查信息的发布。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-fallen-workers-family-simplified-v1/sentence-023

- Source: `osha-fallen-workers-family-simplified-v1`
- Source case: `sentence-023`
- Split: `document`

Input:

```text
在案件结案后，根据书面申请， OSHA 将向您提供根据《信息自由法》可以公开的部分检查档案，您作为家庭成员无需支付任何费用。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-small-business-consultation-simplified-v1/sentence-002

- Source: `osha-small-business-consultation-simplified-v1`
- Source case: `sentence-002`
- Split: `document`

Input:

```text
工地的有效安全与健康项目会让您的工人更好地，更有效率地工作，提高生产率，并确保产品质量。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-small-business-consultation-simplified-v1/sentence-004

- Source: `osha-small-business-consultation-simplified-v1`
- Source case: `sentence-004`
- Split: `document`

Input:

```text
参加OSHA现场咨询项目是一种回馈工人的方式。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-small-business-consultation-simplified-v1/sentence-005

- Source: `osha-small-business-consultation-simplified-v1`
- Source case: `sentence-005`
- Split: `document`

Input:

```text
工人安全是经营一个成功企业的必要条件。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-small-business-consultation-simplified-v1/sentence-007

- Source: `osha-small-business-consultation-simplified-v1`
- Source case: `sentence-007`
- Split: `document`

Input:

```text
小型企业可能没有预算来雇佣一个安全专家，但是这个项目可以免费提供相似的建议。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-small-business-consultation-simplified-v1/sentence-008

- Source: `osha-small-business-consultation-simplified-v1`
- Source case: `sentence-008`
- Split: `document`

Input:

```text
即使您的企业还没有经历任何与工作相关的伤亡事件，但是评估工作环境的安全隐患是很重要的。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-small-business-consultation-simplified-v1/sentence-010

- Source: `osha-small-business-consultation-simplified-v1`
- Source case: `sentence-010`
- Split: `document`

Input:

```text
告诉我们您的安全顾虑 — 咨询会帮您找出解决方案联系当地现场咨询办公室，预约一次咨询访问。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-small-business-consultation-simplified-v1/sentence-011

- Source: `osha-small-business-consultation-simplified-v1`
- Source case: `sentence-011`
- Split: `document`

Input:

```text
您的企业唯一义务是，在合理的时间内，纠正不安全，不健康的工作条件。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-small-business-consultation-simplified-v1/sentence-013

- Source: `osha-small-business-consultation-simplified-v1`
- Source case: `sentence-013`
- Split: `document`

Input:

```text
雇主，工人代表，以及顾问，三者协同详谈该企业，并找出现有的和潜在的安全隐患。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-small-business-consultation-simplified-v1/sentence-015

- Source: `osha-small-business-consultation-simplified-v1`
- Source case: `sentence-015`
- Split: `document`

Input:

```text
在结束会议上，顾问会和您，以及工人代表，一起详细查看所找出的安全隐患。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-small-business-consultation-simplified-v1/sentence-017

- Source: `osha-small-business-consultation-simplified-v1`
- Source case: `sentence-017`
- Split: `document`

Input:

```text
顾问离开后，您会收到一份详细的纸质版咨询报告总结，确认所需纠正之处。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-small-business-consultation-simplified-v1/sentence-018

- Source: `osha-small-business-consultation-simplified-v1`
- Source case: `sentence-018`
- Split: `document`

Input:

```text
若一个情况被定义为“严重”的安全隐患，顾问会帮您开展一个计划，在合理的时间框架内，纠正安全隐患，并同时保护您的工人。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-small-business-consultation-simplified-v1/sentence-019

- Source: `osha-small-business-consultation-simplified-v1`
- Source case: `sentence-019`
- Split: `document`

Input:

```text
顾问是谁? 州机关和大学都咨询安全与工业卫生专家。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-small-business-consultation-simplified-v1/sentence-021

- Source: `osha-small-business-consultation-simplified-v1`
- Source case: `sentence-021`
- Split: `document`

Input:

```text
顾问会帮您找出您企业中的安全与健康需求，并预约一个对您方便的日期。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-small-business-consultation-simplified-v1/sentence-022

- Source: `osha-small-business-consultation-simplified-v1`
- Source case: `sentence-022`
- Split: `document`

Input:

```text
求职者更看好一个拥有强大安全记录的潜在雇主。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-work-zone-traffic-simplified-v1/sentence-001

- Source: `osha-work-zone-traffic-simplified-v1`
- Source case: `sentence-001`
- Split: `document`

Input:

```text
工人在作业区的死亡或受伤，很多是由车辆或其他移动装置的撞击所导致。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-work-zone-traffic-simplified-v1/sentence-002

- Source: `osha-work-zone-traffic-simplified-v1`
- Source case: `sentence-002`
- Split: `document`

Input:

```text
作业区的交通需要通过标识、锥筒、筒和分隔物来划分、控制。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-work-zone-traffic-simplified-v1/sentence-004

- Source: `osha-work-zone-traffic-simplified-v1`
- Source case: `sentence-004`
- Split: `document`

Input:

```text
建设或拆迁工地内的交通控制方案由施工项目经理确定。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-work-zone-traffic-simplified-v1/sentence-005

- Source: `osha-work-zone-traffic-simplified-v1`
- Source case: `sentence-005`
- Split: `document`

Input:

```text
司机按照交通控制设备、信号灯和标示牌所指示的路线，在远离作业区的地方行驶。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-work-zone-traffic-simplified-v1/sentence-007

- Source: `osha-work-zone-traffic-simplified-v1`
- Source case: `sentence-007`
- Split: `document`

Input:

```text
作业区防护：各种混凝土、水马、沙袋、可折叠标识物、防撞垫和卡车减震器可以用来限制司机未经授权进入施工区域。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-work-zone-traffic-simplified-v1/sentence-008

- Source: `osha-work-zone-traffic-simplified-v1`
- Source case: `sentence-008`
- Split: `document`

Input:

```text
信号：信号旗手应穿着具有荧光背景并由反光材料制成的高可见度的工作服，这使其在任何方向至少1000英尺（300米）的范围内都可被看见。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-work-zone-traffic-simplified-v1/sentence-009

- Source: `osha-work-zone-traffic-simplified-v1`
- Source case: `sentence-009`
- Split: `document`

Input:

```text
检查标签或包装以确保服装的性能等级为2级或3级。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-work-zone-traffic-simplified-v1/sentence-010

- Source: `osha-work-zone-traffic-simplified-v1`
- Source case: `sentence-010`
- Split: `document`

Input:

```text
应警告司机前方会有信号旗手。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-work-zone-traffic-simplified-v1/sentence-011

- Source: `osha-work-zone-traffic-simplified-v1`
- Source case: `sentence-011`
- Split: `document`

Input:

```text
信号旗手应使用“停止/减速”棒、带灯的信号棒，或（仅在紧急情况下）信号旗。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-work-zone-traffic-simplified-v1/sentence-012

- Source: `osha-work-zone-traffic-simplified-v1`
- Source case: `sentence-012`
- Split: `document`

Input:

```text
照明：信号站应有良好的照明。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-work-zone-traffic-simplified-v1/sentence-013

- Source: `osha-work-zone-traffic-simplified-v1`
- Source case: `sentence-013`
- Split: `document`

Input:

```text
徒步工人和设备操作员的照度应至少为5英尺烛光（约 54勒克斯）或更高。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-work-zone-traffic-simplified-v1/sentence-014

- Source: `osha-work-zone-traffic-simplified-v1`
- Source case: `sentence-014`
- Split: `document`

Input:

```text
在现有照明不足的情况下，应使用频闪灯或燃烧棒；使用时应控制或消除眩光。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-work-zone-traffic-simplified-v1/sentence-015

- Source: `osha-work-zone-traffic-simplified-v1`
- Source case: `sentence-015`
- Split: `document`

Input:

```text
培训：信号旗手必须经过培训并经认证，且使用经授权的信号装置。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### osha-work-zone-traffic-simplified-v1/sentence-016

- Source: `osha-work-zone-traffic-simplified-v1`
- Source case: `sentence-016`
- Split: `document`

Input:

```text
行驶：应按照制造商的建议在设备和车辆上使用安全带和翻车保护装置。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```
