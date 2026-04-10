//! Core matching engine: daachorse wrapper, identity protection, byte↔codepoint mapping.

use std::collections::{BTreeSet, HashSet};

use daachorse::CharwiseDoubleArrayAhoCorasick;

use crate::header;

// ── Types ────────────────────────────────────────────────────────────────────

#[derive(Debug, Clone)]
pub(crate) struct TermHit {
    pub byte_start: usize,
    pub byte_end: usize,
    pub source: String,
    pub target: String,
}

// ── Pattern table deserialization ────────────────────────────────────────────

/// Reads the binary pattern table format written by build.rs.
///
/// Format:
///   u32 LE: count
///   For each entry:
///     u8: source_mask (0b01=CN, 0b10=HK, 0b11=both)
///     u32 LE: source_len
///     [u8; source_len]: source bytes
///     u32 LE: target_len
///     [u8; target_len]: target bytes
///
/// Returns `(source, target, source_mask)` triples.
pub(crate) fn deserialize_pattern_table(bytes: &[u8]) -> Vec<(String, String, u8)> {
    let mut pos = 0;

    let count = u32::from_le_bytes(bytes[pos..pos + 4].try_into().unwrap()) as usize;
    pos += 4;

    let mut table = Vec::with_capacity(count);
    for _ in 0..count {
        let mask = bytes[pos];
        pos += 1;

        let src_len = u32::from_le_bytes(bytes[pos..pos + 4].try_into().unwrap()) as usize;
        pos += 4;
        let src = std::str::from_utf8(&bytes[pos..pos + src_len])
            .unwrap()
            .to_string();
        pos += src_len;

        let tgt_len = u32::from_le_bytes(bytes[pos..pos + 4].try_into().unwrap()) as usize;
        pos += 4;
        let tgt = std::str::from_utf8(&bytes[pos..pos + tgt_len])
            .unwrap()
            .to_string();
        pos += tgt_len;

        table.push((src, tgt, mask));
    }

    table
}

// ── Automaton construction ──────────────────────────────────────────────────

/// Build a runtime automaton from a pattern list (for custom dictionaries).
pub(crate) fn build_automaton(
    patterns: &[(String, String)],
) -> CharwiseDoubleArrayAhoCorasick<u32> {
    use daachorse::{CharwiseDoubleArrayAhoCorasickBuilder, MatchKind};

    let patvals: Vec<(&str, u32)> = patterns
        .iter()
        .enumerate()
        .map(|(i, (src, _))| (src.as_str(), i as u32))
        .collect();

    CharwiseDoubleArrayAhoCorasickBuilder::new()
        .match_kind(MatchKind::Standard)
        .build_with_values(patvals)
        .expect("failed to build daachorse automaton")
}

/// Deserialize the precompiled default automaton from embedded bytes.
///
/// # Safety
/// Uses `deserialize_unchecked` — safe when bytes come from the same daachorse
/// version (verified by header magic + version check).
pub(crate) fn deserialize_default_automaton(bytes: &[u8]) -> CharwiseDoubleArrayAhoCorasick<u32> {
    let payload = header::verify_header(bytes, header::SourceMask::CN_HK);
    // SAFETY: bytes were produced by the same daachorse version (verified above).
    let (automaton, _trailing) =
        unsafe { CharwiseDoubleArrayAhoCorasick::deserialize_unchecked(payload) };
    automaton
}

// ── Byte ↔ codepoint mapping ────────────────────────────────────────────────

/// Build a mapping from byte offset to codepoint index.
///
/// Returns a `Vec` of length `text.len() + 1` where `map[byte_offset]` gives
/// the codepoint index at that byte position.
pub(crate) fn build_byte_to_cp(text: &str) -> Vec<usize> {
    let mut map = vec![0usize; text.len() + 1];
    for (cp_idx, (byte_idx, ch)) in text.char_indices().enumerate() {
        map[byte_idx] = cp_idx;
        // Fill intermediate bytes within this char with the same cp index.
        for item in map
            .iter_mut()
            .take(byte_idx + ch.len_utf8())
            .skip(byte_idx + 1)
        {
            *item = cp_idx;
        }
    }
    // Sentinel: one past the last byte = total codepoint count.
    map[text.len()] = text.chars().count();
    map
}

// ── Core matching algorithm ─────────────────────────────────────────────────

