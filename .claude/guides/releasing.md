# 發布快速索引

- AI 規則：[`../rules/releasing.md`](../rules/releasing.md)
- 人工核對：[`../../docs/releases/RELEASE-CHECKLIST.md`](../../docs/releases/RELEASE-CHECKLIST.md)
- 唯一入口：Jenkins `zhtw/build`、`zhtw/release`、`zhtw/verify`

```bash
jcli build zhtw/build -s -v -p BRANCH=main -p VERSION_BUMP=patch
jcli build zhtw/release -s -v \
  -p BUILD_NUMBER=<build> -p RELEASE_ACTION=PREVIEW \
  -p SKIP_CONFIRMATION=false
```

沒有使用者明確核准，不可把 `PREVIEW` 改為 `PUBLISH_ALL`。不可使用 GitHub
Actions、手動 tag 或本機 registry publish 當備援。
