<!-- zhtw:disable -->
# Blind-v2 Source Classification 029

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-029.json`
Cases: 70
Seed: `20260719`
Selection: `balanced-remaining-deterministic-sha256-v1`

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

### census-newsroom-zh-hans-v1/page-01-sentence-015

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-01-sentence-015`
- Split: `press_release_01`

Input:

```text
由于州以下的各级数据和特征数据是重点，因此国会席位分配数据完成后能在第一时间开始分析。
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

### census-newsroom-zh-hans-v1/page-01-sentence-037

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-01-sentence-037`
- Split: `press_release_01`

Input:

```text
人口普查局将密切注意 2020 年人口普查的成效以及不同地域和人口群组人数的统计情况。
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

### census-newsroom-zh-hans-v1/page-02-sentence-013

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-02-sentence-013`
- Split: `press_release_02`

Input:

```text
包括所有截至 4 月 1 日在您的住宅生活和留宿的人，即使他们暂时住在别的地方也要算上他们。
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

### census-newsroom-zh-hans-v1/page-03-sentence-020

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-03-sentence-020`
- Split: `press_release_03`

Input:

```text
住房单元的当前居民。
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

### census-newsroom-zh-hans-v1/page-04-sentence-016

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-04-sentence-016`
- Split: `press_release_04`

Input:

```text
这些工作人员与社区组织合作，讲解回答 2020 年人口普查调查有多么容易、安全和重要。
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

### census-newsroom-zh-hans-v1/page-06-sentence-019

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-06-sentence-019`
- Split: `press_release_06`

Input:

```text
将为他们发放个人防护装备，并将遵循当地的使用指南准则。
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

### census-newsroom-zh-hans-v1/page-06-sentence-028

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-06-sentence-028`
- Split: `press_release_06`

Input:

```text
在过去的几个月里，CPEP 的宣传工作主要是通过虚拟的方式进行，以支持留在住宅的命令和社交疏离要求。
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

### census-newsroom-zh-hans-v1/page-07-sentence-002

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-07-sentence-002`
- Split: `press_release_07`

Input:

```text
计划明信片将在人口普查员开始拜访尚未回答住户的几个星期之前 7 月 22 日到 7 月 28 日期间送达。
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

### census-newsroom-zh-hans-v1/page-07-sentence-005

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-07-sentence-005`
- Split: `press_release_07`

Input:

```text
国家约 61.7% 的住户自从邀请在 3 月 12 日开始送达邮政信箱后已经通过在线、电话或邮件回答。
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

### census-newsroom-zh-hans-v1/page-09-sentence-004

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-09-sentence-004`
- Split: `press_release_09`

Input:

```text
我们鼓励住户在收到邀请邮包后尽快回答 2020 年人口普查。
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

### cisa-personal-security-zh-hans-v1/sentence-005

- Source: `cisa-personal-security-zh-hans-v1`
- Source case: `sentence-005`
- Split: `guide`

Input:

```text
本指南概括介绍了如何在家中、工作场所、公共场所和网上保持安全。
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

### cisa-personal-security-zh-hans-v1/sentence-019

- Source: `cisa-personal-security-zh-hans-v1`
- Source case: `sentence-019`
- Split: `guide`

Input:

```text
能够识别在哪些情况下容易受到攻击可有效避免此类情况发生或在面临威胁时做好准备。
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

### cisa-personal-security-zh-hans-v1/sentence-037

- Source: `cisa-personal-security-zh-hans-v1`
- Source case: `sentence-037`
- Split: `guide`

Input:

```text
即使仅离开几分钟，也一定要关闭车窗，拿走贵重物品并锁好车。
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

### cisa-personal-security-zh-hans-v1/sentence-046

- Source: `cisa-personal-security-zh-hans-v1`
- Source case: `sentence-046`
- Split: `guide`

Input:

```text
向警方提供任何监控录像、手机视频或照片，因为这可能有助于调查。
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

### cisa-personal-security-zh-hans-v1/sentence-049

- Source: `cisa-personal-security-zh-hans-v1`
- Source case: `sentence-049`
- Split: `guide`

Input:

```text
在让访客进入您家之前，请务必确认其身份。
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

