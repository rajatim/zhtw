<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 018 (2026-07-26)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `583998140501ba09f594fb2ecd48fa95604fbdce7670e773cbad3fd6497248d2`
Cases: 100
Exact Codex/Gemini classifications: 61
Maintainer review queue: 39

Field differences:

- Eligibility: 0
- Script: 0
- Domain: 0
- Risk: 39

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 39 advisory disagreements and batch-confirmed the 61 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. zhtw-project-it-llm-ui-guard-v1/it-006

Changed: `risk`

Input:

```text
请在日志中记录 X-Request-ID，但不要写入访问令牌。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 IT 技術陳述，核心價值是保護標頭 `X-Request-ID` 與 `access token` 概念不被錯誤翻譯。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 02. zhtw-project-it-llm-ui-guard-v1/it-008

Changed: `risk`

Input:

```text
登录流程采用 OAuth 2.0 Authorization Code 与 PKCE。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 IT 技術陳述，核心價值是保護專有名詞 `OAuth 2.0`, `Authorization Code`, `PKCE` 不變。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 03. zhtw-project-it-llm-ui-guard-v1/it-010

Changed: `risk`

Input:

```text
生产环境只接受 TLS 1.3 加密连接。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 IT 技術陳述，核心價值是保護 `TLS 1.3` 不變。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 04. zhtw-project-it-llm-ui-guard-v1/it-013

Changed: `risk`

Input:

```text
配置文件位于 /etc/acme/service.yaml。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 IT 技術陳述，核心價值是保護檔案路徑 `/etc/acme/service.yaml` 不變。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 05. zhtw-project-it-llm-ui-guard-v1/it-014

Changed: `risk`

Input:

```text
将环境变量 DATABASE_URL 注入 worker 进程。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 IT 技術陳述，核心價值是保護環境變數 `DATABASE_URL` 與 `worker` 不變。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 06. zhtw-project-it-llm-ui-guard-v1/it-015

Changed: `risk`

Input:

```text
SQL 查询引用 user_sessions.last_seen_at 字段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 IT 技術陳述，核心價值是保護 SQL 欄位 `user_sessions.last_seen_at` 不變。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 07. zhtw-project-it-llm-ui-guard-v1/it-026

Changed: `risk`

Input:

```text
运行 npm ci 时必须使用 package-lock.json 的锁定版本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 IT 指令，核心價值是保護 `npm ci` 與 `package-lock.json`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 08. zhtw-project-it-llm-ui-guard-v1/it-028

Changed: `risk`

Input:

```text
Python 程序以 uv run pytest -q 执行快速测试。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 IT 指令，核心價值是保護 `uv run pytest -q`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 09. zhtw-project-it-llm-ui-guard-v1/it-029

Changed: `risk`

Input:

```text
Java 服务的入口类是 com.acme.billing.Main。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 IT 技術陳述，核心價值是保護 Java class name `com.acme.billing.Main`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 10. zhtw-project-it-llm-ui-guard-v1/it-030

Changed: `risk`

Input:

```text
C# 项目将 Nullable 设为 enable。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 IT 技術陳述，核心價值是保護 C# 屬性 `Nullable` 與值 `enable`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 11. zhtw-project-it-llm-ui-guard-v1/it-038

Changed: `risk`

Input:

```text
消息消费者从 orders.created.v2 主题读取事件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 IT 技術陳述，核心價值是保護 message topic `orders.created.v2`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 12. zhtw-project-it-llm-ui-guard-v1/it-048

Changed: `risk`

Input:

```text
数据库迁移编号 202607260915_add_index 不可重复。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 IT 技術陳述，核心價值是保護資料庫遷移編號 `202607260915_add_index`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 13. zhtw-project-it-llm-ui-guard-v1/it-049

Changed: `risk`

Input:

```text
备份文件命名为 customers_2026-07-26.sql.gz。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 IT 技術陳述，核心價值是保護備份檔名格式 `customers_2026-07-26.sql.gz`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 14. zhtw-project-it-llm-ui-guard-v1/it-050

Changed: `risk`

Input:

```text
终端显示 exit code 137，表示进程被系统终止。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 IT 技術陳述，核心價值是保護 `exit code 137`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 15. zhtw-project-it-llm-ui-guard-v1/llm-004

Changed: `risk`

Input:

```text
消息依序使用 system、user 与 assistant 角色。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 LLM 技術陳述，核心價值是保護角色 `system`, `user`, `assistant`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 16. zhtw-project-it-llm-ui-guard-v1/llm-005

Changed: `risk`

Input:

```text
工具调用名称为 get_weather，参数包含 location。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 LLM 技術陳述，核心價值是保護工具調用名稱 `get_weather` 與參數 `location`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 17. zhtw-project-it-llm-ui-guard-v1/llm-006

Changed: `risk`

Input:

```text
函数参数必须符合 response_format 指定的 JSON Schema。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 LLM 技術陳述，核心價值是保護 `response_format` 與 `JSON Schema`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 18. zhtw-project-it-llm-ui-guard-v1/llm-009

Changed: `risk`

Input:

```text
检索系统以 cosine similarity 排序候选段落。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 LLM 技術陳述，核心價值是保護 `cosine similarity`，同時有術語正規化需求 (检索->檢索)。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 19. zhtw-project-it-llm-ui-guard-v1/llm-011

Changed: `risk`

Input:

