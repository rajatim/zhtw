# zhtw 4.5.0 可解釋規則基礎實作計畫

> Status: Done
> Date: 2026-08-27
> Approved: 2026-08-27
> Result: schema v2、Unicode 17、explain、JSON adapter 與六套 SDK parity 已完成；2026-08-27 release gate 通過，版本維持 4.4.5，未執行發布。
> Target: 4.5.0
> Version scope: https://rajatim.wiki/projects/zhtw/roadmap/
> Supporting plan: `docs/plans/2026-08-26-unicode-and-mixed-term-import-plan.md`

## Goal

在不改變 4.4.5 既有預設輸出的前提下，完成後續 profile、地區規則與結構化檔案
需要的基礎：

1. 規則資料結構 v2 與 v1 相容層；
2. 跨 SDK 共用的穩定規則 ID 與描述 metadata；
3. Unicode 17.0 A～J 漢字偵測與安全的中英數混合詞待審流程；
4. 不影響轉換結果的唯讀 `explain`；
5. 明確啟用、只轉字串 value、保留其他原始位元組的 JSON adapter；
6. Python、Java、TypeScript、Rust／WASM、Go、.NET 的同版一致性。

4.5.0 不使用 domain、trust、priority 或 review metadata 改變規則是否生效。這些欄位
先負責描述、稽核與解釋；profile 套用行為留到 4.6.0。4.5.0 也不新增未經人工核准的
詞彙，不擴充香港、新加坡或澳門正式詞庫，不改 leftmost-longest 選擇方式。

### 固定相容性基線

- 以 `v4.4.5`（commit `8c254ca`）的 effective term map、charmap、balanced defaults、
  identity guards、golden output、公開 benchmark 與第二次轉換結果為基線。目前分支
  相對該 tag 的 `src/` 與 `sdk/` 沒有差異。
- schema v2 開啟或關閉 metadata、`explain` 開啟或關閉，都必須產生完全相同的
  轉換文字。
- 一般 `zhtw check`／`zhtw fix` 對 `.json` 的既有行為在 4.x 不默默改變；安全
  JSON adapter 必須由呼叫端明確啟用。

## Blast radius (files & repos)

所有實作都在 `zhtw` repo。wiki 只管理版本範圍，已由獨立的跨 repo 整併計畫處理。
若實作需要更動下列範圍以外的 repo、公開版本範圍或預設輸出，必須先修訂計畫並重新
取得核准。

### Python 規則與資料層

- 新增 `src/zhtw/rules.py`：`RuleRecord`、enum、v1 相容轉換、ID 驗證與 precedence
  結果。
- 新增 `src/zhtw/data/schemas/rule-v2.schema.json`：外部 v2 custom／pending 規則格式。
- 修改 `src/zhtw/dictionary.py`：同時載入 v1 與 v2，保留完整 catalog 與目前相同的
  effective string map。
- 修改 `src/zhtw/import_terms.py`、`src/zhtw/review.py`、`src/zhtw/cli.py`：混合詞
  驗證與 schema v2 待審資料。
- 新增 `src/zhtw/unicode_ranges.py`，修改 `src/zhtw/converter.py` 與
  `src/zhtw/file_converter.py`：共用 Unicode 17.0 Han range 定義。
- 修改 `src/zhtw/export.py`、`src/zhtw/export_cmd.py`：輸出 schema v2 shared data、
  catalog 與共用 golden fixtures。
- 既有 `src/zhtw/data/terms/{cn,hk}/*.json` 在 4.5.0 不做三萬多條的全面格式重寫；
  由 v1 相容層產生 legacy metadata。只有新建或人工修改的規則才使用 v2 authoring
  格式，避免把格式遷移與語言內容變更混在一起。

### Python `explain` 與 JSON adapter

- 修改 `src/zhtw/matcher.py`、`src/zhtw/converter.py`、`src/zhtw/charconv.py`、
  `src/zhtw/lookup.py`：正式單次掃描同時產生 conversion 與 trace。
