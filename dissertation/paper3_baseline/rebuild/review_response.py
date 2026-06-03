"""Paper 3 rebuild — computations answering the Stage-4 round-1 review (compute, don't assert).

The three reviewers reproduced every number. Their charges are about what the numbers mean.
Several are settleable by computation:

1. R2: "the 2.00 band is NOT the strict-mediation band." Compute the composition of the Φ=2.00
   band and the Φ distribution of the 40 canonical strict-mediation wirings.
2. R2/R3: "MTurk's 3.00 is a pure size artifact (Φ = n-1)." Compute strict-AND across n=3,4,5.
3. R2: "dedup removed nothing / 4,144 = 4,096 + 48." Report the dedup count.
4. R3: the equal-Φ pairs are identical TPMs (so the equality is true by construction). Check.
5. R3: the case codings carry the result (Upwork AND vs OR; exchange conduit vs market-maker).
6. R2: "Φ is 0.83" should be "max Φ over reachable states is 0.83" — the partial form is
   reducible at the all-on state. Per-state profile.

Run: ~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/rebuild/review_response.py
"""

import csv
import os
import sys
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import numpy as np
from phi_core import tpm_from_rules, cm_from_rules, phi_over_states, placement


def sec(n, t):
    print("\n" + "=" * 80)
    print(f"{n}. {t}")
    print("=" * 80)


def s1_band_composition():
    sec(1, "Is the 2.00 band the 'strict-mediation band'? (R2-Obj1)")
    path = os.path.join(_HERE, "results", "catalog.csv")
    rows = [r for r in csv.DictReader(open(path)) if r["kind"] == "triad"]
    band200 = [r for r in rows if abs(float(r["max_phi"]) - 2.0) < 1e-6]
    strict200 = [r for r in band200 if int(r["strict_mediation"]) == 1]
    print(f"   Φ=2.00 band: {len(band200)} wirings; strict_mediation=1 among them: {len(strict200)}")
    strict_all = [r for r in rows if int(r["strict_mediation"]) == 1]
    dist = Counter(round(float(r["max_phi"]), 2) for r in strict_all)
    print(f"   canonical strict-mediation wirings: {len(strict_all)} total")
    print(f"   their Φ distribution: {dict(sorted(dist.items()))}")
    print("   => 'strict mediation' is necessary-context, not sufficient: the mediator's Boolean")
    print("      function decides the band (AND-family -> 2.00; parity -> 0.50; some -> 0).")
    print("      This is the STRONGEST evidence for 'Φ is not a feature checklist'.")


def s2_size_law():
    sec(2, "Is the higher-order 3.00 a pure size artifact, Φ = n-1? (R2-Obj2, R3-Obj2)")
    for n in (3, 4, 5):
        # strict-AND: S (node 1) = AND of all other nodes; every other node reads S.
        def mk(n):
            others = [i for i in range(n) if i != 1]
            rules = []
            for j in range(n):
                if j == 1:
                    rules.append(lambda x, o=others: int(all(x[i] for i in o)))
                else:
                    rules.append(lambda x: x[1])
            return rules
        r = placement(mk(n), n)
        print(f"   n={n}: strict-AND mediator  maxΦ = {r['max']:.4f}   (n-1 = {n-1})")
    print("   => for this family Φ = n-1 exactly; MTurk's 3.00 conveys 'n=4 and strict', not more.")
    print("      The §5.5/§8 'partly a function of size' caveat understates it: it is ALL size.")


def s3_dedup():
    sec(3, "Did dedup-by-TPM remove any wirings? (R2-Obj3)")
    from catalog import enumerate_triads, enumerate_higher_order
    seen, n_triad, dup_triad = set(), 0, 0
    for kind, label, rules, n, mtag, parity in enumerate_triads():
        key = tpm_from_rules(rules, n).tobytes()
        n_triad += 1
        if key in seen:
            dup_triad += 1
        seen.add(key)
    seen_ho, n_ho, dup_ho = set(), 0, 0
    for kind, label, rules, n, mtag, parity in enumerate_higher_order():
        key = tpm_from_rules(rules, n).tobytes()
        n_ho += 1
        if key in seen_ho:
            dup_ho += 1
        seen_ho.add(key)
    print(f"   triads enumerated: {n_triad}; duplicate TPMs removed: {dup_triad}")
    print(f"   higher-order enumerated: {n_ho}; duplicate TPMs removed: {dup_ho}")
    print(f"   distinct total: {n_triad - dup_triad + n_ho - dup_ho}")
    print("   => dedup removed 0; '4,144 distinct after removing duplicates' = 4,096 + 48, no")
    print("      reduction. The triad family is complete; the 48 HO forms are a structured SAMPLE,")
    print("      not a complete 4-node family. Do not let 'complete family' bleed onto n=4.")


def s4_identical_pairs():
    sec(4, "Are the equal-Φ pairs identical TPMs? (R3-Obj1 — equality true by construction)")
    from cases import CASES
    by = {c[0]: c for c in CASES}
    def tpm_of(name):
        _, _, _, _, rules, n = by[name]
        return tpm_from_rules(rules, n)
    pairs = [("Uber (ride-hailing)", "NYSE / Nasdaq (securities exchange)"),
             ("Upwork (freelance marketplace)", "ManpowerGroup (staffing firm)")]
    for a, b in pairs:
        same = np.array_equal(tpm_of(a), tpm_of(b))
        print(f"   {a.split(' (')[0]:14s} vs {b.split(' (')[0]:14s}: identical TPM = {same}")
    print("   => within a pair the systems are the SAME object; equal Φ is a theorem, not a")
    print("      finding. 'literal replication' across a pair is the same computation run twice.")


def s5_coding_sensitivity():
    sec(5, "Do the case codings carry the result? (R3-Obj2 — sensitivity of the bands)")
    cases = {
        "Upwork partial, match=AND  W'=S∨C,S'=W∧C,C'=S∨W": [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[1] | x[0]],
        "Upwork partial, match=OR   W'=S∨C,S'=W∨C,C'=S∨W": [lambda x: x[1] | x[2], lambda x: x[0] | x[2], lambda x: x[1] | x[0]],
        "Exchange strict (drafted)  W'=S,  S'=W∧C, C'=S":   [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        "Exchange market-maker      W'=S,  S'=S,   C'=S":   [lambda x: x[1], lambda x: x[1], lambda x: x[1]],
    }
    for label, rules in cases.items():
        r = placement(rules, 3)
        print(f"   {label:44s} maxΦ = {r['max']:.4f}")
    print("   => the AND-vs-OR match choice moves Upwork 0.83 -> 6.00; a market-maker reading of the")
    print("      exchange collapses it to 0.00. The codings are author choices; §5 must show adversarial")
    print("      rival codings and why the documented mechanism forces the chosen one.")


def s6_partial_per_state():
    sec(6, "Is the partial 0.83 form reducible at the all-on state? (R2-Obj5b)")
    rules = [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[1] | x[0]]
    tpm, cm = tpm_from_rules(rules, 3), cm_from_rules(rules, 3)
    for st, phi in phi_over_states(tpm, cm, 3):
        print(f"   state {st}:  Φ = {phi:.4f}")
    print("   => max Φ over reachable states is 0.83; the form is reducible (Φ=0) at the all-on")
    print("      state. The draft should say 'max Φ is 0.83', matching Paper 2's reachable-max rule.")


if __name__ == "__main__":
    s1_band_composition()
    s2_size_law()
    s3_dedup()
    s4_identical_pairs()
    s5_coding_sensitivity()
    s6_partial_per_state()
