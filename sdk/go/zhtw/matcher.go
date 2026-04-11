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

// ── Match selection (placeholder — implemented in Task 3) ───────────────────

// findTermMatches returns non-overlapping, leftmost-longest term matches
// with identity-based protection. Implemented in Task 3.
func (ac *ahoCorasick) findTermMatches(runes []rune) []acMatch {
	return nil // placeholder
}

// bisectRight returns the insertion point for x in a sorted slice a
// such that all elements before the point are <= x.
func bisectRight(a []int, x int) int {
	return sort.Search(len(a), func(i int) bool { return a[i] > x })
}