- 新增 `src/zhtw/explain.py`：共用 event／result model 與敏感內容最小化。
- 新增 `src/zhtw/json_adapter.py`：JSON token span、value-only 轉換、驗證與原子寫入。
- 修改 `src/zhtw/cli.py`、`src/zhtw/cli_support.py`：明確 adapter 選項、報告與錯誤碼。
- 修改 `src/zhtw/__init__.py`：只匯出經核准的公開 `explain`／JSON API；版本號仍
  保持目前值，直到發版準備。

### Shared data 與六種 SDK

- `sdk/data/zhtw-data.schema.json`、`sdk/data/zhtw-data.json`、
  `sdk/data/golden-test.json`：schema v2、catalog、trace 與 parity fixtures。
- 視實作結果新增 `sdk/data/json-adapter-golden.json`；若新增，所有 SDK 必須讀同一份
  fixture，不得各自維護 expected。
- Java：`ZhtwData`、`AhoCorasickMatcher`、`ZhtwConverter`、`Match` 與新增的
  rule／explain／JSON model、tests。
- TypeScript：`src/data/*`、`src/core/{types,matcher,converter}.ts`、Node／browser
  exports 與對應 tests。
- Rust／WASM：`zhtw/{build.rs,src/generated.rs,src/matcher.rs,src/converter.rs,
  src/lib.rs}`、WASM bindings 與 tests。
- Go：`zhtw/{data,types,matcher,converter,builder,zhtw}.go`、CLI bridge 與 tests。
- .NET：`src/{ZhtwData,Types,AhoCorasick,Converter,ConverterBuilder,ZhtwConvert}.cs`
  與 tests。
- 所有 SDK 的 codepoint index 定義維持不變；supplementary-plane Han 在 UTF-16
  runtime 仍以 Unicode codepoint index 對外。

### 測試、文件與發版

- Python：新增或修改 `tests/test_{dictionary,import_terms,converter,matcher,export,
  cli,lookup}.py`，並新增 rule schema、explain、Unicode 與 JSON adapter 專門測試。
- Release gates：`Makefile`、`scripts/release-verify.sh`、`tests/test_release_process.py`
  只在需要新增 schema／fixture freshness gate 時修改，不改 Jenkins-only 原則。
- 文件：`README.md`、`docs/guides/CLI-ADVANCED.md`、新增
  `docs/reference/rule-schema-v2.md`、`docs/reference/explain-api.md`、
  `docs/reference/json-adapter.md`，以及 `CHANGELOG.md` 的 `[Unreleased]`。
- 發版準備才使用 `make bump VERSION=4.5.0`，同步 AGENTS.md 規定的全部版本檔與
  generated SDK data。feature development 期間不先升版、不建 tag、不發布 registry。
- Blind-v3 private artifacts 仍依 `docs/plans/2026-08-01-blind-v3-plan.md` 管理；
  實作未凍結前不得執行 one-shot evaluation。

## Steps

### Phase A0：凍結 4.4.5 行為與契約

1. 匯出並記錄 4.4.5 的 effective source→target map、winning source class、target
   guards、charmap、balanced defaults 與 shared-data checksum。這是 schema 遷移的
   等價性基線，不新增或修正詞彙。
2. 先寫 v2 JSON Schema、`RuleRecord`、enum 與公開契約測試，再修改 loader。
3. 固定規則 ID 政策：
   - v2 authored rule 使用明確 `id`；
   - v1 built-in／custom rule 由 source locale、source、target 與 rule class 產生
     deterministic legacy ID；
   - 檔案路徑不進 ID，搬檔不應改 ID；
   - target 或語意真的改變時視為新規則 ID；
   - ID 碰撞、重複 ID 指向不同內容、未知 enum 一律 fail closed。
4. 固定 precedence 相容層：bulk、generated guard、curated、source order、custom
   override 的 winner 必須和 4.4.5 完全相同。v2 priority 在 4.5.0 只能記錄既有
   precedence，不得重新排序。

