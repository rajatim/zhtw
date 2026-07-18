import type { ZhtwData } from '../core/types';

const isRecord = (value: unknown): value is Record<string, unknown> =>
  typeof value === 'object' && value !== null && !Array.isArray(value);

const oneCodepoint = (value: string): boolean => Array.from(value).length === 1;

function requireOnlyKeys(value: Record<string, unknown>, allowed: string[], name: string): void {
  for (const key of Object.keys(value)) {
    if (!allowed.includes(key)) throw new Error(`${name} contains unsupported field: ${key}`);
  }
}

function requireStringMap(value: unknown, name: string, singleCodepoint: boolean): void {
  if (!isRecord(value)) throw new Error(`${name} must be an object`);
  for (const [key, target] of Object.entries(value)) {
    if (typeof target !== 'string' || key.length === 0 || target.length === 0) {
      throw new Error(`${name} entries must be non-empty strings`);
    }
    if (singleCodepoint && (!oneCodepoint(key) || !oneCodepoint(target))) {
      throw new Error(`${name} entries must contain exactly one Unicode code point`);
    }
  }
}

export function validateData(value: unknown): ZhtwData {
  if (!isRecord(value)) throw new Error('root must be an object');
  requireOnlyKeys(value, ['schema_version', 'version', 'stats', 'charmap', 'terms'], 'root');
  if (value.schema_version !== 1) {
    throw new Error(`unsupported schema_version: ${String(value.schema_version)}`);
  }
  if (typeof value.version !== 'string' || value.version.length === 0) {
    throw new Error('version must be a non-empty string');
  }
  if (!isRecord(value.charmap)) throw new Error('charmap must be an object');
  requireOnlyKeys(
    value.charmap,
    ['chars', 'ambiguous', 'balanced_defaults', 'balanced_protect_terms'],
    'charmap',
  );
  requireStringMap(value.charmap.chars, 'charmap.chars', true);
  requireStringMap(value.charmap.balanced_defaults, 'charmap.balanced_defaults', true);
  if (!Array.isArray(value.charmap.ambiguous) ||
      value.charmap.ambiguous.some((item) => typeof item !== 'string' || !oneCodepoint(item))) {
    throw new Error('charmap.ambiguous must contain single Unicode code points');
  }
  if (!isRecord(value.terms)) throw new Error('terms must be an object');
  for (const [source, terms] of Object.entries(value.terms)) {
    if (source !== 'cn' && source !== 'hk') throw new Error(`unsupported term source: ${source}`);
    requireStringMap(terms, `terms.${source}`, false);
  }
  return value as unknown as ZhtwData;
}
