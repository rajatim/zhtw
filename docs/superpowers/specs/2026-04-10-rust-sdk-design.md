# Rust SDK 設計規格

**Date:** 2026-04-10
**Author:** rajatim + Claude (brainstorming session)
**Status:** Draft — awaiting user review before writing implementation plan

---

## Goal

為 `zhtw` 新增第 4 個有實作的 SDK：**Rust 原生 crate (`zhtw`) + WebAssembly bindings (`zhtw-wasm`)**，以 Rust 3 + 4 個 SDK 已釋出實作，對齊 mono-versioning、golden-test parity，並把現有 `sdk/rust/Cargo.toml` 的 scaffold（和 `.github/workflows/sdk-rust.yml` 的 fake-green stub）替換成真正可用的 pipeline。

## Architecture summary

1. `sdk/rust/` 從 single-crate scaffold 改寫成 **Cargo workspace**，含 `zhtw/`（原生 crate）+ `zhtw-wasm/`（wasm-bindgen 包裝）。
2. **`daachorse` crate + `CharwiseDoubleArrayAhoCorasick`** 當 matcher — 選它的原因是：`aho-corasick` 沒有公開的序列化 API（spike 驗證過），而 daachorse 同時提供原生序列化和專為多位元組文字最佳化的 charwise 實作。
3. **Build-time 資料管線：** `zhtw/build.rs` 讀 `sdk/data/zhtw-data.json`，產出 (a) `phf::Map<char, char>` 字元層完美 hash、(b) 序列化的 `CharwiseDoubleArrayAhoCorasick` bytes（含自製 magic header 驗證），嵌入到 binary。
4. **WASM 走獨立 npm 套件 `zhtw-wasm`**，但公開 TS 型別刻意對齊 `zhtw-js`，維持未來合併的選擇權。
5. **釋出走 crates.io + npm 雙 Trusted Publishing (OIDC)** — 和現有 `zhtw-js` 的無 token 姿態一致。

## Tech stack

- **Rust edition:** 2021, **MSRV:** 1.80（為 `std::sync::LazyLock` stabilization）
- **Matcher crate:** `daachorse = "=1.0.0"`（pin exact，避免 serialized format 漂移 — v1 實作時 confirm 最新穩定版再 pin）
- **Char layer:** `phf = "0.11"` + `phf_codegen = "0.11"` (build-dep)
- **Error:** `thiserror = "2"`
- **Serde:** `serde = "1"` + `serde_json = "1"`（只在 build.rs 和 tests/golden.rs 用，runtime path 不含 serde_json）
- **WASM:** `wasm-bindgen = "0.2"` + `js-sys` + `serde-wasm-bindgen`
- **Build tool:** `wasm-pack` (target: `bundler`)
- **Benchmark:** `criterion = "0.5"` (dev-dep)

---

## §1 · Workspace 架構與 Crate 職責

### File layout

```
sdk/rust/
├── Cargo.toml                    # workspace root (virtual manifest)
├── rust-toolchain.toml           # pin MSRV 1.80
├── .gitignore                    # target/, zhtw-wasm/pkg/*.wasm (but keep pkg/package.json)
│
├── zhtw/                         # → crates.io `zhtw`
│   ├── Cargo.toml                # inherits workspace.package
│   ├── build.rs                  # 核心：phf codegen + daachorse serialize + magic header
│   ├── src/
│   │   ├── lib.rs                # public API re-export
│   │   ├── config.rs             # Config struct + Default
│   │   ├── builder.rs            # Builder (手寫, 不用 typed-builder 避免增加依賴)
│   │   ├── converter.rs          # Converter 主體：convert/check/lookup
│   │   ├── source.rs             # Source enum + FromStr
│   │   ├── matcher.rs            # daachorse wrapper + identity protection + byte↔cp mapping
│   │   ├── generated.rs          # build.rs 產物的 re-export (private)
│   │   └── error.rs              # ZhtwError (thiserror)
│   ├── benches/
│   │   ├── convert.rs            # criterion：單句延遲 + 1MB 吞吐
│   │   └── check.rs              # criterion：check 命中收整合本
│   └── tests/
│       ├── golden.rs             # parity vs sdk/data/golden-test.json
│       ├── codepoint_index.rs    # byte vs codepoint 正確性
│       ├── api.rs                # Builder / free fn / default / Send+Sync
│       └── custom_dict.rs        # 自訂詞條 + 衝突解析
│
└── zhtw-wasm/                    # → npm `zhtw-wasm` (不發 crates.io)
    ├── Cargo.toml                # publish = false, depends on zhtw via path
    ├── src/lib.rs                # wasm-bindgen 薄包裝
    ├── package.json              # checked-in, 主版本來源（mono-versioning 第 8 位置）
    ├── README.md                 # 對齊 sdk/typescript/README.md 形狀
    └── tests/
        └── web.rs                # wasm-bindgen-test
```

### `sdk/rust/Cargo.toml` (workspace root)

```toml
[workspace]
resolver = "2"
members = ["zhtw", "zhtw-wasm"]

[workspace.package]
version = "X.Y.Z"               # updated by `make bump`
edition = "2021"
rust-version = "1.80"
license = "MIT"
repository = "https://github.com/rajatim/zhtw"

[workspace.dependencies]
daachorse = "=1.0.0"            # pin exact — see §3 guardrail 3
phf = { version = "0.11", features = ["macros"] }
serde = { version = "1", features = ["derive"] }
serde_json = "1"
thiserror = "2"
wasm-bindgen = "0.2"
js-sys = "0.3"
serde-wasm-bindgen = "0.6"

[profile.release]
lto = "fat"
codegen-units = 1
panic = "abort"
```

### 關鍵設計點

1. **`zhtw/build.rs` 是整個架構的效能心臟** — 見 §3
2. **`zhtw-wasm` 是 `zhtw` 的薄包裝** — `[dependencies] zhtw = { path = "../zhtw" }`。wasm build 時 `zhtw` 的 `build.rs` 會在 wasm32 target 重跑（host 平臺執行），產出的 bytes 嵌入 wasm binary。**沒有兩份實作**。
3. **`sdk/rust/Cargo.toml` 是 virtual manifest** — 兩 crate 共享版本，`make bump` 只改 `[workspace.package].version` 這單點。

---

## §2 · 公開 API 形狀

### 型別（`zhtw/src/lib.rs`）