### Phase A1：dual loader 與 shared-data schema v2

5. 讓 Python loader 同時接受 legacy string map、現有 extended value object 與 v2
   rule records。loader 回傳完整 catalog；matcher 仍收到和 4.4.5 相同的 effective
   `dict[str, str]`。
6. shared data 升為 schema v2，但保留現有 `terms` effective map，另加 rule catalog
   與 Unicode metadata。六種 SDK 先使用原 `terms` 建 matcher，因此 schema 升級本身
   不改輸出。
7. 每種 SDK 同時接受 shared-data v1 與 v2；未知 schema、未知必要欄位、重複 ID 與
   catalog／terms 不一致時明確失敗。不得把 v2 解析失敗靜默退回 v1。
8. 若任何 production term JSON 需要轉成 v2，格式遷移與文字修改分開 commit；逐筆
   證明 source／target pair 與 effective winner 沒變。純格式搬移遵守 verbatim 與
   `--no-verify` 規則，避免 zhtw hook 改寫簡體來源。

### Phase A2：Unicode 與混合詞待審流程

9. 以 Unicode 17.0 官方 Blocks 資料固定 Unified Ideographs、Extensions A～J、
   Compatibility Ideographs 與 supplement 的 range；加入每個 range 的頭尾與相鄰
   非 Han codepoint 測試。
10. 混合詞 source／target 都必須至少含一個 Han codepoint；只接受核准的 technical
    ASCII allowlist，且移除 Han 後的非 Han 序列完全相同。identity、過長、控制字元、
    前後空白、emoji、未知符號、重複與 conflict 仍拒絕。
11. 匯入結果直接寫 schema v2 pending candidate，包含 provenance、review status 與
    deterministic packet metadata；未經 maintainer final decision 不得進正式規則。

### Phase B：唯讀 `explain`

12. matcher 的同一次 automaton scan 必須保留 raw candidates、identity protection、
    selected conversions、overlap loser、loader conflict winner 與 effective coverage。
    不得為了 `explain` 另跑一套簡化演算法。
13. term、identity、balanced 與 char layer 使用同一個 `ExplainEvent` schema。event
    至少包含 rule ID、layer、outcome、input codepoint span、output span、source、target
    與短 reason code；不同 SDK 的 JSON 名稱與 enum 值完全相同。
14. `explain(text)` 由同一次正式轉換回傳 output 與 events。預設不回傳整份輸入、
    檔案內容或上下文；只包含實際 span。CLI 顯示上下文必須另加明確選項。
15. 對同一個 input、source、ambiguity mode 與 custom rules，`convert(text)` 必須等於
    `explain(text).output`。所有 golden cases 與公開 benchmark 都加此等價閘門。

### Phase C：明確啟用的 JSON value adapter

16. adapter 先用正式 parser 驗證完整 JSON，再以 token span 辨識 object key 與 value。
    只替換 string value token；key、空白、縮排、換行、數字原樣、布林值、`null`、
    結構與 array order 的原始位元組不得改變。
17. 沒變的 string value token 必須逐位元保留；有變的 value 只重寫該 token，並用跨
    SDK 固定的 JSON escaping 規則輸出。轉換後再解析一次並驗證非 value 結構相等。
18. CLI 使用明確 adapter 選項；沒有 adapter 選項時維持現有一般文字流程。單檔寫入
    使用同目錄暫存檔、flush／fsync 與 atomic replace；任何 parse、convert、encode、
    verify 或 write 失敗都保留原檔且回傳非零錯誤碼。
19. shared fixtures 涵蓋 nested object／array、空字串、重複文字、escaped quote、
    backslash、surrogate pair、supplementary Han、混合中英文、不同 whitespace、數字
    表示、duplicate key、invalid syntax 與 read-only／write failure。

### Phase D：跨 SDK、凍結與發版準備

