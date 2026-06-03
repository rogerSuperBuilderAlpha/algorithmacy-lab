"""Probe 42 — redundant determination paths.

Two system nodes compute the SAME joint determination (redundant mediators). Does redundancy raise
integration (two paths binding the parties) or is the duplicate reducible (you can cut one copy)?

H42: a redundant mediator is largely reducible — Φ does not scale with the number of identical
paths, and the duplicate tends to factor, consistent with the redundancy results (probes 2, 10).

Nodes: 0=W, 1=S1, 2=C, 3=S2.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_redundant
"""

from .lib import verdict, major_complex

LABELS = ("W", "S1", "C", "S2")

FORMS = {
    # single mediator (S2 idle): the baseline triad.
    "single":    [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3]],
    # redundant: S1 and S2 both commit W∧C; parties read both (AND).
    "redundant_and": [lambda x: x[1] & x[3], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[0] & x[2]],
    # redundant, parties read either copy (OR).
    "redundant_or":  [lambda x: x[1] | x[3], lambda x: x[0] & x[2], lambda x: x[1] | x[3], lambda x: x[0] & x[2]],
}


def main():
    print("PROBE 42 — redundant determination paths")
    print("=" * 80)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        print(f"  {k:<16} {v.structure:<8} Φ_sys={v.max_phi:.3f}  core={core} Φ={phi:.3f}")
    print("=" * 80)


if __name__ == "__main__":
    main()
