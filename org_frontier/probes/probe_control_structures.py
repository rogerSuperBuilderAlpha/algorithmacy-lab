"""Probe 121 (L1) — which real control structures are conjunctive, and which are parity?

Question: the parity (XOR) commits are the fragile family — irreducible but fading with size (#115),
and the cheap-measure blind spot (#113). Which everyday organizational control structures are parity, and
which are the robust conjunctive kind? Hypothesis: most familiar controls (dual authorization,
escalation) are conjunctive and so scale robustly; the parity structures (allocate to exactly one,
require agreement) are the rare fragile ones, which is why the parity blind spot seldom bites in
practice. Method: model named two-actor control structures as a commit S(W, C); classify each commit's
type, verdict, and Φ.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_control_structures
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from .lib import verdict
from .probe_abm_difficulty import commit_table

LABELS = ("W", "S", "C")
PARITY = {(0, 1, 1, 0), (1, 0, 0, 1)}

# each entry: name -> commit rule S(W, C), with both actors reading the commit
STRUCTURES = {
    "dual authorization (both approve)": lambda x: x[0] & x[2],
    "escalation (either triggers)":      lambda x: x[0] | x[2],
    "allocate to exactly one":           lambda x: x[0] ^ x[2],
    "require agreement (consensus)":     lambda x: 1 - (x[0] ^ x[2]),
    "unilateral directive (boss only)":  lambda x: x[0],
}


def kind(ts):
    if ts in PARITY:
        return "parity"
    if ts in {(0, 0, 0, 0), (1, 1, 1, 1)}:
        return "constant"
    # depends on both inputs and monotone => conjunctive family; one input => single-input
    reads_w = any(ts[c] != ts[c ^ 1] for c in range(4))
    reads_c = any(ts[c] != ts[c ^ 2] for c in range(4))
    if reads_w and reads_c:
        return "conjunctive"
    return "single-input"


def main():
    print("PROBE 121 (L1) — control structures by commit type")
    print("=" * 76)
    print(f"  {'structure':<36}{'type':<14}{'verdict':<10}{'Φ'}")
    for name, s_rule in STRUCTURES.items():
        rules = [lambda x: x[1], s_rule, lambda x: x[1]]
        v = verdict(rules, LABELS)
        ts = commit_table(rules)
        print(f"  {name:<36}{kind(ts):<14}{v.structure:<10}{v.max_phi:.3f}")
    print("=" * 76)
    print("  Reading: the conjunctive controls (dual authorization, escalation) are the robust Φ=2 triads")
    print("  that scale by the n−1 law (#116); the parity controls (exactly-one, require-agreement) are the")
    print("  Φ=0.5 fragile family that fades with size (#115); a one-sided directive is dyadic. Everyday")
    print("  control is mostly conjunctive, so the parity blind spot rarely bites real coordination.")
    print("=" * 76)


if __name__ == "__main__":
    main()
