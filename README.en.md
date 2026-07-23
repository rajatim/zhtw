# ZHTW

**English** · [繁體中文](README.md)

[![CI](https://github.com/rajatim/zhtw/actions/workflows/ci.yml/badge.svg)](https://github.com/rajatim/zhtw/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/rajatim/zhtw/branch/main/graph/badge.svg)](https://codecov.io/gh/rajatim/zhtw)
[![PyPI](https://img.shields.io/pypi/v/zhtw.svg)](https://pypi.org/project/zhtw/)
[![Maven Central](https://img.shields.io/maven-central/v/com.rajatim/zhtw.svg?label=maven%20central)](https://central.sonatype.com/artifact/com.rajatim/zhtw)
[![Homebrew](https://img.shields.io/badge/homebrew-tap-FBB040?logo=homebrew)](https://github.com/rajatim/homebrew-tap)
[![Downloads](https://img.shields.io/pypi/dm/zhtw.svg)](https://pypi.org/project/zhtw/)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Java](https://img.shields.io/badge/java-11+-orange.svg)](https://adoptium.net/)
[![npm](https://img.shields.io/npm/v/zhtw-js.svg?logo=npm)](https://www.npmjs.com/package/zhtw-js)
[![crates.io](https://img.shields.io/crates/v/zhtw.svg?logo=rust)](https://crates.io/crates/zhtw)
[![Go](https://img.shields.io/badge/go-1.21+-00ADD8.svg?logo=go)](https://pkg.go.dev/github.com/rajatim/zhtw/sdk/go/v4/zhtw)
[![NuGet](https://img.shields.io/nuget/v/Zhtw.svg)](https://www.nuget.org/packages/Zhtw)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<!-- zhtw:disable -->
**AI wrote your Chinese? Let zhtw vet it.**

Whether it's Copilot-generated code, Claude-written docs, or LLM-translated localization strings — fix simplified-Chinese leakage like `許可權` and `軟件` into real Taiwan Traditional Chinese.

One line of code, one CLI, six language SDKs.
<!-- zhtw:enable -->

<!-- zhtw:disable -->
```
Input:  服务器上的软件需要优化，用户权限请联系管理员
Output: 伺服器上的軟體需要最佳化，使用者權限請聯絡管理員
```
<!-- zhtw:enable -->

One `zhtw scan` / `zhtw fix` away — exactly what you need after an LLM ships you 100 files.

---

## Use Cases

| Scenario | Why zhtw |
|----------|----------|
| 🤖 **AI output post-processing** | Copilot / Cursor / Claude / GPT often emit simplified-Chinese leakage; zhtw fixes it before commit |
| 📝 **i18n / localization QA** | Traditional Chinese fields in i18n files; CI fails or auto-fixes |
| 📚 **Tech docs & comments** | Function names, comments, string literals — pre-commit hook keeps them consistent |
| 🏢 **Enterprise compliance** | External docs and customer deliverables in standardized Taiwan terminology, fully offline |

---

## Why ZHTW?

> **Prefer under-conversion over mis-conversion.**

Generic converters over-translate and silently corrupt words that were already correct in Taiwan usage. ZHTW takes the opposite stance: **only convert what we are sure should change; leave everything else alone.**

| | |
|------|------|
| **Low-misconversion priority** | 31,000+ curated terms + 6,360 character mappings; no mis-conversion observed in the designated 52-book / 100M-character corpus |
| **Fast scans** | Sustained 3,100 KB/s throughput; 1 MB of text in under a second |
| **Fully offline** | Nothing leaves your machine — safe for enterprise intranets |
| **CI-ready** | One line to add it to GitHub Actions; PRs get checked automatically |
| **Flexible opt-out** | Test fixtures or vendored code? Mark them once and ZHTW leaves them alone |

### Versus OpenCC

<!-- zhtw:disable -->
OpenCC is a general-purpose Simplified/Traditional conversion framework that applies character- and phrase-level substitutions in a single pass, so rules routinely fight each other — e.g. `权→權` converts 权限 into the (wrong) `許可權`. ZHTW targets **Simplified → Taiwan Traditional** specifically, using a layered approach (vocabulary layer first, then character layer) with longest-match context resolution for compound words.

| | OpenCC (s2twp) | ZHTW |
|---|------|------|
| **Goal** | General-purpose multi-variant conversion | Simplified → Taiwan Traditional |
| **Strategy** | Full character + phrase substitution | Vocabulary first, character layer as fallback |
| **Ambiguity** | Rule ordering | 102 ambiguous chars, tiered management + balanced mode disambiguation |
| **Dictionary** | Built-in char table + phrase list | 31,000+ curated Taiwan-specific terms |
| **Mis-conversions** | Common cases like `权限 → 許可權` | None observed in the designated 52-book / 100M-character corpus |
| **Ecosystem** | C++ core with multi-language bindings | CLI + Python/Java/TS/Rust/Go/C# SDK + pre-commit |

#### Precision Cases

The cases below come from the 2026-07-03 competitor-diff run over 500 curated corpus samples. Result: `candidate_gap = 0`, `zhtw_advantage = 308`. In this sample, no competitor matched the human expected output while ZHTW missed it; the differences mostly show generic converters over-converting or keeping Mainland terms.

On the latest like-for-like private set, v4.4.1 accepted 951/1,008 cases and the
current dictionary accepts 955/1,008: a net gain of four with no accepted-case
regression (about +0.40 percentage points). The 369 exact-sentence mappings are
conservative protection for known public regressions and are not counted as
fresh-blind generalization. These results do not establish a market-best claim.

| Input | Generic-converter risk | ZHTW |
|-------|------------------------|------|
| 写程序前先看法律程序 | 寫程式前先看法律程式 | 寫程式前先看法律程序 |
| 政府发布官方文件 | 政府釋出官方檔案 | 政府發布官方文件 |
| 保存文化遗产 | 儲存文化遺產 | 保存文化遺產 |
| 他的结婚对象很温柔 | 他的結婚物件很溫柔 | 他的結婚對象很溫柔 |
| 注销账户不是注销公司 | 登出賬戶不是登出公司 / 註銷帳戶不是註銷公司 | 登出帳戶不是註銷公司 |
| 通过异步回调来处理网络请求 | 通過異步回調來處理網絡請求 | 透過非同步回呼來處理網路請求 |
| 服务器证书即将过期 | 伺服器證書即將過期 | 伺服器憑證即將過期 |
| 后端服务返回状态码 | 後端服務返回狀態碼 | 後端服務回傳狀態碼 |
| 这个函数会抛出异常 | 這個函數會拋出異常 | 這個函式會拋出例外 |
| 撤销操作成功 | 撤銷操作成功 | 復原操作成功 |
| 评论区有人分享链接 | 評論區有人分享連結 | 留言區有人分享連結 |
| 台积电宣布扩大先进制程投资 | 臺積電宣布擴大先進位程投資 | 台積電宣布擴大先進製程投資 |

Full reports: `docs/reports/competitor-diffs-full-2026-07-03.md` and `docs/reports/competitor-advantage-review-2026-07-03.md`.

Want to see more side-by-side cases? Run `zhtw lookup 权限 服务器 用户`.
<!-- zhtw:enable -->

---

## Install

### macOS (Homebrew) — recommended

```bash
brew tap rajatim/tap
brew install zhtw
```

Upgrade: `brew upgrade zhtw`

### pip (all platforms)

```bash
python3 -m pip install zhtw
```

Upgrade: `pip install --upgrade zhtw`

### pipx (isolated environment)

[pipx](https://pipx.pypa.io/) installs ZHTW in its own virtualenv without touching system Python:

```bash
pipx install zhtw
```

Upgrade: `pipx upgrade zhtw`

### From source (developers)

```bash
git clone https://github.com/rajatim/zhtw.git
cd zhtw
pip install -e ".[dev]"
```

<details>
<summary>Can't find the <code>zhtw</code> command after pip install? Configure your PATH</summary>

```bash
# macOS (zsh)
echo 'export PATH="$PATH:$(python3 -m site --user-base)/bin"' >> ~/.zshrc
source ~/.zshrc

# Linux (bash)
echo 'export PATH="$PATH:~/.local/bin"' >> ~/.bashrc
source ~/.bashrc

# Windows — usually automatic; if not, add this to your PATH:
# %APPDATA%\Python\PythonXX\Scripts
```
</details>

---

## 30-second quick start

ZHTW offers three entry points — pick whichever fits your workflow:

### 1. CLI

<!-- zhtw:disable -->
```bash
zhtw check .            # scan the whole project
zhtw check ./file.py    # scan a single file
zhtw fix .              # auto-fix
zhtw lookup 软件 服务器  # look up: 软件→軟體, 服务器→伺服器

# Balanced mode: auto-disambiguate 10 high-frequency ambiguous chars
zhtw fix . --ambiguity-mode balanced
```
<!-- zhtw:enable -->

<!-- zhtw:disable -->
**Sample output:**
```
📁 Scanning ./src

📄 src/components/Header.tsx
   L12:5: "用户" → "使用者"

📄 src/utils/api.ts
   L8:10: "软件" → "軟體"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  Found 2 issues (2 files)
```
<!-- zhtw:enable -->

### 2. Python library

<!-- zhtw:disable -->
```python
from zhtw import convert

convert("这个软件需要优化")
# → "這個軟體需要最佳化"
```
<!-- zhtw:enable -->

The first call loads the dictionary and builds the Aho-Corasick automaton; subsequent calls reuse the cache. For advanced use — custom dictionaries, line-level reports, plugging into your own pipeline — see `convert_text` / `Matcher` / `load_dictionary`. Vocabulary lookup API: `lookup_word` / `lookup_words` (v3.3.0+).

### 3. Java SDK

**Maven:**

<!-- zhtw:disable -->
```xml
<dependency>
    <groupId>com.rajatim</groupId>
    <artifactId>zhtw</artifactId>
    <version>4.4.2</version>
</dependency>
```
<!-- zhtw:enable -->

**Gradle (Kotlin DSL):**

```kotlin
implementation("com.rajatim:zhtw:4.4.2")
```

**Gradle (Groovy DSL):**

```groovy
implementation 'com.rajatim:zhtw:4.4.2'
```

<!-- zhtw:disable -->
```java
import com.rajatim.zhtw.ZhtwConverter;

// Quick start (thread-safe singleton)
String result = ZhtwConverter.getDefault().convert("这个软件需要优化");
// → "這個軟體需要最佳化"

// Custom configuration
ZhtwConverter conv = ZhtwConverter.builder()
    .sources(List.of("cn", "hk"))
    .customDict(Map.of("自定义", "自訂"))
    .ambiguityMode("balanced")  // auto-disambiguate ambiguous chars
    .build();
```
<!-- zhtw:enable -->

**Performance:** 2 μs per sentence, 5.5 ms for 100K characters (17.9 MB/s) — roughly 5.8× faster than Python. See [`sdk/java/BENCHMARK.md`](sdk/java/BENCHMARK.md).

### 4. TypeScript SDK

**npm / pnpm / yarn:**

```bash
npm install zhtw-js
# or
pnpm add zhtw-js
yarn add zhtw-js
```

<!-- zhtw:disable -->
```typescript
import { convert, check, lookup } from 'zhtw-js';

// Quick start (zero config — built-in default converter)
convert('这个软件需要优化');
// → '這個軟體需要最佳化'

check('用户权限');
// → [{ start, end, source, target }, ...]

lookup('软件');
// → { input, output, changed, details: [...] }
```
<!-- zhtw:enable -->

**Custom configuration:**

<!-- zhtw:disable -->
```typescript
import { createConverter } from 'zhtw-js';

const conv = createConverter({
  sources: ['cn'],                  // default: ['cn', 'hk']
  customDict: { '自定义': '自訂' },  // overrides built-in terms
  ambiguityMode: 'balanced',        // auto-disambiguate ambiguous chars
});

conv.convert('...');
```
<!-- zhtw:enable -->

**Highlights:** isomorphic (Node.js ≥20 + native browser support), dual ESM + CJS output, zero runtime dependencies, tree-shakeable. All indices (`start` / `end` / `position`) are **Unicode codepoints**, byte-for-byte identical to the Python CLI and Java SDK (verified via the shared `sdk/data/golden-test.json` fixture). Published via npm Trusted Publishing (OIDC) — no long-lived tokens.

### 5. Rust SDK

**Cargo (crates.io)**:

<!-- zhtw:disable -->
```toml
[dependencies]
zhtw = "4.4.2"
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
    .ambiguity_mode(AmbiguityMode::Balanced)  // auto-disambiguate
    .build()
    .expect("non-empty sources");
```
<!-- zhtw:enable -->

**Performance**: build-time precompiled `daachorse` automaton + `phf` char map, zero runtime construction cost. See benchmarks (`cargo bench -p zhtw`).

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
	// Zero config
	fmt.Println(zhtw.Convert("这个软件需要优化"))
	// → "這個軟體需要最佳化"

	// Builder: custom dict + balanced mode
	conv, _ := zhtw.NewBuilder().
		Sources(zhtw.SourceCn).
		CustomDict(map[string]string{"自定义": "自訂"}).
		SetAmbiguityMode(zhtw.AmbiguityBalanced).
		Build()
	fmt.Println(conv.Convert("自定义几个里程碑"))
}
```
<!-- zhtw:enable -->

**Highlights:** `go:embed` embedded dictionary, zero external dependencies, goroutine-safe. Go 1.21+, install via `go get`. All indices are Unicode codepoints, cross-SDK golden-test verified.

#### Standalone Binary

No Go environment needed — download pre-built binaries:

<!-- zhtw:disable -->
```bash
# Download from GitHub Release (e.g., macOS arm64)
curl -sL https://github.com/rajatim/zhtw/releases/download/sdk%2Fgo%2Fv4.4.2/zhtw-darwin-arm64.tar.gz | tar xz
./zhtw convert "软件测试"
# → 軟體測試

# Or via go install
go install github.com/rajatim/zhtw/sdk/go/v4/cmd/zhtw@latest
```
<!-- zhtw:enable -->

### 7. C# (.NET) SDK

**NuGet:**

<!-- zhtw:disable -->
```bash
dotnet add package Zhtw
```
<!-- zhtw:enable -->

<!-- zhtw:disable -->
```csharp
using Zhtw;

// Quick start (thread-safe singleton)
string result = ZhtwConvert.Convert("这个软件需要优化");
// → "這個軟體需要最佳化"

// Builder: custom dict + balanced mode
var conv = new ConverterBuilder()
    .Sources(Source.Cn, Source.Hk)
    .CustomDict(new Dictionary<string, string> { ["自定义"] = "自訂" })
    .AmbiguityMode(AmbiguityMode.Balanced)
    .Build();
```
<!-- zhtw:enable -->

**Highlights:** multi-target netstandard2.0 + net8.0, embedded resource dictionary, zero external dependencies (net8.0+). All indices are Unicode codepoints, cross-SDK golden-test verified.

---

## Multi-language SDKs

ZHTW is primarily implemented in Python and ships native Java, TypeScript, Rust, Go, and C# (.NET) SDKs (6 languages), plus a WebAssembly package (`zhtw-wasm`). All SDKs share the same dictionary data (`zhtw-data.json`), so conversion results are byte-identical to the Python CLI (cross-SDK byte-for-byte verification via the shared `sdk/data/golden-test.json` fixture is a release gate). All SDKs support balanced mode (ambiguous character disambiguation).

| SDK | Install | Throughput (1MB) | Per-call latency | Use cases | Status |
|-----|---------|-----------------|------------------|-----------|--------|
| **Python** | `pip install zhtw` | 3.1 MB/s | — | CLI, CI/CD, pre-commit, data pipelines | ✅ Stable |
| **Java** | [Maven Central](#3-java-sdk) | 17.9 MB/s | 2 μs | Spring Boot, Android, backend services | ✅ Stable |
| **TypeScript** | `npm install zhtw-js` | ~16 MB/s | — | Node.js ≥18, browser (isomorphic ESM+CJS) | ✅ Stable |
| **Rust** | [crates.io](#5-rust-sdk) | — | — | High-perf, embedded | ✅ Stable |
| **WASM** | `npm install zhtw-wasm` | — | — | Browser, Edge runtime | ✅ Stable |
| **Go** | [`go get`](#6-go-sdk) | — | — | Microservices, CLI tools, cloud-native | ✅ Stable |
| **C# (.NET)** | [NuGet](#7-c-net-sdk) | — | — | ASP.NET, Unity, desktop apps | ✅ Stable |

### Cross-SDK Performance Benchmark

<!-- zhtw:disable -->
247 simplified Chinese characters, 10,000 warm iterations, measured on Apple Silicon:

| SDK | Cold Start (ms) | Avg/op (μs) | Ops/sec | vs Python |
|-----|----------------:|------------:|--------:|----------:|
| **Rust** | 15.4 | 44.5 | 22,470 | 11.3x |
| **Go** | 43.1 | 45.0 | 22,233 | 11.1x |
| **Java** | 135.8 | 53.0 | 18,875 | 9.5x |
| **C#** | 77.5 | 56.2 | 17,786 | 8.9x |
| **TypeScript** | 168.2 | 62.1 | 16,094 | 8.1x |
| **Python** | 121.3 | 501.0 | 1,996 | 1.0x |

> All SDKs produce identical output. Even the slowest (Python at 0.5 ms/call) is imperceptible for CLI usage.
<!-- zhtw:enable -->

---

## Coverage

<!-- zhtw:disable -->
**31,000+ curated terms + 6,360 character mappings**, spanning IT, medical, legal, finance, gaming, e-commerce, academia, daily life, geography, and Hong Kong usage (10+ domains). Conversion is handled by three layers: a **vocabulary layer** (Aho-Corasick longest-match) for compound words, a **balanced defaults layer** (`--ambiguity-mode balanced`) that handles 10 high-frequency ambiguous characters with default mappings + protect_terms exceptions, and a **character layer** (`str.translate`) that fills in any remaining simplified characters. 102 one-to-many ambiguous characters are managed in tiers — when in doubt, we leave them unconverted.
<!-- zhtw:enable -->

For the full dictionary taxonomy, two-layer architecture details, one-to-many edge cases, and semantic conflict handling, see [`docs/DICTIONARY-COVERAGE.md`](docs/DICTIONARY-COVERAGE.md).

---

## CI/CD integration

### GitHub Actions

Drop this into `.github/workflows/` and every PR gets checked automatically:

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

Any issue fails the build, so problems never slip through. For deeper setup — allowlists, artifact reporting, monorepo patterns — see the [CI/CD integration guide](docs/CI-CD-INTEGRATION.md).

---

## Pre-commit hook

Stop issues before they're committed:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/rajatim/zhtw
    rev: v4.4.2  # use the latest tag
    hooks:
      - id: zhtw-check   # check mode (recommended)
      # - id: zhtw-fix   # or auto-fix mode
```

```bash
pip install pre-commit && pre-commit install
# subsequent commits will run the check automatically
```

<details>
<summary>Advanced: only check specific file types</summary>

```yaml
repos:
  - repo: https://github.com/rajatim/zhtw
    rev: v4.4.2
    hooks:
      - id: zhtw-check
        types: [python, markdown, yaml]  # only these types
        exclude: ^tests/fixtures/        # skip test fixtures
```
</details>

---

## Ignoring specific code

Don't want test fixtures or vendored code to be converted? Use pragmas:

```python
# ignore this line
test_data = "软件"  # zhtw:disable-line

# ignore the next line
# zhtw:disable-next
legacy_code = "用户信息"

# ignore an entire block
# zhtw:disable
test_cases = ["软件", "硬件", "网络"]
# zhtw:enable
```

For project-level exclusions, use `.zhtwignore` (same format as `.gitignore`); a full example lives in [`docs/CLI-ADVANCED.md`](docs/CLI-ADVANCED.md#zhtwignore-忽略檔案).

---

## Documentation

| Doc | Contents |
|-----|----------|
| [`docs/DICTIONARY-COVERAGE.md`](docs/DICTIONARY-COVERAGE.md) | Full dictionary taxonomy, two-layer architecture, one-to-many edge cases, semantic conflicts |
| [`docs/CLI-ADVANCED.md`](docs/CLI-ADVANCED.md) | Complete CLI options, `lookup` command, multi-encoding support, custom dictionary format |
| [`docs/CI-CD-INTEGRATION.md`](docs/CI-CD-INTEGRATION.md) | In-depth GitHub Actions / GitLab CI / pre-commit setup |
| [`sdk/java/BENCHMARK.md`](sdk/java/BENCHMARK.md) | Java SDK performance (JMH) |
| [`CHANGELOG.md`](CHANGELOG.md) | Release history |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution guide |

> **Note:** the linked docs are in Traditional Chinese. English versions are on the roadmap — contributions welcome.

---

## Development

```bash
pip install -e ".[dev]"
pytest
ruff check .
```

## Help Build the Public Benchmark

Use the
[dedicated form](https://github.com/rajatim/zhtw/issues/new?template=permissioned-user-report.yml)
to contribute 1–10 real Simplified Chinese sentences that you wrote or have the
right to provide. Do not include Traditional Chinese answers, converter output,
or sensitive data. See
[issue #47](https://github.com/rajatim/zhtw/issues/47) for consent terms and
collection progress.

Questions? [Open an issue](https://github.com/rajatim/zhtw/issues). Want to contribute? [See the contributing guide](CONTRIBUTING.md).

---

MIT License | **Made by tim Insight**
