//! Traditional Chinese converter for Taiwan — Rust SDK.
//!
//! Part of the [rajatim/zhtw](https://github.com/rajatim/zhtw) monorepo.

mod builder;
mod config;
mod converter;
mod error;
mod generated;
mod header;
mod json_adapter;
mod matcher;
mod rule_catalog;
mod source;

pub use builder::Builder;
pub use config::{AmbiguityMode, Config};
pub use converter::{
    ConversionDetail, Converter, ExplainEvent, ExplainResult, Layer, LookupResult, Match,
};
pub use error::{Error, Result};
pub use source::Source;

/// Convert simplified Chinese text to Traditional Chinese (Taiwan) using the
/// default instance (Cn+Hk sources, char layer enabled).
pub fn convert(text: &str) -> String {
    Converter::default_instance().convert(text)
}

/// Convert only JSON string values using the default converter.
pub fn convert_json(text: &str) -> Result<String> {
    Converter::default_instance().convert_json(text)
}

/// Check text for simplified Chinese terms/characters using the default instance.
pub fn check(text: &str) -> Vec<Match> {
    Converter::default_instance().check(text)
}

/// Look up a word/phrase using the default instance.
pub fn lookup(word: &str) -> LookupResult {
    Converter::default_instance().lookup(word)
}

/// Explain a conversion using the default converter.
pub fn explain(text: &str) -> ExplainResult {
    Converter::default_instance().explain(text)
}
