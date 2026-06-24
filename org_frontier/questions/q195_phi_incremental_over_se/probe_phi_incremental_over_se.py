"""Probe 349 (Q195) — discriminant validity: does Φ_coord carry incremental association with ACS
beyond general self-efficacy (SE) and belonging (BE)?

Question: on the simulated algorithmacy cohort, does the per-worker Φ_coord (exact IIT-4.0 max Φ_MIP
over the worker's W-S-C coordination form, built by the study-1 bridge module) predict ACS-total once
generic competence (self-efficacy) and belonging are partialled out, and does Φ track the algorithmacy
factor more tightly than the self-efficacy factor?

H1: Φ_coord predicts ACS-total controlling for SE and belonging (BE): partial r > 0.15 with a 95% CI
    that excludes 0. Null: the partial-r CI includes 0 once SE and BE are partialled out.
H2: Φ_coord's correlation with the ACS factor exceeds its correlation with the SE factor: the
    bootstrap CI on Δ = r(Φ, ACS) - r(Φ, SE) excludes 0, so Φ tracks algorithmacy specifically, not
    generic competence. Null: r(Φ, ACS) and r(Φ, SE) are equal (Δ CI includes 0).

Method: import the study-1 bridge module org_frontier/survey/cohort_algorithmacy/phi_bridge.py.
Simulate a richer cohort (simulate_cohort_full) whose ACS-total loads on the coordination latent that
also drives Φ_coord and on a generic-competence latent g; SE loads on g (and only lightly on the
coordination latent); BE loads on its own latent plus a light competence tie. Hierarchical regression
of ACS-total on SE + BE (nuisance block) then Φ_coord: report the partial correlation of Φ_coord with
ACS-total controlling for SE and BE (H1). Compare r(Φ, ACS) against r(Φ, SE) with a bootstrap CI on the
dependent-overlapping difference (H2).

Determinism: one fixed seed (numpy.random.default_rng(0)) for the cohort; a fixed bootstrap seed (0).
Φ_coord depends only on which of two W-S-C forms a worker maps to, so the sweep reproduces exactly.

Scope: the cohort is SIMULATED. No worker is measured. Φ_coord is a structural property of the Boolean
form a worker's reported conditions map to, read by the exact-Φ instrument. The discriminant-validity
result is evidence about the bridge on synthetic data, not a measured effect in a real cohort.

Run:  python -m org_frontier.questions.q195_phi_incremental_over_se.probe_phi_incremental_over_se
"""

import numpy as np

from org_frontier.classifier.classifier import tpm_from_rules
from org_frontier.probes.lib import max_phi_float, verdict
from org_frontier.survey.cohort_algorithmacy.phi_bridge import (
    LABELS, simulate_cohort_full, partial_corr, steiger_diff, pearson_ci,
)

N = 400
PARTIAL_THRESH = 0.15


def instrument_control():
    """Validate the Φ instrument on the canonical faithful mediated triad."""
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    tpm = tpm_from_rules(triad)
    mx, _ = max_phi_float(tpm)
    v = verdict(triad, LABELS)
    ok = (v.structure == "triadic") and (abs(mx - 2.0) < 1e-9)
    print(f"CONTROL faithful triad [x1, x0&x2, x1]: verdict={v.structure}, max_phi={mx:.6f} "
          f"-> {'PASS' if ok else 'FAIL'}")
    assert ok, "instrument control failed"
    return ok


