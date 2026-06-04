"""Probe 110 (E1) — in what order do parties leave the core as a commit tilts toward the owner?

Question: an extractive commit ejects the parties and leaves {S,P} (Probe 78). Sweeping the tilt finely,
what is the sequence — when does the principal enter, when do the parties leave? Hypothesis: as principal
weight rises, the principal joins the core first (all four in), then the parties drop together (by the
worker/counterpart role symmetry, #55), leaving {S,P}. Method: a four-node form (W, S, C, P) whose commit
is a weighted threshold S = 1 iff W + C + w_P·P ≥ 2, with all parties reading S; sweep the principal
weight w_P and record the major complex at each step.

Nodes: 0=W, 1=S, 2=C, 3=P.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_ejection_order
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from .lib import major_complex

LABELS = ("W", "S", "C", "P")


def build(w_p):
    def s_rule(x):
        return 1 if (x[0] + x[2] + w_p * x[3]) >= 2 else 0
    # parties and principal all read the commit
    return [lambda x: x[1], s_rule, lambda x: x[1], lambda x: x[1]]


def main():
    print("PROBE 110 (E1) — party ejection order as the commit tilts toward the principal")
    print("=" * 68)
    print(f"  {'w_P':<6}{'Φ':<9}{'core':<24}{'W in':<7}{'C in':<7}{'P in'}")
    for w_p in (0, 1, 2, 3):
        core, phi = major_complex(build(w_p), LABELS)
        core = core or ()
        print(f"  {w_p:<6}{phi:<9.3f}{str(core):<24}{('W' in core)!s:<7}{('C' in core)!s:<7}{'P' in core}")
    print("=" * 68)
    print("  Reading: the core trajectory as the owner's weight rises shows the sequence — when the")
    print("  principal enters and when the worker and counterpart drop. Symmetric weights drop the two")
    print("  parties together at a tilt threshold; the endpoint is the {S,P} extractive core (Probe 78).")
    print("=" * 68)


if __name__ == "__main__":
    main()
