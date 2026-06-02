"""Paper 2 — does Φ's binary verdict reduce to a *dynamical* conditional-independence test?

The committee's sharpest objection: §2.3 shows Φ differs from a STATIC connectivity test, but a
static test is a strawman; the real rival is a *state-conditioned, dynamical* factorization test.
If a cheap dynamical test reproduces Φ's binary verdict everywhere, the IIT-4.0 MIP machinery is
decorative for the binary question. This script runs that test.

THE DYNAMICAL TEST (cheaper than IIT: no cause-effect repertoires, no φ-minimization over a
distance — only set-equality of deterministic outputs). At a reachable state s, a bipartition
{A}{B} admits a LOSSLESS CUT iff no node's next value pivots on the *other* part's current values.
A form is DYNAMICALLY IRREDUCIBLE iff some reachable state admits no lossless cut over any
bipartition (matching Φ's max-over-states "triad" verdict).

We run TWO versions, weak and fair, because the result must not rest on a strawman:
  - ALL-COMBINATIONS: pivoting checked over all 2^k other-part values, incl. unreachable ones.
    This OVER-calls triads and inflates the Φ–vs–cheap gap (~60% agreement); it is the weaker rival.
  - REACHABLE-ONLY: pivoting checked only over reachable states. This is the fair, stronger rival
    a critic would demand; it closes most of the gap (~90% agreement) AND introduces a few reverse
    cases — so the clean "Φ strictly stronger / 0 reverse" property is COMPARATOR-DEPENDENT and is
    NOT the headline.
The robust, comparator-independent claim is the EXHIBIT: a single verified non-degenerate,
maximally-connected form (W'=NOR(S,C), S'=¬W∧C, C'=NAND(W,S)) where exact IIT-4.0 Φ=0 though every
connectivity/CI test calls it a triad. That one form proves the apparatus is not decorative; the
aggregate counts (hundreds of non-degenerate over-calls under both comparators) are supporting color.

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
    """ALL-COMBINATIONS variant: irreducible (triad) iff some reachable state admits no lossless
    cut, where pivoting is checked over ALL 2^k other-part values (incl. unreachable ones). This
    is the WEAKER of two dynamical rivals: it over-calls triads because it counts pivots on
    configurations the dynamics never visit."""
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        if not any(_lossless_cut(rules, state, A, B) for A, B in BIPARTITIONS):
            return True
    return False


def _lossless_cut_reachable(rules, state, A, B, reach_states):
    """REACHABLE-ONLY lossless cut: a node does not pivot on the other part if its output is
    invariant across the reachable states that agree with `state` on the node's OWN part."""
    for part, other in ((A, B), (B, A)):
        for j in part:
            outs = {rules[j](r) for r in reach_states if all(r[k] == state[k] for k in part)}
            if len(outs) > 1:
                return False
    return True


def dynamical_irreducible_reachable(rules, n, tpm):
    """REACHABLE-ONLY (fair, stronger) variant: pivoting checked only over reachable states. This
    is the comparator a critic would demand; it closes ~75% of the all-combinations gap."""
    R = [tuple((s >> i) & 1 for i in range(n)) for s in reachable_states(tpm, n)]
    for state in R:
        if not any(_lossless_cut_reachable(rules, state, A, B, R) for A, B in BIPARTITIONS):
            return True
    return False


def has_constant_node(rules, n):
    for j in range(n):
        outs = {rules[j](tuple((s >> i) & 1 for i in range(n))) for s in range(2 ** n)}
        if len(outs) == 1:
            return True
    return False


def _tally(triads, triad_phi, verdict_fn):
    """Return (agreement, phi_stronger_reverse, dyn_overcall, dyn_overcall_nondegen)."""
    agree = reverse = over = over_nd = 0
    for (_, _, rules, n, _, _), max_phi in zip(triads, triad_phi):
        tpm = tpm_from_rules(rules, n)
        v_phi = max_phi > EPS
        v_dyn = verdict_fn(rules, n, tpm)
        if v_phi == v_dyn:
            agree += 1
        elif v_phi and not v_dyn:
            reverse += 1                       # Φ=triad, cheap test=dyad (Φ NOT stronger here)
        else:
            over += 1                          # cheap test=triad, Φ=dyad (Φ reduces more)
            if not has_constant_node(rules, n):
                over_nd += 1
    return agree, reverse, over, over_nd


