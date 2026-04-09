# zhtw-js (TypeScript SDK) Design Spec

**Date:** 2026-04-09
**Status:** Approved design, awaiting implementation plan
**Scope:** v1 of `zhtw-js` — isomorphic TypeScript SDK producing byte-identical output to Python/Java SDK

---

## 1. Goal

Ship `zhtw-js@4.0.0` — a native TypeScript SDK for the zhtw simplified→Taiwan traditional Chinese converter. It must:

1. Run unchanged in Node.js ≥18 and modern browsers.
2. Produce **byte-for-byte identical** output to the Python CLI and Java SDK for any input, verified by the shared `sdk/data/golden-test.json`.
3. Offer a zero-config convenience API (`convert`, `check`, `lookup`) and an advanced factory API (`createConverter`).
4. Ship as dual ESM+CJS with conditional `browser`/`node` entry points.
5. Depend on zero runtime packages (bundled AC automaton).

This is the first SDK to share `sdk/data/zhtw-data.json` from the browser side of the world. Python and Java are both server-side.

---

## 2. Architectural Decisions (Locked)

| Decision | Choice | Rationale |
|---|---|---|
| Targets | Node ≥18 + modern browsers (isomorphic) | Covers backend, CLI, Next.js SSR, Vite, browser extensions |
| Data loading | Dual entry points: Node `fs.readFileSync` / browser bundler-inlined JSON | Node bundle stays ~5KB; browser bundle ~320KB gzip; both APIs stay sync |
| API style | Functional + factory (`convert(text)` + `createConverter(opts)`) | Most idiomatic TS; tree-shakable; no singleton gymnastics (JS is single-threaded) |
| Module format | Dual ESM + CJS | Max consumer compat including Jest-default projects and Webpack 4 holdouts |
| AC automaton | Self-implemented, port of Java's `AhoCorasickMatcher` (~200 lines) | Zero runtime deps; full control over longest-match semantics and codepoint positions; auditable |
| Build tool | tsup (esbuild under the hood) | Native dual ESM+CJS output + `.d.ts` with zero config |
| Test runner | Vitest | ESM-native, fast, built-in happy-dom env for browser subset |
| Package structure | Approach A — thin adapter layer | Core is 100% pure (no I/O); data loaders are ~5-line wrappers; matches Java SDK's `ZhtwData` / `ZhtwConverter` split |

---

## 3. Package Layout

```
sdk/typescript/
├── package.json              # dual ESM+CJS, exports conditional map
├── tsup.config.ts            # two builds: index.node + index.browser
├── tsconfig.json             # strict, target ES2022
├── vitest.config.ts          # Node env default; one subset runs under happy-dom
├── README.md                 # npm-facing usage docs
├── zhtw-data.json            # symlink → ../data/zhtw-data.json (single source of truth)
├── src/
│   ├── core/
│   │   ├── types.ts          # Match, ConversionDetail, LookupResult, ZhtwData, Converter, ConverterOptions
│   │   ├── codepoint.ts      # UTF-16 ↔ codepoint index utilities
│   │   ├── matcher.ts        # AhoCorasickMatcher class (port of Java)
│   │   └── converter.ts      # createConverter(data, options) pure factory
│   ├── data/
│   │   ├── node.ts           # loadData() using fs.readFileSync
│   │   └── browser.ts        # loadData() using `import data from '../../zhtw-data.json'`
│   ├── index.node.ts         # Node entry: wires core + node loader, exports public API
│   └── index.browser.ts      # Browser entry: same exports, browser loader
└── tests/
    ├── matcher.test.ts       # AC automaton unit tests
    ├── codepoint.test.ts     # UTF-16 ↔ codepoint boundary tests
    ├── converter.test.ts     # Two-layer pipeline tests
    ├── golden.test.ts        # Parametrized cross-SDK parity test (reads sdk/data/golden-test.json)
    └── api.test.ts           # Public API smoke tests
```

The `zhtw-data.json` entry at the package root is a symlink so `make bump` keeps it in sync automatically without special-casing TypeScript.

---

## 4. Public API

### Zero-config convenience

