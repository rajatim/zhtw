# C# (.NET) SDK Design Spec

> **Status:** Approved | **Date:** 2026-04-11

## Goal

Implement a fully-featured .NET SDK for zhtw that provides Convert, Check, and Lookup APIs, matching the API surface and conversion behavior of the existing 5 language SDKs. Targets `netstandard2.0` + `net8.0` (multi-target) for maximum compatibility across .NET Framework 4.7.2+, .NET Core, .NET 5+, Mono, and Unity.

## Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Target framework | Multi-target `netstandard2.0` + `net8.0` | Legacy systems (ASP.NET, WinForms, batch jobs, Unity) are a key audience for text conversion tools |
| JSON parser | `System.Text.Json` | NuGet package for netstandard2.0, built-in for net8.0 |
| AC automaton | Self-implemented | All other SDKs self-implement; zero external dependencies; ~100-150 lines |
| NuGet publish | Deferred | Build + test CI first; publish workflow added later |
| External dependencies | Zero runtime deps (except `System.Text.Json` package ref for netstandard2.0) | Matches the minimal-dependency pattern of other SDKs |

## Public API

### Static convenience methods (default instance)

```csharp
namespace Zhtw;

public static class ZhtwConvert
{
    public static string Convert(string text);
    public static IReadOnlyList<Match> Check(string text);
    public static LookupResult Lookup(string word);
    public static string DataVersion { get; }
}
```

The default instance uses `Sources = { Cn, Hk }`, `AmbiguityMode = Strict`, no custom dict. Thread-safe via `Lazy<Converter>`.

### Builder

```csharp
public class ConverterBuilder
{
    public ConverterBuilder Sources(params Source[] sources);
    public ConverterBuilder AmbiguityMode(AmbiguityMode mode);
    public ConverterBuilder CustomDict(IReadOnlyDictionary<string, string> dict);
    public Converter Build();  // throws ArgumentException if sources is empty
}
```

### Converter instance

```csharp
public class Converter
{
    public string Convert(string text);
    public IReadOnlyList<Match> Check(string text);
    public LookupResult Lookup(string word);
}
```

### Types

```csharp
public enum Source { Cn, Hk }
public enum AmbiguityMode { Strict, Balanced }

public sealed class Match
{
    public int Start { get; }    // codepoint index, inclusive
    public int End { get; }      // codepoint index, exclusive
    public string Source { get; } // original simplified text
    public string Target { get; } // converted traditional text
}

public sealed class LookupResult
{
    public string Input { get; }
    public string Output { get; }
    public bool Changed { get; }
    public IReadOnlyList<ConversionDetail> Details { get; }
}

public sealed class ConversionDetail
{
    public string Source { get; }
    public string Target { get; }
    public string Layer { get; }    // "term" or "char"
    public int Position { get; }    // codepoint index
}
```

## Conversion Algorithm

Three-layer model, identical to all other SDKs:

1. **Term layer** — Aho-Corasick automaton matches multi-character terms. Sources selected by `Sources` parameter (`terms.cn`, `terms.hk`). Matched targets inserted verbatim — NOT post-processed by charmap.
2. **Balanced defaults layer** — Enabled only when `AmbiguityMode == Balanced` AND sources contain `Cn`. For each codepoint NOT covered by AC matches, check `charmap.balanced_defaults`.
3. **Char layer** — Enabled only when sources contain `Cn`. For each codepoint NOT covered by layers 1-2, check `charmap.chars`.

A position is "covered" if it falls within any AC match span (including identity mappings). Covered positions skip layers 2 and 3.

### Position indexing

All public API positions use **Unicode codepoint indices**, not .NET's UTF-16 code unit indices. The `CodepointHelper` class handles conversion. This matters for text containing characters outside the BMP (supplementary plane), where a single codepoint = two UTF-16 chars (surrogate pair).

## Data Loading

- `zhtw-data.json` embedded as assembly resource via `<EmbeddedResource>` in `.csproj`
- Parsed with `System.Text.Json` into internal data structures
- Default instance initialized via `Lazy<Converter>` (thread-safe, one-time)
- Each `Build()` call constructs a new AC automaton (merging term sources + custom dict)

### Data schema (from `zhtw-data.json`)

```json
{
  "version": "4.2.1",
  "charmap": {
    "chars": { "simplified_char": "traditional_char", ... },
    "ambiguous": ["char1", "char2", ...],
    "balanced_defaults": { "char": "default_traditional", ... }
  },
  "terms": {
    "cn": { "simplified_term": "traditional_term", ... },
    "hk": { "simplified_term": "traditional_term", ... }
  }
}
```

## File Layout

```
sdk/dotnet/
├── Zhtw.csproj                    # multi-target netstandard2.0 + net8.0
├── src/
│   ├── AhoCorasick.cs             # AC automaton (build + search)
│   ├── Converter.cs               # three-layer conversion + Check + Lookup
│   ├── ConverterBuilder.cs        # fluent builder
│   ├── ZhtwConvert.cs             # static convenience API + Lazy default
│   ├── ZhtwData.cs                # embedded resource loader + JSON parsing
│   ├── Types.cs                   # Source, AmbiguityMode, Match, LookupResult, ConversionDetail
│   └── CodepointHelper.cs         # UTF-16 ↔ codepoint index conversion
├── tests/
│   └── Zhtw.Tests/
│       ├── Zhtw.Tests.csproj      # xUnit test project, targets net8.0
│       ├── GoldenTests.cs         # golden-test.json driven tests
│       ├── ConverterTests.cs      # builder, custom dict, ambiguity mode, edge cases
│       └── AhoCorasickTests.cs    # AC automaton unit tests
```

## CI Workflow

Update `.github/workflows/sdk-dotnet.yml`:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
        with:
          dotnet-version: '8.0.x'
      - name: Build
        working-directory: sdk/dotnet
        run: dotnet build -c Release
      - name: Test
        working-directory: sdk/dotnet
        run: dotnet test -c Release --logger "console;verbosity=detailed"
```

Test project targets `net8.0` and tests both targets via the library's multi-target build. No publish job for now.

## Error Handling

| Scenario | Behavior |
|----------|----------|
| `Build()` with empty sources | `ArgumentException` |
| Embedded resource missing | `InvalidOperationException` (should never happen in normal use) |
| Null/empty text input | Return input unchanged (no exception) |

## Testing Strategy

1. **Golden tests** (`GoldenTests.cs`) — Load `sdk/data/golden-test.json`, run all convert/check/lookup cases. This is the primary correctness gate — if golden tests pass, the SDK matches all other SDKs.
2. **Builder tests** (`ConverterTests.cs`) — Custom sources, custom dict, ambiguity modes, empty sources error.
3. **AC unit tests** (`AhoCorasickTests.cs`) — Pattern matching, overlapping patterns, CJK characters, empty input.

## Not In Scope

- NuGet publishing workflow (deferred)
- net8.0-specific optimizations (future — `Span<T>`, source generators)
- XML doc comments for IntelliSense (can add later)
- .NET AOT / trimming annotations (future)
