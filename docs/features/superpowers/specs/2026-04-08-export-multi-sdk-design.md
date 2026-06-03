<!-- zhtw:disable -->
# zhtw export + Multi-Language SDK Design

> **Sub-project 1 of 6** — export 指令、共享資料格式、golden test、Makefile 骨架

## Goal

在 zhtw CLI 新增 `export` 指令，產出標準化 JSON 資料檔，建立 Monorepo 骨架讓六個語言 SDK（Java、TypeScript、Rust、Go、.NET）能共用同一份轉換資料，並透過 golden test 確保所有 SDK 輸出與 Python 一致。

## Architecture

zhtw 的核心價值是精選詞條和字元映射。`zhtw export` 將這些資料從 Python 內部格式匯出為語言無關的 JSON，放在 `sdk/data/`。各語言 SDK 在 build 時將此 JSON 嵌入為 resource，用原生 Aho-Corasick 函式庫實作轉換引擎。

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
zhtw export --source cn              # 只匯出特定來源
zhtw export --verbose                # 顯示匯出統計
```

### Scope：Maintainer-only 指令

`zhtw export` 僅供 repo maintainer 在 checkout 內使用，不是給終端使用者的功能。原因：

- 預設輸出路徑 `sdk/data/` 只存在於 repo checkout 內
- wheel 只包 `src/zhtw`（`pyproject.toml` hatch build targets），不含 `sdk/`
- pip 安裝的使用者不需要也不應該使用此指令

### 預設輸出路徑

預設輸出到 `./sdk/data/`（CWD 相對路徑）。若目錄不存在，報錯並提示使用 `--output`。

`--output` 覆蓋預設，允許輸出到任意路徑。

### 實作

新增 `src/zhtw/export.py` 模組，複用現有模組：

- `dictionary.load_directory()` — **分別載入** cn 和 hk 詞條（不用 `load_builtin()` 以避免合併）
- `charconv.load_charmap()` — 載入字元映射
- `charconv.get_ambiguous_chars()` — 載入歧義字列表
- `converter.convert_text()` — 產生 golden test 預期結果
- `lookup.lookup_word()` — 產生 lookup golden test

CLI 指令在 `cli.py` 新增 `@main.command()` export。

## 共享資料格式

### `zhtw-data.json`

約 900KB。所有數量為 runtime 實際值，不硬編碼。

```json
{
  "version": "3.3.0",
  "exported_at": "2026-04-08T10:00:00Z",
  "stats": {
    "charmap_count": 6343,
    "ambiguous_count": 119,
    "terms_cn_count": 31794,
    "terms_hk_count": 61
  },
  "charmap": {
    "chars": { "㐷": "傌", "万": "萬", "与": "與" },
    "ambiguous": ["发", "面", "里", "干", "只", "台", "后"]
  },
  "terms": {
    "cn": { "软件": "軟體", "服务器": "伺服器", "头发": "頭髮" },
    "hk": { "軟件": "軟體", "數據庫": "資料庫" }
  }
}
```

欄位說明：

| 欄位 | 用途 |
|------|------|
| `version` | 對應 zhtw Python 版本號 |
| `exported_at` | ISO 8601 匯出時間 |
| `stats` | 各區塊 runtime 數量統計，供 SDK 載入時 sanity check |
| `charmap.chars` | 安全一對一字元映射（簡→繁），目前約 6,343 個 |
| `charmap.ambiguous` | 排除的歧義字列表（由詞彙層處理），目前 119 個 |
| `terms.cn` | 簡體→台灣繁體詞條，已合併（`load_directory` 結果），目前約 31,794 個 |
| `terms.hk` | 港式→台灣繁體詞條，已合併（`load_directory` 結果），目前約 61 個 |

**重要：charmap 僅在 source 包含 "cn" 時套用**。HK 來源只做詞彙層轉換，不做字元層轉換。此規則寫入 JSON 但也必須在各 SDK 文件中明確說明。

terms 的 cn/hk 各自已完成合併（`load_directory` 結果），SDK 不需要處理多檔案合併邏輯。分開存放是為了讓 SDK builder 可以選擇只載入特定 source。

### `golden-test.json`

由 `zhtw export` 自動產生：Python 實際執行 convert/check/lookup 取得預期結果，寫入 JSON。任何 SDK 結果跟 Python 不一致就會被抓到。

```json
{
  "version": "3.3.0",
  "description": "SDK consistency test — all SDKs must pass",
  "convert": [
    {
      "input": "软件测试",
      "sources": ["cn"],
      "expected": "軟體測試"
    },
    {
      "input": "这个服务器的内存不够",
      "sources": ["cn"],
      "expected": "這個伺服器的記憶體不夠"
    },
    {
      "input": "头发很干",
      "sources": ["cn"],
      "expected": "頭髮很乾"
    },
    {
      "input": "軟件工程師",
      "sources": ["hk"],
      "expected": "軟體工程師"
    },
    {
      "input": "已經是繁體",
      "sources": ["cn"],
      "expected": "已經是繁體"
    }
  ],
  "check": [
    {
      "input": "软件测试",
      "sources": ["cn"],
      "expected_matches": [
        {"start": 0, "end": 2, "source": "软件", "target": "軟體"},
        {"start": 2, "end": 4, "source": "测试", "target": "測試"}
      ]
    },
    {
      "input": "已經是繁體",
      "sources": ["cn"],
      "expected_matches": []
    }
  ],
  "lookup": [
    {
      "input": "软件",
      "sources": ["cn"],
      "expected_output": "軟體",
      "expected_changed": true,
      "expected_details": [
        {"source": "软件", "target": "軟體", "layer": "term", "position": 0}
      ]
    },
    {
      "input": "这",
      "sources": ["cn"],
      "expected_output": "這",
      "expected_changed": true,
      "expected_details": [
        {"source": "这", "target": "這", "layer": "char", "position": 0}
      ]
    },
    {
      "input": "台",
      "sources": ["cn"],
      "expected_output": "台",
      "expected_changed": false,
      "expected_details": []
    }
  ]
}
```

**與原 spec 差異**（Codex finding #3 修正）：
- `check` 現在包含完整 `expected_matches`（start/end/source/target），不只是 count
- `lookup` 包含完整 `expected_details`（source/target/layer/position），不只是 single layer
- 這確保 SDK 的位置計算、歸因順序、匹配邏輯都與 Python 一致

測試案例涵蓋：
- 詞彙層轉換（多詞條）
- 字元層轉換（單字）
- 一對多歧義字（发→發/髮、干→乾/幹）
- HK 來源（只有詞彙層，無字元層）
- 無需轉換的繁體文字
- lookup 層歸因（term vs char）

實際產生時，export 會從 Python pipeline 跑更多案例（含 edge cases），上面只是 schema 範例。

## SDK 統一 API 規格

所有六個語言 SDK 實作相同的 API surface（命名風格跟隨各語言慣例）。

### Builder

```java
// Java
ZhtwConverter converter = new ZhtwConverter.Builder()
    .sources(List.of("cn", "hk"))       // 預設 ["cn", "hk"]
    .customDict(Map.of("自定义", "自訂")) // 可選
    .build();

