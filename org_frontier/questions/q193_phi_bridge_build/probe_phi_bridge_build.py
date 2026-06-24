"""Probe 347 (Q193) — a per-worker Φ-based coordination measure that predicts the algorithmacy construct.

Question: can a per-worker Φ-based coordination measure be derived from each simulated worker's
coordination form, and does it predict the latent algorithmacy literacy construct in the simulated panel?

H1: the per-worker Φ_coord (exact IIT-4.0 max Φ_MIP over the worker's W-S-C form, with the S rule
    parameterized by that worker's reported interdependence/commit/substitutability conditions)
    correlates positively with the latent ACS-total factor score across the cohort (r > 0.20, 95% CI
    excludes 0). Null: the r CI includes 0.
H2: on a CONTROL cohort whose forms are rewired to be dyadic/factorizable (Φ_coord identically 0 by
    construction), the Φ_coord-to-ACS correlation vanishes (|r| < 0.10) while it survives in the bridge
    cohort. The association rides on irreducibility, not on a shared scale artifact. Null: the control r
    is as large as the bridge r.

Method: build org_frontier/survey/cohort_algorithmacy/phi_bridge.py — map each simulated worker's
(TI, SA-commit, SU) row to W-S-C Boolean rules (S commits AND(W,C) when the worker reports a binding,
interdependent, non-substitutable coordination; otherwise S conveys W and the form factors). Compute
Φ_coord with classifier.tpm_from_rules + probes.lib.max_phi_float. Simulate a cohort whose reported
conditions and ACS-total factor score load on one latent, so an irreducible form tends to co-occur with
higher algorithmacy. Correlate Φ_coord with ACS-total (Pearson r, Fisher-z 95% CI) in the bridge cohort
and in the forced-dyadic control cohort.

Determinism: one fixed seed (numpy.random.default_rng(0)); Φ_coord depends only on which of two forms a
worker maps to, so the cohort sweep reproduces exactly.

Scope: the cohort is SIMULATED. No worker is measured. Φ_coord is a structural property of the Boolean
form a worker's reported conditions map to, read by the exact-Φ instrument. The association is evidence
about the instrument and the bridge on synthetic data, not a measured effect in a real cohort.

Run:  python -m org_frontier.questions.q193_phi_bridge_build.probe_phi_bridge_build
"""

import numpy as np

from org_frontier.classifier.classifier import tpm_from_rules
from org_frontier.probes.lib import max_phi_float, verdict
from org_frontier.survey.cohort_algorithmacy.phi_bridge import (
    LABELS, simulate_cohort, phi_coord, pearson_ci, worker_rules,
)

N = 300


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
    print("Q193 — per-worker Φ_coord vs the latent algorithmacy construct (SIMULATED cohort)")
    print("=" * 78)

    instrument_control()

    # The two distinct forms and their Φ_coord, shown so the bridge map is auditable.
    print("\nBridge map — the two W-S-C forms a worker can map to:")
    commit_rules = worker_rules(7, 7, 1, control=False)   # high TI, high SA, low SU -> commit
    convey_rules = worker_rules(7, 7, 7, control=False)   # high SU -> convey (pass-through)
    for name, rules in (("commit S'=W AND C", commit_rules), ("convey S'=W", convey_rules)):
        v = verdict(rules, LABELS)
        mx, _ = max_phi_float(tpm_from_rules(rules))
        print(f"  {name:18s}: {v.structure:8s}  Φ_coord={mx:.6f}")

    rng = np.random.default_rng(0)
    coh = simulate_cohort(N, rng)

    n_commit = int((coh["phi_bridge"] > 1e-9).sum())
    print(f"\nCohort: N={N}; bridge cohort has {n_commit} irreducible (commit) forms, "
          f"{N - n_commit} factorizable (convey) forms.")
    print(f"  control cohort irreducible forms: {int((coh['phi_control'] > 1e-9).sum())} "
          f"(0 by construction).")

    rb, rb_lo, rb_hi = pearson_ci(coh["phi_bridge"], coh["acs_total"])
    rc, rc_lo, rc_hi = pearson_ci(coh["phi_control"], coh["acs_total"])

    print("\n" + "-" * 78)
    print(f"{'cohort':<12}{'Φ_coord range':<18}{'r(Φ_coord, ACS-total)':<26}{'95% CI':<22}")
    print("-" * 78)
    pb = f"[{coh['phi_bridge'].min():.2f}, {coh['phi_bridge'].max():.2f}]"
    pc = f"[{coh['phi_control'].min():.2f}, {coh['phi_control'].max():.2f}]"
    print(f"{'bridge':<12}{pb:<18}{rb:<+26.4f}[{rb_lo:+.4f}, {rb_hi:+.4f}]")
    print(f"{'control':<12}{pc:<18}{rc:<+26.4f}[{rc_lo:+.4f}, {rc_hi:+.4f}]")
    print("-" * 78)

    # H1: bridge r > 0.20 and 95% CI excludes 0
    h1 = (rb > 0.20) and (rb_lo > 0.0)
    # H2: control |r| < 0.10 while bridge association survives
    h2 = (abs(rc) < 0.10) and (rb > 0.20) and (rb_lo > 0.0)

    print(f"\nH1 (Φ_coord predicts ACS-total, r>0.20 & CI excludes 0): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"   bridge r={rb:+.4f}, CI=[{rb_lo:+.4f}, {rb_hi:+.4f}]")
    print(f"H2 (control association vanishes, |r|<0.10, bridge survives): "
          f"{'CONFIRMED' if h2 else 'NOT SUPPORTED'}")
    print(f"   control r={rc:+.4f} (|r|={abs(rc):.4f}); bridge r={rb:+.4f}")


if __name__ == "__main__":
    main()
