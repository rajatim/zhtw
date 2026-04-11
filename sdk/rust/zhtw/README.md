# zhtw

> Traditional Chinese converter for Taiwan — Rust SDK

Simplified Chinese / HK Traditional to Taiwan Traditional Chinese converter. Build-time precompiled `daachorse` automaton + `phf` char map for zero runtime construction cost. Byte-for-byte compatible with the Python CLI and all other SDKs.

## Install

<!-- zhtw:disable -->
```toml
[dependencies]
zhtw = "4.3.0"
```
<!-- zhtw:enable -->

## Quick start

<!-- zhtw:disable -->
```rust
// Zero config
assert_eq!(zhtw::convert("这个软件需要优化"), "這個軟體需要最佳化");
```
<!-- zhtw:enable -->

## Builder API

<!-- zhtw:disable -->
```rust
use zhtw::{AmbiguityMode, Converter, Source};

let conv = Converter::builder()
    .sources([Source::Cn])
    .custom_dict([("自定义", "自訂")])
    .ambiguity_mode(AmbiguityMode::Balanced)
    .build()
    .expect("non-empty sources");

conv.convert("自定义几个里程碑");
```
<!-- zhtw:enable -->

## API

| Function | Description |
|----------|-------------|
| `convert(text)` | Convert text (uses default converter) |
| `check(text)` | Return replacements without modifying |
| `lookup(word)` | Look up a single word |
| `Converter::builder()` | Custom converter with builder pattern |

## Performance

Build-time precompiled automaton — runtime is pure matching with zero initialization overhead. Run `cargo bench -p zhtw` for benchmarks.

## Requirements

- Rust 1.80+ (MSRV)
- Zero runtime dependencies beyond `daachorse` and `phf`

## Links

- [Main README](../../../README.md) | [CHANGELOG](../../../CHANGELOG.md) | [crates.io](https://crates.io/crates/zhtw)

## License

MIT
