# CLI 與檔案

## 核心命令

| 命令 | 用途 | 是否修改資料 |
|---|---|---|
| `zhtw check PATH` | 掃描單檔或目錄並回報差異 | 否 |
| `zhtw fix PATH` | 轉換並寫回檔案 | 是 |
| `zhtw lookup TEXT` | 查詢詞彙轉換與來源 | 否 |
| `zhtw explain TEXT` | 回傳結果與每個規則事件 | 否 |
| `zhtw stats` | 顯示規則與字元對映統計 | 否 |
| `zhtw validate` | 驗證正式詞庫 | 否 |

用 `zhtw COMMAND --help` 取得目前版本的完整參數；文件不另外複製整份 help，以免兩邊漂移。

## 常用安全選項

```bash
zhtw check ./src --source cn --json
zhtw fix ./src --source cn --dry-run
zhtw fix ./src --source cn --show-diff
zhtw fix ./src --source cn --backup
zhtw check ./src --exclude node_modules,dist
```

- `--source cn` 只處理簡體來源；`hk` 只處理香港繁體；預設為 `cn,hk`。
- `--ambiguity-mode strict` 是保守預設；`balanced` 會為少量高信心歧義字套用預設規則。
- `--no-char-convert` 關閉字元層，只使用詞彙規則。
- `--json` 控制 CLI 報告格式，不會自動啟用 JSON 結構化處理。

## JSON 檔

一般 `check` 與 `fix` 把內容視為文字。若要保留 key、數字表示與格式，只轉換 string value，必須明確加上 `--adapter json`：

```bash
zhtw check ./locales --adapter json --source cn
zhtw fix ./locales --adapter json --source cn --show-diff
```

詳細失敗與寫檔規則請看 [JSON adapter](../reference/json-adapter.md)。

## 忽略內容

專案根目錄的 `.zhtwignore` 使用類似 `.gitignore` 的目錄與 glob 規則。原始碼內也可用 `zhtw:disable-next`、`zhtw:disable` 與 `zhtw:enable` 保護不該轉換的區塊。

Big5、GBK、GB2312、GB18030 與 UTF-8 的進階選項，以及自訂詞庫格式，仍整理在 [repo 內的 CLI 進階文件](https://github.com/rajatim/zhtw/blob/main/docs/guides/CLI-ADVANCED.md)。
