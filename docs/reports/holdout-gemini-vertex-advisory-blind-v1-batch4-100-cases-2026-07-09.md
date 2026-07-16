<!-- zhtw:disable -->
# Holdout Gemini Vertex Advisory - blind-v1 Batch4 100 Cases

Generated date: `2026-07-09`
Dataset: `blind-v1`
Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Codex advisory: `docs/reports/holdout-codex-first-pass-blind-v1-batch4-100-cases-2026-07-09.json`
Raw Vertex JSON: `/tmp/zhtw-holdout-gemini-vertex-advisory-blind-v1-batch4-100-cases-2026-07-09.raw.json`
Stage: `independent_holdout_expected_review`
Reviewer: `gemini_vertex`

## Policy

- Gemini saw only input cases, not Codex recommendations.
- This report is advisory only.
- It is not ground truth and must not populate `blind-v1.expected.json` directly.
- Maintainer confirmation is required before any expected value becomes human decision.

## Summary

- Cases: 100
- Exact matches with Codex: 74
- Differences from Codex: 26
- Needs maintainer review: 64
- Repaired empty issue_tags from metadata: 17

Gemini confidence:

- `high`: 100

Domain distribution:

- `formal`: 15
- `high_risk`: 10
- `it`: 25
- `llm`: 15
- `social`: 15
- `ui`: 20

## Maintainer Review Queue

- `blind-it-0063` (it, different, Codex medium, Gemini high)
- `blind-it-0064` (it, different, Codex medium, Gemini high)
- `blind-it-0067` (it, different, Codex high, Gemini high)
- `blind-it-0069` (it, different, Codex medium, Gemini high)
- `blind-it-0070` (it, different, Codex medium, Gemini high)
- `blind-it-0072` (it, match, Codex medium, Gemini high)
- `blind-it-0073` (it, match, Codex medium, Gemini high)
- `blind-it-0074` (it, different, Codex medium, Gemini high)
- `blind-it-0075` (it, different, Codex high, Gemini high)
- `blind-it-0077` (it, different, Codex high, Gemini high)
- `blind-it-0078` (it, match, Codex medium, Gemini high)
- `blind-it-0080` (it, different, Codex high, Gemini high)
- `blind-it-0081` (it, match, Codex high, Gemini high)
- `blind-it-0082` (it, match, Codex high, Gemini high)
- `blind-it-0083` (it, match, Codex high, Gemini high)
- `blind-it-0084` (it, match, Codex high, Gemini high)
- `blind-it-0085` (it, different, Codex high, Gemini high)
- `blind-it-0086` (it, different, Codex high, Gemini high)
- `blind-it-0087` (it, different, Codex medium, Gemini high)
- `blind-ui-0048` (ui, different, Codex medium, Gemini high)
- `blind-ui-0049` (ui, match, Codex medium, Gemini high)
- `blind-ui-0050` (ui, match, Codex medium, Gemini high)
- `blind-ui-0053` (ui, different, Codex high, Gemini high)
- `blind-ui-0055` (ui, different, Codex high, Gemini high)
- `blind-ui-0060` (ui, match, Codex high, Gemini high)
- `blind-ui-0061` (ui, different, Codex high, Gemini high)
- `blind-ui-0062` (ui, match, Codex high, Gemini high)
- `blind-ui-0063` (ui, match, Codex medium, Gemini high)
- `blind-ui-0064` (ui, match, Codex high, Gemini high)
- `blind-ui-0067` (ui, match, Codex medium, Gemini high)
- `blind-llm-0033` (llm, different, Codex high, Gemini high)
- `blind-llm-0035` (llm, match, Codex medium, Gemini high)
- `blind-llm-0039` (llm, match, Codex medium, Gemini high)
- `blind-llm-0042` (llm, match, Codex high, Gemini high)
- `blind-llm-0043` (llm, match, Codex high, Gemini high)
- `blind-llm-0044` (llm, match, Codex high, Gemini high)
- `blind-llm-0045` (llm, match, Codex high, Gemini high)
- `blind-formal-0034` (formal, different, Codex medium, Gemini high)
- `blind-formal-0036` (formal, different, Codex medium, Gemini high)
- `blind-formal-0038` (formal, different, Codex high, Gemini high)
- `blind-formal-0041` (formal, match, Codex medium, Gemini high)
- `blind-formal-0043` (formal, match, Codex high, Gemini high)
- `blind-formal-0044` (formal, match, Codex high, Gemini high)
- `blind-formal-0045` (formal, match, Codex high, Gemini high)
- `blind-formal-0046` (formal, match, Codex high, Gemini high)
- `blind-social-0034` (social, match, Codex medium, Gemini high)
- `blind-social-0035` (social, match, Codex medium, Gemini high)
- `blind-social-0036` (social, different, Codex high, Gemini high)
- `blind-social-0040` (social, different, Codex medium, Gemini high)
- `blind-social-0041` (social, different, Codex high, Gemini high)
- `blind-social-0042` (social, match, Codex high, Gemini high)
- `blind-social-0043` (social, match, Codex high, Gemini high)
- `blind-social-0044` (social, match, Codex high, Gemini high)
- `blind-social-0045` (social, match, Codex high, Gemini high)
- `blind-high-risk-0021` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0022` (high_risk, different, Codex medium, Gemini high)
- `blind-high-risk-0023` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0024` (high_risk, different, Codex medium, Gemini high)
- `blind-high-risk-0025` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0026` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0027` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0028` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0029` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0030` (high_risk, different, Codex medium, Gemini high)

## Comparisons

### blind-it-0063：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
這個端點會返回分頁後的稽核日誌
```

