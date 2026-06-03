"""Probe 10 — determination monotonicity in multi-party cores.

The corpus found parity (XOR/XNOR) determinations support irreducibility more readily than monotone
ones at n=3. Extend to n=4 (one worker, two counterparts) and ask which determination types keep all
three parties in the major complex.

H10: a parity determination (S = W ⊕ C1 ⊕ C2) keeps every party pivotal and so in the core, where
monotone determinations (AND, OR, MAJ) may drop or weaken parties.

Nodes: 0=W, 1=S, 2=C1, 3=C2. W, C1, C2 track S.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_parity_multiparty
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C1", "C2")


def maj(a, b, c):
    return (a & b) | (a & c) | (b & c)


FORMS = {
    "AND_all":    [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]],
    "OR_any":     [lambda x: x[1], lambda x: x[0] | x[2] | x[3], lambda x: x[1], lambda x: x[1]],
    "MAJ":        [lambda x: x[1], lambda x: maj(x[0], x[2], x[3]), lambda x: x[1], lambda x: x[1]],
    "PARITY_xor": [lambda x: x[1], lambda x: x[0] ^ x[2] ^ x[3], lambda x: x[1], lambda x: x[1]],
}


def main():
    print("PROBE 10 — determination type vs the multi-party core")
    print("=" * 84)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        parties = [p for p in ("W", "C1", "C2") if core and p in core]
        print(f"  {k:<12} whole-system {v.structure:<8} Φ={v.max_phi:.3f}   core={core} Φ={phi:.3f}   "
              f"parties in core: {parties}")
    print("=" * 84)


if __name__ == "__main__":
    main()
