# 五分鐘開始

## 安裝 CLI

需要 Python 3.10 以上版本：

```bash
python3 -m pip install zhtw
zhtw --version
```

## 轉換第一段文字

<!-- zhtw:disable -->
```bash
echo "这个软件需要网络连接" | zhtw explain --source cn
```
<!-- zhtw:enable -->

`explain` 會顯示轉換結果和套用的規則。只需要程式中的結果時，可以用 Python API：

<!-- zhtw:disable -->
```python
from zhtw import convert

assert convert("这个软件", sources=["cn"]) == "這個軟體"
```
<!-- zhtw:enable -->

## 先檢查，再修改

```bash
zhtw check ./locales --source cn
zhtw fix ./locales --source cn --dry-run
zhtw fix ./locales --source cn --show-diff
```

`check` 不修改檔案。`fix --dry-run` 模擬寫入，`--show-diff` 先顯示差異再詢問。正式自動寫入前，請把來源檔納入版本控制或備份。

## 選擇使用方式

| 情境 | 建議 |
|---|---|
| 掃描 repo 或語系目錄 | Python CLI |
| Python 程式內轉換 | `zhtw` Python package |
| Java、Node.js、Rust、Go、.NET | 對應原生 SDK |
| 不想在網頁後端傳送文字 | `zhtw-wasm` Browser WebAssembly |
| JSON 語系檔 | 明確啟用 [JSON adapter](../reference/json-adapter.md) |

下一步請看 [CLI 與檔案](cli-and-files.md) 或 [SDK 與 Browser WASM](sdk-and-browser.md)。
