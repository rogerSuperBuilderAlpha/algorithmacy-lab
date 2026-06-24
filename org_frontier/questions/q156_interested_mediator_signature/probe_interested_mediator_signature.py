"""q156 — Do interested mediators leave a CRQA signature that faithful mediators lack?

QUESTION
    An interested mediator's rule serves an objective: it weights one party's warrant over the
    other's instead of committing a neutral joint determination of the two. A faithful mediator's
    rule treats the parties as interchangeable. Both can sit on the same wiring graph (S reads W,
    its own previous state, and C; W and C read S) and both can carry the full {W, S, C}
    major-complex core. The question is whether the behavioral trace — the DCRP prominence on the
    mediator's outgoing edges, read from a sampled run — separates the interested mediators from
    the faithful ones once structure is held fixed.

H1  An interested mediator shows lower outgoing-edge DCRP prominence than a faithful mediator with
    identical connectivity, separating the two in over 70% of matched pairs.
    Null: outgoing prominence is statistically indistinguishable between interested and faithful
    mediators.

H2  The interested mediator's structural exact-Φ core is unchanged versus the faithful one, so a
    behavioral signature would carry interestedness information that Φ-membership alone misses.
    Null: major-complex membership already differs between interested and faithful mediators, so
    behavior adds nothing.

METHOD
    One wiring graph: W' = S, C' = S, S' = f(W, S, C), with the mediator's rule a truth table over
    (W, S, C). Faithful rules are symmetric under swapping the two parties; interested rules are
    asymmetric (they favor one party's warrant). The harness enumerate_mediators keeps only rules
    that read all three inputs and whose major-complex core is the full {W, S, C}, so the two pools
    are matched on wiring graph and on structural Φ-core. Outgoing prominence is the mean DCRP peak
    prominence on the mediator's two outgoing edges (S->W, S->C), averaged over a fixed set of
    seeded trajectories per form. H1 forms every interested x faithful pair and measures the
    fraction with interested prominence below faithful; a one-sided Mann-Whitney test on the
    per-form means is the companion read. H2 compares the major-complex cores of the two pools.

    Control = the worker-system-counterpart triad [x[1], x[0]&x[2], x[1]] with labels (W,S,C):
    verdict triadic, max_phi 2.0, full {W,S,C} core. The connectivity-identical faithful mediator
    is the control for the behavioral arm.

    Every number is exact IIT-4.0 Φ and CRQA on synthetic Boolean coordination forms. This is an
    in-silico study of the interested-mediator construct, not a measurement of any field
    organization. "Interested", "agenda", "faithful" are labels for the symmetry of a rule, not
    measured intent.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q156_interested_mediator_signature.probe_interested_mediator_signature
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from scipy.stats import mannwhitneyu

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.recurrence.crqa_phi_bridge import (
    MED_LABELS,
    mediator_rules,
    enumerate_mediators,
    outgoing_prominence,
)

# ---- fixed configuration (all RNG seeded so the run reproduces byte-for-byte) -------------
N_SEEDS = 16              # trajectories averaged per form (a fixed block of seeds)
SEED_BLOCK = range(N_SEEDS)
FAITHFUL_BASE = 1000     # form i -> base + 100*i; seeds base+100*i + 0..N_SEEDS-1
INTEREST_BASE = 5000
SEP_THRESHOLD = 0.70     # H1 matched-pair separation bar
ALPHA = 0.05             # significance for the companion Mann-Whitney read


def avg_outgoing(tt, base):
    """Mean outgoing prominence for a mediator over the fixed seed block."""
    return float(np.mean([outgoing_prominence(tt, base + s) for s in SEED_BLOCK]))


def main():
    print("PROBE 310 (q156) — interested vs faithful mediator: a CRQA outgoing-edge signature")
    print("=" * 84)

    # ---- INSTRUMENT CONTROL: the canonical faithful triad reads triadic, Φ=2.0, full core ----
    ctrl_rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    cv = verdict(ctrl_rules, MED_LABELS)
    ccore, _ = major_complex(ctrl_rules, MED_LABELS)
    ctrl_ok = (
        cv.structure == "triadic"
        and abs(cv.max_phi - 2.0) < 1e-9
        and tuple(ccore) == ("W", "S", "C")
    )
    print(
        f"CONTROL faithful triad [x1, x0&x2, x1]: {cv.structure} max_phi={cv.max_phi:.3f} "
        f"core={tuple(ccore)} -> {'PASS' if ctrl_ok else 'FAIL'}"
    )
    if not ctrl_ok:
        print("CONTROL FAILED — aborting.")
        sys.exit(1)
    print()

    # ---- build the two matched pools on the one wiring graph ----
    faithful, interested = enumerate_mediators()
    print(f"matched pools on the wiring graph W'=S, C'=S, S'=f(W,S,C):")
    print(f"  faithful (symmetric rule):   {len(faithful)} forms")
    print(f"  interested (asymmetric rule): {len(interested)} forms")
    print()

    # ---- H2 first: are the structural cores matched? ----
    faithful_cores = {tuple(major_complex(mediator_rules(tt), MED_LABELS)[0]) for tt in faithful}
    interested_cores = {tuple(major_complex(mediator_rules(tt), MED_LABELS)[0]) for tt in interested}
    cores_match = faithful_cores == interested_cores == {("W", "S", "C")}
    print("STRUCTURAL CORES (exact IIT-4.0 Φ major complex)")
    print(f"  faithful cores:   {sorted(faithful_cores)}")
    print(f"  interested cores: {sorted(interested_cores)}")
    print(f"  membership distinguishes the pools: {not cores_match}")
    print()

    # ---- behavioral arm: outgoing prominence per form ----
    fa_prom = np.array([avg_outgoing(tt, FAITHFUL_BASE + 100 * i) for i, tt in enumerate(faithful)])
    in_prom = np.array([avg_outgoing(tt, INTEREST_BASE + 100 * i) for i, tt in enumerate(interested)])

    print("OUTGOING DCRP PROMINENCE (mean over %d seeded trajectories per form)" % N_SEEDS)
    print(f"  faithful:   mean={fa_prom.mean():.4f}  sd={fa_prom.std():.4f}  n={len(fa_prom)}")
    print(f"  interested: mean={in_prom.mean():.4f}  sd={in_prom.std():.4f}  n={len(in_prom)}")
    print()

    # ---- H1: matched-pair separation + companion Mann-Whitney ----
    wins = int(sum(1 for it in in_prom for ft in fa_prom if it < ft))
    total = len(in_prom) * len(fa_prom)
    sep_frac = wins / total
    U, p_less = mannwhitneyu(in_prom, fa_prom, alternative="less")

    print("H1 MATCHED PAIRS (every interested x faithful pair on the identical wiring graph)")
    print(f"  pairs with interested prominence < faithful: {wins}/{total} = {sep_frac:.4f}")
    print(f"  one-sided Mann-Whitney (interested < faithful): U={U:.1f}  p={p_less:.4f}")
    print(f"  separation threshold: {SEP_THRESHOLD:.2f}   significance alpha: {ALPHA}")
    print()

    # ---- verdicts ----
    h1_supported = sep_frac > SEP_THRESHOLD and p_less < ALPHA
    # H2 is confirmed when structure does NOT distinguish the pools (the null on H2 is rejected),
    # so a behavioral signature would be the only available separator.
    h2_confirmed = cores_match

    print("=" * 84)
    print(
        "H1 (interested mediators show lower outgoing prominence, separating >70% of pairs): "
        + ("SUPPORTED" if h1_supported else "REFUTED")
    )
    print(
        "H2 (structural Φ-core is unchanged, so membership alone misses interestedness): "
        + ("CONFIRMED" if h2_confirmed else "NOT SUPPORTED")
    )


if __name__ == "__main__":
    main()
