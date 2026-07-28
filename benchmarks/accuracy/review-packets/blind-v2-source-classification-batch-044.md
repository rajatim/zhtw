<!-- zhtw:disable -->
# Blind-v2 Source Classification 044

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-044.json`
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

### census-newsroom-zh-hans-v1/page-01-sentence-009

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-01-sentence-009`
- Split: `press_release_01`

Input:

```text
这些指标将包含自己回答、未回复随访（即英文缩写 NRFU）（包括住户访谈、代理人访谈和管理记录普查）、人数再计算和有人居住、空置或废弃地址的指标。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### census-newsroom-zh-hans-v1/page-03-sentence-023

- Source: `census-newsroom-zh-hans-v1`
- Source case: `page-03-sentence-023`
- Split: `press_release_03`

Input:

```text
每个人的信息收集包括姓名、性别、年龄、出生日期、种族、与户主的关系及西班牙后裔。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### cisa-personal-security-zh-hans-v1/sentence-038

- Source: `cisa-personal-security-zh-hans-v1`
- Source case: `sentence-038`
- Split: `guide`

Input:

```text
了解如何使用车内的防盗报警系统。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### cisa-personal-security-zh-hans-v1/sentence-061

- Source: `cisa-personal-security-zh-hans-v1`
- Source case: `sentence-061`
- Split: `guide`

Input:

```text
请将手机放置在可拨打紧急电话的位置。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### cisa-personal-security-zh-hans-v1/sentence-092

- Source: `cisa-personal-security-zh-hans-v1`
- Source case: `sentence-092`
- Split: `guide`

Input:

```text
如果确实发生了不利情况，这些信息可能会对警方有所帮助。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### flores-200-zho-hans-v1/dev-0123

- Source: `flores-200-zho-hans-v1`
- Source case: `dev-0123`
- Split: `dev`

Input:

```text
位于肯尼亚内罗毕的美国大使馆发出了警告称，“索马里极端分子”正策划在肯尼亚和埃塞俄比亚发动自杀性炸弹袭击。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### flores-200-zho-hans-v1/dev-0139

- Source: `flores-200-zho-hans-v1`
- Source case: `dev-0139`
- Split: `dev`

Input:

```text
人如果吸入通过风和海浪进入空气的受污染水气，就可能受到影响。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### flores-200-zho-hans-v1/dev-0290

- Source: `flores-200-zho-hans-v1`
- Source case: `dev-0290`
- Split: `dev`

Input:

```text
美国地质调查局国际地震地图显示，冰岛在前一周并未发生地震。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### flores-200-zho-hans-v1/dev-0294

- Source: `flores-200-zho-hans-v1`
- Source case: `dev-0294`
- Split: `dev`

Input:

```text
这些云可能会让人们怀疑火山到底有没有真正喷发过。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### flores-200-zho-hans-v1/dev-0350

- Source: `flores-200-zho-hans-v1`
- Source case: `dev-0350`
- Split: `dev`

Input:

```text
科学家目前致力打造一种可通过相同的方式产生能量的反应堆。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### flores-200-zho-hans-v1/dev-0404

- Source: `flores-200-zho-hans-v1`
- Source case: `dev-0404`
- Split: `dev`

Input:

```text
在战争开始时，它们大多在海面上航行，但随着雷达的发展和精确度的提高，潜艇被迫潜入水下以免被发现。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### flores-200-zho-hans-v1/dev-0583

- Source: `flores-200-zho-hans-v1`
- Source case: `dev-0583`
- Split: `dev`

Input:

```text
龙卷风能将树木连根拔起，将建筑物上的木板撕下，把汽车抛向天空。龙卷风中的百分之二最为猛烈，能持续肆虐三小时以上。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### flores-200-zho-hans-v1/dev-0648

- Source: `flores-200-zho-hans-v1`
- Source case: `dev-0648`
- Split: `dev`

Input:

```text
我们中有很多人，都发现自己观看的电视节目在告诉我们某种过程或经验，但我们却永远不会参与或应用这些知识。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### flores-200-zho-hans-v1/devtest-0179

- Source: `flores-200-zho-hans-v1`
- Source case: `devtest-0179`
- Split: `devtest`

Input:

```text
跳羚队以五连败收官。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### flores-200-zho-hans-v1/devtest-0196

