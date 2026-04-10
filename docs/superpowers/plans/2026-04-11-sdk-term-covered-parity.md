<!-- zhtw:disable -->
# SDK Term-Covered Parity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix Java/TypeScript/Rust SDKs so convert(), check(), and lookup() skip char-layer conversions on positions covered by any term hit (including identity terms), matching Python behavior.

**Architecture:** Each SDK matcher gets a new `getCoveredPositions()` method that iterates raw automaton hits (including identity terms) and returns all covered positions. `convert()` changes from `applyCharmap(replaceAll(text))` to a gap-mode approach that only applies charmap on uncovered positions. `check()` and `lookup()` use the same covered set to filter char-level results.

**Tech Stack:** Java 11 (Maven, ahocorasick-trie), TypeScript (Vitest, custom AC), Rust (daachorse, PHF charmap)

**Spec:** `docs/superpowers/specs/2026-04-10-sdk-check-parity-design.md`

---

### Task 1: Add identity-protected golden test cases

**Files:**
- Modify: `src/zhtw/export.py:58-77`
- Regenerate: `sdk/data/golden-test.json`, `sdk/data/zhtw-data.json`, `sdk/rust/zhtw/data/zhtw-data.json`

- [ ] **Step 1: Add identity-protected cases to `_GOLDEN_CASES`**

In `src/zhtw/export.py`, insert three new entries at the end of `_GOLDEN_CASES` (before the closing `]` at line 68):

```python
_GOLDEN_CASES = [
    # (input_text, sources, description)
    ("\u8f6f\u4ef6\u6d4b\u8bd5", ["cn"], "term layer: multi-term"),
    ("\u8fd9\u4e2a\u670d\u52a1\u5668\u7684\u5185\u5b58\u4e0d\u591f", ["cn"], "mixed"),
    ("\u5934\u53d1\u5f88\u5e72", ["cn"], "ambiguous chars"),
    ("\u8edf\u4ef6\u5de5\u7a0b\u5e2b", ["hk"], "HK source: term only"),
    ("\u5df2\u7d93\u662f\u7e41\u9ad4", ["cn"], "no conversion needed"),
    ("\u6570\u636e\u5e93\u670d\u52a1\u5668", ["cn"], "term layer: compound terms"),
    ("\u4e91\u8ba1\u7b97", ["cn"], "ambiguous: cloud"),
    ("\u53d1\u5c55\u5f88\u5feb", ["cn"], "ambiguous: fa"),
    # Identity-term protection: char layer must NOT convert chars inside identity terms
    ("\u5c38\u4f4d\u7d20\u9910", ["cn"], "identity: \u5c38\u4f4d\u7d20\u9910 protects \u5c38"),
    ("\u4eba\u4e91\u4ea6\u4e91", ["cn"], "identity: \u4eba\u4e91\u4ea6\u4e91 protects \u4e91"),
    ("\u6025\u75c7\u5f88\u4e25\u91cd", ["cn"], "identity+char: \u6025\u75c7 protected, \u4e25\u91cd char-converted"),
]
```

The three new lines (Unicode decoded):
- `尸位素餐` — identity term protects 尸 from being converted to 屍
- `人云亦云` — identity term protects 云 from being converted to 雲
- `急症很严重` — 急症 is identity-protected, 严→嚴 and 重 are char-converted

- [ ] **Step 2: Add identity-protected case to `_LOOKUP_CASES`**

In `src/zhtw/export.py`, insert one new entry at the end of `_LOOKUP_CASES` (before the closing `]` at line 77):

```python
_LOOKUP_CASES = [
    ("\u8f6f\u4ef6", ["cn"]),
    ("\u8fd9", ["cn"]),
    ("\u53f0", ["cn"]),
    ("\u5934\u53d1", ["cn"]),
    ("\u8edf\u4ef6", ["hk"]),
    ("\u6025\u75c7", ["cn"]),  # identity term: no conversion expected
]
```

- [ ] **Step 3: Verify Python produces correct output for new cases**

