# ZHTW

**繁體中文** · [English](README.en.md)

[![CI](https://github.com/rajatim/zhtw/actions/workflows/ci.yml/badge.svg)](https://github.com/rajatim/zhtw/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/rajatim/zhtw/branch/main/graph/badge.svg)](https://codecov.io/gh/rajatim/zhtw)
[![PyPI](https://img.shields.io/pypi/v/zhtw.svg)](https://pypi.org/project/zhtw/)
[![Maven Central](https://img.shields.io/maven-central/v/com.rajatim/zhtw.svg?label=maven%20central)](https://central.sonatype.com/artifact/com.rajatim/zhtw)
[![Homebrew](https://img.shields.io/badge/homebrew-tap-FBB040?logo=homebrew)](https://github.com/rajatim/homebrew-tap)
[![Downloads](https://img.shields.io/pypi/dm/zhtw.svg)](https://pypi.org/project/zhtw/)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Java](https://img.shields.io/badge/java-11+-orange.svg)](https://adoptium.net/)
[![Go](https://img.shields.io/badge/go-1.21+-00ADD8.svg?logo=go)](https://pkg.go.dev/github.com/rajatim/zhtw/sdk/go/v4/zhtw)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<!-- zhtw:disable -->
**讓你的程式碼說台灣話** — 專治「許可權」「軟件」等違和用語
<!-- zhtw:enable -->

<!-- zhtw:disable -->
```
輸入：服务器上的软件需要优化，用户权限请联系管理员
輸出：伺服器上的軟體需要最佳化，使用者權限請聯絡管理員
```
<!-- zhtw:enable -->

一行程式、一個 CLI、五種語言 SDK —— 把簡體轉成**真正的台灣繁體**。

---

## 為什麼選 ZHTW？

> **寧可少轉，不要錯轉**

通用轉換工具會過度轉換，把台灣正確的詞也改掉。我們不一樣：**只轉確定要改的詞，其他一律不動。**

| | |
|------|------|
| **零誤判** | 31,000+ 詞條 + 6,360 字元對映，52 本書 1 億字驗證零錯轉 |
| **秒級掃描** | 3,100 KB/s 穩定吞吐，1MB 文字 < 1 秒 |
| **完全離線** | 不傳送任何資料到外部，企業內網也能用 |
| **CI 整合** | 一行指令加入 GitHub Actions，PR 自動檢查 |
| **彈性跳過** | 測試資料、第三方程式碼？標記一下就不會被改 |

### 對比 OpenCC

<!-- zhtw:disable -->
OpenCC 是通用的繁簡轉換框架，採用「全字元 + 短語替換」策略，規則之間容易互相牴觸，例如 `权→權` 會把「權限」誤轉成「許可權」。ZHTW 專注於**簡體 → 台灣繁體**一個方向，用「詞彙層 + 字元層」分層處理，複合詞上下文優先匹配。

| | OpenCC (s2twp) | ZHTW |
|---|------|------|
| **設計目標** | 通用繁簡多變體轉換 | 簡體 → 台灣繁體 |
| **轉換策略** | 字元 + 短語全量替換 | 詞彙優先 → 字元層補齊 |
| **歧義處理** | 依規則順序 | 102 個歧義字分級管理 + balanced mode 語義消歧 |
| **詞庫規模** | 內建字表 + 短語 | 31,000+ 精選台灣用詞 |
| **誤轉** | `权限 → 許可權` 等常見案例 | 52 本書 1 億字驗證零錯轉 |
| **生態** | C++ 核心、多語言 bindings | CLI + Python/Java/TS/Rust SDK + pre-commit |

想看更多對比案例？執行 `zhtw lookup 权限 服务器 用户`。
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
source ~/.zshrc

# Linux (bash)
echo 'export PATH="$PATH:~/.local/bin"' >> ~/.bashrc
source ~/.bashrc

# Windows — 通常自動設定，若無請加入環境變數：
# %APPDATA%\Python\PythonXX\Scripts
```
</details>

---

## 30 秒開始使用

ZHTW 提供三種使用方式，選一個最適合你的場景：

### 1. CLI（命令列）

<!-- zhtw:disable -->
```bash
zhtw check .            # 檢查整個專案
zhtw check ./file.py    # 檢查單一檔案
zhtw fix .              # 自動修正
zhtw lookup 软件 服务器  # 查詢：软件→軟體、服务器→伺服器

# Balanced mode：自動消歧 10 個高頻歧義字（几→幾、后→後、里→裡 等）
zhtw fix . --ambiguity-mode balanced
```
<!-- zhtw:enable -->

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

### 2. Python Library

<!-- zhtw:disable -->
```python
from zhtw import convert

convert("这个软件需要优化")
# → "這個軟體需要最佳化"
```
<!-- zhtw:enable -->

首次呼叫會載入字典並建立 Aho-Corasick 自動機，後續呼叫會重用快取。進階用法（自訂詞庫、逐行回報、整合到你自己的 pipeline）見 `convert_text` / `Matcher` / `load_dictionary`。詞彙查詢 API：`lookup_word` / `lookup_words`（v3.3.0+）。

### 3. Java SDK

**Maven**：

<!-- zhtw:disable -->
```xml
<dependency>
    <groupId>com.rajatim</groupId>
    <artifactId>zhtw</artifactId>
    <version>4.2.0</version>
</dependency>
```
<!-- zhtw:enable -->

**Gradle (Kotlin DSL)**：

```kotlin
implementation("com.rajatim:zhtw:4.2.0")
```

**Gradle (Groovy DSL)**：

```groovy
implementation 'com.rajatim:zhtw:4.2.0'
```

<!-- zhtw:disable -->
```java
import com.rajatim.zhtw.ZhtwConverter;

// 快速使用（thread-safe singleton）
String result = ZhtwConverter.getDefault().convert("这个软件需要优化");
// → "這個軟體需要最佳化"

// 自訂設定
ZhtwConverter conv = ZhtwConverter.builder()
    .sources(List.of("cn", "hk"))
    .customDict(Map.of("自定义", "自訂"))
    .ambiguityMode("balanced")  // 歧義字自動消歧
    .build();
```
<!-- zhtw:enable -->

**效能**：單句 2μs、100K 字 5.5ms（17.9 MB/s），比 Python 快 ~5.8 倍。詳見 [`sdk/java/BENCHMARK.md`](sdk/java/BENCHMARK.md)。

### 4. TypeScript SDK

**npm / pnpm / yarn**：

```bash
npm install zhtw-js
# 或
pnpm add zhtw-js
yarn add zhtw-js
```

<!-- zhtw:disable -->
```typescript
import { convert, check, lookup } from 'zhtw-js';

// 快速使用（zero config，內建 default converter）
convert('这个软件需要优化');
// → '這個軟體需要最佳化'

check('用户权限');
// → [{ start, end, source, target }, ...]

lookup('软件');
// → { input, output, changed, details: [...] }
```
<!-- zhtw:enable -->

**自訂設定**：

<!-- zhtw:disable -->
```typescript
import { createConverter } from 'zhtw-js';

const conv = createConverter({
  sources: ['cn'],                  // 預設 ['cn', 'hk']
  customDict: { '自定义': '自訂' },  // 覆蓋內建詞條
  ambiguityMode: 'balanced',        // 歧義字自動消歧
});

conv.convert('...');
```
<!-- zhtw:enable -->

**特色**：isomorphic（Node.js ≥20 + 瀏覽器原生支援）、ESM + CJS 雙產出、零執行期相依、tree-shakeable。所有索引（`start` / `end` / `position`）均為 **Unicode codepoint**，與 Python CLI、Java SDK 完全 byte-for-byte 一致（共享 `sdk/data/golden-test.json` 驗證）。釋出走 npm Trusted Publishing (OIDC)，無 long-lived token。

### 5. Rust SDK

**Cargo (crates.io)**：

<!-- zhtw:disable -->
```toml
[dependencies]
zhtw = "4.2.0"
```
<!-- zhtw:enable -->

<!-- zhtw:disable -->
```rust
use zhtw::{AmbiguityMode, Converter, Source};

// Zero config
assert_eq!(zhtw::convert("这个软件需要优化"), "這個軟體需要最佳化");

// Builder with custom dict + balanced mode
let conv = Converter::builder()
    .sources([Source::Cn])
    .custom_dict([("自定义", "自訂")])
    .ambiguity_mode(AmbiguityMode::Balanced)  // 歧義字自動消歧
    .build()
    .expect("non-empty sources");
```
<!-- zhtw:enable -->

**效能**：build-time 預編譯 `daachorse` automaton + `phf` char map，runtime 零建構成本。詳見 benchmarks（`cargo bench -p zhtw`）。

### 6. Go SDK

<!-- zhtw:disable -->
```bash
go get github.com/rajatim/zhtw/sdk/go/v4@latest
```
<!-- zhtw:enable -->

<!-- zhtw:disable -->
```go
package main

import (
	"fmt"
	"github.com/rajatim/zhtw/sdk/go/v4/zhtw"
)

func main() {
	// 零設定
	fmt.Println(zhtw.Convert("这个软件需要优化"))
	// → "這個軟體需要最佳化"

	// Builder：自訂詞典 + balanced mode
	conv, _ := zhtw.NewBuilder().
		Sources(zhtw.SourceCn).
		CustomDict(map[string]string{"自定义": "自訂"}).
		SetAmbiguityMode(zhtw.AmbiguityBalanced).
		Build()
	fmt.Println(conv.Convert("自定义几个里程碑"))
}
```
<!-- zhtw:enable -->

**特色**：`go:embed` 內嵌字典、零外部依賴、goroutine-safe。Go 1.21+，支援 `go get` 直接安裝。所有索引均為 Unicode codepoint，跨 SDK golden-test 驗證。

---

## 多語言 SDK

ZHTW 以 Python 實作為主，並提供原生 Java、TypeScript、Rust、Go 五種語言 SDK；另提供 1 個 WebAssembly 套件（`zhtw-wasm`）。所有 SDK 共用同一份詞庫資料（`zhtw-data.json`），轉換結果與 Python CLI 完全一致（跨 SDK 透過共享 `sdk/data/golden-test.json` 做 byte-for-byte 驗證，零偏差為釋出條件）。所有 SDK 均支援 balanced mode（歧義字自動消歧）。

| SDK | 安裝 | 吞吐量 (1MB) | 單句延遲 | 適用場景 | 狀態 |
|-----|------|-------------|---------|---------|------|
| **Python** | `pip install zhtw` | 3.1 MB/s | — | CLI、CI/CD、pre-commit、資料處理 | ✅ Stable |
| **Java** | [Maven Central](#3-java-sdk) | 17.9 MB/s | 2μs | Spring Boot、Android、後端服務 | ✅ Stable |
| **TypeScript** | `npm install zhtw-js` | ~16 MB/s | — | Node.js ≥18、瀏覽器（isomorphic ESM+CJS） | ✅ Stable |
| **Rust** | [crates.io](#5-rust-sdk) | — | — | 高效能、嵌入式 | ✅ Stable |
| **WASM** | `npm install zhtw-wasm` | — | — | 瀏覽器、Edge runtime | ✅ Stable |
| **Go** | [`go get`](#6-go-sdk) | — | — | 微服務、CLI 工具、雲端原生 | ✅ Stable |
| **C# (.NET)** | NuGet | — | — | ASP.NET、Unity、桌面應用 | 🚧 Planned |

---

## 涵蓋範圍

<!-- zhtw:disable -->
**31,000+ 精選詞條 + 6,360 字元對映**，涵蓋 IT 科技、醫療、法律、金融、遊戲、電商、學術、日常、地理、港式用語 10+ 領域。轉換由三層架構負責：**詞彙層**（Aho-Corasick 最長匹配）處理複合詞，**balanced defaults 層**（`--ambiguity-mode balanced`）處理 10 個高頻歧義字（几→幾、后→後、里→裡 等）的預設轉換 + protect_terms 例外保護，**字元層**（`str.translate`）補齊剩餘簡體字。102 個一對多歧義字分級管理，不確定就不轉。
<!-- zhtw:enable -->

詳細的詞庫分類、雙層架構原理、一對多特例、語義衝突處理表，見 [`docs/DICTIONARY-COVERAGE.md`](docs/DICTIONARY-COVERAGE.md)。

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
          python-version: '3.x'
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
    rev: v4.2.0  # 使用最新版本
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
    rev: v4.2.0
    hooks:
      - id: zhtw-check
        types: [python, markdown, yaml]  # 只檢查這些型別
        exclude: ^tests/fixtures/        # 排除測試資料
```
</details>

---

## 忽略特定程式碼

測試資料、第三方程式碼不想被轉？用 pragma 標記即可：

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

專案層級的忽略用 `.zhtwignore`（類 `.gitignore` 格式）；完整範例見 [`docs/CLI-ADVANCED.md`](docs/CLI-ADVANCED.md#zhtwignore-忽略檔案)。

---

<!-- zhtw:disable -->
## 文件

| 文件 | 內容 |
|------|------|
| [`docs/DICTIONARY-COVERAGE.md`](docs/DICTIONARY-COVERAGE.md) | 完整詞庫分類、雙層架構細節、一對多特例、語義衝突處理 |
| [`docs/CLI-ADVANCED.md`](docs/CLI-ADVANCED.md) | 完整 CLI 引數、詞彙查詢（`lookup`）、多編碼支援、自訂詞庫格式 |
| [`docs/CI-CD-INTEGRATION.md`](docs/CI-CD-INTEGRATION.md) | GitHub Actions / GitLab CI / pre-commit 深入設定 |
| [`sdk/java/BENCHMARK.md`](sdk/java/BENCHMARK.md) | Java SDK 效能測試（JMH） |
| [`CHANGELOG.md`](CHANGELOG.md) | 版本歷史 |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | 貢獻指南 |
<!-- zhtw:enable -->

---

## 開發

```bash
pip install -e ".[dev]"
pytest
ruff check .
```

有問題？[開 Issue](https://github.com/rajatim/zhtw/issues) | 想貢獻？[看 Contributing Guide](CONTRIBUTING.md)

---

MIT License | **tim Insight 出品**
