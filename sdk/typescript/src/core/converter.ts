import {
  AhoCorasickMatcher,
  type Utf16Match,
  type Utf16MatchScan,
} from './matcher';
import type {
  Converter,
  ConverterOptions,
  ExplainEvent,
  ExplainLayer,
  ExplainReasonCode,
  ExplainResult,
  Match,
  LookupResult,
  Source,
  ZhtwData,
} from './types';
import { utf16ToCodepoint } from './codepoint';
import { convertJsonValues } from './json-adapter';
import { sha256Hex } from './sha256';

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
 * Apply balanced defaults and charmap to a text segment, skipping covered positions.
 * Balanced defaults are checked first (matching Python order). Since balanced_defaults
 * chars are not in charmap, the two lookups never overlap.
 * @param segment - text segment to map
 * @param charmap - single-codepoint charmap
 * @param balancedDefaults - balanced mode defaults (or undefined for strict mode)
 * @param covered - set of covered UTF-16 positions in the ORIGINAL text
 * @param offset - UTF-16 offset of this segment within the original text
 */
function applyLayersSkipping(
  segment: string,
  charmap: Record<string, string>,
  balancedDefaults: Record<string, string> | undefined,
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
      // Balanced defaults first, then charmap.
      let result = ch;
      if (balancedDefaults !== undefined) {
        const bd = balancedDefaults[ch];
        if (bd !== undefined) result = bd;
      }
      const mapped = charmap[result];
      if (mapped !== undefined && mapped !== result) result = mapped;
      out += result;
    }
    i += step;
  }
  return out;
}

interface RuleMeta {
  id: string;
  source: string;
  target: string;
}

function legacyCustomRuleId(source: string, target: string): string {
  const canonical = JSON.stringify({
    rule_class: 'custom',
    source,
    source_locale: 'cn',
    target,
  });
  return `legacy:cn:custom:${sha256Hex(canonical).slice(0, 24)}`;
}

function collectRuleMetadata(
  data: ZhtwData,
  sources: readonly Source[],
  customDict: Record<string, string> | undefined,
): Map<string, RuleMeta[]> {
  const records = new Map<string, RuleMeta[]>();
  for (const group of data.rule_catalog?.groups ?? []) {
    if (!sources.includes(group.source_locale)) continue;
    for (const [id, [source, target]] of Object.entries(group.rules)) {
      const current = records.get(source) ?? [];
      current.push({ id, source, target });
      records.set(source, current);
    }
  }
  for (const [source, target] of Object.entries(customDict ?? {})) {
    if (source.length === 0) continue;
    const current = records.get(source) ?? [];
    current.push({ id: legacyCustomRuleId(source, target), source, target });
    records.set(source, current);
  }
  return records;
}

interface CharacterChange {
  position: number;
  step: number;
  source: string;
  target: string;
  layer: Extract<ExplainLayer, 'balanced' | 'char'>;
  ruleId: string;
  reasonCode: Extract<ExplainReasonCode, 'balanced_default' | 'char_map'>;
}

const codepointLength = (value: string): number => Array.from(value).length;

