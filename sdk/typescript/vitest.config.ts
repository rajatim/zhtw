import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    environment: 'node',
    include: ['tests/**/*.test.ts'],
    exclude: ['node_modules/**'],
    // pack.test.ts is env-gated via `describe.skip` (ZHTW_TS_RUN_PACK=1);
    // no need to exclude it at the config level.
  },
});
