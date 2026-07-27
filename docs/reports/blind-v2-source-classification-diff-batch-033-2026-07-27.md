<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 033 (2026-07-27)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `b07f481061d43600da3bffe5a2e21c6c1e57504274829b0dad4644a53c55f8b4`
Cases: 96
Exact Codex/Gemini classifications: 47
Maintainer review queue: 49

Field differences:

- Eligibility: 5
- Script: 1
- Domain: 7
- Risk: 48

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 6 tool calls and 0 API errors.

The maintainer resolved all 49 advisory disagreements and batch-confirmed the 47 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. aosp-framework-zh-rcn-v1/string-0beac066a573530a

Changed: `risk`

Input:

```text
私密空间
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 Android 介面字串；用於檢驗臺灣 UI 用語、一般字形與受保護 token。

Gemini reason: A standard UI term from Android. '私密' (private/secret) and '空间' (space) are common words.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 02. aosp-framework-zh-rcn-v1/string-7426c6c0c7d314a0

Changed: `risk`

Input:

```text
在线播放时无法查看画中画
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 Android 介面字串；用於檢驗臺灣 UI 用語、一般字形與受保護 token。

Gemini reason: A UI status message from Android. '画中画' (picture-in-picture) is a good test for modern technical jargon conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 03. aosp-framework-zh-rcn-v1/string-886a05c43b8972ad

Changed: `risk`

Input:

```text
读取网络使用情况历史记录
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 Android 介面字串；用於檢驗臺灣 UI 用語、一般字形與受保護 token。

Gemini reason: A permission-related description from Android UI. It contains multiple characters that have direct traditional counterparts ('读', '网', '络', '-用', '-况', '历', '史', '记', '录'), making it a solid baseline test.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 04. aosp-framework-zh-rcn-v1/string-a82a9893561bed3f

Changed: `risk`

Input:

```text
网上诱骗警报
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 Android 介面字串；用於檢驗臺灣 UI 用語、一般字形與受保護 token。

Gemini reason: A security-related UI string. '诱骗' (phishing/luring) is a relatively formal term.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 05. aosp-framework-zh-rcn-v1/string-d0b75c9e07213975

Changed: `risk`

Input:

```text
允许应用请求相应的权限，以便忽略针对该应用的电池优化。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 Android 介面字串；用於檢驗臺灣 UI 用語、一般字形與受保護 token。

Gemini reason: A formal permission string from Android. The term '优化' (optimization) is common in IT contexts and should convert to '優化'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 06. aosp-framework-zh-rcn-v1/string-e0ddd1b2aecd1d59

Changed: `risk`

Input:

```text
用户取消了指纹操作
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 Android 介面字串；用於檢驗臺灣 UI 用語、一般字形與受保護 token。

Gemini reason: A standard UI status message from the Android fingerprint authentication system. Clear and context-specific.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 07. aosp-framework-zh-rcn-v1/string-ec7b57c9f7b40775

Changed: `domain`

Input:

```text
IMPI 解锁请求失败。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 Android 介面字串；用於檢驗臺灣 UI 用語、一般字形與受保護 token。

Gemini reason: A technical error message containing the acronym 'IMPI' (IP Multimedia Private Identity). The acronym must be preserved, making it a good test for over-conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 08. census-newsroom-zh-hans-v1/page-01-sentence-027

Changed: `risk`

Input:

```text
与上一个十年一样，人口普查局计划为此发布多项产品 — 每种都有自己的一组优缺点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Standard formal Simplified Chinese sentence from a government press release.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 09. census-newsroom-zh-hans-v1/page-02-sentence-006

Changed: `script, risk`

Input:

```text
从 3 月 12 日至 20 日，全国 36.2% 的住户在邮政信箱收到送达的邀请后已经回答了 2020 年人口普查。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Formal Simplified Chinese sentence with numbers and dates, which do not alter the script classification.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 10. census-newsroom-zh-hans-v1/page-02-sentence-007

Changed: `risk`

Input:

```text
地图每周七天每天更新回答率，这样公众可以看到他们的社区与全国和其他地区的对比。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Standard formal Simplified Chinese. The word '地图' is a common term and serves as a basic conversion check.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 11. census-newsroom-zh-hans-v1/page-02-sentence-019

Changed: `domain, risk`

Input:

```text
回答时，您可以使用邀请函中的人口普查号码 (Census ID) 或者提供您的地址。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Mixed script (Simplified Chinese + Latin). The English token 'Census ID' must be preserved, making it a high-stakes instructional text.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 12. census-newsroom-zh-hans-v1/page-02-sentence-025

Changed: `risk`

Input:

```text
人口普查局正在采取这一步骤，以帮助保护美国公众、人口普查局雇员以及每一位处于临时人口普查员招聘程序的人的健康和安全。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Formal Simplified Chinese sentence. Contains '程序', testing if the converter correctly handles characters that are part of common IT and general terms.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 13. census-newsroom-zh-hans-v1/page-03-sentence-019

Changed: `risk`

Input:

```text
人口普查局进行这次调查是为了衡量 2020 年人口普查中住房单元和居住在住房单元的人口覆盖率。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Standard formal Simplified Chinese sentence containing common terms like '单元' and '覆盖率'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 14. census-newsroom-zh-hans-v1/page-04-sentence-020

Changed: `eligible, domain, risk`

Input:

```text
人口普查统计数据将用于决定各州在美国众议院的席位数量，以及州、地方和联邦定立法人员未来 10 年如何将数千亿美元的公共资金分配给紧急响应、学校、医院和桥梁等关公共服务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | formal_news | baseline_guard | high | minor_grammatical_error |

Codex reason: 句中「聯邦定立法人員」與「等關公共服務」有明顯黏字或缺字，正式語意不可靠。

Gemini reason: The input contains a minor grammatical error or typo: '等关公共服务' should likely be '等公共服务'. The sentence is otherwise a valid formal text.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 15. census-newsroom-zh-hans-v1/page-06-sentence-014

Changed: `risk`

Input:

```text
从 7 月中旬开始，六个地区人口普查办公室 (ACO)（每个人口普查区一个办公室）将开始对尚未回答 2020 年人口普查的住户进行访谈。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Mixed script due to the presence of the Latin abbreviation 'ACO', which must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 16. census-newsroom-zh-hans-v1/page-06-sentence-020

Changed: `risk`

Input:

```text
人口普查局将偏远地区 Alaska 操作延期到八月份。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Mixed script due to the Latin proper noun 'Alaska'. The word '操作' is also a relevant keyword.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 17. census-newsroom-zh-hans-v1/page-06-sentence-023

Changed: `risk`

Input:

```text
人口普查局将在 9 月份算上居住在暂时居住地点的人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Standard formal Simplified Chinese sentence. The character '算' is a common conversion case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 18. census-newsroom-zh-hans-v1/page-06-sentence-036

Changed: `risk`

Input:

```text
扩大后的广告活动以 33 种语言吸引了新的受众，使得到某种程度付费媒体支持的语言总数达到 45 种非英语语言。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Formal Simplified Chinese. A good test for the context-dependent '后'/'後' conversion ('扩大后').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 19. census-newsroom-zh-hans-v1/page-08-sentence-003

Changed: `risk`

Input:

```text
通过在 2020 年人口普查的首批结果之前公布这些估计数据，人口分析提供了一种独立的人口测量方法，以便与官方人口普查人数进行比较。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Formal Simplified Chinese. Provides a test for context-sensitive characters, specifically '布' in '公布' which should convert to '佈'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 20. census-newsroom-zh-hans-v1/page-08-sentence-010

Changed: `risk`

Input:

```text
因此我们使用人口普查局的美国社区问卷调查 (American Community Survey) 和其他来源的数据来估计国际人口迁移。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Mixed script due to the long Latin phrase 'American Community Survey', which must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 21. census-newsroom-zh-hans-v1/page-08-sentence-024

Changed: `risk`

Input:

```text
除了对国家总人口的估计，2020 年人口分析还提供了国家级别按年龄、性别、广泛的种族和西班牙后裔群组划分的美国人口估计，与 2010 年提供的信息相比，今年公布的年龄细节有所扩大。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Long but valid formal Simplified Chinese sentence. Another test case for the '后'/'後' conversion via the word '后裔'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 22. census-newsroom-zh-hans-v1/page-09-sentence-002

Changed: `risk`

Input:

```text
明信片警示住户人口普查员将很快上门送达人口普查邀请，或稍候对他们进行访谈。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的政府新聞或人口統計敘述；用於檢驗正式用語與統計術語。

Gemini reason: Standard formal Simplified Chinese sentence. The word '明信片' provides a check for polyphone handling, although it's a common case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 23. chromium-strings-zh-cn-v1/translation-8862326446509486874

Changed: `risk`

Input:

```text
您的权限不足，无法进行系统级安装。请尝试以管理员身份再次运行安装程序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的瀏覽器介面字串；用於檢驗臺灣 UI 用語、產品名稱與受保護 token。

Gemini reason: A clear, formal instruction in Simplified Chinese using common IT terms like '管理员' (administrator) and '安装程序' (installer), making it a solid baseline case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 24. kubernetes-docs-zh-cn-v1/page-02-sentence-0028

Changed: `risk`

Input:

```text
指令式对象配置更适合文件，而非目录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的技術文件敘述；用於檢驗 Kubernetes 術語、指令與識別碼保留。

Gemini reason: Standard technical documentation sentence. The term '对象' (object) is a key concept.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 25. kubernetes-docs-zh-cn-v1/page-03-sentence-0029

Changed: `risk`

Input:

```text
Pod 的阶段（Phase）是 Pod 在其生命周期中所处位置的简单宏观概述。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的技術文件敘述；用於檢驗 Kubernetes 術語、指令與識別碼保留。

Gemini reason: Contains an English technical term 'Phase' alongside its Chinese translation. The English term should be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 26. kubernetes-docs-zh-cn-v1/page-03-sentence-0260

Changed: `risk`

Input:

```text
设计的目标是令你能够请求删除进程，并且知道进程何时被终止，同时也能够确保删除操作终将完成。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的技術文件敘述；用於檢驗 Kubernetes 術語、指令與識別碼保留。

Gemini reason: A standard technical sentence describing process termination logic.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 27. kubernetes-docs-zh-cn-v1/page-04-sentence-0168

Changed: `risk`

Input:

```text
此字段可能会在未来的 API 版本中被移除。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的技術文件敘述；用於檢驗 Kubernetes 術語、指令與識別碼保留。

Gemini reason: Contains the common English acronym 'API', which should be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 28. osha-disaster-cleanup-simplified-v1/sentence-003

Changed: `risk`

Input:

```text
OSHA敦促从事清理和重建工作的雇主和工人了解这些危害以及如何保护工人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: Formal text from an official government safety document. The presence of the proper noun 'OSHA' makes the script mixed.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 29. osha-disaster-cleanup-simplified-v1/sentence-006

Changed: `risk`

Input:

```text
根据对危险的初步评估，雇主需要为工人提供适当的个人防护设备、培训和信息，以便工人安全地进行工作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: Standard formal sentence. Contains common but important terms like '评估' (pínggū - assessment).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 30. osha-disaster-cleanup-simplified-v1/sentence-012

Changed: `risk`

Input:

```text
只有经过培训并配备适当个人防护设备的工人才能清理有毒化学品、其他危险废弃物和霉菌。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: The phrase '配备' (pèibèi - to equip) is a good test case; the character '配' must be handled as part of a compound word to avoid incorrect conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 31. osha-disaster-cleanup-simplified-v1/sentence-013

Changed: `risk`

Input:

```text
及时注射破伤风疫苗（最近10年内）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: Medical context. The term '疫苗' (yìmiáo - vaccine) is standard across most Chinese-speaking regions.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 32. osha-disaster-cleanup-simplified-v1/sentence-018

Changed: `risk`

Input:

```text
保证充足且干净的饮用水和清洁用水的供应。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: Classic test case for the character '干'. In '干净' (gānjìng - clean), it must be converted to '乾' (gān), not '幹' (gàn).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 33. osha-disaster-cleanup-simplified-v1/sentence-021

Changed: `risk`

Input:

```text
在倒下的电力线路周围做出清晰的标记，以标示出危险区域。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: Straightforward sentence. The word '标记' (biāojì - mark/marker) converts directly to '標記'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 34. osha-disaster-cleanup-simplified-v1/sentence-035

Changed: `risk`

Input:

```text
使用机械设备抬起重物。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: Good test for context-sensitive character mapping. The character '机' in '机械' (jīxiè - machinery) must be converted to '機'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 35. osha-disaster-cleanup-simplified-v1/sentence-046

Changed: `risk`

Input:

```text
严禁在室内或车库等密闭空间内运行便携式发电机。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: A critical safety warning. Contains several compound words that must be converted as units: '严禁' (yánjìn), '便携式' (biànxiéshì), '发电机' (fādiànjī).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 36. osha-disaster-cleanup-simplified-v1/sentence-058

Changed: `eligible, domain, risk`

Input:

```text
沟和基坑的挖掘事故（塌方）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | high_stakes | candidate_gap | medium | - |

Codex reason: 僅為「溝和基坑的挖掘事故（塌方）」表格項目，缺少可獨立判讀的完整敘述。

