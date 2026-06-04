"""Probe 76 (#32) — does effective oversight have to join the core?

Question: a regulator R can override the determination. Does adding oversight change the verdict, and
must effective oversight be in the irreducible core? Hypothesis: a read-only regulator (it observes but
does nothing) is a sink and stays out; a regulator that overrides the commit AND responds to outcomes
is bidirectionally coupled and joins the core. Method: build regulator forms of increasing coupling and
read the major complex.

Nodes: 0=W, 1=S, 2=C, 3=R.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_regulator
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C", "R")

FORMS = {
    # observer: R reads S, affects nothing
    "observer":        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
    # veto-only: R can block the commit (S' = (W∧C)∧R) but does not respond
    "veto_only":       [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[3]],
    # responsive oversight: R vetoes the commit AND responds to outcomes (R' = S)
    "veto_responsive": [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]],
}


def main():
    print("PROBE 76 (#32) — the regulator / oversight node")
    print("=" * 80)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        r_in = core is not None and "R" in core
        print(f"  {k:<16} whole {v.structure:<8} core={core}  R in core: {r_in}")
    print("=" * 80)
    print("  Reading: oversight enters the irreducible coordination only if it both constrains the")
    print("  commit and is fed by it. An observer that only watches is a sink — structurally outside")
    print("  the coordination it oversees, which is a precise sense of toothless oversight.")
    print("=" * 80)


if __name__ == "__main__":
    main()
