"""Probe 111 (E2) — do two weak regulators jointly bind where one does not?

Question: a single observe-only regulator stays out of the core (Probe 76). Does adding a second weak
regulator change that — does a coalition of overseers bind where one cannot? Hypothesis: number alone
does not rescue observe-only oversight (no influence, so a sink regardless of count); only a regulator
that gates the commit joins the core, and two weak gates that jointly veto do bind. Method: a five-node
form (W, S, C, R1, R2); compare one observe-only regulator, two observe-only regulators, and two
regulators whose joint approval gates the commit (S requires R1∧R2). Read the major complex of each.

Nodes: 0=W, 1=S, 2=C, 3=R1, 4=R2.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_regulator_coalition
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from .lib import major_complex

LABELS = ("W", "S", "C", "R1", "R2")


def form(kind):
    base_parties = [lambda x: x[1], None, lambda x: x[1]]   # W,C read S; S set below
    if kind == "one observe-only":
        # R1 reads S (observes), R2 idle; S = W∧C ignores both
        return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1], lambda x: x[4]]
    if kind == "two observe-only":
        # both regulators observe S, neither gates
        return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1], lambda x: x[1]]
    if kind == "two joint-veto":
        # commit requires the parties AND both regulators' approval; regulators read S (responsive)
        return [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4], lambda x: x[1],
                lambda x: x[1], lambda x: x[1]]
    raise ValueError(kind)


def main():
    print("PROBE 111 (E2) — regulator coalition: does number rescue observe-only oversight?")
    print("=" * 72)
    for kind in ("one observe-only", "two observe-only", "two joint-veto"):
        core, phi = major_complex(form(kind), LABELS)
        core = core or ()
        regs = [r for r in ("R1", "R2") if r in core]
        print(f"  {kind:<20} Φ={phi:<7.3f} core={str(core):<28} regulators in core: {regs}")
    print("=" * 72)
    print("  Reading: if observe-only regulators stay out whether one or two, number does not rescue")
    print("  oversight — a watchdog without a lever is a sink at any count. Two regulators enter only")
    print("  when their joint approval gates the commit, the coalition analogue of the veto+responsive")
    print("  condition (Probes 76, 66).")
    print("=" * 72)


if __name__ == "__main__":
    main()
