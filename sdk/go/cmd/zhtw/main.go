// Command zhtw converts simplified Chinese to Traditional Chinese (Taiwan).
package main

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

// version is set via -ldflags "-X main.version=..." at build time.
var version string

func main() {
	os.Exit(run(os.Args[1:]))
}

// run dispatches to the appropriate subcommand and returns the exit code.
func run(args []string) int {
	if len(args) == 0 {
		usage()
		return 2
	}

	switch args[0] {
	case "convert":
		return runConvert(args[1:])
	case "lookup":
		return runLookup(args[1:])
	case "version":
		fmt.Printf("zhtw %s (data %s)\n", resolveVersion(), zhtw.DataVersion())
		return 0
	default:
		fmt.Fprintf(os.Stderr, "zhtw: unknown command %q\n\n", args[0])
		usage()
		return 2
	}
}

func usage() {
	fmt.Fprintln(os.Stderr, `Usage: zhtw <command> [flags] [args...]

Commands:
  convert   Convert simplified Chinese to traditional
  lookup    Query conversion details for words
  version   Print version information

Run 'zhtw <command> -h' for details on a command.`)
}

// ── convert ─────────────────────────────────────────────────────────────────

func runConvert(args []string) int {
	fs := flag.NewFlagSet("convert", flag.ContinueOnError)
	fs.SetOutput(os.Stderr)

	sources := fs.String("sources", "cn,hk", "comma-separated sources: cn, hk")
	ambiguityMode := fs.String("ambiguity-mode", "strict", "ambiguity mode: strict or balanced")
	jsonOut := fs.Bool("json", false, "output as JSON")
	filePath := fs.String("file", "", "read input from file")
	check := fs.Bool("check", false, "exit 1 if input was changed (for CI)")

	if err := fs.Parse(args); err != nil {
		return 2
	}

	conv, code := buildConverterFromFlags(*sources, *ambiguityMode)
	if code != 0 {
		return code
	}

	// Gather input: --file > positional args > stdin.
	var input string
	switch {
	case *filePath != "":
		data, err := os.ReadFile(*filePath)
		if err != nil {
			return fatalf("cannot read file: %v", err)
		}
		input = string(data)
	case fs.NArg() > 0:
		input = strings.Join(fs.Args(), " ")
	case isStdinPipe():
		data, err := io.ReadAll(os.Stdin)
		if err != nil {
			return fatalf("reading stdin: %v", err)
		}
		input = string(data)
	default:
		return fatalf("no input provided (use args, --file, or pipe)")
	}

	output := conv.Convert(input)
	changed := output != input

	if *jsonOut {
		type result struct {
			Input   string `json:"input"`
			Output  string `json:"output"`
			Changed bool   `json:"changed"`
		}
		writeJSON(struct {
			Results []result `json:"results"`
		}{
			Results: []result{{Input: input, Output: output, Changed: changed}},
		})
	} else {
		fmt.Println(output)
	}

	if *check && changed {
		return 1
	}
	return 0
}

// ── lookup ──────────────────────────────────────────────────────────────────

func runLookup(args []string) int {
	fs := flag.NewFlagSet("lookup", flag.ContinueOnError)
	fs.SetOutput(os.Stderr)

	sources := fs.String("sources", "cn,hk", "comma-separated sources: cn, hk")
	ambiguityMode := fs.String("ambiguity-mode", "strict", "ambiguity mode: strict or balanced")
	jsonOut := fs.Bool("json", false, "output as JSON")
	filePath := fs.String("file", "", "read queries from file (one per line)")

	if err := fs.Parse(args); err != nil {
		return 2
	}

	conv, code := buildConverterFromFlags(*sources, *ambiguityMode)
	if code != 0 {
		return code
	}

	// Gather queries: --file > positional args > stdin.
	var queries []string
	switch {
	case *filePath != "":
		f, err := os.Open(*filePath)
		if err != nil {
			return fatalf("cannot read file: %v", err)
		}
		defer f.Close()
		queries = readLines(f)
	case fs.NArg() > 0:
		queries = fs.Args()
	case isStdinPipe():
		queries = readLines(os.Stdin)
	default:
		return fatalf("no input provided (use args, --file, or pipe)")
	}

	if len(queries) == 0 {
		return fatalf("no input provided (use args, --file, or pipe)")
	}

	results := make([]zhtw.LookupResult, len(queries))
	for i, q := range queries {
		results[i] = conv.Lookup(q)
	}

	if *jsonOut {
		writeJSON(struct {
			Results []zhtw.LookupResult `json:"results"`
		}{Results: results})
	} else {
		for i, r := range results {
			if i > 0 {
				fmt.Println()
			}
			status := "unchanged"
			if r.Changed {
				status = "changed"
			}
			fmt.Printf("%s \u2192 %s (%s)\n", r.Input, r.Output, status)
			for _, d := range r.Details {
				fmt.Printf("  [%s] %s \u2192 %s @%d\n", d.Layer, d.Source, d.Target, d.Position)
			}
		}
	}

	return 0
}

