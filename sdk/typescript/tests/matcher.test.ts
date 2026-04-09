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
