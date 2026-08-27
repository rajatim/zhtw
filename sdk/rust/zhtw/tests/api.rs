use std::collections::HashMap;
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
    let _ = zhtw::explain("test");
    let _ = zhtw::convert_json("{\"value\":\"test\"}").unwrap();
}

#[test]
fn custom_explain_uses_deterministic_legacy_id() {
    let converter = Builder::default()
        .sources([Source::Cn])
        .custom_dict(HashMap::from([(
            "\u{8f6f}\u{4ef6}".to_string(),
            "\u{81ea}\u{8a02}\u{8edf}\u{9ad4}".to_string(),
        )]))
        .build()
        .unwrap();
    let event = converter
        .explain("\u{8f6f}\u{4ef6}")
        .events
        .into_iter()
        .find(|event| event.outcome == "applied")
        .unwrap();
    assert_eq!(event.rule_id, "legacy:cn:custom:6dee1b8fe38334612ee097e8");
}

#[test]
fn custom_explain_is_available_with_hk_only_source() {
    let converter = Builder::default()
        .sources([Source::Hk])
        .custom_dict(HashMap::from([(
            "\u{8f6f}\u{4ef6}".to_string(),
            "\u{81ea}\u{8a02}\u{8edf}\u{9ad4}".to_string(),
        )]))
        .build()
        .unwrap();
    let event = converter
        .explain("\u{8f6f}\u{4ef6}")
        .events
        .into_iter()
        .find(|event| event.outcome == "applied")
        .unwrap();
    assert_eq!(event.rule_id, "legacy:cn:custom:6dee1b8fe38334612ee097e8");
}
