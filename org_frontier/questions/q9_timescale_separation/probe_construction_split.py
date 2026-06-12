"""Q9 / H3 — hold-for-k and probabilistic-1/k disagree on the verdict.

Both slow-commit constructions are swept on `two_sided_match` over the grid k = 1..6.

(A) Deterministic hold-for-k: `hold_k_tpm(rules, k)` is a deterministic composed map,
    classified by `classify`. Its strict flip ratio k*_det is the smallest k reading dyadic.
(B) Probabilistic 1/k commit: only the S column (node 1) of the synchronous base TPM is
    rescaled per row to (1/k)*commit_val + (1 - 1/k)*cur_S, a stochastic state-by-node TPM
    (the #61 modeling flag). Φ_MIP is read by `max_phi_float`; the verdict is dyadic iff
    Φ_MIP <= PHI_EPS. Its strict flip ratio k*_prob is the smallest such k, or "none in grid".

Decision rule (fixed before the run): CONFIRMED if |k*_prob - k*_det| > 1 grid step, or the
probabilistic verdict holds triadic across the whole grid (k*_prob = none) while the
deterministic verdict flips (k*_det finite). REFUTED if both cross the dyadic boundary within
one grid step (|k*_prob - k*_det| <= 1) — the H0 reading that IIT reads the fast/slow ratio
and not its stochastic dressing.

Run:
    ~/iit-playground/venv-4.0/bin/python \
        org_frontier/questions/q9_timescale_separation/probe_construction_split.py
"""

import csv
import os
import sys

# Repo root on the path so the org_frontier.* and proxy_audit.* packages import when this
# file is run as a direct script.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify, tpm_from_rules, cm_from_rules, PHI_EPS
from org_frontier.corpus.forms_library import FORMS_BY_KEY
from org_frontier.probes.lib import max_phi_float, major_complex

FORM_KEY = "two_sided_match"
LABELS = ("W", "S", "C")
S_IDX = 1
N = 3
GRID = [1, 2, 3, 4, 5, 6]
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


# --------------------------------------------------------------------------------------
# The two slow-commit constructions (verbatim from methods.md)
# --------------------------------------------------------------------------------------

def hold_k_tpm(rules, k, n=N, s_idx=S_IDX):
    """Deterministic hold-for-k composed map (state-by-node TPM, connectivity matrix)."""
    def micro(state, commit_S):
        ns = [int(rules[j](tuple(state))) for j in range(n)]
        if not commit_S:
            ns[s_idx] = state[s_idx]          # S holds its previous value
        return ns
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        state = [(s >> i) & 1 for i in range(n)]
        for step in range(k):
            state = micro(state, commit_S=(step == k - 1))  # commit only on the k-th micro-step
        for j in range(n):
            tpm[s, j] = float(state[j])
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9 for s in range(2 ** n)):
                cm[i, j] = 1
    return tpm, cm


def prob_commit_tpm(rules, k, n=N, s_idx=S_IDX):
    """Probabilistic 1/k commit (stochastic state-by-node TPM, only S column rescaled)."""
    base = tpm_from_rules(rules)              # deterministic synchronous next-state, state-by-node
    t = base.copy()
    for s in range(2 ** n):
        cur_S = (s >> s_idx) & 1
        commit_val = base[s, s_idx]
        t[s, s_idx] = (1.0 / k) * commit_val + (1.0 - 1.0 / k) * cur_S
    return t


# --------------------------------------------------------------------------------------
# Instrument control (run first — abort if it fails)
# --------------------------------------------------------------------------------------

def instrument_control(rules):
    """Both constructions reduce to the synchronous map at k=1: triadic, Φ_MIP = 2.0, MIP {W,SC}.

    Also assert the corpus form itself reads triadic at Φ_MIP=2.0 with major complex {W,S,C}
    (the strict-mediation triad reproducing its known verdict). Returns nothing; raises on
    failure.
    """
    # (1) The corpus form's own synchronous verdict: triadic, Φ_MIP=2.0, MIP {W,SC}.
    v0 = classify(tpm_from_rules(rules), cm_from_rules(rules), labels=LABELS)
    assert v0.structure == "triadic", f"control: {FORM_KEY} not triadic synchronously: {v0.structure}"
    assert abs(v0.max_phi - 2.0) < 1e-6, f"control: {FORM_KEY} Φ_MIP != 2.0: {v0.max_phi}"
    assert "{W,SC}" in v0.mip_partition.replace(" ", ""), \
        f"control: {FORM_KEY} MIP not {{W,SC}}: {v0.mip_partition}"

    # Major complex of the strict-mediation triad reads the full {W,S,C} triad.
    core, phi_mc = major_complex(rules, LABELS)
    assert set(core) == {"W", "S", "C"}, f"control: major complex not full triad: {core}"

    # (2) Deterministic hold-for-k at k=1 reduces to the synchronous map.
    tpm_d, cm_d = hold_k_tpm(rules, 1)
    vd = classify(tpm_d, cm_d, labels=LABELS)
    assert vd.structure == "triadic", f"control: det k=1 not triadic: {vd.structure}"
    assert abs(vd.max_phi - 2.0) < 1e-6, f"control: det k=1 Φ_MIP != 2.0: {vd.max_phi}"
    assert "{W,SC}" in vd.mip_partition.replace(" ", ""), \
        f"control: det k=1 MIP not {{W,SC}}: {vd.mip_partition}"

    # (3) Probabilistic 1/k at k=1 reduces to the synchronous map.
    tpm_p = prob_commit_tpm(rules, 1)
    phi_p1, _ = max_phi_float(tpm_p)
    assert abs(phi_p1 - 2.0) < 1e-6, f"control: prob k=1 Φ_MIP != 2.0: {phi_p1}"
    assert phi_p1 > PHI_EPS, f"control: prob k=1 not triadic: {phi_p1}"

    return v0.max_phi, phi_mc, vd.max_phi, phi_p1


