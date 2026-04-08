# zhtw export + Multi-Language SDK Design

> **Sub-project 1 of 6** — export 指令、共享資料格式、golden test、Makefile 骨架

## Goal

在 zhtw CLI 新增 `export` 指令，產出標準化 JSON 資料檔，建立 Monorepo 骨架讓六個語言 SDK（Java、TypeScript、Rust、Go、.NET）能共用同一份轉換資料，並透過 golden test 確保所有 SDK 輸出與 Python 一致。

## Architecture

zhtw 的核心價值是 31,000+ 精選詞條和 6,345 字元對映。`zhtw export` 將這些資料從 Python 內部格式匯出為語言無關的 JSON，放在 `sdk/data/`。各語言 SDK 在 build 時將此 JSON 嵌入為 reOpenCC STPhrases + TWPhrases + MediaWiki ZhConversion，用原生 Aho-Corasick 函式庫實作轉換引擎。

Monorepo 結構，GitHub Actions path filter 各自觸發，`make release` 一鍵全發。

## Monorepo 目錄結構

```
zhtw/
├── src/zhtw/                        # Python（現有，不動）
│   └── export.py                    # 新增：export 模組
├── sdk/
│   ├── data/
│   │   ├── zhtw-data.json           # export 產出：charmap + terms
│   │   └── golden-test.json         # export 產出：一致性測試
│   ├── java/
│   │   ├── pom.xml
│   │   └── src/main/java/com/rajatim/zhtw/
│   │       ├── ZhtwConverter.java
│   │       ├── Matcher.java
│   │       ├── Match.java
│   │       └── LookupResult.java
│   ├── typescript/
│   │   ├── package.json
│   │   └── src/
│   │       ├── index.ts
│   │       ├── converter.ts
│   │       └── matcher.ts
│   ├── rust/
│   │   ├── Cargo.toml
│   │   └── src/
│   │       ├── lib.rs
│   │       ├── converter.rs
│   │       └── matcher.rs
│   ├── go/
│   │   ├── go.mod
│   │   ├── converter.go
│   │   └── matcher.go
│   └── dotnet/
│       ├── Zhtw.csproj
│       └── src/
│           ├── ZhtwConverter.cs
│           └── Matcher.cs
├── Makefile                         # 統一操作入口
└── .github/workflows/
    ├── ci.yml                       # Python（現有）
    ├── sdk-java.yml
    ├── sdk-typescript.yml
    ├── sdk-rust.yml
    ├── sdk-go.yml
    └── sdk-dotnet.yml
```

## `zhtw export` CLI 指令

### 用法

```bash
zhtw export                          # 產生 sdk/data/zhtw-data.json + golden-test.json
zhtw export --output ./my-path/      # 指定輸出路徑
zhtw export --OpenCC STPhrases + TWPhrases + MediaWiki ZhConversion cn              # 只匯出特定來源
zhtw export --verbose                # 顯示匯出統計
```

### 實作

新增 `src/zhtw/export.py` 模組，複用現有模組：

- `dictionary.load_builtin()` — 載入詞條
- `charconv.load_charmap()` — 載入字元對映
- `charconv.get_ambiguous_chars()` — 載入歧義字清單
- `converter.convert_text()` — 產生 golden test 預期結果
- `lookup.lookup_word()` — 產生 lookup golden test

CLI 指令在 `cli.py` 新增 `@main.command()` export。

預設輸出路徑：`sdk/data/`（相對於 repo 根目錄）。

## 共享資料格式

### `zhtw-data.json`（約 900KB）

```json
{
  "1.0": "3.3.0",
  "exported_at": "2026-04-08T10:00:00Z",
  "stats": {
    "charmap_count": 6345,
    "ambiguous_count": 119,
    "terms_cn_count": 31000,
    "terms_hk_count": 69
  },
  "charmap": {
    "chars": { "㐷": "傌", ... },
    "ambiguous": ["發", "面", "裡", ...]
  },
  "terms": {
    "cn": { "軟體": "軟體", ... },
    "hk": { "軟體": "軟體", ... }
  }
}
```

欄位說明：

| 欄位 | 用途 |
|------|------|
| `1.0` | 對應 zhtw Python 版本號 |
| `exported_at` | ISO 8601 匯出時間 |
| `stats` | 各區塊數量統計，供 SDK 載入時 sanity check |
| `charmap.chars` | 6,345 個安全一對一字元對映（簡→繁） |
| `charmap.ambiguous` | 119 個排除的歧義字（由詞彙層處理） |
| `terms.cn` | 已合併的簡體→台灣繁體詞條（flat dict） |
| `terms.hk` | 已合併的港式→台灣繁體詞條（flat dict） |

