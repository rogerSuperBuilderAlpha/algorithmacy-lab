"""Probe — Peirce H1: triadic irreducibility (the negative clause of the reduction thesis).

Question.  Peirce (CP 2.274): a genuine triad's "three members are bound together by it in a way that does
           not consist in any complexus of dyadic relations." Does any wiring of one-input (copy) rules at
           n = 3 (8 wirings) or n = 4 (81 wirings) contain an irreducible distinction of adicity 3?
Hypothesis. H1 (Peirce): none does; the control (one two-input rule) has adicity 3.
Method.    genuine_adicity over all reachable states for every one-input wiring; whole Φ and core alongside.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.peirce.probe_peirce_irreducibility
"""

from org_frontier.thinkers.peirce import forms as F


def main():
    print("Peirce H1 — triadic irreducibility: one-input wirings at n = 3 and n = 4")
    control = F.run_control()
    recs = []
    for n in (3, 4):
        for name, form in F.one_input_wirings(n):
            rec = F.evaluate(name, form)
            rec["n"] = n
            recs.append(rec)
    max_ad = max(r["genuine_adicity"] for r in recs)
    n_whole = sum(1 for r in recs if r["phi_mip"] > 0)
    by_ad = {}
    for r in recs:
        by_ad[r["genuine_adicity"]] = by_ad.get(r["genuine_adicity"], 0) + 1
    print("  wirings=%d  max genuine adicity=%d  adicity counts=%s  whole-irreducible (Φ>0)=%d"
          % (len(recs), max_ad, dict(sorted(by_ad.items())), n_whole))
    status = "CONFIRMED" if (max_ad <= 2 and control["genuine_adicity"] == 3) else "REFUTED"
    print("H1 (no complexus of dyads reaches adicity 3): %s" % status)
    # Post hoc (not pre-registered): split the wirings by whether any node is read by two or more others —
    # a branch point, Peirce's "branching of a line" (CP 8.331), Burch's teridentity.
    def branched(rec):
        srcs = rec["form"][len("copy_"):]
        return any(srcs.count(ch) >= 2 for ch in set(srcs))
    unbranched = [r for r in recs if not branched(r)]
    branches = [r for r in recs if branched(r)]
    max_cause = max(r["cause_adicity"] for r in recs)
    print("  post hoc: unbranched wirings (pure cycles and their products)=%d, max adicity=%d, Φ>0 in %d;"
          " branched wirings=%d, min adicity=%d, Φ>0 in %d; max cause-side adicity over all=%d"
          % (len(unbranched), max(r["genuine_adicity"] for r in unbranched),
             sum(1 for r in unbranched if r["phi_mip"] > 0),
             len(branches), min(r["genuine_adicity"] for r in branches),
             sum(1 for r in branches if r["phi_mip"] > 0), max_cause))
    F.save("probe_peirce_irreducibility", {"control": control, "forms": recs, "max_adicity": max_ad,
                                            "adicity_counts": by_ad, "n_whole_irreducible": n_whole, "H1": status,
                                            "post_hoc": {"n_unbranched": len(unbranched), "n_branched": len(branches),
                                                         "max_cause_adicity": max_cause}})


if __name__ == "__main__":
    main()
