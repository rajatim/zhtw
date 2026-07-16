<!-- zhtw:disable -->
# Gemini Vertex Advisory Review：ui-i18n-0001-ui-i18n-0050（2026-07-06）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`
Raw JSON：`docs/reports/annotation-gemini-vertex-advisory-ui-i18n-0001-0050-2026-07-06.json`

## Boundary

- This is Gemini Vertex AI advisory output, not a human review.
- It must not be recorded as `human_first_pass`, `human_adjudication`, or `blind_reviewer`.
- Maintainer review is required before any `review.expected` value becomes promotion-ready.

## Summary

- Model: `gemini-2.5-flash`
- Project: `tw-el-gemini`
- Location: `us-central1`
- Cases: 50
- Exact matches with Codex draft: 43
- Differences from Codex draft: 7

## Maintainer Decision

Maintainer `tim` accepted the Codex review recommendation on 2026-07-06.
The backlog was updated as follows:

- 43 exact-match cases use the shared Codex/Gemini expected output with
  `expected_source = "human_first_pass"`.
- 1 differing case uses the Gemini advisory expected output with
  `expected_source = "human_adjudication"` and `adjudicator = "tim"`.
- 6 differing cases use the Codex expected output with
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

### ui-i18n-0001：match

Input:

```text
登录页面标题会显示在顶部。
```

Codex draft expected:

```text
登入頁面標題會顯示在頂端。
```

Gemini advisory expected:

```text
登入頁面標題會顯示在頂端。
```

Gemini notes:

```text

```

### ui-i18n-0002：match

Input:

```text
请使用电子邮件地址登录。
```

Codex draft expected:

```text
請使用電子郵件地址登入。
```

Gemini advisory expected:

```text
請使用電子郵件地址登入。
```

Gemini notes:

```text

```

### ui-i18n-0003：match

Input:

```text
忘记密码链接会打开重置页面。
```

Codex draft expected:

```text
忘記密碼連結會開啟重設頁面。
```

Gemini advisory expected:

```text
忘記密碼連結會開啟重設頁面。
```

Gemini notes:

```text

```

### ui-i18n-0004：match

Input:

```text
退出登录后会返回首页。
```

Codex draft expected:

```text
登出後會返回首頁。
```

Gemini advisory expected:

```text
登出後會返回首頁。
```

Gemini notes:

```text

```

### ui-i18n-0005：different

Input:

```text
账户设置保存在云端。
```

Codex draft expected:

```text
帳號設定儲存在雲端。
```

Gemini advisory expected:

```text
帳戶設定儲存在雲端。
```

Gemini notes:

```text

```

### ui-i18n-0006：different

Input:

```text
请更新个人资料中的头像。
```

Codex draft expected:

```text
請更新個人資料中的大頭貼。
```

Gemini advisory expected:

```text
請更新個人資料中的個人頭像。
```

Gemini notes:

```text

```

### ui-i18n-0007：match

Input:

```text
昵称不能为空。
```

Codex draft expected:

```text
暱稱不能為空。
```

Gemini advisory expected:

```text
暱稱不能為空。
```

Gemini notes:

```text

```

### ui-i18n-0008：different

Input:

```text
用户名已经被占用。
```

Codex draft expected:

```text
使用者名稱已被佔用。
```

Gemini advisory expected:

```text
使用者名稱已經被佔用。
```

Gemini notes:

```text

```

### ui-i18n-0009：match

Input:

```text
保存更改前请确认。
```

Codex draft expected:

```text
儲存變更前請確認。
```

Gemini advisory expected:

```text
儲存變更前請確認。
```

Gemini notes:

```text

```

### ui-i18n-0010：match

Input:

```text
更改已保存。
```

Codex draft expected:

```text
變更已儲存。
```

Gemini advisory expected:

```text
變更已儲存。
```

Gemini notes:

```text

```

### ui-i18n-0011：match

Input:

```text
自动保存每分钟运行一次。
```

Codex draft expected:

```text
自動儲存每分鐘執行一次。
```

Gemini advisory expected:

```text
自動儲存每分鐘執行一次。
```

Gemini notes:

```text

```

### ui-i18n-0012：match

Input:

```text
无法保存草稿。
```

Codex draft expected:

```text
無法儲存草稿。
```

Gemini advisory expected:

```text
無法儲存草稿。
```

Gemini notes:

```text

```

### ui-i18n-0013：match

Input:

```text
请刷新列表。
```

Codex draft expected:

```text
請重新整理清單。
```

Gemini advisory expected:

```text
請重新整理清單。
```

Gemini notes:

```text

```

### ui-i18n-0014：match

Input:

```text
下拉刷新已完成。
```

Codex draft expected:

```text
下拉重新整理已完成。
```

Gemini advisory expected:

```text
下拉重新整理已完成。
```

