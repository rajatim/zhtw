<!-- zhtw:disable -->
# Public Benchmark Third-party Reproduction

This procedure lets an outside reviewer reproduce zhtw's two public secondary
benchmark tracks in a clean worktree. It does not provide or test the private
Blind-v2 reference answers.

## Scope

- UD Chinese GSD/GSDSimp: 4,997 sentence pairs.
- NAER computer terminology: 775 accepted evaluation cases.
- Frozen source commit: `4b7f0e66fa0262021d0ec8e37acfae881b06bc4b`.
- Published reports dated 2026-07-31.

These tracks are supporting evidence only. They do not replace the private
Blind-v2 primary market comparison.

## Requirements

- The reviewer was not involved in building or annotating this benchmark.
- Git and `uv` are installed.
- The machine can download the locked Python dependencies.
- The repository has the full Git history, including the frozen source commit.

## Run

From a clean clone or fork of zhtw:

```bash
uv sync --frozen --extra dev
uv run python scripts/reproduce_public_benchmarks.py \
  --operator "YOUR NAME OR HANDLE" \
  --organization "OPTIONAL ORGANIZATION" \
  --independent \
  --output /tmp/zhtw-public-benchmark-attestation.json
```

The command creates a temporary detached worktree at the frozen source commit,
runs both public benchmarks, compares their full score objects and dataset
hashes with the published reports, and removes the worktree. A passing result
does not depend on private benchmark files.

The complete report hashes can differ across operating systems because the
reports include environment details. Acceptance requires matching score hashes
and dataset metadata, not matching environment provenance bytes.

Validate the generated file before submitting it:

```bash
uv run python scripts/validate_public_benchmark_attestation.py \
  /tmp/zhtw-public-benchmark-attestation.json
```

## Submit Evidence

Open a **Benchmark reproduction** issue and include the generated JSON
attestation. Report every command change, dependency change, or failed check.
Do not mark `relationship` as `independent_third_party` if you worked on the
benchmark, its annotations, or its published report.

The project accepts the reproduction only when:

1. Both tracks report `passed: true`.
2. The source worktree is clean.
3. The source commit is the full frozen SHA above.
4. The reviewer is independent from the benchmark work.
5. The attestation contains no private Blind-v2 material.
