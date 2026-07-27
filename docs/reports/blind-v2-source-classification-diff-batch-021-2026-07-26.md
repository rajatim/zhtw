<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 021 (2026-07-26)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `3364332dbd8c9099ee251f466a38a22ba64aee66b00c6d5cdfed6324000f45d9`
Cases: 100
Exact Codex/Gemini classifications: 47
Maintainer review queue: 53

Field differences:

- Eligibility: 0
- Script: 40
- Domain: 0
- Risk: 13

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 53 advisory disagreements and batch-confirmed the 47 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. zhtw-project-balanced-baseline-guard-v1/formal-011

Changed: `risk`

Input:

```text
负责人已说明计划调整的主要原因。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣常用詞或介面用語正規化候選。

Gemini reason: 標準正式用語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 02. zhtw-project-balanced-baseline-guard-v1/formal-016

Changed: `script`

Input:

```text
文件编号 DOC-2026-041 应列在首页右上角。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的實體名稱。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 03. zhtw-project-balanced-baseline-guard-v1/formal-017

Changed: `script`

Input:

```text
附件名称 Appendix C 保留英文格式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的實體名稱。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 04. zhtw-project-balanced-baseline-guard-v1/formal-018

Changed: `script`

Input:

```text
表格中的项目代码 A-104 不得变更。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的實體名稱。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 05. zhtw-project-balanced-baseline-guard-v1/formal-019

Changed: `script`

Input:

```text
公文引用 ISO 8601 时保留标准编号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的實體名稱。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 06. zhtw-project-balanced-baseline-guard-v1/formal-020

Changed: `script`

Input:

```text
会议记录中的网址 https://example.org/report 保持不变。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的網址。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 07. zhtw-project-balanced-baseline-guard-v1/formal-021

Changed: `script`

Input:

```text
报告标题沿用“Project North Star”正式名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的實體名稱。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 08. zhtw-project-balanced-baseline-guard-v1/formal-022

Changed: `script`

Input:

```text
统计表以 FY2026 表示本财政年度。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的實體名稱。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 09. zhtw-project-balanced-baseline-guard-v1/formal-023

Changed: `script`

Input:

```text
公告中的联系信箱 service@example.org 不应改写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的電子郵件地址。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 10. zhtw-project-balanced-baseline-guard-v1/formal-024

Changed: `script`

Input:

```text
决议编号 RES-18/7 必须与附件一致。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的實體名稱。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 11. zhtw-project-balanced-baseline-guard-v1/formal-025

Changed: `script`

Input:

```text
引用原文“as is”时应保留引号内文字。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的引言。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 12. zhtw-project-balanced-baseline-guard-v1/llm-001

Changed: `risk`

Input:

```text
系统先读取用户问题，再生成一段简短摘要。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣常用詞或介面用語正規化候選。

Gemini reason: 描述大型語言模型或相關系統行為。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 13. zhtw-project-balanced-baseline-guard-v1/llm-016

Changed: `script`

Input:

```text
批次名称 batch_2026_07 必须保持原样。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的技術性字串。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 14. zhtw-project-balanced-baseline-guard-v1/llm-017

Changed: `script`

Input:

```text
引用中的“human-in-the-loop”不得改写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的技術性字串。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 15. zhtw-project-balanced-baseline-guard-v1/llm-018

Changed: `script`

Input:

```text
输出对象必须保留字段 review_status。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的技術性字串。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 16. zhtw-project-balanced-baseline-guard-v1/llm-019

Changed: `script`

Input:

```text
系统以 request_id 对应每一次模型请求。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的技術性字串。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 17. zhtw-project-balanced-baseline-guard-v1/llm-020

Changed: `script`

Input:

```text
提示中的 {{source_text}} 是待替换变量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的變數。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 18. zhtw-project-balanced-baseline-guard-v1/llm-021

Changed: `script`

Input:

```text
模型版本名称 acme-reasoner-v2 不应翻译。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的技術性字串。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 19. zhtw-project-balanced-baseline-guard-v1/llm-022

Changed: `script`

Input:

```text
评分报告保留指标名称 groundedness。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的技術性字串。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 20. zhtw-project-balanced-baseline-guard-v1/llm-023

Changed: `script`

Input:

```text
引用编号 [R-17] 必须对应原始资料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的技術性字串。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 21. zhtw-project-balanced-baseline-guard-v1/llm-024

Changed: `script`

Input:

```text
系统消息中的 XML 标签 <policy> 必须成对出现。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的 XML 標籤。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 22. zhtw-project-balanced-baseline-guard-v1/llm-025

Changed: `script`

Input:

```text
失败记录以 status=needs_review 标记。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應轉換的技術性字串。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 23. zhtw-project-balanced-baseline-guard-v1/social-007

Changed: `risk`

Input:

```text
这段视频我已经看过两次了。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣常用詞或介面用語正規化候選。

Gemini reason: 日常社交對話。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 24. zhtw-project-balanced-baseline-guard-v1/social-011

Changed: `risk`

Input:

```text
这辆自行车骑起来很轻松。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣常用詞或介面用語正規化候選。

Gemini reason: 日常社交對話。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 25. zhtw-project-balanced-baseline-guard-v1/social-016

Changed: `script`

Input:

```text
群组名称 Weekend Plan 不需要翻译。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的英文名稱。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 26. zhtw-project-balanced-baseline-guard-v1/social-017

Changed: `script`

Input:

```text
活动标签 #CityWalk2026 保持原样。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的標籤。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 27. zhtw-project-balanced-baseline-guard-v1/social-018

