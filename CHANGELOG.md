<!-- zhtw:disable -->
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- 新增明確啟用的 JSON value adapter：只轉換 string value，逐位元保留 key、空白、
  數字表示與未變更的字串 token；duplicate key 與無效 JSON 會安全失敗，CLI 寫回則使用
  同目錄暫存檔與原子替換。
- 新增唯讀 `explain` Python API 與 CLI 指令，共用正式 matcher scan，回傳穩定規則 ID、
  term／identity／balanced／char layer、input／output codepoint span 與 reason code；預設
  不包含前後文，CLI 必須明確加 `--context` 才會顯示。
- 漢字偵測擴充到 Unicode 17.0 的基本區、Extensions A～J 與兩個相容漢字區；外部詞彙
  匯入可接受非 Han 序列完全一致的安全中英數混合技術詞，並以 schema v2 規則保存
  provenance 與 pending review 狀態。

### Changed
- 外部詞彙匯入一律先進待審核區，不再允許用 `--no-pending` 直接寫入正式詞庫；重複
  來源也會整組拒絕，不再保留最後一筆。
- zhtw Jenkins build、verify、release 改為只在準備發版時手動執行；移除每日與每週
  排程，build 固定從 `main` 建立候選，不再接受任意 branch。
- 候選新增 Rust、Go、.NET、Maven 相依套件安全閘門、完整 toolchain 證據，以及從
  封存 Python、npm、WASM、Rust、NuGet、Maven、Go 成品執行的 consumer smoke test。
- verification receipt 與 release receipt 新增 Jenkins pipeline SHA、驗證證據
  checksum、核准參照、freshness、永久保留與最終公開驗證紀錄。

### Fixed
- 發布中斷後會保留原 build、verify 與 release，並從第一個未完成 registry 接續；
  已完成且內容相同的 registry 不會重複上傳。
- GitHub Release 現在會嚴格驗證 tag、標題、notes、Latest、draft/prerelease 狀態與
  候選 tree，Maven 公開驗證也會確認每個主要 artifact 的簽章存在。
- Dependabot read token 在 checkout 專案程式碼前完成 API 讀取並立即解除綁定，且
  必須和 GitHub Release write token 使用不同的 1Password item 與不同 token。

## [4.4.5] - 2026-08-10

### Fixed
- 修正 Python sdist 會把大型測試、benchmark 與其他 SDK 一起封裝，導致 PyPI 拒收；
  現在只包含可重建 wheel 的 Python 原始碼與必要 metadata，Jenkins 也會檢查大小、
  禁止目錄及從 sdist 重建 wheel，避免同類問題再次進入正式發布。

## [4.4.4] - 2026-08-10

### Added
- 新增可重現的 target identity guard 產生器與 374 條自動保護規則，讓包含 bulk
  詞庫在內的所有有效 target 都通過第二輪轉換穩定性檢查。
- 新增 Unicode 17.0.0 Unihan 固定版本、SHA-256 驗證與來源 metadata，避免
  上游 `latest` 更新後無聲改變字元表。
- 新增 Blind-v3 私有優先執行計畫、忽略規則與洩漏防護測試，禁止重用 Blind-v1、
  Blind-v2 或公開評測語料建立新的 fresh claim。
- 新增 Blind-v2 句級 idempotency 彙總稽核；基線先以 v4.4.3 結果凍結，升版只允許
  在稽核結果完全相同時同步版本欄位。公開資料只保存總數、input hash 與失敗 ID
  集合 hash，不揭露逐筆輸出。

### Changed
- Python、Java、TypeScript、Rust、Go 與 .NET 的 matcher coverage 改為只涵蓋
  實際選中的詞與有效 identity 保護；未選中的重疊候選不再阻擋後續字元轉換。
- 詞庫載入與 SDK export 不再把 `_comment_*` metadata 當成規則；README 改為
  分開揭露正式詞彙、生成保護與歧義字資料，不再用註解墊高規則數。
- release gate 現在會驗證 target guard freshness，並檢查包含 bulk 在內的完整
  target idempotency，不再只驗證 curated 詞庫。
