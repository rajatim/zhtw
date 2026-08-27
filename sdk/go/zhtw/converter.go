package zhtw

import (
	"fmt"
	"sort"
	"strings"
)

// Converter is a reusable simplified-to-traditional Chinese converter.
// All fields are immutable after construction; it is safe for concurrent use.
type Converter struct {
	ac               *ahoCorasick
	charMap          map[rune]rune
	balancedDefaults map[rune]rune // nil for strict mode
	charLayerEnabled bool
	ruleRecords      map[string][]ruleMeta
}

type characterChange struct {
	start      int
	end        int
	source     string
	target     string
	layer      string
	ruleID     string
	reasonCode string
}

// buildConverter creates a Converter from parsed data and configuration.
func buildConverter(
	data *parsedData,
	sources []Source,
	customDict map[string]string,
	mode AmbiguityMode,
) (*Converter, error) {
	if len(sources) == 0 {
		return nil, ErrEmptySources
	}

	// Merge terms from selected sources.
	merged := make(map[string]string)
	for _, src := range sources {
		var bucket map[string]string
		switch src {
		case SourceCn:
			bucket = data.termsCn
		case SourceHk:
			bucket = data.termsHk
		}
		for k, v := range bucket {
			if len(k) > 0 {
				merged[k] = v
			}
		}
	}
	// Custom dict overrides.
	for k, v := range customDict {
		if len(k) > 0 {
			merged[k] = v
		}
	}
	ruleRecords := make(map[string][]ruleMeta)
	for _, source := range sources {
		for term, records := range data.ruleRecords[source] {
			ruleRecords[term] = append(ruleRecords[term], records...)
		}
	}
	for source, target := range customDict {
		if source != "" {
			ruleRecords[source] = append(ruleRecords[source], ruleMeta{
				id: legacyCustomRuleID(source, target), source: source, target: target,
			})
		}
	}

	// Build sorted pattern list for deterministic automaton.
	patterns := make([]acPattern, 0, len(merged))
	for src, tgt := range merged {
		patterns = append(patterns, acPattern{
			source:  src,
			target:  tgt,
			runeLen: len([]rune(src)),
		})
	}
	sort.Slice(patterns, func(i, j int) bool {
		return patterns[i].source < patterns[j].source
	})

	ac := buildAhoCorasick(patterns)

	hasCn := false
	for _, s := range sources {
		if s == SourceCn {
			hasCn = true
			break
		}
	}

	// Balanced defaults only apply when CN source is selected.
	var balanced map[rune]rune
	if mode == AmbiguityBalanced && hasCn {
		balanced = data.balancedDefaults
	}

	return &Converter{
		ac:               ac,
		charMap:          data.charMap,
		balancedDefaults: balanced,
		charLayerEnabled: hasCn,
		ruleRecords:      ruleRecords,
	}, nil
}

// ErrEmptySources is returned when Build() is called with no sources.
var ErrEmptySources = errEmptySources{}

type errEmptySources struct{}

func (errEmptySources) Error() string { return "zhtw: sources must not be empty" }

// Convert converts simplified Chinese text to Traditional Chinese (Taiwan).
func (c *Converter) Convert(text string) string {
	if text == "" {
		return ""
	}
	runes := []rune(text)

	hits, covered := c.ac.scan(runes)
	return c.convertWithScan(runes, hits, covered)
}

func (c *Converter) convertWithScan(runes []rune, hits []acMatch, covered map[int]bool) string {
	layersEnabled := c.charLayerEnabled || c.balancedDefaults != nil

	if len(hits) == 0 {
		if layersEnabled {
			return applyLayersSkipping(runes, c.charMap, c.balancedDefaults, covered, 0)
		}
		return string(runes)
	}

	// Gap mode: term targets inserted verbatim; gaps get char/balanced layers.
	var buf strings.Builder
	buf.Grow(len(runes) * 3)
	lastEnd := 0
	for _, h := range hits {
		gap := runes[lastEnd:h.start]
		if layersEnabled {
			buf.WriteString(applyLayersSkipping(gap, c.charMap, c.balancedDefaults, covered, lastEnd))
		} else {
			for _, r := range gap {
				buf.WriteRune(r)
			}
		}
		buf.WriteString(h.target)
		lastEnd = h.end
	}
	tail := runes[lastEnd:]
	if layersEnabled {
		buf.WriteString(applyLayersSkipping(tail, c.charMap, c.balancedDefaults, covered, lastEnd))
	} else {
		for _, r := range tail {
			buf.WriteRune(r)
		}
	}
	return buf.String()
}

