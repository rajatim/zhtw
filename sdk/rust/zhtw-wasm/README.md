# zhtw-wasm

> Traditional Chinese converter for Taiwan — WebAssembly (Rust core)

Simplified Chinese → Taiwan Traditional Chinese converter compiled from Rust to WebAssembly. API-compatible with `zhtw-js`. Zero runtime dependencies. Byte-for-byte parity with Python CLI, Java SDK, and TypeScript SDK.

## Install

```bash
npm install zhtw-wasm
```

## Quick start

```ts
import { convert, check, lookup } from 'zhtw-wasm';

convert('這個軟體需要最佳化');
// => '這個軟體需要最佳化'
```

## Advanced: custom converter

```ts
import { createConverter } from 'zhtw-wasm';

const conv = createConverter({
  sources: ['cn'],
  customDict: { '自訂': '自訂' },
});

conv.convert('...');
```

## Cross-SDK parity

Verified against `sdk/data/golden-test.json`, the shared fixture consumed by all SDKs. Zero divergence is a release gate.

## License

MIT. Part of [rajatim/zhtw](https://github.com/rajatim/zhtw).
