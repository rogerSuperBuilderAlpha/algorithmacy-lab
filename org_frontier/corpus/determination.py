"""Which determination functions support irreducibility?

Re-analyzes the n=3 strict-mediation population (`results/population.csv`) by the mediator's Boolean
function. Decodes the function index from each form's label (W{iw}_S{is}_C{ic}; is = the 2-input
function index 0-15) and asks, for each of the 16 two-input functions, how many of its 16 forms
(4 W-reads x 4 C-reads) are triadic.

The dissertation found the mediator's function dominates Φ *magnitude*. This asks the prior
question: which functions support the triadic *verdict* at all.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.corpus.determination
"""

import collections
import csv
import os

_RESULTS = os.path.join(os.path.dirname(__file__), "results")

_NAMES = {
    (0, 0, 0, 0): "FALSE", (1, 1, 1, 1): "TRUE", (0, 0, 0, 1): "AND", (1, 1, 1, 0): "NAND",
    (0, 1, 1, 1): "OR", (1, 0, 0, 0): "NOR", (0, 1, 1, 0): "XOR", (1, 0, 0, 1): "XNOR",
    (0, 1, 0, 0): "W&~C", (0, 0, 1, 0): "~W&C", (1, 1, 0, 1): "~W|C", (1, 0, 1, 1): "W|~C",
    (1, 0, 1, 0): "~W", (0, 1, 0, 1): "W", (1, 1, 0, 0): "~C", (0, 0, 1, 1): "C",
}


def fname(m):
    return _NAMES.get(tuple((m >> k) & 1 for k in range(4)), f"f{m}")


def main():
    path = os.path.join(_RESULTS, "population.csv")
    rows = list(csv.DictReader(open(path)))
    tri = collections.Counter()
    tot = collections.Counter()
    for r in rows:
        s_idx = int(r["label"].split("_S")[1].split("_")[0])
        fn = fname(s_idx)
        tot[fn] += 1
        if r["structure"] == "triadic":
            tri[fn] += 1

    print("WHICH DETERMINATION FUNCTIONS SUPPORT IRREDUCIBILITY (n=3 strict mediation)")
    print("=" * 72)
    print("  mediator fn   triadic/total   depends-on")
    for fn in sorted(tot, key=lambda f: (-tri[f], f)):
        dep = "both" if tri[fn] else ("one/none")
        print(f"  {fn:<8}        {tri[fn]:>2}/{tot[fn]:<3}        {dep}")
    zero = sorted(f for f in tot if not tri[f])
    parity = [f for f in ("XOR", "XNOR") if tri[f]]
    print("=" * 72)
    print(f"  zero triadic forms: {', '.join(zero)} (one-input or constant — never reads both)")
    if parity:
        print(f"  parity functions {parity} lead: {tri['XOR']}/16 each vs 2/16 for monotone AND/OR/…")


if __name__ == "__main__":
    main()
