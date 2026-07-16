<!-- zhtw:disable -->
# Holdout Codex/Gemini Diff Review - blind-v1 Batch4 100 Cases

Generated: `2026-07-09`

## Policy

- This report is advisory only.
- It is not ground truth and must not populate `blind-v1.expected.json` directly.
- Maintainer confirmation is required before private expected can be updated.

## Summary

- Total cases: 100
- Exact matches: 74
- Differences: 26
- Exact but policy review: 38
- No immediate question: 36
- Maintainer queue total: 64

Difference recommendations:

- `codex`: 21
- `gemini`: 4
- `third_value`: 1

## Differences

### blind-it-0063

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Reason: Prefer Taiwan engineering usage 「回傳」 for API return in this project style.

Input:

```text
这个端点会返回分页后的审计日志。
```

Codex expected:

```text
這個端點會回傳分頁後的稽核日誌。
```

Gemini expected:

```text
這個端點會傳回分頁後的稽核日誌。
```

Recommended expected:

```text
這個端點會回傳分頁後的稽核日誌。
```

### blind-it-0064

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `gemini`
- Reason: 「請求主體」 is a clear Taiwan technical rendering for request body.

Input:

```text
请在请求体里加入客户端版本号。
```

Codex expected:

```text
請在請求本文裡加入用戶端版本號。
```

Gemini expected:

```text
請在請求主體裡加入用戶端版本號。
```

Recommended expected:

```text
請在請求主體裡加入用戶端版本號。
```

### blind-it-0067

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Reason: Prefer consistent API wording 「回傳」.

Input:

```text
如果连接池已满，服务会返回重试提示。
```

Codex expected:

```text
如果連線池已滿，服務會回傳重試提示。
```

Gemini expected:

```text
如果連線池已滿，服務會傳回重試提示。
```

Recommended expected:

```text
如果連線池已滿，服務會回傳重試提示。
```

### blind-it-0069

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Reason: Input says hook/鉤子; Codex keeps the narrower technical term and avoids broadening to 掛鉤.

Input:

```text
这个钩子会在发布前执行安全扫描。
```

Codex expected:

```text
這個鉤子會在發布前執行安全掃描。
```

Gemini expected:

```text
這個掛鉤會在發布前執行安全性掃描。
```

Recommended expected:

```text
這個鉤子會在發布前執行安全掃描。
```

### blind-it-0070

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Reason: For Kubernetes-like config mapping, Codex wording is closer to the input than 「組態對應」.

Input:

```text
命名空间里的配置映射需要同步更新。
```

Codex expected:

```text
命名空間裡的設定映射需要同步更新。
```

Gemini expected:

```text
命名空間裡的組態對應需要同步更新。
```

Recommended expected:

```text
命名空間裡的設定映射需要同步更新。
```

### blind-it-0074

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Reason: Log filtering is better rendered as 「過濾」 than UI-like 「篩選」.

Input:

```text
日志收集器会过滤健康检查请求。
```

Codex expected:

```text
日誌收集器會過濾健康檢查請求。
```

Gemini expected:

```text
日誌收集器會篩選健康檢查請求。
```

Recommended expected:

```text
日誌收集器會過濾健康檢查請求。
```

### blind-it-0075

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Reason: SSR is commonly called 「伺服器端渲染」 in developer contexts.

Input:

```text
服务端渲染会读取用户偏好设置。
```

Codex expected:

```text
伺服器端渲染會讀取使用者偏好設定。
```

Gemini expected:

```text
伺服器端轉譯會讀取使用者偏好設定。
```

Recommended expected:

```text
伺服器端渲染會讀取使用者偏好設定。
```

### blind-it-0077

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Reason: Database migration is commonly rendered as 「遷移」 in this technical context.

Input:

```text
迁移任务会把旧字段复制到新字段。
```

Codex expected:

```text
遷移任務會把舊欄位複製到新欄位。
```

