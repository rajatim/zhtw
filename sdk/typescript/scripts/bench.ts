import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createConverter } from '../src/core/converter';
import type { ZhtwData } from '../src/core/types';

// Load data directly from sdk/data/ — we bypass src/data/node.ts's lazy
// loader because that resolves zhtw-data.json relative to its own module,
// which only makes sense after tsup copies the JSON next to the built entry.
const here = dirname(fileURLToPath(import.meta.url));
const dataPath = resolve(here, '../../data/zhtw-data.json');
const data = JSON.parse(readFileSync(dataPath, 'utf-8')) as ZhtwData;
const converter = createConverter(data);

// Build ~100KB of Simplified Chinese by repeating a seed phrase.
const seed = '这个软件需要优化，用户体验才能更好。';
const target = 100_000;
let text = '';
while (Buffer.byteLength(text, 'utf-8') < target) {
  text += seed;
}
const byteLen = Buffer.byteLength(text, 'utf-8');

// Warmup.
for (let i = 0; i < 5; i++) converter.convert(text);

// Measure.
const runs = 100;
const start = performance.now();
for (let i = 0; i < runs; i++) converter.convert(text);
const elapsedMs = performance.now() - start;

const totalBytes = byteLen * runs;
const mbPerSec = totalBytes / 1024 / 1024 / (elapsedMs / 1000);

console.log(`input size: ${(byteLen / 1024).toFixed(1)} KB`);
console.log(`runs: ${runs}`);
console.log(`elapsed: ${elapsedMs.toFixed(1)} ms`);
console.log(`throughput: ${mbPerSec.toFixed(1)} MB/s`);
