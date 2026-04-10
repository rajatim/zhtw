//! Traditional Chinese converter for Taiwan — Rust SDK.
//!
//! Part of the [rajatim/zhtw](https://github.com/rajatim/zhtw) monorepo.

mod source;
mod error;
mod config;
mod builder;
mod converter;
mod header;
mod matcher;
mod generated;

pub use source::Source;
pub use error::{Error, Result};
pub use config::Config;
pub use builder::Builder;
pub use converter::{Converter, Match, LookupResult, ConversionDetail, Layer};

/// Convert simplified Chinese text to Traditional Chinese (Taiwan) using the
/// default instance (Cn+Hk sources, char layer enabled).
pub fn convert(text: &str) -> String {
    Converter::default_instance().convert(text)
}

/// Check text for simplified Chinese terms/characters using the default instance.
pub fn check(text: &str) -> Vec<Match> {
    Converter::default_instance().check(text)
}

/// Look up a word/phrase using the default instance.
pub fn lookup(word: &str) -> LookupResult {
    Converter::default_instance().lookup(word)
}