Run:
```bash
cd /Users/tim/GitHub/zhtw
python3 -c "
import sys; sys.path.insert(0, 'src')
from zhtw.converter import convert_text
from zhtw.dictionary import load_dictionary
from zhtw.matcher import Matcher
from zhtw.charconv import get_translate_table
from zhtw.lookup import lookup_word

terms = load_dictionary(sources=['cn'])
matcher = Matcher(terms)
ct = get_translate_table()

# convert tests
for inp, exp in [('\u5c38\u4f4d\u7d20\u9910', '\u5c38\u4f4d\u7d20\u9910'),
                 ('\u4eba\u4e91\u4ea6\u4e91', '\u4eba\u4e91\u4ea6\u4e91'),
                 ('\u6025\u75c7\u5f88\u4e25\u91cd', '\u6025\u75c7\u5f88\u56b4\u91cd')]:
    result, _ = convert_text(inp, matcher, fix=True, char_table=ct)
    status = 'PASS' if result == exp else 'FAIL'
    print(f'{status}: convert({inp}) = {result} (expected {exp})')

# check tests
for inp in ['\u5c38\u4f4d\u7d20\u9910', '\u4eba\u4e91\u4ea6\u4e91']:
    _, matches = convert_text(inp, matcher, fix=False, char_table=ct)
    print(f'check({inp}): {len(matches)} matches (expected 0)')

# lookup test
r = lookup_word('\u6025\u75c7', matcher, ct)
print(f'lookup(\u6025\u75c7): output={r.output}, changed={r.changed}, details={len(r.details)}')
"
```

Expected:
```
PASS: convert(尸位素餐) = 尸位素餐 (expected 尸位素餐)
PASS: convert(人云亦云) = 人云亦云 (expected 人云亦云)
PASS: convert(急症很严重) = 急症很嚴重 (expected 急症很嚴重)
check(尸位素餐): 0 matches (expected 0)
check(人云亦云): 0 matches (expected 0)
lookup(急症): output=急症, changed=False, details=0
```

- [ ] **Step 4: Regenerate golden-test.json and zhtw-data.json**

Run:
```bash
cd /Users/tim/GitHub/zhtw
make export
```

Expected: files regenerated, Rust copy synced.

- [ ] **Step 5: Verify Java SDK fails on new golden cases**

Run:
```bash
cd /Users/tim/GitHub/zhtw/sdk/java
mvn -q test -Dtest=GoldenTest --batch-mode 2>&1 | tail -5
```

Expected: failures on identity-protected cases (尸位素餐, 人云亦云, 急症) plus the existing 6 check() failures.

- [ ] **Step 6: Run Python tests to confirm no regression**

Run:
```bash
cd /Users/tim/GitHub/zhtw
pytest tests/ -x -q
```

Expected: all tests pass.

- [ ] **Step 7: Commit golden test additions**

```bash
cd /Users/tim/GitHub/zhtw
git add src/zhtw/export.py sdk/data/golden-test.json sdk/data/zhtw-data.json sdk/rust/zhtw/data/zhtw-data.json
git commit -m "$(cat <<'EOF'
test: 補 identity-protected golden cases（尸位素餐、人云亦云、急症）

新增 3 組 convert case + 1 組 lookup case 驗證 identity term
保護 char layer 不誤轉。SDKs 尚未修正，預期 fail。

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

### Task 2: Java SDK — getCoveredPositions + fix check/lookup/convert

**Files:**
- Modify: `sdk/java/src/main/java/com/rajatim/zhtw/AhoCorasickMatcher.java`
- Modify: `sdk/java/src/main/java/com/rajatim/zhtw/ZhtwConverter.java`
- Test: `sdk/java/src/test/java/com/rajatim/zhtw/GoldenTest.java` (existing, no changes needed)

- [ ] **Step 1: Add `getCoveredPositions()` to AhoCorasickMatcher**

In `sdk/java/src/main/java/com/rajatim/zhtw/AhoCorasickMatcher.java`, add this method after `replaceAll()` (after line 166, before the closing `}`):

```java
    /**
     * Return all UTF-16 positions covered by any raw automaton hit,
     * including identity terms (source == target). This is used to
     * prevent the char layer from converting characters that are
     * protected by identity term matches.
     */
    Set<Integer> getCoveredPositions(String text) {
        if (trie == null || text == null || text.isEmpty()) {
            return Collections.emptySet();
        }
        Set<Integer> covered = new HashSet<>();
        for (Emit emit : trie.parseText(text)) {
            // Emit.getEnd() is inclusive
            for (int i = emit.getStart(); i <= emit.getEnd(); i++) {
                covered.add(i);
            }
        }
        return covered;
    }
