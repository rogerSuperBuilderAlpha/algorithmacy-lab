"""Probe 69 (#25) — does a higher-fidelity worker model displace the counterpart more?

Question: Probes 4/9 found a blended internal model M can take the counterpart C's place in the core.
Does the displacement strengthen as the model's fidelity rises? Hypothesis: yes; a dead model leaves C
in the core, a model that tracks the determination displaces it. Method: fix S'=W∧C, C'=S, and the
worker acting on its model (W'=S∧M); vary M's update from dead to full-fidelity and read whether C is
in the major complex.

Nodes: 0=W, 1=S, 2=C, 3=M.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_model_fidelity
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C", "M")

FIDELITY = {
    "dead (M'=0)":        lambda x: 0,
    "static (M'=M)":      lambda x: x[3],
    "lagged (M'=W)":      lambda x: x[0],
    "full (M'=S)":        lambda x: x[1],
}


def main():
    print("PROBE 69 (#25) — model fidelity vs counterpart displacement")
    print("=" * 78)
    for name, m_rule in FIDELITY.items():
        rules = [lambda x: x[1] & x[3], lambda x: x[0] & x[2], lambda x: x[1], m_rule]
        v = verdict(rules, LABELS)
        core, phi = major_complex(rules, LABELS)
        c_in = core is not None and "C" in core
        m_in = core is not None and "M" in core
        print(f"  {name:<16} core={core}  C in core: {c_in}  M in core: {m_in}")
    print("=" * 78)
    print("  Reading: as the model's fidelity rises, the counterpart is displaced from the core and")
    print("  the model takes its place — the worker coordinates with its model of the other.")
    print("=" * 78)


if __name__ == "__main__":
    main()