- Source: `flores-200-zho-hans-v1`
- Source case: `devtest-0196`
- Split: `devtest`

Input:

```text
这名摄影师被送往加州大学洛杉矶分校罗纳德·里根医疗中心，其后不治。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### flores-200-zho-hans-v1/devtest-0478

- Source: `flores-200-zho-hans-v1`
- Source case: `devtest-0478`
- Split: `devtest`

Input:

```text
当然，长期剥削菲律宾人民所获得的高额利润成为美帝国主义的基本收益。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### flores-200-zho-hans-v1/devtest-0487

- Source: `flores-200-zho-hans-v1`
- Source case: `devtest-0487`
- Split: `devtest`

Input:

```text
浪漫主义具有很强的文化决定论色彩。这源于歌德、费希特和施莱格尔等作家。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### flores-200-zho-hans-v1/devtest-0524

- Source: `flores-200-zho-hans-v1`
- Source case: `devtest-0524`
- Split: `devtest`

Input:

```text
奥利弗·萨克斯 (Oliver Sacks) 在他的论文《总统的演讲》中指出，那些因为脑损伤而无法理解语言的人仍然能够准确地判断说话人是否有诚意。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### flores-200-zho-hans-v1/devtest-0580

- Source: `flores-200-zho-hans-v1`
- Source case: `devtest-0580`
- Split: `devtest`

Input:

```text
体内中毒可能不会立即显现出来，呕吐等症状十分普遍，因此不能立即作出诊断。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### flores-200-zho-hans-v1/devtest-0590

- Source: `flores-200-zho-hans-v1`
- Source case: `devtest-0590`
- Split: `devtest`

Input:

```text
这些夫妇可能会为他们的孩子制定收养计划。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### flores-200-zho-hans-v1/devtest-1002

- Source: `flores-200-zho-hans-v1`
- Source case: `devtest-1002`
- Split: `devtest`

Input:

```text
更传统的教堂常常在复活节周末的周六晚上举行复活节守夜活动，会众通常在午夜钟声敲响之时涌入庆典，庆祝基督的复活。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ftc-heads-up-simplified-v1/sentence-005

- Source: `ftc-heads-up-simplified-v1`
- Source case: `sentence-005`
- Split: `booklet`

Input:

```text
通过交谈，您可以让孩子知道一旦他们犯了错误，有可以信赖的成年人会帮助他们。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ftc-heads-up-simplified-v1/sentence-031

- Source: `ftc-heads-up-simplified-v1`
- Source case: `sentence-031`
- Split: `booklet`

Input:

```text
由于在网上看不到别人的面部表情、肢体语言或其他视觉线索，你可能会发布或说出不会当面说的话。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ftc-heads-up-simplified-v1/sentence-052

- Source: `ftc-heads-up-simplified-v1`
- Source case: `sentence-052`
- Split: `booklet`

Input:

```text
保存记录并向可以信赖的成年人求助。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ftc-heads-up-simplified-v1/sentence-083

- Source: `ftc-heads-up-simplified-v1`
- Source case: `sentence-083`
- Split: `booklet`

Input:

```text
你的网上账户中有大量的个人信息。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ftc-how-to-avoid-scam-simplified-v1/sentence-008

- Source: `ftc-how-to-avoid-scam-simplified-v1`
- Source case: `sentence-008`
- Split: `handout`

Input:

```text
诈骗者希望您在有时间思考之前就采取行动。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ftc-how-to-avoid-scam-simplified-v1/sentence-011

- Source: `ftc-how-to-avoid-scam-simplified-v1`
- Source case: `sentence-011`
- Split: `handout`

Input:

```text
他们可能会说您的计算机即将损坏。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ftc-identity-theft-simplified-v1/sentence-008

- Source: `ftc-identity-theft-simplified-v1`
- Source case: `sentence-008`
- Split: `handout`

Input:

```text
您是否收到了您从未开立过账户的账单？
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ftc-identity-theft-simplified-v1/sentence-011

