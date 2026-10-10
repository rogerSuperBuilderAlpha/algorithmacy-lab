"""Probe 461 (Q219-H5) — does freezing the claimant collapse the fraud-flag loop?

Question: if the claimant no longer reads the decision, is the claim still decided by an irreducible
three-party arrangement? Hypothesis (H5): `loop_frozen_claimant` (C'=C, E'=C∧A, A'=E∧C) is dyadic
(max Φ_MIP ≤ 1e-9). Method: verdict() and major_complex(), with `loop` (H3) shown as the reference.
Decision rule (methods.md): confirmed if dyadic, refuted if triadic. Instrument control first.

Run (from the repo root, venv active):
    python -m org_frontier.questions.q219_insurance_claim_adjudication.probe_461_liveness
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict
from org_frontier.questions.q219_insurance_claim_adjudication.forms import (
    LOOP, LOOP_FROZEN_CLAIMANT, check_controls,
)
from org_frontier.questions.q219_insurance_claim_adjudication._run import run_form, write_csv


def main():
    print("PROBE 461 (Q219-H5) — claimant liveness: C'=C, E'=C∧A, A'=E∧C")
    print("=" * 72)
    print(check_controls(verdict))
    ref = run_form("loop", LOOP)
    frozen = run_form("loop_frozen_claimant", LOOP_FROZEN_CLAIMANT)
    ok = frozen["structure"] == "dyadic"
    print("=" * 72)
    print(f"  loop_frozen_claimant dyadic: {ok}")
    print(f"  H5 VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")
    write_csv("liveness.csv", [ref, frozen])


if __name__ == "__main__":
    main()
