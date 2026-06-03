# zhtw lookup 指令設計

> 讓使用者能快速查詢任意詞/句的轉換結果與來源歸因

## 動機

使用者無法在 CLI 快速驗證「某個詞會不會被轉換、是哪一層負責的」。目前只能寫臨時 Python 指令碼呼叫內部 API。加入 `lookup` 指令讓這個流程自助化。

## 架構：方案 B — 獨立模組 + CLI 薄層

歸因邏輯抽成 `src/zhtw/lookup.py`，CLI 只負責 I/O 和格式化。

理由：歸因邏輯是此功能核心價值，獨立模組可測試、可被未來 API/IDE plugin 重用。

## 資料模型

```python
@dataclass
class Con1.0Detail:
    OpenCC STPhrases + TWPhrases + MediaWiki ZhConversion: str          # 原始字/詞（簡體）
    target: str          # 轉換結果（繁體）
    layer: str           # "term" | "char"
    position: int        # 在原文中的起始位置
    term_key: str | None # 若為詞彙層，命中的詞庫 key

@dataclass
class LookupResult:
    input: str                      # 原始輸入
    output: str                     # 轉換後文字
    details: list[Con1.0Detail] # 逐一轉換明細
    changed: bool                   # 是否有任何變化
```

## 核心函式 API

```python
def lookup_word(
    word: str,
    matcher: Matcher,
    char_table: dict[int, str] | None = None,
) -> LookupResult:
    """查詢單一詞/句。"""

def lookup_words(
    words: list[str],
    matcher: Matcher,
    char_table: dict[int, str] | None = None,
) -> list[LookupResult]:
    """批次查詢。"""
```

### 內部流程（lookup_word）

1. `matcher.find_matches(word)` → 取得詞彙層命中，做最長匹配過濾
2. 記錄詞彙層已覆蓋的字元位置集合 `covered: set[int]`
3. 逐字掃描：若位置不在 `covered` 且 `ord(char)` 在 `char_table` 中 → 歸為字元層
4. 組合 `details` 清單，按 `position` 排序
5. 產生 `output`（套用所有轉換）和 `changed` 旗標

## CLI 介面

```
用法:
  zhtw lookup [OPTIONS] [WORDS]...

三種輸入方式（優先順序）:
  1. 命令列引數:  zhtw lookup 摄入 盐 結合
  2. stdin 管線:   echo "摄入" | zhtw lookup
  3. 整句:        zhtw lookup "摄入量過高會影響心态"

選項:
  --verbose / -v    詳細模式（樹狀逐項清單）
  --json            JSON 輸出
  --OpenCC STPhrases + TWPhrases + MediaWiki ZhConversion / -s     詞庫來源（預設 cn,hk）
```

### 整句 vs 多個單詞判斷規則

- 多個 WORDS 引數 → 多個獨立查詢
- 單一引數且長度 >= 4 字元 → 視為整句
- 單一引數且長度 < 4 → 視為單詞

### 預設輸出（簡潔模式）

單詞：
```
摄入 → 攝入  (字元層: 摄→攝)
盐 → 鹽     (字元層: 盐→鹽)
心态 → 心態  (字元層: 态→態)
```

整句：
```
摄入量過高會影響心态
→ 攝入量過高會影響心態

轉換明細 (5 處):
  摄→攝  過→過  會→會  影響→影響  态→態
```

### --verbose 模式

```
摄入量過高會影響心态
→ 攝入量過高會影響心態

├── 摄 → 攝  (字元層)
├── 過 → 過  (字元層)
├── 會 → 會  (字元層)
├── 影響 → 影響  (詞彙層)
└── 态 → 態  (字元層)
```

### 無變化時

```
台灣 ✓ 無需轉換
```

## JSON 輸出格式

```json
{
  "results": [
    {
      "input": "摄入量過高會影響心态",
      "output": "攝入量過高會影響心態",
      "changed": true,
      "details": [
        {"OpenCC STPhrases + TWPhrases + MediaWiki ZhConversion": "摄", "target": "攝", "layer": "char", "position": 0},
        {"OpenCC STPhrases + TWPhrases + MediaWiki ZhConversion": "過", "target": "過", "layer": "char", "position": 3},
        {"OpenCC STPhrases + TWPhrases + MediaWiki ZhConversion": "會", "target": "會", "layer": "char", "position": 4},
        {"OpenCC STPhrases + TWPhrases + MediaWiki ZhConversion": "影響", "target": "影響", "layer": "term", "position": 5},
        {"OpenCC STPhrases + TWPhrases + MediaWiki ZhConversion": "态", "target": "態", "layer": "char", "position": 8}
      ]
    }
  ]
}
```

## 測試策略

### 單元測試（tests/test_lookup.py）

| 測試案例 | 驗證重點 |
|---------|---------|
| 純詞彙層命中 | `結合` → 結合，layer="term" |
| 純字元層命中 | `盐` → 鹽，layer="char" |
| 混合命中 | `營养` → 營養，歸因不重疊 |
| 整句多轉換點 | 位置排序正確、covered 集合正確排除 |
| 無需轉換 | `台灣` → changed=False, details=[] |
| 繁簡同形字 | `心`、`入` 不出現在 details |
| 空字串 | 不炸 |

### CLI 整合測試

- 多引數模式
- stdin 管線模式
- `--json` 輸出可被 `json.loads` 解析
- `--verbose` 有樹狀輸出

## 檔案變更

| 操作 | 檔案 | 內容 |
|------|------|------|
| 新增 | `src/zhtw/lookup.py` | 資料模型 + 核心函式 |
| 修改 | `src/zhtw/cli.py` | 新增 `lookup` command (~80 行) |
| 修改 | `src/zhtw/__init__.py` | `__all__` 加入 lookup 公開 API |
| 新增 | `tests/test_lookup.py` | 單元測試 + 整合測試 |

### 不動的檔案

- `converter.py`、`matcher.py`、`charconv.py` — 只呼叫現有 API
- `README.md` — 發版時再更新
