use crate::Source;
use std::collections::HashMap;

#[derive(Debug, Clone)]
pub struct Config {
    pub sources: Vec<Source>,
    pub custom_dict: HashMap<String, String>,
}

impl Default for Config {
    fn default() -> Self {
        Self {
            sources: vec![Source::Cn, Source::Hk],
            custom_dict: HashMap::new(),
        }
    }
}
