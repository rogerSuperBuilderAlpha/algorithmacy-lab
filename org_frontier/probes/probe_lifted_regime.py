"""Probe 63 (#16) — does a bidirectionally-coupled regime bind?

Question: Probe 3 found an emit-only rule-clock stays a spectator and an outcome-tracking regime
destabilizes the core. Does a regime that BOTH switches the determination AND is read into it (so it is
bidirectionally coupled, the condition the two-condition account says is necessary) join the core?
Hypothesis: yes; an endogenous, two-way-coupled regime joins the irreducible core, whereas the emit-only
clock did not. Method: build regime forms with varying coupling and read the major complex.

Nodes: 0=W, 1=S, 2=C, 3=R (regime that switches S' between W∧C and W∨C).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_lifted_regime
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C", "R")


def s_switch(x):
    return (x[0] & x[2]) if x[3] else (x[0] | x[2])


FORMS = {
    # emit-only clock (Probe 3 baseline): R oscillates, reads nothing, just drives S
    "emit_only_clock": [lambda x: x[1], s_switch, lambda x: x[1], lambda x: 1 - x[3]],
    # bidirectional: R switches S AND reads the determination (R' = S), and S reads R
    "bidirectional":   [lambda x: x[1], s_switch, lambda x: x[1], lambda x: x[1]],
    # bidirectional + party-coupled: R reads a party too (R' = S ∧ W)
    "regime_reads_party": [lambda x: x[1], s_switch, lambda x: x[1], lambda x: x[1] & x[0]],
}


def main():
    print("PROBE 63 (#16) — does a bidirectionally-coupled regime bind?")
    print("=" * 80)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        r_in = core is not None and "R" in core
        print(f"  {k:<20} whole {v.structure:<8} Φ={v.max_phi:.3f}  core={core}  R in core: {r_in}")
    print("=" * 80)
    print("  Reading: if the bidirectionally-coupled regime joins the core where the emit-only clock")
    print("  did not (Probe 3), temporal-tracking can be structural after all — but only when the")
    print("  rule that shifts is itself fed by the coordination, not an exogenous clock.")
    print("=" * 80)


if __name__ == "__main__":
    main()
