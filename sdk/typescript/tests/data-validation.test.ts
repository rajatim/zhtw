import { describe, expect, it } from 'vitest';
import { validateData } from '../src/data/validate';
import type { ZhtwData } from '../src/core/types';

const valid = (): ZhtwData => ({
  schema_version: 1,
  version: '1.2.3',
  stats: {},
  charmap: {
    chars: { '软': '軟' },
    ambiguous: ['发'],
    balanced_defaults: {},
    balanced_protect_terms: {},
  },
  terms: { cn: { '软件': '軟體' }, hk: {} },
});

describe('SDK data validation', () => {
  it('accepts the supported schema', () => expect(validateData(valid()).version).toBe('1.2.3'));
  it('rejects unknown schema versions', () => {
    const data = valid();
    expect(() => validateData({ ...data, schema_version: 2 })).toThrow(/schema_version/);
  });
  it('rejects multi-codepoint charmap entries', () => {
    const data = valid();
    data.charmap.chars = { '软件': '軟體' };
    expect(() => validateData(data)).toThrow(/one Unicode code point/);
  });
  it('rejects unknown fields', () => {
    expect(() => validateData({ ...valid(), future_field: true })).toThrow(/unsupported field/);
  });
});
