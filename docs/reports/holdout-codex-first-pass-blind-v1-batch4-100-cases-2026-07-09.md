<!-- zhtw:disable -->
# Holdout Codex First-Pass Advisory - blind-v1 Batch4 100 Cases

Generated date: `2026-07-09`
Dataset: `blind-v1`
Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Expansion audit: `docs/reports/holdout-input-pool-expansion-blind-v1-batch4-100-cases-2026-07-09.json`
Raw JSON: `docs/reports/holdout-codex-first-pass-blind-v1-batch4-100-cases-2026-07-09.json`
Stage: `first_pass_advisory`
Reviewer: `codex`

## Policy

- This report is advisory only.
- It is not ground truth and must not populate `blind-v1.expected.json` directly.
- Expected values still require maintainer confirmation after Gemini advisory review.
- Promotion is not allowed from this report.

## Summary

- Cases: 100
- Review-needed cases before maintainer decision: 53

Confidence:

- `high`: 75
- `medium`: 25

Domain distribution:

- `formal`: 15
- `high_risk`: 10
- `it`: 25
- `llm`: 15
- `social`: 15
- `ui`: 20

## Review Needed Queue

- `blind-it-0063` (it, candidate_gap, medium)
- `blind-it-0064` (it, candidate_gap, medium)
- `blind-it-0069` (it, candidate_gap, medium)
- `blind-it-0070` (it, candidate_gap, medium)
- `blind-it-0072` (it, candidate_gap, medium)
- `blind-it-0073` (it, candidate_gap, medium)
- `blind-it-0074` (it, candidate_gap, medium)
- `blind-it-0078` (it, candidate_gap, medium)
- `blind-it-0080` (it, over_conversion_guard, high)
- `blind-it-0081` (it, over_conversion_guard, high)
- `blind-it-0082` (it, over_conversion_guard, high)
- `blind-it-0083` (it, over_conversion_guard, high)
- `blind-it-0084` (it, over_conversion_guard, high)
- `blind-it-0087` (it, baseline_guard, medium)
- `blind-ui-0048` (ui, candidate_gap, medium)
- `blind-ui-0049` (ui, candidate_gap, medium)
- `blind-ui-0050` (ui, candidate_gap, medium)
- `blind-ui-0060` (ui, over_conversion_guard, high)
- `blind-ui-0061` (ui, over_conversion_guard, high)
- `blind-ui-0062` (ui, over_conversion_guard, high)
- `blind-ui-0063` (ui, over_conversion_guard, medium)
- `blind-ui-0064` (ui, over_conversion_guard, high)
- `blind-ui-0067` (ui, baseline_guard, medium)
- `blind-llm-0035` (llm, candidate_gap, medium)
- `blind-llm-0039` (llm, candidate_gap, medium)
- `blind-llm-0042` (llm, over_conversion_guard, high)
- `blind-llm-0043` (llm, over_conversion_guard, high)
- `blind-llm-0044` (llm, over_conversion_guard, high)
- `blind-llm-0045` (llm, over_conversion_guard, high)
- `blind-formal-0034` (formal, candidate_gap, medium)
- `blind-formal-0036` (formal, candidate_gap, medium)
- `blind-formal-0041` (formal, candidate_gap, medium)
- `blind-formal-0043` (formal, over_conversion_guard, high)
- `blind-formal-0044` (formal, over_conversion_guard, high)
- `blind-formal-0045` (formal, over_conversion_guard, high)
- `blind-formal-0046` (formal, over_conversion_guard, high)
- `blind-social-0034` (social, candidate_gap, medium)
- `blind-social-0035` (social, candidate_gap, medium)
- `blind-social-0040` (social, candidate_gap, medium)
- `blind-social-0042` (social, over_conversion_guard, high)
- `blind-social-0043` (social, over_conversion_guard, high)
- `blind-social-0044` (social, over_conversion_guard, high)
- `blind-social-0045` (social, over_conversion_guard, high)
- `blind-high-risk-0021` (high_risk, candidate_gap, high)
- `blind-high-risk-0022` (high_risk, candidate_gap, medium)
- `blind-high-risk-0023` (high_risk, candidate_gap, high)
- `blind-high-risk-0024` (high_risk, candidate_gap, medium)
- `blind-high-risk-0025` (high_risk, candidate_gap, high)
- `blind-high-risk-0026` (high_risk, over_conversion_guard, high)
- `blind-high-risk-0027` (high_risk, over_conversion_guard, high)
- `blind-high-risk-0028` (high_risk, over_conversion_guard, high)
- `blind-high-risk-0029` (high_risk, baseline_guard, high)
- `blind-high-risk-0030` (high_risk, baseline_guard, medium)