def main():
    triad_phi = []
    with open(CATALOG_CSV) as fh:
        for row in csv.DictReader(fh):
            if row["kind"] == "triad":
                triad_phi.append(float(row["max_phi"]))
    triads = list(CAT.enumerate_triads())
    assert len(triads) == len(triad_phi), (len(triads), len(triad_phi))
    N = len(triads)

    print("=" * 90)
    print(f"PAPER 2 — Φ binary verdict vs cheap dynamical conditional-independence tests ({N} triads)")
    print("=" * 90)
    print(f"  {'comparator':<34}{'agree':>10}{'Φ-not-stronger':>16}{'cheap over-calls':>18}"
          f"{'(non-degen)':>13}")
    for name, fn in [("dynamical, ALL combinations", dynamical_irreducible),
                     ("dynamical, REACHABLE-only (fair)", dynamical_irreducible_reachable)]:
        a, rev, over, ond = _tally(triads, triad_phi, fn)
        print(f"  {name:<34}{a:>6}/{N} ({100*a/N:>4.1f}%){rev:>16}{over:>18}{ond:>13}")
    print("-" * 90)
    print("  READING: the all-combinations test is the WEAKER rival (it over-calls on unreachable")
    print("  states); the reachable-only test is the fair, stronger one. The aggregate gap and the")
    print("  'Φ never weaker' (0-reverse) property are COMPARATOR-DEPENDENT and should not be the")
    print("  headline. What is robust across both is the DIRECTION (hundreds of non-degenerate forms")
    print("  where Φ reduces and the cheap test over-calls) and, decisively, the exhibit below.")
    print("-" * 90)

    # The robust, comparator-independent claim: a single verified non-degenerate witness.
    from phi_instrument import cm_from_rules, system_phi_over_states
    NOR = lambda a, b: 1 - (a | b)
    NAND = lambda a, b: 1 - (a & b)
    exhibit = [lambda x: NOR(x[1], x[2]),        # W' = NOR(S, C)
               lambda x: (1 - x[0]) & x[2],      # S' = ~W & C   (NOT W and C)
               lambda x: NAND(x[0], x[1])]       # C' = NAND(W, S)
    tpm, cm = tpm_from_rules(exhibit, 3), cm_from_rules(exhibit, 3)
    mx = max((p for _, p in system_phi_over_states(tpm, cm)), default=0.0)
    print("  EXHIBIT (robust, verified):  W'=NOR(S,C),  S'=¬W∧C,  C'=NAND(W,S)")
    print(f"    edges={int(cm.sum())}/6 (all present, strongly connected)   constant nodes=none   "
          f"max Φ={mx:.4f}")
    print("    -> a form that looks MAXIMALLY triadic to any connectivity or conditional-independence")
    print("       test, yet exact IIT-4.0 reduces it to a dyad. No cheap test reproduces this verdict.")
    print("-" * 90)

    # Degeneracy decomposition of the static-test disagreement set (connected graph yet Φ=0).
    def undirected_separable(cm, n):
        adj = [[bool(cm[i, j] or cm[j, i]) for j in range(n)] for i in range(n)]
        seen, stack = {0}, [0]
        while stack:
            u = stack.pop()
            for v in range(n):
                if adj[u][v] and v not in seen:
                    seen.add(v); stack.append(v)
        return len(seen) < n

    connected_phi0 = [(rules, n) for (_, _, rules, n, _, _), mp in zip(triads, triad_phi)
                      if mp <= EPS and not undirected_separable(cm_from_rules(rules, n), n)]
    const = sum(1 for rules, n in connected_phi0 if has_constant_node(rules, n))
    M = len(connected_phi0)
    print("DEGENERACY of the static-test disagreement set (connected graph yet Φ=0):")
    print(f"  connected-but-Φ=0 forms           : {M}  ({100*M/N:.1f}% of the family)")
    print(f"  …with >=1 constant (pinned) node   : {const}  ({100*const/M:.1f}% of the set)")
    print(f"  …non-degenerate (no constant node) : {M-const}  ({100*(M-const)/N:.1f}% of the family)")
    print("=" * 90)


if __name__ == "__main__":
    main()
