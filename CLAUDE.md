# ZHTW - Claude AI 開發指南

> **快速定位**: 這是給 AI 助手的開發指南，人類開發者請看 README.md 和 CONTRIBUTING.md

**版本**: v2.5.0 | **更新**: 2025-12-31 | **作者**: rajatim

---

## 🚨 關鍵規則（必讀）

```
┌─────────────────────────────────────────────────────────────────┐
│  1. 寧可少轉，不要錯轉 — 這是本專案的核心理念                    │
│  2. 不要使用 OpenCC — 會過度轉換台灣正確用語                     │
│  3. 詞庫修改要謹慎 — 新增前先確認是否為台灣正確用語              │
│  4. 核心功能保持離線 — LLM 功能是可選的增強                      │
│  5. 測試先行 — 任何修改都要跑 pytest 確認通過                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📋 快速參考

### 專案概述

| 項目 | 說明 |
|------|------|
| **功能** | 簡體/港式中文 → 台灣繁體用語轉換 |
| **核心演算法** | Aho-Corasick（O(n) 時間複雜度）|
| **詞庫數量** | 433 個精選術語 |
| **支援編碼** | UTF-8、Big5、GBK、GB2312、GB18030 |

### 常用指令

```bash
# 開發
pip install -e ".[dev]"    # 安裝開發依賴
pytest                      # 執行測試
ruff check .                # 程式碼檢查
python -m zhtw check ./src  # 本地測試

# 功能
zhtw check <path>           # 檢查
zhtw fix <path>             # 修正
zhtw stats                  # 詞庫統計
zhtw validate               # 詞庫驗證
```

### 重要檔案位置

| 檔案 | 用途 |
|------|------|
| `src/zhtw/cli.py` | CLI 入口，所有指令定義 |
| `src/zhtw/converter.py` | 核心轉換邏輯 |
| `src/zhtw/matcher.py` | Aho-Corasick 比對器 |
| `src/zhtw/encoding.py` | 編碼偵測與轉換 |
| `src/zhtw/dictionary.py` | 詞庫載入 |
| `src/zhtw/data/terms/cn/` | 簡體→台灣詞庫 |
| `src/zhtw/data/terms/hk/` | 港式→台灣詞庫 |

---

## ✅ DO（正確行為）

### 修改程式碼前

```
✅ 先用 Read 工具讀取要修改的檔案
✅ 理解現有程式碼邏輯再修改
✅ 修改後執行 pytest 確認測試通過
✅ 確認 ruff check 無錯誤
```

### 詞庫相關

```
✅ 新增詞彙前，確認這是台灣「不使用」的用語
✅ 新增 identity mapping 防止子字串誤判（如「演算法」→「演算法」）
✅ 考慮詞彙的多種使用情境
✅ 用 zhtw validate 檢查詞庫衝突
```

### 回應使用者

```
✅ 用繁體中文回應
✅ 程式碼註解用英文或繁體中文
✅ commit message 用繁體中文
✅ 提供具體的檔案路徑和行號
```

---

## ❌ DON'T（錯誤行為）

### 絕對禁止

```
❌ 使用 OpenCC 或任何自動轉換工具
❌ 新增不確定的詞彙（寧可少轉不要錯轉）
❌ 修改程式碼但不跑測試
❌ 把台灣正確用語加入詞庫（如「權限」不應轉換）
```

### 詞庫陷阱

```
❌ "表情" → "表情符號"     # 太廣泛，「臉部表情」會被誤轉
❌ "橙" → "柳橙"           # 「橙色」會變成「柳橙色」
❌ "算法" → "演算法"       # 「演算法」會變成「演演算法」
   （正確做法：加入 "演算法" → "演算法" identity mapping）
```

### 常見錯誤

```
❌ 假設檔案是 UTF-8（要用 encoding.py 偵測）
❌ 忽略 zhtw:disable 註解區塊
❌ 修改 .zhtwignore 排除的檔案
❌ 在非 TTY 環境使用動態進度條
```

---

## 🔀 決策樹

### 使用者要求新增詞彙

```
使用者要求新增 "X" → "Y"
         │
         ▼
    "X" 是台灣不使用的用語嗎？
         │
    ┌────┴────┐
    是        否
    │         │
    ▼         ▼
  繼續      拒絕，說明原因
    │
    ▼
  "Y" 在台灣常用嗎？
    │
    ┌────┴────┐
    是        否
    │         │
    ▼         ▼
  繼續      建議更好的翻譯
    │
    ▼
  "X" 是否為其他詞的子字串？
    │
    ┌────┴────┐
    是        否
    │         │
    ▼         ▼
  需要加入    直接新增
  identity
  mapping
