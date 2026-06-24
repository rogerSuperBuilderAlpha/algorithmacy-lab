"""q159 — How many trajectory steps does CRQA need before its triadic/dyadic verdict stabilizes
to the exact-Φ verdict, and does the required length depend on Φ magnitude?

QUESTION
    A CRQA reading of a sampled run gives a behavioral triadic/dyadic verdict; the exact major
    complex gives the structural ground truth. The behavioral verdict is read from a finite run, so
    short runs may misclassify a form that a long run would get right. This study sweeps trajectory
    length and asks two things: at what length does the CRQA verdict settle to its long-run reading,
    and does that length depend on the form's exact Φ magnitude.

H1  The CRQA-implied verdict converges to the long-run (reference) verdict by 600 steps for over
    80% of forms, with no further agreement gain past 1200 steps. Null: agreement with the exact-Φ
    verdict keeps rising past 1200 steps, so 600 steps is insufficient.

H2  High-Φ forms need fewer steps to stabilize than low-Φ borderline forms, so the required
    convergence length decreases with Φ magnitude. Null: convergence length is independent of Φ.

METHOD
    Forms: the 3-node forms_library pooled with a random 3-node ensemble (rand_form) and a random
    4-node ensemble (rand_form4). Each form is labeled triadic (core >= 3) or dyadic (core == 2) by
    its exact major-complex core size; sub-dyadic cores are dropped.

    The CRQA-implied verdict at length L thresholds the prominence-spread feature (the count of
    prominent pairwise lead-lag links, coupling breadth). The threshold is fit once at the reference
    length REF_STEPS against the exact-Φ labels (the single split that best separates triadic from
    dyadic by spread), then held fixed and applied at every swept length. Fixing the threshold
    isolates one effect: how trajectory length alone moves the behavioral feature, not how a
    re-fit decision boundary chases it.

    Convergence length of a form is the smallest swept length at which its CRQA verdict equals its
    reference verdict and stays equal for every longer swept length. H1 reads the share of forms
    converged by 600 steps and compares agreement-with-exact-Φ at 600, 1200, and 2400. H2 bins forms
    by exact-Φ tertile and compares the mean convergence length of the top tertile against the
    bottom tertile; SUPPORTED when the top-tertile mean is the smaller.

    Trajectory sampling is seeded per form, so every feature reproduces byte-for-byte; exact Φ is
    deterministic. The control is the worker-system-counterpart triad [x[1], x[0]&x[2], x[1]] with
    labels (W,S,C): verdict triadic, max_phi 2.0, full 3-node core.

    Every number is exact IIT-4.0 Φ on synthetic Boolean coordination forms. This is an in-silico
    study of the CRQA-to-Φ bridge, not a measurement of any field organization. The convergence
    lengths reported are properties of these synthetic runs.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q159_length_to_verdict_curve.probe_length_to_verdict_curve
"""

import os
import random
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.corpus.forms_library import FORMS
from org_frontier.recurrence.crqa_experiments import rand_form
from org_frontier.recurrence.bridge_four import rand_form4, major_complex as major_complex_n
from org_frontier.recurrence.crqa_phi_bridge import crqa_features_at_length, core_label

# ---- fixed configuration (all RNG seeded so the run reproduces byte-for-byte) -------------
STEP_SWEEP = (150, 300, 600, 1200, 2400)   # swept trajectory lengths
REF_STEPS = 2400                            # reference (long-run) length; last of the sweep
SPREAD_IDX = 3                              # index of the 'spread' feature in crqa_features

N_RAND3 = 120          # random 3-node forms drawn
N_RAND4 = 120          # random 4-node forms drawn
RAND3_SEED = 0
RAND4_SEED = 1

CONVERGED_BY = 600     # H1 convergence checkpoint
H1_SHARE_THRESHOLD = 0.80   # H1 requires this share converged by CONVERGED_BY

# trajectory seeds: a distinct fixed seed per pool member, so features are deterministic.
TRAJ_SEED_LIBRARY = 100    # forms_library member i -> 100 + i
TRAJ_SEED_RAND3 = 1000     # random 3-node form k -> 1000 + k
TRAJ_SEED_RAND4 = 2000     # random 4-node form k -> 2000 + k