/// Find all non-overlapping term matches using the Aho-Corasick automaton,
/// with identity-based protection to avoid false conversions.
///
/// This is the Rust port of Python `matcher.py:find_matches` (lines 60-134).
pub(crate) fn find_term_matches(
    pma: &CharwiseDoubleArrayAhoCorasick<u32>,
    pattern_table: &[(String, String)],
    text: &str,
) -> Vec<TermHit> {
    // 1. Collect all overlapping hits.
    let mut all_hits: Vec<TermHit> = pma
        .find_overlapping_iter(text)
        .map(|m| {
            let idx = m.value() as usize;
            let (ref src, ref tgt) = pattern_table[idx];
            TermHit {
                byte_start: m.start(),
                byte_end: m.end(),
                source: src.clone(),
                target: tgt.clone(),
            }
        })
        .collect();

    if all_hits.is_empty() {
        return Vec::new();
    }

    // 2. Sort by (byte_start ASC, length DESC).
    all_hits.sort_by(|a, b| {
        a.byte_start.cmp(&b.byte_start).then_with(|| {
            let len_a = a.byte_end - a.byte_start;
            let len_b = b.byte_end - b.byte_start;
            len_b.cmp(&len_a) // DESC
        })
    });

    // 3. Build protected byte-range set from identity matches.
    let mut identity_matches: Vec<&TermHit> = Vec::new();
    let mut non_identity_spans: Vec<(usize, usize)> = Vec::new();

    for hit in &all_hits {
        if hit.source == hit.target {
            identity_matches.push(hit);
        } else {
            non_identity_spans.push((hit.byte_start, hit.byte_end));
        }
    }

    let mut protected: BTreeSet<usize> = BTreeSet::new();

    if non_identity_spans.is_empty() {
        // All identity → all ranges are protected (nothing to convert).
        for hit in &identity_matches {
            for b in hit.byte_start..hit.byte_end {
                protected.insert(b);
            }
        }
    } else {
        // Sort non-identity spans by start, build prefix_max_end.
        non_identity_spans.sort_by_key(|&(s, _)| s);

        let mut prefix_max_end: Vec<usize> = Vec::with_capacity(non_identity_spans.len());
        let mut running_max = 0usize;
        for &(_, end) in &non_identity_spans {
            running_max = running_max.max(end);
            prefix_max_end.push(running_max);
        }

        // For each identity match, check if it's fully contained in any non-identity span.
        for hit in &identity_matches {
            if !is_contained_in_non_identity(
                hit.byte_start,
                hit.byte_end,
                &non_identity_spans,
                &prefix_max_end,
            ) {
                for b in hit.byte_start..hit.byte_end {
                    protected.insert(b);
                }
            }
        }
    }

    // 4. Left-to-right greedy filter.
    let mut result: Vec<TermHit> = Vec::new();
    let mut cursor: usize = 0;

    for hit in &all_hits {
        if hit.byte_start < cursor {
            continue; // overlap — skip
        }

        let is_identity = hit.source == hit.target;

        if !is_identity {
            // Check if any byte in [start..end) is protected.
            if (hit.byte_start..hit.byte_end).any(|b| protected.contains(&b)) {
                continue; // protected — skip (don't advance cursor)
            }
        }

        cursor = hit.byte_end;

        if !is_identity {
            result.push(hit.clone());
        }
        // Identity matches advance cursor but are never emitted.
    }

    result
}

/// Return all byte positions covered by any raw automaton hit, including
/// identity terms (source == target). Used to prevent the char layer from
/// converting characters protected by identity term matches.
pub(crate) fn get_covered_positions(
    pma: &CharwiseDoubleArrayAhoCorasick<u32>,
    text: &str,
) -> HashSet<usize> {
    let mut covered = HashSet::new();
    for m in pma.find_overlapping_iter(text) {
        for b in m.start()..m.end() {
            covered.insert(b);
        }
    }
    covered
}

/// Check whether the identity span `[start, end)` is fully contained within
/// some non-identity span, using binary search + prefix_max_end.
fn is_contained_in_non_identity(
    start: usize,
    end: usize,
    spans: &[(usize, usize)],
    prefix_max_end: &[usize],
) -> bool {
    // Find the rightmost span with span.start <= start.
    let idx = match spans.binary_search_by_key(&start, |&(s, _)| s) {
        Ok(i) => i,
        Err(0) => return false, // All spans start after this identity match.
        Err(i) => i - 1,
    };

    // Check if the prefix_max_end up to idx covers end.
    // Any span in [0..=idx] that starts <= start and ends >= end would contain it.
    prefix_max_end[idx] >= end
}

// ── Charmap application ────────────────────────────────────────────────────

/// Apply charmap to a text segment, skipping byte positions that are in the
/// covered set. `offset` is the byte offset of this segment within the
/// original text.
pub(crate) fn apply_charmap_skipping(
    segment: &str,
    char_map: &phf::Map<char, char>,
    covered: &HashSet<usize>,
    offset: usize,
) -> String {
    let mut result = String::with_capacity(segment.len());
    for (byte_idx, ch) in segment.char_indices() {
        if covered.contains(&(offset + byte_idx)) {
            result.push(ch);
        } else {
            result.push(char_map.get(&ch).copied().unwrap_or(ch));
        }
    }
    result
}

// ── Tests ───────────────────────────────────────────────────────────────────

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn byte_to_cp_ascii() {
        let map = build_byte_to_cp("hello");
        assert_eq!(map[0], 0);
        assert_eq!(map[1], 1);
        assert_eq!(map[5], 5);
    }

    #[test]
    fn byte_to_cp_cjk() {
        // "中X" — 中=3 bytes, X=1 byte
        let map = build_byte_to_cp("中X");
        assert_eq!(map[0], 0);
        assert_eq!(map[3], 1);
        assert_eq!(map[4], 2);
    }

    #[test]
    fn byte_to_cp_supplementary() {
        // "𠮷A" — 𠮷=4 bytes, A=1 byte
        let map = build_byte_to_cp("𠮷A");
        assert_eq!(map[0], 0);
        assert_eq!(map[4], 1);
        assert_eq!(map[5], 2);
    }
}
