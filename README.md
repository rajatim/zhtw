# ZHTW

[![CI](https://github.com/rajatim/zhtw/actions/workflows/ci.yml/badge.svg)](https://github.com/rajatim/zhtw/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/zhtw.svg)](https://pypi.org/project/zhtw/)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**專為程式碼和技術文件設計的簡繁轉換工具**

---

## 我們的理念

> 寧可少轉，不要錯轉

通用的簡繁轉換工具很棒，但程式碼和技術文件有自己的術語習慣。「權限」在台灣就是「權限」，不需要變成「許可權」；「代码」應該轉成「程式碼」，而不是保持原樣。

**ZHTW** 專注於這個場景：用精選的術語表，確保每一個轉換都符合台灣開發者的用語習慣。

---

## 30 秒開始使用

```bash
# 安裝
pip install zhtw

# 檢查（只報告，不修改）
zhtw check ./src

# 修正（自動修改檔案）
zhtw fix ./src
```

**輸出範例：**
```
📁 掃描 ./src

📄 src/components/Header.tsx
   L12:5: "用户" → "使用者"

📄 src/utils/api.ts
   L8:10: "软件" → "軟體"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  發現 2 處需修正（2 個檔案）
```

---

## 特點

| | |
|------|------|
| **精準** | 433 個人工驗證術語，每個轉換都經過確認 |
| **快速** | Aho-Corasick 演算法，萬級檔案秒級掃描 |
| **離線** | 完全本地執行，不傳送任何資料到外部 |
| **CI 友善** | JSON 輸出，輕鬆整合 GitHub Actions / Jenkins |
| **可控** | 支援 `zhtw:disable` 註解跳過特定程式碼 |

---

## 術語涵蓋範圍

我們維護 **433 個精選術語**，涵蓋：

- **簡體 IT 術語** — 程序→程式、软件→軟體、服务器→伺服器
- **簡體商業用語** — 信息→資訊、用户→使用者
- **港式繁體差異** — 視像→視訊、軟件→軟體

| 來源 | 類別 | 詞彙數 |
|------|------|--------|
| 簡體 | 基礎詞彙 | 151 |
| 簡體 | IT 術語 | 132 |
| 簡體 | 商業用語 | 42 |
| 簡體 | 擴充詞彙 | 47 |
| 港式 | 基礎詞彙 | 42 |
| 港式 | 科技術語 | 19 |

---

## CI/CD 整合

```yaml
# .github/workflows/chinese-check.yml
- name: 檢查繁體中文用語
  run: |
    pip install zhtw
    zhtw check ./src --json
```

發現問題時會自動失敗，確保程式碼品質。

---

## Pre-commit Hook

在 commit 前自動檢查：

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/rajatim/zhtw
    rev: v2.3.0
    hooks:
      - id: zhtw-check
```

```bash
# 安裝
pip install pre-commit
pre-commit install

# 之後每次 commit 都會自動檢查
git commit -m "feat: 新功能"
# Check Simplified Chinese...............Passed
```

---

## 進階用法

```bash
# 使用自訂詞庫
zhtw fix ./src --dict ./my-terms.json

# 只處理簡體（跳過港式）
zhtw check ./src --source cn

# 排除目錄
zhtw check ./src --exclude node_modules,dist

# 模擬執行（不實際修改）
zhtw fix ./src --dry-run

# 預覽修改（確認後才執行）
zhtw fix ./src --show-diff

# 備份後修改
zhtw fix ./src --backup

# 顯示詞庫統計
zhtw stats
```

### 忽略特定程式碼

```python
# 忽略這一行
test_data = "软件"  # zhtw:disable-line

# 忽略下一行
# zhtw:disable-next
legacy_code = "用户信息"

# 忽略整個區塊
# zhtw:disable
test_cases = ["软件", "硬件", "网络"]
# zhtw:enable
```

### .zhtwignore 忽略檔案

在專案根目錄建立 `.zhtwignore` 檔案，排除不需檢查的目錄或檔案：

```gitignore
# 測試目錄
tests/

# 詞庫檔案（本來就是簡體）
src/data/terms/

# 特定檔案
legacy-code.py
```

支援目錄模式（結尾 `/`）和檔案 glob 模式。

### 自訂詞庫格式

```json
{
  "version": "1.0",
  "description": "我的專案術語",
  "terms": {
    "自定义": "自訂"
  }
}
```

---

## 開發

```bash
pip install -e ".[dev]"
pytest
ruff check .
```

---

MIT License | **rajatim 出品**
