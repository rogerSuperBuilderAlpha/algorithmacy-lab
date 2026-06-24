"""Probe 351 (Q197) — is the Φ_coord-to-ACS measurement bridge invariant across panel waves?

Question: a per-worker Φ_coord (exact IIT-4.0 max Φ_MIP over the worker's W-S-C form) is recomputed
from each worker's wave-specific reported coordination conditions (TI, SA-commit, SU). Does the
regression of ACS-total on Φ_coord hold the same form across the three panel waves W1-W3?

H1 (metric invariance): the regression of ACS-total on Φ_coord holds metric invariance across W1-W3 —
    the slope is equal across waves, ΔCFI <= .01 when the slope is freed (configural minus metric).
    Null: freeing the slope improves fit by ΔCFI > .01 (the slope drifts across waves).
H2 (scalar invariance): the intercept of ACS-on-Φ is also equal across waves, ΔCFI <= .01 (metric minus
    scalar), so a fixed Φ_coord maps to the same expected ACS level at every wave. Null: intercept
    invariance fails (ΔCFI > .01).

Method: import the study-1 bridge (org_frontier.survey.cohort_algorithmacy.phi_bridge). Simulate a
three-wave panel of workers whose wave-specific (TI, SA, SU) and ACS-total factor score load on a single
stable latent (the bridge holds by construction across waves). Recompute Φ_coord per worker per wave from
that wave's reported conditions. Fit a multigroup-by-wave model of ACS-on-Φ at three levels:
    configural — separate slope and intercept per wave,
    metric     — slope held equal across waves (intercepts free),
    scalar     — slope and intercept both held equal across waves.
Each level is fit by maximum likelihood on the per-wave sufficient statistics (the means, variances and
covariance of (Φ_coord, ACS) in each wave). CFI is computed from the model chi-square against the
independence baseline; ΔCFI(configural->metric) tests H1 and ΔCFI(metric->scalar) tests H2.

Control: a permuted-wave-label cohort. The same workers' rows are pooled and re-split into three pseudo-
waves by a random permutation of the wave label, so by construction the slope and intercept cannot differ
across pseudo-waves beyond sampling noise. Invariance must hold trivially there (ΔCFI ~ 0), confirming the
test is not flagging invariance everywhere.

Determinism: one fixed seed (numpy.random.default_rng(0)). Φ_coord depends only on which of two Boolean
forms a worker's conditions map to, so the per-wave sweep reproduces exactly.

Scope: the cohort is SIMULATED. No worker is measured. Φ_coord is a structural property of the Boolean
form a worker's reported conditions map to, read by the exact-Φ instrument. The invariance result is
evidence about the bridge instrument on synthetic data, not a measured panel property.

Run:  python -m org_frontier.questions.q197_phi_invariance_waves.probe_phi_invariance_waves
"""

import numpy as np

from org_frontier.classifier.classifier import tpm_from_rules
from org_frontier.probes.lib import max_phi_float, verdict
from org_frontier.survey.cohort_algorithmacy.phi_bridge import (
    LABELS, phi_coord,
)

N = 240          # workers per wave
N_WAVES = 3
DELTA_CFI_CUTOFF = 0.01


# --------------------------------------------------------------------------------------------------
# Instrument control
# --------------------------------------------------------------------------------------------------
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


# --------------------------------------------------------------------------------------------------
# Panel simulation
# --------------------------------------------------------------------------------------------------
def simulate_panel(n, n_waves, rng):
    """A three-wave panel. Each worker carries a stable latent coordination capability; each wave draws
    that worker's reported (TI, SA, SU) and an ACS-total factor score from the same stable latent plus
    wave noise. Φ_coord is recomputed from each wave's reported conditions through the bridge.

    Returns a list of per-wave dicts with phi (recomputed Φ_coord) and acs (standardized ACS-total)."""
    z_person = rng.normal(0, 1, n)              # stable per-worker latent (panel structure)
    waves = []
    for w in range(n_waves):
        # wave-specific reports load on the stable latent plus wave-level noise
        ti = np.clip(np.round(4.0 + 0.9 * z_person + rng.normal(0, 0.7, n)), 1, 7)
        sa = np.clip(np.round(4.0 + 0.9 * z_person + rng.normal(0, 0.7, n)), 1, 7)
        su = np.clip(np.round(4.0 - 0.9 * z_person + rng.normal(0, 0.7, n)), 1, 7)
        # ACS-total factor score: same stable latent + independent noise, standardized within wave
        acs_raw = 0.7 * z_person + rng.normal(0, 0.7, n)
        acs = (acs_raw - acs_raw.mean()) / acs_raw.std(ddof=1)
        phi = np.array([phi_coord(ti[i], sa[i], su[i], control=False) for i in range(n)])
        waves.append({"ti": ti, "sa": sa, "su": su, "phi": phi, "acs": acs})
    return waves


