<!-- zhtw:disable -->
# Blind-v2 Source Classification 037

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-037.json`
Cases: 96
Seed: `20260719`
Selection: `balanced-source-class-remaining-deterministic-sha256-v1`

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

### census-newsroom-zh-hans-v1/page-01-sentence-012

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-01-sentence-012`
- Split: `press_release_01`

Input:

```text
人口普查局还与独立的外部机构合作评估 2020 年人口普查的质量。
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

### census-newsroom-zh-hans-v1/page-01-sentence-013

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-01-sentence-013`
- Split: `press_release_01`

Input:

```text
具备特定技术和主题技能的外部专家小组将向人口普查局给出质量评估方面的建议，包括围绕 2020 年人口普查数据质量审查和评估机构的计划、流程、步骤和拟定的指标。
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

### census-newsroom-zh-hans-v1/page-01-sentence-021

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-01-sentence-021`
- Split: `press_release_01`

Input:

```text
在线回答语言选项的成效。
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

### census-newsroom-zh-hans-v1/page-01-sentence-032

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-01-sentence-032`
- Split: `press_release_01`

Input:

```text
这些估算将在 2021 年和 2022 年出台。
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

### census-newsroom-zh-hans-v1/page-02-sentence-017

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-02-sentence-017`
- Split: `press_release_02`

Input:

```text
但是，如果他们住在校外的私人住宅或公寓里，即使他们应该使用校外地址自行回答人口普查，即使当前暂时居住别处也应如此。
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

### census-newsroom-zh-hans-v1/page-06-sentence-007

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-06-sentence-007`
- Split: `press_release_06`

Input:

```text
人口普查员将更新人口普查局的地址名单，其包括部分 Maine 北部地区和 Alaska 东南部的偏远地区，也将与住户进行 2020 年人口普查访谈。
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

### census-newsroom-zh-hans-v1/page-07-sentence-004

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-07-sentence-004`
- Split: `press_release_07`

Input:

```text
现在回答将使人口普查员拜访住宅亲自收集答案的必要性降到最低。
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

### census-newsroom-zh-hans-v1/page-08-sentence-011

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-08-sentence-011`
- Split: `press_release_08`

Input:

```text
“人口统计分析使我们能够利用现有的数据，例如当前和历史管理记录及问卷调查数据，来估计人口的规模，”人口司人口分析资深技术专家 Eric Jensen 说：“自 1960 年人口普查以来，我们一直在进行人口统计分析。
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

### census-newsroom-zh-hans-v1/page-08-sentence-012

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-08-sentence-012`
- Split: `press_release_08`

Input:

```text
随着时间的推移，我们的估计不仅得益于方法的改进，而且得益于现有管理记录的改进。
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

### census-newsroom-zh-hans-v1/page-08-sentence-022

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-08-sentence-022`
- Split: `press_release_08`

Input:

```text
预计在 2021 年 11 月发布普查后问卷调查的覆盖率估计。
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

### census-newsroom-zh-hans-v1/page-09-sentence-003

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-09-sentence-003`
- Split: `press_release_09`

Input:

```text
明信片还提供了如何通过在线或电话回答 2020 年人口普查的信息。
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

### massive-1-0-zh-cn-v1/10643

- Source: `massive-1-0-zh-cn-v1`
- Source case: `10643`
- Split: `train`

Input:

```text
清单上的最后一项漏了
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

### massive-1-0-zh-cn-v1/10647

- Source: `massive-1-0-zh-cn-v1`
- Source case: `10647`
- Split: `train`

Input:

```text
把清洁小狗放在清洁清单最上面
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

### massive-1-0-zh-cn-v1/11313

- Source: `massive-1-0-zh-cn-v1`
- Source case: `11313`
- Split: `train`

Input:

```text
我想看上一集
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

### massive-1-0-zh-cn-v1/11819

- Source: `massive-1-0-zh-cn-v1`
- Source case: `11819`
- Split: `dev`

Input:

