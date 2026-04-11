# zhtw (Go SDK)

> Traditional Chinese converter for Taiwan — Go SDK

Simplified Chinese / HK Traditional to Taiwan Traditional Chinese converter. `go:embed` dictionary, zero external dependencies, goroutine-safe. Byte-for-byte compatible with the Python CLI and all other SDKs.

## Install

<!-- zhtw:disable -->
```bash
go get github.com/rajatim/zhtw/sdk/go/v4@latest
```
<!-- zhtw:enable -->

## Quick start

<!-- zhtw:disable -->
```go
package main

import (
    "fmt"
    "github.com/rajatim/zhtw/sdk/go/v4/zhtw"
)

func main() {
    fmt.Println(zhtw.Convert("这个软件需要优化"))
    // => "這個軟體需要最佳化"
}
```
<!-- zhtw:enable -->

## Builder API

<!-- zhtw:disable -->
```go
conv, _ := zhtw.NewBuilder().
    Sources(zhtw.SourceCn).
    CustomDict(map[string]string{"自定义": "自訂"}).
    SetAmbiguityMode(zhtw.AmbiguityBalanced).
    Build()

conv.Convert("自定义几个里程碑")
```
<!-- zhtw:enable -->

## Standalone binary

Pre-built binaries available on [GitHub Releases](https://github.com/rajatim/zhtw/releases) — no Go toolchain required:

<!-- zhtw:disable -->
```bash
# macOS arm64
curl -sL https://github.com/rajatim/zhtw/releases/download/sdk%2Fgo%2Fv4.3.0/zhtw-darwin-arm64.tar.gz | tar xz
./zhtw convert "软件测试"

# Or via go install
go install github.com/rajatim/zhtw/sdk/go/v4/cmd/zhtw@latest
```
<!-- zhtw:enable -->

## API

| Function | Description |
|----------|-------------|
| `Convert(text)` | Convert text (uses default converter) |
| `Check(text)` | Return replacements without modifying |
| `Lookup(word)` | Look up a single word |
| `NewBuilder()` | Custom converter with builder pattern |

## Requirements

- Go 1.21+
- Zero external dependencies

## Links

- [Main README](../../README.md) | [CHANGELOG](../../CHANGELOG.md) | [pkg.go.dev](https://pkg.go.dev/github.com/rajatim/zhtw/sdk/go/v4/zhtw)

## License

MIT