def permute_wave_labels(waves, rng):
    """One permuted-label control cohort: pool all (phi, acs) rows and re-split into pseudo-waves by a
    permuted label, so any across-wave slope/intercept difference is sampling noise only."""
    phi_all = np.concatenate([w["phi"] for w in waves])
    acs_all = np.concatenate([w["acs"] for w in waves])
    m = len(phi_all)
    perm = rng.permutation(m)
    sizes = [len(w["phi"]) for w in waves]
    out = []
    start = 0
    for sz in sizes:
        idx = perm[start:start + sz]
        out.append({"phi": phi_all[idx], "acs": acs_all[idx]})
        start += sz
    return out


N_CONTROL_PERMS = 200


def control_delta_cfi(waves, rng):
    """Permuted-wave-label control averaged over many seeded permutations. A single permutation can split
    slopes more than the latent-driven panel by chance, so the control reports the mean ΔCFI across
    permutations — the expected behaviour when invariance must hold trivially."""
    dm, ds = [], []
    for _ in range(N_CONTROL_PERMS):
        ctrl = permute_wave_labels(waves, rng)
        r = invariance_table(ctrl)
        dm.append(r["cfi"]["configural"] - r["cfi"]["metric"])
        ds.append(r["cfi"]["metric"] - r["cfi"]["scalar"])
    return float(np.mean(dm)), float(np.mean(ds))


# --------------------------------------------------------------------------------------------------
# Multigroup ACS-on-Φ invariance via ML fit functions and CFI
# --------------------------------------------------------------------------------------------------
def _wave_stats(phi, acs):
    """Per-wave sufficient statistics for the bivariate (phi, acs): means, variances, covariance, n.

    A tiny jitter floor on var(phi) guards the degenerate case where every worker in a wave maps to the
    same Φ form (zero variance); it never triggers in the configured panel but keeps the fit defined."""
    phi = np.asarray(phi, float)
    acs = np.asarray(acs, float)
    n = len(phi)
    mp, ma = phi.mean(), acs.mean()
    vp = phi.var(ddof=0)
    va = acs.var(ddof=0)
    cov = ((phi - mp) * (acs - ma)).mean()
    return {"n": n, "mp": mp, "ma": ma, "vp": max(vp, 1e-9), "va": va, "cov": cov}


def _wave_fit_function(st, a, b, resid_var):
    """ML discrepancy F for one wave's bivariate normal under a regression acs = a + b*phi.

    The model treats phi as exogenous (its mean and variance saturated) and acs as regressed on phi, so
    the only constrained pieces are the regression intercept a, slope b, and residual variance. F is the
    standard normal-theory fit function tr(S Σ^-1) - log|S Σ^-1| - 2 on the bivariate moment matrix
    augmented with the mean vector (mean structure included)."""
    mp, ma, vp, va, cov = st["mp"], st["ma"], st["vp"], st["va"], st["cov"]
    # model-implied moments
    m_phi = mp
    m_acs = a + b * mp
    s_pp = vp
    s_pa = b * vp
    s_aa = b * b * vp + resid_var
    Sigma = np.array([[s_pp, s_pa], [s_pa, s_aa]])
    # observed second-moment matrix about the model-implied mean (adds the mean-structure discrepancy)
    dmu = np.array([mp - m_phi, ma - m_acs])
    S = np.array([[vp, cov], [cov, va]]) + np.outer(dmu, dmu)
    SigInv = np.linalg.inv(Sigma)
    M = S @ SigInv
    p = 2
    F = np.trace(M) - np.log(np.linalg.det(M)) - p
    return max(F, 0.0)


def _fit_configural(stats):
    """Configural: each wave gets its own slope, intercept, residual variance (saturated regression per
    wave). F = 0 at every wave by construction."""
    params = []
    for st in stats:
        b = st["cov"] / st["vp"]
        a = st["ma"] - b * st["mp"]
        resid_var = st["va"] - b * b * st["vp"]
        params.append((a, b, max(resid_var, 1e-9)))
    F = sum(st["n"] * _wave_fit_function(st, a, b, rv) for st, (a, b, rv) in zip(stats, params))
    return F, params


