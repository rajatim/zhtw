use std::collections::{HashMap, HashSet};
use std::sync::{Arc, LazyLock};

use daachorse::CharwiseDoubleArrayAhoCorasick;

use crate::config::{AmbiguityMode, Config};
use crate::error::{Error, Result};
use crate::generated::{
    AUTOMATON_CNHK_BYTES, BALANCED_DEFAULTS, CHAR_MAP, PATTERN_TABLE_CNHK_BYTES,
};
use crate::matcher;
use crate::rule_catalog;
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

#[derive(Debug, Clone, PartialEq, Eq, serde::Serialize)]
pub struct ExplainEvent {
    pub rule_id: String,
    pub layer: String,
    pub outcome: String,
    pub input_start: usize,
    pub input_end: usize,
    pub output_start: usize,
    pub output_end: usize,
    pub source: String,
    pub target: String,
    pub reason_code: String,
}

#[derive(Debug, Clone, PartialEq, Eq, serde::Serialize)]
pub struct ExplainResult {
    pub output: String,
    pub events: Vec<ExplainEvent>,
}

// ── Shared internals ────────────────────────────────────────────────────────

struct Inner {
    automaton: CharwiseDoubleArrayAhoCorasick<u32>,
    pattern_table: Vec<matcher::Pattern>,
    char_layer_enabled: bool,
    ambiguity_mode: AmbiguityMode,
    source_mask: u8,
}

// SAFETY: CharwiseDoubleArrayAhoCorasick is an immutable data structure after
// construction — it is safe to share across threads.  The daachorse crate
// simply doesn't add the marker impls because it uses raw pointers internally.
unsafe impl Send for Inner {}
unsafe impl Sync for Inner {}

struct CharacterChange {
    byte_start: usize,
    byte_end: usize,
    source: String,
    target: String,
    layer: &'static str,
    rule_id: String,
    reason_code: &'static str,
}

// ── Precompiled defaults (LazyLock) ─────────────────────────────────────────

