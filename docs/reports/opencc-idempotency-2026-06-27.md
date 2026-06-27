# OpenCC 匯入詞庫 target 冪等性報告

<!-- zhtw:disable -->

生成日期：2026-06-27

## 摘要

```bash
uv run python scripts/audit_idempotency.py --sources cn,hk --limit 20
```

目前結果：

| 項目 | 數值 |
|------|------|
| 非冪等 target | 403 |
| 來源檔案 | `cn/opencc.json` |
| release gate | report-only |

`curated-only` 仍為 0 issue：

```bash
uv run python scripts/audit_idempotency.py --sources cn,hk --curated-only --fail-on-issues
```

## 本次處理

corpus 擴充到 300 筆時發現 `設備` 會被第二輪轉成 `裝置`：

```text
设备 -> 設備 -> 裝置
```

這屬於已確認的 target 二次轉換破壞，因此已在手工詞庫補：

```json
"設備": "設備"
```

修正後：

```text
设备 -> 設備 -> 設備
```

OpenCC report-only 數字因此由 404 降為 403。

## 剩餘項目如何看待

剩餘 403 筆包含人名、地名、古文、罕見詞與語境模糊詞，例如：

- `于...` 人名或地名是否應轉 `於...` 不能靠裸詞判斷。
- `准...` 在「准/準」之間有語義差異。
- `出/齣`、`斗/鬥`、`表/錶` 需要語境。

這些項目不應硬追歸零。只有在出現人工確認錯轉、corpus failure、使用者回報或官方台灣用語依據時，才應補手工詞條與 regression。

<!-- zhtw:enable -->
