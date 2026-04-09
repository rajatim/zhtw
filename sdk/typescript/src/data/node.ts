import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import type { ZhtwData } from '../core/types';

// Resolve the directory of this module at runtime. tsup (platform: 'neutral')
// emits two bundles:
//   • .mjs  — real ESM; import.meta.url is a valid file:// URL
//   • .cjs  — esbuild replaces import.meta with {}, so import.meta.url is
//             undefined; __dirname is the real module directory
//
// We cannot use `typeof __dirname !== 'undefined'` as the ESM guard because
// esbuild's 'neutral' platform shims __dirname in the ESM bundle, making the
// check pass with a wrong (cwd-relative) value. Probe import.meta.url first
// (only truthy in real ESM), fall back to __dirname for the CJS path.
interface ImportMetaLike {
  url?: string;
  dirname?: string;
}
const meta: ImportMetaLike = import.meta;

const HERE: string = (() => {
  if (typeof meta.url === 'string' && meta.url.startsWith('file://')) {
    // Prefer import.meta.dirname (Node ≥20.11) to skip the URL parse.
    return meta.dirname ?? dirname(fileURLToPath(meta.url));
  }
  return __dirname;
})();

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