```

- [ ] **Step 2: Fix `check()` in ZhtwConverter**

In `sdk/java/src/main/java/com/rajatim/zhtw/ZhtwConverter.java`, replace the `check()` method (lines 90-121) with:

```java
    public List<Match> check(String text) {
        if (text == null || text.isEmpty()) {
            return Collections.emptyList();
        }

        List<Match> result = new ArrayList<>();

        // Covered positions from ALL automaton hits (including identity terms)
        Set<Integer> coveredUtf16 = matcher.getCoveredPositions(text);

        // Term-level matches (matcher returns UTF-16 indices, convert to codepoint)
        for (Match m : matcher.findMatches(text)) {
            int cpStart = Character.codePointCount(text, 0, m.getStart());
            int cpEnd = Character.codePointCount(text, 0, m.getEnd());
            result.add(new Match(cpStart, cpEnd, m.getSource(), m.getTarget()));
        }

        // Char-level matches (on original text, skip covered positions)
        if (charLayerEnabled) {
            int cpIndex = 0;
            int i = 0;
            while (i < text.length()) {
                int cp = text.codePointAt(i);
                if (!coveredUtf16.contains(i)) {
                    String replacement = charmap.get(cp);
                    String original = new String(Character.toChars(cp));
                    if (replacement != null && !replacement.equals(original)) {
                        result.add(new Match(cpIndex, cpIndex + 1, original, replacement));
                    }
                }
                cpIndex++;
                i += Character.charCount(cp);
            }
        }

        return result;
    }
```

- [ ] **Step 3: Fix `lookup()` in ZhtwConverter**

In `sdk/java/src/main/java/com/rajatim/zhtw/ZhtwConverter.java`, in the `lookup()` method (lines 130-190), replace the covered-set construction. Change lines 142-156 from:

```java
        List<ConversionDetail> utf16Details = new ArrayList<>();
        Set<Integer> coveredUtf16 = new HashSet<>();

        // 1. Term layer
        List<Match> termMatches = matcher.findMatches(word);
        for (Match m : termMatches) {
            String target = m.getTarget();
            // Apply charmap to term target (matching Python pipeline)
            if (charLayerEnabled) {
                target = applyCharmap(target);
            }
            utf16Details.add(new ConversionDetail(m.getSource(), target, "term", m.getStart()));
            for (int i = m.getStart(); i < m.getEnd(); i++) {
                coveredUtf16.add(i);
            }
        }
```

to:

```java
        List<ConversionDetail> utf16Details = new ArrayList<>();

        // Covered positions from ALL automaton hits (including identity terms)
        Set<Integer> coveredUtf16 = matcher.getCoveredPositions(word);

        // 1. Term layer
        List<Match> termMatches = matcher.findMatches(word);
        for (Match m : termMatches) {
            String target = m.getTarget();
            // Apply charmap to term target (matching Python pipeline)
            if (charLayerEnabled) {
                target = applyCharmap(target);
            }
            utf16Details.add(new ConversionDetail(m.getSource(), target, "term", m.getStart()));
        }
```

- [ ] **Step 4: Add `applyCharmapSkipping()` helper to ZhtwConverter**

In `sdk/java/src/main/java/com/rajatim/zhtw/ZhtwConverter.java`, add this private method after `applyCharmap()` (after line 230):

```java
    /**
     * Apply charmap to a text segment, skipping positions that are in the covered set.
     * @param segment text segment to process
     * @param covered set of covered UTF-16 positions in the ORIGINAL text
     * @param offset UTF-16 offset of this segment within the original text
     */
    private String applyCharmapSkipping(String segment, Set<Integer> covered, int offset) {
        StringBuilder sb = new StringBuilder(segment.length());
        boolean changed = false;
        int i = 0;
        while (i < segment.length()) {
            int cp = segment.codePointAt(i);
            int charLen = Character.charCount(cp);
            if (covered.contains(offset + i)) {
                sb.appendCodePoint(cp);
            } else {
                String replacement = charmap.get(cp);
                if (replacement != null) {
                    sb.append(replacement);
                    changed = true;
                } else {
                    sb.appendCodePoint(cp);
                }
            }
            i += charLen;
        }
        return changed ? sb.toString() : segment;
    }
