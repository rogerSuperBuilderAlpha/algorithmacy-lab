"""Probe q174 — does propagated Φ-CI width scale with coder disagreement (1 - alpha)?

QUESTION
    A coded account of a coordination is read by two coders. They disagree on which
    active-bit decisions hold, and that disagreement propagates through the
    rules->TPM->exact-Φ bridge into a confidence interval on Φ. Does the CI width grow
    as agreement (Krippendorff alpha) falls, and is there an agreement floor below which
    the interval straddles zero so the dyadic-vs-triadic verdict goes indeterminate?

H1  Across a synthetic alpha-sweep (alpha ~0.5 -> 1.0, fixed consensus rules), mean
    Φ-CI width decreases monotonically with alpha: Spearman rho <= -0.9, p < 0.01.
    NULL: |rho| < 0.5 or non-monotone -> CI width does not track agreement.

H2  There is an agreement threshold alpha* below which the CI straddles zero (verdict
    indeterminate dyadic-vs-triadic) for > 50% of forms, and alpha* is stable (+/-0.05)
    across two independent synthetic ensembles. NULL: no such threshold, or alpha*
    differs by > 0.1 between ensembles.

METHOD
    Each form has a true triadic rule set (max Φ_MIP > 0) and a dyadic collapse reading
    (Φ_MIP = 0) reached by dropping the mediating coupling. A coder reads K active-bit
    decision units; with per-unit dissent probability p each coder may flip the coupling
    unit, switching their reading between the triadic and collapsed rule set. The per-coder
    Φ readings feed `phi_ci` (the bridge's bootstrap-t CI), and the coder x unit decision
    matrix gives Krippendorff alpha. Sweeping p sweeps alpha. CI width and the fraction of
    forms whose CI crosses zero are measured against alpha. Φ is not reimplemented; the
    bridge wraps the IIT-4.0 classifier.

    INSTRUMENT CONTROL: the faithful triad [x1, x0&x2, x1] reads triadic with max Φ_MIP
    = 2.0; alpha=1.0 panels (identical readings) return a degenerate CI of width 0; a
    verdict-invariant panel (two distinct positive-Φ readings, never the collapse) gives a
    nonzero width that never crosses zero.

    All inputs are synthetic coded rule sets, not measured worker states.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q174_alpha_phi_width.probe_alpha_phi_width
"""

import os

import numpy as np
from scipy.stats import spearmanr

from org_frontier.field.rule_to_phi import rule_to_phi, phi_ci, krippendorff_alpha

LABELS = ("W", "S", "C")

# A faithful triad and its dyadic collapse (drop the C->S coupling so C factors off).
TRIAD = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
COLLAPSE = [lambda x: x[1], lambda x: x[0], lambda x: x[1]]

# Three borderline forms: each a triad (Φ>0) whose collapse reads dyadic (Φ=0).
FORMS = {
    "read_recipient": (
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        [lambda x: x[1], lambda x: x[0], lambda x: x[1]],
    ),
    "gated_mediator": (
        [lambda x: x[1] & x[2], lambda x: x[0], lambda x: x[1]],
        [lambda x: x[1], lambda x: x[0], lambda x: x[1]],
    ),
    "shared_state": (
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[0]],
        [lambda x: x[1], lambda x: x[0], lambda x: x[0]],
    ),
}

N_CODERS = 8          # coders per account panel
K_UNITS = 12          # active-bit decision units per coder
COUPLING_UNIT = 0     # the unit whose dissent flips triad <-> collapse
N_BOOT = 1200


def _phi_of(rules):
    return rule_to_phi(rules, LABELS)["max_phi"]


