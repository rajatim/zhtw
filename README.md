# ZHTW

[![CI](https://github.com/rajatim/zhtw/actions/workflows/ci.yml/badge.svg)](https://github.com/rajatim/zhtw/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/zhtw.svg)](https://pypi.org/project/zhtw/)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<!-- zhtw:disable -->
**讓你的程式碼說台灣話** — 專治「許可權」「軟件」等違和用語
<!-- zhtw:enable -->

---

## 你是否遇過這些情況？

<!-- zhtw:disable -->
- Code review 被指出「伺服器」寫成「服务器」
- 用 OpenCC 轉換，結果「權限」變成「許可權」
- 文件裡混著「用戶」和「使用者」，不知道漏了哪些
<!-- zhtw:enable -->

**ZHTW** 就是為了解決這個問題。

---

## 我們的理念

> 寧可少轉，不要錯轉

通用轉換工具會過度轉換，把台灣正確的詞也改掉。我們不一樣：**只轉確定要改的詞，其他一律不動。**

---

## 30 秒開始使用

```bash
python3 -m pip install zhtw

zhtw check .    # 檢查整個專案
zhtw fix .      # 自動修正
```

<details>
<summary>zhtw 指令找不到？設定 PATH</summary>

```bash
# macOS (zsh)
echo 'export PATH="$PATH:$(python3 -m site --user-base)/bin"' >> ~/.zshrc
source ~/.zshrc

# Linux (bash)
echo 'export PATH="$PATH:~/.local/bin"' >> ~/.bashrc
source ~/.bashrc

# Windows — 通常自動設定，若無請加入環境變數：
# %APPDATA%\Python\PythonXX\Scripts
```
</details>

<!-- zhtw:disable -->
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
<!-- zhtw:enable -->

---

## 為什麼選 ZHTW？

| | |
|------|------|
| **零誤判** | 433 個術語，人工 + AI 雙重審稿，不會把「權限」改成「許可權」 |
| **秒級掃描** | 10 萬行程式碼 < 1 秒，大型專案也不怕 |
| **完全離線** | 不傳送任何資料到外部，企業內網也能用 |
| **CI 整合** | 一行指令加入 GitHub Actions，PR 自動檢查 |
| **彈性跳過** | 測試資料、第三方程式碼？標記一下就不會被改 |

---

## 涵蓋範圍

**433 個精選術語**，兩岸三地都顧到：

<!-- zhtw:disable -->
| 來源 | 範例 |
|------|------|
| 簡體 → 台灣 | 程序→程式、软件→軟體、服务器→伺服器、用户→使用者 |
| 港式 → 台灣 | 視像→視訊、軟件→軟體、數據庫→資料庫 |
<!-- zhtw:enable -->

---

## CI/CD 整合

加入 GitHub Actions，每個 PR 自動檢查：

```yaml
# .github/workflows/chinese-check.yml
- name: 檢查繁體中文用語
  run: |
    pip install zhtw
    zhtw check ./src --json
```

有問題就會失敗，再也不怕漏掉。

---

## Pre-commit Hook

Commit 前自動擋住問題：

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/rajatim/zhtw
    rev: v2.3.0
    hooks:
      - id: zhtw-check
```

```bash
pip install pre-commit && pre-commit install
# 之後每次 commit 都會自動檢查
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

# 驗證詞庫品質（檢查衝突和無效轉換）
zhtw validate

# 詳細輸出
zhtw check ./src --verbose
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

## 立即試試

```bash
python3 -m pip install zhtw && zhtw check .
```

有問題？[開 Issue](https://github.com/rajatim/zhtw/issues) | 想貢獻？[看 Contributing Guide](CONTRIBUTING.md)

---

MIT License | **rajatim 出品**
