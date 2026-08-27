package zhtw

import (
	"encoding/json"
	"errors"
	"os"
	"reflect"
	"testing"
)

// ── Golden test fixture types ───────────────────────────────────────────────

type goldenFile struct {
	Convert []goldenConvert `json:"convert"`
	Check   []goldenCheck   `json:"check"`
	Lookup  []goldenLookup  `json:"lookup"`
	Explain []goldenExplain `json:"explain"`
}

type goldenExplain struct {
	Input          string         `json:"input"`
	Sources        []string       `json:"sources"`
	ExpectedOutput string         `json:"expected_output"`
	ExpectedEvents []ExplainEvent `json:"expected_events"`
	AmbiguityMode  string         `json:"ambiguity_mode,omitempty"`
}

type jsonAdapterGolden struct {
	Version string            `json:"version"`
	Cases   []jsonAdapterCase `json:"cases"`
	Reject  []jsonRejectCase  `json:"reject"`
}

type jsonAdapterCase struct {
	ID            string   `json:"id"`
	Input         string   `json:"input"`
	Sources       []string `json:"sources"`
	Expected      string   `json:"expected"`
	AmbiguityMode string   `json:"ambiguity_mode,omitempty"`
}

type jsonRejectCase struct {
	ID        string `json:"id"`
	Input     string `json:"input"`
	ErrorCode string `json:"error_code"`
}

type goldenConvert struct {
	ID            string   `json:"id,omitempty"`
	Input         string   `json:"input"`
	Sources       []string `json:"sources"`
	Expected      string   `json:"expected"`
	AmbiguityMode string   `json:"ambiguity_mode,omitempty"`
}

func TestApprovedConformance(t *testing.T) {
	raw, err := os.ReadFile("../../data/conformance-v1.json")
	if err != nil {
		t.Fatal(err)
	}
	var fixture goldenFile
	if err := json.Unmarshal(raw, &fixture); err != nil {
		t.Fatal(err)
	}
	for _, tc := range fixture.Convert {
		conv := buildGoldenConverter(t, tc.Sources, tc.AmbiguityMode)
		if got := conv.Convert(tc.Input); got != tc.Expected {
			t.Errorf("conformance %s: got %q, want %q", tc.ID, got, tc.Expected)
		}
	}
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

func TestGoldenExplain(t *testing.T) {
	gf := loadGolden(t)
	for _, tc := range gf.Explain {
		conv := buildGoldenConverter(t, tc.Sources, tc.AmbiguityMode)
		got := conv.Explain(tc.Input)
		if got.Output != tc.ExpectedOutput {
			t.Errorf("explain input=%q output: got %q, want %q", tc.Input, got.Output, tc.ExpectedOutput)
		}
		if got.Output != conv.Convert(tc.Input) {
			t.Errorf("explain input=%q diverged from Convert", tc.Input)
		}
		if !reflect.DeepEqual(got.Events, tc.ExpectedEvents) {
			t.Errorf("explain input=%q events differ\n  got:  %+v\n  want: %+v", tc.Input, got.Events, tc.ExpectedEvents)
		}
	}
}

func TestJSONAdapterGolden(t *testing.T) {
	raw, err := os.ReadFile("../../data/json-adapter-golden.json")
	if err != nil {
		t.Fatal(err)
	}
	var fixture jsonAdapterGolden
	if err := json.Unmarshal(raw, &fixture); err != nil {
		t.Fatal(err)
	}
	if fixture.Version != DataVersion() {
		t.Fatalf("fixture version %s does not match data version %s", fixture.Version, DataVersion())
	}
	for _, tc := range fixture.Cases {
		conv := buildGoldenConverter(t, tc.Sources, tc.AmbiguityMode)
		got, err := conv.ConvertJSON(tc.Input)
		if err != nil {
			t.Errorf("JSON adapter case %s returned error: %v", tc.ID, err)
			continue
		}
		if got != tc.Expected {
			t.Errorf("JSON adapter case %s: got %q, want %q", tc.ID, got, tc.Expected)
		}
	}
	for _, tc := range fixture.Reject {
		_, err := ConvertJSON(tc.Input)
		var adapterError *JSONAdapterError
		if !errors.As(err, &adapterError) {
			t.Errorf("JSON adapter reject %s: got %v, want JSONAdapterError", tc.ID, err)
			continue
		}
		if adapterError.Code != tc.ErrorCode {
			t.Errorf("JSON adapter reject %s: got code %s, want %s", tc.ID, adapterError.Code, tc.ErrorCode)
		}
	}
}
