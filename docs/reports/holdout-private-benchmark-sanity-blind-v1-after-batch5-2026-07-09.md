<!-- zhtw:disable -->
# Accuracy Benchmark (2026-07-09)

Dataset: `blind-v1`
Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Expected: `benchmarks/accuracy/blind-v1.expected.json`
Competitors lock: `benchmarks/accuracy/competitors.lock.json`

## Hashes

- Inputs sha256: `29200c136659fecd27e8efb59390d18f53a33508962848845c4eb78de6cd0f41`
- Expected sha256: `8682ef7b0a2cf1bc61a75628eadc16d196d7d64b6ebc3f28fc0ae447ae913fdf`
- Lock sha256: `d9bf3f57e280287e1cc1699d82d62bcbe28c1b1665b82ab1db60ef8520bdad18`

## Summary

- Cases: 338

Domain distribution:

- `formal`: 54
- `high_risk`: 36
- `it`: 68
- `llm`: 57
- `social`: 55
- `ui`: 68

Risk distribution:

- `baseline_guard`: 53
- `candidate_gap`: 197
- `over_conversion_guard`: 88

## Engine Scores

### zhtw

- Availability: available
- Version: `4.4.1`
- Accepted accuracy: 0.8905
- Primary exact accuracy: 0.7160
- Idempotency rate: 0.9911
- Accepted: 301 / 338
- Misses: 37

## Misses

### blind-llm-0026 / zhtw

- Domain: `llm`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion`

Input:

```text
请保留原文中的台湾用语，不要自动改写。
```

Expected:

```text
請保留原文中的台灣用語，不要自動改寫。
```

Actual:

```text
請保留原文中的臺灣用語，不要自動改寫。
```

### blind-llm-0028 / zhtw

- Domain: `llm`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion`

Input:

```text
范例输出里的台北地址应保持原样。
```

Expected:

```text
範例輸出裡的台北地址應保持原樣。
```

Actual:

```text
範例輸出裡的臺北地址應保持原樣。
```

### blind-formal-0029 / zhtw

- Domain: `formal`
- Risk: `over_conversion_guard`
- Issue tags: `formal_term, regional_term, over_conversion`

Input:

```text
本案涉及台北市既有法规用语。
```

Expected:

```text
本案涉及台北市既有法規用語。
```

Actual:

```text
本案涉及臺北市既有法規用語。
```

### blind-social-0025 / zhtw

- Domain: `social`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion`

Input:

```text
留言里提到的台湾地名不要被改成其他说法。
```

Expected:

```text
留言裡提到的台灣地名不要被改成其他說法。
```

Actual:

```text
留言裡提到的臺灣地名不要被改成其他說法。
```

### blind-social-0026 / zhtw

- Domain: `social`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion`

Input:

```text
这段贴文已经是台湾朋友写的繁体版本。
```

Expected:

```text
這段貼文已經是台灣朋友寫的繁體版本。
```

Actual:

```text
這段貼文已經是臺灣朋友寫的繁體版本。
```

### blind-it-0083 / zhtw

- Domain: `it`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion, it_term`

Input:

```text
测试资料包含台中门市的原始地址。
```

Expected:

```text
測試資料包含台中門市的原始地址。
```

Actual:

```text
測試資料包含臺中門市的原始地址。
```

### blind-ui-0060 / zhtw

- Domain: `ui`
- Risk: `over_conversion_guard`
- Issue tags: `ui_term, regional_term, over_conversion`

Input:

```text
品牌页里的台北店名称必须保持原样。
```

Expected:

```text
品牌頁裡的台北店名稱必須保持原樣。
```

Actual:

```text
品牌頁裡的臺北店名稱必須保持原樣。
```

### blind-ui-0061 / zhtw

- Domain: `ui`
- Risk: `over_conversion_guard`
- Issue tags: `ui_term, regional_term, over_conversion`

Input:

```text
用户自定义标签“台湾行程”不要自动改写。
```

Expected:

```text
使用者自訂標籤「台灣行程」不要自動改寫。
```

Actual:

```text
使用者自訂標籤“臺灣行程”不要自動改寫。
```

### blind-llm-0043 / zhtw

- Domain: `llm`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion, it_term`

Input:

```text
范例输出中的台湾邮递区号不要改。
```

Expected:

```text
範例輸出中的台灣郵遞區號不要改。
```

Actual:

```text
範例輸出中的臺灣郵遞區號不要改。
```

### blind-llm-0044 / zhtw

