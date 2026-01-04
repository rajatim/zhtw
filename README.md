# ZHTW

[![CI](https://github.com/rajatim/zhtw/actions/workflows/ci.yml/badge.svg)](https://github.com/rajatim/zhtw/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/rajatim/zhtw/branch/main/graph/badge.svg)](https://codecov.io/gh/rajatim/zhtw)
[![PyPI](https://img.shields.io/pypi/v/zhtw.svg)](https://pypi.org/project/zhtw/)
[![Downloads](https://img.shields.io/pypi/dm/zhtw.svg)](https://pypi.org/project/zhtw/)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
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

<!-- zhtw:disable -->
通用轉換工具會過度轉換，把台灣正確的詞也改掉。我們不一樣：**只轉確定要改的詞，其他一律不動。**
<!-- zhtw:enable -->

---

## 30 秒開始使用

```bash
python3 -m pip install zhtw

zhtw check .          # 檢查整個專案
zhtw check ./file.py  # 檢查單一檔案
zhtw fix .            # 自動修正
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
| **零誤判** | 3,490 個術語，人工 + AI 雙重審稿，不會把「權限」改成「許可權」 |
| **秒級掃描** | 10 萬行程式碼 < 1 秒，大型專案也不怕 |
| **完全離線** | 不傳送任何資料到外部，企業內網也能用 |
| **CI 整合** | 一行指令加入 GitHub Actions，PR 自動檢查 |
| **彈性跳過** | 測試資料、第三方程式碼？標記一下就不會被改 |

---

## 涵蓋範圍

**3,490 個精選術語**，涵蓋 10+ 專業領域：

<!-- zhtw:disable -->
| 領域 | 詞彙數 | 範例 |
|------|--------|------|
| **IT 科技** | 380+ | 软件→軟體、服务器→伺服器、缓存→快取、异步→非同步 |
| **醫療健康** | 230+ | 心脏病→心臟病、胰岛素→胰島素、核磁共振→核磁共振 |
| **法律合規** | 170+ | 知识产权→智慧財產權、劳动合同→勞動契約、诉讼→訴訟 |
| **金融財務** | 140+ | 股票→股票、期权→選擇權、市盈率→本益比、理财→理財 |
| **遊戲娛樂** | 150+ | 氪金→課金、副本→副本、充值→儲值、段位→段位 |
| **電商零售** | 110+ | 购物车→購物車、优惠券→優惠券、物流→物流 |
| **學術教育** | 110+ | 博士生→博士生、论文→論文、奖学金→獎學金 |
| **日常生活** | 230+ | 地铁→地鐵、空调→冷氣、塑料→塑膠、自行车→腳踏車 |
| **地理國名** | 160+ | 意大利→義大利、悉尼→雪梨、新西兰→紐西蘭 |
| **港式用語** | 60+ | 視像→視訊、軟件→軟體、數據庫→資料庫 |
<!-- zhtw:enable -->

### 一對多字形完整支援

<!-- zhtw:disable -->
很多簡體字對應多個繁體字，我們用 **「預設 + 特例覆蓋」** 策略精準處理：

| 簡體 | 情境 | 繁體 | 範例 |
|-----|------|-----|------|
| 发 | 一般 | 發 | 发送→發送、发展→發展 |
| 发 | 毛髮 | 髮 | 头发→頭髮、理发→理髮 |
| 面 | 一般 | 面 | 面试→面試、表面→表面 |
| 面 | 食物 | 麵 | 面条→麵條、方便面→泡麵 |
| 里 | 內部 | 裡 | 心里→心裡、这里→這裡 |
| 里 | 距離 | 里 | 公里→公里、英里→英里 |
| 干 | 乾燥 | 乾 | 干净→乾淨、饼干→餅乾 |
| 干 | 幹部 | 幹 | 干部→幹部、树干→樹幹 |

**完整覆蓋 22 個一對多危險字**：发/面/里/干/只/台/后/余/松/斗/谷/系/范/征/钟/冲/历/复/制/准/几/云
<!-- zhtw:enable -->

### 語義衝突智慧處理

<!-- zhtw:disable -->
同一個詞在不同語境有不同翻譯？我們用複合詞優先匹配解決：

| 詞彙 | UI 介面 | 法律/電競 |
|-----|---------|----------|
| 禁用 | 禁用功能 → **停用**功能 | 禁用角色 → **禁用**角色 |
| 撤销 | 撤销操作 → **復原**操作 | 撤销合同 → **撤銷**合同 |
| 注销 | 注销账户 → **登出**帳戶 | 注销公司 → **註銷**公司 |
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
    rev: v2.8.0
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
# 單檔案模式（v2.8.0+）
zhtw check ./src/api.py    # 檢查單一檔案
zhtw fix ./src/api.py      # 修正單一檔案

# 使用自訂詞庫
zhtw fix ./src --dict ./my-terms.json

# 只處理簡體（跳過港式）  # zhtw:disable-line
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

### 多編碼支援 (v2.5.0+)

自動偵測並處理 Big5、GBK 等舊編碼檔案：

```bash
# 自動偵測編碼（預設）
zhtw fix ./legacy-code/

# 強制輸出為 UTF-8
zhtw fix ./big5-files/ --output-encoding utf-8

# 保留原編碼
zhtw fix ./mixed/ --output-encoding keep

# CI/CD 模式（無互動確認）
zhtw fix ./src/ --yes
# 或用環境變數
ZHTW_YES=1 zhtw fix ./src/
```

**支援編碼**: UTF-8 (含 BOM)、Big5、GBK、GB2312、GB18030

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

<!-- zhtw:disable -->
```json
{
  "version": "1.0",
  "description": "我的專案術語",
  "terms": {
    "自定义": "自訂"
  }
}
```
<!-- zhtw:enable -->

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
