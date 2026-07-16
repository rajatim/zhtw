<!-- zhtw:disable -->
# Gemini CLI Advisory Review Attempt（2026-07-05）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`

Blind packet：
`docs/reports/annotation-blind-review-packet-it-api-cli-2026-07-05.md`

## Scope

User requested replacing the second human reviewer step with Gemini CLI review.
This report records the attempt to run Gemini CLI as an AI advisory reviewer for
the 25 `it-api-cli` cases that were in `needs_blind_review` at the time of the
attempt.

Important boundary:

- Gemini CLI output can be used as advisory evidence only.
- It must not be recorded as `human_first_pass`, `human_adjudication`, or a human
  `blind_reviewer`.
- No case should be marked `approved` from this attempt unless the maintainer
  explicitly accepts a single-human-review policy and updates the promotion rule.

## Current Result

Gemini CLI authentication has been moved away from the failing Code Assist OAuth
path and now uses Vertex AI configuration. However, Gemini CLI still hangs after
initializing the request and does not produce model output.

No backlog case was updated from Gemini CLI output.

## Attempt 1：Existing Gemini CLI Configuration

Command shape:

```bash
gemini --skip-trust --approval-mode plan -p '<review prompt>' \
  < docs/reports/annotation-blind-review-packet-it-api-cli-2026-07-05.md
```

Observed environment:

- `gemini --version`: `0.49.0`
- `~/.gemini/settings.json` auth type: `oauth-personal`

Failure:

```text
PERMISSION_DENIED:
Permission 'cloudaicompanion.companions.generateChat' denied on resource
'//cloudaicompanion.googleapis.com/projects/tw-el-gemini/locations/global'
```

Interpretation:

The installed CLI selected the Google Code Assist / OAuth path and the current
account or project does not have the required permission.

## Attempt 2：Temporary HOME With API Key Auth

Command shape:

```bash
tmp_home=$(mktemp -d)
HOME="$tmp_home" \
GEMINI_API_KEY="$GEMINI_API_KEY" \
GOOGLE_API_KEY="$GEMINI_API_KEY" \
gemini --skip-trust --approval-mode plan -p '<review prompt>' \
  < docs/reports/annotation-blind-review-packet-it-api-cli-2026-07-05.md
```

Observed environment:

- `GEMINI_API_KEY` exists.
- Key length: 39 characters.

Failure:

```text
API_KEY_INVALID:
API key not valid. Please pass a valid API key.
```

Interpretation:

The CLI reached the Gemini Developer API path, but the local API key is not valid
for `generativelanguage.googleapis.com`.

## Auth Fix Applied：Vertex AI

`~/.gemini/settings.json` was backed up to:

```text
/Users/tim/.gemini/settings.json.bak-20260705-gemini-auth
```

Then `security.auth.selectedType` was changed:

```json
{
  "security": {
    "auth": {
      "selectedType": "vertex-ai"
    }
  }
}
```

Vertex AI authentication was validated outside Gemini CLI with the same local
Google Cloud credentials:

```text
generateContent HTTP 200: Vertex auth OK
streamGenerateContent HTTP 200: Vertex stream OK
```

This confirms the Google Cloud account, ADC, project, location, Vertex API, and
streaming endpoint are usable.

## Remaining CLI Runtime Issue

After switching Gemini CLI to `vertex-ai`, the CLI no longer fails with OAuth,
Code Assist permission, or invalid API key errors. It initializes successfully:

```text
type=init, model=gemini-2.5-flash
type=message, role=user
```

But it does not emit a model response, even in an empty temporary directory and
with `gemini-2.5-flash`. The same behavior was observed with:

- installed Gemini CLI `0.49.0`
- `@google/gemini-cli@preview`
- `@google/gemini-cli@nightly`

Therefore the remaining blocker is Gemini CLI runtime/model streaming behavior,
not authentication.

## Vertex Advisory Workaround

Because Vertex AI itself works, an advisory review was generated through the
same Gemini model via the official Vertex endpoint:

- Raw JSON: `docs/reports/annotation-gemini-vertex-advisory-2026-07-05.json`
- Comparison report: `docs/reports/annotation-gemini-vertex-advisory-2026-07-05.md`
- Cases: 25
- Exact matches with first pass: 11
- Differences: 14

This is still AI advisory output, not a human blind review.

Maintainer `tim` later reviewed the 14 differences and accepted the Gemini
advisory version. Those 14 cases were recorded as `human_adjudication`; Gemini
remains recorded under `review.ai_advisory`, not as `blind_reviewer`.

## Current Backlog State

The 25 `it-api-cli` cases are now:

```text
review.status = approved
11 cases: review.expected_source = human_first_pass
14 cases: review.expected_source = human_adjudication
review.first_reviewer = tim
review.blind_reviewer = ""
14 cases: review.adjudicator = tim
25 cases: review.ai_advisory.reviewer = gemini_vertex
```

Promotion-ready approved cases: `25`.

## Next Step

To complete a Gemini CLI advisory review specifically through `gemini`:

1. Keep `~/.gemini/settings.json` on `vertex-ai`, or replace the invalid
   `GEMINI_API_KEY` with a valid Gemini Developer API key and switch auth to
   `gemini-api-key`.
2. Resolve the CLI runtime hang observed after request initialization.
3. Re-run the same blind packet through Gemini CLI.
4. Compare Gemini output against `review.expected`.
5. Record the comparison as advisory evidence.

Do not treat the failed CLI attempt or Vertex advisory workaround as reviewer
approval.