// ── helpers ─────────────────────────────────────────────────────────────────

// parseSources converts a comma-separated string to []zhtw.Source, validating each.
func parseSources(s string) ([]zhtw.Source, error) {
	parts := strings.Split(s, ",")
	var out []zhtw.Source
	for _, p := range parts {
		p = strings.TrimSpace(p)
		switch zhtw.Source(p) {
		case zhtw.SourceCn, zhtw.SourceHk:
			out = append(out, zhtw.Source(p))
		default:
			return nil, fmt.Errorf("unknown source %q (valid: cn, hk)", p)
		}
	}
	if len(out) == 0 {
		return nil, fmt.Errorf("sources must not be empty")
	}
	return out, nil
}

// parseAmbiguityMode validates an ambiguity mode string.
func parseAmbiguityMode(s string) (zhtw.AmbiguityMode, error) {
	switch zhtw.AmbiguityMode(s) {
	case zhtw.AmbiguityStrict, zhtw.AmbiguityBalanced:
		return zhtw.AmbiguityMode(s), nil
	default:
		return "", fmt.Errorf("unknown ambiguity mode %q (valid: strict, balanced)", s)
	}
}

// buildConverterFromFlags constructs a *zhtw.Converter from flag values.
// Returns (converter, 0) on success or (nil, 2) on error (after printing to stderr).
func buildConverterFromFlags(sourcesStr, modeStr string) (*zhtw.Converter, int) {
	srcs, err := parseSources(sourcesStr)
	if err != nil {
		return nil, fatalf("%v", err)
	}
	mode, err := parseAmbiguityMode(modeStr)
	if err != nil {
		return nil, fatalf("%v", err)
	}
	conv, err := zhtw.NewBuilder().Sources(srcs...).SetAmbiguityMode(mode).Build()
	if err != nil {
		return nil, fatalf("building converter: %v", err)
	}
	return conv, 0
}

// isStdinPipe returns true when stdin is a pipe (not a terminal).
func isStdinPipe() bool {
	fi, err := os.Stdin.Stat()
	if err != nil {
		return false
	}
	return fi.Mode()&os.ModeCharDevice == 0
}

// readLines reads non-empty, trimmed lines from r.
func readLines(r io.Reader) []string {
	var lines []string
	sc := bufio.NewScanner(r)
	for sc.Scan() {
		line := strings.TrimSpace(sc.Text())
		if line != "" {
			lines = append(lines, line)
		}
	}
	return lines
}

// writeJSON encodes v as pretty JSON to stdout with HTML escaping disabled.
func writeJSON(v any) {
	enc := json.NewEncoder(os.Stdout)
	enc.SetEscapeHTML(false)
	enc.SetIndent("", "  ")
	_ = enc.Encode(v)
}

// fatalf prints a formatted error to stderr and returns exit code 2.
func fatalf(format string, args ...any) int {
	fmt.Fprintf(os.Stderr, "zhtw: "+format+"\n", args...)
	return 2
}

// resolveVersion returns the binary version string.
// Priority: (1) -ldflags -X main.version (2) debug.ReadBuildInfo (3) "dev".
func resolveVersion() string {
	if version != "" {
		return version
	}
	if info, ok := debug.ReadBuildInfo(); ok && info.Main.Version != "" && info.Main.Version != "(devel)" {
		return info.Main.Version
	}
	return "dev"
}
