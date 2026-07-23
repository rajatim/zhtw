<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 006 (2026-07-23)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `24ee1f560805f539ac9d259b23f4a26dba642f875ee40dd2bc46c515c78d68f1`
Cases: 100
Exact Codex/Gemini classifications: 58
Maintainer review queue: 42

Field differences:

- Eligibility: 0
- Script: 8
- Domain: 0
- Risk: 35

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

The maintainer resolved all 42 advisory disagreements and batch-confirmed the 58 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. zhtw-project-it-api-cli-v1/it-002

Changed: `risk`

Input:

```text
请求体必须包含用户编号和当前时区。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 含中國技術用語或臺灣工程語境可能採不同說法的詞彙，列為候選缺口。

Gemini reason: 主要為字元層級轉換，無特殊術語風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 02. zhtw-project-it-api-cli-v1/it-005

Changed: `risk`

Input:

```text
删除资源后，再次请求应返回明确的状态码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 含中國技術用語或臺灣工程語境可能採不同說法的詞彙，列為候選缺口。

Gemini reason: 主要為字元層級轉換，「狀態碼」一詞通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 03. zhtw-project-it-api-cli-v1/it-007

Changed: `script`

Input:

```text
Webhook 签名校验失败时，不要处理消息内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 包含英文專有名詞「Webhook」，需避免轉換。同時涉及術語「簽名」、「校驗」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 04. zhtw-project-it-api-cli-v1/it-009

Changed: `script`

Input:

```text
GraphQL 查询深度超过限制时，应拒绝执行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 包含英文專有名詞「GraphQL」，需避免轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 05. zhtw-project-it-api-cli-v1/it-010

Changed: `script, risk`

Input:

```text
API 版本升级后，旧字段至少保留一个迁移周期。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 含中國技術用語或臺灣工程語境可能採不同說法的詞彙，列為候選缺口。

Gemini reason: 包含英文縮寫「API」，需避免轉換。同時涉及術語「版本」、「升級」、「字段」、「遷移」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 06. zhtw-project-it-api-cli-v1/it-012

Changed: `script`

Input:

```text
使用 --dry-run 参数预览即将发生的修改。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 包含命令列參數「--dry-run」，需避免轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 07. zhtw-project-it-api-cli-v1/it-013

Changed: `risk`

Input:

```text
命令执行失败后，将退出码传给调用脚本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 涉及術語「退出碼」、「腳本」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 08. zhtw-project-it-api-cli-v1/it-014

Changed: `risk`

Input:

```text
管道中的前一个命令失败时，整个任务也应停止。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「管道」，在台灣可能用「管線」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 09. zhtw-project-it-api-cli-v1/it-017

Changed: `risk`

Input:

```text
日志输出到标准错误，正常结果输出到标准输出。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 涉及術語「日誌」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 10. zhtw-project-it-api-cli-v1/it-022

Changed: `risk`

Input:

```text
合并冲突解决后，重新运行完整测试。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「合併衝突」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 11. zhtw-project-it-api-cli-v1/it-024

Changed: `risk`

Input:

```text
拉取请求需要关联问题编号和测试证据。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「拉取請求」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 12. zhtw-project-it-api-cli-v1/it-025

Changed: `risk`

Input:

```text
发布标签必须指向通过构建的提交。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 涉及術語「發布標籤」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 13. zhtw-project-it-api-cli-v1/it-035

Changed: `risk`

Input:

```text
只读副本落后时，不要用于读取刚写入的数据。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「只讀副本」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 14. zhtw-project-it-api-cli-v1/it-037

Changed: `risk`

Input:

```text
备份完成不代表恢复流程已经验证。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「備份」、「恢復流程」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 15. zhtw-project-it-api-cli-v1/it-038

Changed: `script`

Input:

```text
时间戳统一保存为 UTC，显示时再转换时区。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 包含時區標準「UTC」，需避免轉換。同時涉及「時間戳」、「時區」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 16. zhtw-project-it-api-cli-v1/it-043

Changed: `script`

Input:

```text
容器启动后应以非 root 用户运行服务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 包含系統用戶名「root」，需避免轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 17. zhtw-project-it-api-cli-v1/it-044

Changed: `risk`

Input:

```text
健康检查失败不一定代表进程已经退出。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「健康檢查」、「進程」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 18. zhtw-project-it-api-cli-v1/it-047

Changed: `risk`

Input:

```text
滚动更新期间必须维持最少可用实例数。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「滾動更新」、「實例」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 19. zhtw-project-it-api-cli-v1/it-050

Changed: `risk`

Input:

```text
服务网格升级前，先验证代理版本兼容性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 涉及術語「服務網格」、「代理」、「兼容性」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 20. zhtw-project-it-api-cli-v1/it-053

Changed: `risk`

Input:

```text
缓存键必须包含操作系统和运行时版本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 涉及術語「緩存鍵」、「操作系統」、「運行時」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 21. zhtw-project-it-api-cli-v1/it-057

