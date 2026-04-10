use zhtw::{Builder, Config, Error, Source};

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
        .custom_dict([("test".to_string(), "\u{6e2c}\u{8a66}".to_string())])
        .build();
    assert!(result.is_ok());
}

// zhtw:disable
#[test]
fn convert_basic() {
    let result = zhtw::convert("软件测试");
    assert_eq!(result, "\u{8edf}\u{9ad4}\u{6e2c}\u{8a66}");
}

#[test]
fn check_basic() {
    let hits = zhtw::check("软件测试");
    assert!(!hits.is_empty());
    let first = &hits[0];
    assert_eq!(first.source, "软件");
    assert_eq!(first.target, "\u{8edf}\u{9ad4}");
}

#[test]
fn lookup_basic() {
    let result = zhtw::lookup("软件");
    assert!(result.changed);
    assert_eq!(result.output, "\u{8edf}\u{9ad4}");
}
// zhtw:enable

#[test]
fn default_instance_is_send_sync() {
    fn assert_send_sync<T: Send + Sync>() {}
    assert_send_sync::<zhtw::Converter>();
}

#[test]
fn free_functions_delegate_to_default() {
    let _ = zhtw::convert("test");
    let _ = zhtw::check("test");
    let _ = zhtw::lookup("test");
}