```ts
import { convert, check, lookup } from 'zhtw-js';

convert('这个软件需要优化');       // => '這個軟體需要最佳化'
check('用户权限');                  // => Match[]
lookup('软件');                     // => LookupResult
```

The convenience functions wrap a module-level lazy-initialized default converter with `sources: ['cn', 'hk']` and no custom dict.

### Advanced factory

```ts
import { createConverter } from 'zhtw-js';

const conv = createConverter({
  sources: ['cn'],                     // default: ['cn', 'hk']
  customDict: { '自定义': '自訂' },    // takes priority over built-in terms
});

conv.convert('...');
conv.check('...');
conv.lookup('...');
```

### Type surface

```ts
export interface Match {
  start: number;      // codepoint index, inclusive
  end: number;        // codepoint index, exclusive
  source: string;     // original text matched
  target: string;     // replacement (post-charmap)
}

export interface ConversionDetail {
  source: string;
  target: string;
  layer: 'term' | 'char';
  position: number;   // codepoint index
}

export interface LookupResult {
  input: string;
  output: string;
  changed: boolean;
  details: ConversionDetail[];
}

export interface ConverterOptions {
  sources?: Array<'cn' | 'hk'>;        // default: ['cn', 'hk']
  customDict?: Record<string, string>;
}

export interface Converter {
  convert(text: string): string;
  check(text: string): Match[];
  lookup(word: string): LookupResult;
}
```

**Position semantics:** All `start`/`end`/`position` values are **Unicode codepoint indices**, not JavaScript's native UTF-16 code unit indices. This matches Python and Java and keeps cross-SDK output identical for supplementary plane characters (e.g., CJK Extension B+).

---

## 5. Data Flow

```
Consumer imports 'zhtw-js'
    ↓
package.json "exports" conditional resolution:
    Node    → dist/index.node.{mjs|cjs}
    Browser → dist/index.browser.{mjs|cjs}
    ↓
First call to convert/check/lookup triggers lazy init:
    defaultConverter ??= createConverter(loadData(), { sources: ['cn', 'hk'] })
    ↓
loadData():
    Node    → fs.readFileSync(join(__dirname, 'zhtw-data.json'))
    Browser → bundler has inlined the JSON at build time via `import data from '...'`
    ↓
createConverter(data, opts) returns { convert, check, lookup } closures
    ↓
convert(text):
    1. Term layer: matcher.replaceAll(text)  — AC longest-match
    2. Char layer (if 'cn' in sources): applyCharmap(result)
    3. Return converted string

check(text):
    1. Term matches: matcher.findMatches(text)
       → convert UTF-16 positions to codepoint positions
    2. Char matches (if 'cn' in sources): scan codepoints, record differing charmap entries
    3. Return combined Match[]

lookup(word):
    1. Run term layer, track UTF-16 positions covered by term matches
    2. Run char layer on uncovered codepoints only
    3. Sort details by UTF-16 position, rebuild output string
    4. Convert positions to codepoint indices for the public result
    5. Return LookupResult
```

The `lookup` algorithm intentionally mirrors Java's `ZhtwConverter.lookup()` to guarantee identical output.

---

## 6. Components

### `core/types.ts`

Pure TypeScript interfaces and type aliases. No runtime code. Exported to consumers.

### `core/codepoint.ts`

Small helpers for UTF-16 ↔ codepoint index conversion. JavaScript strings are UTF-16, so a string like `"𠮷"` has `length === 2` but represents 1 codepoint. All public APIs must expose codepoint indices for cross-SDK parity.

Functions:
- `codepointLength(s: string): number` — count codepoints via iteration
- `utf16ToCodepoint(text: string, utf16Index: number): number` — convert a UTF-16 offset to codepoint offset
- `codepointAt(text: string, cpIndex: number): { char: string; utf16Index: number }` — walk to the nth codepoint

Tests cover ASCII, BMP CJK, supplementary plane, and empty strings.

### `core/matcher.ts`

`AhoCorasickMatcher` class, direct port of Java's `AhoCorasickMatcher.java`:

```ts
export class AhoCorasickMatcher {
  constructor(patterns: Record<string, string>);
  replaceAll(text: string): string;
  findMatches(text: string): Match[];  // UTF-16 positions; caller converts to codepoint
}
```

Internal data structures:
- Goto trie (children map per node)
- Failure links (BFS-built)
- Output links (pattern terminals)
- Longest-match semantics: on a match, record it, then resume from the position **after** the match (not after one char)

The Java implementation is 167 lines; the TS port should land within ±20% of that.

### `core/converter.ts`

Pure factory, no I/O:

```ts
export function createConverter(data: ZhtwData, options: ConverterOptions = {}): Converter;
```

Internal responsibilities:
1. Validate `options.sources` (throw on unknown source)
2. Merge terms from requested sources + customDict
3. Build `AhoCorasickMatcher`
4. Build codepoint→replacement `Map` from `data.charmap.chars`
5. Compute `charLayerEnabled = sources.includes('cn')`
6. Return `{ convert, check, lookup }` closures sharing the above state

### `data/node.ts`

```ts
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import type { ZhtwData } from '../core/types';

const HERE = typeof __dirname !== 'undefined'
  ? __dirname
  : dirname(fileURLToPath(import.meta.url));
const DATA_PATH = join(HERE, 'zhtw-data.json');

export function loadData(): ZhtwData {
  return JSON.parse(readFileSync(DATA_PATH, 'utf-8')) as ZhtwData;
}
```

The file will live next to `dist/index.node.{mjs,cjs}` in the published tarball. tsup's `publicDir` or a post-build copy step handles placement.

### `data/browser.ts`

```ts
import data from '../../zhtw-data.json';
import type { ZhtwData } from '../core/types';

export function loadData(): ZhtwData {
  return data as unknown as ZhtwData;
}
```

tsup resolves the JSON import at build time and inlines it into `dist/index.browser.{mjs,cjs}`.

### `index.node.ts` / `index.browser.ts`

Thin wrappers. Each is ~30 lines:

```ts
import { loadData } from './data/node'; // or './data/browser'
import { createConverter as createCoreConverter } from './core/converter';
import type {
  Converter, ConverterOptions, Match, LookupResult, ConversionDetail, ZhtwData,
} from './core/types';

// Cache the parsed data at module level so default converter and custom
// converters share the same in-memory copy (avoids re-parsing 1MB JSON).
let cachedData: ZhtwData | null = null;
let defaultConverter: Converter | null = null;

function getData(): ZhtwData {
  if (!cachedData) {
    cachedData = loadData();
  }
  return cachedData;
}

function getDefault(): Converter {
  if (!defaultConverter) {
    defaultConverter = createCoreConverter(getData());
  }
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

export type { Converter, ConverterOptions, Match, LookupResult, ConversionDetail };
```

Note: `cachedData` is shared between the default converter and any custom converter built via `createConverter`. The data is immutable after load, so sharing is safe and avoids re-parsing the 1MB JSON for every factory call.

---

## 7. Error Handling

The rule is: validate only at system boundaries (consumer input + JSON parsing). No defensive checks for internal invariants.

