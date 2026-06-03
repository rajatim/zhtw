# zhtw-js (TypeScript SDK) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship `zhtw-js@4.0.0` — an isomorphic TypeScript SDK producing byte-for-byte identical output to the Python CLI and Java SDK, verified by `sdk/data/golden-test.json`.

**Architecture:** Thin-adapter layout (Approach A). A pure `core/` (types, codepoint utils, hand-rolled Aho-Corasick matcher, converter factory) sits above two tiny data loaders (`data/node.ts`, `data/browser.ts`), wired up by entry files `index.node.ts` / `index.browser.ts` that resolve via the package.json `exports` conditional map. Build via tsup (dual ESM+CJS), test via Vitest.

**Tech Stack:** TypeScript 5 (strict, ES2022), tsup (esbuild), Vitest (+ happy-dom), pnpm, GitHub Actions, zero runtime dependencies.

**Reference implementations to port:**
- `sdk/java/src/main/java/com/rajatim/zhtw/AhoCorasickMatcher.java` — matcher pattern (raw AC trie + hand-rolled longest-match with identity-protected ranges)
- `sdk/java/src/main/java/com/rajatim/zhtw/ZhtwConverter.java` — convert/check/lookup semantics
- `src/zhtw/matcher.py` lines 92-132 — protected-range logic
- `sdk/data/zhtw-data.json` — schema (`charmap.chars`, `terms.cn`, `terms.hk`, `version`)
- `sdk/data/golden-test.json` — cross-SDK parity fixtures (convert: 8, check: 8, lookup: 5)

<!-- zhtw:disable -->

---

## File Structure

**Created files:**
- `sdk/typescript/package.json` (rewritten from stub)
- `sdk/typescript/tsconfig.json`
- `sdk/typescript/tsup.config.ts`
- `sdk/typescript/vitest.config.ts`
- `sdk/typescript/.gitignore`
- `sdk/typescript/README.md`
- `sdk/typescript/src/core/types.ts`
- `sdk/typescript/src/core/codepoint.ts`
- `sdk/typescript/src/core/matcher.ts`
- `sdk/typescript/src/core/converter.ts`
- `sdk/typescript/src/data/node.ts`
- `sdk/typescript/src/data/browser.ts`
- `sdk/typescript/src/index.node.ts`
- `sdk/typescript/src/index.browser.ts`
- `sdk/typescript/tests/codepoint.test.ts`
- `sdk/typescript/tests/matcher.test.ts`
- `sdk/typescript/tests/converter.test.ts`
- `sdk/typescript/tests/golden.test.ts`
- `sdk/typescript/tests/api.test.ts`
- `sdk/typescript/tests/pack.test.ts`
- `sdk/typescript/scripts/bench.ts`
- `.github/workflows/sdk-typescript.yml`

**Modified files:**
- `README.md` (root) — update Multi-language SDKs table (TypeScript status + throughput)

**Unchanged (verified):**
- `Makefile` (already includes TypeScript in `bump` and `version-check`)
- `sdk/data/zhtw-data.json` and `sdk/data/golden-test.json` (already contain all three fixture sections at v4.0.0)

---

## Task 1: Scaffold package + build tooling

**Files:**
- Create: `sdk/typescript/package.json` (overwrite stub)
- Create: `sdk/typescript/tsconfig.json`
- Create: `sdk/typescript/.gitignore`
- Create: `sdk/typescript/vitest.config.ts`
- Create: `sdk/typescript/tsup.config.ts`

**Context:** Stand up the build and test tooling before writing any source code. We need tsup for dual ESM+CJS output with a post-build copy step that places `zhtw-data.json` inside `dist/`. Vitest handles unit + happy-dom browser tests. TypeScript runs in strict mode targeting ES2022.

- [ ] **Step 1: Write `package.json`**

Replace the existing stub at `sdk/typescript/package.json`:

```json
{
  "name": "zhtw-js",
  "version": "4.0.0",
  "description": "Traditional Chinese converter for Taiwan — TypeScript SDK",
  "type": "module",
  "sideEffects": false,
  "exports": {
    ".": {
      "browser": {
        "types": "./dist/index.browser.d.ts",
        "import": "./dist/index.browser.mjs",
        "require": "./dist/index.browser.cjs"
      },
      "node": {
        "types": "./dist/index.node.d.ts",
        "import": "./dist/index.node.mjs",
        "require": "./dist/index.node.cjs"
      }
    }
  },
  "files": ["dist", "README.md", "LICENSE"],
  "engines": { "node": ">=18" },
  "repository": {
    "type": "git",
    "url": "https://github.com/rajatim/zhtw.git",
    "directory": "sdk/typescript"
  },
  "license": "MIT",
  "keywords": ["chinese", "traditional-chinese", "taiwan", "zhtw", "converter", "simplified-to-traditional"],
  "scripts": {
    "build": "tsup",
    "test": "vitest run",
    "test:watch": "vitest",
    "bench": "tsx scripts/bench.ts"
  },
  "devDependencies": {
    "@types/node": "^20.11.0",
    "happy-dom": "^14.0.0",
    "tsup": "^8.0.0",
    "tsx": "^4.7.0",
    "typescript": "^5.4.0",
    "vitest": "^1.4.0"
  }
}
```

- [ ] **Step 2: Write `tsconfig.json`**

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "lib": ["ES2022", "DOM"],
    "strict": true,
    "noImplicitAny": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "exactOptionalPropertyTypes": true,
    "declaration": true,
    "esModuleInterop": true,
    "resolveJsonModule": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "isolatedModules": true,
    "outDir": "dist"
  },
  "include": ["src/**/*", "tests/**/*", "scripts/**/*", "tsup.config.ts", "vitest.config.ts"]
}
```

- [ ] **Step 3: Write `.gitignore`**

```
node_modules/
dist/
*.tgz
.vitest-cache/
```

- [ ] **Step 4: Write `vitest.config.ts`**

```ts
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    environment: 'node',
    include: ['tests/**/*.test.ts'],
    exclude: ['tests/pack.test.ts', 'node_modules/**'],
  },
});
```

Note: `pack.test.ts` is excluded from the default `vitest run`; it is opted-in via env var in CI (see Task 15).

- [ ] **Step 5: Write `tsup.config.ts`**

```ts
import { defineConfig } from 'tsup';
import { copyFileSync, mkdirSync } from 'node:fs';
import { resolve } from 'node:path';

export default defineConfig({
  entry: {
    'index.node': 'src/index.node.ts',
    'index.browser': 'src/index.browser.ts',
  },
  format: ['esm', 'cjs'],
  dts: true,
  sourcemap: true,
  clean: true,
  target: 'es2022',
  platform: 'neutral',
  outDir: 'dist',
  // Inline the browser JSON import so the browser bundle is self-contained;
  // the Node loader reads zhtw-data.json from disk next to the entry file.
  loader: { '.json': 'json' },
  onSuccess: async () => {
    const src = resolve(__dirname, '../data/zhtw-data.json');
    const outDir = resolve(__dirname, 'dist');
    mkdirSync(outDir, { recursive: true });
    copyFileSync(src, resolve(outDir, 'zhtw-data.json'));
    console.log('[tsup] copied zhtw-data.json → dist/');
  },
});
```

- [ ] **Step 6: Install dependencies**

Run: `cd sdk/typescript && pnpm install`
Expected: Installs cleanly, creates `node_modules/` and `pnpm-lock.yaml`.

- [ ] **Step 7: Commit**

```bash
git add sdk/typescript/package.json sdk/typescript/tsconfig.json sdk/typescript/.gitignore \
        sdk/typescript/vitest.config.ts sdk/typescript/tsup.config.ts sdk/typescript/pnpm-lock.yaml
git commit -m "feat(ts-sdk): scaffold package, build, and test tooling"
```

---

## Task 2: Core public types

**Files:**
- Create: `sdk/typescript/src/core/types.ts`

**Context:** Define the public type surface so every subsequent file can import from one place. Per spec §4, `Source = 'cn' | 'hk'`, `Match` uses **codepoint** indices, and `ConverterOptions.sources` is `Source[]`. The internal `Utf16Match` type lives in `matcher.ts`, not here — keeping them in separate files prevents accidental re-export.

- [ ] **Step 1: Write `src/core/types.ts`**

```ts
export type Source = 'cn' | 'hk';

export interface Match {
  /** Codepoint index, inclusive. */
  start: number;
  /** Codepoint index, exclusive. */
  end: number;
  /** Original text matched. */
  source: string;
  /** Replacement text (post-charmap). */
  target: string;
}

export interface ConversionDetail {
  source: string;
  target: string;
  layer: 'term' | 'char';
  /** Codepoint index of the matched/replaced segment in the input. */
  position: number;
}

export interface LookupResult {
  input: string;
  output: string;
  changed: boolean;
  details: ConversionDetail[];
}

export interface ConverterOptions {
  /** Which source dictionaries to use. Default: ['cn', 'hk']. */
  sources?: Source[];
  /** User overrides, take priority over built-in terms. */
  customDict?: Record<string, string>;
}

export interface Converter {
  convert(text: string): string;
  check(text: string): Match[];
  lookup(word: string): LookupResult;
}

