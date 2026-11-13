#!/bin/sh
# Runs every board solution in the instructor key against LeetCode's examples,
# edge cases, and random inputs checked by brute force. Needs Python 3.13.
# Run from anywhere:  sh algorithms-data-structures/tests/run_tests.sh
# Some sections print RecursionError on chains of 1,000 or more nodes on
# purpose: they show the limit that the key warns about. That is not a failure.
set -eu
cd "$(dirname "$0")"
PY=${PYTHON:-python3.13}
"$PY" -I extract_solutions.py
for t in test_problems_1.py test_problems_2.py test_problems_3.py test_problems_4.py; do
  "$PY" -s "$t" > "${t%.py}.out" 2>&1 || true
done
status=0
pass=$(grep -c ': PASS' test_problems_1.out || true)
fail=$(grep -c ': FAIL' test_problems_1.out || true)
echo "test_problems_1: $pass problems pass, $fail fail"
[ "$pass" -eq 24 ] && [ "$fail" -eq 0 ] || status=1
for f in test_problems_2.out test_problems_3.out; do
  line=$(grep '^TOTAL checks' "$f" || echo "TOTAL checks: missing")
  echo "${f%.out}: $line"
  echo "$line" | grep -q 'failed 0$' || status=1
done
line=$(grep '^SUMMARY' test_problems_4.out || echo "SUMMARY: missing")
echo "test_problems_4: $line"
echo "$line" | grep -q 'SUMMARY: 8 PASS of 8' || status=1
if grep -q Traceback test_problems_*.out; then echo "a test file crashed"; status=1; fi
exit $status
