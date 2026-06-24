"""Probe 356 (Q202) — does the Φ-bridge survive its own pre-registered falsification battery?

Question: the survey arm's bridge maps each simulated worker's coordination row to a W-S-C
Boolean form and reads a per-worker Φ_coord with the exact IIT-4.0 instrument. Studies 1-9 of
the line report Φ_coord-to-ACS relations on the simulated cohorts. Two cheap-explanation
threats remain. First, the relation could be a labelling artifact: any per-worker scalar paired
with ACS by the same index would correlate. Second, a cheap non-Φ structural proxy of the same
forms (their connectivity-matrix edge density) could carry the whole relation, so the exact-Φ
content would add nothing. The battery confronts both.

H1: a randomization test that shuffles the worker-to-form mapping destroys every Φ_coord-to-ACS
    relation. The real correlation falls outside the shuffled null at p < .05 (two-sided), and
    the shuffled effects center on 0. Null: the real effect lies inside the shuffled null (the
    bridge is an index artifact).
H2: Φ_coord predicts ACS incrementally over a cheap node-count/edge-density structural proxy of
    the same forms (ΔR^2 > 0, bootstrap CI excludes 0), so irreducibility carries variance the
    cheap proxy misses. Null: the cheap proxy fully subsumes Φ_coord (incremental ΔR^2 CI
    includes 0).

Method: import the study-1 bridge module phi_bridge. The battery runs on two cohorts the bridge
already builds. The whole-system cohort (simulate_cohort) maps every worker to one of two forms
(commit AND, convey pass-through). The facet cohort (simulate_facet_cohort) maps workers to four
forms whose Φ_whole and edge density rank them differently: the counterpart-coupled form has the
highest edge density yet lower Φ than the mediated form, so the two measures decouple. For each
cohort: (1) the worker-form-shuffle permutation null — permute the per-worker Φ_coord vector
against fixed ACS (1000 shuffles, seed 0) and locate the real r in the null (H1); (2) the
incremental-validity test — edge density of each worker's form's connectivity matrix as a
competing predictor, hierarchical regression ACS ~ proxy then ACS ~ proxy + Φ_coord, with a
nonparametric bootstrap CI on ΔR^2 (2000 resamples, seed 0) (H2). The proxy is the cheap
structural reading: edges / n^2 of cm_from_rules for the worker's form, no Φ.

Determinism: one fixed cohort seed (numpy.random.default_rng(0)); fixed permutation seed (0) and
bootstrap seed (0). Φ_coord depends only on which form a worker maps to, so the sweep reproduces
exactly.

Scope: both cohorts are SIMULATED. No worker is measured. The association is built into the
synthetic data by construction; the battery tests whether the bridge's reported relation is a
labelling artifact and whether exact Φ adds over a cheap proxy on that synthetic data. The
verdicts are evidence about the instrument and the proxy, not a measured effect in a real cohort.

Run:  python -m org_frontier.questions.q202_phi_bridge_falsification.probe_phi_bridge_falsification
"""

import numpy as np

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from org_frontier.probes.lib import max_phi_float, verdict
from org_frontier.survey.cohort_algorithmacy.phi_bridge import (
    LABELS, simulate_cohort, simulate_facet_cohort, coordination_form,
)

N = 400
N_PERM = 1000
N_BOOT = 2000


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


def edge_density(rules):
    """Cheap non-Φ structural proxy: edges / n^2 of the form's connectivity matrix."""
    cm = cm_from_rules(rules)
    n = cm.shape[0]
    return float(cm.sum()) / float(n * n)


def r2(y, X):
    """OLS R^2 of y on design [1, X]."""
    y = np.asarray(y, float)
    X = np.asarray(X, float)
    if X.ndim == 1:
        X = X[:, None]
    D = np.column_stack([np.ones(len(y)), X])
    beta, *_ = np.linalg.lstsq(D, y, rcond=None)
    resid = y - D @ beta
    ss_res = float((resid ** 2).sum())
    ss_tot = float(((y - y.mean()) ** 2).sum())
    return 1.0 - ss_res / ss_tot


