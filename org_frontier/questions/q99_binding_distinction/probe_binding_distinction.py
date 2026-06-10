"""Probe Q99 (H1-H4) — is the dual binding pair the common shape of irreducible coordination?

Reads the cause-effect structure of structurally different triads (joint determination, chain, ring,
required market) and dyadic controls, and tests whether each triad carries the spanning/joint dual pair.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q99_binding_distinction.probe_binding_distinction
"""

import csv
import os

from org_frontier.questions.q99_binding_distinction import forms as F


def analyse(name, rules, labels):
    phi, dists = F.ces(rules, labels)
    dp = F.dual_pair(dists)
    max_pd = max((pd for _, _, pd in dists), default=0.0)
    max_is_joint = any(len(m) >= 2 and abs(pd - max_pd) < 1e-9 and abs(pd - phi) < 1e-9
                       for m, _, pd in dists)
    covered = set()
    if dp:
        for key in ("spanning", "joint"):
            m, p, _ = dp[key]
            covered |= set(m) | set(p)
    spans_all = covered == set(labels)
    print(f"  {name:<24} Φ={phi:<5} dual_pair={'yes' if dp else 'no ':<3}"
          f" max_is_joint={max_is_joint} spans_all={spans_all}")
    if dp:
        print(f"  {'':24} spanning {dp['spanning'][0]}->{dp['spanning'][1]} | "
              f"joint {dp['joint'][0]}->{dp['joint'][1]}")
    return {"name": name, "phi": phi, "dual": bool(dp), "max_is_joint": max_is_joint,
            "spans_all": spans_all}


def main():
    print("PROBE Q99 (H1-H4) — the dual binding pair across triadic and dyadic forms")
    print("=" * 80)
    print("TRIADIC:")
    tri = [analyse(n, r, l) for n, (r, l) in F.TRIADIC.items()]
    print("DYADIC:")
    dya = [analyse(n, r, l) for n, (r, l) in F.DYADIC.items()]

    h1 = all(t["dual"] for t in tri)
    h2 = all(t["max_is_joint"] for t in tri)
    h3 = not any(d["dual"] for d in dya)
    h4 = all(t["spans_all"] for t in tri)
    print("=" * 80)
    print(f"  H1 every triadic form carries a dual binding pair:           {h1}")
    print(f"  H2 the maximal distinction is a joint mechanism (φ_d=Φ):     {h2}")
    print(f"  H3 no dyadic form carries a dual pair:                       {h3}")
    print(f"  H4 the dual pair spans every party of the form:              {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "binding_distinction.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "class", "phi", "dual_pair", "max_is_joint", "spans_all"])
        for t in tri:
            w.writerow([t["name"], "triadic", t["phi"], t["dual"], t["max_is_joint"], t["spans_all"]])
        for d in dya:
            w.writerow([d["name"], "dyadic", d["phi"], d["dual"], d["max_is_joint"], d["spans_all"]])


if __name__ == "__main__":
    main()
