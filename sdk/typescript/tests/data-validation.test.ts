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
  it('accepts schema v2 and validates catalog coverage', () => {
    const data = valid();
    const v2 = {
      ...data,
      schema_version: 2,
      stats: { rule_catalog_count: 1 },
      rule_catalog: {
        format: 'grouped-v1',
        groups: [{
          source_locale: 'cn',
          rule_class: 'curated',
          domain: 'it',
          trust_level: 'curated',
          priority: 300,
          context: [],
          evidence_source: 'data/terms/cn/it.json',
          review_status: 'approved',
          rules: { 'legacy:cn:curated:123456789012345678901234': ['软件', '軟體'] },
        }],
      },
      terms: { cn: { '软件': '軟體' } },
    };
    expect(validateData(v2).schema_version).toBe(2);
  });
  it('rejects unknown schema versions', () => {
    const data = valid();
    expect(() => validateData({ ...data, schema_version: 3 })).toThrow(/schema_version/);
  });
  it('rejects multi-codepoint charmap entries', () => {
    const data = valid();
    data.charmap.chars = { '软件': '軟體' };
    expect(() => validateData(data)).toThrow(/one Unicode code point/);
  });
  it('rejects unknown fields', () => {
    expect(() => validateData({ ...valid(), future_field: true })).toThrow(/unsupported field/);
  });
  it('rejects catalog and effective-term disagreement', () => {
    const data = valid();
    expect(() => validateData({
      ...data,
      schema_version: 2,
      stats: { rule_catalog_count: 0 },
      rule_catalog: { format: 'grouped-v1', groups: [] },
    })).toThrow(/does not cover effective term/);
  });
});
