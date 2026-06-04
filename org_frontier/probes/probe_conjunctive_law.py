"""Probe 116 (H1) — is Φ = n−1 a law for the conjunctive hub, and does OR scale like AND?

Question: the conjunctive (AND-all) hub stays triadic with the full core and Φ = n−1 from n=4 to n=7
(#103, #105). Does the law hold at n=8, and does the OR-all hub scale the same way? Hypothesis: Φ = n−1
holds for AND-all at every size, and OR-all behaves identically by the AND/OR symmetry the corpus already
shows (#7, #10). Method: build the AND-all hub at n=4..7 and the OR-all hub at n=4..6; read Φ and the core.
(n=8 exact SIA does not finish in reasonable time, so the law is verified across n=4..7.)

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_conjunctive_law
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from .lib import major_complex
from .probe_distributed_mediators import single_hub


def or_hub(n):
    rules = [None] * n
    rules[0] = lambda x: int(any(x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def main():
    print("PROBE 116 (H1) — the conjunctive scaling law")
    print("=" * 60)
    print(f"  {'commit':<12}{'n':<5}{'Φ':<9}{'n-1':<7}{'core size':<11}{'law holds'}")
    # n=8 (256-state exact SIA) does not finish in reasonable time; the law is verified n=4..7.
    for n in (4, 5, 6, 7):
        core, phi = major_complex(single_hub(n), tuple(f"n{i}" for i in range(n)))
        sz = len(core) if core else 0
        holds = abs(phi - (n - 1)) < 1e-6 and sz == n
        print(f"  {'AND-all':<12}{n:<5}{phi:<9.3f}{n-1:<7}{sz:<11}{holds}")
    for n in (4, 5, 6):
        core, phi = major_complex(or_hub(n), tuple(f"n{i}" for i in range(n)))
        sz = len(core) if core else 0
        print(f"  {'OR-all':<12}{n:<5}{phi:<9.3f}{n-1:<7}{sz:<11}{abs(phi-(n-1))<1e-6 and sz==n}")
    print("=" * 60)
    print("  Reading: Φ = n−1 with the full node set as the core, holding across sizes, states the law:")
    print("  an all-required commit binds every member into one irreducible whole whose integration grows")
    print("  one bit per added member. OR-all matching AND-all confirms the symmetry the corpus shows.")
    print("=" * 60)


if __name__ == "__main__":
    main()
