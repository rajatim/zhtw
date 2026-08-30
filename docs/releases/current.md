# 目前版本

目前版本：**4.5.0**（2026-08-30）。

## 4.5.0 重點

- 新增明確啟用的 JSON string value adapter，保留 object key、結構與未改內容。
- 新增 `explain` CLI 與跨 SDK API，回傳穩定規則 ID、span、layer、outcome 與 reason code。
- 新增 rule schema v2 metadata、穩定 ID 與人工 review lifecycle。
- 擴充 Unicode 17.0 漢字驗證與安全的中英數混合技術詞匯入。
- 強化 Jenkins-only 候選、驗證、供應鏈稽核、封裝 smoke test 與中斷後續跑。

完整修正與安全更新請看 [4.5.0 CHANGELOG](https://github.com/rajatim/zhtw/blob/main/CHANGELOG.md#450---2026-08-30)。

## 相容性

- Python：3.10～3.13。
- Java：11 以上；候選版本以 11、17、21 驗證。
- Node.js：20 以上；候選版本以 20、22 驗證。
- Rust：最低支援 toolchain 1.80.1，並驗證 stable。
- .NET：`netstandard2.0` 與 `net8.0`。
- Go 與 Browser WASM 的實際需求以各套件 README 為準。

所有 SDK 使用同一個版本。升級時不要混用不同版本的 runtime 與 shared data。

## 公開發布證據

公開 registry、GitHub tag、release notes 與 checksum 必須對應同一個候選內容。registry 接受版本後不會重用或覆寫；若內容需要修正，會發布下一個 patch 版本。

內部 Jenkins 收據與憑證操作不屬於公開 API。使用者可從 [GitHub Releases](https://github.com/rajatim/zhtw/releases) 與各套件 registry 核對正式成品。
