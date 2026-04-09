/** Count the number of Unicode codepoints in a JS (UTF-16) string. */
export function codepointLength(s: string): number {
  let count = 0;
  for (let i = 0; i < s.length; ) {
    const code = s.charCodeAt(i);
    i += code >= 0xd800 && code <= 0xdbff && i + 1 < s.length ? 2 : 1;
    count++;
  }
  return count;
}

/**
 * Convert a UTF-16 code-unit index into a codepoint index.
 * For BMP-only strings this is identity.
 */
export function utf16ToCodepoint(text: string, utf16Index: number): number {
  let cp = 0;
  let i = 0;
  while (i < utf16Index && i < text.length) {
    const code = text.charCodeAt(i);
    i += code >= 0xd800 && code <= 0xdbff && i + 1 < text.length ? 2 : 1;
    cp++;
  }
  return cp;
}

/**
 * Walk to the `cpIndex`-th codepoint (0-based). Returns the character (as a
 * 1- or 2-code-unit string) and its UTF-16 offset.
 */
export function codepointAt(
  text: string,
  cpIndex: number,
): { char: string; utf16Index: number } {
  let cp = 0;
  let i = 0;
  while (i < text.length) {
    const code = text.charCodeAt(i);
    const isHigh = code >= 0xd800 && code <= 0xdbff && i + 1 < text.length;
    const step = isHigh ? 2 : 1;
    if (cp === cpIndex) {
      return { char: text.substring(i, i + step), utf16Index: i };
    }
    cp++;
    i += step;
  }
  throw new RangeError(`codepointAt: index ${cpIndex} out of range (length ${cp})`);
}
