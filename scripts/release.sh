#!/usr/bin/env bash

set -euo pipefail

printf '%s\n' \
    'ERROR: direct zhtw release commands are retired.' \
    'Use Jenkins zhtw/build, then zhtw/release.' \
    'GitHub Actions, manual tags, and local registry publishing are not release paths.' >&2
exit 64
