# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Rust SDK**: new `zhtw` crate published to crates.io
  - Feature parity with Java / TypeScript SDK (`convert`, `check`, `lookup`, `sources`, `custom_dict`)
  - Compile-time `phf::Map` character layer (zero runtime hash construction)
  - Pre-compiled `daachorse::CharwiseDoubleArrayAhoCorasick` embedded via `build.rs`
  - Byte-for-byte parity verified via shared `sdk/data/golden-test.json`
- **WASM SDK**: new `zhtw-wasm` npm package (Rust core compiled to WebAssembly)
  - Drop-in API compatible with `zhtw-js`
  - Published via npm Trusted Publishing (OIDC)

### Changed
- `make bump` updates 8 locations (added `sdk/rust/zhtw-wasm/package.json`)
- `sdk/rust/` converted from single-crate scaffold to workspace
- `.github/workflows/sdk-rust.yml` replaced fake-green stub with full pipeline
- CLAUDE.md golden rule 6 updated: 7 → 8 mono-versioning locations

## [4.0.1] - 2026-04-09

### Added
- **TypeScript SDK**（`zhtw-js`）**首次 npm 釋出**：完整 isomorphic SDK，與 Python / Java pipeline byte-for-byte 一致
  - 支援 Node ≥18 與現代瀏覽器，ESM + CJS 雙格式（tsup 外帶）
  - 公開 API：`convert` / `check` / `lookup`（位置全部以 Unicode codepoint index 回傳，非 UTF-16 code-unit）
  - 手刻 Aho-Corasick 自動機 + 詞彙層/字元層雙層架構
  - 72 個測試（含 21 個 cross-SDK golden fixture 比對）
  - CI matrix（Node 18/20/22）+ `pack + install` smoke test
  - npm publish 由 GitHub Release trigger（provenance 開啟）
  - Benchmark：1MB 輸入 ~16 MB/s 吞吐量
  - 檔案：[`sdk/typescript/README.md`](sdk/typescript/README.md)

### Fixed
- **ts-sdk: matcher identity-protection**（Codex review #1）：補上 Python `src/zhtw/matcher.py:89-133` 的 identity-protection 規則。`AhoCorasickMatcher.findMatches` 現在會拆分 identity 與 non-identity matches、用 bisect_right + prefix-max-end 建立 protected ranges、過濾重疊的 non-identity 轉換、且只 yield non-identity。
  - 修復前 `createConverter({ sources: ['hk'], customDict: { '檔案': '檔案', '檔案': '檔案' } }).convert('無中文檔案')` 會誤轉成 `無中檔案案`；修復後保留 `無中文檔案`，與 Python/Java 行為一致。
- **ts-sdk: lookup() charmap 後處理**（Codex review #2）：對齊 Python `src/zhtw/lookup.py:78-83`，term 層比對到詞之後把 target 再丟進 charmap translate 一次。
  - 修復前 `lookup('伙頭').output` 回 `伙頭`（term target 未過字元層），但 `convert('伙頭')` 回 `夥頭`；修復後兩者一致。
- **ts-sdk: sdk/typescript/LICENSE**（Codex review #3）：補上 `package.json` 的 `files` 欄位早就引用但實際缺漏的 LICENSE 檔案，避免未來 `npm publish` tarball 缺授權檔案。

### Mono-versioning（所有 SDK 同步升至 4.0.1）
Python / Java / Rust / .NET 程式碼與 4.0.0 **完全相同**，僅為滿足 mono-versioning 規則而重新釋出：
- Python: `zhtw` 4.0.0 → **4.0.1**（程式碼未變；PyPI 重新釋出）
- Java: `com.rajatim:zhtw` 4.0.0 → **4.0.1**（程式碼未變；Maven Central 重新釋出）
- TypeScript: `zhtw-js` 4.0.0（未曾釋出）→ **4.0.1**（npm **首次**釋出，含上述 fix）
- Rust: `zhtw` 4.0.0 → **4.0.1**（Planned，未實際釋出）
- .NET: `Zhtw` 4.0.0 → **4.0.1**（Planned，未實際釋出）
- `sdk/data/zhtw-data.json` + `golden-test.json` 已透過 `zhtw export` 重新產生，嵌入版本號為 `4.0.1`

