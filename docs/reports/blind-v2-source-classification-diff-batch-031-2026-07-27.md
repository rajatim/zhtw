<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 031 (2026-07-27)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `79d12a09e64acd2911d1e35e5afdbc8116398006307e6a78f48eeedff2c7d0d3`
Cases: 100
Exact Codex/Gemini classifications: 43
Maintainer review queue: 57

Field differences:

- Eligibility: 0
- Script: 1
- Domain: 25
- Risk: 39

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

The maintainer resolved all 57 advisory disagreements and batch-confirmed the 43 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. zhtw-project-llm-domain-balance-v1/formal-002

Changed: `risk`

Input:

```text
主管机关要求业者在期限内补正资料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可独立判读的正式书面情境；用于检验机构用语、专业词汇与识别码保留。

Gemini reason: 正式公文用語，要求業者補件。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 02. zhtw-project-llm-domain-balance-v1/formal-003

Changed: `domain, risk`

Input:

```text
审计人员逐项核对付款日期与支出凭证。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可独立判读的正式书面情境；用于检验机构用语、专业词汇与识别码保留。

Gemini reason: 財會審計用語。「审计」是中國大陸常用詞，台灣多用「查核」，存在地區詞彙差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 03. zhtw-project-llm-domain-balance-v1/formal-005

Changed: `risk`

Input:

```text
地方政府已说明预算执行进度与差异原因。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可独立判读的正式书面情境；用于检验机构用语、专业词汇与识别码保留。

Gemini reason: 政府報告用語，說明預算執行情況。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 04. zhtw-project-llm-domain-balance-v1/formal-007

Changed: `domain`

Input:

```text
本办法自公告之日起正式施行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的正式书面情境；用于检验机构用语、专业词汇与识别码保留。

Gemini reason: 法律或規章的生效條文。用語非常正式，繁簡體意思一致。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 05. zhtw-project-llm-domain-balance-v1/formal-009

Changed: `risk`

Input:

```text
新闻稿引用的统计数字以原始资料为准。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可独立判读的正式书面情境；用于检验机构用语、专业词汇与识别码保留。

Gemini reason: 新聞發布準則。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 06. zhtw-project-llm-domain-balance-v1/formal-010

Changed: `script, domain`

Input:

```text
法院文件沿用案件编号 115年度诉字第42号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可独立判读的正式书面情境；用于检验机构用语、专业词汇与识别码保留。

Gemini reason: 法律文件用語，包含一個必須保持原樣的案件編號「115年度诉字第42号」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 07. zhtw-project-llm-domain-balance-v1/formal-011

Changed: `domain, risk`

Input:

```text
契约附件应与采购公告的版本一致。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可独立判读的正式书面情境；用于检验机构用语、专业词汇与识别码保留。

Gemini reason: 合約規範用語。「契约」在台灣較少用，通用詞是「合約」，存在地區詞彙差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 08. zhtw-project-llm-domain-balance-v1/formal-012

Changed: `domain, risk`

Input:

```text
银行将在交易完成后寄送电子对账单。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的正式书面情境；用于检验机构用语、专业词汇与识别码保留。

Gemini reason: 銀行服務說明。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 09. zhtw-project-llm-domain-balance-v1/formal-013

Changed: `domain, risk`

Input:

```text
保险公司应向客户说明保单的重要条款。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的正式书面情境；用于检验机构用语、专业词汇与识别码保留。

Gemini reason: 保險合約說明。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 10. zhtw-project-llm-domain-balance-v1/formal-014

Changed: `domain, risk`

Input:

```text
医疗机构必须妥善保存患者的检查记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的正式书面情境；用于检验机构用语、专业词汇与识别码保留。

Gemini reason: 醫療法規要求。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 11. zhtw-project-llm-domain-balance-v1/formal-017

Changed: `domain`

Input:

```text
财政年度 FY2027 的预算金额另表列示。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可独立判读的正式书面情境；用于检验机构用语、专业词汇与识别码保留。

Gemini reason: 財務報告用語。包含財政年度縮寫「FY2027」，不得轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 12. zhtw-project-llm-domain-balance-v1/formal-020

Changed: `domain`

Input:

```text
个人资料仅能用于原先告知的特定目的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的正式书面情境；用于检验机构用语、专业词汇与识别码保留。

Gemini reason: 隱私權政策條款。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 13. zhtw-project-llm-domain-balance-v1/llm-003

Changed: `risk`

Input:

```text
检索流程会从多个文档中挑选相关片段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 資訊檢索或 RAG 流程說明。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 14. zhtw-project-llm-domain-balance-v1/llm-004

Changed: `domain`

Input:

```text
请将结果输出为有效的 JSON 对象。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: API 或程式指令。包含專有名詞「JSON」，不得轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 15. zhtw-project-llm-domain-balance-v1/llm-007

Changed: `risk`

Input:

```text
向量嵌入用于计算查询与段落的相似度。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: LLM/ML 技術說明，關於向量嵌入。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 16. zhtw-project-llm-domain-balance-v1/llm-008

Changed: `risk`

Input:

```text
重排序模型会调整搜索结果的优先级。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 資訊檢索/LLM 技術說明。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 17. zhtw-project-llm-domain-balance-v1/llm-009

Changed: `risk`

Input:

```text
回答不得虚构来源中没有出现的数字。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: LLM 行為準則，關於避免幻覺。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 18. zhtw-project-llm-domain-balance-v1/llm-010

Changed: `risk`

Input:

```text
每项结论都必须附上对应的引用编号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: LLM 輸出要求，關於引用。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 19. zhtw-project-llm-domain-balance-v1/llm-011

Changed: `domain`

Input:

```text
模板中的 {{user_query}} 是待替换的占位符。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 模板語法說明。包含一個程式佔位符「{{user_query}}」，不得轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 20. zhtw-project-llm-domain-balance-v1/llm-012

Changed: `domain`

Input:

```text
请求标头中的 API_TOKEN 不得写入日志。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 系統安全規定。包含一個變數名稱「API_TOKEN」，不得轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 21. zhtw-project-llm-domain-balance-v1/llm-013

Changed: `domain`

Input:

```text
请保留 Markdown 表格内的代码片段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 文件處理指令。包含專有名稱「Markdown」，不得轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 22. zhtw-project-llm-domain-balance-v1/llm-014

Changed: `domain`

Input:

```text
YAML 文件中的缩进层级不能改变。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 文件格式規定。包含專有名稱「YAML」，不得轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 23. zhtw-project-llm-domain-balance-v1/llm-015

Changed: `domain, risk`

Input:

```text
生成的 SQL 查询只能读取审计视图。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 程式安全規定。包含專有名詞「SQL」且「审计」是中國大陸常用詞，台灣多用「查核」，存在地區詞彙差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 24. zhtw-project-llm-domain-balance-v1/llm-016

Changed: `domain`

Input:

```text
函数名称 fetch_user_profile 必须保持原样。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 程式碼修改指令。明確指出函數名稱「fetch_user_profile」需保留原樣。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 25. zhtw-project-llm-domain-balance-v1/llm-017

Changed: `domain`

Input:

```text
错误代码 E_MODEL_TIMEOUT 表示模型响应超时。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 錯誤碼說明。包含一個錯誤碼「E_MODEL_TIMEOUT」，不得轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 26. zhtw-project-llm-domain-balance-v1/llm-022

Changed: `risk`

Input:

```text
训练数据集不得包含真实客户的个人资料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: LLM 資料處理倫理規範。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 27. zhtw-project-llm-domain-balance-v1/llm-023

Changed: `risk`

Input:

```text
验证集只用于选择模型参数，不参与训练。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 機器學習術語「验证集」(驗證集)在兩岸用法基本一致，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 28. zhtw-project-llm-domain-balance-v1/llm-024

Changed: `risk`

Input:

```text
这个批次包含一百条待审核的测试样本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 資料處理或品管用語。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 29. zhtw-project-llm-domain-balance-v1/llm-025

