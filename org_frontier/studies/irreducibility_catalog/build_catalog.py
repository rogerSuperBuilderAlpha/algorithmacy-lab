"""Classify every catalog entry through the bypass-counterfactual and render the catalog table.

Reads the entries and structural templates from catalog_entries.py, runs `contingency_test` on each, prints a
deterministic table and summary, and asserts each entry classifies as cataloged. Registered as a reproduce
check, so a model that drifts from its catalogued class fails CI.

The headline dichotomy is necessary (the classifier's "intrinsic") vs contingent; partial and reducible fill
the spectrum.

Run:  python org_frontier/studies/irreducibility_catalog/build_catalog.py
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.contingency import contingency_test  # noqa: E402
from org_frontier.studies.irreducibility_catalog.catalog_entries import ENTRIES, TEMPLATES  # noqa: E402

DISPLAY = {"intrinsic": "necessary", "contingent": "contingent", "partial": "partial", "reducible": "reducible"}
ORDER = ["intrinsic", "contingent", "partial", "reducible"]


def classify(entry):
    labels, rules, party, downstream, upstream, mode = TEMPLATES[entry["template"]]()
    return contingency_test(rules, labels, party, downstream=downstream, upstream=upstream, mode=mode)


def main():
    print("IRREDUCIBILITY CATALOG — necessary and contingent irreducible triads")
    print("=" * 84)
    print("  entries: %d   instrument: bypass-counterfactual (classifier/contingency.py)" % len(ENTRIES))
    print("  " + "-" * 80)
    print("  %-22s %-14s %-22s %-11s %6s" % ("entry", "domain", "constraint_type", "class", "margin"))
    counts = {k: 0 for k in ORDER}
    all_ok = True
    for e in ENTRIES:
        r = classify(e)
        counts[r.kind] = counts.get(r.kind, 0) + 1
        ok = r.kind == e["expected"]
        all_ok &= ok
        flag = "" if ok else "  <-- MISMATCH (expected %s)" % e["expected"]
        print("  %-22s %-14s %-22s %-11s %6.3f%s"
              % (e["name"], e["domain"][:14], e["constraint_type"][:22], DISPLAY[r.kind], r.margin, flag))
    print("  " + "-" * 80)
    print("  by class: necessary=%d  contingent=%d  partial=%d  reducible=%d"
          % (counts["intrinsic"], counts["contingent"], counts["partial"], counts["reducible"]))
    print("  necessary vs contingent: %d vs %d" % (counts["intrinsic"], counts["contingent"]))
    print("  all entries classify as cataloged: %s" % all_ok)
    print("=" * 84)
    assert all_ok, "a catalog entry classified differently from its cataloged class"


if __name__ == "__main__":
    main()
