#!/usr/bin/env python
r"""Q7 / H4 — party noise decays Φ faster than mediator noise (asymmetry direction).

H4: the clean-limit slope magnitude |dΦ/dp| at small p is larger for the party (W) site than
the mediator (S) site, and the party curve sits at or below the mediator curve across the
interior.

Form / ensemble (fixed, shared with the rest of Q7): the triadic conjunctive mediated chain at
n=3, labels (W,S,C), clean rules W' = S, S' = W & C, C' = S (#26/#33/#27). Flip-noise of
strength p is output noise on one node column of the state-by-node TPM:
    P(out=1 | row) = (1-p)*col_clean + p*(1-col_clean),
so the output lands on its clean value with reliability 1-p and flips with probability p. The
connectivity matrix is the clean form's cm_from_rules(...), reused for every p. Φ_MIP(p) for a
site is max_phi_float(noisy_tpm(p, cols))[0]. The two sites here:
  - mediator S: cols=(1,)  (the commit S' = W & C)
  - party    W: cols=(0,)  (W' = S)

Grid (fixed before run): p = 0.00, 0.01, ..., 0.50 (51 points, step 0.01), the Q6 grid.

Measure: the clean-limit slope magnitude at each site, evaluated at the first interior grid
point p=0.01 by the forward difference from p=0,
    m_site = |Φ_site(0.01) - Φ_site(0.00)| / 0.01,
and the interior ordering sign — the count of interior p in {0.01, ..., 0.49} where
Φ_W(p) < Φ_S(p).

Controls: instrument control (run first) — the clean form at p=0 must read triadic,
max_phi = 2.0 (to 1e-6), MIP "2 parts: {W,SC}", and max_phi_float(noisy_tpm(0.0, cols)) = 2.0
for both sites; abort if it fails. H4 is read jointly with H1: the slope comparison counts only
if H1 holds (the two curves are genuinely distinct on the same sweep). Self-control: m_S on a
repeat computation is identical (|Δ| <= TOL = 1e-6), a determinism check.

Decision rule (fixed before run): H4 is CONFIRMED if m_W > m_S AND Φ_W(p) <= Φ_S(p) at every
interior p, with strict inequality somewhere (party steeper and at/below across the interior).
H4 is REFUTED if m_W <= m_S (mediator at least as steep) or the ordering reverses at any
interior p (Φ_W(p) > Φ_S(p)). Predicted: Φ_W(0.1)=0.76 < Φ_S(0.1)=1.19, the party curve drops
below immediately and stays below, m_W > m_S.

Run:
  ~/iit-playground/venv-4.0/bin/python \
      org_frontier/questions/q7_party_vs_mediator_noise/probe_slope_asymmetry.py \
      2>&1 | grep -v "Welcome to PyPhi\|pyphi.config"
"""

import csv
import os
import sys

# Repo root onto sys.path so this runs as a direct script and via the package.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from org_frontier.probes.lib import verdict, max_phi_float

# ---------------------------------------------------------------------------
# The form and the noise model (fixed for every Q7 test)
# ---------------------------------------------------------------------------
LABELS = ("W", "S", "C")
RULES = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]  # W'=S, S'=W&C, C'=S
CLEAN_TPM = tpm_from_rules(RULES).astype(float)
CM = cm_from_rules(RULES)

STEP = 0.01
GRID = [round(k * STEP, 2) for k in range(51)]  # 0.00, 0.01, ..., 0.50
TOL = 1e-6

SITE_S = (1,)   # mediator site
SITE_W = (0,)   # party site


def noisy_tpm(p, cols):
    """State-by-node TPM with output flip-noise of strength p on each column in cols."""
    t = CLEAN_TPM.copy()
    for c in cols:
        sc = CLEAN_TPM[:, c]
        t[:, c] = (1.0 - p) * sc + p * (1.0 - sc)
    return t


def sweep(cols):
    """The 51-point Φ_MIP(p) sweep for one injection site."""
    out = []
    for p in GRID:
        ph, _ = max_phi_float(noisy_tpm(p, cols))
        out.append(round(float(ph), 12))
    return out