/** Shape of sdk/data/zhtw-data.json. */
export interface ZhtwData {
  version: string;
  charmap: {
    chars: Record<string, string>;
    ambiguous: Record<string, string[]>;
  };
  terms: Record<string, Record<string, string>>;
  stats?: Record<string, unknown>;
}
```

- [ ] **Step 2: Verify it type-checks**

Run: `cd sdk/typescript && npx tsc --noEmit`
Expected: No errors (empty output).

- [ ] **Step 3: Commit**

```bash
git add sdk/typescript/src/core/types.ts
git commit -m "feat(ts-sdk): add public type surface"
```

---

## Task 3: Codepoint utilities (TDD)

**Files:**
- Create: `sdk/typescript/src/core/codepoint.ts`
- Test: `sdk/typescript/tests/codepoint.test.ts`

**Context:** JavaScript strings are UTF-16. A supplementary-plane codepoint like `𠮷` (U+20BB7) has `.length === 2` but represents 1 codepoint. All public positions must be codepoint indices for cross-SDK parity, so we need conversion helpers. Follow TDD: write failing tests first.

- [ ] **Step 1: Write failing tests**

Create `sdk/typescript/tests/codepoint.test.ts`:

```ts
import { describe, it, expect } from 'vitest';
import { codepointLength, utf16ToCodepoint, codepointAt } from '../src/core/codepoint';

describe('codepointLength', () => {
  it('counts ASCII as 1 per char', () => {
    expect(codepointLength('hello')).toBe(5);
  });
  it('counts BMP CJK as 1 per char', () => {
    expect(codepointLength('軟體測試')).toBe(4);
  });
  it('counts supplementary-plane codepoints as 1 each', () => {
    // 𠮷 is U+20BB7, one codepoint, two UTF-16 code units
    expect(codepointLength('𠮷')).toBe(1);
    expect(codepointLength('𠮷野家')).toBe(3);
  });
  it('returns 0 for empty string', () => {
    expect(codepointLength('')).toBe(0);
  });
});

describe('utf16ToCodepoint', () => {
  it('is identity for pure BMP', () => {
    const s = 'abc軟體';
    expect(utf16ToCodepoint(s, 0)).toBe(0);
    expect(utf16ToCodepoint(s, 3)).toBe(3);
    expect(utf16ToCodepoint(s, 5)).toBe(5);
  });
  it('collapses surrogate pairs', () => {
    const s = '𠮷野家'; // utf16 length 4, codepoint length 3
    expect(utf16ToCodepoint(s, 0)).toBe(0);
    expect(utf16ToCodepoint(s, 2)).toBe(1); // after 𠮷
    expect(utf16ToCodepoint(s, 3)).toBe(2);
    expect(utf16ToCodepoint(s, 4)).toBe(3);
  });
  it('handles mixed BMP + supplementary', () => {
    const s = 'a𠮷b'; // utf16: a(1) + 𠮷(2) + b(1) = 4
    expect(utf16ToCodepoint(s, 1)).toBe(1); // after a
    expect(utf16ToCodepoint(s, 3)).toBe(2); // after 𠮷
    expect(utf16ToCodepoint(s, 4)).toBe(3); // after b
  });
});

describe('codepointAt', () => {
  it('walks to nth codepoint', () => {
    const s = 'a𠮷b';
    expect(codepointAt(s, 0)).toEqual({ char: 'a', utf16Index: 0 });
    expect(codepointAt(s, 1)).toEqual({ char: '𠮷', utf16Index: 1 });
    expect(codepointAt(s, 2)).toEqual({ char: 'b', utf16Index: 3 });
  });
});
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd sdk/typescript && pnpm test codepoint`
Expected: FAIL — `Cannot find module '../src/core/codepoint'`

- [ ] **Step 3: Implement `src/core/codepoint.ts`**

```ts
/** Count the number of Unicode codepoints in a JS (UTF-16) string. */
export function codepointLength(s: string): number {
  let count = 0;
  for (let i = 0; i < s.length; ) {
    const code = s.charCodeAt(i);
    i += code >= 0xd800 && code <= 0xdbff && i + 1 < s.length ? 2 : 1;
    count++;
  }
  return count;
}

/**
 * Convert a UTF-16 code-unit index into a codepoint index.
 * For BMP-only strings this is identity.
 */
export function utf16ToCodepoint(text: string, utf16Index: number): number {
  let cp = 0;
  let i = 0;
  while (i < utf16Index && i < text.length) {
    const code = text.charCodeAt(i);
    i += code >= 0xd800 && code <= 0xdbff && i + 1 < text.length ? 2 : 1;
    cp++;
  }
  return cp;
}

/**
 * Walk to the `cpIndex`-th codepoint (0-based). Returns the character (as a
 * 1- or 2-code-unit string) and its UTF-16 offset.
 */
export function codepointAt(
  text: string,
  cpIndex: number,
): { char: string; utf16Index: number } {
  let cp = 0;
  let i = 0;
  while (i < text.length) {
    const code = text.charCodeAt(i);
    const isHigh = code >= 0xd800 && code <= 0xdbff && i + 1 < text.length;
    const step = isHigh ? 2 : 1;
    if (cp === cpIndex) {
      return { char: text.substring(i, i + step), utf16Index: i };
    }
    cp++;
    i += step;
  }
  throw new RangeError(`codepointAt: index ${cpIndex} out of range (length ${cp})`);
}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd sdk/typescript && pnpm test codepoint`
Expected: All tests pass (11/11).

- [ ] **Step 5: Commit**

```bash
git add sdk/typescript/src/core/codepoint.ts sdk/typescript/tests/codepoint.test.ts
git commit -m "feat(ts-sdk): add UTF-16 ↔ codepoint utilities"
```

---

## Task 4: Aho-Corasick matcher — raw automaton (TDD)

**Files:**
- Create: `sdk/typescript/src/core/matcher.ts` (raw AC only; protected-range filter added in Task 5)
- Test: `sdk/typescript/tests/matcher.test.ts`

**Context:** This is the most delicate port. The Java/Python SDKs use external libraries to build the raw trie, then hand-roll longest-match + identity-protected ranges on top. We have no external AC library in JS, so we implement the raw automaton ourselves and layer the same filtering logic on top. This task implements ONLY the raw emission (every possible match at every position). Task 5 adds the longest-match + protected-range filter.

- [ ] **Step 1: Write failing tests for raw emission**

Create `sdk/typescript/tests/matcher.test.ts`:

```ts
import { describe, it, expect } from 'vitest';
import { AhoCorasickMatcher, type Utf16Match } from '../src/core/matcher';

describe('AhoCorasickMatcher — raw emissions (iterEmissions)', () => {
  it('emits empty array for no matches', () => {
    const m = new AhoCorasickMatcher({ abc: 'XYZ' });
    expect(Array.from(m.iterEmissions('zzz'))).toEqual([]);
  });

  it('emits a single match', () => {
    const m = new AhoCorasickMatcher({ ab: 'XX' });
    const emissions = Array.from(m.iterEmissions('xabx'));
    expect(emissions).toEqual([{ start: 1, end: 3, source: 'ab', target: 'XX' }]);
  });

  it('emits all overlapping matches (raw Aho-Corasick)', () => {
    // With patterns "ab" and "abc", raw AC reports BOTH at the same right edge.
    const m = new AhoCorasickMatcher({ ab: 'X', abc: 'Y' });
    const emissions = Array.from(m.iterEmissions('abc'));
    // Expect both matches present.
    expect(emissions).toContainEqual({ start: 0, end: 2, source: 'ab', target: 'X' });
    expect(emissions).toContainEqual({ start: 0, end: 3, source: 'abc', target: 'Y' });
  });

  it('handles unicode BMP patterns', () => {
    const m = new AhoCorasickMatcher({ 軟體: '軟體' });
    const emissions = Array.from(m.iterEmissions('這個軟體'));
    expect(emissions).toEqual([{ start: 2, end: 4, source: '軟體', target: '軟體' }]);
  });
});
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd sdk/typescript && pnpm test matcher`
Expected: FAIL — `Cannot find module '../src/core/matcher'`

- [ ] **Step 3: Implement raw AC in `src/core/matcher.ts`**

```ts
/**
 * Internal match type. Uses UTF-16 code-unit indices because JS strings are
 * UTF-16. NOT exported from the package — core/converter.ts converts these
 * into codepoint-indexed public `Match` values before returning to callers.
 */
export interface Utf16Match {
  /** UTF-16 code-unit index, inclusive. */
  start: number;
  /** UTF-16 code-unit index, exclusive. */
  end: number;
  source: string;
  target: string;
}

interface Node {
  children: Map<number, Node>;
  fail: Node | null;
  /** Patterns that terminate at (or via output-link through) this node. */
  outputs: string[];
}

function createNode(): Node {
  return { children: new Map(), fail: null, outputs: [] };
}

export class AhoCorasickMatcher {
  private readonly root: Node = createNode();
  private readonly patterns: Record<string, string>;

  constructor(patterns: Record<string, string>) {
    this.patterns = patterns;
    for (const key of Object.keys(patterns)) {
      if (key.length === 0) continue; // skip empty-key entries (matches Python)
      this.addPattern(key);
    }
    this.buildFailureLinks();
  }

  private addPattern(pattern: string): void {
    let node = this.root;
    for (let i = 0; i < pattern.length; i++) {
      const code = pattern.charCodeAt(i);
      let next = node.children.get(code);
      if (!next) {
        next = createNode();
        node.children.set(code, next);
      }
      node = next;
    }
    node.outputs.push(pattern);
  }

  private buildFailureLinks(): void {
    const queue: Node[] = [];
    for (const child of this.root.children.values()) {
      child.fail = this.root;
      queue.push(child);
    }
    while (queue.length > 0) {
      const node = queue.shift()!;
      for (const [code, child] of node.children) {
        queue.push(child);
        let f = node.fail;
        while (f !== null && !f.children.has(code)) {
          f = f.fail;
        }
        child.fail = f === null ? this.root : (f.children.get(code) ?? this.root);
        // Merge output link patterns (longest-output-first is not required here;
        // we emit every output reachable from this state).
        if (child.fail.outputs.length > 0) {
          child.outputs = [...child.outputs, ...child.fail.outputs];
        }
      }
    }
  }