## Cases

### blind-it-0063

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
这个端点会返回分页后的审计日志。
```

Codex expected:

```text
這個端點會回傳分頁後的稽核日誌。
```

Acceptable variants:

```text
這個端點會傳回分頁後的稽核記錄。
```

Rationale:

```text
API 語境採「端點」「回傳」；audit log 在台灣可作「稽核日誌」或「稽核記錄」。
```

### blind-it-0064

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
请在请求体里加入客户端版本号。
```

Codex expected:

```text
請在請求本文裡加入用戶端版本號。
```

Acceptable variants:

```text
請在請求主體裡加入用戶端版本號。
```

Rationale:

```text
HTTP request body 在台灣文件常見「請求本文」，也可見「請求主體」。
```

### blind-it-0065

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
缓存命中率会显示在监控面板上。
```

Codex expected:

```text
快取命中率會顯示在監控面板上。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
cache hit rate 採「快取命中率」。
```

### blind-it-0066

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
部署脚本会检查环境变量是否完整。
```

Codex expected:

```text
部署指令碼會檢查環境變數是否完整。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
deployment/script/environment variables 採台灣工程文件常用語。
```

### blind-it-0067

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
如果连接池已满，服务会返回重试提示。
```

Codex expected:

```text
如果連線池已滿，服務會回傳重試提示。
```

Acceptable variants:

```text
如果連線池已滿，服務會傳回重試提示。
```

Rationale:

```text
connection pool 採「連線池」；服務端結果採「回傳」。
```

### blind-it-0068

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
请把错误堆栈附加到工单描述里。
```

Codex expected:

```text
請把錯誤堆疊附加到工單描述裡。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
stack trace 依語境作「錯誤堆疊」。
```

### blind-it-0069

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
这个钩子会在发布前执行安全扫描。
```

Codex expected:

```text
這個鉤子會在發布前執行安全掃描。
```

Acceptable variants:

```text
這個 hook 會在發布前執行安全掃描。
```

Rationale:

```text
hook 可譯「鉤子」或保留英文，需依專案用語。
```

### blind-it-0070

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
命名空间里的配置映射需要同步更新。
```

Codex expected:

```text
命名空間裡的設定映射需要同步更新。
```

Acceptable variants:

```text
命名空間裡的 ConfigMap 需要同步更新。
```

Rationale:

```text
Kubernetes ConfigMap 台灣文件可譯「設定映射」或保留英文。
```

### blind-it-0071

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
消息队列会保留失败任务的重试次数。
```

Codex expected:

```text
訊息佇列會保留失敗任務的重試次數。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
message queue 採「訊息佇列」。
```

### blind-it-0072

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term, regional_term`

Input:

```text
请在变更记录中说明破坏性更新。
```

Codex expected:

```text
請在變更記錄中說明破壞性更新。
```

Acceptable variants:

```text
請在變更紀錄中說明破壞性更新。
```

Rationale:

```text
「記錄/紀錄」在文件語境需依風格確認。
```

### blind-it-0073

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
上传接口会验证文件校验和。
```

Codex expected:

```text
上傳介面會驗證檔案校驗和。
```

Acceptable variants:

```text
上傳 API 會驗證檔案校驗和。
```

Rationale:

```text
接口可作「介面」或 API；checksum 採「校驗和」。
```

### blind-it-0074

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
日志收集器会过滤健康检查请求。
```

Codex expected:

```text
日誌收集器會過濾健康檢查請求。
```

