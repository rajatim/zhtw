/** @vitest-environment happy-dom */
import { describe, it, expect } from 'vitest';
import {
  convert,
  check,
  lookup,
  createConverter,
} from '../src/index.browser';

describe('public API (browser entry under happy-dom)', () => {
  it('module-level convert works', () => {
    expect(typeof convert('')).toBe('string');
  });

  it('module-level check returns an array', () => {
    expect(Array.isArray(check(''))).toBe(true);
  });

  it('module-level lookup returns a LookupResult shape', () => {
    const r = lookup('');
    expect(r).toEqual({ input: '', output: '', changed: false, details: [] });
  });

  it('createConverter returns a working Converter', () => {
    const c = createConverter({ sources: ['cn'] });
    expect(typeof c.convert).toBe('function');
    expect(typeof c.check).toBe('function');
    expect(typeof c.lookup).toBe('function');
  });

  it('end-to-end: a known conversion goes through', () => {
    // Use the real data file; this phrase is in the canonical corpus.
    // Exact output is verified by the golden test; here we just assert change.
    const c = createConverter({ sources: ['cn'] });
    const r = c.lookup('软件');
    expect(r.changed).toBe(true);
    expect(r.output).not.toBe('软件');
  });

  it('default sources convert works without options', () => {
    const c = createConverter();
    expect(typeof c.convert('hello')).toBe('string');
  });
});
