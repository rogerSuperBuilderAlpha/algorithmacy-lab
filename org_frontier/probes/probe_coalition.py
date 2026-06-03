"""Probe 1 — counterpart coalition.

Concept: collective action inside the triadic structure. Two counterparts (C1, C2) coordinate with
a worker (W) through a system (S). What happens when the counterparts gain a DIRECT channel to each
other (a coalition / union), while still reaching the worker only through S?

H1: the coalition channel pulls the irreducible core toward {C1, C2, S} and pushes the worker out.
H0: the worker stays in the core; the coalition channel does not displace it.

Nodes: 0=W, 1=S, 2=C1, 3=C2.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_coalition
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C1", "C2")

FORMS = {
    # baseline: all-required pool, no coalition. (triadic, core all four)
    "no_coalition": [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]],
    # weak coalition: counterparts also read each other, still read S.
    "weak_coalition": [lambda x: x[1], lambda x: x[0] & x[2] & x[3],
                       lambda x: x[1] | x[3], lambda x: x[1] | x[2]],
    # strong coalition: counterparts coordinate mainly with each other (sync), S still needs both.
    "strong_coalition": [lambda x: x[1], lambda x: x[0] & x[2] & x[3],
                         lambda x: x[3], lambda x: x[2]],
}


def main():
    print("PROBE 1 — counterpart coalition")
    print("=" * 80)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        w_in = core is not None and "W" in core
        print(f"  {k:<18} whole-system {v.structure:<8} Φ={v.max_phi:.3f}   "
              f"core={core} Φ={phi:.3f}   W in core: {w_in}")
    print("=" * 80)


if __name__ == "__main__":
    main()
