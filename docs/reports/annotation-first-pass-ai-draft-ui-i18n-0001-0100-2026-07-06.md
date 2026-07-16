<!-- zhtw:disable -->
# Annotation First-Pass AI Draft：ui-i18n 0001-0100（2026-07-06）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`

## Boundary

- This is Codex AI draft only.
- Do not promote these expected values directly.
- Workflow for this batch is Codex draft -> Gemini independent advisory -> maintainer final review.
- Maintainer must choose the final expected value before anything is copied into `review.expected`.
- Do not set `review.expected_source = "human_first_pass"` until maintainer final review accepts a value.

## Cases

### ui-i18n-0001

Input:

```text
登录页面标题会显示在顶部。
```

AI draft expected:

```text
登入頁面標題會顯示在頂端。
```

Notes：登入頁語境：登录→登入、页面→頁面、顶部→頂端。

### ui-i18n-0002

Input:

```text
请使用电子邮件地址登录。
```

AI draft expected:

```text
請使用電子郵件地址登入。
```

Notes：登入表單語境：电子邮件地址→電子郵件地址、登录→登入。

### ui-i18n-0003

Input:

```text
忘记密码链接会打开重置页面。
```

AI draft expected:

```text
忘記密碼連結會開啟重設頁面。
```

Notes：帳號復原語境：链接→連結、打开→開啟、重置→重設。

### ui-i18n-0004

Input:

```text
退出登录后会返回首页。
```

AI draft expected:

```text
登出後會返回首頁。
```

Notes：工作階段語境：退出登录→登出、后→後、首页→首頁。

### ui-i18n-0005

Input:

```text
账户设置保存在云端。
```

AI draft expected:

```text
帳號設定儲存在雲端。
```

Notes：帳號設定語境：账户→帳號、保存→儲存、云端→雲端。

### ui-i18n-0006

Input:

```text
请更新个人资料中的头像。
```

AI draft expected:

```text
請更新個人資料中的大頭貼。
```

Notes：個人資料語境：头像→大頭貼，採台灣常見介面用語。

### ui-i18n-0007

Input:

```text
昵称不能为空。
```

AI draft expected:

```text
暱稱不能為空。
```

Notes：個人資料語境：昵称→暱稱、为空→為空。

### ui-i18n-0008

Input:

```text
用户名已经被占用。
```

AI draft expected:

```text
使用者名稱已被佔用。
```

Notes：帳號註冊語境：用户名→使用者名稱、占用→佔用。

### ui-i18n-0009

Input:

```text
保存更改前请确认。
```

AI draft expected:

```text
儲存變更前請確認。
```

Notes：表單語境：保存→儲存、更改→變更、请→請。

### ui-i18n-0010

Input:

```text
更改已保存。
```

AI draft expected:

```text
變更已儲存。
```

Notes：狀態提示語境：更改→變更、保存→儲存。

### ui-i18n-0011

Input:

```text
自动保存每分钟运行一次。
```

AI draft expected:

```text
自動儲存每分鐘執行一次。
```

Notes：編輯器語境：自动保存→自動儲存、运行→執行。

### ui-i18n-0012

Input:

```text
无法保存草稿。
```

AI draft expected:

```text
無法儲存草稿。
```

Notes：草稿語境：无法→無法、保存→儲存。

### ui-i18n-0013

Input:

```text
请刷新列表。
```

AI draft expected:

```text
請重新整理清單。
```

Notes：清單 UI 語境：刷新→重新整理、列表→清單。

### ui-i18n-0014

Input:

```text
下拉刷新已完成。
```

AI draft expected:

```text
下拉重新整理已完成。
```

Notes：行動 UI 語境：刷新→重新整理。

### ui-i18n-0015

Input:

```text
页面正在加载。
```

AI draft expected:

```text
頁面正在載入。
```

Notes：載入狀態語境：页面→頁面、加载→載入。

### ui-i18n-0016

Input:

```text
加载失败，请稍后再试。
```

AI draft expected:

```text
載入失敗，請稍後再試。
```

Notes：錯誤提示語境：加载→載入、请→請、稍后→稍後。

### ui-i18n-0017

Input:

```text
默认语言会跟随系统。
```

AI draft expected:

```text
預設語言會跟隨系統。
```

Notes：設定語境：默认→預設。

### ui-i18n-0018

Input:

```text
请恢复默认设置。
```

AI draft expected:

```text
請還原預設設定。
```

Notes：設定語境：恢复默认设置→還原預設設定。

### ui-i18n-0019

Input:

```text
默认排序为最新优先。
```

AI draft expected:

