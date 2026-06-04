"""Probe 73 (#29) — multi-role agents: are the two cores independent?

Question: an agent X is the worker on one platform (with counterpart C1 through system S1) and the
counterpart on another (with worker W2 through system S2). Are the two coordinations independent, or
does sharing X merge them into one complex? Hypothesis: the two triads stay separate; the major
complex is one triad, not a merged six-element whole, unless X bridges them. Method: build the
two-platform system and read the major complex.

Nodes: 0=X, 1=S1, 2=C1, 3=S2, 4=W2.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_multirole
"""

from .lib import verdict, major_complex

LABELS = ("X", "S1", "C1", "S2", "W2")

FORMS = {
    # X responds to whichever platform; each platform jointly determines its triad
    "two_platforms": [
        lambda x: x[1] | x[3],          # X' = S1 OR S2 (responds to either platform)
        lambda x: x[0] & x[2],          # S1' = X AND C1
        lambda x: x[1],                 # C1' = S1
        lambda x: x[0] & x[4],          # S2' = X AND W2
        lambda x: x[3],                 # W2' = S2
    ],
    # X only on platform 1 (platform 2's worker reads S2 but X ignores S2): control
    "x_only_p1": [
        lambda x: x[1],                 # X' = S1
        lambda x: x[0] & x[2],
        lambda x: x[1],
        lambda x: x[0] & x[4],
        lambda x: x[3],
    ],
}


def main():
    print("PROBE 73 (#29) — multi-role agent across two platforms")
    print("=" * 80)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        size = len(core) if core else 0
        print(f"  {k:<14} whole {v.structure:<8}  core={core} (size {size}) Φ={phi:.3f}")
    print("=" * 80)
    print("  Reading: if the core is a single triad rather than the merged five-element system, the")
    print("  two coordinations are structurally separate even though one agent stands in both.")
    print("=" * 80)


if __name__ == "__main__":
    main()
