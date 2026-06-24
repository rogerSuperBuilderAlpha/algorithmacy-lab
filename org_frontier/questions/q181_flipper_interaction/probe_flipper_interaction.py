"""q181 — Two flippers at once: do substitutability and pass-through compose additively, or does one flipper mask the other in the Φ CI?

QUESTION
    A coded account of a worker-system-counterpart coordination names a Boolean
    determination rule for each party. Two coding choices each flip a triadic verdict to
    dyadic on their own. The SUBSTITUTABILITY flipper re-reads the single irreplaceable
    worker as one slot in an interchangeable pool (W becomes D1|...|Dk). The PASS-THROUGH
    flipper switches the system from commit (S = W & R, act only when the worker decision
    and counterpart request both hold) to relay (S = W, pass the worker decision through).
    When both flippers are coded at once, do their verdict effects compose additively, or
    does one flipper mask the other in the Φ confidence interval?

H1 (fixed before computing)
    Applying substitutability and pass-through together yields the same dyadic verdict as
    either alone: no triadic re-emergence. The flippers do not interact to restore
    irreducibility.
    NULL: at least one combined account reads triadic while each single flipper reads
    dyadic, so the flippers interact non-trivially.

H2 (fixed before computing)
    In the contested case, coders split on each flipper independently. The joint Φ CI
    (both flippers contested) equals the union of the two single-flipper CIs to within
    10% of width: disagreements compose.
    NULL: the joint CI width exceeds the union width by > 25%, so flipper disagreements
    amplify each other.

METHOD
    Reuse the field bridge org_frontier/field/rule_to_phi.py (study 1 of the field line):
    rule_to_phi encodes per-party rules into a TPM and reads the exact IIT-4.0 Φ verdict;
    phi_ci propagates coder disagreement into a bootstrap-t Φ interval. Φ is not
    reimplemented.
    The account is parameterised by pool size k (k = 1 is the specific irreplaceable
    worker; k >= 2 is the substitutable pool) and system mode (commit vs relay). The 2x2
    design over {specific, pooled} x {commit, relay} gives the no-flipper baseline, each
    single flipper, and the double flipper. H1 reads the verdict of every cell.
    For H2, each coder independently decides whether to apply each flipper. A coder's Φ
    reading is the verdict of the cell their two decisions select. The single-flipper
    panels contest one flipper (the other off); the joint panel contests both. Each
    panel's CI is read through phi_ci. The union CI is the envelope of the two
    single-flipper CIs; the test compares the joint CI width to the union width.
    CONTROLS: the faithful triad reads triadic with max Φ = 2.0 (no-flipper baseline);
    the double flipper must read dyadic; and a spectator-only condition (a node that
    reads the system but feeds nothing back) leaves the major-complex triad at Φ = 2.0,
    isolating that masking requires a flipper to touch the cycle rather than merely
    observe it.
    All inputs are synthetic coded rule sets, not measured worker states.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
      python -m org_frontier.questions.q181_flipper_interaction.probe_flipper_interaction
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import PHI_EPS
from org_frontier.field.rule_to_phi import rule_to_phi, phi_ci
from org_frontier.probes.lib import major_complex

BASELINE_PHI = 2.0


# --------------------------------------------------------------------------------------
# The 2x2 account: pool size k x system mode (commit / relay)
# --------------------------------------------------------------------------------------

def account(k, system="commit"):
    """Coded rule set parameterised by the two flippers.

    Nodes (D1, ..., Dk, S, R). k = 1 is the specific irreplaceable worker (no
    substitutability flip); k >= 2 is the substitutable pool (substitutability ON). The
    system rule commits (S = OR(D) & R) or relays (S = OR(D), counterpart ignored); relay
    is the pass-through flip. R reads off S; each pool member reads off S. k = 1, commit
    is the faithful worker-system-counterpart triad.
    """
    s_idx = k
    r_idx = k + 1
    rules = [(lambda x, _s=s_idx: x[_s]) for _ in range(k)]

    def s_rule(x, _k=k, _r=r_idx, _mode=system):
        orv = 0
        for i in range(_k):
            orv |= x[i]
        return (orv & x[_r]) if _mode == "commit" else orv

    rules.append(s_rule)
    rules.append(lambda x, _s=s_idx: x[_s])
    labels = tuple(f"D{i + 1}" for i in range(k)) + ("S", "R")
    return rules, labels


def cell_phi(k, system):
    return rule_to_phi(*account(k, system))


# --------------------------------------------------------------------------------------
# INSTRUMENT CONTROL
# --------------------------------------------------------------------------------------

def control():
    # No-flipper baseline: faithful triad reads triadic at max Φ = 2.0.
    base = cell_phi(1, "commit")
    assert base["structure"] == "triadic" and abs(base["max_phi"] - BASELINE_PHI) < 1e-9, base

    # Double flipper must stay dyadic.
    dbl = cell_phi(2, "relay")
    assert dbl["structure"] == "dyadic" and dbl["max_phi"] < PHI_EPS, dbl

    # Spectator-only condition: a node X reads S but feeds nothing back. The whole-system
    # verdict drops (X is reducible), but the major complex stays the triad at Φ = 2.0,
    # so a pure spectator does not flip the irreducible core.
    spec_rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]]
    spec_labels = ("W", "S", "C", "X")
    core, core_phi = major_complex(spec_rules, spec_labels)
    assert core == ("W", "S", "C") and abs(core_phi - BASELINE_PHI) < 1e-9, (core, core_phi)

    print("CONTROL no-flipper triad triadic@2.0, double-flipper dyadic@0.0, "
          "spectator-only keeps major complex (W,S,C)@2.0 ... PASS")


# --------------------------------------------------------------------------------------
# H1 — does the double flipper restore irreducibility?
# --------------------------------------------------------------------------------------

def h1_grid(k_pool=2):
    """Read the verdict of every cell of the {specific, pooled} x {commit, relay} grid."""
    cells = [
        ("none", 1, "commit"),
        ("substitutability", k_pool, "commit"),
        ("pass-through", 1, "relay"),
        ("both", k_pool, "relay"),
    ]
    rows = []
    for name, k, mode in cells:
        v = cell_phi(k, mode)
        rows.append((name, k, mode, v["structure"], v["max_phi"]))
    return rows


# --------------------------------------------------------------------------------------
# H2 — do flipper disagreements compose, or amplify?
# --------------------------------------------------------------------------------------

def coder_phi(apply_sub, apply_pass, k_pool=2):
    """Φ a coder reads given their two independent flipper decisions."""
    k = k_pool if apply_sub else 1
    mode = "relay" if apply_pass else "commit"
    return cell_phi(k, mode)["max_phi"]


def panel_ci(contest_sub, contest_pass, n_coders=24, k_pool=2, seed=0):
    """CI from a coder panel.

    `contest_sub` / `contest_pass` mark which flippers are contested. A contested flipper
    is applied by a randomly drawn subset of coders (split in the genuine-contest band); a
    non-contested flipper is off for everyone. Each coder's Φ is the verdict their two
    decisions select; phi_ci propagates the panel disagreement into a bootstrap-t CI.
    """
    rng = np.random.default_rng(seed)
    # Draw a contest split for each contested flipper, in the genuine-contest band.
    frac_sub = rng.uniform(0.3, 0.7) if contest_sub else 0.0
    frac_pass = rng.uniform(0.3, 0.7) if contest_pass else 0.0
    apply_sub = rng.random(n_coders) < frac_sub
    apply_pass = rng.random(n_coders) < frac_pass
    phis = np.array([coder_phi(bool(a), bool(b), k_pool)
                     for a, b in zip(apply_sub, apply_pass)], dtype=float)
    codings = np.stack([apply_sub.astype(int), apply_pass.astype(int)], axis=1)
    out = phi_ci(phis, coder_codings=codings, n_boot=600, ci=0.95,
                 rng=np.random.default_rng(seed + 100))
    return out, phis


def width(ci):
    return ci["ci_high"] - ci["ci_low"]


def h2_compose(n_coders=24, k_pool=2):
    """Single-flipper CIs vs joint CI vs the union of the singles."""
    sub_ci, sub_phis = panel_ci(True, False, n_coders, k_pool, seed=1)
    pass_ci, pass_phis = panel_ci(False, True, n_coders, k_pool, seed=2)
    joint_ci, joint_phis = panel_ci(True, True, n_coders, k_pool, seed=3)

    union_low = min(sub_ci["ci_low"], pass_ci["ci_low"])
    union_high = max(sub_ci["ci_high"], pass_ci["ci_high"])
    union_width = union_high - union_low

    joint_width = width(joint_ci)
    rel_gap = (joint_width - union_width) / union_width if union_width > PHI_EPS else 0.0
    return {
        "sub_ci": sub_ci, "pass_ci": pass_ci, "joint_ci": joint_ci,
        "union_low": union_low, "union_high": union_high, "union_width": union_width,
        "joint_width": joint_width, "rel_gap": rel_gap,
    }


# --------------------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------------------

def main():
    control()
    print()

    rows = h1_grid()
    print("H1  2x2 flipper grid (substitutability x pass-through), pool size k=2")
    print(f"    {'flippers':18} {'k':>2} {'system':>7}  {'structure':9}  max_phi")
    triadic_combined = []
    for name, k, mode, struct, phi in rows:
        print(f"    {name:18} {k:>2} {mode:>7}  {struct:9}  {phi:.6f}")
        if name in ("substitutability", "pass-through", "both") and struct == "triadic":
            triadic_combined.append(name)
    base_struct = rows[0][3]
    singles_dyadic = all(r[3] == "dyadic" for r in rows[1:3])
    both_struct = rows[3][3]
    print()

    res = h2_compose()
    print("H2  contested-case CI composition (coders split on each flipper independently)")
    print(f"    {'panel':14} {'ci_low':>9} {'ci_high':>9} {'width':>9}  {'alpha':>6}")
    for tag, ci in (("substitut.", res["sub_ci"]), ("pass-through", res["pass_ci"]),
                    ("joint", res["joint_ci"])):
        print(f"    {tag:14} {ci['ci_low']:9.4f} {ci['ci_high']:9.4f} "
              f"{width(ci):9.4f}  {ci['alpha']:6.3f}")
    print(f"    union of singles: [{res['union_low']:.4f}, {res['union_high']:.4f}]  "
          f"width {res['union_width']:.4f}")
    print(f"    joint width {res['joint_width']:.4f}  vs union width {res['union_width']:.4f}  "
          f"relative gap {res['rel_gap']:+.3f}")
    print()

    # H1 verdict: SUPPORTED if the baseline is triadic, each single flipper is dyadic, the
    # double flipper is dyadic, and no combined account re-reads triadic.
    h1_supported = (base_struct == "triadic" and singles_dyadic
                    and both_struct == "dyadic" and not triadic_combined)
    print(f"H1 flippers do not interact to restore irreducibility (no triadic re-emergence): "
          f"{'SUPPORTED' if h1_supported else 'REFUTED'}")
    if not h1_supported and triadic_combined:
        print(f"   NULL holds: combined account(s) {triadic_combined} read triadic while each "
              f"single flipper reads dyadic.")

    # H2 verdict: SUPPORTED if the joint CI width is within 10% of the union width;
    # NOT SUPPORTED if it exceeds the union by > 25% (amplification).
    within_10 = abs(res["rel_gap"]) <= 0.10
    amplifies = res["rel_gap"] > 0.25
    h2_word = "SUPPORTED" if within_10 else "NOT SUPPORTED"
    print(f"H2 flipper disagreements compose (joint CI = union to within 10% width): "
          f"{h2_word}")
    if not within_10:
        if amplifies:
            kind = f"amplify (joint exceeds union by {res['rel_gap']:+.1%}, over the 25% null)"
        elif res["rel_gap"] > 0.10:
            kind = f"widen modestly (joint exceeds union by {res['rel_gap']:+.1%}, under the 25% null)"
        else:
            kind = (f"contract (joint is {-res['rel_gap']:.1%} narrower than the union); "
                    f"the amplification null also fails")
        print(f"   joint vs union relative gap {res['rel_gap']:+.3f}: disagreements {kind}.")


if __name__ == "__main__":
    main()
