<!-- zhtw:disable -->
# Benchmark Data Licenses

Every dataset manifest must reference a matching `notice_id` heading in this
file. A manifest is invalid when its attribution or output-license obligation
is missing.

## zhtw-project-original

- Source: Original zhtw benchmark and regression material.
- License: MIT unless a case records a more restrictive source license.
- Attribution: Copyright zhtw contributors.
- Modifications: Human annotation and Taiwan Traditional normalization.
- Output license: MIT.

## zhtw-project-ui-i18n-v1

- Source: Project-original Simplified Chinese UI and internationalization input-only scenarios drafted 2026-07-23.
- License: MIT
- Attribution: Copyright zhtw contributors; initial input-only scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT
- Bias notice: Synthetic Codex-drafted scenarios are not independently observed market traffic. Independent Gemini and maintainer source review remain pending.

## zhtw-project-llm-product-v1

- Source: Project-original Simplified Chinese LLM product input-only scenarios drafted 2026-07-23.
- License: MIT
- Attribution: Copyright zhtw contributors; initial input-only scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT
- Bias notice: Synthetic Codex-drafted scenarios are not independently observed market traffic. Independent Gemini and maintainer source review remain pending.

## ud-gsd-v1

- Source: Universal Dependencies Chinese GSD commit
  `e0d85a020182e264d6384be2a59c0f4879a1cc35` and Chinese GSDSimp commit
  `7b61ed473f963e911788efdf1f478154bc1053e4` (tag `r2.18`).
- License: CC BY-SA 4.0
- Attribution: Universal Dependencies Chinese GSD contributors and Chinese GSDSimp contributors.
- Modifications: Extracted paired sentence text by sent_id, normalized JSON serialization, and added benchmark metadata; no linguistic content was corrected by zhtw.
- Output license: CC BY-SA 4.0
- Bias notice: GSDSimp was initially generated with OpenCC and later manually
  corrected. Results are secondary evidence and are not independent evidence
  against OpenCC-family converters.

## flores-200-zho-hans-v1

- Source: FLORES-200 archive associated with `facebookresearch/flores` commit
  `a6c830c6e1051fb4ac1a44b32358f00463f332bd`; archive S3 version
  `KJZoZnGvyduN3osrx.67C_UQ7C9oNDic`.
- License: CC BY-SA 4.0
- Attribution: FLORES-200 contributors, Meta AI.
- Modifications: Extracted zho_Hans dev and devtest sentences, applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: CC BY-SA 4.0
- Bias notice: Professional web-article translations are not representative of
  ordinary Taiwan product traffic. Domain and risk remain pending input-only
  review.

## ud-chinese-cfl-v1

- Source: Universal Dependencies Chinese-CFL commit
  `ad71b068e4581343dab897ef2d54abf102580897` (tag `r2.18`).
- License: CC BY-SA 4.0
- Attribution: Universal Dependencies Chinese-CFL contributors.
- Modifications: Extracted sentence text from the pinned CoNLL-U file, applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: CC BY-SA 4.0
- Bias notice: Learner essays contain non-native wording and source errors.
  Domain and risk remain pending input-only review.

## massive-1-0-zh-cn-v1

- Source: MASSIVE dataset 1.0 `zh-CN`, localized from the SLURP text dataset.
- License: CC BY 4.0
- Attribution: MASSIVE dataset, Copyright Amazon.com, Inc. or its affiliates; localized from the CC BY 4.0 SLURP text dataset; cite FitzGerald et al. (2022) and Bastianelli et al. (2020).
- Modifications: Extracted only id, partition, and Simplified Chinese utterance text from the checksum-pinned zh-CN JSONL member, applied Unicode NFC and whitespace normalization, removed exact within-source duplicate utterances, and added input-only candidate metadata; worker identifiers, judgments, intents, slot annotations, converter output, and expected text were excluded.
- Output license: CC BY 4.0
- Bias notice: Localized single-shot voice-assistant utterances are not independently
  authored organic Simplified Chinese traffic. Short commands, fragments, wake
  words, and mixed-language rows require input-only quality review.

## aosp-framework-zh-rcn-v1

- Source: Android Open Source Project `platform/frameworks/base`, Simplified
  Chinese core framework string resources at commit
  `1cdfff555f4a21f71ccc978290e2e212e2f8b168`.
- License: Apache License 2.0, stated in the source-file header.
- Attribution: Android Open Source Project contributors.
- Modifications: Extracted single-line Simplified Chinese <string> resources with stable name/msgid keys, applied Unicode NFC and whitespace normalization, and excluded short non-prose values, URLs, email addresses, and converter or expected output.
- Output license: Apache License 2.0.
- Bias notice: Platform-localized Android UI and system terminology are not
  independently authored organic Simplified Chinese traffic. Context-dependent
  messages and formatting placeholders require input-only review.

## vscode-loc-zh-hans-v1

- Source: Microsoft `vscode-loc` Chinese (Simplified) language pack,
  `main.i18n.json`, commit `da6509eed60b550e0e785d0d78ac05be46d5e982`.