```text
帮我找一个卖啤酒的店
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

### massive-1-0-zh-cn-v1/12507

- Source: `massive-1-0-zh-cn-v1`
- Source case: `12507`
- Split: `train`

Input:

```text
我要一张去俄勒冈的火车票
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

### massive-1-0-zh-cn-v1/12646

- Source: `massive-1-0-zh-cn-v1`
- Source case: `12646`
- Split: `train`

Input:

```text
火车什么时候离开宾州车站
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

### massive-1-0-zh-cn-v1/12714

- Source: `massive-1-0-zh-cn-v1`
- Source case: `12714`
- Split: `train`

Input:

```text
马上订辆优步在长岛酒吧外接我
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

### massive-1-0-zh-cn-v1/13305

- Source: `massive-1-0-zh-cn-v1`
- Source case: `13305`
- Split: `train`

Input:

```text
小度把我的家务做了让我好打个盹
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

### massive-1-0-zh-cn-v1/13515

- Source: `massive-1-0-zh-cn-v1`
- Source case: `13515`
- Split: `dev`

Input:

```text
一个地球日是多长时间
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

### massive-1-0-zh-cn-v1/13519

- Source: `massive-1-0-zh-cn-v1`
- Source case: `13519`
- Split: `dev`

Input:

```text
谁在披头士乐队
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

### massive-1-0-zh-cn-v1/13538

- Source: `massive-1-0-zh-cn-v1`
- Source case: `13538`
- Split: `train`

Input:

```text
你能描述一下她在那部电影里的穿着吗
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

### massive-1-0-zh-cn-v1/142

- Source: `massive-1-0-zh-cn-v1`
- Source case: `142`
- Split: `train`

Input:

```text
那是一首好歌
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

### massive-1-0-zh-cn-v1/14485

- Source: `massive-1-0-zh-cn-v1`
- Source case: `14485`
- Split: `train`

Input:

```text
一美元在加拿大是多少
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

### massive-1-0-zh-cn-v1/14861

- Source: `massive-1-0-zh-cn-v1`
- Source case: `14861`
- Split: `dev`

Input:

```text
如果我有五美元那澳元是多少
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

### massive-1-0-zh-cn-v1/15711

- Source: `massive-1-0-zh-cn-v1`
- Source case: `15711`
- Split: `train`

Input:

```text
消费者发微博
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

### massive-1-0-zh-cn-v1/15989

- Source: `massive-1-0-zh-cn-v1`
- Source case: `15989`
- Split: `train`

Input:

```text
这个人发过任何电子邮件吗
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

### massive-1-0-zh-cn-v1/16155

- Source: `massive-1-0-zh-cn-v1`
- Source case: `16155`
- Split: `train`

Input:

```text
李雷的地址是什么
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

### massive-1-0-zh-cn-v1/16944

- Source: `massive-1-0-zh-cn-v1`
- Source case: `16944`
- Split: `test`

Input:

```text
给奶奶发封电子邮件说我们星期六来拜访到时候见
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

### massive-1-0-zh-cn-v1/2319

- Source: `massive-1-0-zh-cn-v1`
- Source case: `2319`
- Split: `train`

Input:

```text
关闭电源灯
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

### massive-1-0-zh-cn-v1/3559

- Source: `massive-1-0-zh-cn-v1`
- Source case: `3559`
- Split: `train`

Input:

```text
切换到我的运动歌单
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

### massive-1-0-zh-cn-v1/3661

- Source: `massive-1-0-zh-cn-v1`
- Source case: `3661`
- Split: `train`

Input:

```text
设置一个早上的闹铃
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

### massive-1-0-zh-cn-v1/5987

- Source: `massive-1-0-zh-cn-v1`
- Source case: `5987`
- Split: `train`

Input:

```text
帮我们从兰州拉面点新疆炒面
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

### massive-1-0-zh-cn-v1/6268

- Source: `massive-1-0-zh-cn-v1`
- Source case: `6268`
- Split: `test`

Input:

```text
如果为了救三个人你必须杀一个人你会这样做吗如果会告诉我为什么
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