### cisa-personal-security-zh-hans-v1/sentence-098

- Source: `cisa-personal-security-zh-hans-v1`
- Source case: `sentence-098`
- Split: `guide`

Input:

```text
此外，始终确保您的车辆有足够的燃料（如果是电动车，则有足够的电量）供您完成旅程。
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

### cisa-personal-security-zh-hans-v1/sentence-106

- Source: `cisa-personal-security-zh-hans-v1`
- Source case: `sentence-106`
- Split: `guide`

Input:

```text
请只从信誉良好的“应用程序商店”安装应用程序，以避免潜在的有害下载。
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

### cisa-personal-security-zh-hans-v1/sentence-115

- Source: `cisa-personal-security-zh-hans-v1`
- Source case: `sentence-115`
- Split: `guide`

Input:

```text
确保您使用的应用程序具有端到端加密功能。
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

### cisa-personal-security-zh-hans-v1/sentence-121

- Source: `cisa-personal-security-zh-hans-v1`
- Source case: `sentence-121`
- Split: `guide`

Input:

```text
请监测您发布的信息，并负责任地发布信息，从而确保不会有人因您公开的信息而面临风险。
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

### cisa-personal-security-zh-hans-v1/sentence-127

- Source: `cisa-personal-security-zh-hans-v1`
- Source case: `sentence-127`
- Split: `guide`

Input:

```text
针对人肉搜索的法律因辖区而异，因此在考虑预防和缓解方案时，一定要查阅所在地区的相关法律。
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

### osha-disaster-cleanup-simplified-v1/sentence-001

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-001`
- Split: `document`

Input:

```text
在灾后清理以及重建时确保工人安全自然灾害可能导致洪水的大范围泛滥，并对财产和基础设施造成破坏。
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

### osha-disaster-cleanup-simplified-v1/sentence-007

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-007`
- Split: `document`

Input:

```text
我们将会给您提供帮助。
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

### osha-disaster-cleanup-simplified-v1/sentence-015

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-015`
- Split: `document`

Input:

```text
使用防水靴、乳胶或橡胶手套和其他防护服装。
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

### osha-disaster-cleanup-simplified-v1/sentence-019

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-019`
- Split: `document`

Input:

```text
倾倒的电线接触与倒下的电力线相连接的线或物体（包括树枝）会有灼伤和触电的危险。
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

### osha-disaster-cleanup-simplified-v1/sentence-022

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-022`
- Split: `document`

Input:

```text
与所有倒下的电力线路保持至少10英尺（3米）的距离。
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

### osha-disaster-cleanup-simplified-v1/sentence-038

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-038`
- Split: `document`

Input:

```text
在湿滑且不平坦的作业面，工人可能会因滑倒、绊倒和跌倒而造成伤害。
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

### osha-disaster-cleanup-simplified-v1/sentence-044

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-044`
- Split: `document`

Input:

```text
发电机废气中有毒的一氧化碳(CO)。
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

### osha-disaster-cleanup-simplified-v1/sentence-051

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-051`
- Split: `document`

Input:

```text
穿着符合ANSI/ISEA 107-2004标准的高反光服装和安全帽。
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

### osha-disaster-cleanup-simplified-v1/sentence-056

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-056`
- Split: `document`

Input:

```text
施工活动在拆除房屋和建筑物时，接触被石棉污染的材料。
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

### osha-disaster-cleanup-simplified-v1/sentence-071

- Source: `osha-disaster-cleanup-simplified-v1`
- Source case: `sentence-071`
- Split: `document`

Input:

```text
如果工人认为他们的雇主没有遵守OSHA标准或存在严重的危险，他们可以提出投诉、让OSHA检查他们的工作场所。
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

### ready-gov-drought-zh-hans-v1/sentence-014

- Source: `ready-gov-drought-zh-hans-v1`
- Source case: `sentence-014`
- Split: `article`

Input:

```text
选择效率更高、性能更佳的设备。
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

### ready-gov-drought-zh-hans-v1/sentence-021

- Source: `ready-gov-drought-zh-hans-v1`
- Source case: `sentence-021`
- Split: `article`

Input:

```text
如果自动泵不用水时会打开和关闭，则说明在漏水。
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

