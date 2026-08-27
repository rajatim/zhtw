//! Build script: parses zhtw-data.json, generates:
//!   - `generated_maps.rs`  — phf char map + DATA_VERSION const
//!   - `automaton-cnhk.bin` — 28-byte magic header + daachorse serialized automaton
//!   - `pattern-table-cnhk.bin` — pattern table (source/target byte pairs)

use std::collections::{HashMap, HashSet};
use std::env;
use std::fs;
use std::io::Write;
use std::path::PathBuf;

use daachorse::{CharwiseDoubleArrayAhoCorasickBuilder, MatchKind};
use serde::Deserialize;

// ── JSON schema ──────────────────────────────────────────────────────────────

#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
struct ZhtwData {
    schema_version: u32,
    version: String,
    #[allow(dead_code)]
    stats: Stats,
    charmap: CharMap,
    terms: Terms,
    #[serde(default)]
    rule_catalog: Option<RuleCatalog>,
}

#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
#[allow(dead_code)]
struct Stats {
    charmap_count: usize,
    ambiguous_count: usize,
    terms_cn_count: usize,
    terms_hk_count: usize,
    #[serde(default)]
    rule_catalog_count: Option<usize>,
}

#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
struct CharMap {
    chars: HashMap<String, String>,
    // `ambiguous` field exists but we don't need it in build
    #[serde(default)]
    ambiguous: Vec<String>,
    #[serde(default)]
    balanced_defaults: HashMap<String, String>,
    #[allow(dead_code)]
    balanced_protect_terms: HashMap<String, Vec<String>>,
}

#[allow(dead_code)]
fn _use_ambiguous(_: Vec<String>) {}

#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
struct Terms {
    cn: HashMap<String, String>,
    hk: HashMap<String, String>,
}

#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
struct RuleCatalog {
    format: String,
    groups: Vec<RuleGroup>,
}

#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
struct RuleGroup {
    source_locale: String,
    rule_class: String,
    domain: String,
    trust_level: String,
    priority: i32,
    context: Vec<String>,
    evidence_source: Option<String>,
    review_status: String,
    rules: indexmap::IndexMap<String, [String; 2]>,
}

fn valid_rule_id(value: &str) -> bool {
    let bytes = value.as_bytes();
    if !(3..=128).contains(&bytes.len()) {
        return false;
    }
    (bytes[0].is_ascii_lowercase() || bytes[0].is_ascii_digit())
        && bytes[1..].iter().all(|byte| {
            byte.is_ascii_lowercase() || byte.is_ascii_digit() || b"._:-".contains(byte)
        })
}

fn validate_rule_catalog(data: &ZhtwData) {
    match (data.schema_version, data.rule_catalog.as_ref()) {
        (1, None) => return,
        (2, Some(_)) => {}
        _ => panic!("build.rs: rule catalog does not match schema version"),
    }
    let catalog = data.rule_catalog.as_ref().unwrap();
    assert_eq!(
        catalog.format, "grouped-v1",
        "build.rs: invalid rule catalog format"
    );
    let expected_count = data
        .stats
        .rule_catalog_count
        .expect("build.rs: missing rule catalog count");
    let mut ids = HashSet::new();
    let mut approved = HashSet::new();
    let mut count = 0usize;
    for group in &catalog.groups {
        assert!(
            matches!(group.source_locale.as_str(), "cn" | "hk")
                && matches!(
                    group.rule_class.as_str(),
                    "bulk" | "generated_guard" | "curated" | "custom"
                )
                && matches!(
                    group.domain.as_str(),
                    "general"
                        | "business"
                        | "daily"
                        | "ecommerce"
                        | "education"
                        | "finance"
                        | "formal"
                        | "gaming"
                        | "geography"
                        | "it"
                        | "legal"
                        | "medical"
                        | "social"
                        | "ui"
                )
                && matches!(
                    group.trust_level.as_str(),
                    "imported" | "generated" | "curated" | "custom"
                )
                && (-1000..=1000).contains(&group.priority)
                && matches!(
                    group.review_status.as_str(),
                    "pending" | "approved" | "rejected"
                ),
            "build.rs: invalid rule catalog group"
        );
        let mut context = HashSet::new();
        assert!(
            group
                .context
                .iter()
                .all(|value| !value.is_empty() && context.insert(value)),
            "build.rs: invalid rule catalog context"
        );
        assert!(
            group
                .evidence_source
                .as_ref()
                .map_or(true, |value| !value.is_empty()),
            "build.rs: invalid rule catalog evidence"
        );
        assert!(
            group.review_status != "approved" || group.evidence_source.is_some(),
            "build.rs: approved rule catalog group requires evidence"
        );
        for (id, pair) in &group.rules {
            assert!(
                valid_rule_id(id) && ids.insert(id) && !pair[0].is_empty() && !pair[1].is_empty(),
                "build.rs: duplicate or invalid rule catalog entry"
            );
            count += 1;
            if group.review_status == "approved" {
                approved.insert((
                    group.source_locale.as_str(),
                    pair[0].as_str(),
                    pair[1].as_str(),
                ));
            }
        }
    }
    assert_eq!(
        count, expected_count,
        "build.rs: rule catalog count mismatch"
    );
    for (locale, terms) in [("cn", &data.terms.cn), ("hk", &data.terms.hk)] {
        for (source, target) in terms {
            assert!(
                approved.contains(&(locale, source.as_str(), target.as_str())),
                "build.rs: rule catalog does not cover effective terms"
            );
        }
    }
}

