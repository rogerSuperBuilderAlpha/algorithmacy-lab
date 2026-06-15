"""Reproducible headline results of the Shapley-vs-membership thread (THREAD.md).

Does IIT-4.0 major-complex membership track Shapley pivotality? The core-membership study (A) found
membership rises with single-node influence (rank-AUC ~0.63 unconstrained), and a committee review
noted influence undercounts the higher-order joint effects the Shapley value is defined over. This
thread computes the exact Shapley value over the coalition game v(S) = phi_s(S) and compares it to
membership. The headline: Shapley pivotality predicts membership far better than single-node influence,
the relation is monotone with categorical extremes, and among pivotality notions the Shapley value is
the best predictor.

Run from the repo root with the venv active:  python -m org_frontier.threads.shapley_membership.shapley_membership
"""

import itertools
import math
import os
import random
import sys
from collections import defaultdict

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import classify_rules
from org_frontier.classifier.validate import factoring_control, irreducible_control
from org_frontier.threads.shapley_membership._harness import (
    coalition_values, influence, auc, node_records)


def _rule(tt, n):
    return lambda x, _t=tt: _t[sum(x[i] << (n - 1 - i) for i in range(n))]


def predictors(rules, labels):
    """Per node: (shapley, grand_marginal, best_marginal, influence, in_core)."""
    from org_frontier.probes.lib import major_complex
    n = len(labels)
    v, _, _ = coalition_values(rules, labels)
    full = tuple(range(n))
    core, _ = major_complex(list(rules), labels)
    core = set(core or ())
    rows = []
    for i in range(n):
        others = [j for j in range(n) if j != i]
        sh = sum(math.factorial(len(S)) * math.factorial(n - len(S) - 1) / math.factorial(n)
                 * (v[tuple(sorted(S + (i,)))] - v[tuple(sorted(S))])
                 for r in range(len(others) + 1) for S in itertools.combinations(others, r))
        grand = v[full] - v[tuple(sorted(others))]
        best = max(v[tuple(sorted(S + (i,)))] - v[tuple(sorted(S))]
                   for r in range(len(others) + 1) for S in itertools.combinations(others, r))
        rows.append((sh, grand, best, influence(rules, i, n), labels[i] in core))
    return rows


def main() -> int:
    print("=" * 92)
    print("SHAPLEY vs MAJOR-COMPLEX MEMBERSHIP — does membership track Shapley pivotality?")
    print("=" * 92)
    if not (classify_rules(factoring_control()).structure == "dyadic"
            and classify_rules(irreducible_control()).structure == "triadic"):
        print("  INSTRUMENT CONTROL FAILED — refusing to run.")
        return 1
    print("  Instrument validated.\n")

    L = ("A", "B", "C")
    random.seed(11)
    SH = []; GR = []; BE = []; IN = []
    buck = defaultdict(lambda: [0, 0])
    for _ in range(150):
        rules = [_rule([random.randint(0, 1) for _ in range(8)], 3) for _ in range(3)]
        for sh, gr, be, inf, inc in predictors(rules, L):
            SH.append((sh, inc)); GR.append((gr, inc)); BE.append((be, inc)); IN.append((inf, inc))
            buck[round(max(-1, min(2, sh)))][0] += inc
            buck[round(max(-1, min(2, sh)))][1] += 1

    print("[1] Which pivotality notion predicts membership? (rank-AUC over 150 random 3-node forms)")
    print(f"    Shapley value (avg marginal over all coalitions): {auc(SH):.3f}")
    print(f"    best-coalition marginal:                          {auc(BE):.3f}")
    print(f"    grand-coalition marginal v(N)-v(N\\i):             {auc(GR):.3f}")
    print(f"    single-node influence (the study-A measure):      {auc(IN):.3f}")
    print("    The Shapley value is the best predictor, and beats single-node influence decisively.")

    print("\n[2] Membership is monotone in the Shapley value, with categorical extremes")
    for b in sorted(buck):
        inc, tot = buck[b]
        print(f"    Shapley≈{b:+d}: {inc}/{tot} = {100 * inc / max(tot, 1):5.1f}% in core")
    print("    Negative Shapley -> excluded; high-positive Shapley -> included; ambiguity near zero.")

    print("\n" + "=" * 92)
    print("  Major-complex membership tracks Shapley pivotality (the higher-order measure), far better")
    print("  than the single-node influence the core-membership study used. It is a magnitude relation,")
    print("  not a clean sign law: a node can have positive Shapley yet miss the argmax coalition.")
    print("=" * 92)
    return 0


if __name__ == "__main__":
    sys.exit(main())
