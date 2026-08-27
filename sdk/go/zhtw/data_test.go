package zhtw

import "testing"

func TestSchemaV1StillLoads(t *testing.T) {
	raw := []byte(`{
  "schema_version": 1,
  "version": "1.2.3",
  "stats": {},
  "charmap": {
    "chars": {},
    "ambiguous": [],
    "balanced_defaults": {},
    "balanced_protect_terms": {}
  },
  "terms": {"cn": {}, "hk": {}}
}`)

	if parsed := mustParseData(raw); parsed.version != "1.2.3" {
		t.Fatalf("unexpected data version: %s", parsed.version)
	}
}

func TestSchemaV2CatalogMismatchPanics(t *testing.T) {
	raw := []byte(`{
  "schema_version": 2,
  "version": "1.2.3",
  "stats": {
    "charmap_count": 0,
    "ambiguous_count": 0,
    "terms_cn_count": 1,
    "terms_hk_count": 0,
    "rule_catalog_count": 0
  },
  "charmap": {
    "chars": {},
    "ambiguous": [],
    "balanced_defaults": {},
    "balanced_protect_terms": {}
  },
  "terms": {"cn": {"software": "target"}},
  "rule_catalog": {"format": "grouped-v1", "groups": []}
}`)

	defer func() {
		if recover() == nil {
			t.Fatal("mustParseData should reject catalog and effective-term disagreement")
		}
	}()
	mustParseData(raw)
}
