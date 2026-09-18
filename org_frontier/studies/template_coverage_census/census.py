"""Census: which triadic forms escape the four catalog templates?

Closes the catalog README's open signal — a form that fits none of relay / conjunctive / additive /
free is the cue for a fifth template — and answers RESEARCH_AGENDA_50_V2 F27 (is the holistic
residual the affine class?). Hypotheses fixed in hypotheses.md before this run.

Run:  python org_frontier/studies/template_coverage_census/census.py
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict

from org_frontier.classifier.classifier import classify_rules
from org_frontier.classifier.contingency import contingency_test
from org_frontier.corpus.determination import fname
from org_frontier.corpus.population import enumerate_family
from org_frontier.studies.template_coverage_census.signatures import (
    FOUR,
    PARITY_TABLES,
    commit_table,
    is_affine_2,
    match_templates,
)

LABELS = ("W", "S", "C")
PANEL = os.path.join(_REPO_ROOT, "org_frontier", "probes", "results", "residual_panel.csv")
FEATURES = ("n_edges", "n_bidir", "strongly_connected", "syn_sum", "syn_min", "syn_max",
            "n_fixed", "n_reachable", "invertible", "max_period")
RESULTS = os.path.join(os.path.dirname(__file__), "results")


def instrument_control():
    """Canonical triad and catalog templates must reproduce known verdicts before the census."""
    print("INSTRUMENT CONTROL")
    print("-" * 72)
    conj = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    relay = [lambda x: x[2], lambda x: x[0], lambda x: x[1]]
    free = [lambda x: x[2], lambda x: x[0], lambda x: x[0]]
    xor = [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]]
    checks = []
    for name, rules, expect_struct, expect_phi in (
        ("conjunctive triad", conj, "triadic", 2.0),
        ("relay cycle", relay, "triadic", 2.0),
        ("free conduit", free, "dyadic", 0.0),
        ("parity XOR triad", xor, "triadic", 0.5),
    ):
        v = classify_rules(rules, labels=("A", "M", "B"))
        ok = v.structure == expect_struct and abs(v.max_phi - expect_phi) < 1e-6
        checks.append(ok)
        print(f"  {name:<22} {v.structure:<8} Φ={v.max_phi:.6f}  "
              f"{'PASS' if ok else 'FAIL (expected %s Φ=%s)' % (expect_struct, expect_phi)}")
    # signature matcher sanity on the same forms
    assert "conjunctive" in match_templates(conj) and "parity" not in match_templates(conj)
    assert "relay" in match_templates(relay)
    assert "free" in match_templates(free)
    assert "parity" in match_templates(xor) and "conjunctive" not in match_templates(xor)
    if not all(checks):
        raise SystemExit("ABORT: instrument control failed")
    print("  instrument control: PASS")
    print()


def census_strict_mediation():
    """H1: among the 24 triadic SM forms, how many escape the four templates?"""
    print("H1 — TEMPLATE COVERAGE CENSUS (strict-mediation n=3, 256 forms)")
    print("-" * 72)
    triadic = []
    for label, rules in enumerate_family():
        v = classify_rules(rules, labels=LABELS)
        if v.structure != "triadic":
            continue
        hits = match_templates(rules)
        four_hits = hits & FOUR
        table = commit_table(rules)
        s_idx = int(label.split("_S")[1].split("_")[0])
        triadic.append({
            "label": label,
            "phi": round(v.max_phi, 6),
            "commit": fname(s_idx),
            "table": table,
            "templates": sorted(hits),
            "four": sorted(four_hits),
            "residual": len(four_hits) == 0,
            "parity": table in PARITY_TABLES,
        })

    n_tri = len(triadic)
    n_res = sum(r["residual"] for r in triadic)
    n_parity = sum(r["parity"] for r in triadic)
    n_conj = sum("conjunctive" in r["templates"] for r in triadic)
    phi_bands = {}
    for r in triadic:
        phi_bands.setdefault(r["phi"], 0)
        phi_bands[r["phi"]] += 1

    print(f"  triadic forms:              {n_tri}")
    print(f"  matching conjunctive:       {n_conj}")
    print(f"  matching relay/additive/free among triadic: "
          f"{sum(bool(set(r['four']) - {'conjunctive'}) for r in triadic)}")
    print(f"  outside the four templates: {n_res}")
    print(f"  of which parity (XOR/XNOR): {sum(r['residual'] and r['parity'] for r in triadic)}")
    print(f"  residual rate:              {100.0 * n_res / n_tri:.1f}% of triadic "
          f"({n_res}/{n_tri})")
    print(f"  Φ bands among triadic:      "
          + ", ".join(f"{p}×{c}" for p, c in sorted(phi_bands.items(), reverse=True)))

    # residual characterization
    residual = [r for r in triadic if r["residual"]]
    print("  residual forms:")
    for r in residual:
        print(f"    {r['label']:<14} commit={r['commit']:<6} Φ={r['phi']}  "
              f"templates={r['templates'] or ['(none of four)']}")

    all_residual_are_parity = n_res == n_parity and n_res > 0 and all(
        r["parity"] for r in residual
    )
    h1 = "SUPPORTED" if all_residual_are_parity else "REFUTED"
    print(f"  H1 (residual nonempty and exactly the 8 parity forms): {h1}")
    print()
    return {
        "n_triadic": n_tri,
        "n_residual": n_res,
        "n_parity": n_parity,
        "n_conjunctive": n_conj,
        "residual_rate": n_res / n_tri,
        "h1": h1,
        "triadic": triadic,
        "phi_bands": phi_bands,
    }


def h2_parity_contingency():
    """H2: worked parity forms classify intrinsic under the bypass-counterfactual."""
    print("H2 — PARITY BYPASS-COUNTERFACTUAL (candidate fifth template)")
    print("-" * 72)
    forms = {
        "parity_xor": (
            ("A", "M", "B"),
            [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]],
        ),
        "parity_xnor": (
            ("A", "M", "B"),
            [lambda x: x[1], lambda x: 1 - (x[0] ^ x[2]), lambda x: x[1]],
        ),
    }
    kinds = []
    for name, (labels, rules) in forms.items():
        v = classify_rules(rules, labels=labels)
        r = contingency_test(rules, labels, "M", downstream="B", upstream="A", mode="replace")
        kinds.append(r.kind)
        print(f"  {name:<14} structure={v.structure} Φ={v.max_phi:.3f}  "
              f"class={r.kind} margin={r.margin:.3f}  "
              f"core {r.core_constrained} -> {r.core_bypass}")
    h2 = "SUPPORTED" if kinds == ["intrinsic", "intrinsic"] else "REFUTED"
    print(f"  H2 (parity XOR and XNOR both intrinsic/necessary): {h2}")
    print()
    return {"h2": h2, "kinds": kinds}


def h3_holistic_affine():
    """H3 / F27: are the Probe-131 RF misses exactly the affine wirings?"""
    print("H3 — HOLISTIC RESIDUAL vs AFFINE/GF(2) (F27)")
    print("-" * 72)
    rows = list(csv.DictReader(open(PANEL)))
    assert len(rows) == 4096, f"expected 4096-panel rows, got {len(rows)}"
    X = np.array([[float(r[f]) for f in FEATURES] for r in rows])
    y = np.array([int(r["triadic"]) for r in rows])
    clf = RandomForestClassifier(n_estimators=400, random_state=0, n_jobs=-1)
    proba = cross_val_predict(clf, X, y, cv=5, method="predict_proba")[:, 1]
    pred = (proba >= 0.5).astype(int)
    miss = pred != y
    n_miss = int(miss.sum())
    rate = float(miss.mean())

    tables = [tuple((m >> k) & 1 for k in range(4)) for m in range(16)]
    affine = []
    for ta in tables:
        for tb in tables:
            for tc in tables:
                affine.append(int(is_affine_2(ta) and is_affine_2(tb) and is_affine_2(tc)))
    affine = np.array(affine)
    assert len(affine) == 4096

    n_affine = int(affine.sum())
    n_affine_miss = int((miss & (affine == 1)).sum())
    miss_affine_frac = float(affine[miss].mean()) if n_miss else 0.0
    near = float(np.mean(np.abs(proba[miss] - 0.5) < 0.25)) if n_miss else 0.0

    print(f"  wirings:                    {len(y)}")
    print(f"  RF misclassified (holistic residual): {n_miss} ({100 * rate:.1f}%)")
    print(f"  affine wirings (all-3 rules GF(2)-linear): {n_affine}")
    print(f"  affine among residual misses: {n_affine_miss}/{n_miss} "
          f"({100 * miss_affine_frac:.1f}%)")
    print(f"  miss rate among affine:     {100 * miss[affine == 1].mean():.1f}%")
    print(f"  miss rate among non-affine: {100 * miss[affine == 0].mean():.1f}%")
    print(f"  residual near-boundary (|p-0.5|<0.25): {near:.2f}")

    # F27 claims residual == affine. Refuted if overlap empty or sets differ.
    h3 = "SUPPORTED" if (n_miss == n_affine and n_affine_miss == n_miss and n_miss > 0) else "REFUTED"
    print(f"  H3 (holistic residual == affine class, F27): {h3}")
    print()
    return {
        "h3": h3,
        "n_miss": n_miss,
        "residual_rate": rate,
        "n_affine": n_affine,
        "n_affine_miss": n_affine_miss,
        "near_boundary": near,
    }


def h4_n4_scope():
    """F26: n=4 residual rate — document why not in this run."""
    print("H4 — n=4 HOLISTIC RESIDUAL (F26), SCOPE")
    print("-" * 72)
    print("  A Probe-125-style cheap panel at n=4 needs an enumerated family with exact Φ labels.")
    print("  The n=4 strict-mediation family is 4^3 × 256 = 16,384 forms for unary party reads and")
    print("  a 3-input mediator already, and the unconstrained 2-input-per-node analogue of the")
    print("  4096 is 16^4 = 65,536 wirings — each exact-Φ evaluation is materially slower at n=4.")
    print("  This run therefore does not re-estimate the residual fraction at n=4.")
    print("  Follow-up: build an n=4 residual panel on a fixed sample (e.g. N=3000 as in probe_n4_census)")
    print("  with the same cheap-feature set, report RF miss rate vs the n=3 4.8% baseline (F26).")
    print("  H4: SCOPED OUT (precise follow-up left)")
    print()
    return {"h4": "SCOPED_OUT"}


def write_results(c1, c2, c3):
    os.makedirs(RESULTS, exist_ok=True)
    path = os.path.join(RESULTS, "census.csv")
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=[
            "label", "phi", "commit", "residual", "parity", "templates",
        ])
        w.writeheader()
        for r in c1["triadic"]:
            w.writerow({
                "label": r["label"],
                "phi": r["phi"],
                "commit": r["commit"],
                "residual": int(r["residual"]),
                "parity": int(r["parity"]),
                "templates": "|".join(r["templates"]) or "none",
            })
    print(f"  wrote {path}")


def main():
    print("TEMPLATE COVERAGE CENSUS — triad base expansion")
    print("=" * 72)
    print("  universe: 256 strict-mediation n=3 forms (24 triadic under exact Φ)")
    print("  secondary: 4096-wiring residual panel (Probe 125/131) for F27")
    print("  templates: relay / conjunctive / additive / free  (+ parity candidate)")
    print("=" * 72)
    print()
    instrument_control()
    c1 = census_strict_mediation()
    c2 = h2_parity_contingency()
    c3 = h3_holistic_affine()
    h4_n4_scope()
    write_results(c1, c2, c3)

    print("=" * 72)
    print("SUMMARY")
    print(f"  triadic forms:              {c1['n_triadic']}")
    print(f"  outside four templates:     {c1['n_residual']}")
    print(f"  residual rate:              {100 * c1['residual_rate']:.1f}%")
    print(f"  residual = parity forms:    {c1['n_parity']} (XOR/XNOR, Φ=0.5)")
    print(f"  fifth template:             parity (affine joint determination)")
    print(f"  holistic residual rate:     {100 * c3['residual_rate']:.1f}% ({c3['n_miss']}/4096)")
    print(f"  affine overlap with residual: {c3['n_affine_miss']}/{c3['n_miss']}")
    print(f"  H1={c1['h1']}  H2={c2['h2']}  H3={c3['h3']}  H4=SCOPED_OUT")
    print("=" * 72)
    assert c1["h1"] == "SUPPORTED"
    assert c2["h2"] == "SUPPORTED"
    assert c3["h3"] == "REFUTED"
    assert c1["n_triadic"] == 24
    assert c1["n_residual"] == 8
    assert c3["n_miss"] == 196


if __name__ == "__main__":
    main()