def shuffle_null(phi, acs, n_perm, seed):
    """Permutation null for r(Φ_coord, ACS): shuffle the worker-to-form mapping (permute Φ_coord
    against fixed ACS). Returns (r_real, null_mean, p_two_sided, n_perm)."""
    rng = np.random.default_rng(seed)
    r_real = float(np.corrcoef(phi, acs)[0, 1])
    null = np.empty(n_perm)
    for k in range(n_perm):
        null[k] = float(np.corrcoef(rng.permutation(phi), acs)[0, 1])
    # two-sided p: fraction of |null| at least as extreme as |real| (add-one smoothing)
    p = (1 + int((np.abs(null) >= abs(r_real)).sum())) / (n_perm + 1)
    return r_real, float(null.mean()), float(null.std(ddof=1)), p


def incremental_dr2(phi, proxy, acs, n_boot, seed):
    """Hierarchical ΔR^2 of Φ_coord over the edge-density proxy, with a nonparametric bootstrap CI.
    Returns (r2_proxy, r2_full, dr2, lo, hi, r_phi_proxy)."""
    r2_proxy = r2(acs, proxy)
    r2_full = r2(acs, np.column_stack([proxy, phi]))
    dr2 = r2_full - r2_proxy
    r_phi_proxy = float(np.corrcoef(phi, proxy)[0, 1]) if np.std(proxy) > 1e-12 else 0.0

    rng = np.random.default_rng(seed)
    n = len(acs)
    boots = np.empty(n_boot)
    for k in range(n_boot):
        idx = rng.integers(0, n, n)
        p_b, x_b, y_b = proxy[idx], phi[idx], acs[idx]
        # guard against a resample with no proxy variance
        if np.std(p_b) < 1e-12 or np.std(x_b) < 1e-12:
            boots[k] = 0.0
            continue
        boots[k] = r2(y_b, np.column_stack([p_b, x_b])) - r2(y_b, p_b)
    lo = float(np.quantile(boots, 0.025))
    hi = float(np.quantile(boots, 0.975))
    return r2_proxy, r2_full, dr2, lo, hi, r_phi_proxy


def run_cohort(name, phi, acs, proxy):
    print("\n" + "-" * 78)
    print(f"Cohort: {name}  (N={len(acs)})")
    forms = sorted(set(np.round(phi, 3)))
    dens = sorted(set(np.round(proxy, 3)))
    print(f"  distinct Φ_coord readings: {forms}")
    print(f"  distinct edge-density proxy readings: {dens}")

    r_real, null_mean, null_sd, p = shuffle_null(phi, acs, N_PERM, seed=0)
    print(f"\n  H1 worker-form-shuffle null ({N_PERM} shuffles, seed 0):")
    print(f"    r(Φ_coord, ACS) real = {r_real:+.4f}")
    print(f"    shuffled null: mean = {null_mean:+.4f}, sd = {null_sd:.4f}, "
          f"two-sided p = {p:.4f}")
    h1 = (p < 0.05) and (abs(null_mean) < 0.05)

    r2_proxy, r2_full, dr2, lo, hi, rpp = incremental_dr2(phi, proxy, acs, N_BOOT, seed=0)
    print(f"\n  H2 incremental validity over edge-density proxy "
          f"(bootstrap {N_BOOT}, seed 0):")
    print(f"    r(Φ_coord, proxy) = {rpp:+.4f}")
    print(f"    R^2(proxy) = {r2_proxy:.4f}   R^2(proxy + Φ_coord) = {r2_full:.4f}")
    print(f"    ΔR^2 = {dr2:+.4f}   95% CI [{lo:+.4f}, {hi:+.4f}]")
    h2 = (dr2 > 1e-6) and (lo > 0.0)

    return {"name": name, "r_real": r_real, "null_mean": null_mean, "p": p,
            "dr2": dr2, "lo": lo, "hi": hi, "rpp": rpp, "h1": h1, "h2": h2}


