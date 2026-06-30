"""Classify each (entity, function) pair and print the per-entity profile.

A platform's power is a portfolio of roles. This runs the bypass-counterfactual on each function separately and
shows that every entity bundles at least one integrating function (necessary or partial) with at least one
contingent gate — the integration it earns beside the toll it holds. Amazon spans all four cells.

Run:  python org_frontier/studies/dual_function_entities/analyze_dual.py
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.contingency import contingency_test  # noqa: E402
from org_frontier.studies.dual_function_entities.entities import ENTITIES, TEMPLATES  # noqa: E402

DISPLAY = {"intrinsic": "necessary", "contingent": "contingent", "partial": "partial", "reducible": "reducible"}
INTEGRATING = {"necessary", "partial"}


def classify(template):
    labels, rules, party, dn, up, mode = TEMPLATES[template]()
    return contingency_test(rules, labels, party, downstream=dn, upstream=up, mode=mode)


def main():
    print("DUAL-FUNCTION ENTITIES — one entity, several roles, several cells")
    print("=" * 80)
    n_functions = 0
    all_ok = True
    all_dual = True
    for entity, functions in ENTITIES:
        print("  %s" % entity)
        kinds = []
        for fname, parties, _what, template, expected in functions:
            r = classify(template)
            n_functions += 1
            ok = r.kind == expected
            all_ok &= ok
            kinds.append(DISPLAY[r.kind])
            print("    %-26s %-11s margin=%.3f  (%s)%s"
                  % (fname, DISPLAY[r.kind], r.margin, parties, "" if ok else "  <-- MISMATCH"))
        has_integrating = any(k in INTEGRATING for k in kinds)
        has_gate = "contingent" in kinds
        dual = has_integrating and has_gate
        all_dual &= dual
        order = ["necessary", "partial", "contingent", "reducible"]
        profile = " + ".join(k for k in order if k in kinds)
        print("    profile: %s%s" % (profile, "" if dual else "   (not dual)"))
    print("=" * 80)
    print("  entities: %d   functions: %d" % (len(ENTITIES), n_functions))
    print("  every entity bundles an integrating function with a contingent gate: %s" % all_dual)
    print("  all functions classify as expected: %s" % all_ok)
    print("=" * 80)
    assert all_ok, "a function classified differently from its cataloged class"
    assert all_dual, "an entity was not dual (missing an integrating function or a gate)"


if __name__ == "__main__":
    main()