Changed: `risk`

Input:

```text
系统会从最近的检查点恢复训练任务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 機器學習訓練流程說明。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 30. zhtw-project-llm-domain-balance-v1/llm-027

Changed: `domain`

Input:

```text
缓存过期后，服务会重新计算嵌入结果。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 系統架構技術說明。「缓存」是中國大陸常用詞，台灣多用「快取」，存在地區詞彙差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 31. zhtw-project-llm-domain-balance-v1/llm-028

Changed: `domain, risk`

Input:

```text
任务队列按照请求的优先级依次处理。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 系統設計說明。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 32. zhtw-project-llm-domain-balance-v1/llm-029

Changed: `risk`

Input:

```text
流式输出会逐段显示模型生成的内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: LLM 功能說明。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 33. zhtw-project-llm-domain-balance-v1/llm-030

Changed: `domain`

Input:

```text
请求失败时最多重试三次，并记录状态码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: API 客戶端或系統韌性設計。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 34. zhtw-project-llm-domain-balance-v1/llm-031

Changed: `risk`

Input:

```text
低置信度回答必须进入人工审核队列。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: AI 系統工作流程說明。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 35. zhtw-project-llm-domain-balance-v1/llm-032

Changed: `risk`

Input:

```text
分类器的置信度阈值由管理员设定。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 機器學習模型設定說明。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 36. zhtw-project-llm-domain-balance-v1/llm-034

Changed: `risk`

Input:

```text
系统会遮盖姓名、电话和身份证号等敏感资料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 隱私資料處理說明。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 37. zhtw-project-llm-domain-balance-v1/llm-036

Changed: `risk`

Input:

```text
安全过滤器会拦截包含恶意指令的请求。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: AI 安全機制說明。「过滤器」是中國大陸常用詞，台灣多用「篩選器」，存在地區詞彙差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 38. zhtw-project-llm-domain-balance-v1/llm-039

Changed: `risk`

Input:

```text
长期记忆只保存用户明确同意的偏好。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: AI 個人化功能說明。「用户」是中國大陸常用詞，台灣多用「使用者」，存在地區詞彙差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 39. zhtw-project-llm-domain-balance-v1/llm-044

Changed: `domain`

Input:

```text
时间戳 2026-07-27T16:45:00+08:00 不得改写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 資料格式規定。明確指出時間戳「2026-07-27T16:45:00+08:00」不得改寫。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 40. zhtw-project-llm-domain-balance-v1/llm-045

Changed: `domain`

Input:

```text
来源网址 https://example.com/report?id=42 必须保持有效。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 資料引用規定。包含一個 URL，不得轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 41. zhtw-project-llm-domain-balance-v1/llm-046

Changed: `domain`

Input:

```text
附件名称 quarterly_review_v2.pdf 不应转换。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 文件命名規定。明確指出檔案名稱「quarterly_review_v2.pdf」不應轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 42. zhtw-project-llm-domain-balance-v1/llm-047

Changed: `domain`

Input:

```text
代码块里的变量名和字符串常量必须保留。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 程式碼處理指令。這是一條元規則，說明程式碼中的變數和字串必須保留。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 43. zhtw-project-llm-domain-balance-v1/llm-048

Changed: `domain`

Input:

```text
正则表达式 ^user_[0-9]+$ 用于检查账号格式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可独立判读的 LLM 产品或评测情境；用于检验技术用语、一般字形与受保护 token。

Gemini reason: 程式碼註解或技術說明。包含一個正規表示式「^user_[0-9]+$」，不得轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 44. zhtw-project-llm-domain-balance-v1/social-001

Changed: `risk`

Input:

```text
请提醒我下班后去超市买牛奶。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且可独立判读的日常情境；用于检验台湾生活用语、一般字形与专名保留。

Gemini reason: 日常生活指令。「超市」雖在台灣也用，但「视频」對「影片」的轉換更為必要，此處標為 candidate_gap 以表示地區用語差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 45. zhtw-project-llm-domain-balance-v1/social-004

