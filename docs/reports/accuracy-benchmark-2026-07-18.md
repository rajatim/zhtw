<!-- zhtw:disable -->
# Accuracy Benchmark (2026-07-18)

Dataset: `blind-v1`
Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Expected: `benchmarks/accuracy/blind-v1.expected.json`
Competitors lock: `benchmarks/accuracy/competitors.lock.json`

## Hashes

- Inputs sha256: `4367f25a4bde5a1703163334815e5579788f528bed9401f4197a93bea5ee03e7`
- Expected sha256: `80d27928a962cb03319c09b80f8b0aa22f25be3eb756130e63bfcac1df1c3dcc`
- Lock sha256: `d9bf3f57e280287e1cc1699d82d62bcbe28c1b1665b82ab1db60ef8520bdad18`

## Summary

- Cases: 1008

Domain distribution:

- `formal`: 164
- `high_risk`: 128
- `it`: 189
- `llm`: 159
- `social`: 180
- `ui`: 188

Risk distribution:

- `baseline_guard`: 161
- `candidate_gap`: 564
- `over_conversion_guard`: 283

## Engine Scores

### zhtw

- Availability: available
- Version: `4.4.1`
- Accepted accuracy: 0.9474
- Primary exact accuracy: 0.7520
- Idempotency rate: 0.9841
- Accepted: 955 / 1008
- Misses: 53

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

### blind-it-0131 / zhtw

- Domain: `it`
- Risk: `over_conversion_guard`
- Issue tags: `over_conversion, it_term, regional_term`

Input:

```text
README 里的 zh-TW 示例路径不要转换成其他地区。
```

Expected:

```text
README 裡的 zh-TW 範例路徑不要轉換成其他地區。
```

Actual:

```text
README 裡的 zh-TW 示例路徑不要轉換成其他地區。
```

### blind-ui-0102 / zhtw

- Domain: `ui`
- Risk: `over_conversion_guard`
- Issue tags: `over_conversion, ui_term, regional_term`

Input:

```text
语言包里已经本地化的「登入」不要改写。
```

Expected:

```text
語言套件裡已經在地化的「登入」不要改寫。
```

Actual:

```text
語言包裡已經本機化的「登入」不要改寫。
```

### blind-high-risk-0053 / zhtw

- Domain: `high_risk`
- Risk: `candidate_gap`
- Issue tags: `regional_term, high_risk_term`

Input:

```text
银行会在交易异常时暂停付款指令。
```

Expected:

```text
銀行會在交易異常時暫停付款指令。
```

Actual:

```text
銀行會在交易例外時暫停付款指令。
```

### blind-high-risk-0058 / zhtw

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, high_risk_term, over_conversion`

Input:

```text
本繁體醫療聲明已經核准，請勿改寫。
```

Expected:

```text
本繁體醫療聲明已經核准，請勿改寫。
```

Actual:

```text
本繁體醫療宣告已經核准，請勿改寫。
```

### blind-ui-0147 / zhtw

- Domain: `ui`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, ui_term, over_conversion`

Input:

```text
請不要轉換已核准的客服視窗文案。
```

Expected:

```text
請不要轉換已核准的客服視窗文案。
```

Actual:

```text
請不要轉換已覈准的客服視窗文案。
```

### blind-formal-0105 / zhtw

- Domain: `formal`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, formal_term, over_conversion`

Input:

```text
本繁體公告已核定，請勿改寫。
```

Expected:

```text
本繁體公告已核定，請勿改寫。
```

Actual:

```text
本繁體公告已覈定，請勿改寫。
```

### blind-high-risk-0064 / zhtw

- Domain: `high_risk`
- Risk: `candidate_gap`
- Issue tags: `regional_term, high_risk_term, candidate_gap`

Input:

```text
法院可依申请核发支付命令。
```

Expected:

```text
法院可依申請核發支付命令。
```

Actual:

```text
法院可依申請核發付款命令。
```

### blind-high-risk-0068 / zhtw

- Domain: `high_risk`
- Risk: `baseline_guard`
- Issue tags: `regional_term, high_risk_term, baseline_guard`

Input:

```text
请保留金融机构代码 812。
```

Expected:

```text
請保留金融機構代碼 812。
```

Actual:

```text
請保留金融機構程式碼 812。
```

### blind-social-0110 / zhtw

- Domain: `social`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, social_term, over_conversion`

