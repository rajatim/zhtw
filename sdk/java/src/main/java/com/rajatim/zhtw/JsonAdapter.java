package com.rajatim.zhtw;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;
import java.util.function.Function;
import java.util.regex.Pattern;

/** Exact-byte JSON string-value conversion. */
final class JsonAdapter {
    private static final Pattern NUMBER = Pattern.compile(
            "-?(?:0|[1-9][0-9]*)(?:\\.[0-9]+)?(?:[eE][+-]?[0-9]+)?");

    private JsonAdapter() {}

    static String convert(String text, Function<String, String> converter) {
        if (text == null) return null;
        Scanner originalScanner = new Scanner(text);
        Node original = originalScanner.parse();
        List<Replacement> replacements = new ArrayList<>();
        for (StringToken token : originalScanner.values) {
            String target = converter.apply(token.value);
            if (target == null) {
                throw new JsonAdapterException(
                        "JSON value converter must return a string",
                        "invalid_converter_result");
            }
            if (!target.equals(token.value)) {
                replacements.add(new Replacement(token.start, token.end, quote(target)));
            }
        }
        if (replacements.isEmpty()) return text;

        StringBuilder output = new StringBuilder(text.length());
        int lastEnd = 0;
        for (Replacement replacement : replacements) {
            output.append(text, lastEnd, replacement.start).append(replacement.value);
            lastEnd = replacement.end;
        }
        output.append(text, lastEnd, text.length());
        String convertedText = output.toString();
        Node converted = new Scanner(convertedText).parse();
        if (!original.equals(converted)) {
            throw new JsonAdapterException(
                    "converted JSON changed non-value structure", "structure_changed");
        }
        return convertedText;
    }

    static String quote(String value) {
        validateUnicode(value);
        StringBuilder result = new StringBuilder(value.length() + 2).append('"');
        for (int i = 0; i < value.length(); ) {
            int cp = value.codePointAt(i);
            switch (cp) {
                case '"': result.append("\\\""); break;
                case '\\': result.append("\\\\"); break;
                case '\b': result.append("\\b"); break;
                case '\f': result.append("\\f"); break;
                case '\n': result.append("\\n"); break;
                case '\r': result.append("\\r"); break;
                case '\t': result.append("\\t"); break;
                default:
                    if (cp <= 0x1f) result.append(String.format("\\u%04x", cp));
                    else result.appendCodePoint(cp);
            }
            i += Character.charCount(cp);
        }
        return result.append('"').toString();
    }

    private static void validateUnicode(String value) {
        for (int i = 0; i < value.length(); i++) {
            char current = value.charAt(i);
            if (Character.isHighSurrogate(current)) {
                if (i + 1 >= value.length() || !Character.isLowSurrogate(value.charAt(i + 1))) {
                    throw invalid("JSON contains an unpaired Unicode surrogate");
                }
                i++;
            } else if (Character.isLowSurrogate(current)) {
                throw invalid("JSON contains an unpaired Unicode surrogate");
            }
        }
    }

    private static JsonAdapterException invalid(String message) {
        return new JsonAdapterException(message, "invalid_json");
    }

    private static final class Replacement {
        final int start;
        final int end;
        final String value;

        Replacement(int start, int end, String value) {
            this.start = start;
            this.end = end;
            this.value = value;
        }
    }

    private static final class StringToken {
        final int start;
        final int end;
        final String value;

        StringToken(int start, int end, String value) {
            this.start = start;
            this.end = end;
            this.value = value;
        }
    }

    private static final class Node {
        final String kind;
        final String value;
        final List<Node> children;

        Node(String kind, String value, List<Node> children) {
            this.kind = kind;
            this.value = value;
            this.children = children;
        }

        @Override
        public boolean equals(Object other) {
            if (this == other) return true;
            if (!(other instanceof Node)) return false;
            Node node = (Node) other;
            return Objects.equals(kind, node.kind)
                    && Objects.equals(value, node.value)
                    && Objects.equals(children, node.children);
        }

        @Override
        public int hashCode() { return Objects.hash(kind, value, children); }
    }

