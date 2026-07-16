<!-- zhtw:disable -->
# Holdout Maintainer Confirmation Packet - blind-v1 Batch4 100 Cases

Generated: `2026-07-09`

This packet is for maintainer confirmation. It is not ground truth by itself and must not be promoted directly.

## Summary

- Total review cases: 64
- Difference cases: 26
- Policy-review cases: 38
- No immediate question: 36

## Cases

### blind-it-0063 (difference)

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-it-0064 (difference)

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `gemini`
- Maintainer action: `confirm_or_edit`
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

### blind-it-0067 (difference)

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-it-0069 (difference)

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-it-0070 (difference)

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-it-0074 (difference)

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-it-0075 (difference)

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-it-0077 (difference)

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-it-0080 (difference)

- Domain: `it`
- Risk: `over_conversion_guard`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-it-0085 (difference)

- Domain: `it`
- Risk: `baseline_guard`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-it-0086 (difference)

- Domain: `it`
- Risk: `baseline_guard`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-it-0087 (difference)

- Domain: `it`
- Risk: `baseline_guard`
- Recommendation: `gemini`
- Maintainer action: `confirm_or_edit`
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

### blind-ui-0048 (difference)

- Domain: `ui`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-ui-0053 (difference)

- Domain: `ui`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-ui-0055 (difference)

- Domain: `ui`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-ui-0061 (difference)

- Domain: `ui`
- Risk: `over_conversion_guard`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-llm-0033 (difference)

- Domain: `llm`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-formal-0034 (difference)

- Domain: `formal`
- Risk: `candidate_gap`
- Recommendation: `third_value`
- Maintainer action: `confirm_or_edit`
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

### blind-formal-0036 (difference)

- Domain: `formal`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-formal-0038 (difference)

- Domain: `formal`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-social-0036 (difference)

- Domain: `social`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-social-0040 (difference)

- Domain: `social`
- Risk: `candidate_gap`
- Recommendation: `gemini`
- Maintainer action: `confirm_or_edit`
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

### blind-social-0041 (difference)

- Domain: `social`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-high-risk-0022 (difference)

- Domain: `high_risk`
- Risk: `candidate_gap`
- Recommendation: `gemini`
- Maintainer action: `confirm_or_edit`
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

### blind-high-risk-0024 (difference)

- Domain: `high_risk`
- Risk: `candidate_gap`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-high-risk-0030 (difference)

- Domain: `high_risk`
- Risk: `baseline_guard`
- Recommendation: `codex`
- Maintainer action: `confirm_or_edit`
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

### blind-it-0072 (exact_but_policy_review)

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: Codex confidence medium

Input:

```text
请在变更记录中说明破坏性更新。
```

Codex expected:

```text
請在變更記錄中說明破壞性更新。
```

Gemini expected:

```text
請在變更記錄中說明破壞性更新。
```

Recommended expected:

```text
請在變更記錄中說明破壞性更新。
```

### blind-it-0073 (exact_but_policy_review)

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: Codex confidence medium

Input:

```text
上传接口会验证文件校验和。
```

Codex expected:

```text
上傳介面會驗證檔案校驗和。
```

Gemini expected:

```text
上傳介面會驗證檔案校驗和。
```

Recommended expected:

```text
上傳介面會驗證檔案校驗和。
```

### blind-it-0078 (exact_but_policy_review)

- Domain: `it`
- Risk: `candidate_gap`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: Codex confidence medium

Input:

```text
构建产物会上传到内部制品库。
```

Codex expected:

```text
建置產物會上傳到內部製品庫。
```

Gemini expected:

```text
建置產物會上傳到內部製品庫。
```

Recommended expected:

```text
建置產物會上傳到內部製品庫。
```

### blind-it-0081 (exact_but_policy_review)

- Domain: `it`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
变量名 userStatusText 不应被翻译。
```

Codex expected:

```text
變數名稱 userStatusText 不應被翻譯。
```

Gemini expected:

```text
變數名稱 userStatusText 不應被翻譯。
```

Recommended expected:

```text
變數名稱 userStatusText 不應被翻譯。
```

### blind-it-0082 (exact_but_policy_review)

- Domain: `it`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
项目代号 TaipeiBridge 必须维持原样。
```

Codex expected:

```text
專案代號 TaipeiBridge 必須維持原樣。
```

Gemini expected:

```text
專案代號 TaipeiBridge 必須維持原樣。
```

Recommended expected:

```text
專案代號 TaipeiBridge 必須維持原樣。
```

### blind-it-0083 (exact_but_policy_review)

- Domain: `it`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
测试资料包含台中门市的原始地址。
```

Codex expected:

```text
測試資料包含台中門市的原始地址。
```

Gemini expected:

```text
測試資料包含台中門市的原始地址。
```

Recommended expected:

```text
測試資料包含台中門市的原始地址。
```

### blind-it-0084 (exact_but_policy_review)

- Domain: `it`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
请不要改写已经本地化的按钮标签。
```

