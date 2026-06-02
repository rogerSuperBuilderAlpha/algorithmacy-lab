"""Paper 2 — does Φ's binary verdict reduce to a *dynamical* conditional-independence test?

The committee's sharpest objection: §2.3 shows Φ differs from a STATIC connectivity test, but a
static test is a strawman; the real rival is a *state-conditioned, dynamical* factorization test.
If a cheap dynamical test reproduces Φ's binary verdict everywhere, the IIT-4.0 MIP machinery is
decorative for the binary question. This script runs that test.

THE DYNAMICAL TEST (cheaper than IIT: no cause-effect repertoires, no φ-minimization over a
distance — only set-equality of deterministic outputs). At a reachable state s, a bipartition
{A}{B} admits a LOSSLESS CUT iff no node's next value pivots on the *other* part's current values,
holding its own part fixed at s. This is genuinely state-dependent: an edge can exist yet not pivot
at s, so a lossless cut can be found even on a connected graph — exactly where a static test fails.
A form is DYNAMICALLY IRREDUCIBLE iff some reachable state admits no lossless cut over any
bipartition (matching Φ's max-over-states "triad" verdict). We compare this to the committed Φ
verdict over all 4,096 triads, and decompose the disagreements by constant-node degeneracy.

Run:  ~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/dynamical_comparator.py
"""

import csv
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_P3 = os.path.abspath(os.path.join(_HERE, "..", "paper3_baseline"))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
for p in (_P3, _ROOT):
    if p not in sys.path:
        sys.path.insert(0, p)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from phi_instrument import tpm_from_rules  # noqa: E402
from proxy_audit.exact_phi import reachable_states  # noqa: E402
import catalog as CAT  # noqa: E402

CATALOG_CSV = os.path.join(_P3, "results", "catalog.csv")
EPS = 1e-9
BIPARTITIONS = [((0,), (1, 2)), ((1,), (0, 2)), ((2,), (0, 1))]


def _lossless_cut(rules, state, A, B):
    """True iff cutting {A}{B} loses nothing at `state`: no node in one part has its output
    changed by varying the other part's current values (own part held at `state`)."""
    cur = list(state)
    for part, other in ((A, B), (B, A)):
        for j in part:
            base = rules[j](tuple(cur))
            for mask in range(1 << len(other)):
                trial = list(cur)
                for k, idx in enumerate(other):
                    trial[idx] = (mask >> k) & 1
                if rules[j](tuple(trial)) != base:
                    return False
    return True


def dynamical_irreducible(rules, n, tpm):
    """Irreducible (triad) iff some reachable state admits no lossless cut over any bipartition."""
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        if not any(_lossless_cut(rules, state, A, B) for A, B in BIPARTITIONS):
            return True
    return False


def has_constant_node(rules, n):
    for j in range(n):
        outs = {rules[j](tuple((s >> i) & 1 for i in range(n))) for s in range(2 ** n)}
        if len(outs) == 1:
            return True
    return False


def main():
    triad_phi = []
    with open(CATALOG_CSV) as fh:
        for row in csv.DictReader(fh):
            if row["kind"] == "triad":
                triad_phi.append(float(row["max_phi"]))
    triads = list(CAT.enumerate_triads())
    assert len(triads) == len(triad_phi), (len(triads), len(triad_phi))

    N = len(triads)
    agree = 0
    phi_irr_dyn_red = []   # Φ says triad, dynamical says dyad  (apparatus does EXTRA work)
    dyn_irr_phi_red = []   # dynamical says triad, Φ says dyad  (apparatus is WEAKER)
    dyn_over_nondegen = []  # the money set: Φ=dyad, dynamical=triad, NO constant node
    for (_, label, rules, n, _, _), max_phi in zip(triads, triad_phi):
        tpm = tpm_from_rules(rules, n)
        v_phi = max_phi > EPS
        v_dyn = dynamical_irreducible(rules, n, tpm)
        if v_phi == v_dyn:
            agree += 1
        elif v_phi and not v_dyn:
            phi_irr_dyn_red.append((label, max_phi))
        else:
            dyn_irr_phi_red.append((label, max_phi))
            if not has_constant_node(rules, n):
                dyn_over_nondegen.append((label, max_phi))

    print("=" * 86)
    print(f"PAPER 2 — Φ binary verdict vs a DYNAMICAL conditional-independence test ({N} triads)")
    print("=" * 86)
    print(f"  agreement: {agree}/{N} ({100*agree/N:.1f}%)")
    print(f"  Φ=triad but dynamical=dyad (Φ stronger): {len(phi_irr_dyn_red)}")
    print(f"  dynamical=triad but Φ=dyad (Φ weaker)  : {len(dyn_irr_phi_red)}")
    print("-" * 86)
    if phi_irr_dyn_red:
        print("  EXAMPLES where the MIP machinery calls TRIAD and the cheap dynamical test calls DYAD")
        print("  (these are forms where IIT-4.0 does work a dynamical CI test does not):")
        for label, mp in phi_irr_dyn_red[:8]:
            print(f"    Φ={mp:.3f}   {label}")
    if dyn_irr_phi_red:
        print(f"  of the {len(dyn_irr_phi_red)} dynamical-over-calls, NON-DEGENERATE (no constant "
              f"node): {len(dyn_over_nondegen)}")
        print("  NON-DEGENERATE forms where Φ reduces (DYAD) but the dynamical CI test calls TRIAD —")
        print("  i.e. the MIP machinery does work NO cheaper test here reproduces, on real forms:")
        for label, mp in dyn_over_nondegen[:10]:
            print(f"    Φ={mp:.3f}   {label}")
    if agree == N:
        print("  The dynamical test reproduces Φ's binary verdict on EVERY form — for the binary")
        print("  question the MIP machinery adds no discriminating power over this cheaper test.")
    print("-" * 86)

    # Degeneracy decomposition of the STATIC-test disagreement set (connected graph yet Φ=0).
    from phi_instrument import cm_from_rules

    def undirected_separable(cm, n):
        adj = [[bool(cm[i, j] or cm[j, i]) for j in range(n)] for i in range(n)]
        seen, stack = {0}, [0]
        while stack:
            u = stack.pop()
            for v in range(n):
                if adj[u][v] and v not in seen:
                    seen.add(v); stack.append(v)
        return len(seen) < n

    connected_phi0 = []
    for (_, label, rules, n, _, _), max_phi in zip(triads, triad_phi):
        cm = cm_from_rules(rules, n)
        if (max_phi <= EPS) and (not undirected_separable(cm, n)):
            connected_phi0.append((rules, n, label))
    const = sum(1 for rules, n, _ in connected_phi0 if has_constant_node(rules, n))
    M = len(connected_phi0)
    print("DEGENERACY of the STATIC-test disagreement set (connected graph yet Φ=0):")
    print(f"  total connected-but-Φ=0 forms     : {M}  ({100*M/N:.1f}% of the family)")
    print(f"  …with >=1 constant (pinned) node   : {const}  ({100*const/M:.1f}% of the set)")
    print(f"  …non-degenerate (no constant node) : {M-const}  ({100*(M-const)/N:.1f}% of the family)")
    print("=" * 86)


if __name__ == "__main__":
    main()