20. 依序完成 Python reference、shared golden schema，再完成 Java、TypeScript、Rust／
    WASM、Go、.NET。任一公開 feature 尚未達 parity，就不能標示 4.5.0 完成。
21. 每一 phase 跑 targeted tests；完成後跑：
    - `zhtw validate`；
    - `make version-check`；
    - `make export-check`；
    - `make benchmark-validate`；
    - `make test-all`；
    - `make release-gate`。
22. 程式與公開契約凍結後，才依 Blind-v3 plan 收集／完成 private data、annotation、
    preregistration 與 one-shot evaluation。不得使用 Blind-v1／v2 或公開 regression
    內容建立 fresh claim，也不得看到 Blind-v3 分數後調整同一候選。
23. 更新主計畫為 `Done` 並記錄結果。實際 4.5.0 mono-version bump、Jenkins build、
    `all` verify、release preview 與 publish 另依 release checklist 取得明確核准。

## Risks & rollback

- **schema v2 偷改輸出：** catalog 與 effective map 分離；4.5.0 matcher 仍吃相同
  string map。任何 baseline map、golden output、benchmark 或 idempotency 差異都阻擋。
- **ID 不穩定：** legacy ID 不含檔案路徑；相同規則跨重建與搬檔保持一致。碰撞與同 ID
  異內容 fail closed。
- **metadata 被誤當 runtime logic：** domain、trust、review、priority 在 4.5.0 只供
  驗證與 explain；任何以它們改變生效規則的程式碼都超出本版範圍。
- **shared data 變大：** catalog metadata 會增加 SDK package 大小。release gate 必須
  記錄各 artifact 前後大小並設合理上限；超出時先調整 compact encoding，不移除必要
  驗證欄位。
- **trace 造成效能下降：**一般 `convert` 不建完整 event objects；`explain` 共用同一次
  scan。以既有 stress／benchmark 比較時間與記憶體，明顯退步就停下 review。
- **敏感內容洩漏：** explain 預設只有命中 span，不含整份文件、路徑、環境或上下文；
  CLI 額外上下文必須 opt-in，錯誤 log 不印完整輸入。
- **JSON parser 重新排版：** adapter 不用一般 deserialize→serialize 流程改寫整份文件，
  只替換已確認的 value token span，並用 exact-byte fixture 阻擋無關 diff。
- **JSON duplicate key：**正式 parser 可能接受但合併 duplicate key。token scanner 不得
  因此漏轉或重排；若任一 SDK 無法安全保留，全部 SDK 對 duplicate key 統一 fail closed。
- **原子寫入跨平台差異：**每個 SDK／CLI 需有失敗注入測試；原檔在任何失敗後都必須
  保持可解析且內容不變。
- **多 SDK 範圍過大：**按 A～D 分段 commit 與 review。若需要縮小 4.5.0，先更新 wiki
  範圍與本計畫再繼續，不能發布部分 feature 卻宣稱完整。
- **rollback：**A、B、C 各自獨立 commit chain。未發布時可一般 revert；shared data
  回到 schema v1 後需一起 revert SDK loader。registry 一旦接受 4.5.0 就不能刪版，內容
  問題只能修正後發布下一個 patch。

## Decisions

1. `explain` 使用單一 API 回傳 `{output, events}`，呼叫端不需再跑一次 convert。
2. CLI 在既有 `check`／`fix` 加上 `--adapter json`；SDK 提供 `convertJson` 或語言慣用的
   等價名稱，避免和 `--json` 機器輸出混淆。
3. shared-data schema v2 保留現有 `terms` effective map，再新增完整 catalog，讓 matcher
   的輸入與輸出保持不變。
4. legacy rule 的 target 或 rule class 改變時產生新 ID；檔案搬移與重新建置不改 ID。
5. duplicate JSON key 在六種 SDK 全部 fail closed，避免 parser 合併規則不同。

## Open questions

無。以上五項公開契約已由 maintainer 於 2026-08-27 核准；實作若需要改變其中任何一項，
必須先更新本計畫並重新取得核准。