- License: MIT License.
- Attribution: Visual Studio Code Localization Packs, Copyright Microsoft Corporation, Chinese (Simplified) language pack, microsoft/vscode-loc commit da6509eed60b550e0e785d0d78ac05be46d5e982.
- Modifications: Extracted Simplified Chinese UI message values from the checksum-pinned main.i18n.json, applied Unicode NFC and whitespace normalization, generated stable IDs from module/message keys, removed exact within-source duplicate values, and excluded multiline text, pure placeholders, URLs, email addresses, HTML, Markdown links, code fragments, and converter or expected output.
- Output license: MIT License.
- Bias notice: Microsoft-managed developer-tool localization is not organic
  market traffic and heavily represents UI and software terminology.

## chromium-strings-zh-cn-v1

- Source: Chromium Chinese (Simplified) browser UI, `chromium_strings_zh-CN.xtb`,
  commit `13ef0a3b8e7a97c94d0acbef5da410b68a0f7d81`.
- License: BSD 3-Clause License.
- Attribution: Copyright 2015 The Chromium Authors; Chinese (Simplified) Chromium browser UI at commit 13ef0a3b8e7a97c94d0acbef5da410b68a0f7d81.
- Modifications: Parsed the checksum-pinned XTB XML resource, extracted variable-free Simplified Chinese translation values with stable numeric IDs, applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and excluded placeholders, URLs, email addresses, markup, code fragments, converter output, and expected text.
- Output license: BSD 3-Clause License.
- Bias notice: Chromium-managed browser localization is not independently
  authored organic Simplified Chinese traffic. Browser, account, privacy, and
  Google service terminology are overrepresented, and context-dependent labels
  still require input-only review.

## zhtw-project-formal-llm-balance-v1

- Source: zhtw project-original formal-writing and LLM semantic-preservation
  balance scenarios drafted on 2026-07-27.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only formal-writing and LLM semantic-preservation balance scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: This is synthetic project-original coverage, not independently
  observed market traffic. It intentionally overrepresents formal writing,
  identifier preservation, and LLM semantic constraints.

## zhtw-project-llm-domain-balance-v1

- Source: zhtw project-original LLM-heavy domain-balance input-only scenarios
  drafted on 2026-07-27.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only LLM-heavy domain-balance scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: This is synthetic project-original coverage, not independently
  observed market traffic. It intentionally emphasizes LLM product behavior,
  protected technical tokens, and underrepresented domain/risk cells. AI source
  classification remains advisory until maintainer confirmation.

## zhtw-project-llm-social-baseline-v1

- Source: zhtw project-original LLM and everyday-social input-only scenarios
  drafted on 2026-07-27.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only LLM and everyday-social scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: This is synthetic project-original coverage, not independently
  observed market traffic. It intentionally emphasizes underrepresented LLM and
  everyday-social usage. AI source classification remains advisory until
  maintainer confirmation.

## zhtw-project-it-llm-social-guard-v1

- Source: zhtw project-original IT guard, LLM, and social entity input-only
  scenarios drafted on 2026-07-28.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only IT guard, LLM, and social entity scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: This is synthetic project-original coverage, not independently
  observed market traffic. It intentionally targets preregistered IT
  over-conversion, LLM candidate/baseline, and social entity-guard quota gaps.
  Independent Gemini review and maintainer confirmation completed on 2026-07-28;
  64 sampled cases passed promotion deduplication across batches 037-038.

## zhtw-project-llm-it-ui-baseline-v1

- Source: zhtw project-original LLM, IT, and UI baseline input-only scenarios
  drafted on 2026-07-28.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only LLM, IT, and UI baseline scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: Synthetic quota coverage is not independently observed market
  traffic. It targets preregistered LLM, IT, and UI baseline-guard gaps; Codex and
  Gemini advisories received maintainer confirmation on 2026-07-28.

## zhtw-project-it-api-cli-v1

- Source: zhtw project-original IT, API, and CLI input-only scenarios drafted
  on 2026-07-23.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only IT, API, and CLI scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: Synthetic engineering scenarios are coverage material, not
  independently observed market-frequency evidence.

## zhtw-project-formal-llm-semantic-v1

- Source: zhtw project-original formal-writing and LLM semantic-preservation
  input-only scenarios drafted on 2026-07-24.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only formal-writing and LLM semantic-preservation scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: Synthetic challenge coverage is not independently observed
  market-frequency evidence. Independent Gemini advisory and maintainer
  input-only review completed on 2026-07-24; all 100 cases passed promotion
  deduplication.

## zhtw-project-formal-entity-guard-v1

- Source: zhtw project-original formal-news entity, citation, identifier, and baseline input-only scenarios drafted on 2026-07-24.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only formal entity-guard scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: Synthetic challenge coverage is not independently observed market-frequency evidence. Independent Gemini advisory and maintainer input-only review completed on 2026-07-24.

## zhtw-project-it-llm-ui-guard-v1

- Source: zhtw project-original IT, LLM, and UI guard input-only scenarios drafted on 2026-07-26.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only IT, LLM, and UI guard scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: Synthetic challenge coverage is not independently observed market-frequency evidence. Independent Gemini advisory and maintainer input-only review completed on 2026-07-26.

## zhtw-project-balanced-baseline-guard-v1

- Source: zhtw project-original balanced LLM, formal-writing, social, and UI baseline-guard input-only scenarios drafted on 2026-07-26.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only balanced baseline and preservation scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: Synthetic benchmark coverage is not independently observed market-frequency evidence. Independent Gemini advisory and maintainer input-only review completed on 2026-07-27; all 100 cases passed promotion deduplication.

## ftc-small-business-simplified-v1