```text
預設排序為最新優先。
```

Notes：排序語境：默认→預設、为→為、优先→優先。

### ui-i18n-0020

Input:

```text
当前筛选条件没有结果。
```

AI draft expected:

```text
目前篩選條件沒有結果。
```

Notes：篩選語境：当前→目前、筛选→篩選。

### ui-i18n-0021

Input:

```text
搜索框支持模糊匹配。
```

AI draft expected:

```text
搜尋框支援模糊比對。
```

Notes：搜尋語境：搜索→搜尋、支持→支援、匹配→比對。

### ui-i18n-0022

Input:

```text
清除搜索历史。
```

AI draft expected:

```text
清除搜尋記錄。
```

Notes：搜尋語境：搜索历史→搜尋記錄。

### ui-i18n-0023

Input:

```text
最近搜索会显示在这里。
```

AI draft expected:

```text
最近搜尋會顯示在這裡。
```

Notes：搜尋語境：搜索→搜尋、这里→這裡。

### ui-i18n-0024

Input:

```text
请打开高级筛选。
```

AI draft expected:

```text
請開啟進階篩選。
```

Notes：篩選語境：打开→開啟、高级→進階、筛选→篩選。

### ui-i18n-0025

Input:

```text
侧边栏可以固定在左侧。
```

AI draft expected:

```text
側邊欄可以固定在左側。
```

Notes：版面語境：侧边栏→側邊欄、左侧→左側。

### ui-i18n-0026

Input:

```text
右键菜单包含复制链接。
```

AI draft expected:

```text
右鍵選單包含複製連結。
```

Notes：選單語境：菜单→選單、复制→複製、链接→連結。

### ui-i18n-0027

Input:

```text
请从下拉菜单选择地区。
```

AI draft expected:

```text
請從下拉式選單選擇地區。
```

Notes：選單語境：下拉菜单→下拉式選單、选择→選擇。

### ui-i18n-0028

Input:

```text
这个对话框会阻止背景操作。
```

AI draft expected:

```text
這個對話方塊會阻止背景操作。
```

Notes：對話框語境：对话框→對話方塊、这个→這個。

### ui-i18n-0029

Input:

```text
弹窗关闭后不会再次显示。
```

AI draft expected:

```text
彈出式視窗關閉後不會再次顯示。
```

Notes：彈窗語境：弹窗→彈出式視窗、关闭→關閉、后→後。

### ui-i18n-0030

Input:

```text
工具提示会在悬停时显示。
```

AI draft expected:

```text
工具提示會在游標停留時顯示。
```

Notes：提示語境：悬停→游標停留，避免直譯成懸停。

### ui-i18n-0031

Input:

```text
选项卡可以拖动排序。
```

AI draft expected:

```text
索引標籤可以拖曳排序。
```

Notes：分頁控制語境：选项卡→索引標籤、拖动→拖曳。

### ui-i18n-0032

Input:

```text
新标签页会在后台打开。
```

AI draft expected:

```text
新分頁會在背景開啟。
```

Notes：瀏覽器語境：标签页→分頁、后台→背景、打开→開啟。

### ui-i18n-0033

Input:

```text
面包屑导航显示当前位置。
```

AI draft expected:

```text
麵包屑導覽顯示目前位置。
```

Notes：導覽語境：面包屑导航→麵包屑導覽、当前→目前。

### ui-i18n-0034

Input:

```text
返回按钮位于左上角。
```

AI draft expected:

```text
返回按鈕位於左上角。
```

Notes：按鈕語境：按钮→按鈕、位于→位於。

### ui-i18n-0035

Input:

```text
请点击确认按钮。
```

AI draft expected:

```text
請點選確認按鈕。
```

Notes：按鈕操作語境：点击→點選、按钮→按鈕。

### ui-i18n-0036

Input:

```text
禁用按钮会显示灰色状态。
```

AI draft expected:

```text
停用按鈕會顯示灰色狀態。
```

Notes：控制項語境：禁用→停用、按钮→按鈕、状态→狀態。

### ui-i18n-0037

Input:

```text
开关关闭时不会发送通知。
```

AI draft expected:

```text
開關關閉時不會傳送通知。
```

Notes：設定開關語境：发送→傳送。

### ui-i18n-0038

Input:

```text
复选框默认未选中。
```

AI draft expected:

```text
核取方塊預設未勾選。
```

Notes：表單控制項語境：复选框→核取方塊、默认→預設、选中→勾選。

### ui-i18n-0039

Input:

```text
单选按钮只能选择一个。
```

AI draft expected:

```text
選項按鈕只能選擇一個。
```

Notes：表單控制項語境：单选按钮→選項按鈕、选择→選擇。

### ui-i18n-0040

Input:

```text
滑块支持键盘调整。
```

AI draft expected:

```text
滑桿支援鍵盤調整。
```

Notes：控制項語境：滑块→滑桿、支持→支援。

### ui-i18n-0041

Input:

```text
进度条显示上传进度。
```

AI draft expected:

```text
進度列顯示上傳進度。
```

Notes：狀態控制項語境：进度条→進度列、上传→上傳。

### ui-i18n-0042

Input:

```text
状态徽章会显示在标题旁。
```

AI draft expected:

```text
狀態徽章會顯示在標題旁。
```

Notes：狀態 UI 語境：状态→狀態、标题→標題。

### ui-i18n-0043

Input:

```text
未读消息会显示红点。
```

AI draft expected:

```text
未讀訊息會顯示紅點。
```

Notes：通知語境：未读→未讀、消息→訊息、红点→紅點。

### ui-i18n-0044

Input:

```text
通知中心会保留七天。
```

AI draft expected:

```text
通知中心會保留七天。
```

Notes：通知中心語境：基本簡繁轉換，保留產品用語。

### ui-i18n-0045

Input:

```text
推送通知已关闭。
```

AI draft expected:

```text
推播通知已關閉。
```

Notes：通知語境：推送通知→推播通知、关闭→關閉。

### ui-i18n-0046

Input:

```text
请允许浏览器通知权限。
```

AI draft expected:

```text
請允許瀏覽器通知權限。
```

Notes：權限提示語境：请→請、权限→權限。

### ui-i18n-0047

Input:

```text
设备列表会显示上次登录时间。
```

AI draft expected:

```text
裝置清單會顯示上次登入時間。
```

Notes：裝置管理語境：设备→裝置、列表→清單、登录→登入。

### ui-i18n-0048

Input:

```text
管理已连接的设备。
```

AI draft expected:

```text
管理已連線的裝置。
```

Notes：裝置管理語境：连接→連線、设备→裝置。

### ui-i18n-0049

Input:

```text
触控板手势可以自定义。
```

AI draft expected:

```text
觸控板手勢可以自訂。
```

Notes：裝置設定語境：触控板→觸控板、自定义→自訂。

### ui-i18n-0050

Input:

```text
屏幕阅读器会朗读标签。
```

AI draft expected:

```text
螢幕閱讀器會朗讀標籤。
```

Notes：無障礙語境：屏幕阅读器→螢幕閱讀器、标签→標籤。

### ui-i18n-0051

Input:

```text
高对比度模式已启用。
```

AI draft expected:

```text
高對比模式已啟用。
```

Notes：無障礙語境：高对比度模式→高對比模式、启用→啟用。

### ui-i18n-0052

Input:

```text
字体大小会影响所有页面。
```

AI draft expected:

```text
字型大小會影響所有頁面。
```

Notes：顯示設定語境：字体→字型、页面→頁面。

### ui-i18n-0053

Input:

```text
请调整显示比例。
```

AI draft expected:

```text
請調整顯示比例。
```

Notes：顯示設定語境：请→請、调整→調整。

### ui-i18n-0054

Input:

```text
全屏模式下隐藏工具栏。
```

AI draft expected:

```text
全螢幕模式下隱藏工具列。
```

Notes：顯示語境：全屏→全螢幕、隐藏→隱藏、工具栏→工具列。

### ui-i18n-0055

Input:

```text
剪贴板内容已复制。
```

AI draft expected:

```text
剪貼簿內容已複製。
```

Notes：編輯操作語境：剪贴板→剪貼簿、复制→複製。

### ui-i18n-0056

Input:

```text
粘贴前请检查格式。
```

AI draft expected:

```text
貼上前請檢查格式。
```

Notes：編輯操作語境：粘贴→貼上、请→請。

### ui-i18n-0057

Input:

```text
撤销操作不会删除文件。
```

AI draft expected:

```text
復原操作不會刪除檔案。
```

Notes：編輯操作語境：撤销→復原、文件→檔案。

### ui-i18n-0058

Input:

```text
重做按钮当前不可用。
```

AI draft expected:

```text
重做按鈕目前無法使用。
```

Notes：編輯操作語境：按钮→按鈕、当前→目前、不可用→無法使用。

### ui-i18n-0059

Input:

```text
快捷键冲突需要重新分配。
```

AI draft expected:

```text
快捷鍵衝突需要重新指派。
```

Notes：快捷鍵設定語境：冲突→衝突、分配→指派。

