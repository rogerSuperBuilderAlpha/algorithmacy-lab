"""q190 — is the disagreement-Φ spread robust to small synthetic noise in rule elicitation?

QUESTION
    The disagreement-Φ bridge (q183) scores how far apart two party accounts of one coordination
    sit: verdict_agreement (both read the same structure), phi_gap (the gap in whole-system max
    Φ_MIP), and core_jaccard. Each account is an elicited rule set. Elicitation is imprecise, so
    each party's stated rule table carries jitter. Does the measured spread survive that jitter,
    flipping verdict_agreement only for pairs whose noiseless Φ sits at the dyad/triad boundary,
    or does jitter flip agreement for pairs far from the boundary, making the spread an artifact
    of elicitation precision?

H1 (fixed before computing)
    Adding bounded Bernoulli noise to either account's elicited rule table leaves verdict_agreement
    and the sign of the signed phi_gap unchanged, except for account pairs whose noiseless Φ sits
    within epsilon of the dyad/triad boundary (a clean dyad, Φ ~ 0, which jitter can lift across).
    H1-null: noise flips verdict_agreement for pairs far from the boundary (both accounts triadic,
    Φ well above 0), so the spread is an artifact of elicitation precision.

H2 (fixed before computing)
    For pairs that genuinely disagree at noise zero (verdict_agreement = 0), the standard deviation
    of phi_gap under elicitation noise is smaller than its mean (signal-to-noise > 1), so the gap
    magnitude is a measurable quantity. H2-null: phi_gap noise swamps the mean (SNR <= 1), so the
    gap magnitude is not measurable.

METHOD
    Synthetic accounts. Each account is a per-node Boolean rule list over labels (W, S, C). The
    deterministic TPM is built by tpm_from_rules. Elicitation noise perturbs that TPM: each entry
    is gated by Bernoulli(RATE); a gated entry is pulled toward 0.5 by DELTA (a deterministic 1.0
    becomes 1-DELTA, a 0.0 becomes DELTA). This keeps the table near-deterministic, modeling an
    imprecise but honest rule elicitation. Whole-system max Φ_MIP of the perturbed (now mildly
    stochastic) TPM is read by max_phi_float, which infers the connectivity matrix numerically.

    The bridge is exercised on six account pairs that span the boundary:
      - two FAR pairs: both accounts triadic (faithful triad vs an AND/OR triad), noiseless
        min Φ = 2.0, far above the boundary; these agree (both triadic).
      - two NEAR pairs: a triad vs a clean dyad (Φ ~ 0 at the boundary); these disagree.
      - one FAR-agree dyad pair: two clean dyads (both Φ ~ 0). Both sit at the boundary, so this
        pair is also NEAR-boundary by the min-Φ test; it is kept to show agreement can flip on
        either side of the boundary, not only on disagreeing pairs.
      - one same-account pair (faithful triad vs itself): the bridge anchor, phi_gap noiseless 0.

    A pair is NEAR-boundary iff min(Φ_A, Φ_B) at noise zero is within EPS_BOUNDARY of 0 (at least
    one account is a clean dyad). Otherwise it is FAR. Over SEEDS seeded draws per pair, the probe
    records: how often verdict_agreement flips from its noiseless value, how often the signed
    phi_gap changes sign, and (for the noiseless-disagreeing pairs) the mean and sd of phi_gap.

    Control = a near-boundary pair (faithful triad Φ=2.0 vs clean dyad Φ=0) expected to flip its
    agreement under noise, and a far-from-boundary pair (faithful triad vs AND-triad, both Φ=2.0)
    expected to be stable, plus the faithful-triad bridge anchor (phi_gap 0, agreement 1,
    core_jaccard 1 at noise zero). The control passes when the anchor is exact and the two
    classes behave as named.

    H1 SUPPORTED if every verdict_agreement flip and every signed-phi_gap sign change occurs on a
    NEAR-boundary pair and no FAR pair ever flips. H2 SUPPORTED if, pooled over the
    noiseless-disagreeing pairs, sd(phi_gap) < mean(phi_gap) (SNR > 1).

    Determinism: every draw uses numpy.random.default_rng(seed) with a fixed seed loop; the Φ
    oracle seeds its state search with numpy.random.default_rng(seed). Re-runs reproduce byte for
    byte.

    Validation gap: exact IIT-4.0 Φ on small synthetic Boolean coordination forms. "Account",
    "elicitation noise", "spread", and "boundary" name rule-table-and-Φ quantities, not measured
    organizations. In-silico scope; the Φ-to-organization bridge is open. Both empirical arms run
    on synthetic accounts, so every rate reported is a baseline on synthetic data.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q190_spread_robustness_noise.probe_spread_robustness_noise
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import tpm_from_rules
from org_frontier.probes.lib import max_phi_float
from org_frontier.qualitative.disagreement_phi import spread

# ---- fixed configuration (all RNG seeded so the run reproduces byte-for-byte) -------------
TOL = 1e-6
EPS_PHI = 1e-9            # Φ above this is triadic, matching the classifier
EPS_BOUNDARY = 1e-6      # noiseless min Φ within this of 0 = a near-boundary pair
RATE = 0.10              # Bernoulli gate: fraction of TPM entries jittered
DELTA = 0.10             # pull of a gated entry toward 0.5
SEEDS = 30               # seeded elicitation draws per pair
H2_SNR_FLOOR = 1.0       # sd(phi_gap) < mean(phi_gap) for the gap to be measurable

LABELS = ("W", "S", "C")

# Account rule sets (synthetic). Per-node Boolean lambdas over the little-endian state tuple x.
FAITHFUL = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]   # triad, Φ = 2.0
AND_TRIAD = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[0]]  # triad, Φ = 2.0
OR_TRIAD = [lambda x: x[1], lambda x: x[0] | x[2], lambda x: x[1]]   # triad, Φ = 2.0
CLEAN_DYAD = [lambda x: x[2], lambda x: 0, lambda x: x[0]]           # dyad, Φ = 0.0
DYAD_INDEP = [lambda x: x[2], lambda x: x[1], lambda x: x[0]]        # dyad, Φ = 0.0

PAIRS = [
    ("anchor_triad_self",   FAITHFUL,  FAITHFUL),    # bridge anchor: identical accounts
    ("far_triad_triad",     FAITHFUL,  AND_TRIAD),   # FAR, agree (both triadic)
    ("far_triad_ortriad",   FAITHFUL,  OR_TRIAD),    # FAR, agree (both triadic)
    ("near_triad_dyad",     FAITHFUL,  CLEAN_DYAD),  # NEAR, disagree (triad vs clean dyad)
    ("near_ortriad_indep",  OR_TRIAD,  DYAD_INDEP),  # NEAR, disagree (triad vs clean dyad)
    ("near_dyad_dyad",      CLEAN_DYAD, DYAD_INDEP), # NEAR (both clean dyads), agree
]


def perturb(tpm, rng):
    """Elicitation noise on a deterministic TPM: gate by Bernoulli(RATE), pull gated entries
    toward 0.5 by DELTA. A deterministic 1.0 becomes 1-DELTA, a 0.0 becomes DELTA."""
    t = tpm.copy()
    gate = rng.random(t.shape) < RATE
    t[gate] = t[gate] * (1.0 - DELTA) + (1.0 - t[gate]) * DELTA
    return np.clip(t, 0.0, 1.0)


def noiseless_phi(rules):
    """Whole-system max Φ_MIP of the deterministic TPM (seeded oracle)."""
    tpm = tpm_from_rules(rules)
    mx, _ = max_phi_float(tpm, np.random.default_rng(0))
    return float(mx)


def noisy_phi(rules, seed, salt):
    """Whole-system max Φ_MIP after one seeded elicitation draw."""
    base = tpm_from_rules(rules)
    tpm = perturb(base, np.random.default_rng(seed + salt))
    mx, _ = max_phi_float(tpm, np.random.default_rng(seed + salt))
    return float(mx)


def structure_of(phi):
    return "triadic" if phi > EPS_PHI else "dyadic"


# --------------------------------------------------------------------------------------
# Instrument control.
# --------------------------------------------------------------------------------------

def control():
    """INSTRUMENT CONTROL: (1) the bridge anchor — faithful triad vs itself reads
    verdict_agreement 1, phi_gap 0.0, core_jaccard 1.0; (2) the noiseless faithful triad reads
    max_phi 2.0 (triadic); (3) a near-boundary pair (triad vs clean dyad) flips agreement under
    noise while a far pair (triad vs AND-triad) never does."""
    anchor = spread(FAITHFUL, FAITHFUL, LABELS)
    anchor_ok = (anchor["verdict_agreement"] == 1
                 and abs(anchor["phi_gap"]) < TOL
                 and abs(anchor["core_jaccard"] - 1.0) < TOL)

    triad_phi = noiseless_phi(FAITHFUL)
    triad_ok = (abs(triad_phi - 2.0) < TOL)

    # near-boundary pair must flip at least once; far pair must never flip.
    near_flip = 0
    far_flip = 0
    for seed in range(SEEDS):
        pa = noisy_phi(FAITHFUL, seed, 0)
        pd = noisy_phi(CLEAN_DYAD, seed, 7000)
        if int(structure_of(pa) == structure_of(pd)) != 0:  # noiseless they disagree (0)
            near_flip += 1
        pf = noisy_phi(AND_TRIAD, seed, 13000)
        if int(structure_of(pa) == structure_of(pf)) != 1:  # noiseless they agree (1)
            far_flip += 1
    class_ok = (near_flip >= 1 and far_flip == 0)

    ok = anchor_ok and triad_ok and class_ok
    print("CONTROL anchor(agree=%d gap=%.3f jacc=%.3f) triad_phi=%.3f near_flips=%d far_flips=%d -> %s"
          % (anchor["verdict_agreement"], anchor["phi_gap"], anchor["core_jaccard"],
             triad_phi, near_flip, far_flip, "PASS" if ok else "FAIL"), flush=True)
    if not ok:
        raise SystemExit("instrument control failed")


# --------------------------------------------------------------------------------------
# Main.
# --------------------------------------------------------------------------------------

def main():
    control()
    print("=" * 96, flush=True)
    print("q190 — disagreement-Φ spread under synthetic elicitation noise (RATE=%.2f DELTA=%.2f, %d draws)"
          % (RATE, DELTA, SEEDS), flush=True)
    print("=" * 96, flush=True)

    rows = []
    disagree_gaps = []   # pooled phi_gap draws over noiseless-disagreeing pairs (for H2)
    any_far_flip = False
    flips_off_boundary = []

    for key, ra, rb in PAIRS:
        phiA0 = noiseless_phi(ra)
        phiB0 = noiseless_phi(rb)
        agree0 = int(structure_of(phiA0) == structure_of(phiB0))
        signed_gap0 = phiA0 - phiB0
        sign0 = 0 if abs(signed_gap0) < EPS_BOUNDARY else (1 if signed_gap0 > 0 else -1)
        near_boundary = min(phiA0, phiB0) < EPS_BOUNDARY

        agree_flips = 0
        sign_flips = 0
        gaps = []
        for seed in range(SEEDS):
            pa = noisy_phi(ra, seed, 100)
            pb = noisy_phi(rb, seed, 5100)
            agree = int(structure_of(pa) == structure_of(pb))
            if agree != agree0:
                agree_flips += 1
            sg = pa - pb
            sgn = 0 if abs(sg) < EPS_BOUNDARY else (1 if sg > 0 else -1)
            if sign0 != 0 and sgn != 0 and sgn != sign0:
                sign_flips += 1
            gaps.append(abs(sg))

        gaps = np.asarray(gaps)
        rows.append({
            "key": key, "phiA0": phiA0, "phiB0": phiB0, "agree0": agree0,
            "near": near_boundary, "agree_flips": agree_flips, "sign_flips": sign_flips,
            "gap_mean": float(gaps.mean()), "gap_sd": float(gaps.std()),
        })
        if agree0 == 0:   # genuinely disagree at noise zero
            disagree_gaps.extend(gaps.tolist())
        if not near_boundary and (agree_flips > 0 or sign_flips > 0):
            any_far_flip = True
            flips_off_boundary.append(key)

    # ---- table ---------------------------------------------------------------------------
    print("Per-pair spread under elicitation noise (flips counted out of %d draws)" % SEEDS, flush=True)
    print("-" * 96, flush=True)
    print("  %-20s %8s %8s %7s %9s %11s %10s %9s %9s"
          % ("pair", "phiA0", "phiB0", "agree0", "boundary", "agree_flip", "sign_flip",
             "gap_mean", "gap_sd"), flush=True)
    print("-" * 96, flush=True)
    for r in rows:
        print("  %-20s %8.3f %8.3f %7d %9s %11d %10d %9.3f %9.3f"
              % (r["key"], r["phiA0"], r["phiB0"], r["agree0"],
                 "NEAR" if r["near"] else "FAR", r["agree_flips"], r["sign_flips"],
                 r["gap_mean"], r["gap_sd"]), flush=True)
    print("-" * 96, flush=True)

    # ---- H1 ------------------------------------------------------------------------------
    near_flips_total = sum(r["agree_flips"] + r["sign_flips"] for r in rows if r["near"])
    far_flips_total = sum(r["agree_flips"] + r["sign_flips"] for r in rows if not r["near"])
    h1 = (not any_far_flip) and far_flips_total == 0
    print(flush=True)
    print("H1 check: NEAR-boundary pairs accrued %d agree/sign flips; FAR pairs accrued %d."
          % (near_flips_total, far_flips_total), flush=True)
    if flips_off_boundary:
        print("    FAR pairs that flipped: %s" % ", ".join(flips_off_boundary), flush=True)
    print("H1 (flips occur only near the dyad/triad boundary, never far from it): %s"
          % ("SUPPORTED" if h1 else "REFUTED"), flush=True)

    # ---- H2 ------------------------------------------------------------------------------
    g = np.asarray(disagree_gaps)
    gmean = float(g.mean()) if g.size else 0.0
    gsd = float(g.std()) if g.size else 0.0
    snr = gmean / gsd if gsd > 0 else float("inf")
    h2 = snr > H2_SNR_FLOOR
    print(flush=True)
    print("H2 check: pooled over noiseless-disagreeing pairs, phi_gap mean=%.4f sd=%.4f SNR=%.3f (n=%d)"
          % (gmean, gsd, snr, g.size), flush=True)
    print("H2 (sd(phi_gap) < mean(phi_gap) for disagreeing pairs, SNR > %.1f): %s"
          % (H2_SNR_FLOOR, "SUPPORTED" if h2 else "REFUTED"), flush=True)


if __name__ == "__main__":
    main()