Acceptable variants:

```text
記錄收集器會過濾健康檢查請求。
```

Rationale:

```text
logging collector 可作「日誌收集器」或「記錄收集器」。
```

### blind-it-0075

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term, ui_term`

Input:

```text
服务端渲染会读取用户偏好设置。
```

Codex expected:

```text
伺服器端渲染會讀取使用者偏好設定。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
server-side rendering 採「伺服器端渲染」。
```

### blind-it-0076

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
请先撤销旧的访问密钥再生成新的。
```

Codex expected:

```text
請先撤銷舊的存取金鑰再產生新的。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
access key 採「存取金鑰」。
```

### blind-it-0077

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
迁移任务会把旧字段复制到新字段。
```

Codex expected:

```text
遷移任務會把舊欄位複製到新欄位。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
database field 採「欄位」。
```

### blind-it-0078

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
构建产物会上传到内部制品库。
```

Codex expected:

```text
建置產物會上傳到內部製品庫。
```

Acceptable variants:

```text
建置成品會上傳到內部製品庫。
```

Rationale:

```text
artifact repository 可作「製品庫」；「產物/成品」需看團隊用語。
```

### blind-it-0079

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
这个参数控制批量写入的缓冲大小。
```

Codex expected:

```text
這個參數控制批次寫入的緩衝大小。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
batch write/buffer 採「批次寫入」「緩衝」。
```

### blind-it-0080

- Domain: `it`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, regional_term`

Input:

```text
请保留 README 里的台湾示例路径。
```

Codex expected:

```text
請保留 README 裡的台灣範例路徑。
```

Acceptable variants:

```text
請保留 README 裡的臺灣範例路徑。
```

Rationale:

```text
over-conversion guard：台灣/臺灣圖形需保留政策確認。
```

### blind-it-0081

- Domain: `it`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, it_term`

Input:

```text
变量名 userStatusText 不应被翻译。
```

Codex expected:

```text
變數名稱 userStatusText 不應被翻譯。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
變數名稱必須保留原樣。
```

### blind-it-0082

- Domain: `it`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, it_term`

Input:

```text
项目代号 TaipeiBridge 必须维持原样。
```

Codex expected:

```text
專案代號 TaipeiBridge 必須維持原樣。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
專案代號含 TaipeiBridge，應保留原文。
```

### blind-it-0083

- Domain: `it`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, regional_term`

Input:

```text
测试资料包含台中门市的原始地址。
```

Codex expected:

```text
測試資料包含台中門市的原始地址。
```

Acceptable variants:

```text
測試資料包含臺中門市的原始地址。
```

Rationale:

```text
over-conversion guard：地名圖形需保留政策確認。
```

### blind-it-0084

- Domain: `it`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, ui_term`

Input:

```text
请不要改写已经本地化的按钮标签。
```

Codex expected:

```text
請不要改寫已經在地化的按鈕標籤。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
已在地化文字應避免二次轉換。
```

### blind-it-0085

- Domain: `it`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
执行完成后，命令会输出摘要。
```

Codex expected:

```text
執行完成後，指令會輸出摘要。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
CLI command 採「指令」。
```

### blind-it-0086

- Domain: `it`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
配置文件缺少必要字段时会停止启动。
```

Codex expected:

```text
設定檔缺少必要欄位時會停止啟動。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
config file/field 採「設定檔」「欄位」。
```

### blind-it-0087

