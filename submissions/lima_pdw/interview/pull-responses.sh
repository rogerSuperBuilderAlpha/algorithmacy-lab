#!/usr/bin/env bash
#
# Pull submitted interviews into the working tree so they can be read and coded
# here, without any of them entering git.
#
#   ./pull-responses.sh          # sync new files into ./responses/
#   ./pull-responses.sh --list   # show what is in the bucket, download nothing
#
# ./responses/ is gitignored. This repository is public; a response that reaches
# a commit is a response that has been published. Check `git status` before
# committing anything from this directory.

set -euo pipefail

BUCKET="${INTAKE_BUCKET:-pitch-rise-interview-intake}"
DEST="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/responses"

command -v gcloud >/dev/null 2>&1 || { echo "gcloud not found." >&2; exit 1; }

if [[ "${1:-}" == "--list" ]]; then
  gcloud storage ls -l "gs://${BUCKET}/" 2>/dev/null || {
    echo "Could not list gs://${BUCKET}/. Check credentials and project." >&2; exit 1; }
  exit 0
fi

mkdir -p "$DEST"

# rsync rather than cp: re-running is cheap and does not re-download.
gcloud storage rsync "gs://${BUCKET}/" "$DEST/" --recursive 2>/dev/null || {
  echo "Sync failed. Check credentials and that gs://${BUCKET}/ exists." >&2; exit 1; }

count=$(find "$DEST" -name '*.md' -type f | wc -l | tr -d ' ')
echo "${count} response(s) in ${DEST}"

# A gitignore rule already covers this, but a stray `git add -f` should not be
# one keystroke away from publishing an interview.
if git -C "$DEST" check-ignore -q . 2>/dev/null; then
  echo "responses/ is gitignored — good."
else
  echo "WARNING: responses/ is NOT gitignored. Do not commit until that is fixed." >&2
fi