Changed: `risk`

Input:

```text
把这张照片发送到朋友群组。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可独立判读的日常情境；用于检验台湾生活用语、一般字形与专名保留。

Gemini reason: 日常社交指令。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 46. zhtw-project-llm-domain-balance-v1/social-006

Changed: `risk`

Input:

```text
我的手机电量只剩百分之十。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可独立判读的日常情境；用于检验台湾生活用语、一般字形与专名保留。

Gemini reason: 日常生活對話。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 47. zhtw-project-llm-domain-balance-v1/social-007

Changed: `risk`

Input:

```text
导航建议从下一个路口右转。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可独立判读的日常情境；用于检验台湾生活用语、一般字形与专名保留。

Gemini reason: 導航指令用語。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 48. zhtw-project-llm-domain-balance-v1/social-008

Changed: `risk`

Input:

```text
外卖订单预计四十分钟后送达。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可独立判读的日常情境；用于检验台湾生活用语、一般字形与专名保留。

Gemini reason: 外送情境用語。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 49. zhtw-project-llm-domain-balance-v1/social-010

Changed: `risk`

Input:

```text
我想取消今晚八点的预约。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可独立判读的日常情境；用于检验台湾生活用语、一般字形与专名保留。

Gemini reason: 日常預約情境。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 50. zhtw-project-llm-domain-balance-v1/social-011

Changed: `risk`

Input:

```text
王小明刚才发来一条语音消息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且可独立判读的日常情境；用于检验台湾生活用语、一般字形与专名保留。

Gemini reason: 即時通訊用語。「消息」是中國大陸常用詞，台灣多用「訊息」，存在地區詞彙差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 51. zhtw-project-llm-domain-balance-v1/social-012

Changed: `risk`

Input:

```text
台北今天下午可能会下大雨。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可独立判读的日常情境；用于检验台湾生活用语、一般字形与专名保留。

Gemini reason: 天氣預報用語。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 52. zhtw-project-llm-domain-balance-v1/social-013

Changed: `risk`

Input:

```text
这份食谱需要两百克面粉。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可独立判读的日常情境；用于检验台湾生活用语、一般字形与专名保留。

Gemini reason: 食譜用語。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 53. zhtw-project-llm-domain-balance-v1/social-015

Changed: `risk`

Input:

```text
我已经把会议地址传到群组了。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可独立判读的日常情境；用于检验台湾生活用语、一般字形与专名保留。

Gemini reason: 日常溝通。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 54. zhtw-project-llm-domain-balance-v1/ui-004

Changed: `risk`

Input:

```text
启用通知后即可接收最新消息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整且可独立判读的产品介面字串；用于检验台湾 UI 用语、一般字形与受保护 token。

Gemini reason: UI 設定文字。「启用」是中國大陸常用詞，台灣多用「啟用」或「開啟」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 55. zhtw-project-llm-domain-balance-v1/ui-007

Changed: `risk`

Input:

```text
此操作会永久删除所选文件夹。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可独立判读的产品介面字串；用于检验台湾 UI 用语、一般字形与受保护 token。

Gemini reason: UI 警告訊息。用詞在繁簡體中通用，屬於基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 56. zhtw-project-llm-domain-balance-v1/ui-008

Changed: `risk`

Input:

```text
系统正在同步您的联系人和日历。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整且可独立判读的产品介面字串；用于检验台湾 UI 用语、一般字形与受保护 token。

Gemini reason: UI 狀態文字。「同步您的联系人」中的「联系人」是中國大陸常用詞，台灣多用「聯絡人」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 57. zhtw-project-llm-domain-balance-v1/ui-011

Changed: `risk`

Input:

```text
验证码将在十分钟后失效。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整且可独立判读的产品介面字串；用于检验台湾 UI 用语、一般字形与受保护 token。

Gemini reason: UI 提示。「验证码」是中國大陸常用詞，台灣也用，但有時也用「認證碼」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`
