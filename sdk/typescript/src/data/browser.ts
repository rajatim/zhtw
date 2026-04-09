// Import the canonical source at sdk/data/zhtw-data.json directly.
// tsup inlines this JSON into the browser bundle at build time, so the
// runtime has no fs/path dependency.
import data from '../../../data/zhtw-data.json';
import type { ZhtwData } from '../core/types';

export function loadData(): ZhtwData {
  return data as unknown as ZhtwData;
}