- Source: Federal Trade Commission, *Scams and Your Small Business*, Simplified
  Chinese, July 2023.
- License: U.S. Public Domain under the FTC website policy; third-party content,
  graphics, and agency seals are excluded.
- Attribution: Federal Trade Commission, Scams and Your Small Business, Simplified Chinese, July 2023; no FTC endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese prose sentences from the checksum-pinned FTC-authored PDF, joined PDF layout wraps, removed headings, page furniture, navigation URLs, phone instructions, and incomplete fragments, and added input-only provenance; no images, seals, expected text, or converter output were used.
- Output license: U.S. Public Domain.
- Bias notice: U.S.-focused fraud and small-business guidance intentionally
  concentrates financial, legal, and cybersecurity language.

## ftc-heads-up-simplified-v1

- Source: Federal Trade Commission, *Heads Up: Stop. Think. Connect.*,
  Simplified Chinese, August 2023.
- License: U.S. Public Domain under the FTC website policy; third-party content,
  graphics, and agency seals are excluded.
- Attribution: Federal Trade Commission, Heads Up: Stop. Think. Connect., Simplified Chinese, August 2023; no FTC endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese prose sentences from the checksum-pinned FTC-authored PDF, joined PDF layout wraps and cross-page sentences, removed headings, page furniture, English parallel text, navigation URLs, and incomplete fragments, and added input-only provenance; no images, seals, expected text, or converter output were used.
- Output license: U.S. Public Domain.
- Bias notice: U.S.-focused youth online-safety guidance concentrates social
  media, privacy, account-security, cyberbullying, and device-safety language.

## nps-essential-acadia-simplified-v1

- Source: National Park Service, Acadia National Park, *Essential Acadia:
  Simplified Chinese*, page last updated October 6, 2023.
- License: U.S. Public Domain under the NPS website disclaimer; third-party
  content, images, graphics, and agency insignia are excluded.
- Attribution: National Park Service, Acadia National Park, Essential Acadia: Simplified Chinese; no NPS endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese prose sentences from the checksum-pinned NPS article content container, removed navigation, images, English labels, page furniture, URLs without complete sentences, and incomplete fragments, and added input-only provenance; no trademarks, expected text, or converter output were used.
- Output license: U.S. Public Domain.
- Bias notice: U.S. national-park visitor guidance concentrates travel,
  outdoor-safety, park-rule, and mixed-language place-name usage.

## ready-gov-floods-zh-hans-v1

- Source: Federal Emergency Management Agency, Ready.gov, *Floods*, Simplified
  Chinese, page last updated October 22, 2025.
- License: U.S. Public Domain under 17 U.S.C. 105 for FEMA-authored text; third-party linked content excluded
- Attribution: Federal Emergency Management Agency, Ready.gov, Floods, Simplified Chinese; no FEMA, DHS, or U.S. Government endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese paragraph and list-item sentences from the checksum-pinned Ready.gov main element, removed navigation, images, external resources, phone/URL instructions, page furniture, and exact duplicates, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.
- Bias notice: U.S. flood, evacuation, insurance, medical, and safety guidance
  is not representative of ordinary Taiwan traffic.

## ready-gov-hurricanes-zh-hans-v1

- Source: Federal Emergency Management Agency, Ready.gov, *Hurricanes*,
  Simplified Chinese, page last updated July 9, 2026.
- License: U.S. Public Domain under 17 U.S.C. 105 for FEMA-authored text; third-party linked content excluded
- Attribution: Federal Emergency Management Agency, Ready.gov, Hurricanes, Simplified Chinese; no FEMA, DHS, or U.S. Government endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese paragraph and list-item sentences from the checksum-pinned Ready.gov main element, removed navigation, images, external resources, phone/URL instructions, page furniture, and exact duplicates, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.
- Bias notice: U.S. hurricane, evacuation, insurance, medical, and safety
  guidance is not representative of ordinary Taiwan traffic.

## ready-gov-earthquakes-zh-hans-v1

- Source: Federal Emergency Management Agency, Ready.gov, *Earthquakes*,
  Simplified Chinese, page last updated October 22, 2025.
- License: U.S. Public Domain under 17 U.S.C. 105 for FEMA-authored text; third-party linked content excluded
- Attribution: Federal Emergency Management Agency, Ready.gov, Earthquakes, Simplified Chinese; no FEMA, DHS, or U.S. Government endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese paragraph and list-item sentences from the checksum-pinned Ready.gov main element, removed navigation, images, external resources, phone/URL instructions, page furniture, and exact duplicates, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.
- Bias notice: U.S. earthquake, evacuation, medical, and safety guidance is not
  representative of ordinary Taiwan traffic.

## ready-gov-drought-zh-hans-v1

- Source: Federal Emergency Management Agency, Ready.gov, *Drought*, Simplified Chinese, page last updated October 31, 2025.
- License: U.S. Public Domain under 17 U.S.C. 105 for FEMA-authored text; third-party linked content excluded.
- Attribution: Federal Emergency Management Agency, Ready.gov, Drought, Simplified Chinese; no FEMA, DHS, or U.S. Government endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese paragraph and list-item sentences from the checksum-pinned Ready.gov main element, removed navigation, images, external resources, phone/URL instructions, page furniture, and exact duplicates, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.
- Bias notice: U.S. drought, water-conservation, agriculture, and public-safety guidance is not representative of ordinary Taiwan traffic.