```rust
// ──────────────────────────────────────────
// Core types
// ──────────────────────────────────────────

/// 簡轉繁的來源字典選擇。
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum Source {
    /// 中國大陸簡體 → 台灣繁體
    Cn,
    /// 香港繁體 → 台灣繁體
    Hk,
}

impl std::str::FromStr for Source {
    type Err = Error;
    fn from_str(s: &str) -> Result<Self> {
        match s {
            "cn" => Ok(Self::Cn),
            "hk" => Ok(Self::Hk),
            _ => Err(Error::InvalidSource(s.to_string())),
        }
    }
}

/// 內部 Config（builder.build() 的產物）。
#[derive(Debug, Clone)]
pub struct Config {
    pub sources: Vec<Source>,
    pub custom_dict: std::collections::HashMap<String, String>,
}

impl Default for Config {
    fn default() -> Self {
        Self {
            sources: vec![Source::Cn, Source::Hk],
            custom_dict: std::collections::HashMap::new(),
        }
    }
}

/// check() 的單一命中記錄。index 皆為 **Unicode codepoint offset**。
#[derive(Debug, Clone, PartialEq, Eq, serde::Serialize)]
pub struct Match {
    pub start: usize,      // codepoint, inclusive
    pub end: usize,        // codepoint, exclusive
    pub source: String,
    pub target: String,
}

/// lookup() 的回傳。
#[derive(Debug, Clone, PartialEq, Eq, serde::Serialize)]
pub struct LookupResult {
    pub input: String,
    pub output: String,
    pub changed: bool,
    pub details: Vec<ConversionDetail>,
}

#[derive(Debug, Clone, PartialEq, Eq, serde::Serialize)]
pub struct ConversionDetail {
    pub source: String,
    pub target: String,
    pub layer: Layer,
    pub position: usize,   // codepoint
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, serde::Serialize)]
#[serde(rename_all = "lowercase")]
pub enum Layer {
    Term,
    Char,
}

#[derive(Debug, thiserror::Error)]
#[non_exhaustive]
pub enum Error {
    #[error("invalid source string: {0}")]
    InvalidSource(String),
    // 未來擴充用 — v1 只有這一個 variant。
    // 熱路徑 convert/check/lookup 不回 Result。
}

pub type Result<T> = std::result::Result<T, Error>;

// ──────────────────────────────────────────
// Converter (Send + Sync, 不可變)
// ──────────────────────────────────────────

pub struct Converter {
    // Opaque fields:
    //   - term automaton (Arc<CharwiseDoubleArrayAhoCorasick<u32>>)
    //   - char_map (&'static phf::Map<char, char>)
    //   - pattern_data (Arc<Vec<(String, String)>>)  // pattern idx → (source, target)
    //   - custom_dict empty? flag (True → 走 LazyLock default automaton 的熱路徑)
}

impl Converter {
    pub fn new(config: Config) -> Self { /* see §3.4 */ }
    pub fn default_instance() -> &'static Self { /* LazyLock, see §2.3 */ }
    pub fn builder() -> Builder { Builder::default() }

    // 熱路徑 — 不回 Result
    pub fn convert(&self, text: &str) -> String { /* see §3.5 */ }
    pub fn check(&self, text: &str) -> Vec<Match> { /* see §3.5 */ }
    pub fn lookup(&self, word: &str) -> LookupResult { /* see §3.5 */ }
}

impl Default for Converter {
    fn default() -> Self { Self::default_instance().clone() }
}

// Clone is cheap because inner state is Arc.
impl Clone for Converter { /* ... */ }

// ──────────────────────────────────────────
// Builder
// ──────────────────────────────────────────

#[derive(Debug, Default)]
pub struct Builder {
    config: Config,
}

impl Builder {
    pub fn sources<I: IntoIterator<Item = Source>>(mut self, sources: I) -> Self {
        self.config.sources = sources.into_iter().collect();
        self
    }

    pub fn custom_dict<I, K, V>(mut self, dict: I) -> Self
    where
        I: IntoIterator<Item = (K, V)>,
        K: Into<String>,
        V: Into<String>,
    {
        self.config.custom_dict = dict.into_iter()
            .map(|(k, v)| (k.into(), v.into()))
            .collect();
        self
    }

    pub fn build(self) -> Converter {
        Converter::new(self.config)
    }
}

// ──────────────────────────────────────────
// Free functions (zero-config)
// ──────────────────────────────────────────

pub fn convert(text: &str) -> String {
    Converter::default_instance().convert(text)
}

pub fn check(text: &str) -> Vec<Match> {
    Converter::default_instance().check(text)
}

pub fn lookup(word: &str) -> LookupResult {
    Converter::default_instance().lookup(word)
}
```

### 2.3 `default_instance()` 的 LazyLock 實作

```rust
// zhtw/src/converter.rs
use std::sync::LazyLock;

static DEFAULT: LazyLock<Converter> = LazyLock::new(|| {
    Converter::new(Config::default())  // Cn + Hk, no custom dict
});

impl Converter {
    pub fn default_instance() -> &'static Self {
        &DEFAULT
    }
}
```

使用者呼叫 `zhtw::convert("...")` → 第一次觸發 `DEFAULT` init（含 automaton deserialize）→ 之後零成本。**熱路徑不付 JSON parse 也不付 automaton build。**

### 2.4 設計決策（明確 rationale）

1. **`convert/check/lookup` 不回 `Result`** — 熱路徑對任何 `&str` 都能成功，無失敗模式；回 `Result` 會強迫 `.unwrap()`/`?` 噪音。
2. **`Converter: Send + Sync`** — 內部 `Arc<...>` + `&'static`，可跨 thread 共享，對齊 Java SDK thread-safe 保證。Compile-time 強制。
3. **`default_instance()` 回 `&'static`** — 零 allocation 的 zero-config 入口，從第二次呼叫起完全免費。
4. **`Source` 是 enum，不是 `&str`** — 編譯期防打錯，WASM 邊界用 `FromStr` 解析。
5. **`custom_dict` 觸發 runtime automaton build**（見 §3.4）— 預設路徑吃預編譯，自訂路徑付正常建構成本。

### 2.5 使用範例（檔案等級）

```rust
use zhtw::{Converter, Source};

// Zero config
assert_eq!(zhtw::convert("這個軟體需要最佳化"), "這個軟體需要最佳化");

// Builder
let conv = Converter::builder()
    .sources([Source::Cn])
    .custom_dict([("自訂", "自訂")])
    .build();
assert_eq!(conv.convert("自訂伺服器"), "自訂伺服器");

// Check
let hits = zhtw::check("使用者權限");
assert_eq!(hits[0].start, 0);  // codepoint index
assert_eq!(hits[0].source, "使用者");
assert_eq!(hits[0].target, "使用者");

// Lookup
let detail = zhtw::lookup("軟體");
assert!(detail.changed);
assert_eq!(detail.output, "軟體");
```

---

## §3 · Build-time 資料管線（`zhtw/build.rs`）

