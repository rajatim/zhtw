# 釋出核對清單

> zhtw 只透過 Jenkins 建置、驗證與發布。完整規則：`.claude/rules/releasing.md`。

## 釋出前人工判斷

- [ ] 使用者／Maintainer 明確同意要發布的確切 Jenkins build。
- [ ] CHANGELOG `[Unreleased]` 能讓使用者判斷是否值得升級。
- [ ] 版號符合語意：breaking → major、新功能 → minor、修復 → patch。
- [ ] 詞庫有改動時，精準度 release gate 與治理證據均已完成。
- [ ] 已接受目前 Jenkins 沒有 macOS／Windows 原生 agent 的限制。

## 候選與唯讀預演

```bash
jcli build zhtw/build -s -v -p BRANCH=main -p VERSION_BUMP=patch
jcli build zhtw/release -s -v \
  -p BUILD_NUMBER=<成功-build> -p RELEASE_ACTION=PREVIEW \
  -p SKIP_CONFIRMATION=false
```

- [ ] build 的 lint、release gate、全部套件建置與 checksum 都成功。
- [ ] manifest 的 base SHA、base tree、candidate tree、release/build version 正確。
- [ ] preview 使用同一 build，且沒有新增 tag、Release 或 registry version。

## 正式發布

```bash
jcli build zhtw/release -s -v \
  -p BUILD_NUMBER=<同一-build> -p RELEASE_ACTION=PUBLISH_ALL \
  -p SKIP_CONFIRMATION=true
```

- [ ] 雙 tag 指向同一個 candidate release commit。
- [ ] GitHub root/Go Release 與五個 Go 檔案、checksum 完整。
- [ ] PyPI、npm x2、crates.io、NuGet、Maven Central、Go proxy 都可見。
- [ ] Homebrew formula 指向同一版本 PyPI sdist 與正確 SHA-256。
- [ ] Jenkins 最後 12/12 公開檢查通過。

## 部分失敗

- [ ] 使用同一 build 重跑 `PUBLISH_ALL`，或使用正確的 `RETRY_*`。
- [ ] 不刪除、不移動 tag，不覆蓋已存在的 registry version。
- [ ] 若內容本身有錯，修正後升下一個 patch，不重用版號。