```

- [ ] **Step 5: Fix `convert()` in ZhtwConverter**

In `sdk/java/src/main/java/com/rajatim/zhtw/ZhtwConverter.java`, replace the `convert()` method (lines 63-80) with:

```java
    public String convert(String text) {
        if (text == null) {
            return null;
        }
        if (text.isEmpty()) {
            return text;
        }

        // Covered positions from ALL automaton hits (including identity terms).
        // Must be computed on original text before any replacements.
        Set<Integer> covered = matcher.getCoveredPositions(text);
        List<Match> matches = matcher.findMatches(text);

        if (matches.isEmpty()) {
            return charLayerEnabled ? applyCharmapSkipping(text, covered, 0) : text;
        }

        // Gap mode: term targets are inserted verbatim; gaps get char-layer
        // applied only on uncovered positions.
        StringBuilder sb = new StringBuilder(text.length());
        int lastEnd = 0;
        for (Match m : matches) {
            String gap = text.substring(lastEnd, m.getStart());
            sb.append(charLayerEnabled ? applyCharmapSkipping(gap, covered, lastEnd) : gap);
            sb.append(m.getTarget());
            lastEnd = m.getEnd();
        }
        String tail = text.substring(lastEnd);
        sb.append(charLayerEnabled ? applyCharmapSkipping(tail, covered, lastEnd) : tail);
        return sb.toString();
    }
```

- [ ] **Step 6: Run Java golden tests**

Run:
```bash
cd /Users/tim/GitHub/zhtw/sdk/java
mvn -q test -Dtest=GoldenTest --batch-mode 2>&1 | tail -5
```

Expected: `Tests run: N, Failures: 0, Errors: 0`

- [ ] **Step 7: Run all Java tests**

Run:
```bash
cd /Users/tim/GitHub/zhtw/sdk/java
mvn -q test --batch-mode 2>&1 | tail -5
```

Expected: all tests pass. Some existing `ZhtwConverterTest` check tests may need adjustment if they assert exact match counts that changed. If `checkReturnsTermAndCharMatches` (line 110) fails because fewer char matches are returned, update its assertion.

Check specifically:
```bash
cd /Users/tim/GitHub/zhtw/sdk/java
mvn -q test -Dtest=ZhtwConverterTest --batch-mode 2>&1 | tail -10
```

If `checkReturnsTermAndCharMatches` fails, update line 117 from `assertTrue(matches.size() >= 2, ...)` — the term matches for "软件测试" should remain (软件 + 测试 are non-identity terms), but char matches for 软/件/测/试 should now be filtered. The exact assertion depends on what `findMatches` returns for this input.

- [ ] **Step 8: Commit Java SDK changes**

```bash
cd /Users/tim/GitHub/zhtw
git add sdk/java/src/main/java/com/rajatim/zhtw/AhoCorasickMatcher.java sdk/java/src/main/java/com/rajatim/zhtw/ZhtwConverter.java
git commit -m "$(cat <<'EOF'
fix(java): SDK convert/check/lookup 對齊 Python covered positions

- 新增 AhoCorasickMatcher.getCoveredPositions(): 走 raw trie hits 含 identity
- check(): 跳過 covered 位置的 char matches
- lookup(): covered set 改用 getCoveredPositions()
- convert(): 改為 gap 模式，uncovered 位置才跑 char layer

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

### Task 3: TypeScript SDK — getCoveredPositions + fix check/lookup/convert

**Files:**
- Modify: `sdk/typescript/src/core/matcher.ts`
- Modify: `sdk/typescript/src/core/converter.ts`
- Test: `sdk/typescript/tests/golden.test.ts` (existing, no changes needed)

