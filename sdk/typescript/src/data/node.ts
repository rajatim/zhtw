import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import type { ZhtwData } from '../core/types';

// Resolve the directory of the compiled entry file at runtime. Works under
// both CJS (__dirname is defined) and ESM (use import.meta.url).
const HERE =
  typeof __dirname !== 'undefined'
    ? __dirname
    : dirname(fileURLToPath(import.meta.url));

const DATA_PATH = join(HERE, 'zhtw-data.json');

export function loadData(): ZhtwData {
  try {
    const raw = readFileSync(DATA_PATH, 'utf-8');
    return JSON.parse(raw) as ZhtwData;
  } catch (err) {
    const reason = err instanceof Error ? err.message : String(err);
    throw new Error(`zhtw: failed to load zhtw-data.json: ${reason}`);
  }
}