func (c *Converter) characterChanges(runes []rune, covered map[int]bool) []characterChange {
	changes := make([]characterChange, 0)
	for position, source := range runes {
		if covered[position] {
			continue
		}
		if c.balancedDefaults != nil {
			if balanced, ok := c.balancedDefaults[source]; ok {
				target := balanced
				if mapped, found := c.charMap[target]; found {
					target = mapped
				}
				if target != source {
					changes = append(changes, characterChange{
						start: position, end: position + 1, source: string(source), target: string(target),
						layer: "balanced", ruleID: fmt.Sprintf("balanced:u%x", source), reasonCode: "balanced_default",
					})
				}
				continue
			}
		}
		if c.charLayerEnabled {
			if target, ok := c.charMap[source]; ok && target != source {
				changes = append(changes, characterChange{
					start: position, end: position + 1, source: string(source), target: string(target),
					layer: "char", ruleID: fmt.Sprintf("charmap:u%x", source), reasonCode: "char_map",
				})
			}
		}
	}
	return changes
}

// Explain converts text and returns stable events from the same matcher scan.
func (c *Converter) Explain(text string) ExplainResult {
	if text == "" {
		return ExplainResult{Output: "", Events: []ExplainEvent{}}
	}
	runes := []rune(text)
	selected, covered, decisions := c.ac.scanDetailed(runes)
	changes := c.characterChanges(runes, covered)
	selectedByStart := make(map[int]acMatch, len(selected))
	for _, hit := range selected {
		selectedByStart[hit.start] = hit
	}
	changesByStart := make(map[int]characterChange, len(changes))
	for _, change := range changes {
		changesByStart[change.start] = change
	}
	spans := make([][2]int, len(runes))
	var output strings.Builder
	outputPosition := 0
	for inputPosition := 0; inputPosition < len(runes); {
		if hit, ok := selectedByStart[inputPosition]; ok {
			outputEnd := outputPosition + len([]rune(hit.target))
			for position := hit.start; position < hit.end; position++ {
				spans[position] = [2]int{outputPosition, outputEnd}
			}
			output.WriteString(hit.target)
			outputPosition = outputEnd
			inputPosition = hit.end
			continue
		}
		target := string(runes[inputPosition])
		if change, ok := changesByStart[inputPosition]; ok {
			target = change.target
		}
		outputEnd := outputPosition + len([]rune(target))
		spans[inputPosition] = [2]int{outputPosition, outputEnd}
		output.WriteString(target)
		outputPosition = outputEnd
		inputPosition++
	}
	converted := output.String()
	if converted != c.convertWithScan(runes, selected, covered) {
		panic("zhtw: explain trace diverged from conversion output")
	}

	events := make([]ExplainEvent, 0, len(decisions)+len(changes))
	for _, decision := range decisions {
		hit := decision.hit
		outputStart, outputEnd := spans[hit.start][0], spans[hit.start][1]
		for position := hit.start + 1; position < hit.end; position++ {
			if spans[position][0] < outputStart {
				outputStart = spans[position][0]
			}
			if spans[position][1] > outputEnd {
				outputEnd = spans[position][1]
			}
		}
		candidates := c.ruleRecords[hit.source]
		winner := -1
		for index := len(candidates) - 1; index >= 0; index-- {
			if candidates[index].target == hit.target {
				winner = index
				break
			}
		}
		ruleID := legacyCustomRuleID(hit.source, hit.target)
		if winner >= 0 {
			ruleID = candidates[winner].id
		}
		conflicts := make([]ruleMeta, 0)
		for index, record := range candidates {
			if index != winner {
				conflicts = append(conflicts, record)
			}
		}
		reasonCode := decision.reasonCode
		if decision.outcome == "applied" && len(conflicts) > 0 {
			reasonCode = "loader_conflict_winner"
		}
		layer := "term"
		if hit.source == hit.target {
			layer = "identity"
		}
		events = append(events, ExplainEvent{
			RuleID: ruleID, Layer: layer, Outcome: decision.outcome,
			InputStart: hit.start, InputEnd: hit.end, OutputStart: outputStart, OutputEnd: outputEnd,
			Source: hit.source, Target: hit.target, ReasonCode: reasonCode,
		})
		if decision.outcome == "applied" {
			for _, conflict := range conflicts {
				events = append(events, ExplainEvent{
					RuleID: conflict.id, Layer: "term", Outcome: "skipped",
					InputStart: hit.start, InputEnd: hit.end, OutputStart: outputStart, OutputEnd: outputEnd,
					Source: conflict.source, Target: conflict.target, ReasonCode: "loader_conflict_loser",
				})
			}
		}
	}
	for _, change := range changes {
		events = append(events, ExplainEvent{
			RuleID: change.ruleID, Layer: change.layer, Outcome: "applied",
			InputStart: change.start, InputEnd: change.end,
			OutputStart: spans[change.start][0], OutputEnd: spans[change.start][1],
			Source: change.source, Target: change.target, ReasonCode: change.reasonCode,
		})
	}
	outcomeOrder := func(outcome string) int {
		switch outcome {
		case "applied":
			return 0
		case "protected":
			return 1
		default:
			return 2
		}
	}
	sort.Slice(events, func(i, j int) bool {
		left, right := events[i], events[j]
		if left.InputStart != right.InputStart {
			return left.InputStart < right.InputStart
		}
		if left.InputEnd != right.InputEnd {
			return left.InputEnd < right.InputEnd
		}
		if outcomeOrder(left.Outcome) != outcomeOrder(right.Outcome) {
			return outcomeOrder(left.Outcome) < outcomeOrder(right.Outcome)
		}
		return left.RuleID < right.RuleID
	})
	return ExplainResult{Output: converted, Events: events}
}

