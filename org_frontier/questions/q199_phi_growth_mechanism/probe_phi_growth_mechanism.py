"""Probe 353 (Q199) — does within-person change in Φ_coord track within-person change in algorithmacy?

Question: across waves of the simulated panel, does within-person wave-to-wave change in the per-worker
Φ_coord (exact IIT-4.0 max Φ_MIP over the worker's W-S-C coordination form, built by the study-1 bridge
module) covary with within-person change in ACS-total? Does the bridge move together with the construct,
not just at baseline?

H1: within-person wave-to-wave change in Φ_coord positively covaries with within-person change in
    ACS-total. The multilevel within-person slope of ACS on person-mean-centered Φ_coord is > 0 with a
    person-level cluster-bootstrap 95% CI that excludes 0. Null: within-person ΔΦ and ΔACS are
    uncorrelated (the within slope CI includes 0).
H2: the within-person Φ-ACS coupling exceeds the between-person coupling. The within-person slope is
    larger than the between-person slope, and the bootstrap CI on Δ = within − between excludes 0, so the
    effect is a person-level dynamic, not just stable selection. Null: the within- and between-person
    Φ-ACS slopes are equal (Δ CI includes 0).

Method: import the study-1 bridge module org_frontier/survey/cohort_algorithmacy/phi_bridge.py. Simulate a
longitudinal panel (simulate_panel) with one stable between-person coordination trait per person and a
within-person, time-varying coordination state per wave; the reported conditions (TI, SA-commit, SU) and
the Φ_coord map respond to the person's current total coordination, and ACS-total loads more on the
within-person state than on the stable trait. Person-mean-center Φ_coord in the long file into a
within-person deviation and a between-person mean, regress ACS-total on both, and read the within- and
between-person slopes (within_between_slopes). Confidence intervals come from a person-level cluster
bootstrap (resample whole persons, fixed seed). Control comparison: the between-person Φ term is the
comparison slope (H2 tests within − between). A forced-dyadic control panel (Φ_coord ≡ 0) is reported to
confirm the slopes collapse when the form is rewired to factorize.

Determinism: one fixed seed (numpy.random.default_rng(0)) for the panel and a fixed bootstrap seed (0).
Φ_coord depends only on which of two W-S-C forms a worker maps to, so the panel sweep reproduces exactly.

Scope: the panel is SIMULATED. No worker is measured. Φ_coord is a structural property of the Boolean
form a worker's reported conditions map to, read by the exact-Φ instrument. The within-person coupling is
evidence about the bridge on synthetic longitudinal data, not a measured effect in a real cohort.

Run:  python -m org_frontier.questions.q199_phi_growth_mechanism.probe_phi_growth_mechanism
"""

import numpy as np

from org_frontier.classifier.classifier import tpm_from_rules
from org_frontier.probes.lib import max_phi_float, verdict
from org_frontier.survey.cohort_algorithmacy.phi_bridge import (
    LABELS, simulate_panel, person_center, within_between_slopes,
)

N_PERSONS = 300
N_WAVES = 5
N_BOOT = 5000


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
    print("Q199 — within-person ΔΦ_coord vs within-person ΔACS-total (SIMULATED panel)")
    print("=" * 78)

    instrument_control()

    rng = np.random.default_rng(0)
    panel = simulate_panel(N_PERSONS, N_WAVES, rng)

    phi = panel["phi_bridge"]
    phi_c = panel["phi_control"]
    acs = panel["acs_total"]
    person = panel["person"]
    n_rows = len(person)

    n_commit_rows = int((phi > 1e-9).sum())
    between_phi, within_phi = person_center(phi, person)
    # persons whose Φ_coord moves at least once across waves (within-person variance present)
    movers = sum(1 for pid in np.unique(person) if np.ptp(phi[person == pid]) > 1e-9)

    print(f"\nPanel: {N_PERSONS} persons x {N_WAVES} waves = {n_rows} rows.")
    print(f"  irreducible (commit) form rows: {n_commit_rows} / {n_rows} "
          f"(Φ_coord = 2.0); rest factorize (Φ_coord = 0.0).")
    print(f"  persons with within-person Φ_coord change across waves: {movers} / {N_PERSONS}.")
    print(f"  within-person Φ_coord deviation std = {np.std(within_phi):.4f} "
          f"(wave-to-wave movement the within slope reads).")

    # Multilevel within/between slopes of ACS on person-mean-centered Φ_coord (bridge panel).
    (bw, bw_lo, bw_hi,
     bb, bb_lo, bb_hi,
     bd, bd_lo, bd_hi) = within_between_slopes(phi, acs, person, n_boot=N_BOOT, seed=0)

    # Control panel: Φ_coord identically 0, so both slopes are 0 by construction.
    (cw, cw_lo, cw_hi,
     cb, cb_lo, cb_hi,
     cd, cd_lo, cd_hi) = within_between_slopes(phi_c, acs, person, n_boot=N_BOOT, seed=0)

    print("\n" + "-" * 78)
    print(f"{'panel':<10}{'term':<12}{'slope (ACS on Φ_coord)':<26}{'95% CI (cluster bootstrap)':<26}")
    print("-" * 78)
    print(f"{'bridge':<10}{'within':<12}{bw:<+26.4f}[{bw_lo:+.4f}, {bw_hi:+.4f}]")
    print(f"{'bridge':<10}{'between':<12}{bb:<+26.4f}[{bb_lo:+.4f}, {bb_hi:+.4f}]")
    print(f"{'bridge':<10}{'Δ w−b':<12}{bd:<+26.4f}[{bd_lo:+.4f}, {bd_hi:+.4f}]")
    print(f"{'control':<10}{'within':<12}{cw:<+26.4f}[{cw_lo:+.4f}, {cw_hi:+.4f}]")
    print(f"{'control':<10}{'between':<12}{cb:<+26.4f}[{cb_lo:+.4f}, {cb_hi:+.4f}]")
    print("-" * 78)

    # H1: within-person slope > 0 and CI excludes 0.
    h1 = (bw > 0.0) and (bw_lo > 0.0)
    # H2: within exceeds between and the Δ CI excludes 0.
    h2 = (bd > 0.0) and (bd_lo > 0.0)

    print("\n" + "=" * 78)
    print(f"H1 (within-person ΔΦ tracks ΔACS, within slope > 0 & CI excludes 0): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"   within slope = {bw:+.4f}, 95% CI [{bw_lo:+.4f}, {bw_hi:+.4f}]")
    print(f"H2 (within coupling exceeds between, Δ CI excludes 0): "
          f"{'SUPPORTED' if h2 else 'NOT SUPPORTED'}")
    print(f"   within = {bw:+.4f}, between = {bb:+.4f}, Δ = {bd:+.4f}, "
          f"95% CI [{bd_lo:+.4f}, {bd_hi:+.4f}]")
    print(f"   control panel (Φ_coord ≡ 0): within = {cw:+.4f}, between = {cb:+.4f} "
          f"(both 0 by construction)")
    print("=" * 78)


if __name__ == "__main__":
    main()
