<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 011 (2026-07-24)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `862db4947e11dc11df809b01d42d0b08e1e65135b978b70de8259552c2909970`
Cases: 100
Exact Codex/Gemini classifications: 35
Maintainer review queue: 65

Field differences:

- Eligibility: 4
- Script: 0
- Domain: 31
- Risk: 50

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

The maintainer resolved all 65 advisory disagreements and batch-confirmed the 35 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. vscode-loc-zh-hans-v1/entry-0051ac02d21f3951

Changed: `domain`

Input:

```text
你将信任 {1} 上“{0}”下的所有存储库和分支。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: 包含代碼佔位符。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 02. vscode-loc-zh-hans-v1/entry-0069e37b6f0e20de

Changed: `risk`

Input:

```text
智能体会话视图的图标
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的 AI／聊天產品介面文字。

Gemini reason: AI 代理相關術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 03. vscode-loc-zh-hans-v1/entry-09618f3bdd3c063c

Changed: `domain`

Input:

```text
重启扩展
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: 「擴展」在台灣多稱「擴充功能」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 04. vscode-loc-zh-hans-v1/entry-0cfd4e1544007e6f

Changed: `risk`

Input:

```text
表示底部面板对齐方式设为居中
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 05. vscode-loc-zh-hans-v1/entry-0e09bd6f9c17b08d

Changed: `domain`

Input:

```text
添加新挂钩...
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: 「掛鉤」(hook) 為開發術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 06. vscode-loc-zh-hans-v1/entry-0eb9c25c118ea361

Changed: `risk`

Input:

```text
已配置制表符大小
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 07. vscode-loc-zh-hans-v1/entry-185b91993d167e5b

Changed: `risk`

Input:

```text
操作栏中切换的操作项的背景色。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 08. vscode-loc-zh-hans-v1/entry-1c52c0716654e119

Changed: `domain`

Input:

```text
是否将 {1} 文件中出现的 {0} 替换为“{2}”?
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: 包含代碼佔位符。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 09. vscode-loc-zh-hans-v1/entry-248c8ba7416e401a

Changed: `risk`

Input:

```text
将大写和小写名称混合在一起。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 10. vscode-loc-zh-hans-v1/entry-26688e3e2c17a256

Changed: `domain`

Input:

```text
此请求包含一个响应 API tool_search_output 项。未捕获到上一个响应续传标记，因此显示的输入可能是完整请求或历史切片请求，而非仅续传增量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立裁決的 AI／聊天產品介面文字。

Gemini reason: 包含 API 特定術語 `tool_search_output`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 11. vscode-loc-zh-hans-v1/entry-28115d85b27abca4

Changed: `domain, risk`

Input:

```text
控制搜索结果的最大数目，可将其设置为 “null”(空)，以返回无限结果。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: 包含程式碼關鍵字 `null`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 12. vscode-loc-zh-hans-v1/entry-30855006f8ec5f0e

Changed: `risk`

Input:

```text
删除自动插入的尾随空白符号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 13. vscode-loc-zh-hans-v1/entry-30c400765bc76010

Changed: `risk`

Input:

```text
导出的聊天没有存储库上下文。未检测到 Git 存储库。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立裁決的 AI／聊天產品介面文字。

Gemini reason: 包含產品名稱 Git，且與 AI 聊天功能相關。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 14. vscode-loc-zh-hans-v1/entry-3bc2558a39853869

Changed: `domain`

Input:

```text
“editorIndentGuide.background” 已弃用。请改用 “editorIndentGuide.background1”。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: 包含程式碼設定鍵 `editorIndentGuide.background` 及 `editorIndentGuide.background1`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 15. vscode-loc-zh-hans-v1/entry-3da3a66cc6801c1f

Changed: `eligible, domain, risk`

Input:

```text
自以下时间已修改的文件:
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | heading_fragment |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 冒號結尾的標題失去後續列表或正文，無法獨立裁決。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 16. vscode-loc-zh-hans-v1/entry-451643b3ebef0ac0

Changed: `domain`

Input:

```text
速览视图编辑器背景色。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: 「速覽」可能存在地區用詞差異（如「快速查看」）。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 17. vscode-loc-zh-hans-v1/entry-4c58151a363a4042

Changed: `risk`

Input:

```text
管理受信任的域
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 18. vscode-loc-zh-hans-v1/entry-50fe5444ea0eead4

Changed: `risk`

Input:

```text
挂钩命令必须至少指定“command”、“windows”、“linux”或“osx”中的一项。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: 包含程式碼關鍵字 `command`, `windows`, `linux`, `osx`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 19. vscode-loc-zh-hans-v1/entry-5442b7940224caa1

