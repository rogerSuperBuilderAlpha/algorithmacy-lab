"""Probe 367 (Q213) — contingent irreducibility and the bypass-counterfactual.

A mediator can sit in a triad's core for two reasons. INTRINSIC: it does integrative work no direct edge
between its neighbours reproduces. CONTINGENT: it is a conduit that would factor out, held in the core only
because a constraint forbids the bypass — the car dealer under franchise law. The probe runs the
bypass-counterfactual (classifier/contingency.py) over four constructed forms and reads whether the test
separates the two and realizes the four-way taxonomy.

Forms (n=3):
  conjunctive clearinghouse (intrinsic): W'=S, S'=W&C, C'=S ; bypass C reads W (replace)
  car dealer (contingent):               M'=B, D'=M, B'=D    ; bypass B reads M (replace)
  clearinghouse + back-channel (partial):W'=S, S'=W&C, C'=S ; bypass C'=S|W (add)
  free conduit (reducible):              M'=B, D'=M, B'=M    ; bypass B reads M (replace)

Hypotheses (fixed before computing, see hypotheses.md):
  H1 control — conjunctive triad triadic Φ=2.0.
  H2 — the constrained car dealer is irreducible with the dealer in the core (a conduit irreducible by constraint).
  H3 — the bypass-counterfactual removes the dealer: kind=contingent, margin=2.0.
  H4 — the same bypass leaves the conjunctive mediator in place: kind=intrinsic, margin=0.0.
  H5 — partial and reducible forms classify as labeled; margins order contingent >= partial > intrinsic.

Validation gap: in-silico Boolean models with exact Φ; evidence about a category of irreducibility, not a
measurement of any organization. The car dealer is a worked illustration, not a fitted model of a market.

Run:  python -m org_frontier.questions.q213_contingent_irreducibility.probe_contingent_irreducibility
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict, major_complex  # noqa: E402
from org_frontier.classifier.contingency import contingency_test  # noqa: E402
from org_frontier.classifier.classifier import PHI_EPS  # noqa: E402

# constrained forms
CLEARINGHOUSE = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]          # W'=S, S'=W&C, C'=S
CAR_DEALER = [lambda x: x[2], lambda x: x[0], lambda x: x[1]]                    # M'=B, D'=M, B'=D
FREE_CONDUIT = [lambda x: x[2], lambda x: x[0], lambda x: x[0]]                  # M'=B, D'=M, B'=M
WSC = ("W", "S", "C")
MDB = ("M", "D", "B")


def main():
    print("PROBE 367 (Q213) — contingent irreducibility: the bypass-counterfactual")
    print("=" * 84)

    # ---- H1 instrument control ----
    v0 = verdict(CLEARINGHOUSE, WSC)
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print("  H1 control  conjunctive triad : %s Φ=%.6f %s"
          % (v0.structure, v0.max_phi, "PASS" if ctrl else "FAIL"))
    assert ctrl, "instrument control failed; aborting"

    # ---- H2: the constrained car dealer is irreducible with the dealer in the core ----
    vd = verdict(CAR_DEALER, MDB)
    cd_core, cd_phi = major_complex(CAR_DEALER, MDB)
    print("  car dealer (constrained)      : %s Φ=%.3f core=%s  D in core: %s"
          % (vd.structure, vd.max_phi, cd_core, "D" in cd_core))

    # ---- classify the four forms ----
    intr = contingency_test(CLEARINGHOUSE, WSC, "S", downstream="C", upstream="W", mode="replace")
    cont = contingency_test(CAR_DEALER, MDB, "D", downstream="B", upstream="M", mode="replace")
    part = contingency_test(CLEARINGHOUSE, WSC, "S", downstream="C", upstream="W", mode="add")
    redu = contingency_test(FREE_CONDUIT, MDB, "D", downstream="B", upstream="M", mode="replace")

    print("  intrinsic   (clearinghouse)   : %s" % intr.line())
    print("  contingent  (car dealer)      : %s" % cont.line())
    print("  partial     (+ back-channel)  : %s" % part.line())
    print("  reducible   (free conduit)    : %s" % redu.line())

    print("=" * 84)
    h2 = vd.structure == "triadic" and "D" in cd_core
    h3 = cont.kind == "contingent" and not cont.in_core_bypass and abs(cont.margin - 2.0) < 1e-6
    h4 = intr.kind == "intrinsic" and intr.in_core_bypass and intr.margin < PHI_EPS
    h5 = (part.kind == "partial" and 0.0 < part.margin < 2.0
          and redu.kind == "reducible" and not redu.in_core_constrained
          and cont.margin >= part.margin > intr.margin)
    print("  H2 (a conduit is irreducible under constraint: dealer in core): %s" % _v(h2))
    print("  H3 (bypass removes the contingent party: kind=contingent, margin=2.0): %s" % _v(h3))
    print("  H4 (same bypass leaves the intrinsic mediator: kind=intrinsic, margin=0): %s" % _v(h4))
    print("  H5 (taxonomy realized; margins order contingent>=partial>intrinsic): %s" % _v(h5))
    print("=" * 84)


def _v(b):
    return "SUPPORTED" if b else "REFUTED"


if __name__ == "__main__":
    main()
