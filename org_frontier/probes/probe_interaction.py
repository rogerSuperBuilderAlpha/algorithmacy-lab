"""Probe 37 — feature interaction: principal × coalition.

Earlier probes studied a corporate principal (relocates/joins the core under bidirectional coupling)
and a counterpart coalition (relocates the core to {C1,C2}, ejecting the worker) separately. Do they
interact? Put both in one n=5 form and see which structure wins.

H37: the two displacement effects compete — either the coalition core {C1,C2} dominates, or the
principal pulls a {S,P}-centric core, or they combine. Honest exploration; report the core.

Nodes: 0=W, 1=S, 2=C1, 3=C2, 4=P.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_interaction
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C1", "C2", "P")

FORMS = {
    # coalition only: C1<->C2 channel, plain all-required match, no active principal
    "coalition_only":   [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1] | x[3], lambda x: x[1] | x[2], lambda x: x[4]],
    # principal only: P gates and monitors, no coalition
    "principal_only":   [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
    # both: coalition AND an active gating/monitoring principal
    "coalition+principal": [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4], lambda x: x[1] | x[3], lambda x: x[1] | x[2], lambda x: x[1]],
}


def main():
    print("PROBE 37 — feature interaction: principal × coalition (n=5)")
    print("=" * 84)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        print(f"  {k:<22} {v.structure:<8} Φ_sys={v.max_phi:.3f}  core={core} Φ={phi:.3f}")
    print("=" * 84)


if __name__ == "__main__":
    main()
