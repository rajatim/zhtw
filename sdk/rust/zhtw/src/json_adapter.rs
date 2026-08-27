use crate::error::{Error, Result};

#[derive(Debug, PartialEq, Eq)]
enum Node {
    StringValue,
    Primitive(String),
    Array(Vec<Node>),
    Object(Vec<(String, Node)>),
}

struct StringToken {
    start: usize,
    end: usize,
    value: String,
}

struct Scanner<'a> {
    text: &'a str,
    position: usize,
    values: Vec<StringToken>,
}

impl<'a> Scanner<'a> {
    fn new(text: &'a str) -> Self {
        Self {
            text,
            position: 0,
            values: Vec::new(),
        }
    }

    fn parse(&mut self) -> Result<Node> {
        self.skip_whitespace();
        let node = self.parse_value(true)?;
        self.skip_whitespace();
        if self.position != self.text.len() {
            return Err(invalid("trailing JSON content"));
        }
        Ok(node)
    }

    fn parse_value(&mut self, collect_string: bool) -> Result<Node> {
        self.skip_whitespace();
        match self.peek_byte() {
            Some(b'"') => {
                self.parse_string(collect_string)?;
                Ok(Node::StringValue)
            }
            Some(b'{') => self.parse_object(),
            Some(b'[') => self.parse_array(),
            Some(_) => {
                let start = self.position;
                while let Some(byte) = self.peek_byte() {
                    if b",]} \t\r\n".contains(&byte) {
                        break;
                    }
                    self.position += 1;
                }
                let primitive = &self.text[start..self.position];
                if !matches!(primitive, "true" | "false" | "null") && !valid_number(primitive) {
                    return Err(invalid("invalid JSON primitive"));
                }
                Ok(Node::Primitive(primitive.to_string()))
            }
            None => Err(invalid("missing JSON value")),
        }
    }

    fn parse_object(&mut self) -> Result<Node> {
        self.expect_byte(b'{')?;
        self.skip_whitespace();
        let mut members = Vec::new();
        let mut keys = std::collections::HashSet::new();
        if self.peek_byte() == Some(b'}') {
            self.position += 1;
            return Ok(Node::Object(members));
        }
        loop {
            self.skip_whitespace();
            if self.peek_byte() != Some(b'"') {
                return Err(invalid("JSON object key must be a string"));
            }
            let key = self.parse_string(false)?;
            if !keys.insert(key.clone()) {
                return Err(adapter_error("duplicate_key", "duplicate JSON object key"));
            }
            self.skip_whitespace();
            self.expect_byte(b':')?;
            members.push((key, self.parse_value(true)?));
            self.skip_whitespace();
            if self.peek_byte() == Some(b'}') {
                self.position += 1;
                return Ok(Node::Object(members));
            }
            self.expect_byte(b',')?;
        }
    }

    fn parse_array(&mut self) -> Result<Node> {
        self.expect_byte(b'[')?;
        self.skip_whitespace();
        let mut values = Vec::new();
        if self.peek_byte() == Some(b']') {
            self.position += 1;
            return Ok(Node::Array(values));
        }
        loop {
            values.push(self.parse_value(true)?);
            self.skip_whitespace();
            if self.peek_byte() == Some(b']') {
                self.position += 1;
                return Ok(Node::Array(values));
            }
            self.expect_byte(b',')?;
        }
    }

    fn parse_string(&mut self, collect: bool) -> Result<String> {
        let start = self.position;
        self.expect_byte(b'"')?;
        let mut decoded = String::new();
        while self.position < self.text.len() {
            let ch = self.text[self.position..].chars().next().unwrap();
            self.position += ch.len_utf8();
            if ch == '"' {
                if collect {
                    self.values.push(StringToken {
                        start,
                        end: self.position,
                        value: decoded.clone(),
                    });
                }
                return Ok(decoded);
            }
            if ch <= '\u{1f}' {
                return Err(invalid("unescaped JSON control character"));
            }
            if ch != '\\' {
                decoded.push(ch);
                continue;
            }
            let escaped = self
                .next_byte()
                .ok_or_else(|| invalid("unterminated JSON escape"))?;
            match escaped {
                b'"' => decoded.push('"'),
                b'\\' => decoded.push('\\'),
                b'/' => decoded.push('/'),
                b'b' => decoded.push('\u{8}'),
                b'f' => decoded.push('\u{c}'),
                b'n' => decoded.push('\n'),
                b'r' => decoded.push('\r'),
                b't' => decoded.push('\t'),
                b'u' => {
                    let first = self.parse_hex_quad()?;
                    let codepoint = if (0xd800..=0xdbff).contains(&first) {
                        if self.next_byte() != Some(b'\\') || self.next_byte() != Some(b'u') {
                            return Err(invalid("unpaired Unicode surrogate"));
                        }
                        let second = self.parse_hex_quad()?;
                        if !(0xdc00..=0xdfff).contains(&second) {
                            return Err(invalid("unpaired Unicode surrogate"));
                        }
                        0x10000 + (((first - 0xd800) as u32) << 10) + (second - 0xdc00) as u32
                    } else if (0xdc00..=0xdfff).contains(&first) {
                        return Err(invalid("unpaired Unicode surrogate"));
                    } else {
                        first as u32
                    };
                    decoded
                        .push(char::from_u32(codepoint).ok_or_else(|| invalid("invalid Unicode"))?);
                }
                _ => return Err(invalid("invalid JSON escape")),
            }
        }
        Err(invalid("unterminated JSON string"))
    }