Codex expected:

```text
請不要改寫已經在地化的按鈕標籤。
```

Gemini expected:

```text
請不要改寫已經在地化的按鈕標籤。
```

Recommended expected:

```text
請不要改寫已經在地化的按鈕標籤。
```

### blind-ui-0049 (exact_but_policy_review)

- Domain: `ui`
- Risk: `candidate_gap`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: Codex confidence medium

Input:

```text
当前页面会在保存后自动刷新。
```

Codex expected:

```text
目前頁面會在儲存後自動重新整理。
```

Gemini expected:

```text
目前頁面會在儲存後自動重新整理。
```

Recommended expected:

```text
目前頁面會在儲存後自動重新整理。
```

### blind-ui-0050 (exact_but_policy_review)

- Domain: `ui`
- Risk: `candidate_gap`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: Codex confidence medium

Input:

```text
请在弹窗里显示上传进度。
```

Codex expected:

```text
請在彈出視窗裡顯示上傳進度。
```

Gemini expected:

```text
請在彈出視窗裡顯示上傳進度。
```

Recommended expected:

```text
請在彈出視窗裡顯示上傳進度。
```

### blind-ui-0060 (exact_but_policy_review)

- Domain: `ui`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
品牌页里的台北店名称必须保持原样。
```

Codex expected:

```text
品牌頁裡的台北店名稱必須保持原樣。
```

Gemini expected:

```text
品牌頁裡的台北店名稱必須保持原樣。
```

Recommended expected:

```text
品牌頁裡的台北店名稱必須保持原樣。
```

### blind-ui-0062 (exact_but_policy_review)

- Domain: `ui`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
请保留频道名称里的繁体字样。
```

Codex expected:

```text
請保留頻道名稱裡的繁體字樣。
```

Gemini expected:

```text
請保留頻道名稱裡的繁體字樣。
```

Recommended expected:

```text
請保留頻道名稱裡的繁體字樣。
```

### blind-ui-0063 (exact_but_policy_review)

- Domain: `ui`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: Codex confidence medium, over-conversion guard

Input:

```text
收藏夹里的 Taipei 2026 不需要翻译。
```

Codex expected:

```text
我的最愛裡的 Taipei 2026 不需要翻譯。
```

Gemini expected:

```text
我的最愛裡的 Taipei 2026 不需要翻譯。
```

Recommended expected:

```text
我的最愛裡的 Taipei 2026 不需要翻譯。
```

### blind-ui-0064 (exact_but_policy_review)

- Domain: `ui`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
已经审核的繁体说明不应再次转换。
```

Codex expected:

```text
已經審核的繁體說明不應再次轉換。
```

Gemini expected:

```text
已經審核的繁體說明不應再次轉換。
```

Recommended expected:

```text
已經審核的繁體說明不應再次轉換。
```

### blind-ui-0067 (exact_but_policy_review)

- Domain: `ui`
- Risk: `baseline_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: Codex confidence medium

Input:

```text
页面载入时先显示骨架画面。
```

Codex expected:

```text
頁面載入時先顯示骨架畫面。
```

Gemini expected:

```text
頁面載入時先顯示骨架畫面。
```

Recommended expected:

```text
頁面載入時先顯示骨架畫面。
```

### blind-llm-0035 (exact_but_policy_review)

- Domain: `llm`
- Risk: `candidate_gap`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: Codex confidence medium

Input:

```text
生成的摘要应保留原文的时间顺序。
```

Codex expected:

```text
產生的摘要應保留原文的時間順序。
```

Gemini expected:

```text
產生的摘要應保留原文的時間順序。
```

Recommended expected:

```text
產生的摘要應保留原文的時間順序。
```

### blind-llm-0039 (exact_but_policy_review)

- Domain: `llm`
- Risk: `candidate_gap`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: Codex confidence medium

Input:

```text
这个代理会调用工具读取文件列表。
```

Codex expected:

```text
這個代理會呼叫工具讀取檔案清單。
```

Gemini expected:

```text
這個代理會呼叫工具讀取檔案清單。
```

Recommended expected:

```text
這個代理會呼叫工具讀取檔案清單。
```

### blind-llm-0042 (exact_but_policy_review)

- Domain: `llm`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
请保留提示词里的变量名 productTitle。
```

Codex expected:

```text
請保留提示詞裡的變數名稱 productTitle。
```

Gemini expected:

```text
請保留提示詞裡的變數名稱 productTitle。
```

Recommended expected:

```text
請保留提示詞裡的變數名稱 productTitle。
```

### blind-llm-0043 (exact_but_policy_review)

- Domain: `llm`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
范例输出中的台湾邮递区号不要改。
```

