# SDKs and Browser WASM

Every runtime reads the same version of the shared data. Releases use mono-versioning: Python, Java, TypeScript, Rust, Go, .NET, and WebAssembly versions must match.

## Choose a package

| Environment | Install | Detailed guide |
|---|---|---|
| Python | `pip install zhtw` | [README](https://github.com/rajatim/zhtw/blob/main/README.en.md#python) |
| Java | Maven Central: `com.rajatim:zhtw` | [Java README](https://github.com/rajatim/zhtw/blob/main/sdk/java/README.md) |
| Node.js and TypeScript | `npm install zhtw-js` | [TypeScript README](https://github.com/rajatim/zhtw/blob/main/sdk/typescript/README.md) |
| Rust | `cargo add zhtw` | [Rust README](https://github.com/rajatim/zhtw/blob/main/sdk/rust/zhtw/README.md) |
| Go | `go get github.com/rajatim/zhtw/sdk/go` | [Go README](https://github.com/rajatim/zhtw/blob/main/sdk/go/README.md) |
| .NET | `dotnet add package Zhtw` | [.NET README](https://github.com/rajatim/zhtw/blob/main/sdk/dotnet/README.md) |
| Modern browsers | `npm install zhtw-wasm` | [WASM README](https://github.com/rajatim/zhtw/blob/main/sdk/rust/zhtw-wasm/README.md) |

## What Browser WASM means

Browser WASM compiles the Rust converter to WebAssembly so JavaScript can run it inside a browser. User text does not need to go to a backend. It works well for offline tools, content previews, and privacy-focused frontends.

It is not a separate dictionary or a network API. `zhtw-wasm` uses the same golden fixtures and versioned data as the other SDKs. Your app bundler must still load the package, and browser or CSP settings may affect loading.

```javascript
import init, { convert, explain } from "zhtw-wasm";

await init();
console.log(convert("这个软件"));
console.log(explain("软件"));
```

## Features and verification

Public names follow each language style, but the main features match: `convert`, `check`, `lookup`, JSON string-value conversion, and `explain`. Every release candidate runs SDK tests, shared golden data, package tests, and version checks.

Use `zhtw-js` for Node.js. Use `zhtw-wasm` when conversion must run inside the browser.