// Check scans text for simplified Chinese terms/characters and returns match info.
// Output order: term matches first, then balanced defaults, then charmap.
// This order is NOT sorted by position — it matches all other SDKs.
func (c *Converter) Check(text string) []Match {
	if text == "" {
		return []Match{}
	}
	runes := []rune(text)

	hits, covered := c.ac.scan(runes)

	var matches []Match

	// 1. Term layer.
	for _, h := range hits {
		matches = append(matches, Match{
			Start:  h.start,
			End:    h.end,
			Source: h.source,
			Target: h.target,
		})
	}

	// 2. Balanced defaults layer (if enabled).
	if c.balancedDefaults != nil {
		for i, r := range runes {
			if covered[i] {
				continue
			}
			if mapped, ok := c.balancedDefaults[r]; ok {
				matches = append(matches, Match{
					Start:  i,
					End:    i + 1,
					Source: string(r),
					Target: string(mapped),
				})
			}
		}
	}

	// 3. Char layer (if enabled).
	if c.charLayerEnabled {
		for i, r := range runes {
			if covered[i] {
				continue
			}
			if mapped, ok := c.charMap[r]; ok && mapped != r {
				matches = append(matches, Match{
					Start:  i,
					End:    i + 1,
					Source: string(r),
					Target: string(mapped),
				})
			}
		}
	}

	return matches
}

// Lookup returns detailed conversion information for a word or phrase.
// Details are sorted by position (ascending).
func (c *Converter) Lookup(word string) LookupResult {
	if word == "" {
		return LookupResult{Input: "", Output: "", Changed: false, Details: []ConversionDetail{}}
	}
	runes := []rune(word)

	hits, covered := c.ac.scan(runes)

	var details []ConversionDetail

	// 1. Term layer.
	for _, h := range hits {
		details = append(details, ConversionDetail{
			Source:   h.source,
			Target:   h.target,
			Layer:    "term",
			Position: h.start,
		})
	}

	// 2. Balanced defaults layer (if enabled).
	if c.balancedDefaults != nil {
		for i, r := range runes {
			if covered[i] {
				continue
			}
			if mapped, ok := c.balancedDefaults[r]; ok {
				details = append(details, ConversionDetail{
					Source:   string(r),
					Target:   string(mapped),
					Layer:    "char",
					Position: i,
				})
			}
		}
	}

	// 3. Char layer (if enabled).
	if c.charLayerEnabled {
		for i, r := range runes {
			if covered[i] {
				continue
			}
			if mapped, ok := c.charMap[r]; ok && mapped != r {
				details = append(details, ConversionDetail{
					Source:   string(r),
					Target:   string(mapped),
					Layer:    "char",
					Position: i,
				})
			}
		}
	}

	// Sort by position.
	sort.Slice(details, func(i, j int) bool {
		return details[i].Position < details[j].Position
	})

	output := c.Convert(word)
	changed := output != word

	return LookupResult{
		Input:   word,
		Output:  output,
		Changed: changed,
		Details: details,
	}
}

// applyLayersSkipping applies balanced defaults then charmap to each rune
// in the segment, skipping positions that are covered by AC term hits.
// offset is the rune index of this segment's start in the original text.
func applyLayersSkipping(
	runes []rune,
	charMap map[rune]rune,
	balanced map[rune]rune,
	covered map[int]bool,
	offset int,
) string {
	var buf strings.Builder
	buf.Grow(len(runes) * 3)
	for i, r := range runes {
		if covered[offset+i] {
			buf.WriteRune(r)
			continue
		}
		out := r
		// Balanced defaults first.
		if balanced != nil {
			if mapped, ok := balanced[r]; ok {
				out = mapped
			}
		}
		// Charmap second.
		if mapped, ok := charMap[out]; ok {
			out = mapped
		}
		buf.WriteRune(out)
	}
	return buf.String()
}
