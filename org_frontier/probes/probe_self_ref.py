"""Probe 43 — a self-referential mediator (the system has inertia/memory of itself).

The system's commit depends on its own previous state (S' reads S): a sticky or oscillating
mediator. Does mediator self-reference change the verdict or the core?

H43: a self-loop on the system does not break the triad (S is already in the core); it shifts Φ —
inertia (sticky) and parity-memory (XOR) move the magnitude but the verdict holds.

Nodes: 0=W, 1=S, 2=C.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_self_ref
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C")

FORMS = {
    "memoryless": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
    "sticky":     [lambda x: x[1], lambda x: (x[0] & x[2]) | x[1], lambda x: x[1]],
    "xor_memory": [lambda x: x[1], lambda x: (x[0] & x[2]) ^ x[1], lambda x: x[1]],
}


def main():
    print("PROBE 43 — self-referential mediator")
    print("=" * 72)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        print(f"  {k:<14} {v.structure:<8} Φ={v.max_phi:.3f}  core={core}")
    print("=" * 72)


if __name__ == "__main__":
    main()
