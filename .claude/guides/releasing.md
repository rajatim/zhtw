# ZHTW 版本發布 SOP

本文件不再維護獨立流程，以免發布規則分歧。請使用以下兩個規範入口：

- 執行流程與自動化閘門：[`../rules/releasing.md`](../rules/releasing.md)
- 每版人工核對項目：[`../../docs/releases/RELEASE-CHECKLIST.md`](../../docs/releases/RELEASE-CHECKLIST.md)

正式發布一律使用：

```bash
make release-dry VERSION=X.Y.Z
make release VERSION=X.Y.Z
make release-verify VERSION=X.Y.Z
```

沒有 Maintainer 明確同意，不可執行正式發布。
