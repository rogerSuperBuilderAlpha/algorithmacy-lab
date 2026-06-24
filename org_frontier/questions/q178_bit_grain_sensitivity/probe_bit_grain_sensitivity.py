"""q178 — Does the bit cut on a graded coded action change the Φ verdict, and does coder
threshold disagreement widen the Φ CI?

Question: A coded account often records an action on a graded scale (none / partial / full),
then collapses it to a single bit before the rule set is built. The cut point of that collapse
is a coding choice. This probe asks whether moving the cut changes the structural Φ verdict
(dyadic <-> triadic), and whether two coders who place the cut differently produce a wider Φ
confidence interval than two coders who place it the same.

H1 (fixed before computing): For synthetic accounts whose underlying counterpart action is
3-valued, the binarization threshold changes the verdict (dyadic <-> triadic) for > 20% of
accounts.
    H1-null: < 5% of accounts flip across all thresholds, so the bit cut is verdict-neutral.

H2 (fixed before computing): When two coders place the binary threshold differently, the
propagated Φ CI width on threshold-sensitive accounts exceeds the same-threshold (single-cut)
CI width by a factor > 2.
    H2-null: the ratio is <= 1.2, so threshold disagreement contributes negligibly to verdict
    uncertainty.

Method: each synthetic account fixes a graded counterpart-action level g in {0, 1, 2}. A coder's
threshold t in {1, 2} collapses g to a bit b = 1[g >= t]. When b = 1 the counterpart C is wired
into the system rule (the worker-system-counterpart triad [x1, x0 & x2, x1]); when b = 0 the
counterpart drops out and the account reads as a dyad [x1, x0, x1]. rule_to_phi reads each
collapsed rule set to its exact IIT-4.0 Φ verdict. H1 sweeps both thresholds over a seeded panel
of accounts and counts verdict flips. H2 builds, for each threshold-sensitive account, a
two-coder split panel (one cut at t=1, one at t=2) and a same-threshold panel (both at the same
cut), and compares the phi_ci widths via the q173 bridge. Controls: monotone threshold-invariant
accounts (g in {0, 2}) must never flip; identical-threshold coders must give the single-cut CI
width.

Run: source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
  python -m org_frontier.questions.q178_bit_grain_sensitivity.probe_bit_grain_sensitivity
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import verdict
from org_frontier.field.rule_to_phi import rule_to_phi, phi_ci

# Labels for the worker-system-counterpart triad.
LABELS = ("W", "S", "C")
FAITHFUL_TRIAD = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

# Graded action levels and the two threshold cuts a coder may place.
GRADES = (0, 1, 2)
THRESHOLDS = (1, 2)


def collapse_to_rules(grade, threshold):
    """Collapse a graded counterpart action to a bit at a cut, then build the rule set.

    bit b = 1[grade >= threshold]. b = 1 wires the counterpart C into the system rule (the
    worker-system-counterpart triad); b = 0 drops C and the account reads as a dyad."""
    bit = 1 if grade >= threshold else 0
    if bit:
        return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    return [lambda x: x[1], lambda x: x[0], lambda x: x[1]]


def phi_at(grade, threshold):
    return rule_to_phi(collapse_to_rules(grade, threshold), labels=LABELS)


def main():
    rng = np.random.default_rng(0)

    # ---- INSTRUMENT CONTROL ---------------------------------------------------------------
    v = verdict(FAITHFUL_TRIAD, LABELS)
    assert v.structure == "triadic", f"control structure {v.structure!r}"
    assert abs(v.max_phi - 2.0) < 1e-9, f"control max_phi {v.max_phi}"
    print(f"CONTROL faithful triad reads '{v.structure}' max_phi={v.max_phi:.6f}: PASS")
    print()

    # ---- THRESHOLD-INVARIANCE CONTROL: monotone accounts (g in {0,2}) must not flip --------
    invariant_ok = True
    for g in (0, 2):
        verds = {phi_at(g, t)["structure"] for t in THRESHOLDS}
        if len(verds) != 1:
            invariant_ok = False
    print(f"CONTROL monotone accounts (g in {{0,2}}) are threshold-invariant: "
          f"{'PASS' if invariant_ok else 'FAIL'}")
    print()

    # ---- ACCOUNT PANEL: seeded mix of graded levels ---------------------------------------
    # Draw 200 synthetic accounts with graded counterpart-action levels. The mix is deliberately
    # balanced so the flip rate reflects the share of boundary-grade (g=1) accounts, not a
    # contrived majority.
    n_accounts = 200
    grades = rng.integers(0, 3, size=n_accounts)  # uniform over {0,1,2}

    print("Per-grade verdict by threshold")
    print(f"{'grade':>6}{'t=1 verdict':>14}{'t=1 Φ':>9}{'t=2 verdict':>14}{'t=2 Φ':>9}{'flips':>7}")
    grade_flips = {}
    for g in GRADES:
        a = phi_at(g, 1)
        b = phi_at(g, 2)
        flips = a["structure"] != b["structure"]
        grade_flips[g] = flips
        print(f"{g:>6}{a['structure']:>14}{a['max_phi']:>9.3f}"
              f"{b['structure']:>14}{b['max_phi']:>9.3f}{str(flips):>7}")
    print()

    # ---- H1: verdict-flip rate across the threshold sweep ---------------------------------
    n_flip = int(sum(grade_flips[int(g)] for g in grades))
    flip_rate = n_flip / n_accounts
    sensitive_grades = [g for g in GRADES if grade_flips[g]]

    print("H1  threshold-induced verdict flips over the account panel")
    print(f"  accounts                 = {n_accounts}")
    print(f"  threshold-sensitive grade(s) = {sensitive_grades}")
    print(f"  accounts that flip       = {n_flip}")
    print(f"  flip rate                = {flip_rate:.4f}")
    print()

    # ---- H2: split-coder vs same-coder CI width on a threshold-sensitive account -----------
    # Threshold-sensitive account: g = 1. The bit cut decides the verdict (t=1 -> triadic Φ=2.0,
    # t=2 -> dyadic Φ=0.0). Two coder panels of equal size read this one account.
    #
    # Split panel: half the coders cut at t=1, half at t=2, so the panel's Φ readings split
    # between 2.0 and 0.0. Same-threshold panel: every coder cuts at t=1, so the readings cluster
    # at 2.0. Both panels carry the same small seeded reading jitter (ordinary within-coder noise
    # on a Φ read), so the same-threshold panel is a non-degenerate single-cut baseline and the
    # width ratio is well-defined. The active-bit coding matrix (the bit C contributes) records
    # each coder's cut decision: split = [1...1, 0...0], same = all 1.
    g_sens = 1
    phi_t1 = phi_at(g_sens, 1)["max_phi"]
    phi_t2 = phi_at(g_sens, 2)["max_phi"]

    n_coders = 8
    half = n_coders // 2
    jitter_sd = 0.02  # small within-coder reading noise on a Φ read

    j_split = rng.normal(0.0, jitter_sd, size=n_coders)
    j_same = rng.normal(0.0, jitter_sd, size=n_coders)
    split_phis = ([phi_t1 + j_split[k] for k in range(half)]
                  + [phi_t2 + j_split[k] for k in range(half, n_coders)])
    same_phis = [phi_t1 + j_same[k] for k in range(n_coders)]

    split_codings = np.array([[1]] * half + [[0]] * (n_coders - half))
    same_codings = np.array([[1]] * n_coders)

    split = phi_ci(split_phis, coder_codings=split_codings, rng=np.random.default_rng(1))
    same = phi_ci(same_phis, coder_codings=same_codings, rng=np.random.default_rng(2))

    split_width = split["ci_high"] - split["ci_low"]
    same_width = same["ci_high"] - same["ci_low"]
    ratio = float("inf") if same_width < 1e-12 else split_width / same_width

    split_ci = f"[{split['ci_low']:.4f}, {split['ci_high']:.4f}]"
    same_ci = f"[{same['ci_low']:.4f}, {same['ci_high']:.4f}]"
    print(f"H2  CI width: split-threshold coders vs same-threshold coders "
          f"(g=1 account, {n_coders} coders)")
    print(f"{'panel':<24}{'point Φ':>10}{'alpha':>8}{'CI':>24}{'width':>10}")
    print(f"{'split (t=1 / t=2)':<24}{split['phi_point']:>10.4f}{split['alpha']:>8.3f}"
          f"{split_ci:>24}{split_width:>10.4f}")
    print(f"{'same (all t=1)':<24}{same['phi_point']:>10.4f}{same['alpha']:>8.3f}"
          f"{same_ci:>24}{same_width:>10.4f}")
    print(f"  width ratio (split / same) = {ratio:.4f}")
    print()

    # ---- VERDICTS -------------------------------------------------------------------------
    h1_supported = flip_rate > 0.20
    h1_null = flip_rate < 0.05
    if h1_supported:
        h1_line = "SUPPORTED"
    elif h1_null:
        h1_line = "REFUTED (null: bit cut verdict-neutral)"
    else:
        h1_line = "REFUTED (intermediate: between null and H1 thresholds)"

    # H2: split-panel CI width must exceed the same-threshold (single-cut) width by factor > 2.
    h2_supported = (split_width > 1e-9) and (ratio > 2.0)
    h2_null = ratio <= 1.2
    if h2_supported:
        h2_line = "SUPPORTED"
    elif h2_null:
        h2_line = "NOT SUPPORTED (null: threshold disagreement negligible)"
    else:
        h2_line = "NOT SUPPORTED (intermediate)"

    print(f"H1 threshold flips verdict for >20% of accounts (flip rate {flip_rate:.4f}): {h1_line}")
    print(f"H2 split-threshold CI width exceeds same-threshold width by >2x "
          f"(ratio {ratio:.4f}): {h2_line}")


if __name__ == "__main__":
    main()
