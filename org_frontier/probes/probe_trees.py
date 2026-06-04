"""Probe 58 (#13) — tree (branching) mediation.

Question: does branching mediation dilute irreducibility like breadth, or preserve it like depth?
Hypothesis: a tree of mediators behaves more like breadth (added branches give more ways to factor)
than like a chain (which is Φ-invariant). Method: build branching-mediation forms and classify, against
the chain (preserves) and pool (breadth) baselines.

Nodes per form labeled inline.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_trees
"""

from .lib import verdict, major_complex


def main():
    print("PROBE 58 (#13) — tree (branching) mediation")
    print("=" * 84)
    cases = [
        # chain baseline (depth): W -> S1 -> S2 -> C
        ("chain_depth", ("W", "S1", "S2", "C"),
         [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[2]]),
        # tree: a root mediator joins two branch mediators, one per party.
        # nodes 0=W,1=Sa,2=C,3=Sb,4=Sroot ; Sa reads W, Sb reads C, Sroot = Sa AND Sb; ends read Sroot
        ("tree_join", ("W", "Sa", "C", "Sb", "Sroot"),
         [lambda x: x[4], lambda x: x[0], lambda x: x[4], lambda x: x[2],
          lambda x: x[1] & x[3]]),
        # tree where branches recombine pairwise (cross-coupled), to contrast
        ("tree_crosscoupled", ("W", "Sa", "C", "Sb", "Sroot"),
         [lambda x: x[4], lambda x: x[0] & x[4], lambda x: x[4], lambda x: x[2] & x[4],
          lambda x: x[1] & x[3]]),
    ]
    for name, labels, rules in cases:
        v = verdict(rules, labels)
        core, phi = major_complex(rules, labels)
        print(f"  {name:<18} whole {v.structure:<8} Φ={v.max_phi:.3f}   core={core} Φ={phi:.3f}")
    print("=" * 84)
    print("  Comparison anchors: a chain is Φ-invariant and triadic (depth preserves); a broadcast")
    print("  fan-out is dyadic (breadth dilutes). Where the tree lands says which force dominates")
    print("  branching mediation.")
    print("=" * 84)


if __name__ == "__main__":
    main()
