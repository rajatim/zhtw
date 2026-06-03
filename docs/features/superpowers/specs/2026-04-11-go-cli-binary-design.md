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

**Parity validation:** `lookup --json` output for the same input should produce identical JSON to `python -m zhtw lookup --json` (modulo trailing whitespace). Verified by checked-in golden fixtures; inner `LookupResult` structure is already cross-SDK validated by `sdk/data/golden-test.json`.

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

1. **`-ldflags` injection** (CI release builds): `-X main.version=4.2.0` at compile time
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
   - Note: inner `LookupResult` structure is already cross-SDK verified by `sdk/data/golden-test.json` (46 cases). CLI golden fixtures validate the `{"results": [...]}` envelope and formatting only. If Python CLI output changes, fixtures must be manually updated — acceptable for MVP since the envelope is trivially simple.

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

### Cross-Compilation Workflow

No GoReleaser — its monorepo tag-prefix support (`sdk/go/v*`) requires GoReleaser Pro. For 5 static Go binaries with zero CGO, a custom `go build` matrix is simpler and has no external dependency.

**Trigger:** `.github/workflows/go-binary.yml`, on push of `sdk/go/v*` tags.

**Targets:**

| OS | Arch | Artifact |
|----|------|----------|
| darwin | amd64 | `zhtw-darwin-amd64.tar.gz` |
| darwin | arm64 | `zhtw-darwin-arm64.tar.gz` |
| linux | amd64 | `zhtw-linux-amd64.tar.gz` |
| linux | arm64 | `zhtw-linux-arm64.tar.gz` |
| windows | amd64 | `zhtw-windows-amd64.zip` |

Each archive includes: binary + LICENSE.

**Checksums:** `zhtw_checksums.txt` (SHA-256), uploaded alongside archives.

**Release model:** The workflow creates a **separate GitHub Release** on the `sdk/go/vX.Y.Z` tag. This is independent from the root `vX.Y.Z` release (which triggers PyPI/Maven). Maintainer may optionally edit the root release notes to link to the Go binary release after it completes.

**Version injection:** The workflow extracts version from the tag (`sdk/go/v4.2.0` → `4.2.0`) and passes `-ldflags "-X main.version=4.2.0"` to `go build`.

### CI Workflow (`.github/workflows/go-binary.yml`)

```yaml
name: Go Binary Release
on:
  push:
    tags: ['sdk/go/v*']
jobs:
  build:
    strategy:
      matrix:
        include:
          - {goos: darwin, goarch: amd64}
          - {goos: darwin, goarch: arm64}
          - {goos: linux, goarch: amd64}
          - {goos: linux, goarch: arm64}
          - {goos: windows, goarch: amd64}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-go@v5
        with:
          go-version: stable
      - name: Extract version
        id: version
        run: echo "version=${GITHUB_REF_NAME#sdk/go/v}" >> "$GITHUB_OUTPUT"
      - name: Build
        working-directory: sdk/go
        env:
          GOOS: ${{ matrix.goos }}
          GOARCH: ${{ matrix.goarch }}
          CGO_ENABLED: '0'
        run: |
          ext="" && [[ "$GOOS" == "windows" ]] && ext=".exe"
          go build -ldflags "-X main.version=${{ steps.version.outputs.version }}" \
            -o "zhtw-${GOOS}-${GOARCH}${ext}" ./cmd/zhtw
      - uses: actions/upload-artifact@v4
        with:
          name: zhtw-${{ matrix.goos }}-${{ matrix.goarch }}
          path: sdk/go/zhtw-*

  release:
    needs: build
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/download-artifact@v4
        with:
          merge-multiple: true
      - name: Archive and checksum
        run: |
          for f in zhtw-*; do
            if [[ "$f" == *windows* ]]; then
              zip "${f%.exe}.zip" "$f"
            else
              chmod +x "$f"
              tar czf "${f}.tar.gz" "$f"
            fi
          done
          shasum -a 256 *.tar.gz *.zip > zhtw_checksums.txt
      - name: Create release
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          gh release create "${{ github.ref_name }}" \
            --repo "${{ github.repository }}" \
            --title "Go CLI ${GITHUB_REF_NAME#sdk/go/}" \
            --generate-notes \
            *.tar.gz *.zip zhtw_checksums.txt
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
- Cross-compilation workflow (5 targets, pure `go build`)
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

- **`check` subcommand:** When added, it should be a file scanner matching Python CLI semantics — not a text-level check. The Go SDK's `Check()` method (text-level match detection) has no CLI equivalent in MVP; users who need match details should use `lookup`.
- **Shell completion:** Can be added later with a `completion` subcommand generating bash/zsh/fish scripts.
- **`--dict`:** Requires file I/O + JSON parsing in CLI layer; reasonable v2 addition.

---

## File Summary

| File | Action | Description |
|------|--------|-------------|
| `sdk/go/cmd/zhtw/main.go` | Create | CLI entry point (~250-350 lines) |
| `sdk/go/cmd/zhtw/main_test.go` | Create | CLI integration tests |
| `sdk/go/cmd/zhtw/testdata/` | Create | Golden test fixtures (expected JSON outputs) |
| `.github/workflows/go-binary.yml` | Create | Cross-compilation + release workflow |
| `sdk/go/zhtw/data.go` | Modify | Expose data version (small addition) |
| `README.md` / `README.en.md` | Modify | Add Go CLI install instructions |
| `Makefile` | No change | Existing `release` target already creates `sdk/go/v*` tag |
<!-- zhtw:enable -->
