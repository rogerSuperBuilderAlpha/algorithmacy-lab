"""Probe 28 — information-richness asymmetry.

One party brings richer state than the other: the worker has two bits of intent (W1, W2), the
counterpart one (C). Does asymmetric information richness shift the irreducible core toward the
richer party? (PyPhi is binary, so "rich" = two nodes.)

H28: the richer party occupies more of the core; a determination that reads both worker bits and the
counterpart binds all three, while one that reads only one worker bit drops the other.

Nodes: 0=W1, 1=W2, 2=S, 3=C. W1,W2,C track S.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_richness
"""

from .lib import verdict, major_complex

LABELS = ("W1", "W2", "S", "C")

FORMS = {
    # determination reads both worker bits jointly with the counterpart
    "rich_both_bits": [lambda x: x[2], lambda x: x[2], lambda x: (x[0] & x[1]) & x[3], lambda x: x[2]],
    # reads the worker bits via XOR (both pivotal) with the counterpart
    "rich_xor_bits":  [lambda x: x[2], lambda x: x[2], lambda x: (x[0] ^ x[1]) & x[3], lambda x: x[2]],
    # reads only one worker bit (the other intent dimension is unused)
    "one_bit_used":   [lambda x: x[2], lambda x: x[2], lambda x: x[0] & x[3], lambda x: x[2]],
    # symmetric baseline: collapse the worker to one bit (W1 only), reads W1 and C
    "symmetric_1v1":  [lambda x: x[2], lambda x: x[1], lambda x: x[0] & x[3], lambda x: x[2]],
}


def main():
    print("PROBE 28 — information-richness asymmetry")
    print("=" * 84)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        wbits = [b for b in ("W1", "W2") if core and b in core]
        c_in = core is not None and "C" in core
        print(f"  {k:<16} {v.structure:<8} Φ={v.max_phi:.3f}  core={core}  "
              f"worker bits in core={wbits}  C in core={c_in}")
    print("=" * 84)


if __name__ == "__main__":
    main()