- [ ] **Step 1: Add `getCoveredPositions()` to AhoCorasickMatcher**

In `sdk/typescript/src/core/matcher.ts`, add this method inside the `AhoCorasickMatcher` class, after `replaceAll()` (after line 203, before the closing `}`):

```typescript
  /**
   * Return all UTF-16 code-unit positions covered by any raw automaton hit,
   * including identity terms (source === target). Used to prevent the char
   * layer from converting characters protected by identity term matches.
   */
  getCoveredPositions(text: string): Set<number> {
    const covered = new Set<number>();
    for (const m of this.iterEmissions(text)) {
      for (let i = m.start; i < m.end; i++) {
        covered.add(i);
      }
    }
    return covered;
  }
```

- [ ] **Step 2: Add `applyCharmapSkipping()` helper to converter.ts**

In `sdk/typescript/src/core/converter.ts`, add this function after the existing `applyCharmap()` function (after line 71):

```typescript
/**
 * Apply charmap to a text segment, skipping positions covered by term hits.
 * @param segment - text segment to map
 * @param charmap - single-codepoint charmap
 * @param covered - set of covered UTF-16 positions in the ORIGINAL text
 * @param offset - UTF-16 offset of this segment within the original text
 */
function applyCharmapSkipping(
  segment: string,
  charmap: Record<string, string>,
  covered: Set<number>,
  offset: number,
): string {
  let out = '';
  let i = 0;
  while (i < segment.length) {
    const code = segment.charCodeAt(i);
    const isHigh = code >= 0xd800 && code <= 0xdbff && i + 1 < segment.length;
    const step = isHigh ? 2 : 1;
    const ch = segment.substring(i, i + step);
    if (covered.has(offset + i)) {
      out += ch;
    } else {
      const mapped = charmap[ch];
      out += mapped !== undefined && mapped !== ch ? mapped : ch;
    }
    i += step;
  }
  return out;
}
```

- [ ] **Step 3: Fix `convert()` in converter.ts**

In `sdk/typescript/src/core/converter.ts`, replace the `convert()` function (lines 83-88) with:

```typescript
  function convert(text: string): string {
    requireString(text, 'convert');
    if (text.length === 0) return '';

    // Covered positions from ALL automaton hits (including identity terms).
    const covered = matcher.getCoveredPositions(text);
    const matches = matcher.findMatches(text);

    if (matches.length === 0) {
      return charLayerEnabled ? applyCharmapSkipping(text, charmap, covered, 0) : text;
    }

    // Gap mode: term targets inserted verbatim; gaps get char-layer on uncovered only.
    let result = '';
    let lastEnd = 0;
    for (const m of matches) {
      const gap = text.substring(lastEnd, m.start);
      result += charLayerEnabled ? applyCharmapSkipping(gap, charmap, covered, lastEnd) : gap;
      result += m.target;
      lastEnd = m.end;
    }
    const tail = text.substring(lastEnd);
    result += charLayerEnabled ? applyCharmapSkipping(tail, charmap, covered, lastEnd) : tail;
    return result;
  }
```

- [ ] **Step 4: Fix `check()` in converter.ts**

In `sdk/typescript/src/core/converter.ts`, replace the `check()` function (lines 90-117) with:

```typescript
  function check(text: string): Match[] {
    requireString(text, 'check');
    if (text.length === 0) return [];

    const results: Match[] = [];

    // Covered positions from ALL automaton hits (including identity terms)
    const coveredUtf16 = matcher.getCoveredPositions(text);

    // Term layer
    for (const m of matcher.findMatches(text)) {
      results.push({
        start: utf16ToCodepoint(text, m.start),
        end: utf16ToCodepoint(text, m.end),
        source: m.source,
        target: m.target,
      });
    }

    // Char layer: skip covered positions
    if (charLayerEnabled) {
      let cp = 0;
      let i = 0;
      while (i < text.length) {
        const code = text.charCodeAt(i);
        const isHigh = code >= 0xd800 && code <= 0xdbff && i + 1 < text.length;
        const step = isHigh ? 2 : 1;
        if (!coveredUtf16.has(i)) {
          const ch = text.substring(i, i + step);
          const mapped = charmap[ch];
          if (mapped !== undefined && mapped !== ch) {
            results.push({ start: cp, end: cp + 1, source: ch, target: mapped });
          }
        }
        cp++;
        i += step;
      }
    }
    return results;
  }
```