Gemini notes:

```text
「端点」轉為「端點」，「分页」轉為「分頁」，「审计日志」轉為「稽核日誌」，「返回」在IT語境下更常用「傳回」。
```

### blind-it-0064：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
請在請求體裡加入用戶端版本號
```

Gemini notes:

```text
「请」轉為「請」，「请求体」轉為「請求主體」，「里」轉為「裡」，「客户端」轉為「用戶端」，「版本号」轉為「版本號」。
```

### blind-it-0065：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
缓存命中率会显示在监控面板上。
```

Codex expected:

```text
快取命中率會顯示在監控面板上。
```

Gemini expected:

```text
快取命中率會顯示在監控面板上。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「缓存」轉為「快取」，「会」轉為「會」，「显示」轉為「顯示」，「监控面板」轉為「監控面板」。
```

### blind-it-0066：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
部署脚本会检查环境变量是否完整。
```

Codex expected:

```text
部署指令碼會檢查環境變數是否完整。
```

Gemini expected:

```text
部署指令碼會檢查環境變數是否完整。
```

Gemini acceptable variants:

```text
部署腳本會檢查環境變數是否完整
```

Gemini notes:

```text
「脚本」轉為「指令碼」，「会」轉為「會」，「检查」轉為「檢查」，「环境变量」轉為「環境變數」。
```

### blind-it-0067：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
如果連線池已滿，服務會返回重試提示
```

Gemini notes:

```text
「连接池」轉為「連線池」，「已满」轉為「已滿」，「会」轉為「會」，「返回」在IT語境下更常用「傳回」。
```

### blind-it-0068：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请把错误堆栈附加到工单描述里。
```

Codex expected:

```text
請把錯誤堆疊附加到工單描述裡。
```

Gemini expected:

```text
請把錯誤堆疊附加到工單描述裡。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」，「错误堆栈」轉為「錯誤堆疊」，「工单」轉為「工單」，「里」轉為「裡」。
```

### blind-it-0069：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「这个」轉為「這個」，「钩子」轉為「掛鉤」，「会」轉為「會」，「发布」轉為「發布」，「安全扫描」轉為「安全性掃描」。
```

### blind-it-0070：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
命名空間裡的配置映射需要同步更新
```

Gemini notes:

```text
「命名空间」轉為「命名空間」，「里」轉為「裡」，「配置映射」轉為「組態對應」。
```

### blind-it-0071：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
消息队列会保留失败任务的重试次数。
```

Codex expected:

```text
訊息佇列會保留失敗任務的重試次數。
```

Gemini expected:

```text
訊息佇列會保留失敗任務的重試次數。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「消息队列」轉為「訊息佇列」，「会」轉為「會」，「失败」轉為「失敗」，「任务」轉為「任務」，「重试次数」轉為「重試次數」。
```

