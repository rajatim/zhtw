package zhtw

import (
	"bytes"
	_ "embed"
	"encoding/json"
	"sync"
)

//go:embed zhtw-data.json
var rawDataJSON []byte

// ── JSON schema ──────────────────────────────────────────────────────────────

type zhtwDataJSON struct {
	SchemaVersion int             `json:"schema_version"`
	Version       string          `json:"version"`
	Stats         json.RawMessage `json:"stats"`
	Charmap       struct {
		Chars                map[string]string   `json:"chars"`
		Ambiguous            []string            `json:"ambiguous"`
		BalancedDefaults     map[string]string   `json:"balanced_defaults"`
		BalancedProtectTerms map[string][]string `json:"balanced_protect_terms"`
	} `json:"charmap"`
	Terms map[string]map[string]string `json:"terms"` // "cn" -> {...}, "hk" -> {...}
}

// ── Parsed data (rune-optimised) ─────────────────────────────────────────────

type parsedData struct {
	version          string
	charMap          map[rune]rune
	balancedDefaults map[rune]rune
	termsCn          map[string]string
	termsHk          map[string]string
}

var (
	dataMu     sync.Once
	globalData *parsedData
)

func getParsedData() *parsedData {
	dataMu.Do(func() {
		globalData = mustParseData(rawDataJSON)
	})
	return globalData
}

func mustParseData(raw []byte) *parsedData {
	var j zhtwDataJSON
	decoder := json.NewDecoder(bytes.NewReader(raw))
	decoder.DisallowUnknownFields()
	if err := decoder.Decode(&j); err != nil {
		panic("zhtw: failed to parse embedded zhtw-data.json: " + err.Error())
	}
	if j.SchemaVersion != 1 {
		panic("zhtw: unsupported embedded data schema version")
	}
	if j.Version == "" || j.Charmap.Chars == nil || j.Charmap.BalancedDefaults == nil || j.Terms == nil {
		panic("zhtw: embedded data is missing required fields")
	}
	for _, value := range j.Charmap.Ambiguous {
		if len([]rune(value)) != 1 {
			panic("zhtw: ambiguous entries must contain one Unicode code point")
		}
	}
	for source := range j.Terms {
		if source != "cn" && source != "hk" {
			panic("zhtw: unsupported term source")
		}
	}

	charMap := make(map[rune]rune, len(j.Charmap.Chars))
	for k, v := range j.Charmap.Chars {
		kr := []rune(k)
		vr := []rune(v)
		if len(kr) != 1 || len(vr) != 1 {
			panic("zhtw: charmap entries must contain one Unicode code point")
		}
		charMap[kr[0]] = vr[0]
	}

	balancedDefaults := make(map[rune]rune, len(j.Charmap.BalancedDefaults))
	for k, v := range j.Charmap.BalancedDefaults {
		kr := []rune(k)
		vr := []rune(v)
		if len(kr) != 1 || len(vr) != 1 {
			panic("zhtw: balanced defaults must contain one Unicode code point")
		}
		balancedDefaults[kr[0]] = vr[0]
	}

	termsCn := j.Terms["cn"]
	if termsCn == nil {
		termsCn = make(map[string]string)
	}
	termsHk := j.Terms["hk"]
	if termsHk == nil {
		termsHk = make(map[string]string)
	}

	return &parsedData{
		version:          j.Version,
		charMap:          charMap,
		balancedDefaults: balancedDefaults,
		termsCn:          termsCn,
		termsHk:          termsHk,
	}
}

// DataVersion returns the version string from the embedded zhtw-data.json.
func DataVersion() string {
	return getParsedData().version
}