def main():
    print("=" * 78)
    print("Q195 — Φ_coord incremental over self-efficacy and belonging (SIMULATED cohort)")
    print("=" * 78)

    instrument_control()

    rng = np.random.default_rng(0)
    coh = simulate_cohort_full(N, rng)
    phi = coh["phi_bridge"]
    acs = coh["acs_total"]
    se = coh["se"]
    be = coh["be"]

    n_commit = int((phi > 1e-9).sum())
    print(f"\nCohort: N={N}; {n_commit} irreducible (commit) forms, {N - n_commit} factorizable "
          f"(convey) forms; Φ_coord in [{phi.min():.2f}, {phi.max():.2f}].")

    # Zero-order correlations among the constructs (auditable nuisance structure).
    r_phi_acs = pearson_ci(phi, acs)[0]
    r_phi_se = pearson_ci(phi, se)[0]
    r_phi_be = pearson_ci(phi, be)[0]
    r_se_acs = pearson_ci(se, acs)[0]
    r_be_acs = pearson_ci(be, acs)[0]

    print("\nZero-order correlations (Pearson r):")
    print(f"  r(Φ_coord, ACS) = {r_phi_acs:+.4f}   r(Φ_coord, SE) = {r_phi_se:+.4f}   "
          f"r(Φ_coord, BE) = {r_phi_be:+.4f}")
    print(f"  r(SE, ACS)      = {r_se_acs:+.4f}   r(BE, ACS)      = {r_be_acs:+.4f}   "
          f"(SE is generic competence: correlated with ACS)")

    # Hierarchical regression: block 1 = SE + BE (nuisance), block 2 adds Φ_coord.
    covars = np.column_stack([se, be])

    def r2(y, X):
        D = np.column_stack([np.ones(len(y)), X])
        beta, *_ = np.linalg.lstsq(D, y, rcond=None)
        resid = y - D @ beta
        ss_res = float((resid ** 2).sum())
        ss_tot = float(((y - y.mean()) ** 2).sum())
        return 1.0 - ss_res / ss_tot

    r2_block1 = r2(acs, covars)
    r2_block2 = r2(acs, np.column_stack([covars, phi]))
    dr2 = r2_block2 - r2_block1

    # H1: partial correlation of Φ_coord with ACS controlling SE and BE.
    pr, pr_lo, pr_hi = partial_corr(phi, acs, covars)

    print("\n" + "-" * 78)
    print("Hierarchical regression of ACS-total:")
    print(f"  block 1  SE + BE            : R^2 = {r2_block1:.4f}")
    print(f"  block 2  SE + BE + Φ_coord  : R^2 = {r2_block2:.4f}   ΔR^2 = {dr2:+.4f}")
    print(f"  partial r(Φ_coord, ACS | SE, BE) = {pr:+.4f}   95% CI [{pr_lo:+.4f}, {pr_hi:+.4f}]")
    print("-" * 78)

    # H2: Φ-ACS vs Φ-SE latent correlation difference, bootstrap CI on the dependent difference.
    delta, d_lo, d_hi, r_xacs, r_xse = steiger_diff(phi, acs, se, n_boot=5000, seed=0)
    print("\nDiscriminant test  Δ = r(Φ, ACS) - r(Φ, SE)  (bootstrap, 5000 resamples, seed 0):")
    print(f"  r(Φ, ACS) = {r_xacs:+.4f}   r(Φ, SE) = {r_xse:+.4f}   "
          f"Δ = {delta:+.4f}   95% CI [{d_lo:+.4f}, {d_hi:+.4f}]")

    # Verdicts.
    h1 = (pr > PARTIAL_THRESH) and (pr_lo > 0.0)
    h2 = (d_lo > 0.0)

    print("\n" + "=" * 78)
    print(f"H1 (partial r(Φ,ACS|SE,BE) > {PARTIAL_THRESH} & CI excludes 0): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"   partial r = {pr:+.4f}, CI = [{pr_lo:+.4f}, {pr_hi:+.4f}]; ΔR^2 = {dr2:+.4f}")
    print(f"H2 (r(Φ,ACS) > r(Φ,SE), Δ CI excludes 0): "
          f"{'SUPPORTED' if h2 else 'NOT SUPPORTED'}")
    print(f"   Δ = {delta:+.4f}, CI = [{d_lo:+.4f}, {d_hi:+.4f}]")
    print("=" * 78)


if __name__ == "__main__":
    main()