- Domain: `it`
- Risk: `baseline_guard`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
单元测试失败时，流水线会标记为失败。
```

Codex expected:

```text
單元測試失敗時，流水線會標記為失敗。
```

Acceptable variants:

```text
單元測試失敗時，管線會標記為失敗。
```

Rationale:

```text
pipeline 可作「流水線」或「管線」，需依團隊用語。
```

### blind-ui-0048

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `ui_term, regional_term`

Input:

```text
点击筛选按钮后，列表只显示未处理项目。
```

Codex expected:

```text
點選篩選按鈕後，清單只顯示未處理項目。
```

Acceptable variants:

```text
點擊篩選按鈕後，清單只顯示未處理項目。
```

Rationale:

```text
UI 動作「點選/點擊」需依產品風格。
```

### blind-ui-0049

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `ui_term, regional_term`

Input:

```text
当前页面会在保存后自动刷新。
```

Codex expected:

```text
目前頁面會在儲存後自動重新整理。
```

Acceptable variants:

```text
當前頁面會在儲存後自動重新整理。
```

Rationale:

```text
UI 狀態常用「目前」，但「當前」也是可見變體。
```

### blind-ui-0050

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `ui_term`

Input:

```text
请在弹窗里显示上传进度。
```

Codex expected:

```text
請在彈出視窗裡顯示上傳進度。
```

Acceptable variants:

```text
請在彈窗裡顯示上傳進度。
```

Rationale:

```text
「弹窗」可作「彈出視窗」或產品用語「彈窗」。
```

### blind-ui-0051

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
用户可以拖拽卡片调整顺序。
```

Codex expected:

```text
使用者可以拖曳卡片調整順序。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
drag 採「拖曳」。
```

### blind-ui-0052

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
表格列宽会根据内容自动调整。
```

Codex expected:

```text
表格欄寬會根據內容自動調整。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
table column width 採「表格欄寬」。
```

### blind-ui-0053

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
找不到结果时显示空状态提示。
```

Codex expected:

```text
找不到結果時顯示空狀態提示。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
empty state 採「空狀態」。
```

### blind-ui-0054

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
请把错误信息放在输入框下方。
```

Codex expected:

```text
請把錯誤訊息放在輸入框下方。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
UI error message 採「錯誤訊息」。
```

### blind-ui-0055

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term, regional_term`

Input:

```text
切换语言后，导航菜单会重新载入。
```

Codex expected:

```text
切換語言後，導覽選單會重新載入。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
navigation menu 採「導覽選單」。
```

### blind-ui-0056

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
这个开关控制是否接收系统通知。
```

Codex expected:

```text
這個開關控制是否接收系統通知。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
toggle 在設定頁可作「開關」。
```

### blind-ui-0057

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
编辑模式下会锁定删除按钮。
```

Codex expected:

```text
編輯模式下會鎖定刪除按鈕。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
edit mode/delete button 直譯自然。
```

### blind-ui-0058

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
请在确认页列出所有已选项目。
```

Codex expected:

```text
請在確認頁列出所有已選項目。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
confirmation page 採「確認頁」。
```

### blind-ui-0059

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
面包屑会显示上一层分类名称。
```

Codex expected:

```text
麵包屑會顯示上一層分類名稱。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
breadcrumb UI 採「麵包屑」。
```

### blind-ui-0060

- Domain: `ui`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, regional_term, ui_term`

Input:

```text
品牌页里的台北店名称必须保持原样。
```

Codex expected:

```text
品牌頁裡的台北店名稱必須保持原樣。
```

Acceptable variants:

```text
品牌頁裡的臺北店名稱必須保持原樣。
```

Rationale:

```text
over-conversion guard：台北/臺北圖形需保留政策確認。
```

### blind-ui-0061

- Domain: `ui`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, regional_term, ui_term`

Input:

```text
用户自定义标签“台湾行程”不要自动改写。
```

Codex expected:

```text
使用者自訂標籤「台灣行程」不要自動改寫。
```

Acceptable variants:

```text
使用者自訂標籤「臺灣行程」不要自動改寫。
```

Rationale:

```text
使用者自訂標籤應保留。
```

### blind-ui-0062

- Domain: `ui`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, ui_term`

Input:

```text
请保留频道名称里的繁体字样。
```

Codex expected:

```text
請保留頻道名稱裡的繁體字樣。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
頻道名稱與既有繁體字樣應保留。
```

### blind-ui-0063

- Domain: `ui`
- Risk: `over_conversion_guard`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `over_conversion, ui_term`

Input:

```text
收藏夹里的 Taipei 2026 不需要翻译。
```

Codex expected:

```text
我的最愛裡的 Taipei 2026 不需要翻譯。
```

Acceptable variants:

```text
收藏夾裡的 Taipei 2026 不需要翻譯。
```

Rationale:

```text
favorite 在台灣 UI 常用「我的最愛」，但產品也可能使用「收藏夾」。
```

### blind-ui-0064

- Domain: `ui`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion`

