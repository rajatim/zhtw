use std::collections::HashSet;
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
    let pattern_table = matcher::deserialize_pattern_table(PATTERN_TABLE_CNHK_BYTES);
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
        let mut pattern_map: std::collections::HashMap<String, String> =
            matcher::deserialize_pattern_table(PATTERN_TABLE_CNHK_BYTES)
                .into_iter()
                .collect();

        // Merge custom dict (overrides built-in entries with the same key).
        for (k, v) in &config.custom_dict {
            pattern_map.insert(k.clone(), v.clone());
        }

        // Collect back to sorted Vec for deterministic automaton.
        let mut patterns: Vec<(String, String)> = pattern_map.into_iter().collect();
        patterns.sort_by(|a, b| a.0.cmp(&b.0));

        let automaton = matcher::build_automaton(&patterns);

        Ok(Converter {
            inner: Arc::new(Inner {
                automaton,
                pattern_table: patterns,
                char_layer_enabled: true,
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
        let hits = matcher::find_term_matches(&inner.automaton, &inner.pattern_table, text);
        let after_terms = matcher::apply_term_replacements(text, &hits);

        if inner.char_layer_enabled {
            matcher::apply_charmap(&after_terms, &CHAR_MAP)
        } else {
            after_terms
        }
    }

    /// Check text for simplified Chinese terms/characters, returning match info.
    pub fn check(&self, text: &str) -> Vec<Match> {
        if text.is_empty() {
            return Vec::new();
        }

        let inner = &self.inner;
        let byte_to_cp = matcher::build_byte_to_cp(text);

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

        // Char layer matches (if enabled).
        if inner.char_layer_enabled {
            for (cp_idx, ch) in text.chars().enumerate() {
                if let Some(&mapped) = CHAR_MAP.get(&ch) {
                    if mapped != ch {
                        matches.push(Match {
                            start: cp_idx,
                            end: cp_idx + 1,
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

        // Track which bytes are covered by term hits.
        let mut covered_bytes: HashSet<usize> = HashSet::new();
        for h in &hits {
            for b in h.byte_start..h.byte_end {
                covered_bytes.insert(b);
            }
        }

        let mut details: Vec<ConversionDetail> = Vec::new();

        // Term details — apply charmap post-pass on target if char_layer_enabled.
        for h in &hits {
            let target = if inner.char_layer_enabled {
                matcher::apply_charmap(&h.target, &CHAR_MAP)
            } else {
                h.target.clone()
            };
            details.push(ConversionDetail {
                source: h.source.clone(),
                target,
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
