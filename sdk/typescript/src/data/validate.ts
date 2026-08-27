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

const RULE_ID = /^[a-z0-9][a-z0-9._:-]{2,127}$/;
const RULE_CLASSES = ['bulk', 'generated_guard', 'curated', 'custom'];
const TRUST_LEVELS = ['imported', 'generated', 'curated', 'custom'];
const REVIEW_STATUSES = ['pending', 'approved', 'rejected'];
const RULE_DOMAINS = [
  'general', 'business', 'daily', 'ecommerce', 'education', 'finance', 'formal',
  'gaming', 'geography', 'it', 'legal', 'medical', 'social', 'ui',
];

function validateRuleCatalog(
  value: unknown,
  terms: Record<string, unknown>,
  expectedCount: unknown,
): void {
  if (!isRecord(value)) throw new Error('rule_catalog must be an object');
  requireOnlyKeys(value, ['format', 'groups'], 'rule_catalog');
  if (value.format !== 'grouped-v1' || !Array.isArray(value.groups)) {
    throw new Error('rule_catalog must use grouped-v1');
  }

  const ids = new Set<string>();
  const approved = new Set<string>();
  let count = 0;
  for (const [index, item] of value.groups.entries()) {
    if (!isRecord(item)) throw new Error(`rule_catalog.groups[${index}] must be an object`);
    requireOnlyKeys(
      item,
      [
        'source_locale',
        'rule_class',
        'domain',
        'trust_level',
        'priority',
        'context',
        'evidence_source',
        'review_status',
        'rules',
      ],
      `rule_catalog.groups[${index}]`,
    );
    if (item.source_locale !== 'cn' && item.source_locale !== 'hk') {
      throw new Error('rule catalog has unsupported source locale');
    }
    if (typeof item.rule_class !== 'string' || !RULE_CLASSES.includes(item.rule_class)) {
      throw new Error('rule catalog has unsupported rule class');
    }
    if (typeof item.domain !== 'string' || !RULE_DOMAINS.includes(item.domain)) {
      throw new Error('rule catalog has unsupported domain');
    }
    if (typeof item.trust_level !== 'string' || !TRUST_LEVELS.includes(item.trust_level)) {
      throw new Error('rule catalog has unsupported trust level');
    }
    if (!Number.isInteger(item.priority) || (item.priority as number) < -1000 ||
        (item.priority as number) > 1000) {
      throw new Error('rule catalog priority is invalid');
    }
    if (!Array.isArray(item.context) ||
        item.context.some((entry) => typeof entry !== 'string' || entry.length === 0) ||
        new Set(item.context).size !== item.context.length) {
      throw new Error('rule catalog context is invalid');
    }
    if (item.evidence_source !== null &&
        (typeof item.evidence_source !== 'string' || item.evidence_source.length === 0)) {
      throw new Error('rule catalog evidence source is invalid');
    }
    if (typeof item.review_status !== 'string' ||
        !REVIEW_STATUSES.includes(item.review_status)) {
      throw new Error('rule catalog has unsupported review status');
    }
    if (item.review_status === 'approved' && item.evidence_source === null) {
      throw new Error('approved rule catalog groups require evidence');
    }
    if (!isRecord(item.rules)) throw new Error('rule catalog rules must be an object');
    for (const [id, pair] of Object.entries(item.rules)) {
      if (!RULE_ID.test(id) || ids.has(id)) throw new Error(`duplicate or invalid rule id: ${id}`);
      if (!Array.isArray(pair) || pair.length !== 2 ||
          pair.some((entry) => typeof entry !== 'string' || entry.length === 0)) {
        throw new Error(`rule ${id} must contain source and target strings`);
      }
      ids.add(id);
      count += 1;
      if (item.review_status === 'approved') {
        approved.add(`${item.source_locale}\0${pair[0]}\0${pair[1]}`);
      }
    }
  }
  if (!Number.isInteger(expectedCount) || expectedCount !== count) {
    throw new Error('rule catalog count does not match stats');
  }
  for (const [locale, sourceTerms] of Object.entries(terms)) {
    if (!isRecord(sourceTerms)) continue;
    for (const [source, target] of Object.entries(sourceTerms)) {
      if (!approved.has(`${locale}\0${source}\0${String(target)}`)) {
        throw new Error(`rule catalog does not cover effective term: ${locale}/${source}`);
      }
    }
  }
}

export function validateData(value: unknown): ZhtwData {
  if (!isRecord(value)) throw new Error('root must be an object');
  if (value.schema_version !== 1 && value.schema_version !== 2) {
    throw new Error(`unsupported schema_version: ${String(value.schema_version)}`);
  }
  const rootKeys = ['schema_version', 'version', 'stats', 'charmap', 'terms'];
  if (value.schema_version === 2) rootKeys.push('rule_catalog');
  requireOnlyKeys(value, rootKeys, 'root');
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
  if (value.schema_version === 2) {
    if (!isRecord(value.stats)) throw new Error('stats must be an object');
    validateRuleCatalog(value.rule_catalog, value.terms, value.stats.rule_catalog_count);
  }
  return value as unknown as ZhtwData;
}
