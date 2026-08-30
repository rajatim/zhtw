# 釋出流程

> zhtw 的建置、驗證、套件發布與公開文件發布只走 Jenkins。GitHub Actions、手動 tag、
> `gh workflow run`、本機 registry publish 都不是備援路徑。

## 最高優先順序規則

```text
⛔ 沒有使用者明確同意，不可公開釋出
⛔ 不可用 make release、手動 tag 或手動 publish 繞過 Jenkins
⛔ 已被 registry 接受的版本不可回滾、覆蓋或重用
✅ 所有 SDK 必須維持 mono-versioning
✅ build、verify、read-only preview、正式 publication 必須使用同一份封存候選
```

## 角色分工

- 貢獻者可以執行 `make bump VERSION=X.Y.Z`、`make version-check`、
  `make release-gate`，但不能因此建立正式版本。
- `zhtw/build` 計算版本、產生候選 patch、測試一次並封存所有套件。
- `zhtw/verify` 只能選成功的 main `zhtw/build`；`VERIFY_SUITE=all` 通過後會封存
  繫結 SHA、tree、版本與候選 checksum 的 release-eligible receipt。
- `zhtw/release` 預設 `PREVIEW`，而且連 preview 都必須提供完全相符的成功
  verification receipt。`CREDENTIAL_PREFLIGHT` 會安全驗證所有發布 credential，
  但不建立 tag、Release 或 registry version；只有明確核准後才可 `PUBLISH_ALL`。
- `make release` 與 `make release-dry` 會 fail-closed，提醒改用 Jenkins。
- 三個 job 都只在準備發布時手動執行，不設每日、每週或 SCM 自動觸發。
  `zhtw/build` 固定從 `main` 建立候選，不接受任意 branch。
- 公開文件另用手動 `zhtw/docs-build` 與 `zhtw/docs-publish`。它們不建立套件候選、
  tag 或 registry version，也不能接受任意 branch。

## 標準流程

### 1. 建立完整候選

```bash
jcli build zhtw/build \
  -p VERSION_BUMP=patch
```

`patch` 用於修正、`minor` 用於向下相容的新功能、`major` 用於 breaking
change。Jenkins 會同步更新所有 SDK 版本、提升 CHANGELOG `[Unreleased]`、跑完整
release gate，阻擋 open medium 以上 Dependabot 警示與即將到期的 npm token；它也會
執行 Python、npm、Rust、Go、.NET、Maven 的相依套件安全檢查。完成後建出 PyPI、
npm x2、crate、NuGet、Maven 與五種 Go binary，並從封存成品逐一執行 consumer
smoke test。release gate 同時執行公開文件雙語配對、版本／邊界檢查與 MkDocs strict
build；文件錯誤會阻擋候選。候選會記錄 Jenkins pipeline 與完整 toolchain 版本證據。

### 2. 驗證同一份候選

```bash
jcli build zhtw/verify \
  -p BUILD_NUMBER=<成功的-zhtw-build> \
  -p VERIFY_SUITE=all
```

只有 `all` 會產生可供發布的 receipt。receipt 也會繫結驗證 pipeline 與驗證證據
checksum。`sdk-matrix` 與 `competitor-benchmark` 可以單獨診斷，但不能解除
release gate。`sdk-matrix` 會在獨立 Python 環境重跑 public docs check 與 strict
site build，避免候選只在 build workspace 偶然成功。

### 3. 唯讀預演

```bash
jcli build zhtw/release \
  -p BUILD_NUMBER=<成功的-zhtw-build> \
  -p VERIFY_BUILD_NUMBER=<相符的-zhtw-verify> \
  -p RELEASE_ACTION=PREVIEW \
  -p SKIP_CONFIRMATION=false
```

預演會先驗證 receipt、候選、toolchain 與驗證證據的 checksum，以及 base SHA、base
tree、candidate tree、版本完全相同，再檢查 main 前進關係與既有 tag。它不繫結
registry credential，也不改 Git 或外部服務。

### 4. 安全驗證所有 credential

```bash
jcli build zhtw/release \
  -p BUILD_NUMBER=<成功的-zhtw-build> \
  -p VERIFY_BUILD_NUMBER=<相符的-zhtw-verify> \
  -p RELEASE_ACTION=CREDENTIAL_PREFLIGHT \
  -p SKIP_CONFIRMATION=false
```

這個動作只做 authentication 與權限 probe，不上傳套件。它會驗證 GitHub API/SSH、
PyPI、npm 兩個 package 的 read-write scope 與到期日、crates.io、NuGet、Maven
Central token，以及 Maven GPG 簽章。

### 5. 明確核准後正式發布

```bash
jcli build zhtw/release \
  -p BUILD_NUMBER=<同一個-zhtw-build> \
  -p VERIFY_BUILD_NUMBER=<同一個-zhtw-verify> \
  -p RELEASE_ACTION=PUBLISH_ALL \
  -p APPROVAL_REFERENCE='<目前對話或變更單參照>' \
  -p SKIP_CONFIRMATION=true
```

正常順序是：雙 tag 與 GitHub Release → PyPI → npm `zhtw-js` → npm
`zhtw-wasm` → crates.io → NuGet → Maven Central → Homebrew → 完整公開驗證。

