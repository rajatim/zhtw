<!-- zhtw:disable -->
# 語義歧義消解 v1 設計檔案

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 為 119 個歧義字中最安全的子集提供 opt-in 預設對映，提升 balanced mode 下的轉換覆蓋率。

**Architecture:** 在現有詞庫層和字元層之間插入「歧義預設值層」，僅在 `ambiguity_mode='balanced'` 時啟用。

**Tech Stack:** Python（核心）、CLI（click flag）、`zhtw-data.json`（跨 SDK 資料共享）

---

## 1. 設計決定摘要

| 決定 | 結論 | 理由 |
|------|------|------|
| Mode 數量 | 2：`strict`（預設）+ `balanced` | 公開 API 簡單；內部可分層但不暴露複雜度 |
| v1 範圍 | 3 字：几→幾、丰→豐、杰→傑 | 驗證架構是否值得存在，不追求最大覆蓋 |
| v1 候選 | 并→並（diff-gated） | 需 corpus diff 驗證後才啟用 |
| API 位置 | Converter 層級引數 + CLI flag | explicit > implicit；不做全域設定 |
| 契約語義 | strict = stable contract；balanced = evolving contract | strict 行為改變是 breaking change；balanced 規則改進是 minor/patch |

## 2. 轉換管線

### strict 模式（現行，不變）

```
輸入 → [詞庫層 Aho-Corasick] → [字元層 str.translate] → 輸出
```

### balanced 模式

```
輸入 → [詞庫層 Aho-Corasick] → [歧義預設值層 ★NEW] → [字元層 str.translate] → 輸出
```

歧義預設值層邏輯：

1. 掃描經過詞庫層後**仍未被轉換**的文字位置
2. 對 `balanced_defaults` curated list 中的歧義字，套用預設對映
3. 已被詞庫層處理過的位置**不重複處理**（詞庫層優先）

## 3. v1 字表

### 啟用集（v1 shipped）

| 簡 | 預設對映 | 為什麼安全 | 正向測試 | 負向測試 |
|---|---|---|---|---|
| 几 | 幾 | 「几」作小桌義極罕，「茶几」已在詞庫 identity protect | `几个` → `幾個` | `茶几` 不變 |
| 丰 | 豐 | 「丰姿」是古語，現代幾乎不用 | `丰富` → `豐富` | （無常見反例） |
| 杰 | 傑 | 異體字，無語義差異 | `杰出` → `傑出` | （無常見反例） |

### 候選集（v1.1 diff-gated）

| 簡 | 預設對映 | 風險點 | 啟用條件 |
|---|---|---|---|
| 并 | 並 | 兼并、吞并、并入 等場景可能需要「併」 | corpus diff 通過，確認無大量誤轉 |

### 已評估但不納入 v1

| 簡 | 原因 |
|---|---|
| 出→出 | identity mapping，對 `convert()` 輸出無變化 |
| 了→了 | identity mapping，對 `convert()` 輸出無變化 |
| 千→千 | identity mapping，對 `convert()` 輸出無變化 |
| 秋→秋 | identity mapping，對 `convert()` 輸出無變化 |
| 丑→醜 | 丑時/辛丑/乙丑 仍活躍，風險偏高 |

## 4. API 設計

### Python

```python
from zhtw.converter import Converter

# 預設 strict（現行行為，不變）
converter = Converter()

# opt-in balanced
converter = Converter(ambiguity_mode='balanced')
result = converter.convert('几个人')  # → '幾個人'
```

引數型別：`ambiguity_mode: Literal['strict', 'balanced'] = 'strict'`

無效值丟擲 `ValueError`。

### CLI

```bash
# 預設 strict
zhtw fix src/

# opt-in balanced
zhtw fix --ambiguity-mode balanced src/
zhtw check --ambiguity-mode balanced src/
```

### 其他 SDK（v1 不實作，下次 mono-versioning 同步）

```typescript
// TypeScript
createConverter({ ambiguityMode: 'balanced' })

// Rust
Converter::builder().ambiguity_mode(AmbiguityMode::Balanced).build()?

// Java
Converter.builder().ambiguityMode(AmbiguityMode.BALANCED).build()
```

## 5. 資料格式

在 `zhtw-data.json` 的 `charmap` 區段新增 `balanced_defaults`：

```json
{
  "charmap": {
    "chars": { "说": "說", "...": "..." },
    "ambiguous_excluded": ["䴘", "丑", "..."],
    "balanced_defaults": {
      "几": "幾",
      "丰": "豐",
      "杰": "傑"
    }
  }
}
```

- 所有 SDK 讀 `balanced_defaults`，不各自維護字表
- 新增/移除字只需改 Python 來源 + `zhtw export` 重新產生
- `ambiguous_excluded` 不變（balanced_defaults 是其子集）

## 6. 實作位置

| 檔案 | 變更 |
|------|------|
| `src/zhtw/data/charmap/balanced_defaults.json` | **新增**：curated 字表來源檔 |
| `src/zhtw/charconv.py` | 新增 `apply_balanced_defaults()` 函式 |
| `src/zhtw/converter.py` | `convert_text()` 接受 `ambiguity_mode` 引數，在詞庫層後、字元層前呼叫 |
| `src/zhtw/cli.py` | `fix` / `check` 命令加 `--ambiguity-mode` flag |
| `src/zhtw/matcher.py` | 提供「哪些 byte range 已被詞庫層處理」的資訊給歧義層 |
| `tests/test_ambiguous_balanced.py` | **新增**：balanced mode 專屬測試 |
| `tests/data/golden-balanced.json` | **新增**：balanced mode 獨立 golden fixture |
| `src/zhtw/encoding.py` | `export` 命令輸出 `balanced_defaults` 到 `zhtw-data.json` |

## 7. 測試策略

| 測試型別 | 內容 |
|---------|------|
| **正向測試** | `几个→幾個`、`丰富→豐富`、`杰出→傑出`（balanced mode） |
| **負向測試** | `茶几` 不變（詞庫 identity protect 優先） |
| **strict 不變** | 所有現有測試在 strict mode 下結果完全不變 |
| **balanced golden** | 獨立 golden fixture，和 strict golden 分開維護 |
| **corpus diff** | 跑完整語料，人工檢視 balanced vs strict 差異清單 |
| **API 驗證** | `ambiguity_mode='invalid'` 丟擲 `ValueError` |

## 8. 不做的事

- 不做全域 `zhtw config set ambiguity_mode`
- 不做 heuristic 上下文消歧（v2 考慮）
- 不對 119 個歧義字全部套預設值
- 不改 strict mode 的任何行為
- v1 不實作其他 SDK（TypeScript / Rust / Java / .NET）

## 9. 未來方向

- **v1.1：** 并→並 通過 corpus diff 後加入 balanced_defaults
- **v1.x：** 從 Tier 2 挑選經 corpus diff 驗證的字逐步擴充
- **v2：** 對少數高價值字（如 干、面、后）加啟發式上下文規則
- **Future work：** 如果使用者反覆需要 project-level 預設值，可考慮 config 支援；v1 保持 explicit per invocation
