"""Probe 352 (Q198) — does baseline (W1) Φ_coord predict the latent ACS-growth slope?

Question: in the simulated algorithmacy panel, does a worker's baseline (W1) Φ_coord predict the
individual latent growth slope of algorithmacy competence (ACS-total) over waves W1-W3?

H1: W1 Φ_coord positively predicts the individual latent ACS-growth slope (β > 0, 95% CI excludes 0):
    workers in more irreducible W1 coordination forms gain competence faster.
    Null: the W1-Φ-to-slope β CI includes 0.
H2: W1 Φ_coord predicts the slope above and beyond the W1 ACS intercept (incremental over baseline
    competence; the partial β for Φ_coord with the W1 intercept controlled has a 95% CI that excludes 0).
    Null: once the W1 ACS intercept is controlled, W1 Φ_coord adds nothing to the slope.

Method: reuse phi_bridge.phi_coord to assign each simulated worker a W1 Φ_coord from the worker's reported
(TI, SA-commit, SU) row mapped to a W-S-C Boolean form (commit -> irreducible, Φ_coord=2.0; convey ->
factorizable, Φ_coord=0.0). Simulate a 3-wave panel where ACS-total has a per-worker intercept (baseline
competence, on the latent factor + noise) and a per-worker linear slope whose mean is lifted by the
worker's W1 Φ_coord plus independent slope noise. Fit a per-worker latent growth curve (intercept + linear
slope) by OLS on the three equally-spaced timepoints. Regress the recovered slope on W1 Φ_coord (H1) and,
in a two-predictor model, on W1 Φ_coord with the W1 ACS intercept controlled (H2). A shuffled-Φ placebo
predictor (W1 Φ_coord permuted across workers) gives a null reference; a forced-dyadic control cohort
(Φ_coord identically 0) gives a second null.

Determinism: one fixed seed (numpy.random.default_rng(0)). Φ_coord depends only on which of two forms a
worker maps to, so the panel sweep reproduces exactly.

Scope: the panel is SIMULATED. No worker is measured. The growth structure and the Φ-to-slope coupling are
built into the synthetic data on purpose; the probe recovers them through the exact-Φ instrument and the
LGC fit. The result is evidence about the bridge and the growth pipeline on synthetic data, not a measured
effect in a real cohort.

Run:  python -m org_frontier.questions.q198_phi_predicts_growth.probe_phi_predicts_growth
"""

import numpy as np

from org_frontier.classifier.classifier import tpm_from_rules
from org_frontier.probes.lib import max_phi_float, verdict
from org_frontier.survey.cohort_algorithmacy.phi_bridge import (
    LABELS, phi_coord, worker_rules,
)

N = 300
WAVES = np.array([0.0, 1.0, 2.0])  # W1, W2, W3 as time codes 0,1,2


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


def ols_with_ci(X, y, alpha=0.05):
    """OLS β with classical normal-theory standard errors and a (1-alpha) CI per coefficient.

    X already includes an intercept column. Returns (beta, se, lo, hi) arrays.
    """
    X = np.asarray(X, float)
    y = np.asarray(y, float)
    n, k = X.shape
    XtX_inv = np.linalg.inv(X.T @ X)
    beta = XtX_inv @ X.T @ y
    resid = y - X @ beta
    dof = n - k
    sigma2 = float(resid @ resid) / dof
    cov = sigma2 * XtX_inv
    se = np.sqrt(np.diag(cov))
    # 0.975 normal quantile (z), used as a t≈z approximation (large dof here, n-k >= 297)
    zcrit = 1.959963984540054
    lo = beta - zcrit * se
    hi = beta + zcrit * se
    return beta, se, lo, hi