### massive-1-0-zh-cn-v1/6334

- Source: `massive-1-0-zh-cn-v1`
- Source case: `6334`
- Split: `train`

Input:

```text
olly 我今天度过了最糟糕的一天
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

### massive-1-0-zh-cn-v1/6921

- Source: `massive-1-0-zh-cn-v1`
- Source case: `6921`
- Split: `train`

Input:

```text
设定一个通知三月十一号与罗德里格斯先生有个面试
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

### massive-1-0-zh-cn-v1/7053

- Source: `massive-1-0-zh-cn-v1`
- Source case: `7053`
- Split: `train`

Input:

```text
下周二上午十一点到下午三点之间有什么日程事项吗
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

### massive-1-0-zh-cn-v1/7986

- Source: `massive-1-0-zh-cn-v1`
- Source case: `7986`
- Split: `train`

Input:

```text
你能删除这个晚餐聚会吗
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

### massive-1-0-zh-cn-v1/8090

- Source: `massive-1-0-zh-cn-v1`
- Source case: `8090`
- Split: `train`

Input:

```text
我的星期六预约的时间是几点
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

### massive-1-0-zh-cn-v1/8847

- Source: `massive-1-0-zh-cn-v1`
- Source case: `8847`
- Split: `dev`

Input:

```text
提醒我带上我的雨衣因为会下雨
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

### massive-1-0-zh-cn-v1/8883

- Source: `massive-1-0-zh-cn-v1`
- Source case: `8883`
- Split: `train`

Input:

```text
给我的生日设置一个提示
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

### massive-1-0-zh-cn-v1/9557

- Source: `massive-1-0-zh-cn-v1`
- Source case: `9557`
- Split: `train`

Input:

```text
目前电视上观众选择最多的节目是什么
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

### massive-1-0-zh-cn-v1/9835

- Source: `massive-1-0-zh-cn-v1`
- Source case: `9835`
- Split: `train`

Input:

```text
音乐一
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

### ready-gov-home-fires-zh-hans-v1/sentence-004

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-004`
- Split: `article`

Input:

```text
热量比火焰更具威胁性。
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

### ready-gov-home-fires-zh-hans-v1/sentence-014

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-014`
- Split: `article`

Input:

```text
烹饪时切勿停用烟雾报警器，因为可能致命。
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

### ready-gov-home-fires-zh-hans-v1/sentence-032

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-032`
- Split: `article`

Input:

```text
开门前先摸门把手和门。
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

### ready-gov-home-fires-zh-hans-v1/sentence-033

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-033`
- Split: `article`

Input:

```text
如果其中一个很热，或门周围有烟出来，不要开门，用第二条出路。
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

### ready-gov-home-fires-zh-hans-v1/sentence-037

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-037`
- Split: `article`

Input:

```text
如果出不去，关上门，用布或胶带盖住门周围的通风口和裂缝，以防烟雾进入。
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

### ready-gov-home-fires-zh-hans-v1/sentence-044

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-044`
- Split: `article`

Input:

```text
如需临时住所、食物和药品，联系当地救灾服务机构（如红十字会）。
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

### ready-gov-home-fires-zh-hans-v1/sentence-046

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-046`
- Split: `article`

Input:

```text
切勿自己尝试重新连接公用设施。
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

### ready-gov-home-fires-zh-hans-v1/sentence-067

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-067`
- Split: `article`

Input:

```text
每天给圣诞树浇水，不要让它干涸。
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

### ready-gov-home-fires-zh-hans-v1/sentence-068

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-068`
- Split: `article`

Input:

```text
干燥的树更易燃。
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

### ready-gov-home-fires-zh-hans-v1/sentence-080

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-080`
- Split: `article`

Input:

```text
将火柴和打火机放在孩子够不到也看不见的地方，最好放在上锁的柜子里。
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

### ready-gov-home-fires-zh-hans-v1/sentence-083

- Source: `ready-gov-home-fires-zh-hans-v1`
- Source case: `sentence-083`
- Split: `article`

Input:

```text
这会增加火灾和烧伤的风险，并可能损坏电器。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-006

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-006`
- Split: `article`

Input:

```text
土地利用分区、专业检查和适当的设计可以减少许多滑坡问题，但疏散通常是保护生命免受泥石流或其他快速移动的滑坡伤害的唯一方法。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-008

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-008`
- Split: `article`

Input:

```text
一些缓慢移动的山体滑坡以蜗牛的速度移动，停止和开始，并且每年前进不超过三英尺。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-010

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-010`
- Split: `article`

Input:

```text
制定一个计划，包括您的宠物，以便您和您的家人知道在发生山体滑坡时该做什么以及该去哪里。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-013

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-013`
- Split: `article`

Input:

```text
如果您被告知要撤离，或者您觉得留在家里不安全，请离开。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-030

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-030`
- Split: `article`

Input:

```text
门或窗第一次粘住或卡住。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-033

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-033`
- Split: `article`

Input:

```text
地面或街道或车道等铺砌区域出现缓慢发展、扩大的裂缝。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-042

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-042`
- Split: `article`

Input:

```text
在可能导致山体滑坡的暴风雨中保持警惕和清醒。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-048

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-048`
- Split: `article`

Input:

```text
危险时避开河谷和低洼地带。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-054

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-054`
- Split: `article`

Input:

```text
在不进入直接滑道区域的情况下，检查滑道附近是否有受伤和被困人员。
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

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-056

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-056`
- Split: `article`

Input:

```text
向有关当局报告断裂的公用事业线路以及损坏的公路和铁路。
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

### zhtw-project-it-llm-social-guard-v1/it-001

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-001`
- Split: `project_original`

Input:

```text
服务器返回 HTTP 429 时，客户端必须读取 Retry-After 标头。
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

### zhtw-project-it-llm-social-guard-v1/it-002

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-002`
- Split: `project_original`

Input:

```text
请求路径 /v1/orders/{order_id} 中的参数名称不能改写。
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

### zhtw-project-it-llm-social-guard-v1/it-010

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-010`
- Split: `project_original`

Input:

```text
CI 工作流使用 ubuntu-24.04 作为固定运行环境。
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

### zhtw-project-it-llm-social-guard-v1/it-018

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-018`
- Split: `project_original`

Input:

```text
配置文件将 feature.new_checkout 设为 false。
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

### zhtw-project-it-llm-social-guard-v1/it-019

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-019`
- Split: `project_original`

Input:

```text
执行 SELECT ... FOR UPDATE 时要留意锁等待时间。
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

### zhtw-project-it-llm-social-guard-v1/it-022

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-022`
- Split: `project_original`

Input:

```text
备份文件命名为 customer-db_2026-07-28.sql.gz。
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

### zhtw-project-it-llm-social-guard-v1/it-028

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-028`
- Split: `project_original`

Input:

```text
JSON Schema 使用 additionalProperties: false 限制未知字段。
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

### zhtw-project-it-llm-social-guard-v1/it-029

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-029`
- Split: `project_original`

Input:

```text
S3 对象键 reports/2026/Q3/summary.csv 区分大小写。
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

### zhtw-project-it-llm-social-guard-v1/it-030

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-030`
- Split: `project_original`

Input:

```text
请确认 gRPC 方法 BillingService/CreateInvoice 已注册。
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

### zhtw-project-it-llm-social-guard-v1/it-036

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-036`
- Split: `project_original`

Input:

```text
请将时区标识 Asia/Taipei 写入排程配置。
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

### zhtw-project-it-llm-social-guard-v1/it-038

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-038`
- Split: `project_original`

Input:

```text
事件载荷的 schema_version 当前固定为 2.1。
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

### zhtw-project-it-llm-social-guard-v1/it-040

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-040`
- Split: `project_original`

Input:

```text
浏览器将 SameSite=None 与 Secure 属性一起发送。
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