# ---------------------------------------------------------------------------
# Instrument control (run first)
# ---------------------------------------------------------------------------
def instrument_control():
    """Clean form at p=0 must read triadic, max_phi=2.0 (1e-6), MIP '2 parts: {W,SC}';
    and both sites' p=0 endpoint must reproduce 2.0 via the stochastic-TPM path."""
    v = verdict(RULES, LABELS)
    ok_struct = v.structure == "triadic"
    ok_phi = abs(v.max_phi - 2.0) <= TOL
    ok_mip = "{W,SC}" in v.mip_partition.replace(" ", "")
    phi0_s, _ = max_phi_float(noisy_tpm(0.0, SITE_S))
    phi0_w, _ = max_phi_float(noisy_tpm(0.0, SITE_W))
    ok_s = abs(phi0_s - 2.0) <= TOL
    ok_w = abs(phi0_w - 2.0) <= TOL
    print("INSTRUMENT CONTROL (clean form, p=0):")
    print(f"  verdict.structure   = {v.structure!r}        (need 'triadic')   -> {ok_struct}")
    print(f"  verdict.max_phi     = {v.max_phi:.6f}     (need 2.0 +/-1e-6) -> {ok_phi}")
    print(f"  verdict.mip         = {v.mip_partition!r} -> {ok_mip}")
    print(f"  max_phi_float(S,p=0)= {phi0_s:.6f}     (need 2.0 +/-1e-6) -> {ok_s}")
    print(f"  max_phi_float(W,p=0)= {phi0_w:.6f}     (need 2.0 +/-1e-6) -> {ok_w}")
    if not (ok_struct and ok_phi and ok_mip and ok_s and ok_w):
        print("INSTRUMENT CONTROL FAILED — aborting; swept values are not trusted.")
        sys.exit(1)
    print("  PASS\n")


# ---------------------------------------------------------------------------
# H1 joint read — the two curves must be genuinely distinct on the same sweep
# ---------------------------------------------------------------------------
def h1_holds(phi_s, phi_w):
    """H1: the party and mediator curves separate beyond grid noise. Confirmed if the max
    absolute interior gap g_max = max_p |Φ_W(p) - Φ_S(p)| over p in {0.01..0.49} exceeds 1e-3."""
    s = np.array(phi_s)
    w = np.array(phi_w)
    interior = slice(1, 50)  # indices 1..49 -> p = 0.01..0.49
    gap = np.abs(w[interior] - s[interior])
    k = int(np.argmax(gap))
    g_max = float(gap[k])
    p_at = GRID[1 + k]
    return (g_max > 1e-3), g_max, p_at