    private static final class Scanner {
        final String text;
        final List<StringToken> values = new ArrayList<>();
        int position;

        Scanner(String text) { this.text = text; }

        Node parse() {
            skipWhitespace();
            Node result = parseValue(true);
            skipWhitespace();
            if (position != text.length()) throw invalid("trailing JSON content");
            return result;
        }

        private Node parseValue(boolean collectString) {
            skipWhitespace();
            if (position >= text.length()) throw invalid("missing JSON value");
            char current = text.charAt(position);
            if (current == '"') {
                parseString(collectString);
                return new Node("string", null, List.of());
            }
            if (current == '{') return parseObject();
            if (current == '[') return parseArray();
            int start = position;
            while (position < text.length()
                    && ",]} \t\r\n".indexOf(text.charAt(position)) < 0) position++;
            String primitive = text.substring(start, position);
            if (!(primitive.equals("true") || primitive.equals("false")
                    || primitive.equals("null") || NUMBER.matcher(primitive).matches())) {
                throw invalid("invalid JSON primitive");
            }
            return new Node("primitive", primitive, List.of());
        }

        private Node parseObject() {
            expect('{');
            skipWhitespace();
            List<Node> children = new ArrayList<>();
            Set<String> keys = new HashSet<>();
            if (peek('}')) {
                position++;
                return new Node("object", null, children);
            }
            while (true) {
                skipWhitespace();
                if (!peek('"')) throw invalid("JSON object key must be a string");
                String key = parseString(false);
                if (!keys.add(key)) {
                    throw new JsonAdapterException(
                            "duplicate JSON object key", "duplicate_key");
                }
                skipWhitespace();
                expect(':');
                children.add(new Node("member", key, List.of(parseValue(true))));
                skipWhitespace();
                if (peek('}')) {
                    position++;
                    return new Node("object", null, children);
                }
                expect(',');
            }
        }

        private Node parseArray() {
            expect('[');
            skipWhitespace();
            List<Node> children = new ArrayList<>();
            if (peek(']')) {
                position++;
                return new Node("array", null, children);
            }
            while (true) {
                children.add(parseValue(true));
                skipWhitespace();
                if (peek(']')) {
                    position++;
                    return new Node("array", null, children);
                }
                expect(',');
            }
        }

        private String parseString(boolean collect) {
            int start = position;
            expect('"');
            StringBuilder decoded = new StringBuilder();
            while (position < text.length()) {
                char current = text.charAt(position++);
                if (current == '"') {
                    String value = decoded.toString();
                    validateUnicode(value);
                    if (collect) values.add(new StringToken(start, position, value));
                    return value;
                }
                if (current < 0x20) throw invalid("unescaped JSON control character");
                if (current != '\\') {
                    decoded.append(current);
                    continue;
                }
                if (position >= text.length()) throw invalid("unterminated JSON escape");
                char escaped = text.charAt(position++);
                switch (escaped) {
                    case '"': case '\\': case '/': decoded.append(escaped); break;
                    case 'b': decoded.append('\b'); break;
                    case 'f': decoded.append('\f'); break;
                    case 'n': decoded.append('\n'); break;
                    case 'r': decoded.append('\r'); break;
                    case 't': decoded.append('\t'); break;
                    case 'u':
                        if (position + 4 > text.length()) throw invalid("short Unicode escape");
                        int value = 0;
                        for (int i = 0; i < 4; i++) {
                            int digit = Character.digit(text.charAt(position++), 16);
                            if (digit < 0) throw invalid("invalid Unicode escape");
                            value = value * 16 + digit;
                        }
                        decoded.append((char) value);
                        break;
                    default: throw invalid("invalid JSON escape");
                }
            }
            throw invalid("unterminated JSON string");
        }

        private void skipWhitespace() {
            while (position < text.length()
                    && " \t\r\n".indexOf(text.charAt(position)) >= 0) position++;
        }

        private boolean peek(char expected) {
            return position < text.length() && text.charAt(position) == expected;
        }

        private void expect(char expected) {
            if (!peek(expected)) throw invalid("unexpected JSON token");
            position++;
        }
    }
}
