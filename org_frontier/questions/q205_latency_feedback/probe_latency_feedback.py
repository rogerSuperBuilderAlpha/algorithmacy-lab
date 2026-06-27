"""Probe 359 (Q205) — does latency in the mediator's feedback path hide integration from one-step Φ?

Question: when a mediator's effect on the parties arrives one step late, does exact IIT-4.0 Φ still read
the coordination as integrated, and does that depend on whether the delay is given its own node?

Reference form F0 (immediate triad, n=3): W'=S, S'=W∧C, C'=S — known triadic, Φ_MIP=2.0.
F1 (represented latency, n=4): a buffer B holds S's last output and the parties read B, so the mediator's
feedback is one step late: W'=B, S'=W∧C, C'=B, B'=S.
F2 (hidden latency): run F1 but estimate a one-step state-by-node TPM over only (W,S,C), marginalizing B.
estF0 (estimation control): estimate the same way from F0, with no latency.

Hypotheses (fixed before computing, see hypotheses.md):
  H1 instrument control — F0 reads triadic, Φ=2.0.
  H2 — represented latency stays triadic (F1 Φ>0).
  H3 — the buffer B is in F1's major complex.
  H4 — hidden latency factors: F2 reads dyadic while F1 is triadic.
  H5 — estimation alone does not factor: estF0 reads triadic.

Validation gap: in-silico Boolean models with exact Φ; evidence about the instrument's blind spot to
unrepresented lag, not a measurement of any organization.

Run:  python -m org_frontier.questions.q205_latency_feedback.probe_latency_feedback
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np  # noqa: E402

from org_frontier.probes.lib import verdict, major_complex  # noqa: E402
from org_frontier.classifier.classifier import classify, PHI_EPS  # noqa: E402

# F0: immediate triad, labels (W, S, C)
F0 = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
# F1: one-step latency via buffer B, labels (W, S, C, B); W'=B, S'=W∧C, C'=B, B'=S
F1 = [lambda x: x[3], lambda x: x[0] & x[2], lambda x: x[3], lambda x: x[1]]

STEPS, WARMUP, FLIP, SEED = 20000, 200, 0.05, 0


def simulate(rules, n, units, steps=STEPS, warmup=WARMUP, flip=FLIP, seed=SEED):
    """Run the noisy Boolean dynamics; return the recorded (steps x len(units)) array over `units`."""
    rng = np.random.default_rng(seed)
    x = rng.integers(0, 2, n).tolist()
    rec = []
    for t in range(steps + warmup):
        nxt = [int(r(x)) ^ int(rng.random() < flip) for r in rules]
        x = nxt
        if t >= warmup:
            rec.append([x[u] for u in units])
    return np.array(rec, dtype=int)


def estimate_tpm(rec):
    """One-step state-by-node TPM over the recorded units, estimated by counting (as q204 does)."""
    k = rec.shape[1]
    counts = np.zeros((2 ** k, k))
    tot = np.zeros(2 ** k)
    for t in range(len(rec) - 1):
        s = int(sum(rec[t, j] << j for j in range(k)))
        tot[s] += 1
        counts[s] += rec[t + 1]
    tpm = np.divide(counts, tot[:, None], out=np.full((2 ** k, k), 0.5), where=tot[:, None] > 0)
    return tpm


def infer_cm(tpm):
    """Node i feeds node j iff flipping bit i of some state changes column j of the TPM."""
    k = tpm.shape[1]
    cm = np.zeros((k, k), dtype=int)
    for j in range(k):
        for i in range(k):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-6 for s in range(2 ** k)):
                cm[i, j] = 1
    return cm


def classify_estimated(rules, n, units, labels):
    tpm = estimate_tpm(simulate(rules, n, units))
    return classify(tpm, infer_cm(tpm), labels=labels)


def main():
    print("PROBE 359 (Q205) — latency in the mediator's feedback path vs one-step Φ")
    print("=" * 82)

    # ---- H1: instrument control ----
    v0 = verdict(F0, ("W", "S", "C"))
    ctrl_ok = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(f"  H1 control  F0 immediate triad     : {v0.structure:<8} Φ={v0.max_phi:.3f}  "
          f"{'PASS' if ctrl_ok else 'FAIL'}")
    assert ctrl_ok, "instrument control failed; aborting"

    # ---- H2 + H3: represented latency (exact, n=4) ----
    v1 = verdict(F1, ("W", "S", "C", "B"))
    core, core_phi = major_complex(F1, ("W", "S", "C", "B"))
    b_in_core = "B" in core
    print(f"  H2 represented latency  F1 (n=4)    : {v1.structure:<8} Φ={v1.max_phi:.3f}")
    print(f"  H3 major complex of F1             : core={core}  Φ={core_phi:.3f}  "
          f"(B in core: {b_in_core})")

    # ---- H4: hidden latency (estimate one-step TPM over (W,S,C) only) ----
    v2 = classify_estimated(F1, 4, units=(0, 1, 2), labels=("W", "S", "C"))
    print(f"  H4 hidden latency  F2 est (W,S,C)   : {v2.structure:<8} Φ={v2.max_phi:.3f}")

    # ---- H5: estimation control (estimate the same way from F0, no latency) ----
    v3 = classify_estimated(F0, 3, units=(0, 1, 2), labels=("W", "S", "C"))
    print(f"  H5 estimation control  estF0        : {v3.structure:<8} Φ={v3.max_phi:.3f}")

    print("=" * 82)
    h2 = v1.structure == "triadic" and v1.max_phi > PHI_EPS
    h3 = b_in_core
    h4 = v2.structure == "dyadic" and v1.structure == "triadic"
    h5 = v3.structure == "triadic" and v3.max_phi > PHI_EPS
    print(f"  H2 (represented latency stays triadic): {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (the delay node B is in the core): {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (hidden latency hides integration: F2 dyadic, F1 triadic): "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (estimation alone preserves integration: estF0 triadic): "
          f"{'SUPPORTED' if h5 else 'REFUTED'}")
    print("=" * 82)
    print("  Reading: a one-step Φ misses lagged coordination only when the delay is left out of the "
          "model; representing the delay as a node recovers the integration the q204 caveat flags.")
    print("=" * 82)


if __name__ == "__main__":
    main()