Note: The char-layer loop now tracks both UTF-16 (`i`) and codepoint (`cp`) indices, and checks `coveredUtf16.has(i)` at each position. This differs from the original which used `for (const ch of text)` — the new version needs explicit UTF-16 index tracking.

- [ ] **Step 5: Fix `lookup()` in converter.ts**

In `sdk/typescript/src/core/converter.ts`, in the `lookup()` function, replace line 136 and lines 144-153:

Change:
```typescript
    const covered = new Set<number>(); // UTF-16 code-unit indices covered by a term match
```
to:
```typescript
    // Covered positions from ALL automaton hits (including identity terms)
    const covered = matcher.getCoveredPositions(word);
```

Then remove the `for` loop that manually builds `covered` from `findMatches` results. Change lines 144-153 from:

```typescript
    for (const m of matcher.findMatches(word)) {
      const target = charLayerEnabled ? applyCharmap(m.target, charmap) : m.target;
      internal.push({
        source: m.source,
        target,
        layer: 'term',
        utf16Start: m.start,
        utf16End: m.end,
      });
      for (let i = m.start; i < m.end; i++) covered.add(i);
    }
```

to:

```typescript
    for (const m of matcher.findMatches(word)) {
      const target = charLayerEnabled ? applyCharmap(m.target, charmap) : m.target;
      internal.push({
        source: m.source,
        target,
        layer: 'term',
        utf16Start: m.start,
        utf16End: m.end,
      });
    }
```

- [ ] **Step 6: Build and run TypeScript golden tests**

Run:
```bash
cd /Users/tim/GitHub/zhtw/sdk/typescript
npm run build && npm test 2>&1 | tail -15
```

Expected: all golden tests pass.

- [ ] **Step 7: Commit TypeScript SDK changes**

