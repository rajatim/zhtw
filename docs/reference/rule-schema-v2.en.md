# Rule schema v2 reference

> Available since 4.5.0. Packages and shared data use mono-versioning and must match.

Rule schema v2 adds a stable ID, source locale, and review metadata to each conversion rule. Version 4.5.0 uses this data for validation, audit, and `explain`. The schema migration did not rewrite the effective source-to-target map just to add metadata. `domain`, `trust_level`, `priority`, and `review_status` do not change whether an approved rule is active in 4.5.0.

The formal JSON Schema is [`src/zhtw/data/schemas/rule-v2.schema.json`](https://github.com/rajatim/zhtw/blob/main/src/zhtw/data/schemas/rule-v2.schema.json).

## Authoring envelope

```json
{
  "schema_version": 2,
  "rules": [
    {
      "id": "team:cn:custom:software",
      "source_locale": "cn",
      "source": "软件",
      "target": "軟體",
      "rule_class": "custom",
      "domain": "it",
      "trust_level": "custom",
      "priority": 0,
      "context": ["product-ui"],
      "evidence_source": "terminology review 2026-08-27",
      "review_status": "approved"
    }
  ]
}
```

The envelope and every rule reject missing or unknown fields. `schema_version` must be `2`, and `rules` must be an array.

## Main fields

| Field | Rule and purpose |
|---|---|
| `id` | 3 to 128 ASCII characters matching `^[a-z0-9][a-z0-9._:-]{2,127}$`; unique in the catalog |
| `source_locale` | `cn` or `hk`; describes the input locale |
| `source` | Non-empty matcher input pattern |
| `target` | Non-empty Taiwan Traditional output |
| `rule_class` | `bulk`, `generated_guard`, `curated`, or `custom` |
| `domain` | Usage area such as `general`, `it`, `medical`, or `ui` |
| `trust_level` | `imported`, `generated`, `curated`, or `custom` |
| `priority` | Integer from `-1000` to `1000`; metadata only in 4.5.0 |
| `context` | Unique non-empty strings; an empty array means no extra context limit |
| `evidence_source` | `null` or a non-empty string; required for approved rules |
| `review_status` | `pending`, `approved`, or `rejected` |

## Stable IDs

New v2 rules should use explicit IDs that remain stable. Moving a file, exporting again, or changing metadata must not change an ID. Create a new ID when the meaning of `source_locale`, `source`, `target`, or `rule_class` truly changes.

Legacy v1 rules receive deterministic IDs based on their core fields. File paths are not part of the ID, so a move does not change rule identity. Conflicting content for one ID, duplicate IDs, invalid IDs, and unknown enum values fail closed.

## Review lifecycle

- `pending`: candidate data that may enter a review packet but is not an effective production rule.
- `approved`: a human made the final decision, and `evidence_source` is required.
- `rejected`: keeps the decision record but does not enter the effective runtime map.

AI review can give advice. It cannot turn a pending item into human-approved ground truth.

## Shared data

`sdk/data/zhtw-data.json` is the exported cross-SDK format. It keeps the effective `terms` map and a compressed rule catalog. It is not the external authoring envelope and must not be edited by hand.

After maintained rules change, rebuild and verify the export:

```bash
zhtw export
zhtw validate
make export-check
```

Version 4.5.0 does not automatically apply domain profiles, reorder existing rules by `priority`, activate pending or rejected rules, or change matching behavior during schema migration.
