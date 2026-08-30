# zhtw 4.5.0 發版候選計畫

> Status: Done
> Result: build #31、verify #13、PREVIEW #24 與 CREDENTIAL_PREFLIGHT #25 皆成功；其後依獨立明確核准完成 release #26，4.5.0 公開驗證 12/12 通過。
> Date: 2026-08-27
> Approved: 2026-08-27
> Source branch: `plan/4.5.0-rule-foundation`
> Feature implementation SHA before this plan: `891ab3da86d0ee04dcd31c7c80a9f058be6254b6`
> Current local main SHA: `79f179e360bfdfb37198fe0bdd8ae397ab697c50`
> Target version: `4.5.0`（minor）

## Goal

把已完成並通過完整測試的 4.5.0 規則基礎整合到 `main`，再透過 Jenkins 建立、驗證與
唯讀預演同一份 4.5.0 封存候選。這份計畫不授權 `PUBLISH_ALL`、tag、GitHub Release
或任何 registry 發布；正式發布必須等候選 build 與 verify 編號確定後，再取得一次
明確核准。

已完成的前置證據：

- `make release-gate` 通過；Python 5,631、Java 196、TypeScript 200、Rust 35、.NET 31
  項測試通過，Go race／vet／lint 通過。
- 2026-08-27 使用 Chrome `151.0.7922.174` 與相同版本 ChromeDriver，在真正的 headless
  Chrome 執行 WASM browser tests：3 passed、0 failed，涵蓋 `convert`、Converter
  instance、`explain` 與 JSON adapter。
- `wasm-pack 0.13.1` 自動快取 ChromeDriver 152，和本機 Chrome 151 不相容；直接指定
  官方相符 driver 後測試成功，因此原本 HTTP 404／SIGKILL 是測試環境版本不相容，
  不是 WASM assertion 失敗。

## Blast radius (files & repos)

### `zhtw` Git 歷史

- 在新增本計畫前，`plan/4.5.0-rule-foundation` 比本機 `main` 領先 17 個 commit、沒有
  落後 commit。功能範圍共有 116 個檔案；本計畫獨立提交後會再增加 1 個 commit 與
  1 個檔案。
- 合併目標是把 `main` fast-forward 到「本計畫 Approved commit」的確切 SHA；提交後
  必須重新記錄。若 `origin/main` 已前進或無法 fast-forward，停止並重新 review，
  不自動 rebase、merge 或改寫歷史。
- 功能差異主要是 schema v2、Unicode 17、`explain`、JSON adapter、shared fixtures、
  六套 SDK 與文件；版本仍是 4.4.5。
- 本計畫核准後先以獨立 commit 保存，再開始合併操作。

### 遠端 `origin/main`

- push 是對外動作。執行前必須重新 fetch、顯示 local／remote SHA、確認工作樹乾淨，
  並取得針對這個確切 SHA 的明確同意。
- 只允許一般 fast-forward push；禁止 force push、刪 branch／tag或改寫歷史。

### Jenkins 與候選內容

- 只使用 `zhtw/build`、`zhtw/verify`、`zhtw/release` 三個 Jenkins job，全部 detached
  啟動並用 API／UI 監看。
- `zhtw/build` 從 remote `main` 建候選並使用 `VERSION_BUMP=minor`，在 disposable
  workspace 執行 `make bump VERSION=4.5.0`。它會同步 pyproject、Python、Java、
  TypeScript、Rust、.NET、shared data 與 WASM package 的 mono-version，不在本機
  branch 先手動升版。
- `zhtw/verify` 對同一個成功 build 執行 `VERIFY_SUITE=all`；`zhtw/release` 只執行
  `PREVIEW` 與 `CREDENTIAL_PREFLIGHT`。這些步驟不得建立 tag、Release 或 registry
  version。
- `PUBLISH_ALL`、`RESUME_ALL`、任何 `RETRY_*`、正式 tag、GitHub Release、Homebrew
  commit 與 registry 上傳全部排除在本計畫之外。

### 其他 repo 與基礎設施