## ready-gov-home-fires-zh-hans-v1

- Source: Federal Emergency Management Agency, Ready.gov, *Home Fires*, Simplified Chinese, page last updated October 31, 2025.
- License: U.S. Public Domain under 17 U.S.C. 105 for FEMA-authored text; third-party linked content excluded.
- Attribution: Federal Emergency Management Agency, Ready.gov, Home Fires, Simplified Chinese; no FEMA, DHS, or U.S. Government endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese paragraph and list-item sentences from the checksum-pinned Ready.gov main element, removed navigation, images, external resources, phone/URL instructions, page furniture, and exact duplicates, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.
- Bias notice: U.S. fire-prevention, evacuation, burn, smoke-alarm, and emergency-response guidance is not representative of ordinary Taiwan traffic.

## ready-gov-landslides-debris-flow-zh-hans-v1

- Source: Federal Emergency Management Agency, Ready.gov, *Landslides and Debris Flow*, Simplified Chinese, page last updated November 12, 2025.
- License: U.S. Public Domain under 17 U.S.C. 105 for FEMA-authored text; third-party linked content excluded.
- Attribution: Federal Emergency Management Agency, Ready.gov, Landslides and Debris Flow, Simplified Chinese; no FEMA, DHS, or U.S. Government endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese paragraph and list-item sentences from the checksum-pinned Ready.gov main element, removed navigation, images, external resources, phone/URL instructions, page furniture, and exact duplicates, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.
- Bias notice: U.S. landslide, debris-flow, evacuation, geology, and public-safety guidance is not representative of ordinary Taiwan traffic.

## ready-gov-radiation-zh-hans-v1

- Source: Federal Emergency Management Agency, Ready.gov, *Radiation Emergencies*, Simplified Chinese, page last updated April 8, 2025.
- License: U.S. Public Domain under 17 U.S.C. 105 for FEMA-authored text; third-party linked content excluded.
- Attribution: Federal Emergency Management Agency, Ready.gov, Radiation Emergencies, Simplified Chinese; no FEMA, DHS, or U.S. Government endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese paragraph and list-item sentences from the checksum-pinned Ready.gov main element, removed navigation, images, external resources, phone/URL instructions, page furniture, and exact duplicates, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.
- Bias notice: U.S. radiation, nuclear-incident, decontamination, sheltering, and medical guidance is not representative of ordinary Taiwan traffic.

## ready-gov-tornadoes-zh-hans-v1

- Source: Federal Emergency Management Agency, Ready.gov, *Tornadoes*, Simplified Chinese, page last updated November 12, 2025.
- License: U.S. Public Domain under 17 U.S.C. 105 for FEMA-authored text; third-party linked content excluded.
- Attribution: Federal Emergency Management Agency, Ready.gov, Tornadoes, Simplified Chinese; no FEMA, DHS, or U.S. Government endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese paragraph and list-item sentences from the checksum-pinned Ready.gov main element, removed navigation, images, external resources, phone/URL instructions, page furniture, and exact duplicates, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.
- Bias notice: U.S. tornado, sheltering, evacuation, weather-alert, and public-safety guidance is not representative of ordinary Taiwan traffic. Codex and Gemini independently classified 16 sampled cases; maintainer `tim` confirmed the synthesis on 2026-07-28.

## ready-gov-winter-weather-zh-hans-v1

- Source: Federal Emergency Management Agency, Ready.gov, *Winter Weather*, Simplified Chinese, page last updated November 12, 2025.
- License: U.S. Public Domain under 17 U.S.C. 105 for FEMA-authored text; third-party linked content excluded.
- Attribution: Federal Emergency Management Agency, Ready.gov, Winter Weather, Simplified Chinese; no FEMA, DHS, or U.S. Government endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese paragraph and list-item sentences from the checksum-pinned Ready.gov main element, removed navigation, images, external resources, phone/URL instructions, page furniture, and exact duplicates, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.
- Bias notice: U.S. winter-storm, cold-exposure, heating, travel, and public-safety guidance is not representative of ordinary Taiwan traffic. Codex and Gemini independently classified 48 sampled cases across batches 040-041; maintainer `tim` confirmed both syntheses on 2026-07-28.

## ready-gov-kids-tornadoes-zh-hans-v1

- Source: Federal Emergency Management Agency, Ready.gov, *Tornadoes for Kids*, Simplified Chinese, page last updated October 29, 2025.
- License: U.S. Public Domain under 17 U.S.C. 105 for FEMA-authored text; third-party linked content excluded.
- Attribution: Federal Emergency Management Agency, Ready.gov, Tornadoes for Kids, Simplified Chinese; no FEMA, DHS, or U.S. Government endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese paragraph and list-item sentences from the checksum-pinned Ready.gov main element, removed navigation, images, external resources, phone/URL instructions, page furniture, and exact duplicates, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.
- Bias notice: U.S. child-focused tornado, sheltering, weather-alert, and public-safety guidance is not representative of ordinary Taiwan traffic.

## ready-gov-campus-zh-hans-v1