> **[IMPORTANT — 2026-04-10 spike finding]**
> 原本設計打算用 `aho-corasick` 的 `to_bytes_native_endian()` / `from_bytes()`，spike 驗證發現 **這些 API 不存在**於公開表面（docs.rs 確認 `aho-corasick` v1.1.x 無序列化 API）。
>
> **選定 `daachorse::CharwiseDoubleArrayAhoCorasick`** 的原因：
> - 原生 `Serializable` trait（`serialize`/`deserialize_unchecked`）支援預編譯 automaton bytes
> - Charwise 變體用 Unicode codepoint 做 state transition，對 CJK 多位元組文字效能更好
> - 在日本 NLP 生態（vibrato/vaporetto）已 production-proven
>
> Rationale wording（for README / commit message）:
> > We choose `daachorse` over `aho-corasick` because the Rust `aho-corasick` crate does not expose a stable automaton serialization API, while `daachorse` provides native serialization for double-array automata and a charwise implementation optimized for multibyte text. This enables build-time automaton generation and near-zero runtime construction cost for the default converter.

### 3.1 Build flow

```
sdk/data/zhtw-data.json  (~38K lines, ~1.5 MB)
          │
          ▼  zhtw/build.rs (編譯期執行)
┌────────────────────────────────────────────────────────┐
│ 1. serde_json parse → RawZhtwData                      │
│ 2. Split: term_dict{cn,hk} + char_map                  │
│ 3. Produce 3 artifacts to $OUT_DIR:                    │
│    a) generated_maps.rs     (phf::Map macro output)    │
│    b) automaton-cnhk.bin    (daachorse serialized +    │
│                              magic header)             │
│    c) pattern-table-cnhk.bin (pattern_id → (src, tgt)) │
└────────────────────────────────────────────────────────┘
          │
          ▼  runtime (include_bytes! + deserialize)
┌────────────────────────────────────────────────────────┐
│ Converter::default_instance() → LazyLock::new(|| {     │
│   verify_magic_header(AUTOMATON_BYTES)?;               │
│   let pma = unsafe {                                    │
│     CharwiseDoubleArrayAhoCorasick::deserialize_unchecked│
│       (&AUTOMATON_BYTES[HEADER_LEN..])                 │
│   };                                                    │
│   Converter { pma, char_map, ... }                     │
│ })                                                      │
└────────────────────────────────────────────────────────┘
```

### 3.2 Magic header 格式（**Guardrail 2**）

`deserialize_unchecked` 是 `unsafe` — 餵錯格式會 UB。所以 build.rs 產出的每個 bytes blob 前面都包一層自製 header：

```rust
// zhtw/src/matcher.rs (shared struct, used by both build.rs and runtime)
#[repr(C)]
pub(crate) struct AutomatonHeader {
    /// "ZHTWDAAC" (8 bytes)
    pub magic: [u8; 8],
    /// Schema version of this header format itself (u16, currently 1)
    pub header_version: u16,
    /// daachorse crate version as packed (major<<16 | minor<<8 | patch)
    pub daachorse_version: u32,
    /// Hash of sdk/data/zhtw-data.json (first 8 bytes of blake3)
    pub dict_hash: [u8; 8],
    /// Source set encoded: bit 0 = Cn, bit 1 = Hk
    pub source_mask: u8,
    /// Reserved for future use
    pub _reserved: [u8; 5],
}

const ZHTW_AUTOMATON_MAGIC: [u8; 8] = *b"ZHTWDAAC";
const CURRENT_HEADER_VERSION: u16 = 1;

pub(crate) fn verify_header(bytes: &[u8], expected_mask: u8) -> Result<&[u8]> {
    if bytes.len() < std::mem::size_of::<AutomatonHeader>() {
        panic!("zhtw: automaton bytes truncated");
    }
    let header: &AutomatonHeader = unsafe {
        &*(bytes.as_ptr() as *const AutomatonHeader)
    };
    if header.magic != ZHTW_AUTOMATON_MAGIC {
        panic!("zhtw: invalid automaton magic (corrupt or wrong format)");
    }
    if header.header_version != CURRENT_HEADER_VERSION {
        panic!(
            "zhtw: automaton header version mismatch (got {}, expected {})",
            header.header_version, CURRENT_HEADER_VERSION
        );
    }
    if header.source_mask != expected_mask {
        panic!("zhtw: automaton source mask mismatch");
    }
    // dict_hash verification is build-time only; runtime trusts it
    // (it's baked into the binary alongside the data that was used to build it)
    Ok(&bytes[std::mem::size_of::<AutomatonHeader>()..])
}
```

**Panic policy rationale:** 這些 assertion failure 代表 binary 本身被破壞或錯誤 build，panic 是正確反應；不該試圖 fallback 或 silently swallow。這些都是 `build.rs` 產物，使用者正常流程不會觸發。

### 3.3 `build.rs` 骨架

```rust
// sdk/rust/zhtw/build.rs
use std::{env, fs, path::PathBuf};
use daachorse::CharwiseDoubleArrayAhoCorasick;
// ... other imports

const DATA_JSON: &str = "../../data/zhtw-data.json";

fn main() {
    println!("cargo:rerun-if-changed={}", DATA_JSON);
    println!("cargo:rerun-if-changed=build.rs");

    let json_str = fs::read_to_string(DATA_JSON)
        .expect("sdk/data/zhtw-data.json missing — run `zhtw export` to regenerate");
    let raw: RawZhtwData = serde_json::from_str(&json_str)
        .expect("zhtw-data.json schema drift — Python producer out of sync with Rust reader");

    // Compute dict hash for header
    let dict_hash = blake3_first_8_bytes(json_str.as_bytes());

    let out_dir = PathBuf::from(env::var("OUT_DIR").unwrap());

    // 1. Char map → phf codegen
    generate_char_map(&raw, &out_dir);

    // 2. Automaton for (Cn + Hk) default set
    generate_automaton(
        &raw,
        SourceMask::CN | SourceMask::HK,
        dict_hash,
        out_dir.join("automaton-cnhk.bin"),
        out_dir.join("pattern-table-cnhk.bin"),
    );

    // 3. Optional: also produce Cn-only automaton if we decide to
    //    pre-compile that case. v1: skip (custom sources → runtime build).
}
```

### 3.4 Runtime automaton 策略（**Guardrail 4**）

```
Config → Converter::new:
  ┌─ sources == [Cn, Hk] AND custom_dict.is_empty()
  │   → 走預編譯路徑：deserialize AUTOMATON_BYTES (LazyLock shared)
  │
  └─ 否則（自訂 sources 或有 custom_dict）
      → 走 runtime build：
         1. 從記憶體裡的 PATTERN_TABLE 篩選符合 sources 的詞條
         2. Merge custom_dict（覆蓋 built-in，同 key 以 custom 為準）
         3. 當場 CharwiseDoubleArrayAhoCorasick::new(patterns)
         4. 這條路徑會比預設慢（估 50-200 ms init，依 pattern 數量），但只付一次
```

