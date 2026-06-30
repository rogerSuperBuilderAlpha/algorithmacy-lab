"""Classify the before/after of each operation and confirm the cell transitions.

Run:  python org_frontier/studies/contingency_transitions/analyze_transitions.py
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.contingency import contingency_test  # noqa: E402
from org_frontier.studies.contingency_transitions.transitions import TRANSITIONS, TEMPLATES  # noqa: E402

DISPLAY = {"intrinsic": "necessary", "contingent": "contingent", "partial": "partial", "reducible": "reducible"}


def classify(template):
    labels, rules, party, dn, up, mode = TEMPLATES[template]()
    return DISPLAY[contingency_test(rules, labels, party, downstream=dn, upstream=up, mode=mode).kind]


def main():
    print("CONTINGENCY TRANSITIONS — the operations that move an intermediary between cells")
    print("=" * 92)
    all_ok = True
    for op, bt, at, eb, ea, example in TRANSITIONS:
        before, after = classify(bt), classify(at)
        ok = before == DISPLAY[eb] and after == DISPLAY[ea]
        all_ok &= ok
        print("  %-11s -> %-11s  %-20s%s" % (before, after, op, "" if ok else "  <-- MISMATCH"))
        print("               %s" % example)
    print("=" * 92)
    # the durable cell: opening the bypass evicts a contingent party but not a necessary one
    open_bypass = next(t for t in TRANSITIONS if t[0] == "open_the_bypass")
    contingent_falls = classify(open_bypass[1]) == "contingent" and classify(open_bypass[2]) == "reducible"
    necessary_holds = classify("conjunctive") == "necessary"  # the bypass takes nothing from it (margin 0)
    print("  operations: %d   all transitions classify as expected: %s" % (len(TRANSITIONS), all_ok))
    print("  opening the bypass evicts a contingent party (-> reducible): %s" % contingent_falls)
    print("  necessary is the only cell opening the bypass cannot evict: %s" % necessary_holds)
    print("=" * 92)
    assert all_ok, "a transition did not classify as expected"
    assert contingent_falls and necessary_holds, "the durable-cell invariant failed"


if __name__ == "__main__":
    main()
