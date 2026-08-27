# Rule schema v2 參考

> 4.5.0 開發中；正式發版前，套件與 shared data 的版本仍維持 4.4.5。

Rule schema v2 為每一條轉換規則加入穩定 ID、來源地區與 review metadata。4.5.0 只用
這些欄位做驗證、稽核與 `explain`；runtime 仍使用和 4.4.5 相同的 effective
source-to-target map。`domain`、`trust_level`、`priority` 與 `review_status` 不會在 4.5.0
改變規則是否生效。

正式 JSON Schema 位於
[`src/zhtw/data/schemas/rule-v2.schema.json`](../../src/zhtw/data/schemas/rule-v2.schema.json)。

## Authoring 格式

外部 custom 規則與待審 packet 使用以下 envelope：

<!-- zhtw:disable -->
```json
{
  "schema_version": 2,
  "rules": [
    {
      "id": "team:cn:custom:software",
      "source_locale": "cn",
      "source": "软件",
      "target": "軟體",
      "rule_class": "custom",
      "domain": "it",
      "trust_level": "custom",
      "priority": 0,
      "context": ["product-ui"],
      "evidence_source": "internal terminology review 2026-08-27",
      "review_status": "approved"
    }
  ]
}
```
<!-- zhtw:enable -->

Envelope 與每一筆 rule 都會拒絕未知或缺少的欄位。`schema_version` 必須是 `2`，
`rules` 必須是 array。

## Rule 欄位

| 欄位 | 限制與用途 |
|---|---|
| `id` | 3～128 個 ASCII 字元；符合 `^[a-z0-9][a-z0-9._:-]{2,127}$`，而且整份 catalog 不得重複 |
| `source_locale` | `cn` 或 `hk`；表示規則的輸入來源，不是輸出地區 |
| `source` | 非空字串；matcher 的輸入 pattern |
| `target` | 非空字串；選中規則後輸出的臺灣繁體文字 |
| `rule_class` | `bulk`、`generated_guard`、`curated` 或 `custom` |
| `domain` | 描述使用領域；可用值見下節 |
| `trust_level` | `imported`、`generated`、`curated` 或 `custom` |
| `priority` | `-1000`～`1000` 的整數；4.5.0 只記錄 metadata，不重新排序規則 |
| `context` | 不重複的非空字串 array；空 array 代表沒有額外 context 限制 |
| `evidence_source` | `null` 或非空字串；`approved` 規則不得為 `null` |
| `review_status` | `pending`、`approved` 或 `rejected` |

`domain` 可使用：`general`、`business`、`daily`、`ecommerce`、`education`、
`finance`、`formal`、`gaming`、`geography`、`it`、`legal`、`medical`、`social`、`ui`。

`rule_class` 的意義如下：

- `bulk`：大量、可重建的基礎對映。
- `generated_guard`：由已核准流程產生的 identity 保護規則。
- `curated`：經人工整理的詞彙或字詞規則。
- `custom`：呼叫端或專案提供的 override。

## 穩定 ID

新建的 v2 authored rule 應使用明確、長期不變的 `id`。搬檔、重新匯出或變更 metadata
不得順便更換 ID；若 `source_locale`、`source`、`target` 或 `rule_class` 的語意真的改變，
應建立新 ID。

舊版 v1 規則沒有 ID，相容層會產生 deterministic legacy ID。計算方式為：

1. 建立只含 `rule_class`、`source`、`source_locale`、`target` 的 JSON object。
2. 依 key 排序，以 UTF-8、compact JSON、直接保留 Unicode 的方式編碼。
3. 計算 SHA-256，取前 24 個小寫十六進位字元。
4. 組成 `legacy:<locale>:<rule_class>:<digest>`。

檔案路徑不參與 ID，因此純搬移不會改變規則身分。同一 ID 指向不同核心內容、重複 ID、
無效 ID 或未知 enum 都會 fail closed（安全失敗），不會靜默降級成 v1。

## Review lifecycle

- `pending`：候選資料，可進 review packet，但不得成為正式 effective rule。
- `approved`：已由人工做出 final decision，且必須有 `evidence_source`。
- `rejected`：保留判斷紀錄，但不進 runtime effective map。

AI review 只能提供建議，不能自行把 `pending` 改成 human-approved ground truth。混合中英數
詞彙也必須先通過 Unicode、符號與 provenance 驗證，再由 maintainer 作最後判斷。

## v1 相容層與 shared data

現有 production term 檔不會在 4.5.0 為了格式而全面重寫。loader 同時接受 legacy string
map、既有 extended value 與 v2 record，最後產生兩份結果：

- effective map：提供 matcher 使用，必須和 4.4.5 完全相同；
- full catalog：保留所有核准記錄，提供驗證與 `explain` 的 winner／loser 資訊。

`sdk/data/zhtw-data.json` 是給各 SDK 的匯出格式。它保留 `terms` effective map，並用
`rule_catalog.format = "grouped-v1"` 壓縮重複 metadata。這是 shared-data envelope，不是
外部 authoring envelope；請勿手動修改。更新正式規則後應透過 `zhtw export` 重建，再用：

```bash
zhtw validate
make export-check
```

確認 catalog、effective terms 與 committed shared data 完全一致。

## 4.5.0 不做的事

- 不依 `domain` 自動套用 profile；這留到 4.6.0。
- 不依 `priority` 重新排列現有規則。
- 不讓 `pending` 或 `rejected` 候選進正式轉換。
- 不因 schema 遷移改變 leftmost-longest、identity guard、balanced 或 charmap 行為。
- 不把資料格式遷移和詞彙文字修改混在同一個 commit。
