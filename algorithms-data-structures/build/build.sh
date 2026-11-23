#!/bin/sh
# Builds the four course documents (.docx and .pdf) from the Markdown in source/.
# Run from anywhere:  sh algorithms-data-structures/build/build.sh
# Needs pandoc 3, python3 with python-docx, and LibreOffice (soffice).
set -eu

HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
SRC="$ROOT/source"
OUT="$ROOT"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

# The draft label appears in every footer. Change it here, in one place.
LABEL="Draft 3, rewritten by Claude on 12 November 2026"
BASE="Algorithms & Data Structures  |  Professor Roger Hunt  |  $LABEL"

SOFFICE=$(command -v soffice || echo /Applications/LibreOffice.app/Contents/MacOS/soffice)

python3 "$HERE/make_reference.py" "$BASE" "$TMP/ref.docx"
python3 "$HERE/make_reference.py" "$BASE  |  Instructor key" "$TMP/ref-key.docx"

pandoc "$SRC/syllabus.md" -o "$OUT/ADS_Syllabus_Draft.docx" \
  --reference-doc "$TMP/ref.docx" --syntax-highlighting=none --lua-filter "$HERE/filters/common.lua"

pandoc "$SRC/take_homes.md" -o "$OUT/ADS_Take_Homes.docx" \
  --reference-doc "$TMP/ref.docx" --syntax-highlighting=none --lua-filter "$HERE/filters/take_homes.lua" \
  --lua-filter "$HERE/filters/common.lua"

pandoc "$SRC/board_intro.md" "$SRC/problems.md" -o "$OUT/ADS_In_Class_Board_Problems.docx" \
  --reference-doc "$TMP/ref.docx" --syntax-highlighting=none -M mode=board --lua-filter "$HERE/filters/problems.lua" \
  --lua-filter "$HERE/filters/common.lua"

pandoc "$SRC/key_intro.md" "$SRC/problems.md" -o "$OUT/ADS_In_Class_Solutions.docx" \
  --reference-doc "$TMP/ref-key.docx" --syntax-highlighting=none -M mode=key --lua-filter "$HERE/filters/problems.lua" \
  --lua-filter "$HERE/filters/common.lua"

for f in ADS_Syllabus_Draft ADS_Take_Homes ADS_In_Class_Board_Problems ADS_In_Class_Solutions; do
  "$SOFFICE" --headless --convert-to pdf --outdir "$OUT" "$OUT/$f.docx" >/dev/null 2>&1
  printf '%s: %s pages\n' "$f" "$(pdfinfo "$OUT/$f.pdf" 2>/dev/null | awk '/^Pages/ {print $2}')"
done