```

### 使用者報告誤判

```
使用者報告 "A" 被誤轉為 "B"
         │
         ▼
    檢查詞庫是否有 "A" → "B"
         │
    ┌────┴────┐
    有        沒有
    │         │
    ▼         ▼
  評估是否    檢查是否為
  應該移除    子字串問題
    │         │
    ▼         ▼
  移除或      加入 identity
  加入例外    mapping 保護
```

### 修改核心模組

```
要修改 converter.py / matcher.py / encoding.py
         │
         ▼
    1. 先讀取完整檔案內容
    2. 理解現有邏輯
    3. 寫出修改計畫
    4. 執行修改
    5. 執行 pytest
         │
    ┌────┴────┐
  通過       失敗
    │         │
    ▼         ▼
  完成      分析錯誤
           修復後重測
```

---

## 📁 專案結構

```
zhtw/
├── src/zhtw/
│   ├── __init__.py          # 版本號 (2.5.0)
│   ├── __main__.py          # python -m zhtw 入口
│   ├── cli.py               # CLI 指令 (click 框架)
│   ├── converter.py         # 檔案轉換引擎
│   ├── matcher.py           # Aho-Corasick 比對器
│   ├── dictionary.py        # 詞庫載入/合併
│   ├── encoding.py          # 編碼偵測/轉換 (v2.5.0+)
│   ├── config.py            # 設定管理
│   ├── import_terms.py      # 詞庫匯入
│   ├── review.py            # 詞彙審核
│   │
│   ├── llm/                 # LLM 模組（可選）
│   │   ├── client.py        # Gemini API 客戶端
│   │   ├── usage.py         # 用量追蹤
│   │   └── prompts.py       # 提示詞範本
│   │
│   └── data/terms/
│       ├── cn/              # 簡體 → 台灣
│       │   ├── base.json    # 基礎詞彙
│       │   ├── it.json      # IT 術語
│       │   └── business.json
│       ├── hk/              # 港式 → 台灣
│       │   ├── base.json
│       │   └── tech.json
│       └── pending/         # 待審核
│
├── tests/
│   ├── test_matcher.py
│   ├── test_converter.py
│   ├── test_dictionary.py
│   └── test_encoding.py
│
├── pyproject.toml
├── README.md                # 使用者文件
├── CONTRIBUTING.md          # 貢獻指南
├── CHANGELOG.md             # 版本記錄
└── CLAUDE.md                # 本文件
```

---

## 🔧 核心模組詳解

### converter.py — 轉換引擎

```python
# 主要函式
process_directory(path, sources, fix, ...)  # 主入口
convert_directory(path, matcher, fix, ...)  # 遍歷目錄
convert_file(path, matcher, fix, ...)       # 處理單檔

# 重要參數
fix: bool              # True=修改檔案, False=只檢查
encoding: str          # 輸入編碼 (auto/utf-8/big5/...)
output_encoding: str   # 輸出編碼 (auto/utf-8/keep)
yes: bool              # 跳過確認提示
```

### matcher.py — Aho-Corasick 比對器

```python
class Matcher:
    def __init__(self, terms: dict[str, str]):
        # 建立 Aho-Corasick 自動機
        # 處理 identity mapping 優先權

    def find_matches(self, text: str) -> list[Match]:
        # 找出所有比對，過濾重疊

    def find_matches_with_lines(self, text: str) -> list[MatchWithLine]:
        # 帶行號/列號的比對結果

    def replace_all(self, text: str) -> str:
        # 替換所有比對

# Identity Mapping 機制
# 當 terms 包含 {"演算法": "演算法"} 時
# "演算法" 會建立保護區，防止內部的 "算法" 被轉換
```

### encoding.py — 編碼處理 (v2.5.0+)

```python
def detect_encoding(file_path: Path) -> EncodingInfo:
    # 使用 charset-normalizer 偵測編碼
    # 回傳 EncodingInfo(encoding, confidence, has_bom)

