"""Probe 361 (Q207) — does a half-rate mediator still bind the triad?

Agenda Q9. The lab's instrument reads a one-step synchronous transition, but a mediating system often
commits on a slower cadence than the parties it coordinates. This holds the parties at full rate and slows
only the mediator to every second step, modeled with a clock node K that gates the mediator's recompute,
and asks whether the major complex still holds the worker–system–counterpart triad.

Reference F0 (synchronous triad, n=3): W'=S, S'=W∧C, C'=S — triadic, Φ_MIP=2.0.
F_slow (half-rate mediator, n=4): clock K toggles; the mediator recomputes W∧C only on K-ticks and holds
otherwise; parties update every step.
F_held (zero-rate control, n=4): the mediator never recomputes (S'=S); the parties copy a frozen mediator.

Hypotheses (fixed before computing, see hypotheses.md):
  H1 control — F0 reads triadic, Φ=2.0.
  H2 — F_slow keeps {W,S,C} in the major complex (the half-rate mediator still binds).
  H3 — the clock K is a spectator (not in F_slow's core).
  H4 — F_slow's core Φ < 2.0 (slowing lowers integration).
  H5 — F_held factors (a never-committing mediator cannot bind the triad).

Validation gap: in-silico Boolean models with exact Φ; evidence about how a mediator's update rate shapes
irreducibility, not a measurement of any organization.

Run:  python -m org_frontier.questions.q207_slow_mediator.probe_slow_mediator
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict, major_complex  # noqa: E402
from org_frontier.classifier.classifier import PHI_EPS  # noqa: E402

TRIAD = ("W", "S", "C")
QUAD = ("W", "S", "C", "K")

# F0: synchronous conjunctive triad
F0 = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
# F_slow: clock K gates the mediator's recompute; parties update every step
F_slow = [
    lambda x: x[1],                                  # W' = S
    lambda x: (x[0] & x[2]) if x[3] else x[1],       # S' = W∧C on a K-tick, else hold
    lambda x: x[1],                                  # C' = S
    lambda x: 1 - x[3],                              # K' = ¬K
]
# F_held: mediator never recomputes (S'=S); parties copy the frozen mediator
F_held = [
    lambda x: x[1],        # W' = S
    lambda x: x[1],        # S' = S  (frozen)
    lambda x: x[1],        # C' = S
    lambda x: 1 - x[3],   # K' = ¬K
]


def main():
    print("PROBE 361 (Q207) — half-rate mediator and the triad")
    print("=" * 78)

    # ---- H1 instrument control ----
    v0 = verdict(F0, TRIAD)
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print("  H1 control  F0 synchronous triad : %s Φ=%.6f %s"
          % (v0.structure, v0.max_phi, "PASS" if ctrl else "FAIL"))
    assert ctrl, "instrument control failed; aborting"

    # ---- F_slow: verdict + major complex ----
    vs = verdict(F_slow, QUAD)
    core_s, phi_s = major_complex(F_slow, QUAD)
    triad_in = all(p in core_s for p in ("W", "S", "C"))
    k_in = "K" in core_s
    print("  F_slow half-rate mediator        : %s Φ=%.3f" % (vs.structure, vs.max_phi))
    print("  F_slow major complex             : core=%s Φ=%.3f" % (core_s, phi_s))

    # ---- F_held: zero-rate control ----
    vh = verdict(F_held, QUAD)
    core_h, phi_h = major_complex(F_held, QUAD)
    triad_in_h = all(p in core_h for p in ("W", "S", "C"))
    print("  F_held frozen mediator           : %s Φ=%.3f  core=%s Φ=%.3f"
          % (vh.structure, vh.max_phi, core_h, phi_h))

    print("=" * 78)
    h2 = triad_in and vs.structure == "triadic"
    h3 = not k_in
    h4 = phi_s < 2.0 - PHI_EPS
    h5 = vh.structure == "dyadic" or not triad_in_h
    print("  H2 (half-rate mediator keeps {W,S,C} in the core): %s"
          % ("SUPPORTED" if h2 else "REFUTED"))
    print("  H3 (the gating clock K is a spectator, not in the core): %s"
          % ("SUPPORTED" if h3 else "REFUTED"))
    print("  H4 (half-rate mediation lowers core Φ below 2.0): %s"
          % ("SUPPORTED" if h4 else "REFUTED"))
    print("  H5 (a never-committing mediator factors): %s"
          % ("SUPPORTED" if h5 else "REFUTED"))
    print("=" * 78)


if __name__ == "__main__":
    main()
