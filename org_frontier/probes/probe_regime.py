"""Probe 3 — temporal-tracking (the regime-switching dimension).

The temporal-tracking dimension of algorithmacy: the determination's rule shifts over time and the
worker must track it. Model a regime node R that switches the mediator's rule:
    R = 1  ->  S' = W AND C   (strict)
    R = 0  ->  S' = W OR  C   (lax)

H3: when the rule actually switches (R coupled and changing), the regime node joins the irreducible
core — tracking the shifting rule is part of the coordination. A fixed rule leaves R outside.

Nodes: 0=W, 1=S, 2=C, 3=R. W and C track S.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_regime
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C", "R")


def s_switch(x):
    return (x[0] & x[2]) if x[3] else (x[0] | x[2])


FORMS = {
    # fixed rule: R static and irrelevant (S' = W AND C regardless).
    "fixed_rule":      [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3]],
    # switching, regime oscillates autonomously (R' = NOT R): an exogenous rule clock.
    "switch_osc":      [lambda x: x[1], s_switch, lambda x: x[1], lambda x: 1 - x[3]],
    # switching, regime tracks the outcome (R' = S): the rule adapts to what the system did.
    "switch_tracks":   [lambda x: x[1], s_switch, lambda x: x[1], lambda x: x[1]],
}


def main():
    print("PROBE 3 — temporal-tracking (regime switching)")
    print("=" * 84)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        r_in = core is not None and "R" in core
        print(f"  {k:<16} whole-system {v.structure:<8} Φ={v.max_phi:.3f}   core={core} Φ={phi:.3f}   "
              f"R in core: {r_in}")
    print("=" * 84)


if __name__ == "__main__":
    main()