**為什麼這樣拆：** 99% 的使用者呼叫 `zhtw::convert()` 走預設 → 零建構成本。少數自訂使用者付一次 runtime build cost → acceptable。不這樣拆的話，預設路徑也要付建構成本，直接把 daachorse 預編譯的優勢吐回去。

### 3.5 Match semantics（**Guardrail 5**）— longest-match + identity protection

**重要：** `daachorse::MatchKind::LeftmostLongest` 只給 longest + non-overlapping，**不處理 identity mapping 的保護語意**。Python / Java / TS 三個 SDK 實作的是更細的語意：

```
Algorithm (port from src/zhtw/matcher.py:60-133):

1. Collect ALL matches including identity (source == target)
   - 用 daachorse find_iter with LeftmostLongest
   - Iterator 回傳 (start_byte, end_byte, pattern_id)
   - 從 PATTERN_TABLE 查 (source, target)

2. Build "protected ranges":
   - Identity matches (source == target) 如果 NOT fully contained in a
     longer non-identity match → 加進 protected set
   - 目的：保護「檔案」不被「檔案→檔案」誤轉；但「件」被「軟體」完全包住
     時不保護（它其實不在表面文字上）

3. Filter:
   - 左到右掃描 sorted matches
   - Skip if start < last_end (overlap)
   - Skip if non-identity 且範圍內有 protected codepoint
   - Emit non-identity matches; identity matches 只扮演 blocker，不 emit

4. Output:
   - convert() → 套用 emitted matches 到字串 + 字元層 fallback
   - check() → 回傳 emitted matches as Vec<Match> (codepoint indices)
   - lookup(word) → check(word) + 對殘餘字元跑 char_map
```

Rust 實作見 `zhtw/src/matcher.rs`，會直接 port Python 的 `find_matches` 函式。**這是 v1 必須測試的核心語意**，`tests/golden.rs` 和 Python 行為 byte-for-byte 相同就代表 port 正確。

### 3.6 Cross-platform / cross-target 注意事項

- **`build.rs` 永遠在 host 平臺執行**（即使 `--target wasm32-unknown-unknown`）。
- **daachorse 的序列化格式** — 需要在 M2 spike 時 confirm 是否 endian-safe。如果不是，`build.rs` 要 branch on `CARGO_CFG_TARGET_ENDIAN`。假設 daachorse 預設是 LE（所有現代平臺包含 wasm32 都是 LE），99% 情況沒問題。
- **`zhtw/Cargo.toml` `[package].include`** 必須明確列：`src/**, build.rs, Cargo.toml, ../../data/zhtw-data.json`，**不含** `OUT_DIR/*`。crates.io tarball 不攜帶預編譯產物；使用者 `cargo build` 時本機重跑 `build.rs`。

### 3.7 Build time 成本（估）

| 階段 | 成本（粗估） |
|------|-------------|
| serde_json parse 38K lines | ~200 ms |
| phf codegen (6,344 entries) | ~100 ms |
| daachorse build (31K patterns, charwise) | ~500-1500 ms |
| Serialize automaton to bytes | ~50 ms |
| rustc compile `generated_maps.rs` (~250KB phf) | ~3-5 s |
| **Total clean build overhead** | **~5-8 s** |
| Incremental build (JSON unchanged) | 0（cargo skip build.rs） |

**Guardrail 1**：這些數字是**目標而非承諾**。真實數字在 M2 benchmark 後填進 spec 和 README。

---

## §4 · `zhtw-wasm` bindings 與 npm 產出

### 4.1 Build toolchain

**決策：** `wasm-pack build --target bundler`

- `wasm-bindgen` 產 JS glue + TypeScript `.d.ts`
- `--target bundler` 輸出 ESM，適合 webpack/vite/rollup，和 `zhtw-js` bundler-first 定位一致
- 捨棄 `--target web`/`nodejs`/`no-modules` — 見設計討論的 rationale

### 4.2 `zhtw-wasm/src/lib.rs` 骨架

```rust
use wasm_bindgen::prelude::*;
use zhtw::{Converter as CoreConverter, Source};

// ─── Zero-config free functions (aligned with zhtw-js) ───

#[wasm_bindgen]
pub fn convert(text: &str) -> String {
    zhtw::convert(text)
}

#[wasm_bindgen]
pub fn check(text: &str) -> Result<JsValue, JsValue> {
    serde_wasm_bindgen::to_value(&zhtw::check(text)).map_err(Into::into)
}

#[wasm_bindgen]
pub fn lookup(word: &str) -> Result<JsValue, JsValue> {
    serde_wasm_bindgen::to_value(&zhtw::lookup(word)).map_err(Into::into)
}

// ─── createConverter factory ───

#[wasm_bindgen]
pub struct Converter {
    inner: CoreConverter,
}

#[wasm_bindgen]
impl Converter {
    #[wasm_bindgen(js_name = convert)]
    pub fn convert(&self, text: &str) -> String {
        self.inner.convert(text)
    }

    #[wasm_bindgen(js_name = check)]
    pub fn check(&self, text: &str) -> Result<JsValue, JsValue> {
        serde_wasm_bindgen::to_value(&self.inner.check(text)).map_err(Into::into)
    }

    #[wasm_bindgen(js_name = lookup)]
    pub fn lookup(&self, word: &str) -> Result<JsValue, JsValue> {
        serde_wasm_bindgen::to_value(&self.inner.lookup(word)).map_err(Into::into)
    }
}

#[wasm_bindgen(js_name = createConverter)]
pub fn create_converter(options: JsValue) -> Result<Converter, JsValue> {
    let sources = parse_sources_from_js(&options)?;
    let custom_dict = parse_custom_dict_from_js(&options)?;
    let mut builder = CoreConverter::builder().sources(sources);
    if let Some(dict) = custom_dict {
        builder = builder.custom_dict(dict);
    }
    Ok(Converter { inner: builder.build() })
}

// internal helpers: parse_sources_from_js, parse_custom_dict_from_js
```

### 4.3 Public `.d.ts` surface（must match `zhtw-js`）

```typescript
// 手改 wasm-pack output 以移除 `any`
export type Source = 'cn' | 'hk';

export interface Match {
  start: number;
  end: number;
  source: string;
  target: string;
}

export interface ConversionDetail {
  source: string;
  target: string;
  layer: 'term' | 'char';
  position: number;
}

export interface LookupResult {
  input: string;
  output: string;
  changed: boolean;
  details: ConversionDetail[];
}

export interface ConverterOptions {
  sources?: Source[];
  customDict?: Record<string, string>;
}

export interface Converter {
  convert(text: string): string;
  check(text: string): Match[];
  lookup(word: string): LookupResult;
}

export function convert(text: string): string;
export function check(text: string): Match[];
export function lookup(word: string): LookupResult;
export function createConverter(options?: ConverterOptions): Converter;
```