## [4.0.0] - 2026-04-09

### ⚠️ Breaking Changes
- **Python 3.9 support removed**（EOL: 2025-10-05）。最低版本 bump 至 **Python 3.10**。
  - 理由：Python 3.9 已於 2025-10-05 結束上游安全維護。為滿足金融業審查對「default branch 0 open alerts」的要求，我們放棄 py3.9 resolution branch，讓 `uv.lock` 可以全面升級到最新安全修補版本。
  - 影響：
    - 使用 Python 3.9 的使用者請繼續使用 v3.4.x 系列（功能凍結，僅提供關鍵安全修補）。
    - Python 3.10+ 使用者無行為變動，純粹是元資料與 CI 矩陣調整。
  - 升級：`pip install --upgrade zhtw`（需 Python ≥ 3.10）。

### Security
- 全面升級 `uv.lock` 依賴至最新安全修補版本，清除 Dependabot 所有 open alerts（py<3.10 resolution branch 已不再存在）。

### Changed
- `requires-python = ">=3.10"`（原 `">=3.9"`）
- CI 測試矩陣 `['3.10', '3.11', '3.12', '3.13']`（原 `['3.9', '3.11', '3.12']`）
- Ruff `target-version = "py310"`（原 `"py39"`）

### Mono-versioning（所有 SDK 同步升至 4.0.0）
依循 v3.4.0 引入的 mono-versioning 策略，所有 SDK 版本號與 Python 主版本對齊。Java / TypeScript / Rust / .NET SDK 雖然 **沒有 breaking API 變更**，仍同步升版以維持跨語言一致性，並避免 Maven Central 釋出衝突（tag → release → `sdk-java.yml` 自動觸發 `mvn deploy`，pom 版本必須跟 tag 對齊）：
- Java: `com.rajatim:zhtw` 3.4.0 → **4.0.0**（Stable，自動釋出到 Maven Central）
- TypeScript: `zhtw-js` 3.4.0 → **4.0.0**（Planned）
- Rust: `zhtw` 3.4.0 → **4.0.0**（Planned）
- .NET: `Zhtw` 3.3.0 → **4.0.0**（Planned，補齊 v3.4.0 漏升）
- `sdk/data/zhtw-data.json` + `golden-test.json` 已透過 `zhtw export` 重新產生，嵌入版本號為 `4.0.0`

## [3.4.0] - 2026-04-09

### Added
- **Java SDK**（`com.rajatim:zhtw`）：完整 Java SDK，與 Python pipeline 行為一致
  - `ZhtwConverter`：convert / check / lookup 三大公開 API
  - `AhoCorasickMatcher`：Aho-Corasick 詞彙匹配（最長非重疊、identity mapping 保護）
  - Builder pattern、thread-safe singleton（`getDefault()`）
  - Supplementary plane 完整支援（codepoint-based 位置，非 UTF-16 index）
  - 73 個測試（含 golden test 21 cases 一致性驗證）
  - JMH benchmark：convertShort ~2μs、convertLarge 17.9 MB/s（~5.8× Python）
  - Maven 專案結構 + CI workflow（Java 11/17/21）+ Maven Central 自動釋出
- **README 多語言 SDK 對照表**：Python / Java 資料已填，TS / Rust / C# 規劃中

### Changed
- **版本策略**：改為 mono-versioning，Python + Java SDK 共用同一版本號
- **Maven 釋出管道**：從 OSSRH 遷移至 Sonatype Central Portal（`central-publishing-maven-plugin`）

