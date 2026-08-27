package zhtw

import (
	"fmt"
	"reflect"
	"strings"
	"unicode/utf16"
	"unicode/utf8"
)

// JSONAdapterError reports a stable failure code for safe JSON conversion.
type JSONAdapterError struct {
	Code    string
	Message string
}

func (err *JSONAdapterError) Error() string {
	return fmt.Sprintf("zhtw: JSON adapter %s: %s", err.Code, err.Message)
}

type jsonNode struct {
	kind      byte
	primitive string
	array     []jsonNode
	object    []jsonMember
}

type jsonMember struct {
	key   string
	value jsonNode
}

type jsonStringToken struct {
	start int
	end   int
	value string
}

type jsonScanner struct {
	text     string
	position int
	values   []jsonStringToken
}

func (scanner *jsonScanner) parse() (jsonNode, error) {
	scanner.skipWhitespace()
	node, err := scanner.parseValue(true)
	if err != nil {
		return jsonNode{}, err
	}
	scanner.skipWhitespace()
	if scanner.position != len(scanner.text) {
		return jsonNode{}, invalidJSON("trailing JSON content")
	}
	return node, nil
}

func (scanner *jsonScanner) parseValue(collectString bool) (jsonNode, error) {
	scanner.skipWhitespace()
	switch scanner.peekByte() {
	case '"':
		if _, err := scanner.parseString(collectString); err != nil {
			return jsonNode{}, err
		}
		return jsonNode{kind: 's'}, nil
	case '{':
		return scanner.parseObject()
	case '[':
		return scanner.parseArray()
	case 0:
		return jsonNode{}, invalidJSON("missing JSON value")
	default:
		start := scanner.position
		for current := scanner.peekByte(); current != 0 && !strings.ContainsRune(",]} \t\r\n", rune(current)); current = scanner.peekByte() {
			scanner.position++
		}
		primitive := scanner.text[start:scanner.position]
		if primitive != "true" && primitive != "false" && primitive != "null" && !validJSONNumber(primitive) {
			return jsonNode{}, invalidJSON("invalid JSON primitive")
		}
		return jsonNode{kind: 'p', primitive: primitive}, nil
	}
}

func (scanner *jsonScanner) parseObject() (jsonNode, error) {
	if err := scanner.expectByte('{'); err != nil {
		return jsonNode{}, err
	}
	scanner.skipWhitespace()
	members := make([]jsonMember, 0)
	keys := make(map[string]bool)
	if scanner.peekByte() == '}' {
		scanner.position++
		return jsonNode{kind: 'o', object: members}, nil
	}
	for {
		scanner.skipWhitespace()
		if scanner.peekByte() != '"' {
			return jsonNode{}, invalidJSON("JSON object key must be a string")
		}
		key, err := scanner.parseString(false)
		if err != nil {
			return jsonNode{}, err
		}
		if keys[key] {
			return jsonNode{}, jsonAdapterError("duplicate_key", "duplicate JSON object key")
		}
		keys[key] = true
		scanner.skipWhitespace()
		if err := scanner.expectByte(':'); err != nil {
			return jsonNode{}, err
		}
		value, err := scanner.parseValue(true)
		if err != nil {
			return jsonNode{}, err
		}
		members = append(members, jsonMember{key: key, value: value})
		scanner.skipWhitespace()
		if scanner.peekByte() == '}' {
			scanner.position++
			return jsonNode{kind: 'o', object: members}, nil
		}
		if err := scanner.expectByte(','); err != nil {
			return jsonNode{}, err
		}
	}
}

func (scanner *jsonScanner) parseArray() (jsonNode, error) {
	if err := scanner.expectByte('['); err != nil {
		return jsonNode{}, err
	}
	scanner.skipWhitespace()
	values := make([]jsonNode, 0)
	if scanner.peekByte() == ']' {
		scanner.position++
		return jsonNode{kind: 'a', array: values}, nil
	}
	for {
		value, err := scanner.parseValue(true)
		if err != nil {
			return jsonNode{}, err
		}
		values = append(values, value)
		scanner.skipWhitespace()
		if scanner.peekByte() == ']' {
			scanner.position++
			return jsonNode{kind: 'a', array: values}, nil
		}
		if err := scanner.expectByte(','); err != nil {
			return jsonNode{}, err
		}
	}
}

func (scanner *jsonScanner) parseString(collect bool) (string, error) {
	start := scanner.position
	if err := scanner.expectByte('"'); err != nil {
		return "", err
	}
	var decoded strings.Builder
	for scanner.position < len(scanner.text) {
		value, size := utf8.DecodeRuneInString(scanner.text[scanner.position:])
		if value == utf8.RuneError && size == 1 {
			return "", invalidJSON("invalid UTF-8 in JSON string")
		}
		scanner.position += size
		if value == '"' {
			result := decoded.String()
			if collect {
				scanner.values = append(scanner.values, jsonStringToken{start: start, end: scanner.position, value: result})
			}
			return result, nil
		}
		if value < 0x20 {
			return "", invalidJSON("unescaped JSON control character")
		}
		if value != '\\' {
			decoded.WriteRune(value)
			continue
		}
		escaped := scanner.nextByte()
		switch escaped {
		case '"', '\\', '/':
			decoded.WriteByte(escaped)
		case 'b':
			decoded.WriteByte('\b')
		case 'f':
			decoded.WriteByte('\f')
		case 'n':
			decoded.WriteByte('\n')
		case 'r':
			decoded.WriteByte('\r')
		case 't':
			decoded.WriteByte('\t')
		case 'u':
			first, err := scanner.parseHexQuad()
			if err != nil {
				return "", err
			}
			if first >= 0xd800 && first <= 0xdbff {
				if scanner.nextByte() != '\\' || scanner.nextByte() != 'u' {
					return "", invalidJSON("unpaired Unicode surrogate")
				}
				second, err := scanner.parseHexQuad()
				if err != nil || second < 0xdc00 || second > 0xdfff {
					return "", invalidJSON("unpaired Unicode surrogate")
				}
				decoded.WriteRune(utf16.DecodeRune(rune(first), rune(second)))
			} else if first >= 0xdc00 && first <= 0xdfff {
				return "", invalidJSON("unpaired Unicode surrogate")
			} else {
				decoded.WriteRune(rune(first))
			}
		default:
			return "", invalidJSON("invalid JSON escape")
		}
	}
	return "", invalidJSON("unterminated JSON string")
}