### blind-it-0072：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」，「变更记录」轉為「變更記錄」，「说明」轉為「說明」，「破坏性更新」轉為「破壞性更新」。
```

### blind-it-0073：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
上傳接口會驗證檔案校驗和
```

Gemini notes:

```text
「上传」轉為「上傳」，「接口」轉為「介面」，「会」轉為「會」，「验证」轉為「驗證」，「文件校验和」轉為「檔案校驗和」。
```

### blind-it-0074：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「日志」轉為「日誌」，「会」轉為「會」，「过滤」轉為「篩選」，「检查」轉為「檢查」，「请求」轉為「請求」。
```

### blind-it-0075：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
伺服器端渲染會讀取使用者偏好設定
```

Gemini notes:

```text
「服务端」轉為「伺服器端」，「渲染」轉為「轉譯」，「会」轉為「會」，「用户」轉為「使用者」，「偏好设置」轉為「偏好設定」。
```

### blind-it-0076：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请先撤销旧的访问密钥再生成新的。
```

Codex expected:

```text
請先撤銷舊的存取金鑰再產生新的。
```

Gemini expected:

```text
請先撤銷舊的存取金鑰再產生新的。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」，「撤销」轉為「撤銷」，「访问密钥」轉為「存取金鑰」，「生成」轉為「產生」。
```

### blind-it-0077：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
遷移任務會把舊欄位複製到新欄位
```

Gemini notes:

```text
「迁移」轉為「移轉」，「任务」轉為「任務」，「会」轉為「會」，「字段」轉為「欄位」，「复制」轉為「複製」。
```

### blind-it-0078：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「构建」轉為「建置」，「产物」轉為「產物」，「会」轉為「會」，「上传」轉為「上傳」，「内部」轉為「內部」，「制品库」轉為「製品庫」。
```

### blind-it-0079：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这个参数控制批量写入的缓冲大小。
```

Codex expected:

```text
這個參數控制批次寫入的緩衝大小。
```

Gemini expected:

```text
這個參數控制批次寫入的緩衝大小。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「这个」轉為「這個」，「参数」轉為「參數」，「批量写入」轉為「批次寫入」，「缓冲大小」轉為「緩衝大小」。
```

### blind-it-0080：different

- Domain: `it`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」，「里」轉為「裡」，「台湾」轉為「臺灣」，「示例」轉為「範例」，「路径」轉為「路徑」。此處「臺灣」為通用詞，非專有名稱，故轉換。
```

### blind-it-0081：match

- Domain: `it`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「变量名」轉為「變數名稱」，「不应」轉為「不應」，「翻译」轉為「翻譯」。變數名稱 'userStatusText' 依規定保留。
```

### blind-it-0082：match

- Domain: `it`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「项目」轉為「專案」，「代号」轉為「代號」，「必须」轉為「必須」，「维持原样」轉為「維持原樣」。專案代號 'TaipeiBridge' 依規定保留。
```

### blind-it-0083：match

- Domain: `it`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「测试」轉為「測試」，「资料」轉為「資料」，「门市」轉為「門市」。此處「台中」為地址一部分，依規定保留其圖形。
```

### blind-it-0084：match

- Domain: `it`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
請不要改寫已經本地化的按鈕標籤
```

Gemini notes:

```text
「请」轉為「請」，「改写」轉為「改寫」，「已经」轉為「已經」，「本地化」轉為「在地化」，「按钮」轉為「按鈕」，「标签」轉為「標籤」。
```

### blind-it-0085：different

- Domain: `it`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「执行」轉為「執行」，「完成后」轉為「完成後」，「会」轉為「會」，「输出」轉為「輸出」。
```

### blind-it-0086：different

- Domain: `it`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
配置文件缺少必要欄位時會停止啟動
```

Gemini notes:

```text
「配置文件」轉為「組態檔」，「必要字段」轉為「必要欄位」，「会」轉為「會」，「启动」轉為「啟動」。
```

### blind-it-0087：different

- Domain: `it`
- Risk: `baseline_guard`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
單元測試失敗時，流水線會標記為失敗
```

Gemini notes:

```text
「单元测试」轉為「單元測試」，「失败」轉為「失敗」，「流水线」轉為「管線」，「会」轉為「會」，「标记」轉為「標記」。
```

### blind-ui-0048：different

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
點擊篩選按鈕後，列表只顯示未處理項目
```

Gemini notes:

```text
「点击」轉為「點擊」，「筛选」轉為「篩選」，「按钮」轉為「按鈕」，「列表」轉為「清單」。
```

### blind-ui-0049：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
目前頁面會在保存後自動重新整理
```

Gemini notes:

```text
「当前」轉為「目前」，「页面」轉為「頁面」，「会」轉為「會」，「保存」轉為「儲存」，「刷新」轉為「重新整理」。
```

### blind-ui-0050：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
請在彈窗裡顯示上傳進度
```

Gemini notes:

```text
「请」轉為「請」，「弹窗」轉為「彈出視窗」，「里」轉為「裡」，「显示」轉為「顯示」，「上传」轉為「上傳」，「进度」轉為「進度」。
```

### blind-ui-0051：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
用户可以拖拽卡片调整顺序。
```

Codex expected:

```text
使用者可以拖曳卡片調整順序。
```

Gemini expected:

```text
使用者可以拖曳卡片調整順序。
```

Gemini acceptable variants:

```text
使用者可以拖拽卡片調整順序
```

Gemini notes:

```text
「用户」轉為「使用者」，「拖拽」轉為「拖曳」，「调整」轉為「調整」，「顺序」轉為「順序」。
```

### blind-ui-0052：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
表格列宽会根据内容自动调整。
```

Codex expected:

```text
表格欄寬會根據內容自動調整。
```

Gemini expected:

```text
表格欄寬會根據內容自動調整。
```

Gemini acceptable variants:

```text
表格列寬會根據內容自動調整
```

Gemini notes:

```text
「列宽」轉為「欄寬」，「会」轉為「會」，「根据」轉為「根據」，「自动调整」轉為「自動調整」。
```

### blind-ui-0053：different

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
找不到結果時顯示空狀態提示
```

Gemini notes:

```text
「结果」轉為「結果」，「显示」轉為「顯示」，「空状态」轉為「空白狀態」。
```

### blind-ui-0054：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请把错误信息放在输入框下方。
```

Codex expected:

```text
請把錯誤訊息放在輸入框下方。
```

Gemini expected:

```text
請把錯誤訊息放在輸入框下方。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」，「错误信息」轉為「錯誤訊息」，「输入框」轉為「輸入框」。
```

### blind-ui-0055：different

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
切換語言後，導航菜單會重新載入
```

Gemini notes:

```text
「切换」轉為「切換」，「语言」轉為「語言」，「导航菜单」轉為「導覽功能表」，「会」轉為「會」，「重新载入」轉為「重新載入」。
```

### blind-ui-0056：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这个开关控制是否接收系统通知。
```

Codex expected:

```text
這個開關控制是否接收系統通知。
```

Gemini expected:

```text
這個開關控制是否接收系統通知。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「这个」轉為「這個」，「开关」轉為「開關」，「系统通知」轉為「系統通知」。
```

### blind-ui-0057：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
编辑模式下会锁定删除按钮。
```

Codex expected:

```text
編輯模式下會鎖定刪除按鈕。
```

Gemini expected:

```text
編輯模式下會鎖定刪除按鈕。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「编辑模式」轉為「編輯模式」，「会」轉為「會」，「锁定」轉為「鎖定」，「删除按钮」轉為「刪除按鈕」。
```

### blind-ui-0058：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请在确认页列出所有已选项目。
```

Codex expected:

```text
請在確認頁列出所有已選項目。
```

Gemini expected:

```text
請在確認頁列出所有已選項目。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」，「确认页」轉為「確認頁」，「已选」轉為「已選」。
```

### blind-ui-0059：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
面包屑会显示上一层分类名称。
```

Codex expected:

```text
麵包屑會顯示上一層分類名稱。
```

Gemini expected:

```text
麵包屑會顯示上一層分類名稱。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「面包屑」轉為「麵包屑」，「会」轉為「會」，「显示」轉為「顯示」，「上一层」轉為「上一層」，「分类名称」轉為「分類名稱」。
```

