<!-- zhtw:disable -->
# Blind-v2 Source Classification 035

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-035.json`
Cases: 96
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

### census-newsroom-zh-hans-v1/page-01-sentence-003

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-01-sentence-003`
- Split: `press_release_01`

Input:

```text
鉴于 2020 年人口普查面临新冠病毒 COVID-19 疫情传播带来的特殊挑战，人口普查局计划发布更多数据质量指标。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-01-sentence-010

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-01-sentence-010`
- Split: `press_release_01`

Input:

```text
这些指标是对人口普查局已经为 2020 年人口普查提供的早期指标的补充，包括细化到普查区域水平的自己回答率(仅英语)、州 (state) 一级的初始完成率(仅英语)、地区人口普查办公室 (Area Census Office) 的 NRFU 工作量完成率(仅英语)、和国家管理记录与代理人受访者(仅英语)普查率。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-01-sentence-029

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-01-sentence-029`
- Split: `press_release_01`

Input:

```text
这些估算是使用当前和原有的出生与死亡记录、国际人口迁移数据和医疗记录创建的。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-01-sentence-030

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-01-sentence-030`
- Split: `press_release_01`

Input:

```text
它们完全独立于 2020 年人口普查人数。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-02-sentence-002

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-02-sentence-002`
- Split: `press_release_02`

Input:

```text
美国宪法强制规定每十年开展一次人口普查。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-02-sentence-015

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-02-sentence-015`
- Split: `press_release_02`

Input:

```text
在大学生上学的地址算上大学生。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-02-sentence-018

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-02-sentence-018`
- Split: `press_release_02`

Input:

```text
要了解关于“算上谁”问题的更多答案，请访问 2020 Census。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-02-sentence-021

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-02-sentence-021`
- Split: `press_release_02`

Input:

```text
现在就回答，最大限度地减少人口普查员在今年晚些时候拜访您的住宅对您跟进访谈。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-02-sentence-023

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-02-sentence-023`
- Split: `press_release_02`

Input:

```text
所有尚未在线回答的住户都将在 4 月 8 日到 16 日之间收到一份纸质问卷。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-03-sentence-009

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-03-sentence-009`
- Split: `press_release_03`

Input:

```text
将于 6 月底将宣布这 6 个地区人口普查办公室 (area census offices)。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-03-sentence-012

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-03-sentence-012`
- Split: `press_release_03`

Input:

```text
将为所有人口普查员进行社交疏离规则培训。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-03-sentence-015

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-03-sentence-015`
- Split: `press_release_03`

Input:

```text
重新访谈是为了确认每一个人口普查员都接受了我们的培训，并正确地完成了他们的工作。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-03-sentence-016

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-03-sentence-016`
- Split: `press_release_03`

Input:

```text
重新访谈将由不同的人口普查人员进行，而不是最初访问该住户的人。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-04-sentence-001

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-04-sentence-001`
- Split: `press_release_04`

Input:

```text
2020 年 3 月 9 日 — 2020 年人口普查的邀请本周开始陆续送达住户的邮政信箱，美国人口普查局希望您知道一个事实，即您现在可以用比以往任何时候都更多的语言来回答。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-04-sentence-007

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-04-sentence-007`
- Split: `press_release_04`

Input:

```text
不太可能在线回答的住户也将在首次邀请中收到纸质问卷。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-04-sentence-010

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-04-sentence-010`
- Split: `press_release_04`

Input:

```text
从 5 月中旬开始，全国各地的人口普查员将走访那些没有回答的住户，亲自收集答案。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-05-sentence-005

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-05-sentence-005`
- Split: `press_release_05`

Input:

```text
人口普查员将按计划从八月开始拜访尚未回答 2020 年人口普查的住户。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-05-sentence-006

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-05-sentence-006`
- Split: `press_release_05`

Input:

```text
从 5 月 4 日那周开始，人口普查局与联邦、州 (state)和地方卫生官员协调，在选定地理区域分阶段地重新恢复部分2020 年人口普查的外勤操作。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-05-sentence-010

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-05-sentence-010`
- Split: `press_release_05`

Input:

```text
所有复工的工作人员都将得到关于社交疏离规则的安全培训，并在重新开始工作前收到个人防护装备。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-06-sentence-006

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-06-sentence-006`
- Split: `press_release_06`