def _build_pool():
    """The labeled pool: list of (exact_label, phi, traj_seed, rules).

    exact_label: 1 triadic / 0 dyadic from the exact major-complex core size. phi: the exact
    major-complex Φ magnitude. Sub-dyadic cores are dropped.
    """
    pool = []
    for i, f in enumerate(FORMS):
        core, phi = major_complex(f.rules, ("W", "S", "C"))
        lab = core_label(core)
        if lab is not None:
            pool.append((lab, float(phi), TRAJ_SEED_LIBRARY + i, f.rules))
    rng = random.Random(RAND3_SEED)
    for k in range(N_RAND3):
        rules = rand_form(rng)
        core, phi = major_complex_n(rules, 3)
        lab = core_label(core)
        if lab is not None:
            pool.append((lab, float(phi), TRAJ_SEED_RAND3 + k, rules))
    rng = random.Random(RAND4_SEED)
    for k in range(N_RAND4):
        rules = rand_form4(rng)
        core, phi = major_complex_n(rules, 4)
        lab = core_label(core)
        if lab is not None:
            pool.append((lab, float(phi), TRAJ_SEED_RAND4 + k, rules))
    return pool


def _spread_at(rules, seed, steps):
    """The prominence-spread feature for one form at one trajectory length."""
    return crqa_features_at_length(rules, seed, steps)[SPREAD_IDX]


def _fit_threshold(spreads, labels):
    """The spread split that best separates triadic (1) from dyadic (0).

    Triadic forms couple more parties, so they carry more prominent links. A form is called
    triadic when spread >= t. The threshold is the midpoint between adjacent sorted spread values
    that maximizes balanced accuracy against the exact-Φ labels.
    """
    spreads = np.asarray(spreads, dtype=float)
    labels = np.asarray(labels, dtype=int)
    candidates = sorted(set(spreads.tolist()))
    cuts = [candidates[0] - 0.5] + [
        (candidates[i] + candidates[i + 1]) / 2.0 for i in range(len(candidates) - 1)
    ] + [candidates[-1] + 0.5]
    pos = labels == 1
    neg = labels == 0
    best_t, best_score = cuts[0], -1.0
    for t in cuts:
        pred = (spreads >= t).astype(int)
        tpr = (pred[pos] == 1).mean() if pos.any() else 0.0
        tnr = (pred[neg] == 0).mean() if neg.any() else 0.0
        score = 0.5 * (tpr + tnr)
        if score > best_score:
            best_score, best_t = score, t
    return float(best_t), float(best_score)


def instrument_control():
    """Validate the machinery on the known worker-system-counterpart triad."""
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    labels = ("W", "S", "C")
    v = verdict(rules, labels)
    core, phi = major_complex(rules, labels)
    assert v.structure == "triadic", v.structure
    assert abs(v.max_phi - 2.0) < 1e-6, v.max_phi
    assert set(core) == set(labels), core
    assert abs(phi - 2.0) < 1e-6, phi
    assert core_label(core) == 1, core
    # the length-parameterized feature returns a finite spread at each swept length
    for L in STEP_SWEEP:
        s = _spread_at(rules, TRAJ_SEED_LIBRARY, L)
        assert np.isfinite(s) and s >= 0.0, (L, s)
    print(
        f"CONTROL worker-system-counterpart triad: verdict={v.structure}, "
        f"max_phi={v.max_phi:.3f}, mc_phi={phi:.3f}, core={core} (label=triadic): PASS"
    )


