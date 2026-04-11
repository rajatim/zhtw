<!-- zhtw:disable -->
# Go CLI Binary — Design Spec

> **Status:** Draft  
> **Date:** 2026-04-11  
> **Depends on:** Go SDK v4 (`sdk/go/zhtw/`, released v4.2.0)

## Goal

Provide a standalone `zhtw` binary — no Python runtime required — for CI pipelines, shell integration, and environments where installing Python is impractical. This is a **second CLI runtime**, not a sixth language SDK.

## Positioning

| | Python CLI | Go CLI Binary |
|---|-----------|---------------|
| **Runtime** | Python 3.10+ | None (static binary) |
| **Install** | `pip install zhtw` / `brew install` | `go install` / GitHub Release binary |
| **Scope** | Full: check, fix, lookup, stats, validate | MVP: convert, lookup, version |
| **Use case** | Development, pre-commit, data pipelines | CI, pipeline, shell, Docker |

The Go CLI is **not** a port of the Python CLI. It is a minimal text-processing tool built on the Go SDK library. Features like file scanning (`check`), auto-fix (`fix`), encoding detection, and `.zhtwignore` are explicitly out of scope for this version.

---

## Architecture

### Directory Structure

```
sdk/go/
├── go.mod                    # Shared module: github.com/rajatim/zhtw/sdk/go/v4
├── cmd/
│   └── zhtw/
│       └── main.go           # CLI entry point (single file)
└── zhtw/                     # Existing library (unchanged)
    ├── builder.go
    ├── converter.go
    ├── data.go
    ├── matcher.go
    ├── types.go
    ├── zhtw.go
    └── zhtw-data.json
```

### Key Constraints

- **Same `go.mod`:** CLI lives in the same module as the library. No separate module, no extra release tag.
- **Zero external dependencies:** Only stdlib (`flag`, `os`, `io`, `encoding/json`, `fmt`, `bufio`, `strings`, `runtime/debug`). No cobra, no pflag.
- **Library-first:** CLI calls Go SDK public API only (`zhtw.NewBuilder()`, `converter.Convert()`, `converter.Lookup()`). Zero conversion logic in the CLI layer.

---

## Subcommands

```
zhtw convert [TEXT...]        Convert text from simplified to traditional
zhtw lookup  [WORD...]        Query conversion details for words/phrases
zhtw version                  Print version information
```

Unknown subcommand or no subcommand → print usage + exit 2.

### Subcommand Parsing

Manual `os.Args[1]` switch with per-subcommand `flag.FlagSet`:

```go
if len(os.Args) < 2 {
    printUsage()
    os.Exit(2)
}
switch os.Args[1] {
case "convert":
    // flag.NewFlagSet("convert", flag.ExitOnError)
case "lookup":
    // flag.NewFlagSet("lookup", flag.ExitOnError)
case "version":
    // print version info
default:
    printUsage()
    os.Exit(2)
}
```

---

## Flags

### Shared Flags (on both `convert` and `lookup` FlagSets)

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--sources` | string | `"cn,hk"` | Comma-separated: `cn`, `hk`, `cn,hk` |
| `--ambiguity-mode` | string | `"strict"` | `strict` or `balanced` |
| `--json` | bool | false | JSON output |
| `--file` | string | `""` | Read input from file |

### convert-only Flag

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--check` | bool | false | Exit 1 if input was changed (for CI) |

### Flags NOT in MVP

- `--dict` (custom dictionary)
- `--encoding` / `--output-encoding`
- `--verbose`
- `--exclude`
- `--dry-run` / `--backup`

---

## Input Semantics

Input handling differs by subcommand:

### `convert`

All input is treated as **one text block**.

| Source | Behavior |
|--------|----------|
| `--file path` | Read entire file as one text |
| Positional args | Join with space into one text |
| stdin (non-TTY) | Read entire stdin as one text |
| None | Print usage + exit 2 |

Priority: `--file` > args > stdin. Only one source is used.

`results[]` always contains exactly 1 element in MVP.

### `lookup`

Each input item is a **separate query**.

| Source | Behavior |
|--------|----------|
| `--file path` | Read line-by-line; trim whitespace; skip empty lines |
| Positional args | Each arg is one query |
| stdin (non-TTY) | Read line-by-line; trim whitespace; skip empty lines |
| None | Print usage + exit 2 |

Priority: `--file` > args > stdin. Only one source is used.

`results[]` contains N elements (one per input item).

---

