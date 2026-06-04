"""Probe 50 — adversarial / anti-coordination.

Platform determinations need not reward the parties' alignment; the system's objective may oppose
the worker's. Does irreducibility care about valence? Compare a cooperative determination (S commits
when W and C align) with adversarial ones (S commits when they differ, or when not-both).

H50: irreducibility is valence-free — adversarial joint determinations are triadic too. Whether the
parties' interests align does not bear on whether the coordination is structurally irreducible.

Nodes: 0=W, 1=S, 2=C.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_adversarial
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C")

FORMS = {
    "cooperative (W∧C)":   [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
    "adversarial (W⊕C)":   [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]],
    "adversarial (¬(W∧C))":[lambda x: x[1], lambda x: 1 - (x[0] & x[2]), lambda x: x[1]],
    "adversarial (W∧¬C)":  [lambda x: x[1], lambda x: x[0] & (1 - x[2]), lambda x: x[1]],
}


def main():
    print("PROBE 50 — adversarial / anti-coordination")
    print("=" * 72)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        print(f"  {k:<22} {v.structure:<8} Φ={v.max_phi:.3f}  core={core}")
    print("=" * 72)
    print("  Irreducibility is valence-free: a determination that opposes the parties is still")
    print("  triadic. The structural verdict is about binding, not whether interests align.")
    print("=" * 72)


if __name__ == "__main__":
    main()
