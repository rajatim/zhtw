use crate::Error;

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum Source {
    Cn,
    Hk,
}

impl std::str::FromStr for Source {
    type Err = Error;
    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        match s {
            "cn" => Ok(Self::Cn),
            "hk" => Ok(Self::Hk),
            _ => Err(Error::InvalidSource(s.to_string())),
        }
    }
}

impl std::fmt::Display for Source {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::Cn => write!(f, "cn"),
            Self::Hk => write!(f, "hk"),
        }
    }
}
