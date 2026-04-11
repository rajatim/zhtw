package zhtw

import (
	"strings"
	"testing"
)

func TestACBasicMatch(t *testing.T) {
	ac := buildAhoCorasick([]acPattern{
		{source: "ab", target: "AB", runeLen: 2},
		{source: "bc", target: "BC", runeLen: 2},
	})
	runes := []rune("abc")
	hits := ac.iterEmissions(runes)

	// "ab" matches at [0,2), "bc" matches at [1,3) — both overlapping
	if len(hits) < 2 {
		t.Fatalf("expected at least 2 hits, got %d", len(hits))
	}
}

func TestACCJKMatch(t *testing.T) {
	ac := buildAhoCorasick([]acPattern{
		{source: "\u8f6f\u4ef6", target: "\u8edf\u9ad4", runeLen: 2}, // 软件→軟體
		{source: "\u6d4b\u8bd5", target: "\u6e2c\u8a66", runeLen: 2}, // 测试→測試
	})
	runes := []rune("\u8f6f\u4ef6\u6d4b\u8bd5") // 软件测试
	hits := ac.iterEmissions(runes)

	if len(hits) != 2 {
		t.Fatalf("expected 2 hits, got %d", len(hits))
	}
	if hits[0].source != "\u8f6f\u4ef6" || hits[0].start != 0 || hits[0].end != 2 {
		t.Errorf("hit[0] = %+v", hits[0])
	}
	if hits[1].source != "\u6d4b\u8bd5" || hits[1].start != 2 || hits[1].end != 4 {
		t.Errorf("hit[1] = %+v", hits[1])
	}
}

func TestFindTermMatchesBasic(t *testing.T) {
	ac := buildAhoCorasick([]acPattern{
		{source: "\u8f6f\u4ef6", target: "\u8edf\u9ad4", runeLen: 2}, // 软件→軟體
		{source: "\u6d4b\u8bd5", target: "\u6e2c\u8a66", runeLen: 2}, // 测试→測試
	})
	runes := []rune("\u8f6f\u4ef6\u6d4b\u8bd5") // 软件测试
	matches := ac.findTermMatches(runes)

	if len(matches) != 2 {
		t.Fatalf("expected 2 matches, got %d", len(matches))
	}
	if matches[0].source != "\u8f6f\u4ef6" || matches[0].start != 0 || matches[0].end != 2 {
		t.Errorf("match[0] = %+v", matches[0])
	}
	if matches[1].source != "\u6d4b\u8bd5" || matches[1].start != 2 || matches[1].end != 4 {
		t.Errorf("match[1] = %+v", matches[1])
	}
}

func TestFindTermMatchesLongestWins(t *testing.T) {
	ac := buildAhoCorasick([]acPattern{
		{source: "\u4e91", target: "\u96f2", runeLen: 1},                                // 云→雲 (short)
		{source: "\u4e91\u8ba1\u7b97", target: "\u96f2\u7aef\u904b\u7b97", runeLen: 3}, // 云计算→雲端運算 (long)
	})
	runes := []rune("\u4e91\u8ba1\u7b97") // 云计算
	matches := ac.findTermMatches(runes)

	if len(matches) != 1 {
		t.Fatalf("expected 1 match, got %d", len(matches))
	}
	if matches[0].source != "\u4e91\u8ba1\u7b97" {
		t.Errorf("expected longest match, got %q", matches[0].source)
	}
}

func TestFindTermMatchesIdentityProtection(t *testing.T) {
	// "檔案" is identity (protects positions 0-1).
	// "文檔" overlaps position 0, so it should be blocked.
	ac := buildAhoCorasick([]acPattern{
		{source: "\u6587\u6a94", target: "\u6587\u4ef6", runeLen: 2}, // 文檔→文件
		{source: "\u6a94\u6848", target: "\u6a94\u6848", runeLen: 2}, // 檔案→檔案 (identity)
	})
	runes := []rune("\u6a94\u6848") // 檔案
	matches := ac.findTermMatches(runes)

	// Identity match covers positions 0-1 but is not emitted.
	if len(matches) != 0 {
		t.Fatalf("expected 0 non-identity matches, got %d: %+v", len(matches), matches)
	}
}

func TestConverterConvertBasic(t *testing.T) {
	conv := mustBuildTestConverter([]Source{SourceCn, SourceHk}, nil, AmbiguityStrict)

	tests := []struct {
		input    string
		expected string
	}{
		{"", ""},
		{"\u8f6f\u4ef6\u6d4b\u8bd5", "\u8edf\u9ad4\u6e2c\u8a66"},                       // 软件测试 → 軟體測試
		{"\u5df2\u7d93\u662f\u7e41\u9ad4", "\u5df2\u7d93\u662f\u7e41\u9ad4"},             // 已經是繁體 (unchanged)
		{"hello", "hello"},                                                                 // ASCII pass-through
		{"\u6570\u636e\u5e93\u670d\u52a1\u5668", "\u8cc7\u6599\u5eab\u4f3a\u670d\u5668"}, // 数据库服务器 → 資料庫伺服器
	}
	for _, tt := range tests {
		got := conv.Convert(tt.input)
		if got != tt.expected {
			t.Errorf("Convert(%q) = %q, want %q", tt.input, got, tt.expected)
		}
	}
}

func mustBuildTestConverter(sources []Source, customDict map[string]string, mode AmbiguityMode) *Converter {
	data := getParsedData()
	conv, err := buildConverter(data, sources, customDict, mode)
	if err != nil {
		panic(err)
	}
	return conv
}

