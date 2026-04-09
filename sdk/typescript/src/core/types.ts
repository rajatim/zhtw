export type Source = 'cn' | 'hk';

export interface Match {
  /** Codepoint index, inclusive. */
  start: number;
  /** Codepoint index, exclusive. */
  end: number;
  /** Original text matched. */
  source: string;
  /** Replacement text (post-charmap). */
  target: string;
}

export interface ConversionDetail {
  source: string;
  target: string;
  layer: 'term' | 'char';
  /** Codepoint index of the matched/replaced segment in the input. */
  position: number;
}

export interface LookupResult {
  input: string;
  output: string;
  changed: boolean;
  details: ConversionDetail[];
}

export interface ConverterOptions {
  /** Which source dictionaries to use. Default: ['cn', 'hk']. */
  sources?: Source[];
  /** User overrides, take priority over built-in terms. */
  customDict?: Record<string, string>;
}

export interface Converter {
  convert(text: string): string;
  check(text: string): Match[];
  lookup(word: string): LookupResult;
}

/** Shape of sdk/data/zhtw-data.json. */
export interface ZhtwData {
  version: string;
  charmap: {
    chars: Record<string, string>;
    ambiguous: Record<string, string[]>;
  };
  terms: Record<string, Record<string, string>>;
  stats?: Record<string, unknown>;
}
