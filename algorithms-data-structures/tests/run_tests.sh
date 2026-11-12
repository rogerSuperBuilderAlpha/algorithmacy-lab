#!/bin/sh
# Runs every board solution in the instructor key against LeetCode's examples,
# edge cases, and random inputs checked by brute force. Needs Python 3.13.
# Run from anywhere:  sh algorithms-data-structures/tests/run_tests.sh
# The #98 section prints RecursionError on chains of 1,000 or more nodes on
# purpose: it shows the limit that the key warns about. It is not a failure.
set -eu
cd "$(dirname "$0")"
PY=${PYTHON:-python3.13}
"$PY" -I extract_solutions.py
for t in test_classes_01_15.py test_classes_16_22.py test_classes_23_30.py; do
  "$PY" -s "$t" > "${t%.py}.out" 2>&1 || true
done
status=0
pass=$(grep -c ': PASS' test_classes_01_15.out || true)
fail=$(grep -c ': FAIL' test_classes_01_15.out || true)
echo "classes 1-15: $pass problems pass, $fail fail"
[ "$pass" -eq 30 ] && [ "$fail" -eq 0 ] || status=1
for f in test_classes_16_22.out test_classes_23_30.out; do
  line=$(grep '^TOTAL checks' "$f" || echo "TOTAL checks: missing")
  echo "${f%.out}: $line"
  echo "$line" | grep -q 'failed 0$' || status=1
done
if grep -q Traceback test_classes_*.out; then echo "a test file crashed"; status=1; fi
exit $status