- Domain: `llm`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion, it_term`

Input:

```text
请不要改写用户提供的台北地址。
```

Expected:

```text
請不要改寫使用者提供的台北地址。
```

Actual:

```text
請不要改寫使用者提供的臺北地址。
```

### blind-formal-0043 / zhtw

- Domain: `formal`
- Risk: `over_conversion_guard`
- Issue tags: `formal_term, regional_term, over_conversion`

Input:

```text
文件中既有的台北市法规名称不得改写。
```

Expected:

```text
文件中既有的台北市法規名稱不得改寫。
```

Actual:

```text
文件中既有的臺北市法規名稱不得改寫。
```

### blind-formal-0044 / zhtw

- Domain: `formal`
- Risk: `over_conversion_guard`
- Issue tags: `formal_term, regional_term, over_conversion`

Input:

```text
附件里的台湾大学专有名称应保持原样。
```

Expected:

```text
附件裡的台灣大學專有名稱應保持原樣。
```

Actual:

```text
附件裡的臺灣大學專有名稱應保持原樣。
```

### blind-formal-0045 / zhtw

- Domain: `formal`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion, formal_term`

Input:

```text
请保留表格中原始的台中地址。
```

Expected:

```text
請保留表格中原始的台中地址。
```

Actual:

```text
請保留表格中原始的臺中地址。
```

### blind-formal-0046 / zhtw

- Domain: `formal`
- Risk: `over_conversion_guard`
- Issue tags: `formal_term, regional_term, over_conversion`

Input:

```text
合约编号 TW-2026-台南 不应被转换。
```

Expected:

```text
合約編號 TW-2026-台南 不應被轉換。
```

Actual:

```text
合約編號 TW-2026-臺南 不應被轉換。
```

### blind-social-0042 / zhtw

- Domain: `social`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion`

Input:

```text
昵称里的台湾队长不要自动改。
```

Expected:

```text
暱稱裡的台灣隊長不要自動改。
```

Actual:

```text
暱稱裡的臺灣隊長不要自動改。
```

### blind-social-0043 / zhtw

- Domain: `social`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion`

Input:

```text
照片说明里的台北小旅行保持原样。
```

Expected:

```text
照片說明裡的台北小旅行保持原樣。
```

Actual:

```text
照片說明裡的臺北小旅行保持原樣。
```

### blind-social-0044 / zhtw

- Domain: `social`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion`

Input:

```text
社群标签 #台中美食 不要转换。
```

Expected:

```text
社群標籤 #台中美食 不要轉換。
```

Actual:

```text
社群標籤 #臺中美食 不要轉換。
```

### blind-high-risk-0026 / zhtw

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Issue tags: `high_risk_term, formal_term, regional_term, over_conversion`

Input:

```text
病历中的台北院区名称不得改写。
```

Expected:

```text
病歷中的台北院區名稱不得改寫。
```

Actual:

```text
病歷中的臺北院區名稱不得改寫。
```

### blind-high-risk-0027 / zhtw

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Issue tags: `high_risk_term, formal_term, regional_term, over_conversion`

Input:

```text
契约附件里的台湾分公司名称应保持原样。
```

Expected:

```text
契約附件裡的台灣分公司名稱應保持原樣。
```

Actual:

```text
契約附件裡的臺灣分公司名稱應保持原樣。
```

### blind-it-0088 / zhtw

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`

Input:

```text
部署平台会在发布前检查环境变量是否完整。
```

Expected:

```text
部署平台會在發布前檢查環境變數是否完整。
```

Actual:

```text
部署平臺會在發布前檢查環境變數是否完整。
```

### blind-it-0089 / zhtw

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`

Input:

```text
这个 SDK 会缓存身份令牌并在过期前刷新。
```

Expected:

```text
這個 SDK 會快取身分權杖並在過期前重新整理。
```

Actual:

```text
這個 SDK 會快取身份權杖並在過期前刷新。
```

### blind-it-0090 / zhtw

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`

Input:

```text
请把错误堆栈写入调试日志。
```

Expected:

```text
請把錯誤堆疊寫入偵錯日誌。
```

Actual:

```text
請把錯誤堆疊寫入除錯日誌。
```

### blind-it-0092 / zhtw

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`

Input:

```text
命令行工具支持从配置文件读取默认区域。
```

Expected:

```text
命令列工具支援從設定檔讀取預設區域。
```

Actual:

```text
命令列工具支持從設定檔讀取默認區域。
```

### blind-it-0094 / zhtw

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`

Input:

```text
请在迁移脚本里新增回滚步骤。
```

