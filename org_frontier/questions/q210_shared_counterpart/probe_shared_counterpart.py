"""Probe 364 (Q210) — do two triads sharing a counterpart merge into one core?

Agenda #16, extending the multi-role result (#73) to two full triads. Two conjunctive triads share one
counterpart C. The shared counterpart reads the two mediators through a bridge, swept three ways (none,
AND, OR). The probe reads whether the major complex spans both triads (one merged core) or stays a single
triad, and how the bridge rule changes the result.

Node order (n=5): W1, S1, W2, S2, C. S1'=W1∧C, S2'=W2∧C, W1'=S1, W2'=S2, C'=bridge(S1,S2).

Hypotheses (fixed before computing, see hypotheses.md):
  H1 control — F0 single triad reads triadic, Φ=2.0.
  H2 — under the AND bridge, both mediators S1, S2 sit in one major complex (the triads merge).
  H3 — the shared counterpart C is in the merged core.
  H4 — the merged core Φ exceeds a single triad's 2.0 (super-additive).
  H5 — the AND bridge yields a higher core Φ than the OR bridge (the combination rule matters).

Validation gap: in-silico Boolean models with exact Φ; evidence about how a shared party binds two
coordinations, not a measurement of any organization.

Run:  python -m org_frontier.questions.q210_shared_counterpart.probe_shared_counterpart
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict, major_complex  # noqa: E402
from org_frontier.classifier.classifier import PHI_EPS  # noqa: E402

LABELS5 = ("W1", "S1", "W2", "S2", "C")

BRIDGES = {
    "none": lambda x: x[1],            # C updates from mediator 1 only
    "AND":  lambda x: x[1] & x[3],     # C commits when both mediators fire
    "OR":   lambda x: x[1] | x[3],     # C commits when either fires
}


def form(bridge):
    return [
        lambda x: x[1],          # W1' = S1
        lambda x: x[0] & x[4],   # S1' = W1 ∧ C
        lambda x: x[3],          # W2' = S2
        lambda x: x[2] & x[4],   # S2' = W2 ∧ C
        BRIDGES[bridge],         # C'  = bridge(S1, S2)
    ]


def main():
    print("PROBE 364 (Q210) — two triads sharing a counterpart: one core or two?")
    print("=" * 80)

    # ---- H1 instrument control ----
    v0 = verdict([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], ("W", "S", "C"))
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print("  H1 control  single triad : %s Φ=%.6f %s"
          % (v0.structure, v0.max_phi, "PASS" if ctrl else "FAIL"))
    assert ctrl, "instrument control failed; aborting"

    res = {}
    for name in ("none", "AND", "OR"):
        v = verdict(form(name), LABELS5)
        core, core_phi = major_complex(form(name), LABELS5)
        res[name] = (v.structure, v.max_phi, core, core_phi)
        print("  bridge=%-4s  %-8s wholeΦ_MIP=%.4f  core=%s coreΦ=%.3f"
              % (name, v.structure, v.max_phi, core, core_phi))

    print("=" * 80)
    and_core, and_phi = res["AND"][2], res["AND"][3]
    or_phi = res["OR"][3]
    h2 = "S1" in and_core and "S2" in and_core
    h3 = "C" in and_core
    h4 = and_phi > 2.0 + PHI_EPS
    h5 = and_phi > or_phi + PHI_EPS
    print("  AND-bridge core Φ = %.3f ; OR-bridge core Φ = %.3f" % (and_phi, or_phi))
    print("  H2 (AND bridge merges both mediators into one core): %s"
          % ("SUPPORTED" if h2 else "REFUTED"))
    print("  H3 (the shared counterpart C is in the merged core): %s"
          % ("SUPPORTED" if h3 else "REFUTED"))
    print("  H4 (merging two triads is super-additive, core Φ > 2.0): %s"
          % ("SUPPORTED" if h4 else "REFUTED"))
    print("  H5 (AND bridge core Φ > OR bridge core Φ): %s"
          % ("SUPPORTED" if h5 else "REFUTED"))
    print("=" * 80)


if __name__ == "__main__":
    main()
