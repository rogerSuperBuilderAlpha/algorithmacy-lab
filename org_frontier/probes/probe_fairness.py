"""Probe 78 (#35) — does a fair determination carry a different signature?

Question: Probe 16 tied the triad to balanced influence. Does an extractive determination (one that
weights the principal over the parties) carry a different Φ signature than a fair (balanced) one?
Hypothesis: a fair, balanced-influence commit keeps all parties in the core; as the commit is weighted
toward a principal, the parties lose influence and can be displaced toward an {S,P}-centric core.
Method: a four-node form (W, S, C, P) whose commit interpolates from balanced (S = W∧C, P idle) to
principal-dominated (S follows P), reading the influence balance and the major complex at each step.

Nodes: 0=W, 1=S, 2=C, 3=P.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_fairness
"""

from .lib import major_complex

LABELS = ("W", "S", "C", "P")

FORMS = {
    # fair: balanced joint commit, principal idle
    "fair_balanced":   [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3]],
    # tilted: commit needs the parties but the principal can also force it (P OR (W∧C))
    "tilted":          [lambda x: x[1], lambda x: x[3] | (x[0] & x[2]), lambda x: x[1], lambda x: x[1]],
    # extractive: commit follows the principal, parties' inputs marginal
    "extractive":      [lambda x: x[1], lambda x: x[3], lambda x: x[1], lambda x: x[1]],
}


def main():
    print("PROBE 78 (#35) — fairness signature (balanced vs principal-weighted commit)")
    print("=" * 80)
    for k, r in FORMS.items():
        core, phi = major_complex(r, LABELS)
        parties = [p for p in ("W", "C") if core and p in core]
        p_in = core is not None and "P" in core
        print(f"  {k:<16} core={core}  parties in core: {parties}  P in core: {p_in}")
    print("=" * 80)
    print("  Reading: a balanced commit keeps the parties in the core; as the commit tilts toward the")
    print("  principal, the parties lose their place and the core moves toward the platform and owner —")
    print("  an extractive determination has a recognizably different structural signature.")
    print("=" * 80)


if __name__ == "__main__":
    main()
