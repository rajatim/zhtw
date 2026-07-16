<!-- zhtw:disable -->
# Gemini Vertex Advisory Review：ui-i18n-0051-ui-i18n-0100（2026-07-06）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`
Raw JSON：`docs/reports/annotation-gemini-vertex-advisory-ui-i18n-0051-0100-2026-07-06.json`

## Boundary

- This is Gemini Vertex AI advisory output, not a human review.
- It must not be recorded as `human_first_pass`, `human_adjudication`, or `blind_reviewer`.
- Maintainer review is required before any `review.expected` value becomes promotion-ready.

## Summary

- Model: `gemini-2.5-flash`
- Project: `tw-el-gemini`
- Location: `us-central1`
- Cases: 50
- Exact matches with Codex draft: 29
- Differences from Codex draft: 21

## Maintainer Decision

Maintainer `tim` accepted the Codex review recommendation on 2026-07-06.
The backlog was updated as follows:

- 29 exact-match cases use the shared Codex/Gemini expected output with
  `expected_source = "human_first_pass"`.
- 3 differing cases use the Gemini advisory expected output with
  `expected_source = "human_adjudication"` and `adjudicator = "tim"`.
- 18 differing cases use the Codex expected output with
  `expected_source = "human_adjudication"`, `adjudicator = "tim"`, and Gemini
  advisory recorded as `decision = "rejected"`.
- All 50 cases are now `approved`, promotion-ready, and promoted into
  `regression-v1.json`.

## Historical Maintainer Action

For each case, choose the final Taiwan Traditional expected output. After maintainer approval:

- write the final value to `review.expected`
- set `review.expected_source = "human_first_pass"` when accepting one advisory version unchanged
- set `review.expected_source = "human_adjudication"` and `review.adjudicator = "tim"` when resolving a difference
- keep Gemini under `review.ai_advisory`; do not set it as `blind_reviewer`

## Comparison

### ui-i18n-0051：match

Input:

```text
高对比度模式已启用。
```

Codex draft expected:

```text
高對比模式已啟用。
```

Gemini advisory expected:

```text
高對比模式已啟用。
```

Gemini notes:

```text

```

### ui-i18n-0052：different

Input:

```text
字体大小会影响所有页面。
```

Codex draft expected:

```text
字型大小會影響所有頁面。
```

Gemini advisory expected:

```text
字體大小會影響所有頁面。
```

Gemini notes:

```text

```

### ui-i18n-0053：match

Input:

```text
请调整显示比例。
```

Codex draft expected:

```text
請調整顯示比例。
```

Gemini advisory expected:

```text
請調整顯示比例。
```

Gemini notes:

```text

```

### ui-i18n-0054：match

Input:

```text
全屏模式下隐藏工具栏。
```

Codex draft expected:

```text
全螢幕模式下隱藏工具列。
```

Gemini advisory expected:

```text
全螢幕模式下隱藏工具列。
```

Gemini notes:

```text

```

### ui-i18n-0055：match

Input:

```text
剪贴板内容已复制。
```

Codex draft expected:

```text
剪貼簿內容已複製。
```

Gemini advisory expected:

```text
剪貼簿內容已複製。
```

Gemini notes:

```text

```

### ui-i18n-0056：match

Input:

```text
粘贴前请检查格式。
```

Codex draft expected:

```text
貼上前請檢查格式。
```

Gemini advisory expected:

```text
貼上前請檢查格式。
```

Gemini notes:

```text

```

### ui-i18n-0057：match

Input:

```text
撤销操作不会删除文件。
```

Codex draft expected:

```text
復原操作不會刪除檔案。
```

Gemini advisory expected:

```text
復原操作不會刪除檔案。
```

Gemini notes:

```text

```

### ui-i18n-0058：match

Input:

```text
重做按钮当前不可用。
```

Codex draft expected:

```text
重做按鈕目前無法使用。
```

Gemini advisory expected:

```text
重做按鈕目前無法使用。
```

Gemini notes:

```text

```

### ui-i18n-0059：different

Input:

```text
快捷键冲突需要重新分配。
```

Codex draft expected:

```text
快捷鍵衝突需要重新指派。
```

Gemini advisory expected:

```text
快速鍵衝突需要重新指派。
```

Gemini notes:

```text

```

### ui-i18n-0060：match

Input:

```text
请按住 Shift 进行多选。
```

Codex draft expected:

```text
請按住 Shift 進行多選。
```

Gemini advisory expected:

```text
請按住 Shift 進行多選。
```

Gemini notes:

```text

```

### ui-i18n-0061：different

Input:

```text
拖放文件到上传区域。
```

Codex draft expected:

```text
將檔案拖放到上傳區域。
```

Gemini advisory expected:

```text
拖曳檔案到上傳區域。
```

Gemini notes:

```text

```

### ui-i18n-0062：different

Input:

```text
上传队列正在等待网络连接。
```

Codex draft expected:

```text
上傳佇列正在等待網路連線。
```

Gemini advisory expected:

```text
上傳佇列正在等候網路連線。
```

Gemini notes:

```text

```

