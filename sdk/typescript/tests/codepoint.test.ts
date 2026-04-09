import { describe, it, expect } from 'vitest';
import { codepointLength, utf16ToCodepoint, codepointAt } from '../src/core/codepoint';

describe('codepointLength', () => {
  it('counts ASCII as 1 per char', () => {
    expect(codepointLength('hello')).toBe(5);
  });
  it('counts BMP CJK as 1 per char', () => {
    expect(codepointLength('軟體測試')).toBe(4);
  });
  it('counts supplementary-plane codepoints as 1 each', () => {
    // 𠮷 is U+20BB7, one codepoint, two UTF-16 code units
    expect(codepointLength('𠮷')).toBe(1);
    expect(codepointLength('𠮷野家')).toBe(3);
  });
  it('returns 0 for empty string', () => {
    expect(codepointLength('')).toBe(0);
  });
});

describe('utf16ToCodepoint', () => {
  it('is identity for pure BMP', () => {
    const s = 'abc軟體';
    expect(utf16ToCodepoint(s, 0)).toBe(0);
    expect(utf16ToCodepoint(s, 3)).toBe(3);
    expect(utf16ToCodepoint(s, 5)).toBe(5);
  });
  it('collapses surrogate pairs', () => {
    const s = '𠮷野家'; // utf16 length 4, codepoint length 3
    expect(utf16ToCodepoint(s, 0)).toBe(0);
    expect(utf16ToCodepoint(s, 2)).toBe(1); // after 𠮷
    expect(utf16ToCodepoint(s, 3)).toBe(2);
    expect(utf16ToCodepoint(s, 4)).toBe(3);
  });
  it('handles mixed BMP + supplementary', () => {
    const s = 'a𠮷b'; // utf16: a(1) + 𠮷(2) + b(1) = 4
    expect(utf16ToCodepoint(s, 1)).toBe(1); // after a
    expect(utf16ToCodepoint(s, 3)).toBe(2); // after 𠮷
    expect(utf16ToCodepoint(s, 4)).toBe(3); // after b
  });
});

describe('codepointAt', () => {
  it('walks to nth codepoint', () => {
    const s = 'a𠮷b';
    expect(codepointAt(s, 0)).toEqual({ char: 'a', utf16Index: 0 });
    expect(codepointAt(s, 1)).toEqual({ char: '𠮷', utf16Index: 1 });
    expect(codepointAt(s, 2)).toEqual({ char: 'b', utf16Index: 3 });
  });
});
