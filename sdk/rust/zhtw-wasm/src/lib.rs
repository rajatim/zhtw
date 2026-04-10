use wasm_bindgen::prelude::*;
use zhtw::{Converter as CoreConverter, Source};

// ─── Zero-config free functions ───

#[wasm_bindgen]
pub fn convert(text: &str) -> String {
    zhtw::convert(text)
}

#[wasm_bindgen]
pub fn check(text: &str) -> Result<JsValue, JsValue> {
    serde_wasm_bindgen::to_value(&zhtw::check(text)).map_err(|e| JsValue::from_str(&e.to_string()))
}

#[wasm_bindgen]
pub fn lookup(word: &str) -> Result<JsValue, JsValue> {
    serde_wasm_bindgen::to_value(&zhtw::lookup(word)).map_err(|e| JsValue::from_str(&e.to_string()))
}

// ─── Converter class ───

#[wasm_bindgen]
pub struct Converter {
    inner: CoreConverter,
}

#[wasm_bindgen]
impl Converter {
    #[wasm_bindgen(js_name = convert)]
    pub fn convert(&self, text: &str) -> String {
        self.inner.convert(text)
    }

    #[wasm_bindgen(js_name = check)]
    pub fn check(&self, text: &str) -> Result<JsValue, JsValue> {
        serde_wasm_bindgen::to_value(&self.inner.check(text))
            .map_err(|e| JsValue::from_str(&e.to_string()))
    }

    #[wasm_bindgen(js_name = lookup)]
    pub fn lookup(&self, word: &str) -> Result<JsValue, JsValue> {
        serde_wasm_bindgen::to_value(&self.inner.lookup(word))
            .map_err(|e| JsValue::from_str(&e.to_string()))
    }
}

// ─── createConverter factory ───

#[wasm_bindgen(js_name = createConverter)]
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