Changed: `risk`

Input:

```text
需要聊天用户操作
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的 AI／聊天產品介面文字。

Gemini reason: AI 聊天相關術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 20. vscode-loc-zh-hans-v1/entry-59e7eccd502ceb69

Changed: `domain`

Input:

```text
MCP 服务器“{0}”需要访问 {1} 帐户“{2}”。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: 包含縮寫詞 MCP 及代碼佔位符，涉及帳號存取安全議題。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 21. vscode-loc-zh-hans-v1/entry-5b0abfcd5e3e929e

Changed: `eligible, domain, risk`

Input:

```text
规划方法
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | no | null | null | high | context_dependent_fragment |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: 語意不明確，高度依賴上下文。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 22. vscode-loc-zh-hans-v1/entry-5dcc08b30461b6b4

Changed: `risk`

Input:

```text
当前可见快速输入的类型
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 23. vscode-loc-zh-hans-v1/entry-5f5b0496699c2ff0

Changed: `domain`

Input:

```text
扩展视图中“配置建议的扩展”操作的图标。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: 「擴展」在台灣多稱「擴充功能」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 24. vscode-loc-zh-hans-v1/entry-64a03661b97583f0

Changed: `domain, risk`

Input:

```text
将文件夹添加到上一个活动窗口。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 25. vscode-loc-zh-hans-v1/entry-66638959e243f413

Changed: `domain, risk`

Input:

```text
键入要打开的编辑器名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 26. vscode-loc-zh-hans-v1/entry-695847b5a35b3aea

Changed: `domain, risk`

Input:

```text
没有可用的重构操作
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: 「重構」為常見開發術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 27. vscode-loc-zh-hans-v1/entry-6dbf9426a4d30c06

Changed: `eligible, domain, risk`

Input:

```text
已追加新消息 - 预期增长
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | no | null | null | high | context_dependent_fragment |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: 語意不明確，高度依賴上下文。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 28. vscode-loc-zh-hans-v1/entry-6e8b497db0d8de97

Changed: `risk`

Input:

```text
这些按钮与文本筛选器协同工作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 29. vscode-loc-zh-hans-v1/entry-6ec38c7aa4ddc709

Changed: `domain, risk`

Input:

```text
(未知命令)
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 30. vscode-loc-zh-hans-v1/entry-72ce544d66a729cb

Changed: `risk`

Input:

```text
测试开始时打开测试结果视图
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 31. vscode-loc-zh-hans-v1/entry-7e36d9bf95e8bed9

Changed: `domain`

Input:

```text
确定要移除动态身份验证提供程序“{0}”吗?
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: 涉及安全議題（移除身份驗證提供程序）與佔位符。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 32. vscode-loc-zh-hans-v1/entry-7ed8bbe9a5f3b75f

Changed: `risk`

Input:

```text
已选项在列表或树非活动时的背景颜色。活动的列表或树具有键盘焦点，非活动的没有。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 33. vscode-loc-zh-hans-v1/entry-7f0e900dae3691eb

Changed: `eligible, domain, risk`

Input:

```text
关于 Web 视图的重要信息:
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | heading_fragment |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 冒號結尾的標題失去後續列表或正文，無法獨立裁決。

Gemini reason: 「Web 視圖」為特定術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 34. vscode-loc-zh-hans-v1/entry-7f8e48ba6d106341

Changed: `risk`

Input:

```text
此任务依赖的其他任务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 35. vscode-loc-zh-hans-v1/entry-856cbd656423cb94

Changed: `risk`

Input:

```text
从历史记录中移除
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 36. vscode-loc-zh-hans-v1/entry-8fc02f08634e4b0d

Changed: `domain, risk`

Input:

```text
选择日志文件
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 37. vscode-loc-zh-hans-v1/entry-94381a24276104af

Changed: `risk`

Input:

```text
终端将被任务重用，按任意键关闭。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 38. vscode-loc-zh-hans-v1/entry-9b6362038d22e2cf

Changed: `risk`

Input:

```text
你正在筛选问题。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 39. vscode-loc-zh-hans-v1/entry-9c70830d7d27fdd0

Changed: `domain`

Input:

```text
向上滚动编辑器悬停。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: 「懸停」在台灣多稱「懸浮」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 40. vscode-loc-zh-hans-v1/entry-9ca9abf622010003

Changed: `domain, risk`

Input:

```text
显示文件(统一)
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 41. vscode-loc-zh-hans-v1/entry-9cbbc08caf93b140

Changed: `domain, risk`

Input:

```text
无法写入文件。请打开文件以更正错误或警告，然后重试。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 42. vscode-loc-zh-hans-v1/entry-9ea6ebf32e5ff215

Changed: `domain, risk`

Input:

```text
已应用代码操作
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 43. vscode-loc-zh-hans-v1/entry-a090a75ec1580ca3

Changed: `risk`

Input:

```text
已重新连接到正在运行的任务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 44. vscode-loc-zh-hans-v1/entry-a099104a591d86b5

Changed: `domain`

Input:

```text
{0} (快照)
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: 包含佔位符，「快照」為技術術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 45. vscode-loc-zh-hans-v1/entry-a10503591691a1f3

Changed: `domain, risk`

Input:

```text
启用自动任务 - 请注意，任务将不会在不受信任的工作区中运行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: 涉及工作區信任與安全議題。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 46. vscode-loc-zh-hans-v1/entry-a3dbd60b440641ab

Changed: `risk`

Input:

```text
始终以最大化方式打开面板。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 47. vscode-loc-zh-hans-v1/entry-a8e95d30efdb9a64

Changed: `risk`

Input:

```text
“打开预览”操作的图标。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 48. vscode-loc-zh-hans-v1/entry-b143b64fca5f5204

Changed: `risk`

Input:

```text
选择下载位置
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 49. vscode-loc-zh-hans-v1/entry-c418fc97de5ef87b

Changed: `risk`

Input:

```text
添加代码单元格
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 50. vscode-loc-zh-hans-v1/entry-c871a62cd669ef44

Changed: `domain`

Input:

```text
无法单独禁用 "{0}" 扩展。"{1}" 扩展依赖于此扩展。要禁用所有这些扩展吗?
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: 包含佔位符，且「擴展」在台灣多稱「擴充功能」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 51. vscode-loc-zh-hans-v1/entry-ca5513941592c416

Changed: `risk`

Input:

```text
活动自定义编辑器差异是否可在内联与并排布局之间切换
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: 「內聯」與「並排」為常見佈局術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 52. vscode-loc-zh-hans-v1/entry-ca69b4c84786a324

Changed: `risk`

Input:

```text
模型想要运行所有测试。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的 AI／聊天產品介面文字。

Gemini reason: AI 模型相關術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 53. vscode-loc-zh-hans-v1/entry-cb126e5b4fa8ec31

Changed: `domain`

Input:

```text
附加文件，{0}，行 {1} 到行 {2}
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: 包含佔位符。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 54. vscode-loc-zh-hans-v1/entry-d703bfb0a5c29bea

Changed: `risk`

Input:

```text
放弃更改并重新打开
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 55. vscode-loc-zh-hans-v1/entry-d87fdb7d2e15f8c2

Changed: `risk`

Input:

```text
内容从左侧滑入。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 56. vscode-loc-zh-hans-v1/entry-e433e1dfab11db9c

Changed: `domain, risk`

Input:

```text
切换正则表达式
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: 「正則表達式」為常見術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 57. vscode-loc-zh-hans-v1/entry-e5872f63c3f3ffdb

Changed: `risk`

Input:

```text
菜单显示在窗口顶部，并且仅在全屏模式下隐藏。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 58. vscode-loc-zh-hans-v1/entry-e8c009efa14ec353

Changed: `risk`

Input:

```text
导航路径
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 59. vscode-loc-zh-hans-v1/entry-ede28d50696fc56b

Changed: `risk`

Input:

```text
显示稳定版设置
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 60. vscode-loc-zh-hans-v1/entry-f5510e85cd7fc11b

Changed: `risk`

Input:

```text
与上一个版本比较
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 61. vscode-loc-zh-hans-v1/entry-f684886e6f1776ae

Changed: `risk`

Input:

```text
“转到下一个”标记的图标。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的產品介面文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 62. vscode-loc-zh-hans-v1/entry-f70da209d44d911d

Changed: `risk`

Input:

```text
从不扫描此任务的任务输出
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 63. vscode-loc-zh-hans-v1/entry-f85cf53973975aae

Changed: `risk`

Input:

```text
新的拆分终端将使用父终端开始时使用的工作目录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 64. vscode-loc-zh-hans-v1/entry-fa06d285423fec57

Changed: `domain, risk`

Input:

```text
控制在编辑器中是否允许通过拖放来移动选中内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 65. vscode-loc-zh-hans-v1/entry-fb67fda66dd60fa8

Changed: `domain`

Input:

```text
配置任务(&&C)…
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | medium | - |

Codex reason: 完整且可獨立裁決的開發工具或技術設定文字。

Gemini reason: 包含 UI 加速鍵標記 `&&C`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`
