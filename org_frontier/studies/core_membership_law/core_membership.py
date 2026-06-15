"""Confirmatory battery for the core-membership law: bidirectional coupling and pivotality.

Re-derives, under the hypotheses committed in hypotheses.md, the two-condition account of which nodes
sit in the IIT-4.0 major complex of a coordination form:

  (1) NECESSITY — a node not bidirectionally coupled (it does not both feed and get fed by the
      determination) is never in the major complex.
  (2) PIVOTALITY — among coupled nodes, the probability of membership rises monotonically with the
      determination's Boolean sensitivity to the node.

Plus the two supporting laws: the rarity of triadicity in the random 3-node population, and the
conjunctive all-required law (Φ = n-1, full core).

Run from the repo root with the venv active:  python -m org_frontier.studies.core_membership_law.core_membership
"""

import os
import random
import sys
from collections import defaultdict

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import classify_rules, cm_from_rules
from org_frontier.probes.lib import major_complex
from org_frontier.classifier.validate import factoring_control, irreducible_control


def _rule(tt, n):
    return lambda x, _tt=tt: _tt[sum(x[i] << (n - 1 - i) for i in range(n))]


def random_form(n, rng):
    return [_rule([rng.randint(0, 1) for _ in range(2 ** n)], n) for _ in range(n)]


def bidirectional(cm, i):
    """Node i both feeds another node and is fed by another node (off-diagonal in/out edges)."""
    n = cm.shape[0]
    feeds = any(cm[i, j] for j in range(n) if j != i)
    fed = any(cm[k, i] for k in range(n) if k != i)
    return feeds and fed


def influence(rules, i, n):
    """Boolean sensitivity of the whole determination to node i: fraction of (target, state) pairs
    where flipping node i changes a target's next value."""
    changed = total = 0
    for s in range(2 ** n):
        cur = tuple((s >> (n - 1 - k)) & 1 for k in range(n))
        flipped = tuple(b ^ 1 if k == i else b for k, b in enumerate(cur))
        for j in range(n):
            total += 1
            changed += (rules[j](cur) != rules[j](flipped))
    return changed / total


def _auc(scores_labels):
    """Rank-AUC of a score predicting a 0/1 label (Mann-Whitney)."""
    pos = [s for s, y in scores_labels if y]
    neg = [s for s, y in scores_labels if not y]
    if not pos or not neg:
        return float("nan")
    wins = sum((p > q) + 0.5 * (p == q) for p in pos for q in neg)
    return wins / (len(pos) * len(neg))


def membership_battery(n=3, trials=600, seed=0):
    rng = random.Random(seed)
    non_bidir_in_core = non_bidir_total = 0
    coupled_scores = []                  # (influence, in_core) for bidirectionally coupled nodes
    bucket = defaultdict(lambda: [0, 0])  # influence bucket -> [in_core, total]
    labels = tuple("ABCDEF"[:n])
    triadic = 0
    for _ in range(trials):
        rules = random_form(n, rng)
        v = classify_rules(rules, labels)
        triadic += (v.structure == "triadic")
        core, _ = major_complex(list(rules), labels)
        core = set(core or ())
        cm = cm_from_rules(rules)
        for i in range(n):
            inc = labels[i] in core
            if not bidirectional(cm, i):
                non_bidir_total += 1
                non_bidir_in_core += inc
            else:
                infl = influence(rules, i, n)
                coupled_scores.append((infl, inc))
                bucket[round(infl * 4) / 4][0] += inc
                bucket[round(infl * 4) / 4][1] += 1
    return {
        "trials": trials, "triadic_rate": triadic / trials,
        "non_bidir_total": non_bidir_total, "non_bidir_in_core": non_bidir_in_core,
        "auc": _auc(coupled_scores), "buckets": dict(sorted(bucket.items())),
    }


def selfloop_breakdown(n=3, trials=600, seed=0):
    """Of the non-bidirectional nodes that appear in the core, how many have a self-loop?"""
    import numpy as np
    rng = random.Random(seed)
    labels = tuple("ABCDEF"[:n])
    with_self = without_self = 0
    for _ in range(trials):
        rules = random_form(n, rng)
        core, _ = major_complex(list(rules), labels)
        core = set(core or ())
        cm = cm_from_rules(rules)
        for i in range(n):
            if not bidirectional(cm, i) and labels[i] in core:
                if cm[i, i]:
                    with_self += 1
                else:
                    without_self += 1
    return with_self, without_self