Codex expected:

```text
範例輸出中的台灣郵遞區號不要改。
```

Gemini expected:

```text
範例輸出中的台灣郵遞區號不要改。
```

Recommended expected:

```text
範例輸出中的台灣郵遞區號不要改。
```

### blind-llm-0044 (exact_but_policy_review)

- Domain: `llm`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
请不要改写用户提供的台北地址。
```

Codex expected:

```text
請不要改寫使用者提供的台北地址。
```

Gemini expected:

```text
請不要改寫使用者提供的台北地址。
```

Recommended expected:

```text
請不要改寫使用者提供的台北地址。
```

### blind-llm-0045 (exact_but_policy_review)

- Domain: `llm`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
训练资料里的繁体句子应保持原样。
```

Codex expected:

```text
訓練資料裡的繁體句子應保持原樣。
```

Gemini expected:

```text
訓練資料裡的繁體句子應保持原樣。
```

Recommended expected:

```text
訓練資料裡的繁體句子應保持原樣。
```

### blind-formal-0041 (exact_but_policy_review)

- Domain: `formal`
- Risk: `candidate_gap`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: Codex confidence medium

Input:

```text
公告内容将同步发送给相关单位。
```

Codex expected:

```text
公告內容將同步發送給相關單位。
```

Gemini expected:

```text
公告內容將同步發送給相關單位。
```

Recommended expected:

```text
公告內容將同步發送給相關單位。
```

### blind-formal-0043 (exact_but_policy_review)

- Domain: `formal`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
文件中既有的台北市法规名称不得改写。
```

Codex expected:

```text
文件中既有的台北市法規名稱不得改寫。
```

Gemini expected:

```text
文件中既有的台北市法規名稱不得改寫。
```

Recommended expected:

```text
文件中既有的台北市法規名稱不得改寫。
```

### blind-formal-0044 (exact_but_policy_review)

- Domain: `formal`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
附件里的台湾大学专有名称应保持原样。
```

Codex expected:

```text
附件裡的台灣大學專有名稱應保持原樣。
```

Gemini expected:

```text
附件裡的台灣大學專有名稱應保持原樣。
```

Recommended expected:

```text
附件裡的台灣大學專有名稱應保持原樣。
```

### blind-formal-0045 (exact_but_policy_review)

- Domain: `formal`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
请保留表格中原始的台中地址。
```

Codex expected:

```text
請保留表格中原始的台中地址。
```

Gemini expected:

```text
請保留表格中原始的台中地址。
```

Recommended expected:

```text
請保留表格中原始的台中地址。
```

### blind-formal-0046 (exact_but_policy_review)

- Domain: `formal`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
合约编号 TW-2026-台南 不应被转换。
```

Codex expected:

```text
合約編號 TW-2026-台南 不應被轉換。
```

Gemini expected:

```text
合約編號 TW-2026-台南 不應被轉換。
```

Recommended expected:

```text
合約編號 TW-2026-台南 不應被轉換。
```

### blind-social-0034 (exact_but_policy_review)

- Domain: `social`
- Risk: `candidate_gap`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: Codex confidence medium

Input:

```text
我已经把活动照片传到共享相册了。
```

Codex expected:

```text
我已經把活動照片傳到共享相簿了。
```

Gemini expected:

```text
我已經把活動照片傳到共享相簿了。
```

Recommended expected:

```text
我已經把活動照片傳到共享相簿了。
```

### blind-social-0035 (exact_but_policy_review)

- Domain: `social`
- Risk: `candidate_gap`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: Codex confidence medium

Input:

```text
这家店的外卖速度比上次快。
```

Codex expected:

```text
這家店的外送速度比上次快。
```

Gemini expected:

```text
這家店的外送速度比上次快。
```

Recommended expected:

```text
這家店的外送速度比上次快。
```

### blind-social-0042 (exact_but_policy_review)

- Domain: `social`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
昵称里的台湾队长不要自动改。
```

Codex expected:

```text
暱稱裡的台灣隊長不要自動改。
```

Gemini expected:

```text
暱稱裡的台灣隊長不要自動改。
```

Recommended expected:

```text
暱稱裡的台灣隊長不要自動改。
```

### blind-social-0043 (exact_but_policy_review)

- Domain: `social`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
照片说明里的台北小旅行保持原样。
```

Codex expected:

```text
照片說明裡的台北小旅行保持原樣。
```

Gemini expected:

```text
照片說明裡的台北小旅行保持原樣。
```

Recommended expected:

```text
照片說明裡的台北小旅行保持原樣。
```

### blind-social-0044 (exact_but_policy_review)

