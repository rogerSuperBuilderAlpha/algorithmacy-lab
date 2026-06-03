"""Probe 5 — signal asymmetry (scope condition).

The dissertation lists signal asymmetry as a scope condition of algorithmacy. Operationalize it as
asymmetric feedback: does each party get to observe the determination (read S), or only one side?

H5: the triad requires both parties to be dynamically coupled to the determination. One-sided
feedback (only the worker, or only the counterpart, reads S) collapses it — a party that gets no
feedback is an emit-only source and drops out of the core (the bidirectionality principle).

Nodes: 0=W, 1=S, 2=C. S' = W AND C throughout; only the parties' feedback varies.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_asymmetry
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C")

FORMS = {
    "symmetric":        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],   # both read S
    "worker_only_fb":   [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]],   # C static (no fb)
    "counterpart_only": [lambda x: x[0], lambda x: x[0] & x[2], lambda x: x[1]],   # W static (no fb)
}


def main():
    print("PROBE 5 — signal asymmetry (asymmetric feedback)")
    print("=" * 80)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        print(f"  {k:<18} whole-system {v.structure:<8} Φ={v.max_phi:.3f}   core={core} Φ={phi:.3f}")
    print("=" * 80)


if __name__ == "__main__":
    main()