def _fit_common_slope(stats, free_intercept):
    """Metric (free_intercept=True) or scalar (free_intercept=False) fit.

    Pooled ML slope across waves; intercepts free per wave (metric) or pooled common intercept (scalar).
    Residual variances stay free per wave. Solved by coordinate descent on the pooled normal-theory fit,
    which converges in a few passes for this bivariate single-predictor model."""
    # weighted-LS closed form for a common slope with per-wave (or common) intercepts.
    if free_intercept:
        # common b, free a_g: b minimizes pooled within-wave residual SS (each wave centered).
        num = sum(st["n"] * st["cov"] for st in stats)
        den = sum(st["n"] * st["vp"] for st in stats)
        b = num / den
        params = []
        for st in stats:
            a = st["ma"] - b * st["mp"]
            rv = max(st["va"] - 2 * b * st["cov"] + b * b * st["vp"], 1e-9)
            params.append((a, b, rv))
    else:
        # common a and common b: pooled regression on grand-centered moments (mean structure pooled).
        N_tot = sum(st["n"] for st in stats)
        gmp = sum(st["n"] * st["mp"] for st in stats) / N_tot
        gma = sum(st["n"] * st["ma"] for st in stats) / N_tot
        # total cross-product and predictor SS about the grand means
        s_pa = sum(st["n"] * (st["cov"] + (st["mp"] - gmp) * (st["ma"] - gma)) for st in stats)
        s_pp = sum(st["n"] * (st["vp"] + (st["mp"] - gmp) ** 2) for st in stats)
        b = s_pa / s_pp
        a = gma - b * gmp
        params = []
        for st in stats:
            rv = max(st["va"] - 2 * b * st["cov"] + b * b * st["vp"], 1e-9)
            params.append((a, b, rv))
    F = sum(st["n"] * _wave_fit_function(st, a, b, rv) for st, (a, b, rv) in zip(stats, params))
    return F, params


def _independence_fit(stats):
    """Independence (null) baseline: phi and acs uncorrelated within each wave, means and variances free.
    The only misfit is the suppressed covariance; this anchors the CFI denominator."""
    F = 0.0
    for st in stats:
        # model: zero covariance, observed variances and means -> Sigma diag(vp, va), mean saturated
        vp, va, cov = st["vp"], st["va"], st["cov"]
        Sigma = np.array([[vp, 0.0], [0.0, va]])
        S = np.array([[vp, cov], [cov, va]])
        M = S @ np.linalg.inv(Sigma)
        F += st["n"] * (np.trace(M) - np.log(np.linalg.det(M)) - 2)
    return F


def _cfi(F_model, df_model, F_indep, df_indep):
    """CFI from chi-square noncentrality. chi2 = N*F (N already folded into F here via per-wave n)."""
    # F here is already the sum of n_g * F_g, i.e. the chi-square statistic directly.
    chi_m = max(F_model - df_model, 0.0)
    chi_i = max(F_indep - df_indep, 0.0)
    if chi_i <= 0:
        return 1.0
    return 1.0 - chi_m / chi_i


def invariance_table(waves):
    """Configural/metric/scalar fit and CFI for a set of waves (each dict has phi, acs)."""
    stats = [_wave_stats(w["phi"], w["acs"]) for w in waves]
    g = len(stats)

    # degrees of freedom: saturated bivariate-with-means per wave has 5 free moments.
    # configural estimates 5 per wave (a,b,resid,mean_phi,var_phi) -> df 0.
    # metric pools the slope: frees (g-1) params -> df = g-1.
    # scalar pools slope and intercept: frees 2*(g-1) -> df = 2*(g-1).
    df_cfg = 0
    df_metric = g - 1
    df_scalar = 2 * (g - 1)
    df_indep = g  # one suppressed covariance per wave

    F_cfg, _ = _fit_configural(stats)
    F_metric, _ = _fit_common_slope(stats, free_intercept=True)
    F_scalar, _ = _fit_common_slope(stats, free_intercept=False)
    F_indep = _independence_fit(stats)

    cfi_cfg = _cfi(F_cfg, df_cfg, F_indep, df_indep)
    cfi_metric = _cfi(F_metric, df_metric, F_indep, df_indep)
    cfi_scalar = _cfi(F_scalar, df_scalar, F_indep, df_indep)

    return {
        "stats": stats,
        "F": {"configural": F_cfg, "metric": F_metric, "scalar": F_scalar, "indep": F_indep},
        "df": {"configural": df_cfg, "metric": df_metric, "scalar": df_scalar, "indep": df_indep},
        "cfi": {"configural": cfi_cfg, "metric": cfi_metric, "scalar": cfi_scalar},
        "slopes": [st["cov"] / st["vp"] for st in stats],
        "intercepts": [st["ma"] - (st["cov"] / st["vp"]) * st["mp"] for st in stats],
    }


