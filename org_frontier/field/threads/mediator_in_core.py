"""Reproducible headline results of the 'is the mediator in the core?' thread (THREAD.md).

A single through-line, dug 20 questions deep from the M4 anomaly: when is a mediating system a
member of the irreducible coordination, and when is it a bypassable side-channel? This script
reproduces the load-bearing numbers — the platform trichotomy, the membership of the ten mocks, the
regime frequencies over random forms, and the disintermediation trajectory.

Run from the repo root with the venv active:  python -m org_frontier.field.threads.mediator_in_core
"""

import os
import random
import sys
from collections import Counter

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import classify_rules
from org_frontier.probes.lib import major_complex
from org_frontier.classifier.validate import factoring_control, irreducible_control
from org_frontier.field.mocks import MOCKS


def _lesion_survives(rules, labels, mi):
    """Do the non-mediator parties still coordinate (triadic) when the mediator is frozen?"""
    rest = [i for i in range(len(labels)) if i != mi]
    if len(rest) < 2:
        return False
    for c in (0, 1):
        red = [(lambda y, _j=j, _c=c: rules[_j](
                 tuple(_c if k == mi else y[rest.index(k)] for k in range(len(labels)))))
               for j in rest]
        if classify_rules(red, tuple(labels[i] for i in rest)).structure == "triadic":
            return True
    return False


def regime(rules, labels, mi):
    """BOTTLENECK / ENRICHER / BYPASSED / dyadic for the mediator at index mi."""
    v = classify_rules(rules, labels)
    core, _ = major_complex(list(rules), labels)
    core = set(core or ())
    med = labels[mi]
    if v.structure == "dyadic":
        return "dyadic" + ("" if med in core else " (med out)")
    if med not in core:
        return "BYPASSED"
    return "ENRICHER" if _lesion_survives(rules, labels, mi) else "BOTTLENECK"


def main() -> int:
    print("=" * 92)
    print("THREAD — is the mediator in the irreducible core? (reproducible headline results)")
    print("=" * 92)
    fac = classify_rules(factoring_control())
    irr = classify_rules(irreducible_control())
    if not (fac.structure == "dyadic" and irr.structure == "triadic"):
        print("  INSTRUMENT CONTROL FAILED — refusing to run.")
        return 1
    print("  Instrument validated.\n")

    L = ("W", "S", "C")

    print("[1] The platform trichotomy (same mediator can be each, depending on the arrangement)")
    tri = {
        "BOTTLENECK  S=W&C, no fallback": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        "ENRICHER    S=W&C, complement":  [lambda x: x[1] & x[2], lambda x: x[0] & x[2], lambda x: x[1] & x[0]],
        "BYPASSED    S=W&C, substitute":  [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[1] | x[0]],
    }
    for name, r in tri.items():
        print(f"    {name:<34} -> {regime(r, L, 1)}")

    print("\n[2] The ten field mocks, by mediator regime")
    for m in MOCKS:
        print(f"    {m.mid} {m.org:<32} med={m.parties[1]:<4} -> {regime(m.rules, m.parties, 1)}")

    print("\n[3] Regime frequency over 500 random 3-node mediated forms (seed 7)")
    random.seed(7)
    cnt = Counter()
    for _ in range(500):
        rules = [(lambda x, _tt=[random.randint(0, 1) for _ in range(8)]:
                  _tt[(x[0] << 2) | (x[1] << 1) | x[2]]) for _ in range(3)]
        cnt[regime(rules, L, 1).split()[0]] += 1
    for k in ("dyadic", "BYPASSED", "BOTTLENECK", "ENRICHER"):
        print(f"    {k:<12} {cnt[k]:4d}  ({100 * cnt[k] / 500:4.1f}%)")

    print("\n[4] Ride-hail disintermediation trajectory (platform P=D&R fixed; off-platform contact grows)")
    Lp = ("D", "P", "R")
    P = lambda x: x[0] & x[2]
    traj = {
        "0 no off-platform contact": [lambda x: x[1], P, lambda x: x[1]],
        "1 complement off-platform": [lambda x: x[1] & x[2], P, lambda x: x[1] & x[0]],
        "2 substitute off-platform":  [lambda x: x[1] | x[2], P, lambda x: x[1] | x[0]],
    }
    for name, r in traj.items():
        print(f"    {name:<28} -> {regime(r, Lp, 1)}")

    print("\n" + "=" * 92)
    print("  Load-bearing is relational: whether the platform is in the core is a property of the")
    print("  whole arrangement (a Φ-competition with the parties' own coalition), not of the platform.")
    print("=" * 92)
    return 0


if __name__ == "__main__":
    sys.exit(main())