### ui-i18n-0060

Input:

```text
请按住 Shift 进行多选。
```

AI draft expected:

```text
請按住 Shift 進行多選。
```

Notes：多選操作語境：请→請、进行→進行。

### ui-i18n-0061

Input:

```text
拖放文件到上传区域。
```

AI draft expected:

```text
將檔案拖放到上傳區域。
```

Notes：上傳語境：文件→檔案、上传→上傳，補出自然的將字句。

### ui-i18n-0062

Input:

```text
上传队列正在等待网络连接。
```

AI draft expected:

```text
上傳佇列正在等待網路連線。
```

Notes：上傳語境：队列→佇列、网络连接→網路連線。

### ui-i18n-0063

Input:

```text
下载完成后会显示提示。
```

AI draft expected:

```text
下載完成後會顯示提示。
```

Notes：下載語境：下载→下載、后→後。

### ui-i18n-0064

Input:

```text
附件大小超过限制。
```

AI draft expected:

```text
附件大小超過限制。
```

Notes：附件語境：超过→超過。

### ui-i18n-0065

Input:

```text
请选择文件夹位置。
```

AI draft expected:

```text
請選擇資料夾位置。
```

Notes：檔案選擇語境：文件夹→資料夾、选择→選擇。

### ui-i18n-0066

Input:

```text
文件名包含不支持的字符。
```

AI draft expected:

```text
檔案名稱包含不支援的字元。
```

Notes：檔案命名語境：文件名→檔案名稱、支持→支援、字符→字元。

### ui-i18n-0067

Input:

```text
收藏夹已同步。
```

AI draft expected:

```text
我的最愛已同步。
```

Notes：瀏覽器/清單語境：收藏夹→我的最愛。

### ui-i18n-0068

Input:

```text
加入收藏后可离线查看。
```

AI draft expected:

```text
加入收藏後可離線檢視。
```

Notes：收藏語境：后→後、离线→離線、查看→檢視。

### ui-i18n-0069

Input:

```text
书签栏可以隐藏。
```

AI draft expected:

```text
書籤列可以隱藏。
```

Notes：瀏覽器語境：书签栏→書籤列、隐藏→隱藏。

### ui-i18n-0070

Input:

```text
取消星标不会删除项目。
```

AI draft expected:

```text
取消星號不會刪除項目。
```

Notes：收藏狀態語境：星标→星號、删除→刪除。

### ui-i18n-0071

Input:

```text
置顶项目会显示在列表最上方。
```

AI draft expected:

```text
釘選項目會顯示在清單最上方。
```

Notes：清單操作語境：置顶→釘選、列表→清單。

### ui-i18n-0072

Input:

```text
归档后的对话可以恢复。
```

AI draft expected:

```text
封存後的對話可以還原。
```

Notes：訊息 UI 語境：归档→封存、恢复→還原。

### ui-i18n-0073

Input:

```text
请举报不当内容。
```

AI draft expected:

```text
請檢舉不當內容。
```

Notes：社群安全語境：举报→檢舉、不当→不當。

### ui-i18n-0074

Input:

```text
屏蔽用户后不会收到消息。
```

AI draft expected:

```text
封鎖使用者後不會收到訊息。
```

Notes：社群安全語境：屏蔽用户→封鎖使用者、消息→訊息。

### ui-i18n-0075

Input:

```text
隐私设置会影响个人资料可见性。
```

AI draft expected:

```text
隱私權設定會影響個人資料可見度。
```

Notes：隱私語境：隐私设置→隱私權設定、可见性→可見度。

### ui-i18n-0076

Input:

```text
位置权限仅在使用时开启。
```

AI draft expected:

```text
位置權限僅在使用時開啟。
```

Notes：權限語境：权限→權限、仅→僅、开启→開啟。

### ui-i18n-0077

Input:

```text
支付方式需要重新验证。
```

AI draft expected:

```text
付款方式需要重新驗證。
```

Notes：付款 UI 語境：支付方式→付款方式、验证→驗證。

### ui-i18n-0078

Input:

```text
发票信息可以在账单页面编辑。
```

AI draft expected:

```text
發票資訊可以在帳單頁面編輯。
```

Notes：帳務語境：信息→資訊、账单→帳單、页面→頁面。

### ui-i18n-0079

Input:

```text
订阅将在下个月续费。
```

AI draft expected:

```text
訂閱將在下個月續費。
```

Notes：訂閱語境：订阅→訂閱、续费→續費。

### ui-i18n-0080

Input:

```text
免费试用还剩三天。
```

AI draft expected:

```text
免費試用還剩三天。
```

Notes：訂閱語境：免费→免費、试用→試用。

### ui-i18n-0081

Input:

```text
购物车中的商品已更新。
```

AI draft expected:

```text
購物車中的商品已更新。
```

Notes：電商語境：购物车→購物車。

### ui-i18n-0082

Input:

```text
优惠券代码无效。
```

AI draft expected:

```text
優惠券代碼無效。
```

Notes：電商語境：优惠券代码→優惠券代碼、无效→無效。

### ui-i18n-0083

Input:

```text
配送地址缺少邮政编码。
```

AI draft expected:

```text
配送地址缺少郵遞區號。
```

Notes：地址語境：邮政编码→郵遞區號。

### ui-i18n-0084

Input:

```text
订单摘要会显示税费。
```

AI draft expected:

```text
訂單摘要會顯示稅費。
```

Notes：結帳語境：订单→訂單、税费→稅費。

### ui-i18n-0085

Input:

```text
表单提交前会验证必填字段。
```

AI draft expected:

```text
表單送出前會驗證必填欄位。
```

Notes：表單語境：提交→送出、字段→欄位。

### ui-i18n-0086

Input:

```text
占位符文本不会被提交。
```

AI draft expected:

```text
預留位置文字不會被送出。
```

Notes：表單語境：占位符文本→預留位置文字、提交→送出。

### ui-i18n-0087

Input:

```text
输入框会自动修剪空格。
```

AI draft expected:

```text
輸入框會自動修剪空白。
```

Notes：表單語境：输入框→輸入框、空格→空白。

### ui-i18n-0088

Input:

```text
错误消息显示在字段下方。
```

AI draft expected:

```text
錯誤訊息顯示在欄位下方。
```

Notes：表單錯誤語境：错误消息→錯誤訊息、字段→欄位。

### ui-i18n-0089

Input:

```text
验证码已发送到手机。
```

AI draft expected:

```text
驗證碼已傳送到手機。
```

Notes：驗證流程語境：发送→傳送、手机→手機。

### ui-i18n-0090

Input:

```text
二维码将在一分钟后失效。
```

AI draft expected:

```text
QR Code 將在一分鐘後失效。
```

Notes：驗證流程語境：二维码→QR Code，保留台灣常見產品寫法。

### ui-i18n-0091

Input:

```text
请扫描二维码完成绑定。
```

AI draft expected:

```text
請掃描 QR Code 完成綁定。
```

Notes：綁定流程語境：二维码→QR Code、绑定→綁定。

### ui-i18n-0092

Input:

```text
绑定成功后会显示绿色勾号。
```

AI draft expected:

```text
綁定成功後會顯示綠色勾號。
```

Notes：狀態提示語境：绑定→綁定、后→後、勾号→勾號。

### ui-i18n-0093

Input:

```text
版本更新说明已打开。
```

AI draft expected:

```text
版本更新說明已開啟。
```

Notes：版本資訊語境：说明→說明、打开→開啟。

### ui-i18n-0094

Input:

```text
新功能引导可以跳过。
```

AI draft expected:

```text
新功能導覽可以略過。
```

Notes：導覽語境：引导→導覽、跳过→略過。

### ui-i18n-0095

Input:

```text
空状态插图会显示在列表中。
```

AI draft expected:

```text
空狀態插圖會顯示在清單中。
```

Notes：空狀態 UI 語境：状态→狀態、列表→清單。

### ui-i18n-0096

Input:

```text
骨架屏会在数据加载前显示。
```

AI draft expected:

```text
骨架畫面會在資料載入前顯示。
```

Notes：載入 UI 語境：骨架屏→骨架畫面、数据→資料、加载→載入。

### ui-i18n-0097

Input:

```text
分页控件位于表格底部。
```

AI draft expected:

```text
分頁控制項位於表格底部。
```

Notes：表格 UI 語境：分页控件→分頁控制項、位于→位於。

### ui-i18n-0098

Input:

```text
表格列宽可以调整。
```

AI draft expected:

```text
表格欄寬可以調整。
```

Notes：表格 UI 語境：列宽→欄寬、调整→調整。

### ui-i18n-0099

Input:

```text
行内编辑会保留原始格式。
```

AI draft expected:

```text
行內編輯會保留原始格式。
```

Notes：表格編輯語境：行内→行內。

### ui-i18n-0100

Input:

```text
本地化字符串缺少翻译。
```

AI draft expected:

```text
在地化字串缺少翻譯。
```

Notes：i18n 語境：本地化→在地化、字符串→字串、翻译→翻譯。