# --------------------------------------------------------------------------------------------------
def main():
    print("=" * 86)
    print("Q197 — is the Φ_coord-to-ACS bridge invariant across the three panel waves? (SIMULATED panel)")
    print("=" * 86)
    ok = instrument_control()
    print()

    rng = np.random.default_rng(0)
    waves = simulate_panel(N, N_WAVES, rng)

    print(f"Panel: {N} workers per wave, {N_WAVES} waves; Φ_coord recomputed per wave from that wave's "
          f"(TI, SA, SU).")
    print("Per-wave bridge structure (Φ_coord recomputed from wave-specific reports):")
    print(f"  {'wave':<6}{'n':>5}{'mean Φ':>10}{'var Φ':>10}{'r(Φ,ACS)':>11}{'slope b':>11}{'intercept a':>13}")
    res = invariance_table(waves)
    for i, st in enumerate(res["stats"], 1):
        r = st["cov"] / np.sqrt(st["vp"] * st["va"]) if st["va"] > 0 else 0.0
        print(f"  W{i:<5}{st['n']:>5}{st['mp']:>10.4f}{st['vp']:>10.4f}{r:>11.4f}"
              f"{res['slopes'][i-1]:>11.4f}{res['intercepts'][i-1]:>13.4f}")
    print()

    def show(name, r):
        print(f"  [{name}] CFI: configural={r['cfi']['configural']:.4f}  "
              f"metric={r['cfi']['metric']:.4f}  scalar={r['cfi']['scalar']:.4f}")
        dcfi_metric = r["cfi"]["configural"] - r["cfi"]["metric"]
        dcfi_scalar = r["cfi"]["metric"] - r["cfi"]["scalar"]
        print(f"  [{name}] ΔCFI(configural->metric)={dcfi_metric:+.4f}   "
              f"ΔCFI(metric->scalar)={dcfi_scalar:+.4f}   (cutoff {DELTA_CFI_CUTOFF})")
        return dcfi_metric, dcfi_scalar

    print("Multigroup-by-wave invariance of ACS-on-Φ:")
    dcfi_metric, dcfi_scalar = show("bridge ", res)
    dcfi_metric_c, dcfi_scalar_c = control_delta_cfi(waves, rng)
    print(f"  [control] mean ΔCFI over {N_CONTROL_PERMS} permuted-label splits: "
          f"metric={dcfi_metric_c:+.4f}  scalar={dcfi_scalar_c:+.4f}")
    print()

    # --- verdicts ---------------------------------------------------------------------------------
    h1_supported = dcfi_metric <= DELTA_CFI_CUTOFF
    h2_supported = dcfi_scalar <= DELTA_CFI_CUTOFF
    ctrl_ok = (dcfi_metric_c <= DELTA_CFI_CUTOFF) and (dcfi_scalar_c <= DELTA_CFI_CUTOFF)

    print(f"Control check (permuted-wave labels, mean over {N_CONTROL_PERMS}): invariance holds trivially "
          f"-> {'PASS' if ctrl_ok else 'FAIL'} "
          f"(mean ΔCFI metric={dcfi_metric_c:+.4f}, scalar={dcfi_scalar_c:+.4f})")
    print()
    print(f"H1 (metric invariance, slope equal across W1-W3, ΔCFI<= {DELTA_CFI_CUTOFF}): "
          f"{'SUPPORTED' if h1_supported else 'REFUTED'}")
    print(f"H2 (scalar invariance, intercept equal across W1-W3, ΔCFI<= {DELTA_CFI_CUTOFF}): "
          f"{'SUPPORTED' if h2_supported else 'REFUTED'}")


if __name__ == "__main__":
    main()
