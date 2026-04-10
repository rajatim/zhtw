//! Re-exports of build.rs generated artifacts.

include!(concat!(env!("OUT_DIR"), "/generated_maps.rs"));

/// Precompiled automaton bytes (header + daachorse serialized data) for Cn+Hk.
pub(crate) static AUTOMATON_CNHK_BYTES: &[u8] =
    include_bytes!(concat!(env!("OUT_DIR"), "/automaton-cnhk.bin"));

/// Precompiled pattern table for Cn+Hk.
pub(crate) static PATTERN_TABLE_CNHK_BYTES: &[u8] =
    include_bytes!(concat!(env!("OUT_DIR"), "/pattern-table-cnhk.bin"));
