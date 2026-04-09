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