// ── Magic header constants ────────────────────────────────────────────────────

const MAGIC: &[u8; 8] = b"ZHTWDAAC";
const HEADER_VERSION: u16 = 1;
const DAACHORSE_VERSION_PACKED: u32 = 0x0001_0000; // 1.0.0
const HEADER_LEN: usize = 28;
const SOURCE_MASK_CN_HK: u8 = 0b11;

fn build_header(dict_hash: [u8; 8]) -> [u8; HEADER_LEN] {
    let mut buf = [0u8; HEADER_LEN];
    buf[0..8].copy_from_slice(MAGIC);
    buf[8..10].copy_from_slice(&HEADER_VERSION.to_le_bytes());
    buf[10..14].copy_from_slice(&DAACHORSE_VERSION_PACKED.to_le_bytes());
    buf[14..22].copy_from_slice(&dict_hash);
    buf[22] = SOURCE_MASK_CN_HK;
    // buf[23..28] stays 0 (reserved)
    buf
}

// ── Main ─────────────────────────────────────────────────────────────────────

fn main() {
    let manifest_dir = PathBuf::from(env::var("CARGO_MANIFEST_DIR").unwrap());
    let data_path = manifest_dir.join("data").join("zhtw-data.json");
    let out_dir = PathBuf::from(env::var("OUT_DIR").unwrap());

    // Tell Cargo to re-run if the JSON changes.
    println!("cargo:rerun-if-changed={}", data_path.display());

    // ── 1. Read + parse JSON ─────────────────────────────────────────────────
    let json_bytes = fs::read(&data_path)
        .unwrap_or_else(|e| panic!("build.rs: cannot read {}: {}", data_path.display(), e));

    let data: ZhtwData = serde_json::from_slice(&json_bytes)
        .unwrap_or_else(|e| panic!("build.rs: cannot parse {}: {}", data_path.display(), e));
    assert!(
        matches!(data.schema_version, 1 | 2),
        "build.rs: unsupported zhtw data schema version"
    );
    validate_rule_catalog(&data);
    assert!(
        !data.version.is_empty(),
        "build.rs: missing zhtw data version"
    );

    // ── 2. blake3 hash of the raw JSON bytes (first 8 bytes) ─────────────────
    let hash_full = blake3::hash(&json_bytes);
    let hash_bytes: [u8; 8] = hash_full.as_bytes()[..8].try_into().unwrap();

    // ── 3. Generate generated_maps.rs (phf char map + DATA_VERSION) ──────────
    {
        let out_file = out_dir.join("generated_maps.rs");
        let mut f = fs::File::create(&out_file)
            .unwrap_or_else(|e| panic!("build.rs: cannot create generated_maps.rs: {}", e));

        // DATA_VERSION const
        writeln!(
            f,
            "#[allow(dead_code)]\n\
             /// Version of the embedded zhtw data.\n\
             pub(crate) const DATA_VERSION: &str = \"{}\";",
            data.version
        )
        .unwrap();
        writeln!(f).unwrap();

        // PHF char map: only unambiguous entries in charmap.chars
        let ambiguous_set: std::collections::HashSet<&str> =
            data.charmap.ambiguous.iter().map(String::as_str).collect();

        let mut map_builder = phf_codegen::Map::<char>::new();

        // Collect and sort for determinism
        let mut char_entries: Vec<(char, char)> = data
            .charmap
            .chars
            .iter()
            .filter_map(|(src, tgt)| {
                // Skip ambiguous chars and multi-char keys/values
                if ambiguous_set.contains(src.as_str()) {
                    return None;
                }
                assert_eq!(src.chars().count(), 1, "charmap key must be one code point");
                assert_eq!(
                    tgt.chars().count(),
                    1,
                    "charmap value must be one code point"
                );
                let src_char = src.chars().next().unwrap();
                let tgt_char = tgt.chars().next().unwrap();
                Some((src_char, tgt_char))
            })
            .collect();
        char_entries.sort_by_key(|(c, _)| *c as u32);

        // phf_codegen 0.13+ borrows the value &str, so we must own the
        // formatted strings until build() is called.
        let char_values: Vec<String> = char_entries
            .iter()
            .map(|(_, tgt_char)| format!("'\\u{{{:X}}}'", *tgt_char as u32))
            .collect();
        for ((src_char, _), value) in char_entries.iter().zip(char_values.iter()) {
            map_builder.entry(*src_char, value);
        }

        writeln!(
            f,
            "/// Compile-time char → char map (unambiguous simplified→traditional).\n\
             #[allow(clippy::unreadable_literal)]\n\
             pub(crate) static CHAR_MAP: phf::Map<char, char> = {};",
            map_builder.build()
        )
        .unwrap();

        // PHF balanced defaults map: ambiguous chars with clear majority mappings
        let mut balanced_entries: Vec<(char, char)> = data
            .charmap
            .balanced_defaults
            .iter()
            .map(|(src, tgt)| {
                assert_eq!(
                    src.chars().count(),
                    1,
                    "balanced key must be one code point"
                );
                assert_eq!(
                    tgt.chars().count(),
                    1,
                    "balanced value must be one code point"
                );
                let src_char = src.chars().next().unwrap();
                let tgt_char = tgt.chars().next().unwrap();
                (src_char, tgt_char)
            })
            .collect();
        balanced_entries.sort_by_key(|(c, _)| *c as u32);

        let mut balanced_builder = phf_codegen::Map::<char>::new();
        let balanced_values: Vec<String> = balanced_entries
            .iter()
            .map(|(_, tgt_char)| format!("'\\u{{{:X}}}'", *tgt_char as u32))
            .collect();
        for ((src_char, _), value) in balanced_entries.iter().zip(balanced_values.iter()) {
            balanced_builder.entry(*src_char, value);
        }

        writeln!(f).unwrap();
        writeln!(
            f,
            "/// Balanced-mode defaults: ambiguous chars with clear majority mappings.\n\
             #[allow(clippy::unreadable_literal)]\n\
             pub(crate) static BALANCED_DEFAULTS: phf::Map<char, char> = {};",
            balanced_builder.build()
        )
        .unwrap();
    }

    // ── 4. Build daachorse automaton (cn + hk terms) ─────────────────────────
    //
    // Pattern table: ordered list of (source, target) pairs.
    // Each pattern's u32 value = its index in this table.
    // Sort sources for determinism.

    // Track which source(s) each term key comes from.
    // CN = 0b01, HK = 0b10, both = 0b11.
    let mut source_masks: HashMap<String, u8> = HashMap::new();
    for key in data.terms.cn.keys() {
        *source_masks.entry(key.clone()).or_insert(0) |= 0b01;
    }
    for key in data.terms.hk.keys() {
        *source_masks.entry(key.clone()).or_insert(0) |= 0b10;
    }

    // Keep approved rule IDs beside each runtime pattern. This avoids embedding
    // and parsing the full shared JSON in Rust/WASM at runtime just for explain().
    let mut rule_records: HashMap<String, Vec<(String, u8, String)>> = HashMap::new();
    if let Some(catalog) = &data.rule_catalog {
        for group in &catalog.groups {
            if group.review_status != "approved" {
                continue;
            }
            let locale_mask = match group.source_locale.as_str() {
                "cn" => 0b01,
                "hk" => 0b10,
                _ => unreachable!("catalog locale was validated"),
            };
            for (id, pair) in &group.rules {
                rule_records.entry(pair[0].clone()).or_default().push((
                    id.clone(),
                    locale_mask,
                    pair[1].clone(),
                ));
            }
        }
    }

    let mut patterns: Vec<(String, String)> =
        data.terms.cn.into_iter().chain(data.terms.hk).collect();
    patterns.sort_by(|(a, _), (b, _)| a.cmp(b));
    patterns.dedup_by(|(a, _), (b, _)| a == b); // remove exact duplicates

    // Build pattern-value pairs for daachorse
    let patvals: Vec<(&str, u32)> = patterns
        .iter()
        .enumerate()
        .map(|(i, (src, _))| (src.as_str(), i as u32))
        .collect();

    let automaton = CharwiseDoubleArrayAhoCorasickBuilder::new()
        .match_kind(MatchKind::Standard)
        .build_with_values(patvals)
        .unwrap_or_else(|e| panic!("build.rs: daachorse build failed: {}", e));

    let automaton_bytes = automaton.serialize();

    // ── 5. Write automaton-cnhk.bin ──────────────────────────────────────────
    {
        let out_file = out_dir.join("automaton-cnhk.bin");
        let mut f = fs::File::create(&out_file)
            .unwrap_or_else(|e| panic!("build.rs: cannot create automaton-cnhk.bin: {}", e));

        let header = build_header(hash_bytes);
        f.write_all(&header).unwrap();
        f.write_all(&automaton_bytes).unwrap();
    }

    // ── 6. Write pattern-table-cnhk.bin ──────────────────────────────────────
    //
    // Format:
    //   u32 LE: count
    //   For each entry:
    //     u8: source_mask (0b01=CN, 0b10=HK, 0b11=both)
    //     u32 LE: source_len
    //     [u8; source_len]: source UTF-8 bytes
    //     u32 LE: target_len
    //     [u8; target_len]: target UTF-8 bytes
    //     u32 LE: approved rule record count
    //     For each record: locale mask + ID bytes + target bytes
    {
        let out_file = out_dir.join("pattern-table-cnhk.bin");
        let mut f = fs::File::create(&out_file)
            .unwrap_or_else(|e| panic!("build.rs: cannot create pattern-table-cnhk.bin: {}", e));

        let count = patterns.len() as u32;
        f.write_all(&count.to_le_bytes()).unwrap();

        for (src, tgt) in &patterns {
            let mask = source_masks.get(src).copied().unwrap_or(0b11);
            f.write_all(&[mask]).unwrap();

            let src_bytes = src.as_bytes();
            let tgt_bytes = tgt.as_bytes();

            f.write_all(&(src_bytes.len() as u32).to_le_bytes())
                .unwrap();
            f.write_all(src_bytes).unwrap();
            f.write_all(&(tgt_bytes.len() as u32).to_le_bytes())
                .unwrap();
            f.write_all(tgt_bytes).unwrap();

            let records = rule_records.get(src).map(Vec::as_slice).unwrap_or(&[]);
            f.write_all(&(records.len() as u32).to_le_bytes()).unwrap();
            for (id, locale_mask, record_target) in records {
                f.write_all(&[*locale_mask]).unwrap();
                f.write_all(&(id.len() as u32).to_le_bytes()).unwrap();
                f.write_all(id.as_bytes()).unwrap();
                f.write_all(&(record_target.len() as u32).to_le_bytes())
                    .unwrap();
                f.write_all(record_target.as_bytes()).unwrap();
            }
        }
    }
}
