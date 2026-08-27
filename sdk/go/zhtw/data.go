package zhtw

import (
	"bytes"
	_ "embed"
	"encoding/json"
	"errors"
	"regexp"
	"sync"
)

//go:embed zhtw-data.json
var rawDataJSON []byte

// ── JSON schema ──────────────────────────────────────────────────────────────

type zhtwDataJSON struct {
	SchemaVersion int    `json:"schema_version"`
	Version       string `json:"version"`
	Stats         struct {
		CharmapCount     int  `json:"charmap_count"`
		AmbiguousCount   int  `json:"ambiguous_count"`
		TermsCnCount     int  `json:"terms_cn_count"`
		TermsHkCount     int  `json:"terms_hk_count"`
		RuleCatalogCount *int `json:"rule_catalog_count,omitempty"`
	} `json:"stats"`
	Charmap struct {
		Chars                map[string]string   `json:"chars"`
		Ambiguous            []string            `json:"ambiguous"`
		BalancedDefaults     map[string]string   `json:"balanced_defaults"`
		BalancedProtectTerms map[string][]string `json:"balanced_protect_terms"`
	} `json:"charmap"`
	Terms       map[string]map[string]string `json:"terms"` // "cn" -> {...}, "hk" -> {...}
	RuleCatalog *ruleCatalogJSON             `json:"rule_catalog,omitempty"`
}

type ruleCatalogJSON struct {
	Format string          `json:"format"`
	Groups []ruleGroupJSON `json:"groups"`
}

type ruleGroupJSON struct {
	SourceLocale string           `json:"source_locale"`
	RuleClass    string           `json:"rule_class"`
	Domain       string           `json:"domain"`
	TrustLevel   string           `json:"trust_level"`
	Priority     int              `json:"priority"`
	Context      []string         `json:"context"`
	Evidence     *string          `json:"evidence_source"`
	ReviewStatus string           `json:"review_status"`
	Rules        orderedRulePairs `json:"rules"`
}

type orderedRulePair struct {
	id   string
	pair []string
}

type orderedRulePairs struct {
	present bool
	entries []orderedRulePair
}

func (rules *orderedRulePairs) UnmarshalJSON(raw []byte) error {
	decoder := json.NewDecoder(bytes.NewReader(raw))
	token, err := decoder.Token()
	if err != nil || token != json.Delim('{') {
		return errors.New("zhtw: rule pairs must be a JSON object")
	}
	rules.present = true
	rules.entries = make([]orderedRulePair, 0)
	for decoder.More() {
		key, err := decoder.Token()
		if err != nil {
			return err
		}
		var pair []string
		if err := decoder.Decode(&pair); err != nil {
			return err
		}
		rules.entries = append(rules.entries, orderedRulePair{id: key.(string), pair: pair})
	}
	_, err = decoder.Token()
	return err
}

// ── Parsed data (rune-optimised) ─────────────────────────────────────────────

type parsedData struct {
	version          string
	charMap          map[rune]rune
	balancedDefaults map[rune]rune
	termsCn          map[string]string
	termsHk          map[string]string
	ruleRecords      map[Source]map[string][]ruleMeta
}

type ruleMeta struct {
	id     string
	source string
	target string
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
	if j.SchemaVersion != 1 && j.SchemaVersion != 2 {
		panic("zhtw: unsupported embedded data schema version")
	}
	if (j.SchemaVersion == 1 && j.RuleCatalog != nil) ||
		(j.SchemaVersion == 2 && j.RuleCatalog == nil) {
		panic("zhtw: rule catalog does not match embedded data schema version")
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
	if j.SchemaVersion == 2 {
		validateRuleCatalog(&j)
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
	ruleRecords := map[Source]map[string][]ruleMeta{
		SourceCn: make(map[string][]ruleMeta),
		SourceHk: make(map[string][]ruleMeta),
	}
	if j.RuleCatalog != nil {
		for _, group := range j.RuleCatalog.Groups {
			if group.ReviewStatus != "approved" {
				continue
			}
			locale := Source(group.SourceLocale)
			for _, entry := range group.Rules.entries {
				record := ruleMeta{id: entry.id, source: entry.pair[0], target: entry.pair[1]}
				ruleRecords[locale][record.source] = append(ruleRecords[locale][record.source], record)
			}
		}
	}

	return &parsedData{
		version:          j.Version,
		charMap:          charMap,
		balancedDefaults: balancedDefaults,
		termsCn:          termsCn,
		termsHk:          termsHk,
		ruleRecords:      ruleRecords,
	}
}

var ruleIDPattern = regexp.MustCompile(`^[a-z0-9][a-z0-9._:-]{2,127}$`)

func validateRuleCatalog(data *zhtwDataJSON) {
	catalog := data.RuleCatalog
	if catalog.Format != "grouped-v1" || catalog.Groups == nil ||
		data.Stats.RuleCatalogCount == nil {
		panic("zhtw: invalid rule catalog envelope")
	}
	allowedClass := map[string]bool{"bulk": true, "generated_guard": true, "curated": true, "custom": true}
	allowedTrust := map[string]bool{"imported": true, "generated": true, "curated": true, "custom": true}
	allowedReview := map[string]bool{"pending": true, "approved": true, "rejected": true}
	allowedDomain := map[string]bool{
		"general": true, "business": true, "daily": true, "ecommerce": true,
		"education": true, "finance": true, "formal": true, "gaming": true,
		"geography": true, "it": true, "legal": true, "medical": true,
		"social": true, "ui": true,
	}
	ids := make(map[string]bool)
	approved := make(map[string]bool)
	count := 0
	for _, group := range catalog.Groups {
		if (group.SourceLocale != "cn" && group.SourceLocale != "hk") ||
			!allowedClass[group.RuleClass] || !allowedDomain[group.Domain] ||
			!allowedTrust[group.TrustLevel] || !allowedReview[group.ReviewStatus] ||
			group.Priority < -1000 || group.Priority > 1000 || group.Context == nil ||
			!group.Rules.present {
			panic("zhtw: invalid rule catalog group")
		}
		context := make(map[string]bool)
		for _, value := range group.Context {
			if value == "" || context[value] {
				panic("zhtw: invalid rule catalog context")
			}
			context[value] = true
		}
		if group.Evidence != nil && *group.Evidence == "" {
			panic("zhtw: invalid rule catalog evidence")
		}
		if group.ReviewStatus == "approved" && group.Evidence == nil {
			panic("zhtw: approved rule catalog group requires evidence")
		}
		for _, entry := range group.Rules.entries {
			id, pair := entry.id, entry.pair
			if !ruleIDPattern.MatchString(id) || ids[id] || len(pair) != 2 ||
				pair[0] == "" || pair[1] == "" {
				panic("zhtw: duplicate or invalid rule catalog entry")
			}
			ids[id] = true
			count++
			if group.ReviewStatus == "approved" {
				approved[group.SourceLocale+"\x00"+pair[0]+"\x00"+pair[1]] = true
			}
		}
	}
	if count != *data.Stats.RuleCatalogCount {
		panic("zhtw: rule catalog count does not match stats")
	}
	for locale, terms := range data.Terms {
		for source, target := range terms {
			if !approved[locale+"\x00"+source+"\x00"+target] {
				panic("zhtw: rule catalog does not cover effective terms")
			}
		}
	}
}

// DataVersion returns the version string from the embedded zhtw-data.json.
func DataVersion() string {
	return getParsedData().version
}
