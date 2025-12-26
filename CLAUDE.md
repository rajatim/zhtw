# ZHTW - Claude AI 開發指南

**專案名稱**: ZHTW - 簡轉繁台灣用語轉換器
**作者**: rajatim
**語言**: Python 3.9+
**最後更新**: 2025-12-26

---

## 專案概述

將程式碼和文件中的簡體中文轉換為台灣繁體中文用語的 CLI 工具。

### 核心設計原則

1. **預設離線** - 基礎功能不需網路，LLM 功能可選
2. **術語表優先** - 只轉換明確定義的詞彙，避免過度轉換
3. **高效能** - Aho-Corasick 演算法處理大量術語
4. **可擴充** - JSON 詞庫格式，易於維護
5. **用量可控** - LLM 功能有嚴格的用量監控與限制

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
│   ├── matcher.py       # Aho-Corasick 比對器
│   ├── config.py        # 設定管理
│   ├── import_terms.py  # 詞庫匯入
│   ├── review.py        # 詞彙審核
│   ├── llm/             # LLM 模組（v2.0+）
│   │   ├── __init__.py
│   │   ├── client.py    # Gemini API 客戶端
│   │   ├── usage.py     # 用量追蹤與限制
│   │   └── prompts.py   # 提示詞範本
│   └── data/
│       └── terms/
│           ├── cn/          # 簡體 → 台灣繁體
│           │   ├── base.json
│           │   ├── it.json
│           │   └── business.json
│           ├── hk/          # 港式 → 台灣繁體
│           │   ├── base.json
│           │   └── tech.json
│           └── pending/     # 待審核詞彙
├── tests/
├── pyproject.toml
├── README.md
└── CLAUDE.md            # 本文件
```

---

## 核心模組說明

### cli.py
- 使用 `click` 框架
- 核心命令: `check`, `fix`, `stats`, `validate`
- LLM 命令: `import`, `review`, `validate-llm`, `usage`, `config`
- 參數: `--source`, `--dict`, `--exclude`, `--json`, `--verbose`, `--dry-run`

### converter.py
- `convert_file(path, matcher, fix)` - 處理單一檔案
- `convert_directory(path, matcher, fix)` - 處理目錄
- `process_directory()` - 主要入口，載入詞庫並處理

### matcher.py
- 使用 `pyahocorasick` 建立自動機
- `Matcher` 類別:
  - `find_matches(text)` - 找出所有比對
  - `find_matches_with_lines(text)` - 帶行列資訊
  - `replace_all(text)` - 替換所有比對

### dictionary.py
- `load_builtin(sources)` - 載入內建 cn/hk 詞庫
- `load_dictionary(sources, custom_path)` - 主要載入函式
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
<!-- zhtw:disable -->
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
<!-- zhtw:enable -->

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

## v2.0 LLM 模組

### config.py
- 設定管理（`~/.config/zhtw/config.json`）
- 預設限制值、pricing 計算

### llm/client.py
- `GeminiClient` - Gemini API 客戶端
- 自動用量追蹤和限制檢查
- 錯誤處理和重試機制

### llm/usage.py
- `UsageTracker` - 用量追蹤
- 每日/每月/總計統計
- 限制檢查和警告

### import_terms.py
- 從 URL 或本地檔案匯入詞庫
- 格式驗證、衝突偵測
- 儲存到 pending 目錄待審核

### review.py
- 互動式審核待匯入詞彙
- 可選 LLM 輔助驗證
- 核准後加入主詞庫

---

## 開發進度與決策記錄

### 目前版本
**v2.4.0** (2025-12-26)

### 已完成功能
| 版本 | 功能 |
|------|------|
| v1.0 | 基礎 check/fix、Aho-Corasick 演算法、JSON 輸出 |
| v1.5 | stats、validate、忽略註解 (zhtw:disable) |
| v2.0 | LLM 整合（import、review、validate-llm、usage、config） |
| v2.1 | 47 個 IT 術語、review 預設啟用 LLM |
| v2.2 | .zhtwignore 檔案支援 |
| v2.3 | --show-diff、--backup、非 git 警告 |
| v2.4 | 進度條顯示（TTY/非TTY 自動偵測） |

### 待開發功能 (GitHub Issues)

| Issue | 功能 | 優先級 | 難度評估 |
|-------|------|--------|---------|
| #11 | 瀏覽器擴充套件 (Chrome/Firefox) | 🔴 高 | 低 - 純 JS，1-2 天 MVP |
| #10 | 資料庫支援 (zhtw-db) | 🔴 高 | 中 - 核心簡單，備份機制複雜 |
| #8 | VS Code 擴充套件 | 🟡 中 | 中 |
| #6 | Office 文件支援 (zhtw-office) | 🟡 中 | 高 - 格式保留困難 |

### 技術決策記錄

1. **為什麼不用 OpenCC？**
   - OpenCC 會過度轉換（如 權限→許可權）
   - 我們使用精確術語表，寧可少轉不要錯轉

2. **Office vs 資料庫優先級？** (2025-12-26 討論)
   - 資料庫：核心邏輯簡單，但備份機制複雜（需要 dump/export）
   - Office：備份簡單（複製檔案），但格式保留困難（run 拆分問題）
   - 結論：兩者各有難處，風險不同

3. **瀏覽器擴充套件為何優先？** (2025-12-26 決定)
   - 受眾最廣（不只開發者）
   - 開發最快（純 JS）
   - 維護最輕（不依賴外部套件）
   - 推廣容易（Web Store 曝光）

4. **進度條實作** (v2.4.0)
   - TTY 模式：動態進度條 `[████░░░░] 50/100`
   - 非 TTY 模式（Jenkins）：靜態輸出 `25% (25/100)`
   - 使用 `sys.stderr.isatty()` 偵測環境

### 下次開發建議

1. **瀏覽器擴充套件 MVP** (#11)
   - 建立 `zhtw-browser/` 目錄
   - 實作右鍵選單轉換
   - 實作彈出視窗貼上轉換
   - 詞庫從 Python 版導出為 JSON

2. **或者資料庫 MVP** (#10)
   - 先做 SQLite 支援
   - `zhtw db check/fix` 命令
   - 分頁處理 + 進度條

---

## 未來規劃

### v3.0 插件架構
- zhtw-db（資料庫支援）
- zhtw-office（Office 文件支援）

### v3.1 生態整合
- 瀏覽器擴充套件
- VS Code 擴充套件

### v4.0 本地模型
- 微調小型中文模型
- 完全離線高準確度

---

## AI 開發注意事項

1. **不要使用 OpenCC** - 會過度轉換台灣正確用語
2. **核心功能保持離線** - LLM 功能是可選的
3. **詞庫修改要謹慎** - 確認轉換在台灣用語中正確
4. **測試要全面** - 包含邊界案例和誤判測試
5. **不要新增不確定的詞彙** - 寧可少轉不要錯轉
6. **LLM 用量要監控** - 使用 UsageTracker 追蹤並限制費用

---

## README 撰寫策略

### 核心原則

1. **簡單至上** - 使用者 30 秒內要能開始使用
2. **離線優先** - 強調不需要任何外部服務或 API
3. **品質保證** - 強調「人工 + LLM 雙重審稿」作為品質背書

### LLM 功能的呈現方式

- **不要**：強調使用者可以用 LLM 功能（需要設定 API key，增加使用門檻）
- **要**：強調詞庫「經過 LLM 審稿驗證」（品質保證，不需使用者操作）

LLM 相關命令（`import`, `review`, `validate-llm`, `usage`, `config`）保留在 CLI 中，但 README 不主動介紹。進階使用者可透過 `zhtw --help` 發現這些功能。

### 行銷賣點優先順序（結果導向，不講技術）

| 技術說法 | 行銷說法 |
|---------|---------|
| Aho-Corasick 演算法 | 10 萬行程式碼 < 1 秒 |
| 人工 + LLM 雙重審稿 | 零誤判，不會把「權限」改成「許可權」 |
| 完全本地執行 | 企業內網也能用 |
| JSON 輸出 | 一行指令加入 GitHub Actions |
| zhtw:disable 註解 | 標記一下就不會被改 |

### 結構

```
1. 標題 + Badge
2. Hero：讓你的程式碼說台灣話
3. 痛點共鳴：你是否遇過這些情況？
4. 理念：寧可少轉不要錯轉
5. 30 秒快速開始
6. 為什麼選 ZHTW？（賣點表格）
7. 涵蓋範圍（精簡版）
8. CI/CD 整合
9. Pre-commit Hook
10. 進階用法
11. 開發
12. 立即試試（CTA）
```

### 寫作風格

- **口語化** — 「有問題就會失敗，再也不怕漏掉」
- **結果導向** — 不講演算法，講「< 1 秒」
- **精簡** — 表格能 2 行就不要 6 行
- **有行動** — 結尾要有 CTA

### 不要寫的內容

- LLM 功能設定教學（進階使用者自己會找）
- 內部架構細節（這些放 CLAUDE.md）
- 過長的 API 文件
- 未來規劃（避免給使用者不切實際的期待）
- 技術術語（Aho-Corasick、JSON schema 等）

---

*rajatim 出品*
