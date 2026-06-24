"""q194 — Does Φ_coord predict the three ACS facets differentially, per the facet-to-structure map?

QUESTION
    The survey arm scores algorithmacy on three facets: counterpart inference (ACS-CI), signal
    compression (ACS-SC), and rule-change tracking (ACS-RT). The cognition arm's survey_bridge map
    ties counterpart inference to a hidden counterpart behind a committing third party. The question
    is whether an exact-Φ coordination measure predicts the facets differentially, with a partition-
    restricted (worker-counterpart) component carrying ACS-CI above and beyond whole-system Φ.

H1 (fixed before computing)
    Φ_coord predicts counterpart-inference (ACS-CI) more strongly than it predicts a non-targeted
    covariate. The CI slope on Φ exceeds the self-efficacy (SE) slope, and the difference in the
    Φ-to-construct correlation (ACS-CI vs SE) excludes 0.
    Null: Φ_coord predicts CI no better than it predicts self-efficacy.

H2 (fixed before computing)
    A Φ component restricted to the W-C (counterpart) partition predicts ACS-CI above and beyond
    whole-system Φ_coord. The incremental ΔR² exceeds 0 and its bootstrap CI excludes 0.
    Null: the partition-restricted Φ adds no variance over whole-system Φ.

METHOD
    Reuse the simulated cohort machinery and the q194 facet cohort in the shared bridge module
    (survey/cohort_algorithmacy/phi_bridge.py). Each worker's reported coordination row maps to a
    W-S-C Boolean form. The exact IIT-4.0 instrument reads two numbers per form: whole-system Φ
    (max Φ_MIP over reachable states) and a W-C-restricted component Φ_WC (max over states of the
    least-informative W-C-separating cut, the partition-restricted analogue of the MIP). The three
    ACS facets and the discriminant covariate SE are generated to the survey_bridge facet map.

    H1: standardized slopes of ACS-CI and SE on Φ_whole, plus a bootstrap CI on the difference of
        the Φ-to-construct correlations (steiger_diff).
    H2: nested OLS of ACS-CI on Φ_whole alone vs Φ_whole + Φ_WC; the incremental ΔR² with a
        bootstrap CI.

    Scope: the cohort is SIMULATED. No worker is measured. Results characterize the instrument and
    the bridge on synthetic data built to the survey_bridge map; they are not field evidence.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q194_phi_facet_specificity.probe_phi_facet_specificity \
      | tee org_frontier/questions/q194_phi_facet_specificity/results/output.txt
"""

import numpy as np

from org_frontier.probes.lib import verdict
from org_frontier.survey.cohort_algorithmacy import phi_bridge as pb

SEED = 0
N = 300
N_BOOT = 5000


def _r2(cols, y):
    """OLS R^2 of y on an intercept plus the given predictor columns."""
    X = np.column_stack([np.ones(len(y))] + list(cols))
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    tot = ((y - y.mean()) ** 2).sum()
    return 1.0 - float(resid @ resid) / float(tot)


def _std_slope(x, y):
    """Standardized OLS slope of y on x (both z-scored), with x already z-scored."""
    X = np.column_stack([np.ones(len(y)), x])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    return float(beta[1])


def _incremental_r2_ci(phi_whole, phi_wc, y, n_boot, seed):
    """Bootstrap percentile CI for the incremental R^2 of phi_wc over phi_whole on y."""
    base = _r2([phi_whole], y)
    full = _r2([phi_whole, phi_wc], y)
    delta = full - base
    rng = np.random.default_rng(seed)
    n = len(y)
    deltas = np.empty(n_boot)
    for k in range(n_boot):
        idx = rng.integers(0, n, n)
        pw, pwc, yy = phi_whole[idx], phi_wc[idx], y[idx]
        deltas[k] = _r2([pw, pwc], yy) - _r2([pw], yy)
    lo = float(np.quantile(deltas, 0.025))
    hi = float(np.quantile(deltas, 0.975))
    return delta, lo, hi, base, full


