//! Build script: parses zhtw-data.json, generates:
//!   - `generated_maps.rs`  — phf char map + DATA_VERSION const
//!   - `automaton-cnhk.bin` — 28-byte magic header + daachorse serialized automaton
//!   - `pattern-table-cnhk.bin` — pattern table (source/target byte pairs)

use std::collections::HashMap;
use std::env;
use std::fs;
use std::io::Write;
use std::path::PathBuf;

use daachorse::{CharwiseDoubleArrayAhoCorasickBuilder, MatchKind};
use serde::Deserialize;

// ── JSON schema ──────────────────────────────────────────────────────────────

#[derive(Deserialize)]
struct ZhtwData {
    version: String,
    charmap: CharMap,
    terms: Terms,
}

#[derive(Deserialize)]
struct CharMap {
    chars: HashMap<String, String>,
    // `ambiguous` field exists but we don't need it in build
    #[serde(default)]
    ambiguous: Vec<String>,
}

#[allow(dead_code)]
fn _use_ambiguous(_: Vec<String>) {}

#[derive(Deserialize)]
struct Terms {
    cn: HashMap<String, String>,
    hk: HashMap<String, String>,
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
            "/// Version of the embedded zhtw data.\n\
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
                let src_char = src.chars().next()?;
                if src.chars().count() != 1 {
                    return None;
                }
                let tgt_char = tgt.chars().next()?;
                if tgt.chars().count() != 1 {
                    return None;
                }
                Some((src_char, tgt_char))
            })
            .collect();
        char_entries.sort_by_key(|(c, _)| *c as u32);

        for (src_char, tgt_char) in &char_entries {
            map_builder.entry(
                *src_char,
                &format!("'\\u{{{:X}}}'", *tgt_char as u32),
            );
        }

        writeln!(
            f,
            "/// Compile-time char → char map (unambiguous simplified→traditional).\n\
             #[allow(clippy::unreadable_literal)]\n\
             pub(crate) static CHAR_MAP: phf::Map<char, char> = {};",
            map_builder.build()
        )
        .unwrap();
    }

    // ── 4. Build daachorse automaton (cn + hk terms) ─────────────────────────
    //
    // Pattern table: ordered list of (source, target) pairs.
    // Each pattern's u32 value = its index in this table.
    // Sort sources for determinism.

    let mut patterns: Vec<(String, String)> = data
        .terms
        .cn
        .into_iter()
        .chain(data.terms.hk.into_iter())
        .collect();
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
    //     u32 LE: source_len
    //     [u8; source_len]: source UTF-8 bytes
    //     u32 LE: target_len
    //     [u8; target_len]: target UTF-8 bytes
    {
        let out_file = out_dir.join("pattern-table-cnhk.bin");
        let mut f = fs::File::create(&out_file)
            .unwrap_or_else(|e| panic!("build.rs: cannot create pattern-table-cnhk.bin: {}", e));

        let count = patterns.len() as u32;
        f.write_all(&count.to_le_bytes()).unwrap();

        for (src, tgt) in &patterns {
            let src_bytes = src.as_bytes();
            let tgt_bytes = tgt.as_bytes();

            f.write_all(&(src_bytes.len() as u32).to_le_bytes()).unwrap();
            f.write_all(src_bytes).unwrap();
            f.write_all(&(tgt_bytes.len() as u32).to_le_bytes()).unwrap();
            f.write_all(tgt_bytes).unwrap();
        }
    }
}
