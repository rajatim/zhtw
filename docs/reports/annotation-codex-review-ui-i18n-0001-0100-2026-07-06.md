<!-- zhtw:disable -->
# Codex Review：ui-i18n 0001-0100（2026-07-06）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`

## Boundary

- This is Codex review of Codex-vs-Gemini advisory differences only.
- It is not maintainer final review.
- Do not promote these recommendations directly.
- Maintainer must choose the final expected value before `review.expected` is populated.

## Summary

- Cases reviewed: 100
- Codex/Gemini exact matches: 72
- Differences needing maintainer decision: 28
- Codex recommendation: 24
- Gemini recommendation: 4

## Maintainer Decision

Maintainer `tim` accepted this Codex review recommendation on 2026-07-06.
The backlog was updated as follows:

- 72 exact-match cases use the shared Codex/Gemini expected output with
  `expected_source = "human_first_pass"`.
- 4 differing cases use the Gemini advisory expected output with
  `expected_source = "human_adjudication"` and `adjudicator = "tim"`.
- 24 differing cases use the Codex expected output with
  `expected_source = "human_adjudication"`, `adjudicator = "tim"`, and Gemini
  advisory recorded as `decision = "rejected"`.
- All 100 cases are now `approved`, promotion-ready, and promoted into
  `regression-v1.json`.

## Recommended Decisions

