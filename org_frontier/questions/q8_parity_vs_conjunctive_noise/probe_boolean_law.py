"""Q8 / H4 — the parity collapse threshold tracks the Boolean-function law (1-2p)^n.

Hypothesis (H4, the sharpest, most falsifiable Q8 claim): the parity (XOR) hub's collapse
threshold on the normalized curve Phi-hat_parity,n(p) lands on the closed-form Boolean-function
prediction p_pred(n) solving (1-2*p_pred)^n = r_n, to within one grid step (0.01), at both n=3
and n=4.

Form / ensemble (methods.md). Node 0 is the hub S; nodes 1..n-1 are parties that each read S
(party' = S). Parity hub: S' = x[1] XOR x[2] XOR ... XOR x[n-1] (parity_hub(n) from #115). Clean
Phi = 2^(2-n): 0.5 at n=3, 0.25 at n=4, triadic, MIP the all-singletons cut. Flip-noise p is
output noise on the hub column (node 0) of the state-by-node TPM, the Q6/Q7 model:
col -> (1-p)*col_clean + p*(1-col_clean). Party columns stay deterministic. CM is the clean
cm_from_rules(rules), reused for every p. Phi_MIP(p) = max_phi_float(noisy_tpm(rules,p))[0].
The 51-point grid p = 0.00, 0.01, ..., 0.50. Normalized curve Phi-hat_parity,n(p) =
Phi_parity,n(p) / Phi_parity,n(0).

Measure (per n in {3,4}).
  (a) Measured collapse p_par* = strict verdict-flip p_v(parity,n): the smallest grid p at which
      the normalized curve drops below the resolution floor r_n = PHI_EPS / Phi_parity,n(0)
      (equivalently Phi_MIP <= PHI_EPS, the strict dyadic reading).
  (b) Closed-form prediction p_pred(n) solving (1-2*p_pred)^n = r_n, i.e.
      p_pred(n) = (1 - r_n**(1/n)) / 2.
  Contrast |p_par* - p_pred(n)| vs grid spacing 0.01.
  Weaker corroborant (recorded, not decisive): max_p |Phi-hat_parity,n(p) - (1-2p)^n| over the
  interior grid points.

Controls.
  Instrument control (run first, abort on failure): the strict-mediation conjunctive triad reads
  triadic at Phi=2.0 (single_hub(3), the #116/Q6/Q7 reference). Also the parity p=0 endpoints
  reproduce 0.5 and 0.25 triadic, and Phi-hat(0)=1=(1-2*0)^n so closed form and measured curve
  share the start.
  Positive control: feed the analytic (1-2p)^n sampled on the grid against itself through the
  residual machinery -> max residual must read exactly 0.

Decision rule (fixed before run). H4 CONFIRMED if at BOTH n=3 and n=4
|p_par* - p_pred(n)| <= 0.01. H4 REFUTED if > 0.01 at either size.

Run:  ~/iit-playground/venv-4.0/bin/python \
        org_frontier/questions/q8_parity_vs_conjunctive_noise/probe_boolean_law.py
"""

import csv
import os
import sys

# Repo root on sys.path so org_frontier.* and proxy_audit.* import when run as a direct script.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi

from org_frontier.classifier.classifier import (
    PHI_EPS,
    classify,
    cm_from_rules,
    tpm_from_rules,
)
from org_frontier.probes.lib import max_phi_float, verdict
from org_frontier.probes.probe_parity_scaling import parity_hub
from org_frontier.probes.probe_distributed_mediators import single_hub

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

_RESULTS = os.path.join(os.path.dirname(__file__), "results")

# The fixed 51-point grid p = 0.00, 0.01, ..., 0.50.
GRID = [round(k * 0.01, 2) for k in range(51)]
GRID_STEP = 0.01


def noisy_tpm(rules, p, n):
    """State-by-node TPM with flip-noise p on the hub column (node 0).

    The clean hub column col_clean in {0,1} per row becomes (1-p)*col_clean + p*(1-col_clean).
    Party columns stay deterministic at their clean values.
    """
    t = tpm_from_rules(rules, n=n).copy()
    sc = t[:, 0]
    t[:, 0] = (1.0 - p) * sc + p * (1.0 - sc)
    return t