func TestConverterCheck(t *testing.T) {
	conv := mustBuildTestConverter([]Source{SourceCn}, nil, AmbiguityStrict)
	matches := conv.Check("\u8f6f\u4ef6\u6d4b\u8bd5") // 软件测试

	if len(matches) != 2 {
		t.Fatalf("expected 2 matches, got %d: %+v", len(matches), matches)
	}
	// 软件→軟體 at [0,2)
	if matches[0].Start != 0 || matches[0].End != 2 || matches[0].Source != "\u8f6f\u4ef6" {
		t.Errorf("match[0] = %+v", matches[0])
	}
	// 测试→測試 at [2,4)
	if matches[1].Start != 2 || matches[1].End != 4 || matches[1].Source != "\u6d4b\u8bd5" {
		t.Errorf("match[1] = %+v", matches[1])
	}
}

func TestConverterCheckEmpty(t *testing.T) {
	conv := mustBuildTestConverter([]Source{SourceCn}, nil, AmbiguityStrict)
	matches := conv.Check("")

	if len(matches) != 0 {
		t.Errorf("expected 0 matches for empty string, got %d", len(matches))
	}
}

func TestConverterLookup(t *testing.T) {
	conv := mustBuildTestConverter([]Source{SourceCn}, nil, AmbiguityStrict)
	result := conv.Lookup("\u8f6f\u4ef6") // 软件

	if result.Input != "\u8f6f\u4ef6" || result.Output != "\u8edf\u9ad4" || !result.Changed {
		t.Errorf("Lookup = %+v", result)
	}
	if len(result.Details) != 1 {
		t.Fatalf("expected 1 detail, got %d", len(result.Details))
	}
	d := result.Details[0]
	if d.Layer != "term" || d.Position != 0 || d.Source != "\u8f6f\u4ef6" || d.Target != "\u8edf\u9ad4" {
		t.Errorf("detail = %+v", d)
	}
}

func TestConverterLookupUnchanged(t *testing.T) {
	conv := mustBuildTestConverter([]Source{SourceCn}, nil, AmbiguityStrict)
	result := conv.Lookup("\u53f0") // 台 — ambiguous, no conversion in strict mode

	if result.Changed {
		t.Errorf("expected unchanged, got output=%q", result.Output)
	}
	if len(result.Details) != 0 {
		t.Errorf("expected 0 details, got %d", len(result.Details))
	}
}

func TestDataLoading(t *testing.T) {
	data := getParsedData()
	if data == nil {
		t.Fatal("getParsedData() returned nil")
	}
	// charMap should have entries (thousands of simplified→traditional mappings).
	if len(data.charMap) < 100 {
		t.Errorf("charMap too small: %d entries", len(data.charMap))
	}
	// terms.cn should have entries.
	if len(data.termsCn) < 100 {
		t.Errorf("termsCn too small: %d entries", len(data.termsCn))
	}
	// balancedDefaults should have 10 entries.
	if len(data.balancedDefaults) != 10 {
		t.Errorf("balancedDefaults: expected 10, got %d", len(data.balancedDefaults))
	}
}

func TestBuilderDefault(t *testing.T) {
	conv, err := NewBuilder().Build()
	if err != nil {
		t.Fatal(err)
	}
	got := conv.Convert("\u8f6f\u4ef6\u6d4b\u8bd5") // 软件测试
	if got != "\u8edf\u9ad4\u6e2c\u8a66" {            // 軟體測試
		t.Errorf("got %q", got)
	}
}

func TestBuilderCustomDict(t *testing.T) {
	conv, err := NewBuilder().
		Sources(SourceCn).
		CustomDict(map[string]string{"\u81ea\u5b9a\u4e49": "\u81ea\u8a02"}).
		Build()
	if err != nil {
		t.Fatal(err)
	}
	got := conv.Convert("\u81ea\u5b9a\u4e49") // 自定义 → 自訂
	if got != "\u81ea\u8a02" {
		t.Errorf("got %q", got)
	}
}

func TestBuilderEmptySourcesError(t *testing.T) {
	_, err := NewBuilder().Sources().Build()
	if err == nil {
		t.Fatal("expected error for empty sources")
	}
}

func TestBuilderBalancedMode(t *testing.T) {
	conv, err := NewBuilder().
		Sources(SourceCn).
		SetAmbiguityMode(AmbiguityBalanced).
		Build()
	if err != nil {
		t.Fatal(err)
	}
	// "以后再说" → "以後再說" in balanced mode
	got := conv.Convert("\u4ee5\u540e\u518d\u8bf4")
	if got != "\u4ee5\u5f8c\u518d\u8aaa" {
		t.Errorf("got %q", got)
	}
}

func TestConvenienceConvert(t *testing.T) {
	got := Convert("\u8f6f\u4ef6\u6d4b\u8bd5") // 软件测试
	want := "\u8edf\u9ad4\u6e2c\u8a66"          // 軟體測試
	if got != want {
		t.Errorf("Convert() = %q, want %q", got, want)
	}
}

func TestConvenienceCheck(t *testing.T) {
	matches := Check("\u8f6f\u4ef6") // 软件
	if len(matches) < 1 {
		t.Fatalf("expected at least 1 match, got %d", len(matches))
	}
}

func TestConvenienceLookup(t *testing.T) {
	result := Lookup("\u8f6f\u4ef6") // 软件
	if !result.Changed {
		t.Error("expected changed=true")
	}
}

func TestDataVersion(t *testing.T) {
	v := DataVersion()
	if v == "" {
		t.Fatal("DataVersion() returned empty string")
	}
	parts := strings.Split(v, ".")
	if len(parts) != 3 {
		t.Fatalf("DataVersion() = %q, want X.Y.Z format", v)
	}
}