static DEFAULT_INNER: LazyLock<Arc<Inner>> = LazyLock::new(|| {
    let automaton = matcher::deserialize_default_automaton(AUTOMATON_CNHK_BYTES);
    let pattern_table = matcher::deserialize_pattern_table(PATTERN_TABLE_CNHK_BYTES);
    Arc::new(Inner {
        automaton,
        pattern_table,
        char_layer_enabled: true,
        ambiguity_mode: AmbiguityMode::Strict,
        source_mask: 0b11,
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
            && config.ambiguity_mode == AmbiguityMode::Strict
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
        let mut pattern_map: std::collections::HashMap<String, matcher::Pattern> =
            matcher::deserialize_pattern_table(PATTERN_TABLE_CNHK_BYTES)
                .into_iter()
                .filter(|pattern| pattern.source_mask & desired_mask != 0)
                .map(|pattern| (pattern.source.clone(), pattern))
                .collect();

        // Merge custom dict (overrides built-in entries with the same key).
        // Skip empty keys — daachorse panics on empty patterns.
        for (k, v) in &config.custom_dict {
            if !k.is_empty() {
                let custom_record = rule_catalog::RuleMeta {
                    id: rule_catalog::legacy_custom_rule_id(k, v),
                    source: k.clone(),
                    target: v.clone(),
                    source_mask: 0b11,
                };
                if let Some(pattern) = pattern_map.get_mut(k) {
                    pattern.target.clone_from(v);
                    pattern.records.push(custom_record);
                } else {
                    pattern_map.insert(
                        k.clone(),
                        matcher::Pattern {
                            source: k.clone(),
                            target: v.clone(),
                            source_mask: 0b11,
                            records: vec![custom_record],
                        },
                    );
                }
            }
        }

        // Collect back to sorted Vec for deterministic automaton.
        let mut patterns: Vec<matcher::Pattern> = pattern_map.into_values().collect();
        patterns.sort_by(|a, b| a.source.cmp(&b.source));

        let automaton = matcher::build_automaton(&patterns);

        // Char layer only runs when CN source is selected (matches Python behavior).
        let char_layer_enabled = config.sources.contains(&Source::Cn);

        // balanced defaults are CN→TW mappings; degrade to strict when CN not in sources.
        let effective_mode = if char_layer_enabled {
            config.ambiguity_mode
        } else {
            AmbiguityMode::Strict
        };

        Ok(Converter {
            inner: Arc::new(Inner {
                automaton,
                pattern_table: patterns,
                char_layer_enabled,
                ambiguity_mode: effective_mode,
                source_mask: desired_mask,
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
        let (hits, covered) = matcher::scan(&inner.automaton, &inner.pattern_table, text);
        self.convert_with_scan(text, &hits, &covered)
    }

    fn convert_with_scan(
        &self,
        text: &str,
        hits: &[matcher::TermHit],
        covered: &std::collections::HashSet<usize>,
    ) -> String {
        let inner = &self.inner;
        let balanced = if inner.ambiguity_mode == AmbiguityMode::Balanced {
            Some(&BALANCED_DEFAULTS)
        } else {
            None
        };

        if hits.is_empty() {
            return if inner.char_layer_enabled || balanced.is_some() {
                matcher::apply_layers_skipping(text, &CHAR_MAP, balanced, covered, 0)
            } else {
                text.to_string()
            };
        }

        // Gap mode: term targets inserted verbatim; gaps get char/balanced layers on uncovered only.
        let mut result = String::with_capacity(text.len());
        let mut last_end: usize = 0;
        for h in hits {
            let gap = &text[last_end..h.byte_start];
            if inner.char_layer_enabled || balanced.is_some() {
                result.push_str(&matcher::apply_layers_skipping(
                    gap, &CHAR_MAP, balanced, covered, last_end,
                ));
            } else {
                result.push_str(gap);
            }
            result.push_str(&h.target);
            last_end = h.byte_end;
        }
        let tail = &text[last_end..];
        if inner.char_layer_enabled || balanced.is_some() {
            result.push_str(&matcher::apply_layers_skipping(
                tail, &CHAR_MAP, balanced, covered, last_end,
            ));
        } else {
            result.push_str(tail);
        }
        result
    }

    /// Convert only JSON string values while preserving unrelated bytes.
    pub fn convert_json(&self, text: &str) -> Result<String> {
        crate::json_adapter::convert_json_values(text, |value| self.convert(value))
    }

    /// Check text for simplified Chinese terms/characters, returning match info.
    pub fn check(&self, text: &str) -> Vec<Match> {
        if text.is_empty() {
            return Vec::new();
        }

        let inner = &self.inner;
        let byte_to_cp = matcher::build_byte_to_cp(text);

        // Term matches and effective coverage come from one automaton walk.
        let (hits, covered_bytes) = matcher::scan(&inner.automaton, &inner.pattern_table, text);
        let mut matches: Vec<Match> = hits
            .iter()
            .map(|h| Match {
                start: byte_to_cp[h.byte_start],
                end: byte_to_cp[h.byte_end],
                source: h.source.clone(),
                target: h.target.clone(),
            })
            .collect();

        // Balanced defaults layer (if enabled): emit matches for uncovered positions.
        if inner.ambiguity_mode == AmbiguityMode::Balanced {
            for (byte_idx, ch) in text.char_indices() {
                if covered_bytes.contains(&byte_idx) {
                    continue;
                }
                if let Some(&mapped) = BALANCED_DEFAULTS.get(&ch) {
                    matches.push(Match {
                        start: byte_to_cp[byte_idx],
                        end: byte_to_cp[byte_idx] + 1,
                        source: ch.to_string(),
                        target: mapped.to_string(),
                    });
                }
            }
        }

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
        let (hits, covered_bytes) = matcher::scan(&inner.automaton, &inner.pattern_table, word);

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

        // Balanced defaults (if enabled): walk original text, skip covered bytes.
        if inner.ambiguity_mode == AmbiguityMode::Balanced {
            for (byte_idx, ch) in word.char_indices() {
                if covered_bytes.contains(&byte_idx) {
                    continue;
                }
                if let Some(&mapped) = BALANCED_DEFAULTS.get(&ch) {
                    details.push(ConversionDetail {
                        source: ch.to_string(),
                        target: mapped.to_string(),
                        layer: Layer::Char,
                        position: byte_to_cp[byte_idx],
                    });
                }
            }
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

    fn character_changes(&self, text: &str, covered: &HashSet<usize>) -> Vec<CharacterChange> {
        let mut changes = Vec::new();
        for (byte_start, source) in text.char_indices() {
            if covered.contains(&byte_start) {
                continue;
            }
            if self.inner.ambiguity_mode == AmbiguityMode::Balanced {
                if let Some(&balanced) = BALANCED_DEFAULTS.get(&source) {
                    let target = CHAR_MAP.get(&balanced).copied().unwrap_or(balanced);
                    if target != source {
                        changes.push(CharacterChange {
                            byte_start,
                            byte_end: byte_start + source.len_utf8(),
                            source: source.to_string(),
                            target: target.to_string(),
                            layer: "balanced",
                            rule_id: format!("balanced:u{:x}", source as u32),
                            reason_code: "balanced_default",
                        });
                    }
                    continue;
                }
            }
            if self.inner.char_layer_enabled {
                if let Some(&target) = CHAR_MAP.get(&source) {
                    if target != source {
                        changes.push(CharacterChange {
                            byte_start,
                            byte_end: byte_start + source.len_utf8(),
                            source: source.to_string(),
                            target: target.to_string(),
                            layer: "char",
                            rule_id: format!("charmap:u{:x}", source as u32),
                            reason_code: "char_map",
                        });
                    }
                }
            }
        }
        changes
    }

    /// Convert text and return stable rule events from the same matcher scan.
    pub fn explain(&self, text: &str) -> ExplainResult {
        if text.is_empty() {
            return ExplainResult {
                output: String::new(),
                events: Vec::new(),
            };
        }
        let scan = matcher::scan_detailed(&self.inner.automaton, &self.inner.pattern_table, text);
        let changes = self.character_changes(text, &scan.covered);
        let selected_by_start: HashMap<usize, &matcher::TermHit> = scan
            .selected
            .iter()
            .map(|hit| (hit.byte_start, hit))
            .collect();
        let changes_by_start: HashMap<usize, &CharacterChange> = changes
            .iter()
            .map(|change| (change.byte_start, change))
            .collect();
        let mut spans = vec![(0usize, 0usize); text.len()];
        let mut output = String::with_capacity(text.len());
        let mut input_position = 0usize;
        let mut output_position = 0usize;
        while input_position < text.len() {
            if let Some(hit) = selected_by_start.get(&input_position) {
                let output_end = output_position + hit.target.chars().count();
                for span in spans.iter_mut().take(hit.byte_end).skip(hit.byte_start) {
                    *span = (output_position, output_end);
                }
                output.push_str(&hit.target);
                output_position = output_end;
                input_position = hit.byte_end;
                continue;
            }
            let source = text[input_position..].chars().next().unwrap();
            let byte_end = input_position + source.len_utf8();
            let target = changes_by_start
                .get(&input_position)
                .map_or_else(|| source.to_string(), |change| change.target.clone());
            let output_end = output_position + target.chars().count();
            for span in spans.iter_mut().take(byte_end).skip(input_position) {
                *span = (output_position, output_end);
            }
            output.push_str(&target);
            output_position = output_end;
            input_position = byte_end;
        }
        assert_eq!(
            output,
            self.convert_with_scan(text, &scan.selected, &scan.covered),
            "explain trace diverged from conversion output"
        );

        let byte_to_cp = matcher::build_byte_to_cp(text);
        let mut events = Vec::new();
        for decision in &scan.decisions {
            let hit = &decision.hit;
            let affected = &spans[hit.byte_start..hit.byte_end];
            let output_start = affected.iter().map(|span| span.0).min().unwrap();
            let output_end = affected.iter().map(|span| span.1).max().unwrap();
            let candidates: Vec<_> = self.inner.pattern_table[hit.pattern_index]
                .records
                .iter()
                .filter(|record| record.source_mask & self.inner.source_mask != 0)
                .collect();
            let winner = candidates
                .iter()
                .rev()
                .find(|record| record.target == hit.target);
            let conflicts: Vec<_> = candidates
                .iter()
                .filter(|record| winner.map_or(true, |value| record.id != value.id))
                .collect();
            events.push(ExplainEvent {
                rule_id: winner.map_or_else(
                    || rule_catalog::legacy_custom_rule_id(&hit.source, &hit.target),
                    |record| record.id.clone(),
                ),
                layer: if hit.source == hit.target {
                    "identity".to_string()
                } else {
                    "term".to_string()
                },
                outcome: decision.outcome.to_string(),
                input_start: byte_to_cp[hit.byte_start],
                input_end: byte_to_cp[hit.byte_end],
                output_start,
                output_end,
                source: hit.source.clone(),
                target: hit.target.clone(),
                reason_code: if decision.outcome == "applied" && !conflicts.is_empty() {
                    "loader_conflict_winner".to_string()
                } else {
                    decision.reason_code.to_string()
                },
            });
            if decision.outcome == "applied" {
                for conflict in conflicts {
                    events.push(ExplainEvent {
                        rule_id: conflict.id.clone(),
                        layer: "term".to_string(),
                        outcome: "skipped".to_string(),
                        input_start: byte_to_cp[hit.byte_start],
                        input_end: byte_to_cp[hit.byte_end],
                        output_start,
                        output_end,
                        source: conflict.source.clone(),
                        target: conflict.target.clone(),
                        reason_code: "loader_conflict_loser".to_string(),
                    });
                }
            }
        }
        for change in &changes {
            events.push(ExplainEvent {
                rule_id: change.rule_id.clone(),
                layer: change.layer.to_string(),
                outcome: "applied".to_string(),
                input_start: byte_to_cp[change.byte_start],
                input_end: byte_to_cp[change.byte_end],
                output_start: spans[change.byte_start].0,
                output_end: spans[change.byte_start].1,
                source: change.source.clone(),
                target: change.target.clone(),
                reason_code: change.reason_code.to_string(),
            });
        }
        fn outcome_order(value: &str) -> u8 {
            match value {
                "applied" => 0,
                "protected" => 1,
                _ => 2,
            }
        }
        events.sort_by(|left, right| {
            left.input_start
                .cmp(&right.input_start)
                .then_with(|| left.input_end.cmp(&right.input_end))
                .then_with(|| outcome_order(&left.outcome).cmp(&outcome_order(&right.outcome)))
                .then_with(|| left.rule_id.cmp(&right.rule_id))
        });
        ExplainResult { output, events }
    }
}