Input:

```text
已经审核的繁体说明不应再次转换。
```

Codex expected:

```text
已經審核的繁體說明不應再次轉換。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
已審核繁體說明應避免二次轉換。
```

### blind-ui-0065

- Domain: `ui`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
提交成功后会显示绿色提示。
```

Codex expected:

```text
提交成功後會顯示綠色提示。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
submit/success message 直譯自然。
```

### blind-ui-0066

- Domain: `ui`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
密码输入错误三次后会暂时锁定。
```

Codex expected:

```text
密碼輸入錯誤三次後會暫時鎖定。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
lockout 採「暫時鎖定」。
```

### blind-ui-0067

- Domain: `ui`
- Risk: `baseline_guard`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `ui_term`

Input:

```text
页面载入时先显示骨架画面。
```

Codex expected:

```text
頁面載入時先顯示骨架畫面。
```

Acceptable variants:

```text
頁面載入時先顯示 skeleton 畫面。
```

Rationale:

```text
skeleton UI 可譯「骨架畫面」或保留英文。
```

### blind-llm-0033

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term, regional_term`

Input:

```text
请根据上下文补全这段说明。
```

Codex expected:

```text
請根據上下文補全這段說明。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
context completion 採「上下文」「補全」。
```

### blind-llm-0034

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
模型需要解释每个参数的用途。
```

Codex expected:

```text
模型需要解釋每個參數的用途。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
parameter 採「參數」。
```

### blind-llm-0035

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `regional_term`

Input:

```text
生成的摘要应保留原文的时间顺序。
```

Codex expected:

```text
產生的摘要應保留原文的時間順序。
```

Acceptable variants:

```text
生成的摘要應保留原文的時間順序。
```

Rationale:

```text
LLM 語境「生成/產生」需依政策確認。
```

### blind-llm-0036

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
请把长回复改写成三点建议。
```

Codex expected:

```text
請把長回覆改寫成三點建議。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
reply 採「回覆」。
```

### blind-llm-0037

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
系统提示词要求输出有效的 YAML。
```

Codex expected:

```text
系統提示詞要求輸出有效的 YAML。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
system prompt 採「系統提示詞」。
```

### blind-llm-0038

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
如果证据不足，请明确说明限制。
```

Codex expected:

```text
如果證據不足，請明確說明限制。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
保留語意不擴寫。
```

### blind-llm-0039

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
这个代理会调用工具读取文件列表。
```

Codex expected:

```text
這個代理會呼叫工具讀取檔案清單。
```

Acceptable variants:

```text
這個 agent 會呼叫工具讀取檔案清單。
```

Rationale:

```text
agent 可譯「代理」或保留英文，需依產品語境。
```

### blind-llm-0040

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
请把客服对话整理成后续任务。
```

Codex expected:

```text
請把客服對話整理成後續任務。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
support chat/task 轉為自然台灣用語。
```

### blind-llm-0041

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
回答里不要加入用户没有提供的日期。
```

Codex expected:

```text
回答裡不要加入使用者沒有提供的日期。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
hallucination guard 類句子保持直譯。
```

### blind-llm-0042

- Domain: `llm`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, it_term`

Input:

```text
请保留提示词里的变量名 productTitle。
```

Codex expected:

```text
請保留提示詞裡的變數名稱 productTitle。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
變數名稱必須保留。
```

### blind-llm-0043

- Domain: `llm`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, regional_term`

Input:

```text
范例输出中的台湾邮递区号不要改。
```

Codex expected:

```text
範例輸出中的台灣郵遞區號不要改。
```

Acceptable variants:

```text
範例輸出中的臺灣郵遞區號不要改。
```

Rationale:

```text
台灣/臺灣圖形需保留政策確認。
```

### blind-llm-0044