- Source: Federal Emergency Management Agency, Ready.gov, *Campus Preparedness*, Simplified Chinese, page last updated October 29, 2025.
- License: U.S. Public Domain under 17 U.S.C. 105 for FEMA-authored text; third-party linked content excluded.
- Attribution: Federal Emergency Management Agency, Ready.gov, Campus Preparedness, Simplified Chinese; no FEMA, DHS, or U.S. Government endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese paragraph and list-item sentences from the checksum-pinned Ready.gov main element, removed navigation, images, external resources, phone/URL instructions, page furniture, and exact duplicates, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.
- Bias notice: U.S. campus emergency-planning, weather-alert, evacuation, and training guidance is not representative of ordinary Taiwan traffic.

## zhtw-project-formal-llm-overconversion-guard-v1

- Source: zhtw project-original formal-document and LLM over-conversion guard scenarios drafted from declared Blind-v2 coverage gaps.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only formal-document and LLM over-conversion guard scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: Synthetic project-original inputs intentionally concentrate on formal documents, LLM systems, identifiers, proper names, quotations, codes, and formatting-preservation contexts; they are not independently observed market traffic.

## ready-gov-evacuation-zh-hans-v1

- Source: Ready.gov, *Evacuation*, Simplified Chinese, page last updated 2022-05-19.
- License: U.S. Public Domain under 17 U.S.C. 105 for FEMA-authored text; third-party linked content excluded.
- Attribution: Federal Emergency Management Agency, Ready.gov, Evacuation, Simplified Chinese; no FEMA, DHS, or U.S. Government endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese paragraph and list-item sentences from the checksum-pinned Ready.gov main element, removed navigation, images, external resources, phone/URL instructions, page furniture, and exact duplicates, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.
- Bias notice: Official U.S. evacuation and emergency guidance is not representative of ordinary Taiwan traffic; list-derived fragments and inline link joins require input-only review.

## ready-gov-cybersecurity-zh-hans-v1

- Source: Ready.gov, *Cybersecurity*, Simplified Chinese, page last updated 2025-11-12.
- License: U.S. Public Domain under 17 U.S.C. 105 for FEMA-authored text; third-party linked content excluded.
- Attribution: Federal Emergency Management Agency, Ready.gov, Cybersecurity, Simplified Chinese; no FEMA, DHS, or U.S. Government endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese paragraph and list-item sentences from the checksum-pinned Ready.gov main element, removed navigation, images, external resources, phone/URL instructions, page furniture, and exact duplicates, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.
- Bias notice: Official U.S. cybersecurity guidance is not representative of ordinary Taiwan traffic; list-derived fragments and third-party resource descriptions require input-only review.

## zhtw-project-formal-llm-context-guard-v1

- Source: zhtw project-original formal-news and LLM context-guard scenarios drafted from declared Blind-v2 domain and risk gaps.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only formal-news and LLM context-guard scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: Synthetic project-original inputs intentionally concentrate on formal-news and LLM semantic contexts; they are not independently observed market traffic.

## ready-gov-are-you-ready-guide-simplified-v1

- Source: Federal Emergency Management Agency, Ready.gov, *Are You Ready? An In-Depth Guide to Citizen Preparedness*, Simplified Chinese, FEMA P-2157, September 2020.
- License: U.S. Public Domain under 17 U.S.C. 105 for FEMA-authored text; third-party material excluded
- Attribution: Federal Emergency Management Agency, Ready.gov, Are You Ready? An In-Depth Guide to Citizen Preparedness, Simplified Chinese, FEMA P-2157; no FEMA, DHS, or U.S. Government endorsement or affiliation is implied.
- Modifications: Extracted complete Simplified Chinese prose sentences from checksum-pinned body pages, removed contents pages, page furniture, URLs, phone instructions, images, insignia, third-party material, and exact duplicates, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.
- Bias notice: Official U.S. disaster-preparation guidance is not representative of ordinary Taiwan traffic; the PDF text layer also repeats some visual headings and emphasis.

## zhtw-project-formal-llm-evidence-guard-v1

- Source: zhtw project-original formal-reporting and LLM evidence-preservation scenarios drafted from declared Blind-v2 domain and risk gaps.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only formal-reporting and LLM evidence-preservation scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: Synthetic project-original inputs intentionally concentrate on formal reporting and LLM evidence-preservation contexts; they are not independently observed market traffic.

## zhtw-project-ui-social-baseline-guard-v1

- Source: zhtw project-original UI localization and everyday social-language scenarios drafted from declared Blind-v2 domain and risk gaps.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only UI and everyday-social baseline and preservation scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: Synthetic project-original inputs intentionally concentrate on UI localization, ordinary messages, and preservation guards; they are not independently observed market traffic.

## zhtw-project-llm-formal-reasoning-guard-v1

- Source: zhtw project-original LLM reasoning and formal-reporting scenarios drafted from declared Blind-v2 domain and risk gaps.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only LLM reasoning and formal-reporting scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: Synthetic project-original inputs intentionally concentrate on LLM reasoning, formal reporting, identifiers, and evidence-preservation contexts; they are not independently observed market traffic.

## zhtw-project-llm-formal-operations-guard-v1

- Source: zhtw project-original LLM operations and formal-administration scenarios drafted from declared Blind-v2 domain and risk gaps.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only LLM operations and formal-administration scenarios drafted by Codex and subject to independent Agy/Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: Synthetic project-original inputs intentionally concentrate on LLM operations, formal administration, identifiers, and evidence-preservation contexts; they are not independently observed market traffic.

## osha-electrical-safety-simplified-v1