Gemini notes:

```text

```

### ui-i18n-0015：match

Input:

```text
页面正在加载。
```

Codex draft expected:

```text
頁面正在載入。
```

Gemini advisory expected:

```text
頁面正在載入。
```

Gemini notes:

```text

```

### ui-i18n-0016：match

Input:

```text
加载失败，请稍后再试。
```

Codex draft expected:

```text
載入失敗，請稍後再試。
```

Gemini advisory expected:

```text
載入失敗，請稍後再試。
```

Gemini notes:

```text

```

### ui-i18n-0017：match

Input:

```text
默认语言会跟随系统。
```

Codex draft expected:

```text
預設語言會跟隨系統。
```

Gemini advisory expected:

```text
預設語言會跟隨系統。
```

Gemini notes:

```text

```

### ui-i18n-0018：match

Input:

```text
请恢复默认设置。
```

Codex draft expected:

```text
請還原預設設定。
```

Gemini advisory expected:

```text
請還原預設設定。
```

Gemini notes:

```text

```

### ui-i18n-0019：match

Input:

```text
默认排序为最新优先。
```

Codex draft expected:

```text
預設排序為最新優先。
```

Gemini advisory expected:

```text
預設排序為最新優先。
```

Gemini notes:

```text

```

### ui-i18n-0020：match

Input:

```text
当前筛选条件没有结果。
```

Codex draft expected:

```text
目前篩選條件沒有結果。
```

Gemini advisory expected:

```text
目前篩選條件沒有結果。
```

Gemini notes:

```text

```

### ui-i18n-0021：match

Input:

```text
搜索框支持模糊匹配。
```

Codex draft expected:

```text
搜尋框支援模糊比對。
```

Gemini advisory expected:

```text
搜尋框支援模糊比對。
```

Gemini notes:

```text

```

### ui-i18n-0022：different

Input:

```text
清除搜索历史。
```

Codex draft expected:

```text
清除搜尋記錄。
```

Gemini advisory expected:

```text
清除搜尋紀錄。
```

Gemini notes:

```text

```

### ui-i18n-0023：match

Input:

```text
最近搜索会显示在这里。
```

Codex draft expected:

```text
最近搜尋會顯示在這裡。
```

Gemini advisory expected:

```text
最近搜尋會顯示在這裡。
```

Gemini notes:

```text

```

### ui-i18n-0024：match

Input:

```text
请打开高级筛选。
```

Codex draft expected:

```text
請開啟進階篩選。
```

Gemini advisory expected:

```text
請開啟進階篩選。
```

Gemini notes:

```text

```

### ui-i18n-0025：match

Input:

```text
侧边栏可以固定在左侧。
```

Codex draft expected:

```text
側邊欄可以固定在左側。
```

Gemini advisory expected:

```text
側邊欄可以固定在左側。
```

Gemini notes:

```text

```

### ui-i18n-0026：match

Input:

```text
右键菜单包含复制链接。
```

Codex draft expected:

```text
右鍵選單包含複製連結。
```

Gemini advisory expected:

```text
右鍵選單包含複製連結。
```

Gemini notes:

```text

```

### ui-i18n-0027：match

Input:

```text
请从下拉菜单选择地区。
```

Codex draft expected:

```text
請從下拉式選單選擇地區。
```

Gemini advisory expected:

```text
請從下拉式選單選擇地區。
```

Gemini notes:

```text

```

### ui-i18n-0028：different

Input:

```text
这个对话框会阻止背景操作。
```

Codex draft expected:

```text
這個對話方塊會阻止背景操作。
```

Gemini advisory expected:

```text
這個對話方塊會阻擋背景操作。
```

Gemini notes:

```text

```

### ui-i18n-0029：match

Input:

```text
弹窗关闭后不会再次显示。
```

Codex draft expected:

```text
彈出式視窗關閉後不會再次顯示。
```

Gemini advisory expected:

```text
彈出式視窗關閉後不會再次顯示。
```

Gemini notes:

```text

```

### ui-i18n-0030：different

Input:

```text
工具提示会在悬停时显示。
```

Codex draft expected:

```text
工具提示會在游標停留時顯示。
```

Gemini advisory expected:

```text
工具提示會在懸停時顯示。
```

Gemini notes:

```text

```

### ui-i18n-0031：different

Input:

```text
选项卡可以拖动排序。
```

Codex draft expected:

```text
索引標籤可以拖曳排序。
```

Gemini advisory expected:

```text
分頁可以拖曳排序。
```

Gemini notes:

```text

```

### ui-i18n-0032：match

Input:

```text
新标签页会在后台打开。
```

Codex draft expected:

```text
新分頁會在背景開啟。
```

Gemini advisory expected:

```text
新分頁會在背景開啟。
```

Gemini notes:

```text

```

