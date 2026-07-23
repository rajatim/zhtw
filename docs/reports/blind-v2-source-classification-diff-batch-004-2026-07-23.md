<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 004 (2026-07-23)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `014e1cc3e3dba34464bef7f6f8e566e9a5e00d2b7443ac7d56a883b784dca93f`
Cases: 100
Exact Codex/Gemini classifications: 69
Maintainer review queue: 31

Field differences:

- Eligibility: 0
- Script: 0
- Domain: 5
- Risk: 27

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

The maintainer resolved all 31 advisory disagreements and batch-confirmed the 69 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. zhtw-project-llm-product-v1/llm-007

Changed: `risk`

Input:

```text
用户停止生成后，不再发送新的模型请求。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「用戶」、「模型請求」等 LLM 相關術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 02. zhtw-project-llm-product-v1/llm-019

Changed: `risk`

Input:

```text
模型切换后，界面需要显示当前使用的模型名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「模型」、「界面」等 LLM/UI 術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 03. zhtw-project-llm-product-v1/llm-026

Changed: `domain, risk`

Input:

```text
审核结果只能作为建议，最终决定由授权人员确认。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 含臺灣產品或技術語境可能需要調整的區域術語，列為候選缺口。

Gemini reason: 通用審核流程說明，地區詞彙差異風險較低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 04. zhtw-project-llm-product-v1/llm-029

Changed: `risk`

Input:

```text
工具返回的数据不得被当作新的系统指令执行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 含模板、程式符號或需精確保留的技術邊界，列為過度轉換防護。

Gemini reason: 涉及「工具返回的數據」、「系統指令」等 LLM 安全術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 05. zhtw-project-llm-product-v1/llm-032

Changed: `domain`

Input:

```text
自动修改文件前，先显示将要变更的文件清单。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含臺灣產品或技術語境可能需要調整的區域術語，列為候選缺口。

Gemini reason: 涉及「自動修改文件」等 CLI/Agent 功能術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 06. zhtw-project-llm-product-v1/llm-033

Changed: `domain`

Input:

```text
代码审查通过前，不得自动合并到主分支。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含臺灣產品或技術語境可能需要調整的區域術語，列為候選缺口。

Gemini reason: 涉及「代碼審查」、「主分支」等 Git 工作流程術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 07. zhtw-project-llm-product-v1/llm-035

Changed: `risk`

Input:

```text
同一评测只能在固定模型和固定参数下比较。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「評測」、「模型」、「參數」等 LLM 評估術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 08. zhtw-project-llm-product-v1/llm-038

Changed: `risk`

Input:

```text
两个审核模型意见一致，也不能替代人工确认。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「審核模型」、「人工確認」等 LLM 評估流程術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 09. zhtw-project-llm-product-v1/llm-042

Changed: `risk`

Input:

```text
模型输出繁体中文时，不要自动改写专有名词。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 含模板、程式符號或需精確保留的技術邊界，列為過度轉換防護。

Gemini reason: 涉及「繁體中文」、「專有名詞」等語言處理術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 10. zhtw-project-llm-product-v1/llm-048

Changed: `risk`

Input:

```text
翻译请求包含代码时，只翻译代码之外的说明文字。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 含模板、程式符號或需精確保留的技術邊界，列為過度轉換防護。

Gemini reason: 涉及「翻譯請求」、「代碼」等術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 11. zhtw-project-llm-product-v1/llm-049

Changed: `domain`

Input:

```text
批量生成任务应允许单独重试失败的项目。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含臺灣產品或技術語境可能需要調整的區域術語，列為候選缺口。

Gemini reason: 涉及「批量生成任務」等術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 12. zhtw-project-llm-product-v1/llm-050

Changed: `domain`

Input:

```text
服务降级时，明确告知哪些模型功能暂时不可用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含臺灣產品或技術語境可能需要調整的區域術語，列為候選缺口。

Gemini reason: 涉及「服務降級」、「模型功能」等後端服務術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 13. zhtw-project-ui-i18n-v1/ui-001

Changed: `risk`

Input:

```text
用户点击保存按钮后，页面应显示成功提示。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「用戶」、「按鈕」、「頁面」等 UI 術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 14. zhtw-project-ui-i18n-v1/ui-002

Changed: `risk`

Input:

```text
表单提交失败时，应将焦点移到第一个错误字段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「表單」、「焦點」等 UI 術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 15. zhtw-project-ui-i18n-v1/ui-004

Changed: `risk`

Input:

```text
上传失败后，保留用户已经选择的文件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「上傳」、「文件」等 UI 術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 16. zhtw-project-ui-i18n-v1/ui-005

Changed: `risk`

Input:

```text
文件大小超过限制时，提示允许的最大容量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「文件大小」、「容量」等 UI 術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 17. zhtw-project-ui-i18n-v1/ui-006

Changed: `risk`

Input:

```text
日期选择器应支持键盘方向键操作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「日期選擇器」、「鍵盤」等 UI 無障礙術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 18. zhtw-project-ui-i18n-v1/ui-008

Changed: `risk`

Input:

```text
搜索结果为空时，显示清晰的空白状态。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「搜索結果」、「空白狀態」等 UI 術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 19. zhtw-project-ui-i18n-v1/ui-012

Changed: `risk`

Input:

```text
阿拉伯语界面启用从右到左的布局方向。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「界面」、「佈局方向」等 UI 國際化 (RTL) 術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 20. zhtw-project-ui-i18n-v1/ui-014

Changed: `risk`

Input:

```text
系统时区变化后，日程时间需要重新计算。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「時區」、「日程」等 UI 國際化術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 21. zhtw-project-ui-i18n-v1/ui-015

Changed: `risk`

Input:

```text
日期格式应遵循用户选择的语言区域。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「日期格式」、「語言區域」等 UI 國際化術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 22. zhtw-project-ui-i18n-v1/ui-019

Changed: `risk`

Input:

```text
复数消息应根据数量选择正确的语言形式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「複數消息」等 UI 國際化 (pluralization) 術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 23. zhtw-project-ui-i18n-v1/ui-021

Changed: `risk`

Input:

```text
图片未加载时，替代文字仍应说明图片内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「替代文字」等 UI 無障礙術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 24. zhtw-project-ui-i18n-v1/ui-031

Changed: `risk`

Input:

```text
按钮正在处理请求时，应防止用户重复提交。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「重複提交」等 UI 表單術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 25. zhtw-project-ui-i18n-v1/ui-034

Changed: `risk`

Input:

```text
通知中心按照时间倒序显示未读消息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「通知中心」、「未讀消息」等 UI 術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 26. zhtw-project-ui-i18n-v1/ui-035

Changed: `risk`

Input:

```text
已读状态应在多个设备之间保持同步。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「已讀狀態」、「設備同步」等 UI 術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 27. zhtw-project-ui-i18n-v1/ui-037

Changed: `risk`

Input:

```text
自动保存失败时，明确说明本地草稿是否仍然存在。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「自動保存」、「本地草稿」等 UI 術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 28. zhtw-project-ui-i18n-v1/ui-039

Changed: `risk`

Input:

```text
电话号码输入框不要强制使用单一国家格式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「電話號碼輸入框」、「國家格式」等 UI 國際化術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 29. zhtw-project-ui-i18n-v1/ui-042

Changed: `risk`

Input:

```text
用户选择深色模式后，系统刷新页面仍应保留设置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「深色模式」、「刷新頁面」等 UI 術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 30. zhtw-project-ui-i18n-v1/ui-043

Changed: `risk`

Input:

```text
高对比度模式下，禁用状态也必须清楚可辨。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「高對比度模式」等 UI 無障礙術語，有地区词汇差异风险。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 31. zhtw-project-ui-i18n-v1/ui-045

Changed: `risk`

Input:

```text
错误提示出现时，不应导致提交按钮突然移动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整可判讀，主要覆蓋一般字形轉換與不應擴張的基線行為。

Gemini reason: 涉及「錯誤提示」、「提交按鈕」等 UI 術語，有地區詞彙差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`
