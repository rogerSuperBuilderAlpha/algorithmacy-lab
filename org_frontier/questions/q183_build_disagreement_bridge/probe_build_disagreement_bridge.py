"""q183 — build and validate the disagreement-Φ bridge module.

Question: Can a bridge module take two divergent party accounts of one coordination as two rule
sets, compute each Φ verdict, and report a stable spread tuple (verdict_agreement, phi_gap,
core_jaccard) that is exactly zero divergence when both parties give the same account?

H1: On a control where both accounts are the identical rule set, the module returns
    verdict_agreement = 1, phi_gap = 0.0, and core_jaccard = 1.0 (the spread is a valid
    zero-anchored construct).
    H1-null: the spread is nonzero on identical accounts.

H2: Swapping which party is account A versus account B leaves |phi_gap|, verdict_agreement, and
    core_jaccard unchanged (the spread is symmetric in the two parties).
    H2-null: relabelling the parties changes at least one spread component (the construct
    encodes order, not disagreement).

Method: build org_frontier/qualitative/disagreement_phi.py exposing spread(A, B, labels). Run an
instrument control on the faithful triad. Validate H1 on an identity control (A == B). Validate
H2 on a label-swap control over a divergent pair: one account is the worker-system-counterpart
triad [x1, x0&x2, x1] (triadic), the other is a dyadic rewrite [x1, x0, x1] (S copies W only, the
mediator drops the counterpart). Synthetic accounts.

Run: source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
  python -m org_frontier.questions.q183_build_disagreement_bridge.probe_build_disagreement_bridge
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import verdict
from org_frontier.qualitative.disagreement_phi import spread

# Seed all RNG for determinism (the spread itself is exact; this guards any sampled path).
np.random.default_rng(0)

LABELS = ("W", "S", "C")

# The faithful worker-system-counterpart triad: S binds W and C (strict mediation). Triadic.
TRIAD = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
# A divergent dyadic account of the same coordination: S copies W only, dropping C from the core.
DYAD = [lambda x: x[1], lambda x: x[0], lambda x: x[1]]


def main():
    # ---- INSTRUMENT CONTROL ---------------------------------------------------------------
    v = verdict(TRIAD, LABELS)
    assert v.structure == "triadic", f"control structure {v.structure!r}"
    assert abs(v.max_phi - 2.0) < 1e-9, f"control max_phi {v.max_phi}"
    print(f"CONTROL faithful triad reads '{v.structure}' max_phi={v.max_phi:.6f}: PASS")
    print()

    # ---- H1: identity control (A == B) ----------------------------------------------------
    s_ident = spread(TRIAD, TRIAD, LABELS)
    print("H1 identity control  A == B (faithful triad vs itself)")
    print(f"  verdict_agreement = {s_ident['verdict_agreement']}")
    print(f"  phi_gap           = {s_ident['phi_gap']:.6f}")
    print(f"  core_jaccard      = {s_ident['core_jaccard']:.6f}")
    print(f"  both_verdicts     = {s_ident['both_verdicts']}")
    print()

    h1_ok = (
        s_ident["verdict_agreement"] == 1
        and abs(s_ident["phi_gap"]) < 1e-9
        and abs(s_ident["core_jaccard"] - 1.0) < 1e-9
    )

    # ---- H2: label-swap control over a divergent pair -------------------------------------
    s_ab = spread(TRIAD, DYAD, LABELS)   # A = triad account, B = dyad account
    s_ba = spread(DYAD, TRIAD, LABELS)   # parties relabelled

    print("Divergent pair  triad account vs dyad account of one coordination")
    print(f"{'orientation':<14}{'verdict_agree':>14}{'phi_gap':>12}{'core_jaccard':>14}"
          f"   both_verdicts")
    print(f"{'A=triad B=dyad':<14}{s_ab['verdict_agreement']:>14}{s_ab['phi_gap']:>12.6f}"
          f"{s_ab['core_jaccard']:>14.6f}   {s_ab['both_verdicts']}")
    print(f"{'A=dyad B=triad':<14}{s_ba['verdict_agreement']:>14}{s_ba['phi_gap']:>12.6f}"
          f"{s_ba['core_jaccard']:>14.6f}   {s_ba['both_verdicts']}")
    print()

    h2_ok = (
        s_ab["verdict_agreement"] == s_ba["verdict_agreement"]
        and abs(s_ab["phi_gap"] - s_ba["phi_gap"]) < 1e-9
        and abs(s_ab["core_jaccard"] - s_ba["core_jaccard"]) < 1e-9
    )

    # the divergent pair must actually diverge, else H2 is vacuous
    diverges = (s_ab["verdict_agreement"] == 0) or (s_ab["phi_gap"] > 1e-9)
    print(f"divergent pair actually diverges: {diverges}")
    print()

    print(f"H1 zero-anchored spread on identical accounts: "
          f"{'SUPPORTED' if h1_ok else 'REFUTED'}")
    print(f"H2 spread symmetric under party relabelling: "
          f"{'SUPPORTED' if (h2_ok and diverges) else 'REFUTED'}")


if __name__ == "__main__":
    main()
