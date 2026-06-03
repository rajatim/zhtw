<!-- zhtw:disable -->
# 複雜多義字 v2 語義消歧

**Date:** 2026-04-11
**Status:** Ready for implementation

---

## Goal

建立可擴展的歧義字消歧框架，以 `disambiguation.json` 為 canonical source，
用 default mapping + protect_terms (identity terms) 模型處理有明確主流義的歧義字。
v2.0 首批：后→後、里→裡。

## 背景

### 現有三層架構

```
Term layer (Aho-Corasick) → Balanced layer → Char layer
```

- **Term layer**：多字詞轉換（软件→軟體）+ identity term 保護
- **Balanced layer**：v1 已有 8 個「95%+ 主流義」的簡單 default mapping（几→幾、丰→豐 等）
- **Char layer**：6,360 個安全一對一字元映射

### 問題

102 個 ambiguous_excluded 字在 strict mode 完全不轉，在 balanced mode 也只處理 8 個。
高頻字如「后」「里」出現在真實文本中佔歧義字出現次數的很大比例，但因為它們
有少量例外用法（皇后、公里），不能簡單放進 balanced_defaults。

### v1 vs v2 差異

| 項目 | v1 (現有) | v2 (本設計) |
|------|-----------|-------------|
| 資料格式 | `balanced_defaults.json` flat dict | `disambiguation.json` structured rules |
| 保護機制 | 無（不需要，v1 字沒有例外） | `protect_terms` → identity terms |
| 首批覆蓋 | 几、丰、杰、卤、坛、弥、摆、纤 (8字) | + 后、里 (2字，含 protect_terms) |

## 設計原則

- **寧可少轉，不要錯轉** — 只有「主流義明確 + 例外可列舉」的字才給 default
- **不加新 runtime 引擎** — exception 一律用現有 identity term 機制
- **直接改，不做向後相容** — `balanced_defaults.json` 淘汰
- **Python 是 source of truth** — SDK 透過 export 取得衍生資料

## 歧義字分類

### Class 1：有明確主流義，可給 default + protect_terms

| 字 | default | protect_terms | 理由 |
|----|---------|---------------|------|
| 后 | 後 | 皇后、太后、后妃、后土、影后、歌后、后冠 | 現代中文「后」幾乎都是「後」；「后」義僅限皇后等固定詞 |
| 里 | 裡 | 公里、英里、海里、里程、里長、鄰里、故里、里民、里幹事、三里屯 | 現代中文「里」大多是「裡」（裡面）；距離/行政單位用法有限且可列舉 |

### Class 2：雙義都高頻，先不給 default，只靠詞庫

干（幹/乾/干 三義）、台（臺/檯/台）、系（係/繫）、制（製/制）、
折（摺/折）、采（採/彩）、复（復/複）、钟（鐘/鍾）、面（面/麵）、
只（只/隻）、谷（谷/穀）、征（徵/征，待 corpus diff 驗證後可升 Class 1）

### Class 3：Deferred

其餘 ~80 字（卜、斗、曲、朴、松、栗 等低頻或極難判斷的字）。

## 資料結構

### 新檔案：`src/zhtw/data/charmap/disambiguation.json`

```json
{
  "schema_version": 1,
  "rules": {
    "几": { "default": "幾" },
    "丰": { "default": "豐" },
    "杰": { "default": "傑" },
    "卤": { "default": "滷" },
    "坛": { "default": "壇" },
    "弥": { "default": "彌" },
    "摆": { "default": "擺" },
    "纤": { "default": "纖" },
    "后": {
      "default": "後",
      "protect_terms": ["皇后", "太后", "后妃", "后土", "影后", "歌后", "后冠"]
    },
    "里": {
      "default": "裡",
      "protect_terms": [
        "公里", "英里", "海里", "里程", "里長", "鄰里",
        "故里", "里民", "里幹事", "三里屯"
      ]
    }
  }
}
```

**Schema 規則：**
- `schema_version`：整數，用於未來擴展
- `rules`：key 是簡體字（必須在 `ambiguous_excluded` 清單中）
- `default`：必填，balanced mode 的預設映射目標
- `protect_terms`：選填，注入為 identity terms 的詞組清單。每個詞必須包含該歧義字