Input:

```text
人口普查局将在 6 月 14 日继续更新/普查操作。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-06-sentence-012

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-06-sentence-012`
- Split: `press_release_06`

Input:

```text
人口普查局将逐渐开始软启动未回复随访。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-06-sentence-022

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-06-sentence-022`
- Split: `press_release_06`

Input:

```text
截止 6 月 11 日，78% 的 Alaska 偏远地区工作已经完成。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-06-sentence-038

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-06-sentence-038`
- Split: `press_release_06`

Input:

```text
此外，人口普查局扩大了媒体供应商列表，通过在数字、印刷、电视和无线电广播平台上的付费广告扩大了人口普查局对历来被低估的人口的影响。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-07-sentence-001

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-07-sentence-001`
- Split: `press_release_07`

Input:

```text
2020 年 6 月24日 — 美国人口普查局今日宣布人口普查局将向尚未回答 2020 年人口普查的住户发送额外提醒明信片。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-07-sentence-007

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-07-sentence-007`
- Split: `press_release_07`

Input:

```text
明信片 – 计划于 6 月底发送 – 警示住户人口普查员将上门递送人口普查邀请或者会与他们进行访谈。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-07-sentence-009

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-07-sentence-009`
- Split: `press_release_07`

Input:

```text
新冠病毒 (COVID-19) 疫情大流行推迟了向一些社区发送普查邀请的时间，但人口普查员已重新开始分阶段在全国各地投递邀请函。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-07-sentence-010

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-07-sentence-010`
- Split: `press_release_07`

Input:

```text
我们鼓励住户在收到邀请邮包后尽快回答 2020 年的人口普查。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-08-sentence-001

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-08-sentence-001`
- Split: `press_release_08`

Input:

```text
2020 年 12 月 15 日 — 美国人口普查局今天发布了 2020 年人口分析报告，该报告提供了截至 2020 年 4 月 1 日国家人口的一系列的低、中和高估计值。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-08-sentence-002

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-08-sentence-002`
- Split: `press_release_08`

Input:

```text
人口统计分析不是像 2020 年人口普查那样从住户收集答案，而是使用当前和历史的重要统计数据记录和其他数据来估计美国人口的规模。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-08-sentence-005

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-08-sentence-005`
- Split: `press_release_08`

Input:

```text
“人口分析是一个有价值的资源，可以帮助我们分析 2020 年人口普查人口人数的完整性。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-08-sentence-032

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-08-sentence-032`
- Split: `press_release_08`

Input:

```text
三组值中总人口中的性别比例（每 100 个女性的男性人数）均为 98.1。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-08-sentence-037

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-08-sentence-037`
- Split: `press_release_08`

Input:

```text
2020 年人口分析主页(仅英语) 有完整的表格。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/10036

- Source: `massive-1-0-zh-cn-v1`
- Source case: `10036`
- Split: `train`

Input:

```text
如何煮黄米饭
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/10510

- Source: `massive-1-0-zh-cn-v1`
- Source case: `10510`
- Split: `train`

Input:

```text
我有的清单
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/10567

- Source: `massive-1-0-zh-cn-v1`
- Source case: `10567`
- Split: `train`

Input:

```text
删除杂货清单
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/11073

- Source: `massive-1-0-zh-cn-v1`
- Source case: `11073`
- Split: `train`

Input:

```text
把存款支票从必做清单里移除
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/11186

- Source: `massive-1-0-zh-cn-v1`
- Source case: `11186`
- Split: `test`

Input:

```text
我有我的衣服清单
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/11286

- Source: `massive-1-0-zh-cn-v1`
- Source case: `11286`
- Split: `test`

Input:

```text
播放年轻的土耳其人播客
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/11552

- Source: `massive-1-0-zh-cn-v1`
- Source case: `11552`
- Split: `dev`

Input:

```text
更多更清晰和以主题为导向
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/11811

- Source: `massive-1-0-zh-cn-v1`
- Source case: `11811`
- Split: `train`

Input:

```text
光明大剧院正在上映什么
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/1197

- Source: `massive-1-0-zh-cn-v1`
- Source case: `1197`
- Split: `dev`

Input:

```text
会下雨吗
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/11973