## Output

### JSON Output (`--json`)

Use `json.NewEncoder(os.Stdout)` with:
- `encoder.SetEscapeHTML(false)` — critical for Python parity (`<`, `>`, `&` must not be escaped)
- `encoder.SetIndent("", "  ")` — match Python `json.dumps(indent=2)`

#### `convert --json`

New schema (not in Python CLI). Defined here as the canonical reference.

```json
{
  "results": [
    {
      "input": "软件测试",
      "output": "軟體測試",
      "changed": true
    }
  ]
}
```

Fields:
- `input` (string): original text
- `output` (string): converted text
- `changed` (bool): `input != output`

#### `lookup --json`

**Must match Python CLI schema** (`src/zhtw/cli.py:856-877`).

```json
{
  "results": [
    {
      "input": "软件",
      "output": "軟體",
      "changed": true,
      "details": [
        {
          "source": "软件",
          "target": "軟體",
          "layer": "term",
          "position": 0
        }
      ]
    }
  ]
}
```

The Go SDK's `LookupResult` struct already has matching JSON tags. Implementation: marshal `[]LookupResult` wrapped in `{"results": [...]}`.

**Parity validation:** `lookup --json` output for the same input must produce identical JSON to `python -m zhtw lookup --json` (modulo trailing whitespace). This is a release-gate test.

### Plain Text Output (no `--json`)

#### `convert` (plain text)

Print converted text to stdout. No prefix, no decoration. Exactly one trailing newline. Designed for piping:

```bash
echo "软件测试" | zhtw convert
# stdout: 軟體測試
```

#### `lookup` (plain text)

Go-specific compact text format (not identical to Python CLI):

```
软件 → 軟體 (changed)
  [term] 软件 → 軟體 @0

测试 → 測試 (changed)
  [char] 测 → 測 @0
  [char] 试 → 試 @1
```

Format per word:
```
{input} → {output} (changed|unchanged)
  [{layer}] {source} → {target} @{position}
  ...
```

Blank line between entries when multiple words.

---

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | `convert --check` only: input was changed |
| 2 | Usage error (bad flag, no input, unknown subcommand, bad --sources value, etc.) |

**Rules:**
- `convert` without `--check`: always exit 0 on success (even if text changed)
- `convert --check`: exit 1 if `changed == true`, exit 0 if unchanged
- `lookup`: always exit 0 (informational tool)
- `version`: always exit 0

All errors (bad flags, file not found, invalid source/mode) go to stderr + exit 2.

---

## Version

### `zhtw version` Output

```
zhtw 4.2.0 (data 4.2.0)
```

When binary version == data version (normal case), still print both for clarity.

When they diverge:
```
zhtw 4.3.0 (data 4.2.0)
```

During development:
```
zhtw dev (data 4.2.0)
```

### Version Resolution

Three-tier fallback:

1. **`-ldflags` injection** (GoReleaser builds): `-X main.version=4.2.0` at compile time
2. **`debug.ReadBuildInfo()`** (`go install` users): reads module version from build metadata
3. **Fallback:** `"dev"` string

Data version: add a `DataVersion() string` function to the `zhtw` package that returns the `"version"` field from the embedded `zhtw-data.json` (already parsed by `getParsedData()`).

---

## Error Handling

All error output goes to **stderr**. stdout is reserved for results only.

| Scenario | Behavior |
|----------|----------|
| Unknown subcommand | stderr: usage + exit 2 |
| No input (no args, no stdin, no --file) | stderr: "error: no input provided" + exit 2 |
| Bad `--sources` value | stderr: "error: invalid source: ..." + exit 2 |
| Bad `--ambiguity-mode` value | stderr: "error: invalid ambiguity mode: ..." + exit 2 |
| `--file` not found / unreadable | stderr: "error: cannot read file: ..." + exit 2 |
| `Build()` returns `ErrEmptySources` | stderr: "error: sources must not be empty" + exit 2 |

No panics, no stack traces in normal operation.

---

## Testing

### CLI Tests (`sdk/go/cmd/zhtw/main_test.go`)

Use `os/exec.Command` to run the compiled binary. Test categories:

1. **Exit code tests:**
   - `convert` success → exit 0
   - `convert --check` with change → exit 1
   - `convert --check` without change → exit 0
   - Bad flag → exit 2
   - No input → exit 2
   - `lookup` always → exit 0

