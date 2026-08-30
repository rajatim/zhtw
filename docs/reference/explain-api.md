<!-- zhtw:disable -->
# Explain API 參考

> 自 4.5.0 起提供；所有 SDK 的 event shape 由共用 fixtures 驗證。

`explain` 使用正式 matcher 的同一次 Aho-Corasick scan，回傳轉換結果與規則事件。
它不會另外跑一套簡化演算法，因此 `explain(text).output` 必須永遠等於
`convert(text)`。

## Python

```python
from zhtw import explain

result = explain("这个软件", sources=["cn"])
print(result.output)
# 這個軟體

for event in result.events:
    print(event.rule_id, event.reason_code, event.input_start, event.input_end)
```

要取得跨 SDK 共用的 JSON shape，可呼叫 `result.to_mapping()`：

```json
{
  "output": "軟體",
  "events": [
    {
      "rule_id": "legacy:cn:curated:d53fbca4452dd2624fced37d",
      "layer": "term",
      "outcome": "applied",
      "input_start": 0,
      "input_end": 2,
      "output_start": 0,
      "output_end": 2,
      "source": "软件",
      "target": "軟體",
      "reason_code": "term_selected"
    }
  ]
}
```

所有 index 都是 Unicode codepoint index，`end` 不包含在 span 內。補充平面漢字在
Python 中仍算一個 codepoint。

## CLI

```bash
zhtw explain "这个软件" --source cn
zhtw explain "这个软件" --source cn --json
echo "这个软件" | zhtw explain --source cn
```

預設 event 只包含實際命中的 `source`／`target` 與 span，不包含整段 input、檔案路徑或
前後文。只有明確加上 `--context` 時，CLI 才會為每個 event 額外輸出前後文；處理客戶
資料或其他敏感文字時，不要開這個選項。

## Event 欄位

| 欄位 | 說明 |
|---|---|
| `rule_id` | 穩定規則 ID；字元層使用 `charmap:u...`，balanced 使用 `balanced:u...` |
| `layer` | `term`、`identity`、`balanced` 或 `char` |
| `outcome` | `applied`、`protected` 或 `skipped` |
| `input_start` / `input_end` | 原始文字的 codepoint span |
| `output_start` / `output_end` | 轉換結果的 codepoint span |
| `source` / `target` | 該規則本身的來源與目標 |
| `reason_code` | 穩定、供程式判斷的短原因碼 |

## Reason codes

| reason code | 意義 |
|---|---|
| `term_selected` | 最長匹配選中的詞彙規則 |
| `identity_guard` | identity rule 保護該 span，不做轉換 |
| `identity_contained` | identity candidate 完全包含在較長轉換內，未形成保護 |
| `overlap_loser` | raw candidate 因重疊而未被選中 |
| `protected_by_identity` | 轉換 candidate 和有效 identity guard 重疊，因此略過 |
| `loader_conflict_winner` | 同一 source 有多個已核准定義；此規則是 effective winner |
| `loader_conflict_loser` | 同一 source 的另一個已核准定義被 loader precedence 蓋過 |
| `balanced_default` | 未被詞彙覆蓋的歧義字套用 balanced 預設 |
| `char_map` | 未被詞彙覆蓋的字套用安全字元對映 |

## 低階 API

已有自訂 `Matcher` 的呼叫端可使用：

```python
from zhtw import Matcher, explain_text

matcher = Matcher({"软件": "軟體"})
result = explain_text("软件", matcher)
```

要讓自訂 matcher 回傳自訂規則 ID，可在建立 `Matcher` 時傳入對應的 `RuleRecord`
集合；未提供時會產生 deterministic legacy custom ID。
<!-- zhtw:enable -->
