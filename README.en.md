# ZHTW

**English** · [繁體中文](README.md)

## The top-ranked Simplified Chinese to Taiwan Traditional Chinese converter in a formal blind benchmark

ZHTW converts Simplified Chinese into natural, conservative Taiwan Traditional Chinese. It is built for AI output, software interfaces, technical documents, and automated CI checks.

**Blind-v2 result: zhtw reached 33.72%, above OpenCC at 30.82% and zhconv at 28.57%. Both leads were statistically significant.**

[![PyPI](https://img.shields.io/pypi/v/zhtw.svg)](https://pypi.org/project/zhtw/)
[![npm](https://img.shields.io/npm/v/zhtw-js.svg?logo=npm)](https://www.npmjs.com/package/zhtw-js)
[![crates.io](https://img.shields.io/crates/v/zhtw.svg?logo=rust)](https://crates.io/crates/zhtw)
[![Maven Central](https://img.shields.io/maven-central/v/com.rajatim/zhtw.svg?label=maven%20central)](https://central.sonatype.com/artifact/com.rajatim/zhtw)
[![NuGet](https://img.shields.io/nuget/v/Zhtw.svg)](https://www.nuget.org/packages/Zhtw)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<!-- zhtw:disable -->
```text
Input:  服务器上的软件需要优化，用户权限请联系管理员
Output: 伺服器上的軟體需要最佳化，使用者權限請聯絡管理員
```
<!-- zhtw:enable -->

Its core rule is simple: **prefer under-conversion over a wrong conversion.**

## Formal benchmark results

### zhtw was more accurate than OpenCC and zhconv

Blind-v2 froze 1,960 test sentences and expected answers before evaluation. All three tools received the same inputs, rules, and locked versions. The primary metric was strict sentence-level accepted accuracy.

| Tool | Accepted | Accuracy | 95% confidence interval |
|---|---:|---:|---:|
| **zhtw 4.4.2** | **661 / 1,960** | **33.72%** | **31.73%–35.87%** |
| OpenCC `s2twp` 1.4.1 | 604 / 1,960 | 30.82% | 28.88%–32.91% |
| zhconv `zh-tw` 1.4.3 | 560 / 1,960 | 28.57% | 26.63%–30.46% |

| Comparison | Lead | Paired 95% confidence interval | McNemar p-value |
|---|---:|---:|---:|
| zhtw vs OpenCC | **+2.91 percentage points** | +1.48 to +4.34 | 0.0000904 |
| zhtw vs zhconv | **+5.15 percentage points** | +3.67 to +6.63 | 1.18 × 10⁻¹¹ |

Both paired confidence intervals are fully above zero, so zhtw's lead was statistically significant.

[Read the full formal market benchmark report](docs/reports/formal-market-benchmark-2026-07-31.md)

### Version 4.4.3 fixed 51 more public benchmark gaps

After the formal benchmark, we manually reviewed 100 disagreements from public localization data. We confirmed 57 real gaps and fixed 51. Six context-free cases stayed conservative instead of forcing a conversion.

| Public benchmark | 4.4.2 | 4.4.3 | Change |
|---|---:|---:|---:|
| AOSP Taiwan UI | 380 / 1,968 | **403 / 1,968** | **+23** |
| Firefox Taiwan UI | 270 / 1,264 | **293 / 1,264** | **+23** |
| VS Code Taiwan UI | 2,089 / 17,133 | **2,092 / 17,133** | **+3** |
| UD GSD | 3,522 / 4,997 | **3,524 / 4,997** | **+2** |
| NAER terminology | 311 / 775 | **311 / 775** | no change |

**Version 4.4.3 added 51 exact sentence matches across the public benchmarks, and none of the five tracks went backward.** On UD GSD, changed-span precision was **94.30%**, recall was **94.21%**, and F1 was **94.25%**.

<details>
<summary>How does the benchmark avoid teaching to the test?</summary>

- Sentence-level accepted accuracy is strict: one different character, term, or punctuation mark fails the full sentence. It is useful for comparing tools on the same data, but it is not character-level accuracy for normal traffic.
- Blind-v2 froze 1,960 cases from a pool of 5,896 before the formal run. SHA-256 hashes locked the inputs, expected answers, competitor versions, and protocol.
- The formal run did not read detailed expected rows. The public report exposes aggregate results and audit hashes only.
- The maintainer made every final expected decision. Codex and Agy gave independent advice but did not become ground truth by themselves.
- Public AOSP, Firefox, VS Code, UD GSD, and NAER tracks use pinned upstream commits so third parties can reproduce them.
- Official vendor translations are not always the only valid Taiwan wording, so public paired data is secondary evidence and does not replace the formal blind result.

See the [accuracy standard](docs/testing/accuracy/precision-standard.md) and [formal report](docs/reports/formal-market-benchmark-2026-07-31.md) for the full governance process.
</details>

## Why ZHTW is more reliable than character replacement

Simplified-to-Taiwan conversion is more than one-to-one character replacement. A character may need to stay unchanged in one context and become a different Taiwan term in another.

<!-- zhtw:disable -->
| Simplified input | Character-level conversion risk | ZHTW |
|---|---|---|
| 用户权限 | 使用者許可權 | **使用者權限** |
| 写程序前先看法律程序 | 寫程式前先看法律程式 | **寫程式前先看法律程序** |
| 政府发布官方文件 | 政府釋出官方檔案 | **政府發布官方文件** |
| 保存文化遗产 | 儲存文化遺產 | **保存文化遺產** |
| 这个函数会抛出异常 | 這個函數會拋出異常 | **這個函式會拋出例外** |
| 台积电扩大先进制程投资 | 臺積電擴大先進位程投資 | **台積電擴大先進製程投資** |
<!-- zhtw:enable -->

ZHTW 4.4.4 uses:

- **31,904 exported CN mappings**: 31,505 lexical rules, 374 generated target-stability guards, and 25 additional generated context guards.
- **6,352 safe character mappings** limited to suitable one-to-one conversions.
- **111 ambiguous characters excluded from the safe character layer**, plus 13 balanced defaults and 32 protection phrases for reviewed contexts.
- Aho-Corasick longest matching, with complete terms handled before safe characters.
- A `balanced` mode for more active conversion of common ambiguous characters while keeping context protections.

All processing runs locally. ZHTW does not send your text to an external service.

## Quick start

### Install the CLI

macOS:

```bash
brew tap rajatim/tap
brew install zhtw
```

Python environments:

```bash
python3 -m pip install zhtw
```

Both install methods give you the **same `zhtw` command** with identical features.

### Check, fix, and inspect

<!-- zhtw:disable -->
```bash
zhtw check .                         # inspect a project without changing files
zhtw fix . --show-diff               # show the diff before applying changes
zhtw lookup 软件 服务器 用户权限     # inspect individual conversions
zhtw fix . --ambiguity-mode balanced # enable common ambiguous-char handling
```
<!-- zhtw:enable -->

### Python

<!-- zhtw:disable -->
```python
from zhtw import convert

result = convert("这个软件需要优化")
assert result == "這個軟體需要最佳化"
```
<!-- zhtw:enable -->

See the [advanced CLI guide](docs/guides/CLI-ADVANCED.md) for custom dictionaries, encodings, ignore rules, and output formats.

## One dictionary, seven runtimes

Python, Java, TypeScript, Rust, WebAssembly, Go, and C# share the same versioned dictionary and golden tests. Cross-SDK output must match byte for byte before a release can ship.

| Runtime | Install | Documentation |
|---|---|---|
| Python | `pip install zhtw` | [PyPI](https://pypi.org/project/zhtw/) |
| Java | `com.rajatim:zhtw:4.4.5` | [Java README](sdk/java/README.md) |
| TypeScript | `npm install zhtw-js` | [TypeScript README](sdk/typescript/README.md) |
| Rust | `cargo add zhtw` | [Rust README](sdk/rust/zhtw/README.md) |
| WebAssembly | `npm install zhtw-wasm` | [WASM README](sdk/rust/zhtw-wasm/README.md) |
| Go | `go get github.com/rajatim/zhtw/sdk/go/v4@latest` | [Go README](sdk/go/README.md) |
| C# / .NET | `dotnet add package Zhtw` | [.NET README](sdk/dotnet/README.md) |

If Python is not available, download a single executable for macOS, Linux, or Windows (built in Go) from [GitHub Releases](https://github.com/rajatim/zhtw/releases). It is a lightweight build with only `convert`, `lookup`, and `version`; use the `zhtw` command above when you need `check` or `fix`.

## Put accuracy checks in CI

```yaml
name: Taiwan Traditional Chinese check
on: [push, pull_request]

jobs:
  zhtw:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.x"
      - run: pip install zhtw
      - run: zhtw check . --json
```

You can also check each commit:

```yaml
repos:
  - repo: https://github.com/rajatim/zhtw
    rev: v4.4.5
    hooks:
      - id: zhtw-check
```

To use this check in another project, see the
[consumer CI/CD integration guide](docs/deployment/CI-CD-INTEGRATION.md).

## Control what must stay unchanged

Use `.zhtwignore` to exclude files, or use pragmas to protect fixtures, quotations, and third-party text:

```python
fixture = "软件"  # zhtw:disable-line

# zhtw:disable-next
quoted_text = "用户信息"

# zhtw:disable
third_party_samples = ["软件", "硬件", "网络"]
# zhtw:enable
```

`zhtw fix . --show-diff` displays changes first, which is useful for initial adoption and human-reviewed workflows.

## Where ZHTW fits

Good uses:

- Post-processing Taiwan Traditional Chinese generated by AI, LLMs, or translation models.
- Software UI, i18n resources, technical docs, code comments, and customer deliverables.
- CI and enterprise environments that need local processing and repeatable rules.
- Systems that need matching output across Python, Java, TypeScript, Rust, Go, C#, and WebAssembly.

Not a fit:

- Tasks that need full-document meaning, style rewriting, or a new translation.
- Workflows that force one answer for every ambiguous term without context.
- General multilingual translation outside Simplified and Traditional Chinese.

ZHTW is a rule-based conversion and quality-checking tool, not a generative translation model.

## Documentation and audit data

| Document | Contents |
|---|---|
| [Formal market benchmark](docs/reports/formal-market-benchmark-2026-07-31.md) | Blind-v2 scores, statistical comparisons, limits, and governance hashes |
| [Accuracy standard](docs/testing/accuracy/precision-standard.md) | Ground truth, human review, and benchmark rules |
| [Dictionary coverage](docs/reports/DICTIONARY-COVERAGE.md) | Term groups, ambiguous characters, and conversion design |
| [Advanced CLI guide](docs/guides/CLI-ADVANCED.md) | Custom dictionaries, ignore rules, encodings, and output formats |
| [Consumer CI/CD integration](docs/deployment/CI-CD-INTEGRATION.md) | Use zhtw from GitHub Actions, GitLab CI, or pre-commit in another repo |
| [Changelog](CHANGELOG.md) | Accuracy, feature, and compatibility changes by release |
| [Contributing guide](CONTRIBUTING.md) | Development, testing, and dictionary change process |
| [Security policy](SECURITY.md) | Supported versions and private vulnerability reporting |
| [MIT License](LICENSE) | Terms for use, modification, and distribution |
| [Acknowledgments](docs/reference/ACKNOWLEDGMENTS.md) | Development assistance from OpenAI Codex and Anthropic Claude |

## Help improve accuracy

Use the [corpus submission form](https://github.com/rajatim/zhtw/issues/new?template=permissioned-user-report.yml) to share 1–10 real Simplified Chinese sentences that you wrote, may publish, and that contain no sensitive data. Do not include expected Traditional Chinese answers or converter output, because that would contaminate blind evaluation data.

See the [corpus invitation](docs/testing/benchmark/PERMISSIONED-USER-REPORT-INVITATION.md) for permission terms and shareable text. Use [GitHub Issues](https://github.com/rajatim/zhtw/issues) for normal questions and bug reports.

## Development

```bash
python3 -m pip install -e ".[dev]"
pytest
ruff check .
zhtw validate
```

MIT License · tim Insight
