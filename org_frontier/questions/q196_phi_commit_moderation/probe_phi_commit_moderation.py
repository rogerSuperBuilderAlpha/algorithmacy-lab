"""Probe 350 (Q196) — does the Φ_coord-to-ACS association strengthen under perceived commit?

Question: does the Φ_coord-to-ACS association strengthen under perceived system commitment
(commit vs convey)? Φ_coord is the per-worker exact IIT-4.0 max Φ_MIP of the worker's W-S-C
coordination form (study 1 / q193 bridge). SA-commit is the reported commit-vs-convey of the
system the worker coordinates through.

H1: the interaction Φ_coord × SA-commit on ACS-total is positive (95% CI excludes 0). Φ_coord
    predicts ACS more where workers report the system commits. Null: the interaction CI includes 0.
H2: in a convey-only control cohort (SA-commit floored so forms stay dyadic), Φ_coord is
    near-constant and its ACS slope is flat, while the commit cohort shows a positive slope. The
    slope difference (commit minus convey) CI excludes 0. Null: commit and convey cohorts have equal
    Φ-ACS slopes.

Method: import the study-1 bridge module (org_frontier/survey/cohort_algorithmacy/phi_bridge.py).
Build forms whose S-rule strength scales with SA-commit: a high-commit, interdependent,
non-substitutable row maps to the irreducible AND(W,C) form (Φ_coord = 2.0); otherwise the form
conveys (Φ_coord = 0). Simulate a commit cohort whose ACS-total loads on Φ_coord only through an
interaction with standardized SA-commit, and a convey-floored control cohort whose SA is capped
below the commit threshold so every form is dyadic and Φ_coord is identically 0. Fit a moderated OLS
ACS ~ 1 + Φ_coord + SA + Φ_coord×SA in the commit cohort and read the interaction coefficient and
its 95% CI (H1). Compute the Φ-ACS slope in each cohort and the slope difference with a paired
bootstrap CI (H2).

Determinism: one fixed seed (numpy.random.default_rng(0)) for the cohort draw and a fixed seed for
the bootstrap. Φ_coord depends only on which of two forms a worker maps to, so the sweep reproduces
exactly on re-run.

Scope: the cohort is SIMULATED. No worker is measured. Φ_coord is a structural property of the
Boolean form a worker's reported conditions map to, read by the exact-Φ instrument. The moderation
is evidence about the bridge and instrument on synthetic data, not a measured effect in a real panel.

Run:  python -m org_frontier.questions.q196_phi_commit_moderation.probe_phi_commit_moderation
"""

import numpy as np

from org_frontier.classifier.classifier import tpm_from_rules
from org_frontier.probes.lib import max_phi_float, verdict
from org_frontier.survey.cohort_algorithmacy.phi_bridge import (
    LABELS,
    worker_rules,
    simulate_commit_convey_cohorts,
    ols_with_ci,
)

N = 600


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


def phi_acs_slope(phi, acs):
    """OLS slope of ACS on Φ_coord (univariate). Returns 0.0 if Φ has no variance."""
    if np.std(phi) < 1e-12:
        return 0.0
    X = np.column_stack([np.ones_like(phi), phi])
    beta, _, _, _ = ols_with_ci(X, acs)
    return float(beta[1])


def bootstrap_slope_diff(commit, convey, n_boot=5000, seed=0):
    """Bootstrap CI for the slope difference (commit Φ-ACS slope minus convey Φ-ACS slope).

    Resamples each cohort independently with replacement and recomputes both slopes. The convey
    slope is 0 whenever Φ has no variance in the resample (it is identically 0 by construction)."""
    rng = np.random.default_rng(seed)
    pc, ac = commit["phi"], commit["acs_total"]
    pv, av = convey["phi"], convey["acs_total"]
    nc, nv = len(pc), len(pv)
    diffs = np.empty(n_boot)
    for b in range(n_boot):
        ic = rng.integers(0, nc, nc)
        iv = rng.integers(0, nv, nv)
        sc = phi_acs_slope(pc[ic], ac[ic])
        sv = phi_acs_slope(pv[iv], av[iv])
        diffs[b] = sc - sv
    lo, hi = np.percentile(diffs, [2.5, 97.5])
    return float(diffs.mean()), float(lo), float(hi)


