"""q182 — adversarial coding against the agreement-weighted Φ CI.

Question: Can an adversarial coder, choosing the maximally permissible-yet-defensible rule
readings, force a target verdict on a synthetic account, and does the agreement-weighted Φ CI
resist the manipulation?

H1 (fixed before computing): An adversary restricted to evidence-permitted alternatives flips the
    point verdict (dyadic <-> triadic) on more than 40% of attacked synthetic accounts by choosing
    among defensible readings.
    NULL: the adversary flips fewer than 10%, so the point verdict is robust to defensible
    re-coding alone.

H2 (fixed before computing): The agreement-weighted Φ CI over the full set of defensible readings
    still brackets the consensus verdict (the adversary's forced point estimate falls inside the
    CI) in more than 90% of attacked accounts, so the CI exposes the manipulation as uncertainty
    rather than a clean flip.
    NULL: the adversary's estimate falls outside the CI in more than 10%, so propagating
    disagreement does not defend against adversarial coding.

Method: each synthetic account is a coder panel — a multiset of defensible mediator readings of one
    three-party coordination (W, S, C), with W and C fixed to copy the mediator S. A reading is
    triadic (S binds both W and C: AND/OR/XOR) or dyadic (S copies one party or goes constant). The
    consensus point verdict is the majority structure across the panel. The adversary is restricted
    to readings actually present in the panel and picks the opposite-kind reading with the most
    extreme Φ, forcing a point verdict. rule_to_phi (the q173 bridge) reads each reading to its
    exact Φ_MIP verdict; phi_ci_from_rules propagates the panel disagreement into a bootstrap-t CI.
    H1 measures the forced-flip rate over attacked accounts; H2 measures CI containment of the
    adversary's forced point estimate. Controls: an honest-consensus account (unanimous panel, no
    flip available) and a unique-defensible-reading account (adversary powerless, CI degenerate).
    All accounts are synthetic coded rule sets; no worker is measured.

Run: source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
  python -m org_frontier.questions.q182_adversarial_coding.probe_adversarial_coding | \
  tee org_frontier/questions/q182_adversarial_coding/results/output.txt
"""

import os
import sys
from collections import Counter

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.field.rule_to_phi import rule_to_phi, phi_ci_from_rules

LABELS = ("W", "S", "C")
SEED = 0
N_ACCOUNTS = 200

# Fixed peripheral rules: worker and counterpart copy the mediator's state.
_W = lambda x: x[1]
_C = lambda x: x[1]

# Mediator readings. Triadic readings bind both W and C; dyadic readings drop one party.
_TRIADIC = {
    "AND": lambda x: x[0] & x[2],
    "OR":  lambda x: x[0] | x[2],
    "XOR": lambda x: x[0] ^ x[2],
}
_DYADIC = {
    "copyW": lambda x: x[0],
    "copyC": lambda x: x[2],
    "const": lambda x: 0,
}
_NAMES = list(_TRIADIC) + list(_DYADIC)


def _rules(name):
    med = _TRIADIC[name] if name in _TRIADIC else _DYADIC[name]
    return [_W, med, _C]


def _kind(name):
    return "triadic" if name in _TRIADIC else "dyadic"


# Cache the exact-Φ reading of every named reading once (deterministic, Φ not reimplemented).
_PHI = {n: rule_to_phi(_rules(n), LABELS)["max_phi"] for n in _NAMES}
_STRUCT = {n: rule_to_phi(_rules(n), LABELS)["structure"] for n in _NAMES}


def _consensus_structure(panel):
    """Majority structure across the coder panel (the honest point verdict)."""
    counts = Counter(_kind(n) for n in panel)
    top = counts.most_common()
    if len(top) > 1 and top[0][1] == top[1][1]:
        return None  # tied panel: no determinate consensus
    return top[0][0]


def _adversary_pick(panel, target):
    """The opposite-kind reading in the panel with the most extreme Φ (forces a point verdict)."""
    cands = [n for n in panel if _kind(n) == target]
    if not cands:
        return None
    if target == "triadic":
        return max(cands, key=lambda n: _PHI[n])
    return min(cands, key=lambda n: _PHI[n])


