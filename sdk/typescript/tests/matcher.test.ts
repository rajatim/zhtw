import { describe, it, expect } from 'vitest';
import { AhoCorasickMatcher } from '../src/core/matcher';

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