## [3.3.0] - 2026-04-08

### Added
- **`zhtw lookup` 指令**：查詢任意詞/句的轉換結果與來源歸因（詞彙層 vs 字元層）
  - 三種輸入：命令列引數、stdin 管線、整句模式
  - `--verbose` 樹狀詳細歸因、`--json` 結構化輸出
  - 核心邏輯獨立為 `lookup.py` 模組，可供程式化使用
- **lookup 公開 API**：`lookup_word()`、`lookup_words()`、`LookupResult`、`ConversionDetail`

### Fixed
- **config 全域狀態汙染**：`DEFAULT_CONFIG` 改用 `copy.deepcopy` 防止淺複製突變
- **review skip 資料遺失**：全部 skip 時保留 pending 檔，不再靜默刪除
- **UTF-16 雙 BOM**：Python `utf-16` codec 已自動寫 BOM，不再手動重複寫入
- **custom dict 缺 target 欄位**：extended entry 缺 `target` 時跳過，不再把整個 dict 當替換值
- **list 格式匯入重複偵測**：`_list_to_dict()` 在轉 dict 前偵測重複，正確計入 `duplicates`
- **usage --reset 許可權錯誤**：`PermissionError` 轉為乾淨的 CLI 錯誤訊息
- **lookup/converter 輸出一致性**：term target 套用 charmap，確保與 converter pipeline 一致

## [3.2.1] - 2026-03-22

### Fixed
- **Python 3.9 CI 修復**：測試檔案補上 `from __future__ import annotations`

## [3.2.0] - 2026-03-22

### Added
- **Check mode 字元級偵測**：check 模式現在也會報告字元層轉換（之前只報告詞彙層）
- **30+ 新保護詞條**：划船/划水/划拳 identity、周到/周密/周旋/周折 保護、屋裡/水裡/夢裡/城裡 等
- **Thread safety**：charconv.py 全域快取加入 `threading.Lock`

### Fixed
- **opencc.json 122 條古字修復**：吃→吃、孃→娘、昇→升、鬨→哄（臺灣不用古字形）
- **苹果→Apple 危險對映**：改為 `Apple 手機→Apple 手機` 等特定複合詞
- **筆記本→筆記型電腦 過度轉換**：改為 `筆記型電腦→筆記型電腦`，裸詞 identity 保護
- **頭像→大頭貼**：改為通用正確的 `頭像→頭像`
- **儲存→儲存空間**：改為不過度翻譯的 `儲存→儲存`
- **encoding.py confidence 型別錯誤**：從 `encoding_aliases[0]`（str）改為 `best.coherence`（float）
- **于 歧義字排除**：從 safe_chars.json 移至 ambiguous_excluded（于可為姓氏）

## [3.1.0] - 2026-03-22

### Performance
- **Matcher 效能最佳化**：修復超線性退化，1MB 文字吞吐量 33 → 3,068 KB/s（**93 倍**）
  - Protected ranges：O(n×m) 巢狀迴圈 → O(m log m) 二分搜尋（bisect）
  - replace_all：O(n×m) 字串切片 → O(n) list+join
  - 吞吐量穩定 ~3,100 KB/s，不受文字大小影響
- 測試套件執行時間：249s → 41s（6 倍加速）

## [3.0.0] - 2026-03-22

### Added
- **字元級轉換層**：新增 6,344 個安全一對一簡繁字元對映（`str.translate()`），作為詞彙級轉換後的第二層
- **OpenCC 詞庫整合**：修復 `opencc.json` 格式並新增 28,106 個詞條
- **Aho-Corasick 重疊保護**：13 個新保護詞條，修復周/週過度轉換
- **7 個驗證測試模組**（623 項測試）：字元對映完整性、詞庫品質、過度轉換偵測、歧義字消歧、邊界案例、壓力效能、黃金對照
- **52 書大規模審計**：103M 字、0 殘留簡體、0 古字、0 真實過度轉換
- `charconv.py` 模組：字元級轉換核心
- `generate_charmap.py`：從 Unicode Unihan 自動產生對映指令碼
- `audit_books.py`：多書籍 epub 品質審計指令碼