Input:

```text
这家店的菜单更新了吗？
```

Expected:

```text
這家店的菜單更新了嗎？
```

Actual:

```text
這家店的選單更新了嗎？
```

### blind-high-risk-0084 / zhtw

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, formal_term, high_risk_term, over_conversion`

Input:

```text
契约解除条件应以双方书面约定为准。
```

Expected:

```text
契約解除條件應以雙方書面約定為準。
```

Actual:

```text
契約解除條件應以雙方書面約定為准。
```

### blind-it-0249 / zhtw

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `regional_term, it_term, candidate_gap`

Input:

```text
权限中间件会拒绝缺少作用域的令牌。
```

Expected:

```text
權限中介軟體會拒絕缺少範圍的權杖。
```

Actual:

```text
權限中介軟體會拒絕缺少作用域的權杖。
```

### blind-it-0256 / zhtw

- Domain: `it`
- Risk: `baseline_guard`
- Issue tags: `regional_term, it_term, baseline_guard`

Input:

```text
TLS 握手失败会记录远端地址。
```

Expected:

```text
TLS 握手失敗會記錄遠端位址。
```

Actual:

```text
TLS 握手失敗會記錄遠端地址。
```

### blind-it-0259 / zhtw

- Domain: `it`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, it_term, over_conversion`

Input:

```text
这个 README 已经使用台湾繁体术语。
```

Expected:

```text
這個 README 已經使用台灣繁體術語。
```

Actual:

```text
這個 README 已經使用臺灣繁體術語。
```

### blind-it-0260 / zhtw

- Domain: `it`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, it_term, over_conversion`

Input:

```text
请保留 AzureBlobStorage 这个类名。
```

Expected:

```text
請保留 AzureBlobStorage 這個類別名稱。
```

Actual:

```text
請保留 AzureBlobStorage 這個類名。
```

### blind-ui-0188 / zhtw

- Domain: `ui`
- Risk: `candidate_gap`
- Issue tags: `regional_term, ui_term, candidate_gap`

Input:

```text
设置页面会显示当前账号的安全等级。
```

Expected:

```text
設定頁面會顯示目前帳號的安全等級。
```

Actual:

```text
設定頁面會顯示當前帳號的安全等級。
```

### blind-ui-0193 / zhtw

- Domain: `ui`
- Risk: `candidate_gap`
- Issue tags: `regional_term, ui_term, candidate_gap`

Input:

```text
日期选择器打开后，焦点应停在今天。
```

Expected:

```text
日期選擇器開啟後，焦點應停在今天。
```

Actual:

```text
日期選擇器打開後，焦點應停在今天。
```

### blind-ui-0199 / zhtw

- Domain: `ui`
- Risk: `candidate_gap`
- Issue tags: `regional_term, ui_term, candidate_gap`

Input:

```text
空状态插图下方要显示重新载入按钮。
```

Expected:

```text
空白狀態插圖下方應顯示重新載入按鈕。
```

Actual:

```text
空狀態插圖下方要顯示重新載入按鈕。
```

### blind-ui-0203 / zhtw

- Domain: `ui`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, ui_term, over_conversion`

Input:

```text
按钮标签「取消」已经通过台湾审核。
```

Expected:

```text
按鈕標籤「取消」已經通過台灣審核。
```

Actual:

```text
按鈕標籤「取消」已經透過臺灣審核。
```

### blind-llm-0145 / zhtw

- Domain: `llm`
- Risk: `candidate_gap`
- Issue tags: `regional_term, llm_term, candidate_gap`

Input:

```text
提示模板里的占位符不能被翻译。
```

Expected:

```text
提示範本裡的預留位置不能被翻譯。
```

Actual:

```text
提示範本裡的佔位符不能被翻譯。
```

### blind-formal-0146 / zhtw

- Domain: `formal`
- Risk: `candidate_gap`
- Issue tags: `regional_term, formal_term, candidate_gap`

