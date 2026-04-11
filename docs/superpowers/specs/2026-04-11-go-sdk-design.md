<!-- zhtw:disable -->
# Go SDK 設計規格

**Date:** 2026-04-11
**Author:** rajatim + Claude (brainstorming session)
**Status:** Draft — awaiting user review before writing implementation plan

---

## Goal

為 `zhtw` 新增第 6 個 SDK：**Go 原生 module**，留在 monorepo 內（`sdk/go/`），共用 `zhtw-data.json` 字典，API 對齊 Python/Java/TS/Rust，透過 `golden-test.json` 跨 SDK 驗證。

## Architecture summary

1. **Monorepo 內的 Go module**：`github.com/rajatim/zhtw/sdk/go/v4`，主 package 在 `sdk/go/zhtw/`。Go 的 semantic import versioning 要求 major >= 2 的 module path 帶 `/vN` 後綴。
2. **自己實作 Aho-Corasick**（trie + failure links + leftmost-longest match）— 零外部依賴，參考 TypeScript SDK 的自實作模式。
3. **`//go:embed` 嵌入字典**：`sdk/go/data/zhtw-data.json` **commit 進 VCS**（不 gitignore），透過 `make export` 從 `sdk/data/zhtw-data.json` 同步。這確保 `go get` 拉下來的 module zip 包含字典，consumer build 不會壞。
4. **三層轉換**：Term layer（AC longest match）→ Balanced defaults layer → Char layer，邏輯與所有 SDK 一致。
5. **版本走 Go prefix tag**：`sdk/go/v4.2.0` 格式，`make bump` 自動建立。Go proxy 從 Git tag 抓版本，不需要額外 registry。

## Tech stack

- **Go:** 1.21+（支援 `go:embed`、generics）
- **外部依賴：** 無（零 `require` in go.mod）
- **Aho-Corasick：** 自實作
- **測試：** `testing` 標準庫 + `golden-test.json`
- **Lint：** `go vet` + `golangci-lint`

---

## S1 - 檔案結構

```
sdk/go/
├── go.mod                        # module github.com/rajatim/zhtw/sdk/go/v4, go 1.21
├── data/
│   └── zhtw-data.json            # committed to VCS，make export 同步自 sdk/data/
└── zhtw/
    ├── zhtw.go                   # 公開 API：Convert/Check/Lookup 便利函式
    ├── converter.go              # Converter struct + 三層轉換邏輯
    ├── builder.go                # Builder pattern
    ├── matcher.go                # Aho-Corasick automaton 實作
    ├── data.go                   # go:embed + JSON 反序列化 + sync.Once 預設初始化
    ├── types.go                  # Match, LookupResult, ConversionDetail, Source, AmbiguityMode
    ├── zhtw_test.go              # 單元測試
    └── golden_test.go            # golden-test.json 跨 SDK 驗證
```

## S2 - 公開 API

### 便利函式

```go
package zhtw

// Convert 使用預設 Converter（Cn+Hk, Strict mode）轉換簡體中文為繁體中文（台灣）。
// Thread-safe，內部用 sync.Once 延遲初始化。
func Convert(text string) string

// Check 掃描文字中的簡體中文詞彙/字元，回傳匹配資訊。
func Check(text string) []Match

// Lookup 查詢單一詞彙的詳細轉換資訊。
func Lookup(word string) LookupResult
```

### Converter 與 Builder

```go
// Converter 是可重複使用的轉換器。Thread-safe（所有欄位在建構後不可變）。
type Converter struct { /* unexported */ }

func (c *Converter) Convert(text string) string
func (c *Converter) Check(text string) []Match
func (c *Converter) Lookup(word string) LookupResult

// Builder 用於建構自訂 Converter。
type Builder struct { /* unexported */ }

func NewBuilder() *Builder
func (b *Builder) Sources(sources ...Source) *Builder
func (b *Builder) CustomDict(dict map[string]string) *Builder
func (b *Builder) AmbiguityMode(mode AmbiguityMode) *Builder
func (b *Builder) Build() (*Converter, error)
// Build() 回傳 error 的情境：sources 為空。
```

### Types