### Fixed
- `opencc.json` 儲存為 Python dict literal 而非 JSON，導致無法載入
- `灶→竈`、`𬮤→閤` 古字對映移除（臺灣不用）
- 25 處 `週圍`（應為 `周圍`）過度轉換
- 2 處 `週全`（應為 `周全`）過度轉換

## [2.8.7] - 2026-01-18

### Changed
- **品牌更新為 tim Insight**
  - 作者名稱：rajatim → tim Insight
  - Email：rajatim@gmail.com
  - Blog 連結更新至 timinsight.com

## [2.8.6] - 2026-01-13

### Changed
- **PyPI SEO 最佳化**：增加專案曝光度
  - 新增 Blog Post 連結（中文/English）
  - 新增 Documentation、Changelog 連結
  - 擴充 keywords：l10n, localization, nlp, vibe-coding, ai-tools
  - 新增 classifiers：Natural Language, Internationalization, Localization
  - 新增 Python 3.13 支援宣告

## [2.8.5] - 2026-01-05

### Changed
- **validate 命令大幅改善**：808 警告 → 0
  - 預設跳過 identity mapping（設計如此）
  - 區分同來源衝突（bug）與跨來源衝突（設計）
  - 新增 `--strict` 選項顯示完整資訊
- 測試覆蓋率提升：82% → 90%
- 新增 Codecov 整合與徽章

### Fixed
- 移除 28 個跨檔案重複詞彙
- 修正「控制檯」衝突（控制檯→控制檯 vs 控制檯→主控臺）
- 修正「奶油」連鎖轉換問題

## [2.8.4] - 2026-01-04

### Changed
- 完整測試 Jenkins Pipeline（含 GitHub Release）

## [2.8.3] - 2026-01-04

### Changed
- 測試 Jenkins Pipeline 釋出流程

## [2.8.2] - 2026-01-04

### Changed
- 新增 Jenkins 釋出流程

## [2.8.1] - 2026-01-04

### Changed
- 精簡釋出 SOP 檔案

## [2.8.0] - 2026-01-04

### Added
- **單檔案掃描模式**：現在可以直接對單一檔案執行 check 或 fix
  - `zhtw check ./file.py`
  - `zhtw fix ./file.py`
- CLI 訊息區分檔案（📄）和目錄（📁）圖示
- 版本釋出 SOP 檔案（`.claude/guides/releasing.md`）

### Fixed
- 補齊 77 條基礎簡繁字元對應（P0）
- 統一術語 key 格式為簡體（P1）
- 補上 隨身碟→隨身碟 轉換（P2）

## [2.7.0] - 2026-01-03

### Added
- **詞庫重大擴充**：433 → 3,490 詞彙（8 倍成長）
- 10+ 專業領域詞庫：
  - 醫療健康（230+）、法律合規（170+）、金融財務（140+）
  - 遊戲娛樂（150+）、電商零售（110+）、學術教育（110+）
  - 每日生活（230+）、地理國名（160+）、商業基礎（80+）
- 22 個一對多危險字完整覆蓋（發/髮、面/麵、裡/裡 等）

### Fixed
- 語義衝突智慧處理（停用/撤銷/登出 在 UI 語境的正確轉換）

### Changed
- 使用 Trusted Publishing 釋出到 PyPI

## [2.6.0] - 2026-01-03

### Added
- 900+ 高頻簡體單字轉換（詞庫從 ~1100 → 2071 個詞彙）
  - 涵蓋人稱代詞：們→們、他→他
  - 常用動詞：說→說、會→會、進→進、動→動
  - 常用名詞：國→國、時→時、機→機、電→電
  - 形容詞副詞：難→難、專→專、遠→遠

