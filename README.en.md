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
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<!-- zhtw:disable -->
**Make your code speak Taiwan** — cures awkward phrases like `許可權` and `軟件` that don't belong in Taiwan Traditional Chinese.
<!-- zhtw:enable -->

<!-- zhtw:disable -->
```
Input:  服务器上的软件需要优化，用户权限请联系管理员
Output: 伺服器上的軟體需要最佳化，使用者權限請聯絡管理員
```
<!-- zhtw:enable -->

One line of code, one CLI, one Maven coordinate — three languages, all producing **real Taiwan Traditional Chinese**.

---

## Why ZHTW?

> **Prefer under-conversion over mis-conversion.**

Generic converters over-translate and silently corrupt words that were already correct in Taiwan usage. ZHTW takes the opposite stance: **only convert what we are sure should change; leave everything else alone.**

| | |
|------|------|
| **Zero false positives** | 31,000+ curated terms + 6,344 character mappings, verified against 52 books / 100M characters with zero mis-conversions |
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
| **Ambiguity** | Rule ordering | 22 hand-curated dangerous-character exceptions |
| **Dictionary** | Built-in char table + phrase list | 31,000+ curated Taiwan-specific terms |
| **Mis-conversions** | Common cases like `权限 → 許可權` | Zero across 52 books / 100M chars |
| **Ecosystem** | C++ core with multi-language bindings | CLI + Python Library + Java SDK + pre-commit |

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
    <version>4.0.1</version>
</dependency>
```
<!-- zhtw:enable -->

**Gradle (Kotlin DSL):**

```kotlin
implementation("com.rajatim:zhtw:4.0.1")
```

**Gradle (Groovy DSL):**

```groovy
implementation 'com.rajatim:zhtw:4.0.1'
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
zhtw = "4.0.1"
```
<!-- zhtw:enable -->

<!-- zhtw:disable -->
```rust
use zhtw::{Converter, Source};

// Zero config
assert_eq!(zhtw::convert("这个软件需要优化"), "這個軟體需要最佳化");

// Builder with custom dict
let conv = Converter::builder()
    .sources([Source::Cn])
    .custom_dict([("自定义", "自訂")])
    .build()
    .expect("non-empty sources");
```
<!-- zhtw:enable -->

**Performance**: build-time precompiled `daachorse` automaton + `phf` char map, zero runtime construction cost. See benchmarks (`cargo bench -p zhtw`).

---

## Multi-language SDKs

ZHTW is primarily implemented in Python and ships native Java and TypeScript SDKs. All SDKs share the same dictionary data (`zhtw-data.json`), so conversion results are byte-identical to the Python CLI (cross-SDK byte-for-byte verification via the shared `sdk/data/golden-test.json` fixture is a release gate).

| SDK | Install | Throughput (1MB) | Per-call latency | Use cases | Status |
|-----|---------|-----------------|------------------|-----------|--------|
| **Python** | `pip install zhtw` | 3.1 MB/s | — | CLI, CI/CD, pre-commit, data pipelines | ✅ Stable |
| **Java** | [Maven Central](#3-java-sdk) | 17.9 MB/s | 2 μs | Spring Boot, Android, backend services | ✅ Stable |
| **TypeScript** | `npm install zhtw-js` | ~16 MB/s | — | Node.js ≥20, browser (isomorphic ESM+CJS) | ✅ Stable |
| **Rust** | [crates.io](#5-rust-sdk) | — | — | High-perf, WebAssembly, embedded | ✅ Stable |
| **C# (.NET)** | NuGet | — | — | ASP.NET, Unity, desktop apps | 🚧 Planned |

---

## Coverage

<!-- zhtw:disable -->
**31,000+ curated terms + 6,344 character mappings**, spanning IT, medical, legal, finance, gaming, e-commerce, academia, daily life, geography, and Hong Kong usage (10+ domains). Conversion is handled by two layers: a **vocabulary layer** (Aho-Corasick longest-match) for compound words, and a **character layer** (`str.translate`) that fills in any remaining simplified characters. 22 one-to-many danger characters (发/面/里/干 etc.) are disambiguated by the vocabulary layer from surrounding context, so they never mis-convert.
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
    rev: v4.0.1  # use the latest tag
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
    rev: v4.0.1
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

Questions? [Open an issue](https://github.com/rajatim/zhtw/issues). Want to contribute? [See the contributing guide](CONTRIBUTING.md).

---

MIT License | **Made by tim Insight**
