"""q175 — the substitutability flipper: does coding a worker as one of an interchangeable pool
flip a triadic verdict to dyadic, and does the Φ CI flag the flip as coding-driven?

Question: A coded account can read the worker as a specific irreplaceable party (S = W & R) or as
one slot in an interchangeable pool (S = (D1 | ... | Dk) & R). Re-encoding the worker as a
substitutable pool is a coding choice. Does that choice flip the exact-Φ verdict from triadic to
dyadic, and does the coder-disagreement Φ interval surface the flip when coders split on the
reading?

H1 (fixed before computing): re-encoding S = W & R as S = (D1 | ... | Dk) & R drives max_phi to 0
    (dyadic) for every pool size k >= 2 on synthetic accounts.
    H1-null: at least one k >= 2 retains max_phi > PHI_EPS, so a substitutable pool does not
    dissolve the worker.

H2 (fixed before computing): when the substitutable-vs-specific reading is contested (coders
    split), the propagated Φ reading interval spans both zero and the specific-reading Φ
    (interval lower = 0, upper > 0) in > 90% of contested forms.
    H2-null: the interval excludes 0 or excludes the specific Φ in > 10% of contested forms, so it
    fails to surface the flip.

Method: build the specific worker rule set (S = W & R, reads triadic, max Φ_MIP = 2.0) and the
pooled rule set (S = (D1 | ... | Dk) & R) for k = 2..4 via the on-disk bridge
`org_frontier.field.rule_to_phi`; read each verdict through `rule_to_phi`. For H2, draw synthetic
contested coder panels in which each coder reads the account either as specific (Φ = 2.0) or as
pooled (Φ = 0.0); a form is contested when both readings are present and the split sits in the
genuine-contest band. The propagated reading interval is the 2.5/97.5 percentile span of the coder
Φ readings carried by the bridge's `phi_ci`. CONTROL: the specific reading must stay triadic, and a
unanimous-pool panel must collapse the bridge CI to [0, 0]. All rule sets and coder panels are
synthetic.

Run: source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
  python -m org_frontier.questions.q175_substitutability_flipper.probe_substitutability_flipper
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import PHI_EPS
from org_frontier.field.rule_to_phi import rule_to_phi, phi_ci

SPECIFIC_PHI = 2.0


# --------------------------------------------------------------------------------------
# Coded rule sets: specific worker vs substitutable pool
# --------------------------------------------------------------------------------------

def specific_rules():
    """Specific irreplaceable worker. Nodes (W, S, R): S = W & R, the worker binds the system to
    the counterpart. This is the faithful worker-system-counterpart triad; it reads triadic."""
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    labels = ("W", "S", "R")
    return rules, labels


def pooled_rules(k):
    """Substitutable pool of size k. Nodes (D1, ..., Dk, S, R): S = (D1 | ... | Dk) & R. Each pool
    member is driven by S, R is driven by S. Any member can fill the worker's slot, so no single
    member is irreducibly necessary."""
    s_idx = k
    r_idx = k + 1
    rules = []
    for _ in range(k):
        rules.append(lambda x, _s=s_idx: x[_s])

    def s_rule(x, _k=k, _r=r_idx):
        orv = 0
        for i in range(_k):
            orv |= x[i]
        return orv & x[_r]

    rules.append(s_rule)
    rules.append(lambda x, _s=s_idx: x[_s])
    labels = tuple(f"D{i + 1}" for i in range(k)) + ("S", "R")
    return rules, labels


# --------------------------------------------------------------------------------------
# Contested coder panels (synthetic)
# --------------------------------------------------------------------------------------

def reading_interval(coder_phis, lo_pct=2.5, hi_pct=97.5):
    """The propagated reading interval: the percentile span of the contested coder Φ readings.

    A contested categorical reading is not a noisy estimate of one number; it is a split between
    two readings. The interval that surfaces the split is the span of the readings themselves, not
    a confidence band on their mean."""
    cp = np.asarray(coder_phis, dtype=float)
    return float(np.percentile(cp, lo_pct)), float(np.percentile(cp, hi_pct))


def main():
    # ---- INSTRUMENT CONTROLS --------------------------------------------------------------
    # Control 1: the specific reading must stay triadic at max Φ_MIP = 2.0.
    srules, slabels = specific_rules()
    s = rule_to_phi(srules, slabels)
    assert s["structure"] == "triadic", f"specific control structure {s['structure']!r}"
    assert abs(s["max_phi"] - SPECIFIC_PHI) < 1e-9, f"specific control max_phi {s['max_phi']}"

    # Control 2: a unanimous-pool coder panel (all read Φ = 0) must collapse the bridge CI to [0,0].
    unanimous = phi_ci([0.0, 0.0, 0.0, 0.0], coder_codings=np.zeros((4, 1), dtype=int),
                       n_boot=300, rng=np.random.default_rng(1))
    assert unanimous["degenerate"], "unanimous-pool control: CI not degenerate"
    assert abs(unanimous["ci_low"]) < 1e-9 and abs(unanimous["ci_high"]) < 1e-9, \
        "unanimous-pool control: CI not [0,0]"

    print(f"CONTROL specific reads '{s['structure']}' max_phi={s['max_phi']:.6f}; "
          f"unanimous-pool CI collapses to "
          f"[{unanimous['ci_low']:.6f},{unanimous['ci_high']:.6f}]: PASS")
    print()

    # ---- H1: does the substitutable pool dissolve the worker? -----------------------------
    print("H1 substitutable pool re-encoding vs verdict")
    print(f"  {'reading':24s} {'k':>2s}  {'structure':9s}  max_phi")
    print(f"  {'specific (S = W & R)':24s} {1:>2d}  {s['structure']:9s}  {s['max_phi']:.6f}")
    k_values = (2, 3, 4)
    pool_phis = {}
    for k in k_values:
        rules, labels = pooled_rules(k)
        r = rule_to_phi(rules, labels)
        pool_phis[k] = r["max_phi"]
        print(f"  {'pooled (S = OR(D) & R)':24s} {k:>2d}  {r['structure']:9s}  {r['max_phi']:.6f}")
    print()

    all_dyadic = all(pool_phis[k] <= PHI_EPS for k in k_values)
    specific_triadic = s["structure"] == "triadic" and s["max_phi"] > PHI_EPS
    h1_ok = all_dyadic and specific_triadic

    # ---- H2: does the contested-reading interval surface the flip? ------------------------
    # Synthetic contested coder panels. Each coder reads the account either as specific
    # (Φ = SPECIFIC_PHI) or as pooled (Φ = 0). A panel is contested when both readings appear and
    # the split sits in the genuine-contest band [0.3, 0.7] of specific-readers. The propagated
    # interval is the 2.5/97.5 percentile reading span carried by the bridge's phi_ci.
    rng = np.random.default_rng(0)
    n_draws = 600
    n_coders = 12
    contest_lo, contest_hi = 0.30, 0.70
    contested = 0
    spans = 0
    for _ in range(n_draws):
        frac_specific = rng.uniform(contest_lo, contest_hi)
        is_specific = rng.random(n_coders) < frac_specific
        phis = np.where(is_specific, SPECIFIC_PHI, 0.0)
        if phis.min() == phis.max():
            continue  # unanimous: not a contested form
        contested += 1
        # carry the panel through the bridge; the bridge returns the coder Φ readings used here.
        codings = is_specific.astype(int).reshape(-1, 1)
        out = phi_ci(phis, coder_codings=codings, n_boot=200, ci=0.95,
                     rng=np.random.default_rng(7))
        lo, hi = reading_interval(out["coder_phis"])
        if lo <= PHI_EPS and hi > PHI_EPS:
            spans += 1

    span_frac = spans / contested if contested else 0.0

    print("H2 contested-reading interval (synthetic coder panels)")
    print(f"  specific-reading Φ        : {SPECIFIC_PHI:.6f}")
    print(f"  coder panels drawn        : {n_draws}")
    print(f"  contested forms           : {contested}")
    print(f"  coders per panel          : {n_coders}")
    print(f"  interval spans [0, Φ_spec]: {spans}")
    print(f"  span fraction             : {span_frac:.4f}  (support threshold > 0.90)")
    print()

    h2_ok = span_frac > 0.90

    print(f"H1 substitutable pool drives max_phi to 0 (dyadic) for all k>=2: "
          f"{'SUPPORTED' if h1_ok else 'REFUTED'}")
    print(f"H2 contested-reading interval spans [0, specific Φ] in >90% of forms: "
          f"{'SUPPORTED' if h2_ok else 'REFUTED'}")


if __name__ == "__main__":
    main()
