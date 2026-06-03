"""Probe 7 — "determinations neither party controls".

The dissertation defines the triad as a worker coordinating with a counterpart through a system that
"commits determinations neither party controls." Test that clause: vary how much each party controls
the determination S.

H7: the triad requires that neither party unilaterally controls S. Mutual dependence (S = W AND C,
both can veto, neither forces) is triadic; if one party controls S (S = W, or S = C), the form is
dyadic. The either-forces case (S = W OR C) is open — compute.

Nodes: 0=W, 1=S, 2=C. W and C track S.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_control
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C")

FORMS = {
    "mutual_veto_AND":  [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],   # neither controls
    "worker_controls":  [lambda x: x[1], lambda x: x[0],        lambda x: x[1]],   # S follows W alone
    "cp_controls":      [lambda x: x[1], lambda x: x[2],        lambda x: x[1]],   # S follows C alone
    "either_forces_OR": [lambda x: x[1], lambda x: x[0] | x[2], lambda x: x[1]],   # either can force
}


def main():
    print("PROBE 7 — determinations neither party controls")
    print("=" * 80)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        print(f"  {k:<18} whole-system {v.structure:<8} Φ={v.max_phi:.3f}   core={core} Φ={phi:.3f}")
    print("=" * 80)


if __name__ == "__main__":
    main()
