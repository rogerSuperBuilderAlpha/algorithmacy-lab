"""Probe 366 (Q212) — must the merging channel run between the mediators?

q211 merged two triads with a direct AND channel between their mediators. This localizes that result. The
same single AND cross-triad channel is moved across three homologous node pairs — mediator (S1↔S2, the q211
baseline), worker (W1↔W2), counterpart (C1↔C2) — and the probe reads which placements produce a major
complex spanning both triads, and at what Φ. In the conjunctive triad the worker and counterpart are
symmetric leaves, so those two channels are expected to agree.

Node order (n=6): W1, S1, C1, W2, S2, C2. Each triad is the plain conjunctive triad except for the one
node pair carrying the AND channel.

Hypotheses (fixed before computing, see hypotheses.md):
  H1 control — single triad triadic Φ=2.0; mediator channel reproduces q211 (spans both, Φ=3.0).
  H2 — the worker-worker channel merges (core spans both triads).
  H3 — the counterpart-counterpart channel merges, matching the worker channel by leaf symmetry.
  H4 — the mediator channel gives the highest core Φ.
  H5 — channel location matters; the three placements are not all identical.

Validation gap: in-silico Boolean models with exact Φ; evidence about where a direct link must sit to bind
two model coordinations, not a measurement of any organization.

Run:  python -m org_frontier.questions.q212_channel_location.probe_channel_location
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


def form(location):
    """Two conjunctive triads with one AND cross-triad channel at the named node pair."""
    if location == "mediator":
        return [
            lambda x: x[1],                  # W1' = S1
            lambda x: (x[0] & x[2]) & x[4],  # S1' = (W1 ∧ C1) ∧ S2
            lambda x: x[1],                  # C1' = S1
            lambda x: x[4],                  # W2' = S2
            lambda x: (x[3] & x[5]) & x[1],  # S2' = (W2 ∧ C2) ∧ S1
            lambda x: x[4],                  # C2' = S2
        ]
    if location == "worker":
        return [
            lambda x: x[1] & x[3],           # W1' = S1 ∧ W2
            lambda x: x[0] & x[2],           # S1' = W1 ∧ C1
            lambda x: x[1],                  # C1' = S1
            lambda x: x[4] & x[0],           # W2' = S2 ∧ W1
            lambda x: x[3] & x[5],           # S2' = W2 ∧ C2
            lambda x: x[4],                  # C2' = S2
        ]
    if location == "counterpart":
        return [
            lambda x: x[1],                  # W1' = S1
            lambda x: x[0] & x[2],           # S1' = W1 ∧ C1
            lambda x: x[1] & x[5],           # C1' = S1 ∧ C2
            lambda x: x[4],                  # W2' = S2
            lambda x: x[3] & x[5],           # S2' = W2 ∧ C2
            lambda x: x[4] & x[2],           # C2' = S2 ∧ C1
        ]
    raise ValueError(location)


def spans_both(core):
    c = set(core)
    return bool(c & TRIAD1) and bool(c & TRIAD2)


def main():
    print("PROBE 366 (Q212) — where must the cross-triad channel sit to merge two triads?")
    print("=" * 80)

    # ---- H1 instrument control ----
    v0 = verdict([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], ("W", "S", "C"))
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print("  H1 control  single triad : %s Φ=%.6f %s"
          % (v0.structure, v0.max_phi, "PASS" if ctrl else "FAIL"))
    assert ctrl, "instrument control failed; aborting"

    res = {}
    for loc in ("mediator", "worker", "counterpart"):
        v = verdict(form(loc), LABELS6)
        core, core_phi = major_complex(form(loc), LABELS6)
        res[loc] = (v.structure, v.max_phi, tuple(core), core_phi, spans_both(core))
        print("  channel@%-11s %-8s wholeΦ_MIP=%.4f  core=%s coreΦ=%.3f spans_both=%s"
              % (loc, v.structure, v.max_phi, tuple(core), core_phi, spans_both(core)))

    print("=" * 80)
    med_phi, med_span = res["mediator"][3], res["mediator"][4]
    wrk_phi, wrk_span = res["worker"][3], res["worker"][4]
    cpt_phi, cpt_span = res["counterpart"][3], res["counterpart"][4]
    h1 = med_span and abs(med_phi - 3.0) < PHI_EPS
    h2 = wrk_span
    h3 = cpt_span and abs(cpt_phi - wrk_phi) < PHI_EPS
    h4 = med_phi > wrk_phi + PHI_EPS and med_phi > cpt_phi + PHI_EPS
    spans = {res[loc][4] for loc in res}
    phis = [round(res[loc][3], 6) for loc in res]
    h5 = len(spans) > 1 or len(set(phis)) > 1
    print("  mediator coreΦ=%.3f span=%s ; worker coreΦ=%.3f span=%s ; counterpart coreΦ=%.3f span=%s"
          % (med_phi, med_span, wrk_phi, wrk_span, cpt_phi, cpt_span))
    print("  H1 (mediator channel reproduces q211: spans both, Φ=3.0): %s"
          % ("SUPPORTED" if h1 else "REFUTED"))
    print("  H2 (worker-worker channel merges): %s" % ("SUPPORTED" if h2 else "REFUTED"))
    print("  H3 (counterpart channel merges, matches worker by symmetry): %s"
          % ("SUPPORTED" if h3 else "REFUTED"))
    print("  H4 (mediator channel gives the highest core Φ): %s" % ("SUPPORTED" if h4 else "REFUTED"))
    print("  H5 (channel location matters): %s" % ("SUPPORTED" if h5 else "REFUTED"))
    print("=" * 80)


if __name__ == "__main__":
    main()