### zhtw-project-it-llm-social-guard-v1/llm-002

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `llm-002`
- Split: `project_original`

Input:

```text
检索器只返回相关性最高的五段内容，再交给模型整理。
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

### zhtw-project-it-llm-social-guard-v1/llm-010

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `llm-010`
- Split: `project_original`

Input:

```text
模型上线前要完成离线评估和小流量灰度测试。
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

### zhtw-project-it-llm-social-guard-v1/llm-011

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `llm-011`
- Split: `project_original`

Input:

```text
向量数据库重建索引期间，线上查询仍使用旧版本。
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

### zhtw-project-it-llm-social-guard-v1/llm-013

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `llm-013`
- Split: `project_original`

Input:

```text
评审界面会隐藏产品输出，避免影响人工判断。
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

### zhtw-project-it-llm-social-guard-v1/llm-016

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `llm-016`
- Split: `project_original`

Input:

```text
如果输入包含多个任务，助手应先确认执行顺序。
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

### zhtw-project-it-llm-social-guard-v1/llm-018

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `llm-018`
- Split: `project_original`

Input:

```text
语音转写结果中的人名需要与联系人资料再次核对。
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

### zhtw-project-it-llm-social-guard-v1/llm-022

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `llm-022`
- Split: `project_original`

Input:

```text
请把会议记录整理成行动项目，并标出负责人。
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

### zhtw-project-it-llm-social-guard-v1/llm-024

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `llm-024`
- Split: `project_original`

Input:

```text
多轮对话超过保存范围后，较早的消息会被移除。
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

### zhtw-project-it-llm-social-guard-v1/llm-026

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `llm-026`
- Split: `project_original`

Input:

```text
批量评估完成后，报告会列出通过、失败和跳过的数量。
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

### zhtw-project-it-llm-social-guard-v1/llm-028

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `llm-028`
- Split: `project_original`

Input:

```text
编辑人员修正实体名称后，系统会重新生成摘要。
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

### zhtw-project-it-llm-social-guard-v1/llm-029

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `llm-029`
- Split: `project_original`

Input:

```text
低信心的分类结果会进入人工复核队列。
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

### zhtw-project-it-llm-social-guard-v1/social-002

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `social-002`
- Split: `project_original`

Input:

```text
周末想去看《海角七号》，先确认光点华山的场次。
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

### zhtw-project-it-llm-social-guard-v1/social-003

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `social-003`
- Split: `project_original`

Input:

```text
王先生把 ThinkPad X1 Carbon 忘在会议室了。
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

### zhtw-project-it-llm-social-guard-v1/social-004

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `social-004`
- Split: `project_original`

Input:

```text
这张发票的统一编号是 AB-20260728，请不要改动。
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

### zhtw-project-it-llm-social-guard-v1/social-006

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `social-006`
- Split: `project_original`

Input:

```text
请把照片传到群组「暑假旅行 2026」，不要传错地方。
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

### zhtw-project-it-llm-social-guard-v1/social-009

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `social-009`
- Split: `project_original`

Input:

```text
捷运红线在中山站临时停靠较久，请预留时间。
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

### zhtw-project-it-llm-social-guard-v1/social-011

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `social-011`
- Split: `project_original`

Input:

```text
陈医师提醒我按药袋上的指示服用，不要自行加量。
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

### zhtw-project-it-llm-social-guard-v1/social-019

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `social-019`
- Split: `project_original`

Input:

```text
民宿主人说钥匙放在 FamilyMart 店到店柜台。
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

### zhtw-project-it-llm-social-guard-v1/social-026

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `social-026`
- Split: `project_original`

Input:

```text
请把文件放进 Google Drive 的 Shared with me 文件夹。
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

### zhtw-project-it-llm-social-guard-v1/social-028

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `social-028`
- Split: `project_original`

Input:

```text
票券上的活动代码 TW-EXPO-2026 必须完整显示。
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
