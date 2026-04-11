package zhtw

import "sync"

var (
	defaultOnce sync.Once
	defaultConv *Converter
)

func getDefault() *Converter {
	defaultOnce.Do(func() {
		data := getParsedData()
		conv, err := buildConverter(data, []Source{SourceCn, SourceHk}, nil, AmbiguityStrict)
		if err != nil {
			panic("zhtw: failed to build default converter: " + err.Error())
		}
		defaultConv = conv
	})
	return defaultConv
}

// Convert converts simplified Chinese text to Traditional Chinese (Taiwan)
// using the default converter (Cn+Hk sources, Strict mode).
// Thread-safe; the default converter is lazily initialised with sync.Once.
func Convert(text string) string {
	return getDefault().Convert(text)
}

// Check scans text for simplified Chinese terms/characters using the default
// converter and returns match information.
func Check(text string) []Match {
	return getDefault().Check(text)
}

// Lookup returns detailed conversion information for a single word or phrase
// using the default converter.
func Lookup(word string) LookupResult {
	return getDefault().Lookup(word)
}
