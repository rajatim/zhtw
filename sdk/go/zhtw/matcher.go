package zhtw

import "sort"

// ── Internal types ──────────────────────────────────────────────────────────

type acPattern struct {
	source  string
	target  string
	runeLen int // len([]rune(source)), precomputed
}

type acMatch struct {
	start  int // rune index, inclusive
	end    int // rune index, exclusive
	source string
	target string
}

type acNode struct {
	children map[rune]*acNode
	fail     *acNode
	outputs  []int // indices into ahoCorasick.patterns
}

type ahoCorasick struct {
	root     *acNode
	patterns []acPattern
}

// ── Construction ────────────────────────────────────────────────────────────

func newACNode() *acNode {
	return &acNode{children: make(map[rune]*acNode)}
}

func buildAhoCorasick(patterns []acPattern) *ahoCorasick {
	ac := &ahoCorasick{
		root:     newACNode(),
		patterns: patterns,
	}
	// Insert patterns into trie.
	for idx, pat := range patterns {
		node := ac.root
		for _, r := range pat.source {
			next, ok := node.children[r]
			if !ok {
				next = newACNode()
				node.children[r] = next
			}
			node = next
		}
		node.outputs = append(node.outputs, idx)
	}
	// Build failure links (BFS).
	queue := make([]*acNode, 0)
	for _, child := range ac.root.children {
		child.fail = ac.root
		queue = append(queue, child)
	}
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		for r, child := range node.children {
			queue = append(queue, child)
			f := node.fail
			for f != nil && f.children[r] == nil {
				f = f.fail
			}
			if f == nil {
				child.fail = ac.root
			} else if next, ok := f.children[r]; ok {
				child.fail = next
			} else {
				child.fail = ac.root
			}
			// Merge output-link patterns from fail node.
			if len(child.fail.outputs) > 0 {
				merged := make([]int, len(child.outputs)+len(child.fail.outputs))
				copy(merged, child.outputs)
				copy(merged[len(child.outputs):], child.fail.outputs)
				child.outputs = merged
			}
		}
	}
	return ac
}

// ── Raw emissions ───────────────────────────────────────────────────────────

// iterEmissions returns ALL overlapping AC hits (rune-indexed).
func (ac *ahoCorasick) iterEmissions(runes []rune) []acMatch {
	var hits []acMatch
	node := ac.root
	for i, r := range runes {
		for node != ac.root && node.children[r] == nil {
			node = node.fail
		}
		if next, ok := node.children[r]; ok {
			node = next
		}
		for _, idx := range node.outputs {
			pat := ac.patterns[idx]
			start := i + 1 - pat.runeLen
			hits = append(hits, acMatch{
				start:  start,
				end:    i + 1,
				source: pat.source,
				target: pat.target,
			})
		}
	}
	return hits
}

// ── Covered positions ───────────────────────────────────────────────────────

// getCoveredPositions returns all rune indices covered by any raw AC hit,
// including identity terms (source == target). Used to prevent char/balanced
// layers from converting characters protected by term matches.
func (ac *ahoCorasick) getCoveredPositions(runes []rune) map[int]bool {
	covered := make(map[int]bool)
	for _, m := range ac.iterEmissions(runes) {
		for i := m.start; i < m.end; i++ {
			covered[i] = true
		}
	}
	return covered
}

// ── Match selection ──────────────────────────────────────────────────────────

// findTermMatches returns non-overlapping, leftmost-longest term matches
// with identity-based protection. Identity terms (source == target) advance
// the cursor but are never emitted. Non-identity terms overlapping a
// protected position are skipped without advancing the cursor.
//
// Mirrors Python src/zhtw/matcher.py:find_matches.
func (ac *ahoCorasick) findTermMatches(runes []rune) []acMatch {
	raw := ac.iterEmissions(runes)
	if len(raw) == 0 {
		return nil
	}

	// Sort by (start ASC, length DESC).
	sort.Slice(raw, func(i, j int) bool {
		if raw[i].start != raw[j].start {
			return raw[i].start < raw[j].start
		}
		lenI := raw[i].end - raw[i].start
		lenJ := raw[j].end - raw[j].start
		return lenI > lenJ
	})

	// Separate identity and non-identity hits.
	var identity []acMatch
	var nonIdentitySpans [][2]int
	for _, m := range raw {
		if m.source == m.target {
			identity = append(identity, m)
		} else {
			nonIdentitySpans = append(nonIdentitySpans, [2]int{m.start, m.end})
		}
	}

	// Build protected rune positions from identity matches not contained
	// in any non-identity span.
	protected := make(map[int]bool)
	if len(nonIdentitySpans) == 0 {
		for _, m := range identity {
			for i := m.start; i < m.end; i++ {
				protected[i] = true
			}
		}
	} else {
		sort.Slice(nonIdentitySpans, func(i, j int) bool {
			return nonIdentitySpans[i][0] < nonIdentitySpans[j][0]
		})
		// Build prefix-max-end array.
		prefixMaxEnd := make([]int, len(nonIdentitySpans))
		maxEnd := 0
		for i, span := range nonIdentitySpans {
			if span[1] > maxEnd {
				maxEnd = span[1]
			}
			prefixMaxEnd[i] = maxEnd
		}
		niStarts := make([]int, len(nonIdentitySpans))
		for i, span := range nonIdentitySpans {
			niStarts[i] = span[0]
		}
		for _, m := range identity {
			idx := bisectRight(niStarts, m.start) - 1
			contained := idx >= 0 && prefixMaxEnd[idx] >= m.end
			if !contained {
				for i := m.start; i < m.end; i++ {
					protected[i] = true
				}
			}
		}
	}

	// Left-to-right greedy filter.
	var result []acMatch
	cursor := 0
	for _, m := range raw {
		if m.start < cursor {
			continue
		}
		isIdentity := m.source == m.target
		if !isIdentity {
			overlaps := false
			for i := m.start; i < m.end; i++ {
				if protected[i] {
					overlaps = true
					break
				}
			}
			if overlaps {
				continue // skip without advancing cursor
			}
		}
		cursor = m.end
		if !isIdentity {
			result = append(result, m)
		}
	}
	return result
}

// bisectRight returns the insertion point for x in a sorted slice a
// such that all elements before the point are <= x.
func bisectRight(a []int, x int) int {
	return sort.Search(len(a), func(i int) bool { return a[i] > x })
}