- Source: OSHA 4281-08 2023, *Electrical Safety*, Chinese Simplified.
- License: U.S. Public Domain for OSHA-authored text under the DOL reuse policy; third-party content excluded
- Attribution: Occupational Safety and Health Administration, Electrical Safety, OSHA 4281-08 2023, Chinese Simplified; no OSHA or U.S. Department of Labor endorsement or affiliation is implied.
- Modifications: Extracted complete Simplified Chinese sentences from the checksum-pinned OSHA PDF, excluded the English page, URLs, phone instructions, page furniture, images, logos, and third-party content, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.

## osha-chainsaw-safety-simplified-v1

- Source: OSHA 4286-08 2023, *Chainsaw Safety*, Chinese Simplified.
- License: U.S. Public Domain for OSHA-authored text under the DOL reuse policy; third-party content excluded
- Attribution: Occupational Safety and Health Administration, Chainsaw Safety, OSHA 4286-08 2023, Chinese Simplified; no OSHA or U.S. Department of Labor endorsement or affiliation is implied.
- Modifications: Extracted complete Simplified Chinese sentences from the checksum-pinned OSHA PDF, excluded the English page, URLs, phone instructions, page furniture, images, logos, and third-party content, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.

## osha-work-zone-traffic-simplified-v1

- Source: OSHA 4291-08 2023, *Work Zone Traffic Safety*, Chinese Simplified.
- License: U.S. Public Domain for OSHA-authored text under the DOL reuse policy; third-party content excluded
- Attribution: Occupational Safety and Health Administration, Work Zone Traffic Safety, OSHA 4291-08 2023, Chinese Simplified; no OSHA or U.S. Department of Labor endorsement or affiliation is implied.
- Modifications: Extracted complete Simplified Chinese sentences from the checksum-pinned OSHA PDF, excluded the English page, URLs, phone instructions, page furniture, images, logos, and third-party content, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.

## osha-disaster-falls-simplified-v1

- Source: OSHA 4301-08 2023, *Protecting Workers from Slips, Trips and Falls during Disaster Response*, Chinese Simplified.
- License: U.S. Public Domain for OSHA-authored text under the DOL reuse policy; third-party content excluded
- Attribution: Occupational Safety and Health Administration, Protecting Workers from Slips, Trips and Falls during Disaster Response, OSHA 4301-08 2023, Chinese Simplified; no OSHA or U.S. Department of Labor endorsement or affiliation is implied.
- Modifications: Extracted complete Simplified Chinese sentences from the checksum-pinned OSHA PDF, excluded the English page, URLs, phone instructions, page furniture, images, logos, and third-party content, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.

## osha-small-business-consultation-simplified-v1

- Source: OSHA 4230-05 2023, *On-Site Consultation for Small Business*, Chinese Simplified.
- License: U.S. Public Domain for OSHA-authored text under the DOL reuse policy; third-party content excluded
- Attribution: Occupational Safety and Health Administration, On-Site Consultation for Small Business, OSHA 4230-05 2023, Chinese Simplified; no OSHA or U.S. Department of Labor endorsement or affiliation is implied.
- Modifications: Extracted complete Simplified Chinese sentences from the checksum-pinned OSHA PDF, excluded URLs, phone instructions, page furniture, images, logos, attributed third-party testimonials, and other third-party content, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.

## osha-disaster-cleanup-simplified-v1

- Source: OSHA DTSEM FS-4355 08/2023, *Keeping Workers Safe during Disaster Cleanup and Recovery*, Chinese Simplified.
- License: U.S. Public Domain for OSHA-authored text under the DOL reuse policy; third-party content excluded
- Attribution: Occupational Safety and Health Administration, Keeping Workers Safe during Disaster Cleanup and Recovery, DTSEM FS-4355 08/2023, Chinese Simplified; no OSHA or U.S. Department of Labor endorsement or affiliation is implied.
- Modifications: Extracted complete Simplified Chinese sentences from the checksum-pinned OSHA PDF, excluded URLs, phone instructions, page furniture, images, logos, photo credits, and other third-party content, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.

## osha-fallen-workers-family-simplified-v1

- Source: OSHA 2023, *Fallen Workers Brochure*, Chinese Simplified.
- License: U.S. Public Domain for OSHA-authored text under the DOL reuse policy; third-party content excluded
- Attribution: Occupational Safety and Health Administration, Fallen Workers Brochure, 2023, Chinese Simplified; no OSHA or U.S. Department of Labor endorsement or affiliation is implied.
- Modifications: Extracted complete Simplified Chinese sentences from the checksum-pinned OSHA PDF, excluded URLs, phone and crisis-line instructions, email addresses, page furniture, images, logos, external organizations, and other third-party content, and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.

## cdc-stacks-111808-v1

- Source: CDC Stacks item `cdc:111808`, *当您生病时*, main-document checksum
  `af99f6f5dc63f2dbebd5d1ed0010dd492b27d9b742fd8416cff2f90b26f63b78`.
- License: U.S. Public Domain.
- Attribution: Centers for Disease Control and Prevention (U.S.).
- Modifications: Extracted complete Simplified Chinese sentences from the checksum-pinned PDF with pypdf 5.9.0, applied Unicode NFC and conservative PDF-whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; headings, fragments, and converter output were excluded, and no expected text was used.
- Output license: U.S. Public Domain.
- Bias notice: Historical translated COVID-19 guidance is not current medical
  advice or representative of ordinary Taiwan product traffic.