Input:

```text
统计报告发布前须完成资料校验。
```

Expected:

```text
統計報告發布前須完成資料檢核。
```

Actual:

```text
統計報告發布前須完成資料校驗。
```

### blind-formal-0149 / zhtw

- Domain: `formal`
- Risk: `baseline_guard`
- Issue tags: `regional_term, formal_term, baseline_guard`

Input:

```text
该说明文字只用于内部测试。
```

Expected:

```text
該說明文字僅用於內部測試。
```

Actual:

```text
該說明文字只用於內部測試。
```

### blind-social-0139 / zhtw

- Domain: `social`
- Risk: `candidate_gap`
- Issue tags: `regional_term, social_term, candidate_gap`

Input:

```text
朋友把聚餐地点发到群组里。
```

Expected:

```text
朋友把聚餐地點傳到群組裡。
```

Actual:

```text
朋友把聚餐地點發到群組裡。
```

### blind-social-0143 / zhtw

- Domain: `social`
- Risk: `candidate_gap`
- Issue tags: `regional_term, social_term, candidate_gap`

Input:

```text
明天如果下雨就改约室内。
```

Expected:

```text
明天如果下雨就改約在室內。
```

Actual:

```text
明天如果下雨就改約室內。
```

### blind-high-risk-0097 / zhtw

- Domain: `high_risk`
- Risk: `candidate_gap`
- Issue tags: `regional_term, formal_term, high_risk_term, candidate_gap`

Input:

```text
药品保存温度不得超过标示范围。
```

Expected:

```text
藥品保存溫度不得超過標示範圍。
```

Actual:

```text
藥品保存溫度不得超過標示範围。
```

### blind-high-risk-0121 / zhtw

- Domain: `high_risk`
- Risk: `candidate_gap`
- Issue tags: `regional_term, high_risk_term, candidate_gap`

Input:

```text
医师开具处方前应确认患者过敏史。
```

Expected:

```text
醫師開立處方前應確認病人過敏史。
```

Actual:

```text
醫師開具處方前應確認患者過敏史。
```

### blind-it-0278 / zhtw

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `regional_term, it_term, candidate_gap`

Input:

```text
部署脚本应在失败时返回非零退出码。
```

Expected:

```text
部署腳本應在失敗時回傳非零結束碼。
```

Actual:

```text
部署指令碼應在失敗時返回非零退出碼。
```

### blind-it-0279 / zhtw

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `regional_term, it_term, candidate_gap`

Input:

```text
数据库迁移前必须建立可恢复的备份。
```

Expected:

```text
資料庫移轉前必須建立可還原的備份。
```

Actual:

```text
資料庫遷移前必須建立可恢復的備份。
```

### blind-it-0294 / zhtw

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `regional_term, it_term, candidate_gap`

Input:

```text
事件处理器必须支持重复投递。
```

Expected:

```text
事件處理常式必須支援重複投遞。
```

Actual:

```text
事件處理器必須支持重複投遞。
```

### blind-ui-0227 / zhtw

- Domain: `ui`
- Risk: `candidate_gap`
- Issue tags: `regional_term, ui_term, candidate_gap`

Input:

```text
表单字段错误时将焦点移到第一个问题。
```

Expected:

```text
表單欄位發生錯誤時，將焦點移到第一個錯誤欄位。
```

Actual:

```text
表單欄位錯誤時將焦點移到第一個問題。
```

### blind-llm-0175 / zhtw

- Domain: `llm`
- Risk: `candidate_gap`
- Issue tags: `regional_term, llm_term, candidate_gap`

Input:

```text
批量请求中每个样本都要有唯一标识符。
```

Expected:

```text
批次請求中每個樣本都要有唯一識別碼。
```

Actual:

```text
批次請求中每個樣本都要有唯一識別符號。
```

### blind-llm-0177 / zhtw

- Domain: `llm`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, llm_term, over_conversion_guard`

Input:

```text
代理不得把工具返回的文本当成系统指令。
```

Expected:

```text
代理不得把工具回傳的文字當成系統指令。
```

Actual:

```text
代理不得把工具返回的文字當成系統指令。
```