**Invariant:** 這個 surface 必須是 `sdk/typescript/src/core/types.ts` 的 superset 或 identical。CI gate（§4.4）強制。

### 4.4 CI gate：TypeScript 型別相容性

新增 job 到 `sdk-rust.yml`：

```yaml
typescript-compat:
  needs: wasm
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-node@v4
      with: { node-version: '22' }
    - name: Install TypeScript + both SDKs
      run: |
        npm install -g typescript@5
        npm pack sdk/typescript --pack-destination /tmp/
        # (wasm build in previous job produces pkg/)
    - name: Cross-assign type test
      run: |
        cat > /tmp/compat.ts <<'EOF'
        import type * as js from 'zhtw-js';
        import type * as wasm from 'zhtw-wasm';

        const a: typeof js.convert = wasm.convert;
        const b: typeof wasm.convert = js.convert;
        const c: typeof js.createConverter = wasm.createConverter;
        EOF
        tsc --noEmit --strict /tmp/compat.ts
```

### 4.5 Binary size 預算

| 專案 | 大小（估，M7 後實測填入） |
|------|--------------------------|
| daachorse crate（runtime） | ~100 KB |
| 預編譯 automaton bytes | ~300-500 KB |
| phf CHAR_MAP | ~50 KB |
| wasm-bindgen + js-sys | ~80 KB |
| serde + serde-wasm-bindgen | ~60 KB |
| zhtw crate logic | ~30 KB |
| **Estimated `zhtw_wasm_bg.wasm`** | **~650-850 KB** |
| After `wasm-opt -O3` | **~500-700 KB** |
| After gzip | **~200-300 KB** |

**CI gate：** WASM binary > 1 MB → fail（Cloudflare Workers free tier 限制）。

### 4.6 Non-goals

1. **`zhtw-wasm` 不發 crates.io** — 只是 npm artifact，`Cargo.toml` 設 `publish = false`
2. **不暴露 Rust-specific API** — 沒有 `Source` enum 匯出（JS 只看 `'cn' | 'hk'` string literal type），沒有 `Error` enum 匯出（throw 即可）
3. **不做 Deno 相容版本** — v1 跳過，等使用者需求

---

## §5 · 測試策略

### 5.1 Layer 1 · Golden-test parity（CI gate）

```rust
// zhtw/tests/golden.rs
use std::collections::HashMap;
use serde::Deserialize;
use zhtw::{Converter, Source};

#[derive(Deserialize)]
struct GoldenFile {
    version: String,
    convert: Vec<ConvertCase>,
    check: Vec<CheckCase>,
    lookup: Vec<LookupCase>,
}

// ... case structs (fields match sdk/data/golden-test.json schema)

const GOLDEN_JSON: &str = include_str!("../../../data/golden-test.json");

#[test]
fn golden_version_matches_crate() {
    let golden: GoldenFile = serde_json::from_str(GOLDEN_JSON).unwrap();
    assert_eq!(
        golden.version,
        env!("CARGO_PKG_VERSION"),
        "golden-test.json version drift vs Cargo.toml — mono-versioning broken"
    );
}

#[test]
fn convert_parity() {
    let golden: GoldenFile = serde_json::from_str(GOLDEN_JSON).unwrap();
    let mut failures = Vec::new();

    for (idx, case) in golden.convert.iter().enumerate() {
        let sources: Vec<Source> = case.sources.iter()
            .map(|s| s.parse().expect("known source"))
            .collect();
        let conv = Converter::builder()
            .sources(sources)
            .custom_dict(case.custom_dict.clone().unwrap_or_default())
            .build();
        let actual = conv.convert(&case.input);
        if actual != case.expected {
            failures.push(format!(
                "[{}] input={:?}\n  expected={:?}\n  actual  ={:?}",
                idx, case.input, case.expected, actual
            ));
        }
    }

    assert!(
        failures.is_empty(),
        "convert parity failed ({} cases):\n{}",
        failures.len(),
        failures.join("\n")
    );
}

#[test]
fn check_parity() { /* identical structure for check */ }

#[test]
fn lookup_parity() { /* identical structure for lookup */ }
```

### 5.2 Layer 2 · Codepoint index correctness

```rust
// zhtw/tests/codepoint_index.rs

#[test]
fn check_returns_codepoint_not_byte_index() {
    // "中 X 軟體" — 6 codepoints, 11 bytes
    let text = "中 X 軟體";
    let hits = zhtw::check(text);
    assert_eq!(hits.len(), 1);
    assert_eq!(hits[0].start, 4);  // 中=0, space=1, X=2, space=3, 軟=4
    assert_eq!(hits[0].end, 6);    // exclusive
    // If start == 6 or end == 11, we're returning byte indices (bug)
}

#[test]
fn lookup_position_is_codepoint() {
    // 中 = 3 bytes, 軟 = 3 bytes, 件 = 3 bytes; ASCII = 1 byte.
    // "中文a軟體" → codepoints: [中=0, 文=1, a=2, 軟=3, 件=4]
    //              bytes:      [中=0..3, 文=3..6, a=6..7, 軟=7..10, 件=10..13]
    // 軟體 match: codepoint start=3, byte start=7 — MUST return 3.
    let result = zhtw::lookup("中文a軟體");
    let term = result.details.iter()
        .find(|d| d.source == "軟體")
        .expect("軟體 match");
    assert_eq!(term.position, 3, "must be codepoint (3), not byte (7)");
}

#[test]
fn supplementary_plane_chars() {
    // "𠮷" is U+20BB7, one codepoint, 4 UTF-8 bytes.
    // "𠮷軟體" → codepoints: [𠮷=0, 軟=1, 件=2]
    //            bytes:      [𠮷=0..4, 軟=4..7, 件=7..10]
    // 軟體 match: codepoint start=1, byte start=4 — MUST return 1.
    let text = "𠮷軟體";
    let hits = zhtw::check(text);
    assert_eq!(hits[0].start, 1, "must be codepoint (1), not byte (4)");
    assert_eq!(hits[0].end, 3, "must be codepoint (3), not byte (10)");
}
```

### 5.3 Layer 3 · Criterion benchmarks