def main():
    instrument_control()
    print("=" * 88)
    print("q159 — length to a stable CRQA triadic/dyadic verdict")
    print("=" * 88)

    pool = _build_pool()
    n = len(pool)
    exact_lab = np.array([p[0] for p in pool], dtype=int)
    phi = np.array([p[1] for p in pool], dtype=float)

    # spread of every form at every swept length (deterministic, seeded per form)
    spreads = {L: np.array([_spread_at(p[3], p[2], L) for p in pool], dtype=float)
               for L in STEP_SWEEP}

    # decision threshold fit once at the reference length against the exact-Φ labels
    thr, fit_bal_acc = _fit_threshold(spreads[REF_STEPS], exact_lab)

    # CRQA-implied verdict at each length under the fixed threshold
    crqa_verd = {L: (spreads[L] >= thr).astype(int) for L in STEP_SWEEP}
    ref_verd = crqa_verd[REF_STEPS]

    # agreement of the CRQA verdict with the exact-Φ verdict at each length
    agree_exact = {L: float((crqa_verd[L] == exact_lab).mean()) for L in STEP_SWEEP}

    n_tri = int(exact_lab.sum())
    n_dy = n - n_tri
    print(
        f"pool: n={n} forms ({n_tri} triadic, {n_dy} dyadic); "
        f"Φ range {phi.min():.3f}-{phi.max():.3f}, median {np.median(phi):.3f}"
    )
    print(
        f"spread threshold fit at {REF_STEPS} steps: spread >= {thr:.1f} => triadic "
        f"(balanced accuracy {fit_bal_acc:.4f})"
    )
    print("-" * 88)

    # ---- length curve: agreement with exact-Φ, and stability vs the reference verdict ----
    print(f"  {'steps':<10}{'agree exact-Φ':<18}{'matches ref verdict':<22}")
    for L in STEP_SWEEP:
        match_ref = float((crqa_verd[L] == ref_verd).mean())
        print(f"  {L:<10}{agree_exact[L]:<18.4f}{match_ref:<22.4f}")
    print("-" * 88)

    # ---- convergence length per form ------------------------------------------------------
    # smallest swept length at which a form's verdict equals its reference verdict AND stays
    # equal at every longer swept length.
    conv_len = np.full(n, REF_STEPS, dtype=int)
    for f in range(n):
        for li, L in enumerate(STEP_SWEEP):
            tail = STEP_SWEEP[li:]
            if all(crqa_verd[Lt][f] == ref_verd[f] for Lt in tail):
                conv_len[f] = L
                break

    share_by = float((conv_len <= CONVERGED_BY).mean())

    print(f"convergence length (steps to a verdict that stays at the reference reading):")
    for L in STEP_SWEEP:
        cnt = int((conv_len == L).sum())
        print(f"  {'converged at ' + str(L):<24}{cnt:>4}  ({cnt / n:6.2%})")
    print(f"  {'share converged by ' + str(CONVERGED_BY):<24}{share_by:6.2%}")
    print("-" * 88)

    # ---- H2: convergence length by exact-Φ tertile ---------------------------------------
    # The Φ distribution piles up at the ceiling (many forms share Φ=2.0), so a value-quantile cut
    # leaves bins empty. Binning by rank with ties broken by ascending Φ then form index gives three
    # near-equal bins regardless of ties; the split is deterministic.
    order = np.lexsort((np.arange(n), phi))   # ascending Φ, then form index
    rank = np.empty(n, dtype=int)
    rank[order] = np.arange(n)
    lo_bin = rank < n // 3
    hi_bin = rank >= n - n // 3
    mid_bin = ~(lo_bin | hi_bin)
    lo_mean = float(conv_len[lo_bin].mean()) if lo_bin.any() else float("nan")
    mid_mean = float(conv_len[mid_bin].mean()) if mid_bin.any() else float("nan")
    hi_mean = float(conv_len[hi_bin].mean()) if hi_bin.any() else float("nan")
    lo_phi_hi = float(phi[lo_bin].max()) if lo_bin.any() else float("nan")
    hi_phi_lo = float(phi[hi_bin].min()) if hi_bin.any() else float("nan")

    print(
        f"convergence length by exact-Φ tertile "
        f"(rank split: low Φ<= {lo_phi_hi:.3f}, high Φ>= {hi_phi_lo:.3f}):"
    )
    print(f"  {'Φ tertile':<16}{'n':>5}{'mean conv. length':>22}")
    print(f"  {'low':<16}{int(lo_bin.sum()):>5}{lo_mean:>22.1f}")
    print(f"  {'mid':<16}{int(mid_bin.sum()):>5}{mid_mean:>22.1f}")
    print(f"  {'high':<16}{int(hi_bin.sum()):>5}{hi_mean:>22.1f}")
    print("=" * 88)

    # ---- H1 -------------------------------------------------------------------------------
    no_gain_past_1200 = agree_exact[2400] <= agree_exact[1200] + 1e-9
    h1_supported = (share_by >= H1_SHARE_THRESHOLD) and no_gain_past_1200
    print(
        f"H1 summary: {share_by:.2%} of forms converged by {CONVERGED_BY} steps "
        f"(threshold {H1_SHARE_THRESHOLD:.0%}); "
        f"agreement at 1200={agree_exact[1200]:.4f}, at 2400={agree_exact[2400]:.4f} "
        f"({'no gain' if no_gain_past_1200 else 'still rising'} past 1200)."
    )
    # ---- H2 -------------------------------------------------------------------------------
    h2_supported = hi_mean < lo_mean
    print(
        f"H2 summary: mean convergence length low-Φ={lo_mean:.1f}, high-Φ={hi_mean:.1f} "
        f"(high {'<' if hi_mean < lo_mean else '>='} low)."
    )
    print("=" * 88)

    print(
        f"H1 CRQA verdict converges by {CONVERGED_BY} steps for >{H1_SHARE_THRESHOLD:.0%} of "
        f"forms with no gain past 1200: " + ("SUPPORTED" if h1_supported else "REFUTED")
    )
    print(
        "H2 required convergence length decreases with Φ magnitude: "
        + ("SUPPORTED" if h2_supported else "REFUTED")
    )


if __name__ == "__main__":
    main()