### blind-ui-0060：match

- Domain: `ui`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「品牌页」轉為「品牌頁」，「里」轉為「裡」，「名称」轉為「名稱」，「必须」轉為「必須」，「保持原样」轉為「保持原樣」。此處「台北店」為專有名稱，依規定保留其圖形。
```

### blind-ui-0061：different

- Domain: `ui`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
使用者自定義標籤「台灣行程」不要自動改寫
```

Gemini notes:

```text
「用户」轉為「使用者」，「自定义」轉為「自訂義」，「标签」轉為「標籤」，「自动改写」轉為「自動改寫」。此處「台灣行程」為使用者自訂標籤，依規定保留其圖形。
```

### blind-ui-0062：match

- Domain: `ui`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」，「频道」轉為「頻道」，「名称」轉為「名稱」，「里」轉為「裡」，「繁体字样」轉為「繁體字樣」。此處「繁體字樣」為描述性文字，應轉換。
```

### blind-ui-0063：match

- Domain: `ui`
- Risk: `over_conversion_guard`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
收藏夾裡的 Taipei 2026 不需要翻譯
```

Gemini notes:

```text
「收藏夹」轉為「我的最愛」，「里」轉為「裡」，「翻译」轉為「翻譯」。'Taipei 2026' 依規定保留。
```

### blind-ui-0064：match

- Domain: `ui`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「已经」轉為「已經」，「审核」轉為「審核」，「繁体说明」轉為「繁體說明」，「不应」轉為「不應」，「转换」轉為「轉換」。此處「繁體說明」為描述性文字，應轉換。
```

### blind-ui-0065：match

- Domain: `ui`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
提交成功后会显示绿色提示。
```

Codex expected:

```text
提交成功後會顯示綠色提示。
```

Gemini expected:

```text
提交成功後會顯示綠色提示。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「成功后」轉為「成功後」，「会」轉為「會」，「显示」轉為「顯示」，「绿色」轉為「綠色」。
```

### blind-ui-0066：match

- Domain: `ui`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
密码输入错误三次后会暂时锁定。
```

Codex expected:

```text
密碼輸入錯誤三次後會暫時鎖定。
```

Gemini expected:

```text
密碼輸入錯誤三次後會暫時鎖定。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「密码」轉為「密碼」，「输入」轉為「輸入」，「错误」轉為「錯誤」，「三次后」轉為「三次後」，「会」轉為「會」，「暂时」轉為「暫時」，「锁定」轉為「鎖定」。
```

### blind-ui-0067：match

- Domain: `ui`
- Risk: `baseline_guard`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「页面」轉為「頁面」，「载入」轉為「載入」，「显示」轉為「顯示」，「骨架画面」轉為「骨架畫面」。
```

### blind-llm-0033：different

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
請根據上下文補全這段說明
```

Gemini notes:

```text
「请」轉為「請」，「根据」轉為「根據」，「补全」轉為「補齊」，「这段」轉為「這段」，「说明」轉為「說明」。
```

### blind-llm-0034：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
模型需要解释每个参数的用途。
```

Codex expected:

```text
模型需要解釋每個參數的用途。
```

Gemini expected:

```text
模型需要解釋每個參數的用途。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「解释」轉為「解釋」，「每个」轉為「每個」，「参数」轉為「參數」。
```

### blind-llm-0035：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
生成的摘要應保留原文的時間順序
```

Gemini notes:

```text
「生成」轉為「產生」，「应」轉為「應」，「时间顺序」轉為「時間順序」。
```

### blind-llm-0036：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请把长回复改写成三点建议。
```

Codex expected:

```text
請把長回覆改寫成三點建議。
```

Gemini expected:

```text
請把長回覆改寫成三點建議。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」，「长回复」轉為「長回覆」，「改写」轉為「改寫」，「三点」轉為「三點」，「建议」轉為「建議」。
```

### blind-llm-0037：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
系统提示词要求输出有效的 YAML。
```

Codex expected:

```text
系統提示詞要求輸出有效的 YAML。
```

Gemini expected:

```text
系統提示詞要求輸出有效的 YAML。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「系统」轉為「系統」，「提示词」轉為「提示詞」，「输出」轉為「輸出」。
```

### blind-llm-0038：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
如果证据不足，请明确说明限制。
```

