"""Probe 460 (Q219-H3, H4) — is the fraud-flag loop triadic, and does it survive removing override learning?

Question: when the adjuster upholds the engine's fraud flag only if flag and claim agree, and the engine's
next flag learns from the adjuster's last call, are all three parties bound? Does the triad depend on the
learning edge? Hypotheses: H3 — `loop` (C'=A, E'=C∧A, A'=E∧C) is triadic with major complex {C, E, A}.
H4 — `loop_nolearn` (C'=A, E'=C, A'=E∧C) is also triadic with major complex {C, E, A}. Method: verdict()
and major_complex(); Φ magnitudes reported, not compared. Instrument control first.

Run (from the repo root, venv active):
    python -m org_frontier.questions.q219_insurance_claim_adjudication.probe_460_loop
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict
from org_frontier.questions.q219_insurance_claim_adjudication.forms import (
    LOOP, LOOP_NOLEARN, check_controls,
)
from org_frontier.questions.q219_insurance_claim_adjudication._run import run_form, triadic_full, write_csv


def main():
    print("PROBE 460 (Q219-H3, H4) — fraud-flag loop with and without override learning")
    print("=" * 72)
    print(check_controls(verdict))
    loop = run_form("loop", LOOP)
    nolearn = run_form("loop_nolearn", LOOP_NOLEARN)
    h3 = triadic_full(loop)
    h4 = triadic_full(nolearn)
    print("=" * 72)
    print(f"  loop triadic with core {{C,E,A}}: {h3}")
    print(f"  H3 VERDICT: {'CONFIRMED' if h3 else 'REFUTED'}")
    print(f"  loop_nolearn triadic with core {{C,E,A}}: {h4}")
    print(f"  H4 VERDICT: {'CONFIRMED' if h4 else 'REFUTED'}")
    write_csv("loop.csv", [loop, nolearn])


if __name__ == "__main__":
    main()