```go
type Source string

const (
    SourceCn Source = "cn"
    SourceHk Source = "hk"
)

type AmbiguityMode string

const (
    AmbiguityStrict  AmbiguityMode = "strict"
    AmbiguityBalanced AmbiguityMode = "balanced"
)

type Match struct {
    Start  int    `json:"start"`  // Unicode codepoint index
    End    int    `json:"end"`    // Unicode codepoint index
    Source string `json:"source"` // 原始簡體
    Target string `json:"target"` // 轉換後繁體
}

type LookupResult struct {
    Input   string             `json:"input"`
    Output  string             `json:"output"`
    Changed bool               `json:"changed"`
    Details []ConversionDetail `json:"details"`
}

type ConversionDetail struct {
    Source   string `json:"source"`
    Target   string `json:"target"`
    Layer    string `json:"layer"`    // "term" | "char"
    Position int    `json:"position"` // Unicode codepoint index
}
```

## S3 - 資料載入

### JSON 結構（zhtw-data.json）

```go
type zhtwData struct {
    Charmap struct {
        Chars            map[string]string `json:"chars"`
        Ambiguous        []string          `json:"ambiguous"`         // 102 個歧義字列表（不直接用於轉換）
        BalancedDefaults map[string]string `json:"balanced_defaults"` // optional
    } `json:"charmap"`
    Terms map[string]map[string]string `json:"terms"` // "cn" -> {"\u8f6f\u4ef6": "\u8edf\u9ad4", ...}, "hk" -> {...}
}
```

### 初始化流程

1. `data.go` 用 `//go:embed ../data/zhtw-data.json` 嵌入原始 JSON bytes。此路徑相對於 `sdk/go/zhtw/data.go` 指向 `sdk/go/data/zhtw-data.json`，該檔案已 commit 進 VCS。
2. `sync.Once` 在首次呼叫便利函式時反序列化 JSON、建構 AC automaton、初始化 charmap。
3. 預設 Converter 用 `Sources: [Cn, Hk]`、`AmbiguityMode: Strict`。
4. 自訂 Builder 每次 `Build()` 都建新 AC automaton（跟 Rust/Java 模式一致）。

### charmap 最佳化

`zhtw-data.json` 的 `chars` 是 `map[string]string`（單字元 key/value）。載入後轉為 `map[rune]rune` 以避免每次查詢時 string→rune 轉換開銷。同理 `balanced_defaults` 也轉為 `map[rune]rune`。

## S4 - Aho-Corasick 實作

### 設計

`matcher.go` 實作標準 Aho-Corasick automaton：

1. **Trie 建構**：從 term patterns 建立 goto function
2. **Failure links**：BFS 計算 failure function
3. **搜尋**：leftmost-longest match（跟其他 SDK 一致）

### 介面

```go
type ahoCorasick struct { /* unexported */ }

// buildAhoCorasick 從 patterns 建構 automaton。
func buildAhoCorasick(patterns []acPattern) *ahoCorasick

type acPattern struct {
    source string
    target string
}

type acMatch struct {
    byteStart int
    byteEnd   int
    source    string
    target    string
}

// findTermMatches 回傳所有非重疊的 leftmost-longest matches。
func (ac *ahoCorasick) findTermMatches(text string) []acMatch

// getCoveredPositions 回傳所有 automaton hit 覆蓋的 byte positions（含 identity terms）。
func (ac *ahoCorasick) getCoveredPositions(text string) map[int]bool
```

### Leftmost-longest 語義

跟所有 SDK 一致：掃描所有 hit → 按 start 排序 → 貪婪取最長不重疊 match。Identity terms（source == target）不產生替換但會標記 covered positions，防止 char layer 誤轉。

## S5 - 三層轉換邏輯

`converter.go` 的 `Convert()` 流程：

1. 計算 covered positions（所有 AC hit 含 identity terms）
2. 取得 term matches（source != target）
3. Gap mode：term targets 原樣插入；gap 區間對未 covered 的字元依序查 balanced defaults → charmap
4. 空文字直接回傳 `""`

`Check()` 和 `Lookup()` 遵循相同的三層邏輯，只是輸出格式不同（Match list / LookupResult）。

### 索引位置

所有外部 API 的 `Start` / `End` / `Position` 都是 **Unicode codepoint index**。Go 的 `[]rune` index 就是 codepoint index，所以內部只需建一個 byte-offset → rune-index 的對映表。