Codex expected:

```text
如果證據不足，請明確說明限制。
```

Gemini expected:

```text
如果證據不足，請明確說明限制。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「证据」轉為「證據」，「请」轉為「請」，「明确」轉為「明確」，「说明」轉為「說明」。
```

### blind-llm-0039：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
這個代理會調用工具讀取檔案清單
```

Gemini notes:

```text
「这个」轉為「這個」，「会」轉為「會」，「调用」轉為「呼叫」，「文件列表」轉為「檔案清單」。
```

### blind-llm-0040：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请把客服对话整理成后续任务。
```

Codex expected:

```text
請把客服對話整理成後續任務。
```

Gemini expected:

```text
請把客服對話整理成後續任務。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」，「对话」轉為「對話」，「后续」轉為「後續」，「任务」轉為「任務」。
```

### blind-llm-0041：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
回答里不要加入用户没有提供的日期。
```

Codex expected:

```text
回答裡不要加入使用者沒有提供的日期。
```

Gemini expected:

```text
回答裡不要加入使用者沒有提供的日期。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「里」轉為「裡」，「用户」轉為「使用者」，「没有」轉為「沒有」。
```

### blind-llm-0042：match

- Domain: `llm`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」，「提示词」轉為「提示詞」，「里」轉為「裡」，「变量名」轉為「變數名稱」。變數名稱 'productTitle' 依規定保留。
```

### blind-llm-0043：match

- Domain: `llm`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「范例」轉為「範例」，「输出」轉為「輸出」。此處「台灣郵遞區號」為範例輸出內容，依規定保留其圖形。
```

### blind-llm-0044：match

- Domain: `llm`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」，「改写」轉為「改寫」，「用户」轉為「使用者」。此處「台北地址」為地址一部分，依規定保留其圖形。
```

### blind-llm-0045：match

- Domain: `llm`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「训练」轉為「訓練」，「资料」轉為「資料」，「里」轉為「裡」，「繁体句子」轉為「繁體句子」，「应」轉為「應」，「保持原样」轉為「保持原樣」。此處「繁體句子」為描述性文字，應轉換。
```

### blind-llm-0046：match

- Domain: `llm`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请用一句话说明这个功能的限制。
```

Codex expected:

```text
請用一句話說明這個功能的限制。
```

Gemini expected:

```text
請用一句話說明這個功能的限制。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」，「一句话」轉為「一句話」，「说明」轉為「說明」，「这个」轉為「這個」。
```

### blind-llm-0047：match

- Domain: `llm`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
模型回答前应先检查输入是否完整。
```

Codex expected:

```text
模型回答前應先檢查輸入是否完整。
```

Gemini expected:

```text
模型回答前應先檢查輸入是否完整。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「应」轉為「應」，「检查」轉為「檢查」，「输入」轉為「輸入」。
```

### blind-formal-0034：different

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
本公司將於下季度調整服務條款
```

Gemini notes:

```text
「将于」轉為「將於」，「下季度」轉為「下個季度」，「调整」轉為「調整」，「服务条款」轉為「服務條款」。
```

### blind-formal-0035：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
申请人需在期限内补交身份证明。
```

Codex expected:

```text
申請人需在期限內補交身分證明。
```

Gemini expected:

```text
申請人需在期限內補交身分證明。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「申请人」轉為「申請人」，「期限内」轉為「期限內」，「身份证明」轉為「身分證明」。
```

### blind-formal-0036：different

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「会议记录」轉為「會議記錄」，「应」轉為「應」，「各项」轉為「各項」，「决议」轉為「決議」。
```

### blind-formal-0037：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
主管机关将公告最新审查标准。
```

Codex expected:

```text
主管機關將公告最新審查標準。
```

Gemini expected:

```text
主管機關將公告最新審查標準。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「主管机关」轉為「主管機關」，「将」轉為「將」，「审查标准」轉為「審查標準」。
```

### blind-formal-0038：different

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
本計畫預計改善公共運輸效率
```

Gemini notes:

```text
「本计划」轉為「本計畫」，「预计」轉為「預計」，「公共运输」轉為「大眾運輸」。
```