- Source: `massive-1-0-zh-cn-v1`
- Source case: `11973`
- Split: `train`

Input:

```text
跳蚤市场
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/12027

- Source: `massive-1-0-zh-cn-v1`
- Source case: `12027`
- Split: `train`

Input:

```text
在西部地区举行的巡回竞赛
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/12238

- Source: `massive-1-0-zh-cn-v1`
- Source case: `12238`
- Split: `train`

Input:

```text
我怎么去科德角
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/12312

- Source: `massive-1-0-zh-cn-v1`
- Source case: `12312`
- Split: `train`

Input:

```text
考虑到公园大道
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/12815

- Source: `massive-1-0-zh-cn-v1`
- Source case: `12815`
- Split: `train`

Input:

```text
告诉我的最近的银行的位置
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/12867

- Source: `massive-1-0-zh-cn-v1`
- Source case: `12867`
- Split: `train`

Input:

```text
请用优步
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/13281

- Source: `massive-1-0-zh-cn-v1`
- Source case: `13281`
- Split: `dev`

Input:

```text
我想给我的妻子写一些原创的浪漫的短信
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/1342

- Source: `massive-1-0-zh-cn-v1`
- Source case: `1342`
- Split: `train`

Input:

```text
这是我最喜欢的歌
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/13642

- Source: `massive-1-0-zh-cn-v1`
- Source case: `13642`
- Split: `train`

Input:

```text
请定义纹理
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/13721

- Source: `massive-1-0-zh-cn-v1`
- Source case: `13721`
- Split: `train`

Input:

```text
加币兑美元的汇率
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/1379

- Source: `massive-1-0-zh-cn-v1`
- Source case: `1379`
- Split: `test`

Input:

```text
必胜客有外卖吗
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/14267

- Source: `massive-1-0-zh-cn-v1`
- Source case: `14267`
- Split: `dev`

Input:

```text
六减四等于多少
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/15452

- Source: `massive-1-0-zh-cn-v1`
- Source case: `15452`
- Split: `train`

Input:

```text
请发微博说中国电信客户服务很糟糕
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/156

- Source: `massive-1-0-zh-cn-v1`
- Source case: `156`
- Split: `train`

Input:

```text
调低亮度
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/16604

- Source: `massive-1-0-zh-cn-v1`
- Source case: `16604`
- Split: `train`

Input:

```text
给女儿发送电子邮件
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/16860

- Source: `massive-1-0-zh-cn-v1`
- Source case: `16860`
- Split: `train`

Input:

```text
我一周前发送邮件给家明请告诉我写了什么
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/2282

- Source: `massive-1-0-zh-cn-v1`
- Source case: `2282`
- Split: `dev`

Input:

```text
把我房子里所有的灯都设置成蓝色
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/3363

- Source: `massive-1-0-zh-cn-v1`
- Source case: `3363`
- Split: `train`

Input:

```text
一位神父走进一间酒吧
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/3662

- Source: `massive-1-0-zh-cn-v1`
- Source case: `3662`
- Split: `train`

Input:

```text
创建下午五点的闹钟
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/6035

- Source: `massive-1-0-zh-cn-v1`
- Source case: `6035`
- Split: `dev`

Input:

```text
开启闹钟
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/6126

- Source: `massive-1-0-zh-cn-v1`
- Source case: `6126`
- Split: `train`

Input:

```text
我需要穿外套吗
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/6826

- Source: `massive-1-0-zh-cn-v1`
- Source case: `6826`
- Split: `train`

Input:

```text
添加重复事项周六上午七点为看电影时间
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### massive-1-0-zh-cn-v1/6890

- Source: `massive-1-0-zh-cn-v1`
- Source case: `6890`
- Split: `train`

Input:

```text
告诉我演出时间是什么时候
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/llm-003

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `llm-003`
- Split: `project_original`

Input:

```text
系统会保存最近十轮对话，超过范围的消息不会传给模型。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/llm-004

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `llm-004`
- Split: `project_original`

Input:

```text
评估报告分别列出准确率、召回率和无法作答的比例。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/llm-007

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `llm-007`
- Split: `project_original`

Input:

```text
提示词要求模型先识别语言，再按照指定格式输出 JSON。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/llm-009

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `llm-009`
- Split: `project_original`

