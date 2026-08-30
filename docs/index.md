# ZHTW 公開文件

ZHTW 是一套保守的簡體中文、香港繁體轉台灣繁體中文工具。它優先避免錯轉，適合程式碼、語系檔、文件與自動化流程。

目前正式版本是 **4.5.0**。同一份規則資料提供 Python CLI、Python、Java、TypeScript、Rust、Go、.NET 與 Browser WebAssembly 使用。

## 先從哪裡開始

- 第一次使用：看[五分鐘開始](guides/getting-started.md)。
- 要掃描或修正檔案：看 [CLI 與檔案](guides/cli-and-files.md)。
- 要整合應用程式或瀏覽器：看 [SDK 與 Browser WASM](guides/sdk-and-browser.md)。
- 想知道為什麼某個詞有轉或沒轉：看 [Explain API](reference/explain-api.md)。
- 要核對精準度主張：看[品質與證據](testing/quality-and-evidence.md)。

## 設計原則

ZHTW 不使用 OpenCC 作為執行期依賴，也不假設每個簡體字都只有一個繁體答案。轉換順序是詞彙規則、identity protection（原文保護）、選用的 balanced mode，最後才是安全的一對一字元對映。

完整邊界請看[轉換行為與限制](reference/conversion-behavior.md)。

## 公開與內部文件邊界

這裡是產品行為、公開 API、品質證據與版本資訊的真相來源。內部 Jenkins 工作編號、憑證、核准紀錄與復原操作不屬於公開產品契約，也不會寫在這個網站。
