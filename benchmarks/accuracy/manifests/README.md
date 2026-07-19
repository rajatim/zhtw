<!-- zhtw:disable -->
# Dataset Manifests

Each normalized benchmark track must have one manifest conforming to
`../manifest.schema.json`. A manifest is accepted only when its source revision,
license, attribution, raw/normalized hashes, importer, known biases, and matching
`../LICENSES.md` notice all validate.

Run:

```bash
make benchmark-validate
```

External track manifests are added by Issues #40 and #41. Blind-v2 is added by
Issue #43.