### Fixed
- 修正 identity mapping 阻擋長詞轉換問題
  - 例如「件→件」不再阻擋「軟體→軟體」
  - 保留正確的保護機制（如「檔案」保護免受「檔案」影響）

## [2.5.0] - 2025-12-31

### Added
- 一對多危險字完整覆蓋（22 個字）
  - 發→發/髮、面→面/麵、裡→裡/裡、後→後/後
  - 複→複/復、幹→幹/乾、隻→隻/隻 等
- 完整測試覆蓋（208 個測試案例）

### Changed
- 最佳化 Token 使用：AI 檔案分層架構

## [2.4.0] - 2025-12-26

### Added
- 進度條顯示：掃描檔案時顯示即時進度
  - TTY 模式：動態進度條 `掃描中 [████████░░░░] 50/100`
  - 非 TTY 模式（Jenkins/CI）：靜態輸出 `掃描中... 25% (25/100)`
- `--json` 模式自動停用進度顯示

## [2.3.0] - 2025-12-26

### Added
- `--show-diff` 選項：顯示修改預覽，確認後才執行
- `--backup` 選項：修改前備份原檔到 `.zhtw-backup/`
- 非 git 目錄警告：提醒使用者使用 --backup 或 --dry-run
- 142 個測試

## [2.2.0] - 2025-12-26

### Added
- `.zhtwignore` 檔案支援，可排除不需檢查的目錄和檔案
- 139 個測試（CLI、忽略指令、.zhtwignore）

### Fixed
- 測試檔案中未使用的 imports

## [2.1.0] - 2025-12-25

### Added
- 47 個 IT 術語（來自 OpenCC TWPhrasesIT.txt）
- `zhtw review` 預設啟用 LLM 驗證

### Changed
- 簡化 README，移除 LLM 功能檔案（進階功能）

## [2.0.0] - 2025-12-24

### Added
- LLM 整合功能
  - `zhtw import` - 從外部來源匯入詞彙
  - `zhtw review` - 審核待匯入詞彙（支援 LLM 驗證）
  - `zhtw validate-llm` - 用 LLM 驗證詞庫正確性
  - `zhtw usage` - 顯示 LLM 用量統計
  - `zhtw config` - 管理設定
- 用量追蹤與成本控制

## [1.5.0] - 2025-12-24

### Added
- `zhtw stats` - 顯示詞庫統計資訊
- `zhtw validate` - 驗證詞庫品質（衝突、無效轉換）
- 忽略註解功能
  - `zhtw:disable-line` - 忽略當前行
  - `zhtw:disable-next` - 忽略下一行
  - `zhtw:disable` / `zhtw:enable` - 區塊忽略

### Changed
- 優化詞庫品質，移除無效轉換

## [1.0.0] - 2025-12-23

### Added
- 初始版本
- `zhtw check` - 檢查簡體中文
- `zhtw fix` - 自動修正
- 支援 cn（簡體）和 hk（港式）來源
- 330+ 精選詞彙（IT、商業、基礎）
- Aho-Corasick 高效匹配演算法
- `--json` 輸出（CI/CD 整合）
- `--dry-run` 模擬執行
- `--exclude` 排除目錄
- 自訂詞庫支援

[2.4.0]: https://github.com/rajatim/zhtw/compare/v2.3.0...v2.4.0
[2.3.0]: https://github.com/rajatim/zhtw/compare/v2.2.0...v2.3.0
[2.2.0]: https://github.com/rajatim/zhtw/compare/v2.1.0...v2.2.0
[2.1.0]: https://github.com/rajatim/zhtw/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/rajatim/zhtw/compare/v1.5.0...v2.0.0
[1.5.0]: https://github.com/rajatim/zhtw/compare/v1.0.0...v1.5.0
[1.0.0]: https://github.com/rajatim/zhtw/releases/tag/v1.0.0