def main():
    print("=" * 78)
    print("Q202 — does the Φ-bridge survive its falsification battery? (SIMULATED cohorts)")
    print("=" * 78)

    instrument_control()

    # --- whole-system cohort: two forms (commit AND, convey) ---
    rng = np.random.default_rng(0)
    coh = simulate_cohort(N, rng)
    phi_w = coh["phi_bridge"]
    acs_w = coh["acs_total"]
    commit_form = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    convey_form = [lambda x: x[1], lambda x: x[0], lambda x: x[1]]
    dens_w = {True: edge_density(commit_form), False: edge_density(convey_form)}
    proxy_w = np.array([dens_w[p > 1e-9] for p in phi_w])

    # --- facet cohort: four forms whose Φ and edge density rank differently ---
    rng_f = np.random.default_rng(0)
    fac = simulate_facet_cohort(N, rng_f)
    phi_f = fac["phi_whole"]
    acs_f = fac["acs_sc"]   # the whole-system facet (loads on Φ_whole), the natural ACS target
    proxy_f = np.array([
        edge_density(coordination_form(bool(c), bool(k)))
        for c, k in zip(fac["commit"], fac["coupled"])
    ])

    res_w = run_cohort("whole-system (2 forms: commit AND / convey)", phi_w, acs_w, proxy_w)
    res_f = run_cohort("facet (4 forms: Φ and edge density rank differently)",
                       phi_f, acs_f, proxy_f)

    # --- battery summary table ---
    print("\n" + "=" * 78)
    print("Falsification battery (across the simulated cohorts):")
    print(f"  {'cohort':<34} {'r_real':>8} {'null_mean':>10} {'p':>8} "
          f"{'ΔR^2':>8} {'CI_lo':>8} {'CI_hi':>8}")
    for r in (res_w, res_f):
        print(f"  {r['name'][:34]:<34} {r['r_real']:>+8.4f} {r['null_mean']:>+10.4f} "
              f"{r['p']:>8.4f} {r['dr2']:>+8.4f} {r['lo']:>+8.4f} {r['hi']:>+8.4f}")
    print("=" * 78)

    # H1: bridge survives the shuffle null if EVERY cohort's real effect falls outside the null.
    h1_all = res_w["h1"] and res_f["h1"]
    # H2: Φ adds over the cheap proxy where the form space decouples them (facet cohort). The
    # two-form whole-system cohort is the boundary case: only two forms, so Φ and edge density are
    # perfectly collinear and ΔR^2 is 0 by construction. Report both; H2 is SUPPORTED where the
    # form space is rich enough to separate irreducibility from edge density.
    h2_facet = res_f["h2"]
    h2_whole = res_w["h2"]

    print(f"\nH1 (worker-form shuffle destroys every Φ_coord-to-ACS relation; "
          f"real r outside null at p<.05 in all cohorts): "
          f"{'SUPPORTED' if h1_all else 'REFUTED'}")
    print(f"   whole-system: r={res_w['r_real']:+.4f}, p={res_w['p']:.4f}; "
          f"facet: r={res_f['r_real']:+.4f}, p={res_f['p']:.4f}")
    verdict_h2 = "SUPPORTED" if h2_facet else "NOT SUPPORTED"
    print(f"H2 (Φ_coord predicts ACS incrementally over the cheap edge-density proxy; "
          f"ΔR^2>0, CI excludes 0): {verdict_h2}")
    print(f"   facet (4 forms): ΔR^2={res_f['dr2']:+.4f}, CI=[{res_f['lo']:+.4f}, "
          f"{res_f['hi']:+.4f}], r(Φ,proxy)={res_f['rpp']:+.4f}")
    print(f"   whole-system (2 forms, boundary): ΔR^2={res_w['dr2']:+.4f}, "
          f"r(Φ,proxy)={res_w['rpp']:+.4f} -> proxy ties Φ where only two forms exist "
          f"({'subsumed' if not h2_whole else 'not subsumed'})")
    print("=" * 78)


if __name__ == "__main__":
    main()
