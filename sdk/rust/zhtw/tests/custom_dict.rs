use zhtw::{Converter, Source};

#[test]
fn custom_dict_overrides_builtin() {
    let conv = Converter::builder()
        .custom_dict([("自定义", "自訂")])
        .build()
        .unwrap();
    let result = conv.convert("自定义服务器");
    assert!(
        result.contains("自訂"),
        "custom dict should override: got {result}"
    );
    assert!(
        result.contains("伺服器"),
        "built-in should still work: got {result}"
    );
}

#[test]
fn identity_protection_blocks_overlap() {
    let conv = Converter::builder()
        .custom_dict([("文件", "檔案"), ("檔案", "檔案")])
        .build()
        .unwrap();
    let result = conv.convert("無中文檔案");
    assert_eq!(result, "無中文檔案", "identity should protect 檔案");
}

#[test]
fn hk_only_converts_hk_terms_only() {
    let hk = Converter::builder().sources([Source::Hk]).build().unwrap();

    // HK term: 軟件 → 軟體
    assert_eq!(hk.convert("軟件工程師"), "軟體工程師");

    // CN simplified input must NOT be converted — HK-only has no CN terms
    // and char layer is disabled (matches Python behavior).
    assert_eq!(
        hk.convert("软件"),
        "软件",
        "HK-only must not convert CN simplified"
    );
    assert!(
        hk.check("软件").is_empty(),
        "HK-only check must find no matches for CN simplified"
    );
}

#[test]
fn empty_custom_dict_key_is_skipped() {
    // Empty key must not panic — daachorse rejects empty patterns.
    let conv = Converter::builder()
        .custom_dict([("", "x"), ("软件", "軟體")])
        .build()
        .unwrap();
    assert_eq!(conv.convert("软件"), "軟體");
}

#[test]
fn empty_text_returns_empty() {
    assert_eq!(zhtw::convert(""), "");
    assert!(zhtw::check("").is_empty());
    let lookup = zhtw::lookup("");
    assert!(!lookup.changed);
    assert_eq!(lookup.output, "");
}
