# zhtw 公開文件 Hosting

正式網址為 `https://zhtw.rajatim.com`。月臺使用私有 S3 origin、CloudFront OAC、
ACM 與 Route 53，不使用 Hub，也不得更改 `rajatim.wiki` 的 IP 白名單。

## 基礎設施

- Stack：`zhtw-public-docs`
- Region：`us-east-1`（CloudFront 自訂網域的 ACM certificate 必須在此區域）
- Bucket：`rajatim-zhtw-docs-381083412708-use1`
- IAM user：`zhtw-docs-publisher`
- Jenkins jobs：`zhtw/docs-build`、`zhtw/docs-publish`

CloudFormation 不建立 access key。Stack change set 先由 operator 預覽，取得精確核准後
才可執行。Access key 建立後只進 `zhtw/` folder-scoped Jenkins Credential；1Password
若有副本也只作備份，所有 Jenkins runtime 都不得呼叫 `op`。

## 內容配置

| Prefix | 用途 |
|---|---|
| `releases/<source-sha>/` | 完整、不可變的 MkDocs 成品 |
| `current/` | CloudFront origin 目前讀取的版本 |
| `deploy-state/` | 目前與歷史 release manifest，不含 secret |

S3 Block Public Access 必須四項全開。匿名 S3 object URL 應回 403；只有 CloudFront
distribution 能透過 OAC 讀 `current/`。

## 驗證與回復

`docs-publish` 預設為 `PREVIEW`。`CREDENTIAL_PREFLIGHT` 只驗證 AWS identity 與最小
權限；`DEPLOY` 和 `ROLLBACK` 必須指定成功的 `docs-build`，並通過 Jenkins 確認閘門。

部署先上傳 `releases/<source-sha>/` 並核對 checksum，才更新 `current/`。若 live switch
後驗證失敗，adapter 會從本次 deployment state 中的前一個精確 source SHA 回復並重新
建立 CloudFront invalidation。不得用 wildcard 刪 bucket、distribution、certificate、
IAM user 或 Route 53 zone。