```rust
// zhtw/benches/convert.rs
use criterion::{black_box, criterion_group, criterion_main, Criterion, Throughput, BenchmarkId};

fn bench_convert_single(c: &mut Criterion) {
    let text = "這個軟體需要最佳化";
    c.bench_function("convert/single_sentence", |b| {
        b.iter(|| zhtw::convert(black_box(text)))
    });
}

fn bench_convert_throughput(c: &mut Criterion) {
    let mut group = c.benchmark_group("convert/throughput");
    for size_kb in &[1, 10, 100, 1024] {
        let text = "這個軟體需要最佳化，伺服器的使用者權限請聯繫管理員。"
            .repeat(size_kb * 1024 / 30);
        group.throughput(Throughput::Bytes(text.len() as u64));
        group.bench_with_input(
            BenchmarkId::from_parameter(format!("{}KB", size_kb)),
            &text,
            |b, t| b.iter(|| zhtw::convert(black_box(t))),
        );
    }
    group.finish();
}

fn bench_default_instance_access(c: &mut Criterion) {
    c.bench_function("init/default_instance_access", |b| {
        b.iter(|| zhtw::Converter::default_instance())
    });
}

criterion_group!(benches,
    bench_convert_single,
    bench_convert_throughput,
    bench_default_instance_access,
);
criterion_main!(benches);
```

### 5.4 Regression gate（**Guardrail 1 的實踐**）

- CI job 在 PR 上跑 baseline（main）+ PR bench 比對
- 初始門檻：5% regression → fail
- 實測如果 false positive 率 > 10% → 放寬到 10%
- 門檻和實測數字在 spec follow-up 更新

### 5.5 測試檔案總表

| 檔案 | 內容 | CI 階段 |
|------|------|---------|
| `tests/golden.rs` | parity vs `sdk/data/golden-test.json` | test (blocking) |
| `tests/codepoint_index.rs` | byte vs codepoint + supplementary plane | test (blocking) |
| `tests/api.rs` | Builder, free fn, `default_instance`, `Send+Sync`, `Clone` | test (blocking) |
| `tests/custom_dict.rs` | 自訂詞條覆寫 + 衝突解析 | test (blocking) |
| `benches/convert.rs` | criterion: 單句延遲, 1MB 吞吐, default access | benchmark |
| `benches/check.rs` | criterion: check 收集 overhead | benchmark |
| `zhtw-wasm/tests/web.rs` | wasm-bindgen-test: 煙霧 + golden 子集 | wasm-test |

---

## §6 · Release 流程與 CI 整合

### 6.1 Mono-versioning 擴充（從 7 點變 8 點）

| # | 檔案 | 內容 |
|---|------|------|
| 1 | `pyproject.toml` | `version = "X.Y.Z"` |
| 2 | `src/zhtw/__init__.py` | `__version__ = "X.Y.Z"` |
| 3 | `sdk/java/pom.xml` | `<version>X.Y.Z</version>` |
| 4 | `sdk/typescript/package.json` | `"version": "X.Y.Z"` |
| 5 | `sdk/rust/Cargo.toml` | `[workspace.package] version = "X.Y.Z"`（**語意改變：workspace root**） |
| 6 | `sdk/dotnet/Zhtw.csproj` | `<Version>X.Y.Z</Version>` |
| 7 | `sdk/data/zhtw-data.json` + `golden-test.json` | `zhtw export` 重新產生 |
| **8** | **`sdk/rust/zhtw-wasm/package.json`** | **`"version": "X.Y.Z"`** — 新增 |

**`Makefile` bump 規則更新：**

```makefile
# 原本（single crate）
@sed -i '' 's|^version = "[0-9][0-9.]*"|version = "$(VERSION)"|' sdk/rust/Cargo.toml

# 改成（workspace，鎖定 [workspace.package] 區段）
@sed -i '' '/^\[workspace\.package\]/,/^\[/ s|^version = "[0-9][0-9.]*"|version = "$(VERSION)"|' sdk/rust/Cargo.toml

# 新增：zhtw-wasm package.json
@sed -i '' 's|"version": "[0-9][0-9.]*"|"version": "$(VERSION)"|' sdk/rust/zhtw-wasm/package.json
```

**`make version-check` 也要同步擴充**以檢查這兩個新位置。

**CLAUDE.md 的黃金規則 6 表格也要更新為 8 檔。**

### 6.2 `zhtw-wasm/package.json` 維護策略

**決策：B（checked-in + build-time sync）**

- `sdk/rust/zhtw-wasm/package.json` 是主版本來源，checked-in git
- `wasm-pack build` 會產 `pkg/package.json`，build step 再從 checked-in source 複製版本欄位覆蓋
- 好處：`make version-check` 能守到，和 `sdk/typescript/package.json` 處理方式一致
- 成本：Build step 多 3 行 sed

### 6.3 替換 `sdk-rust.yml`（殺掉 fake-green）

**現況（刪除）：**
```yaml
- name: Build
  working-directory: sdk/rust
  run: echo "TODO — SDK not yet implemented"   # fake green
```

**替換後（完整 pipeline）：**

```yaml
name: SDK Rust

on:
  push:
    paths: ['sdk/rust/**', 'sdk/data/**', '.github/workflows/sdk-rust.yml']
  pull_request:
    paths: ['sdk/rust/**', 'sdk/data/**', '.github/workflows/sdk-rust.yml']
  release:
    types: [published]

jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: dtolnay/rust-toolchain@stable
      - uses: Swatinem/rust-cache@v2
        with: { workspaces: sdk/rust }
      - run: cargo build -p zhtw --release
        working-directory: sdk/rust
      - run: cargo test -p zhtw --release
        working-directory: sdk/rust
      - run: cargo clippy -p zhtw -- -D warnings
        working-directory: sdk/rust
      - run: cargo fmt --check
        working-directory: sdk/rust

  wasm:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: dtolnay/rust-toolchain@stable
        with: { targets: wasm32-unknown-unknown }
      - uses: Swatinem/rust-cache@v2
        with: { workspaces: sdk/rust }
      - name: Install wasm-pack
        run: curl https://rustwasm.github.io/wasm-pack/installer/init.sh -sSf | sh
      - name: Build zhtw-wasm
        working-directory: sdk/rust/zhtw-wasm
        run: wasm-pack build --target bundler --release
      - name: Sync version from checked-in package.json
        working-directory: sdk/rust/zhtw-wasm
        run: |
          version=$(jq -r .version package.json)
          jq ".version = \"$version\"" pkg/package.json > pkg/package.json.tmp
          mv pkg/package.json.tmp pkg/package.json
      - name: Binary size gate
        working-directory: sdk/rust/zhtw-wasm/pkg
        run: |
          size=$(wc -c < zhtw_wasm_bg.wasm)
          echo "WASM size: $size bytes"
          if [ $size -gt 1048576 ]; then
            echo "::error::WASM > 1 MB — Cloudflare Workers free tier broken"
            exit 1
          fi
      - name: Headless browser test
        working-directory: sdk/rust/zhtw-wasm
        run: wasm-pack test --headless --chrome

  typescript-compat:
    needs: wasm
    runs-on: ubuntu-latest
    steps:
      # As specified in §4.4

  benchmark:
    if: github.event_name == 'pull_request'
    needs: test
    runs-on: ubuntu-latest
    steps:
      # As specified in §5.4

  publish-crates-io:
    needs: [test, wasm, typescript-compat]
    if: github.event_name == 'release' && github.event.action == 'published'
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: dtolnay/rust-toolchain@stable
      - uses: rust-lang/crates-io-auth-action@v1
        id: auth
      - name: Publish zhtw to crates.io
        working-directory: sdk/rust/zhtw
        env:
          CARGO_REGISTRY_TOKEN: ${{ steps.auth.outputs.token }}
        run: cargo publish

  publish-npm:
    needs: [test, wasm, typescript-compat]
    if: github.event_name == 'release' && github.event.action == 'published'
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: dtolnay/rust-toolchain@stable
        with: { targets: wasm32-unknown-unknown }
      - uses: actions/setup-node@v4
        with:
          node-version: '22'
          registry-url: 'https://registry.npmjs.org'
      - run: curl https://rustwasm.github.io/wasm-pack/installer/init.sh -sSf | sh
      - name: Build zhtw-wasm
        working-directory: sdk/rust/zhtw-wasm
        run: wasm-pack build --target bundler --release
      - name: Sync package.json version
        working-directory: sdk/rust/zhtw-wasm
        run: |
          version=$(jq -r .version package.json)
          jq ".version = \"$version\"" pkg/package.json > pkg/package.json.tmp
          mv pkg/package.json.tmp pkg/package.json
      - name: Upgrade npm for Trusted Publishing
        run: npm install -g npm@latest
      - name: Publish zhtw-wasm to npm
        working-directory: sdk/rust/zhtw-wasm/pkg
        run: npm publish --access public --provenance
```

