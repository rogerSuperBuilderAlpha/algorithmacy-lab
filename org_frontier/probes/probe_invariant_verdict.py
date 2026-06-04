"""Probe 112 (F1) — is there a verdict robust to observation grain and update schedule?

Question: the verdict flips to dyadic under a 2-step grain (Probe 32) and under sequential update (Probe
62). For empirical use, is there an aggregate verdict robust to both, or must the modeling convention be
declared? Hypothesis: no aggregate is robust — triadic forms are called dyadic under coarse grain and
sequential update, so a vote across conditions destroys the verdict; the finest-grain synchronous reading
is the only correct convention and must be stated. Method: over the triadic corpus forms, compute the
verdict under grain-1 synchronous (canonical), grain-2 synchronous, and grain-1 sequential update; report
how each condition calls them and what an across-condition majority would conclude.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_invariant_verdict
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules
from org_frontier.corpus.population import enumerate_family
from .lib import max_phi_float

PHI_EPS = 1e-6
N = 3


def step(rules, st):
    return tuple(int(rules[i](st)) for i in range(N))


def two_step_tpm(rules):
    tpm = np.zeros((2 ** N, N))
    for s in range(2 ** N):
        st = tuple((s >> i) & 1 for i in range(N))
        ns = step(rules, step(rules, st))
        for i in range(N):
            tpm[s, i] = ns[i]
    return tpm


def seq_tpm(rules, order=(0, 1, 2)):
    tpm = np.zeros((2 ** N, N))
    for s in range(2 ** N):
        st = [(s >> i) & 1 for i in range(N)]
        for j in order:
            st[j] = int(rules[j](st))
        for i in range(N):
            tpm[s, i] = st[i]
    return tpm


def is_tri(tpm):
    phi, _ = max_phi_float(tpm)
    return phi > PHI_EPS


def main():
    print("PROBE 112 (F1) — verdict robustness across grain and update schedule")
    print("=" * 68)
    triadic = [rules for _, rules in enumerate_family()
               if classify_rules(rules, labels=("W", "S", "C")).structure == "triadic"]
    canon = grain2 = seq = majority_tri = 0
    for rules in triadic:
        c = is_tri(tpm_from_rules(rules))     # grain-1 synchronous (canonical)
        g2 = is_tri(two_step_tpm(rules))
        sq = is_tri(seq_tpm(rules))
        canon += c
        grain2 += g2
        seq += sq
        majority_tri += int((c + g2 + sq) >= 2)
    n = len(triadic)
    print(f"  {n} canonically-triadic forms; fraction still called triadic under each condition:")
    print(f"  grain-1 synchronous (canonical) : {canon}/{n}  ({100*canon/n:.0f}%)")
    print(f"  grain-2 synchronous             : {grain2}/{n}  ({100*grain2/n:.0f}%)")
    print(f"  grain-1 sequential update       : {seq}/{n}  ({100*seq/n:.0f}%)")
    print(f"  across-condition majority = triadic: {majority_tri}/{n}  ({100*majority_tri/n:.0f}%)")
    print("=" * 68)
    if majority_tri < n:
        print("  Reading: a majority vote across grain and schedule does not preserve the verdict — coarse")
        print("  grain and sequential update both call triadic forms dyadic, so aggregating destroys it.")
        print("  The verdict has no modeling-free invariant; it must be reported at the finest grain with")
        print("  synchronous update, and that convention stated. Robustness is a declaration, not a result.")
    else:
        print("  Reading: the verdict survives a majority vote across conditions — an aggregate is robust.")
    print("=" * 68)


if __name__ == "__main__":
    main()
