"""q188 — handoff directionality spread: does narrated reciprocity move the Φ verdict?

Question: in a clinical handoff, the outgoing clinician narrates a one-way note (write the
record and leave) and the incoming clinician narrates reciprocal coupling through the record
(query back, the outgoing one revises). The two narrations are two ACCOUNTS of the same
shift-boundary coordination over the same parties O (outgoing), R (record), I (incoming). Does
the Φ spread between the two accounts distinguish a conveyed handoff from a bound one?

H1: The one-way account is dyadic and the reciprocal account triadic, so verdict_agreement = 0,
    and the incoming clinician I sits in the integrated core only under the reciprocal account
    (core_jaccard < 1). H1-null: both directionality accounts give the same verdict and the same
    core, so reciprocity in the narration leaves no Φ spread.

H2: phi_gap grows monotonically as the synthetic strength beta of the back-channel
    (incoming -> record -> outgoing) coupling in the reciprocal account increases from zero. The
    one-way account is held fixed at phi = 0, so phi_gap(beta) = Φ of the reciprocal account at
    back-channel strength beta. H2-null: phi_gap is flat in beta, so the spread does not track
    the degree of reciprocity the accounts disagree about.

Method: two rule sets over the interdependence prior (parties O, R, I; little-endian current
state x with x[0]=O, x[1]=R, x[2]=I).
  - One-way account A: O persists, R copies O, I copies R. No path from I back to O.
  - Reciprocal account B: O reads I, R = O & I (couples both clinicians), I copies R. The path
    I -> R -> O closes the loop.
The discrete bridge spread() scores verdict_agreement, phi_gap, core_jaccard, both_verdicts on
A vs B. For H2 the back-channel is dialed: account B's O-node fires with probability
(1-beta)*O + beta*I, a stochastic TPM whose only tunable edge is I -> O; beta=0 removes the
back-channel and beta=1 is full reciprocal coupling. phi_gap(beta) = |Φ(A) - Φ(B_beta)| with
Φ(A) = 0. Control: with the back-channel set to zero in both accounts both collapse to the
conveyed case and the spread is zero (phi_gap = 0). The instrument control validates the
classifier on the faithful triad (reads triadic, max_phi 2.0).

Scope: in-silico. The two accounts are synthetic coder-supplied rule sets, not measured
clinician behavior. The construct scored is divergence between two stated narrations of one
coordination. No clinician is measured; the empirical reading is on synthetic data.

Run:
  source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
  python -m org_frontier.questions.q188_handoff_directionality_spread.probe_handoff_directionality_spread
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import tpm_from_rules
from org_frontier.probes.lib import verdict, max_phi_float
from org_frontier.qualitative.disagreement_phi import spread

LABELS = ("O", "R", "I")

# One-way handoff account: O persists, R copies O, I copies R. No return path to O.
ACCOUNT_ONEWAY = [lambda x: x[0], lambda x: x[0], lambda x: x[1]]

# Reciprocal account: O reads I, R = O & I, I copies R. The loop I -> R -> O closes.
ACCOUNT_RECIP = [lambda x: x[2], lambda x: x[0] & x[2], lambda x: x[1]]


def reciprocal_tpm(beta: float) -> np.ndarray:
    """State-by-node TPM of the reciprocal account with back-channel strength beta in [0, 1].

    O fires with probability (1-beta)*O + beta*I (the only tunable edge, I -> O). R = O & I and
    I = R are held deterministic. beta = 0 removes the back-channel; beta = 1 is full coupling.
    """
    t = np.zeros((8, 3))
    for s in range(8):
        x = tuple((s >> i) & 1 for i in range(3))
        t[s, 0] = (1.0 - beta) * x[0] + beta * x[2]
        t[s, 1] = float(x[0] & x[2])
        t[s, 2] = float(x[1])
    return t


def main() -> None:
    rng = np.random.default_rng(0)

    # ---- INSTRUMENT CONTROL: faithful triad reads triadic, max_phi 2.0 ----
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    cv = verdict(triad, ("W", "S", "C"))
    assert cv.structure == "triadic" and abs(cv.max_phi - 2.0) < 1e-9, (
        f"control failed: {cv.structure} {cv.max_phi}")

    # ---- CONTROL collapse: back-channel zero in both accounts -> conveyed, zero spread ----
    phi_oneway, _ = max_phi_float(tpm_from_rules(ACCOUNT_ONEWAY), rng=np.random.default_rng(0))
    phi_recip0, _ = max_phi_float(reciprocal_tpm(0.0), rng=np.random.default_rng(0))
    gap0 = abs(phi_oneway - phi_recip0)
    assert gap0 < 1e-9, f"collapse control failed: gap0={gap0}"
    print(f"CONTROL faithful-triad triadic @ max_phi {cv.max_phi:.6f}; "
          f"zero-back-channel gap {gap0:.6f}: PASS")
    print()

    # ---- H1: discrete one-way vs reciprocal accounts via the bridge spread ----
    sp = spread(ACCOUNT_ONEWAY, ACCOUNT_RECIP, LABELS)
    structA, structB = sp["both_verdicts"]
    print("H1  two accounts of one handoff (one-way vs reciprocal)")
    print(f"  {'account':<24}{'verdict':<10}{'core':<14}")
    # core sets via the bridge's major_complex (recomputed for the table)
    from org_frontier.qualitative.disagreement_phi import _core_set
    cA = tuple(sorted(_core_set(ACCOUNT_ONEWAY, LABELS)))
    cB = tuple(sorted(_core_set(ACCOUNT_RECIP, LABELS)))
    print(f"  {'A one-way (outgoing)':<24}{structA:<10}{str(cA or '()'):<14}")
    print(f"  {'B reciprocal (incoming)':<24}{structB:<10}{str(cB or '()'):<14}")
    print(f"  verdict_agreement = {sp['verdict_agreement']}   "
          f"phi_gap = {sp['phi_gap']:.6f}   core_jaccard = {sp['core_jaccard']:.6f}")
    I_in_A = "I" in cA
    I_in_B = "I" in cB
    print(f"  incoming clinician I in core:  one-way={I_in_A}   reciprocal={I_in_B}")
    print()

    h1 = (sp["verdict_agreement"] == 0 and sp["core_jaccard"] < 1.0
          and (not I_in_A) and I_in_B)

    # ---- H2: phi_gap monotone in back-channel strength beta ----
    betas = np.linspace(0.0, 1.0, 6)
    print("H2  phi_gap vs back-channel strength beta (one-way held at phi=0)")
    print(f"  {'beta':<8}{'phi_recip':<14}{'phi_gap':<12}")
    gaps = []
    for b in betas:
        phi_b, _ = max_phi_float(reciprocal_tpm(float(b)), rng=np.random.default_rng(0))
        gap = abs(phi_oneway - phi_b)
        gaps.append(gap)
        print(f"  {b:<8.2f}{phi_b:<14.6f}{gap:<12.6f}")
    diffs = np.diff(gaps)
    strictly_increasing = bool(np.all(diffs > 1e-9))
    print(f"  strictly increasing in beta: {strictly_increasing}  "
          f"(min step {float(diffs.min()):.6f})")
    print()

    # ---- verdicts ----
    print(f"H1 one-way dyadic / reciprocal triadic, I in core only under reciprocal: "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"H2 phi_gap monotone increasing in back-channel strength: "
          f"{'CONFIRMED' if strictly_increasing else 'NOT SUPPORTED'}")


if __name__ == "__main__":
    main()