### ui-i18n-0033：match

Input:

```text
面包屑导航显示当前位置。
```

Codex draft expected:

```text
麵包屑導覽顯示目前位置。
```

Gemini advisory expected:

```text
麵包屑導覽顯示目前位置。
```

Gemini notes:

```text

```

### ui-i18n-0034：match

Input:

```text
返回按钮位于左上角。
```

Codex draft expected:

```text
返回按鈕位於左上角。
```

Gemini advisory expected:

```text
返回按鈕位於左上角。
```

Gemini notes:

```text

```

### ui-i18n-0035：match

Input:

```text
请点击确认按钮。
```

Codex draft expected:

```text
請點選確認按鈕。
```

Gemini advisory expected:

```text
請點選確認按鈕。
```

Gemini notes:

```text

```

### ui-i18n-0036：match

Input:

```text
禁用按钮会显示灰色状态。
```

Codex draft expected:

```text
停用按鈕會顯示灰色狀態。
```

Gemini advisory expected:

```text
停用按鈕會顯示灰色狀態。
```

Gemini notes:

```text

```

### ui-i18n-0037：match

Input:

```text
开关关闭时不会发送通知。
```

Codex draft expected:

```text
開關關閉時不會傳送通知。
```

Gemini advisory expected:

```text
開關關閉時不會傳送通知。
```

Gemini notes:

```text

```

### ui-i18n-0038：match

Input:

```text
复选框默认未选中。
```

Codex draft expected:

```text
核取方塊預設未勾選。
```

Gemini advisory expected:

```text
核取方塊預設未勾選。
```

Gemini notes:

```text

```

### ui-i18n-0039：match

Input:

```text
单选按钮只能选择一个。
```

Codex draft expected:

```text
選項按鈕只能選擇一個。
```

Gemini advisory expected:

```text
選項按鈕只能選擇一個。
```

Gemini notes:

```text

```

### ui-i18n-0040：match

Input:

```text
滑块支持键盘调整。
```

Codex draft expected:

```text
滑桿支援鍵盤調整。
```

Gemini advisory expected:

```text
滑桿支援鍵盤調整。
```

Gemini notes:

```text

```

### ui-i18n-0041：match

Input:

```text
进度条显示上传进度。
```

Codex draft expected:

```text
進度列顯示上傳進度。
```

Gemini advisory expected:

```text
進度列顯示上傳進度。
```

Gemini notes:

```text

```

### ui-i18n-0042：match

Input:

```text
状态徽章会显示在标题旁。
```

Codex draft expected:

```text
狀態徽章會顯示在標題旁。
```

Gemini advisory expected:

```text
狀態徽章會顯示在標題旁。
```

Gemini notes:

```text

```

### ui-i18n-0043：match

Input:

```text
未读消息会显示红点。
```

Codex draft expected:

```text
未讀訊息會顯示紅點。
```

Gemini advisory expected:

```text
未讀訊息會顯示紅點。
```

Gemini notes:

```text

```

### ui-i18n-0044：match

Input:

```text
通知中心会保留七天。
```

Codex draft expected:

```text
通知中心會保留七天。
```

Gemini advisory expected:

```text
通知中心會保留七天。
```

Gemini notes:

```text

```

### ui-i18n-0045：match

Input:

```text
推送通知已关闭。
```

Codex draft expected:

```text
推播通知已關閉。
```

Gemini advisory expected:

```text
推播通知已關閉。
```

Gemini notes:

```text

```

### ui-i18n-0046：match

Input:

```text
请允许浏览器通知权限。
```

Codex draft expected:

```text
請允許瀏覽器通知權限。
```

Gemini advisory expected:

```text
請允許瀏覽器通知權限。
```

Gemini notes:

```text

```

### ui-i18n-0047：match

Input:

```text
设备列表会显示上次登录时间。
```

Codex draft expected:

```text
裝置清單會顯示上次登入時間。
```

Gemini advisory expected:

```text
裝置清單會顯示上次登入時間。
```

Gemini notes:

```text

```

### ui-i18n-0048：match

Input:

```text
管理已连接的设备。
```

Codex draft expected:

```text
管理已連線的裝置。
```

Gemini advisory expected:

```text
管理已連線的裝置。
```

Gemini notes:

```text

```

### ui-i18n-0049：match

Input:

```text
触控板手势可以自定义。
```

Codex draft expected:

```text
觸控板手勢可以自訂。
```

Gemini advisory expected:

```text
觸控板手勢可以自訂。
```

Gemini notes:

```text

```

### ui-i18n-0050：match

Input:

```text
屏幕阅读器会朗读标签。
```

Codex draft expected:

```text
螢幕閱讀器會朗讀標籤。
```

Gemini advisory expected:

```text
螢幕閱讀器會朗讀標籤。
```

Gemini notes:

```text

```
