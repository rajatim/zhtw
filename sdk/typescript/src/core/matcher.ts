/**
 * Internal match type. Uses UTF-16 code-unit indices because JS strings are
 * UTF-16. NOT exported from the package — core/converter.ts converts these
 * into codepoint-indexed public `Match` values before returning to callers.
 */
export interface Utf16Match {
  /** UTF-16 code-unit index, inclusive. */
  start: number;
  /** UTF-16 code-unit index, exclusive. */
  end: number;
  source: string;
  target: string;
}

interface Node {
  children: Map<number, Node>;
  fail: Node | null;
  /** Patterns that terminate at (or via output-link through) this node. */
  outputs: string[];
}

function createNode(): Node {
  return { children: new Map(), fail: null, outputs: [] };
}

export class AhoCorasickMatcher {
  private readonly root: Node = createNode();
  private readonly patterns: Record<string, string>;

  constructor(patterns: Record<string, string>) {
    this.patterns = patterns;
    for (const key of Object.keys(patterns)) {
      if (key.length === 0) continue; // skip empty-key entries (matches Python)
      this.addPattern(key);
    }
    this.buildFailureLinks();
  }

  private addPattern(pattern: string): void {
    let node = this.root;
    for (let i = 0; i < pattern.length; i++) {
      const code = pattern.charCodeAt(i);
      let next = node.children.get(code);
      if (!next) {
        next = createNode();
        node.children.set(code, next);
      }
      node = next;
    }
    node.outputs.push(pattern);
  }

  private buildFailureLinks(): void {
    const queue: Node[] = [];
    for (const child of this.root.children.values()) {
      child.fail = this.root;
      queue.push(child);
    }
    while (queue.length > 0) {
      const node = queue.shift()!;
      for (const [code, child] of node.children) {
        queue.push(child);
        let f = node.fail;
        while (f !== null && !f.children.has(code)) {
          f = f.fail;
        }
        child.fail = f === null ? this.root : (f.children.get(code) ?? this.root);
        // Merge output link patterns (longest-output-first is not required here;
        // we emit every output reachable from this state).
        if (child.fail.outputs.length > 0) {
          child.outputs = [...child.outputs, ...child.fail.outputs];
        }
      }
    }
  }

  /**
   * Yield every raw AC match in `text`. At each right-edge position, emit
   * all patterns that terminate there (possibly multiple, possibly overlapping
   * with emissions at other positions). The longest-match + protected-range
   * filter happens in `findMatches` (added in the next task).
   */
  *iterEmissions(text: string): Generator<Utf16Match> {
    let node: Node = this.root;
    for (let i = 0; i < text.length; i++) {
      const code = text.charCodeAt(i);
      while (node !== this.root && !node.children.has(code)) {
        node = node.fail ?? this.root;
      }
      const next = node.children.get(code);
      if (next) {
        node = next;
      }
      if (node.outputs.length > 0) {
        for (const pat of node.outputs) {
          const start = i + 1 - pat.length;
          yield {
            start,
            end: i + 1,
            source: pat,
            target: this.patterns[pat]!,
          };
        }
      }
    }
  }

  /** Stub — implemented in the next task. */
  findMatches(_text: string): Utf16Match[] {
    throw new Error('findMatches: not implemented yet (see Task 5)');
  }

  /** Stub — implemented in the next task. */
  replaceAll(_text: string): string {
    throw new Error('replaceAll: not implemented yet (see Task 5)');
  }
}
