import { describe, it, expect } from 'vitest';
import { execFileSync } from 'node:child_process';
import { mkdtempSync, writeFileSync, readdirSync, rmSync, mkdirSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';

// Skipped by default; CI sets ZHTW_TS_RUN_PACK=1 to run it.
const runPack = process.env.ZHTW_TS_RUN_PACK === '1';
const describeOrSkip = runPack ? describe : describe.skip;

describeOrSkip('pack + install smoke test', () => {
  it('packs, installs, and imports from the tarball', () => {
    const pkgDir = resolve(__dirname, '..');
    const scratch = mkdtempSync(join(tmpdir(), 'zhtw-js-pack-'));
    try {
      // 1. Pack the package into scratch.
      const packDir = join(scratch, 'tgz');
      mkdirSync(packDir, { recursive: true });
      execFileSync('pnpm', ['pack', '--pack-destination', packDir], {
        cwd: pkgDir,
        encoding: 'utf-8',
        stdio: 'inherit',
      });
      const tarball = readdirSync(packDir).find((f) => f.endsWith('.tgz'));
      if (!tarball) throw new Error('pnpm pack did not produce a .tgz');
      const tarballPath = join(packDir, tarball);

      // 2. Install the tarball into a fresh consumer dir.
      const consumer = join(scratch, 'consumer');
      mkdirSync(consumer, { recursive: true });
      writeFileSync(
        join(consumer, 'package.json'),
        JSON.stringify({ name: 'consumer', version: '0.0.0', type: 'module', private: true }),
      );
      execFileSync('npm', ['install', '--silent', tarballPath], {
        cwd: consumer,
        stdio: 'inherit',
      });

      // 3. Write a smoke script that exercises all three APIs.
      const smoke = `
import { convert, check, lookup, createConverter } from 'zhtw-js';
const c1 = convert('hello');
if (typeof c1 !== 'string') throw new Error('convert: not a string');
const c2 = check('');
if (!Array.isArray(c2)) throw new Error('check: not an array');
const c3 = lookup('');
if (c3.changed !== false) throw new Error('lookup: empty should be unchanged');
const conv = createConverter({ sources: ['cn'] });
if (typeof conv.convert !== 'function') throw new Error('factory: no convert');
console.log('OK');
`;
      writeFileSync(join(consumer, 'smoke.mjs'), smoke);

      // 4. Run the smoke script.
      const out = execFileSync('node', ['smoke.mjs'], {
        cwd: consumer,
        encoding: 'utf-8',
      });
      expect(out.trim()).toBe('OK');
    } finally {
      rmSync(scratch, { recursive: true, force: true });
    }
  }, 60_000);
});