// TypeScript
const converter = new ZhtwConverter({ sources: ["cn", "hk"], customDict: { "自定义": "自訂" } });

// Rust
let converter = ZhtwConverter::builder().sources(&["cn", "hk"]).custom_dict(custom).build();

// Go
converter := zhtw.NewConverter(zhtw.WithSources("cn", "hk"), zhtw.WithCustomDict(custom))

// C#
var converter = new ZhtwConverter.Builder().Sources("cn", "hk").CustomDict(custom).Build();
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
    source: string          // "软件"（原始簡體/港式）
    target: string          // "軟體"（台灣繁體）
    line: int
    column: int
}

LookupResult {
    input: string
    output: string
    changed: bool
    details: ConversionDetail[]
}

ConversionDetail {
    source: string
    target: string
    layer: "term" | "char"
    position: int
}
```

### 資料載入

每個 SDK 在 build 時將 `sdk/data/zhtw-data.json` 嵌入為 resource（jar resource、npm bundled file、Rust `include_str!`、Go `//go:embed`、.NET embedded resource）。執行期不需讀外部檔案。

### 轉換演算法

兩階段 pipeline，與 Python 完全一致：

1. **詞彙層**：Aho-Corasick 最長匹配，identity mapping 保護，protected range 二分搜尋
2. **字元層**：逐字查表替換（跳過已被詞彙層覆蓋的位置）

**重要規則**：字元層僅在 sources 包含 "cn" 時啟用。HK source 只做詞彙層。（對應 Python `converter.py:609` 的 `if char_convert and "cn" in sources` 邏輯）

各語言使用原生 Aho-Corasick 函式庫：