- Jenkins 是唯一 CI/CD；`zhtw/verify` 現在必須對指定的 main `zhtw/build` 跑完
  `all`，並產生綁定 SHA、tree、版本、manifest 與 checksum 的 receipt。
  `zhtw/release` 的 `PREVIEW`、正式發布與所有 retry 都只接受完全相符的 receipt。
- Jenkins 候選新增 Dependabot medium 以上警示與 npm token 到期閘門；release 新增
  pinned `pip-audit`、`pnpm audit` 與不發布的完整 credential preflight；正式發布
  仍會在確認前重新驗證所需權限。
- Jenkins release 新增 `RESUME_ALL`；中斷後會用同一組 build/verify 核對並跳過已成功
  且內容完全相同的 registry，從第一個未完成項目接續，最後再跑完整公開驗證。
- 公開 benchmark gate 分開檢查「目前候選不得低於歷史基線」與「歷史報告可重現」；
  zhtw 分數可以提升，但資料集、鎖定競品輸出或 zhtw 指標退步都會失敗。
- Blind-v2 句級 idempotency 由 1,915/1,960（97.70%）提升至
  1,925/1,960（98.21%），只更新 aggregate 與失敗 ID 集合雜湊。
- 公開 UD GSD exact 由 3,524/4,997（70.52%）提升至 3,544/4,997（70.92%），
  idempotency 由 4,894/4,997（97.94%）提升至 4,954/4,997（99.14%）。
- 品質稽核腳本改走正式 public converter；LLM 詞彙審查只接受結構正確且含 boolean
  `correct` 的 JSON，無法解析或語意不清時一律 fail closed。
- TypeScript release gate 新增 CommonJS 與 ESM 成品 smoke tests，並移除已由成品測試
  覆蓋的 `import.meta` 已知建置警告。
- 將大型 Blind-v1 與 Blind-v2 歷史測試依 collection、governance、post-review 與 batch
  範圍拆分，維持原有 222 項稽核斷言。
- 將精準度與 benchmark 投稿文件移入 `docs/testing/` 標準分類，並更新所有連結。

### Fixed
- 修正 npm credential preflight 把個人帳號誤當 organization 而回傳 403；現在會核對
  目前 token 的有效期、package write、2FA bypass 與兩個套件的 maintainer 權限，
  npm cache 與錯誤 log 也只會寫入 Jenkins disposable workspace。
- 修正 crates.io 已禁止 API token 呼叫 `/api/v1/me` 而造成的 403；現在改用唯讀查詢
  驗證 token 屬於 `rajatim`，並確認它的 crate scope 涵蓋 `zhtw`，不執行任何發布或
  owner 變更。
- 修正 NuGet verify-scope key 的 POST 未送出明確零長度 body 而回傳 411；現在設定
  `Content-Length: 0` 後再驗證一次性 key，不上傳套件。
- 修正 Jenkins workspace 內的 GnuPG 路徑過長，導致 gpg-agent Unix socket 無法建立；
  Maven 預檢與發布現在使用 workspace 內的短暫存路徑，結束時停止 agent 並清除私鑰。
- 修正依賴警示證據在 Python 3.10 無法匯入 `datetime.UTC`；現在使用相容的 UTC
  timezone 寫法，並由完整 Python 3.10 測試覆蓋。
- 修正 `应用于` 會輸出 `應用于`、`两千万` 會輸出 `兩千万` 的重疊詞尾端漏轉，
  並加入跨 SDK golden regressions。
- 修正 release subprocess test 使用裸 `python3` 時可能匯入系統舊版 zhtw；現在使用
  目前測試 interpreter，腳本也會把專案 `src/` 放在 import path 最前面。
- 主 GitHub Release 明確設為 Latest；後發布的 Go CLI 子 release 使用
  `--latest=false`，不再覆蓋主要版本的 Latest 標記。
- 補齊 `zhtw-wasm` npm 套件的 MIT LICENSE 與 NuGet 套件 README；Jenkins 會直接
  檢查封裝內容，避免帶著 registry metadata 警告發布。
- 補齊 CHANGELOG 的版本 compare links；Jenkins 提升 `[Unreleased]` 時會同步更新
  `[Unreleased]` 與新版本連結，GitHub Release notes 仍原樣取自該版本內容。
