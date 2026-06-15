"""Reproducible headline results of the enricher-regime thread (THREAD_enricher.md).

A second twenty-step dive, into the enricher regime from the mediator-in-core thread. It splits the
in-core mediator into genuine enrichment versus capture, finds enrichment rare and fragile, and lands
on an outside-option theory: a platform's irreducible core is itself plus exactly the parties without
an outside option. Reproduces the load-bearing numbers.

Run from the repo root with the venv active:  python -m org_frontier.field.threads.enricher_regime
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

L = ("W", "S", "C")


def _lesion_survives(rules):
    fW, fS, fC = rules
    return any(classify_rules([lambda y, _c=c: fW((y[0], _c, y[1])),
                               lambda y, _c=c: fC((y[0], _c, y[1]))], ("W", "C")).structure == "triadic"
               for c in (0, 1))


def regime(rules):
    """Five-way: dyadic / BYPASSED / CAPTURE / BOTTLENECK / ENRICHER for the mediator S (index 1)."""
    v = classify_rules(rules, L)
    if v.structure == "dyadic":
        return "dyadic"
    core, _ = major_complex(list(rules), L)
    core = set(core or ())
    if "S" not in core:
        return "BYPASSED"
    if core != set(L):
        return "CAPTURE"
    return "ENRICHER" if _lesion_survives(rules) else "BOTTLENECK"


def _rule(t):
    return lambda x, _t=t: _t[(x[0] << 2) | (x[1] << 1) | x[2]]


def main() -> int:
    print("=" * 92)
    print("THREAD — the enricher regime (reproducible headline results)")
    print("=" * 92)
    if not (classify_rules(factoring_control()).structure == "dyadic"
            and classify_rules(irreducible_control()).structure == "triadic"):
        print("  INSTRUMENT CONTROL FAILED — refusing to run.")
        return 1
    print("  Instrument validated.\n")

    print("[1] Refined regime frequencies over 500 random mediated forms (seed 7) — capture split out")
    random.seed(7)
    cnt = Counter()
    for _ in range(500):
        cnt[regime([_rule([random.randint(0, 1) for _ in range(8)]) for _ in range(3)])] += 1
    for k in ("dyadic", "BYPASSED", "CAPTURE", "BOTTLENECK", "ENRICHER"):
        print(f"    {k:<11} {cnt[k]:4d}  ({100 * cnt[k] / 500:4.1f}%)")
    print("    Genuine enrichment is rare; capture is the dominant in-core regime.")

    print("\n[2] Enrichment is fragile: single-bit perturbations of the symmetric escrow enricher")
    base = [[((i >> (2 - (j + 1) % 3)) & 1) & ((i >> (2 - (j + 2) % 3)) & 1) for i in range(8)]
            for j in range(3)]  # each node = AND of the other two
    random.seed(5)
    pert = Counter()
    for _ in range(150):
        t = [row[:] for row in base]
        t[random.randint(0, 2)][random.randint(0, 7)] ^= 1
        pert[regime([_rule(t[0]), _rule(t[1]), _rule(t[2])])] += 1
    print("    " + "  ".join(f"{k}:{pert[k]}" for k in ("ENRICHER", "CAPTURE", "BYPASSED", "dyadic", "BOTTLENECK")))
    print("    The canonical enricher degenerates into capture under perturbation — it is not defendable.")

    print("\n[3] Outside-option phase diagram (platform S=W&C; rows W's option, cols C's)")
    S = lambda x: x[0] & x[2]
    Wlv = {"none": lambda x: x[1], "cond": lambda x: x[1] & x[2], "full": lambda x: x[1] | x[2]}
    Clv = {"none": lambda x: x[1], "cond": lambda x: x[1] & x[0], "full": lambda x: x[1] | x[0]}
    print(f"    {'':<10}" + "".join(f"{c:<13}" for c in ("C:none", "C:cond", "C:full")))
    for wk in ("none", "cond", "full"):
        print(f"    W:{wk:<7}" + "".join(f"{regime([Wlv[wk], S, Clv[ck]]):<13}" for ck in ("none", "cond", "full")))

    print("\n[4] The core law: platform core = {S} + parties WITHOUT an outside option (4-node battery)")
    L4 = ("A", "B", "C", "P")
    P4 = lambda x: x[0] & x[1] & x[2]
    def party(i, opt):
        peer = (i + 1) % 3
        return (lambda x, _p=peer: x[3] | x[_p]) if opt else (lambda x: x[3])
    random.seed(1)
    ok = 0
    for _ in range(60):
        opts = [random.random() < 0.5 for _ in range(3)]
        rules = [party(0, opts[0]), party(1, opts[1]), party(2, opts[2]), P4]
        core, _ = major_complex(list(rules), L4)
        core = set(core or ())
        predicted = set() if all(opts) else ({"P"} | {("A", "B", "C")[i] for i in range(3) if not opts[i]})
        ok += (core == predicted) or (all(opts) and "P" not in core)
    print(f"    law holds on {ok}/60 random option configurations")

    print("\n[5] Field instrument: measure each side's outside option, read the platform's fate")
    opt = {"none": (lambda x: x[1]), "cond": (lambda x: x[1] & x[2]), "full": (lambda x: x[1] | x[2])}
    optC = {"none": (lambda x: x[1]), "cond": (lambda x: x[1] & x[0]), "full": (lambda x: x[1] | x[0])}
    for name, wk, ct in [
        ("captive worker, mobile counterpart", "none", "full"),
        ("both mobile (mature market)", "full", "full"),
        ("neither can exit (arbitration)", "none", "none"),
        ("portable reputation (escrow)", "cond", "cond"),
    ]:
        print(f"    {name:<38} [{wk}/{ct}] -> {regime([opt[wk], S, optC[ct]])}")

    print("\n" + "=" * 92)
    print("  A platform's irreducible core is itself plus the parties with no outside option.")
    print("  Bottleneck (no options) -> enricher (conditional, symmetric, fragile) -> capture")
    print("  (asymmetric options, locks in the dependent side) -> bypassed (both options).")
    print("=" * 92)
    return 0


if __name__ == "__main__":
    sys.exit(main())
