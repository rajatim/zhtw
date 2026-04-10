use crate::{Config, Result, Source};

#[derive(Debug)]
pub struct Builder {
    config: Config,
}

impl Default for Builder {
    fn default() -> Self {
        Self {
            config: Config::default(),
        }
    }
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

    pub fn build(self) -> Result<crate::Converter> {
        crate::Converter::new(self.config)
    }
}
