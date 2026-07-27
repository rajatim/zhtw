<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 032 (2026-07-27)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `8e13a4dd9f1f3bd4299a6afbe2b27e257aa00a299d7288246c765d383c7271e5`
Cases: 96
Exact Codex/Gemini classifications: 48
Maintainer review queue: 48

Field differences:

- Eligibility: 2
- Script: 4
- Domain: 6
- Risk: 43

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. aosp-framework-zh-rcn-v1/string-03aa6ccee6fefa59

Changed: `risk`

Input:

```text
新建/修改/删除通话记录
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 Android 介面字串；用於檢驗臺灣 UI 用語、一般字形與受保護 token。

Gemini reason: Standard UI string. Key char: '话'.

Maintainer decision: `pending`

### 02. aosp-framework-zh-rcn-v1/string-27d9fdead1a448e4

Changed: `risk`

Input:

```text
确定附近的设备之间的相对位置
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 Android 介面字串；用於檢驗臺灣 UI 用語、一般字形與受保護 token。

Gemini reason: Standard UI string. Involves multiple common simplified characters (确, 备, 间, 维).

Maintainer decision: `pending`

### 03. aosp-framework-zh-rcn-v1/string-4b7a12b0d424de44

Changed: `risk`

Input:

```text
发送短信
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 Android 介面字串；用於檢驗臺灣 UI 用語、一般字形與受保護 token。

Gemini reason: Standard UI string. Key char: '发'.

Maintainer decision: `pending`

### 04. aosp-framework-zh-rcn-v1/string-5ac849f0cca94bdb

Changed: `risk`

Input:

```text
这可能会导致您的手机号产生费用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 Android 介面字串；用於檢驗臺灣 UI 用語、一般字形與受保護 token。

Gemini reason: Standard UI string with multiple simplified characters (这, 导, 产, 费).

Maintainer decision: `pending`

### 05. aosp-framework-zh-rcn-v1/string-6ae6f919648a2e41

Changed: `risk`

Input:

```text
当您使用此应用时，此应用可以通过位置信息服务获取您的确切位置信息。您必须开启设备的位置信息服务，此应用才能获取位置信息。这可能会增加耗电量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 Android 介面字串；用於檢驗臺灣 UI 用語、一般字形與受保護 token。

Gemini reason: A longer permission-related string, good for block conversion accuracy.

Maintainer decision: `pending`

### 06. aosp-framework-zh-rcn-v1/string-6f8f5a67146ab91f

Changed: `domain`

Input:

```text
USSD 请求已更改为视频通话
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 Android 介面字串；用於檢驗臺灣 UI 用語、一般字形與受保護 token。

Gemini reason: Contains a technical acronym 'USSD' which must not be converted.

Maintainer decision: `pending`

### 07. aosp-framework-zh-rcn-v1/string-806bc01fc1b65653

Changed: `risk`

Input:

```text
禁用漫游横幅
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 Android 介面字串；用於檢驗臺灣 UI 用語、一般字形與受保護 token。

Gemini reason: Standard UI string with multiple simplified characters (禁, 漫, 游, 横, 幅).

Maintainer decision: `pending`

### 08. aosp-framework-zh-rcn-v1/string-939146a9f0a8eb5d

Changed: `domain`

Input:

```text
清空此用户在这部手机上的数据，而不事先发出警告。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的 Android 介面字串；用於檢驗臺灣 UI 用語、一般字形與受保護 token。

Gemini reason: A high-stakes warning about data deletion. Accuracy is critical.

Maintainer decision: `pending`

### 09. aosp-framework-zh-rcn-v1/string-a305ae8c90ab8db1

Changed: `risk`

Input:

```text
设备存储空间
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 Android 介面字串；用於檢驗臺灣 UI 用語、一般字形與受保護 token。

Gemini reason: Standard UI string with multiple simplified characters (设备, 储, 间).

Maintainer decision: `pending`

### 10. aosp-framework-zh-rcn-v1/string-f697285350775f51

Changed: `domain`

Input:

```text
RUIM 解锁成功。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 Android 介面字串；用於檢驗臺灣 UI 用語、一般字形與受保護 token。

Gemini reason: Contains a technical acronym 'RUIM' which must not be converted.

Maintainer decision: `pending`

### 11. census-newsroom-zh-hans-v1/page-01-sentence-034

Changed: `risk`

Input:

```text
该问卷调查独立访谈人员，询问他们在 4 月 1 日的居住地点，然后将信息与人口普查结果匹配。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Standard formal sentence describing a process.

Maintainer decision: `pending`

### 12. census-newsroom-zh-hans-v1/page-03-sentence-002

Changed: `risk`

Input:

```text
改进覆盖：人口普查局开始给部分尚未回答 2020 年人口普查的住户打电话跟进。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: The terms '改进覆盖' and '跟进' are specific and require careful conversion to maintain meaning.

Maintainer decision: `pending`

### 13. census-newsroom-zh-hans-v1/page-03-sentence-013

Changed: `risk`

Input:

```text
他们将获得个人防护装备 (PPE)，并遵循当地的使用指南准则。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Contains a Latin abbreviation (PPE) which must be preserved.

Maintainer decision: `pending`

### 14. census-newsroom-zh-hans-v1/page-04-sentence-019

Changed: `risk`

Input:

```text
2020 年人口普查的目标是算上截止 2020 年 4 月 1 日（人口普查日）居住在美国的每一个人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Standard formal sentence with a date.

Maintainer decision: `pending`

### 15. census-newsroom-zh-hans-v1/page-05-sentence-002

Changed: `risk`

Input:

```text
目前的互联网自发回应率比人口普查局的预测高出 9.2 个百分点，原因在于美国住户继续倾向于通过在线而不是电话和邮件来回答人口普查。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: A long, complex sentence but standard for formal reporting.

Maintainer decision: `pending`

### 16. census-newsroom-zh-hans-v1/page-05-sentence-014

Changed: `risk`

Input:

```text
为了在国家范围内增加对 2020 年人口普查的回答率，人口普查局要求全国社区通过在线、电话或邮件完成人口普查。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Standard formal sentence (call to action).

Maintainer decision: `pending`

### 17. census-newsroom-zh-hans-v1/page-08-sentence-009

Changed: `risk`

Input:

```text
但是，对国际人口移徙的估计有较大的不确定性，因为没有可以生成这些估计值的管理记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Contains technical terms like '国际人口移徙' and '管理记录'.

Maintainer decision: `pending`

### 18. census-newsroom-zh-hans-v1/page-08-sentence-013

Changed: `risk`

Input:

```text
2020 年人口普查最终结果将与 2020 年人口分析估计结果进行比较，以根据年龄、性别、广泛的种族和西班牙后裔群体估算潜在的净覆盖错误。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Contains specific demographic and technical terms like '西班牙后裔群体' and '净覆盖错误' that are sensitive to over-conversion.

Maintainer decision: `pending`

### 19. census-newsroom-zh-hans-v1/page-08-sentence-015

Changed: `eligible, domain, risk`

Input:

```text
2021 年西班牙裔和非西班牙裔人口 0 - 39 岁(今天发布扩展了从 0 岁到 29 岁年龄段) 按性别的估计。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | formal_news | baseline_guard | medium | - |

Codex reason: 人口統計表列項目缺少完整述語，無法作為可獨立判讀的句子。

Gemini reason: The sentence structure is slightly complex due to the parenthetical, but it's a standard data description.

Maintainer decision: `pending`

### 20. census-newsroom-zh-hans-v1/page-08-sentence-016

Changed: `risk`

Input:

```text
2022 年将首次发布州 (state) 和县一级对 0 - 4 岁儿童的估计。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Contains a Latin word '(state)' as an annotation, which must be preserved.

Maintainer decision: `pending`

### 21. census-newsroom-zh-hans-v1/page-08-sentence-023

Changed: `risk`

Input:

```text
人口普查局正在努力处理 2020 年人口普查数据，以便尽可能地在邻近 2020 年 12 月 31 日法定截止日期提供完整、准确的州 (state) 人口统计人数。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Contains a Latin word '(state)' as an annotation, which must be preserved.

Maintainer decision: `pending`

### 22. chromium-strings-zh-cn-v1/translation-2451727308784734061

Changed: `risk`

Input:

```text
使用快捷方式可快速访问密码管理工具。您可将快捷方式移到电脑的主屏幕上或应用启动器中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的瀏覽器介面字串；用於檢驗臺灣 UI 用語、產品名稱與受保護 token。

Gemini reason: A standard UI descriptive text that tests baseline conversion quality for a longer sentence.

Maintainer decision: `pending`

### 23. chromium-strings-zh-cn-v1/translation-7216228761061470870

Changed: `risk`

Input:

```text
当您在桌面设备上使用“图片搜索”功能时，系统会将网页标题、网址和内容（包括 PDF 文件）发送给服务器
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的瀏覽器介面字串；用於檢驗臺灣 UI 用語、產品名稱與受保護 token。

Gemini reason: Contains key candidate term '服务器' (server) and technical token 'PDF' which should be preserved.

Maintainer decision: `pending`

### 24. chromium-strings-zh-cn-v1/translation-80790299200510644

Changed: `risk`

Input:

```text
图片搜索
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的瀏覽器介面字串；用於檢驗臺灣 UI 用語、產品名稱與受保護 token。

Gemini reason: Simple feature name.

Maintainer decision: `pending`

### 25. kubernetes-docs-zh-cn-v1/page-01-sentence-0013

Changed: `risk`

Input:

```text
以下是比较常见的四种资源命名约束。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的技術文件敘述；用於檢驗 Kubernetes 術語、指令與識別碼保留。

Gemini reason: Standard technical documentation sentence.

Maintainer decision: `pending`

### 26. kubernetes-docs-zh-cn-v1/page-03-sentence-0070

Changed: `risk`

Input:

```text
回退重置：如果容器成功运行了一定时间（如 10 分钟）， Kubernetes 会重置回退延迟机制，将新的崩溃视为第一次崩溃。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的技術文件敘述；用於檢驗 Kubernetes 術語、指令與識別碼保留。

Gemini reason: Contains 'Kubernetes'. The character '退' is common but worth noting in '回退'.

Maintainer decision: `pending`

### 27. kubernetes-docs-zh-cn-v1/page-03-sentence-0344

Changed: `eligible, domain, risk`

Input:

```text
动手实践为容器生命周期时间关联处理程序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 教學連結標題與說明文字疑似誤接，語意及句法不完整。

Gemini reason: Contains several characters with potential one-to-many mappings (动, 实, 处, 理, 联).

Maintainer decision: `pending`

### 28. kubernetes-docs-zh-cn-v1/page-04-sentence-0170

Changed: `risk`

Input:

```text
如果你正在为集成到 Kubernetes 的负载均衡器编写代码，请避免使用此字段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的技術文件敘述；用於檢驗 Kubernetes 術語、指令與識別碼保留。

Gemini reason: Contains 'Kubernetes' and the term '负载均衡' which involves multiple character conversions.

Maintainer decision: `pending`

### 29. osha-disaster-cleanup-simplified-v1/sentence-011

Changed: `risk`

Input:

```text
除非有确实证据，首先假设洪水已被污染。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: Formal safety instruction from an OSHA document. Key characters for conversion include '证' (證), '确' (確), and '污' (汙).

Maintainer decision: `pending`

### 30. osha-disaster-cleanup-simplified-v1/sentence-023

Changed: `risk`

Input:

```text
只有经过适当培训和有齐全装备的工人才能修理电线。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: A clear, straightforward safety rule. Good baseline test for common character conversions like '过' (過), '备' (備), and '线' (線).

Maintainer decision: `pending`

### 31. osha-disaster-cleanup-simplified-v1/sentence-029

Changed: `script, risk`

Input:

```text
电力线周围10 英尺（3米）范围内的所有树木都需要修剪/移除，该工作必须由经过培训的树木修剪工来完成。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: A complex sentence from a safety document involving technical actions and units. Tests conversion of terms like '电力线' (電力線) and '修剪' (修剪).

Maintainer decision: `pending`

### 32. osha-disaster-cleanup-simplified-v1/sentence-031

Changed: `risk`

Input:

```text
使用工作手套、安全帽、工作靴，听力防护和眼睛及面部保护装置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: A list of personal protective equipment (PPE). It tests the conversion of common nouns such as '听' (聽) and '脸' (臉).

Maintainer decision: `pending`

### 33. osha-disaster-cleanup-simplified-v1/sentence-050

Changed: `risk`

Input:

```text
作业区工人在作业区被移动的车辆和装置撞到，发生交通事故（导致伤亡）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: A formal description of a potential workplace accident. It uses standard vocabulary, such as '车辆' (車輛) and '装置' (裝置).

Maintainer decision: `pending`

### 34. osha-disaster-cleanup-simplified-v1/sentence-052

Changed: `risk`

Input:

```text
使用适当的交通控制（即信号、锥筒、分隔物）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: An instruction involving a list of items. It tests common nouns and punctuation within parentheses.

Maintainer decision: `pending`

### 35. osha-disaster-cleanup-simplified-v1/sentence-059

Changed: `risk`

Input:

```text
人工搬抬及处理建筑材料和倒下的树枝时，可能会导致背部、膝盖和肩部受伤。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: A standard warning about potential injuries from manual labor, testing common anatomical and construction-related terms.

Maintainer decision: `pending`

### 36. osha-disaster-cleanup-simplified-v1/sentence-061

Changed: `risk`

Input:

```text
未经培训和许可，不得进入需要许可的密闭空间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: A formal safety rule for confined spaces. The repetition of '许可' (許可) and the term '密闭空间' (密閉空間) make it a good test case.

Maintainer decision: `pending`

### 37. osha-disaster-cleanup-simplified-v1/sentence-066

Changed: `script`

Input:

```text
DTSEM FS-435508/2023 Fact Sheet: Keeping Workers Safe during Disaster Cleanup and Recovery — Chinese Simplified 劳动者权益您有在安全的工作场所工作的权利。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | headline_mixed_with_body |
| Gemini | no | null | null | high | concatenated_content, footer_or_header, garbled_text |

Codex reason: 英文文件頁首、語言標籤與中文正文黏連，不是乾淨的單一語料。

Gemini reason: The input is a combination of document metadata/footer content (including English) and a grammatically awkward Chinese fragment. It is not a clean, complete sentence suitable for evaluation.

Maintainer decision: `pending`

### 38. osha-disaster-cleanup-simplified-v1/sentence-072

Changed: `domain`

Input:

```text
我们将向您提供帮助。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: A very simple and common polite sentence. It serves as a basic sanity check for the converter, particularly for the character '们' (們).

Maintainer decision: `pending`

### 39. ready-gov-home-fires-zh-hans-v1/sentence-001

Changed: `risk`

Input:

```text
火灾可能会在短短两分钟内危及生命，而火焰在五分钟内就能吞没一座住宅。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與單位保留。

Gemini reason: Source text from ready.gov, providing public safety information.

Maintainer decision: `pending`

### 40. ready-gov-home-fires-zh-hans-v1/sentence-012

Changed: `risk`

Input:

```text
在家中每一层都要安装烟雾报警器，包括地下室。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與單位保留。

Gemini reason: Source text from ready.gov, providing public safety information.

Maintainer decision: `pending`

### 41. ready-gov-home-fires-zh-hans-v1/sentence-020

Changed: `risk`

Input:

```text
每年都要两次练习家中火灾逃生计划。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與單位保留。

Gemini reason: Source text from ready.gov, providing public safety information.

Maintainer decision: `pending`

### 42. ready-gov-home-fires-zh-hans-v1/sentence-029

Changed: `risk`

Input:

```text
考虑在住房安装自动喷水灭火系统。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與單位保留。

Gemini reason: Source text from ready.gov, providing public safety information.

Maintainer decision: `pending`

### 43. ready-gov-home-fires-zh-hans-v1/sentence-048

Changed: `risk`

Input:

```text
清点损坏的财产和物品。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與單位保留。

Gemini reason: Source text from ready.gov, providing public safety information.

Maintainer decision: `pending`

### 44. ready-gov-home-fires-zh-hans-v1/sentence-060

Changed: `risk`

Input:

```text
立即更换所有磨损、陈旧或损坏的电器电源线，不要将电源线放在地毯或家具下面。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與單位保留。

Gemini reason: Source text from ready.gov, providing public safety information.

Maintainer decision: `pending`

### 45. ready-gov-home-fires-zh-hans-v1/sentence-065

Changed: `risk`

Input:

```text
更换磨损或破损的任何灯串电线或松动的灯泡连接。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與單位保留。

Gemini reason: Source text from ready.gov, providing public safety information.

Maintainer decision: `pending`

### 46. ready-gov-home-fires-zh-hans-v1/sentence-069

Changed: `script, risk`

Input:

```text
确保你的树离任何热源至少三英尺远，例如壁炉、散热器、蜡烛、热通风口或灯，并且不阻塞出口。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與單位保留。

Gemini reason: Source text from ready.gov, providing public safety information.

Maintainer decision: `pending`

### 47. ready-gov-home-fires-zh-hans-v1/sentence-070

Changed: `risk`

Input:

```text
不要使延长线和插座超载。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與單位保留。

Gemini reason: Source text from ready.gov, providing public safety information.

Maintainer decision: `pending`

### 48. ready-gov-home-fires-zh-hans-v1/sentence-074

Changed: `script, risk`

Input:

```text
在可燃物体与便携式加热设备之间保持至少 3 英尺的距离。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與單位保留。

Gemini reason: Source text from ready.gov, providing public safety information.

Maintainer decision: `pending`
