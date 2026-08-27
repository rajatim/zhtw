/** @vitest-environment happy-dom */
// zhtw:disable - test inputs intentionally use Simplified Chinese
import { describe, it, expect } from 'vitest';
import {
  convert,
  convertJson,
  check,
  explain,
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

  it('module-level JSON conversion only changes values', () => {
    expect(convertJson('{"软件":"软件"}')).toBe('{"软件":"軟體"}');
  });

  it('module-level explain returns the conversion output', () => {
    expect(explain('软件').output).toBe(convert('软件'));
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
    expect(typeof c.convertJson).toBe('function');
    expect(typeof c.explain).toBe('function');
  });

  it('custom rules use the cross-SDK deterministic legacy ID', () => {
    const c = createConverter({
      sources: ['cn'],
      customDict: { 软件: '自訂軟體' },
    });
    expect(c.explain('软件').events.find((event) => event.outcome === 'applied')?.rule_id).toBe(
      'legacy:cn:custom:6dee1b8fe38334612ee097e8',
    );
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