  /**
   * Yield every raw AC match in `text`. At each right-edge position, emit
   * all patterns that terminate there (possibly multiple, possibly overlapping
   * with emissions at other positions). The longest-match + protected-range
   * filter happens in `findMatches` (added in the next task).
   */
  *iterEmissions(text: string): Generator<Utf16Match> {
    let node: Node = this.root;
    for (let i = 0; i < text.length; i++) {
      const code = text.charCodeAt(i);
      while (node !== this.root && !node.children.has(code)) {
        node = node.fail ?? this.root;
      }
      const next = node.children.get(code);
      if (next) {
        node = next;
      }
      if (node.outputs.length > 0) {
        for (const pat of node.outputs) {
          const start = i + 1 - pat.length;
          yield {
            start,
            end: i + 1,
            source: pat,
            target: this.patterns[pat]!,
          };
        }
      }
    }
  }

  /** Stub — implemented in the next task. */
  findMatches(_text: string): Utf16Match[] {
    throw new Error('findMatches: not implemented yet (see Task 5)');
  }

  /** Stub — implemented in the next task. */
  replaceAll(_text: string): string {
    throw new Error('replaceAll: not implemented yet (see Task 5)');
  }
}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd sdk/typescript && pnpm test matcher`
Expected: All 4 raw-emission tests pass. `findMatches` / `replaceAll` stubs throw; that's fine — no test hits them yet.

- [ ] **Step 5: Commit**

```bash
git add sdk/typescript/src/core/matcher.ts sdk/typescript/tests/matcher.test.ts
git commit -m "feat(ts-sdk): implement raw Aho-Corasick automaton"
```

---

## Task 5: Longest-match + protected-range filter (TDD)

**Files:**
- Modify: `sdk/typescript/src/core/matcher.ts` (replace `findMatches` and `replaceAll` stubs)
- Modify: `sdk/typescript/tests/matcher.test.ts` (add tests for filtered behavior)

**Context:** This mirrors `AhoCorasickMatcher.java` lines 60-140 and `src/zhtw/matcher.py` lines 92-132. The algorithm: collect all raw emissions, sort by (start ASC, length DESC), walk left-to-right picking the longest match that starts at or after the current cursor, and maintain a set of "protected" UTF-16 positions that shorter matches are not allowed to start inside of (because they'd nest inside an already-chosen longer one). Uses binary search for containment check.

- [ ] **Step 1: Add failing tests for filtered behavior**

Append to `sdk/typescript/tests/matcher.test.ts`:

```ts
describe('AhoCorasickMatcher.findMatches — longest-match + protected ranges', () => {
  it('picks the longer of two overlapping candidates at the same start', () => {
    // 'ab' vs 'abc' at start 0 → 'abc' wins, 'ab' is dropped.
    const m = new AhoCorasickMatcher({ ab: 'X', abc: 'Y' });
    expect(m.findMatches('abc')).toEqual([
      { start: 0, end: 3, source: 'abc', target: 'Y' },
    ]);
  });

  it('drops a shorter match that would start inside a chosen longer one', () => {
    // Patterns 'abcd' and 'bc'. On input 'abcd':
    //  - raw AC emits 'abcd' (0..4) and 'bc' (1..3)
    //  - after sort+filter, 'abcd' wins at start 0, and 'bc' is nested inside
    //    the protected range 0..4, so it's dropped.
    const m = new AhoCorasickMatcher({ abcd: 'XXXX', bc: 'YY' });
    expect(m.findMatches('abcd')).toEqual([
      { start: 0, end: 4, source: 'abcd', target: 'XXXX' },
    ]);
  });

  it('allows a later match that does not overlap an earlier one', () => {
    const m = new AhoCorasickMatcher({ ab: 'X', cd: 'Y' });
    expect(m.findMatches('abcd')).toEqual([
      { start: 0, end: 2, source: 'ab', target: 'X' },
      { start: 2, end: 4, source: 'cd', target: 'Y' },
    ]);
  });

  it('returns [] for text with no matches', () => {
    const m = new AhoCorasickMatcher({ ab: 'X' });
    expect(m.findMatches('xyz')).toEqual([]);
  });
});

describe('AhoCorasickMatcher.replaceAll', () => {
  it('returns the input unchanged when nothing matches', () => {
    const m = new AhoCorasickMatcher({ ab: 'X' });
    expect(m.replaceAll('xyz')).toBe('xyz');
  });

  it('replaces all non-overlapping matches', () => {
    const m = new AhoCorasickMatcher({ ab: 'AB', cd: 'CD' });
    expect(m.replaceAll('-ab-cd-')).toBe('-AB-CD-');
  });

  it('prefers longest-match when patterns overlap', () => {
    const m = new AhoCorasickMatcher({ ab: 'X', abc: 'Y' });
    expect(m.replaceAll('xabcx')).toBe('xYx');
  });
});
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd sdk/typescript && pnpm test matcher`
Expected: FAIL — the new tests throw "not implemented yet".

- [ ] **Step 3: Implement `findMatches` and `replaceAll`**

In `sdk/typescript/src/core/matcher.ts`, replace the two stub methods at the bottom of the class with:

```ts
  /**
   * Longest-match, non-overlapping, left-to-right. Mirrors
   * `AhoCorasickMatcher.java::findMatches` + `buildProtectedRanges` logic.
   */
  findMatches(text: string): Utf16Match[] {
    const raw = Array.from(this.iterEmissions(text));
    if (raw.length === 0) return [];
    // Sort by start ASC, then length DESC (longer match wins at same start).
    raw.sort((a, b) => {
      if (a.start !== b.start) return a.start - b.start;
      return b.end - a.end;
    });

    // Protected starts: sorted list of `start` positions already claimed by
    // a chosen longer match. For each candidate, we binary-search the most
    // recent protected start ≤ candidate.start and check whether the
    // candidate lies *inside* that protected range.
    const chosen: Utf16Match[] = [];
    const protectedStarts: number[] = [];
    const protectedEnds: number[] = [];
    let cursor = 0;

    for (const m of raw) {
      if (m.start < cursor) continue; // overlaps previous chosen match
      // Is m nested inside any already-protected range?
      const idx = bisectRight(protectedStarts, m.start) - 1;
      if (idx >= 0 && m.end <= protectedEnds[idx]! && m.start >= protectedStarts[idx]!) {
        continue;
      }
      chosen.push(m);
      protectedStarts.push(m.start);
      protectedEnds.push(m.end);
      cursor = m.end;
    }
    return chosen;
  }

  replaceAll(text: string): string {
    const matches = this.findMatches(text);
    if (matches.length === 0) return text;
    let out = '';
    let last = 0;
    for (const m of matches) {
      if (m.start > last) out += text.substring(last, m.start);
      out += m.target;
      last = m.end;
    }
    if (last < text.length) out += text.substring(last);
    return out;
  }
}

/** Rightmost insertion point for `x` in sorted array `arr`. */
function bisectRight(arr: number[], x: number): number {
  let lo = 0;
  let hi = arr.length;
  while (lo < hi) {
    const mid = (lo + hi) >>> 1;
    if (x < arr[mid]!) hi = mid;
    else lo = mid + 1;
  }
  return lo;
}
```

Important: make sure the `bisectRight` helper is placed **outside** the class (after the closing `}` of `AhoCorasickMatcher`), and that the stub method bodies are removed (not left alongside the real implementations).

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd sdk/typescript && pnpm test matcher`
Expected: All matcher tests pass (raw + filtered + replaceAll = 11/11).

- [ ] **Step 5: Commit**

```bash
git add sdk/typescript/src/core/matcher.ts sdk/typescript/tests/matcher.test.ts
git commit -m "feat(ts-sdk): add longest-match filter + replaceAll to matcher"
```

---

## Task 6: Converter factory — convert() (TDD)

**Files:**
- Create: `sdk/typescript/src/core/converter.ts`
- Test: `sdk/typescript/tests/converter.test.ts`

**Context:** `createConverter(data, options)` is a pure factory that merges terms from the requested sources + customDict, builds a matcher, builds a codepoint→replacement map from `data.charmap.chars`, and returns `{ convert, check, lookup }` closures. This task implements `convert` only; check/lookup come in later tasks. The char layer is enabled only when 'cn' is in sources (matches Java `ZhtwConverter.java:120`).

- [ ] **Step 1: Write failing tests for `convert`**

Create `sdk/typescript/tests/converter.test.ts`:

```ts
import { describe, it, expect } from 'vitest';
import { createConverter } from '../src/core/converter';
import type { ZhtwData } from '../src/core/types';

// Minimal in-memory fixture — not the full data file.
const DATA: ZhtwData = {
  version: '4.0.0',
  charmap: {
    chars: {
      '软': '軟',
      '件': '件',  // identity — should not appear in check() output
      '这': '這',
      '个': '個',
      '优': '優',
      '化': '化',
    },
    ambiguous: {},
  },
  terms: {
    cn: {
      '软件': '軟體',
      '优化': '最佳化',
    },
    hk: {
      '巴士': '公車',
    },
  },
};

describe('createConverter.convert', () => {
  it('returns empty string unchanged', () => {
    const c = createConverter(DATA);
    expect(c.convert('')).toBe('');
  });

  it('applies term layer for cn source', () => {
    const c = createConverter(DATA, { sources: ['cn'] });
    expect(c.convert('这个软件')).toBe('這個軟體');
  });

  it('applies hk terms when hk is in sources', () => {
    const c = createConverter(DATA, { sources: ['cn', 'hk'] });
    expect(c.convert('搭巴士')).toBe('搭公車');
  });

  it('does not apply char layer when cn is not in sources', () => {
    // hk-only: no char layer, so 软件 (no hk term) passes through unchanged
    const c = createConverter(DATA, { sources: ['hk'] });
    expect(c.convert('软件')).toBe('软件');
  });

  it('customDict overrides built-in terms', () => {
    const c = createConverter(DATA, {
      sources: ['cn'],
      customDict: { '软件': '軟件' }, // HK-style override
    });
    expect(c.convert('软件')).toBe('軟件');
  });

  it('throws on empty sources array', () => {
    expect(() => createConverter(DATA, { sources: [] })).toThrow(/non-empty array/);
  });

  it('throws on unknown source', () => {
    expect(() => createConverter(DATA, { sources: ['xx' as any] })).toThrow(/unknown source/);
  });

  it('throws TypeError on non-string convert input', () => {
    const c = createConverter(DATA);
    expect(() => c.convert(null as any)).toThrow(TypeError);
    expect(() => c.convert(42 as any)).toThrow(TypeError);
  });

  it('returns the default sources [cn, hk] when options are omitted', () => {
    const c = createConverter(DATA);
    expect(c.convert('这个软件')).toBe('這個軟體');  // cn terms
    expect(c.convert('巴士')).toBe('公車');          // hk terms
  });
});
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd sdk/typescript && pnpm test converter`
Expected: FAIL — `Cannot find module '../src/core/converter'`

