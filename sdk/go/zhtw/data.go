package zhtw

import (
	_ "embed"
	"encoding/json"
	"sync"
)

//go:embed zhtw-data.json
var rawDataJSON []byte

// ── JSON schema ──────────────────────────────────────────────────────────────

type zhtwDataJSON struct {
	Version string `json:"version"`
	Charmap struct {
		Chars            map[string]string `json:"chars"`
		Ambiguous        []string          `json:"ambiguous"`
		BalancedDefaults map[string]string `json:"balanced_defaults"`
	} `json:"charmap"`
	Terms map[string]map[string]string `json:"terms"` // "cn" -> {...}, "hk" -> {...}
}

// ── Parsed data (rune-optimised) ─────────────────────────────────────────────

type parsedData struct {
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
	if err := json.Unmarshal(raw, &j); err != nil {
		panic("zhtw: failed to parse embedded zhtw-data.json: " + err.Error())
	}

	charMap := make(map[rune]rune, len(j.Charmap.Chars))
	for k, v := range j.Charmap.Chars {
		kr := []rune(k)
		vr := []rune(v)
		if len(kr) == 1 && len(vr) == 1 {
			charMap[kr[0]] = vr[0]
		}
	}

	balancedDefaults := make(map[rune]rune, len(j.Charmap.BalancedDefaults))
	for k, v := range j.Charmap.BalancedDefaults {
		kr := []rune(k)
		vr := []rune(v)
		if len(kr) == 1 && len(vr) == 1 {
			balancedDefaults[kr[0]] = vr[0]
		}
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
		charMap:          charMap,
		balancedDefaults: balancedDefaults,
		termsCn:          termsCn,
		termsHk:          termsHk,
	}
}
