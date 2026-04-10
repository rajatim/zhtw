use zhtw::{Source, Error, Config, Builder};

#[test]
fn source_from_str() {
    assert_eq!("cn".parse::<Source>().unwrap(), Source::Cn);
    assert_eq!("hk".parse::<Source>().unwrap(), Source::Hk);
    assert!(matches!(
        "xx".parse::<Source>(),
        Err(Error::InvalidSource(_))
    ));
}

#[test]
fn config_default_has_cn_hk() {
    let cfg = Config::default();
    assert_eq!(cfg.sources, vec![Source::Cn, Source::Hk]);
    assert!(cfg.custom_dict.is_empty());
}

#[test]
fn builder_default_builds_ok() {
    let result = Builder::default().build();
    assert!(result.is_ok());
}

#[test]
fn builder_empty_sources_rejected() {
    let result = Builder::default()
        .sources(std::iter::empty::<Source>())
        .build();
    assert!(matches!(result, Err(Error::EmptySources)));
}

#[test]
fn builder_custom_dict() {
    let result = Builder::default()
        .custom_dict([("test".to_string(), "測試".to_string())])
        .build();
    assert!(result.is_ok());
}
