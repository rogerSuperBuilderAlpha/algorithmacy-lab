"""Probe 105 (B3) — does a lean triadic n=6 form exist?

Question: random sampling found no triadic strict-mediation form at n=6 (Probe 97, 0/300). Is the lean
n=6 triad genuinely empty, or just measure-zero under random function fills? Hypothesis: the specific
conjunctive (all-required) strict-mediation form is triadic at n=6 even though random fills miss it — the
set is non-empty, just vanishingly rare. Method: build the single conjunctive strict-mediation n=6 form
(S = AND of all five parties, each party reads S) and classify it directly; report the verdict, Φ, and
core, with the n=4 and n=5 conjunctive forms for reference.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_lean_n6
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from .lib import major_complex
from .probe_distributed_mediators import single_hub


def main():
    print("PROBE 105 (B3) — the lean conjunctive triad at n=4, 5, 6")
    print("=" * 64)
    print(f"  {'n':<5}{'verdict':<10}{'Φ':<9}{'core size':<11}{'edges 2(n-1)':<13}")
    for n in (4, 5, 6):
        core, phi = major_complex(single_hub(n), tuple(f"n{i}" for i in range(n)))
        sz = len(core) if core else 0
        verdict = "triadic" if phi > 1e-6 else "dyadic"
        print(f"  {n:<5}{verdict:<10}{phi:<9.3f}{sz:<11}{2*(n-1):<13}")
    print("=" * 64)
    print("  Reading: if the conjunctive form is triadic at n=6, the lean n=6 triad exists — the 0/300")
    print("  random result (Probe 97) means triadic n=6 forms are vanishingly rare under random fills,")
    print("  not absent. The all-required commit is the surviving triadic structure at this size.")
    print("=" * 64)


if __name__ == "__main__":
    main()
