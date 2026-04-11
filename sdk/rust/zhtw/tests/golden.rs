//! Byte-for-byte parity with Python CLI, Java SDK, and TypeScript SDK.
//! Reads sdk/data/golden-test.json via include_str! (workspace-relative path).

use serde::Deserialize;
use std::collections::HashMap;
use zhtw::{Converter, Source};

#[derive(Deserialize)]
struct GoldenFile {
    version: String,
    convert: Vec<ConvertCase>,
    check: Vec<CheckCase>,
    lookup: Vec<LookupCase>,
}

#[derive(Deserialize)]
struct ConvertCase {
    input: String,
    sources: Vec<String>,
    expected: String,
    #[serde(default)]
    custom_dict: Option<HashMap<String, String>>,
    #[serde(default)]
    ambiguity_mode: Option<String>,
}

#[derive(Deserialize)]
struct CheckCase {
    input: String,
    sources: Vec<String>,
    expected_matches: Vec<ExpectedMatch>,
    #[serde(default)]
    ambiguity_mode: Option<String>,
}

#[derive(Debug, Deserialize)]
struct ExpectedMatch {
    start: usize,
    end: usize,
    source: String,
    target: String,
}

#[derive(Deserialize)]
struct LookupCase {
    input: String,
    sources: Vec<String>,
    expected_output: String,
    expected_changed: bool,
    expected_details: Vec<ExpectedDetail>,
}

#[derive(Deserialize)]
struct ExpectedDetail {
    source: String,
    target: String,
    layer: String,
    position: usize,
}

const GOLDEN_JSON: &str = include_str!("../../../data/golden-test.json");

fn build_converter(sources: &[String], custom_dict: Option<&HashMap<String, String>>) -> Converter {
    let sources: Vec<Source> = sources
        .iter()
        .map(|s| s.parse().expect("known source"))
        .collect();
    let mut builder = Converter::builder().sources(sources);
    if let Some(dict) = custom_dict {
        builder = builder.custom_dict(dict.clone());
    }
    builder.build().expect("builder should succeed")
}

#[test]
fn golden_version_matches_crate() {
    let golden: GoldenFile = serde_json::from_str(GOLDEN_JSON).unwrap();
    assert_eq!(
        golden.version,
        env!("CARGO_PKG_VERSION"),
        "golden-test.json version ({}) != Cargo.toml version ({}) — mono-versioning broken",
        golden.version,
        env!("CARGO_PKG_VERSION"),
    );
}

#[test]
fn convert_parity() {
    let golden: GoldenFile = serde_json::from_str(GOLDEN_JSON).unwrap();
    let mut failures = Vec::new();

    for (idx, case) in golden.convert.iter().enumerate() {
        // SDK does not implement balanced mode yet — skip those cases.
        if case.ambiguity_mode.as_deref() == Some("balanced") {
            continue;
        }
        let conv = build_converter(&case.sources, case.custom_dict.as_ref());
        let actual = conv.convert(&case.input);
        if actual != case.expected {
            failures.push(format!(
                "[{}] input={:?}\n  expected={:?}\n  actual  ={:?}",
                idx, case.input, case.expected, actual
            ));
        }
    }

    assert!(
        failures.is_empty(),
        "convert parity failed ({} cases):\n{}",
        failures.len(),
        failures.join("\n")
    );
}

#[test]
fn check_parity() {
    let golden: GoldenFile = serde_json::from_str(GOLDEN_JSON).unwrap();
    let mut failures = Vec::new();

    for (idx, case) in golden.check.iter().enumerate() {
        // SDK does not implement balanced mode yet — skip those cases.
        if case.ambiguity_mode.as_deref() == Some("balanced") {
            continue;
        }
        let conv = build_converter(&case.sources, None);
        let actual = conv.check(&case.input);

        if actual.len() != case.expected_matches.len() {
            failures.push(format!(
                "[{}] input={:?}: match count mismatch (expected {}, got {})\n  expected={:?}\n  actual={:?}",
                idx, case.input, case.expected_matches.len(), actual.len(),
                case.expected_matches, actual
            ));
            continue;
        }
        for (j, (exp, act)) in case.expected_matches.iter().zip(actual.iter()).enumerate() {
            if exp.start != act.start
                || exp.end != act.end
                || exp.source != act.source
                || exp.target != act.target
            {
                failures.push(format!(
                    "[{}.{}] input={:?}: match mismatch\n  expected=({},{},{:?},{:?})\n  actual  =({},{},{:?},{:?})",
                    idx, j, case.input,
                    exp.start, exp.end, exp.source, exp.target,
                    act.start, act.end, act.source, act.target,
                ));
            }
        }
    }

    assert!(
        failures.is_empty(),
        "check parity failed ({} cases):\n{}",
        failures.len(),
        failures.join("\n")
    );
}

#[test]
fn lookup_parity() {
    let golden: GoldenFile = serde_json::from_str(GOLDEN_JSON).unwrap();
    let mut failures = Vec::new();

    for (idx, case) in golden.lookup.iter().enumerate() {
        let conv = build_converter(&case.sources, None);
        let actual = conv.lookup(&case.input);

        if actual.output != case.expected_output {
            failures.push(format!(
                "[{}] input={:?}: output mismatch (expected {:?}, got {:?})",
                idx, case.input, case.expected_output, actual.output
            ));
        }
        if actual.changed != case.expected_changed {
            failures.push(format!(
                "[{}] input={:?}: changed mismatch (expected {}, got {})",
                idx, case.input, case.expected_changed, actual.changed
            ));
        }
        if actual.details.len() != case.expected_details.len() {
            failures.push(format!(
                "[{}] input={:?}: detail count mismatch ({} vs {})",
                idx,
                case.input,
                case.expected_details.len(),
                actual.details.len()
            ));
            continue;
        }
        for (j, (exp, act)) in case
            .expected_details
            .iter()
            .zip(actual.details.iter())
            .enumerate()
        {
            let exp_layer = &exp.layer;
            let act_layer = match act.layer {
                zhtw::Layer::Term => "term",
                zhtw::Layer::Char => "char",
            };
            if exp.source != act.source
                || exp.target != act.target
                || exp_layer != act_layer
                || exp.position != act.position
            {
                failures.push(format!(
                    "[{}.{}] input={:?}: detail mismatch\n  expected=({:?},{:?},{},{})  actual=({:?},{:?},{},{})",
                    idx, j, case.input,
                    exp.source, exp.target, exp.layer, exp.position,
                    act.source, act.target, act_layer, act.position,
                ));
            }
        }
    }

    assert!(
        failures.is_empty(),
        "lookup parity failed ({} cases):\n{}",
        failures.len(),
        failures.join("\n")
    );
}
