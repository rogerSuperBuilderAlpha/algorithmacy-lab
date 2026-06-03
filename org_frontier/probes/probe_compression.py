"""Probe 2 — intent compression (the translational dimension).

The translational dimension of algorithmacy: the worker compresses situated intent into the
system's narrow schema, with loss. Model the worker's intent as two bits (W1, W2). Vary how much of
that intent the system's determination reads.

H2: compression removes intent dimensions from the irreducible core — an intent bit the system does
not read drops out of the worker's footprint in the coordination, even though the worker "has" it.

Nodes: 0=W1, 1=W2, 2=S, 3=C. Both intent bits and C track the determination S; only S' varies.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_compression
"""

from .lib import verdict, major_complex

LABELS = ("W1", "W2", "S", "C")

FORMS = {
    # high fidelity: S reads both intent bits distinctly (XOR uses both) and C.
    "full_intent_xor": [lambda x: x[2], lambda x: x[2], lambda x: (x[0] ^ x[1]) & x[3], lambda x: x[2]],
    # redundant: S reads both bits but only their OR (both matter, redundantly) and C.
    "redundant_or":    [lambda x: x[2], lambda x: x[2], lambda x: (x[0] | x[1]) & x[3], lambda x: x[2]],
    # compressed: S reads only W1; the second intent bit W2 is dropped from the determination.
    "compressed_w1":   [lambda x: x[2], lambda x: x[2], lambda x: x[0] & x[3], lambda x: x[2]],
}


def main():
    print("PROBE 2 — intent compression (translational dimension)")
    print("=" * 84)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        bits = [b for b in ("W1", "W2") if core and b in core]
        print(f"  {k:<18} whole-system {v.structure:<8} Φ={v.max_phi:.3f}   core={core} Φ={phi:.3f}   "
              f"intent bits in core: {bits}")
    print("=" * 84)


if __name__ == "__main__":
    main()