- 詞庫 validator 分開顯示 bulk-to-curated 的 116 個刻意 pin／覆蓋與真正重複；移除
  3 個跨手工檔的同值重複詞條，並新增防止重複回歸的測試。
- 修正發布後公開驗證實際只能到 11/12、crates.io probe 缺少 User-Agent、PyPI
  部分成功後無法只補缺檔，以及 Maven 狀態查詢斷線後可能遺失 deployment ID。
  Registry 已存在版本現在會比對封存內容；NuGet 只忽略官方 repository signature
  產生的 wrapper 檔案。

### Security
- `cryptography` 更新至 50.0.0、`pypdf` 更新至 6.15.0、`postcss` 更新至 8.5.23，
  `click` 更新至 8.4.2，修補本次 release gate 與獨立套件稽核發現的警示。

## [4.4.3] - 2026-07-31

### Added
- 建立 1,960 筆 Blind-v2 正式盲測與完整治理流程，從 5,896 筆候選語料凍結抽樣；
  expected 維持私密，公開報告只包含彙總結果與可稽核雜湊。
- 新增 UD GSD、國教院術語，以及 AOSP、VS Code、Firefox 官方在地化配對等公開
  次要評測；同時提供固定 commit、容器化競品環境與第三方重現 attestation 流程。

### Changed
- 依 100 筆公開配對差異人工稽核，保守修正 57 個確認缺口中的 51 個；無語境的
  「保存／文件／默认／不支持／壁纸」等 6 筆維持不強制轉換，避免矯枉過正。
- 補強「裝置／檔案／資料夾／使用者名稱／飛航模式／桌布」等 UI 語境，以及下載、
  藍牙、登入資訊與密碼管理的完整片語保護。
- 公開次要診斷相較 4.4.2：AOSP exact 380→403、VS Code 2089→2092、
  Firefox 270→293、UD GSD 3522→3524；正式 Blind-v2 仍保留為 4.4.2 的歷史
  one-shot 結果，不將調校後資料回寫為新證據。

### Fixed
- 修正字元層將「旋轉」錯轉成「鏇轉」；把「旋／吁／蔑」移出安全一對一映射，
  改由語境規則與保護詞處理。
- 移除過廣的「日常→每日」與「私密→私人」，並將「禁用扩展」修正為台灣常用的
  「停用擴充套件」。
- 修復 frozen Blind-v2 驗證會重掃已變動參考資料的問題，同時還原正式 protocol
  固定的治理腳本雜湊。
- 補齊公開 paired benchmark 與 CHANGELOG-only release commit 的 CI 觸發條件，
  避免報告未同步或正式發布等待不到遠端 conformance。

### Security
- 更新 `pypdf`、`httplib2`、`pyasn1` 與 `postcss` 至已修補版本，清除發版閘門
  所列的 36 個 medium/high Dependabot 警示。

## [4.4.2] - 2026-07-19

### Added
- 新增可稽核的 accuracy pipeline：500 筆人工 annotation、1,008 筆 sealed holdout、
  1,251 筆公開 regression，以及 Codex → Gemini → maintainer 的 advisory 流程。
- 新增 release `export-check`，確保所有 SDK data 與當前詞庫的 fresh export 完全一致。
- 新增版本化 SDK JSON Schema、嚴格資料載入驗證，以及 55 筆不由 exporter 產生的
  maintainer-approved 跨語言 conformance corpus。
- 新增全 SDK `make test-all` 與 GitHub conformance gate；GitHub Release 必須全綠後
  才會分派 PyPI、Maven Central、npm、crates.io 與 NuGet 發布。

### Changed
- 擴充 IT、UI、正式文書與日常語境的保守轉換保護；同一批 1,008 筆私有案例相較
  v4.4.1 淨增 4 筆 accepted、0 筆 accepted regression（約 +0.40 個百分點）。
- Java release gate 由 `mvn test` 強化為 `mvn verify`；發版前新增詞庫、target
  idempotency、版本同步與 SDK export freshness 驗證。
- 精準度文件改以可重現樣本結果表述，不再使用「零誤判／零錯轉」絕對宣稱。
- Java、TypeScript、Rust、Go、.NET 的 Aho-Corasick 熱路徑改為單次掃描，同時產出
  詞彙命中與覆蓋位置；Python CLI helper 與檔案處理也拆分為獨立模組，公開 API 不變。

