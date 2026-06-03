"""Probe 23 — system memory / reputation.

Platforms score workers: the determination depends on accumulated history, not just the present
move. Model a memory node M that the system maintains from the worker's behavior; the determination
reads the memory. Does the reputation node join the irreducible core, and does it change the bind?

H23: a reputation memory joins the core when it is bidirectionally coupled (M reads W, S reads M),
per the established coupling principle — and when it does, the worker's binding now runs through her
reputation rather than her present action.

Nodes: 0=W, 1=S, 2=C, 3=M (the system's memory/score of the worker).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_memory
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C", "M")

FORMS = {
    # no memory: present-move determination (baseline triad + idle M).
    "no_memory":     [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3]],
    # reputation read: S matches on reputation AND counterpart; M accumulates the worker.
    "reputation":    [lambda x: x[1], lambda x: x[3] & x[2], lambda x: x[1], lambda x: x[0] | x[3]],
    # reputation + present: S reads present worker, counterpart, and reputation jointly.
    "rep_plus_now":  [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[0] | x[3]],
    # write-only memory: M records W but S ignores it (a dormant score).
    "dormant_score": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[0] | x[3]],
}


def main():
    print("PROBE 23 — system memory / reputation")
    print("=" * 84)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        m_in = core is not None and "M" in core
        print(f"  {k:<16} {v.structure:<8} Φ={v.max_phi:.3f}  core={core}  M in core: {m_in}")
    print("=" * 84)


if __name__ == "__main__":
    main()