### 6.4 Publish 廣播（3 條 → 5 條）

發 release 後同時觸發 5 個 publish workflow，**maintainer 必須檢查全部綠燈**：

| Workflow | 目標 |
|----------|------|
| `publish.yml` | PyPI |
| `sdk-java.yml` | Maven Central |
| `sdk-typescript.yml` | npm (`zhtw-js`) |
| `sdk-rust.yml` (publish-crates-io) | **crates.io (`zhtw`) ← 新** |
| `sdk-rust.yml` (publish-npm) | **npm (`zhtw-wasm`) ← 新** |

CLAUDE.md 的 release 檢查清單要更新。

### 6.5 首發手動流程（一次性，v1 release 前執行）

**Trusted Publishing 需要 package 已存在才能設定**（和 npm 相同 chicken-and-egg）。

#### 6.5.1 crates.io 首發

```bash
cd sdk/rust/zhtw
cargo login
cargo publish --dry-run
cargo publish

# 上架後設 Trusted Publisher:
#   URL: https://crates.io/crates/zhtw/settings
#   Repository owner: rajatim
#   Repository name: zhtw
#   Workflow filename: sdk-rust.yml
#   Environment: (留空)
#   Job name: publish-crates-io
```

#### 6.5.2 npm `zhtw-wasm` 首發

```bash
cd sdk/rust/zhtw-wasm
wasm-pack build --target bundler --release
cd pkg
# 如果啟用 2FA: 需要 OTP
npm publish --access public --provenance

# 上架後設 Trusted Publisher:
#   URL: https://www.npmjs.com/package/zhtw-wasm/access
#   Publishing access: "Require 2FA and disallow tokens"
#   Trusted Publisher:
#     Provider: GitHub Actions
#     Owner: rajatim
#     Repo: zhtw
#     Workflow filename: sdk-rust.yml
#     Environment: (留空)
```

**寫進新 reference memory** `reference_crates_io_trusted_publishing.md`，記錄流程細節和踩坑。

### 6.6 CHANGELOG 範本

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- **Rust SDK**: new `zhtw` crate published to crates.io
  - Feature parity with Java / TypeScript SDK (`convert`, `check`, `lookup`, `sources`, `custom_dict`)
  - Compile-time `phf::Map` character layer (zero runtime hash construction)
  - Pre-compiled `daachorse::CharwiseDoubleArrayAhoCorasick` embedded via `build.rs`
  - Native codepoint-based state transitions optimized for multibyte CJK text
  - Byte-for-byte parity with Python / Java / TypeScript via shared `sdk/data/golden-test.json`
- **WASM SDK**: new `zhtw-wasm` npm package (Rust core compiled to WebAssembly)
  - Drop-in API compatible with `zhtw-js`
  - Published via npm Trusted Publishing (OIDC, no token)

### Changed
- `make bump` updates 8 locations (added `sdk/rust/zhtw-wasm/package.json`)
- `sdk/rust/` converted from single-crate scaffold to workspace (`zhtw` + `zhtw-wasm`)
- `.github/workflows/sdk-rust.yml` replaced (was fake-green stub before)
- CLAUDE.md golden rule 6 updated: 7 → 8 mono-versioning locations
```

---

## §7 · Non-goals, Open Questions, Invariants, Risks, Milestones

### 7.1 Non-goals（v1 刻意不做）

1. `zhtw-wasm` 不發 crates.io — 只是 npm artifact，`Cargo.toml` `publish = false`
2. 不吸收進 `zhtw-js` v5 — 保持獨立套件（選擇權策略）
3. 不做 `Converter` trait 抽象（YAGNI，沒有第二個實作）
4. 不做 `no_std` 支援 — WASM 已 cover 受限環境
5. 不做並行 convert（`convert_par`）— text 通常不夠大，thread pool overhead 主導
6. 不做 streaming API — 無使用者需求
7. 不重新設計 `zhtw-data.json` schema — 只讀 Python 端現有產出
8. 不做 Component Model (WIT) bindings — 生態未成熟
9. v1 `Error` 只有 `InvalidSource` 一個 variant，`#[non_exhaustive]` 保留擴充
10. 不加 feature flags — 所有 v1 功能預設開啟

### 7.2 Open Questions（不 block v1，追蹤後續）

1. **Release status aggregator workflow** — 從 3 條 publish 變 5 條，需要集中 dashboard。v1 後評估。
2. **Post-release smoke test** — 自動 `cargo install zhtw` + `npm install zhtw-wasm` e2e 測試。v1 手動，v2 自動化。
3. **Deno 相容版本** — 等使用者提需求。
4. **Criterion regression gate 5% 門檻**是否合理 — 實測後調整。
5. **wasm-opt 最佳化 level** — v1 `-O3`，之後實測 `-Oz`（小但慢）的 trade-off。
6. **`zhtw` crate 的 `keywords` / `categories` / `description`** — 實作時填 crates.io 可搜尋的字串。

### 7.3 Invariants（實作和 refactor 必須守住）