### Fixed
- 完成 1,251 筆 regression expected 與 132 筆 acceptable variants 的最終語意稽核；
  修正 13 筆舊 ground truth、移除 29 筆過時中國用語 acceptable，並保護「租用戶／
  命名空間」、將「熱重載」修正為台灣官方術語「熱重新載入」。
- 完成 474 筆新增詞條的第二輪全量審校，再修正 16 筆台灣用語、UI 文案與語意
  ground truth，包括「金鑰／設定檔／儲存貯體／檢查碼」、「回到首頁／由新到舊」
  及「分頁控制項」；同步清除會接受舊錯譯的 acceptable variants。
- 修正 14 筆 IT 語境的台灣用語與 ground truth，包括「請求簽章／請求逾時」、
  「權杖桶／檢查碼／設定對應」、「漸進式發布」及「移轉指令碼／復原」；同步更新
  9 筆 annotation、5 筆 holdout regression 與所有 SDK 詞庫資料。
- 修正 3 筆 expert re-audit 發現的語意 ground truth：rollback 不再誤作「回溯」、
  `future` 型別不再直譯成「未來物件」、物業管理單位不再偷換成管委會。
- 移除 4 筆已由泛化規則覆蓋的冗餘完整句 source mapping，保留必要 identity 防止
  二次轉換破壞「發布／分區／命名空間／綁定」。
- CI：升級 `central-publishing-maven-plugin` 0.7.0 → 0.11.0。Sonatype Central API 新增 `warnings` 欄位，舊版 plugin 嚴格解析會丟 `UnrecognizedPropertyException` 導致 Java 發布流程誤報 BUILD FAILURE（v4.4.1 artifact 其實已成功發布到 Maven Central，僅回應無法解析）

## [4.4.1] - 2026-06-30

### Fixed
- Phase 0 spike 精準度修復（held-out 真實書籍語料盲測發現，非 corpus 自我循環）：
  - **過度轉換**：`临时` 由 `暫時` 修正為 `臨時`（暫時 zànshí ≠ 臨時 línshí；連帶 `临时工/临时演员/临时服务`），違反「寧可少轉，不要錯轉」的舊詞條
  - **殘留簡體字**：`卧` 補進安全字元層（`卧室→臥室`）；Unihan kTraditionalVariant 未收此 1:1，新增 `generate_charmap.py` 的 `MANUAL_ADDITIONS` 防 regenerate 遺失
  - **漏在地化**：新增醫療術語 `超声波→超音波`
- `.zhtwignore` 補上 `src/zhtw/data/charmap/`（字元映射 key 為簡體，先前未排除，有被自身 hook 轉換之虞）

### Added
- `tests/test_golden_rule_battery.py`：新增 8 句 Phase 0 spike 回歸案例（247→255 句）

## [4.4.0] - 2026-06-11

### Fixed
- 詞庫根因稽核：22 個雙語境裸詞長詞化（收藏/返回/保存/评论/质量/支持/对象/文件/程序/项目 等）、
  歧義字防火牆補洞（克→公克 等災難級預設移除；干/复/舍/咸/范/伙/佣/沈/姜/症 改逐詞列舉）、
  保護詞擴充（天后/后羿/辛丑）與簡繁形盲點修復（邻里→鄰里）、opencc 變體字清洗 126 條
- 詞庫載入優先序明確化：手工詞庫必定覆蓋 bulk 匯入（opencc.json）
- `process_directory(sources=None)` 字元層靜默關閉
- pre-commit zhtw hook 改用 repo 當前程式碼並尊重 `.zhtwignore`（文件反覆損毀的根因）

### Changed
- 轉換效能 2.1x（單次 Aho-Corasick 掃描 + str.translate fast path），公開 API 不變
- opencc.json 純 Apache-2.0 化：移除 1,372 條 MediaWiki（GPL-2.0+）詞條，新增 THIRD_PARTY_NOTICES.md
- 釋出流程腳本化：`make release` 強化（CHANGELOG/分支/乾淨樹閘門、Java 驗證、雙 tag）、
  新增 `make release-dry` 與 `make release-verify`（workflow + 6 registry + Homebrew 驗證）

