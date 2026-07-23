<!-- zhtw:disable -->
# Blind-v2 Source Classification Synthesis 005

Status: confirmed by maintainer `tim` on 2026-07-23

Source: MASSIVE 1.0 `zh-CN`

## Summary

- Total: 100
- Exact Codex/Gemini matches: 35
- Review queue: 65
- Recommended eligible: 98
- Recommended excluded: 2
- Recommended domains: 54 social/daily, 33 UI/i18n, 8 formal/news, 3 high-stakes
- Recommended risks: 47 baseline, 20 candidate-gap, 31 over-conversion guard
- Selection basis: 35 agreement, 16 Codex, 45 Gemini, 4 field-level hybrid

Gemini's accepted run covered 100/100 IDs with zero tool calls and zero API
errors. Two earlier attempts are retained in the Gemini advisory as rejected:
one used `write_file`, and one exposed a Gemini CLI 0.52.0 deny-all policy bug.

## Domain Rule

Voice-assistant context alone does not make every utterance UI/i18n. The
synthesis uses:

- `ui_i18n`: direct manipulation of lists, email, calendar, playback,
  reminders, alarms, or device state.
- `social_daily`: weather, transport, people, places, shopping, cooking, and
  general questions.
- `formal_news`: explicit news retrieval.
- `high_stakes`: medical or financial subject matter.

## Eligibility

Exclude:

- `15939`: asks to send “the following message” but contains no message.
- `6887`: isolated “好” has no independently reviewable conversion context.

Keep after Codex re-review:

- `10952`: unusual, but “delete the form titled 踢球” remains independently
  interpretable from the input alone.
- `7423`: “星期一的会议” is a conventional, understandable assistant query
  fragment.

## Script

- `2685` is `mixed` because it contains the Latin wake word `olly`.
- `1193` and `14778` remain `simplified`; their wake words are Chinese
  transliterations, not mixed-script text.

## Advisory Selection

Exact agreement (35):

`10221, 10514, 11108, 11570, 11601, 11830, 11904, 12226, 12560, 12682,
12830, 13074, 13225, 13416, 14482, 15057, 15238, 15605, 16166, 1983,
2920, 3318, 3452, 3795, 4674, 4845, 5561, 5695, 6782, 6821, 6847,
7230, 7256, 7491, 7902`

Adopt Codex (16):

`12393, 12903, 13301, 13540, 14056, 14337, 14778, 15127, 15939, 1866,
2248, 2651, 2992, 5601, 5869, 6887`

Adopt Gemini (45):

`10144, 10276, 10467, 10615, 10635, 10952, 11084, 11438, 11816, 12301,
14413, 15225, 15448, 15870, 16001, 16168, 162, 16436, 16682, 17000,
17031, 17108, 2096, 2260, 2685, 3061, 3399, 3777, 5355, 6965, 709,
7168, 7179, 7344, 7423, 748, 7595, 7718, 787, 8077, 8116, 8225,
8769, 9099, 961`

Field-level hybrid (4):

- `10872`: UI/i18n domain, baseline risk.
- `118`: social/daily domain, baseline risk.
- `1193`: UI/i18n domain, simplified script, over-conversion risk.
- `635`: UI/i18n domain, baseline risk.

## Human Gate

These recommendations began as AI advisory. Maintainer `tim` confirmed the
complete synthesis on 2026-07-23 using `batch_human_confirmation`: 98 eligible
cases were promoted and 2 ineligible cases were excluded.
