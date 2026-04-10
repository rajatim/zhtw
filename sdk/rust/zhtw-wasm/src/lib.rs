use wasm_bindgen::prelude::*;
use zhtw::{Converter as CoreConverter, Source};

// ─── TypeScript type declarations ───
//
// wasm-bindgen auto-generates `any` for JsValue returns. We suppress those
// with `skip_typescript` and provide correct declarations here.

#[wasm_bindgen(typescript_custom_section)]
const TS_TYPES: &str = r#"
export interface Match {
    start: number;
    end: number;
    source: string;
    target: string;
}

export interface LookupResult {
    input: string;
    output: string;
    changed: boolean;
    details: ConversionDetail[];
}

export interface ConversionDetail {
    source: string;
    target: string;
    layer: "term" | "char";
    position: number;
}

export interface ConverterOptions {
    sources?: ("cn" | "hk")[];
    customDict?: Record<string, string>;
}
"#;

// Manual function/class declarations (replacing the auto-generated `any` ones).
#[wasm_bindgen(typescript_custom_section)]
const TS_API: &str = r#"
export function convert(text: string): string;
export function check(text: string): Match[];
export function lookup(word: string): LookupResult;
export function createConverter(options?: ConverterOptions): Converter;

export class Converter {
    free(): void;
    convert(text: string): string;
    check(text: string): Match[];
    lookup(word: string): LookupResult;
}
"#;

// ─── Zero-config free functions ───

// `convert` returns String → already typed as `string`, but we skip to avoid
// duplicate declaration (we declared it in the custom section above).
#[wasm_bindgen(skip_typescript)]
pub fn convert(text: &str) -> String {
    zhtw::convert(text)
}

#[wasm_bindgen(skip_typescript)]
pub fn check(text: &str) -> Result<JsValue, JsValue> {
    serde_wasm_bindgen::to_value(&zhtw::check(text)).map_err(|e| JsValue::from_str(&e.to_string()))
}

#[wasm_bindgen(skip_typescript)]
pub fn lookup(word: &str) -> Result<JsValue, JsValue> {
    serde_wasm_bindgen::to_value(&zhtw::lookup(word)).map_err(|e| JsValue::from_str(&e.to_string()))
}

// ─── Converter class ───

#[wasm_bindgen(skip_typescript)]
pub struct Converter {
    inner: CoreConverter,
}

#[wasm_bindgen]
impl Converter {
    #[wasm_bindgen(js_name = convert, skip_typescript)]
    pub fn convert(&self, text: &str) -> String {
        self.inner.convert(text)
    }

    #[wasm_bindgen(js_name = check, skip_typescript)]
    pub fn check(&self, text: &str) -> Result<JsValue, JsValue> {
        serde_wasm_bindgen::to_value(&self.inner.check(text))
            .map_err(|e| JsValue::from_str(&e.to_string()))
    }

    #[wasm_bindgen(js_name = lookup, skip_typescript)]
    pub fn lookup(&self, word: &str) -> Result<JsValue, JsValue> {
        serde_wasm_bindgen::to_value(&self.inner.lookup(word))
            .map_err(|e| JsValue::from_str(&e.to_string()))
    }
}

// ─── createConverter factory ───

#[wasm_bindgen(skip_typescript, js_name = createConverter)]
pub fn create_converter(options: Option<JsValue>) -> Result<Converter, JsValue> {
    let mut builder = CoreConverter::builder();

    if let Some(opts) = options {
        if let Ok(sources_val) = js_sys::Reflect::get(&opts, &"sources".into()) {
            if let Some(arr) = sources_val.dyn_ref::<js_sys::Array>() {
                let sources: Vec<Source> = arr
                    .iter()
                    .map(|v| {
                        let s = v.as_string().ok_or_else(|| {
                            JsValue::from_str("sources must be an array of strings")
                        })?;
                        s.parse::<Source>()
                            .map_err(|e| JsValue::from_str(&e.to_string()))
                    })
                    .collect::<Result<Vec<_>, _>>()?;
                builder = builder.sources(sources);
            }
        }

        if let Ok(dict_val) = js_sys::Reflect::get(&opts, &"customDict".into()) {
            if dict_val.is_object() && !dict_val.is_null() && !dict_val.is_undefined() {
                let entries = js_sys::Object::entries(&dict_val.unchecked_into());
                let dict: std::collections::HashMap<String, String> = entries
                    .iter()
                    .filter_map(|entry| {
                        let arr: js_sys::Array = entry.unchecked_into();
                        let k = arr.get(0).as_string()?;
                        let v = arr.get(1).as_string()?;
                        Some((k, v))
                    })
                    .collect();
                builder = builder.custom_dict(dict);
            }
        }
    }

    let inner = builder
        .build()
        .map_err(|e| JsValue::from_str(&format!("zhtw: {e}")))?;
    Ok(Converter { inner })
}
