#[derive(Debug, thiserror::Error)]
#[non_exhaustive]
pub enum Error {
    #[error("invalid source string: {0}")]
    InvalidSource(String),
    #[error("sources must be a non-empty list of Source variants")]
    EmptySources,
}

pub type Result<T> = std::result::Result<T, Error>;
