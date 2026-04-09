# zhtw-js

> Traditional Chinese converter for Taiwan — TypeScript SDK

Simplified Chinese → Taiwan Traditional Chinese converter with zero runtime dependencies. Runs identically in Node.js ≥18 and modern browsers. Byte-for-byte compatible with the Python CLI and Java SDK, verified by a shared golden fixture.

## Install

```bash
npm install zhtw-js
# or
pnpm add zhtw-js
# or
yarn add zhtw-js
```

## Quick start

Zero config — the module exports a ready-to-use default converter:

<!-- zhtw:disable -->
```ts
import { convert, check, lookup } from 'zhtw-js';

convert('这个软件需要优化');
// => '這個軟體需要最佳化'

check('用户权限');
// => [{ start, end, source, target }, ...]

lookup('软件');
// => { input, output, changed, details: [...] }
```
<!-- zhtw:enable -->

## Advanced: custom converter

<!-- zhtw:disable -->
```ts
import { createConverter } from 'zhtw-js';

const conv = createConverter({
  sources: ['cn'],               // default: ['cn', 'hk']
  customDict: {                  // overrides built-in terms
    '自定义': '自訂',
  },
});

conv.convert('...');
conv.check('...');
conv.lookup('...');
```
<!-- zhtw:enable -->

## API reference

```ts
type Source = 'cn' | 'hk';

interface Match {
  start: number;      // codepoint index, inclusive
  end: number;        // codepoint index, exclusive
  source: string;
  target: string;
}

interface ConversionDetail {
  source: string;
  target: string;
  layer: 'term' | 'char';
  position: number;   // codepoint index
}

interface LookupResult {
  input: string;
  output: string;
  changed: boolean;
  details: ConversionDetail[];
}

interface ConverterOptions {
  sources?: Source[];                  // default: ['cn', 'hk']
  customDict?: Record<string, string>;
}

interface Converter {
  convert(text: string): string;
  check(text: string): Match[];
  lookup(word: string): LookupResult;
}
```

All `start` / `end` / `position` fields are **Unicode codepoint indices**, not JavaScript UTF-16 code-unit indices. This keeps cross-SDK output byte-for-byte identical on supplementary-plane characters.

## Cross-SDK parity

Every release is verified against [`sdk/data/golden-test.json`](https://github.com/rajatim/zhtw/blob/main/sdk/data/golden-test.json), the shared fixture file consumed by the Python CLI, Java SDK, and TypeScript SDK. Zero divergence is a release gate.

## License

MIT. See [LICENSE](https://github.com/rajatim/zhtw/blob/main/LICENSE).

Part of the [rajatim/zhtw](https://github.com/rajatim/zhtw) monorepo.