### ready-gov-drought-zh-hans-v1/sentence-029

- Source: `ready-gov-drought-zh-hans-v1`
- Source case: `sentence-029`
- Split: `article`

Input:

```text
定期检查自动洒水系统和计时装置，确保能正常运行。
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

### ready-gov-drought-zh-hans-v1/sentence-030

- Source: `ready-gov-drought-zh-hans-v1`
- Source case: `sentence-030`
- Split: `article`

Input:

```text
将割草机刀片升高到至少三英寸或最高水平。
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

### ready-gov-drought-zh-hans-v1/sentence-032

- Source: `ready-gov-drought-zh-hans-v1`
- Source case: `sentence-032`
- Split: `article`

Input:

```text
种植抗旱的草种。
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

### ready-gov-drought-zh-hans-v1/sentence-050

- Source: `ready-gov-drought-zh-hans-v1`
- Source case: `sentence-050`
- Split: `article`

Input:

```text
刷牙、洗脸或剃须时，不要让水不停地流。
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

### ready-gov-drought-zh-hans-v1/sentence-052

- Source: `ready-gov-drought-zh-hans-v1`
- Source case: `sentence-052`
- Split: `article`

Input:

```text
自动洗碗机装满了再洗。
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

### ready-gov-drought-zh-hans-v1/sentence-054

- Source: `ready-gov-drought-zh-hans-v1`
- Source case: `sentence-054`
- Split: `article`

Input:

```text
手动洗碗时，用两个容器放满水，一个放肥皂水，另一个放含少量氯漂白剂的漂洗水。
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

### ready-gov-drought-zh-hans-v1/sentence-064

- Source: `ready-gov-drought-zh-hans-v1`
- Source case: `sentence-064`
- Split: `article`

Input:

```text
如果土壤仍然潮湿，则无需浇水。
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

### ready-gov-drought-zh-hans-v1/sentence-072

- Source: `ready-gov-drought-zh-hans-v1`
- Source case: `sentence-072`
- Split: `article`

Input:

```text
使用利用回收水的商用洗车场。
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

### ready-gov-home-fires-zh-hans-v1/sentence-008

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-008`
- Split: `article`

Input:

```text
烟雾和毒气比火焰造成的死亡人数更多。
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

### ready-gov-home-fires-zh-hans-v1/sentence-021

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-021`
- Split: `article`

Input:

```text
如果主要通道被火焰或烟雾挡住，要找两种离开每个房间的方法。
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

### ready-gov-home-fires-zh-hans-v1/sentence-022

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-022`
- Split: `article`

Input:

```text
确保窗户不会卡住，纱窗能快速取下，安全栏能正确打开。
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

### ready-gov-home-fires-zh-hans-v1/sentence-027

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-027`
- Split: `article`

Input:

```text
在厨房放一个灭火器。
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

### ready-gov-home-fires-zh-hans-v1/sentence-034

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-034`
- Split: `article`

Input:

```text
如果出现浓烟或火灾，准备好迅速关门。
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

### ready-gov-home-fires-zh-hans-v1/sentence-035

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-035`
- Split: `article`

Input:

```text
告诉急救人员此人所在地方。
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

### ready-gov-home-fires-zh-hans-v1/sentence-036

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-036`
- Split: `article`

Input:

```text
如有宠物困在家中，立即告诉消防员。
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

### ready-gov-home-fires-zh-hans-v1/sentence-051

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-051`
- Split: `article`

Input:

```text
保险公司以后可能需要这些收据，核实所得税索赔损失也可能需要。
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

### ready-gov-home-fires-zh-hans-v1/sentence-079

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-079`
- Split: `article`

Input:

```text
告诉孩子，火是一种工具，不是玩具，让孩子明白为什么不能玩火。
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