### ui-i18n-0063：match

Input:

```text
下载完成后会显示提示。
```

Codex draft expected:

```text
下載完成後會顯示提示。
```

Gemini advisory expected:

```text
下載完成後會顯示提示。
```

Gemini notes:

```text

```

### ui-i18n-0064：different

Input:

```text
附件大小超过限制。
```

Codex draft expected:

```text
附件大小超過限制。
```

Gemini advisory expected:

```text
附件大小超出限制。
```

Gemini notes:

```text

```

### ui-i18n-0065：match

Input:

```text
请选择文件夹位置。
```

Codex draft expected:

```text
請選擇資料夾位置。
```

Gemini advisory expected:

```text
請選擇資料夾位置。
```

Gemini notes:

```text

```

### ui-i18n-0066：different

Input:

```text
文件名包含不支持的字符。
```

Codex draft expected:

```text
檔案名稱包含不支援的字元。
```

Gemini advisory expected:

```text
檔名包含不支援的字元。
```

Gemini notes:

```text

```

### ui-i18n-0067：different

Input:

```text
收藏夹已同步。
```

Codex draft expected:

```text
我的最愛已同步。
```

Gemini advisory expected:

```text
收藏已同步。
```

Gemini notes:

```text

```

### ui-i18n-0068：different

Input:

```text
加入收藏后可离线查看。
```

Codex draft expected:

```text
加入收藏後可離線檢視。
```

Gemini advisory expected:

```text
加入收藏後可離線查看。
```

Gemini notes:

```text

```

### ui-i18n-0069：match

Input:

```text
书签栏可以隐藏。
```

Codex draft expected:

```text
書籤列可以隱藏。
```

Gemini advisory expected:

```text
書籤列可以隱藏。
```

Gemini notes:

```text

```

### ui-i18n-0070：match

Input:

```text
取消星标不会删除项目。
```

Codex draft expected:

```text
取消星號不會刪除項目。
```

Gemini advisory expected:

```text
取消星號不會刪除項目。
```

Gemini notes:

```text

```

### ui-i18n-0071：different

Input:

```text
置顶项目会显示在列表最上方。
```

Codex draft expected:

```text
釘選項目會顯示在清單最上方。
```

Gemini advisory expected:

```text
釘選項目會顯示在列表最上方。
```

Gemini notes:

```text

```

### ui-i18n-0072：different

Input:

```text
归档后的对话可以恢复。
```

Codex draft expected:

```text
封存後的對話可以還原。
```

Gemini advisory expected:

```text
封存後的對話可以復原。
```

Gemini notes:

```text

```

### ui-i18n-0073：match

Input:

```text
请举报不当内容。
```

Codex draft expected:

```text
請檢舉不當內容。
```

Gemini advisory expected:

```text
請檢舉不當內容。
```

Gemini notes:

```text

```

### ui-i18n-0074：match

Input:

```text
屏蔽用户后不会收到消息。
```

Codex draft expected:

```text
封鎖使用者後不會收到訊息。
```

Gemini advisory expected:

```text
封鎖使用者後不會收到訊息。
```

Gemini notes:

```text

```

### ui-i18n-0075：different

Input:

```text
隐私设置会影响个人资料可见性。
```

Codex draft expected:

```text
隱私權設定會影響個人資料可見度。
```

Gemini advisory expected:

```text
隱私設定會影響個人資料可見度。
```

Gemini notes:

```text

```

### ui-i18n-0076：different

Input:

```text
位置权限仅在使用时开启。
```

Codex draft expected:

```text
位置權限僅在使用時開啟。
```

Gemini advisory expected:

```text
定位權限僅在使用時開啟。
```

Gemini notes:

```text

```

### ui-i18n-0077：match

Input:

```text
支付方式需要重新验证。
```

Codex draft expected:

```text
付款方式需要重新驗證。
```

Gemini advisory expected:

```text
付款方式需要重新驗證。
```

Gemini notes:

```text

```

### ui-i18n-0078：match

Input:

```text
发票信息可以在账单页面编辑。
```

Codex draft expected:

```text
發票資訊可以在帳單頁面編輯。
```

Gemini advisory expected:

```text
發票資訊可以在帳單頁面編輯。
```

Gemini notes:

```text

```

### ui-i18n-0079：different

Input:

```text
订阅将在下个月续费。
```

Codex draft expected:

```text
訂閱將在下個月續費。
```

Gemini advisory expected:

```text
訂閱將在下個月續訂。
```

Gemini notes:

```text

```

### ui-i18n-0080：match

Input:

```text
免费试用还剩三天。
```

Codex draft expected:

```text
免費試用還剩三天。
```

Gemini advisory expected:

```text
免費試用還剩三天。
```

Gemini notes:

```text

```

### ui-i18n-0081：match

Input:

```text
购物车中的商品已更新。
```

Codex draft expected:

```text
購物車中的商品已更新。
```

Gemini advisory expected:

```text
購物車中的商品已更新。
```

Gemini notes:

```text

```

### ui-i18n-0082：match

Input:

```text
优惠券代码无效。
```

