//! Verify all public API indices are Unicode codepoints, not UTF-8 bytes.

#[test]
fn check_returns_codepoint_not_byte_index() {
    // "中 X 软件" — 6 codepoints, 12 bytes
    //   codepoint offsets: 中=0, ' '=1, X=2, ' '=3, 软=4, 件=5
    //   byte offsets:      中=0, ' '=3, X=4, ' '=5, 软=6, 件=9
    let text = "中 X 软件";
    let term = zhtw::check(text)
        .into_iter()
        .find(|m| m.source == "软件")
        .expect("软件 term match");
    assert_eq!(term.start, 4, "must be codepoint (4), not byte (6)");
    assert_eq!(term.end, 6, "must be codepoint (6), not byte (12)");
    assert_eq!(term.target, "軟體");
}

#[test]
fn lookup_position_is_codepoint() {
    // "中文a软件" — 5 codepoints, 13 bytes
    //   codepoint offsets: 中=0, 文=1, a=2, 软=3, 件=4
    let result = zhtw::lookup("中文a软件");
    let term = result
        .details
        .iter()
        .find(|d| d.source == "软件")
        .expect("软件 term detail");
    assert_eq!(term.position, 3, "must be codepoint (3), not byte (7)");
    assert_eq!(term.target, "軟體");
}

#[test]
fn supplementary_plane_chars() {
    // "𠮷软件" — 3 codepoints, 10 bytes
    //   𠮷 = U+20BB7 (4 UTF-8 bytes, 1 codepoint)
    let text = "𠮷软件";
    let term = zhtw::check(text)
        .into_iter()
        .find(|m| m.source == "软件")
        .expect("软件 term match");
    assert_eq!(term.start, 1, "must be codepoint (1), not byte (4)");
    assert_eq!(term.end, 3, "must be codepoint (3), not byte (10)");
}
