//! Traditional Chinese converter for Taiwan — Rust SDK.
//!
//! Part of the [rajatim/zhtw](https://github.com/rajatim/zhtw) monorepo.

mod source;
mod error;
mod config;

pub use source::Source;
pub use error::{Error, Result};
pub use config::Config;