- [ ] **Step 3: Implement `src/core/converter.ts` (convert only)**

```ts
import { AhoCorasickMatcher, type Utf16Match } from './matcher';
import type {
  Converter,
  ConverterOptions,
  Match,
  LookupResult,
  Source,
  ZhtwData,
} from './types';
import { utf16ToCodepoint } from './codepoint';

const DEFAULT_SOURCES: readonly Source[] = ['cn', 'hk'];
const VALID_SOURCES = new Set<string>(['cn', 'hk']);

function validateOptions(options: ConverterOptions): readonly Source[] {
  if (options.sources === undefined) return DEFAULT_SOURCES;
  if (!Array.isArray(options.sources) || options.sources.length === 0) {
    throw new Error(
      'zhtw: sources must be a non-empty array of "cn" | "hk", or omitted',
    );
  }
  for (const s of options.sources) {
    if (!VALID_SOURCES.has(s)) {
      throw new Error(`zhtw: unknown source '${s}', expected 'cn' or 'hk'`);
    }
  }
  return options.sources;
}

function mergeTerms(
  data: ZhtwData,
  sources: readonly Source[],
  customDict: Record<string, string> | undefined,
): Record<string, string> {
  const merged: Record<string, string> = {};
  for (const src of sources) {
    const bucket = data.terms[src];
    if (!bucket) continue;
    for (const [k, v] of Object.entries(bucket)) {
      if (k.length === 0) continue;
      merged[k] = v;
    }
  }
  if (customDict) {
    for (const [k, v] of Object.entries(customDict)) {
      if (k.length === 0) continue;
      merged[k] = v; // customDict wins
    }
  }
  return merged;
}

function requireString(value: unknown, fnName: string): string {
  if (typeof value !== 'string') {
    throw new TypeError(`zhtw: ${fnName} text must be a string`);
  }
  return value;
}

/**
 * Apply the char layer (single-codepoint charmap) to a string. Returns the
 * transformed string. Walks codepoints so supplementary-plane chars work.
 */
function applyCharmap(text: string, charmap: Record<string, string>): string {
  let out = '';
  for (const ch of text) {
    const mapped = charmap[ch];
    out += mapped !== undefined ? mapped : ch;
  }
  return out;
}

export function createConverter(
  data: ZhtwData,
  options: ConverterOptions = {},
): Converter {
  const sources = validateOptions(options);
  const terms = mergeTerms(data, sources, options.customDict);
  const matcher = new AhoCorasickMatcher(terms);
  const charmap = data.charmap.chars;
  const charLayerEnabled = sources.includes('cn');

  function convert(text: string): string {
    requireString(text, 'convert');
    if (text.length === 0) return '';
    const afterTerms = matcher.replaceAll(text);
    return charLayerEnabled ? applyCharmap(afterTerms, charmap) : afterTerms;
  }

  function check(_text: string): Match[] {
    requireString(_text, 'check');
    throw new Error('check: implemented in Task 7');
  }

  function lookup(_word: string): LookupResult {
    requireString(_word, 'lookup');
    throw new Error('lookup: implemented in Task 8');
  }

  return { convert, check, lookup };
}

// Re-export so callers can import utilities if needed (internal helpers stay private).
export { utf16ToCodepoint };
export type { Utf16Match };
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd sdk/typescript && pnpm test converter`
Expected: All 9 convert tests pass. (check/lookup tests don't exist yet.)

- [ ] **Step 5: Commit**

```bash
git add sdk/typescript/src/core/converter.ts sdk/typescript/tests/converter.test.ts
git commit -m "feat(ts-sdk): implement convert() in converter factory"
```

---

## Task 7: Converter.check() (TDD)

**Files:**
- Modify: `sdk/typescript/src/core/converter.ts` (replace `check` stub)
- Modify: `sdk/typescript/tests/converter.test.ts` (add `check` tests)

**Context:** `check` returns all matches found — term matches from the matcher + char matches from the charmap scan. Per `ZhtwConverter.java::check()`, term matches and char matches are **both** emitted (the char scan does NOT skip positions already covered by a term match — this differs from `lookup`). Positions must be in codepoint indices.

- [ ] **Step 1: Add failing tests for `check`**

Append to `sdk/typescript/tests/converter.test.ts`:

```ts
describe('createConverter.check', () => {
  it('returns [] for empty input', () => {
    const c = createConverter(DATA, { sources: ['cn'] });
    expect(c.check('')).toEqual([]);
  });

  it('reports a term match with codepoint indices', () => {
    const c = createConverter(DATA, { sources: ['cn'] });
    expect(c.check('这个软件')).toEqual(
      expect.arrayContaining([
        { start: 2, end: 4, source: '软件', target: '軟體' },
      ]),
    );
  });

  it('reports char matches where the charmap differs from the input', () => {
    const c = createConverter(DATA, { sources: ['cn'] });
    const matches = c.check('这个');
    // Both 这→這 and 个→個 should appear.
    expect(matches).toContainEqual({ start: 0, end: 1, source: '这', target: '這' });
    expect(matches).toContainEqual({ start: 1, end: 2, source: '个', target: '個' });
  });

  it('does NOT report identity char mappings (件 → 件)', () => {
    const c = createConverter(DATA, { sources: ['cn'] });
    const matches = c.check('件');
    // 件 maps to 件 in fixture DATA; check() should skip no-op entries.
    expect(matches).toEqual([]);
  });

  it('reports BOTH term and char matches at overlapping positions', () => {
    // Term 软件 covers positions 0..2, but char scan still emits 软→軟 at position 0.
    // This is Java's behavior (differs from lookup, which skips covered positions).
    const c = createConverter(DATA, { sources: ['cn'] });
    const matches = c.check('软件');
    expect(matches).toContainEqual({ start: 0, end: 2, source: '软件', target: '軟體' });
    expect(matches).toContainEqual({ start: 0, end: 1, source: '软', target: '軟' });
  });

  it('does not run char layer when cn is not in sources', () => {
    const c = createConverter(DATA, { sources: ['hk'] });
    // No term matches, no char layer → no output.
    expect(c.check('软件')).toEqual([]);
  });
});
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd sdk/typescript && pnpm test converter`
Expected: FAIL — `check: implemented in Task 7`

- [ ] **Step 3: Implement `check` in `src/core/converter.ts`**

Replace the `check` stub (keep `convert` as-is) with:

```ts
  function check(text: string): Match[] {
    requireString(text, 'check');
    if (text.length === 0) return [];
    const results: Match[] = [];

    // Term layer: matcher returns UTF-16 positions; convert to codepoint.
    for (const m of matcher.findMatches(text)) {
      results.push({
        start: utf16ToCodepoint(text, m.start),
        end: utf16ToCodepoint(text, m.end),
        source: m.source,
        target: m.target,
      });
    }

    // Char layer: walk codepoints regardless of term coverage (Java semantics).
    if (charLayerEnabled) {
      let cp = 0;
      for (const ch of text) {
        const mapped = charmap[ch];
        if (mapped !== undefined && mapped !== ch) {
          results.push({ start: cp, end: cp + 1, source: ch, target: mapped });
        }
        cp++;
      }
    }
    return results;
  }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd sdk/typescript && pnpm test converter`
Expected: All tests pass (previous convert tests + 6 new check tests).

- [ ] **Step 5: Commit**

```bash
git add sdk/typescript/src/core/converter.ts sdk/typescript/tests/converter.test.ts
git commit -m "feat(ts-sdk): implement check() with codepoint positions"
```

---

## Task 8: Converter.lookup() (TDD)

**Files:**
- Modify: `sdk/typescript/src/core/converter.ts` (replace `lookup` stub)
- Modify: `sdk/typescript/tests/converter.test.ts` (add `lookup` tests)

**Context:** `lookup` is the most intricate API. Per `ZhtwConverter.java::lookup()`:
1. Work internally in UTF-16 positions.
2. Run term matcher, collect matches, mark UTF-16 positions covered.
3. Run char scan **only on uncovered codepoints** (differs from check).
4. Merge term + char details, sort by UTF-16 position.
5. Build output by walking the sorted details with a UTF-16 cursor: append uncovered slice, then the replacement target, advance cursor past the match.
6. Convert positions to codepoint indices **for the public result only**.
7. Set `changed = output !== input`.

- [ ] **Step 1: Add failing tests for `lookup`**

Append to `sdk/typescript/tests/converter.test.ts`:

```ts
describe('createConverter.lookup', () => {
  it('returns the empty-input baseline', () => {
    const c = createConverter(DATA, { sources: ['cn'] });
    expect(c.lookup('')).toEqual({
      input: '',
      output: '',
      changed: false,
      details: [],
    });
  });

  it('returns changed=false when nothing matches', () => {
    const c = createConverter(DATA, { sources: ['cn'] });
    const r = c.lookup('hello');
    expect(r.output).toBe('hello');
    expect(r.changed).toBe(false);
    expect(r.details).toEqual([]);
  });

  it('applies a term match and records details', () => {
    const c = createConverter(DATA, { sources: ['cn'] });
    const r = c.lookup('软件');
    expect(r.output).toBe('軟體');
    expect(r.changed).toBe(true);
    expect(r.details).toEqual([
      { source: '软件', target: '軟體', layer: 'term', position: 0 },
    ]);
  });

  it('skips char layer on positions already covered by a term match', () => {
    const c = createConverter(DATA, { sources: ['cn'] });
    // Term 软件 covers 0..2. Char scan must NOT emit 软→軟 or 件→件 here.
    const r = c.lookup('软件');
    expect(r.details.length).toBe(1);
    expect(r.details[0]!.layer).toBe('term');
  });

  it('applies char layer on uncovered codepoints in sorted order', () => {
    const c = createConverter(DATA, { sources: ['cn'] });
    // 这个 has no term; both chars fall through to char layer.
    const r = c.lookup('这个');
    expect(r.output).toBe('這個');
    expect(r.changed).toBe(true);
    expect(r.details).toEqual([
      { source: '这', target: '這', layer: 'char', position: 0 },
      { source: '个', target: '個', layer: 'char', position: 1 },
    ]);
  });

  it('mixes term + char in a single input, sorted by position', () => {
    const c = createConverter(DATA, { sources: ['cn'] });
    // 这(0) + 个(1) [char] + 软件(2..4) [term] + 化(5) [char; 优化 not at 4..6 because 化 follows]
    // Use a simpler mix: 这软件 → 這[软件→軟體]
    const r = c.lookup('这软件');
    expect(r.output).toBe('這軟體');
    expect(r.changed).toBe(true);
    expect(r.details).toEqual([
      { source: '这', target: '這', layer: 'char', position: 0 },
      { source: '软件', target: '軟體', layer: 'term', position: 1 },
    ]);
  });

  it('does not run char layer when cn is not in sources', () => {
    const c = createConverter(DATA, { sources: ['hk'] });
    const r = c.lookup('软件');
    expect(r.output).toBe('软件');
    expect(r.changed).toBe(false);
    expect(r.details).toEqual([]);
  });
});
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd sdk/typescript && pnpm test converter`
Expected: FAIL — `lookup: implemented in Task 8`

- [ ] **Step 3: Implement `lookup` in `src/core/converter.ts`**

Replace the `lookup` stub with:

```ts
  function lookup(word: string): LookupResult {
    requireString(word, 'lookup');
    if (word.length === 0) {
      return { input: '', output: '', changed: false, details: [] };
    }

    // Internal type used only for sorting by UTF-16 position before we
    // build the output and convert to codepoint indices.
    interface InternalDetail {
      source: string;
      target: string;
      layer: 'term' | 'char';
      utf16Start: number;
      utf16End: number;
    }

    const internal: InternalDetail[] = [];
    const covered = new Set<number>(); // UTF-16 code-unit indices covered by a term match

    // Term layer.
    for (const m of matcher.findMatches(word)) {
      internal.push({
        source: m.source,
        target: m.target,
        layer: 'term',
        utf16Start: m.start,
        utf16End: m.end,
      });
      for (let i = m.start; i < m.end; i++) covered.add(i);
    }

    // Char layer (only if 'cn' is in sources). Skip covered codepoints.
    if (charLayerEnabled) {
      let i = 0;
      while (i < word.length) {
        const code = word.charCodeAt(i);
        const isHigh = code >= 0xd800 && code <= 0xdbff && i + 1 < word.length;
        const step = isHigh ? 2 : 1;
        if (!covered.has(i)) {
          const ch = word.substring(i, i + step);
          const mapped = charmap[ch];
          if (mapped !== undefined && mapped !== ch) {
            internal.push({
              source: ch,
              target: mapped,
              layer: 'char',
              utf16Start: i,
              utf16End: i + step,
            });
          }
        }
        i += step;
      }
    }

    // Sort by UTF-16 start position.
    internal.sort((a, b) => a.utf16Start - b.utf16Start);

    // Build output string by walking details with a UTF-16 cursor.
    let output = '';
    let cursor = 0;
    for (const d of internal) {
      if (d.utf16Start > cursor) output += word.substring(cursor, d.utf16Start);
      output += d.target;
      cursor = d.utf16End;
    }
    if (cursor < word.length) output += word.substring(cursor);

    // Convert UTF-16 positions to codepoint indices for the public result.
    const details = internal.map((d) => ({
      source: d.source,
      target: d.target,
      layer: d.layer,
      position: utf16ToCodepoint(word, d.utf16Start),
    }));

    return {
      input: word,
      output,
      changed: output !== word,
      details,
    };
  }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd sdk/typescript && pnpm test converter`
Expected: All tests pass.

- [ ] **Step 5: Commit**

```bash
git add sdk/typescript/src/core/converter.ts sdk/typescript/tests/converter.test.ts
git commit -m "feat(ts-sdk): implement lookup() with char/term layer merge"
```

---

## Task 9: Data loaders (Node + browser)

**Files:**
- Create: `sdk/typescript/src/data/node.ts`
- Create: `sdk/typescript/src/data/browser.ts`

**Context:** Two tiny adapters, one per platform. Node reads `zhtw-data.json` from next to the compiled entry file (copied there by tsup's onSuccess). Browser imports the JSON directly — tsup inlines it at build time. The browser import path `'../../../data/zhtw-data.json'` resolves from `sdk/typescript/src/data/browser.ts` to `sdk/data/zhtw-data.json` — the single source of truth that `make bump` regenerates.

- [ ] **Step 1: Write `src/data/node.ts`**

```ts
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import type { ZhtwData } from '../core/types';

// Resolve the directory of the compiled entry file at runtime. Works under
// both CJS (__dirname is defined) and ESM (use import.meta.url).
const HERE =
  typeof __dirname !== 'undefined'
    ? __dirname
    : dirname(fileURLToPath(import.meta.url));

const DATA_PATH = join(HERE, 'zhtw-data.json');

export function loadData(): ZhtwData {
  try {
    const raw = readFileSync(DATA_PATH, 'utf-8');
    return JSON.parse(raw) as ZhtwData;
  } catch (err) {
    const reason = err instanceof Error ? err.message : String(err);
    throw new Error(`zhtw: failed to load zhtw-data.json: ${reason}`);
  }
}
```

- [ ] **Step 2: Write `src/data/browser.ts`**

```ts
// Import the canonical source at sdk/data/zhtw-data.json directly.
// tsup inlines this JSON into the browser bundle at build time, so the
// runtime has no fs/path dependency.
import data from '../../../data/zhtw-data.json';
import type { ZhtwData } from '../core/types';

export function loadData(): ZhtwData {
  return data as unknown as ZhtwData;
}
```

- [ ] **Step 3: Type-check**

Run: `cd sdk/typescript && npx tsc --noEmit`
Expected: No errors.

- [ ] **Step 4: Commit**

```bash
git add sdk/typescript/src/data/node.ts sdk/typescript/src/data/browser.ts
git commit -m "feat(ts-sdk): add node and browser data loaders"
```

---

## Task 10: Entry points (Node + browser)

**Files:**
- Create: `sdk/typescript/src/index.node.ts`
- Create: `sdk/typescript/src/index.browser.ts`

**Context:** Thin wrappers. Each caches the parsed data and the default converter at module level, so the convenience `convert`/`check`/`lookup` and any factory-made converter share the same in-memory copy. The two files differ only in which `loadData` they import.

- [ ] **Step 1: Write `src/index.node.ts`**

```ts
import { loadData } from './data/node';
import { createConverter as createCoreConverter } from './core/converter';
import type {
  Converter,
  ConverterOptions,
  Match,
  LookupResult,
  ConversionDetail,
  Source,
  ZhtwData,
} from './core/types';

let cachedData: ZhtwData | null = null;
let defaultConverter: Converter | null = null;

function getData(): ZhtwData {
  if (!cachedData) cachedData = loadData();
  return cachedData;
}

function getDefault(): Converter {
  if (!defaultConverter) defaultConverter = createCoreConverter(getData());
  return defaultConverter;
}

export function convert(text: string): string {
  return getDefault().convert(text);
}

export function check(text: string): Match[] {
  return getDefault().check(text);
}

export function lookup(word: string): LookupResult {
  return getDefault().lookup(word);
}

export function createConverter(options: ConverterOptions = {}): Converter {
  return createCoreConverter(getData(), options);
}

export type {
  Converter,
  ConverterOptions,
  Match,
  LookupResult,
  ConversionDetail,
  Source,
};
```

- [ ] **Step 2: Write `src/index.browser.ts`**

Identical to `index.node.ts` except for the loader import:

```ts
import { loadData } from './data/browser';
import { createConverter as createCoreConverter } from './core/converter';
import type {
  Converter,
  ConverterOptions,
  Match,
  LookupResult,
  ConversionDetail,
  Source,
  ZhtwData,
} from './core/types';

let cachedData: ZhtwData | null = null;
let defaultConverter: Converter | null = null;

function getData(): ZhtwData {
  if (!cachedData) cachedData = loadData();
  return cachedData;
}

function getDefault(): Converter {
  if (!defaultConverter) defaultConverter = createCoreConverter(getData());
  return defaultConverter;
}

export function convert(text: string): string {
  return getDefault().convert(text);
}

export function check(text: string): Match[] {
  return getDefault().check(text);
}

export function lookup(word: string): LookupResult {
  return getDefault().lookup(word);
}

export function createConverter(options: ConverterOptions = {}): Converter {
  return createCoreConverter(getData(), options);
}

export type {
  Converter,
  ConverterOptions,
  Match,
  LookupResult,
  ConversionDetail,
  Source,
};
```

- [ ] **Step 3: Type-check**

Run: `cd sdk/typescript && npx tsc --noEmit`
Expected: No errors.

- [ ] **Step 4: Commit**

```bash
git add sdk/typescript/src/index.node.ts sdk/typescript/src/index.browser.ts
git commit -m "feat(ts-sdk): add node and browser entry points with lazy caching"
```

---

## Task 11: First build + verify dist layout

**Files:**
- No new files; verifies tsup config + entry points produce the right output

**Context:** Before writing the golden test, we need a real `dist/` so we know the build pipeline works. This task runs `pnpm build` and asserts the six expected files exist.

- [ ] **Step 1: Run the build**

Run: `cd sdk/typescript && pnpm build`
Expected: Completes without errors. Console shows `[tsup] copied zhtw-data.json → dist/`.

- [ ] **Step 2: Verify `dist/` contents**

Run: `ls sdk/typescript/dist/`
Expected output includes:
- `index.node.mjs`
- `index.node.cjs`
- `index.node.d.ts`
- `index.browser.mjs`
- `index.browser.cjs`
- `index.browser.d.ts`
- `zhtw-data.json`

- [ ] **Step 3: Verify the browser bundle does NOT reference `node:fs`**

Run: `grep -l 'node:fs' sdk/typescript/dist/index.browser.* || echo "clean"`
Expected: `clean`

If the grep matches anything, the tsup config is leaking the Node loader into the browser bundle.

- [ ] **Step 4: Smoke-import the built Node entry from a throwaway script**

Run: `cd sdk/typescript && node -e "import('./dist/index.node.mjs').then(m => console.log(m.convert('这个软件')))"`
Expected: `這個軟體` (or the project's canonical conversion of that phrase).

- [ ] **Step 5: Commit `dist/` is NOT tracked (covered by .gitignore); nothing new to commit here**

Skip. Move on.

---

## Task 12: Golden cross-SDK parity test (TDD)

**Files:**
- Create: `sdk/typescript/tests/golden.test.ts`

**Context:** This is the non-negotiable release gate. The same `sdk/data/golden-test.json` already drives Python and Java tests. Load the JSON directly in the test (we can read the real fixture file, not the in-memory minimal fixture from `converter.test.ts`), parametrize over all three sections, and assert zero divergence.

The test needs to load **both** the real data file and the golden fixtures. We'll use `createConverter` directly with `loadData()` from the node loader to avoid depending on the lazy module-level default.

- [ ] **Step 1: Write `tests/golden.test.ts`**

```ts
import { describe, it, expect } from 'vitest';
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { createConverter } from '../src/core/converter';
import type { Source, ZhtwData } from '../src/core/types';

// Load the real data file and golden fixtures from sdk/data/.
const DATA_FILE = resolve(__dirname, '../../data/zhtw-data.json');
const GOLDEN_FILE = resolve(__dirname, '../../data/golden-test.json');

const data = JSON.parse(readFileSync(DATA_FILE, 'utf-8')) as ZhtwData;

interface GoldenConvertCase {
  input: string;
  sources: Source[];
  expected: string;
}

interface GoldenCheckMatch {
  start: number;
  end: number;
  source: string;
  target: string;
}

interface GoldenCheckCase {
  input: string;
  sources: Source[];
  expected_matches: GoldenCheckMatch[];
}

interface GoldenLookupDetail {
  source: string;
  target: string;
  layer: 'term' | 'char';
  position: number;
}

interface GoldenLookupCase {
  input: string;
  sources: Source[];
  expected_output: string;
  expected_changed: boolean;
  expected_details: GoldenLookupDetail[];
}

interface GoldenFile {
  version: string;
  convert: GoldenConvertCase[];
  check: GoldenCheckCase[];
  lookup: GoldenLookupCase[];
}

const golden = JSON.parse(readFileSync(GOLDEN_FILE, 'utf-8')) as GoldenFile;

describe('golden-test.json — convert parity', () => {
  for (const tc of golden.convert) {
    it(`convert(${JSON.stringify(tc.input)}, ${JSON.stringify(tc.sources)})`, () => {
      const conv = createConverter(data, { sources: tc.sources });
      expect(conv.convert(tc.input)).toBe(tc.expected);
    });
  }
});

describe('golden-test.json — check parity', () => {
  for (const tc of golden.check) {
    it(`check(${JSON.stringify(tc.input)}, ${JSON.stringify(tc.sources)})`, () => {
      const conv = createConverter(data, { sources: tc.sources });
      const actual = conv.check(tc.input);
      // Sort both sides by (start, end, source) for a stable comparison,
      // since the spec does not mandate a specific order and Java/Python
      // may emit in subtly different orders.
      const norm = (arr: GoldenCheckMatch[]) =>
        [...arr].sort(
          (a, b) =>
            a.start - b.start ||
            a.end - b.end ||
            a.source.localeCompare(b.source),
        );
      expect(norm(actual)).toEqual(norm(tc.expected_matches));
    });
  }
});

describe('golden-test.json — lookup parity', () => {
  for (const tc of golden.lookup) {
    it(`lookup(${JSON.stringify(tc.input)}, ${JSON.stringify(tc.sources)})`, () => {
      const conv = createConverter(data, { sources: tc.sources });
      const r = conv.lookup(tc.input);
      expect(r.output).toBe(tc.expected_output);
      expect(r.changed).toBe(tc.expected_changed);
      expect(r.details).toEqual(tc.expected_details);
    });
  }
});
```

Note on order: `check` normalizes both sides before comparing because the spec does not mandate a specific emission order. `lookup` does **not** normalize — per spec §5 and `ZhtwConverter.java`, details are sorted by (UTF-16) position, and Java/Python produce the same order; we assert exact equality to catch any drift.

- [ ] **Step 2: Run the golden test**

Run: `cd sdk/typescript && pnpm test golden`
Expected: All 21 fixture cases pass (8 convert + 8 check + 5 lookup).

If `check` fails with an order mismatch, the normalization in step 1 handles it. If it fails with a value mismatch, that's a real bug — debug the converter.

If `lookup` fails with an order mismatch, compare `r.details` vs `tc.expected_details` carefully: the Java SDK sorts by UTF-16 position, which matches our implementation, so any order difference is a bug in our port.

- [ ] **Step 3: Commit**

```bash
git add sdk/typescript/tests/golden.test.ts
git commit -m "test(ts-sdk): add cross-SDK golden parity tests for convert/check/lookup"
```

---

## Task 13: Public API smoke test (Node + happy-dom)

**Files:**
- Create: `sdk/typescript/tests/api.test.ts`

**Context:** Exercises the module-level convenience functions under both the Node environment (default) and happy-dom. The happy-dom block uses a `@vitest-environment` pragma — but pragmas are per-file, so we use Vitest's `environmentMatchGlobs` in vitest.config.ts, or simpler: a single file with `/** @vitest-environment happy-dom */` that only imports the **browser** build. To avoid a second config file, split the api test into two files if needed — but for v1, a single Node-based smoke test is enough since the pack.test (Task 15) proves the browser loader via install+import.

Actually, per spec §8 we want at least one happy-dom test. Keep it simple: a single `api.test.ts` file under happy-dom that imports the source directly (not the dist) and checks that no Node built-ins leak. The source of `src/index.browser.ts` imports `./data/browser`, which in turn imports the JSON — Vite handles JSON imports natively via Vitest, so this works without a build.

- [ ] **Step 1: Write `tests/api.test.ts`**

```ts
/** @vitest-environment happy-dom */
import { describe, it, expect } from 'vitest';
import {
  convert,
  check,
  lookup,
  createConverter,
} from '../src/index.browser';

describe('public API (browser entry under happy-dom)', () => {
  it('module-level convert works', () => {
    expect(typeof convert('')).toBe('string');
  });

  it('module-level check returns an array', () => {
    expect(Array.isArray(check(''))).toBe(true);
  });

  it('module-level lookup returns a LookupResult shape', () => {
    const r = lookup('');
    expect(r).toEqual({ input: '', output: '', changed: false, details: [] });
  });

  it('createConverter returns a working Converter', () => {
    const c = createConverter({ sources: ['cn'] });
    expect(typeof c.convert).toBe('function');
    expect(typeof c.check).toBe('function');
    expect(typeof c.lookup).toBe('function');
  });

  it('end-to-end: a known conversion goes through', () => {
    // Use the real data file; this phrase is in the canonical corpus.
    // Exact output is verified by the golden test; here we just assert change.
    const c = createConverter({ sources: ['cn'] });
    const r = c.lookup('软件');
    expect(r.changed).toBe(true);
    expect(r.output).not.toBe('软件');
  });

  it('default sources convert works without options', () => {
    const c = createConverter();
    expect(typeof c.convert('hello')).toBe('string');
  });
});
```

- [ ] **Step 2: Run the api test**

Run: `cd sdk/typescript && pnpm test api`
Expected: All 6 tests pass under happy-dom.

If Vitest complains about happy-dom not being installed, run `pnpm install` (it's already in devDependencies from Task 1).

- [ ] **Step 3: Commit**

```bash
git add sdk/typescript/tests/api.test.ts
git commit -m "test(ts-sdk): add public API smoke test under happy-dom"
```

---

## Task 14: Full local test run + build sanity check

**Files:**
- No new files; just verification

**Context:** Run the entire suite to catch any cross-test interaction bugs before we wire in CI.

- [ ] **Step 1: Run full vitest suite**

Run: `cd sdk/typescript && pnpm test`
Expected: All tests pass across all 5 included files (codepoint, matcher, converter, golden, api). `pack.test.ts` is excluded by config.

- [ ] **Step 2: Re-run the build from clean**

Run: `cd sdk/typescript && rm -rf dist && pnpm build`
Expected: Build completes, `dist/` contains all 7 expected files (see Task 11).

- [ ] **Step 3: No commit — verification only**

Move on.

---

## Task 15: Pack + install smoke test (CI-only)

**Files:**
- Create: `sdk/typescript/tests/pack.test.ts`

**Context:** Proves the published tarball actually works when installed from scratch. This is the only test that exercises the real `package.json exports` resolution with `node` condition plus the runtime `fs.readFileSync(join(__dirname, 'zhtw-data.json'))` path. Gated behind `ZHTW_TS_RUN_PACK=1` because it pollutes the filesystem and takes ~20s.

Uses `execFileSync` with explicit argv arrays (never shell strings) so there is no possibility of shell-interpretation or command injection.

- [ ] **Step 1: Write `tests/pack.test.ts`**

```ts
import { describe, it, expect } from 'vitest';
import { execFileSync } from 'node:child_process';
import { mkdtempSync, writeFileSync, readdirSync, rmSync, mkdirSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';

// Skipped by default; CI sets ZHTW_TS_RUN_PACK=1 to run it.
const runPack = process.env.ZHTW_TS_RUN_PACK === '1';
const describeOrSkip = runPack ? describe : describe.skip;

describeOrSkip('pack + install smoke test', () => {
  it('packs, installs, and imports from the tarball', () => {
    const pkgDir = resolve(__dirname, '..');
    const scratch = mkdtempSync(join(tmpdir(), 'zhtw-js-pack-'));
    try {
      // 1. Pack the package into scratch.
      const packDir = join(scratch, 'tgz');
      mkdirSync(packDir, { recursive: true });
      execFileSync('pnpm', ['pack', '--pack-destination', packDir], {
        cwd: pkgDir,
        encoding: 'utf-8',
        stdio: 'inherit',
      });
      const tarball = readdirSync(packDir).find((f) => f.endsWith('.tgz'));
      if (!tarball) throw new Error('pnpm pack did not produce a .tgz');
      const tarballPath = join(packDir, tarball);

      // 2. Install the tarball into a fresh consumer dir.
      const consumer = join(scratch, 'consumer');
      mkdirSync(consumer, { recursive: true });
      writeFileSync(
        join(consumer, 'package.json'),
        JSON.stringify({ name: 'consumer', version: '0.0.0', type: 'module', private: true }),
      );
      execFileSync('npm', ['install', '--silent', tarballPath], {
        cwd: consumer,
        stdio: 'inherit',
      });

      // 3. Write a smoke script that exercises all three APIs.
      const smoke = `
import { convert, check, lookup, createConverter } from 'zhtw-js';
const c1 = convert('hello');
if (typeof c1 !== 'string') throw new Error('convert: not a string');
const c2 = check('');
if (!Array.isArray(c2)) throw new Error('check: not an array');
const c3 = lookup('');
if (c3.changed !== false) throw new Error('lookup: empty should be unchanged');
const conv = createConverter({ sources: ['cn'] });
if (typeof conv.convert !== 'function') throw new Error('factory: no convert');
console.log('OK');
`;
      writeFileSync(join(consumer, 'smoke.mjs'), smoke);

      // 4. Run the smoke script.
      const out = execFileSync('node', ['smoke.mjs'], {
        cwd: consumer,
        encoding: 'utf-8',
      });
      expect(out.trim()).toBe('OK');
    } finally {
      rmSync(scratch, { recursive: true, force: true });
    }
  }, 60_000);
});
```

- [ ] **Step 2: Run it locally (opt-in)**

Run: `cd sdk/typescript && ZHTW_TS_RUN_PACK=1 npx vitest run tests/pack.test.ts`
Expected: Test passes (takes ~20-30 seconds). Because `pack.test.ts` is excluded from the default glob in `vitest.config.ts`, we invoke it by file path.

If this fails with a "No tests found" error, remove `tests/pack.test.ts` from the `exclude` array in `vitest.config.ts` temporarily, or run `npx vitest run --testPathIgnorePatterns= tests/pack.test.ts`.

- [ ] **Step 3: Commit**

```bash
git add sdk/typescript/tests/pack.test.ts
git commit -m "test(ts-sdk): add pack+install smoke test (CI-only)"
```

---

## Task 16: CI workflow

**Files:**
- Create: `.github/workflows/sdk-typescript.yml`

**Context:** Runs tests across Node 18/20/22 on push + PR, runs the pack test, and on `release: published` publishes to npm with provenance.

- [ ] **Step 1: Write the workflow**

```yaml
name: SDK TypeScript

on:
  push:
    branches: [main]
    paths:
      - 'sdk/typescript/**'
      - 'sdk/data/**'
      - '.github/workflows/sdk-typescript.yml'
  pull_request:
    paths:
      - 'sdk/typescript/**'
      - 'sdk/data/**'
      - '.github/workflows/sdk-typescript.yml'
  release:
    types: [published]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        node: ['18', '20', '22']
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with:
          version: 9
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
          cache: pnpm
          cache-dependency-path: sdk/typescript/pnpm-lock.yaml
      - name: Install dependencies
        working-directory: sdk/typescript
        run: pnpm install --frozen-lockfile
      - name: Type-check
        working-directory: sdk/typescript
        run: npx tsc --noEmit
      - name: Run tests
        working-directory: sdk/typescript
        run: pnpm test
      - name: Build
        working-directory: sdk/typescript
        run: pnpm build
      - name: Verify dist layout
        working-directory: sdk/typescript
        run: |
          test -f dist/index.node.mjs
          test -f dist/index.node.cjs
          test -f dist/index.node.d.ts
          test -f dist/index.browser.mjs
          test -f dist/index.browser.cjs
          test -f dist/index.browser.d.ts
          test -f dist/zhtw-data.json
      - name: Pack + install smoke test
        working-directory: sdk/typescript
        env:
          ZHTW_TS_RUN_PACK: '1'
        run: npx vitest run tests/pack.test.ts

  publish:
    needs: test
    if: github.event_name == 'release' && github.event.action == 'published'
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with:
          version: 9
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: pnpm
          cache-dependency-path: sdk/typescript/pnpm-lock.yaml
          registry-url: 'https://registry.npmjs.org'
      - name: Install dependencies
        working-directory: sdk/typescript
        run: pnpm install --frozen-lockfile
      - name: Build
        working-directory: sdk/typescript
        run: pnpm build
      - name: Publish to npm
        working-directory: sdk/typescript
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
        run: pnpm publish --provenance --access public --no-git-checks
```

- [ ] **Step 2: Lint the YAML locally (best-effort)**

Run: `cd /Users/tim/GitHub/zhtw && npx --yes yaml-lint .github/workflows/sdk-typescript.yml 2>&1 || true`
Expected: No hard errors. (If yaml-lint is unavailable, skip — GitHub will parse it on push.)

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/sdk-typescript.yml
git commit -m "ci(ts-sdk): add test + publish workflow for Node 18/20/22"
```

---

## Task 17: Benchmark script

**Files:**
- Create: `sdk/typescript/scripts/bench.ts`

**Context:** Spec §11 item 9 requires a "lightweight throughput measurement" — not a full benchmark suite, just enough to put a number in the root README. We measure `convert` over a synthetic ~100KB text and report MB/s.

- [ ] **Step 1: Write `scripts/bench.ts`**

```ts
import { convert } from '../src/index.node';

// Build ~100KB of Simplified Chinese by repeating a seed phrase.
const seed = '这个软件需要优化，用户体验才能更好。';
const target = 100_000;
let text = '';
while (Buffer.byteLength(text, 'utf-8') < target) {
  text += seed;
}
const byteLen = Buffer.byteLength(text, 'utf-8');

// Warmup.
for (let i = 0; i < 5; i++) convert(text);

// Measure.
const runs = 100;
const start = performance.now();
for (let i = 0; i < runs; i++) convert(text);
const elapsedMs = performance.now() - start;

const totalBytes = byteLen * runs;
const mbPerSec = totalBytes / 1024 / 1024 / (elapsedMs / 1000);

console.log(`input size: ${(byteLen / 1024).toFixed(1)} KB`);
console.log(`runs: ${runs}`);
console.log(`elapsed: ${elapsedMs.toFixed(1)} ms`);
console.log(`throughput: ${mbPerSec.toFixed(1)} MB/s`);
```

- [ ] **Step 2: Run it**

Run: `cd sdk/typescript && pnpm bench`
Expected: Prints input size / runs / elapsed / throughput. Record the throughput number — you'll need it for Task 19 (root README update).

- [ ] **Step 3: Commit**

```bash
git add sdk/typescript/scripts/bench.ts
git commit -m "perf(ts-sdk): add lightweight convert throughput benchmark"
```

---

## Task 18: SDK README

**Files:**
- Create: `sdk/typescript/README.md`

**Context:** This is the npm landing page. Keep it focused: install, quick start (all three APIs), factory example, type reference, cross-SDK parity note, link back to the monorepo.

- [ ] **Step 1: Write `sdk/typescript/README.md`**

```markdown
# zhtw-js

> Traditional Chinese converter for Taiwan — TypeScript SDK

Simplified Chinese → Taiwan Traditional Chinese converter with zero runtime dependencies. Runs identically in Node.js ≥18 and modern browsers. Byte-for-byte compatible with the Python CLI and Java SDK, verified by a shared golden fixture.

## Install

```bash
npm install zhtw-js
# or
pnpm add zhtw-js
# or
yarn add zhtw-js
```

## Quick start

Zero config — the module exports a ready-to-use default converter:

```ts
import { convert, check, lookup } from 'zhtw-js';

convert('这个软件需要优化');
// => '這個軟體需要最佳化'

check('用户权限');
// => [{ start, end, source, target }, ...]

lookup('软件');
// => { input, output, changed, details: [...] }
```

## Advanced: custom converter

```ts
import { createConverter } from 'zhtw-js';

const conv = createConverter({
  sources: ['cn'],               // default: ['cn', 'hk']
  customDict: {                  // overrides built-in terms
    '自定义': '自訂',
  },
});

conv.convert('...');
conv.check('...');
conv.lookup('...');
```

## API reference

```ts
type Source = 'cn' | 'hk';

interface Match {
  start: number;      // codepoint index, inclusive
  end: number;        // codepoint index, exclusive
  source: string;
  target: string;
}

interface ConversionDetail {
  source: string;
  target: string;
  layer: 'term' | 'char';
  position: number;   // codepoint index
}

interface LookupResult {
  input: string;
  output: string;
  changed: boolean;
  details: ConversionDetail[];
}

interface ConverterOptions {
  sources?: Source[];                  // default: ['cn', 'hk']
  customDict?: Record<string, string>;
}

interface Converter {
  convert(text: string): string;
  check(text: string): Match[];
  lookup(word: string): LookupResult;
}
```

All `start` / `end` / `position` fields are **Unicode codepoint indices**, not JavaScript UTF-16 code-unit indices. This keeps cross-SDK output byte-for-byte identical on supplementary-plane characters.

## Cross-SDK parity

Every release is verified against [`sdk/data/golden-test.json`](https://github.com/rajatim/zhtw/blob/main/sdk/data/golden-test.json), the shared fixture file consumed by the Python CLI, Java SDK, and TypeScript SDK. Zero divergence is a release gate.

## License

MIT. See [LICENSE](https://github.com/rajatim/zhtw/blob/main/LICENSE).

Part of the [rajatim/zhtw](https://github.com/rajatim/zhtw) monorepo.
```

- [ ] **Step 2: Verify the examples survive the pre-commit hook**

The repo's own pre-commit hook would convert `这个软件需要优化` → `這個軟體需要最佳化`, which would break the illustrative before/after semantics.

The hook excludes files matching certain patterns — check if `sdk/typescript/README.md` is excluded. If not, wrap the code blocks in `<!-- zhtw:disable --> ... <!-- zhtw:enable -->` markers like the spec does.

Run: `cd /Users/tim/GitHub/zhtw && uv run python -m zhtw check sdk/typescript/README.md`

- If it reports issues, wrap each problematic code block in the disable/enable markers.
- If it reports clean, no action needed.

- [ ] **Step 3: Commit**

```bash
git add sdk/typescript/README.md
git commit -m "docs(ts-sdk): add npm-facing README"
```

---

## Task 19: Root README — update multi-SDK table

**Files:**
- Modify: `README.md` (root)

**Context:** Spec §11 item 10 requires the root README's "Multi-language SDKs" table to show TypeScript as ✅ Stable with the throughput number captured in Task 17.

- [ ] **Step 1: Read the current root README**

Run: `head -n 200 /Users/tim/GitHub/zhtw/README.md | grep -n -A 10 -i 'multi.*sdk\|SDK.*多語\|SDK.*table\|typescript'`

- [ ] **Step 2: Locate the Multi-language SDKs table**

The table should have rows for Python, Java, TypeScript, Rust, .NET with columns like Status / Throughput / Notes. If the exact headings differ, adapt accordingly.

- [ ] **Step 3: Update the TypeScript row**

Replace the TypeScript row so:
- Status: ✅ Stable (was probably 🚧 or Placeholder)
- Throughput: the MB/s number from Task 17 (e.g., "~120 MB/s convert")
- Notes: any existing notes preserved, plus "isomorphic Node ≥18 + browsers"

Use `Edit` with precise `old_string` / `new_string` values based on what you find in step 1-2. If the table uses Chinese column headers, preserve them.

- [ ] **Step 4: Verify the table still renders**

Run: `uv run python -m zhtw check README.md` (to make sure no accidental simplified chars slipped in) and inspect the diff with `git diff README.md`.

- [ ] **Step 5: Commit**

```bash
git add README.md
git commit -m "docs: mark TypeScript SDK as stable in root README multi-SDK table"
```

---

## Task 20: Version-check alignment

**Files:**
- No new files; just verification

**Context:** `Makefile`'s `version-check` target already includes `sdk/typescript/package.json` (confirmed in the pre-work read). This task just confirms it passes at 4.0.0.

- [ ] **Step 1: Run version-check**

Run: `cd /Users/tim/GitHub/zhtw && make version-check`
Expected: All 7 version locations report `4.0.0` and the target exits 0 with "✅ All SDKs aligned at 4.0.0".

If it fails: inspect the mismatch and fix whichever file drifted. Do NOT modify the Makefile.

- [ ] **Step 2: No commit — verification only**

---

## Task 21: Final end-to-end sanity pass

**Files:**
- No new files; final verification

**Context:** Before handing this back, run the full Python + TypeScript test flow from a cold state to catch any staleness.

- [ ] **Step 1: Python tests still pass**

Run: `cd /Users/tim/GitHub/zhtw && pytest -q`
Expected: All tests pass. (The TS SDK changes should not affect Python tests; this is a safety net.)

- [ ] **Step 2: TypeScript tests pass from clean**

Run: `cd sdk/typescript && rm -rf dist node_modules && pnpm install && pnpm test && pnpm build`
Expected: Install → test → build all succeed.

- [ ] **Step 3: Pack test passes**

Run: `cd sdk/typescript && ZHTW_TS_RUN_PACK=1 npx vitest run tests/pack.test.ts`
Expected: Pack test prints "OK" and passes.

- [ ] **Step 4: Golden test explicitly passes against the real data**

Run: `cd sdk/typescript && pnpm test golden`
Expected: All 21 fixtures pass.

- [ ] **Step 5: Version check passes**

Run: `cd /Users/tim/GitHub/zhtw && make version-check`
Expected: Green.

- [ ] **Step 6: Git status is clean, no stray files**

Run: `git status`
Expected: Clean working tree (or only the files you intentionally want to commit as part of the final merge).

- [ ] **Step 7: Hand back to user**

Report results. This plan does NOT release to npm — that happens through the mono-versioning release flow (`make release VERSION=X.Y.Z`) which is outside this plan's scope.

---

<!-- zhtw:enable -->

## Self-Review

**Spec coverage map** (verified against `docs/superpowers/specs/2026-04-09-typescript-sdk-design.md`):

| Spec section | Requirements | Implementing tasks |
|---|---|---|
| §1 Goal | Node ≥18 + browsers, byte-identical output, zero-config + factory API, dual ESM+CJS, zero deps | Tasks 1, 10, 11, 12 |
| §2 Architecture | tsup, Vitest, self-impl AC, thin adapter | Tasks 1, 4, 5, 9, 10 |
| §3 Package layout | File structure incl. single data file in dist/ | Tasks 1, 9, 10, 11 |
| §4 Public API | Source, Match, LookupResult, strict-string inputs, Utf16Match separation | Tasks 2, 4, 6, 7, 8 |
| §5 Data flow | Lazy init, shared cache, two-layer pipeline | Tasks 6, 7, 8, 10 |
| §6 Components | core/{types,codepoint,matcher,converter}, data/{node,browser}, index.{node,browser} | Tasks 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| §7 Error handling | Empty string valid, non-string throws, empty sources throws, unknown source throws, customDict precedence, load failure | Tasks 6, 9 (load error), 7, 8 |
| §8 Testing | matcher, codepoint, converter, golden (convert+check+lookup), api (happy-dom), pack | Tasks 3, 4, 5, 6, 7, 8, 12, 13, 15 |
| §9 Distribution | package.json exports, files, engines, scripts, publish workflow | Tasks 1, 16 |
| §10 Non-goals | Explicitly excluded from every task — no streaming/worker/UMD/DI/JMH/tuning | (Excluded by design) |
| §11 Acceptance | All 10 criteria | Tasks 14, 15, 16, 17, 18, 19, 20, 21 |

**Placeholder scan:** No "TBD", "TODO", "fill in later", or "add appropriate X" phrases. All step code is complete. All tests have concrete assertions. All commands have expected output. The only conditional step is Task 18 Step 2 (check if the README needs zhtw:disable markers), which explicitly provides both branches.

**Type consistency:**
- `Source` is `'cn' | 'hk'` in `types.ts` (Task 2), `ConverterOptions.sources: Source[]` in `types.ts` (Task 2), consumed as `readonly Source[]` in `converter.ts` (Task 6). ✅
- `Utf16Match` is declared in `matcher.ts` (Task 4), used in `converter.ts` (Task 8 for lookup internal tracking), never re-exported from `index.{node,browser}.ts` (Task 10). ✅
- `Match.start/end` are codepoint indices everywhere in public API; `Utf16Match.start/end` are UTF-16 code-unit indices and only used internally. ✅
- Converter closures `convert/check/lookup` have identical signatures across `converter.ts` and the entry files. ✅
- `findMatches` returns `Utf16Match[]` in Task 4 and is consumed as such in Tasks 7 and 8. ✅
- `replaceAll` returns `string` in Task 5 and is consumed as such in Task 6 `convert`. ✅

---

## Execution

**Plan complete and saved to `docs/superpowers/plans/2026-04-09-typescript-sdk.md`. Two execution options:**

**1. Subagent-Driven (recommended)** — I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** — Execute tasks in this session using executing-plans, batch execution with checkpoints

**Which approach?**
