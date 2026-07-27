<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 030 (2026-07-27)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `7dbac14cff695ef87e16e15162e1e930775ac60105e3bb50c8535ef6853d2ff3`
Cases: 96
Exact Codex/Gemini classifications: 33
Maintainer review queue: 63

Field differences:

- Eligibility: 8
- Script: 11
- Domain: 23
- Risk: 54

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. aosp-framework-zh-rcn-v1/string-39ee26479ef00a58

Changed: `script`

Input:

```text
Android 正在启动…
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整 Android UI 字串；适合检验台湾介面用语与受保护格式。

Gemini reason: UI 字串。包含產品名稱 `Android`，必須保留。

Maintainer decision: `pending`

### 02. aosp-framework-zh-rcn-v1/string-4fc1884214f4fd7c

Changed: `risk`

Input:

```text
此国家/地区不支持卫星紧急呼救功能
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 Android UI 字串；适合检验台湾介面用语与受保护格式。

Gemini reason: UI 字串。用詞遣詞直譯即可，在台灣語境下亦可理解。

Maintainer decision: `pending`

### 03. aosp-framework-zh-rcn-v1/string-5287bf96626f0e09

Changed: `script`

Input:

```text
要将%1$s和%2$s保存到""%3$s""吗？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整 Android UI 字串；适合检验台湾介面用语与受保护格式。

Gemini reason: UI 字串。包含 C-style 格式化預留位置 (`%1$s`, `%2$s`, `%3$s`)，必須保留，不可轉換。

Maintainer decision: `pending`

### 04. aosp-framework-zh-rcn-v1/string-57315c6f0fad613a

Changed: `risk`

Input:

```text
试试其他解锁方式
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 Android UI 字串；适合检验台湾介面用语与受保护格式。

Gemini reason: UI 字串。用詞通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 05. aosp-framework-zh-rcn-v1/string-6119391d5253c064

Changed: `risk`

Input:

```text
包括信用卡号和密码等个人数据。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；适合检验台湾介面用语与受保护格式。

Gemini reason: UI 字串。「信用卡号」(信用卡號)、「密码」(密碼)、「数据」(資料) 均為需對應台灣用語的詞彙。

Maintainer decision: `pending`

### 06. aosp-framework-zh-rcn-v1/string-9c4d2231777dbcde

Changed: `risk`

Input:

```text
无法使用紧急呼救服务
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 Android UI 字串；适合检验台湾介面用语与受保护格式。

Gemini reason: UI 字串。用詞遣詞直譯即可，在台灣語境下亦可理解。

Maintainer decision: `pending`

### 07. aosp-framework-zh-rcn-v1/string-bae73a5b7e8edba2

Changed: `script, risk`

Input:

```text
%1$s 进程的堆转储数据现已可供您分享。请注意，此堆转储数据中可能包含该进程有权访问的敏感个人信息，其中可能包含您的输入内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；适合检验台湾介面用语与受保护格式。

Gemini reason: UI 字串。包含多個中國大陸 IT 用語：「进程」(處理程序)、「堆转储」(堆疊傾印)、「数据」(資料)，需在地化。同時包含預留位置 (`%1$s`)，需保護。

Maintainer decision: `pending`

### 08. aosp-framework-zh-rcn-v1/string-fabbc3db5344bf41

Changed: `script`

Input:

```text
输入一个4至8位数的PIN码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整 Android UI 字串；适合检验台湾介面用语与受保护格式。

Gemini reason: UI 字串。「PIN码」的「码」是簡體字，台灣用「碼」。包含拉丁縮寫 `PIN`，需保護。

Maintainer decision: `pending`

### 09. census-newsroom-zh-hans-v1/page-01-sentence-014

Changed: `script, risk`

Input:

```text
外部专家将在 2021 年初审查运作指标、人数和特征数据表，首先是国家和州 (state) 级别的数据，然后是国家以下各级数据。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整的美国人口普查正式资讯句；适合检验机构、统计与公共服务语境。

Gemini reason: 政府新聞稿。包含英文單詞 `state` 需保留。「运作指标」、「数据」、「级别」等為中國大陸用語，台灣會說「營運指標」、「資料」、「層級」。

Maintainer decision: `pending`

### 10. census-newsroom-zh-hans-v1/page-02-sentence-005

Changed: `risk`

Input:

```text
人口普查统计数据也告知各州、地方和联邦立法者如何在未来 10 年里每年向社区分配数成百上千亿美元的公众资金，用于医院、紧急救援服务、学校和桥梁等公众服务和基础设施。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整的美国人口普查正式资讯句；适合检验机构、统计与公共服务语境。