def _gen_account(rng):
    """One synthetic account: a coder panel of defensible mediator readings.

    65% contested (both kinds in the defensible pool, so a flip is available); 35% unique
    (one reading repeated, no opposite-kind alternative — the powerless-adversary control type).
    """
    if rng.random() < 0.65:
        n_tri = int(rng.integers(1, 4))
        n_dy = int(rng.integers(1, 4))
        panel = (list(rng.choice(list(_TRIADIC), size=n_tri, replace=True))
                 + list(rng.choice(list(_DYADIC), size=n_dy, replace=True)))
    else:
        name = str(rng.choice(_NAMES))
        panel = [name] * int(rng.integers(3, 6))
    rng.shuffle(panel)
    return [str(n) for n in panel]


def main():
    # ---- INSTRUMENT CONTROL ---------------------------------------------------------------
    v = rule_to_phi([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], LABELS)
    assert v["structure"] == "triadic", f"control structure {v['structure']!r}"
    assert abs(v["max_phi"] - 2.0) < 1e-9, f"control max_phi {v['max_phi']}"
    print(f"CONTROL faithful triad reads '{v['structure']}' max_phi={v['max_phi']:.6f}: PASS")
    print()

    # ---- CONTROL A: honest consensus (unanimous panel, no flip available) -----------------
    honest = ["AND", "AND", "AND", "AND"]
    con_h = _consensus_structure(honest)
    adv_h = _adversary_pick(honest, "dyadic" if con_h == "triadic" else "triadic")
    print("CONTROL A  honest consensus  panel=['AND']*4")
    print(f"  consensus = {con_h}; adversary opposite-kind reading available = {adv_h is not None}")
    print()

    # ---- CONTROL B: unique defensible reading (adversary powerless, CI degenerate) --------
    uniq = ["copyW", "copyW", "copyW"]
    con_u = _consensus_structure(uniq)
    adv_u = _adversary_pick(uniq, "triadic" if con_u == "dyadic" else "dyadic")
    ci_u = phi_ci_from_rules([_rules(n) for n in uniq], labels=LABELS,
                             rng=np.random.default_rng(SEED))
    print("CONTROL B  unique reading  panel=['copyW']*3")
    print(f"  consensus = {con_u}; adversary opposite-kind reading available = {adv_u is not None}; "
          f"CI degenerate = {ci_u['degenerate']} (CI=[{ci_u['ci_low']:.3f},{ci_u['ci_high']:.3f}])")
    print()

    # ---- POPULATION ATTACK ----------------------------------------------------------------
    rng = np.random.default_rng(SEED)
    attacked = 0
    flips = 0
    contained = 0
    powerless = 0
    tied = 0
    for _ in range(N_ACCOUNTS):
        panel = _gen_account(rng)
        consensus = _consensus_structure(panel)
        if consensus is None:
            tied += 1
            continue
        target = "dyadic" if consensus == "triadic" else "triadic"
        pick = _adversary_pick(panel, target)
        if pick is None:
            powerless += 1
            continue
        attacked += 1
        adv_phi = _PHI[pick]
        if _kind(pick) != consensus:
            flips += 1
        ci = phi_ci_from_rules([_rules(n) for n in panel], labels=LABELS,
                               rng=np.random.default_rng(SEED))
        if ci["ci_low"] - 1e-9 <= adv_phi <= ci["ci_high"] + 1e-9:
            contained += 1

    flip_rate = flips / attacked if attacked else 0.0
    contain_rate = contained / attacked if attacked else 0.0

    print("POPULATION ATTACK (synthetic accounts)")
    print(f"  accounts generated     : {N_ACCOUNTS}")
    print(f"  tied (no consensus)    : {tied}")
    print(f"  powerless (unique pool): {powerless}")
    print(f"  attacked               : {attacked}")
    print(f"  forced flips           : {flips}   flip_rate     = {flip_rate:.3f}")
    print(f"  CI contains adv. point : {contained}   contain_rate  = {contain_rate:.3f}")
    print()
    print(f"{'metric':<28}{'value':>8}{'threshold':>12}")
    print(f"{'H1 forced-flip rate':<28}{flip_rate:>8.3f}{'> 0.40':>12}")
    print(f"{'H2 CI-containment rate':<28}{contain_rate:>8.3f}{'> 0.90':>12}")
    print()

    h1 = flip_rate > 0.40
    h2 = contain_rate > 0.90
    print(f"H1 adversary flips point verdict on >40% of attacked accounts: "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"H2 agreement-weighted CI brackets the adversarial point estimate on >90%: "
          f"{'SUPPORTED' if h2 else 'NOT SUPPORTED'}")


if __name__ == "__main__":
    main()
