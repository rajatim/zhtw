use std::sync::{Arc, LazyLock};

use daachorse::CharwiseDoubleArrayAhoCorasick;

use crate::config::Config;
use crate::error::{Error, Result};
use crate::generated::{AUTOMATON_CNHK_BYTES, CHAR_MAP, PATTERN_TABLE_CNHK_BYTES};
use crate::matcher;
use crate::source::Source;

// ── Public types ────────────────────────────────────────────────────────────

#[derive(Debug, Clone, PartialEq, Eq, serde::Serialize)]
pub struct Match {
    pub start: usize,
    pub end: usize,
    pub source: String,
    pub target: String,
}

#[derive(Debug, Clone, PartialEq, Eq, serde::Serialize)]
pub struct LookupResult {
    pub input: String,
    pub output: String,
    pub changed: bool,
    pub details: Vec<ConversionDetail>,
}

#[derive(Debug, Clone, PartialEq, Eq, serde::Serialize)]
pub struct ConversionDetail {
    pub source: String,
    pub target: String,
    pub layer: Layer,
    pub position: usize,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, serde::Serialize)]
#[serde(rename_all = "lowercase")]
pub enum Layer {
    Term,
    Char,
}

// ── Shared internals ────────────────────────────────────────────────────────

struct Inner {
    automaton: CharwiseDoubleArrayAhoCorasick<u32>,
    pattern_table: Vec<(String, String)>,
    char_layer_enabled: bool,
}

// SAFETY: CharwiseDoubleArrayAhoCorasick is an immutable data structure after
// construction — it is safe to share across threads.  The daachorse crate
// simply doesn't add the marker impls because it uses raw pointers internally.
unsafe impl Send for Inner {}
unsafe impl Sync for Inner {}

// ── Precompiled defaults (LazyLock) ─────────────────────────────────────────

static DEFAULT_INNER: LazyLock<Arc<Inner>> = LazyLock::new(|| {
    let automaton = matcher::deserialize_default_automaton(AUTOMATON_CNHK_BYTES);
    // Strip source masks — default path uses all patterns, indices match pre-compiled automaton.
    let pattern_table: Vec<(String, String)> =
        matcher::deserialize_pattern_table(PATTERN_TABLE_CNHK_BYTES)
            .into_iter()
            .map(|(s, t, _mask)| (s, t))
            .collect();
    Arc::new(Inner {
        automaton,
        pattern_table,
        char_layer_enabled: true,
    })
});

static DEFAULT_INSTANCE: LazyLock<Converter> = LazyLock::new(|| Converter {
    inner: Arc::clone(&DEFAULT_INNER),
});

// ── Converter ───────────────────────────────────────────────────────────────

#[derive(Clone)]
pub struct Converter {
    inner: Arc<Inner>,
}

impl Converter {
    pub fn new(config: Config) -> Result<Self> {
        if config.sources.is_empty() {
            return Err(Error::EmptySources);
        }

        let is_default = config.custom_dict.is_empty()
            && config.sources.len() == 2
            && config.sources.contains(&Source::Cn)
            && config.sources.contains(&Source::Hk);

        if is_default {
            // Share the precompiled LazyLock automaton.
            return Ok(Converter {
                inner: Arc::clone(&DEFAULT_INNER),
            });
        }

        // Custom config: build automaton at runtime.
        // Compute source mask from selected sources.
        let desired_mask: u8 = config.sources.iter().fold(0u8, |acc, s| match s {
            Source::Cn => acc | 0b01,
            Source::Hk => acc | 0b10,
        });

        // Filter built-in patterns by source mask.
        let mut pattern_map: std::collections::HashMap<String, String> =
            matcher::deserialize_pattern_table(PATTERN_TABLE_CNHK_BYTES)
                .into_iter()
                .filter(|&(_, _, mask)| mask & desired_mask != 0)
                .map(|(s, t, _)| (s, t))
                .collect();

        // Merge custom dict (overrides built-in entries with the same key).
        // Skip empty keys — daachorse panics on empty patterns.
        for (k, v) in &config.custom_dict {
            if !k.is_empty() {
                pattern_map.insert(k.clone(), v.clone());
            }
        }

        // Collect back to sorted Vec for deterministic automaton.
        let mut patterns: Vec<(String, String)> = pattern_map.into_iter().collect();
        patterns.sort_by(|a, b| a.0.cmp(&b.0));

        let automaton = matcher::build_automaton(&patterns);

        // Char layer only runs when CN source is selected (matches Python behavior).
        let char_layer_enabled = config.sources.contains(&Source::Cn);

        Ok(Converter {
            inner: Arc::new(Inner {
                automaton,
                pattern_table: patterns,
                char_layer_enabled,
            }),
        })
    }

    pub fn builder() -> crate::Builder {
        crate::Builder::default()
    }