def main():
    # ---- INSTRUMENT CONTROL ------------------------------------------------------------------
    # The faithful mediated triad reads 'triadic' with max Φ_MIP 2.0, and the W-C-restricted
    # component of that triad is exactly 1.0 (the counterpart relation carries half the global Φ).
    control_rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = verdict(control_rules, ("W", "S", "C"))
    phi_whole_c, phi_wc_c = pb.phi_whole_and_wc(control_rules)
    assert v.structure == "triadic", v.structure
    assert abs(v.max_phi - 2.0) < 1e-9, v.max_phi
    assert abs(phi_whole_c - 2.0) < 1e-9, phi_whole_c
    assert abs(phi_wc_c - 1.0) < 1e-9, phi_wc_c
    print(f"CONTROL faithful triad: verdict '{v.structure}', max Φ_MIP {v.max_phi:.1f}, "
          f"W-C component {phi_wc_c:.1f} ... PASS")
    print()

    # ---- form table --------------------------------------------------------------------------
    print("Coordination forms (exact Φ readings, deterministic):")
    print(f"  {'commit':>6} {'coupled':>7}   {'Φ_whole':>8} {'Φ_WC':>6}")
    for commit in (0, 1):
        for coupled in (0, 1):
            pw, pwc = pb.phi_whole_and_wc(pb.coordination_form(bool(commit), bool(coupled)))
            print(f"  {commit:>6} {coupled:>7}   {pw:>8.4f} {pwc:>6.4f}")
    print()

    # ---- simulated facet cohort --------------------------------------------------------------
    rng = np.random.default_rng(SEED)
    c = pb.simulate_facet_cohort(N, rng)
    phi_whole = c["phi_whole"]
    phi_wc = c["phi_wc"]
    phi_whole_z = (phi_whole - phi_whole.mean()) / phi_whole.std(ddof=1)

    print(f"SIMULATED facet cohort (n={N}, seed={SEED}):")
    print(f"  commit rate {c['commit'].mean():.3f}, coupled rate {c['coupled'].mean():.3f}")
    print(f"  corr(Φ_whole, Φ_WC) = {np.corrcoef(phi_whole, phi_wc)[0, 1]:+.3f}")
    print()

    # ---- facet-by-Φ correlations (the differential pattern) ----------------------------------
    print("Φ-to-facet correlations (whole-system Φ and the W-C component):")
    print(f"  {'construct':>10} {'r(Φ_whole)':>11} {'r(Φ_WC)':>9}")
    for name, y in (("ACS-CI", c["acs_ci"]), ("ACS-SC", c["acs_sc"]),
                    ("ACS-RT", c["acs_rt"]), ("SE", c["se"])):
        r_w, *_ = pb.pearson_ci(phi_whole, y)
        r_wc, *_ = pb.pearson_ci(phi_wc, y)
        print(f"  {name:>10} {r_w:>+11.3f} {r_wc:>+9.3f}")
    print()

    # ---- H1: CI slope on Φ exceeds the SE slope; correlation difference excludes 0 ------------
    slope_ci = _std_slope(phi_whole_z, c["acs_ci"])
    slope_se = _std_slope(phi_whole_z, c["se"])
    delta_r, dlo, dhi, r_ci, r_se = pb.steiger_diff(
        phi_whole, c["acs_ci"], c["se"], n_boot=N_BOOT, seed=SEED)
    print("H1 — Φ predicts ACS-CI more than the discriminant covariate (SE):")
    print(f"  standardized slope ACS-CI on Φ_whole = {slope_ci:+.3f}")
    print(f"  standardized slope SE     on Φ_whole = {slope_se:+.3f}")
    print(f"  Δr [r(Φ,CI) - r(Φ,SE)] = {delta_r:+.3f}  95% CI [{dlo:+.3f}, {dhi:+.3f}]")
    h1 = (slope_ci > slope_se) and (dlo > 0.0)
    print()

    # ---- H2: W-C component adds variance over whole-system Φ for ACS-CI -----------------------
    delta_r2, r2lo, r2hi, base_r2, full_r2 = _incremental_r2_ci(
        phi_whole, phi_wc, c["acs_ci"], n_boot=N_BOOT, seed=SEED)
    print("H2 — W-C-restricted Φ adds variance over whole-system Φ for ACS-CI:")
    print(f"  R^2 (Φ_whole only)      = {base_r2:.4f}")
    print(f"  R^2 (Φ_whole + Φ_WC)    = {full_r2:.4f}")
    print(f"  incremental ΔR^2        = {delta_r2:+.4f}  95% CI [{r2lo:+.4f}, {r2hi:+.4f}]")
    h2 = (delta_r2 > 0.0) and (r2lo > 0.0)
    print()

    # ---- verdicts ----------------------------------------------------------------------------
    print(f"H1 (Φ predicts CI more than SE; Δr CI excludes 0): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"H2 (W-C component adds ΔR^2 over whole-system Φ; CI excludes 0): "
          f"{'SUPPORTED' if h2 else 'NOT SUPPORTED'}")


if __name__ == "__main__":
    main()