Input:

```text
这个工作流会先调用搜索工具，再根据来源生成带引用的回答。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/llm-010

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `llm-010`
- Split: `project_original`

Input:

```text
管理员可以查看令牌用量，但看不到对话中的敏感字段。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/llm-013

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `llm-013`
- Split: `project_original`

Input:

```text
批量任务完成后，页面会显示成功、失败和跳过的记录数。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/llm-017

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `llm-017`
- Split: `project_original`

Input:

```text
语音转写把专有名词听错了，编辑可以直接修改文字稿。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/llm-023

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `llm-023`
- Split: `project_original`

Input:

```text
自动评分器认为格式正确，不代表回答内容一定准确。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/llm-024

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `llm-024`
- Split: `project_original`

Input:

```text
训练资料包含重复样本时，验证分数可能被高估。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/llm-036

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `llm-036`
- Split: `project_original`

Input:

```text
多模态输入包含图片和文字，缺少任一部分都可能影响判断。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/llm-038

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `llm-038`
- Split: `project_original`

Input:

```text
请维持 SQL 查询原样，只解释各个条件的用途。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/llm-039

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `llm-039`
- Split: `project_original`

Input:

```text
模型建议的补丁尚未执行，必须先通过测试和代码审查。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/llm-040

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `llm-040`
- Split: `project_original`

Input:

```text
分段策略改变后，检索到的上下文顺序也发生了变化。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/llm-041

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `llm-041`
- Split: `project_original`

Input:

```text
请识别客服对话中的主要诉求，不要推测用户的身份。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/llm-043

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `llm-043`
- Split: `project_original`

Input:

```text
生成图片前，系统会检查提示内容是否符合使用政策。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/llm-050

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `llm-050`
- Split: `project_original`

Input:

```text
请为每项建议注明依据，无法验证的部分标记为未知。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/social-003

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `social-003`
- Split: `project_original`

Input:

```text
快递放在管理处了，下班回家时记得领取。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/social-005

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `social-005`
- Split: `project_original`

Input:

```text
明天可能下雨，我们把聚会改到室内吧。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/social-007

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `social-007`
- Split: `project_original`

Input:

```text
这部电影前半段很慢，后面的节奏就好多了。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/social-011

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `social-011`
- Split: `project_original`

Input:

```text
这双鞋尺寸刚好，但走久了脚后跟会有点痛。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/social-012

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `social-012`
- Split: `project_original`

Input:

```text
朋友推荐的咖啡店搬家了，地图上的地址还没更新。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/social-015

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `social-015`
- Split: `project_original`

Input:

```text
房间的空调声音有点大，晚上睡觉会听见。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/social-018

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `social-018`
- Split: `project_original`

Input:

```text
我把钥匙忘在办公室，只好请同事帮忙送下来。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/social-025

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `social-025`
- Split: `project_original`

Input:

```text
停车场入口正在施工，要从旁边的小路绕进去。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/social-026

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `social-026`
- Split: `project_original`

Input:

```text
这次旅行没有排太多景点，想留点时间随便走走。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/social-028

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `social-028`
- Split: `project_original`

Input:

```text
我已经把账单分好了，每个人的金额都写在备注里。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/social-029

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `social-029`
- Split: `project_original`

Input:

```text
店员态度很好，还主动提醒我可以使用优惠券。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/social-031

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `social-031`
- Split: `project_original`

Input:

```text
这个杯子的盖子不太紧，放进包里容易漏水。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/social-033

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `social-033`
- Split: `project_original`

Input:

```text
周末想去剪头发，但熟悉的设计师刚好休假。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/social-035

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `social-035`
- Split: `project_original`

Input:

```text
小区电梯正在保养，搬东西要改走另一栋。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/social-044

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `social-044`
- Split: `project_original`

Input:

```text
我把旧书整理成三箱，准备周末拿去捐赠。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-llm-social-baseline-v1/social-046

- Source: `zhtw-project-llm-social-baseline-v1`
- Source case: `social-046`
- Split: `project_original`

Input:

```text
这款饮料甜度偏高，加一点冰块会比较顺口。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```