# --------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------

def main():
    rules = FORMS_BY_KEY[FORM_KEY].rules

    print("=" * 78)
    print("Q9 / H3 — hold-for-k vs probabilistic-1/k construction split")
    print(f"form = {FORM_KEY}   grid k = {GRID}   PHI_EPS = {PHI_EPS:g}")
    print("=" * 78)

    # --- Instrument control first; abort if it fails ----------------------------------
    print("\n[instrument control] both constructions reduce to the synchronous map at k=1")
    phi_form, phi_mc, phi_det1, phi_prob1 = instrument_control(rules)
    print(f"  {FORM_KEY} synchronous: triadic, Φ_MIP={phi_form:.6f}, MIP {{W,SC}}")
    print(f"  major complex (strict-mediation triad): full {{W,S,C}}, φ={phi_mc:.6f}")
    print(f"  deterministic hold_k_tpm(k=1): triadic, Φ_MIP={phi_det1:.6f}")
    print(f"  probabilistic prob_commit_tpm(k=1): triadic, Φ_MIP={phi_prob1:.6f}")
    print("  CONTROL PASSED")

    # --- Sweep both constructions over the grid ---------------------------------------
    rows = []
    det_phi = {}
    prob_phi = {}
    print("\n[sweep] k : deterministic (classify) | probabilistic (max_phi_float)")
    for k in GRID:
        tpm_d, cm_d = hold_k_tpm(rules, k)
        vd = classify(tpm_d, cm_d, labels=LABELS)
        det_struct = vd.structure
        det_phi[k] = vd.max_phi

        tpm_p = prob_commit_tpm(rules, k)
        phi_p, _ = max_phi_float(tpm_p)
        prob_phi[k] = phi_p
        prob_struct = "dyadic" if phi_p <= PHI_EPS else "triadic"

        print(f"  k={k}: det Φ_MIP={vd.max_phi:.6f} [{det_struct}]   "
              f"prob Φ_MIP={phi_p:.6f} [{prob_struct}]")
        rows.append({
            "k": k,
            "det_phi_mip": f"{vd.max_phi:.10g}",
            "det_structure": det_struct,
            "det_mip": vd.mip_partition,
            "prob_phi_mip": f"{phi_p:.10g}",
            "prob_structure": prob_struct,
        })

    # --- Strict flip ratios -----------------------------------------------------------
    det_flips = [k for k in GRID if det_phi[k] <= PHI_EPS]
    prob_flips = [k for k in GRID if prob_phi[k] <= PHI_EPS]
    k_det = det_flips[0] if det_flips else None
    k_prob = prob_flips[0] if prob_flips else None

    print("\n[flip ratios]")
    print(f"  k*_det  (deterministic) = {k_det if k_det is not None else 'none in grid'}")
    print(f"  k*_prob (probabilistic) = {k_prob if k_prob is not None else 'none in grid'}")
    print(f"  probabilistic Φ_MIP(k) profile = "
          f"{[round(prob_phi[k], 3) for k in GRID]}")
    print("  #61 modeling flag: probabilistic commit needs the stochastic state-by-node TPM; "
          "deterministic hold-for-k does not.")

    # --- Decision rule (fixed before the run) -----------------------------------------
    if k_det is not None and k_prob is None:
        verdict = "confirmed"
        reason = (f"deterministic flips at k*_det={k_det}; probabilistic holds triadic "
                  f"across the whole grid (k*_prob = none)")
    elif k_det is not None and k_prob is not None:
        gap = abs(k_prob - k_det)
        if gap > 1:
            verdict = "confirmed"
            reason = f"|k*_prob - k*_det| = {gap} > 1 grid step"
        else:
            verdict = "refuted"
            reason = (f"|k*_prob - k*_det| = {gap} <= 1 grid step (both cross within one step; "
                      f"H0 'IIT reads the ratio not its dressing')")
    elif k_det is None and k_prob is None:
        verdict = "refuted"
        reason = "neither construction flips in the grid"
    else:
        verdict = "refuted"
        reason = (f"probabilistic flips (k*_prob={k_prob}) while deterministic does not "
                  f"(k*_det none) — opposite of the predicted direction")

    print("\n[decision]")
    print(f"  VERDICT: {verdict.upper()}")
    print(f"  reason: {reason}")

    # --- Write CSV --------------------------------------------------------------------
    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "construction_split.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"\n  CSV written: {csv_path}")

    return verdict, k_det, k_prob, [prob_phi[k] for k in GRID]


if __name__ == "__main__":
    main()
