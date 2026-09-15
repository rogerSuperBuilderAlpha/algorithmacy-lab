"""Probe — Simmel H2: the decisive step from two to three.

Question.  Simmel (1902, II) holds the first numerical step decisive and later ones secondary. Over
           mutual conjunctive cliques of n = 2..5, is the Φ increment largest at 2→3 and diminishing after?
Hypothesis. H2 (Simmel): ΔΦ(2→3) > ΔΦ(3→4) ≥ ΔΦ(4→5).
Method.    Exact whole-system Φ_MIP and major complex of clique(n), each node the AND of all others.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.simmel.probe_simmel_number [n_max]
"""

import sys

from org_frontier.thinkers.simmel import forms as F


def main():
    n_max = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    print("Simmel H2 — the decisive step (mutual conjunctive cliques, n = 2..%d)" % n_max)
    control = F.run_control()
    recs = {}
    for n in range(2, n_max + 1):
        recs[n] = F.evaluate("clique_%d" % n, F.clique(n))
    phis = [recs[n]["phi_mip"] for n in range(2, n_max + 1)]
    deltas = [round(b - a, 6) for a, b in zip(phis, phis[1:])]
    for n, d in zip(range(2, n_max), deltas):
        print("  ΔΦ(%d→%d) = %+.6f" % (n, n + 1, d))
    if len(deltas) >= 3:
        ok = deltas[0] > deltas[1] >= deltas[2]
    elif len(deltas) == 2:
        ok = deltas[0] > deltas[1]
    else:
        ok = False
    status = "CONFIRMED" if ok else "REFUTED"
    print("H2 (2→3 is the decisive step; increments diminish): %s" % status)
    F.save("probe_simmel_number", {"control": control, "forms": {str(k): v for k, v in recs.items()},
                                   "phi_by_n": dict(zip(range(2, n_max + 1), phis)), "deltas": deltas, "H2": status})


if __name__ == "__main__":
    main()
