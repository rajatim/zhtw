# Zhtw (.NET SDK)

> Traditional Chinese converter for Taiwan — C# (.NET) SDK

Simplified Chinese / HK Traditional to Taiwan Traditional Chinese converter. Multi-target `netstandard2.0` + `net8.0`, embedded resource dictionary, zero external dependencies on net8.0+. Byte-for-byte compatible with the Python CLI and all other SDKs.

## Install

<!-- zhtw:disable -->
```bash
dotnet add package Zhtw
```
<!-- zhtw:enable -->

## Quick start

<!-- zhtw:disable -->
```csharp
using Zhtw;

// Thread-safe singleton, zero config
string result = ZhtwConvert.Convert("这个软件需要优化");
// => "這個軟體需要最佳化"
```
<!-- zhtw:enable -->

## Builder API

<!-- zhtw:disable -->
```csharp
var conv = new ConverterBuilder()
    .Sources(Source.Cn, Source.Hk)
    .CustomDict(new Dictionary<string, string> { ["自定义"] = "自訂" })
    .AmbiguityMode(AmbiguityMode.Balanced)
    .Build();

conv.Convert("自定义几个里程碑");
```
<!-- zhtw:enable -->

## API

| Method | Description |
|--------|-------------|
| `ZhtwConvert.Convert(text)` | Convert text (static, uses default converter) |
| `ZhtwConvert.Check(text)` | Return replacements without modifying |
| `ZhtwConvert.Lookup(word)` | Look up a single word |
| `ConverterBuilder` | Custom converter with builder pattern |

## Requirements

- .NET Standard 2.0+ / .NET 8.0+
- Zero external dependencies (net8.0)

## Links

- [Main README](../../README.md) | [CHANGELOG](../../CHANGELOG.md) | [NuGet](https://www.nuget.org/packages/Zhtw)

## License

MIT
