# ZHTW - Claude AI 開發指南

**專案名稱**: ZHTW - 簡轉繁台灣用語轉換器
**作者**: rajatim
**語言**: Python 3.9+
**最後更新**: 2025-12-26

---

## 專案概述

將程式碼和文件中的簡體中文轉換為台灣繁體中文用語的 CLI 工具。

### 核心設計原則

1. **完全離線** - 不傳送任何資料到外部伺服器
2. **術語表優先** - 只轉換明確定義的詞彙，避免過度轉換
3. **高效能** - Aho-Corasick 演算法處理大量術語
4. **可擴充** - JSON 詞庫格式，易於維護

### 為什麼不用 OpenCC？

OpenCC 會過度轉換台灣正確的詞彙（如 權限→許可權）。我們使用精確術語表避免這問題。

---

## 專案結構

```
zhtw/
├── src/zhtw/
│   ├── __init__.py      # 版本號、匯出
│   ├── cli.py           # CLI 入口 (click)
│   ├── converter.py     # 核心轉換邏輯
│   ├── dictionary.py    # 詞庫載入/管理
│   ├── matcher.py       # Aho-Corasick 匹配器
│   └── data/
│       └── terms/
│           ├── cn/          # 簡體 → 台灣繁體
│           │   ├── base.json
│           │   ├── it.json
│           │   └── business.json
│           └── hk/          # 港式 → 台灣繁體
│               ├── base.json
│               └── tech.json
├── tests/
├── pyproject.toml
├── README.md
└── CLAUDE.md            # 本文件
```

---

## 核心模組說明

### cli.py
- 使用 `click` 框架
- 子命令: `check`, `fix`
- 參數: `--source`, `--dict`, `--exclude`, `--json`, `--verbose`, `--dry-run`

### converter.py
- `convert_file(path, matcher, fix)` - 處理單一檔案
- `convert_directory(path, matcher, fix)` - 處理目錄
- `process_directory()` - 主要入口，載入詞庫並處理

### matcher.py
- 使用 `pyahocorasick` 建立自動機
- `Matcher` 類別:
  - `find_matches(text)` - 找出所有匹配
  - `find_matches_with_lines(text)` - 帶行列資訊
  - `replace_all(text)` - 替換所有匹配

### dictionary.py
- `load_builtin(sources)` - 載入內建 cn/hk 詞庫
- `load_dictionary(sources, custom_path)` - 主要載入函數
- 支援簡單格式和擴展格式

---

## CLI 使用方式

```bash
# 檢查模式（只報告）
zhtw check ./src

# 修正模式（自動修改）
zhtw fix ./src

# 指定來源
zhtw check ./src --source cn      # 只處理簡體
zhtw check ./src --source hk      # 只處理港式
zhtw check ./src --source cn,hk   # 兩者都處理（預設）

# 自訂詞庫
zhtw fix ./src --dict ./custom.json

# JSON 輸出（CI/CD）
zhtw check ./src --json

# 模擬執行
zhtw fix ./src --dry-run

# 詳細輸出
zhtw check ./src --verbose
```

---

## 開發指令

```bash
# 安裝開發依賴
pip install -e ".[dev]"

# 執行測試
pytest

# 執行 lint
ruff check .

# 本地測試 CLI
python -m zhtw check ./test-files
```

---

## 詞庫格式

### 簡單格式（v1.0）
```json
{
  "version": "1.0",
  "description": "說明文字",
  "terms": {
    "简体": "繁體"
  }
}
```

### 擴展格式（v1.5+，未來支援）
```json
{
  "version": "1.5",
  "terms": {
    "文档": {
      "target": "文件",
      "category": "it",
      "confidence": 1.0,
      "context": "一般情境"
    }
  }
}
```

---

## 效能考量

- **Aho-Corasick**: O(n) 時間複雜度掃描，不受術語數量影響
- **預過濾**: 跳過不含中文字元的檔案（約 70%+）
- **預設排除**: node_modules, .git, dist, build 等
- **支援副檔名**: .py, .ts, .tsx, .js, .jsx, .java, .vue, .go, .rs, .json, .yml, .yaml, .md, .txt, .html, .css

---

## 新增詞彙

1. 找到對應的詞庫檔案（cn/ 或 hk/）
2. 新增 key-value 對
3. 確保轉換在台灣用語中正確
4. 提交 PR

範例：
```json
{
  "terms": {
    "existing_term": "existing_translation",
    "new_term": "新翻譯"
  }
}
```

---

## 未來規劃

### v2.0 LLM 整合
- 詞彙探索: 用 LLM 發現新詞彙
- 上下文感知: 依上下文判斷轉換
- 主動學習: 收集使用者修正

### v3.0 本地模型
- 微調小型中文模型
- 完全離線高準確度

---

## AI 開發注意事項

1. **不要使用 OpenCC** - 會過度轉換台灣正確用語
2. **不要呼叫外部 API** - 保持離線運作
3. **詞庫修改要謹慎** - 確認轉換在台灣用語中正確
4. **測試要全面** - 包含邊界案例和誤判測試
5. **不要新增不確定的詞彙** - 寧可少轉不要錯轉

---

*rajatim 出品*