func (scanner *jsonScanner) parseHexQuad() (uint16, error) {
	var value uint16
	for i := 0; i < 4; i++ {
		current := scanner.nextByte()
		var digit byte
		switch {
		case current >= '0' && current <= '9':
			digit = current - '0'
		case current >= 'a' && current <= 'f':
			digit = current - 'a' + 10
		case current >= 'A' && current <= 'F':
			digit = current - 'A' + 10
		default:
			return 0, invalidJSON("invalid Unicode escape")
		}
		value = value*16 + uint16(digit)
	}
	return value, nil
}

func (scanner *jsonScanner) skipWhitespace() {
	for strings.ContainsRune(" \t\r\n", rune(scanner.peekByte())) {
		scanner.position++
	}
}

func (scanner *jsonScanner) peekByte() byte {
	if scanner.position >= len(scanner.text) {
		return 0
	}
	return scanner.text[scanner.position]
}

func (scanner *jsonScanner) nextByte() byte {
	value := scanner.peekByte()
	if value != 0 {
		scanner.position++
	}
	return value
}

func (scanner *jsonScanner) expectByte(expected byte) error {
	if scanner.nextByte() != expected {
		return invalidJSON("unexpected JSON token")
	}
	return nil
}

func (c *Converter) ConvertJSON(text string) (string, error) {
	originalScanner := jsonScanner{text: text}
	original, err := originalScanner.parse()
	if err != nil {
		return "", err
	}
	type replacement struct {
		start, end int
		value      string
	}
	replacements := make([]replacement, 0)
	for _, token := range originalScanner.values {
		target := c.Convert(token.value)
		if target != token.value {
			replacements = append(replacements, replacement{token.start, token.end, quoteJSONString(target)})
		}
	}
	if len(replacements) == 0 {
		return text, nil
	}
	var output strings.Builder
	output.Grow(len(text))
	lastEnd := 0
	for _, replacement := range replacements {
		output.WriteString(text[lastEnd:replacement.start])
		output.WriteString(replacement.value)
		lastEnd = replacement.end
	}
	output.WriteString(text[lastEnd:])
	convertedText := output.String()
	convertedScanner := jsonScanner{text: convertedText}
	converted, err := convertedScanner.parse()
	if err != nil {
		return "", err
	}
	if !reflect.DeepEqual(original, converted) {
		return "", jsonAdapterError("structure_changed", "converted JSON changed non-value structure")
	}
	return convertedText, nil
}

func quoteJSONString(value string) string {
	var output strings.Builder
	output.Grow(len(value) + 2)
	output.WriteByte('"')
	for _, current := range value {
		switch current {
		case '"':
			output.WriteString(`\"`)
		case '\\':
			output.WriteString(`\\`)
		case '\b':
			output.WriteString(`\b`)
		case '\f':
			output.WriteString(`\f`)
		case '\n':
			output.WriteString(`\n`)
		case '\r':
			output.WriteString(`\r`)
		case '\t':
			output.WriteString(`\t`)
		default:
			if current < 0x20 {
				fmt.Fprintf(&output, `\u%04x`, current)
			} else {
				output.WriteRune(current)
			}
		}
	}
	output.WriteByte('"')
	return output.String()
}

func validJSONNumber(value string) bool {
	position := 0
	if position < len(value) && value[position] == '-' {
		position++
	}
	if position >= len(value) {
		return false
	}
	if value[position] == '0' {
		position++
	} else if value[position] >= '1' && value[position] <= '9' {
		for position < len(value) && value[position] >= '0' && value[position] <= '9' {
			position++
		}
	} else {
		return false
	}
	if position < len(value) && value[position] == '.' {
		position++
		start := position
		for position < len(value) && value[position] >= '0' && value[position] <= '9' {
			position++
		}
		if position == start {
			return false
		}
	}
	if position < len(value) && (value[position] == 'e' || value[position] == 'E') {
		position++
		if position < len(value) && (value[position] == '+' || value[position] == '-') {
			position++
		}
		start := position
		for position < len(value) && value[position] >= '0' && value[position] <= '9' {
			position++
		}
		if position == start {
			return false
		}
	}
	return position == len(value)
}

func invalidJSON(message string) error {
	return jsonAdapterError("invalid_json", message)
}

func jsonAdapterError(code, message string) error {
	return &JSONAdapterError{Code: code, Message: message}
}