Changed: `risk`

Input:

```text
构建日志中的访问令牌必须自动遮盖。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 涉及術語「構建日誌」、「訪問令牌」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 22. zhtw-project-it-api-cli-v1/it-058

Changed: `risk`

Input:

```text
定时任务重复触发时，只允许一个实例继续执行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「定時任務」、「實例」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 23. zhtw-project-it-api-cli-v1/it-065

Changed: `risk`

Input:

```text
可选依赖缺失时，只停用相关功能。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「可選依賴」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 24. zhtw-project-it-api-cli-v1/it-066

Changed: `risk`

Input:

```text
依赖解析结果在不同平台上可能不完全相同。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「依賴解析」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 25. zhtw-project-it-api-cli-v1/it-068

Changed: `risk`

Input:

```text
移除软件包前，检查是否仍被其他模块引用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「软件包」、「模塊」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 26. zhtw-project-it-api-cli-v1/it-070

Changed: `risk`

Input:

```text
软件物料清单应记录所有间接依赖。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 涉及術語「軟件物料清單」(SBOM)、「間接依賴」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 27. zhtw-project-it-api-cli-v1/it-071

Changed: `risk`

Input:

```text
认证成功后，仍需检查用户是否有操作权限。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 含中國技術用語或臺灣工程語境可能採不同說法的詞彙，列為候選缺口。

Gemini reason: 主要為字元層級轉換，無特殊術語風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 28. zhtw-project-it-api-cli-v1/it-076

Changed: `risk`

Input:

```text
审计日志需要记录操作者和目标资源。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「審計日誌」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 29. zhtw-project-it-api-cli-v1/it-078

Changed: `script`

Input:

```text
内部服务之间也必须验证 TLS 证书。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 包含協定名稱「TLS」，需避免轉換。同時涉及「證書」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 30. zhtw-project-it-api-cli-v1/it-080

Changed: `risk`

Input:

```text
管理员下载资料前，需要再次确认身份。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 含中國技術用語或臺灣工程語境可能採不同說法的詞彙，列為候選缺口。

Gemini reason: 主要為字元層級轉換，無特殊術語風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 31. zhtw-project-it-api-cli-v1/it-081

Changed: `risk`

Input:

```text
指标标签不要使用用户编号等高基数数据。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 涉及術語「指標標籤」、「高基數」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 32. zhtw-project-it-api-cli-v1/it-082

Changed: `risk`

Input:

```text
分布式跟踪必须跨服务传递追踪编号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 涉及術語「分佈式跟踪」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 33. zhtw-project-it-api-cli-v1/it-085

Changed: `risk`

Input:

```text
仪表板上的延迟应显示分位数而不是平均值。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 涉及術語「儀表板」、「延遲」、「分位數」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 34. zhtw-project-it-api-cli-v1/it-086

Changed: `risk`

Input:

```text
采样率变化必须记录在监控配置历史中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「採樣率」、「監控」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 35. zhtw-project-it-api-cli-v1/it-087

Changed: `risk`

Input:

```text
健康检查请求不应污染业务访问日志。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「健康檢查」、「訪問日誌」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 36. zhtw-project-it-api-cli-v1/it-088

Changed: `risk`

Input:

```text
错误预算耗尽后，暂停非必要的功能发布。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「錯誤預算」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 37. zhtw-project-it-api-cli-v1/it-089

Changed: `risk`

Input:

```text
系统时间漂移会影响跨节点事件排序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「系統時間漂移」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 38. zhtw-project-it-api-cli-v1/it-092

Changed: `risk`

Input:

```text
事件格式新增字段时，旧消费者应继续正常工作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「事件格式」、「字段」、「消費者」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 39. zhtw-project-it-api-cli-v1/it-096

Changed: `risk`

Input:

```text
缓存失效后，避免大量请求同时查询数据库。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「緩存」、「數據庫」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 40. zhtw-project-it-api-cli-v1/it-097

Changed: `script`

Input:

```text
域名切换前，先降低 DNS 记录的生存时间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 包含協定名稱「DNS」，需避免轉換。同時涉及「域名」、「記錄」、「生存時間」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 41. zhtw-project-it-api-cli-v1/it-099

Changed: `risk`

Input:

```text
配置中心不可用时，服务使用最后一次有效配置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 主要驗證一般簡體字形與完整技術句的保守轉換，不預設特定區域詞替換。

Gemini reason: 涉及術語「配置中心」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 42. zhtw-project-it-api-cli-v1/it-100

Changed: `risk`

Input:

```text
远程端点恢复后，断路器应逐步允许测试请求。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含 API、協定、CLI 參數或技術識別字，需防止字面或專名遭過度轉換。

Gemini reason: 涉及術語「遠程端點」、「斷路器」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`