### Added
- `tests/test_golden_rule_battery.py`：172 句「寧可少轉，不要錯轉」回歸驗收

## [4.3.0] - 2026-04-11

### Added
- **C# (.NET) SDK**：全新 `Zhtw` NuGet package，第 6 個語言 SDK
  - Multi-target `netstandard2.0` + `net8.0`（支援 .NET Framework 4.7.2+、.NET Core、Mono、Unity）
  - 完整 Convert/Check/Lookup API，與其他 5 語言 SDK 功能對等
  - Self-implemented Aho-Corasick automaton，三層轉換（詞彙→balanced→字元）
  - 24 tests，含 golden-test.json 跨語言一致性驗證
  - CI/CD：GitHub Actions build + test + NuGet publish
- **Go CLI binary**：standalone `zhtw` 命令列工具，跨平台（macOS/Linux/Windows × amd64/arm64）
  - `convert`、`check`、`lookup` 子命令，支援 `--json`、`--file`、`--sources`、`--ambiguity-mode`
  - GitHub Releases 自動編譯 + 上傳 tarball/zip + checksums

## [4.1.0] - 2026-04-11

### Added
- **Balanced Mode（歧義字語義消歧 v1）**：全新 `ambiguityMode: "balanced"` 選項，10 個高頻歧義字自動套用預設繁體 + protect_terms 例外保護
  - 10 個已處理歧義字：几→幾、丰→豐、杰→傑、卤→滷、坛→壇、弥→彌、摆→擺、纤→纖、后→後、里→裡
  - 17 個 protect_terms：皇后/太后/后妃/后土/影后/歌后/后冠、公里/英里/海里/萬里長城/千里 等
  - 三層轉換架構：詞彙層（Aho-Corasick）→ balanced defaults 層 → 字元層（charmap）
  - CLI：`zhtw fix --ambiguity-mode balanced`、`zhtw check --ambiguity-mode balanced`、`zhtw lookup --ambiguity-mode balanced`
  - Balanced mode 為 CN→TW 專屬，HK-only 路徑自動降級為 strict（6 處 CN gate）
  - 全 4 SDK 實作一致，golden-test.json 跨語言驗證
- **Rust SDK**：全新 `zhtw` crate 釋出至 crates.io
  - 與 Java / TypeScript SDK 完整功能對等（`convert`、`check`、`lookup`、`sources`、`custom_dict`、`ambiguity_mode`）
  - Compile-time `phf::Map` 字元層（zero runtime hash construction）
  - Pre-compiled `daachorse::CharwiseDoubleArrayAhoCorasick` 嵌入 via `build.rs`
  - Byte-for-byte parity verified via shared `sdk/data/golden-test.json`
- **WASM SDK**：全新 `zhtw-wasm` npm package（Rust core compiled to WebAssembly）
  - Drop-in API compatible with `zhtw-js`
  - Published via npm Trusted Publishing (OIDC)
- **歧義字擴充 v1.2/v1.3**：18 個歧義字從 charmap 排除至安全名單（仆/尸/赝/镋/镌 等）
- **SDK 全面對齊**：Python / Java / TypeScript / Rust 四語言 convert/check/lookup 行為完全一致
  - Covered positions（identity term 保護）跨 SDK 統一
  - Identity golden cases：尸位素餐、人云亦云、急症、炎症、党太尉吃匾食
  - 伙头→伙頭 regression gate（term target 不被 charmap 二次轉換）
  - 影后 protect-term balanced lookup golden case

### Fixed
- **pre-commit hook 汙染修復**：`generate_charmap.py` 被 zhtw hook 靜默轉換簡體 key → 繁體，導致 7 個歧義字洩漏至 safe_chars.json；已修復並加 `# zhtw:disable` header
- **Java lookup() term target 二次轉換**：移除錯誤的 `applyCharmap(target)` 呼叫，term target 現在與 Python/TS/Rust 一致（verbatim 輸出）
- **Python lookup_word() 缺 balanced mode**：新增 `ambiguity_mode` 參數 + CN gate 防護
- **Balanced mode HK 洩漏**：6 處 CN gate 確保 balanced defaults 不在 HK-only 路徑生效

