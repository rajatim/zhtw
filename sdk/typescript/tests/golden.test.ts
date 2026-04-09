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
