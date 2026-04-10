use crate::{Config, Error, Result};

pub struct Converter {
    _config: Config,
}

impl Converter {
    pub fn new(config: Config) -> Result<Self> {
        if config.sources.is_empty() {
            return Err(Error::EmptySources);
        }
        Ok(Self { _config: config })
    }

    pub fn builder() -> crate::Builder {
        crate::Builder::default()
    }
}