2. **JSON format golden tests (2-3 fixtures):**
   - `lookup --json "软件"` → diff against checked-in expected JSON
   - `convert --json "软件测试"` → diff against checked-in expected JSON
   - Key: validates `SetEscapeHTML(false)` and `SetIndent` formatting

3. **Input source tests:**
   - Args input
   - stdin pipe input
   - `--file` input
   - No input → error

4. **Flag parsing tests:**
   - `--sources cn` (single source)
   - `--ambiguity-mode balanced`
   - Unknown flag → error

Library-level conversion correctness is already verified by `sdk/go/zhtw/golden_test.go` (46 cases). CLI tests focus on **I/O format and behavior**, not conversion logic.

---

## Release & Distribution

### Install Methods

1. **`go install`** (source):
   ```bash
   go install github.com/rajatim/zhtw/sdk/go/v4/cmd/zhtw@latest
   ```

2. **GitHub Release binary** (pre-built):
   Download from the `sdk/go/vX.Y.Z` release page.

### GoReleaser Configuration

**File:** `sdk/go/.goreleaser.yml`

**Trigger:** `.github/workflows/go-binary.yml`, on push of `sdk/go/v*` tags.

**Targets:**

| OS | Arch | Artifact |
|----|------|----------|
| darwin | amd64 | `zhtw-darwin-amd64.tar.gz` |
| darwin | arm64 | `zhtw-darwin-arm64.tar.gz` |
| linux | amd64 | `zhtw-linux-amd64.tar.gz` |
| linux | arm64 | `zhtw-linux-arm64.tar.gz` |
| windows | amd64 | `zhtw-windows-amd64.zip` |

Each archive includes: binary + LICENSE + README.

**Checksums:** `zhtw_checksums.txt` (SHA-256).

**Release model:** GoReleaser creates a **separate GitHub Release** on the `sdk/go/vX.Y.Z` tag. This is independent from the root `vX.Y.Z` release (which triggers PyPI/Maven). Root release notes should include a link:

> Go CLI binary: see [sdk/go/v4.2.0](link) release.

**Version injection:** GoReleaser sets `-ldflags "-X main.version={{.Version}}"` automatically.

### CI Workflow (`.github/workflows/go-binary.yml`)

```yaml
name: Go Binary Release
on:
  push:
    tags: ['sdk/go/v*']
jobs:
  goreleaser:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: stable
      - uses: goreleaser/goreleaser-action@v6
        with:
          args: release --clean
          workdir: sdk/go
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

---

## Scope Boundaries

### In Scope (MVP)

- `convert` subcommand (text conversion)
- `lookup` subcommand (conversion detail query)
- `version` subcommand
- `--sources`, `--ambiguity-mode`, `--json`, `--file`, `--check` flags
- stdin / args / file input
- JSON + plain text output
- GoReleaser cross-compilation (5 targets)
- CLI-level tests (exit codes, JSON format golden, input sources)

### Explicitly Out of Scope

- `check` subcommand (name collision with Python CLI's file scanner; deferred)
- `fix` subcommand (file modification)
- `--dict` custom dictionary flag
- Directory recursive scanning
- `.zhtwignore` support
- Encoding detection / transcoding
- TUI / colored output
- Shell completion (bash/zsh/fish)
- Homebrew formula for Go binary

### Future Considerations

- **`check` subcommand:** When added, it should be a file scanner matching Python CLI semantics — not a text-level check. The Go SDK's `Check()` method is exposed through `lookup`.
- **Shell completion:** Can be added later with a `completion` subcommand generating bash/zsh/fish scripts.
- **`--dict`:** Requires file I/O + JSON parsing in CLI layer; reasonable v2 addition.

---

## File Summary

| File | Action | Description |
|------|--------|-------------|
| `sdk/go/cmd/zhtw/main.go` | Create | CLI entry point (~250-350 lines) |
| `sdk/go/cmd/zhtw/main_test.go` | Create | CLI integration tests |
| `sdk/go/cmd/zhtw/testdata/` | Create | Golden test fixtures (expected JSON outputs) |
| `sdk/go/.goreleaser.yml` | Create | GoReleaser configuration |
| `.github/workflows/go-binary.yml` | Create | Release workflow for Go binary |
| `sdk/go/zhtw/data.go` | Modify | Expose data version (small addition) |
| `README.md` / `README.en.md` | Modify | Add Go CLI install instructions |
| `Makefile` | No change | Existing `release` target already creates `sdk/go/v*` tag |
<!-- zhtw:enable -->
