"""Probe 333 (q179) — does the update time-grain change the Φ verdict, and is grain-sensitivity
predictable from rule structure before computing Φ?

QUESTION
    A coded account fixes an update time-grain: one coded step is one tick, or several real
    events are coarse-grained into one macro-transition. The grain is a coding choice. Does it
    change the dyadic/triadic verdict, and can the bridge expose grain as a choice with its own CI?

H1 (fixed before computing)
    Coarse-graining a synthetic account that is triadic per-tick into a 2-tick macro-transition
    flips a measurable fraction (>15%) of accounts to dyadic. NULL: <5% flip, so the verdict is
    invariant to the time-grain choice.

H2 (fixed before computing)
    When coders disagree on the time-grain (per-tick vs coarse), the verdict is indeterminate
    (the Φ confidence interval crosses 0) for the grain-sensitive subset, and that subset is
    identifiable a priori from rule structure (orbit folding / attractor period). NULL:
    grain-sensitivity is not predictable from structure (AUC <= 0.6) so it cannot be flagged
    before computing Φ.

METHOD
    Reuse the bridge org_frontier.field.rule_to_phi (rule-set -> TPM -> exact-Φ verdict, with
    coder-disagreement -> Φ CI). Build a seeded ensemble of synthetic coded accounts that read
    triadic per tick. For each, compose the rule-TPM with itself for the 2-tick macro grain and
    re-read the verdict (per-tick vs coarse). H1 = fraction flipping triadic->dyadic. For each
    account form a two-coder panel {per-tick reading, coarse reading} and run the bridge CI; the
    grain-sensitive subset (the flippers) is the one whose CI crosses 0. A purely structural
    predictor (image-collapse under 2-step + even attractor period, computed from the orbit, no
    Φ) is scored by AUC against the flip label. CONTROL = a memoryless feedforward triple
    (grain-invariant) vs the cyclic faithful triad (known grain-sensitive).

    All inputs are synthetic coded rule sets. No worker state is measured. The result is an
    in-silico property of the coding scheme and the grain choice, not an empirical finding about
    any organization.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q179_time_grain_sensitivity.probe_time_grain_sensitivity
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify, classify_rules, cm_from_rules
from org_frontier.field.rule_to_phi import rule_to_phi, phi_ci

LABELS = ("W", "S", "C")
N = 3
PHI_EPS = 1e-9

# Hypothesis thresholds (fixed before computing).
H1_FLIP = 0.15          # >15% flip -> grain changes the verdict
H1_NULL = 0.05          # <5% flip -> verdict invariant
H2_AUC = 0.6            # structural predictor must clear this to be usable a priori
N_ACCOUNTS = 80         # ensemble size
SEED = 0


# ----------------------------------------------------------------------------------------
# Time-grain machinery: compose the rule-TPM with itself for a k-tick macro-transition
# ----------------------------------------------------------------------------------------

def succ_state(rules, s, n=N):
    """Little-endian successor state index under one tick of the coded rules."""
    b = tuple((s >> i) & 1 for i in range(n))
    o = tuple(int(rules[j](b)) for j in range(n))
    return sum(o[j] << j for j in range(n))


def compose_tpm(rules, n=N, k=2):
    """State-by-node TPM and connectivity for the k-tick macro-transition (rule-TPM composed
    with itself k times). The deterministic core of coarse-graining the time-grain."""
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        cur = s
        for _ in range(k):
            cur = succ_state(rules, cur, n)
        b = tuple((cur >> i) & 1 for i in range(n))
        for j in range(n):
            tpm[s, j] = float(b[j])
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9 for s in range(2 ** n)):
                cm[i, j] = 1
    return tpm, cm


def coarse_verdict(rules, k=2):
    """rule_to_phi-style verdict at the k-tick macro grain (verdict + max Φ)."""
    tpm, cm = compose_tpm(rules, k=k)
    v = classify(tpm, cm, labels=LABELS)
    return v.structure, float(v.max_phi)


# ----------------------------------------------------------------------------------------
# A priori structural predictor of grain-sensitivity (no Φ; from the orbit and connectivity)
# ----------------------------------------------------------------------------------------

def structural_score(rules, n=N):
    """Structural grain-sensitivity score from the rule's state-transition orbit, computed
    without Φ. Two ingredients:
      - image collapse: how many distinct one-step images vanish under the 2-step map (the
        2-tick grain folding the dynamics);
      - even attractor period: an attractor whose period is even desynchronizes under a 2-tick
        stride.
    Higher score = more grain-sensitive. Returned with the two raw parts for the table."""
    img1 = set(succ_state(rules, s, n) for s in range(2 ** n))
    img2 = set()
    for s in range(2 ** n):
        c = s
        for _ in range(2):
            c = succ_state(rules, c, n)
        img2.add(c)
    collapse = len(img1) - len(img2)
    any_even = False
    for s0 in range(2 ** n):
        seen = {}
        c = s0
        t = 0
        while c not in seen:
            seen[c] = t
            c = succ_state(rules, c, n)
            t += 1
        period = t - seen[c]
        if period >= 2 and period % 2 == 0:
            any_even = True
    score = float(collapse) + 4.0 * float(any_even)
    return score, collapse, int(any_even)


def auc(score, y):
    """Rank AUC (probability a positive outranks a negative; ties 0.5)."""
    score = np.asarray(score, dtype=float)
    y = np.asarray(y, dtype=int)
    pos = score[y == 1]
    neg = score[y == 0]
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    c = sum((p > q) + 0.5 * (p == q) for p in pos for q in neg)
    return float(c) / (len(pos) * len(neg))


# ----------------------------------------------------------------------------------------
# Ensemble of synthetic coded accounts that read triadic per tick
# ----------------------------------------------------------------------------------------

def rand_rule(rng):
    """One per-party Boolean determination rule: a random truth table over the 3-party state."""
    table = rng.integers(0, 2, size=2 ** N)
    return lambda x, t=table: int(t[x[0] | (x[1] << 1) | (x[2] << 2)])


def triadic_ensemble(n_accounts, rng):
    """Draw seeded random 3-party coded accounts, keep those triadic at the per-tick grain."""
    out = []
    tries = 0
    while len(out) < n_accounts and tries < 200 * n_accounts:
        tries += 1
        r = [rand_rule(rng) for _ in range(N)]
        if classify_rules(r, labels=LABELS).structure == "triadic":
            out.append(r)
    return out, tries


# ----------------------------------------------------------------------------------------
# Instrument control
# ----------------------------------------------------------------------------------------

def instrument_control():
    """Validate the machinery on known cases.

    1. The faithful cyclic triad reads triadic with max Φ = 2.0 at the per-tick grain.
    2. That cyclic triad is grain-sensitive: the 2-tick macro grain reads dyadic (flips).
    3. A memoryless feedforward triple is grain-invariant: dyadic at both grains.
    4. The structural predictor ranks the cyclic triad above the feedforward one.
    """
    cyclic = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    feedforward = [lambda x: 0, lambda x: x[0], lambda x: x[1]]

    v = rule_to_phi(cyclic, labels=LABELS)
    assert v["structure"] == "triadic", v
    assert abs(v["max_phi"] - 2.0) < 1e-6, v

    cyc_coarse, cyc_phi2 = coarse_verdict(cyclic, k=2)
    assert cyc_coarse == "dyadic", (cyc_coarse, cyc_phi2)

    ff_tick = classify_rules(feedforward, labels=LABELS).structure
    ff_coarse, _ = coarse_verdict(feedforward, k=2)
    assert ff_tick == "dyadic" and ff_coarse == "dyadic", (ff_tick, ff_coarse)

    sc_cyc, _, _ = structural_score(cyclic)
    sc_ff, _, _ = structural_score(feedforward)
    assert sc_cyc > sc_ff, (sc_cyc, sc_ff)

    print(f"CONTROL faithful triad: triadic, max_phi={v['max_phi']:.4f}; "
          f"cyclic 2-tick={cyc_coarse}; feedforward grain-invariant ({ff_tick}/{ff_coarse}); "
          f"struct score cyclic={sc_cyc:.1f} > feedforward={sc_ff:.1f} ... PASS")


# ----------------------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------------------

def main():
    print("=" * 78)
    print("PROBE 333 (q179) — update time-grain sensitivity of the Φ verdict")
    print("=" * 78)

    instrument_control()

    rng = np.random.default_rng(SEED)
    accounts, tries = triadic_ensemble(N_ACCOUNTS, rng)
    print(f"\nEnsemble: {len(accounts)} synthetic coded accounts triadic at the per-tick grain "
          f"(seed={SEED}, drawn in {tries} tries). SYNTHETIC coded data.")

    # Per account: per-tick verdict, 2-tick macro verdict, flip label, structural score,
    # and the coder-disagreement Φ CI over a grain panel. The panel models a six-coder team in
    # which a fraction code the account per-tick and the rest coarse-grain to 2 ticks; the bridge
    # propagates that disagreement into a Φ CI. The verdict is INDETERMINATE when the panel
    # straddles the dyadic/triadic boundary, i.e. the bridge CI's lower bound sits at the dyadic
    # floor (some coder reads Φ = 0 while others read Φ > 0). This is exactly what a grain flip
    # produces: per-tick coders read triadic, coarse coders read dyadic.
    N_CODERS = 6
    N_COARSE = 3  # half the panel coarse-grain; a 3/3 split is the maximal-disagreement case
    rows = []
    flips = 0
    scores = []
    labels = []
    n_indet_flip = 0
    n_indet_noflip = 0
    ci_rng = np.random.default_rng(SEED)
    for r in accounts:
        v1 = rule_to_phi(r, labels=LABELS)
        struct2, phi2 = coarse_verdict(r, k=2)
        flip = (struct2 == "dyadic")
        flips += int(flip)
        score, collapse, even = structural_score(r)
        scores.append(score)
        labels.append(int(flip))
        # Six-coder grain panel: N_COARSE coders coarse-grain (read phi2), the rest per-tick.
        panel = [v1["max_phi"]] * (N_CODERS - N_COARSE) + [phi2] * N_COARSE
        ci = phi_ci(panel, n_boot=400, rng=ci_rng)
        # Indeterminate verdict: the panel spans the dyadic/triadic boundary (a Φ ≈ 0 reading is
        # present, so the CI's lower bound rests on the dyadic floor).
        indeterminate = min(panel) <= PHI_EPS
        if flip:
            n_indet_flip += int(indeterminate)
        else:
            n_indet_noflip += int(indeterminate)
        rows.append((v1["structure"], v1["max_phi"], struct2, phi2, flip,
                     collapse, even, ci["ci_low"], ci["ci_high"]))

    flip_frac = flips / len(accounts)
    pred_auc = auc(scores, labels)

    # Fraction of the grain-sensitive (flipping) subset whose panel verdict is indeterminate,
    # and the false-positive rate on the grain-invariant subset.
    frac_flip_indeterminate = (n_indet_flip / flips) if flips else float("nan")
    frac_noflip_indeterminate = (
        n_indet_noflip / (len(accounts) - flips)) if (len(accounts) - flips) else float("nan")

    # ---- table ----
    print("\nPer-account (first 12 of the ensemble):")
    print(f"  {'tick':<8}{'Φ_tick':>8}  {'2-tick':<8}{'Φ_2tk':>8}  {'flip':>5}  "
          f"{'collapse':>9}{'even':>5}  {'CI_low':>8}{'CI_high':>8}")
    for row in rows[:12]:
        s1, p1, s2, p2, fl, col, ev, lo, hi = row
        print(f"  {s1:<8}{p1:>8.3f}  {s2:<8}{p2:>8.3f}  {str(fl):>5}  "
              f"{col:>9}{ev:>5}  {lo:>8.3f}{hi:>8.3f}")

    print("\n" + "-" * 78)
    print("SUMMARY (synthetic coded data)")
    print(f"  accounts triadic per-tick ............ {len(accounts)}")
    print(f"  flipped triadic->dyadic at 2-tick .... {flips} "
          f"(fraction = {flip_frac:.3f})")
    print(f"  structural predictor AUC (flip) ...... {pred_auc:.3f}")
    print(f"  panel verdict indeterminate | flip ... {n_indet_flip}/{flips} "
          f"(= {frac_flip_indeterminate:.3f})")
    print(f"  panel verdict indeterminate | no flip  {n_indet_noflip}/"
          f"{len(accounts) - flips} (= {frac_noflip_indeterminate:.3f})")
    print("-" * 78)

    # ---- H1 verdict ----
    if flip_frac > H1_FLIP:
        h1 = "SUPPORTED"
        h1_reason = (f"flip fraction {flip_frac:.3f} > {H1_FLIP:.2f}: the 2-tick grain flips "
                     f"a measurable share of triadic accounts to dyadic")
    elif flip_frac < H1_NULL:
        h1 = "REFUTED"
        h1_reason = (f"flip fraction {flip_frac:.3f} < {H1_NULL:.2f}: the verdict is invariant "
                     f"to the time-grain choice (NULL)")
    else:
        h1 = "REFUTED"
        h1_reason = (f"flip fraction {flip_frac:.3f} in the inconclusive band "
                     f"[{H1_NULL:.2f},{H1_FLIP:.2f}]: not a measurable flip")

    # ---- H2 verdict ----
    # Two parts, both required:
    #   (a) the grain-sensitive (flipping) subset is verdict-indeterminate under coder
    #       disagreement (the panel straddles the dyadic/triadic boundary) while the
    #       grain-invariant subset stays determinate; and
    #   (b) that subset is predictable a priori from rule structure (AUC > threshold).
    subset_indeterminate = (frac_flip_indeterminate >= 0.99
                            and frac_noflip_indeterminate <= 0.01)
    predictable = pred_auc > H2_AUC
    if subset_indeterminate and predictable:
        h2 = "SUPPORTED"
        h2_reason = (f"the flipping subset is verdict-indeterminate under grain disagreement "
                     f"({frac_flip_indeterminate:.3f}) while grain-invariant accounts stay "
                     f"determinate ({frac_noflip_indeterminate:.3f}), and structure predicts the "
                     f"flip a priori (AUC {pred_auc:.3f} > {H2_AUC:.2f})")
    elif not predictable:
        h2 = "REFUTED"
        h2_reason = (f"structural predictor AUC {pred_auc:.3f} <= {H2_AUC:.2f}: grain-sensitivity "
                     f"is not flaggable before computing Φ (NULL)")
    else:
        h2 = "REFUTED"
        h2_reason = (f"the indeterminacy split fails: flip-subset indeterminate "
                     f"{frac_flip_indeterminate:.3f}, invariant-subset indeterminate "
                     f"{frac_noflip_indeterminate:.3f}")

    print(f"\nH1 (>15% of triadic accounts flip under the 2-tick grain): {h1}")
    print(f"    {h1_reason}")
    print(f"H2 (grain-sensitive subset is indeterminate under coder disagreement and "
          f"predictable a priori): {h2}")
    print(f"    {h2_reason}")
    print("=" * 78)


if __name__ == "__main__":
    main()