- Source: `ftc-identity-theft-simplified-v1`
- Source case: `sentence-011`
- Split: `handout`

Input:

```text
将您的出生证明、社会保障卡和账户对账单等正式文件保存在安全的地方。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ftc-identity-theft-simplified-v1/sentence-017

- Source: `ftc-identity-theft-simplified-v1`
- Source case: `sentence-017`
- Split: `handout`

Input:

```text
为提供多重身份验证功能的帐户添加多重身份验证，例如通过短信获取访问代码。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ftc-identity-theft-simplified-v1/sentence-019

- Source: `ftc-identity-theft-simplified-v1`
- Source case: `sentence-019`
- Split: `handout`

Input:

```text
仔细查看您未购买商品的费用或意外账单。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-earthquakes-zh-hans-v1/sentence-002

- Source: `ready-gov-earthquakes-zh-hans-v1`
- Source case: `sentence-002`
- Split: `article`

Input:

```text
虽然可能在没有警告的情况下在任何地方发生，但是，地震风险较高的地区包括阿拉斯加、加州、夏威夷、俄勒冈、波多黎各、华盛顿和整个密西西比河谷。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-floods-zh-hans-v1/sentence-027

- Source: `ready-gov-floods-zh-hans-v1`
- Source case: `sentence-027`
- Split: `article`

Input:

```text
清理排水管和檐沟。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-hurricanes-zh-hans-v1/sentence-002

- Source: `ready-gov-hurricanes-zh-hans-v1`
- Source case: `sentence-002`
- Split: `article`

Input:

```text
飓风可能发生在美国任何沿海地区，或大西洋、太平洋的任何领土上。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-007

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-007`
- Split: `article`

Input:

```text
并非所有的山体滑坡都很快。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-landslides-debris-flow-zh-hans-v1/sentence-046

- Source: `ready-gov-landslides-debris-flow-zh-hans-v1`
- Source case: `sentence-046`
- Split: `article`

Input:

```text
如果您看到有水流逼近，切勿过桥，因为水流会变得越来越大，您无法逃脱。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-radiation-zh-hans-v1/sentence-005

- Source: `ready-gov-radiation-zh-hans-v1`
- Source case: `sentence-005`
- Split: `article`

Input:

```text
在任何辐射紧急情况下保持安全的最佳方法是进入室内，待在室内并保持关注。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-radiation-zh-hans-v1/sentence-042

- Source: `ready-gov-radiation-zh-hans-v1`
- Source case: `sentence-042`
- Split: `article`

Input:

```text
如果建议撤离，请听取有关路线、避难所和程序的信息。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-radiation-zh-hans-v1/sentence-048

- Source: `ready-gov-radiation-zh-hans-v1`
- Source case: `sentence-048`
- Split: `article`

Input:

```text
尽可能避免触摸眼睛、鼻子和嘴巴。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-radiation-zh-hans-v1/sentence-051

- Source: `ready-gov-radiation-zh-hans-v1`
- Source case: `sentence-051`
- Split: `article`

Input:

```text
不要在皮肤上使用家用清洁湿巾。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-radiation-zh-hans-v1/sentence-053

- Source: `ready-gov-radiation-zh-hans-v1`
- Source case: `sentence-053`
- Split: `article`

Input:

```text
遵循CDC关于为自己和他人消除核污染的指南。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-tornadoes-zh-hans-v1/sentence-001

- Source: `ready-gov-tornadoes-zh-hans-v1`
- Source case: `sentence-001`
- Split: `article`

Input:

```text
龙卷风是剧烈旋转的气柱，从雷暴延伸到地面，能摧毁建筑物，翻转汽车，并产生致命的飞溅碎片。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-tornadoes-zh-hans-v1/sentence-018

- Source: `ready-gov-tornadoes-zh-hans-v1`
- Source case: `sentence-018`
- Split: `article`

Input:

```text
气象员能预测什么情况最可能发生龙卷风。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-winter-weather-zh-hans-v1/sentence-008

- Source: `ready-gov-winter-weather-zh-hans-v1`
- Source case: `sentence-008`
- Split: `article`

Input:

```text
提醒公众注意可能发生暴风雪、大雪、强冻雨或大雨夹雪。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-winter-weather-zh-hans-v1/sentence-009

- Source: `ready-gov-winter-weather-zh-hans-v1`
- Source case: `sentence-009`
- Split: `article`

Input:

```text
冬季风暴观察通常在冬季风暴开始前 12 至 48 小时发布。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-winter-weather-zh-hans-v1/sentence-012

- Source: `ready-gov-winter-weather-zh-hans-v1`
- Source case: `sentence-012`
- Split: `article`

Input:

```text
收听紧急信息和警示。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-winter-weather-zh-hans-v1/sentence-016

- Source: `ready-gov-winter-weather-zh-hans-v1`
- Source case: `sentence-016`
- Split: `article`

Input:

```text
了解如何防止管道冻结。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-winter-weather-zh-hans-v1/sentence-051

- Source: `ready-gov-winter-weather-zh-hans-v1`
- Source case: `sentence-051`
- Split: `article`

Input:

```text
保持发电机干燥并防止雨淋或水浸。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### vscode-loc-zh-hans-v1/entry-1bc2d120c0821a7f

- Source: `vscode-loc-zh-hans-v1`
- Source case: `entry-1bc2d120c0821a7f`
- Split: `language_pack`

Input:

```text
自动换行(&&W)
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### vscode-loc-zh-hans-v1/entry-252ac876ba500bc7

- Source: `vscode-loc-zh-hans-v1`
- Source case: `entry-252ac876ba500bc7`
- Split: `language_pack`

Input:

```text
开始新聊天并存档当前聊天
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### vscode-loc-zh-hans-v1/entry-2c85090743bfc31a

- Source: `vscode-loc-zh-hans-v1`
- Source case: `entry-2c85090743bfc31a`
- Split: `language_pack`

Input:

```text
语音录制已停止
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### vscode-loc-zh-hans-v1/entry-374e2ac3e2f1c83c

- Source: `vscode-loc-zh-hans-v1`
- Source case: `entry-374e2ac3e2f1c83c`
- Split: `language_pack`

Input:

```text
省略语言时，"contributes.{0}.path" 的值必须为一个 ".code-snippets" 文件。提供的值: {1}
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### vscode-loc-zh-hans-v1/entry-482ab0292c54829a

- Source: `vscode-loc-zh-hans-v1`
- Source case: `entry-482ab0292c54829a`
- Split: `language_pack`

Input:

```text
由更改工具栏中的“提供反馈”按钮使用
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### vscode-loc-zh-hans-v1/entry-5115572476a38b26

- Source: `vscode-loc-zh-hans-v1`
- Source case: `entry-5115572476a38b26`
- Split: `language_pack`

Input:

```text
启用后，痕迹导航栏将显示“字段”符号。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### vscode-loc-zh-hans-v1/entry-633aa45197b3dce7

- Source: `vscode-loc-zh-hans-v1`
- Source case: `entry-633aa45197b3dce7`
- Split: `language_pack`

Input:

```text
视图的类型。对于基于树状视图的视图，这可以是 "tree"，对于基于 Web 视图的视图，这可以是 "webview"。默认值为 "tree"。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### vscode-loc-zh-hans-v1/entry-7273bc36a8168b75

- Source: `vscode-loc-zh-hans-v1`
- Source case: `entry-7273bc36a8168b75`
- Split: `language_pack`

Input:

```text
智能体会话边栏中“新建会话”按钮的前景色。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### vscode-loc-zh-hans-v1/entry-8c957017a839953e

- Source: `vscode-loc-zh-hans-v1`
- Source case: `entry-8c957017a839953e`
- Split: `language_pack`

Input:

```text
继续操作前，请确保你信任该代码。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### vscode-loc-zh-hans-v1/entry-af83496e04575bf7

- Source: `vscode-loc-zh-hans-v1`
- Source case: `entry-af83496e04575bf7`
- Split: `language_pack`

Input:

```text
按名称排列文件和文件夹。两者穿插显示。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### vscode-loc-zh-hans-v1/entry-c19d884c9e5923ca

- Source: `vscode-loc-zh-hans-v1`
- Source case: `entry-c19d884c9e5923ca`
- Split: `language_pack`

Input:

```text
执行单元格和焦点容器
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### vscode-loc-zh-hans-v1/entry-d8563114f52568ca