```bash
cd /Users/tim/GitHub/zhtw
git add sdk/typescript/src/core/matcher.ts sdk/typescript/src/core/converter.ts
git commit -m "$(cat <<'EOF'
fix(typescript): SDK convert/check/lookup 對齊 Python covered positions

- 新增 AhoCorasickMatcher.getCoveredPositions(): 走 raw emissions 含 identity
- check(): 跳過 covered 位置的 char matches
- lookup(): covered set 改用 getCoveredPositions()
- convert(): 改為 gap 模式，uncovered 位置才跑 char layer

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

### Task 4: Rust SDK — get_covered_positions + fix check/lookup/convert

**Files:**
- Modify: `sdk/rust/zhtw/src/matcher.rs`
- Modify: `sdk/rust/zhtw/src/converter.rs`
- Test: `sdk/rust/zhtw/tests/golden.rs` (existing, no changes needed)

- [ ] **Step 1: Add `get_covered_positions()` to matcher.rs**

In `sdk/rust/zhtw/src/matcher.rs`, add this function after `find_term_matches()` (after line 234):

```rust
/// Return all byte positions covered by any raw automaton hit, including
/// identity terms (source == target). Used to prevent the char layer from
/// converting characters protected by identity term matches.
pub(crate) fn get_covered_positions(
    pma: &CharwiseDoubleArrayAhoCorasick<u32>,
    text: &str,
) -> HashSet<usize> {
    let mut covered = HashSet::new();
    for m in pma.find_overlapping_iter(text) {
        for b in m.start()..m.end() {
            covered.insert(b);
        }
    }
    covered
}
```

Also add the required import at the top of `matcher.rs` if `HashSet` is not already imported:

```rust
use std::collections::HashSet;
```

(Check — it may already be imported via `BTreeSet`. If `HashSet` is not in the existing imports, add it.)

- [ ] **Step 2: Add `apply_charmap_skipping()` to matcher.rs**

In `sdk/rust/zhtw/src/matcher.rs`, add this function after `apply_charmap()` (after line 286):

```rust
/// Apply charmap to a text segment, skipping byte positions that are in the
/// covered set. `offset` is the byte offset of this segment within the
/// original text.
pub(crate) fn apply_charmap_skipping(
    segment: &str,
    char_map: &phf::Map<char, char>,
    covered: &HashSet<usize>,
    offset: usize,
) -> String {
    let mut result = String::with_capacity(segment.len());
    for (byte_idx, ch) in segment.char_indices() {
        if covered.contains(&(offset + byte_idx)) {
            result.push(ch);
        } else {
            result.push(char_map.get(&ch).copied().unwrap_or(ch));
        }
    }
    result
}
```

- [ ] **Step 3: Fix `check()` in converter.rs**

In `sdk/rust/zhtw/src/converter.rs`, replace the `check()` method (lines 173-210) with:

```rust
    pub fn check(&self, text: &str) -> Vec<Match> {
        if text.is_empty() {
            return Vec::new();
        }

        let inner = &self.inner;
        let byte_to_cp = matcher::build_byte_to_cp(text);

        // Covered byte positions from ALL automaton hits (including identity terms)
        let covered_bytes = matcher::get_covered_positions(&inner.automaton, text);

        // Term layer matches.
        let hits = matcher::find_term_matches(&inner.automaton, &inner.pattern_table, text);
        let mut matches: Vec<Match> = hits
            .iter()
            .map(|h| Match {
                start: byte_to_cp[h.byte_start],
                end: byte_to_cp[h.byte_end],
                source: h.source.clone(),
                target: h.target.clone(),
            })
            .collect();

        // Char layer matches (if enabled): skip covered byte positions.
        if inner.char_layer_enabled {
            for (byte_idx, ch) in text.char_indices() {
                if covered_bytes.contains(&byte_idx) {
                    continue;
                }
                if let Some(&mapped) = CHAR_MAP.get(&ch) {
                    if mapped != ch {
                        matches.push(Match {
                            start: byte_to_cp[byte_idx],
                            end: byte_to_cp[byte_idx] + 1,
                            source: ch.to_string(),
                            target: mapped.to_string(),
                        });
                    }
                }
            }
        }

        matches
    }
```

- [ ] **Step 4: Fix `lookup()` in converter.rs**

In `sdk/rust/zhtw/src/converter.rs`, in the `lookup()` method, replace the covered-bytes construction (lines 227-233):

Change from:
```rust
        // Track which bytes are covered by term hits.
        let mut covered_bytes: HashSet<usize> = HashSet::new();
        for h in &hits {
            for b in h.byte_start..h.byte_end {
                covered_bytes.insert(b);
            }
        }
```

to:
```rust
        // Covered byte positions from ALL automaton hits (including identity terms)
        let covered_bytes = matcher::get_covered_positions(&inner.automaton, word);
```

Add the import for `HashSet` at the top of `converter.rs` if not already present (it's likely already there from the old manual construction).

- [ ] **Step 5: Fix `convert()` in converter.rs**

In `sdk/rust/zhtw/src/converter.rs`, replace the `convert()` method (lines 156-170) with:

```rust
    pub fn convert(&self, text: &str) -> String {
        if text.is_empty() {
            return String::new();
        }

        let inner = &self.inner;

        // Covered byte positions from ALL automaton hits (including identity terms).
        // Must be computed on original text before any replacements.
        let covered = matcher::get_covered_positions(&inner.automaton, text);
        let hits = matcher::find_term_matches(&inner.automaton, &inner.pattern_table, text);

        if hits.is_empty() {
            return if inner.char_layer_enabled {
                matcher::apply_charmap_skipping(text, &CHAR_MAP, &covered, 0)
            } else {
                text.to_string()
            };
        }

        // Gap mode: term targets inserted verbatim; gaps get char-layer on uncovered only.
        let mut result = String::new();
        let mut last_end: usize = 0;
        for h in &hits {
            let gap = &text[last_end..h.byte_start];
            if inner.char_layer_enabled {
                result.push_str(&matcher::apply_charmap_skipping(
                    gap, &CHAR_MAP, &covered, last_end,
                ));
            } else {
                result.push_str(gap);
            }
            result.push_str(&h.target);
            last_end = h.byte_end;
        }
        let tail = &text[last_end..];
        if inner.char_layer_enabled {
            result.push_str(&matcher::apply_charmap_skipping(
                tail, &CHAR_MAP, &covered, last_end,
            ));
        } else {
            result.push_str(tail);
        }
        result
    }
