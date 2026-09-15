"""Probe — Heider H1: balance is a property of the sign product.

Question.  Heider (1946: 110): a triad is balanced if all three relations are positive or two are negative
           and one positive; Cartwright & Harary: iff the sign product is positive. Under signed majority
           with hold, do the eight sign patterns fall into exactly two structural classes matching the
           product — and is the balanced class the one with the higher Φ (Heider's "unit")?
Hypothesis. H1: two classes by product; Φ(balanced) > Φ(unbalanced).
Method.    All eight sign vectors on (po, pq, oq); Φ_MIP, core, attractors, rest states.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.heider.probe_heider_balance
"""

import itertools

from org_frontier.thinkers.heider import forms as F


def main():
    print("Heider H1 — balance as sign product: the eight signed triads")
    control = F.run_control()
    recs = {}
    for signs in itertools.product((1, -1), repeat=3):
        name = "triad_" + F.sign_str(signs).replace("−", "m").replace("+", "p")
        recs[name] = F.evaluate(name, F.triad(signs), F.TRIAD_LABELS, F.TRIAD_EDGES, signs)
        print(F.line(recs[name]))

    def key(r):
        return (r["phi_mip"], len(r["core"]), tuple(sorted(len(a) for a in r["attractors"])))

    classes = {}
    for r in recs.values():
        classes.setdefault(key(r), []).append(r)
    by_product = {1: {key(r) for r in recs.values() if r["product"] == 1},
                  -1: {key(r) for r in recs.values() if r["product"] == -1}}
    two_classes = len(classes) == 2 and len(by_product[1]) == 1 and len(by_product[-1]) == 1
    phi_bal = next(iter(by_product[1]))[0] if len(by_product[1]) == 1 else None
    phi_unb = next(iter(by_product[-1]))[0] if len(by_product[-1]) == 1 else None
    print("  structural classes=%d  balanced (product +) Φ_MIP=%s  unbalanced (product −) Φ_MIP=%s"
          % (len(classes), phi_bal, phi_unb))
    if two_classes and phi_bal > phi_unb:
        status = "CONFIRMED"
    elif two_classes:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H1 (two classes by sign product, and the balanced class has the greater Φ): %s" % status)
    F.save("probe_heider_balance", {"control": control, "forms": recs, "n_classes": len(classes),
                                     "phi_balanced": phi_bal, "phi_unbalanced": phi_unb, "H1": status})


if __name__ == "__main__":
    main()