Gemini expected:

```text
移轉任務會把舊欄位複製到新欄位。
```

Recommended expected:

```text
遷移任務會把舊欄位複製到新欄位。
```

### blind-it-0080

- Domain: `it`
- Risk: `over_conversion_guard`
- Recommendation: `codex`
- Reason: Over-conversion guard should preserve the 台灣 graph from the input phrase.

Input:

```text
请保留 README 里的台湾示例路径。
```

Codex expected:

```text
請保留 README 裡的台灣範例路徑。
```

Gemini expected:

```text
請保留 README 裡的臺灣範例路徑。
```

Recommended expected:

```text
請保留 README 裡的台灣範例路徑。
```

### blind-it-0085

- Domain: `it`
- Risk: `baseline_guard`
- Recommendation: `codex`
- Reason: CLI command is better rendered as 「指令」 in Taiwan developer wording.

Input:

```text
执行完成后，命令会输出摘要。
```

Codex expected:

```text
執行完成後，指令會輸出摘要。
```

Gemini expected:

```text
執行完成後，命令會輸出摘要。
```

Recommended expected:

```text
執行完成後，指令會輸出摘要。
```

### blind-it-0086

- Domain: `it`
- Risk: `baseline_guard`
- Recommendation: `codex`
- Reason: Project style has favored 「設定檔」 over 「組態檔」 for config file.

Input:

```text
配置文件缺少必要字段时会停止启动。
```

Codex expected:

```text
設定檔缺少必要欄位時會停止啟動。
```

Gemini expected:

```text
組態檔缺少必要欄位時會停止啟動。
```

Recommended expected:

```text
設定檔缺少必要欄位時會停止啟動。
```

### blind-it-0087

- Domain: `it`
- Risk: `baseline_guard`
- Recommendation: `gemini`
- Reason: 「管線」 is the more common Taiwan developer rendering for pipeline.

Input:

```text
单元测试失败时，流水线会标记为失败。
```

Codex expected:

```text
單元測試失敗時，流水線會標記為失敗。
```

Gemini expected:

```text
單元測試失敗時，管線會標記為失敗。
```

Recommended expected:

```text
單元測試失敗時，管線會標記為失敗。
```

### blind-ui-0048

- Domain: `ui`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Reason: Product UI action wording should prefer 「點選」 unless the product style says otherwise.

Input:

```text
点击筛选按钮后，列表只显示未处理项目。
```

Codex expected:

```text
點選篩選按鈕後，清單只顯示未處理項目。
```

Gemini expected:

```text
點擊篩選按鈕後，清單只顯示未處理項目。
```

Recommended expected:

```text
點選篩選按鈕後，清單只顯示未處理項目。
```

### blind-ui-0053

- Domain: `ui`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Reason: UI term 「空狀態」 is precise and common in product localization.

Input:

```text
找不到结果时显示空状态提示。
```

Codex expected:

```text
找不到結果時顯示空狀態提示。
```

Gemini expected:

```text
找不到結果時顯示空白狀態提示。
```

Recommended expected:

```text
找不到結果時顯示空狀態提示。
```

### blind-ui-0055

- Domain: `ui`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Reason: UI navigation menu should prefer 「導覽選單」 over 「導覽功能表」.

Input:

```text
切换语言后，导航菜单会重新载入。
```

Codex expected:

```text
切換語言後，導覽選單會重新載入。
```

Gemini expected:

```text
切換語言後，導覽功能表會重新載入。
```

Recommended expected:

```text
切換語言後，導覽選單會重新載入。
```

### blind-ui-0061

- Domain: `ui`
- Risk: `over_conversion_guard`
- Recommendation: `codex`
- Reason: Gemini output contains awkward 「自訂義」; Codex is cleaner.

Input:

```text
用户自定义标签“台湾行程”不要自动改写。
```

Codex expected:

```text
使用者自訂標籤「台灣行程」不要自動改寫。
```

Gemini expected:

```text
使用者自訂義標籤「台灣行程」不要自動改寫。
```

Recommended expected:

```text
使用者自訂標籤「台灣行程」不要自動改寫。
```

### blind-llm-0033

- Domain: `llm`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Reason: LLM completion wording commonly uses 「補全」.

Input:

```text
请根据上下文补全这段说明。
```

Codex expected:

```text
請根據上下文補全這段說明。
```

Gemini expected:

```text
請根據上下文補齊這段說明。
```

Recommended expected:

```text
請根據上下文補全這段說明。
```

### blind-formal-0034

- Domain: `formal`
- Risk: `candidate_gap`
- Recommendation: `third_value`
- Reason: 「下一季」 is more natural Taiwan formal wording than 下季度/下個季度.

Input:

```text
本公司将于下季度调整服务条款。
```

Codex expected:

```text
本公司將於下季度調整服務條款。
```

Gemini expected:

```text
本公司將於下個季度調整服務條款。
```

Recommended expected:

```text
本公司將於下一季調整服務條款。
```

### blind-formal-0036

- Domain: `formal`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Reason: Meeting minutes should use 「會議紀錄」 in Taiwan formal writing.

Input:

```text
会议记录应列明各项决议。
```

Codex expected:

```text
會議紀錄應列明各項決議。
```

Gemini expected:

```text
會議記錄應列明各項決議。
```

Recommended expected:

```text
會議紀錄應列明各項決議。
```

### blind-formal-0038

- Domain: `formal`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Reason: Official policy wording can use 「公共運輸」 and should not narrow to 大眾運輸.

Input:

```text
本计划预计改善公共运输效率。
```

Codex expected:

```text
本計畫預計改善公共運輸效率。
```

Gemini expected:

```text
本計畫預計改善大眾運輸效率。
```

Recommended expected:

```text
本計畫預計改善公共運輸效率。
```

### blind-social-0036

- Domain: `social`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Reason: Chat wording in Taiwan naturally uses 「傳到群組」.

Input:

```text
你要不要先把行程发到群组？
```

Codex expected:

```text
你要不要先把行程傳到群組？
```

Gemini expected:

```text
你要不要先把行程發到群組？
```

Recommended expected:

```text
你要不要先把行程傳到群組？
```

### blind-social-0040

- Domain: `social`
- Risk: `candidate_gap`
- Recommendation: `gemini`
- Reason: Taiwan social/video wording usually says 「直播重播」 rather than 回放.

Input:

```text
朋友说直播回放已经可以观看。
```

Codex expected:

```text
朋友說直播回放已經可以觀看。
```

Gemini expected:

```text
朋友說直播重播已經可以觀看。
```

Recommended expected:

```text
朋友說直播重播已經可以觀看。
```

### blind-social-0041

- Domain: `social`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Reason: Daily messaging wording favors 「傳給你」.

Input:

```text
我把路线截图发给你了。
```

Codex expected:

```text
我把路線截圖傳給你了。
```

Gemini expected:

```text
我把路線截圖發給你了。
```

Recommended expected:

```text
我把路線截圖傳給你了。
```

### blind-high-risk-0022

- Domain: `high_risk`
- Risk: `candidate_gap`
- Recommendation: `gemini`
- Reason: Financial notification wording commonly uses 「發送交易通知」.

Input:

```text
银行应在扣款前发送交易通知。
```

Codex expected:

```text
銀行應在扣款前傳送交易通知。
```

Gemini expected:

```text
銀行應在扣款前發送交易通知。
```

Recommended expected:

```text
銀行應在扣款前發送交易通知。
```

### blind-high-risk-0024

- Domain: `high_risk`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Reason: Prefer Taiwan medical wording 「病患」 as primary; 患者 can remain a possible variant later.

Input:

```text
患者出院后仍需定期回诊追踪。
```

