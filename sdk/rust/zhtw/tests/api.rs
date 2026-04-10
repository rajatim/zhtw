use zhtw::{Source, Error, Config};

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
