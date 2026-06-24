"""Probe 355 (Q201) — does worker substitutability degrade Φ_coord and capture algorithmacy?

Question: does perceived substitutability (SU) lower Φ_coord, and does that degraded Φ_coord track
lower reported algorithmacy (ACS) — the displacement/capture prediction? Φ_coord is the per-worker
exact IIT-4.0 max Φ_MIP of the worker's W-S-C coordination form (study-1 / q193 bridge). SU is the
reported substitutability of the worker's role: a worker whose role admits an interchangeable copy
sits in a more factorizable coordination form.

H1: higher SU lowers Φ_coord (β < 0, 95% CI excludes 0), and lower Φ_coord predicts lower ACS.
    Workers whose form admits a substitutable copy factor the coordination, so SU degrades the
    irreducibility the instrument reads. Null: SU is unrelated to Φ_coord.
H2: Φ_coord mediates SU -> ACS. The indirect path SU -> Φ_coord -> ACS is nonzero (bootstrap CI
    excludes 0) and exceeds the direct SU -> ACS path. Null: no indirect path through Φ_coord.

Method: import the study-1 bridge module (org_frontier/survey/cohort_algorithmacy/phi_bridge.py).
Parameterize the W-node as duplicable when SU is high: a high-SU row maps to the convey pass-through
(Φ_coord = 0) and a low-SU, interdependent, committing row maps to the irreducible AND(W,C) mediated
triad (Φ_coord = 2.0). Simulate a bridge cohort where SU gates the form and ACS-total rides on the
resulting Φ_coord, and a pivotal-W control cohort where the worker is never duplicable (every form
held irreducible) so SU cannot factor the form and Φ_coord is constant. Regress Φ_coord on
standardized SU and read the slope and 95% CI (H1, structural leg); regress ACS on Φ_coord (H1,
construct leg). Bootstrap the single-mediator path SU -> Φ_coord -> ACS and compare the indirect and
direct effects (H2). The control arm's flat SU -> Φ_coord slope shows the degradation rides on
substitutability factoring the form, not a shared-scale artifact.

Determinism: one fixed seed (numpy.random.default_rng(0)) for the cohort draw and a fixed seed for
the bootstrap. Φ_coord depends only on which of two forms a worker maps to, so the sweep reproduces
exactly on re-run.

Scope: the cohort is SIMULATED. No worker is measured. Φ_coord is a structural property of the
Boolean form a worker's reported conditions map to, read by the exact-Φ instrument. The
displacement/capture path is evidence about the bridge and instrument on synthetic data, not a
measured effect in a real panel.

Run:  python -m org_frontier.questions.q201_phi_substitutability_capture.probe_phi_substitutability_capture
"""

import numpy as np