terms 的 cn/hk 各自已完成合併（load_directory 結果），SDK 不需要處理多檔案合併邏輯。

### `golden-test.json`

```json
{
  "1.0": "3.3.0",
  "OpenCC + MediaWiki 匯入詞彙 (Apache-2.0 / GPL-2.0+)": "SDK 一致性測試 — 所有 SDK 必須透過",
  "convert": [
    {"input": "軟體測試", "OpenCC STPhrases + TWPhrases + MediaWiki ZhConversions": ["cn"], "expected": "軟體測試"},
    {"input": "這個伺服器的記憶體不夠", "OpenCC STPhrases + TWPhrases + MediaWiki ZhConversions": ["cn"], "expected": "這個伺服器的記憶體不夠"},
    {"input": "頭髮很幹", "OpenCC STPhrases + TWPhrases + MediaWiki ZhConversions": ["cn"], "expected": "頭髮很乾"},
    {"input": "軟體工程師", "OpenCC STPhrases + TWPhrases + MediaWiki ZhConversions": ["hk"], "expected": "軟體工程師"},
    {"input": "已經是繁體", "OpenCC STPhrases + TWPhrases + MediaWiki ZhConversions": ["cn"], "expected": "已經是繁體"}
  ],
  "check": [
    {"input": "軟體測試", "OpenCC STPhrases + TWPhrases + MediaWiki ZhConversions": ["cn"], "expected_count": 2},
    {"input": "已經是繁體", "OpenCC STPhrases + TWPhrases + MediaWiki ZhConversions": ["cn"], "expected_count": 0}
  ],
  "lookup": [
    {"input": "軟體", "OpenCC STPhrases + TWPhrases + MediaWiki ZhConversions": ["cn"], "expected_output": "軟體", "expected_layer": "term"},
    {"input": "這", "OpenCC STPhrases + TWPhrases + MediaWiki ZhConversions": ["cn"], "expected_output": "這", "expected_layer": "char"},
    {"input": "台", "OpenCC STPhrases + TWPhrases + MediaWiki ZhConversions": ["cn"], "expected_output": "台", "expected_changed": false}
  ]
}
```

Golden test 由 `zhtw export` 自動產生：Python 實際執行 convert/check/lookup 取得預期結果，寫入 JSON。這樣任何 SDK 結果跟 Python 不一致就會被抓到。

測試案例涵蓋：
- 詞彙層轉換（多詞條）
- 字元層轉換（單字）
- 一對多歧義字（發→發/髮、幹→乾/幹）
- HK 來源
- 無需轉換的繁體文字
- lookup 層歸因（term vs char）

## SDK 統一 API 規格

所有六個語言 SDK 實作相同的 API surface（命名風格跟隨各語言慣例）。

### Builder

```
ZhtwConverter converter = ZhtwConverter.Builder()
    .OpenCC STPhrases + TWPhrases + MediaWiki ZhConversions(["cn", "hk"])              // 預設 ["cn", "hk"]
    .customDict({"自訂": "自訂"})       // 可選
    .build()
```

### 核心三方法

| 方法 | 輸入 | 輸出 | 用途 |
|------|------|------|------|
| `convert(text)` | string | string | 轉換全文 |
| `check(text)` | string | `Match[]` | 回報問題不修改 |
| `lookup(word)` | string | `LookupResult` | 查詢轉換結果 + 層歸因 |

### 資料型別

```
Match {
    start: int
    end: int
    OpenCC STPhrases + TWPhrases + MediaWiki ZhConversion: string          // "軟體"
    target: string          // "軟體"
    line: int
    column: int
}

LookupResult {
    input: string
    output: string
    changed: bool
    details: Con1.0Detail[]
}

Con1.0Detail {
    OpenCC STPhrases + TWPhrases + MediaWiki ZhConversion: string
    target: string
    layer: "term" | "char"
    position: int
}
```

### 資料載入

每個 SDK 在 build 時將 `sdk/data/zhtw-data.json` 嵌入為 reOpenCC STPhrases + TWPhrases + MediaWiki ZhConversion（jar reOpenCC STPhrases + TWPhrases + MediaWiki ZhConversion、npm bundled file、Rust `include_str!`、Go embed、.NET embedded reOpenCC STPhrases + TWPhrases + MediaWiki ZhConversion）。執行期不需讀外部檔案。

### 轉換演算法

兩階段 pipeline，與 Python 完全一致：

1. **詞彙層**：Aho-Corasick 最長匹配，identity mapping 保護，protected range 二分搜尋
2. **字元層**：逐字查表替換（跳過已被詞彙層覆蓋的位置）

