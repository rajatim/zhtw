// Package zhtw converts simplified Chinese text to Traditional Chinese (Taiwan).
package zhtw

// Source identifies a dictionary source.
type Source string

const (
	SourceCn Source = "cn"
	SourceHk Source = "hk"
)

// AmbiguityMode controls how ambiguous characters are handled.
type AmbiguityMode string

const (
	AmbiguityStrict   AmbiguityMode = "strict"
	AmbiguityBalanced AmbiguityMode = "balanced"
)

// Match represents a detected simplified Chinese segment in the input text.
type Match struct {
	Start  int    `json:"start"`  // Unicode codepoint index, inclusive
	End    int    `json:"end"`    // Unicode codepoint index, exclusive
	Source string `json:"source"` // Original simplified text
	Target string `json:"target"` // Converted traditional text
}

// LookupResult contains detailed conversion information for a word or phrase.
type LookupResult struct {
	Input   string             `json:"input"`
	Output  string             `json:"output"`
	Changed bool               `json:"changed"`
	Details []ConversionDetail `json:"details"`
}

// ConversionDetail describes one conversion within a lookup result.
type ConversionDetail struct {
	Source   string `json:"source"`
	Target   string `json:"target"`
	Layer    string `json:"layer"`    // "term" or "char"
	Position int    `json:"position"` // Unicode codepoint index
}

// ExplainEvent describes why one rule was applied, protected, or skipped.
type ExplainEvent struct {
	RuleID      string `json:"rule_id"`
	Layer       string `json:"layer"`
	Outcome     string `json:"outcome"`
	InputStart  int    `json:"input_start"`
	InputEnd    int    `json:"input_end"`
	OutputStart int    `json:"output_start"`
	OutputEnd   int    `json:"output_end"`
	Source      string `json:"source"`
	Target      string `json:"target"`
	ReasonCode  string `json:"reason_code"`
}

// ExplainResult contains converted output and stable rule events.
type ExplainResult struct {
	Output string         `json:"output"`
	Events []ExplainEvent `json:"events"`
}