- Source: `vscode-loc-zh-hans-v1`
- Source case: `entry-d8563114f52568ca`
- Split: `language_pack`

Input:

```text
属性“{0}”设置为“{1}”。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### vscode-loc-zh-hans-v1/entry-e5adeb3575e96524

- Source: `vscode-loc-zh-hans-v1`
- Source case: `entry-e5adeb3575e96524`
- Split: `language_pack`

Input:

```text
[['''{0}']] 中的编辑已被拒绝
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### vscode-loc-zh-hans-v1/entry-ec63ec66cb3a69b7

- Source: `vscode-loc-zh-hans-v1`
- Source case: `entry-ec63ec66cb3a69b7`
- Split: `language_pack`

Input:

```text
假定未连接屏幕阅读器。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### vscode-loc-zh-hans-v1/entry-f8e6646a386ac002

- Source: `vscode-loc-zh-hans-v1`
- Source case: `entry-f8e6646a386ac002`
- Split: `language_pack`

Input:

```text
在此工作区中允许此工具和自变量特定组合而不进行确认。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### vscode-loc-zh-hans-v1/entry-ff6d9986f54d171a

- Source: `vscode-loc-zh-hans-v1`
- Source case: `entry-ff6d9986f54d171a`
- Split: `language_pack`

Input:

```text
已找到 {0}
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-social-guard-v1/it-005

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-005`
- Split: `project_original`

Input:

```text
这个端点只接受 Content-Type: application/json。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-social-guard-v1/it-008

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-008`
- Split: `project_original`

Input:

```text
Kubernetes 清单中的 metadata.name 必须与服务名称一致。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-social-guard-v1/it-012

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-012`
- Split: `project_original`

Input:

```text
日志字段 trace_id 和 span_id 用于串联同一次请求。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-social-guard-v1/it-013

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-013`
- Split: `project_original`

Input:

```text
Prometheus 指标 http_request_duration_seconds 保留原始名称。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-social-guard-v1/it-016

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-016`
- Split: `project_original`

Input:

```text
OAuth 2.0 回调网址必须与 redirect_uri 完全匹配。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-social-guard-v1/it-021

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-021`
- Split: `project_original`

Input:

```text
版本范围 >=3.2.0,<4.0.0 必须原样写入清单。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-social-guard-v1/it-023

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-023`
- Split: `project_original`

Input:

```text
API 响应中的 next_page_token 为空时停止分页。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-social-guard-v1/it-024

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-024`
- Split: `project_original`

Input:

```text
请在 curl 命令中加入 --fail-with-body 选项。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-social-guard-v1/it-034

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `it-034`
- Split: `project_original`

Input:

```text
发布说明引用 CVE-2026-12345 时要保留完整编号。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-social-guard-v1/llm-017

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `llm-017`
- Split: `project_original`

Input:

```text
自动评分器只能检查结构，不能代替事实核查。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-social-guard-v1/llm-025

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `llm-025`
- Split: `project_original`

Input:

```text
模型无法读取本地文件，除非用户主动上传。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-social-guard-v1/llm-030

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `llm-030`
- Split: `project_original`

Input:

```text
提示内容只允许改写语气，数字与引用必须保持不变。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-social-guard-v1/social-010

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `social-010`
- Split: `project_original`

Input:

```text
这杯饮料点的是五十岚的「四季春珍波椰」。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-social-guard-v1/social-020

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `social-020`
- Split: `project_original`

Input:

```text
台风「青鸟」接近时，学校会通过官方渠道通知停课。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-social-guard-v1/social-021

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `social-021`
- Split: `project_original`

Input:

```text
我在 momo 购物网买的空气清净机明天送达。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-social-guard-v1/social-022

- Source: `zhtw-project-it-llm-social-guard-v1`
- Source case: `social-022`
- Split: `project_original`

Input:

```text
请确认收件人是 Wu, Mei-Ling，不要调整英文姓名顺序。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-ui-llm-formal-guard-v1/formal-001

- Source: `zhtw-project-it-ui-llm-formal-guard-v1`
- Source case: `formal-001`
- Split: `project_original`

Input:

```text
决议附件沿用编号 SEC(2026) 118 final。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-ui-llm-formal-guard-v1/formal-010

- Source: `zhtw-project-it-ui-llm-formal-guard-v1`
- Source case: `formal-010`
- Split: `project_original`

Input:

```text
财务报表将科目代码 1100-03 列在附注中。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-ui-llm-formal-guard-v1/formal-011

- Source: `zhtw-project-it-ui-llm-formal-guard-v1`
- Source case: `formal-011`
- Split: `project_original`

Input:

```text
专利说明书引用序列表文件 SequenceListing.xml。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-ui-llm-formal-guard-v1/it-006

- Source: `zhtw-project-it-ui-llm-formal-guard-v1`
- Source case: `it-006`
- Split: `project_original`

Input:

```text
命令输出中的 HEAD~2 与 origin/release 不得本地化。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-ui-llm-formal-guard-v1/it-017

- Source: `zhtw-project-it-ui-llm-formal-guard-v1`
- Source case: `it-017`
- Split: `project_original`

Input:

```text
DNS 记录 _acme-challenge.example.com 使用 TXT 类型。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-ui-llm-formal-guard-v1/it-020

- Source: `zhtw-project-it-ui-llm-formal-guard-v1`
- Source case: `it-020`
- Split: `project_original`

Input:

```text
压缩文件内的 META-INF/MANIFEST.MF 路径区分大小写。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-ui-llm-formal-guard-v1/llm-007

- Source: `zhtw-project-it-ui-llm-formal-guard-v1`
- Source case: `llm-007`
- Split: `project_original`

Input:

```text
批次记录以 req_01JAZ8M4Q2 作为不可变识别码。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-ui-llm-formal-guard-v1/llm-008

- Source: `zhtw-project-it-ui-llm-formal-guard-v1`
- Source case: `llm-008`
- Split: `project_original`

Input:

```text
模型输出必须符合 schema 名称 customer_summary_v1。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-ui-llm-formal-guard-v1/llm-016

- Source: `zhtw-project-it-ui-llm-formal-guard-v1`
- Source case: `llm-016`
- Split: `project_original`

Input:

```text
缓存命中事件的类型为 prompt_cache.hit。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-ui-llm-formal-guard-v1/llm-017

- Source: `zhtw-project-it-ui-llm-formal-guard-v1`
- Source case: `llm-017`
- Split: `project_original`

Input:

```text
测试夹具要求输出字面值 null，而不是空字符串。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-ui-llm-formal-guard-v1/llm-018

- Source: `zhtw-project-it-ui-llm-formal-guard-v1`
- Source case: `llm-018`
- Split: `project_original`

Input:

```text
审核队列以 needs_human_review 标记低信心案例。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-ui-llm-formal-guard-v1/llm-020

- Source: `zhtw-project-it-ui-llm-formal-guard-v1`
- Source case: `llm-020`
- Split: `project_original`

Input:

```text
函数调用结果使用 tool_call_id 对应原始请求。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-ui-llm-formal-guard-v1/llm-025

- Source: `zhtw-project-it-ui-llm-formal-guard-v1`
- Source case: `llm-025`
- Split: `project_original`

Input:

```text
基准报告以 win_rate_paired 表示成对胜率。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-ui-llm-formal-guard-v1/ui-011

- Source: `zhtw-project-it-ui-llm-formal-guard-v1`
- Source case: `ui-011`
- Split: `project_original`

Input:

```text
金额字段采用 ISO 4217 代码 TWD。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-ui-llm-formal-guard-v1/ui-019

- Source: `zhtw-project-it-ui-llm-formal-guard-v1`
- Source case: `ui-019`
- Split: `project_original`

Input:

```text
面包屑最后一项标记 aria-current=page。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-ui-llm-formal-guard-v1/ui-021

- Source: `zhtw-project-it-ui-llm-formal-guard-v1`
- Source case: `ui-021`
- Split: `project_original`

Input:

```text
筛选器标题显示“Created by me”，并保留产品指定措辞。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```