## cisa-cyber-hygiene-zh-hans-v1

- Source: Cybersecurity and Infrastructure Security Agency, *Cyber Hygiene*,
  Simplified Chinese, PDF created 2022-04-22.
- License: U.S. Public Domain for CISA-authored text under 17 U.S.C. 105; third-party content excluded
- Attribution: Cybersecurity and Infrastructure Security Agency, Cyber Hygiene, Simplified Chinese; no CISA or U.S. Department of Homeland Security endorsement or affiliation is implied.
- Modifications: Extracted complete Simplified Chinese sentences from the checksum-pinned CISA PDF; excluded headings, page furniture, logos, contact details, external links, and third-party content; no expected text or converter output was used.
- Output license: U.S. Public Domain.
- Bias notice: A one-page translated U.S. cyber-safety guide is not
  representative of ordinary Taiwan traffic.

## cisa-personal-security-zh-hans-v1

- Source: Cybersecurity and Infrastructure Security Agency, *Personal Security
  Considerations Action Guide: Critical Infrastructure Workers*, Simplified
  Chinese, June 2024 update.
- License: U.S. Public Domain for CISA-authored text under 17 U.S.C. 105; third-party references and cited content excluded
- Attribution: Cybersecurity and Infrastructure Security Agency, Personal Security Considerations Action Guide: Critical Infrastructure Workers, Simplified Chinese; no CISA or U.S. Department of Homeland Security endorsement or affiliation is implied.
- Modifications: Extracted complete Simplified Chinese body sentences from the checksum-pinned CISA PDF; excluded headings, page furniture, logos, contact details, external links, references, and third-party cited content; no expected text or converter output was used.
- Extraction quality: Punctuation-terminated extraction can retain list
  fragments; input-only classification must reject them fail-closed before
  promotion.
- Output license: U.S. Public Domain.
- Bias notice: Translated U.S. critical-infrastructure security guidance
  concentrates physical safety, threat response, privacy, and cybersecurity;
  it is not representative of ordinary Taiwan traffic.

## cdc-stacks-120024-v1

- Source: CDC Stacks item `cdc:120024`, *照顾好你的牙齿*, main-document
  checksum `41a685b4c0ff1805b23afca4599d60583c6ffb5ccb892b391955956c9e365020`.
- License: U.S. Public Domain.
- Attribution: National Center for Chronic Disease Prevention and Health Promotion (U.S.).
- Modifications: Extracted complete Simplified Chinese sentences from the checksum-pinned PDF with pypdf 5.9.0, applied Unicode NFC and conservative PDF-whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; headings without sentence punctuation, fragments, and converter output were excluded, and no expected text was used.
- Output license: U.S. Public Domain.
- Bias notice: A children's oral-health activity booklet is not representative
  of ordinary Taiwan product traffic.

## cdc-stacks-116683-v1

- Source: CDC Stacks item `cdc:116683`, *健康平等措施*, main-document checksum
  `53fcf122e5009fecf2f7caa24cacbf7a43f55367a3b69ccdbcd69a90eae870a7`.
- License: U.S. Public Domain.
- Attribution: National Center for Immunization and Respiratory Diseases (U.S.). Division of Viral Diseases.
- Modifications: Extracted complete Simplified Chinese introductory and purpose sentences from the checksum-pinned PDF with pypdf 5.9.0, applied Unicode NFC and conservative PDF-whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; complex lists, headings, fragments, third-party links, and converter output were excluded, and no expected text was used.
- Output license: U.S. Public Domain.
- Bias notice: Historical translated U.S. public-health program descriptions are
  not current medical guidance or representative of ordinary Taiwan traffic.

## census-newsroom-zh-hans-v1

- Source: United States Census Bureau, nine Simplified Chinese newsroom releases
  concerning 2020 Census operations, response, quality, and demographic analysis.
- License: U.S. Public Domain for Census Bureau-authored text under 17 U.S.C. 105; linked and third-party content excluded
- Attribution: United States Census Bureau, nine Simplified Chinese newsroom releases concerning the 2020 Census; no Census Bureau, Department of Commerce, or U.S. Government endorsement or affiliation is implied.
- Modifications: Extracted complete Simplified Chinese sentences only from checksum-pinned Census newsroom body text components; excluded navigation, headings, page furniture, contact details, URLs, tables without sentence punctuation, and third-party linked content; normalized Unicode and whitespace and added input-only provenance; no expected text or converter output was used.
- Output license: U.S. Public Domain.
- Bias notice: Formal U.S. census communications and 2020 operational context are not
  representative of ordinary Taiwan product traffic.

## zhtw-project-competitor-risk-taxonomy-v1

- Source: zhtw project-original Simplified Chinese scenarios drafted from abstract
  converter error categories observed in public discussions.
- License: MIT.
- Attribution: Copyright zhtw contributors; input-only scenarios drafted by Codex from abstract converter error categories and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; public issue text, converter output, and expected text were not copied or used.
- Output license: MIT.
- Bias notice: These are synthetic risk-focused scenarios, not independently
  observed market traffic.

## kubernetes-docs-zh-cn-v1

- Source: The Kubernetes Authors, four Simplified Chinese concept documentation
  pages from `kubernetes/website` commit
  `8668f30367fe6aeec80d515e364552b45c278f99`.
