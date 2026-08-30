# 釋出核對清單

> zhtw 只透過 Jenkins 建置、驗證與發布。完整規則：`.claude/rules/releasing.md`。

## 釋出前人工判斷

- [ ] 使用者／Maintainer 明確同意要發布的確切 Jenkins build 與 verify build。
- [ ] CHANGELOG `[Unreleased]` 能讓使用者判斷是否值得升級。
- [ ] 中英文公開文件已同步功能、版本、相容性、限制與 roadmap，沒有內部 Jenkins
      編號、credential 名稱、private URL 或 runbook 步驟。
- [ ] 版號符合語意：breaking → major、新功能 → minor、修復 → patch。
- [ ] 詞庫有改動時，精準度 release gate 與治理證據均已完成。
- [ ] 已接受目前 Jenkins 沒有 macOS／Windows 原生 agent 的限制。

## 候選與唯讀預演

三個 zhtw job 都是手動、發版時才執行；不應存在每日、每週或 SCM trigger。

```bash
jcli build zhtw/build -p VERSION_BUMP=patch
jcli build zhtw/verify \
  -p BUILD_NUMBER=<成功-build> -p VERIFY_SUITE=all
jcli build zhtw/release \
  -p BUILD_NUMBER=<成功-build> -p VERIFY_BUILD_NUMBER=<成功-verify> \
  -p RELEASE_ACTION=PREVIEW \
  -p SKIP_CONFIRMATION=false
```

- [ ] build 固定 checkout `main`，沒有可選 branch 或自動排程。
- [ ] build 的 lint、release gate、全部套件建置、consumer smoke test 與 checksum 都成功。
- [ ] `make docs-build` 通過雙語配對、公開邊界、CLI 範例與 MkDocs strict build；
      `site/` 沒有進版控，也沒有在未核准 hostname 上部署。
- [ ] Dependabot 沒有 open medium/high/critical 警示，npm token 距離到期超過 14 天；
      Python、npm、Rust、Go、.NET 與 Maven 的本機安全檢查全部通過。
- [ ] manifest 的 base SHA、base tree、candidate tree、release/build version 正確。
- [ ] manifest schema、build pipeline SHA 與 toolchain 證據 checksum 正確。
- [ ] verify 使用同一 build、`VERIFY_SUITE=all`，並封存 release-eligible receipt。
- [ ] verify 的 SDK matrix 在獨立 Python 環境重跑 public docs check 與 strict site build。
- [ ] receipt 的 build、SHA、tree、版本、pipeline SHA、manifest/checksum 與驗證證據 hash
      都和候選完全相同。
- [ ] preview 使用同一組 build/verify，且沒有新增 tag、Release 或 registry version。
- [ ] 所有 job 都 detached 啟動並用 Jenkins UI/API 監看，沒有使用 `jcli -s -v`。

## Credential 預檢

```bash
jcli build zhtw/release \
  -p BUILD_NUMBER=<同一-build> -p VERIFY_BUILD_NUMBER=<同一-verify> \
  -p RELEASE_ACTION=CREDENTIAL_PREFLIGHT \
  -p SKIP_CONFIRMATION=false
```

- [ ] GitHub API/SSH、PyPI、npm x2、crates.io、NuGet、Maven Central 與 GPG 全部通過。
- [ ] 預檢沒有建立 tag、Release、registry version 或 Homebrew commit。

## 正式發布

```bash
jcli build zhtw/release \
  -p BUILD_NUMBER=<同一-build> -p VERIFY_BUILD_NUMBER=<同一-verify> \
  -p RELEASE_ACTION=PUBLISH_ALL \
  -p APPROVAL_REFERENCE='<目前對話或變更單參照>' \
  -p SKIP_CONFIRMATION=true
```

- [ ] 相依套件閘門在 24 小時內、`all` 驗證在 7 天內完成。
- [ ] Jenkins 已將 build、verify 與本次 release 標記永久保留。
- [ ] 雙 tag 指向同一個 candidate release commit。
- [ ] GitHub root/Go Release 的 tag、標題、notes、draft/prerelease 狀態完全正確；root 是
      Latest，且五個 Go 檔案與 checksum 完整。
- [ ] PyPI、npm x2、crates.io、NuGet、Maven Central、Go proxy 都可見。
- [ ] Homebrew formula 指向同一版本 PyPI sdist 與正確 SHA-256。
- [ ] Jenkins 最後 12/12 公開檢查通過。
- [ ] 公開 registry 內容與 Jenkins 封存 payload 相符；NuGet 僅忽略 registry 簽章 wrapper。

## 部分失敗

- [ ] 使用同一組 build/verify 執行 `RESUME_ALL`；已成功且內容完全相同的項目必須跳過。
- [ ] `RESUME_ALL` 從第一個未完成 registry 接續，並在最後跑完整 12/12 公開驗證。
- [ ] 不刪除、不移動 tag，不覆蓋已存在的 registry version。
- [ ] 若內容本身有錯，修正後升下一個 patch，不重用版號。
- [ ] Maven 若已有 deployment ID，使用 `RESUME_ALL` 加該 ID 續查，不重複上傳。
- [ ] 單項 `RETRY_*` 完成後仍執行 `RESUME_ALL`，補完後續 registry 與最終驗證。
- [ ] Recovery action 使用同一份已保留候選；即使超過 freshness 期限，也沒有重建或
      重用版號，且提供新的 `APPROVAL_REFERENCE`。