### ready-gov-home-fires-zh-hans-v1/sentence-081

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-081`
- Split: `article`

Input:

```text
即使时间很短，也不要让孩子无人看管靠近在用的火炉或燃烧的蜡烛。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-016

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-016`
- Split: `article`

Input:

```text
根据合格岩土工程专家的建议和/或当地市/县关于防止泥石流和洪水的指南保护您的财产。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-017

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-017`
- Split: `article`

Input:

```text
您无法阻止或改变泥石流的路径。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-024

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-024`
- Split: `article`

Input:

```text
如果您在野火燃烧区附近，请注册紧急警报并注意燃烧区的天气预报。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-032

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-032`
- Split: `article`

Input:

```text
外墙、人行道或楼梯开始远离建筑物。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-034

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-034`
- Split: `article`

Input:

```text
地下公用事业线路断裂。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-035

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-035`
- Split: `article`

Input:

```text
隆起的地面出现在斜坡的底部。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-036

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-036`
- Split: `article`

Input:

```text
水在新位置冲破地表。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-040

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-040`
- Split: `article`

Input:

```text
始终遵循当地应急管理人员的指示。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-044

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-044`
- Split: `article`

Input:

```text
请注意，当您确定泥石流即将来临时，再安全逃离就为时已晚。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-055

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-055`
- Split: `article`

Input:

```text
引导救援人员到他们的位置。
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

### ready-gov-radiation-zh-hans-v1/sentence-002

- Source: `ready-gov-radiation-zh-hans-v1`
- Source case: `sentence-002`
- Split: `article`

Input:

```text
辐射紧急情况的一些例子包括：核爆炸（爆炸）、核电站事故、涉及运输放射性材料的运输事故，或在医疗保健或研究环境的职业中暴露。
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

### ready-gov-radiation-zh-hans-v1/sentence-009

- Source: `ready-gov-radiation-zh-hans-v1`
- Source case: `sentence-009`
- Split: `article`

Input:

```text
下载FEMA应用程序并从国家气象局接收全国最多五个地点的实时警报。
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

### ready-gov-radiation-zh-hans-v1/sentence-022

- Source: `ready-gov-radiation-zh-hans-v1`
- Source case: `sentence-022`
- Split: `article`

Input:

```text
进入室内：如果警告可能存在辐射危害，请立即进入最近的建筑物并远离窗户。
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

### ready-gov-radiation-zh-hans-v1/sentence-023

- Source: `ready-gov-radiation-zh-hans-v1`
- Source case: `sentence-023`
- Split: `article`

Input:

```text
在您和外界之间放置尽可能多的墙，以保护您免受外界辐射。
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

### ready-gov-radiation-zh-hans-v1/sentence-028

- Source: `ready-gov-radiation-zh-hans-v1`
- Source case: `sentence-028`
- Split: `article`

Input:

```text
如果您在室外，请面朝下躺下，以保护裸露的皮肤免受高温和飞扬的碎屑的伤害。
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

### ready-gov-radiation-zh-hans-v1/sentence-031

- Source: `ready-gov-radiation-zh-hans-v1`
- Source case: `sentence-031`
- Split: `article`

Input:

```text
如果在爆炸后的几分钟内可以安全到达多层建筑或地下室，请立即前往。
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

### ready-gov-radiation-zh-hans-v1/sentence-033

- Source: `ready-gov-radiation-zh-hans-v1`
- Source case: `sentence-033`
- Split: `article`

Input:

```text
地下停车场和地铁也可以提供良好的庇护所。
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

### ready-gov-radiation-zh-hans-v1/sentence-038

- Source: `ready-gov-radiation-zh-hans-v1`
- Source case: `sentence-038`
- Split: `article`

Input:

```text
关闭壁炉阻尼器。
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

### ready-gov-radiation-zh-hans-v1/sentence-059

- Source: `ready-gov-radiation-zh-hans-v1`
- Source case: `sentence-059`
- Split: `article`

Input:

```text
来自室外的未密封食品可能被放射性物质污染。
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

### ready-gov-radiation-zh-hans-v1/sentence-064

- Source: `ready-gov-radiation-zh-hans-v1`
- Source case: `sentence-064`
- Split: `article`

Input:

```text
PrepTalks：Brooke Buddemeier“在核爆炸后挽救生命”。
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
