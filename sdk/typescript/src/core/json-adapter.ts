export class JsonAdapterError extends Error {
  constructor(
    message: string,
    readonly code: 'invalid_json' | 'duplicate_key' | 'invalid_converter_result' | 'structure_changed',
  ) {
    super(message);
    this.name = 'JsonAdapterError';
  }
}

interface StringToken {
  start: number;
  end: number;
  value: string;
}

class JsonScanner {
  private position = 0;
  readonly values: StringToken[] = [];

  constructor(private readonly text: string) {}

  parse(): unknown {
    this.skipWhitespace();
    const value = this.parseValue(true);
    this.skipWhitespace();
    if (this.position !== this.text.length) this.fail('trailing JSON content');
    return value;
  }

  private fail(message: string, code: 'invalid_json' | 'duplicate_key' = 'invalid_json'): never {
    throw new JsonAdapterError(message, code);
  }

  private skipWhitespace(): void {
    while (
      this.position < this.text.length &&
      (this.text[this.position] === ' ' ||
        this.text[this.position] === '\t' ||
        this.text[this.position] === '\r' ||
        this.text[this.position] === '\n')
    ) {
      this.position++;
    }
  }

  private expect(expected: string): void {
    if (!this.text.startsWith(expected, this.position)) this.fail(`expected ${expected}`);
    this.position += expected.length;
  }

  private parseString(collect: boolean): string {
    const start = this.position;
    this.expect('"');
    let escaped = false;
    while (this.position < this.text.length) {
      const character = this.text[this.position++]!;
      if (escaped) escaped = false;
      else if (character === '\\') escaped = true;
      else if (character === '"') {
        const raw = this.text.slice(start, this.position);
        let value: unknown;
        try {
          value = JSON.parse(raw);
        } catch {
          this.fail('invalid JSON string');
        }
        if (typeof value !== 'string') this.fail('invalid JSON string');
        validateUnicodeScalars(value);
        if (collect) this.values.push({ start, end: this.position, value });
        return value;
      }
    }
    this.fail('unterminated JSON string');
  }

  private parseValue(collectString: boolean): unknown {
    this.skipWhitespace();
    const character = this.text[this.position];
    if (character === '"') return this.parseString(collectString);
    if (character === '{') return this.parseObject();
    if (character === '[') return this.parseArray();

    const start = this.position;
    while (
      this.position < this.text.length &&
      !',]} \t\r\n'.includes(this.text[this.position]!)
    ) {
      this.position++;
    }
    if (start === this.position) this.fail('missing JSON value');
    try {
      return JSON.parse(this.text.slice(start, this.position));
    } catch {
      this.fail('invalid JSON primitive');
    }
  }

  private parseObject(): Record<string, unknown> {
    this.expect('{');
    this.skipWhitespace();
    const result = Object.create(null) as Record<string, unknown>;
    const keys = new Set<string>();
    if (this.text[this.position] === '}') {
      this.position++;
      return result;
    }
    while (true) {
      this.skipWhitespace();
      if (this.text[this.position] !== '"') this.fail('JSON object key must be a string');
      const key = this.parseString(false);
      if (keys.has(key)) this.fail('duplicate JSON object key', 'duplicate_key');
      keys.add(key);
      this.skipWhitespace();
      this.expect(':');
      result[key] = this.parseValue(true);
      this.skipWhitespace();
      if (this.text[this.position] === '}') {
        this.position++;
        return result;
      }
      this.expect(',');
    }
  }

  private parseArray(): unknown[] {
    this.expect('[');
    this.skipWhitespace();
    const result: unknown[] = [];
    if (this.text[this.position] === ']') {
      this.position++;
      return result;
    }
    while (true) {
      result.push(this.parseValue(true));
      this.skipWhitespace();
      if (this.text[this.position] === ']') {
        this.position++;
        return result;
      }
      this.expect(',');
    }
  }
}

function validateUnicodeScalars(value: string): void {
  for (let i = 0; i < value.length; i++) {
    const code = value.charCodeAt(i);
    if (code >= 0xd800 && code <= 0xdbff) {
      const next = value.charCodeAt(i + 1);
      if (!(next >= 0xdc00 && next <= 0xdfff)) {
        throw new JsonAdapterError('JSON contains an unpaired Unicode surrogate', 'invalid_json');
      }
      i++;
    } else if (code >= 0xdc00 && code <= 0xdfff) {
      throw new JsonAdapterError('JSON contains an unpaired Unicode surrogate', 'invalid_json');
    }
  }
}

const STRING_VALUE = Symbol('string-value');

function structure(value: unknown): unknown {
  if (typeof value === 'string') return STRING_VALUE.description;
  if (Array.isArray(value)) return ['array', value.map(structure)];
  if (value !== null && typeof value === 'object') {
    return ['object', Object.entries(value).map(([key, item]) => [key, structure(item)])];
  }
  if (typeof value === 'number' && Object.is(value, -0)) return ['number', '-0'];
  return [typeof value, value];
}

export function convertJsonValues(text: string, converter: (value: string) => string): string {
  if (typeof text !== 'string') throw new TypeError('zhtw: convertJson text must be a string');
  const originalScanner = new JsonScanner(text);
  const original = parseScanner(originalScanner);
  const replacements: Array<{ start: number; end: number; value: string }> = [];
  for (const token of originalScanner.values) {
    const target = converter(token.value);
    if (typeof target !== 'string') {
      throw new JsonAdapterError(
        'JSON value converter must return a string',
        'invalid_converter_result',
      );
    }
    if (target !== token.value) {
      replacements.push({ start: token.start, end: token.end, value: JSON.stringify(target) });
    }
  }
  if (replacements.length === 0) return text;

  let output = '';
  let lastEnd = 0;
  for (const replacement of replacements) {
    output += text.slice(lastEnd, replacement.start) + replacement.value;
    lastEnd = replacement.end;
  }
  output += text.slice(lastEnd);

  const converted = parseScanner(new JsonScanner(output));
  if (JSON.stringify(structure(converted)) !== JSON.stringify(structure(original))) {
    throw new JsonAdapterError('converted JSON changed non-value structure', 'structure_changed');
  }
  return output;
}

function parseScanner(scanner: JsonScanner): unknown {
  try {
    return scanner.parse();
  } catch (error) {
    if (error instanceof JsonAdapterError) throw error;
    throw new JsonAdapterError('invalid JSON', 'invalid_json');
  }
}