## S6 - 測試

### 單元測試（`zhtw_test.go`）

- AC automaton 基礎功能：建構、搜尋、longest match、covered positions
- Convert/Check/Lookup 基本 cases
- Builder：自訂 sources、customDict、balanced mode
- Edge cases：空字串、純 ASCII、混合中英文

### Golden test（`golden_test.go`）

- 讀取 `sdk/data/golden-test.json`
- 驗證三段 API 全部對齊：
  - **convert**：對每個 test case 建構對應 Converter（按 sources + ambiguityMode），驗證 `Convert()` 輸出 == `expected`
  - **check**：驗證 `Check()` 回傳的 `[]Match` 與 fixture 的 start/end/source/target 完全一致
  - **lookup**：驗證 `Lookup()` 回傳的 input/output/changed/details（含 layer、position）完全一致
- 這是跨 SDK parity 的硬性門檻 — byte offset → codepoint index 映射、detail 排序、layer attribution 都在此驗證

## S7 - CI（`sdk-go.yml`）

```yaml
name: SDK Go
on:
  push:
    paths: ['sdk/go/**', 'sdk/data/**', '.github/workflows/sdk-go.yml']
  pull_request:
    paths: ['sdk/go/**', 'sdk/data/**', '.github/workflows/sdk-go.yml']
  release:
    types: [published]

jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        go: ['1.21', 'stable']
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: ${{ matrix.go }}
      - name: Test
        working-directory: sdk/go
        run: go test ./... -v -race
      - name: Vet
        working-directory: sdk/go
        run: go vet ./...
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: stable
      - name: golangci-lint
        uses: golangci/golangci-lint-action@v6
        with:
          working-directory: sdk/go
```

Release 不需要 publish job — Go proxy 直接從 Git tag（`sdk/go/vX.Y.Z`）拉取。

CI 不再需要 `cp` 步驟 — `sdk/go/data/zhtw-data.json` 已在 VCS 中。

## S8 - Mono-versioning 影響

### Go semantic import versioning

Go module path 為 `github.com/rajatim/zhtw/sdk/go/v4`（帶 `/v4` 後綴）。當 monorepo major version 升到 v5 時：
1. `go.mod` 的 module path 改為 `.../v5`
2. 所有 internal import path 更新
3. 用戶 import path 也需跟著改（這是 Go 的設計，不是我們的限制）

### `make bump` / `make export` 新增步驟

1. `make export`：複製 `sdk/data/zhtw-data.json` → `sdk/go/data/zhtw-data.json`
2. `make bump`：同上 + 更新 `go.mod` 的 module path（如果 major 版本變動）
3. Release 時額外建立 prefix tag：`git tag -a sdk/go/vX.Y.Z -m "sdk/go vX.Y.Z"`
4. Push 時多推一個 tag：`git push origin sdk/go/vX.Y.Z`

### `make version-check`

驗證 `sdk/go/data/zhtw-data.json` 與 `sdk/data/zhtw-data.json` 一致（`diff` 或 checksum）。

### `go.mod` 不含版本號

Go module 的版本由 Git tag 決定，`go.mod` 裡沒有 `version` 欄位，所以 `make version-check` 不需要檢查版本數字，只檢查 data 同步。

---

## 使用者使用範例

```go
package main

import (
    "fmt"
    "github.com/rajatim/zhtw/sdk/go/v4/zhtw"
)

func main() {
    // 零設定
    fmt.Println(zhtw.Convert("\u8fd9\u4e2a\u8f6f\u4ef6\u9700\u8981\u4f18\u5316"))
    // → "這個軟體需要最佳化"

    // 自訂設定
    conv, _ := zhtw.NewBuilder().
        Sources(zhtw.SourceCn).
        CustomDict(map[string]string{"\u81ea\u5b9a\u4e49": "自訂"}).
        AmbiguityMode(zhtw.AmbiguityBalanced).
        Build()

    fmt.Println(conv.Convert("\u8fd9\u4e2a\u8f6f\u4ef6\u9700\u8981\u4f18\u5316"))
}
```

安裝：

```bash
go get github.com/rajatim/zhtw/sdk/go/v4/zhtw@v4.2.0
```