| Situation | Behavior |
|---|---|
| `convert(null)` / `convert(undefined)` | Return empty string (matches Java's null-safe convert) |
| `convert('')` | Return empty string |
| `check(null)` / `lookup(null)` | Return `[]` / `{ input: '', output: '', changed: false, details: [] }` |
| `loadData()` JSON parse / read failure | Throw `Error('Failed to load zhtw-data.json: <reason>')` at first `convert`/`check`/`lookup`/`createConverter` call (lazy init). Propagate loudly; this is a package bug, not user error |
| `createConverter({ sources: ['xx'] })` | Throw `Error("Unknown source: 'xx', expected 'cn' or 'hk'")` |
| `customDict: { '': 'foo' }` | Silently skip empty-key entries (matches Python) |
| `customDict` collides with built-in term | customDict wins (matches Java builder semantics) |

No silent fallbacks. No "best effort" degradation. If the package data is corrupt, the consumer should find out at import time, not when their output is mysteriously wrong.

---

## 8. Testing

### Test inventory

| File | Scope | Env |
|---|---|---|
| `matcher.test.ts` | AC unit: basic match, longest match, overlapping patterns, supplementary plane, customDict merge/override, `replaceAll` return identity when nothing matches | Node |
| `codepoint.test.ts` | UTF-16 ↔ codepoint: ASCII, BMP CJK, supplementary plane (CJK Extension B+, emoji), empty strings | Node |
| `converter.test.ts` | Two-layer pipeline: term-only, char-only, combined, `sources: ['cn']` vs `['cn','hk']`, empty input, null input, customDict precedence | Node |
| `golden.test.ts` | Parametrized: reads `sdk/data/golden-test.json`, asserts `convert(input) === expected` for every entry | Node |
| `api.test.ts` | Public API smoke: zero-config functions, `createConverter`, type exports resolve | Node + happy-dom |

### The golden gate

`golden.test.ts` is the cross-SDK consistency contract. The same JSON file is already consumed by Python and Java tests. If the TS SDK ever produces a single byte of divergence, this test fails loudly. **This is the non-negotiable gate before release.**

### CI matrix

`.github/workflows/sdk-typescript.yml` will run:
- Node 18, 20, 22 (matrix)
- Steps: `pnpm install` → `pnpm test` → `pnpm build` → verify `dist/` contains both entry points
- On `release: published`: `pnpm publish --provenance` with `NPM_TOKEN` secret

### Browser env test

The `api.test.ts` file has a `// @vitest-environment happy-dom` pragma for at least one test. This proves `dist/index.browser.*` is actually usable with no `fs` / `path` / `node:*` imports leaking in.

---

## 9. Distribution

### package.json essentials

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
  "files": ["dist", "zhtw-data.json", "README.md", "LICENSE"],
  "engines": { "node": ">=18" },
  "repository": {
    "type": "git",
    "url": "https://github.com/rajatim/zhtw.git",
    "directory": "sdk/typescript"
  },
  "license": "MIT",
  "scripts": {
    "build": "tsup",
    "test": "vitest run",
    "test:watch": "vitest"
  }
}
```

### Mono-versioning integration

The version in `sdk/typescript/package.json` is already covered by `make bump` and `make version-check`. No changes to the Makefile needed.

### npm publish

One-time setup: create `NPM_TOKEN` (automation token) at npmjs.com, add to repo secrets as `NPM_TOKEN`. After that every `release: published` event triggers `pnpm publish --provenance` automatically.

---

## 10. Explicit Non-Goals (YAGNI)

The following are **deliberately excluded from v1**:

- **Streaming API** (`convertStream`) — wait for real demand
- **Worker thread support** — text transforms rarely benefit; add if profiling shows a need
- **UMD / `<script>` global bundle** — consumers can bundle themselves
- **Dependency-injected data source** (Approach C) — no demand yet; factory API can be extended later without breaking compat
- **JMH-level benchmark suite** — nice-to-have but separate project
- **Performance tuning** — measure first; the AC automaton port alone should be serviceable
- **`.d.cts` separate declarations** — tsup generates both from the same source; one declaration file per entry is sufficient

If any of these come up in real usage, they can be added in a minor release without breaking the v1 API.

---

## 11. Acceptance Criteria

Before cutting a release:

1. ✅ `make version-check` passes with TS at 4.0.0 (already true)
2. ✅ `pnpm test` in `sdk/typescript/` passes on Node 18, 20, 22
3. ✅ `golden.test.ts` passes zero-divergence against `sdk/data/golden-test.json`
4. ✅ `pnpm build` produces `dist/index.{node,browser}.{mjs,cjs,d.ts}`
5. ✅ `api.test.ts` happy-dom case passes (browser entry is genuinely browser-safe)
6. ✅ CI workflow `sdk-typescript.yml` is green
7. ✅ README.md has Install + Quick Start + API reference
8. ✅ Root README's "Multi-language SDKs" table is updated: TypeScript status → ✅ Stable, add throughput number once measured

---

## 12. Open Questions for Implementation

None blocking. All design decisions are locked. The implementation plan (next step) will break the above into bite-sized TDD tasks.
