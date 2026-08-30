# SDK 與 Browser WASM

所有 runtime 都讀同版本的 shared data，正式發版採 mono-versioning：Python、Java、TypeScript、Rust、Go、.NET 與 WebAssembly 的版本必須一致。

## 套件選擇

| 環境 | 安裝 | 詳細文件 |
|---|---|---|
| Python | `pip install zhtw` | [README](https://github.com/rajatim/zhtw#python) |
| Java | Maven Central：`com.rajatim:zhtw` | [Java README](https://github.com/rajatim/zhtw/blob/main/sdk/java/README.md) |
| Node.js／TypeScript | `npm install zhtw-js` | [TypeScript README](https://github.com/rajatim/zhtw/blob/main/sdk/typescript/README.md) |
| Rust | `cargo add zhtw` | [Rust README](https://github.com/rajatim/zhtw/blob/main/sdk/rust/zhtw/README.md) |
| Go | `go get github.com/rajatim/zhtw/sdk/go` | [Go README](https://github.com/rajatim/zhtw/blob/main/sdk/go/README.md) |
| .NET | `dotnet add package Zhtw` | [.NET README](https://github.com/rajatim/zhtw/blob/main/sdk/dotnet/README.md) |
| 現代瀏覽器 | `npm install zhtw-wasm` | [WASM README](https://github.com/rajatim/zhtw/blob/main/sdk/rust/zhtw-wasm/README.md) |

## Browser WASM 是什麼

Browser WASM 是把 Rust 版轉換器編譯成 WebAssembly，讓 JavaScript 在瀏覽器裡直接執行。使用者輸入不必送到後端，適合離線工具、內容預覽與重視隱私的前端功能。

它不是另一套詞庫，也不是網路 API。`zhtw-wasm` 使用和其他 SDK 相同的 golden fixtures 與版本化資料；套件仍需由應用程式 bundler 載入，並受瀏覽器與 CSP 設定影響。

<!-- zhtw:disable -->
```javascript
import init, { convert, explain } from "zhtw-wasm";

await init();
console.log(convert("这个软件"));
console.log(explain("软件"));
```
<!-- zhtw:enable -->

## 能力與驗證

各 SDK 的公開命名會配合語言習慣，但核心能力對齊：`convert`、`check`、`lookup`、JSON string value conversion 與 `explain`。每次候選版本會執行各 SDK 測試、共用 golden data、封裝測試與版本一致性檢查。

若你只要在 Node.js 使用，選 `zhtw-js`；若程式必須在瀏覽器本機執行，選 `zhtw-wasm`。