def instrument_control():
    """The strict-mediation conjunctive triad must read triadic at Phi=2.0 (single_hub(3)).

    Also confirm the parity p=0 endpoints reproduce 0.5 (n=3) and 0.25 (n=4), triadic, so the
    normalized curve starts at Phi-hat(0)=1 = (1-2*0)^n.
    """
    labels3 = tuple(f"n{i}" for i in range(3))
    vc = verdict(single_hub(3), labels3)
    ok_struct = vc.structure == "triadic"
    ok_phi = abs(vc.max_phi - 2.0) <= 1e-6
    print("INSTRUMENT CONTROL")
    print(f"  conjunctive triad single_hub(3): structure={vc.structure}  "
          f"max_phi={vc.max_phi:.6f}  (require triadic, Phi=2.0)")

    parity_clean = {}
    ok_parity = True
    for n, want in ((3, 0.5), (4, 0.25)):
        rules = parity_hub(n)
        phi0, _ = max_phi_float(noisy_tpm(rules, 0.0, n))
        parity_clean[n] = phi0
        v0 = classify(noisy_tpm(rules, 0.0, n), cm_from_rules(rules, n=n),
                      labels=tuple(f"n{i}" for i in range(n)), eps=PHI_EPS)
        good = abs(phi0 - want) <= 1e-6 and v0.structure == "triadic"
        ok_parity = ok_parity and good
        print(f"  parity p=0, n={n}: Phi(0)={phi0:.6f}  structure={v0.structure}  "
              f"(require {want}, triadic)  Phi-hat(0)={phi0/phi0:.3f}")
    passed = ok_struct and ok_phi and ok_parity
    print(f"  control passed: {passed}")
    print("=" * 72)
    if not passed:
        sys.exit("ABORT: instrument control failed; swept values not trusted.")
    return parity_clean


def boolean_curve(p, n):
    """The analytic Boolean-function law (1-2p)^n at noise p, size n."""
    return (1.0 - 2.0 * p) ** n


def positive_control_residual():
    """Feed (1-2p)^n against itself through the residual statistic -> must be exactly 0."""
    out = {}
    for n in (3, 4):
        analytic = [boolean_curve(p, n) for p in GRID]
        interior = [(p, a) for p, a in zip(GRID, analytic) if 0.0 < p < 0.5]
        resid = max(abs(a - boolean_curve(p, n)) for p, a in interior)
        out[n] = resid
    return out


def sweep_parity(n, phi0):
    """Compute Phi_parity,n(p), Phi-hat, verdict over the grid. Returns rows + lookup dicts."""
    rules = parity_hub(n)
    cm = cm_from_rules(rules, n=n)
    labels = tuple(f"n{i}" for i in range(n))
    rows = []
    phihat = {}
    structure = {}
    for p in GRID:
        tpm = noisy_tpm(rules, p, n)
        phi, _ = max_phi_float(tpm)
        v = classify(tpm, cm, labels=labels, eps=PHI_EPS)
        hat = phi / phi0
        phihat[p] = hat
        structure[p] = v.structure
        rows.append({
            "n": n,
            "p": p,
            "phi": round(phi, 6),
            "phi_hat": round(hat, 6),
            "structure": v.structure,
            "boolean_law": round(boolean_curve(p, n), 6),
            "residual": round(abs(hat - boolean_curve(p, n)), 6),
        })
    return rows, phihat, structure


