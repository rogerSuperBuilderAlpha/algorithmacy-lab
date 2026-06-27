"""Probe 362 (Q208) — how deep can represented latency go before the triad factors?

q205 showed that one represented buffer keeps the conjunctive triad triadic (whole-system Φ_MIP 2.0→1.0)
with the buffer in the core and the worker displaced. This sweeps the buffer depth k = 0, 1, 2, 3 (a delay
line B1→…→Bk on the mediator's feedback to the parties) and reads, at each depth, the verdict, the
whole-system Φ_MIP, and the major complex — turning q205's single point into a decay curve and locating any
depth at which the represented delay finally factors the triad.

F_k (n = 3 + k): S' = W∧C every step; B1' = S, Bj' = B(j-1); the parties read the last buffer (W' = Bk,
C' = Bk), so the mediator reaches them k steps late. F_0 is the synchronous triad.

Hypotheses (fixed before computing, see hypotheses.md):
  H1 control — F_0 reads triadic, Φ=2.0.
  H2 — F_k is triadic at every k=1,2,3 (represented latency never factors).
  H3 — whole-system Φ_MIP strictly decreases with k.
  H4 — every buffer is in the major complex at every depth.
  H5 — the worker stays out of the major complex for all k≥1.

Validation gap: in-silico Boolean models with exact Φ; evidence about how represented delay shapes
irreducibility, not a measurement of any organization.

Run:  python -m org_frontier.questions.q208_latency_depth.probe_latency_depth
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict, major_complex  # noqa: E402
from org_frontier.classifier.classifier import PHI_EPS  # noqa: E402


def form(k):
    """(rules, labels) for the depth-k buffered triad. n = 3 + k."""
    labels = ["W", "S", "C"] + ["B%d" % j for j in range(1, k + 1)]
    rules = []
    rules.append(lambda x: x[1] if k == 0 else x[2 + k])   # W' = S (k=0) or last buffer Bk
    rules.append(lambda x: x[0] & x[2])                    # S' = W ∧ C
    rules.append(lambda x: x[1] if k == 0 else x[2 + k])   # C' = S (k=0) or last buffer Bk
    # buffers: B1' = S (index 1); Bj' = B(j-1) (index 2 + (j-1))
    for j in range(1, k + 1):
        src = 1 if j == 1 else (2 + (j - 1))
        rules.append(lambda x, s=src: x[s])
    return rules, tuple(labels)


def main():
    import sys
    # --ci runs k=0,1,2 only (~30s); k=2 already shows the dip-and-recovery. Full run adds k=3 (n=6, slow).
    kmax = 2 if "--ci" in sys.argv[1:] else 3
    deep = list(range(1, kmax + 1))
    print("PROBE 362 (Q208) — depth of represented latency vs the triad")
    print("=" * 80)

    # ---- H1 instrument control (k=0) ----
    r0, l0 = form(0)
    v0 = verdict(r0, l0)
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print("  H1 control  F_0 synchronous triad : %s Φ=%.6f %s"
          % (v0.structure, v0.max_phi, "PASS" if ctrl else "FAIL"))
    assert ctrl, "instrument control failed; aborting"

    rows = []  # (k, n, structure, max_phi, core, core_phi)
    for k in range(0, kmax + 1):
        r, l = form(k)
        v = verdict(r, l)
        core, core_phi = major_complex(r, l)
        rows.append((k, len(l), v.structure, v.max_phi, core, core_phi))
        print("  k=%d (n=%d)  %-8s wholeΦ_MIP=%.4f  core=%s coreΦ=%.3f"
              % (k, len(l), v.structure, v.max_phi, core, core_phi))

    print("=" * 80)
    phis = [r[3] for r in rows]
    structs = [r[2] for r in rows]
    cores = {r[0]: r[4] for r in rows}
    h2 = all(structs[k] == "triadic" for k in deep)
    h3 = all(phis[k] > phis[k + 1] + PHI_EPS for k in range(kmax))
    h4 = all(all(("B%d" % j) in cores[k] for j in range(1, k + 1)) for k in deep)
    h5 = all("W" not in cores[k] for k in deep)
    print("  whole-system Φ_MIP by depth k=0..%d: %s" % (kmax, ", ".join("%.4f" % p for p in phis)))
    print("  H2 (represented latency stays triadic at every depth): %s"
          % ("SUPPORTED" if h2 else "REFUTED"))
    print("  H3 (whole-system Φ_MIP strictly decreases with depth): %s"
          % ("SUPPORTED" if h3 else "REFUTED"))
    print("  H4 (every buffer is in the major complex at every depth): %s"
          % ("SUPPORTED" if h4 else "REFUTED"))
    print("  H5 (the worker stays out of the major complex for all k>=1): %s"
          % ("SUPPORTED" if h5 else "REFUTED"))
    print("=" * 80)


if __name__ == "__main__":
    main()
