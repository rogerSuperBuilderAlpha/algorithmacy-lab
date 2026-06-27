"""Probe 365 (Q211) — does a direct mediator-mediator channel merge two triads?

The complement of q210. There two triads shared a counterpart and never merged. Here two complete
conjunctive triads are joined only by a direct channel between their two mediators: S1 reads S2 and S2
reads S1. The channel is swept three ways (none, AND, OR). The probe reads whether the major complex spans
both triads (one merged core) or stays inside one triad, and how the channel rule changes the result.

Node order (n=6): W1, S1, C1, W2, S2, C2.
  triad 1: W1'=S1, C1'=S1, S1'=channel(W1∧C1, S2)
  triad 2: W2'=S2, C2'=S2, S2'=channel(W2∧C2, S1)

Hypotheses (fixed before computing, see hypotheses.md):
  H1 control — single triad triadic Φ=2.0; none channel factors, core is one triad at Φ=2.0.
  H2 — under the AND channel the major complex spans both triads.
  H3 — the merged core is super-additive, Φ > 2.0.
  H4 — the direct channel merges where the shared counterpart (q210) did not.
  H5 — the channel rule matters; AND and OR cores differ.

Validation gap: in-silico Boolean models with exact Φ; evidence about how a direct link binds two model
coordinations, not a measurement of any organization.

Run:  python -m org_frontier.questions.q211_direct_mediator_channel.probe_direct_mediator_channel
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict, major_complex  # noqa: E402
from org_frontier.classifier.classifier import PHI_EPS  # noqa: E402

LABELS6 = ("W1", "S1", "C1", "W2", "S2", "C2")
TRIAD1 = {"W1", "S1", "C1"}
TRIAD2 = {"W2", "S2", "C2"}

# channel(own, other): how mediator i combines its own triad's readiness with the other mediator's state.
CHANNELS = {
    "none": lambda own, other: own,
    "AND":  lambda own, other: own & other,
    "OR":   lambda own, other: own | other,
}


def form(channel):
    ch = CHANNELS[channel]
    return [
        lambda x: x[1],                  # W1' = S1
        lambda x: ch(x[0] & x[2], x[4]),  # S1' = channel(W1 ∧ C1, S2)
        lambda x: x[1],                  # C1' = S1
        lambda x: x[4],                  # W2' = S2
        lambda x: ch(x[3] & x[5], x[1]),  # S2' = channel(W2 ∧ C2, S1)
        lambda x: x[4],                  # C2' = S2
    ]


def spans_both(core):
    c = set(core)
    return bool(c & TRIAD1) and bool(c & TRIAD2)


def main():
    print("PROBE 365 (Q211) — direct mediator-mediator channel: one merged core or two?")
    print("=" * 80)

    # ---- H1 instrument control ----
    v0 = verdict([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], ("W", "S", "C"))
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print("  H1 control  single triad : %s Φ=%.6f %s"
          % (v0.structure, v0.max_phi, "PASS" if ctrl else "FAIL"))
    assert ctrl, "instrument control failed; aborting"

    res = {}
    for name in ("none", "AND", "OR"):
        v = verdict(form(name), LABELS6)
        core, core_phi = major_complex(form(name), LABELS6)
        res[name] = (v.structure, v.max_phi, tuple(core), core_phi, spans_both(core))
        print("  channel=%-4s %-8s wholeΦ_MIP=%.4f  core=%s coreΦ=%.3f spans_both=%s"
              % (name, v.structure, v.max_phi, tuple(core), core_phi, spans_both(core)))

    print("=" * 80)
    and_core, and_phi, and_span = res["AND"][2], res["AND"][3], res["AND"][4]
    or_core, or_phi = res["OR"][2], res["OR"][3]
    h2 = and_span
    h3 = and_phi > 2.0 + PHI_EPS
    h4 = any(res[n][4] for n in ("none", "AND", "OR"))
    h5 = (set(and_core) != set(or_core)) or (abs(and_phi - or_phi) > PHI_EPS)
    print("  AND core Φ = %.3f spans_both=%s ; OR core Φ = %.3f" % (and_phi, and_span, or_phi))
    print("  H2 (AND channel major complex spans both triads): %s"
          % ("SUPPORTED" if h2 else "REFUTED"))
    print("  H3 (merged core is super-additive, Φ > 2.0): %s"
          % ("SUPPORTED" if h3 else "REFUTED"))
    print("  H4 (a direct channel merges where the shared counterpart did not): %s"
          % ("SUPPORTED" if h4 else "REFUTED"))
    print("  H5 (channel rule matters; AND and OR cores differ): %s"
          % ("SUPPORTED" if h5 else "REFUTED"))
    print("=" * 80)


if __name__ == "__main__":
    main()
