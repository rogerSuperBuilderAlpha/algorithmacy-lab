"""Probe 6 — the exit option.

Hirschman's exit/voice: a party that can leave. Model the counterpart with an absorbing "exited"
state (C = 0 is a sink: once gone, gone, and the system cannot match it). Does the possibility of
exit change the verdict, and does it shrink the reachable coordination?

H6: an exit option (absorbing departure) reduces the irreducible coordination — the form spends its
reachable dynamics collapsing toward the exited state, so the triad is fragile.

Nodes: 0=W, 1=S, 2=C. Compare a counterpart that always re-engages with one that can exit.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_exit
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C")

FORMS = {
    # no exit: counterpart always re-engages from the determination (C' = S). Base triad.
    "no_exit":   [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
    # exit: C stays engaged only while matched (C' = C AND S); C = 0 is absorbing.
    "with_exit": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2] & x[1]],
    # re-entry: C can come back when the worker is active (C' = C OR W) — exit is reversible.
    "reentry":   [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2] | x[0]],
}


def main():
    print("PROBE 6 — the exit option")
    print("=" * 80)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        print(f"  {k:<12} whole-system {v.structure:<8} Φ={v.max_phi:.3f}   "
              f"core={core} Φ={phi:.3f}   reachable={v.n_states_evaluated}")
    print("=" * 80)


if __name__ == "__main__":
    main()
