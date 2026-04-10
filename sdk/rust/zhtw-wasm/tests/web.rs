use wasm_bindgen_test::*;
wasm_bindgen_test_configure!(run_in_browser);

#[wasm_bindgen_test]
fn convert_smoke() {
    let result = zhtw_wasm::convert("软件测试");
    assert_eq!(result, "軟體測試");
}

#[wasm_bindgen_test]
fn create_converter_default() {
    let conv = zhtw_wasm::create_converter(None).unwrap();
    let result = conv.convert("软件");
    assert_eq!(result, "軟體");
}
