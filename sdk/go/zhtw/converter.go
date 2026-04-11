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