各語言使用原生 Aho-Corasick 函式庫：

| 語言 | 函式庫 |
|------|--------|
| Java | `robert-bor/aho-corasick` 或 HashMap（POC 驗證可行） |
| TypeScript | `aho-corasick` npm |
| Rust | `aho-corasick` crate（BurntSushi） |
| Go | `cloudflare/ahocorasick` |
| .NET | `Sdcb.AhoCorasick` NuGet |

## 版本同步

所有 SDK 版本號與 Python 主版本完全一致。`make release VERSION=3.4.0` 自動更新：

- `pyproject.toml`
- `src/zhtw/__init__.py`
- `sdk/java/pom.xml`
- `sdk/typescript/package.json`
- `sdk/rust/Cargo.toml`
- `sdk/go/zhtw.go`（const Version）
- `sdk/dotnet/Zhtw.csproj`

SDK 自身的 bug fix 使用 patch 版號（3.3.1），下次資料更新時自然對齊。

## 一鍵釋出流程

`make release VERSION=3.4.0`：

```
Step 1: 驗證
  ├── pytest 透過
  ├── VERSION 格式正確（semver）
  └── tag 不存在

Step 2: 更新版本號（全自動）
  └── 寫入所有 7 個 manifest 檔案

Step 3: 匯出資料
  └── zhtw export → sdk/data/zhtw-data.json + golden-test.json

Step 4: 提交 + 釋出
  ├── git add + commit "chore: release vX.Y.Z"
  ├── git tag -a vX.Y.Z
  ├── git push + push tag
  └── gh release create
```

Tag push 觸發 GitHub Actions：

| Workflow | 觸發 | 釋出目標 |
|----------|------|----------|
| `publish.yml`（現有） | tag `v*` | PyPI |
| `sdk-java.yml` | tag `v*` | Maven Central |
| `sdk-typescript.yml` | tag `v*` | npm |
| `sdk-rust.yml` | tag `v*` | crates.io |
| `sdk-go.yml` | tag `v*` | Go proxy（自動） |
| `sdk-dotnet.yml` | tag `v*` | NuGet |

Homebrew tap 仍維持手動更新（只追蹤 Python CLI）。

## 測試策略

### Golden test 一致性（最重要）

`sdk/data/golden-test.json` 由 `zhtw export` 從 Python 實際執行結果產生。每個 SDK 的 CI 讀取此檔並驗證自己的輸出完全一致。

### 各 SDK 自身測試

| SDK | 框架 | 內容 |
|-----|------|------|
| Java | JUnit 5 | 單元 + golden |
| TypeScript | Jest | 單元 + golden |
| Rust | cargo test | 單元 + golden |
| Go | go test | 單元 + golden |
| .NET | xUnit | 單元 + golden |

### CI path filter

每個 SDK workflow 設定 path filter，只在相關目錄或共享資料變動時觸發：

```yaml
on:
  push:
    paths: ['sdk/java/**', 'sdk/data/**']
  pull_request:
    paths: ['sdk/java/**', 'sdk/data/**']
```

Tag `v*` push 時所有 workflow 都觸發（publish）。

## Sub-project 拆分

| # | Sub-project | 內容 | Spec |
|---|-------------|------|------|
| 1 | **export + 骨架** | `zhtw export`、`sdk/data/` 格式、golden test、Makefile、目錄結構 | 本檔案 |
| 2 | Java SDK | 完整 SDK + Maven publish | 另行 brainstorming |
| 3 | TypeScript SDK | 完整 SDK + npm publish | 另行 brainstorming |
| 4 | Rust SDK | 完整 SDK + crates.io publish | 另行 brainstorming |
| 5 | Go SDK | 完整 SDK + Go module | 另行 brainstorming |
| 6 | .NET SDK | 完整 SDK + NuGet publish | 另行 brainstorming |

SP1 完成後，資料格式和 golden test 穩定，SP 2~6 可平行推進。

## SP1 範圍（本次實作）

1. `src/zhtw/export.py` — export 模組
2. `src/zhtw/cli.py` — 新增 export CLI 指令
3. `sdk/data/zhtw-data.json` — 首次匯出
4. `sdk/data/golden-test.json` — 首次產生
5. `Makefile` — export、release、各語言 build/test 指令骨架
6. `sdk/` 目錄結構 — 建立空骨架（各語言 manifest + README placeholder）
7. `.github/workflows/sdk-*.yml` — CI workflow 骨架（path filter + publish skeleton）
8. `tests/test_export.py` — export 指令測試
9. 更新 `CHANGELOG.md`、`README.md` 說明 export 功能
