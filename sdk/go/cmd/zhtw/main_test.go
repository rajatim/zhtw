package main_test

import (
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
	"strings"
	"testing"
)

var binaryPath string

func TestMain(m *testing.M) {
	tmp, err := os.MkdirTemp("", "zhtw-cli-test")
	if err != nil {
		panic(err)
	}
	exe := "zhtw"
	if runtime.GOOS == "windows" {
		exe = "zhtw.exe"
	}
	binaryPath = filepath.Join(tmp, exe)
	cmd := exec.Command("go", "build", "-o", binaryPath, ".")
	cmd.Dir = "."
	if out, err := cmd.CombinedOutput(); err != nil {
		panic("failed to build CLI: " + string(out))
	}
	code := m.Run()
	os.RemoveAll(tmp)
	os.Exit(code)
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
		t.Fatalf("unexpected error: %v", err)
	}
	return outBuf.String(), errBuf.String(), exitCode
}

// ── Exit code tests ────────────────────────────────────────────────────────

func TestVersionExitCode(t *testing.T) {
	stdout, _, code := runCLI(t, "", "version")
	if code != 0 {
		t.Fatalf("want exit 0, got %d", code)
	}
	if !strings.Contains(stdout, "zhtw") {
		t.Errorf("stdout should contain 'zhtw', got %q", stdout)
	}
	if !strings.Contains(stdout, "data") {
		t.Errorf("stdout should contain 'data', got %q", stdout)
	}
}

func TestNoArgsExitCode(t *testing.T) {
	_, _, code := runCLI(t, "")
	if code != 2 {
		t.Fatalf("want exit 2, got %d", code)
	}
}

func TestUnknownCommandExitCode(t *testing.T) {
	_, stderr, code := runCLI(t, "", "badcommand")
	if code != 2 {
		t.Fatalf("want exit 2, got %d", code)
	}
	if !strings.Contains(stderr, "unknown command") {
		t.Errorf("stderr should contain 'unknown command', got %q", stderr)
	}
}

func TestConvertExitZero(t *testing.T) {
	_, _, code := runCLI(t, "", "convert", "软件测试")
	if code != 0 {
		t.Fatalf("want exit 0, got %d", code)
	}
}

func TestConvertCheckChanged(t *testing.T) {
	_, _, code := runCLI(t, "", "convert", "--check", "软件")
	if code != 1 {
		t.Fatalf("want exit 1, got %d", code)
	}
}

func TestConvertCheckUnchanged(t *testing.T) {
	_, _, code := runCLI(t, "", "convert", "--check", "hello")
	if code != 0 {
		t.Fatalf("want exit 0, got %d", code)
	}
}

func TestConvertNoInput(t *testing.T) {
	_, _, code := runCLI(t, "", "convert")
	if code != 2 {
		t.Fatalf("want exit 2, got %d", code)
	}
}

func TestLookupExitZero(t *testing.T) {
	_, _, code := runCLI(t, "", "lookup", "软件")
	if code != 0 {
		t.Fatalf("want exit 0, got %d", code)
	}
}

// ── JSON golden tests ──────────────────────────────────────────────────────

func TestLookupJSONGolden(t *testing.T) {
	golden, err := os.ReadFile("testdata/lookup_software.json")
	if err != nil {
		t.Fatalf("read golden: %v", err)
	}
	stdout, _, code := runCLI(t, "", "lookup", "--json", "软件")
	if code != 0 {
		t.Fatalf("want exit 0, got %d", code)
	}
	if stdout != string(golden) {
		t.Errorf("output mismatch\ngot:\n%s\nwant:\n%s", stdout, string(golden))
	}
}

func TestConvertJSONGolden(t *testing.T) {
	golden, err := os.ReadFile("testdata/convert_software_test.json")
	if err != nil {
		t.Fatalf("read golden: %v", err)
	}
	stdout, _, code := runCLI(t, "", "convert", "--json", "软件测试")
	if code != 0 {
		t.Fatalf("want exit 0, got %d", code)
	}
	if stdout != string(golden) {
		t.Errorf("output mismatch\ngot:\n%s\nwant:\n%s", stdout, string(golden))
	}
}

// ── Input source tests ─────────────────────────────────────────────────────

func TestConvertArgs(t *testing.T) {
	stdout, _, code := runCLI(t, "", "convert", "软件", "测试")
	if code != 0 {
		t.Fatalf("want exit 0, got %d", code)
	}
	// Args have no trailing newline, so output is exactly "軟體 測試\n".
	if stdout != "軟體 測試\n" {
		t.Errorf("want %q, got %q", "軟體 測試\n", stdout)
	}
}

func TestConvertStdin(t *testing.T) {
	// Piped stdin typically ends with \n; output should have exactly one trailing newline.
	stdout, _, code := runCLI(t, "用户权限\n", "convert")
	if code != 0 {
		t.Fatalf("want exit 0, got %d", code)
	}
	if stdout != "使用者權限\n" {
		t.Errorf("want %q, got %q", "使用者權限\n", stdout)
	}
}

func TestConvertFile(t *testing.T) {
	tmp, err := os.CreateTemp("", "zhtw-input-*.txt")
	if err != nil {
		t.Fatalf("create temp file: %v", err)
	}
	defer os.Remove(tmp.Name())
	// File content ends with \n (typical for text files).
	if _, err := tmp.WriteString("软件测试\n"); err != nil {
		t.Fatalf("write temp file: %v", err)
	}
	tmp.Close()

	stdout, _, code := runCLI(t, "", "convert", "--file", tmp.Name())
	if code != 0 {
		t.Fatalf("want exit 0, got %d", code)
	}
	if stdout != "軟體測試\n" {
		t.Errorf("want %q, got %q", "軟體測試\n", stdout)
	}
}

func TestLookupStdinMultiline(t *testing.T) {
	stdout, _, code := runCLI(t, "软件\n测试\n", "lookup", "--json")
	if code != 0 {
		t.Fatalf("want exit 0, got %d", code)
	}
	// Should contain both lookup results.
	if !strings.Contains(stdout, `"input": "软件"`) {
		t.Error("output should contain lookup result for 软件")
	}
	if !strings.Contains(stdout, `"input": "测试"`) {
		t.Error("output should contain lookup result for 测试")
	}
}

// ── Flag parsing tests ─────────────────────────────────────────────────────

func TestConvertSourcesCn(t *testing.T) {
	stdout, _, code := runCLI(t, "", "convert", "--sources", "cn", "软件测试")
	if code != 0 {
		t.Fatalf("want exit 0, got %d", code)
	}
	got := strings.TrimSpace(stdout)
	if got != "軟體測試" {
		t.Errorf("want %q, got %q", "軟體測試", got)
	}
}

func TestConvertBadSources(t *testing.T) {
	_, stderr, code := runCLI(t, "", "convert", "--sources", "xx", "test")
	if code != 2 {
		t.Fatalf("want exit 2, got %d", code)
	}
	if !strings.Contains(stderr, "unknown source") {
		t.Errorf("stderr should contain 'unknown source', got %q", stderr)
	}
}

func TestConvertBalancedMode(t *testing.T) {
	stdout, _, code := runCLI(t, "", "convert", "--ambiguity-mode", "balanced", "几个里程碑")
	if code != 0 {
		t.Fatalf("want exit 0, got %d", code)
	}
	if !strings.Contains(stdout, "幾") {
		t.Errorf("output should contain '幾', got %q", stdout)
	}
}
