<!-- zhtw:disable -->
# Accuracy Benchmark (2026-07-31)

Report mode: `aggregate`
Dataset classification: ``
Dataset: `blind-v2`
Inputs: `benchmarks/accuracy/blind-v2.inputs.json`
Competitors lock: `benchmarks/accuracy/competitors.lock.json`

## Hashes

- Inputs sha256: `ddef836456ee29decf019dae981c1017b9728524c42808ae2d7c2c894299820a`
- Expected sha256: `511b2845969a60c6c5b53e7de17b85fbe00b11521648dac10e77fe6ec6ace9c5`
- Lock sha256: `f72ed6d38c1fe1336a61c267baab518b48cd4d3046d4ca3bd525f94eb7ca8765`
- Competitor environment: `0ea3a0082456cca66973cf7bf6f04e608a1d78ca507c541569b391635de471ae`
- zhtw version: `4.4.2`
- Git SHA: `19626cf119e0ef7c8c04faa81960ee735eb9ac5a`
- Git dirty: `false`

## Summary

- Cases: 1960

Domain distribution:

- `formal_news`: 294
- `high_stakes`: 196
- `it_api_cli`: 490
- `llm_generated`: 294
- `social_daily`: 294
- `ui_i18n`: 392

Risk distribution:

- `baseline_guard`: 392
- `candidate_gap`: 786
- `over_conversion_guard`: 782

## Engine Scores

### zhtw

- Availability: available
- Version: `4.4.2`
- Family: `zhtw`
- Adapter: `local_python`
- Environment: ``
- Image ID: ``
- Config sha256: `f010ebe390dbf3fd21e5cdf41ade9db4057fc66146662610f36ebb46997cbc2e`
- Accepted accuracy: 0.3372
- Macro-domain accuracy: 0.3486
- Primary exact accuracy: 0.3163
- Idempotency rate: 0.9770
- Accepted: 661 / 1960
- Misses: 1299

### opencc-s2twp

- Availability: available
- Version: `1.4.1`
- Family: `opencc`
- Adapter: `container_jsonl`
- Environment: `0ea3a0082456cca66973cf7bf6f04e608a1d78ca507c541569b391635de471ae`
- Image ID: `sha256:c7d4c157e36b9ad84901ab7a189d0cb0d1ad5e43df8dc7685746aed3a0e2721c`
- Config sha256: `681dd1ff5f3a1efe93a6f56006ee7f58f767fa0366fd3a2ec6165c983e39415d`
- Accepted accuracy: 0.3082
- Macro-domain accuracy: 0.3152
- Primary exact accuracy: 0.2893
- Idempotency rate: 0.9842
- Accepted: 604 / 1960
- Misses: 1356

### opencc-js-cn-twp

- Availability: available
- Version: `1.4.1`
- Family: `opencc`
- Adapter: `container_jsonl`
- Environment: `0ea3a0082456cca66973cf7bf6f04e608a1d78ca507c541569b391635de471ae`
- Image ID: `sha256:c7d4c157e36b9ad84901ab7a189d0cb0d1ad5e43df8dc7685746aed3a0e2721c`
- Config sha256: `3e6093597509a9afc3fe36ec33325ac2d485f8fd3148c4f7ac8a5232cb5df767`
- Accepted accuracy: 0.3082
- Macro-domain accuracy: 0.3152
- Primary exact accuracy: 0.2893
- Idempotency rate: 0.9842
- Accepted: 604 / 1960
- Misses: 1356

### zhconv-zh-tw

- Availability: available
- Version: `1.4.3`
- Family: `mediawiki-zhconv`
- Adapter: `container_jsonl`
- Environment: `0ea3a0082456cca66973cf7bf6f04e608a1d78ca507c541569b391635de471ae`
- Image ID: `sha256:c7d4c157e36b9ad84901ab7a189d0cb0d1ad5e43df8dc7685746aed3a0e2721c`
- Config sha256: `5ed77140c1a379ed193b1f2a75c6c14e2e87df01a3f1fdbe00cff2f0ddf97cfb`
- Accepted accuracy: 0.2857
- Macro-domain accuracy: 0.3068
- Primary exact accuracy: 0.2694
- Idempotency rate: 0.9995
- Accepted: 560 / 1960
- Misses: 1400

### zhconv-rs-zh-tw

- Availability: available
- Version: `0.4.1`
- Family: `mediawiki-zhconv`
- Adapter: `container_jsonl`
- Environment: `0ea3a0082456cca66973cf7bf6f04e608a1d78ca507c541569b391635de471ae`
- Image ID: `sha256:c7d4c157e36b9ad84901ab7a189d0cb0d1ad5e43df8dc7685746aed3a0e2721c`
- Config sha256: `5ed77140c1a379ed193b1f2a75c6c14e2e87df01a3f1fdbe00cff2f0ddf97cfb`
- Accepted accuracy: 0.2857
- Macro-domain accuracy: 0.3075
- Primary exact accuracy: 0.2699
- Idempotency rate: 1.0000
- Accepted: 560 / 1960
- Misses: 1400

