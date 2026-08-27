# zhtw-wasm

> Traditional Chinese converter for Taiwan — WebAssembly (Rust core)

Simplified Chinese → Taiwan Traditional Chinese converter compiled from Rust to WebAssembly. API-compatible with `zhtw-js`. Zero runtime dependencies. Byte-for-byte parity with Python CLI, Java SDK, and TypeScript SDK.

## Install

```bash
npm install zhtw-wasm
```

## Quick start

<!-- zhtw:disable -->
```ts
import { convert, convertJson, check, lookup, explain } from 'zhtw-wasm';

convert('这个软件需要优化');
// => '這個軟體需要最佳化'

convertJson('{"软件":"这个软件"}');
// => '{"软件":"這個軟體"}'

explain('软件');
// => { output: '軟體', events: [...] }
```
<!-- zhtw:enable -->

## Advanced: custom converter

```ts
import { createConverter } from 'zhtw-wasm';

const conv = createConverter({
  sources: ['cn'],
  customDict: { '自訂': '自訂' },
  ambiguityMode: 'balanced',
});

conv.convert('...');
```

## Cross-SDK parity

Verified against `sdk/data/golden-test.json` and `sdk/data/json-adapter-golden.json`, the shared fixtures consumed by all SDKs. Zero divergence is a release gate.

## License

MIT. Part of [rajatim/zhtw](https://github.com/rajatim/zhtw).
