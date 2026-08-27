// zhtw:disable - WASM test inputs intentionally use Simplified Chinese
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

#[wasm_bindgen_test]
fn explain_and_json_smoke() {
    let json = zhtw_wasm::convert_json("{\"key\":\"软件\"}").unwrap();
    assert_eq!(json, "{\"key\":\"軟體\"}");
    assert!(zhtw_wasm::explain("软件").is_ok());
}
