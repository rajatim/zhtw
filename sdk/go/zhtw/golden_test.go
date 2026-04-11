package zhtw

import (
	"encoding/json"
	"os"
	"testing"
)

// ── Golden test fixture types ───────────────────────────────────────────────

type goldenFile struct {
	Convert []goldenConvert `json:"convert"`
	Check   []goldenCheck   `json:"check"`
	Lookup  []goldenLookup  `json:"lookup"`
}

type goldenConvert struct {
	Input         string   `json:"input"`
	Sources       []string `json:"sources"`
	Expected      string   `json:"expected"`
	AmbiguityMode string   `json:"ambiguity_mode,omitempty"`
}

type goldenCheck struct {
	Input           string        `json:"input"`
	Sources         []string      `json:"sources"`
	ExpectedMatches []goldenMatch `json:"expected_matches"`
	AmbiguityMode   string        `json:"ambiguity_mode,omitempty"`
}

type goldenMatch struct {
	Start  int    `json:"start"`
	End    int    `json:"end"`
	Source string `json:"source"`
	Target string `json:"target"`
}

type goldenLookup struct {
	Input           string         `json:"input"`
	Sources         []string       `json:"sources"`
	ExpectedOutput  string         `json:"expected_output"`
	ExpectedChanged bool           `json:"expected_changed"`
	ExpectedDetails []goldenDetail `json:"expected_details"`
	AmbiguityMode   string         `json:"ambiguity_mode,omitempty"`
}

type goldenDetail struct {
	Source   string `json:"source"`
	Target   string `json:"target"`
	Layer    string `json:"layer"`
	Position int    `json:"position"`
}

// ── Helpers ─────────────────────────────────────────────────────────────────

func loadGolden(t *testing.T) goldenFile {
	t.Helper()
	raw, err := os.ReadFile("../../data/golden-test.json")
	if err != nil {
		t.Fatalf("cannot read golden-test.json: %v", err)
	}
	var gf goldenFile
	if err := json.Unmarshal(raw, &gf); err != nil {
		t.Fatalf("cannot parse golden-test.json: %v", err)
	}
	return gf
}

func toSources(ss []string) []Source {
	out := make([]Source, len(ss))
	for i, s := range ss {
		out[i] = Source(s)
	}
	return out
}

func buildGoldenConverter(t *testing.T, sources []string, ambiguityMode string) *Converter {
	t.Helper()
	b := NewBuilder().Sources(toSources(sources)...)
	if ambiguityMode == "balanced" {
		b.SetAmbiguityMode(AmbiguityBalanced)
	}
	conv, err := b.Build()
	if err != nil {
		t.Fatalf("Build() error: %v", err)
	}
	return conv
}

// ── Convert tests ───────────────────────────────────────────────────────────

func TestGoldenConvert(t *testing.T) {
	gf := loadGolden(t)
	for i, tc := range gf.Convert {
		conv := buildGoldenConverter(t, tc.Sources, tc.AmbiguityMode)
		got := conv.Convert(tc.Input)
		if got != tc.Expected {
			t.Errorf("convert[%d] input=%q sources=%v mode=%q\n  got:  %q\n  want: %q",
				i, tc.Input, tc.Sources, tc.AmbiguityMode, got, tc.Expected)
		}
	}
}

// ── Check tests ─────────────────────────────────────────────────────────────

func TestGoldenCheck(t *testing.T) {
	gf := loadGolden(t)
	for i, tc := range gf.Check {
		conv := buildGoldenConverter(t, tc.Sources, tc.AmbiguityMode)
		got := conv.Check(tc.Input)

		if len(got) != len(tc.ExpectedMatches) {
			t.Errorf("check[%d] input=%q sources=%v mode=%q\n  got %d matches, want %d\n  got:  %+v\n  want: %+v",
				i, tc.Input, tc.Sources, tc.AmbiguityMode,
				len(got), len(tc.ExpectedMatches), got, tc.ExpectedMatches)
			continue
		}
		for j, exp := range tc.ExpectedMatches {
			g := got[j]
			if g.Start != exp.Start || g.End != exp.End || g.Source != exp.Source || g.Target != exp.Target {
				t.Errorf("check[%d] match[%d] input=%q\n  got:  {%d,%d,%q,%q}\n  want: {%d,%d,%q,%q}",
					i, j, tc.Input,
					g.Start, g.End, g.Source, g.Target,
					exp.Start, exp.End, exp.Source, exp.Target)
			}
		}
	}
}

// ── Lookup tests ────────────────────────────────────────────────────────────

func TestGoldenLookup(t *testing.T) {
	gf := loadGolden(t)
	for i, tc := range gf.Lookup {
		conv := buildGoldenConverter(t, tc.Sources, tc.AmbiguityMode)
		got := conv.Lookup(tc.Input)

		if got.Output != tc.ExpectedOutput {
			t.Errorf("lookup[%d] input=%q output: got %q, want %q",
				i, tc.Input, got.Output, tc.ExpectedOutput)
		}
		if got.Changed != tc.ExpectedChanged {
			t.Errorf("lookup[%d] input=%q changed: got %v, want %v",
				i, tc.Input, got.Changed, tc.ExpectedChanged)
		}
		if len(got.Details) != len(tc.ExpectedDetails) {
			t.Errorf("lookup[%d] input=%q\n  got %d details, want %d\n  got:  %+v\n  want: %+v",
				i, tc.Input, len(got.Details), len(tc.ExpectedDetails), got.Details, tc.ExpectedDetails)
			continue
		}
		for j, exp := range tc.ExpectedDetails {
			g := got.Details[j]
			if g.Source != exp.Source || g.Target != exp.Target || g.Layer != exp.Layer || g.Position != exp.Position {
				t.Errorf("lookup[%d] detail[%d] input=%q\n  got:  {%q,%q,%q,%d}\n  want: {%q,%q,%q,%d}",
					i, j, tc.Input,
					g.Source, g.Target, g.Layer, g.Position,
					exp.Source, exp.Target, exp.Layer, exp.Position)
			}
		}
	}
}