- 不修改 `rajatim-wiki`、`github-workspace` 或 Jenkins job 設定。
- 不安裝或更新系統 Chrome／ChromeDriver。這次相符 driver 只放在 `/tmp` 作為一次性
  測試工具，不進 git。

## Steps

1. 自我 review 本計畫的假設、影響範圍、rollback 與所有外部動作核准點；修正後停下
   等 maintainer 核准。
2. 核准後把本計畫改為 `Approved`，以獨立 commit 提交。
3. `git fetch origin`，確認 `origin/main`、本機 `main` 與來源 branch 的 ancestry；
   remote 若有新 commit，停止並重新 review 差異。
4. 重新確認來源 branch 工作樹乾淨、完整 commit 清單、116 個功能檔案加上本計畫、
   CHANGELOG `[Unreleased]` 與版本仍為 4.4.5。
5. 切到本機 `main`，只用 `git merge --ff-only plan/4.5.0-rule-foundation`；不得建立額外
   merge commit，不得 rebase。
6. 在本機 `main` 重跑 `git diff --check`、`make version-check`、`make export-check`、
   `make benchmark-validate` 與 `make release-gate`。再次用相符 Chrome／ChromeDriver
   跑 3 項 WASM browser tests。
7. 顯示本機 `main`、`origin/main`、待 push commit 與工作樹狀態，說明 push 會改變
   shared remote；停下取得這個確切 SHA 的明確 push 核准。
8. 核准後只執行一般 `git push origin main`，再 fetch 並確認 `origin/main` 指向相同 SHA。
9. 顯示 `zhtw/build` 的確切參數 `VERSION_BUMP=minor`；取得該 job 的明確核准後 detached
   啟動並監看到結束。
10. Review build manifest、source SHA／tree、candidate tree、4.5.0 版本、dependency
    gates、toolchain 證據、套件 checksum、consumer smoke tests 與 release notes。
11. 取得確切 build number 的核准後，對同一候選 detached 執行
    `zhtw/verify VERIFY_SUITE=all`，監看到產生 release-eligible receipt。
12. Review receipt 的 build、SHA、tree、版本、pipeline SHA、manifest/checksum 與驗證
    證據 hash，確認全部和候選一致。
13. 取得確切 build／verify 組合的核准後執行 `zhtw/release PREVIEW`；確認沒有新增 tag、
    GitHub Release 或 registry version。
14. 取得同一組 build／verify 的核准後執行 `CREDENTIAL_PREFLIGHT`；確認只做 authentication
    與權限 probe，沒有上傳套件。
15. 彙整 build／verify／preview／credential 證據、已驗證與未驗證項目，把計畫標為
    `Done`。停下來等待是否正式執行 `PUBLISH_ALL` 的獨立明確核准。

## Risks & rollback

- **remote main 已前進：** fetch 後若 `origin/main` 不是預期 ancestry，停止；不猜測整合
  方式、不 rebase、不 force push。更新計畫並重新核准。
- **大範圍 fast-forward：** 116 個檔案雖已分階段 commit 與測試，仍在 merge 前再次
  核對 commit 清單與完整 gate。push 前保留來源 branch，不刪 branch。
- **push 無法當作未發生：** push 前顯示確切目標並取得明確同意。若內容有問題，使用
  一般 revert commit；不 reset remote、不改寫歷史。
- **Jenkins 候選失敗：** build／verify／preview／preflight 都不發布，可保留失敗證據並
  修正後建立新候選。不得略過 gate 或改用本機發布。
- **Chrome 自動更新再次造成 driver mismatch：**每次 browser test 都先讀取 Chrome
  版本，使用官方相同版本 driver。若沒有相符版本，標記環境阻擋，不把 Node WASM
  測試冒充 browser test。
- **registry 不可 rollback：**本計畫不執行任何 registry 寫入。正式發布必須拿確切
  build／verify 再核准；一旦發布，失敗只能依同一候選 recovery 或升下一個 patch。

## Open questions

1. 是否核准本計畫，先把計畫本身獨立提交，再進行 remote freshness review 與本機
   fast-forward？
2. `origin/main` push、每一個 Jenkins job，以及最後 `PUBLISH_ALL` 都保留各自的明確
   核准點；本次計畫核准不視為提前核准這些對外動作。
