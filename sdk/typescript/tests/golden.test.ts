import { describe, it, expect } from 'vitest';
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { createConverter } from '../src/core/converter';
import { JsonAdapterError } from '../src/core/json-adapter';
import type {
  AmbiguityMode,
  ExplainEvent,
  Source,
  ZhtwData,
} from '../src/core/types';

// Load the real data file and golden fixtures from sdk/data/.
const DATA_FILE = resolve(__dirname, '../../data/zhtw-data.json');
const GOLDEN_FILE = resolve(__dirname, '../../data/golden-test.json');
const CONFORMANCE_FILE = resolve(__dirname, '../../data/conformance-v1.json');
const JSON_ADAPTER_FILE = resolve(__dirname, '../../data/json-adapter-golden.json');

const data = JSON.parse(readFileSync(DATA_FILE, 'utf-8')) as ZhtwData;

interface GoldenConvertCase {
  input: string;
  sources: Source[];
  expected: string;
  ambiguity_mode?: string;
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
  ambiguity_mode?: string;
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
  ambiguity_mode?: string;
}

interface GoldenFile {
  version: string;
  convert: GoldenConvertCase[];
  check: GoldenCheckCase[];
  lookup: GoldenLookupCase[];
  explain: Array<{
    input: string;
    sources: Source[];
    expected_output: string;
    expected_events: ExplainEvent[];
    ambiguity_mode?: string;
  }>;
}

interface JsonAdapterGolden {
  version: string;
  cases: Array<{
    id: string;
    input: string;
    sources: Source[];
    expected: string;
    ambiguity_mode?: string;
  }>;
  reject: Array<{ id: string; input: string; error_code: string }>;
}

const golden = JSON.parse(readFileSync(GOLDEN_FILE, 'utf-8')) as GoldenFile;
const conformance = JSON.parse(readFileSync(CONFORMANCE_FILE, 'utf-8')) as {
  schema_version: number;
  convert: Array<GoldenConvertCase & { id: string }>;
};
const jsonAdapter = JSON.parse(
  readFileSync(JSON_ADAPTER_FILE, 'utf-8'),
) as JsonAdapterGolden;

const packageVersion = (JSON.parse(
  readFileSync(resolve(__dirname, '../package.json'), 'utf-8'),
) as { version: string }).version;

describe('embedded version contract', () => {
  it('matches the npm package and golden fixture', () => {
    expect(data.version).toBe(packageVersion);
    expect(golden.version).toBe(packageVersion);
    expect(jsonAdapter.version).toBe(packageVersion);
  });
});

describe('conformance-v1.json — independently approved cases', () => {
  expect(conformance.schema_version).toBe(1);
  for (const tc of conformance.convert) {
    it(tc.id, () => {
      const conv = createConverter(data, { sources: tc.sources });
      expect(conv.convert(tc.input)).toBe(tc.expected);
    });
  }
});

describe('golden-test.json — convert parity', () => {
  for (const tc of golden.convert) {
    it(`convert(${JSON.stringify(tc.input)}, ${JSON.stringify(tc.sources)})`, () => {
      const conv = createConverter(data, {
        sources: tc.sources,
        ambiguityMode: (tc.ambiguity_mode as AmbiguityMode) ?? 'strict',
      });
      expect(conv.convert(tc.input)).toBe(tc.expected);
    });
  }
});

describe('golden-test.json — check parity', () => {
  for (const tc of golden.check) {
    it(`check(${JSON.stringify(tc.input)}, ${JSON.stringify(tc.sources)})`, () => {
      const conv = createConverter(data, {
        sources: tc.sources,
        ambiguityMode: (tc.ambiguity_mode as AmbiguityMode) ?? 'strict',
      });
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
      const conv = createConverter(data, {
        sources: tc.sources,
        ambiguityMode: (tc.ambiguity_mode as AmbiguityMode) ?? 'strict',
      });
      const r = conv.lookup(tc.input);
      expect(r.output).toBe(tc.expected_output);
      expect(r.changed).toBe(tc.expected_changed);
      expect(r.details).toEqual(tc.expected_details);
    });
  }
});

describe('golden-test.json — explain parity', () => {
  for (const tc of golden.explain) {
    it(`explain(${JSON.stringify(tc.input)}, ${JSON.stringify(tc.sources)})`, () => {
      const conv = createConverter(data, {
        sources: tc.sources,
        ambiguityMode: (tc.ambiguity_mode as AmbiguityMode) ?? 'strict',
      });
      const result = conv.explain(tc.input);
      expect(result.output).toBe(tc.expected_output);
      expect(result.output).toBe(conv.convert(tc.input));
      expect(result.events).toEqual(tc.expected_events);
    });
  }
});

describe('json-adapter-golden.json — value-only parity', () => {
  for (const tc of jsonAdapter.cases) {
    it(tc.id, () => {
      const conv = createConverter(data, {
        sources: tc.sources,
        ambiguityMode: (tc.ambiguity_mode as AmbiguityMode) ?? 'strict',
      });
      expect(conv.convertJson(tc.input)).toBe(tc.expected);
    });
  }
  for (const tc of jsonAdapter.reject) {
    it(`rejects ${tc.id}`, () => {
      try {
        createConverter(data, { sources: ['cn'] }).convertJson(tc.input);
        throw new Error('expected JSON adapter failure');
      } catch (error) {
        expect(error).toBeInstanceOf(JsonAdapterError);
        expect((error as JsonAdapterError).code).toBe(tc.error_code);
      }
    });
  }
});