- Domain: `llm`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, regional_term`

Input:

```text
请不要改写用户提供的台北地址。
```

Codex expected:

```text
請不要改寫使用者提供的台北地址。
```

Acceptable variants:

```text
請不要改寫使用者提供的臺北地址。
```

Rationale:

```text
使用者提供地址應保留原圖形。
```

### blind-llm-0045

- Domain: `llm`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion`

Input:

```text
训练资料里的繁体句子应保持原样。
```

Codex expected:

```text
訓練資料裡的繁體句子應保持原樣。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
既有繁體句子應保留。
```

### blind-llm-0046

- Domain: `llm`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
请用一句话说明这个功能的限制。
```

Codex expected:

```text
請用一句話說明這個功能的限制。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
直譯自然。
```

### blind-llm-0047

- Domain: `llm`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
模型回答前应先检查输入是否完整。
```

Codex expected:

```text
模型回答前應先檢查輸入是否完整。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
直譯自然。
```

### blind-formal-0034

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `formal_term, regional_term`

Input:

```text
本公司将于下季度调整服务条款。
```

Codex expected:

```text
本公司將於下季度調整服務條款。
```

Acceptable variants:

```text
本公司將於下一季調整服務條款。
```

Rationale:

```text
正式公告「下季度/下一季」需依風格確認。
```

### blind-formal-0035

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
申请人需在期限内补交身份证明。
```

Codex expected:

```text
申請人需在期限內補交身分證明。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
身分證明採台灣用字。
```

### blind-formal-0036

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `formal_term, regional_term`

Input:

```text
会议记录应列明各项决议。
```

Codex expected:

```text
會議紀錄應列明各項決議。
```

Acceptable variants:

```text
會議記錄應列明各項決議。
```

Rationale:

```text
會議語境多用「紀錄」，但需看機關慣例。
```

### blind-formal-0037

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
主管机关将公告最新审查标准。
```

Codex expected:

```text
主管機關將公告最新審查標準。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
正式文件採「主管機關」。
```

### blind-formal-0038

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
本计划预计改善公共运输效率。
```

Codex expected:

```text
本計畫預計改善公共運輸效率。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
台灣正式文體採「計畫」「公共運輸」。
```

### blind-formal-0039

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
资料来源必须在报告附录中注明。
```

Codex expected:

```text
資料來源必須在報告附錄中註明。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
formal report wording。
```

### blind-formal-0040

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
承办人员应确认附件是否齐全。
```

Codex expected:

```text
承辦人員應確認附件是否齊全。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
承辦人員/附件齊全為正式文件常用。
```

### blind-formal-0041

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `formal_term`

Input:

```text
公告内容将同步发送给相关单位。
```

Codex expected:

```text
公告內容將同步發送給相關單位。
```

Acceptable variants:

```text
公告內容將同步寄送給相關單位。
```

Rationale:

```text
發送/寄送需依通知管道確認。
```

### blind-formal-0042

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
该办法适用于所有线上申请案件。
```

Codex expected:

```text
該辦法適用於所有線上申請案件。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
正式規範語氣。
```

### blind-formal-0043

- Domain: `formal`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, formal_term, regional_term`

Input:

```text
文件中既有的台北市法规名称不得改写。
```

Codex expected:

```text
文件中既有的台北市法規名稱不得改寫。
```

Acceptable variants:

```text
文件中既有的臺北市法規名稱不得改寫。
```

Rationale:

```text
既有法規名稱應保留圖形。
```

### blind-formal-0044

- Domain: `formal`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, formal_term, regional_term`

Input:

```text
附件里的台湾大学专有名称应保持原样。
```

Codex expected:

```text
附件裡的台灣大學專有名稱應保持原樣。
```

Acceptable variants:

```text
附件裡的臺灣大學專有名稱應保持原樣。
```

Rationale:

```text
專有名稱需保留。
```

### blind-formal-0045

- Domain: `formal`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, regional_term`

Input:

```text
请保留表格中原始的台中地址。
```

Codex expected:

```text
請保留表格中原始的台中地址。
```

Acceptable variants:

```text
請保留表格中原始的臺中地址。
```

Rationale:

```text
地址圖形需保留。
```

### blind-formal-0046

- Domain: `formal`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, regional_term`