function compareText(a: string, b: string): number {
  return a < b ? -1 : a > b ? 1 : 0;
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
  // balanced defaults are CN→TW mappings; degrade to strict when CN not in sources.
  const balancedDefaults =
    options.ambiguityMode === 'balanced' && charLayerEnabled
      ? data.charmap.balanced_defaults
      : undefined;
  const layersEnabled = charLayerEnabled || balancedDefaults !== undefined;
  const ruleRecords = collectRuleMetadata(data, sources, options.customDict);

  function convertWithScan(text: string, scan: Pick<Utf16MatchScan, 'matches' | 'covered'>): string {
    const { covered, matches } = scan;

    if (matches.length === 0) {
      return layersEnabled
        ? applyLayersSkipping(text, charmap, balancedDefaults, covered, 0)
        : text;
    }

    let result = '';
    let lastEnd = 0;
    for (const m of matches) {
      const gap = text.substring(lastEnd, m.start);
      result += layersEnabled
        ? applyLayersSkipping(gap, charmap, balancedDefaults, covered, lastEnd)
        : gap;
      result += m.target;
      lastEnd = m.end;
    }
    const tail = text.substring(lastEnd);
    result += layersEnabled
      ? applyLayersSkipping(tail, charmap, balancedDefaults, covered, lastEnd)
      : tail;
    return result;
  }

  function convert(text: string): string {
    requireString(text, 'convert');
    if (text.length === 0) return '';

    // Covered positions from ALL automaton hits (including identity terms).
    return convertWithScan(text, matcher.scan(text));
  }

  function convertJson(text: string): string {
    return convertJsonValues(text, convert);
  }

  function characterChanges(text: string, covered: Set<number>): CharacterChange[] {
    const changes: CharacterChange[] = [];
    for (let position = 0; position < text.length; ) {
      const code = text.charCodeAt(position);
      const step = code >= 0xd800 && code <= 0xdbff && position + 1 < text.length ? 2 : 1;
      const source = text.substring(position, position + step);
      if (!covered.has(position)) {
        const balanced = balancedDefaults?.[source];
        if (balanced !== undefined) {
          const target = charmap[balanced] ?? balanced;
          if (target !== source) {
            changes.push({
              position,
              step,
              source,
              target,
              layer: 'balanced',
              ruleId: `balanced:u${source.codePointAt(0)!.toString(16)}`,
              reasonCode: 'balanced_default',
            });
          }
        } else if (charLayerEnabled) {
          const target = charmap[source];
          if (target !== undefined && target !== source) {
            changes.push({
              position,
              step,
              source,
              target,
              layer: 'char',
              ruleId: `charmap:u${source.codePointAt(0)!.toString(16)}`,
              reasonCode: 'char_map',
            });
          }
        }
      }
      position += step;
    }
    return changes;
  }

  function ruleRecordFor(match: Utf16Match): RuleMeta | undefined {
    const candidates = ruleRecords.get(match.source) ?? [];
    return [...candidates].reverse().find((record) => record.target === match.target);
  }

  function explain(text: string): ExplainResult {
    requireString(text, 'explain');
    if (text.length === 0) return { output: '', events: [] };

    const scan = matcher.scanDetailed(text);
    const changes = characterChanges(text, scan.covered);
    const selectedByStart = new Map(scan.matches.map((match) => [match.start, match]));
    const changesByStart = new Map(changes.map((change) => [change.position, change]));
    const spans: Array<[number, number]> = new Array(text.length);
    let output = '';
    let inputPosition = 0;
    let outputPosition = 0;
    while (inputPosition < text.length) {
      const match = selectedByStart.get(inputPosition);
      if (match !== undefined) {
        const outputEnd = outputPosition + codepointLength(match.target);
        for (let i = match.start; i < match.end; i++) spans[i] = [outputPosition, outputEnd];
        output += match.target;
        outputPosition = outputEnd;
        inputPosition = match.end;
        continue;
      }
      const code = text.charCodeAt(inputPosition);
      const step = code >= 0xd800 && code <= 0xdbff && inputPosition + 1 < text.length ? 2 : 1;
      const source = text.substring(inputPosition, inputPosition + step);
      const target = changesByStart.get(inputPosition)?.target ?? source;
      const outputEnd = outputPosition + codepointLength(target);
      for (let i = inputPosition; i < inputPosition + step; i++) {
        spans[i] = [outputPosition, outputEnd];
      }
      output += target;
      outputPosition = outputEnd;
      inputPosition += step;
    }
    if (output !== convertWithScan(text, scan)) {
      throw new Error('zhtw: explain trace diverged from conversion output');
    }

    const events: ExplainEvent[] = [];
    for (const decision of scan.decisions) {
      const match = decision.match;
      const affected = spans.slice(match.start, match.end);
      const outputStart = Math.min(...affected.map(([start]) => start));
      const outputEnd = Math.max(...affected.map(([, end]) => end));
      const winner = ruleRecordFor(match);
      const candidates = ruleRecords.get(match.source) ?? [];
      const conflicts = candidates.filter((record) => record.id !== winner?.id);
      events.push({
        rule_id: winner?.id ?? legacyCustomRuleId(match.source, match.target),
        layer: match.source === match.target ? 'identity' : 'term',
        outcome: decision.outcome,
        input_start: utf16ToCodepoint(text, match.start),
        input_end: utf16ToCodepoint(text, match.end),
        output_start: outputStart,
        output_end: outputEnd,
        source: match.source,
        target: match.target,
        reason_code:
          decision.outcome === 'applied' && conflicts.length > 0
            ? 'loader_conflict_winner'
            : decision.reasonCode,
      });
      if (decision.outcome === 'applied') {
        for (const conflict of conflicts) {
          events.push({
            rule_id: conflict.id,
            layer: 'term',
            outcome: 'skipped',
            input_start: utf16ToCodepoint(text, match.start),
            input_end: utf16ToCodepoint(text, match.end),
            output_start: outputStart,
            output_end: outputEnd,
            source: conflict.source,
            target: conflict.target,
            reason_code: 'loader_conflict_loser',
          });
        }
      }
    }
    for (const change of changes) {
      const [outputStart, outputEnd] = spans[change.position]!;
      events.push({
        rule_id: change.ruleId,
        layer: change.layer,
        outcome: 'applied',
        input_start: utf16ToCodepoint(text, change.position),
        input_end: utf16ToCodepoint(text, change.position + change.step),
        output_start: outputStart,
        output_end: outputEnd,
        source: change.source,
        target: change.target,
        reason_code: change.reasonCode,
      });
    }
    const outcomeOrder = { applied: 0, protected: 1, skipped: 2 } as const;
    events.sort(
      (a, b) =>
        a.input_start - b.input_start ||
        a.input_end - b.input_end ||
        outcomeOrder[a.outcome] - outcomeOrder[b.outcome] ||
        compareText(a.rule_id, b.rule_id),
    );
    return { output, events };
  }

  function check(text: string): Match[] {
    requireString(text, 'check');
    if (text.length === 0) return [];

    const results: Match[] = [];

    // Covered positions from ALL automaton hits (including identity terms)
    const { covered: coveredUtf16, matches: termMatches } = matcher.scan(text);

    // Term layer
    for (const m of termMatches) {
      results.push({
        start: utf16ToCodepoint(text, m.start),
        end: utf16ToCodepoint(text, m.end),
        source: m.source,
        target: m.target,
      });
    }

    // Balanced defaults layer: emit matches at uncovered positions
    if (balancedDefaults !== undefined) {
      let cp = 0;
      let i = 0;
      while (i < text.length) {
        const code = text.charCodeAt(i);
        const isHigh = code >= 0xd800 && code <= 0xdbff && i + 1 < text.length;
        const step = isHigh ? 2 : 1;
        if (!coveredUtf16.has(i)) {
          const ch = text.substring(i, i + step);
          const bd = balancedDefaults[ch];
          if (bd !== undefined) {
            results.push({ start: cp, end: cp + 1, source: ch, target: bd });
          }
        }
        cp++;
        i += step;
      }
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
    const { covered, matches: termMatches } = matcher.scan(word);

    // Term layer. Term targets are stored verbatim (matching Python
    // `src/zhtw/lookup.py:49-57`). The charmap does NOT post-process term
    // targets — this keeps lookup().output aligned with convert().
    for (const m of termMatches) {
      internal.push({
        source: m.source,
        target: m.target,
        layer: 'term',
        utf16Start: m.start,
        utf16End: m.end,
      });
    }

    // Balanced defaults layer: skip covered positions.
    if (balancedDefaults !== undefined) {
      let i = 0;
      while (i < word.length) {
        const code = word.charCodeAt(i);
        const isHigh = code >= 0xd800 && code <= 0xdbff && i + 1 < word.length;
        const step = isHigh ? 2 : 1;
        if (!covered.has(i)) {
          const ch = word.substring(i, i + step);
          const bd = balancedDefaults[ch];
          if (bd !== undefined) {
            internal.push({
              source: ch,
              target: bd,
              layer: 'char',
              utf16Start: i,
              utf16End: i + step,
            });
          }
        }
        i += step;
      }
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

  return { convert, convertJson, check, lookup, explain, free };
}

// Re-export so callers can import utilities if needed (internal helpers stay private).
export { utf16ToCodepoint };
export type { Utf16Match };
