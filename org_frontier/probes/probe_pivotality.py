"""Probe 11 — does pivotality predict core membership?

Probes 2, 7, 10 suggested a mechanism: a party is in the irreducible core only if the determination
makes it pivotal (its state can change the outcome). This tests that as a predictor across a
population, controlling for the bidirectional condition by fixing every party to read S.

Setup (n=4: W, S, C1, C2). W' = C1' = C2' = S (all parties coupled both ways). Sweep all 256
determinations S' = f(W, C1, C2). For each party X, compute its INFLUENCE on the determination =
the fraction of the 8 input configurations in which flipping X flips S' (Boolean sensitivity). Then
compute the major complex and record whether X is in it. 256 forms x 3 parties = 768 observations.

H11: influence predicts core membership — zero influence (S ignores X) is never in core, and higher
influence raises P(X in core).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_pivotality
"""

import csv
import os

from .lib import major_complex

LABELS = ("W", "S", "C1", "C2")
_RESULTS = os.path.join(os.path.dirname(__file__), "results")

# config encodes (W, C1, C2) as W | C1<<1 | C2<<2; party -> (config bit, node index, label)
PARTIES = [("W", 0, 0), ("C1", 1, 2), ("C2", 2, 3)]


def influence(table, cfg_bit):
    """Fraction of the 8 configs where flipping the given input flips S'."""
    return sum(table[c] != table[c ^ (1 << cfg_bit)] for c in range(8)) / 8.0


def main():
    rows = []
    for m in range(256):
        table = [(m >> k) & 1 for k in range(8)]   # S' over (W,C1,C2)

        def s_rule(x, table=table):
            return table[(x[0] & 1) | ((x[2] & 1) << 1) | ((x[3] & 1) << 2)]

        rules = [lambda x: x[1], s_rule, lambda x: x[1], lambda x: x[1]]
        core, _ = major_complex(rules, LABELS)
        core = core or ()
        for label, cfg_bit, _idx in PARTIES:
            rows.append({"form": m, "party": label,
                         "influence": influence(table, cfg_bit),
                         "in_core": label in core})

    os.makedirs(_RESULTS, exist_ok=True)
    with open(os.path.join(_RESULTS, "pivotality.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    # P(in core) by influence level
    print("PROBE 11 — pivotality predicts core membership? (768 party-observations)")
    print("=" * 80)
    levels = sorted({r["influence"] for r in rows})
    print("  influence   n     P(in core)")
    for lv in levels:
        grp = [r for r in rows if r["influence"] == lv]
        pin = sum(r["in_core"] for r in grp) / len(grp)
        print(f"   {lv:.3f}     {len(grp):>4}    {100*pin:5.1f}%")
    # zero-influence never in core?
    zero = [r for r in rows if r["influence"] == 0.0]
    zero_in = sum(r["in_core"] for r in zero)
    # rank-AUC: does higher influence rank above lower for in-core vs not?
    pos = [r["influence"] for r in rows if r["in_core"]]
    neg = [r["influence"] for r in rows if not r["in_core"]]
    if pos and neg:
        wins = sum(p > n for p in pos for n in neg) + 0.5 * sum(p == n for p in pos for n in neg)
        auc = wins / (len(pos) * len(neg))
    else:
        auc = float("nan")
    print("=" * 80)
    print(f"  zero-influence observations in core: {zero_in}/{len(zero)} "
          f"({'NEVER' if zero_in == 0 else 'some'} — influence is necessary)")
    print(f"  rank-AUC (influence predicts in-core): {auc:.3f}")
    print("=" * 80)


if __name__ == "__main__":
    main()