Codex draft expected:

```text
優惠券代碼無效。
```

Gemini advisory expected:

```text
優惠券代碼無效。
```

Gemini notes:

```text

```

### ui-i18n-0083：different

Input:

```text
配送地址缺少邮政编码。
```

Codex draft expected:

```text
配送地址缺少郵遞區號。
```

Gemini advisory expected:

```text
寄送地址缺少郵遞區號。
```

Gemini notes:

```text

```

### ui-i18n-0084：different

Input:

```text
订单摘要会显示税费。
```

Codex draft expected:

```text
訂單摘要會顯示稅費。
```

Gemini advisory expected:

```text
訂單摘要會顯示稅金。
```

Gemini notes:

```text

```

### ui-i18n-0085：different

Input:

```text
表单提交前会验证必填字段。
```

Codex draft expected:

```text
表單送出前會驗證必填欄位。
```

Gemini advisory expected:

```text
表單提交前會驗證必填欄位。
```

Gemini notes:

```text

```

### ui-i18n-0086：different

Input:

```text
占位符文本不会被提交。
```

Codex draft expected:

```text
預留位置文字不會被送出。
```

Gemini advisory expected:

```text
預留位置文字不會被提交。
```

Gemini notes:

```text

```

### ui-i18n-0087：different

Input:

```text
输入框会自动修剪空格。
```

Codex draft expected:

```text
輸入框會自動修剪空白。
```

Gemini advisory expected:

```text
輸入框會自動修剪空格。
```

Gemini notes:

```text

```

### ui-i18n-0088：match

Input:

```text
错误消息显示在字段下方。
```

Codex draft expected:

```text
錯誤訊息顯示在欄位下方。
```

Gemini advisory expected:

```text
錯誤訊息顯示在欄位下方。
```

Gemini notes:

```text

```

### ui-i18n-0089：match

Input:

```text
验证码已发送到手机。
```

Codex draft expected:

```text
驗證碼已傳送到手機。
```

Gemini advisory expected:

```text
驗證碼已傳送到手機。
```

Gemini notes:

```text

```

### ui-i18n-0090：match

Input:

```text
二维码将在一分钟后失效。
```

Codex draft expected:

```text
QR Code 將在一分鐘後失效。
```

Gemini advisory expected:

```text
QR Code 將在一分鐘後失效。
```

Gemini notes:

```text

```

### ui-i18n-0091：match

Input:

```text
请扫描二维码完成绑定。
```

Codex draft expected:

```text
請掃描 QR Code 完成綁定。
```

Gemini advisory expected:

```text
請掃描 QR Code 完成綁定。
```

Gemini notes:

```text

```

### ui-i18n-0092：match

Input:

```text
绑定成功后会显示绿色勾号。
```

Codex draft expected:

```text
綁定成功後會顯示綠色勾號。
```

Gemini advisory expected:

```text
綁定成功後會顯示綠色勾號。
```

Gemini notes:

```text

```

### ui-i18n-0093：match

Input:

```text
版本更新说明已打开。
```

Codex draft expected:

```text
版本更新說明已開啟。
```

Gemini advisory expected:

```text
版本更新說明已開啟。
```

Gemini notes:

```text

```

### ui-i18n-0094：different

Input:

```text
新功能引导可以跳过。
```

Codex draft expected:

```text
新功能導覽可以略過。
```

Gemini advisory expected:

```text
新功能導覽可以跳過。
```

Gemini notes:

```text

```

### ui-i18n-0095：different

Input:

```text
空状态插图会显示在列表中。
```

Codex draft expected:

```text
空狀態插圖會顯示在清單中。
```

Gemini advisory expected:

```text
空白狀態插圖會顯示在清單中。
```

Gemini notes:

```text

```

### ui-i18n-0096：different

Input:

```text
骨架屏会在数据加载前显示。
```

Codex draft expected:

```text
骨架畫面會在資料載入前顯示。
```

Gemini advisory expected:

```text
骨架螢幕會在資料載入前顯示。
```

Gemini notes:

```text

```

### ui-i18n-0097：match

Input:

```text
分页控件位于表格底部。
```

Codex draft expected:

```text
分頁控制項位於表格底部。
```

Gemini advisory expected:

```text
分頁控制項位於表格底部。
```

Gemini notes:

```text

```

### ui-i18n-0098：match

Input:

```text
表格列宽可以调整。
```

Codex draft expected:

```text
表格欄寬可以調整。
```

Gemini advisory expected:

```text
表格欄寬可以調整。
```

Gemini notes:

```text

```

### ui-i18n-0099：match

Input:

```text
行内编辑会保留原始格式。
```

Codex draft expected:

```text
行內編輯會保留原始格式。
```

Gemini advisory expected:

```text
行內編輯會保留原始格式。
```

Gemini notes:

```text

```

### ui-i18n-0100：match

Input:

```text
本地化字符串缺少翻译。
```

Codex draft expected:

```text
在地化字串缺少翻譯。
```

Gemini advisory expected:

```text
在地化字串缺少翻譯。
```

Gemini notes:

```text

```
