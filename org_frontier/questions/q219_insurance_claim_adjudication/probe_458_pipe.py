"""Probe 458 (Q219-H1) — is a pass-through claims pipe triadic through closure alone?

Question: when the engine only forwards the claim to the adjuster and the claimant reads the adjuster's
decision, does the three-party arrangement factor? Hypothesis (H1): `pipe` (C'=A, E'=C, A'=E), identical
to Q11's rot_ring(3), is triadic with major complex {C, E, A}. Method: exact IIT-4.0 Φ over the MIP via
verdict() and major_complex(); decision rule from methods.md. Instrument control: chat_dyad reads dyadic
and ats_triad_mediator reads triadic at Φ=2.0 before the comparison.

Run (from the repo root, venv active):
    python -m org_frontier.questions.q219_insurance_claim_adjudication.probe_458_pipe
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict
from org_frontier.questions.q219_insurance_claim_adjudication.forms import PIPE, check_controls
from org_frontier.questions.q219_insurance_claim_adjudication._run import run_form, triadic_full, write_csv


def main():
    print("PROBE 458 (Q219-H1) — pass-through pipe: C'=A, E'=C, A'=E")
    print("=" * 72)
    print(check_controls(verdict))
    r = run_form("pipe", PIPE)
    ok = triadic_full(r)
    print("=" * 72)
    print(f"  pipe triadic with core {{C,E,A}}: {ok}")
    print(f"  H1 VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")
    write_csv("pipe.csv", [r])


if __name__ == "__main__":
    main()