### Changed
- 轉換架構從雙層（詞彙+字元）升級為三層（詞彙 + balanced defaults + 字元）
- `disambiguation.json` 取代 `balanced_defaults.json` 為歧義字資料來源
- `make bump` updates 8 locations（新增 `sdk/rust/zhtw-wasm/package.json`）
- `sdk/rust/` converted from single-crate scaffold to workspace
- `.github/workflows/sdk-rust.yml` replaced fake-green stub with full pipeline
- CLAUDE.md golden rule 6 updated：7 → 8 mono-versioning locations
- charmap 字元數：6,344 → 6,360（歧義字重新評估後微調）

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

[Unreleased]: https://github.com/rajatim/zhtw/compare/v4.4.5...HEAD
[4.4.5]: https://github.com/rajatim/zhtw/compare/v4.4.4...v4.4.5
[4.4.4]: https://github.com/rajatim/zhtw/compare/v4.4.3...v4.4.4
[4.4.3]: https://github.com/rajatim/zhtw/compare/v4.4.2...v4.4.3
[4.4.2]: https://github.com/rajatim/zhtw/compare/v4.4.1...v4.4.2
[4.4.1]: https://github.com/rajatim/zhtw/compare/v4.4.0...v4.4.1
[4.4.0]: https://github.com/rajatim/zhtw/compare/v4.3.0...v4.4.0
[4.3.0]: https://github.com/rajatim/zhtw/compare/v4.1.0...v4.3.0
[4.1.0]: https://github.com/rajatim/zhtw/compare/v4.0.1...v4.1.0
[4.0.1]: https://github.com/rajatim/zhtw/compare/v4.0.0...v4.0.1
[4.0.0]: https://github.com/rajatim/zhtw/compare/v3.4.0...v4.0.0
[3.4.0]: https://github.com/rajatim/zhtw/compare/v3.3.0...v3.4.0
[3.3.0]: https://github.com/rajatim/zhtw/compare/v3.2.1...v3.3.0
[3.2.1]: https://github.com/rajatim/zhtw/compare/v3.2.0...v3.2.1
[3.2.0]: https://github.com/rajatim/zhtw/compare/v3.1.0...v3.2.0
[3.1.0]: https://github.com/rajatim/zhtw/compare/v3.0.0...v3.1.0
[3.0.0]: https://github.com/rajatim/zhtw/compare/v2.8.7...v3.0.0
[2.8.7]: https://github.com/rajatim/zhtw/compare/v2.8.6...v2.8.7
[2.8.6]: https://github.com/rajatim/zhtw/compare/v2.8.5...v2.8.6
[2.8.5]: https://github.com/rajatim/zhtw/compare/v2.8.4...v2.8.5
[2.8.4]: https://github.com/rajatim/zhtw/compare/v2.8.3...v2.8.4
[2.8.3]: https://github.com/rajatim/zhtw/compare/v2.8.2...v2.8.3
[2.8.2]: https://github.com/rajatim/zhtw/compare/v2.8.1...v2.8.2
[2.8.1]: https://github.com/rajatim/zhtw/compare/v2.8.0...v2.8.1
[2.8.0]: https://github.com/rajatim/zhtw/compare/v2.7.0...v2.8.0
[2.7.0]: https://github.com/rajatim/zhtw/compare/v2.6.0...v2.7.0
[2.6.0]: https://github.com/rajatim/zhtw/compare/v2.5.0...v2.6.0
[2.5.0]: https://github.com/rajatim/zhtw/compare/v2.4.0...v2.5.0
[2.4.0]: https://github.com/rajatim/zhtw/compare/v2.3.0...v2.4.0
[2.3.0]: https://github.com/rajatim/zhtw/compare/v2.2.0...v2.3.0
[2.2.0]: https://github.com/rajatim/zhtw/compare/v2.1.0...v2.2.0
[2.1.0]: https://github.com/rajatim/zhtw/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/rajatim/zhtw/compare/v1.5.0...v2.0.0
[1.5.0]: https://github.com/rajatim/zhtw/compare/v1.0.0...v1.5.0
[1.0.0]: https://github.com/rajatim/zhtw/releases/tag/v1.0.0