### blind-formal-0039：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
资料来源必须在报告附录中注明。
```

Codex expected:

```text
資料來源必須在報告附錄中註明。
```

Gemini expected:

```text
資料來源必須在報告附錄中註明。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「资料」轉為「資料」，「来源」轉為「來源」，「必须」轉為「必須」，「报告」轉為「報告」，「附录」轉為「附錄」，「注明」轉為「註明」。
```

### blind-formal-0040：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
承办人员应确认附件是否齐全。
```

Codex expected:

```text
承辦人員應確認附件是否齊全。
```

Gemini expected:

```text
承辦人員應確認附件是否齊全。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「承办人员」轉為「承辦人員」，「应」轉為「應」，「确认」轉為「確認」，「是否齐全」轉為「是否齊全」。
```

### blind-formal-0041：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「内容」轉為「內容」，「将」轉為「將」，「发送」轉為「發送」，「相关」轉為「相關」。
```

### blind-formal-0042：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
该办法适用于所有线上申请案件。
```

Codex expected:

```text
該辦法適用於所有線上申請案件。
```

Gemini expected:

```text
該辦法適用於所有線上申請案件。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「该办法」轉為「該辦法」，「适用」轉為「適用」，「申请」轉為「申請」。
```

### blind-formal-0043：match

- Domain: `formal`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「法规」轉為「法規」，「名称」轉為「名稱」，「改写」轉為「改寫」。此處「台北市」為專有名稱，依規定保留其圖形。
```

### blind-formal-0044：match

- Domain: `formal`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「里」轉為「裡」，「专有名称」轉為「專有名稱」，「应」轉為「應」，「保持原样」轉為「保持原樣」。此處「台灣大學」為專有名稱，依規定保留其圖形。
```

### blind-formal-0045：match

- Domain: `formal`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」。此處「台中」為地址一部分，依規定保留其圖形。
```

### blind-formal-0046：match

- Domain: `formal`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「合约」轉為「合約」，「编号」轉為「編號」，「不应」轉為「不應」，「转换」轉為「轉換」。'TW-2026-台南' 依規定保留。
```

### blind-formal-0047：match

- Domain: `formal`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
本通知自发布日起生效。
```

Codex expected:

```text
本通知自發布日起生效。
```

Gemini expected:

```text
本通知自發布日起生效。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「发布日」轉為「發布日」。
```

### blind-formal-0048：match

- Domain: `formal`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
相关费用由申请单位自行负担。
```

Codex expected:

```text
相關費用由申請單位自行負擔。
```

Gemini expected:

```text
相關費用由申請單位自行負擔。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「相关」轉為「相關」，「费用」轉為「費用」，「申请单位」轉為「申請單位」，「负担」轉為「負擔」。
```

### blind-social-0034：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「已经」轉為「已經」，「传到」轉為「傳到」，「相册」轉為「相簿」。
```

### blind-social-0035：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「这家」轉為「這家」，「外卖」轉為「外送」。
```

### blind-social-0036：different

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「发到」轉為「發到」，「群组」轉為「群組」。
```

### blind-social-0037：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
我晚点再确认订位人数。
```

Codex expected:

```text
我晚點再確認訂位人數。
```

Gemini expected:

```text
我晚點再確認訂位人數。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「晚点」轉為「晚點」，「确认」轉為「確認」，「订位」轉為「訂位」，「人数」轉為「人數」。
```

### blind-social-0038：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这则留言好像被系统隐藏了。
```

Codex expected:

```text
這則留言好像被系統隱藏了。
```

Gemini expected:

```text
這則留言好像被系統隱藏了。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「这则」轉為「這則」，「系统」轉為「系統」，「隐藏」轉為「隱藏」。
```

### blind-social-0039：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请把购物车里的饮料换成无糖。
```

Codex expected:

```text
請把購物車裡的飲料換成無糖。
```

Gemini expected:

```text
請把購物車裡的飲料換成無糖。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」，「购物车」轉為「購物車」，「里」轉為「裡」，「饮料」轉為「飲料」，「换成」轉為「換成」，「无糖」轉為「無糖」。
```