Changed: `script`

Input:

```text
朋友传来的代码是 RSVP-2048。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的代碼。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 28. zhtw-project-balanced-baseline-guard-v1/social-019

Changed: `script`

Input:

```text
贴文引用“stay curious”这句话。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的引言。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 29. zhtw-project-balanced-baseline-guard-v1/social-020

Changed: `script`

Input:

```text
照片说明保留地点名称 Green Lake。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的英文名稱。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 30. zhtw-project-balanced-baseline-guard-v1/social-021

Changed: `script`

Input:

```text
聊天室里的 /remind 指令会建立提醒。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 31. zhtw-project-balanced-baseline-guard-v1/social-022

Changed: `script`

Input:

```text
投票选项 C 保留字母编号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的選項標號。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 32. zhtw-project-balanced-baseline-guard-v1/social-023

Changed: `script`

Input:

```text
分享链接中的 ref=summer 参数不要删除。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的 URL 參數。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 33. zhtw-project-balanced-baseline-guard-v1/social-024

Changed: `script`

Input:

```text
个人简介写着 Product Designer @ Acme。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的實體名稱與符號。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 34. zhtw-project-balanced-baseline-guard-v1/social-025

Changed: `script`

Input:

```text
讨论串编号 thread-105 方便之后查找。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的 ID。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 35. zhtw-project-balanced-baseline-guard-v1/ui-002

Changed: `risk`

Input:

```text
用户可以在设置中调整文字大小。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣常用詞或介面用語正規化候選。

Gemini reason: 使用者介面(UI)文字。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 36. zhtw-project-balanced-baseline-guard-v1/ui-003

Changed: `risk`

Input:

```text
上传完成后页面会显示成功消息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣常用詞或介面用語正規化候選。

Gemini reason: 使用者介面(UI)文字。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 37. zhtw-project-balanced-baseline-guard-v1/ui-004

Changed: `risk`

Input:

```text
搜索结果按照更新时间排列。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣常用詞或介面用語正規化候選。

Gemini reason: 使用者介面(UI)文字。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 38. zhtw-project-balanced-baseline-guard-v1/ui-005

Changed: `risk`

Input:

```text
点击按钮即可返回上一个页面。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣常用詞或介面用語正規化候選。

Gemini reason: 使用者介面(UI)文字。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 39. zhtw-project-balanced-baseline-guard-v1/ui-008

Changed: `risk`

Input:

```text
用户取消操作后关闭对话框。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣常用詞或介面用語正規化候選。

Gemini reason: 使用者介面(UI)文字。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 40. zhtw-project-balanced-baseline-guard-v1/ui-009

Changed: `risk`

Input:

```text
文件下载完成时会出现通知。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣常用詞或介面用語正規化候選。

Gemini reason: 使用者介面(UI)文字。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 41. zhtw-project-balanced-baseline-guard-v1/ui-010

Changed: `risk`

Input:

```text
切换分页不会清除已经输入的内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣常用詞或介面用語正規化候選。

Gemini reason: 使用者介面(UI)文字。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 42. zhtw-project-balanced-baseline-guard-v1/ui-012

Changed: `risk`

Input:

```text
错误消息应说明无法完成操作的原因。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣常用詞或介面用語正規化候選。

Gemini reason: 使用者介面(UI)文字。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 43. zhtw-project-balanced-baseline-guard-v1/ui-014

Changed: `risk`

Input:

```text
表单送出前会检查必填字段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣常用詞或介面用語正規化候選。

Gemini reason: 使用者介面(UI)文字。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 44. zhtw-project-balanced-baseline-guard-v1/ui-016

Changed: `script`

Input:

```text
按钮文字为“继续使用 {account_name}”。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的變數。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 45. zhtw-project-balanced-baseline-guard-v1/ui-017

Changed: `script`

Input:

```text
对话框标题保留产品名称 Acme Cloud。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的產品名稱。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 46. zhtw-project-balanced-baseline-guard-v1/ui-018

Changed: `script`

Input:

```text
错误代码 ERR_NETWORK_OFFLINE 显示在说明下方。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的錯誤碼。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 47. zhtw-project-balanced-baseline-guard-v1/ui-019

Changed: `script`

Input:

```text
分页参数 page_size=50 不随语言改变。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的 URL 參數。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 48. zhtw-project-balanced-baseline-guard-v1/ui-020

Changed: `script`

Input:

```text
帮助链接指向 /docs/getting-started。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的路徑。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 49. zhtw-project-balanced-baseline-guard-v1/ui-021

Changed: `script`

Input:

```text
快捷键 Ctrl+Alt+K 显示在菜单右侧。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的快捷鍵組合。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 50. zhtw-project-balanced-baseline-guard-v1/ui-022

Changed: `script`

Input:

```text
日期格式 YYYY/MM/DD 由地区设置决定。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的日期格式碼。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 51. zhtw-project-balanced-baseline-guard-v1/ui-023

Changed: `script`

Input:

```text
状态值 pending_review 仅供系统内部使用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的狀態值。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 52. zhtw-project-balanced-baseline-guard-v1/ui-024

Changed: `script`

Input:

```text
图标的 aria-describedby 属性引用提示文字。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的 HTML 屬性。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 53. zhtw-project-balanced-baseline-guard-v1/ui-025

Changed: `script`

Input:

```text
版本信息显示 build-2026.07.26。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；識別碼、引用、標籤或格式字串必須保守保留。

Gemini reason: 包含不應翻譯的版本號。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`