| ID | Input | Codex | Gemini | Codex recommendation | Reason |
|----|-------|-------|--------|----------------------|--------|
| ui-i18n-0005 | 账户设置保存在云端。 | 帳號設定儲存在雲端。 | 帳戶設定儲存在雲端。 | Codex | UI 帳號設定較常見，且和登入/使用者名稱語境一致。 |
| ui-i18n-0006 | 请更新个人资料中的头像。 | 請更新個人資料中的大頭貼。 | 請更新個人資料中的個人頭像。 | Codex | `個人頭像` 冗餘；消費者 UI 中 `大頭貼` 較自然。 |
| ui-i18n-0008 | 用户名已经被占用。 | 使用者名稱已被佔用。 | 使用者名稱已經被佔用。 | Codex | UI 錯誤訊息保留簡潔語氣較好。 |
| ui-i18n-0022 | 清除搜索历史。 | 清除搜尋記錄。 | 清除搜尋紀錄。 | Gemini | `搜尋紀錄` 作為 history noun 較自然。 |
| ui-i18n-0028 | 这个对话框会阻止背景操作。 | 這個對話方塊會阻止背景操作。 | 這個對話方塊會阻擋背景操作。 | Codex | 對話方塊阻止操作是抽象行為，`阻止` 較準。 |
| ui-i18n-0030 | 工具提示会在悬停时显示。 | 工具提示會在游標停留時顯示。 | 工具提示會在懸停時顯示。 | Codex | `懸停` 不是常見台灣 UI 用語。 |
| ui-i18n-0031 | 选项卡可以拖动排序。 | 索引標籤可以拖曳排序。 | 分頁可以拖曳排序。 | Codex | `选项卡` 對應 UI control 的 `索引標籤`，不同於 browser `标签页`。 |
| ui-i18n-0052 | 字体大小会影响所有页面。 | 字型大小會影響所有頁面。 | 字體大小會影響所有頁面。 | Codex | 軟體設定中 `字型大小` 較穩定。 |
| ui-i18n-0059 | 快捷键冲突需要重新分配。 | 快捷鍵衝突需要重新指派。 | 快速鍵衝突需要重新指派。 | Gemini | 台灣 UI 較常用 `快速鍵`。 |
| ui-i18n-0061 | 拖放文件到上传区域。 | 將檔案拖放到上傳區域。 | 拖曳檔案到上傳區域。 | Codex | `拖放` 同時保留 drag/drop 語意。 |
| ui-i18n-0062 | 上传队列正在等待网络连接。 | 上傳佇列正在等待網路連線。 | 上傳佇列正在等候網路連線。 | Codex | `等待網路連線` 是自然 UI 狀態句。 |
| ui-i18n-0064 | 附件大小超过限制。 | 附件大小超過限制。 | 附件大小超出限制。 | Codex | `超過限制` 較常見。 |
| ui-i18n-0066 | 文件名包含不支持的字符。 | 檔案名稱包含不支援的字元。 | 檔名包含不支援的字元。 | Gemini | UI 錯誤訊息中 `檔名` 較精簡自然。 |
| ui-i18n-0067 | 收藏夹已同步。 | 我的最愛已同步。 | 收藏已同步。 | Codex | `收藏夹` 不應弱化成泛稱 `收藏`。 |
| ui-i18n-0068 | 加入收藏后可离线查看。 | 加入收藏後可離線檢視。 | 加入收藏後可離線查看。 | Codex | 介面動作中 `檢視` 較穩定。 |
| ui-i18n-0071 | 置顶项目会显示在列表最上方。 | 釘選項目會顯示在清單最上方。 | 釘選項目會顯示在列表最上方。 | Codex | `列表` 應轉台灣 UI 常用 `清單`。 |
| ui-i18n-0072 | 归档后的对话可以恢复。 | 封存後的對話可以還原。 | 封存後的對話可以復原。 | Codex | 從封存狀態移回原處用 `還原` 較準。 |
| ui-i18n-0075 | 隐私设置会影响个人资料可见性。 | 隱私權設定會影響個人資料可見度。 | 隱私設定會影響個人資料可見度。 | Codex | 台灣產品與法規語境多用 `隱私權`。 |
| ui-i18n-0076 | 位置权限仅在使用时开启。 | 位置權限僅在使用時開啟。 | 定位權限僅在使用時開啟。 | Codex | Source 是 `位置权限`，且手機權限也常稱 `位置權限`。 |
| ui-i18n-0079 | 订阅将在下个月续费。 | 訂閱將在下個月續費。 | 訂閱將在下個月續訂。 | Codex | 句子指付款續費，不只是續訂服務。 |
| ui-i18n-0083 | 配送地址缺少邮政编码。 | 配送地址缺少郵遞區號。 | 寄送地址缺少郵遞區號。 | Gemini | 結帳 UI 中 `寄送地址` 較自然。 |
| ui-i18n-0084 | 订单摘要会显示税费。 | 訂單摘要會顯示稅費。 | 訂單摘要會顯示稅金。 | Codex | `税费` 包含 tax/fees，`稅金` 範圍較窄。 |
| ui-i18n-0085 | 表单提交前会验证必填字段。 | 表單送出前會驗證必填欄位。 | 表單提交前會驗證必填欄位。 | Codex | 台灣 UI 表單動作較常用 `送出`。 |
| ui-i18n-0086 | 占位符文本不会被提交。 | 預留位置文字不會被送出。 | 預留位置文字不會被提交。 | Codex | 與表單 UI `送出` 用語一致。 |
| ui-i18n-0087 | 输入框会自动修剪空格。 | 輸入框會自動修剪空白。 | 輸入框會自動修剪空格。 | Codex | 技術 UI 中 trim whitespace 對應 `空白` 較完整。 |
| ui-i18n-0094 | 新功能引导可以跳过。 | 新功能導覽可以略過。 | 新功能導覽可以跳過。 | Codex | 台灣 onboarding UI 常用 `略過`。 |
| ui-i18n-0095 | 空状态插图会显示在列表中。 | 空狀態插圖會顯示在清單中。 | 空白狀態插圖會顯示在清單中。 | Codex | 設計系統術語 `空狀態` 可保留，且 source 是 `空状态`。 |
| ui-i18n-0096 | 骨架屏会在数据加载前显示。 | 骨架畫面會在資料載入前顯示。 | 骨架螢幕會在資料載入前顯示。 | Codex | `screen` 在此是 UI 畫面，不是實體螢幕。 |
