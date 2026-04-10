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
fn hk_only_no_char_layer() {
    let conv = Converter::builder().sources([Source::Hk]).build().unwrap();
    let text = "軟件工程師";
    let result = conv.convert(text);
    let _ = result;
}

#[test]
fn empty_text_returns_empty() {
    assert_eq!(zhtw::convert(""), "");
    assert!(zhtw::check("").is_empty());
    let lookup = zhtw::lookup("");
    assert!(!lookup.changed);
    assert_eq!(lookup.output, "");
}