    fn parse_hex_quad(&mut self) -> Result<u16> {
        let mut value = 0u16;
        for _ in 0..4 {
            let byte = self
                .next_byte()
                .ok_or_else(|| invalid("short Unicode escape"))?;
            let digit = (byte as char)
                .to_digit(16)
                .ok_or_else(|| invalid("invalid Unicode escape"))?;
            value = value * 16 + digit as u16;
        }
        Ok(value)
    }

    fn skip_whitespace(&mut self) {
        while self
            .peek_byte()
            .is_some_and(|byte| b" \t\r\n".contains(&byte))
        {
            self.position += 1;
        }
    }

    fn peek_byte(&self) -> Option<u8> {
        self.text.as_bytes().get(self.position).copied()
    }

    fn next_byte(&mut self) -> Option<u8> {
        let value = self.peek_byte()?;
        self.position += 1;
        Some(value)
    }

    fn expect_byte(&mut self, expected: u8) -> Result<()> {
        if self.next_byte() != Some(expected) {
            return Err(invalid("unexpected JSON token"));
        }
        Ok(())
    }
}

pub(crate) fn convert_json_values(
    text: &str,
    converter: impl Fn(&str) -> String,
) -> Result<String> {
    let mut original_scanner = Scanner::new(text);
    let original = original_scanner.parse()?;
    let mut replacements = Vec::new();
    for token in original_scanner.values {
        let target = converter(&token.value);
        if target != token.value {
            replacements.push((token.start, token.end, quote(&target)));
        }
    }
    if replacements.is_empty() {
        return Ok(text.to_string());
    }
    let mut output = String::with_capacity(text.len());
    let mut last_end = 0;
    for (start, end, replacement) in replacements {
        output.push_str(&text[last_end..start]);
        output.push_str(&replacement);
        last_end = end;
    }
    output.push_str(&text[last_end..]);
    let converted = Scanner::new(&output).parse()?;
    if converted != original {
        return Err(adapter_error(
            "structure_changed",
            "converted JSON changed non-value structure",
        ));
    }
    Ok(output)
}

pub(crate) fn quote(value: &str) -> String {
    let mut output = String::with_capacity(value.len() + 2);
    output.push('"');
    for ch in value.chars() {
        match ch {
            '"' => output.push_str("\\\""),
            '\\' => output.push_str("\\\\"),
            '\u{8}' => output.push_str("\\b"),
            '\u{c}' => output.push_str("\\f"),
            '\n' => output.push_str("\\n"),
            '\r' => output.push_str("\\r"),
            '\t' => output.push_str("\\t"),
            ch if ch <= '\u{1f}' => output.push_str(&format!("\\u{:04x}", ch as u32)),
            ch => output.push(ch),
        }
    }
    output.push('"');
    output
}

fn valid_number(value: &str) -> bool {
    let bytes = value.as_bytes();
    let mut i = 0;
    if bytes.get(i) == Some(&b'-') {
        i += 1;
    }
    match bytes.get(i) {
        Some(b'0') => i += 1,
        Some(b'1'..=b'9') => {
            i += 1;
            while bytes.get(i).is_some_and(u8::is_ascii_digit) {
                i += 1;
            }
        }
        _ => return false,
    }
    if bytes.get(i) == Some(&b'.') {
        i += 1;
        let start = i;
        while bytes.get(i).is_some_and(u8::is_ascii_digit) {
            i += 1;
        }
        if i == start {
            return false;
        }
    }
    if matches!(bytes.get(i), Some(b'e' | b'E')) {
        i += 1;
        if matches!(bytes.get(i), Some(b'+' | b'-')) {
            i += 1;
        }
        let start = i;
        while bytes.get(i).is_some_and(u8::is_ascii_digit) {
            i += 1;
        }
        if i == start {
            return false;
        }
    }
    i == bytes.len()
}

fn invalid(message: &str) -> Error {
    adapter_error("invalid_json", message)
}

fn adapter_error(code: &'static str, message: &str) -> Error {
    Error::JsonAdapter {
        code,
        message: message.to_string(),
    }
}
