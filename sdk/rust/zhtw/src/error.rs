#[derive(Debug, thiserror::Error)]
#[non_exhaustive]
pub enum Error {
    #[error("invalid source string: {0}")]
    InvalidSource(String),
    #[error("sources must be a non-empty list of Source variants")]
    EmptySources,
    #[error("JSON adapter {code}: {message}")]
    JsonAdapter { code: &'static str, message: String },
}

impl Error {
    pub fn json_code(&self) -> Option<&'static str> {
        match self {
            Self::JsonAdapter { code, .. } => Some(code),
            _ => None,
        }
    }
}

pub type Result<T> = std::result::Result<T, Error>;
