<!-- zhtw:disable -->
# Go CLI Binary Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a standalone `zhtw` binary with `convert`, `lookup`, and `version` subcommands, using the existing Go SDK library.

**Architecture:** Single `main.go` file in `sdk/go/cmd/zhtw/` calls the Go SDK's public API. Per-subcommand `flag.FlagSet` parsing, zero external dependencies. Cross-compilation workflow builds 5 targets via `go build` matrix.

**Tech Stack:** Go 1.21+, stdlib only (`flag`, `os`, `io`, `encoding/json`, `fmt`, `bufio`, `strings`, `runtime/debug`), GitHub Actions for binary release.

**Spec:** `docs/superpowers/specs/2026-04-11-go-cli-binary-design.md`

---

## File Structure

| File | Responsibility |
|------|---------------|
| `sdk/go/zhtw/data.go` | Add `DataVersion()` function (small modification) |
| `sdk/go/cmd/zhtw/main.go` | CLI entry point: subcommand dispatch, flag parsing, I/O, output formatting |
| `sdk/go/cmd/zhtw/main_test.go` | Integration tests: exit codes, JSON golden, input sources, flags |
| `sdk/go/cmd/zhtw/testdata/lookup_software.json` | Golden fixture: `lookup --json "软件"` |
| `sdk/go/cmd/zhtw/testdata/convert_software_test.json` | Golden fixture: `convert --json "软件测试"` |
| `.github/workflows/go-binary.yml` | Cross-compilation + release workflow |

---

### Task 1: Expose DataVersion() from the library

**Files:**
- Modify: `sdk/go/zhtw/data.go`
- Test: `sdk/go/zhtw/zhtw_test.go`

The CLI needs the data version for `zhtw version`. The library already parses `zhtw-data.json` but doesn't expose the version field. Add it.

- [ ] **Step 1: Add version field to parsedData and DataVersion() function**

In `sdk/go/zhtw/data.go`, add a `version` field to `parsedData` and a public `DataVersion()` function:

```go
type parsedData struct {
	version          string // NEW
	charMap          map[rune]rune
	balancedDefaults map[rune]rune
	termsCn          map[string]string
	termsHk          map[string]string
}
```

In `mustParseData`, save the version:

```go
func mustParseData(raw []byte) *parsedData {
	var j zhtwDataJSON
	if err := json.Unmarshal(raw, &j); err != nil {
		panic("zhtw: failed to parse embedded zhtw-data.json: " + err.Error())
	}
	// ... existing code ...
	return &parsedData{
		version:          j.Version, // NEW
		charMap:          charMap,
		balancedDefaults: balancedDefaults,
		termsCn:          termsCn,
		termsHk:          termsHk,
	}
}
```

Add the public function:

```go
// DataVersion returns the version string from the embedded zhtw-data.json.
func DataVersion() string {
	return getParsedData().version
}
```

- [ ] **Step 2: Add test for DataVersion**

Append to `sdk/go/zhtw/zhtw_test.go`:

```go
func TestDataVersion(t *testing.T) {
	v := zhtw.DataVersion()
	if v == "" {
		t.Fatal("DataVersion() returned empty string")
	}
	// Version should look like X.Y.Z
	parts := strings.Split(v, ".")
	if len(parts) != 3 {
		t.Fatalf("DataVersion() = %q, want X.Y.Z format", v)
	}
}
```

