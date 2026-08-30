# ZHTW

**繁體中文** · [English](README.en.md)

**公開文件：** [五分鐘開始](docs/guides/getting-started.md) · [CLI](docs/guides/cli-and-files.md) · [SDK 與 Browser WASM](docs/guides/sdk-and-browser.md) · [品質證據](docs/testing/quality-and-evidence.md) · [目前版本](docs/releases/current.md)

## 正式盲測第一的簡體中文轉台灣繁體中文工具

ZHTW 專門把簡體中文轉成自然、保守的台灣繁體中文，適合 AI 生成內容、軟體介面、技術文件與 CI 自動檢查。

**Blind-v2 正式盲測：zhtw 33.72%，勝過 OpenCC 30.82% 與 zhconv 28.57%；兩項領先都達統計顯著。**

Simplified Chinese to Taiwan Traditional Chinese converter with benchmarked accuracy.

[![PyPI](https://img.shields.io/pypi/v/zhtw.svg)](https://pypi.org/project/zhtw/)
[![npm](https://img.shields.io/npm/v/zhtw-js.svg?logo=npm)](https://www.npmjs.com/package/zhtw-js)
[![crates.io](https://img.shields.io/crates/v/zhtw.svg?logo=rust)](https://crates.io/crates/zhtw)
[![Maven Central](https://img.shields.io/maven-central/v/com.rajatim/zhtw.svg?label=maven%20central)](https://central.sonatype.com/artifact/com.rajatim/zhtw)
[![NuGet](https://img.shields.io/nuget/v/Zhtw.svg)](https://www.nuget.org/packages/Zhtw)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<!-- zhtw:disable -->
```text
輸入：服务器上的软件需要优化，用户权限请联系管理员
輸出：伺服器上的軟體需要最佳化，使用者權限請聯絡管理員
```
<!-- zhtw:enable -->

核心原則只有一句：**寧可少轉，不要錯轉。**

## 正式盲測結果

### zhtw 精準度勝過 OpenCC 與 zhconv

Blind-v2 在評測前凍結 1,960 筆測試句與答案，三個工具使用相同輸入、相同判定規則與鎖定版本。主要指標是嚴格的整句 accepted accuracy。

| 工具 | 通過 | 精準度 | 95% 信賴區間 |
|---|---:|---:|---:|
| **zhtw 4.4.2** | **661 / 1,960** | **33.72%** | **31.73%–35.87%** |
| OpenCC `s2twp` 1.4.1 | 604 / 1,960 | 30.82% | 28.88%–32.91% |
| zhconv `zh-tw` 1.4.3 | 560 / 1,960 | 28.57% | 26.63%–30.46% |

| 比較 | 領先幅度 | 配對 95% 信賴區間 | McNemar p-value |
|---|---:|---:|---:|
| zhtw 對 OpenCC | **+2.91 個百分點** | +1.48 至 +4.34 | 0.0000904 |
| zhtw 對 zhconv | **+5.15 個百分點** | +3.67 至 +6.63 | 1.18 × 10⁻¹¹ |

兩個配對信賴區間都完全高於零，表示 zhtw 的領先具有統計顯著性。

[閱讀完整正式市場評測報告](docs/reports/formal-market-benchmark-2026-07-31.md)

### 4.4.3 又修正了 51 個公開評測缺口

正式盲測後，我們另外人工檢查 100 筆公開在地化差異，確認 57 個真正缺口，修正其中 51 個；其餘 6 個因缺少語境而維持保守，不強制轉換。

| 公開評測 | 4.4.2 | 4.4.3 | 變化 |
|---|---:|---:|---:|
| AOSP 台灣介面 | 380 / 1,968 | **403 / 1,968** | **+23** |
| Firefox 台灣介面 | 270 / 1,264 | **293 / 1,264** | **+23** |
| VS Code 台灣介面 | 2,089 / 17,133 | **2,092 / 17,133** | **+3** |
| UD GSD | 3,522 / 4,997 | **3,524 / 4,997** | **+2** |
| 國教院術語 | 311 / 775 | **311 / 775** | 持平 |

**4.4.3 在公開評測共增加 51 筆整句完全符合，五個評測都沒有退步。** UD GSD 的 changed-span precision 為 **94.30%**、recall 為 **94.21%**、F1 為 **94.25%**。

<details>
<summary>評測如何避免自己出題、自己得高分？</summary>

- 整句 accepted accuracy 是嚴格指標：一個字、詞彙或標點不同，整句就不通過。它適合在相同資料上比較工具，不等於一般使用情境的逐字正確率。
- Blind-v2 從 5,896 筆候選語料中凍結 1,960 筆，正式執行前固定輸入、答案、競品版本與評測規則的 SHA-256。
- 正式執行時不讀取逐筆答案，公開報告只顯示彙總結果與可稽核雜湊。
- expected 由 maintainer 最終確認；Codex 與 Agy 只提供相互獨立的建議，不直接成為 ground truth。
- AOSP、Firefox、VS Code、UD GSD 與國教院術語另作公開診斷，固定上游 commit，讓第三方可以重現。
- 公開產品的官方台灣翻譯不一定是唯一正解，所以這些資料只作次要證據，不覆蓋正式盲測結論。

完整治理方式見[精準度標準](docs/testing/accuracy/precision-standard.md)與[正式評測報告](docs/reports/formal-market-benchmark-2026-07-31.md)。
</details>

## 為什麼 ZHTW 比只換字更可靠

簡體轉台灣繁體不只是單一字元替換。同一個字在不同語境可能需要保留，也可能要換成完全不同的台灣用語。

<!-- zhtw:disable -->
| 簡體輸入 | 只做字級轉換的風險 | ZHTW |
|---|---|---|
| 用户权限 | 使用者許可權 | **使用者權限** |
| 写程序前先看法律程序 | 寫程式前先看法律程式 | **寫程式前先看法律程序** |
| 政府发布官方文件 | 政府釋出官方檔案 | **政府發布官方文件** |
| 保存文化遗产 | 儲存文化遺產 | **保存文化遺產** |
| 这个函数会抛出异常 | 這個函數會拋出異常 | **這個函式會拋出例外** |
| 台积电扩大先进制程投资 | 臺積電擴大先進位程投資 | **台積電擴大先進製程投資** |
<!-- zhtw:enable -->

ZHTW 4.5.0 使用：

- **31,904 個匯出的中國來源對映**：31,505 條正式詞彙規則、374 條自動產生的目標穩定保護，以及 25 條額外產生的語境保護。
- **6,352 個安全字元對映**，只放適合一對一轉換的字。
- **111 個從安全字元層排除的歧義字**，另有 13 個 balanced 預設轉換和 32 條經確認的語境保護詞。
- Aho-Corasick 最長匹配，先處理完整詞彙，再處理安全字元。
- `balanced` 模式，為常見歧義字提供更積極但仍有保護的轉換。

所有處理都在本機完成，不會把文字送到外部服務。

## 立即開始

### 安裝 CLI

macOS：

```bash
brew tap rajatim/tap
brew install zhtw
```

Python 環境：

```bash
python3 -m pip install zhtw
```

兩種安裝方式得到的是**同一個 `zhtw` 指令**，功能完全相同。

### 檢查、修正與查詢

<!-- zhtw:disable -->
```bash
zhtw check .                         # 檢查專案，不修改檔案
zhtw fix . --show-diff               # 先顯示差異，再決定是否修正
zhtw lookup 软件 服务器 用户权限     # 查看每個詞的轉換結果
zhtw fix . --ambiguity-mode balanced # 啟用常見歧義字消歧
zhtw fix ./locales --adapter json     # 只轉換 JSON string value
```
<!-- zhtw:enable -->

### Python

<!-- zhtw:disable -->
```python
from zhtw import convert, convert_json

result = convert("这个软件需要优化")
assert result == "這個軟體需要最佳化"

json_result = convert_json('{"软件":"这个软件"}', sources=["cn"])
assert json_result == '{"软件":"這個軟體"}'
```
<!-- zhtw:enable -->

進階 CLI、自訂詞庫、編碼與輸出格式請見 [CLI 進階指南](docs/guides/CLI-ADVANCED.md)。

## 同一份詞庫，七種執行環境

Python、Java、TypeScript、Rust、WebAssembly、Go 與 C# 共用同一份版本化詞庫及 golden tests。跨 SDK 輸出必須 byte-for-byte 相同，否則不能發版。

| 環境 | 安裝 | 文件 |
|---|---|---|
| Python | `pip install zhtw` | [PyPI](https://pypi.org/project/zhtw/) |
| Java | `com.rajatim:zhtw:4.5.0` | [Java README](sdk/java/README.md) |
| TypeScript | `npm install zhtw-js` | [TypeScript README](sdk/typescript/README.md) |
| Rust | `cargo add zhtw` | [Rust README](sdk/rust/zhtw/README.md) |
| WebAssembly | `npm install zhtw-wasm` | [WASM README](sdk/rust/zhtw-wasm/README.md) |
| Go | `go get github.com/rajatim/zhtw/sdk/go/v4@latest` | [Go README](sdk/go/README.md) |
| C# / .NET | `dotnet add package Zhtw` | [.NET README](sdk/dotnet/README.md) |

沒有 Python 的環境，可以到 [GitHub Releases](https://github.com/rajatim/zhtw/releases) 下載單一執行檔（macOS、Linux 與 Windows，Go 編譯）。這是輕量版本，只有 `convert`、`lookup`、`version`；需要 `check` 或 `fix` 請用上面的 `zhtw`。

## 放進 CI，阻止簡體汙染進入主分支

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

也可以在 commit 前檢查：

```yaml
repos:
  - repo: https://github.com/rajatim/zhtw
    rev: v4.5.0
    hooks:
      - id: zhtw-check
```

要在其他專案使用這項檢查，完整設定見
[consumer CI/CD 整合指南](docs/deployment/CI-CD-INTEGRATION.md)。

## 控制哪些內容不能改

用 `.zhtwignore` 排除整個檔案，或用 pragma 保護測試資料、引用文字與第三方內容：

```python
fixture = "软件"  # zhtw:disable-line

# zhtw:disable-next
quoted_text = "用户信息"

# zhtw:disable
third_party_samples = ["软件", "硬件", "网络"]
# zhtw:enable
```

`zhtw fix . --show-diff` 會先顯示差異，適合第一次匯入或需要人工確認的專案。

## 適合與不適合的情境

適合：

- AI、LLM 或翻譯模型產生的台灣繁體中文後處理。
- 軟體 UI、i18n、技術文件、程式碼註解與客戶交付文件。
- 需要離線處理、固定規則、可重現結果的 CI 或企業環境。
- 需要 Python、Java、TypeScript、Rust、Go、C# 或 WebAssembly 一致輸出的系統。

不適合：

- 需要理解整篇文章語意、改寫文風或重新翻譯內容的任務。
- 要求每個歧義詞在沒有上下文時都強制選定單一答案的流程。
- 簡繁以外的通用多語翻譯。

ZHTW 是規則式轉換與品質檢查工具，不是生成式翻譯模型。

## 文件與可稽核資料

| 文件 | 內容 |
|---|---|
| [公開產品文件](docs/index.md) | 安裝、CLI、SDK、Browser WASM、轉換行為、品質、版本與 roadmap |
| [Explain API](docs/reference/explain-api.md) | 穩定規則事件、span、reason code 與敏感文字邊界 |
| [JSON adapter](docs/reference/json-adapter.md) | 只轉換 string value 的結構與寫檔安全契約 |
| [正式市場評測](docs/reports/formal-market-benchmark-2026-07-31.md) | Blind-v2 分數、統計比較、限制與治理雜湊 |
| [精準度標準](docs/testing/accuracy/precision-standard.md) | ground truth、人工審核與 benchmark 規則 |
| [詞庫涵蓋報告](docs/reports/DICTIONARY-COVERAGE.md) | 詞庫分類、歧義字與轉換架構 |
| [CLI 進階指南](docs/guides/CLI-ADVANCED.md) | 自訂詞庫、忽略規則、編碼與輸出格式 |
| [其他專案的 CI/CD 整合指南](docs/deployment/CI-CD-INTEGRATION.md) | 在 consumer repo 使用 GitHub Actions、GitLab CI 與 pre-commit |
| [版本紀錄](CHANGELOG.md) | 每版精準度、功能與相容性變更 |
| [貢獻指南](CONTRIBUTING.md) | 開發、測試與詞庫修改流程 |
| [安全政策](SECURITY.md) | 支援版本與私密漏洞通報方式 |
| [MIT License](LICENSE) | 使用、修改與再發布條款 |
| [致謝](docs/reference/ACKNOWLEDGMENTS.md) | OpenAI Codex 與 Anthropic Claude 的開發協助 |

## 參與改進精準度

你可以透過[語料投稿表單](https://github.com/rajatim/zhtw/issues/new?template=permissioned-user-report.yml)提供 1 至 10 個自己原創、可公開且不含敏感資料的真實簡體中文句子。請不要附上繁體答案或任何轉換器輸出，避免汙染盲測資料。

授權方式與可直接分享的邀請文見[語料徵集說明](docs/testing/benchmark/PERMISSIONED-USER-REPORT-INVITATION.md)。一般問題與錯誤回報請使用 [GitHub Issues](https://github.com/rajatim/zhtw/issues)。

## 開發

```bash
python3 -m pip install -e ".[dev]"
pytest
ruff check .
zhtw validate
```

MIT License · tim Insight