Input:

```text
合约编号 TW-2026-台南 不应被转换。
```

Codex expected:

```text
合約編號 TW-2026-台南 不應被轉換。
```

Acceptable variants:

```text
合約編號 TW-2026-臺南 不應被轉換。
```

Rationale:

```text
合約編號中的文字需保留政策確認。
```

### blind-formal-0047

- Domain: `formal`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
本通知自发布日起生效。
```

Codex expected:

```text
本通知自發布日起生效。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
正式通知常用語。
```

### blind-formal-0048

- Domain: `formal`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
相关费用由申请单位自行负担。
```

Codex expected:

```text
相關費用由申請單位自行負擔。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
正式文件常用語。
```

### blind-social-0034

- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `regional_term, ui_term`

Input:

```text
我已经把活动照片传到共享相册了。
```

Codex expected:

```text
我已經把活動照片傳到共享相簿了。
```

Acceptable variants:

```text
我已經把活動照片上傳到共享相簿了。
```

Rationale:

```text
传到可作「傳到」或「上傳到」，需依語境。
```

### blind-social-0035

- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `regional_term`

Input:

```text
这家店的外卖速度比上次快。
```

Codex expected:

```text
這家店的外送速度比上次快。
```

Acceptable variants:

```text
這家店的外賣速度比上次快。
```

Rationale:

```text
台灣常用「外送」，但店家語境也可能用「外賣」。
```

### blind-social-0036

- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term, ui_term`

Input:

```text
你要不要先把行程发到群组？
```

Codex expected:

```text
你要不要先把行程傳到群組？
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
群組訊息語境「發到」採「傳到」。
```

### blind-social-0037

- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
我晚点再确认订位人数。
```

Codex expected:

```text
我晚點再確認訂位人數。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
餐廳 reservation 採「訂位」。
```

### blind-social-0038

- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term, ui_term`

Input:

```text
这则留言好像被系统隐藏了。
```

Codex expected:

```text
這則留言好像被系統隱藏了。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
社群留言語境自然。
```

### blind-social-0039

- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term, ui_term`

Input:

```text
请把购物车里的饮料换成无糖。
```

Codex expected:

```text
請把購物車裡的飲料換成無糖。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
購物車/無糖為台灣常用語。
```

### blind-social-0040

- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `regional_term`

Input:

```text
朋友说直播回放已经可以观看。
```

Codex expected:

```text
朋友說直播回放已經可以觀看。
```

Acceptable variants:

```text
朋友說直播重播已經可以觀看。
```

Rationale:

```text
「回放/重播」需依平台用語。
```

### blind-social-0041

- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
我把路线截图发给你了。
```

Codex expected:

```text
我把路線截圖傳給你了。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
發給你採「傳給你」。
```

### blind-social-0042

- Domain: `social`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, regional_term`

Input:

```text
昵称里的台湾队长不要自动改。
```

Codex expected:

```text
暱稱裡的台灣隊長不要自動改。
```

Acceptable variants:

```text
暱稱裡的臺灣隊長不要自動改。
```

Rationale:

```text
使用者暱稱應保留圖形。
```

### blind-social-0043

- Domain: `social`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, regional_term`

Input:

```text
照片说明里的台北小旅行保持原样。
```

Codex expected:

```text
照片說明裡的台北小旅行保持原樣。
```

Acceptable variants:

```text
照片說明裡的臺北小旅行保持原樣。
```

Rationale:

```text
照片說明中的既有字樣應保留。
```

### blind-social-0044

- Domain: `social`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion, regional_term`

Input:

```text
社群标签 #台中美食 不要转换。
```

Codex expected:

```text
社群標籤 #台中美食 不要轉換。
```

Acceptable variants:

```text
社群標籤 #臺中美食 不要轉換。
```

Rationale:

```text
hashtag 應保留。
```

### blind-social-0045