def panel_for_form(triad_rules, collapse_rules, f, rng):
    """Build a coder panel for one account at disagreement fraction f in [0, 1].

    Returns (coder_phis, coding_matrix). A fraction f of the K decision units are split
    (half the coders code 1, half 0, in a random order); the rest are unanimous, their
    value alternating per unit so the pooled labels carry variance and Krippendorff alpha
    is well defined. The coupling unit (unit 0) is split whenever f > 0: coders coding 1 on
    it read the dyadic collapse, coders coding 0 read the triad. Disagreement on which
    states are active thus drives both the measured alpha and the Φ spread.
    """
    phi_triad = _phi_of(triad_rules)
    phi_collapse = _phi_of(collapse_rules)
    codings = np.zeros((N_CODERS, K_UNITS), dtype=int)

    # Coupling unit: a graded number of coders read the collapse, scaling with f. This
    # makes the Φ spread (and so the CI) grow smoothly with disagreement instead of
    # saturating at a 50/50 split.
    n_flip = int(round(f * N_CODERS))
    coupling_col = np.array([1] * n_flip + [0] * (N_CODERS - n_flip))
    codings[:, COUPLING_UNIT] = rng.permutation(coupling_col)

    # Remaining units carry background disagreement so the matrix-wide Krippendorff alpha
    # tracks f: a fraction f of them are split 50/50, the rest unanimous (alternating).
    n_split = int(round(f * (K_UNITS - 1)))
    for j in range(1, K_UNITS):
        if j <= n_split:
            col = np.array([0] * (N_CODERS // 2) + [1] * (N_CODERS - N_CODERS // 2))
            codings[:, j] = rng.permutation(col)
        else:
            codings[:, j] = j % 2  # unanimous, value alternates across units

    phis = np.where(codings[:, COUPLING_UNIT] == 1, phi_collapse, phi_triad).astype(float)
    return phis, codings


def sweep(fs, seed):
    """One ensemble: for each disagreement fraction f, average CI width and zero-crossing
    rate over the forms. Returns rows (alpha, mean_width, frac_cross_zero)."""
    rng = np.random.default_rng(seed)
    rows = []
    for f in fs:
        alphas, widths, crosses = [], [], []
        for _name, (triad_rules, collapse_rules) in FORMS.items():
            phis, codings = panel_for_form(triad_rules, collapse_rules, f, rng)
            res = phi_ci(phis, coder_codings=codings, n_boot=N_BOOT, rng=rng)
            a = krippendorff_alpha(codings)
            w = res["ci_high"] - res["ci_low"]
            cross = res["ci_low"] <= 0.0 <= res["ci_high"]
            alphas.append(a)
            widths.append(w)
            crosses.append(1.0 if cross else 0.0)
        rows.append((float(np.mean(alphas)), float(np.mean(widths)),
                     float(np.mean(crosses))))
    return rows


def instrument_control():
    # 1. faithful triad reads triadic, max Φ_MIP = 2.0
    v = rule_to_phi(TRIAD, LABELS)
    assert v["structure"] == "triadic" and abs(v["max_phi"] - 2.0) < 1e-9, v

    rng = np.random.default_rng(0)
    # 2. alpha=1 panel (identical triadic readings) -> degenerate CI, width 0
    phis_id = np.full(N_CODERS, 2.0)
    cod_id = np.zeros((N_CODERS, K_UNITS), dtype=int)
    r_id = phi_ci(phis_id, coder_codings=cod_id, n_boot=N_BOOT, rng=rng)
    width_id = r_id["ci_high"] - r_id["ci_low"]
    assert r_id["degenerate"] and width_id < 1e-9 and abs(r_id["alpha"] - 1.0) < 1e-9, r_id

    # 3. verdict-invariant panel: two distinct positive-Φ readings (2.0 and 3.0),
    #    never the collapse -> nonzero width that never crosses zero.
    phis_inv = np.array([2.0, 3.0] * (N_CODERS // 2))
    cod_inv = np.tile(np.array([0, 1]), (N_CODERS // 2, 1)).reshape(N_CODERS, 1)
    cod_inv = np.repeat(cod_inv, K_UNITS, axis=1)
    r_inv = phi_ci(phis_inv, coder_codings=cod_inv, n_boot=N_BOOT, rng=rng)
    width_inv = r_inv["ci_high"] - r_inv["ci_low"]
    assert width_inv > 1e-6 and r_inv["ci_low"] > 0.0, r_inv

    print(f"CONTROL faithful triad: structure={v['structure']} max_phi={v['max_phi']:.4f} "
          f"| alpha=1 width={width_id:.6f} (degenerate) "
          f"| invariant width={width_inv:.4f} ci_low={r_inv['ci_low']:.4f} "
          f"(>0, no zero-cross) ... PASS")


def main():
    print("PROBE q174 — propagated Φ-CI width vs coder disagreement (1 - alpha)")
    print("=" * 78)
    instrument_control()
    print("=" * 78)

    # Disagreement-fraction grid chosen so measured alpha lands across ~0.5..1.0.
    fs = [0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.35, 0.50]

    rows_a = sweep(fs, seed=0)
    rows_b = sweep(fs, seed=1)

    print(f"{'f_disagree':>10} | {'alpha_A':>8} {'width_A':>8} {'cross_A':>8}"
          f" || {'alpha_B':>8} {'width_B':>8} {'cross_B':>8}")
    print("-" * 78)
    for f, (aa, wa, ca), (ab, wb, cb) in zip(fs, rows_a, rows_b):
        print(f"{f:10.2f} | {aa:8.3f} {wa:8.4f} {ca:8.2f}"
              f" || {ab:8.3f} {wb:8.4f} {cb:8.2f}")
    print("=" * 78)

    # --- H1: width decreases monotonically with alpha (ensemble A) ---
    alphas_a = np.array([r[0] for r in rows_a])
    widths_a = np.array([r[1] for r in rows_a])
    rho, pval = spearmanr(alphas_a, widths_a)
    h1 = (rho <= -0.9) and (pval < 0.01)
    print(f"H1  Spearman rho(alpha, CI width) = {rho:.4f}, p = {pval:.2e} "
          f"(target rho<=-0.9, p<0.01)")
    print(f"H1 monotone CI width tracks agreement: {'SUPPORTED' if h1 else 'REFUTED'}")

    # --- H2: alpha* threshold where >50% of forms cross zero, stable across ensembles ---
    def alpha_star(rows):
        # highest alpha at which the cross-zero fraction first exceeds 0.5,
        # scanning from low alpha (high dissent) upward.
        ordered = sorted(rows, key=lambda r: r[0])  # ascending alpha
        star = None
        for a, _w, c in ordered:
            if c > 0.5:
                star = a  # keep the largest alpha still above the 0.5 line
        return star

    star_a = alpha_star(rows_a)
    star_b = alpha_star(rows_b)
    if star_a is None or star_b is None:
        h2 = False
        diff = float("nan")
        print(f"H2  alpha*_A = {star_a}, alpha*_B = {star_b} "
              f"(no threshold with >50% zero-crossing in one ensemble)")
    else:
        diff = abs(star_a - star_b)
        h2 = diff <= 0.10
        print(f"H2  alpha*_A = {star_a:.3f}, alpha*_B = {star_b:.3f}, "
              f"|diff| = {diff:.3f} (target <= 0.10)")
    print(f"H2 stable agreement threshold for indeterminacy: "
          f"{'CONFIRMED' if h2 else 'NOT SUPPORTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)


if __name__ == "__main__":
    main()