### 淘汰：`balanced_defaults.json`

刪除此檔案。所有 v1 的 8 個 entries 合併到 `disambiguation.json` 的 `rules` 中。

### 修改：`charconv.py`

- `BALANCED_DEFAULTS_FILE` 常數改指向 `disambiguation.json`
- `get_balanced_defaults()` 改讀 `disambiguation.json`，從 `rules` 萃取 `{char: default}` flat view
- 新增 `get_protect_terms()` → 回傳 `{char: [term, ...]}` dict
- 快取機制同現有 pattern

### 修改：`converter.py`

`convert()` 函式（line 554-563）建構 matcher 時：
- 載入 protect_terms
- 將所有 protect terms 注入 term dictionary 作為 identity terms（`source == target`）
- 注入發生在所有模式（identity terms 在 strict mode 不影響結果，
  因為歧義字不在 safe_chars 的 char layer 中；但在 balanced mode
  它們的 covered positions 阻止 balanced layer 的 default 覆寫）

**為什麼不分模式注入：** 如果只在 balanced mode 注入，需要把 cache key 從
`tuple(sources)` 改成 `(tuple(sources), ambiguity_mode)`，
導致同一組 sources 建兩個 matcher。identity terms 在 strict mode 是 no-op，
不影響結果也不影響效能，所以統一注入更簡單。

## Export 與 SDK

### `zhtw-data.json` 變更

```json
{
  "charmap": {
    "chars": { ... },
    "ambiguous": [ ... ],
    "balanced_defaults": { "后": "後", "里": "裡", "几": "幾", ... },
    "balanced_protect_terms": { "后": ["皇后", "太后", ...], "里": ["公里", ...] }
  }
}
```

- `balanced_defaults`：保持 flat `{char: target}` 格式（SDK 已在讀）
- 新增 `balanced_protect_terms`：`{char: [term, ...]}` — SDK 在建構 matcher 時
  注入為 identity terms
- 沒有 `protect_terms` 的字不出現在 `balanced_protect_terms` 中

### SDK 影響

各 SDK 已有 balanced mode 支援（讀 `balanced_defaults`）。新增行為：
- 讀取 `balanced_protect_terms`
- 初始化時把 protect terms 加入 pattern table 作為 identity terms
- 不需要新的 matching engine — 走現有 Aho-Corasick

## 測試

### 資料完整性測試

- `disambiguation.json` 的 `schema_version` 存在且為整數
- 每個 rule 的 `default` 存在且是單字元
- 每個 `protect_terms` 中的詞包含對應的歧義字
- 每個 rule 的 key 在 `ambiguous_excluded` 清單中
- v1 的 8 個字全部在 rules 中（無遺漏）

### 整合測試（Python）

```python
# 后 — default 後 + 保護
("以后再说", "balanced") → "以後再說"
("皇后很美", "balanced") → "皇后很美"
("太后驾到", "balanced") → "太后駕到"

# 里 — default 裡 + 保護
("家里很大", "balanced") → "家裡很大"
("公里数很大", "balanced") → "公里數很大"

# strict mode 不變性
("以后再说", "strict") → "以后再說"
("皇后很美", "strict") → "皇后很美"
```

### Golden test（cross-SDK）

在 `_GOLDEN_CASES` 新增 balanced mode cases。Golden test schema 需擴展：
- 新增 `ambiguity_mode` 欄位（可選，預設 `"strict"`）
- `generate_golden_test()` 對 balanced cases 以 balanced mode 執行轉換
- SDK golden test runner 讀取 `ambiguity_mode` 並相應配置 converter

### 現有測試不變性

- 所有現有 strict mode 測試必須繼續通過
- v1 的 8 個 balanced default 測試必須繼續通過（資料來源換了但行為不變）

## 不做的事

- 不加 regex / context window / bigram 規則引擎
- 不加 `override_terms`（Class 2 字純靠 term layer，不經 disambiguation schema）
- 不改 strict mode 行為
- 不處理 Class 2/3 的字
- 不做 corpus regression（獨立驗證，不在本 spec 範圍）