| 語言 | 函式庫 |
|------|--------|
| Java | `robert-bor/aho-corasick` 或 HashMap（POC 驗證可行） |
| TypeScript | `aho-corasick` npm |
| Rust | `aho-corasick` crate（BurntSushi） |
| Go | `cloudflare/ahocorasick` |
| .NET | `Sdcb.AhoCorasick` NuGet |

## 版本同步

所有 SDK 版本號與 Python 主版本完全一致。不允許 SDK 單獨出 patch — 要改就全部一起改。`make release VERSION=3.4.0` 自動更新：

- `pyproject.toml`
- `src/zhtw/__init__.py`
- `sdk/java/pom.xml`
- `sdk/typescript/package.json`
- `sdk/rust/Cargo.toml`
- `sdk/go/zhtw.go`（const Version）
- `sdk/dotnet/Zhtw.csproj`

若某個 SDK 有 bug 但資料沒變，仍然走正常 release 流程（bump 全域版號）。

## 一鍵發佈流程

`make release VERSION=3.4.0`：

```
Step 1: 驗證
  ├── pytest 通過
  ├── VERSION 格式正確（semver）
  └── tag 不存在

Step 2: 更新版本號（全自動）
  └── 寫入所有 7 個 manifest 檔案

Step 3: 匯出資料
  └── zhtw export → sdk/data/zhtw-data.json + golden-test.json

Step 4: 提交 + 發佈
  ├── git add + commit "chore: release vX.Y.Z"
  ├── git tag -a vX.Y.Z
  ├── git push + push tag
  └── gh release create
```

GitHub Actions 觸發方式：

| Workflow | 觸發條件 | 發佈目標 |
|----------|----------|----------|
| `publish.yml`（現有） | `release: types: [published]` | PyPI |
| `sdk-java.yml` | `release: types: [published]` | Maven Central |
| `sdk-typescript.yml` | `release: types: [published]` | npm |
| `sdk-rust.yml` | `release: types: [published]` | crates.io |
| `sdk-go.yml` | `release: types: [published]` | Go proxy（自動） |
| `sdk-dotnet.yml` | `release: types: [published]` | NuGet |

注意：觸發條件是 `release published`（不是 tag push），與現有 `publish.yml` 一致。

Homebrew tap 仍維持手動更新（只追蹤 Python CLI）。

## 測試策略

### Golden test 一致性（最重要）

`sdk/data/golden-test.json` 由 `zhtw export` 從 Python 實際執行結果產生。每個 SDK 的 CI 讀取此檔並驗證自己的輸出完全一致：convert 結果相同、check 的 match 位置/source/target 相同、lookup 的 details 完整相同。

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
  release:
    types: [published]
```

## Sub-project 拆分

| # | Sub-project | 內容 | Spec |
|---|-------------|------|------|
| 1 | **export + 骨架** | `zhtw export`、`sdk/data/` 格式、golden test、Makefile、目錄結構 | 本文件 |
| 2 | Java SDK | 完整 SDK + Maven publish | 另行 brainstorming |
| 3 | TypeScript SDK | 完整 SDK + npm publish | 另行 brainstorming |
| 4 | Rust SDK | 完整 SDK + crates.io publish | 另行 brainstorming |
| 5 | Go SDK | 完整 SDK + Go module | 另行 brainstorming |
| 6 | .NET SDK | 完整 SDK + NuGet publish | 另行 brainstorming |

SP1 完成後，資料格式和 golden test 穩定，SP 2~6 可平行推進。

## SP1 範圍（本次實作）

1. `src/zhtw/export.py` — export 模組（load_directory per source、repo root 偵測）
2. `src/zhtw/cli.py` — 新增 export CLI 指令（--output、--source、--verbose）
3. `sdk/data/zhtw-data.json` — 首次匯出
4. `sdk/data/golden-test.json` — 首次產生（含完整 match details）
5. `Makefile` — export、release、各語言 build/test 指令骨架
6. `sdk/` 目錄結構 — 建立空骨架（各語言 manifest + README placeholder）
7. `.github/workflows/sdk-*.yml` — CI workflow 骨架（path filter + publish skeleton，不含實際 registry 發版）
8. `tests/test_export.py` — export 指令測試（schema 驗證、source filter、golden 內容與 Python pipeline 一致）
9. 更新 `CHANGELOG.md`、`README.md` 說明 export 功能

注意：SP1 的 CI workflow 只含骨架（build + test），不打通實際 publish 到各 registry。Publish 步驟在各 SDK sub-project 完成時才接上。
<!-- zhtw:enable -->