def fit_lgc_slopes(acs_panel):
    """Per-worker latent growth curve (intercept + linear slope) by OLS over the three waves.

    acs_panel is (N, 3). Returns (intercepts, slopes), each length N. With equally-spaced time codes
    the OLS fit is closed-form and exact; the intercept is the W1 (time=0) level.
    """
    T = np.column_stack([np.ones_like(WAVES), WAVES])  # (3, 2)
    TtT_inv = np.linalg.inv(T.T @ T)
    coef = (TtT_inv @ T.T @ acs_panel.T)  # (2, N): row0 intercept, row1 slope
    return coef[0], coef[1]


def simulate_panel(n, rng, control=False):
    """A 3-wave simulated panel with a per-worker W1 Φ_coord and a Φ-coupled growth slope.

    The latent coordination factor z drives the W1 reported conditions (TI, SA-commit, SU). Those map to
    a W-S-C form whose Φ_coord is 0 or 2 (0 everywhere under control). ACS-total at each wave is built
    from a per-worker intercept (baseline competence, on z + noise) plus a per-worker slope times the
    time code plus measurement noise. The per-worker slope mean is lifted by the worker's W1 Φ_coord, so
    workers in irreducible W1 forms gain competence faster — the effect under test.
    """
    z = rng.normal(0, 1, n)
    ti = np.clip(np.round(4.0 + 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)
    sa = np.clip(np.round(4.0 + 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)
    su = np.clip(np.round(4.0 - 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)

    phi = np.array([phi_coord(ti[i], sa[i], su[i], control=control) for i in range(n)])

    # Per-worker baseline competence (W1 intercept): loads on the latent z plus independent noise.
    intercept_true = 0.7 * z + rng.normal(0, 0.7, n)
    # Per-worker linear slope: a positive base growth, lifted by W1 Φ_coord, plus slope noise.
    #   slope = base + gain * (phi/2) + noise.  phi is 0 or 2, so phi/2 is a 0/1 commit indicator.
    base_slope = 0.20
    phi_gain = 0.35
    slope_true = base_slope + phi_gain * (phi / 2.0) + rng.normal(0, 0.20, n)

    # Observed ACS-total per wave = intercept + slope*time + measurement noise.
    meas_noise = rng.normal(0, 0.30, (n, len(WAVES)))
    acs_panel = (intercept_true[:, None] + slope_true[:, None] * WAVES[None, :] + meas_noise)

    return {
        "phi": phi,
        "acs_panel": acs_panel,
        "ti": ti, "sa": sa, "su": su,
    }


def main():
    print("=" * 78)
    print("Q198 — does W1 Φ_coord predict the latent ACS-growth slope? (SIMULATED panel)")
    print("=" * 78)

    instrument_control()

    # Show the two W1 forms a worker maps to, so the bridge map is auditable.
    print("\nBridge map — the two W-S-C W1 forms a worker can map to:")
    commit_rules = worker_rules(7, 7, 1, control=False)   # high TI, high SA, low SU -> commit
    convey_rules = worker_rules(7, 7, 7, control=False)   # high SU -> convey (pass-through)
    for name, rules in (("commit S'=W AND C", commit_rules), ("convey S'=W", convey_rules)):
        v = verdict(rules, LABELS)
        mx, _ = max_phi_float(tpm_from_rules(rules))
        print(f"  {name:18s}: {v.structure:8s}  Φ_coord={mx:.6f}")

    rng = np.random.default_rng(0)
    panel = simulate_panel(N, rng, control=False)
    ctrl = simulate_panel(N, np.random.default_rng(0), control=True)

    phi = panel["phi"]
    n_commit = int((phi > 1e-9).sum())
    print(f"\nPanel: N={N}; {n_commit} irreducible (commit) W1 forms, {N - n_commit} factorizable "
          f"(convey) W1 forms.")

    # Per-worker LGC fit.
    icpt, slope = fit_lgc_slopes(panel["acs_panel"])
    icpt_c, slope_c = fit_lgc_slopes(ctrl["acs_panel"])

    # Mean trajectory and mean slope by W1 form, as a sanity check on the recovered LGC.
    mean_traj = panel["acs_panel"].mean(axis=0)
    print(f"Mean ACS-total trajectory: W1 {mean_traj[0]:+.3f} -> W2 {mean_traj[1]:+.3f} -> "
          f"W3 {mean_traj[2]:+.3f}")
    print(f"Mean recovered slope: commit={slope[phi > 1e-9].mean():+.4f}  "
          f"convey={slope[phi < 1e-9].mean():+.4f}")

    # --- H1: regress slope on W1 Φ_coord (single predictor). ---
    X1 = np.column_stack([np.ones(N), phi])
    b1, se1, lo1, hi1 = ols_with_ci(X1, slope)
    beta_phi1, lo_phi1, hi_phi1 = b1[1], lo1[1], hi1[1]

    # Placebo: shuffled Φ_coord (permuted across workers), single predictor.
    perm = rng.permutation(N)
    phi_shuf = phi[perm]
    Xp = np.column_stack([np.ones(N), phi_shuf])
    bp, sep, lop, hip = ols_with_ci(Xp, slope)
    beta_phip, lo_phip, hi_phip = bp[1], lop[1], hip[1]

    # Control cohort: Φ_coord identically 0, so the predictor is constant — report the form's behaviour.
    phi_ctrl_const = bool(np.std(ctrl["phi"]) < 1e-12)

    # --- H2: regress slope on W1 Φ_coord controlling the W1 ACS intercept (incremental). ---
    X2 = np.column_stack([np.ones(N), phi, icpt])
    b2, se2, lo2, hi2 = ols_with_ci(X2, slope)
    beta_phi2, lo_phi2, hi_phi2 = b2[1], lo2[1], hi2[1]
    beta_icpt2 = b2[2]

    print("\n" + "-" * 78)
    print(f"{'model':<34}{'β(W1 Φ_coord)':<16}{'95% CI':<24}")
    print("-" * 78)
    print(f"{'H1: slope ~ Φ':<34}{beta_phi1:<+16.4f}[{lo_phi1:+.4f}, {hi_phi1:+.4f}]")
    print(f"{'    placebo: slope ~ shuffled-Φ':<34}{beta_phip:<+16.4f}[{lo_phip:+.4f}, {hi_phip:+.4f}]")
    print(f"{'H2: slope ~ Φ + W1-intercept':<34}{beta_phi2:<+16.4f}[{lo_phi2:+.4f}, {hi_phi2:+.4f}]")
    print("-" * 78)
    print(f"  H2 covariate β(W1 ACS intercept) = {beta_icpt2:+.4f}")
    print(f"  control cohort (forced-dyadic): Φ_coord constant at 0 across the panel = {phi_ctrl_const} "
          f"(predictor has no variance; β undefined by construction)")

    # --- Verdicts. ---
    # H1: β > 0 and 95% CI excludes 0; placebo CI includes 0.
    h1 = (beta_phi1 > 0.0) and (lo_phi1 > 0.0)
    placebo_null = (lo_phip <= 0.0 <= hi_phip)
    # H2: partial β for Φ_coord (W1 intercept controlled) > 0 and 95% CI excludes 0.
    h2 = (beta_phi2 > 0.0) and (lo_phi2 > 0.0)

    print(f"\n  placebo (shuffled-Φ) CI includes 0: {placebo_null}  "
          f"(expected null reference for a non-predictive Φ)")

    print(f"\nH1 (W1 Φ_coord predicts the ACS-growth slope, β>0 & CI excludes 0): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"   β(Φ)={beta_phi1:+.4f}, 95% CI=[{lo_phi1:+.4f}, {hi_phi1:+.4f}]; "
          f"placebo β={beta_phip:+.4f}, CI=[{lo_phip:+.4f}, {hi_phip:+.4f}]")
    print(f"H2 (W1 Φ_coord predicts the slope above and beyond the W1 ACS intercept, "
          f"CI excludes 0): {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"   partial β(Φ | W1-intercept)={beta_phi2:+.4f}, 95% CI=[{lo_phi2:+.4f}, {hi_phi2:+.4f}]")


if __name__ == "__main__":
    main()
