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
