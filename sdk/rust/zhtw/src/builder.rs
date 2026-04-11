use crate::config::AmbiguityMode;
use crate::{Config, Result, Source};

#[derive(Debug, Default)]
pub struct Builder {
    config: Config,
}

impl Builder {
    pub fn sources<I: IntoIterator<Item = Source>>(mut self, sources: I) -> Self {
        self.config.sources = sources.into_iter().collect();
        self
    }

    pub fn custom_dict<I, K, V>(mut self, dict: I) -> Self
    where
        I: IntoIterator<Item = (K, V)>,
        K: Into<String>,
        V: Into<String>,
    {
        self.config.custom_dict = dict
            .into_iter()
            .map(|(k, v)| (k.into(), v.into()))
            .collect();
        self
    }

    pub fn ambiguity_mode(mut self, mode: AmbiguityMode) -> Self {
        self.config.ambiguity_mode = mode;
        self
    }

    pub fn build(self) -> Result<crate::Converter> {
        crate::Converter::new(self.config)
    }
}
