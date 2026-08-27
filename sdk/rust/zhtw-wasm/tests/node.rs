// zhtw:disable - WASM test inputs intentionally use Simplified Chinese
use wasm_bindgen_test::*;

#[wasm_bindgen_test]
fn explain_and_json_bindings_run_in_wasm() {
    let json = zhtw_wasm::convert_json("{\"key\":\"软件\"}").unwrap();
    assert_eq!(json, "{\"key\":\"軟體\"}");
    assert!(zhtw_wasm::explain("软件").is_ok());

    let converter = zhtw_wasm::create_converter(None).unwrap();
    assert_eq!(
        converter.convert_json("{\"value\":\"软件\"}").unwrap(),
        "{\"value\":\"軟體\"}"
    );
    assert!(converter.explain("软件").is_ok());
}