Expected:

```text
請在遷移指令碼裡新增復原步驟。
```

Actual:

```text
請在遷移指令碼裡新增回滾步驟。
```

### blind-it-0095 / zhtw

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`

Input:

```text
当数据库连接失败时，应用会进入只读模式。
```

Expected:

```text
當資料庫連線失敗時，應用程式會進入唯讀模式。
```

Actual:

```text
當資料庫連線失敗時，應用會進入只讀模式。
```

### blind-it-0096 / zhtw

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`

Input:

```text
这个端点会返回上传任务的处理状态。
```

Expected:

```text
這個端點會回傳上傳任務的處理狀態。
```

Actual:

```text
這個端點會返回上傳任務的處理狀態。
```

### blind-it-0097 / zhtw

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`

Input:

```text
构建缓存命中后，流水线可以跳过编译步骤。
```

Expected:

```text
建置快取命中後，管線可以略過編譯步驟。
```

Actual:

```text
建置快取命中後，流水線可以跳過編譯步驟。
```

### blind-it-0105 / zhtw

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`

Input:

```text
容器启动前会先挂载配置卷。
```

Expected:

```text
容器啟動前會先掛載設定磁碟區。
```

Actual:

```text
容器啟動前會先掛載配置卷。
```

### blind-it-0108 / zhtw

- Domain: `it`
- Risk: `over_conversion_guard`
- Issue tags: `over_conversion, it_term, regional_term`

Input:

```text
错误样本里的台北节点名称不应改写。
```

Expected:

```text
錯誤樣本裡的台北節點名稱不應改寫。
```

Actual:

```text
錯誤樣本裡的臺北節點名稱不應改寫。
```

### blind-ui-0070 / zhtw

- Domain: `ui`
- Risk: `candidate_gap`
- Issue tags: `ui_term, regional_term`

Input:

```text
表格支持按更新时间筛选记录。
```

Expected:

```text
表格支援依更新時間篩選記錄。
```

Actual:

```text
表格支持按更新時間篩選記錄。
```

### blind-ui-0073 / zhtw

- Domain: `ui`
- Risk: `candidate_gap`
- Issue tags: `ui_term, regional_term`

Input:

```text
分页控件会显示总页数。
```

Expected:

```text
分頁控制項會顯示總頁數。
```

Actual:

```text
分頁控制元件會顯示總頁數。
```

### blind-ui-0074 / zhtw

- Domain: `ui`
- Risk: `candidate_gap`
- Issue tags: `ui_term, regional_term`

Input:

```text
拖动列标题可以调整显示顺序。
```

Expected:

```text
拖曳欄位標題可以調整顯示順序。
```

Actual:

```text
拖動列標題可以調整顯示順序。
```

### blind-ui-0079 / zhtw

- Domain: `ui`
- Risk: `candidate_gap`
- Issue tags: `ui_term, regional_term`

Input:

```text
通知中心会按时间倒序排列消息。
```

Expected:

```text
通知中心會依時間倒序排列訊息。
```

Actual:

```text
通知中心會按時間倒序排列消息。
```

### blind-ui-0081 / zhtw

- Domain: `ui`
- Risk: `over_conversion_guard`
- Issue tags: `over_conversion, ui_term, regional_term`

Input:

```text
示例账号 TaipeiAdmin 必须维持原样。
```

Expected:

```text
範例帳號 TaipeiAdmin 必須維持原樣。
```

Actual:

```text
示例帳號 TaipeiAdmin 必須維持原樣。
```

### blind-ui-0087 / zhtw

- Domain: `ui`
- Risk: `baseline_guard`
- Issue tags: `ui_term, regional_term`

Input:

```text
二维码失效后会显示提示文字。
```

Expected:

```text
QR Code 失效後會顯示提示文字。
```

Actual:

```text
QR Code失效後會顯示提示文字。
```

### blind-llm-0051 / zhtw

- Domain: `llm`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`

Input:

```text
这个代理会读取工具返回的 JSON 结果。
```

Expected:

```text
這個代理會讀取工具回傳的 JSON 結果。
```

Actual:

```text
這個代理會讀取工具返回的 JSON 結果。
```

### blind-high-risk-0039 / zhtw

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Issue tags: `over_conversion, high_risk_term, formal_term, regional_term`

Input:

```text
病历附件里的台北院区代码不可改写。
```

Expected:

```text
病歷附件裡的台北院區代碼不可改寫。
```

Actual:

```text
病歷附件裡的臺北院區程式碼不可改寫。
```
