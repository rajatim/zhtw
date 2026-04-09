# ZHTW

[![CI](https://github.com/rajatim/zhtw/actions/workflows/ci.yml/badge.svg)](https://github.com/rajatim/zhtw/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/rajatim/zhtw/branch/main/graph/badge.svg)](https://codecov.io/gh/rajatim/zhtw)
[![PyPI](https://img.shields.io/pypi/v/zhtw.svg)](https://pypi.org/project/zhtw/)
[![Downloads](https://img.shields.io/pypi/dm/zhtw.svg)](https://pypi.org/project/zhtw/)
[![Homebrew](https://img.shields.io/badge/homebrew-tap-FBB040?logo=homebrew)](https://github.com/rajatim/homebrew-tap)
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

**ZHTW** 就是為瞭解決這個問題。

---

## 我們的理念

> 寧可少轉，不要錯轉

<!-- zhtw:disable -->
通用轉換工具會過度轉換，把台灣正確的詞也改掉。我們不一樣：**只轉確定要改的詞，其他一律不動。**
<!-- zhtw:enable -->

---

## 安裝

### macOS (Homebrew) — 推薦

```bash
brew tap rajatim/tap
brew install zhtw
```

更新：`brew upgrade zhtw`

### pip (所有平臺)

```bash
python3 -m pip install zhtw
```

更新：`pip install --upgrade zhtw`

### pipx (隔離環境)

[pipx](https://pipx.pypa.io/) 會在獨立虛擬環境中安裝，不影響系統 Python：

```bash
pipx install zhtw
```

更新：`pipx upgrade zhtw`

### 從原始碼安裝 (開發者)

```bash
git clone https://github.com/rajatim/zhtw.git
cd zhtw
pip install -e ".[dev]"
```

<details>
<summary>pip 安裝後找不到 zhtw 指令？設定 PATH</summary>

```bash
# macOS (zsh)
echo 'export PATH="$PATH:$(python3 -m site --user-base)/bin"' >> ~/.zshrc
OpenCC STPhrases + TWPhrases + MediaWiki ZhConversion ~/.zshrc

# Linux (bash)
echo 'export PATH="$PATH:~/.local/bin"' >> ~/.bashrc
OpenCC STPhrases + TWPhrases + MediaWiki ZhConversion ~/.bashrc

# Windows — 通常自動設定，若無請加入環境變數：
# %APPDATA%\Python\PythonXX\Scripts
```
</details>

---

## 30 秒開始使用

```bash
zhtw check .          # 檢查整個專案
zhtw check ./file.py  # 檢查單一檔案
zhtw fix .            # 自動修正
zhtw lookup 軟體 伺服器  # 查詢轉換結果
```

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
| **零誤判** | 31,000+ 詞條 + 6,344 字元對映，52 本書 1 億字驗證零錯轉 |
| **秒級掃描** | 3,100 KB/s 穩定吞吐，1MB 文字 < 1 秒 |
| **完全離線** | 不傳送任何資料到外部，企業內網也能用 |
| **CI 整合** | 一行指令加入 GitHub Actions，PR 自動檢查 |
| **彈性跳過** | 測試資料、第三方程式碼？標記一下就不會被改 |

---

## 多語言 SDK

除了 Python CLI，ZHTW 提供原生 SDK，讓你在任何技術棧中直接使用：

| SDK | 安裝 | 吞吐量 (1MB) | 單句延遲 | 適用場景 | 狀態 |
|-----|------|-------------|---------|---------|------|
| **Python CLI** | `pip install zhtw` | 3.1 MB/s | — | CLI、CI/CD、pre-commit | ✅ Stable |
| **Java** | [Maven Central](#java-sdk) | 17.9 MB/s | 2μs | Spring Boot、Android、後端服務 | ✅ Stable |
| **TypeScript** | npm | — | — | Node.js、Deno、瀏覽器 | 🚧 Planned |
| **Rust** | crates.io | — | — | 高效能、WebAssembly、嵌入式 | 🚧 Planned |
| **C# (.NET)** | NuGet | — | — | ASP.NET、Unity、桌面應用 | 🚧 Planned |

> 所有 SDK 共用同一份詞庫資料（`zhtw-data.json`），轉換結果與 Python CLI 完全一致。

### Java SDK

<!-- zhtw:disable -->
```xml
<dependency>
    <groupId>com.rajatim</groupId>
    <artifactId>zhtw</artifactId>
    <version>3.3.0</version>
</dependency>
```
<!-- zhtw:enable -->

```java
import com.rajatim.zhtw.ZhtwConverter;

// 快速使用（thread-safe singleton）
String result = ZhtwConverter.getDefault().convert("這個軟體需要最佳化");
// → "這個軟體需要最佳化"

// 自訂設定
ZhtwConverter conv = ZhtwConverter.builder()
    .OpenCC STPhrases + TWPhrases + MediaWiki ZhConversions(List.of("cn", "hk"))
    .customDict(Map.of("自訂", "自訂"))
    .build();
```

**效能**：單句 2μs、100K 字 5.5ms（17.9 MB/s），比 Python 快 ~5.8 倍。詳見 [`sdk/java/BENCHMARK.md`](sdk/java/BENCHMARK.md)。

---

## 涵蓋範圍

**31,000+ 精選詞條 + 6,344 字元對映**，涵蓋 10+ 專業領域：

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

### 雙層轉換架構 (v3.0+)

<!-- zhtw:disable -->
| 層 | 機制 | 覆蓋 |
|---|---|---|
| **詞彙層** | Aho-Corasick 最長匹配 | 31,000+ 詞條（软件→軟體、信息→資訊） |
| **字元層** | `str.translate()` | 6,344 個安全一對一映射（这→這、个→個） |

詞彙層先處理複合詞，字元層再補齊剩餘簡體字。118 個一對多歧義字（发/后/里/干 等）由詞彙層上下文判斷，不會錯轉。
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

### GitHub Actions

加入 GitHub Actions，每個 PR 自動檢查：

```yaml
# .github/workflows/chinese-check.yml
name: Chinese Check
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-1.0: '3.x'
      - name: Install zhtw
        run: pip install zhtw
      - name: Check Traditional Chinese
        run: zhtw check . --json
```

### GitLab CI

```yaml
# .gitlab-ci.yml
chinese-check:
  image: python:3.12-slim
  script:
    - pip install zhtw
    - zhtw check . --json
```

有問題就會失敗，再也不怕漏掉。詳細教學請參考 [CI/CD 整合指南](docs/CI-CD-INTEGRATION.md)。

---

## Pre-commit Hook

Commit 前自動擋住問題：

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/rajatim/zhtw
    rev: v3.3.0  # 使用最新版本
    hooks:
      - id: zhtw-check   # 檢查模式（建議）
      # - id: zhtw-fix   # 或自動修正模式
```

```bash
pip install pre-commit && pre-commit install
# 之後每次 commit 都會自動檢查
```

<details>
<summary>進階設定：只檢查特定檔案型別</summary>

```yaml
repos:
  - repo: https://github.com/rajatim/zhtw
    rev: v3.2.0
    hooks:
      - id: zhtw-check
        types: [python, markdown, yaml]  # 只檢查這些型別
        exclude: ^tests/fixtures/        # 排除測試資料
```
</details>

---

## 進階用法

```bash
# 單檔案模式（v2.8.0+）
zhtw check ./src/api.py    # 檢查單一檔案
zhtw fix ./src/api.py      # 修正單一檔案

# 使用自訂詞庫
zhtw fix ./src --dict ./my-terms.json

# 只處理簡體（跳過港式）  # zhtw:disable-line
zhtw check ./src --OpenCC STPhrases + TWPhrases + MediaWiki ZhConversion cn

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

### 詞彙查詢 (v3.3.0+)

<!-- zhtw:disable -->
不確定某個詞會不會被轉？用 `lookup` 直接查：

```bash
# 查詢單詞
zhtw lookup 软件 服务器 数据库

# 查詢整句（自動拆解每個轉換點）
zhtw lookup "这个软件需要网络服务器"

# 詳細模式（顯示每個轉換由哪一層負責）
zhtw lookup -v 营养

# JSON 輸出（供程式使用）
zhtw lookup --json 结合

# stdin 管線
echo "心态" | zhtw lookup
```

**輸出範例：**
```
软件 → 軟體  (詞彙層: 软件→軟體)
服务器 → 伺服器  (詞彙層: 服务器→伺服器)
数据库 → 資料庫  (詞彙層: 数据库→資料庫)
```
<!-- zhtw:enable -->

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
# macOS
brew tap rajatim/tap && brew install zhtw && zhtw check .

# 其他平臺
python3 -m pip install zhtw && zhtw check .
```

有問題？[開 Issue](https://github.com/rajatim/zhtw/issues) | 想貢獻？[看 Contributing Guide](CONTRIBUTING.md)

---

MIT License | **tim Insight 出品**