```text
过滤器应识别提示注入，但不能删除正常引用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 完整輸入；主要風險是識別碼、語法、placeholder 或既有技術名稱遭過度轉換。

Gemini reason: 簡體 LLM 技術陳述，涉及術語正規化 (提示注入->提示詞注入)。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 20. zhtw-project-it-llm-ui-guard-v1/llm-012

Changed: `risk`

Input:

```text
安全分类标签 safety_label 必须原样写入审计日志。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 LLM 技術陳述，核心價值是保護 `safety_label`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 21. zhtw-project-it-llm-ui-guard-v1/llm-014

Changed: `risk`

Input:

````text
模型回答中的 ```json 代码围栏必须成对出现。
````

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 LLM 技術陳述，核心價值是保護 Markdown 語法 ```json。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 22. zhtw-project-it-llm-ui-guard-v1/llm-018

Changed: `risk`

Input:

```text
批处理请求以 custom_id 关联每一笔结果。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 LLM 技術陳述，核心價值是保護 `custom_id`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 23. zhtw-project-it-llm-ui-guard-v1/llm-021

Changed: `risk`

Input:

```text
响应的 usage 字段列出 input_tokens 与 output_tokens。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 LLM 技術陳述，核心價值是保護 `usage`, `input_tokens`, `output_tokens`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 24. zhtw-project-it-llm-ui-guard-v1/llm-022

Changed: `risk`

Input:

```text
缓存键包含 model、prompt_hash 与 schema_version。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 LLM 技術陳述，核心價值是保護 `model`, `prompt_hash`, `schema_version`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 25. zhtw-project-it-llm-ui-guard-v1/llm-024

Changed: `risk`

Input:

```text
人工审查员看不到 A/B 版本的模型名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 LLM 技術陳述，核心價值是保護 `A/B`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 26. zhtw-project-it-llm-ui-guard-v1/llm-027

Changed: `risk`

Input:

```text
多轮对话以 conversation_id 串接上下文。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | high | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 LLM 技術陳述，核心價值是保護 `conversation_id`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 27. zhtw-project-it-llm-ui-guard-v1/ui-002

Changed: `risk`

Input:

```text
欢迎消息中的 %1$s 会替换为用户名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 UI 字串，核心價值是保護 i18n placeholder `%1$s`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 28. zhtw-project-it-llm-ui-guard-v1/ui-004

Changed: `risk`

Input:

```text
按 Ctrl+Shift+P 打开命令面板。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 UI 字串，核心價值是保護快捷鍵 `Ctrl+Shift+P`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 29. zhtw-project-it-llm-ui-guard-v1/ui-005

Changed: `risk`

Input:

```text
应用名称 Acme Drive 不随界面语言改变。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 UI 字串，核心價值是保護應用名稱 `Acme Drive`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 30. zhtw-project-it-llm-ui-guard-v1/ui-006

Changed: `risk`

Input:

```text
隐私政策链接为 https://example.com/privacy?lang=zh-CN。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 UI 字串，核心價值是保護 URL `https://example.com/privacy?lang=zh-CN`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 31. zhtw-project-it-llm-ui-guard-v1/ui-008

Changed: `risk`

Input:

```text
载入期间显示“正在同步…”，完成后自动关闭。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整輸入；主要風險是識別碼、語法、placeholder 或既有技術名稱遭過度轉換。

Gemini reason: 簡體 UI 字串，單純的狀態文字，只需字型轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 32. zhtw-project-it-llm-ui-guard-v1/ui-010

Changed: `risk`

Input:

```text
日期字段接受 YYYY-MM-DD 格式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 UI 技術陳述，核心價值是保護日期格式 `YYYY-MM-DD`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 33. zhtw-project-it-llm-ui-guard-v1/ui-012

Changed: `risk`

Input:

```text
切换到 RTL 布局时，返回图标也会反向。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 UI 技術陳述，核心價值是保護 `RTL`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 34. zhtw-project-it-llm-ui-guard-v1/ui-014

Changed: `risk`

Input:

```text
设置页面分为 General、Privacy 与 Advanced 三个分页。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 UI 字串，核心價值是保護分頁名稱 `General`, `Privacy`, `Advanced`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 35. zhtw-project-it-llm-ui-guard-v1/ui-015

Changed: `risk`

Input:

```text
打开“自动更新”开关后立即检查新版本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整輸入；主要風險是識別碼、語法、placeholder 或既有技術名稱遭過度轉換。

Gemini reason: 簡體 UI 字串，單純的描述性文字，只需字型轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 36. zhtw-project-it-llm-ui-guard-v1/ui-017

Changed: `risk`

Input:

```text
文件选择器只显示 .csv 与 .tsv 文件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 UI 字串，核心價值是保護副檔名 `.csv` 與 `.tsv`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 37. zhtw-project-it-llm-ui-guard-v1/ui-018

Changed: `risk`

Input:

```text
搜索框的占位文本为“输入关键字”。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 UI 佔位文字，只需字型轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 38. zhtw-project-it-llm-ui-guard-v1/ui-019

Changed: `risk`

Input:

```text
空白状态显示“尚无活动记录”。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整輸入；主要風險是識別碼、語法、placeholder 或既有技術名稱遭過度轉換。

Gemini reason: 簡體 UI 空白狀態文字，只需字型轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 39. zhtw-project-it-llm-ui-guard-v1/ui-020

Changed: `risk`

Input:

```text
进度条旁显示 75%，不要插入额外空格。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整輸入；含臺灣技術用語正規化候選，並須保留其中的技術 token 或格式。

Gemini reason: 簡體 UI 字串，核心價值是保護百分比格式 `75%`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`