- Domain: `social`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion`

Input:

```text
请保留朋友写的繁体祝福语。
```

Codex expected:

```text
請保留朋友寫的繁體祝福語。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
既有繁體內容應保留。
```

### blind-social-0046

- Domain: `social`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
明天早上如果下雨就改搭捷运。
```

Codex expected:

```text
明天早上如果下雨就改搭捷運。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
日常台灣用語。
```

### blind-social-0047

- Domain: `social`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
这杯咖啡的甜度刚刚好。
```

Codex expected:

```text
這杯咖啡的甜度剛剛好。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
日常台灣用語。
```

### blind-social-0048

- Domain: `social`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
我们先在车站出口集合。
```

Codex expected:

```text
我們先在車站出口集合。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
日常台灣用語。
```

### blind-high-risk-0021

- Domain: `high_risk`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term, formal_term`

Input:

```text
医师会根据检查结果调整用药剂量。
```

Codex expected:

```text
醫師會根據檢查結果調整用藥劑量。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
醫療高風險，用語保守。
```

### blind-high-risk-0022

- Domain: `high_risk`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `high_risk_term, formal_term`

Input:

```text
银行应在扣款前发送交易通知。
```

Codex expected:

```text
銀行應在扣款前傳送交易通知。
```

Acceptable variants:

```text
銀行應在扣款前寄送交易通知。
```

Rationale:

```text
金融通知「傳送/寄送」需看管道。
```

### blind-high-risk-0023

- Domain: `high_risk`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term, formal_term`

Input:

```text
保险契约变更须经要保人同意。
```

Codex expected:

```text
保險契約變更須經要保人同意。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
保險正式用語。
```

### blind-high-risk-0024

- Domain: `high_risk`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `high_risk_term, formal_term`

Input:

```text
患者出院后仍需定期回诊追踪。
```

Codex expected:

```text
病患出院後仍需定期回診追蹤。
```

Acceptable variants:

```text
患者出院後仍需定期回診追蹤。
```

Rationale:

```text
台灣醫療語境「病患/患者」皆可，需確認。
```

### blind-high-risk-0025

- Domain: `high_risk`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term, formal_term`

Input:

```text
贷款申请资料不得提供给无关第三人。
```

Codex expected:

```text
貸款申請資料不得提供給無關第三人。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
金融/個資正式語氣。
```

### blind-high-risk-0026

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term, over_conversion, regional_term`

Input:

```text
病历中的台北院区名称不得改写。
```

Codex expected:

```text
病歷中的台北院區名稱不得改寫。
```

Acceptable variants:

```text
病歷中的臺北院區名稱不得改寫。
```

Rationale:

```text
醫療院區名稱需保留圖形。
```

### blind-high-risk-0027

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term, over_conversion, regional_term`

Input:

```text
契约附件里的台湾分公司名称应保持原样。
```

Codex expected:

```text
契約附件裡的台灣分公司名稱應保持原樣。
```

Acceptable variants:

```text
契約附件裡的臺灣分公司名稱應保持原樣。
```

Rationale:

```text
契約附件專有名稱需保留。
```

### blind-high-risk-0028

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term, over_conversion`

Input:

```text
汇款备注中的 Taichung Branch 不需翻译。
```

Codex expected:

```text
匯款備註中的 Taichung Branch 不需翻譯。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
金融備註中的英文分行名稱需保留。
```

### blind-high-risk-0029

- Domain: `high_risk`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term, formal_term`

Input:

```text
未成年人的法定代理人应共同签署。
```

Codex expected:

```text
未成年人的法定代理人應共同簽署。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
法律/金融高風險正式用語。
```

### blind-high-risk-0030

- Domain: `high_risk`
- Risk: `baseline_guard`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `high_risk_term, formal_term`

Input:

```text
电子病历存取应留下完整审计记录。
```

Codex expected:

```text
電子病歷存取應留下完整稽核紀錄。
```

Acceptable variants:

```text
電子病歷存取應留下完整審計記錄。
```

Rationale:

```text
audit record 在醫療系統可作「稽核紀錄」，需確認系統用語。
```