1. **Golden-test parity is a release gate** — `tests/golden.rs` 失敗 → 不能 tag release
2. **`zhtw-wasm` 公開 TS 型別 = `zhtw-js` 公開 TS 型別（superset 或 identical）** — `typescript-compat` CI gate 守門
3. **`convert()` 熱路徑不付 JSON parsing 或 automaton build 成本**（預設 sources + 無 custom_dict 時）— `LazyLock` + 預編譯 bytes 實作
4. **`Converter: Send + Sync`** — compile-time 強制，加 non-Send 欄位自動紅字
5. **`sdk/rust/Cargo.toml` `[workspace.package].version` 永遠等於其他 7 個 mono-version 位置** — `make version-check` 守門
6. **`sdk-rust.yml` 不可退回 `echo "TODO"` fake-green pattern** — 任何替代都必須執行真實建置
7. **Automaton bytes 必須帶 magic header + 版本驗證** — 升級 daachorse 必須重跑 build，golden test 必須全綠

### 7.4 風險與緩解

| 風險 | 機率 | 影響 | 緩解 |
|------|------|------|------|
| `daachorse::CharwiseDoubleArrayAhoCorasick` 的序列化 API 實際 signature 和假設不同 | 中 | 中 | M2 spike 先驗證 serialize/deserialize_unchecked 真實可用；失敗 → fallback 到 runtime build（放棄 §3 最大效能優勢但還是能 ship） |
| `phf_codegen` 對 6344 entries 編譯過慢（>1 分鐘） | 低 | 中 | Fallback 到 `match` 語句 generator 或排序 `[(char, char); N]` + binary search |
| Criterion gate 雜訊造成 false positive | 中 | 低 | 門檻 5% → 10% |
| `wasm-pack` 產出 `.d.ts` 手改覆蓋不穩定 | 低 | 中 | 用 `#[wasm_bindgen(typescript_type = "...")]` attribute 在 Rust 端註記 |
| crates.io Trusted Publishing UI 首發陷阱 | 高 | 低 | 已有 npm 經驗；流程即時寫 reference memory |
| 跨 target endianness bug（host build → target run） | 低 | 高 | M2 確認 daachorse 序列化格式是否 endian-safe；若不是，build.rs 強制 LE |
| daachorse minor 版本升級破壞序列化格式 | 中 | 高 | `Cargo.toml` 用 `=1.0.x` 精確 pin；升級 daachorse 必須重跑 build + golden test |
| Identity-protection 語意 port 錯誤導致誤轉 | 中 | 高 | `tests/golden.rs` + `tests/custom_dict.rs` 是直接守門；Python 的 `find_matches` 60-133 行直接對照 port |

### 7.5 裡程碑拆分（給 writing-plans 用）

| M | 目標 | 完成條件 |
|---|------|---------|
| **M1** | Workspace 骨架 | `sdk/rust/Cargo.toml` → workspace root, `zhtw/` + `zhtw-wasm/` 空 crate, `make bump` / `make version-check` 更新, `cargo check` 綠燈 |
| **M2** | Build.rs 資料管線 + daachorse API spike | build.rs 能產 `generated_maps.rs` + `automaton-cnhk.bin` + magic header; 單測驗 generated files 能 load |
| **M3** | Core converter (convert) | `Config` / `Builder` / `Source` / `Converter::new` / `convert()` — `tests/api.rs` + 簡易 convert 測試透過 |
| **M4** | Matcher + identity protection + check/lookup | Port Python `find_matches`; `matcher.rs` byte↔cp 對映; `check()` / `lookup()` — `tests/codepoint_index.rs` 透過 |
| **M5** | Golden parity（核心完成） | `tests/golden.rs` 全綠 = Rust core done |
| **M6** | Criterion benchmarks | `benches/convert.rs` + `benches/check.rs` 有真數字；README placeholder 可以填 |
| **M7** | `zhtw-wasm` 薄包裝 | `zhtw-wasm/src/lib.rs` + `tests/web.rs` 過, `wasm-pack build` 綠燈 |
| **M8** | TypeScript 相容 gate | `.d.ts` 手改完成, `typescript-compat` CI job 綠燈 |
| **M9** | CI pipeline 完整替換 | `sdk-rust.yml` 從 fake-green 換成 §6.3 完整 yaml，所有 job（除 publish）綠燈 |
| **M10** | 手動首發 + Trusted Publisher 設定 | 本機 `cargo publish` + `npm publish` 成功, 兩個 UI Trusted Publisher 設好, `reference_crates_io_trusted_publishing.md` 寫好 |
| **M11** | README / CHANGELOG / CLAUDE.md 同步 | README 新增 Rust 段落, CLAUDE.md 規則 6 升級 7→8, CHANGELOG 填好 |

每個 M 對應一組 commits，TDD 節奏（先測試再實作）。

---

## Appendix A · 設計決策總表

| # | 決策 | 選項 |
|---|------|------|
| 1 | Workspace 結構 | `zhtw/` + `zhtw-wasm/` workspace |
| 2 | API 形狀 | Builder + `Source` enum + free functions, Config-first 內部 |
| 3 | Matcher crate | **`daachorse::CharwiseDoubleArrayAhoCorasick`**（非 `aho-corasick`） |
| 4 | 資料建置 | `build.rs` codegen → `phf::Map` 字元層 + 預編譯 automaton bytes + magic header |
| 5 | WASM 產品形狀 | 獨立 `zhtw-wasm` npm package, API 對齊 `zhtw-js` |
| 6 | v1 功能範圍 | 全功能 (`convert`/`check`/`lookup`/`sources`/`custom_dict`) + criterion benchmarks |
| 7 | 釋出機制 | crates.io + npm 雙 Trusted Publishing (OIDC) |
| 8 | MSRV | 1.80 (LazyLock stabilization) |
| 9 | Match semantics | Longest-match + non-overlapping + identity protection (port Python `find_matches`) |
| 10 | `custom_dict` 策略 | 預設走預編譯; 自訂或 non-default sources 走 runtime build |
| 11 | Panic policy | Automaton header 驗證失敗 → panic (不 fallback) |
| 12 | `zhtw-wasm/package.json` | Checked-in, build 時同步到 `pkg/package.json` |

---

## Appendix B · 被取代的設計假設（為什麼留這段）

記錄被 spike 否決的設計假設，避免未來有人又想走回頭路：

1. **`aho-corasick::AhoCorasick::to_bytes_native_endian()` + `from_bytes()`** — 不存在於 v1.1.x 公開 API。原本以為存在是和 `regex-automata` 混淆。
2. **用 `aho-corasick` 在 `default_instance()` 初始化時 build automaton** — 31K patterns build 成本 ~2-4 秒，不可接受為 cold start。
3. **兩套 DFA bytes（Cn-only 和 CnHk 各一份）** — 簡化為單一 CnHk 預編譯；Cn-only 走 runtime build path（同 custom_dict）。省 ~1.2 MB binary 大小，犧牲的是「只用 Cn」場景的 init 速度，但這個場景少。
