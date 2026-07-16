<!-- zhtw:disable -->
# Gemini Vertex Advisory Review：ui-i18n-0101-ui-i18n-0125（2026-07-06）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`
Raw JSON：`docs/reports/annotation-gemini-vertex-advisory-ui-i18n-0101-0125-2026-07-06.json`

## Boundary

- This is Gemini Vertex AI advisory output, not a human review.
- It must not be recorded as `human_first_pass`, `human_adjudication`, or `blind_reviewer`.
- Maintainer review is required before any `review.expected` value becomes promotion-ready.

## Summary

- Model: `gemini-2.5-flash`
- Project: `tw-el-gemini`
- Location: `us-central1`
- Cases: 25
- Exact matches with Codex draft: 18
- Differences from Codex draft: 7

## Maintainer Decision

Maintainer `tim` accepted the Codex review recommendation on 2026-07-06.
The backlog was updated as follows:

- 18 exact-match cases use the shared Codex/Gemini expected output with
  `expected_source = "human_first_pass"`.
- 1 differing case uses the Gemini advisory expected output with
  `expected_source = "human_adjudication"` and `adjudicator = "tim"`.
- 6 differing cases use the Codex expected output with
  `expected_source = "human_adjudication"`, `adjudicator = "tim"`, and Gemini
  advisory recorded as `decision = "rejected"`.
- All 25 cases are now `approved`, promotion-ready, and promoted into
  `regression-v1.json`.

## Historical Maintainer Action

For each case, choose the final Taiwan Traditional expected output. After maintainer approval:

- write the final value to `review.expected`
- set `review.expected_source = "human_first_pass"` when accepting one advisory version unchanged
- set `review.expected_source = "human_adjudication"` and `review.adjudicator = "tim"` when resolving a difference
- keep Gemini under `review.ai_advisory`; do not set it as `blind_reviewer`

## Comparison

### ui-i18n-0101：different

Input:

```text
语言包下载完成。
```

Codex draft expected:

```text
語言套件下載完成。
```

Gemini advisory expected:

```text
語言包下載完成。
```

Gemini notes:

```text

```

### ui-i18n-0102：match

Input:

```text
当前区域设置使用繁体中文。
```

Codex draft expected:

```text
目前地區設定使用繁體中文。
```

Gemini advisory expected:

```text
目前地區設定使用繁體中文。
```

Gemini notes:

```text

```

### ui-i18n-0103：match

Input:

```text
日期格式会根据地区变化。
```

Codex draft expected:

```text
日期格式會根據地區變化。
```

Gemini advisory expected:

```text
日期格式會根據地區變化。
```

Gemini notes:

```text

```

### ui-i18n-0104：match

Input:

```text
请将时区设置为台北。
```

Codex draft expected:

```text
請將時區設定為台北。
```

Gemini advisory expected:

```text
請將時區設定為台北。
```

Gemini notes:

```text

```

### ui-i18n-0105：different

Input:

```text
数字分组符号可以自定义。
```

Codex draft expected:

```text
數字分組符號可以自訂。
```

Gemini advisory expected:

```text
數字分位符號可自訂。
```

Gemini notes:

```text

```

### ui-i18n-0106：match

Input:

```text
货币符号显示在金额前。
```

Codex draft expected:

```text
貨幣符號顯示在金額前。
```

Gemini advisory expected:

```text
貨幣符號顯示在金額前。
```

Gemini notes:

```text

```

### ui-i18n-0107：different

Input:

```text
翻译缺失时会回退到默认语言。
```

Codex draft expected:

```text
翻譯缺漏時會改用預設語言。
```

Gemini advisory expected:

```text
翻譯遺失時會回復為預設語言。
```

Gemini notes:

```text

```

### ui-i18n-0108：different

Input:

```text
字符串键不能重复。
```

Codex draft expected:

```text
字串鍵不能重複。
```

Gemini advisory expected:

```text
字串鍵不可重複。
```

Gemini notes:

```text

```

### ui-i18n-0109：different

Input:

```text
请为每个语言添加说明。
```

Codex draft expected:

```text
請為每種語言新增說明。
```

Gemini advisory expected:

```text
請為每個語言新增說明。
```

Gemini notes:

```text

```

### ui-i18n-0110：different

Input:

```text
导入翻译文件前请预览差异。
```

Codex draft expected:

```text
匯入翻譯檔前請預覽差異。
```

Gemini advisory expected:

```text
匯入翻譯檔案前請預覽差異。
```

Gemini notes:

```text

```

### ui-i18n-0111：match

Input:

```text
导出文件会包含未翻译项目。
```

Codex draft expected:

```text
匯出檔案會包含未翻譯項目。
```

Gemini advisory expected:

```text
匯出檔案會包含未翻譯項目。
```

Gemini notes:

```text

```

### ui-i18n-0112：match

Input:

```text
占位符名称必须保持一致。
```

Codex draft expected:

```text
預留位置名稱必須保持一致。
```

Gemini advisory expected:

```text
預留位置名稱必須保持一致。
```

Gemini notes:

```text

```

### ui-i18n-0113：match

Input:

```text
请不要翻译变量名。
```

Codex draft expected:

```text
請不要翻譯變數名稱。
```

Gemini advisory expected:

```text
請不要翻譯變數名稱。
```

Gemini notes:

```text

```

### ui-i18n-0114：match

Input:

```text
文本方向会影响布局。
```

Codex draft expected:

```text
文字方向會影響版面配置。
```

Gemini advisory expected:

```text
文字方向會影響版面配置。
```

Gemini notes:

```text

```

### ui-i18n-0115：match

Input:

```text
从右到左语言需要镜像图标。
```

Codex draft expected:

```text
從右到左語言需要鏡像圖示。
```

Gemini advisory expected:

```text
從右到左語言需要鏡像圖示。
```

Gemini notes:

```text

```

### ui-i18n-0116：match

Input:

```text
语言切换后页面会重新加载。
```

Codex draft expected:

```text
語言切換後頁面會重新載入。
```

Gemini advisory expected:

```text
語言切換後頁面會重新載入。
```

Gemini notes:

```text

```

### ui-i18n-0117：match

Input:

```text
预览模式不会保存更改。
```

Codex draft expected:

```text
預覽模式不會儲存變更。
```

Gemini advisory expected:

```text
預覽模式不會儲存變更。
```

Gemini notes:

```text

```

### ui-i18n-0118：match

Input:

```text
文案长度超过按钮宽度。
```

Codex draft expected:

```text
文案長度超過按鈕寬度。
```

Gemini advisory expected:

```text
文案長度超過按鈕寬度。
```

Gemini notes:

```text

```

### ui-i18n-0119：match

Input:

```text
请检查换行是否正确。
```

Codex draft expected:

```text
請檢查換行是否正確。
```

Gemini advisory expected:

```text
請檢查換行是否正確。
```

Gemini notes:

```text

```

### ui-i18n-0120：match

Input:

```text
空白字符会被保留。
```

Codex draft expected:

```text
空白字元會被保留。
```

Gemini advisory expected:

```text
空白字元會被保留。
```

Gemini notes:

```text

```

### ui-i18n-0121：match

Input:

```text
本地缓存会存储最近使用的语言。
```

Codex draft expected:

```text
本機快取會儲存最近使用的語言。
```

Gemini advisory expected:

```text
本機快取會儲存最近使用的語言。
```

Gemini notes:

```text

```

### ui-i18n-0122：match

Input:

```text
搜索翻译键时忽略大小写。
```

Codex draft expected:

```text
搜尋翻譯鍵時忽略大小寫。
```

Gemini advisory expected:

```text
搜尋翻譯鍵時忽略大小寫。
```

Gemini notes:

```text

```

### ui-i18n-0123：match

Input:

```text
批量更新会覆盖人工翻译。
```

Codex draft expected:

```text
批次更新會覆寫人工翻譯。
```

Gemini advisory expected:

```text
批次更新會覆寫人工翻譯。
```

Gemini notes:

```text

```

### ui-i18n-0124：match

Input:

```text
审核状态会显示在翻译列表。
```

Codex draft expected:

```text
審核狀態會顯示在翻譯清單。
```

Gemini advisory expected:

```text
審核狀態會顯示在翻譯清單。
```

Gemini notes:

```text

```

### ui-i18n-0125：different

Input:

```text
请在发布前锁定语言版本。
```

Codex draft expected:

```text
請在發佈前鎖定語言版本。
```

Gemini advisory expected:

```text
請在發布前鎖定語言版本。
```

Gemini notes:

```text

```