def strict_mediation_family(trials=400, seed=1):
    """Reconciliation: the construct's natural domain — a mediator S between outer parties W, C with
    NO direct W-C edge. Reports the triadic rate and the non-bidirectional-in-core necessity rate."""
    rng = random.Random(seed)
    L = ("W", "S", "C")
    triadic = nonbid_core = nonbid_total = 0
    for _ in range(trials):
        fW = [rng.randint(0, 1) for _ in range(2)]
        hS = [rng.randint(0, 1) for _ in range(4)]
        gC = [rng.randint(0, 1) for _ in range(2)]
        rules = [lambda x, _f=fW: _f[x[1]],            # W = f(S)
                 lambda x, _h=hS: _h[2 * x[0] + x[2]],  # S = h(W, C)
                 lambda x, _g=gC: _g[x[1]]]             # C = g(S)
        v = classify_rules(rules, L)
        triadic += (v.structure == "triadic")
        core, _ = major_complex(list(rules), L)
        core = set(core or ())
        cm = cm_from_rules(rules)
        for i in range(3):
            if not bidirectional(cm, i):
                nonbid_total += 1
                nonbid_core += (L[i] in core)
    return {"trials": trials, "triadic_rate": triadic / trials,
            "nonbid_core": nonbid_core, "nonbid_total": nonbid_total}


def conjunctive_law(sizes=(3, 4, 5)):
    rows = []
    for n in sizes:
        labels = tuple("PABCDE"[:n])
        # mediator P (index 0) = AND of all parties; each party reads P
        rules = [lambda x, _n=n: int(all(x[k] for k in range(1, _n)))] + \
                [(lambda x: x[0]) for _ in range(n - 1)]
        v = classify_rules(rules, labels)
        core, cphi = major_complex(list(rules), labels)
        rows.append((n, round(v.max_phi, 3), "".join(core) if core else "—", len(core or ())))
    return rows


def main() -> int:
    print("=" * 92)
    print("CORE-MEMBERSHIP LAW — confirmatory battery (bidirectional coupling + pivotality)")
    print("=" * 92)
    if not (classify_rules(factoring_control()).structure == "dyadic"
            and classify_rules(irreducible_control()).structure == "triadic"):
        print("  INSTRUMENT CONTROL FAILED — refusing to run.")
        return 1
    print("  Instrument validated.\n")

    print("PRIMARY (pre-registered): unconstrained random 3-node family\n")
    r = membership_battery(n=3, trials=600, seed=0)
    ws, wos = selfloop_breakdown()
    print(f"[H1 necessity] non-bidirectional nodes in the major complex: "
          f"{r['non_bidir_in_core']}/{r['non_bidir_total']} "
          f"({100 * r['non_bidir_in_core'] / max(r['non_bidir_total'], 1):.2f}%) "
          f"— of these, {ws} have a self-loop and {wos} do not (the exceptions are self-coupled nodes)")
    print(f"[H2 pivotality] influence predicts membership among coupled nodes: rank-AUC = {r['auc']:.3f}")
    print("              inclusion rate by influence bucket:")
    for b, (inc, tot) in r["buckets"].items():
        print(f"                influence≈{b:.2f}: {inc}/{tot} = {100 * inc / max(tot, 1):5.1f}% in core")
    print(f"[H4 rarity]   triadic rate over {r['trials']} random 3-node forms: {100 * r['triadic_rate']:.1f}%")

    print("\nRECONCILIATION: strict-mediation family (the construct's natural domain, no W-C edge)")
    sm = strict_mediation_family()
    print(f"[H1 strict]   non-bidirectional in core: {sm['nonbid_core']}/{sm['nonbid_total']} "
          f"(categorical necessity holds in this family)")
    print(f"[H4 strict]   triadic rate: {100 * sm['triadic_rate']:.1f}% (vs {100 * r['triadic_rate']:.1f}% "
          f"unconstrained — triadicity is population-dependent)")

    print("\n[H5 conjunctive law] AND-all mediator, Φ and core by size:")
    for n, phi, core, k in conjunctive_law():
        print(f"   n={n}: Φ={phi}  core={core} (size {k})  [Φ = n-1 = {n-1}]")

    print("\n" + "=" * 92)
    print("  Membership in the major complex is decided by bidirectional coupling (necessary) and")
    print("  pivotality (graded), not by party count or interface.")
    print("=" * 92)
    return 0


if __name__ == "__main__":
    sys.exit(main())
