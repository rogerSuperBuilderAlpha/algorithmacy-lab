"""Probe 102 (A4) — is there an exact cheap-CES predicate for the verdict?

Question: CES counts predict the verdict at combined AUC 1.0 (Probe 93), and triadic forms carry far more
relations (Probe 36). Is a single CES count an exact verdict equivalent — a cheap predicate with zero
error, not just a good ranker? Hypothesis: yes; a threshold on relations or higher-order distinctions
separates the verdict perfectly. Method: compute the CES suite on a reachable state of each corpus form;
for each candidate predicate (n_relations ≥ k, n_distinctions ≥ k, frac_higher_order > 0, max_order ≥ 2),
count errors against the exact verdict; report any zero-error predicate.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_ces_predicate
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules, cm_from_rules
from org_frontier.corpus.population import enumerate_family
from foundations.proxy_audit.exact_phi import reachable_states
from foundations.structure_suite.suite import extract_suite


def main():
    print("PROBE 102 (A4) — exact cheap-CES predicate search")
    print("=" * 64)
    suites, y = [], []
    for _, rules in enumerate_family():
        sbn = tpm_from_rules(rules)
        rs = reachable_states(sbn, 3)
        if not rs:
            continue
        state = [(rs[0] >> i) & 1 for i in range(3)]
        s = extract_suite(sbn, cm_from_rules(rules), 3, state)
        if s is None:
            continue
        suites.append(s)
        y.append(int(classify_rules(rules, labels=("W", "S", "C")).structure == "triadic"))
    y = np.array(y)
    print(f"  {len(y)} forms ({int(y.sum())} triadic)")

    def report(name, pred):
        pred = np.array(pred, int)
        err = int((pred != y).sum())
        fp = int(((pred == 1) & (y == 0)).sum())
        fn = int(((pred == 1) & (y == 0)).sum())
        fn = int(((pred == 0) & (y == 1)).sum())
        tag = "  *** EXACT ***" if err == 0 else ""
        print(f"  {name:<28}errors={err:<4}(fp={fp}, fn={fn}){tag}")
        return err

    print(f"  {'predicate':<28}result")
    best = None
    for k in range(1, 12):
        e = report(f"n_relations >= {k}", [s["n_relations"] >= k for s in suites])
        if best is None or e < best[1]:
            best = (f"n_relations>={k}", e)
    for k in range(1, 8):
        report(f"n_distinctions >= {k}", [s["n_distinctions"] >= k for s in suites])
    report("frac_higher_order > 0", [s["frac_higher_order"] > 0 for s in suites])
    report("max_order >= 2", [s["max_order"] >= 2 for s in suites])
    print("=" * 64)
    print("  Reading: a predicate with zero errors is an exact cheap test for the verdict — the verdict")
    print("  reduces to counting cause-effect structure, no partition search needed. If the best")
    print("  predicate still errs, CES counts rank the verdict but do not define it.")
    print("=" * 64)


if __name__ == "__main__":
    main()