Codex expected:

```text
病患出院後仍需定期回診追蹤。
```

Gemini expected:

```text
患者出院後仍需定期回診追蹤。
```

Recommended expected:

```text
病患出院後仍需定期回診追蹤。
```

### blind-high-risk-0030

- Domain: `high_risk`
- Risk: `baseline_guard`
- Recommendation: `codex`
- Reason: Medical audit records should use 「稽核紀錄」 in Taiwan wording.

Input:

```text
电子病历存取应留下完整审计记录。
```

Codex expected:

```text
電子病歷存取應留下完整稽核紀錄。
```

Gemini expected:

```text
電子病歷存取應留下完整稽核記錄。
```

Recommended expected:

```text
電子病歷存取應留下完整稽核紀錄。
```


## Exact But Policy Review

- `blind-it-0072` (it, candidate_gap): Codex confidence medium
- `blind-it-0073` (it, candidate_gap): Codex confidence medium
- `blind-it-0078` (it, candidate_gap): Codex confidence medium
- `blind-it-0081` (it, over_conversion_guard): over-conversion guard
- `blind-it-0082` (it, over_conversion_guard): over-conversion guard
- `blind-it-0083` (it, over_conversion_guard): over-conversion guard
- `blind-it-0084` (it, over_conversion_guard): over-conversion guard
- `blind-ui-0049` (ui, candidate_gap): Codex confidence medium
- `blind-ui-0050` (ui, candidate_gap): Codex confidence medium
- `blind-ui-0060` (ui, over_conversion_guard): over-conversion guard
- `blind-ui-0062` (ui, over_conversion_guard): over-conversion guard
- `blind-ui-0063` (ui, over_conversion_guard): Codex confidence medium, over-conversion guard
- `blind-ui-0064` (ui, over_conversion_guard): over-conversion guard
- `blind-ui-0067` (ui, baseline_guard): Codex confidence medium
- `blind-llm-0035` (llm, candidate_gap): Codex confidence medium
- `blind-llm-0039` (llm, candidate_gap): Codex confidence medium
- `blind-llm-0042` (llm, over_conversion_guard): over-conversion guard
- `blind-llm-0043` (llm, over_conversion_guard): over-conversion guard
- `blind-llm-0044` (llm, over_conversion_guard): over-conversion guard
- `blind-llm-0045` (llm, over_conversion_guard): over-conversion guard
- `blind-formal-0041` (formal, candidate_gap): Codex confidence medium
- `blind-formal-0043` (formal, over_conversion_guard): over-conversion guard
- `blind-formal-0044` (formal, over_conversion_guard): over-conversion guard
- `blind-formal-0045` (formal, over_conversion_guard): over-conversion guard
- `blind-formal-0046` (formal, over_conversion_guard): over-conversion guard
- `blind-social-0034` (social, candidate_gap): Codex confidence medium
- `blind-social-0035` (social, candidate_gap): Codex confidence medium
- `blind-social-0042` (social, over_conversion_guard): over-conversion guard
- `blind-social-0043` (social, over_conversion_guard): over-conversion guard
- `blind-social-0044` (social, over_conversion_guard): over-conversion guard
- `blind-social-0045` (social, over_conversion_guard): over-conversion guard
- `blind-high-risk-0021` (high_risk, candidate_gap): high-risk domain
- `blind-high-risk-0023` (high_risk, candidate_gap): high-risk domain
- `blind-high-risk-0025` (high_risk, candidate_gap): high-risk domain
- `blind-high-risk-0026` (high_risk, over_conversion_guard): high-risk domain, over-conversion guard
- `blind-high-risk-0027` (high_risk, over_conversion_guard): high-risk domain, over-conversion guard
- `blind-high-risk-0028` (high_risk, over_conversion_guard): high-risk domain, over-conversion guard
- `blind-high-risk-0029` (high_risk, baseline_guard): high-risk domain