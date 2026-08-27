using System;
using System.Collections.Generic;
using System.Globalization;
using System.Text;

namespace Zhtw
{
    public sealed class JsonAdapterException : Exception
    {
        public string Code { get; }

        internal JsonAdapterException(string code, string message)
            : base("zhtw JSON adapter " + code + ": " + message)
        {
            Code = code;
        }
    }

    internal static class JsonAdapter
    {
        private sealed class Node
        {
            internal char Kind;
            internal string Primitive;
            internal List<Node> Array;
            internal List<Member> Object;

            internal bool SameStructure(Node other)
            {
                if (other == null || Kind != other.Kind || Primitive != other.Primitive) return false;
                if (Array != null)
                {
                    if (other.Array == null || Array.Count != other.Array.Count) return false;
                    for (int i = 0; i < Array.Count; i++)
                        if (!Array[i].SameStructure(other.Array[i])) return false;
                }
                if (Object != null)
                {
                    if (other.Object == null || Object.Count != other.Object.Count) return false;
                    for (int i = 0; i < Object.Count; i++)
                    {
                        if (Object[i].Key != other.Object[i].Key ||
                            !Object[i].Value.SameStructure(other.Object[i].Value)) return false;
                    }
                }
                return true;
            }
        }

        private sealed class Member
        {
            internal string Key;
            internal Node Value;
        }

        private sealed class StringToken
        {
            internal int Start;
            internal int End;
            internal string Value;
        }

        private sealed class Scanner
        {
            private readonly string _text;
            private int _position;
            internal List<StringToken> Values { get; } = new List<StringToken>();

            internal Scanner(string text)
            {
                _text = text ?? throw new ArgumentNullException(nameof(text));
            }

            internal Node Parse()
            {
                SkipWhitespace();
                Node node = ParseValue(true);
                SkipWhitespace();
                if (_position != _text.Length) throw Invalid("trailing JSON content");
                return node;
            }

            private Node ParseValue(bool collectString)
            {
                SkipWhitespace();
                char current = Peek();
                if (current == '"')
                {
                    ParseString(collectString);
                    return new Node { Kind = 's' };
                }
                if (current == '{') return ParseObject();
                if (current == '[') return ParseArray();
                if (current == '\0') throw Invalid("missing JSON value");
                int start = _position;
                while (_position < _text.Length &&
                    ",]} \t\r\n".IndexOf(_text[_position]) < 0) _position++;
                string primitive = _text.Substring(start, _position - start);
                if (primitive != "true" && primitive != "false" && primitive != "null" &&
                    !ValidNumber(primitive)) throw Invalid("invalid JSON primitive");
                return new Node { Kind = 'p', Primitive = primitive };
            }

            private Node ParseObject()
            {
                Expect('{');
                SkipWhitespace();
                var members = new List<Member>();
                var keys = new HashSet<string>(StringComparer.Ordinal);
                if (Peek() == '}')
                {
                    _position++;
                    return new Node { Kind = 'o', Object = members };
                }
                while (true)
                {
                    SkipWhitespace();
                    if (Peek() != '"') throw Invalid("JSON object key must be a string");
                    string key = ParseString(false);
                    if (!keys.Add(key)) throw Error("duplicate_key", "duplicate JSON object key");
                    SkipWhitespace();
                    Expect(':');
                    members.Add(new Member { Key = key, Value = ParseValue(true) });
                    SkipWhitespace();
                    if (Peek() == '}')
                    {
                        _position++;
                        return new Node { Kind = 'o', Object = members };
                    }
                    Expect(',');
                }
            }

            private Node ParseArray()
            {
                Expect('[');
                SkipWhitespace();
                var values = new List<Node>();
                if (Peek() == ']')
                {
                    _position++;
                    return new Node { Kind = 'a', Array = values };
                }
                while (true)
                {
                    values.Add(ParseValue(true));
                    SkipWhitespace();
                    if (Peek() == ']')
                    {
                        _position++;
                        return new Node { Kind = 'a', Array = values };
                    }
                    Expect(',');
                }
            }