(Add `"strings"` to the test file's import block if not already present.)

- [ ] **Step 3: Run tests**

Run: `cd sdk/go && go test ./zhtw/ -v -run TestDataVersion`
Expected: PASS

- [ ] **Step 4: Run all existing tests to confirm no regression**

Run: `cd sdk/go && go test ./zhtw/ -v -race -count=1`
Expected: All 21+ tests PASS

- [ ] **Step 5: Commit**

```bash
git add sdk/go/zhtw/data.go sdk/go/zhtw/zhtw_test.go
git commit -m "feat(go): DataVersion() 公開 embedded data 版本號"
```

---

### Task 2: CLI skeleton — subcommand dispatch + version

**Files:**
- Create: `sdk/go/cmd/zhtw/main.go`

Build the minimal CLI skeleton: subcommand parsing, usage, and `version` subcommand. No convert/lookup yet.

- [ ] **Step 1: Create main.go with subcommand dispatch and version**

Create `sdk/go/cmd/zhtw/main.go`:

```go
package main

import (
	"fmt"
	"os"
	"runtime/debug"

	"github.com/rajatim/zhtw/sdk/go/v4/zhtw"
)

// version is set by -ldflags at build time; fallback uses debug.ReadBuildInfo.
var version string

func main() {
	if len(os.Args) < 2 {
		printUsage()
		os.Exit(2)
	}
	switch os.Args[1] {
	case "convert":
		os.Exit(runConvert(os.Args[2:]))
	case "lookup":
		os.Exit(runLookup(os.Args[2:]))
	case "version":
		printVersion()
	default:
		fmt.Fprintf(os.Stderr, "error: unknown command %q\n\n", os.Args[1])
		printUsage()
		os.Exit(2)
	}
}

func printUsage() {
	fmt.Fprintln(os.Stderr, `Usage: zhtw <command> [flags] [args...]

Commands:
  convert    Convert simplified Chinese to traditional
  lookup     Query conversion details for words/phrases
  version    Print version information

Run 'zhtw <command> --help' for command-specific flags.`)
}

func printVersion() {
	v := resolveVersion()
	dv := zhtw.DataVersion()
	fmt.Printf("zhtw %s (data %s)\n", v, dv)
}

func resolveVersion() string {
	if version != "" {
		return version
	}
	if info, ok := debug.ReadBuildInfo(); ok && info.Main.Version != "" && info.Main.Version != "(devel)" {
		return info.Main.Version
	}
	return "dev"
}

// Stubs — implemented in Task 3 and Task 4.
func runConvert(args []string) int { return 0 }
func runLookup(args []string) int  { return 0 }
```

- [ ] **Step 2: Verify it compiles**

Run: `cd sdk/go && go build ./cmd/zhtw/`
Expected: No errors, produces `zhtw` binary in `sdk/go/`.

- [ ] **Step 3: Manual smoke test**

```bash
cd sdk/go
./zhtw version
./zhtw
./zhtw badcommand
```

Expected:
- `version`: prints `zhtw dev (data 4.2.0)` + exit 0
- no args: prints usage + exit 2
- bad command: prints error + usage + exit 2

- [ ] **Step 4: Clean up binary and commit**

```bash
rm -f sdk/go/zhtw  # remove built binary (not the zhtw/ directory)
git add sdk/go/cmd/zhtw/main.go
git commit -m "feat(go): CLI skeleton——subcommand dispatch + version"
```

---

### Task 3: convert subcommand

**Files:**
- Modify: `sdk/go/cmd/zhtw/main.go`

Implement `runConvert`: flag parsing, input reading, converter build, plain text + JSON output, `--check` exit code logic.

- [ ] **Step 1: Implement runConvert**

Replace the `runConvert` stub in `main.go` with the full implementation. Also add the necessary imports and helper functions.

Add these imports (merge into existing import block):

```go
import (
	"bufio"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"os"
	"runtime/debug"
	"strings"

	"github.com/rajatim/zhtw/sdk/go/v4/zhtw"
)
```

Add the shared helper functions and convert implementation:

```go
// ── Shared helpers ──────────────────────────────────────────────────────────

func parseSources(s string) ([]zhtw.Source, error) {
	var sources []zhtw.Source
	for _, part := range strings.Split(s, ",") {
		part = strings.TrimSpace(part)
		switch part {
		case "cn":
			sources = append(sources, zhtw.SourceCn)
		case "hk":
			sources = append(sources, zhtw.SourceHk)
		default:
			return nil, fmt.Errorf("invalid source: %q (valid: cn, hk)", part)
		}
	}
	return sources, nil
}

func parseAmbiguityMode(s string) (zhtw.AmbiguityMode, error) {
	switch s {
	case "strict":
		return zhtw.AmbiguityStrict, nil
	case "balanced":
		return zhtw.AmbiguityBalanced, nil
	default:
		return "", fmt.Errorf("invalid ambiguity mode: %q (valid: strict, balanced)", s)
	}
}

func buildConverter(sources []zhtw.Source, mode zhtw.AmbiguityMode) (*zhtw.Converter, error) {
	return zhtw.NewBuilder().
		Sources(sources...).
		SetAmbiguityMode(mode).
		Build()
}

func isStdinPipe() bool {
	fi, err := os.Stdin.Stat()
	if err != nil {
		return false
	}
	return fi.Mode()&os.ModeCharDevice == 0
}

func writeJSON(v any) {
	enc := json.NewEncoder(os.Stdout)
	enc.SetEscapeHTML(false)
	enc.SetIndent("", "  ")
	enc.Encode(v)
}

func fatalf(format string, args ...any) int {
	fmt.Fprintf(os.Stderr, "error: "+format+"\n", args...)
	return 2
}

// ── convert ─────────────────────────────────────────────────────────────────

func runConvert(args []string) int {
	fs := flag.NewFlagSet("convert", flag.ContinueOnError)
	fs.SetOutput(os.Stderr)
	sourcesFlag := fs.String("sources", "cn,hk", "conversion sources (cn, hk, cn,hk)")
	modeFlag := fs.String("ambiguity-mode", "strict", "ambiguity mode (strict, balanced)")
	jsonFlag := fs.Bool("json", false, "JSON output")
	fileFlag := fs.String("file", "", "read input from file")
	checkFlag := fs.Bool("check", false, "exit 1 if input was changed (for CI)")
	if err := fs.Parse(args); err != nil {
		return 2
	}

	sources, err := parseSources(*sourcesFlag)
	if err != nil {
		return fatalf("%v", err)
	}
	mode, err := parseAmbiguityMode(*modeFlag)
	if err != nil {
		return fatalf("%v", err)
	}

	input, err := readConvertInput(*fileFlag, fs.Args())
	if err != nil {
		return fatalf("%v", err)
	}

	conv, err := buildConverter(sources, mode)
	if err != nil {
		return fatalf("%v", err)
	}

	output := conv.Convert(input)
	changed := output != input

	if *jsonFlag {
		type convertResult struct {
			Input   string `json:"input"`
			Output  string `json:"output"`
			Changed bool   `json:"changed"`
		}
		writeJSON(struct {
			Results []convertResult `json:"results"`
		}{
			Results: []convertResult{{Input: input, Output: output, Changed: changed}},
		})
	} else {
		fmt.Println(output)
	}

	if *checkFlag && changed {
		return 1
	}
	return 0
}

func readConvertInput(filePath string, args []string) (string, error) {
	if filePath != "" {
		data, err := os.ReadFile(filePath)
		if err != nil {
			return "", fmt.Errorf("cannot read file: %v", err)
		}
		return string(data), nil
	}
	if len(args) > 0 {
		return strings.Join(args, " "), nil
	}
	if isStdinPipe() {
		data, err := io.ReadAll(os.Stdin)
		if err != nil {
			return "", fmt.Errorf("cannot read stdin: %v", err)
		}
		return string(data), nil
	}
	return "", fmt.Errorf("no input provided")
}
```

- [ ] **Step 2: Verify it compiles**

Run: `cd sdk/go && go build ./cmd/zhtw/`
Expected: No errors.

- [ ] **Step 3: Manual smoke test**

```bash
cd sdk/go
./zhtw convert "软件测试"
./zhtw convert --json "软件测试"
echo "用户权限" | ./zhtw convert
./zhtw convert --check "hello"
echo $?  # should be 0
./zhtw convert --check "软件"
echo $?  # should be 1
```

Expected outputs:
- `軟體測試`
- JSON with `{"results": [{"input": "软件测试", ...}]}`
- `使用者權限`
- exit 0 for "hello" (no change)
- exit 1 for "软件" (changed)

- [ ] **Step 4: Clean up and commit**

```bash
rm -f sdk/go/zhtw  # built binary
git add sdk/go/cmd/zhtw/main.go
git commit -m "feat(go): convert subcommand——text/JSON 輸出 + --check flag"
```

---

### Task 4: lookup subcommand

**Files:**
- Modify: `sdk/go/cmd/zhtw/main.go`

Implement `runLookup`: per-word queries, line-by-line stdin/file, plain text + JSON output.

- [ ] **Step 1: Implement runLookup**

Replace the `runLookup` stub in `main.go`:

```go
// ── lookup ──────────────────────────────────────────────────────────────────

func runLookup(args []string) int {
	fs := flag.NewFlagSet("lookup", flag.ContinueOnError)
	fs.SetOutput(os.Stderr)
	sourcesFlag := fs.String("sources", "cn,hk", "conversion sources (cn, hk, cn,hk)")
	modeFlag := fs.String("ambiguity-mode", "strict", "ambiguity mode (strict, balanced)")
	jsonFlag := fs.Bool("json", false, "JSON output")
	fileFlag := fs.String("file", "", "read input from file (one word per line)")
	if err := fs.Parse(args); err != nil {
		return 2
	}

	sources, err := parseSources(*sourcesFlag)
	if err != nil {
		return fatalf("%v", err)
	}
	mode, err := parseAmbiguityMode(*modeFlag)
	if err != nil {
		return fatalf("%v", err)
	}

	words, err := readLookupInput(*fileFlag, fs.Args())
	if err != nil {
		return fatalf("%v", err)
	}

	conv, err := buildConverter(sources, mode)
	if err != nil {
		return fatalf("%v", err)
	}

	results := make([]zhtw.LookupResult, len(words))
	for i, w := range words {
		results[i] = conv.Lookup(w)
	}

	if *jsonFlag {
		writeJSON(struct {
			Results []zhtw.LookupResult `json:"results"`
		}{
			Results: results,
		})
	} else {
		for i, r := range results {
			if i > 0 {
				fmt.Println()
			}
			status := "changed"
			if !r.Changed {
				status = "unchanged"
			}
			fmt.Printf("%s → %s (%s)\n", r.Input, r.Output, status)
			for _, d := range r.Details {
				fmt.Printf("  [%s] %s → %s @%d\n", d.Layer, d.Source, d.Target, d.Position)
			}
		}
	}

	return 0
}

func readLookupInput(filePath string, args []string) ([]string, error) {
	if filePath != "" {
		return readLines(filePath)
	}
	if len(args) > 0 {
		return args, nil
	}
	if isStdinPipe() {
		return readLinesFromReader(os.Stdin)
	}
	return nil, fmt.Errorf("no input provided")
}

func readLines(path string) ([]string, error) {
	f, err := os.Open(path)
	if err != nil {
		return nil, fmt.Errorf("cannot read file: %v", err)
	}
	defer f.Close()
	return readLinesFromReader(f)
}

func readLinesFromReader(r io.Reader) ([]string, error) {
	var lines []string
	scanner := bufio.NewScanner(r)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line != "" {
			lines = append(lines, line)
		}
	}
	if err := scanner.Err(); err != nil {
		return nil, err
	}
	if len(lines) == 0 {
		return nil, fmt.Errorf("no input provided")
	}
	return lines, nil
}
```

- [ ] **Step 2: Verify it compiles**

Run: `cd sdk/go && go build ./cmd/zhtw/`
Expected: No errors.

- [ ] **Step 3: Manual smoke test**

```bash
cd sdk/go
./zhtw lookup "软件" "测试"
./zhtw lookup --json "软件"
echo -e "软件\n测试" | ./zhtw lookup --json
./zhtw lookup --sources cn --ambiguity-mode balanced "几个"
```

Expected:
- Plain text: two entries with `→` and detail lines
- JSON: `{"results": [...]}` matching Python schema
- stdin: two results in JSON array
- balanced mode: `几个` → `幾個`

- [ ] **Step 4: Clean up and commit**

```bash
rm -f sdk/go/zhtw
git add sdk/go/cmd/zhtw/main.go
git commit -m "feat(go): lookup subcommand——逐詞查詢 + JSON/plain text 輸出"
```

---

### Task 5: Golden test fixtures

**Files:**
- Create: `sdk/go/cmd/zhtw/testdata/lookup_software.json`
- Create: `sdk/go/cmd/zhtw/testdata/convert_software_test.json`

Generate the golden fixtures by running the CLI and capturing exact output.

- [ ] **Step 1: Build the CLI**

```bash
cd sdk/go && go build -o zhtw-test-bin ./cmd/zhtw/
```

- [ ] **Step 2: Generate lookup golden fixture**

```bash
cd sdk/go
./zhtw-test-bin lookup --json "软件" > cmd/zhtw/testdata/lookup_software.json
```

Verify the content matches Python output:

```bash
diff <(python -m zhtw lookup --json "软件" 2>/dev/null) cmd/zhtw/testdata/lookup_software.json
```

Expected: no diff. The file should contain:

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

- [ ] **Step 3: Generate convert golden fixture**

```bash
cd sdk/go
./zhtw-test-bin convert --json "软件测试" > cmd/zhtw/testdata/convert_software_test.json
```

The file should contain:

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

- [ ] **Step 4: Clean up and commit**

```bash
rm -f sdk/go/zhtw-test-bin
mkdir -p sdk/go/cmd/zhtw/testdata
git add sdk/go/cmd/zhtw/testdata/
git commit -m "test(go): CLI golden fixtures——lookup + convert JSON"
```

---

### Task 6: CLI integration tests

**Files:**
- Create: `sdk/go/cmd/zhtw/main_test.go`

Integration tests using `os/exec` to run the compiled binary. Tests I/O format and behavior, not conversion correctness.

- [ ] **Step 1: Create main_test.go with test helper and build step**

Create `sdk/go/cmd/zhtw/main_test.go`:

```go
package main_test

import (
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"testing"
)

var binaryPath string

func TestMain(m *testing.M) {
	// Build the binary once for all tests.
	tmp, err := os.MkdirTemp("", "zhtw-cli-test")
	if err != nil {
		panic(err)
	}
	defer os.RemoveAll(tmp)

	binaryPath = filepath.Join(tmp, "zhtw")
	cmd := exec.Command("go", "build", "-o", binaryPath, ".")
	cmd.Dir = "."
	if out, err := cmd.CombinedOutput(); err != nil {
		panic("failed to build CLI: " + string(out))
	}

	os.Exit(m.Run())
}

func runCLI(t *testing.T, stdin string, args ...string) (stdout, stderr string, exitCode int) {
	t.Helper()
	cmd := exec.Command(binaryPath, args...)
	if stdin != "" {
		cmd.Stdin = strings.NewReader(stdin)
	}
	var outBuf, errBuf strings.Builder
	cmd.Stdout = &outBuf
	cmd.Stderr = &errBuf
	err := cmd.Run()
	exitCode = 0
	if exitErr, ok := err.(*exec.ExitError); ok {
		exitCode = exitErr.ExitCode()
	} else if err != nil {
		t.Fatalf("unexpected error running CLI: %v", err)
	}
	return outBuf.String(), errBuf.String(), exitCode
}
```

- [ ] **Step 2: Add exit code tests**

Append to `main_test.go`:

```go
func TestVersionExitCode(t *testing.T) {
	stdout, _, code := runCLI(t, "", "version")
	if code != 0 {
		t.Fatalf("version exit code = %d, want 0", code)
	}
	if !strings.Contains(stdout, "zhtw") || !strings.Contains(stdout, "data") {
		t.Fatalf("version output = %q, want 'zhtw ... (data ...)'", stdout)
	}
}

func TestNoArgsExitCode(t *testing.T) {
	_, _, code := runCLI(t, "", /* no args */)
	if code != 2 {
		t.Fatalf("no args exit code = %d, want 2", code)
	}
}

func TestUnknownCommandExitCode(t *testing.T) {
	_, stderr, code := runCLI(t, "", "badcommand")
	if code != 2 {
		t.Fatalf("unknown command exit code = %d, want 2", code)
	}
	if !strings.Contains(stderr, "unknown command") {
		t.Fatalf("stderr = %q, want 'unknown command'", stderr)
	}
}

func TestConvertExitZero(t *testing.T) {
	_, _, code := runCLI(t, "", "convert", "软件测试")
	if code != 0 {
		t.Fatalf("convert exit code = %d, want 0", code)
	}
}

func TestConvertCheckChanged(t *testing.T) {
	_, _, code := runCLI(t, "", "convert", "--check", "软件")
	if code != 1 {
		t.Fatalf("convert --check (changed) exit code = %d, want 1", code)
	}
}

func TestConvertCheckUnchanged(t *testing.T) {
	_, _, code := runCLI(t, "", "convert", "--check", "hello")
	if code != 0 {
		t.Fatalf("convert --check (unchanged) exit code = %d, want 0", code)
	}
}

func TestConvertNoInput(t *testing.T) {
	_, _, code := runCLI(t, "", "convert")
	if code != 2 {
		t.Fatalf("convert no input exit code = %d, want 2", code)
	}
}

func TestLookupExitZero(t *testing.T) {
	_, _, code := runCLI(t, "", "lookup", "软件")
	if code != 0 {
		t.Fatalf("lookup exit code = %d, want 0", code)
	}
}
```

- [ ] **Step 3: Add JSON golden tests**

Append to `main_test.go`:

```go
func TestLookupJSONGolden(t *testing.T) {
	stdout, _, code := runCLI(t, "", "lookup", "--json", "软件")
	if code != 0 {
		t.Fatalf("exit code = %d, want 0", code)
	}
	expected, err := os.ReadFile("testdata/lookup_software.json")
	if err != nil {
		t.Fatalf("read golden: %v", err)
	}
	if stdout != string(expected) {
		t.Fatalf("lookup --json mismatch.\ngot:\n%s\nwant:\n%s", stdout, string(expected))
	}
}

func TestConvertJSONGolden(t *testing.T) {
	stdout, _, code := runCLI(t, "", "convert", "--json", "软件测试")
	if code != 0 {
		t.Fatalf("exit code = %d, want 0", code)
	}
	expected, err := os.ReadFile("testdata/convert_software_test.json")
	if err != nil {
		t.Fatalf("read golden: %v", err)
	}
	if stdout != string(expected) {
		t.Fatalf("convert --json mismatch.\ngot:\n%s\nwant:\n%s", stdout, string(expected))
	}
}
```

- [ ] **Step 4: Add input source tests**

Append to `main_test.go`:

```go
func TestConvertArgs(t *testing.T) {
	stdout, _, code := runCLI(t, "", "convert", "软件", "测试")
	if code != 0 {
		t.Fatalf("exit code = %d", code)
	}
	// Args joined with space: "软件 测试" → "軟體 測試"
	if got := strings.TrimSpace(stdout); got != "軟體 測試" {
		t.Fatalf("got %q, want %q", got, "軟體 測試")
	}
}

func TestConvertStdin(t *testing.T) {
	stdout, _, code := runCLI(t, "用户权限", "convert")
	if code != 0 {
		t.Fatalf("exit code = %d", code)
	}
	if got := strings.TrimSpace(stdout); got != "使用者權限" {
		t.Fatalf("got %q, want %q", got, "使用者權限")
	}
}

func TestConvertFile(t *testing.T) {
	tmp, err := os.CreateTemp("", "zhtw-test-*.txt")
	if err != nil {
		t.Fatal(err)
	}
	defer os.Remove(tmp.Name())
	tmp.WriteString("软件测试")
	tmp.Close()

	stdout, _, code := runCLI(t, "", "convert", "--file", tmp.Name())
	if code != 0 {
		t.Fatalf("exit code = %d", code)
	}
	if got := strings.TrimSpace(stdout); got != "軟體測試" {
		t.Fatalf("got %q, want %q", got, "軟體測試")
	}
}

func TestLookupStdinMultiline(t *testing.T) {
	stdout, _, code := runCLI(t, "软件\n测试\n", "lookup", "--json")
	if code != 0 {
		t.Fatalf("exit code = %d", code)
	}
	// Should have 2 results
	if !strings.Contains(stdout, `"input": "软件"`) || !strings.Contains(stdout, `"input": "测试"`) {
		t.Fatalf("expected two results in JSON, got:\n%s", stdout)
	}
}
```

- [ ] **Step 5: Add flag parsing tests**

Append to `main_test.go`:

```go
func TestConvertSourcesCn(t *testing.T) {
	stdout, _, code := runCLI(t, "", "convert", "--sources", "cn", "软件测试")
	if code != 0 {
		t.Fatalf("exit code = %d", code)
	}
	if got := strings.TrimSpace(stdout); got != "軟體測試" {
		t.Fatalf("got %q, want %q", got, "軟體測試")
	}
}

func TestConvertBadSources(t *testing.T) {
	_, stderr, code := runCLI(t, "", "convert", "--sources", "xx", "test")
	if code != 2 {
		t.Fatalf("bad sources exit code = %d, want 2", code)
	}
	if !strings.Contains(stderr, "invalid source") {
		t.Fatalf("stderr = %q, want 'invalid source'", stderr)
	}
}

func TestConvertBalancedMode(t *testing.T) {
	stdout, _, code := runCLI(t, "", "convert", "--ambiguity-mode", "balanced", "几个里程碑")
	if code != 0 {
		t.Fatalf("exit code = %d", code)
	}
	got := strings.TrimSpace(stdout)
	// Balanced mode should convert 几→幾 and 里→裡 (when not in a term)
	if !strings.Contains(got, "幾") {
		t.Fatalf("balanced mode: got %q, expected 幾 in output", got)
	}
}
```

- [ ] **Step 6: Run all CLI tests**

Run: `cd sdk/go/cmd/zhtw && go test -v -count=1`
Expected: All tests PASS.

- [ ] **Step 7: Run all tests (library + CLI) together**

Run: `cd sdk/go && go test ./... -v -race -count=1`
Expected: All tests PASS (library + CLI).

- [ ] **Step 8: Commit**

```bash
git add sdk/go/cmd/zhtw/main_test.go
git commit -m "test(go): CLI 整合測試——exit code + JSON golden + input sources + flags"
```

---

### Task 7: Cross-compilation release workflow

**Files:**
- Create: `.github/workflows/go-binary.yml`

GitHub Actions workflow that builds 5 platform binaries and creates a release on `sdk/go/v*` tag push.

- [ ] **Step 1: Create the workflow file**

Create `.github/workflows/go-binary.yml`:

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

- [ ] **Step 2: Validate YAML syntax**

Run: `python -c "import yaml; yaml.safe_load(open('.github/workflows/go-binary.yml'))" 2>&1 || echo "YAML syntax error"`
Expected: No output (valid YAML).

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/go-binary.yml
git commit -m "ci(go): cross-compilation workflow——5 targets + GitHub Release"
```

---

### Task 8: Update sdk-go.yml to also test CLI

**Files:**
- Modify: `.github/workflows/sdk-go.yml`

The existing Go SDK CI workflow should also build and test the CLI.

- [ ] **Step 1: Add CLI test step to sdk-go.yml**

In `.github/workflows/sdk-go.yml`, after the existing `Test` step (line ~28), the `run` command already uses `go test ./... -v -race` which will automatically pick up `cmd/zhtw/` tests. Verify this is the case — no change needed if `./...` is already used.

If the existing command is `go test ./zhtw/ -v -race` (only testing the library subdirectory), change it to:

```yaml
      - name: Test
        working-directory: sdk/go
        run: go test ./... -v -race
```

And update the Vet step similarly:

```yaml
      - name: Vet
        working-directory: sdk/go
        run: go vet ./...
```

- [ ] **Step 2: Verify locally**

Run: `cd sdk/go && go test ./... -v -race -count=1`
Expected: Both `zhtw` (library) and `cmd/zhtw` (CLI) test suites pass.

- [ ] **Step 3: Commit (only if changes were needed)**

```bash
git add .github/workflows/sdk-go.yml
git commit -m "ci(go): SDK CI 擴展涵蓋 CLI 測試"
```

---

### Task 9: Update README with Go CLI install instructions

**Files:**
- Modify: `README.md`
- Modify: `README.en.md`

Add Go CLI binary install instructions to the Go SDK section in both READMEs.

- [ ] **Step 1: Update README.md**

In the Go SDK section (section 6), after the existing code example and feature description, add:

```markdown
#### Standalone Binary

不需要 Go 環境，直接下載預編譯 binary：

<!-- zhtw:disable -->
```bash
# 從 GitHub Release 下載（以 macOS arm64 為例）
curl -sL https://github.com/rajatim/zhtw/releases/download/sdk%2Fgo%2Fv4.2.0/zhtw-darwin-arm64.tar.gz | tar xz
./zhtw convert "软件测试"
# → 軟體測試

# 或透過 go install
go install github.com/rajatim/zhtw/sdk/go/v4/cmd/zhtw@latest
```
<!-- zhtw:enable -->
```

- [ ] **Step 2: Update README.en.md**

Same section, English version:

```markdown
#### Standalone Binary

No Go environment needed — download pre-built binaries:

<!-- zhtw:disable -->
```bash
# Download from GitHub Release (e.g., macOS arm64)
curl -sL https://github.com/rajatim/zhtw/releases/download/sdk%2Fgo%2Fv4.2.0/zhtw-darwin-arm64.tar.gz | tar xz
./zhtw convert "软件测试"
# → 軟體測試

# Or via go install
go install github.com/rajatim/zhtw/sdk/go/v4/cmd/zhtw@latest
```
<!-- zhtw:enable -->
```

- [ ] **Step 3: Commit**

```bash
git add README.md README.en.md
git commit -m "docs: Go CLI binary 安裝說明"
```

---

## Self-Review Checklist

**Spec coverage:**
- [x] convert subcommand → Task 3
- [x] lookup subcommand → Task 4
- [x] version subcommand → Task 2
- [x] --sources, --ambiguity-mode, --json, --file flags → Tasks 3, 4
- [x] --check flag (convert only) → Task 3
- [x] Input semantics: args/stdin/file, convert vs lookup differences → Tasks 3, 4
- [x] JSON output with SetEscapeHTML(false) + SetIndent → Task 3 (`writeJSON` helper)
- [x] Plain text output format → Tasks 3, 4
- [x] Exit codes: 0/1/2 → Tasks 3, 4
- [x] Version resolution: ldflags → ReadBuildInfo → "dev" → Task 2
- [x] DataVersion() → Task 1
- [x] Error handling to stderr → Tasks 3, 4 (`fatalf` helper)
- [x] CLI tests: exit codes, golden JSON, input sources, flags → Task 6
- [x] Golden fixtures → Task 5
- [x] Cross-compilation workflow → Task 7
- [x] CI integration → Task 8
- [x] README update → Task 9

**Placeholder scan:** No TBD/TODO found.

**Type consistency:** `parseSources`, `parseAmbiguityMode`, `buildConverter`, `writeJSON`, `fatalf`, `isStdinPipe` — all used consistently across Tasks 3 and 4. `DataVersion()` in Task 1 matches usage in Task 2's `printVersion()`.
<!-- zhtw:enable -->