def main():
    parity_clean = instrument_control()
    pos_ctrl = positive_control_residual()
    print("POSITIVE CONTROL (analytic (1-2p)^n vs itself, interior residual)")
    for n in (3, 4):
        print(f"  n={n}: max residual = {pos_ctrl[n]:.6e}  (require 0)")
    if any(pos_ctrl[n] != 0.0 for n in (3, 4)):
        sys.exit("ABORT: positive control residual nonzero; residual statistic miscalibrated.")
    print("=" * 72)

    all_rows = []
    per_n = {}
    for n in (3, 4):
        phi0 = parity_clean[n]
        rows, phihat, structure = sweep_parity(n, phi0)
        all_rows.extend(rows)

        r_n = PHI_EPS / phi0  # resolution floor on the normalized curve

        # (a) measured collapse p_par* = strict verdict-flip: smallest grid p with Phi-hat < r_n
        # (equivalently structure dyadic, Phi_MIP <= PHI_EPS).
        collapse_ps = [p for p in GRID if phihat[p] < r_n]
        p_par_star = min(collapse_ps) if collapse_ps else None
        # cross-check against the strict dyadic verdict
        dyadic_ps = [p for p in GRID if structure[p] == "dyadic"]
        p_v = min(dyadic_ps) if dyadic_ps else None

        # (b) closed-form prediction p_pred(n) solving (1-2*p_pred)^n = r_n
        p_pred = (1.0 - r_n ** (1.0 / n)) / 2.0

        # weaker corroborant: max interior residual |Phi-hat - (1-2p)^n|
        interior = [p for p in GRID if 0.0 < p < 0.5]
        max_resid = max(abs(phihat[p] - boolean_curve(p, n)) for p in interior)
        argmax_resid = max(interior, key=lambda p: abs(phihat[p] - boolean_curve(p, n)))

        diff = abs(p_par_star - p_pred) if p_par_star is not None else float("inf")
        within = diff <= GRID_STEP

        per_n[n] = {
            "phi0": phi0,
            "r_n": r_n,
            "p_par_star": p_par_star,
            "p_v": p_v,
            "p_pred": p_pred,
            "diff": diff,
            "within": within,
            "max_resid": max_resid,
            "argmax_resid": argmax_resid,
        }

    print("Q8 / H4 — measured parity collapse vs (1-2p)^n prediction")
    print("=" * 72)
    for n in (3, 4):
        d = per_n[n]
        print(f"  n={n}:")
        print(f"    Phi_parity,n(0) = {d['phi0']:.6f}   r_n = PHI_EPS/Phi(0) = {d['r_n']:.6e}")
        print(f"    measured collapse p_par* (Phi-hat < r_n) = {d['p_par_star']}")
        print(f"    strict verdict-flip p_v (dyadic)         = {d['p_v']}")
        print(f"    closed-form p_pred ((1-2p)^n = r_n)      = {d['p_pred']:.6f}")
        print(f"    |p_par* - p_pred|                        = {d['diff']:.6f}   "
              f"(grid step {GRID_STEP})")
        print(f"    within one grid step (<= 0.01)           = {d['within']}")
        print(f"    weaker corroborant max_p|Phi-hat - (1-2p)^n| = {d['max_resid']:.6f} "
              f"at p={d['argmax_resid']}")
    print("=" * 72)

    # also surface the n-independence note + the boolean-law n-dependence at sample points
    print("  Trial-note check (parity normalized curve at sample p, both n):")
    pts = [0.05, 0.10, 0.20]
    rowmap = {(r["n"], r["p"]): r for r in all_rows}
    for p in pts:
        h3 = rowmap[(3, p)]["phi_hat"]
        h4 = rowmap[(4, p)]["phi_hat"]
        b3 = boolean_curve(p, 3)
        b4 = boolean_curve(p, 4)
        print(f"    p={p:.2f}: Phi-hat(n3)={h3:.3f}  Phi-hat(n4)={h4:.3f}  | "
              f"(1-2p)^3={b3:.3f}  (1-2p)^4={b4:.3f}")
    print("=" * 72)

    os.makedirs(_RESULTS, exist_ok=True)
    csv_path = os.path.join(_RESULTS, "q8_boolean_law.csv")
    with open(csv_path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(all_rows[0].keys()))
        w.writeheader()
        w.writerows(all_rows)

    # Decision rule (fixed before run): CONFIRMED iff within one grid step at BOTH n.
    within_both = per_n[3]["within"] and per_n[4]["within"]
    verdict_str = "CONFIRMED" if within_both else "REFUTED"

    print("RESULT")
    print(f"  n=3: |p_par* - p_pred| = {per_n[3]['diff']:.6f}  -> within 0.01: {per_n[3]['within']}")
    print(f"  n=4: |p_par* - p_pred| = {per_n[4]['diff']:.6f}  -> within 0.01: {per_n[4]['within']}")
    print("=" * 72)
    print(f"  H4 VERDICT: {verdict_str}")
    print(f"  CSV: {csv_path}")
    return verdict_str, per_n


if __name__ == "__main__":
    main()