### blind-social-0040：different

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
朋友說直播回放已經可以觀看
```

Gemini notes:

```text
「说」轉為「說」，「回放」轉為「重播」，「已经」轉為「已經」，「观看」轉為「觀看」。
```

### blind-social-0041：different

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「路线」轉為「路線」，「截图」轉為「截圖」，「发给」轉為「發給」。
```

### blind-social-0042：match

- Domain: `social`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「昵称」轉為「暱稱」，「里」轉為「裡」，「自动」轉為「自動」。此處「台灣隊長」為暱稱，依規定保留其圖形。
```

### blind-social-0043：match

- Domain: `social`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「说明」轉為「說明」，「里」轉為「裡」，「保持原样」轉為「保持原樣」。此處「台北小旅行」為照片說明，依規定保留其圖形。
```

### blind-social-0044：match

- Domain: `social`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「标签」轉為「標籤」，「转换」轉為「轉換」。此處「#台中美食」為社群標籤，依規定保留其圖形。
```

### blind-social-0045：match

- Domain: `social`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」，「写」轉為「寫」，「繁体祝福语」轉為「繁體祝福語」。此處「繁體祝福語」為描述性文字，應轉換。
```

### blind-social-0046：match

- Domain: `social`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
明天早上如果下雨就改搭捷运。
```

Codex expected:

```text
明天早上如果下雨就改搭捷運。
```

Gemini expected:

```text
明天早上如果下雨就改搭捷運。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「捷运」轉為「捷運」。
```

### blind-social-0047：match

- Domain: `social`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这杯咖啡的甜度刚刚好。
```

Codex expected:

```text
這杯咖啡的甜度剛剛好。
```

Gemini expected:

```text
這杯咖啡的甜度剛剛好。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「这杯」轉為「這杯」，「刚刚好」轉為「剛剛好」。
```

### blind-social-0048：match

- Domain: `social`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
我们先在车站出口集合。
```

Codex expected:

```text
我們先在車站出口集合。
```

Gemini expected:

```text
我們先在車站出口集合。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「我们」轉為「我們」，「车站」轉為「車站」。
```

### blind-high-risk-0021：match

- Domain: `high_risk`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「医师」轉為「醫師」，「会」轉為「會」，「根据」轉為「根據」，「检查结果」轉為「檢查結果」，「调整」轉為「調整」，「用药剂量」轉為「用藥劑量」。
```

### blind-high-risk-0022：different

- Domain: `high_risk`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「银行」轉為「銀行」，「应」轉為「應」，「发送」轉為「發送」。
```

### blind-high-risk-0023：match

- Domain: `high_risk`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「保险」轉為「保險」，「契约」轉為「契約」，「变更」轉為「變更」。
```

### blind-high-risk-0024：different

- Domain: `high_risk`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「后」轉為「後」，「回诊」轉為「回診」，「追踪」轉為「追蹤」。
```

### blind-high-risk-0025：match

- Domain: `high_risk`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「贷款」轉為「貸款」，「申请」轉為「申請」，「资料」轉為「資料」，「给」轉為「給」，「无关」轉為「無關」。
```

### blind-high-risk-0026：match

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「病历」轉為「病歷」，「院区」轉為「院區」，「名称」轉為「名稱」，「改写」轉為「改寫」。此處「台北」為專有名稱，依規定保留其圖形。
```

### blind-high-risk-0027：match

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「契约」轉為「契約」，「里」轉為「裡」，「名称」轉為「名稱」，「应」轉為「應」，「保持原样」轉為「保持原樣」。此處「台灣分公司」為專有名稱，依規定保留其圖形。
```

### blind-high-risk-0028：match

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「汇款」轉為「匯款」，「备注」轉為「備註」，「翻译」轉為「翻譯」。'Taichung Branch' 依規定保留。
```

### blind-high-risk-0029：match

- Domain: `high_risk`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「法定代理人」轉為「法定代理人」，「应」轉為「應」，「签署」轉為「簽署」。
```

### blind-high-risk-0030：different

- Domain: `high_risk`
- Risk: `baseline_guard`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

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

Gemini acceptable variants:

```text
電子病歷存取應留下完整審計記錄
```

Gemini notes:

```text
「电子病历」轉為「電子病歷」，「应」轉為「應」，「审计记录」轉為「稽核記錄」。
```
