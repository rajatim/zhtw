use crate::Source;
use std::collections::HashMap;

/// Controls how ambiguous characters are handled during conversion.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
pub enum AmbiguityMode {
    /// Skip ambiguous characters entirely (safest, no guessing).
    #[default]
    Strict,
    /// Apply majority-rule defaults for ambiguous characters.
    Balanced,
}

#[derive(Debug, Clone)]
pub struct Config {
    pub sources: Vec<Source>,
    pub custom_dict: HashMap<String, String>,
    pub ambiguity_mode: AmbiguityMode,
}

impl Default for Config {
    fn default() -> Self {
        Self {
            sources: vec![Source::Cn, Source::Hk],
            custom_dict: HashMap::new(),
            ambiguity_mode: AmbiguityMode::Strict,
        }
    }
}
