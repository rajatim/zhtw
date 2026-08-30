# Roadmap

Roadmap 是方向，不是日期承諾。相容性或範圍改變會先以 Issue、設計文件與測試確認。

## 4.5.0：已完成

- JSON string value adapter。
- 跨 SDK `explain` 與穩定 rule event。
- Rule schema v2 與 human review metadata。
- 強化跨 SDK 封裝、驗證與發布證據。
- 雙語公開產品文件與文件 gate。

## 4.6.0：下一階段

- 評估以 `domain` 建立明確 profile，但不讓 metadata 在沒有契約時改變現有輸出。
- 改善 custom rule authoring、驗證錯誤與遷移工具。
- 依公開使用問題補強 CLI／SDK 文件，不先製造大量空頁。
- 為下一輪 fresh benchmark 完成獨立資料與治理準備。

## 4.7.0 與 5.0.0：條件式方向

- 只有在公開 API 或轉換契約成熟後，才擴充 profile、context 或更完整的結構化 adapter。
- 只有真正需要不相容改變時才進 5.0.0；不為了排程製造 major version。

Blind-v3 尚未執行，也不是 4.5.0 的 release condition。新的精準度主張必須先凍結版本、資料與評分方式，再公開結果。

想提案請開 [GitHub Issue](https://github.com/rajatim/zhtw/issues)；錯轉案例請先看[貢獻方式](../guides/contributing.md)。