def main():
    instrument_control()

    print("Sweeping the mediator curve Phi_S(p) (cols=(1,)) ...")
    phi_s = sweep(SITE_S)
    print("Sweeping the party curve    Phi_W(p) (cols=(0,)) ...")
    phi_w = sweep(SITE_W)

    # H1 joint read.
    h1_ok, g_max, p_gmax = h1_holds(phi_s, phi_w)

    # Clean-limit slope magnitudes (forward difference at the first interior point p=0.01).
    m_s = abs(phi_s[1] - phi_s[0]) / STEP
    m_w = abs(phi_w[1] - phi_w[0]) / STEP

    # Self-control: m_S recomputed on a repeat sweep is identical (determinism).
    phi_s_repeat = sweep(SITE_S)
    m_s_repeat = abs(phi_s_repeat[1] - phi_s_repeat[0]) / STEP
    self_delta = abs(m_s - m_s_repeat)
    self_ok = self_delta <= TOL

    # Interior ordering: p in {0.01..0.49} (indices 1..49).
    interior_idx = list(range(1, 50))
    n_below = sum(1 for k in interior_idx if phi_w[k] < phi_s[k])         # Φ_W < Φ_S
    n_at_or_below = sum(1 for k in interior_idx if phi_w[k] <= phi_s[k] + TOL)
    n_above = sum(1 for k in interior_idx if phi_w[k] > phi_s[k] + TOL)   # ordering reversed
    n_strict_below = sum(1 for k in interior_idx if phi_w[k] < phi_s[k] - TOL)
    first_above = next((GRID[k] for k in interior_idx if phi_w[k] > phi_s[k] + TOL), None)

    party_steeper = m_w > m_s
    at_or_below_all = (n_above == 0)
    strict_somewhere = (n_strict_below > 0)

    # ---- verdict (fixed decision rule) ----
    # CONFIRMED: m_W > m_S AND Φ_W(p) <= Φ_S(p) at every interior p with strict inequality
    #            somewhere. The slope comparison counts only if H1 holds.
    # REFUTED:   m_W <= m_S, or the ordering reverses at any interior p.
    if party_steeper and at_or_below_all and strict_somewhere and h1_ok:
        h4_verdict = "confirmed"
    elif (not party_steeper) or (not at_or_below_all):
        h4_verdict = "refuted"
    else:
        # party steeper and at/below but H1 fails to certify distinctness, or no strict point.
        h4_verdict = "partial"

    # ---- print exact numbers ----
    print("\nPhi_S(p) (mediator) and Phi_W(p) (party) over the grid; gap = Phi_W - Phi_S:")
    print(f"  {'p':>5}  {'Phi_S':>12}  {'Phi_W':>12}  {'gap':>12}  {'W<S':>5}")
    for k, p in enumerate(GRID):
        gap = phi_w[k] - phi_s[k]
        below = "yes" if (k in interior_idx and phi_w[k] < phi_s[k]) else ""
        print(f"  {p:>5.2f}  {phi_s[k]:>12.6f}  {phi_w[k]:>12.6f}  {gap:>12.6f}  {below:>5}")

    print("\nH1 joint read (the two curves must be genuinely distinct):")
    print(f"  g_max = max_p |Phi_W - Phi_S| (interior) = {g_max:.6f} at p={p_gmax:.2f}"
          f"  (need > 1e-3) -> {h1_ok}")

    print("\nClean-limit slope magnitudes (forward diff at p=0.01):")
    print(f"  m_S = |Phi_S(0.01) - Phi_S(0.00)| / 0.01 = "
          f"|{phi_s[1]:.6f} - {phi_s[0]:.6f}| / 0.01 = {m_s:.6f}")
    print(f"  m_W = |Phi_W(0.01) - Phi_W(0.00)| / 0.01 = "
          f"|{phi_w[1]:.6f} - {phi_w[0]:.6f}| / 0.01 = {m_w:.6f}")
    print(f"  party steeper (m_W > m_S)?               = {party_steeper}")

    print("\nSelf-control (determinism of m_S on repeat):")
    print(f"  m_S repeat = {m_s_repeat:.6f}  |delta| = {self_delta:.2e}  (need <= 1e-6) -> {self_ok}")

    print("\nInterior ordering (p in {0.01..0.49}, 49 points):")
    print(f"  count Phi_W < Phi_S        = {n_below} / 49")
    print(f"  count Phi_W <= Phi_S (+TOL)= {n_at_or_below} / 49")
    print(f"  count Phi_W >  Phi_S (rev) = {n_above} / 49"
          + (f"  first reversal at p={first_above:.2f}" if first_above is not None else ""))
    print(f"  count strict Phi_W < Phi_S = {n_strict_below} / 49")
    print(f"  at/below at every interior p? = {at_or_below_all}; strict somewhere? = {strict_somewhere}")

    print(f"\nH4 VERDICT: {h4_verdict.upper()}")
    if h4_verdict == "partial":
        print("  (party steeper and at/below, but H1 distinctness or a strict point is missing)")

    # ---- write CSV ----
    results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
    os.makedirs(results_dir, exist_ok=True)
    csv_path = os.path.join(results_dir, "q7_slope_asymmetry.csv")
    with open(csv_path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["p", "phi_S", "phi_W", "gap_W_minus_S", "W_below_S"])
        for k, p in enumerate(GRID):
            w.writerow([f"{p:.2f}", f"{phi_s[k]:.12f}", f"{phi_w[k]:.12f}",
                        f"{phi_w[k] - phi_s[k]:.12f}",
                        int(k in interior_idx and phi_w[k] < phi_s[k])])
    print(f"\nWrote {csv_path}")

    return h4_verdict


if __name__ == "__main__":
    main()
