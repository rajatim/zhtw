package zhtw

import (
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