            private string ParseString(bool collect)
            {
                int start = _position;
                Expect('"');
                var decoded = new StringBuilder();
                while (_position < _text.Length)
                {
                    char current = _text[_position++];
                    if (current == '"')
                    {
                        string value = decoded.ToString();
                        if (collect) Values.Add(new StringToken { Start = start, End = _position, Value = value });
                        return value;
                    }
                    if (current < 0x20) throw Invalid("unescaped JSON control character");
                    if (current != '\\')
                    {
                        if (char.IsHighSurrogate(current))
                        {
                            if (_position >= _text.Length || !char.IsLowSurrogate(_text[_position]))
                                throw Invalid("unpaired Unicode surrogate");
                            decoded.Append(current);
                            decoded.Append(_text[_position++]);
                        }
                        else
                        {
                            if (char.IsLowSurrogate(current)) throw Invalid("unpaired Unicode surrogate");
                            decoded.Append(current);
                        }
                        continue;
                    }
                    char escaped = Next();
                    switch (escaped)
                    {
                        case '"': decoded.Append('"'); break;
                        case '\\': decoded.Append('\\'); break;
                        case '/': decoded.Append('/'); break;
                        case 'b': decoded.Append('\b'); break;
                        case 'f': decoded.Append('\f'); break;
                        case 'n': decoded.Append('\n'); break;
                        case 'r': decoded.Append('\r'); break;
                        case 't': decoded.Append('\t'); break;
                        case 'u':
                            char first = (char)ParseHexQuad();
                            if (char.IsHighSurrogate(first))
                            {
                                if (Next() != '\\' || Next() != 'u')
                                    throw Invalid("unpaired Unicode surrogate");
                                char second = (char)ParseHexQuad();
                                if (!char.IsLowSurrogate(second))
                                    throw Invalid("unpaired Unicode surrogate");
                                decoded.Append(first).Append(second);
                            }
                            else
                            {
                                if (char.IsLowSurrogate(first)) throw Invalid("unpaired Unicode surrogate");
                                decoded.Append(first);
                            }
                            break;
                        default: throw Invalid("invalid JSON escape");
                    }
                }
                throw Invalid("unterminated JSON string");
            }

            private int ParseHexQuad()
            {
                int value = 0;
                for (int i = 0; i < 4; i++)
                {
                    char current = Next();
                    int digit;
                    if (current >= '0' && current <= '9') digit = current - '0';
                    else if (current >= 'a' && current <= 'f') digit = current - 'a' + 10;
                    else if (current >= 'A' && current <= 'F') digit = current - 'A' + 10;
                    else throw Invalid("invalid Unicode escape");
                    value = value * 16 + digit;
                }
                return value;
            }

            private void SkipWhitespace()
            {
                while (_position < _text.Length && " \t\r\n".IndexOf(_text[_position]) >= 0)
                    _position++;
            }

            private char Peek() => _position < _text.Length ? _text[_position] : '\0';

            private char Next()
            {
                if (_position >= _text.Length) throw Invalid("unexpected end of JSON");
                return _text[_position++];
            }

            private void Expect(char expected)
            {
                if (Next() != expected) throw Invalid("unexpected JSON token");
            }
        }

        internal static string ConvertValues(Converter converter, string text)
        {
            var originalScanner = new Scanner(text);
            Node original = originalScanner.Parse();
            var output = new StringBuilder(text.Length);
            int lastEnd = 0;
            bool changed = false;
            foreach (var token in originalScanner.Values)
            {
                string target = converter.Convert(token.Value);
                if (target == token.Value) continue;
                output.Append(text, lastEnd, token.Start - lastEnd);
                output.Append(QuoteString(target));
                lastEnd = token.End;
                changed = true;
            }
            if (!changed) return text;
            output.Append(text, lastEnd, text.Length - lastEnd);
            string convertedText = output.ToString();
            Node converted = new Scanner(convertedText).Parse();
            if (!original.SameStructure(converted))
                throw Error("structure_changed", "converted JSON changed non-value structure");
            return convertedText;
        }

        internal static string QuoteString(string value)
        {
            var output = new StringBuilder(value.Length + 2);
            output.Append('"');
            for (int i = 0; i < value.Length; i++)
            {
                char current = value[i];
                switch (current)
                {
                    case '"': output.Append("\\\""); break;
                    case '\\': output.Append("\\\\"); break;
                    case '\b': output.Append("\\b"); break;
                    case '\f': output.Append("\\f"); break;
                    case '\n': output.Append("\\n"); break;
                    case '\r': output.Append("\\r"); break;
                    case '\t': output.Append("\\t"); break;
                    default:
                        if (current < 0x20)
                            output.Append("\\u").Append(((int)current).ToString("x4", CultureInfo.InvariantCulture));
                        else
                            output.Append(current);
                        break;
                }
            }
            output.Append('"');
            return output.ToString();
        }

        private static bool ValidNumber(string value)
        {
            int position = 0;
            if (position < value.Length && value[position] == '-') position++;
            if (position >= value.Length) return false;
            if (value[position] == '0') position++;
            else if (value[position] >= '1' && value[position] <= '9')
            {
                while (position < value.Length && IsAsciiDigit(value[position])) position++;
            }
            else return false;
            if (position < value.Length && value[position] == '.')
            {
                position++;
                int start = position;
                while (position < value.Length && IsAsciiDigit(value[position])) position++;
                if (position == start) return false;
            }
            if (position < value.Length && (value[position] == 'e' || value[position] == 'E'))
            {
                position++;
                if (position < value.Length && (value[position] == '+' || value[position] == '-')) position++;
                int start = position;
                while (position < value.Length && IsAsciiDigit(value[position])) position++;
                if (position == start) return false;
            }
            return position == value.Length;
        }

        private static bool IsAsciiDigit(char value) => value >= '0' && value <= '9';

        private static JsonAdapterException Invalid(string message) =>
            Error("invalid_json", message);

        private static JsonAdapterException Error(string code, string message) =>
            new JsonAdapterException(code, message);
    }
}