def main():
    print("=" * 78)
    print("Q196 — Φ_coord × commit moderation on ACS-total (SIMULATED cohort)")
    print("=" * 78)

    instrument_control()

    # The two distinct forms the S-rule scales between, shown so the bridge map is auditable.
    print("\nBridge map — S-rule strength scales with reported commit:")
    commit_rules = worker_rules(7, 7, 1, control=False)   # high TI, high SA, low SU -> commit
    convey_rules = worker_rules(7, 7, 7, control=False)   # high SU -> convey (pass-through)
    for name, rules in (("commit S'=W AND C", commit_rules), ("convey S'=W", convey_rules)):
        v = verdict(rules, LABELS)
        mx, _ = max_phi_float(tpm_from_rules(rules))
        print(f"  {name:18s}: {v.structure:8s}  Φ_coord={mx:.6f}")

    rng = np.random.default_rng(0)
    coh = simulate_commit_convey_cohorts(N, rng)
    commit, convey = coh["commit"], coh["convey"]

    n_irr_c = int((commit["phi"] > 1e-9).sum())
    n_irr_v = int((convey["phi"] > 1e-9).sum())
    print(f"\nCohorts: N={N} per arm.")
    print(f"  commit arm:  {n_irr_c} irreducible (commit) forms, {N - n_irr_c} convey forms; "
          f"Φ_coord range [{commit['phi'].min():.2f}, {commit['phi'].max():.2f}]")
    print(f"  convey arm:  {n_irr_v} irreducible forms (0 by construction); "
          f"Φ_coord range [{convey['phi'].min():.2f}, {convey['phi'].max():.2f}]")

    # H1: moderated OLS in the commit cohort. ACS ~ 1 + Φ + SA + Φ×SA, SA standardized.
    phi = commit["phi"]
    sa_z = commit["sa_z"]
    inter = phi * sa_z
    X = np.column_stack([np.ones(N), phi, sa_z, inter])
    beta, lo, hi, se = ols_with_ci(X, commit["acs_total"])
    names = ["intercept", "Φ_coord", "SA(z)", "Φ_coord×SA"]

    print("\n" + "-" * 78)
    print(f"Moderated OLS (commit cohort):  ACS-total ~ 1 + Φ_coord + SA(z) + Φ_coord×SA")
    print("-" * 78)
    print(f"{'term':<16}{'coef':>12}{'SE':>10}{'95% CI':>26}")
    for i, nm in enumerate(names):
        print(f"{nm:<16}{beta[i]:>+12.4f}{se[i]:>10.4f}   [{lo[i]:+.4f}, {hi[i]:+.4f}]")
    print("-" * 78)

    b_int, lo_int, hi_int = beta[3], lo[3], hi[3]
    h1 = (b_int > 0.0) and (lo_int > 0.0)

    # H2: per-cohort Φ-ACS slopes and the slope difference with a bootstrap CI.
    slope_c = phi_acs_slope(commit["phi"], commit["acs_total"])
    slope_v = phi_acs_slope(convey["phi"], convey["acs_total"])
    d_mean, d_lo, d_hi = bootstrap_slope_diff(commit, convey, n_boot=5000, seed=0)

    print("\n" + "-" * 78)
    print(f"{'cohort':<14}{'Φ-ACS slope':>16}{'Φ variance':>16}")
    print("-" * 78)
    print(f"{'commit':<14}{slope_c:>+16.4f}{float(np.var(commit['phi'])):>16.4f}")
    print(f"{'convey':<14}{slope_v:>+16.4f}{float(np.var(convey['phi'])):>16.4f}")
    print("-" * 78)
    print(f"slope difference (commit - convey) = {d_mean:+.4f}  "
          f"bootstrap 95% CI [{d_lo:+.4f}, {d_hi:+.4f}]")

    h2 = (abs(slope_v) < 1e-9) and (slope_c > 0.0) and (d_lo > 0.0)

    print("\n" + "=" * 78)
    print(f"H1 (Φ_coord×SA-commit interaction on ACS-total is positive, CI excludes 0): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"   interaction coef={b_int:+.4f}, CI=[{lo_int:+.4f}, {hi_int:+.4f}]")
    print(f"H2 (commit Φ-ACS slope positive, convey slope flat, slope diff CI excludes 0): "
          f"{'CONFIRMED' if h2 else 'NOT SUPPORTED'}")
    print(f"   commit slope={slope_c:+.4f}, convey slope={slope_v:+.4f}, "
          f"diff CI=[{d_lo:+.4f}, {d_hi:+.4f}]")
    print("=" * 78)


if __name__ == "__main__":
    main()