```

- [ ] **Step 6: Run Rust golden tests**

Run:
```bash
cd /Users/tim/GitHub/zhtw/sdk/rust
cargo test --package zhtw 2>&1 | tail -15
```

Expected: all tests pass including golden tests.

- [ ] **Step 7: Run full Rust test suite**

Run:
```bash
cd /Users/tim/GitHub/zhtw/sdk/rust
cargo test --package zhtw -- --nocapture 2>&1 | tail -20
```

Expected: all tests pass.

- [ ] **Step 8: Commit Rust SDK changes**

```bash
cd /Users/tim/GitHub/zhtw
git add sdk/rust/zhtw/src/matcher.rs sdk/rust/zhtw/src/converter.rs
git commit -m "$(cat <<'EOF'
fix(rust): SDK convert/check/lookup 對齊 Python covered positions

- 新增 get_covered_positions(): 走 raw automaton hits 含 identity
- 新增 apply_charmap_skipping(): 跳過 covered byte positions
- check(): 跳過 covered 位置的 char matches
- lookup(): covered set 改用 get_covered_positions()
- convert(): 改為 gap 模式，uncovered 位置才跑 char layer

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

### Task 5: Cross-SDK verification and Python regression check

**Files:** None to modify — verification only.

- [ ] **Step 1: Run Python full test suite**

Run:
```bash
cd /Users/tim/GitHub/zhtw
pytest tests/ -x -q
```

Expected: all tests pass.

- [ ] **Step 2: Run Java full test suite**

Run:
```bash
cd /Users/tim/GitHub/zhtw/sdk/java
mvn -q test --batch-mode 2>&1 | tail -5
```

Expected: `Tests run: N, Failures: 0, Errors: 0`

- [ ] **Step 3: Run TypeScript full test suite**

Run:
```bash
cd /Users/tim/GitHub/zhtw/sdk/typescript
npm run build && npm test
```

Expected: all tests pass.

- [ ] **Step 4: Run Rust full test suite**

Run:
```bash
cd /Users/tim/GitHub/zhtw/sdk/rust
cargo test --package zhtw
```

Expected: all tests pass.

- [ ] **Step 5: Verify identity-term protection end-to-end**

Run a quick smoke test across all SDKs to confirm the key identity terms are protected:

```bash
cd /Users/tim/GitHub/zhtw

# Python (reference)
python3 -c "
import sys; sys.path.insert(0, 'src')
from zhtw.converter import convert_text
from zhtw.dictionary import load_dictionary
from zhtw.matcher import Matcher
from zhtw.charconv import get_translate_table
terms = load_dictionary(sources=['cn'])
matcher = Matcher(terms)
ct = get_translate_table()
for inp in ['\u5c38\u4f4d\u7d20\u9910', '\u4eba\u4e91\u4ea6\u4e91', '\u6025\u75c7']:
    r, _ = convert_text(inp, matcher, fix=True, char_table=ct)
    print(f'Python: {inp} -> {r}')
"

# Java
cd sdk/java
mvn -q test -Dtest=GoldenTest --batch-mode 2>&1 | grep -E "(Tests run|FAIL)"

# TypeScript
cd ../typescript
npm test 2>&1 | grep -E "(Tests|FAIL|pass)"

# Rust
cd ../rust
cargo test --package zhtw golden 2>&1 | grep -E "(test result|FAILED)"
```

Expected: all four SDKs agree — identity terms preserved, no failures.

- [ ] **Step 6: Verify git status is clean (all committed)**

Run:
```bash
cd /Users/tim/GitHub/zhtw
git status
git log --oneline -6
```

Expected: working tree clean, 4 new commits visible (golden cases + 3 SDK fixes).
