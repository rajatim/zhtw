# JSON adapter 參考

> 4.5.0 開發中。JSON adapter 必須由呼叫端明確啟用；一般文字轉換的預設行為不變。

## 用途

JSON adapter 只轉換 JSON 裡的字串 value，不轉換 object key。它適合設定檔、語系檔與
API fixture，讓中文內容可以轉換，同時保留原本的結構與無關格式。

<!-- zhtw:disable -->
```json
{
  "软件 key": "这个软件",
  "number": 1.00e+02
}
```
<!-- zhtw:enable -->

轉換後只有 value 會改變：

```json
{
  "軟體 key": "這個軟體",
  "number": 1.00e+02
}
```

## Python API

<!-- zhtw:disable -->
```python
from zhtw import convert_json

output = convert_json('{"软件":"这个软件","number":1}', sources=["cn"])
assert output == '{"软件":"這個軟體","number":1}'
```
<!-- zhtw:enable -->

`convert_json()` 接受完整 JSON 字串並回傳轉換後的 JSON 字串。輸入不合法或含有重複
object key 時會丟出 `JsonAdapterError`，不會回傳部分結果。

## CLI

<!-- zhtw:disable -->
```bash
# 只檢查 JSON string value，不修改檔案
zhtw check ./locales --adapter json --source cn

# 原子寫回 JSON 檔
zhtw fix ./locales --adapter json --source cn --show-diff
```
<!-- zhtw:enable -->

目錄模式只處理 `.json`；單檔模式也要求 `.json` 副檔名。`--adapter json` 和 `--json`
用途不同：前者決定輸入的解析方式，後者只控制 CLI 報告格式。

## 位元組保留規則

- 先用正式 JSON parser 驗證完整文件，再掃描 token span。
- object key、空白、縮排、換行、數字表示、布林值、`null`、結構與 array 順序不變。
- 沒有轉換的 string value 保留原始 escape 寫法與全部位元組。
- 有轉換的 string value 才重新輸出；固定使用 compact JSON escaping、直接保留 Unicode
  字元，並只 escape JSON 必須處理的引號、反斜線與控制字元。
- 轉換後會再次解析，確認 key 與非字串 value 結構沒有改變。
- duplicate key 一律 fail closed（安全失敗），包含 escape 後才相同的 key，例如 `key`
  與 `\u006bey`。
- `NaN`、`Infinity`、trailing comma 等非標準或無效 JSON 一律拒絕。

## 寫檔安全

CLI 修正時會在原檔同一個目錄建立暫存檔，完成 encode、flush 與 `fsync` 後才 atomic
replace（原子替換）原檔。parse、convert、encode、verify 或 write 任一步驟失敗時，
命令會回傳非零狀態，原檔保持不變。唯讀檔也會直接拒絕，不會嘗試繞過權限。

跨 SDK 的 exact-byte 案例放在 `sdk/data/json-adapter-golden.json`。每個實作都必須使用
同一份輸入與 expected，不得各自改寫測試答案。
