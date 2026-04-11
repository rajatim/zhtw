package zhtw

import (
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

	covered := c.ac.getCoveredPositions(runes)
	hits := c.ac.findTermMatches(runes)
	layersEnabled := c.charLayerEnabled || c.balancedDefaults != nil

	if len(hits) == 0 {
		if layersEnabled {
			return applyLayersSkipping(runes, c.charMap, c.balancedDefaults, covered, 0)
		}
		return text
	}

	// Gap mode: term targets inserted verbatim; gaps get char/balanced layers.
	var buf strings.Builder
	buf.Grow(len(text))
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

// Check scans text for simplified Chinese terms/characters and returns match info.
// Output order: term matches first, then balanced defaults, then charmap.
// This order is NOT sorted by position — it matches all other SDKs.
func (c *Converter) Check(text string) []Match {
	if text == "" {
		return []Match{}
	}
	runes := []rune(text)

	covered := c.ac.getCoveredPositions(runes)
	hits := c.ac.findTermMatches(runes)

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

	covered := c.ac.getCoveredPositions(runes)
	hits := c.ac.findTermMatches(runes)

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
		// Charmap second (only if balanced didn't change it).
		if out == r {
			if mapped, ok := charMap[r]; ok {
				out = mapped
			}
		}
		buf.WriteRune(out)
	}
	return buf.String()
}
