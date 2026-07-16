<!-- zhtw:disable -->
# Annotation First-Pass AI Draft：ui-i18n 0101-0125（2026-07-06）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`

## Boundary

- This is Codex AI draft only.
- Do not promote these expected values directly.
- Workflow for this batch is Codex draft -> Gemini independent advisory -> maintainer final review.
- Maintainer must choose the final expected value before anything is copied into `review.expected`.
- Do not set `review.expected_source = "human_first_pass"` until maintainer final review accepts a value.

## Cases

### ui-i18n-0101

Input:

```text
语言包下载完成。
```

AI draft expected:

```text
語言套件下載完成。
```

Notes：i18n 語境：语言包→語言套件、下载→下載。

### ui-i18n-0102

Input:

```text
当前区域设置使用繁体中文。
```

AI draft expected:

```text
目前地區設定使用繁體中文。
```

Notes：地區設定語境：当前→目前、区域设置→地區設定。

### ui-i18n-0103

Input:

```text
日期格式会根据地区变化。
```

AI draft expected:

```text
日期格式會根據地區變化。
```

Notes：地區格式語境：地区→地區、变化→變化。

### ui-i18n-0104

Input:

```text
请将时区设置为台北。
```

AI draft expected:

```text
請將時區設定為台北。
```

Notes：地區設定語境：时区→時區、设置→設定。

### ui-i18n-0105

Input:

```text
数字分组符号可以自定义。
```

AI draft expected:

```text
數字分組符號可以自訂。
```

Notes：格式設定語境：数字→數字、自定义→自訂。

### ui-i18n-0106

Input:

```text
货币符号显示在金额前。
```

AI draft expected:

```text
貨幣符號顯示在金額前。
```

Notes：貨幣格式語境：货币→貨幣、金额→金額。

### ui-i18n-0107

Input:

```text
翻译缺失时会回退到默认语言。
```

AI draft expected:

```text
翻譯缺漏時會改用預設語言。
```

Notes：fallback 語境：缺失→缺漏、回退到→改用、默认语言→預設語言。

### ui-i18n-0108

Input:

```text
字符串键不能重复。
```

AI draft expected:

```text
字串鍵不能重複。
```

Notes：i18n key 語境：字符串→字串、键→鍵、重复→重複。

### ui-i18n-0109

Input:

```text
请为每个语言添加说明。
```

AI draft expected:

```text
請為每種語言新增說明。
```

Notes：語言管理語境：每个→每種、添加→新增。

### ui-i18n-0110

Input:

```text
导入翻译文件前请预览差异。
```

AI draft expected:

```text
匯入翻譯檔前請預覽差異。
```

Notes：翻譯檔語境：导入→匯入、文件→檔、请→請。

### ui-i18n-0111

Input:

```text
导出文件会包含未翻译项目。
```

AI draft expected:

```text
匯出檔案會包含未翻譯項目。
```

Notes：翻譯檔語境：导出→匯出、文件→檔案、项目→項目。

### ui-i18n-0112

Input:

```text
占位符名称必须保持一致。
```

AI draft expected:

```text
預留位置名稱必須保持一致。
```

Notes：placeholder 語境：占位符→預留位置、名称→名稱、必须→必須。

### ui-i18n-0113

Input:

```text
请不要翻译变量名。
```

AI draft expected:

```text
請不要翻譯變數名稱。
```

Notes：變數語境：变量名→變數名稱、请→請。

### ui-i18n-0114

Input:

```text
文本方向会影响布局。
```

AI draft expected:

```text
文字方向會影響版面配置。
```

Notes：版面語境：文本→文字、布局→版面配置。

### ui-i18n-0115

Input:

```text
从右到左语言需要镜像图标。
```

AI draft expected:

```text
從右到左語言需要鏡像圖示。
```

Notes：RTL 語境：从→從、镜像→鏡像、图标→圖示。

### ui-i18n-0116

Input:

```text
语言切换后页面会重新加载。
```

AI draft expected:

```text
語言切換後頁面會重新載入。
```

Notes：語言切換語境：后→後、页面→頁面、加载→載入。

### ui-i18n-0117

Input:

```text
预览模式不会保存更改。
```

AI draft expected:

```text
預覽模式不會儲存變更。
```

Notes：預覽語境：保存→儲存、更改→變更。

### ui-i18n-0118

Input:

```text
文案长度超过按钮宽度。
```

AI draft expected:

```text
文案長度超過按鈕寬度。
```

Notes：UI 文案語境：长度→長度、超过→超過、按钮→按鈕。

### ui-i18n-0119

Input:

```text
请检查换行是否正确。
```

AI draft expected:

```text
請檢查換行是否正確。
```

Notes：文字排版語境：请→請、正确→正確。

### ui-i18n-0120

Input:

```text
空白字符会被保留。
```

AI draft expected:

```text
空白字元會被保留。
```

Notes：文字處理語境：字符→字元。

### ui-i18n-0121

Input:

```text
本地缓存会存储最近使用的语言。
```

AI draft expected:

```text
本機快取會儲存最近使用的語言。
```

Notes：本機設定語境：本地缓存→本機快取、存储→儲存。

### ui-i18n-0122

Input:

```text
搜索翻译键时忽略大小写。
```

AI draft expected:

```text
搜尋翻譯鍵時忽略大小寫。
```

Notes：搜尋語境：搜索→搜尋、键→鍵。

### ui-i18n-0123

Input:

```text
批量更新会覆盖人工翻译。
```

AI draft expected:

```text
批次更新會覆寫人工翻譯。
```

Notes：批次操作語境：批量→批次、覆盖→覆寫。

### ui-i18n-0124

Input:

```text
审核状态会显示在翻译列表。
```

AI draft expected:

```text
審核狀態會顯示在翻譯清單。
```

Notes：翻譯清單語境：审核状态→審核狀態、列表→清單。

### ui-i18n-0125

Input:

```text
请在发布前锁定语言版本。
```

AI draft expected:

```text
請在發佈前鎖定語言版本。
```

Notes：發布流程語境：发布→發佈、锁定→鎖定。
