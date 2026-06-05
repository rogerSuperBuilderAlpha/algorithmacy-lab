#!/usr/bin/env python
"""Q43 / H1 — the naive Thompson ordering fails under one uniform modeling convention.

Form / ensemble: a matched triple at n=3, AND determination family, little-endian.
  Pooled (independent-contribution relay):  [x->S, x->W, x->S]
  Sequential (pass-through chain):           [x->S, x->(W&C), x->S]
  Reciprocal (feedback cycle, cyclic form):  [x->S, x->(W&C), x->S]
Labels (W, S, C).

Measure: verdict().structure and .max_phi for each; rank the three Φ.

Instrument control (run first): the pass-through mediator chain at n=3 must read triadic,
max_phi = 2.0, MIP "2 parts: {W,SC}". Abort if it fails.

Decision rule (fixed before run): H1 confirmed if pooled is not the strict Φ-minimum OR
sequential Φ does not fall strictly between pooled and reciprocal; refuted only if the three
Φ are strictly monotone in Thompson order with pooled dyadic.
"""

import csv
import os
import sys

# Repo root onto sys.path so this runs as a direct script and via the package.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import classify_rules, PHI_EPS  # noqa: E402
from org_frontier.probes.lib import verdict  # noqa: E402

LABELS = ("W", "S", "C")

# --- Forms (n=3, AND family, little-endian; x[0]=W, x[1]=S, x[2]=C) ---
POOLED = [lambda x: x[1], lambda x: x[0], lambda x: x[1]]
SEQUENTIAL = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
RECIPROCAL = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def instrument_control():
    """The pass-through chain must read triadic at Φ=2.0 with MIP '2 parts: {W,SC}'."""
    v = verdict(SEQUENTIAL, LABELS)
    assert v.structure == "triadic", f"control structure {v.structure!r} != 'triadic'"
    assert abs(v.max_phi - 2.0) < 1e-6, f"control max_phi {v.max_phi} != 2.0"
    assert v.mip_partition == "2 parts: {W,SC}", (
        f"control MIP {v.mip_partition!r} != '2 parts: {{W,SC}}'"
    )
    return v


def main():
    print("=== Q43 / H1 — Thompson ordering under one uniform convention (n=3, AND) ===")

    ctrl = instrument_control()
    print("[instrument control] pass-through chain: "
          f"structure={ctrl.structure}, max_phi={ctrl.max_phi:.6f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    forms = [
        ("pooled", "independent-contribution relay", POOLED),
        ("sequential", "pass-through chain", SEQUENTIAL),
        ("reciprocal", "feedback cycle (cyclic)", RECIPROCAL),
    ]

    rows = []
    for name, desc, rules in forms:
        v = classify_rules(rules, labels=LABELS)
        rows.append({
            "thompson_type": name,
            "form": desc,
            "structure": v.structure,
            "max_phi": v.max_phi,
            "mip_partition": v.mip_partition,
            "n_states_irreducible": v.n_states_irreducible,
        })
        print(f"\n[{name}] {desc}")
        print(f"    structure   = {v.structure}")
        print(f"    max_phi     = {v.max_phi:.6f}")
        print(f"    MIP         = {v.mip_partition!r}")

    phi = {r["thompson_type"]: r["max_phi"] for r in rows}
    struct = {r["thompson_type"]: r["structure"] for r in rows}
    p_pool, p_seq, p_rec = phi["pooled"], phi["sequential"], phi["reciprocal"]

    print("\n=== Φ ranking (Thompson order: pooled, sequential, reciprocal) ===")
    print(f"    pooled     Φ = {p_pool:.6f} ({struct['pooled']})")
    print(f"    sequential Φ = {p_seq:.6f} ({struct['sequential']})")
    print(f"    reciprocal Φ = {p_rec:.6f} ({struct['reciprocal']})")

    # Decision rule (fixed before run).
    pooled_is_strict_min = (p_pool < p_seq - PHI_EPS) and (p_pool < p_rec - PHI_EPS)
    seq_strictly_between = (p_pool + PHI_EPS < p_seq) and (p_seq + PHI_EPS < p_rec)
    pooled_dyadic = struct["pooled"] == "dyadic"

    strict_monotone = (
        pooled_dyadic
        and (p_pool + PHI_EPS < p_seq)
        and (p_seq + PHI_EPS < p_rec)
    )

    step1_fails = not pooled_is_strict_min  # pooled not the strict minimum
    step2_fails = not seq_strictly_between  # sequential not strictly between

    if step1_fails or step2_fails:
        decision = "confirmed"
    elif strict_monotone:
        decision = "refuted"
    else:
        decision = "partial"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    pooled is strict Φ-minimum?            {pooled_is_strict_min}")
    print(f"    sequential strictly between pool/recip? {seq_strictly_between}")
    print(f"    pooled dyadic?                          {pooled_dyadic}")
    print(f"    strictly monotone in Thompson order?    {strict_monotone}")
    print(f"    H1 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "thompson_ordering.csv")
    with open(csv_path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"\nwrote {csv_path}")

    return decision


if __name__ == "__main__":
    main()