Gemini reason: 政府新聞稿。「统计数据」在台灣多稱「統計資料」。

Maintainer decision: `pending`

### 11. census-newsroom-zh-hans-v1/page-02-sentence-016

Changed: `risk`

Input:

```text
如果他们住在大学校园内，例如学生宿舍或兄弟会/姐妹会会所的房子，那么学校管理人员将算上他们，大学生不必自行回答。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的美国人口普查正式资讯句；适合检验机构、统计与公共服务语境。

Gemini reason: 政府新聞稿。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 12. census-newsroom-zh-hans-v1/page-04-sentence-013

Changed: `risk`

Input:

```text
此外，从 3 月 12 日开始，人口普查局将在东部时间早 7 点至凌晨 2 点之间提供实时的非英语电话帮助服务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整的美国人口普查正式资讯句；适合检验机构、统计与公共服务语境。

Gemini reason: 政府新聞稿。「实时」是中國大陸用語，台灣稱「即時」。

Maintainer decision: `pending`

### 13. census-newsroom-zh-hans-v1/page-05-sentence-019

Changed: `risk`

Input:

```text
要查看人口普查更改后的时间安排，请访问2020 年人口普查操作调整页面。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的美国人口普查正式资讯句；适合检验机构、统计与公共服务语境。

Gemini reason: 政府新聞稿。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 14. census-newsroom-zh-hans-v1/page-05-sentence-022

Changed: `script, risk`

Input:

```text
人口普查统计数据用于在接下来的十年内，确定每个州 (state)在美国众议院中的席位，并确定每年成百上千亿美元的联邦资金如何由各州 (state)、地方和联邦立法者进行分配使用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整的美国人口普查正式资讯句；适合检验机构、统计与公共服务语境。

Gemini reason: 政府新聞稿。包含英文單詞 `state` 需保留。「统计数据」在台灣多稱「統計資料」。

Maintainer decision: `pending`

### 15. census-newsroom-zh-hans-v1/page-06-sentence-013

Changed: `risk`

Input:

```text
人口普查局将照例执行软启动操作，以确保系统、操作和外勤计划按计划进行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的美国人口普查正式资讯句；适合检验机构、统计与公共服务语境。

Gemini reason: 政府新聞稿。「软启动」為術語直譯，可直接轉換。

Maintainer decision: `pending`

### 16. census-newsroom-zh-hans-v1/page-08-sentence-014

Changed: `risk`

Input:

```text
预计将于 2021 年发布详细描述 2020 年人口分析净值低估和高估的估计报告。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的美国人口普查正式资讯句；适合检验机构、统计与公共服务语境。

Gemini reason: 政府新聞稿。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 17. census-newsroom-zh-hans-v1/page-08-sentence-035

Changed: `risk`

Input:

```text
由于直到 1990 年代出生和死亡记录中才广泛采用西班牙后裔选项，因此人口分析估计并没有包括所有年龄段的西班牙后裔人口。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的美国人口普查正式资讯句；适合检验机构、统计与公共服务语境。

Gemini reason: 政府新聞稿。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 18. census-newsroom-zh-hans-v1/page-09-sentence-005

Changed: `risk`

Input:

```text
用邮政信箱接收邮件的住户在提供答案时应提供他们的街道地址（而不是邮政信箱号码），以确保他们的答案与他们居住的实际位置相关联，而不是与他们接收邮件的位置关联。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的美国人口普查正式资讯句；适合检验机构、统计与公共服务语境。

Gemini reason: 政府新聞稿。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 19. chromium-strings-zh-cn-v1/translation-22571759390241347

Changed: `risk`

Input:

```text
Chromium 中的技能
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整 Chromium UI 字串；适合检验产品介面用语与专名保留。

Gemini reason: UI 字串。`Chromium` 為產品專有名稱，必須保留。

Maintainer decision: `pending`

### 20. chromium-strings-zh-cn-v1/translation-2648074677641340862

Changed: `risk`

Input:

```text
安装过程中出现操作系统错误。请重新下载 Chromium。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Chromium UI 字串；适合检验产品介面用语与专名保留。

Gemini reason: UI 字串。「操作系统」是中國大陸用語，台灣稱「作業系統」。`Chromium` 為產品專有名稱，必須保留。

Maintainer decision: `pending`

### 21. chromium-strings-zh-cn-v1/translation-2676569452213089702

Changed: `risk`

Input:

```text
在设备上轻松使用 Chromium 中的 Gemini，即使 Chromium 已最小化也无妨。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Chromium UI 字串；适合检验产品介面用语与专名保留。

Gemini reason: UI 字串。「设备」是中國大陸用語，台灣稱「裝置」。`Chromium` 和 `Gemini` 是產品專有名稱，必須保留。

Maintainer decision: `pending`

### 22. chromium-strings-zh-cn-v1/translation-302551344979399011

Changed: `risk`

Input:

```text
技能等 AI 创新功能会保存到您的 Google 账号，并与 Chromium 同步功能分开管理
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Chromium UI 字串；适合检验产品介面用语与专名保留。

Gemini reason: UI 字串。「账号」是中國大陸用語，台灣稱「帳戶」。包含 `AI`、`Google`、`Chromium` 等多個專有名稱需保留。

Maintainer decision: `pending`

### 23. chromium-strings-zh-cn-v1/translation-3104828284009500087

Changed: `script, risk`

Input:

```text
搜索页面上的任何内容
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Chromium UI 字串；适合检验产品介面用语与专名保留。

Gemini reason: UI 字串。「搜索」和「内容」均為中國大陸用語，台灣稱「搜尋」和「內容」。

Maintainer decision: `pending`

### 24. chromium-strings-zh-cn-v1/translation-7047386856539490735

Changed: `script`

Input:

```text
这些结果有用吗？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 Chromium UI 字串；适合检验产品介面用语与专名保留。

Gemini reason: UI 字串。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 25. chromium-strings-zh-cn-v1/translation-8118331347066725040

Changed: `script`

Input:

```text
发送有关智能镜头搜索的反馈
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Chromium UI 字串；适合检验产品介面用语与专名保留。

Gemini reason: UI 字串。「智能镜头」通常指 Google Lens，台灣直稱「智慧鏡頭」或 Google Lens。「反馈」在台灣多用「意見回饋」。

Maintainer decision: `pending`

### 26. chromium-strings-zh-cn-v1/translation-8890569919834781711

Changed: `risk`

Input:

```text
由于登录时发生错误，ChromiumOS 无法将 Chromium 数据保存到您的 Google 账号
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Chromium UI 字串；适合检验产品介面用语与专名保留。

Gemini reason: UI 字串。「账号」是中國大陸用語，台灣稱「帳戶」。`ChromiumOS`, `Chromium`, `Google` 是專有名稱，必須保留。

Maintainer decision: `pending`

### 27. kubernetes-docs-zh-cn-v1/page-01-sentence-0026

Changed: `risk`

Input:

```text
进一步了解 Kubernetes 标签和注解。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可独立判读的 Kubernetes 技术文件句；适合检验技术术语与 token 保留。

Gemini reason: 技術文件。`Kubernetes` 是產品專有名稱，必須保留。

Maintainer decision: `pending`

### 28. kubernetes-docs-zh-cn-v1/page-02-sentence-0024

Changed: `script, risk`

Input:

```text
对象配置需要对对象架构有基本的了解。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可独立判读的 Kubernetes 技术文件句；适合检验技术术语与 token 保留。

Gemini reason: 技術文件。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 29. kubernetes-docs-zh-cn-v1/page-03-sentence-0025

Changed: `risk`

Input:

```text
Kubernetes 不保证现有 Pod 的替换 Pod 会被调度到与被替换的旧 Pod 相同的节点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可独立判读的 Kubernetes 技术文件句；适合检验技术术语与 token 保留。

Gemini reason: 技術文件。「Pod」和「节点」是 Kubernetes 術語，台灣分別稱「Pod」和「節點」。

Maintainer decision: `pending`

### 30. kubernetes-docs-zh-cn-v1/page-03-sentence-0058

Changed: `risk`

Input:

```text
当你使用 `kubectl` 来查询包含 `Waiting` 状态的容器的 Pod 时，你也会看到一个 Reason 字段，其中给出了容器处于等待状态的原因。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可独立判读的 Kubernetes 技术文件句；适合检验技术术语与 token 保留。

Gemini reason: 技術文件。包含多個需保護的技術術語 (`kubectl`, `Pod`, `Waiting`, `Reason`)。「容器」一詞通用。

Maintainer decision: `pending`

### 31. kubernetes-docs-zh-cn-v1/page-03-sentence-0095

Changed: `eligible, domain, risk`

Input:

```text
`restartPolicy` 应用于 Pod 中的和常规的 Init 容器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 句中缺少被修饰的容器类型，离开原始 Markdown 结构后无法独立判读。

Gemini reason: 技術文件。包含技術術語 `restartPolicy`、`Pod`、`Init` 容器，皆須保留。

Maintainer decision: `pending`

### 32. kubernetes-docs-zh-cn-v1/page-03-sentence-0182

Changed: `eligible, domain, risk`

Input:

```text
在 Pod 生命周期的早期阶段，kubelet 还没有开始使用容器运行时为 Pod 设置沙箱时。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 仅有时间条件从句而无主句，离开上下文后语意不完整。

Gemini reason: 技術文件。「kubelet」、「Pod」、「沙箱」是技術術語。台灣稱「kubelet」、「Pod」、「沙箱」。用語通用，但術語需保護。

Maintainer decision: `pending`

### 33. kubernetes-docs-zh-cn-v1/page-03-sentence-0285

Changed: `eligible, domain, risk`

Input:

```text
如果 Pod 中定义了，则存在特殊排序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 「定义了」之后缺少对象，无法独立判定原意。

Gemini reason: 技術文件。`Pod` 是 Kubernetes 術語，必須保留。

Maintainer decision: `pending`

### 34. kubernetes-docs-zh-cn-v1/page-04-sentence-0082

Changed: `eligible, domain, risk`

Input:

```text
不包含支持 trafficDistribution 等新特性所需的信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 句子缺少主语，明显依赖被 Markdown 解析移除的上下文。

Gemini reason: 技術文件。`trafficDistribution` 是欄位名稱，屬於程式碼，必須保留。

Maintainer decision: `pending`

### 35. kubernetes-docs-zh-cn-v1/page-04-sentence-0159

Changed: `risk`

Input:

```text
cloud-controller-manager 组件随后配置外部负载均衡器，以将流量转发到所分配的节点端口。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可独立判读的 Kubernetes 技术文件句；适合检验技术术语与 token 保留。

Gemini reason: 技術文件。「cloud-controller-manager」是元件名稱，需保留。「负载均衡器」台灣稱「負載平衡器」。

Maintainer decision: `pending`

### 36. massive-1-0-zh-cn-v1/10234

Changed: `domain, risk`

Input:

```text
用精确的测量和必要的设备收集烹饪所需的所有配料
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 可独立判读的日常语音助理指令；适合检验生活用语与专名。

Gemini reason: 日常對話。此句為指令。「配料」在台灣較常用於指稱佐料，此處可能指「食材」。

Maintainer decision: `pending`

### 37. massive-1-0-zh-cn-v1/10638

Changed: `domain, risk`

Input:

```text
今天我需要买的东西清单上有哪些
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可独立判读的日常语音助理指令；适合检验生活用语与专名。

Gemini reason: 日常對話，指令語氣。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 38. massive-1-0-zh-cn-v1/11873

Changed: `domain, risk`

Input:

```text
你能推荐下现在在我的附近有什么电影看吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可独立判读的日常语音助理指令；适合检验生活用语与专名。

Gemini reason: 日常對話，指令語氣。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 39. massive-1-0-zh-cn-v1/12315

Changed: `domain`

Input:

```text
请把今天下午的交通情况报告给我
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可独立判读的日常语音助理指令；适合检验生活用语与专名。

Gemini reason: 日常對話，指令語氣。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 40. massive-1-0-zh-cn-v1/13588

Changed: `domain, risk`

Input:

```text
描述一个土豆
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 可独立判读的日常语音助理指令；适合检验生活用语与专名。

Gemini reason: 日常對話，指令語氣。「土豆」在中國大陸指馬鈴薯，在台灣指花生。此處應指馬鈴薯，需轉換為「馬鈴薯」。

Maintainer decision: `pending`

### 41. massive-1-0-zh-cn-v1/16688

Changed: `domain, risk`

Input:

```text
给新地址写封邮件
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可独立判读的日常语音助理指令；适合检验生活用语与专名。

Gemini reason: 日常對話，指令語氣。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 42. massive-1-0-zh-cn-v1/16710

Changed: `domain, risk`

Input:

```text
我的联系人中有多少人在苏州生活或工作
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可独立判读的日常语音助理指令；适合检验生活用语与专名。

Gemini reason: 日常對話，指令語氣。蘇州是地名，應保留。

Maintainer decision: `pending`

### 43. massive-1-0-zh-cn-v1/17170

Changed: `domain, risk`

Input:

```text
家俊给我发电子邮件的时候提醒我
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 可独立判读的日常语音助理指令；适合检验生活用语与专名。

Gemini reason: 日常對話，指令語氣。「电子邮件」是中國大陸用語，台灣稱「電子郵件」。

Maintainer decision: `pending`

### 44. massive-1-0-zh-cn-v1/1982

Changed: `domain`

Input:

```text
设个上午六点三十分的闹钟
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可独立判读的日常语音助理指令；适合检验生活用语与专名。

Gemini reason: 日常對話，指令語氣。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 45. massive-1-0-zh-cn-v1/2174

Changed: `domain, risk`

Input:

```text
谁是只要有你的歌手
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可独立判读的日常语音助理指令；适合检验生活用语与专名。

Gemini reason: 日常對話，指令語氣。「只要有你」是歌名，應保留。

Maintainer decision: `pending`

### 46. massive-1-0-zh-cn-v1/3576

Changed: `domain, risk`

Input:

```text
搜狐新闻的最新消息是什么
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可独立判读的日常语音助理指令；适合检验生活用语与专名。

Gemini reason: 日常對話，指令語氣。「搜狐新闻」是專有名稱，應保留。

Maintainer decision: `pending`

### 47. massive-1-0-zh-cn-v1/3816

Changed: `domain`

Input:

```text
在音轨上播放下一首歌
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 可独立判读的日常语音助理指令；适合检验生活用语与专名。

Gemini reason: 日常對話，指令語氣。「音轨」是中國大陸用語，台灣稱「音軌」。

Maintainer decision: `pending`

### 48. massive-1-0-zh-cn-v1/7785

Changed: `script, domain`

Input:

```text
萨拉生日三天前提醒我
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 可独立判读的日常语音助理指令；适合检验生活用语与专名。

Gemini reason: 日常對話，指令語氣。`萨拉` (Sara) 為音譯人名，應保留。

Maintainer decision: `pending`

### 49. massive-1-0-zh-cn-v1/8697

Changed: `domain, risk`

Input:

```text
我和李雷在三月二十一日十点有一个会面
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可独立判读的日常语音助理指令；适合检验生活用语与专名。

Gemini reason: 日常對話，指令語氣。李雷是人名，應保留。

Maintainer decision: `pending`

### 50. massive-1-0-zh-cn-v1/9327

Changed: `eligible, domain, risk`

Input:

```text
请马上扫描一下收音机的上午拨号盘
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 「上午拨号盘」是 AM dial 的错误本地化，语意已明显失真。

Gemini reason: 日常對話，指令語氣。「扫描」在台灣多用於數位掃描，此處指收音機的「掃描頻道」，用法可通，但稍不自然。

Maintainer decision: `pending`

### 51. massive-1-0-zh-cn-v1/9991

Changed: `domain, risk`

Input:

```text
给我看烹饪食物教程
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 可独立判读的日常语音助理指令；适合检验生活用语与专名。

Gemini reason: 日常對話，指令語氣。「教程」是中國大陸用語，台灣稱「教學」。

Maintainer decision: `pending`

### 52. ready-gov-radiation-zh-hans-v1/sentence-006

Changed: `risk`

Input:

```text
在您收听响应者的指示时，在您和辐射之间放置材料可提供保护。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的辐射安全指示；需保守处理高风险语意。

Gemini reason: 政府應急指南，屬高風險內容。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 53. ready-gov-radiation-zh-hans-v1/sentence-025

Changed: `eligible, domain, risk`

Input:

```text
它会产生巨大的致命爆炸。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | pronoun_dependency |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 「它」依赖前句的核爆炸主题，单独抽出无法完整判读。

Gemini reason: 政府應急指南，屬高風險內容。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 54. ready-gov-radiation-zh-hans-v1/sentence-027

Changed: `risk`

Input:

```text
对于核爆炸，如果您有警告，请躲在任何可能提供保护的东西后面以躲避爆炸。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的辐射安全指示；需保守处理高风险语意。

Gemini reason: 政府應急指南，屬高風險內容。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 55. ready-gov-radiation-zh-hans-v1/sentence-030

Changed: `risk`

Input:

```text
进入室内：爆炸后，您将有10分钟或更长时间在尘埃到达之前找到合适的避难所。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的辐射安全指示；需保守处理高风险语意。

Gemini reason: 政府應急指南，屬高風險內容。「尘埃」在台灣口語較少用，但書面語可通。

Maintainer decision: `pending`

### 56. ready-gov-radiation-zh-hans-v1/sentence-041

Changed: `risk`

Input:

```text
保持警觉：遵循应急响应官员的指示。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的辐射安全指示；需保守处理高风险语意。

Gemini reason: 政府應急指南，屬高風險內容。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 57. ready-gov-radiation-zh-hans-v1/sentence-045

Changed: `eligible, domain, risk`

Input:

```text
脱下受污染衣服的外层，以清除体内的放射性物质。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 脱下外层衣物无法清除「体内」放射性物质；高风险安全指示的语意已经错误。

Gemini reason: 政府應急指南，屬高風險內容。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 58. ready-gov-radiation-zh-hans-v1/sentence-046

Changed: `risk`

Input:

```text
脱掉外层衣服可以去除高达 90%的放射性物质。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的辐射安全指示；需保守处理高风险语意。

Gemini reason: 政府應急指南，屬高風險內容。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 59. ready-gov-radiation-zh-hans-v1/sentence-054

Changed: `risk`

Input:

```text
放射性尘埃到达后，清洁所有在外面的宠物。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的辐射安全指示；需保守处理高风险语意。

Gemini reason: 政府應急指南，屬高風險內容。「尘埃」在台灣口語較少用，但書面語可通。

Maintainer decision: `pending`

### 60. ready-gov-radiation-zh-hans-v1/sentence-055

Changed: `risk`

Input:

```text
轻轻刷洗宠物的皮毛，去除所有放射性颗粒，并用肥皂和水清洗宠物（如果有的话）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的辐射安全指示；需保守处理高风险语意。

Gemini reason: 政府應急指南，屬高風險內容。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 61. ready-gov-radiation-zh-hans-v1/sentence-058

Changed: `eligible, domain, risk`

Input:

```text
将这些毛巾或清洁布密封在塑料袋中，并将它们放在远离人和宠物的地方。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | pronoun_dependency |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 「这些毛巾或清洁布」依赖前文指涉，单句无法独立判读。

Gemini reason: 政府應急指南，屬高風險內容。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 62. ready-gov-radiation-zh-hans-v1/sentence-061

Changed: `risk`

Input:

```text
照顾好自己和他人：如果您生病或受伤，请听取有关如何以及在何处就医的说明。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的辐射安全指示；需保守处理高风险语意。

Gemini reason: 政府應急指南，屬高風險內容。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`

### 63. ready-gov-radiation-zh-hans-v1/sentence-063

Changed: `risk`

Input:

```text
辐射或核紧急情况的威胁可能会给人带来压力，幸存下来可能是一种创伤性的经历。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的辐射安全指示；需保守处理高风险语意。

Gemini reason: 政府應急指南，屬高風險內容。用語通用，單純簡繁轉換即可。

Maintainer decision: `pending`