`PUBLISH_ALL` 只接受 24 小時內完成相依套件閘門、且 7 天內完成 `all` 驗證的候選。
開始任何會改變外部狀態的 action 前，Jenkins 會把選定的 build、verify 與本次 release
標記為永久保留，避免 recovery 證據被一般保留政策清除。

`SKIP_CONFIRMATION=true` 只代表使用者已在目前對話核准這組確切 build 與 verify；此時
`APPROVAL_REFERENCE` 必填。它不會略過 receipt、來源、checksum、tag、GitHub Release
notes、候選 tree 或 registry 驗證。

所有長時間 job 都要 detached 啟動，再用 Jenkins UI 或 API 監看回傳的 build number；
不可使用 attached `jcli -s -v`。CLI 連線中斷曾經直接中止還在執行的 Jenkins build。

## 失敗處理

公開 registry 沒有網站部署式 rollback。某一步失敗時：

1. 停止後續發布。
2. 使用同一組 `zhtw/build` 與 `zhtw/verify` 編號執行 `RESUME_ALL`。它會重新核對
   每個先前步驟，內容完全相同就跳過，從第一個未完成 registry 接續到最終公開驗證。
3. 已存在的版本只有在公開內容與封存候選相符時才會略過；PyPI 只補傳缺少的檔案。
4. 如果已發布內容本身有錯，只能修正後升下一個 patch；不可刪 tag 或重用版號。

```bash
jcli build zhtw/release \
  -p BUILD_NUMBER=<同一個-zhtw-build> \
  -p VERIFY_BUILD_NUMBER=<同一個-zhtw-verify> \
  -p RELEASE_ACTION=RESUME_ALL \
  -p APPROVAL_REFERENCE='<目前對話或 incident 參照>' \
  -p SKIP_CONFIRMATION=true
```

Maven 上傳後會立即封存 deployment ID。若狀態查詢斷線，使用
`RESUME_ALL` 加上該 ID 續查既有 deployment，不可建立第二次 upload。
Recovery action 可以使用超過上述 freshness 期限的同一份封存候選，因為它的目的只
是補完已開始的不可逆發布；SHA、tree、receipt 與 checksum 仍必須完全相符。

可用的修復動作：`RETRY_GIT`、`RETRY_PYPI`、`RETRY_NPM_JS`、
`RETRY_NPM_WASM`、`RETRY_CRATES`、`RETRY_NUGET`、`RETRY_MAVEN`、
`RETRY_HOMEBREW`。單項 `RETRY_*` 只修該項；完成後仍要跑 `RESUME_ALL`，讓後續
registry 與最後 12/12 驗證完成。每個動作仍是不可逆公開操作，必須確認。

## 限制

目前 Jenkins 只有 Linux builder。Python、Java、Node、Rust、Go 與 .NET 的 Linux
版本矩陣已搬到 `zhtw/verify`；Go 也會交叉編譯 Darwin/Windows binary。但 macOS 與
Windows 原生執行測試要等新增 Jenkins agent，不能把交叉編譯說成原生驗證。

內部 credential、job 維護與首次發布證據請依 private Jenkins runbook；公開 repo
不保存 Jenkins URL 或 secret 細節。

## 公開文件發布

正式站為 `https://zhtw.rajatim.com`，使用私有 S3、CloudFront OAC、ACM 與 Route 53。
Hub、Caddy、Lightsail 443 allowlist 與 `rajatim.wiki` 不在此流程內，也不得為文件站放寬。

```bash
jcli build zhtw/docs-build
jcli build zhtw/docs-publish \
  -p DOCS_BUILD_NUMBER=<成功-docs-build> \
  -p PUBLISH_ACTION=PREVIEW \
  -p SKIP_CONFIRMATION=false
```

- `docs-build` 固定 checkout 公開 `main`，執行 `make docs-build`，封存含 full SHA、tree、
  build number、`deployment.json` 與 checksum 的靜態 artifact。它沒有 AWS credential。
- `docs-publish` 不重建，只 CopyArtifact 精確成品。`PREVIEW` 不綁 AWS credential；
  `CREDENTIAL_PREFLIGHT` 只驗證 account、stack、private bucket、versioning 與 distribution。
- `DEPLOY` 與 `ROLLBACK` 會改公開站，必須指定精確 docs build。略過 UI 確認時
  `APPROVAL_REFERENCE` 必填，且 mutating run 與來源 docs build 都永久保留。
- 每個正式 action 在確認前重跑 credential preflight。AWS key 只能由 `zhtw/`
  folder-scoped Jenkins Credential 短暫注入；不得讀 agent profile、1Password 或 host cache。
- 發布先完整上傳 `releases/<source-sha>/` 並驗證 checksum，再更新 `current/` 與
  CloudFront invalidation。live switch 後失敗必須使用本次記錄的 previous SHA 自動回復。
- 公開驗證至少包含繁中、英文、`deployment.json` exact SHA、404 與 HSTS。第一次正式
  上線與重要版面變更另用真實 browser 檢查導覽、語言切換、console、network 與行動版。

純文件發布不變更 mono-version，也不代替套件 release gate。功能契約仍必須在下一個
`zhtw/build`／`verify all` 候選中通過文件檢查。

---

*需要時讀取：準備版本釋出*
