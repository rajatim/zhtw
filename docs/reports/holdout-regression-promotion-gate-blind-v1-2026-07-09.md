<!-- zhtw:disable -->
# Holdout Regression Promotion Gate - blind-v1

Generated: `2026-07-09`

These cases were removed from sealed holdout before tuning. Inputs, expected values, and actual outputs are public in this report.

## Summary

- checked: 22
- promotion_ready: 22
- needs_zhtw_fix: 0
- convert_matches: 22
- convert_mismatches: 0
- expected_idempotent: 22
- expected_not_idempotent: 0
- output_idempotent: 22
- output_not_idempotent: 0

## Promotion Ready

### blind-it-0002

- Promoted id: `holdout/blind-it-0002`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
用户登录后，服务器会返回访问令牌和刷新令牌。
```

Expected:

```text
使用者登入後，伺服器會回傳存取權杖和重新整理權杖。
```

Actual:

```text
使用者登入後，伺服器會回傳存取權杖和重新整理權杖。
```

### blind-it-0005

- Promoted id: `holdout/blind-it-0005`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
这个接口会分页返回订单列表，每页最多五十条。
```

Expected:

```text
這個介面會分頁回傳訂單清單，每頁最多五十筆。
```

Actual:

```text
這個介面會分頁回傳訂單清單，每頁最多五十筆。
```

### blind-it-0006

- Promoted id: `holdout/blind-it-0006`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
当连接超时发生时，请不要重复提交表单。
```

Expected:

```text
當連線逾時發生時，請不要重複送出表單。
```

Actual:

```text
當連線逾時發生時，請不要重複送出表單。
```

### blind-it-0008

- Promoted id: `holdout/blind-it-0008`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
新版 SDK 支持批量上传文件和取消请求。
```

Expected:

```text
新版 SDK 支援批次上傳檔案和取消請求。
```

Actual:

```text
新版 SDK 支援批次上傳檔案和取消請求。
```

### blind-it-0009

- Promoted id: `holdout/blind-it-0009`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
这个命令会覆盖本地设置，请先备份原始文件。
```

Expected:

```text
這個命令會覆寫本機設定，請先備份原始檔案。
```

Actual:

```text
這個命令會覆寫本機設定，請先備份原始檔案。
```

### blind-it-0010

- Promoted id: `holdout/blind-it-0010`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
管理员可以在控制台停用异常的 API 密钥。
```

Expected:

```text
管理員可以在主控台停用異常的 API 金鑰。
```

Actual:

```text
管理員可以在主控台停用異常的 API 金鑰。
```

### blind-it-0015

- Promoted id: `holdout/blind-it-0015`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
你可以用配置文件指定默认语言和时区。
```

Expected:

```text
你可以用設定檔指定預設語言和時區。
```

Actual:

```text
你可以用設定檔指定預設語言和時區。
```

### blind-it-0021

- Promoted id: `holdout/blind-it-0021`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
压缩包解开后，把二进制文件移动到系统路径。
```

Expected:

```text
壓縮檔解壓縮後，把二進位檔案移動到系統路徑。
```

Actual:

```text
壓縮檔解壓縮後，把二進位檔案移動到系統路徑。
```

### blind-it-0023

- Promoted id: `holdout/blind-it-0023`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
任务失败后，调度器会在五分钟后再次尝试。
```

Expected:

```text
任務失敗後，排程器會在五分鐘後再次嘗試。
```

Actual:

```text
任務失敗後，排程器會在五分鐘後再次嘗試。
```

### blind-it-0024

- Promoted id: `holdout/blind-it-0024`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
请确认防火墙允许代理服务器访问内部服务。
```

Expected:

```text
請確認防火牆允許代理伺服器存取內部服務。
```

Actual:

```text
請確認防火牆允許代理伺服器存取內部服務。
```

### blind-it-0025

- Promoted id: `holdout/blind-it-0025`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
如果版本号不匹配，安装程序会停止更新。
```

Expected:

```text
如果版本號不符，安裝程式會停止更新。
```

Actual:

```text
如果版本號不符，安裝程式會停止更新。
```

### blind-ui-0001

- Promoted id: `holdout/blind-ui-0001`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
点击保存后，页面会显示上次更新时间。
```

Expected:

```text
點選儲存後，頁面會顯示上次更新時間。
```

Actual:

```text
點選儲存後，頁面會顯示上次更新時間。
```

### blind-ui-0004

- Promoted id: `holdout/blind-ui-0004`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
拖动滑块调整音量，然后点击应用。
```

Expected:

```text
拖曳滑桿調整音量，然後點選套用。
```

Actual:

```text
拖曳滑桿調整音量，然後點選套用。
```

### blind-ui-0006

- Promoted id: `holdout/blind-ui-0006`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
这个对话框会在离开页面前提醒尚未保存的更改。
```

Expected:

```text
這個對話框會在離開頁面前提醒尚未儲存的變更。
```

Actual:

```text
這個對話框會在離開頁面前提醒尚未儲存的變更。
```

### blind-ui-0009

- Promoted id: `holdout/blind-ui-0009`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
表格支持按创建时间排序和按状态筛选。
```

Expected:

```text
表格支援依建立時間排序和依狀態篩選。
```

Actual:

```text
表格支援依建立時間排序和依狀態篩選。
```

### blind-ui-0019

- Promoted id: `holdout/blind-ui-0019`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
图片上传失败时，缩略图旁边会显示重试图标。
```

Expected:

```text
圖片上傳失敗時，縮圖旁邊會顯示重試圖示。
```

Actual:

```text
圖片上傳失敗時，縮圖旁邊會顯示重試圖示。
```

### blind-ui-0020

- Promoted id: `holdout/blind-ui-0020`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
系统会在会话即将过期时弹出提示。
```

Expected:

```text
系統會在工作階段即將過期時彈出提示。
```

Actual:

```text
系統會在工作階段即將過期時彈出提示。
```

### blind-llm-0010

- Promoted id: `holdout/blind-llm-0010`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
这份教程适合第一次部署服务的开发者。
```

Expected:

```text
這份教學適合第一次部署服務的開發者。
```

Actual:

```text
這份教學適合第一次部署服務的開發者。
```

### blind-llm-0013

- Promoted id: `holdout/blind-llm-0013`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
这条系统消息限制助理不能泄露内部规则。
```

Expected:

```text
這則系統訊息限制助理不能洩漏內部規則。
```

Actual:

```text
這則系統訊息限制助理不能洩漏內部規則。
```

### blind-formal-0003

- Promoted id: `holdout/blind-formal-0003`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
研究团队发现数据来源存在明显偏差。
```

Expected:

```text
研究團隊發現資料來源存在明顯偏差。
```

Actual:

```text
研究團隊發現資料來源存在明顯偏差。
```

### blind-social-0005

- Promoted id: `holdout/blind-social-0005`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
你把照片传给我，我晚点再整理相册。
```

Expected:

```text
你把照片傳給我，我晚點再整理相簿。
```

Actual:

```text
你把照片傳給我，我晚點再整理相簿。
```

### blind-social-0007

- Promoted id: `holdout/blind-social-0007`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
我刚刚在便利店看到同款充电线。
```

Expected:

```text
我剛剛在便利商店看到同款充電線。
```

Actual:

```text
我剛剛在便利商店看到同款充電線。
```