    /// Returns a shared static instance with the default configuration (Cn+Hk).
    pub fn default_instance() -> &'static Self {
        &DEFAULT_INSTANCE
    }

    /// Convert simplified Chinese text to Traditional Chinese (Taiwan).
    pub fn convert(&self, text: &str) -> String {
        if text.is_empty() {
            return String::new();
        }

        let inner = &self.inner;

        // Covered byte positions from ALL automaton hits (including identity terms).
        // Must be computed on original text before any replacements.
        let covered = matcher::get_covered_positions(&inner.automaton, text);
        let hits = matcher::find_term_matches(&inner.automaton, &inner.pattern_table, text);

        if hits.is_empty() {
            return if inner.char_layer_enabled {
                matcher::apply_charmap_skipping(text, &CHAR_MAP, &covered, 0)
            } else {
                text.to_string()
            };
        }

        // Gap mode: term targets inserted verbatim; gaps get char-layer on uncovered only.
        let mut result = String::with_capacity(text.len());
        let mut last_end: usize = 0;
        for h in &hits {
            let gap = &text[last_end..h.byte_start];
            if inner.char_layer_enabled {
                result.push_str(&matcher::apply_charmap_skipping(
                    gap, &CHAR_MAP, &covered, last_end,
                ));
            } else {
                result.push_str(gap);
            }
            result.push_str(&h.target);
            last_end = h.byte_end;
        }
        let tail = &text[last_end..];
        if inner.char_layer_enabled {
            result.push_str(&matcher::apply_charmap_skipping(
                tail, &CHAR_MAP, &covered, last_end,
            ));
        } else {
            result.push_str(tail);
        }
        result
    }

    /// Check text for simplified Chinese terms/characters, returning match info.
    pub fn check(&self, text: &str) -> Vec<Match> {
        if text.is_empty() {
            return Vec::new();
        }

        let inner = &self.inner;
        let byte_to_cp = matcher::build_byte_to_cp(text);

        // Covered byte positions from ALL automaton hits (including identity terms)
        let covered_bytes = matcher::get_covered_positions(&inner.automaton, text);

        // Term layer matches.
        let hits = matcher::find_term_matches(&inner.automaton, &inner.pattern_table, text);
        let mut matches: Vec<Match> = hits
            .iter()
            .map(|h| Match {
                start: byte_to_cp[h.byte_start],
                end: byte_to_cp[h.byte_end],
                source: h.source.clone(),
                target: h.target.clone(),
            })
            .collect();

        // Char layer matches (if enabled): skip covered byte positions.
        if inner.char_layer_enabled {
            for (byte_idx, ch) in text.char_indices() {
                if covered_bytes.contains(&byte_idx) {
                    continue;
                }
                if let Some(&mapped) = CHAR_MAP.get(&ch) {
                    if mapped != ch {
                        matches.push(Match {
                            start: byte_to_cp[byte_idx],
                            end: byte_to_cp[byte_idx] + 1,
                            source: ch.to_string(),
                            target: mapped.to_string(),
                        });
                    }
                }
            }
        }

        matches
    }

    /// Look up a word/phrase and return detailed conversion information.
    pub fn lookup(&self, word: &str) -> LookupResult {
        if word.is_empty() {
            return LookupResult {
                input: String::new(),
                output: String::new(),
                changed: false,
                details: Vec::new(),
            };
        }

        let inner = &self.inner;
        let byte_to_cp = matcher::build_byte_to_cp(word);
        let hits = matcher::find_term_matches(&inner.automaton, &inner.pattern_table, word);

        // Covered byte positions from ALL automaton hits (including identity terms)
        let covered_bytes = matcher::get_covered_positions(&inner.automaton, word);

        let mut details: Vec<ConversionDetail> = Vec::new();

        // Term details.
        for h in &hits {
            details.push(ConversionDetail {
                source: h.source.clone(),
                target: h.target.clone(),
                layer: Layer::Term,
                position: byte_to_cp[h.byte_start],
            });
        }

        // Char details (if enabled): walk original text, skip covered bytes.
        if inner.char_layer_enabled {
            for (byte_idx, ch) in word.char_indices() {
                if covered_bytes.contains(&byte_idx) {
                    continue;
                }
                if let Some(&mapped) = CHAR_MAP.get(&ch) {
                    if mapped != ch {
                        details.push(ConversionDetail {
                            source: ch.to_string(),
                            target: mapped.to_string(),
                            layer: Layer::Char,
                            position: byte_to_cp[byte_idx],
                        });
                    }
                }
            }
        }

        // Sort by position.
        details.sort_by_key(|d| d.position);

        let output = self.convert(word);
        let changed = output != word;

        LookupResult {
            input: word.to_string(),
            output,
            changed,
            details,
        }
    }
}