- License: Creative Commons Attribution 4.0 International (CC BY 4.0).
- Attribution: The Kubernetes Authors, Kubernetes website Simplified Chinese documentation, commit 8668f30367fe6aeec80d515e364552b45c278f99.
- Modifications: Extracted complete visible Simplified Chinese prose sentences from four checksum-pinned Markdown pages; removed front matter, English translation comments, code blocks, headings, links, shortcodes, and markup; normalized Unicode and whitespace and added input-only provenance; no expected text or converter output was used.
- Output license: CC BY 4.0.
- Bias notice: Technical Kubernetes documentation is not representative of
  ordinary consumer traffic, and translated prose can contain source-language
  influence or context-dependent fragments.

## ftc-how-to-avoid-scam-simplified-v1

- Source: Federal Trade Commission, *How to Avoid a Scam*, Simplified Chinese,
  July 2023; PDF Last-Modified 2023-11-29T22:20:42Z and raw SHA-256
  `78720bc248bced72d951e2d72902c6957fc33bb3eefedb2b8df1e31babef8804`.
- License: U.S. Public Domain for FTC-authored text under 17 U.S.C. 105 and
  the FTC website copyright policy; third-party graphics and linked material excluded.
- Attribution: Federal Trade Commission, How to Avoid a Scam, Simplified Chinese, July 2023; no FTC endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese prose sentences from the checksum-pinned FTC-authored PDF, joined PDF layout wraps, removed headings, page furniture, contact instructions, URLs, bullet glyphs, and incomplete list fragments, and added input-only provenance; no images, seals, expected text, or converter output were used.
- Output license: U.S. Public Domain.
- Bias notice: U.S. fraud, payment, account-security and government-impersonation
  guidance is not representative of ordinary Taiwan traffic.

## ftc-identity-theft-simplified-v1

- Source: Federal Trade Commission, *How To Spot, Avoid, and Report Identity
  Theft*, Simplified Chinese, November 2023; PDF Last-Modified
  2024-01-22T14:27:03Z and raw SHA-256
  `d1ec4c4942e12eda9e35a4b50860f43b150bb23d9f6891ba1a59951f8b8e2885`.
- License: U.S. Public Domain for FTC-authored text under 17 U.S.C. 105 and
  the FTC website copyright policy; third-party graphics and linked material excluded.
- Attribution: Federal Trade Commission, How To Spot, Avoid, and Report Identity Theft, Simplified Chinese, November 2023; no FTC endorsement or affiliation is implied.
- Modifications: Extracted only complete Simplified Chinese prose sentences from the checksum-pinned FTC-authored PDF, joined PDF layout wraps, removed headings, page furniture, contact instructions, URLs, bullet glyphs, incomplete list fragments, and added input-only provenance; no images, seals, expected text, or converter output were used.
- Output license: U.S. Public Domain.
- Bias notice: U.S. identity, financial-account, document-security and
  authentication guidance is not representative of ordinary Taiwan traffic.

## zhtw-project-it-ui-llm-formal-guard-v1

- Source: zhtw project-original Simplified Chinese IT, UI, LLM and
  formal-document guard scenarios drafted from declared Blind-v2 coverage gaps.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only IT, UI, LLM, and formal-document guard scenarios drafted by Codex and subject to independent Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: These are synthetic preservation-focused scenarios, not
  independently observed market traffic.

## zhtw-project-social-formal-context-guard-v1

- Source: zhtw project-original Simplified Chinese social/daily and
  formal-document context scenarios drafted from declared Blind-v2 coverage gaps.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only social/daily and formal-document scenarios drafted by Codex and subject to independent Agy/Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: These are synthetic context and preservation scenarios, not
  independently observed market traffic.

## zhtw-project-social-formal-ambiguity-guard-v1

- Source: zhtw project-original Simplified Chinese social/daily and
  formal-document ambiguity scenarios drafted from declared Blind-v2 coverage gaps.
- License: MIT.
- Attribution: Copyright zhtw contributors; initial input-only social/daily and formal-document ambiguity scenarios drafted by Codex and subject to independent Agy/Gemini and maintainer review.
- Modifications: Applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: MIT.
- Bias notice: These are synthetic ambiguity and preservation scenarios, not
  independently observed market traffic.

## naer-terms-v1

- Source: Government Data dataset 15275, `國家教育研究院-兩岸對照名詞-計算機學術名詞`;
  metadata updated 2024-07-08 10:11 Asia/Taipei and CSV Last-Modified
  2024-07-11T03:25:57Z.
- License: 政府資料開放授權條款-第1版 (Open Government Data License, version 1.0)
- Attribution: 國家教育研究院 2024 國家教育研究院-兩岸對照名詞-計算機學術名詞；不暗示國家教育研究院推薦、同意或為 zhtw 背書。
- Modifications: Selected and normalized source fields, preserved unresolved compound cells without delimiter splitting, classified conversion and identity candidates, excluded ambiguous bare terms, deduplicated evaluation cases, and added benchmark metadata; no records were imported into the zhtw product dictionaries.
- Output license: 政府資料開放授權條款-第1版 (Open Government Data License, version 1.0)

## sc-tc-regional-v1

- Source: SC-TC regional benchmark data, only after its repository data-file
  license is independently verified and pinned in a manifest.
- License: Pending verification; no derived data may be committed yet.
- Attribution: Pending verified upstream attribution.
- Modifications: None permitted before license verification.
- Output license: Pending verification.
