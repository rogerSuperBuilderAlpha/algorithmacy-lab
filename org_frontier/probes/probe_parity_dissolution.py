"""Probe 120 (J3) — at what size does parity coordination effectively dissolve?

Question: the parity hub keeps the full core but Φ = 2^(2−n) fades with size (#115). It stays positive
forever in exact arithmetic, but at some size it drops below any detectable floor. Where? Hypothesis:
Φ = 2^(2−n) holds at n=6,7, and the extrapolation puts the sub-1e−6 size near n=22 — XOR coordination is
irreducible in principle yet undetectable in practice well before that. Method: compute the parity hub's
Φ at n=6 and n=7, confirm the 2^(2−n) form, and report the size where the law predicts Φ < 1e−6.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_parity_dissolution
"""

import math
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from .lib import major_complex
from .probe_parity_scaling import parity_hub

PHI_EPS = 1e-6


def main():
    print("PROBE 120 (J3) — the parity hub's dissolution size")
    print("=" * 60)
    print(f"  {'n':<5}{'Φ measured':<14}{'2^(2-n) predicted':<20}{'match'}")
    for n in (3, 4, 5, 6, 7):
        core, phi = major_complex(parity_hub(n), tuple(f"x{i}" for i in range(n)))
        pred = 2.0 ** (2 - n)
        print(f"  {n:<5}{phi:<14.5f}{pred:<20.5f}{abs(phi - pred) < 1e-6}")
    n_diss = 2 - math.log2(PHI_EPS)        # 2^(2-n) < 1e-6  ->  n > 2 - log2(1e-6)
    print("=" * 60)
    print(f"  Φ < {PHI_EPS:g} predicted at n > {n_diss:.1f}, so the parity hub is numerically dyadic from n = {math.ceil(n_diss)}.")
    print("  Reading: XOR-style coordination is irreducible at every size in exact arithmetic, yet its Φ")
    print("  halves with each added member, so by about two dozen parties it is below any measurement")
    print("  floor. Parity binding is real but cannot hold a large group in any detectable sense.")
    print("=" * 60)


if __name__ == "__main__":
    main()
