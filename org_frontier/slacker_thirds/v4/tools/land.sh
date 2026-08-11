#!/usr/bin/env bash
# Wait for a PR's checks and merge ONLY if they pass.
#
# Written after merging #638 into a red contrib. The loop in use until then waited
# for checks to stop being pending and then merged with --admin unconditionally, so
# "finished" was silently doing the work of "passed." Six green PRs hid the flaw.
#
# Usage: v4/tools/land.sh <pr-number> [--merge|--squash]

set -euo pipefail
PR="${1:?usage: land.sh <pr-number> [--merge|--squash]}"
MODE="${2:---squash}"

echo "waiting on checks for #$PR"
until ! gh pr checks "$PR" 2>/dev/null | grep -q pending; do sleep 20; done

gh pr checks "$PR" || true

if gh pr checks "$PR" 2>/dev/null | grep -qE '\bfail\b'; then
  echo
  echo "REFUSING TO MERGE: #$PR has failing checks."
  echo "If the failure is in someone else's area, it is still a red branch, and"
  echo "landing on top of it makes the next person's bisect harder, not easier."
  exit 1
fi

gh pr merge "$PR" "$MODE" --admin --delete-branch
echo "merged #$PR"
