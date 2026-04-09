import { AhoCorasickMatcher, type Utf16Match } from './matcher';
import type {
  Converter,
  ConverterOptions,
  Match,
  LookupResult,
  Source,
  ZhtwData,
} from './types';
import { utf16ToCodepoint } from './codepoint';

const DEFAULT_SOURCES: readonly Source[] = ['cn', 'hk'];
const VALID_SOURCES = new Set<string>(['cn', 'hk']);

function validateOptions(options: ConverterOptions): readonly Source[] {
  if (options.sources === undefined) return DEFAULT_SOURCES;
  if (!Array.isArray(options.sources) || options.sources.length === 0) {
    throw new Error(
      'zhtw: sources must be a non-empty array of "cn" | "hk", or omitted',
    );
  }
  for (const s of options.sources) {
    if (!VALID_SOURCES.has(s)) {
      throw new Error(`zhtw: unknown source '${s}', expected 'cn' or 'hk'`);
    }
  }
  return options.sources;
}

function mergeTerms(
  data: ZhtwData,
  sources: readonly Source[],
  customDict: Record<string, string> | undefined,
): Record<string, string> {
  const merged: Record<string, string> = {};
  for (const src of sources) {
    const bucket = data.terms[src];
    if (!bucket) continue;
    for (const [k, v] of Object.entries(bucket)) {
      if (k.length === 0) continue;
      merged[k] = v;
    }
  }
  if (customDict) {
    for (const [k, v] of Object.entries(customDict)) {
      if (k.length === 0) continue;
      merged[k] = v; // customDict wins
    }
  }
  return merged;
}

function requireString(value: unknown, fnName: string): string {
  if (typeof value !== 'string') {
    throw new TypeError(`zhtw: ${fnName} text must be a string`);
  }
  return value;
}

/**
 * Apply the char layer (single-codepoint charmap) to a string. Returns the
 * transformed string. Walks codepoints so supplementary-plane chars work.
 */
function applyCharmap(text: string, charmap: Record<string, string>): string {
  let out = '';
  for (const ch of text) {
    const mapped = charmap[ch];
    out += mapped !== undefined ? mapped : ch;
  }
  return out;
}

export function createConverter(
  data: ZhtwData,
  options: ConverterOptions = {},
): Converter {
  const sources = validateOptions(options);
  const terms = mergeTerms(data, sources, options.customDict);
  const matcher = new AhoCorasickMatcher(terms);
  const charmap = data.charmap.chars;
  const charLayerEnabled = sources.includes('cn');

  function convert(text: string): string {
    requireString(text, 'convert');
    if (text.length === 0) return '';
    const afterTerms = matcher.replaceAll(text);
    return charLayerEnabled ? applyCharmap(afterTerms, charmap) : afterTerms;
  }

  function check(_text: string): Match[] {
    requireString(_text, 'check');
    throw new Error('check: implemented in Task 7');
  }

  function lookup(_word: string): LookupResult {
    requireString(_word, 'lookup');
    throw new Error('lookup: implemented in Task 8');
  }

  return { convert, check, lookup };
}

// Re-export so callers can import utilities if needed (internal helpers stay private).
export { utf16ToCodepoint };
export type { Utf16Match };