Gemini reason: Contains technical terms ('基坑' - foundation pit, '塌方' - collapse/landslide) for which standard terminology might differ in engineering contexts across regions.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 37. osha-disaster-cleanup-simplified-v1/sentence-064

Changed: `risk`

Input:

```text
相关的详细信息，请参阅29 CFR 1926.651和1926.652。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的職業安全指引；涉及安全語意，適合檢驗專業詞彙與單位保留。

Gemini reason: A reference to a legal code (29 CFR 1926.651). The non-Chinese elements (letters, numbers, punctuation) must be preserved exactly.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 38. osha-disaster-cleanup-simplified-v1/sentence-073

Changed: `eligible, domain, risk`

Input:

```text
职业安全与健康管理局本文属于介绍OSHA计划、政策或标准的重点信息简报系列，它没有引入任何新的合规要求。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | heading_text_join |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 機關頁首「職業安全與健康管理局」與簡報正文直接黏連，不是乾淨的單一句子。

Gemini reason: A complex sentence containing the proper noun 'OSHA'. It also includes '计划' (jìhuà), which maps to '計畫' or '計劃' depending on nuance, and '合规' (héguī - compliance), which has direct but potentially stylistically different equivalents.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 39. ready-gov-home-fires-zh-hans-v1/sentence-003

Changed: `eligible, domain, risk`

Input:

```text
浓浓的黑烟只需几分钟就能充满房屋或被火焰吞没。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 「濃煙充滿房屋或被火焰吞沒」的並列主體錯接，語意不完整。

Gemini reason: Straightforward public safety sentence.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 40. ready-gov-home-fires-zh-hans-v1/sentence-011

Changed: `risk`

Input:

```text
除非用 10 年有效期的锂电池，每年都要换两次电池。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與臺灣用語。

Gemini reason: Standard conversion test for a technical but common term ('锂电池').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 41. ready-gov-home-fires-zh-hans-v1/sentence-025

Changed: `risk`

Input:

```text
如用助行器或轮椅，检查所有出口，确保通道通畅。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與臺灣用語。

Gemini reason: Standard safety instruction with accessibility terms like '轮椅' (wheelchair).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 42. ready-gov-home-fires-zh-hans-v1/sentence-031

Changed: `risk`

Input:

```text
浓烟和毒气会先沿着天花板聚集。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與臺灣用語。

Gemini reason: Basic fire safety science sentence.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 43. ready-gov-home-fires-zh-hans-v1/sentence-041

Changed: `risk`

Input:

```text
如果自己或他人无法停下、趴下和滚动，用毯子或毛巾扑灭火焰。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與臺灣用語。

Gemini reason: Tests a critical, well-known safety instruction ('stop, drop, and roll').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 44. ready-gov-home-fires-zh-hans-v1/sentence-042

Changed: `risk`

Input:

```text
立即用冷水治疗烧伤 3 到 5 分钟。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與臺灣用語。

Gemini reason: Simple and direct first-aid instruction where correctness is critical.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 45. ready-gov-home-fires-zh-hans-v1/sentence-043

Changed: `eligible, domain, risk`

Input:

```text
用干净的干布盖住。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 「用乾淨的乾布蓋住」缺少受詞，必須依賴上一句燒傷語境。

Gemini reason: Excellent test for the polysemous character '干'. In this context ('干布' - dry cloth), '干' (gān) should be converted to '乾', not '幹'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 46. ready-gov-home-fires-zh-hans-v1/sentence-052

Changed: `risk`

Input:

```text
将火灾告诉房贷公司。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與臺灣用語。

Gemini reason: A post-disaster financial instruction. '房贷' (mortgage) is a common term.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 47. ready-gov-home-fires-zh-hans-v1/sentence-056

Changed: `risk`

Input:

```text
如要离开，即使是很短的时间，也要关掉炉子。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與臺灣用語。

Gemini reason: Tests conversion of the common verb phrase '关掉' (guān diào), which should become '關掉' or a similar regional equivalent like '關上'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 48. ready-gov-home-fires-zh-hans-v1/sentence-064

Changed: `risk`

Input:

```text
晚上或离开家时关掉节日装饰灯。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與臺灣用語。

Gemini reason: Holiday fire safety instruction.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 49. ready-gov-home-fires-zh-hans-v1/sentence-078

Changed: `risk`

Input:

```text
如用加热器，房间通风要好，并远离窗帘和其他易燃物品。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的居家防火指引；涉及安全語意，適合檢驗防災詞彙與臺灣用語。

Gemini reason: Space heater safety instructions.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`
