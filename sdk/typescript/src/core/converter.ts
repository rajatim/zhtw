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

/**
 * Apply charmap to a text segment, skipping positions covered by term hits.
 * @param segment - text segment to map
 * @param charmap - single-codepoint charmap
 * @param covered - set of covered UTF-16 positions in the ORIGINAL text
 * @param offset - UTF-16 offset of this segment within the original text
 */
function applyCharmapSkipping(
  segment: string,
  charmap: Record<string, string>,
  covered: Set<number>,
  offset: number,
): string {
  let out = '';
  let i = 0;
  while (i < segment.length) {
    const code = segment.charCodeAt(i);
    const isHigh = code >= 0xd800 && code <= 0xdbff && i + 1 < segment.length;
    const step = isHigh ? 2 : 1;
    const ch = segment.substring(i, i + step);
    if (covered.has(offset + i)) {
      out += ch;
    } else {
      const mapped = charmap[ch];
      out += mapped !== undefined && mapped !== ch ? mapped : ch;
    }
    i += step;
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

    // Covered positions from ALL automaton hits (including identity terms).
    const covered = matcher.getCoveredPositions(text);
    const matches = matcher.findMatches(text);

    if (matches.length === 0) {
      return charLayerEnabled ? applyCharmapSkipping(text, charmap, covered, 0) : text;
    }

    // Gap mode: term targets inserted verbatim; gaps get char-layer on uncovered only.
    let result = '';
    let lastEnd = 0;
    for (const m of matches) {
      const gap = text.substring(lastEnd, m.start);
      result += charLayerEnabled ? applyCharmapSkipping(gap, charmap, covered, lastEnd) : gap;
      result += m.target;
      lastEnd = m.end;
    }
    const tail = text.substring(lastEnd);
    result += charLayerEnabled ? applyCharmapSkipping(tail, charmap, covered, lastEnd) : tail;
    return result;
  }

  function check(text: string): Match[] {
    requireString(text, 'check');
    if (text.length === 0) return [];

    const results: Match[] = [];

    // Covered positions from ALL automaton hits (including identity terms)
    const coveredUtf16 = matcher.getCoveredPositions(text);

    // Term layer
    for (const m of matcher.findMatches(text)) {
      results.push({
        start: utf16ToCodepoint(text, m.start),
        end: utf16ToCodepoint(text, m.end),
        source: m.source,
        target: m.target,
      });
    }

    // Char layer: skip covered positions
    if (charLayerEnabled) {
      let cp = 0;
      let i = 0;
      while (i < text.length) {
        const code = text.charCodeAt(i);
        const isHigh = code >= 0xd800 && code <= 0xdbff && i + 1 < text.length;
        const step = isHigh ? 2 : 1;
        if (!coveredUtf16.has(i)) {
          const ch = text.substring(i, i + step);
          const mapped = charmap[ch];
          if (mapped !== undefined && mapped !== ch) {
            results.push({ start: cp, end: cp + 1, source: ch, target: mapped });
          }
        }
        cp++;
        i += step;
      }
    }
    return results;
  }

  function lookup(word: string): LookupResult {
    requireString(word, 'lookup');
    if (word.length === 0) {
      return { input: '', output: '', changed: false, details: [] };
    }

    // Internal type used only for sorting by UTF-16 position before we
    // build the output and convert to codepoint indices.
    interface InternalDetail {
      source: string;
      target: string;
      layer: 'term' | 'char';
      utf16Start: number;
      utf16End: number;
    }

    const internal: InternalDetail[] = [];
    // Covered positions from ALL automaton hits (including identity terms)
    const covered = matcher.getCoveredPositions(word);

    // Term layer. Term targets are stored verbatim (matching Python
    // `src/zhtw/lookup.py:49-57`). The charmap does NOT post-process term
    // targets — this keeps lookup().output aligned with convert().
    for (const m of matcher.findMatches(word)) {
      internal.push({
        source: m.source,
        target: m.target,
        layer: 'term',
        utf16Start: m.start,
        utf16End: m.end,
      });
    }

    // Char layer (only if 'cn' is in sources). Skip covered codepoints.
    if (charLayerEnabled) {
      let i = 0;
      while (i < word.length) {
        const code = word.charCodeAt(i);
        const isHigh = code >= 0xd800 && code <= 0xdbff && i + 1 < word.length;
        const step = isHigh ? 2 : 1;
        if (!covered.has(i)) {
          const ch = word.substring(i, i + step);
          const mapped = charmap[ch];
          if (mapped !== undefined && mapped !== ch) {
            internal.push({
              source: ch,
              target: mapped,
              layer: 'char',
              utf16Start: i,
              utf16End: i + step,
            });
          }
        }
        i += step;
      }
    }

    // Sort by UTF-16 start position.
    internal.sort((a, b) => a.utf16Start - b.utf16Start);

    // Build output string by walking details with a UTF-16 cursor.
    let output = '';
    let cursor = 0;
    for (const d of internal) {
      if (d.utf16Start > cursor) output += word.substring(cursor, d.utf16Start);
      output += d.target;
      cursor = d.utf16End;
    }
    if (cursor < word.length) output += word.substring(cursor);

    // Convert UTF-16 positions to codepoint indices for the public result.
    const details = internal.map((d) => ({
      source: d.source,
      target: d.target,
      layer: d.layer,
      position: utf16ToCodepoint(word, d.utf16Start),
    }));

    return {
      input: word,
      output,
      changed: output !== word,
      details,
    };
  }

  function free(): void {
    // No-op: JS objects are garbage-collected. Provided for WASM API parity.
  }

  return { convert, check, lookup, free };
}

// Re-export so callers can import utilities if needed (internal helpers stay private).
export { utf16ToCodepoint };
export type { Utf16Match };
