import { defineConfig } from 'tsup';
import { copyFileSync, mkdirSync } from 'node:fs';
import { resolve } from 'node:path';

export default defineConfig({
  entry: {
    'index.node': 'src/index.node.ts',
    'index.browser': 'src/index.browser.ts',
  },
  format: ['esm', 'cjs'],
  dts: true,
  sourcemap: true,
  clean: true,
  target: 'es2022',
  platform: 'neutral',
  outDir: 'dist',
  loader: { '.json': 'json' },
  outExtension({ format }) {
    return { js: format === 'esm' ? '.mjs' : '.cjs' };
  },
  onSuccess: async () => {
    const src = resolve(__dirname, '../data/zhtw-data.json');
    const outDir = resolve(__dirname, 'dist');
    mkdirSync(outDir, { recursive: true });
    copyFileSync(src, resolve(outDir, 'zhtw-data.json'));
    console.log('[tsup] copied zhtw-data.json → dist/');
  },
});