- Domain: `social`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
社群标签 #台中美食 不要转换。
```

Codex expected:

```text
社群標籤 #台中美食 不要轉換。
```

Gemini expected:

```text
社群標籤 #台中美食 不要轉換。
```

Recommended expected:

```text
社群標籤 #台中美食 不要轉換。
```

### blind-social-0045 (exact_but_policy_review)

- Domain: `social`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: over-conversion guard

Input:

```text
请保留朋友写的繁体祝福语。
```

Codex expected:

```text
請保留朋友寫的繁體祝福語。
```

Gemini expected:

```text
請保留朋友寫的繁體祝福語。
```

Recommended expected:

```text
請保留朋友寫的繁體祝福語。
```

### blind-high-risk-0021 (exact_but_policy_review)

- Domain: `high_risk`
- Risk: `candidate_gap`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: high-risk domain

Input:

```text
医师会根据检查结果调整用药剂量。
```

Codex expected:

```text
醫師會根據檢查結果調整用藥劑量。
```

Gemini expected:

```text
醫師會根據檢查結果調整用藥劑量。
```

Recommended expected:

```text
醫師會根據檢查結果調整用藥劑量。
```

### blind-high-risk-0023 (exact_but_policy_review)

- Domain: `high_risk`
- Risk: `candidate_gap`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: high-risk domain

Input:

```text
保险契约变更须经要保人同意。
```

Codex expected:

```text
保險契約變更須經要保人同意。
```

Gemini expected:

```text
保險契約變更須經要保人同意。
```

Recommended expected:

```text
保險契約變更須經要保人同意。
```

### blind-high-risk-0025 (exact_but_policy_review)

- Domain: `high_risk`
- Risk: `candidate_gap`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: high-risk domain

Input:

```text
贷款申请资料不得提供给无关第三人。
```

Codex expected:

```text
貸款申請資料不得提供給無關第三人。
```

Gemini expected:

```text
貸款申請資料不得提供給無關第三人。
```

Recommended expected:

```text
貸款申請資料不得提供給無關第三人。
```

### blind-high-risk-0026 (exact_but_policy_review)

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: high-risk domain, over-conversion guard

Input:

```text
病历中的台北院区名称不得改写。
```

Codex expected:

```text
病歷中的台北院區名稱不得改寫。
```

Gemini expected:

```text
病歷中的台北院區名稱不得改寫。
```

Recommended expected:

```text
病歷中的台北院區名稱不得改寫。
```

### blind-high-risk-0027 (exact_but_policy_review)

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: high-risk domain, over-conversion guard

Input:

```text
契约附件里的台湾分公司名称应保持原样。
```

Codex expected:

```text
契約附件裡的台灣分公司名稱應保持原樣。
```

Gemini expected:

```text
契約附件裡的台灣分公司名稱應保持原樣。
```

Recommended expected:

```text
契約附件裡的台灣分公司名稱應保持原樣。
```

### blind-high-risk-0028 (exact_but_policy_review)

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: high-risk domain, over-conversion guard

Input:

```text
汇款备注中的 Taichung Branch 不需翻译。
```

Codex expected:

```text
匯款備註中的 Taichung Branch 不需翻譯。
```

Gemini expected:

```text
匯款備註中的 Taichung Branch 不需翻譯。
```

Recommended expected:

```text
匯款備註中的 Taichung Branch 不需翻譯。
```

### blind-high-risk-0029 (exact_but_policy_review)

- Domain: `high_risk`
- Risk: `baseline_guard`
- Recommendation: `codex_gemini_match`
- Maintainer action: `quick_confirm_or_edit`
- Reason: high-risk domain

Input:

```text
未成年人的法定代理人应共同签署。
```

Codex expected:

```text
未成年人的法定代理人應共同簽署。
```

Gemini expected:

```text
未成年人的法定代理人應共同簽署。
```

Recommended expected:

```text
未成年人的法定代理人應共同簽署。
```


## No Immediate Question Case IDs

- `blind-it-0065`
- `blind-it-0066`
- `blind-it-0068`
- `blind-it-0071`
- `blind-it-0076`
- `blind-it-0079`
- `blind-ui-0051`
- `blind-ui-0052`
- `blind-ui-0054`
- `blind-ui-0056`
- `blind-ui-0057`
- `blind-ui-0058`
- `blind-ui-0059`
- `blind-ui-0065`
- `blind-ui-0066`
- `blind-llm-0034`
- `blind-llm-0036`
- `blind-llm-0037`
- `blind-llm-0038`
- `blind-llm-0040`
- `blind-llm-0041`
- `blind-llm-0046`
- `blind-llm-0047`
- `blind-formal-0035`
- `blind-formal-0037`
- `blind-formal-0039`
- `blind-formal-0040`
- `blind-formal-0042`
- `blind-formal-0047`
- `blind-formal-0048`
- `blind-social-0037`
- `blind-social-0038`
- `blind-social-0039`
- `blind-social-0046`
- `blind-social-0047`
- `blind-social-0048`