from org_frontier.classifier.classifier import tpm_from_rules
from org_frontier.probes.lib import max_phi_float, verdict
from org_frontier.survey.cohort_algorithmacy.phi_bridge import (
    LABELS,
    worker_rules,
    simulate_substitutability_cohorts,
    bootstrap_mediation,
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


def phi_su_slope_ci(su, phi):
    """OLS slope of Φ_coord on standardized SU with a 95% CI. Returns (beta, lo, hi).

    Returns (0, 0, 0) if Φ_coord has no variance (the control arm holds the form constant)."""
    if np.std(phi) < 1e-12:
        return 0.0, 0.0, 0.0
    su = np.asarray(su, float)
    su_z = (su - su.mean()) / su.std(ddof=1)
    X = np.column_stack([np.ones(len(su_z)), su_z])
    beta, lo, hi, _ = ols_with_ci(X, phi)
    return float(beta[1]), float(lo[1]), float(hi[1])


def acs_on_phi_ci(phi, acs):
    """OLS slope of ACS-total on Φ_coord with a 95% CI. Returns (beta, lo, hi)."""
    if np.std(phi) < 1e-12:
        return 0.0, 0.0, 0.0
    X = np.column_stack([np.ones_like(phi), phi])
    beta, lo, hi, _ = ols_with_ci(X, acs)
    return float(beta[1]), float(lo[1]), float(hi[1])


def main():
    print("=" * 78)
    print("Q201 — substitutability degrades Φ_coord and captures algorithmacy (SIMULATED cohort)")
    print("=" * 78)

    instrument_control()

    # The two distinct forms substitutability gates between, shown so the bridge map is auditable.
    print("\nBridge map — substitutability gates the W-node's duplicability:")
    pivotal_rules = worker_rules(7, 7, 1, control=False)    # high TI/SA, low SU -> pivotal, commit
    substit_rules = worker_rules(7, 7, 7, control=False)    # high SU -> duplicable, form factors
    for name, rules in (("pivotal-W  S'=W AND C", pivotal_rules),
                        ("substitut. S'=W (factors)", substit_rules)):
        v = verdict(rules, LABELS)
        mx, _ = max_phi_float(tpm_from_rules(rules))
        print(f"  {name:26s}: {v.structure:8s}  Φ_coord={mx:.6f}")

    rng = np.random.default_rng(0)
    coh = simulate_substitutability_cohorts(N, rng)
    bridge, control = coh["bridge"], coh["control"]

    n_irr_b = int((bridge["phi"] > 1e-9).sum())
    n_irr_c = int((control["phi"] > 1e-9).sum())
    print(f"\nCohorts: N={N} per arm.")
    print(f"  bridge arm:   {n_irr_b} pivotal (irreducible) forms, {N - n_irr_b} substitutable "
          f"(convey) forms; Φ_coord range [{bridge['phi'].min():.2f}, {bridge['phi'].max():.2f}]")
    print(f"  control arm:  pivotal-W throughout ({n_irr_c} irreducible); Φ_coord held constant at "
          f"{control['phi'][0]:.2f}, variance {float(np.var(control['phi'])):.4f}")

    # H1 structural leg: SU -> Φ_coord slope in each arm.
    b_su_b, lo_su_b, hi_su_b = phi_su_slope_ci(bridge["su"], bridge["phi"])
    b_su_c, lo_su_c, hi_su_c = phi_su_slope_ci(control["su"], control["phi"])
    # H1 construct leg: ACS on Φ_coord in the bridge arm.
    b_ap, lo_ap, hi_ap = acs_on_phi_ci(bridge["phi"], bridge["acs_total"])

    print("\n" + "-" * 78)
    print("H1 structural leg — Φ_coord ~ 1 + SU(z), per arm")
    print("-" * 78)
    print(f"{'arm':<12}{'SU->Φ slope':>16}{'95% CI':>28}")
    print(f"{'bridge':<12}{b_su_b:>+16.4f}   [{lo_su_b:+.4f}, {hi_su_b:+.4f}]")
    if np.std(control["phi"]) < 1e-12:
        print(f"{'control':<12}{'flat (Φ const)':>16}{'[ n/a — no Φ variance ]':>28}")
    else:
        print(f"{'control':<12}{b_su_c:>+16.4f}   [{lo_su_c:+.4f}, {hi_su_c:+.4f}]")
    print("-" * 78)
    print("H1 construct leg — ACS-total ~ 1 + Φ_coord (bridge arm)")
    print(f"   Φ_coord -> ACS slope = {b_ap:+.4f}  95% CI [{lo_ap:+.4f}, {hi_ap:+.4f}]")

    h1 = (b_su_b < 0.0) and (hi_su_b < 0.0) and (b_ap > 0.0) and (lo_ap > 0.0)

    # H2: bootstrap single-mediator path SU -> Φ_coord -> ACS in the bridge arm.
    med = bootstrap_mediation(bridge["su"].astype(float), bridge["phi"],
                              bridge["acs_total"], n_boot=5000, seed=0)
    ind, ind_lo, ind_hi = med["indirect"], med["indirect_ci"][0], med["indirect_ci"][1]
    dir_, dir_lo, dir_hi = med["direct"], med["direct_ci"][0], med["direct_ci"][1]

    print("\n" + "-" * 78)
    print("H2 mediation (bridge arm) — SU -> Φ_coord -> ACS, standardized, 5000-boot")
    print("-" * 78)
    print(f"  path a  (SU -> Φ_coord)        = {med['a']:+.4f}  CI [{med['a_ci'][0]:+.4f}, {med['a_ci'][1]:+.4f}]")
    print(f"  path b  (Φ_coord -> ACS | SU)  = {med['b']:+.4f}  CI [{med['b_ci'][0]:+.4f}, {med['b_ci'][1]:+.4f}]")
    print(f"  indirect (a*b)                = {ind:+.4f}  CI [{ind_lo:+.4f}, {ind_hi:+.4f}]")
    print(f"  direct   (c', SU -> ACS | Φ)  = {dir_:+.4f}  CI [{dir_lo:+.4f}, {dir_hi:+.4f}]")
    print(f"  |indirect| vs |direct|        : {abs(ind):.4f}  vs  {abs(dir_):.4f}")
    print("-" * 78)

    indirect_nonzero = (ind_lo > 0.0) or (ind_hi < 0.0)
    indirect_exceeds_direct = abs(ind) > abs(dir_)
    h2 = indirect_nonzero and indirect_exceeds_direct

    print("\n" + "=" * 78)
    print(f"H1 (SU lowers Φ_coord, CI<0; lower Φ_coord predicts lower ACS, CI>0): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"   SU->Φ_coord={b_su_b:+.4f} CI[{lo_su_b:+.4f},{hi_su_b:+.4f}]; "
          f"Φ_coord->ACS={b_ap:+.4f} CI[{lo_ap:+.4f},{hi_ap:+.4f}]; control SU->Φ flat")
    print(f"H2 (indirect SU->Φ_coord->ACS nonzero and exceeds direct SU->ACS): "
          f"{'CONFIRMED' if h2 else 'NOT SUPPORTED'}")
    print(f"   indirect={ind:+.4f} CI[{ind_lo:+.4f},{ind_hi:+.4f}]; "
          f"direct={dir_:+.4f} CI[{dir_lo:+.4f},{dir_hi:+.4f}]; |ind|>|dir|={indirect_exceeds_direct}")
    print("=" * 78)


if __name__ == "__main__":
    main()