def read_file(file_path: Path, encoding: str = "auto") -> tuple[str, EncodingInfo]:
    # 讀取檔案，自動處理編碼
    # 回傳 (內容, 編碼資訊)

def write_file(file_path: Path, content: str, output_encoding: str, original_encoding: str):
    # 寫入檔案，處理編碼轉換
    # output_encoding="keep" 保留原編碼
    # output_encoding="utf-8" 統一轉 UTF-8
```

### dictionary.py — 詞庫載入

```python
def load_builtin(sources: list[str] = ["cn", "hk"]) -> dict[str, str]:
    # 載入內建詞庫
    # sources: ["cn"], ["hk"], ["cn", "hk"]

def load_dictionary(sources: list[str], custom_path: str = None) -> dict[str, str]:
    # 載入並合併詞庫
    # 自訂詞庫優先於內建
```

---

## 📝 詞庫格式

### 標準格式

```json
{
  "version": "1.0",
  "description": "簡體中文 IT 術語",
  "terms": {
    "软件": "軟體",
    "硬件": "硬體",
    "程序": "程式"
  }
}
```

### Identity Mapping（防止誤判）

```json
{
  "terms": {
    "算法": "演算法",
    "演算法": "演算法"
  }
}
```

當文字包含「演算法」時，整個詞會被保護，不會被拆成「演」+「算法」→「演」+「演算法」。

---

## 🧪 測試要求

### 修改程式碼後必須執行

```bash
# 完整測試
pytest

# 快速測試（開發時）
pytest tests/test_matcher.py -v

# 特定測試
pytest tests/test_converter.py::test_convert_file -v
```

### 測試覆蓋的情境

| 模組 | 測試重點 |
|------|---------|
| matcher | 基本比對、重疊處理、identity mapping |
| converter | 檔案讀寫、忽略註解、編碼轉換 |
| dictionary | 詞庫載入、合併、衝突處理 |
| encoding | 編碼偵測、BOM 處理、轉換 |

---

## 📜 版本歷史

| 版本 | 日期 | 主要功能 |
|------|------|---------|
| v2.5.0 | 2025-12-29 | 多編碼支援、--yes 參數 |
| v2.4.3 | 2025-12-27 | 修正子字串誤判、identity mapping |
| v2.4.0 | 2025-12-26 | 進度條、TTY 偵測 |
| v2.3.0 | - | --show-diff、--backup |
| v2.2.0 | - | .zhtwignore 支援 |
| v2.0.0 | - | LLM 整合 |
| v1.5.0 | - | stats、validate、忽略註解 |
| v1.0.0 | - | 基礎 check/fix |

---

## 🎯 開發中功能 (GitHub Issues)

| Issue | 功能 | 狀態 |
|-------|------|------|
| #10 | 資料庫支援 (zhtw-db) | 📐 架構設計完成 |
| #11 | 瀏覽器擴充套件 | 📋 待開發 |
| #8 | VS Code 擴充套件 | 📋 待開發 |
| #6 | Office 文件支援 | 📋 待開發 |

---

## 💡 常見任務範例

### 新增詞彙

```bash
# 1. 確認詞彙正確性
# 2. 編輯對應的詞庫檔案
vim src/zhtw/data/terms/cn/base.json

# 3. 驗證詞庫
python -m zhtw validate

# 4. 測試
pytest tests/test_dictionary.py -v
```

### 修復誤判 Bug

```bash
# 1. 分析問題
python -c "
from zhtw.matcher import Matcher
m = Matcher({'算法': '演算法'})
print(m.find_matches('演算法'))  # 應該為空或只有 identity
"

# 2. 加入 identity mapping
# 編輯詞庫，加入 "演算法": "演算法"

# 3. 測試修復
pytest tests/test_matcher.py -v
```

### 新增 CLI 參數

```python
# 1. 在 cli.py 找到對應的 command
# 2. 加入 @click.option
@click.option("--new-param", default=None, help="說明")

# 3. 在函式中使用參數
def check(path, new_param, ...):
    if new_param:
        ...

# 4. 測試
python -m zhtw check --help
python -m zhtw check ./test --new-param value
```

---

## 🔗 相關資源

- **Issue #10**: zhtw-db 完整架構設計
- **README.md**: 使用者文件
- **CONTRIBUTING.md**: 貢獻指南
- **tests/**: 測試範例

---

*本文件針對 Claude AI 優化，提供快速參考和明確指引*
