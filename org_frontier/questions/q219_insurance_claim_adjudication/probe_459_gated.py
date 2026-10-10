"""Probe 459 (Q219-H2) — is threshold auto-approval triadic only through flagged claims?

Question: when the engine auto-approves small claims and the adjuster sees only flagged ones, is the
arrangement triadic, and does its irreducibility live only in flagged states? Hypothesis (H2): `gated`
(C'=E∧¬A, E'=C, A'=E∧C) is triadic with major complex {C, E, A}, every reachable state with
Φ_MIP > 1e-9 has E=1, and every E=0 state has Φ_MIP ≤ 1e-9. Method: verdict() with its per-state
phi_profile, and major_complex(). Decision rule (methods.md): confirmed if all three clauses hold; partial
if triadic with full core but the state clause fails; refuted otherwise. Instrument control first.

Run (from the repo root, venv active):
    python -m org_frontier.questions.q219_insurance_claim_adjudication.probe_459_gated
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict
from org_frontier.questions.q219_insurance_claim_adjudication.forms import GATED, check_controls
from org_frontier.questions.q219_insurance_claim_adjudication._run import (
    PHI_EPS, run_form, state_str, triadic_full, write_csv,
)


def main():
    print("PROBE 459 (Q219-H2) — threshold auto-approval: C'=E∧¬A, E'=C, A'=E∧C")
    print("=" * 72)
    print(check_controls(verdict))
    r = run_form("gated", GATED)
    full = triadic_full(r)
    e1_only = all(s[1] == 1 for s in r["irreducible"]) and len(r["irreducible"]) > 0
    e0_zero = all(p <= PHI_EPS for s, p in r["profile"] if s[1] == 0)
    e0_states = [state_str(s) for s, _ in r["profile"] if s[1] == 0]
    print("=" * 72)
    print(f"  (i)+(ii) triadic with core {{C,E,A}}: {full}")
    print(f"  (iii) every irreducible state has E=1: {e1_only} | "
          f"every E=0 state Φ=0: {e0_zero} (E=0 states reached: {' '.join(e0_states) or 'none'})")
    if full and e1_only and e0_zero:
        tag = "CONFIRMED"
    elif full:
        tag = "PARTIAL"
    else:
        tag = "REFUTED"
    print(f"  H2 VERDICT: {tag}")
    write_csv("gated.csv", [r])


if __name__ == "__main__":
    main()
