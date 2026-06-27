"""Probe 363 (Q209) — is rate-1 the unique binding cadence?

q207 showed a period-2 mediator factors the triad. This sweeps the commit period p = 1, 2, 3, 4 (the
mediator gated by a mod-p counter that lets it recompute W∧C once per period and hold otherwise) and asks
whether the triad factors at every p ≥ 2, and how the surviving counter's Φ scales with the period. It is
the period-sweep analog of q208's latency-depth sweep.

F_1 (n=3): synchronous triad. F_2 (n=4): 1-bit toggle clock (q207's form). F_3, F_4 (n=5): 2-bit counter
cycling mod 3 / mod 4; the mediator commits when the counter reads zero.

Hypotheses (fixed before computing, see hypotheses.md):
  H1 control — F_1 reads triadic, Φ=2.0.
  H2 — F_p is dyadic at every p=2,3,4 (rate-1 is the unique binding cadence).
  H3 — the triad leaves the core at every p≥2 (the counter is the surviving complex).
  H4 — the surviving counter's Φ is non-decreasing in period.
  H5 — whole-system Φ_MIP is zero at every p≥2.

Validation gap: in-silico Boolean models with exact Φ; evidence about how a mediator's commit cadence
shapes irreducibility, not a measurement of any organization.

Run:  python -m org_frontier.questions.q209_commit_period.probe_commit_period
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


def form(p):
    """(rules, labels) for the commit-period-p form."""
    if p == 1:
        return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], TRIAD
    if p == 2:
        # 1-bit toggle counter K (index 3); commit when K marks the reset (K==1 here, as in q207)
        labels = ("W", "S", "C", "K")
        rules = [
            lambda x: x[1],                                   # W' = S
            lambda x: (x[0] & x[2]) if x[3] else x[1],        # S' = W∧C on the tick, else hold
            lambda x: x[1],                                   # C' = S
            lambda x: 1 - x[3],                              # K' = ¬K
        ]
        return rules, labels
    # p in {3,4}: 2-bit counter c0 (LSB, index 3), c1 (MSB, index 4), increment mod p; commit when counter==0
    labels = ("W", "S", "C", "c0", "c1")

    def nxt_c0(x, p=p):
        v = x[3] + 2 * x[4]
        return ((v + 1) % p) & 1

    def nxt_c1(x, p=p):
        v = x[3] + 2 * x[4]
        return ((v + 1) % p >> 1) & 1

    rules = [
        lambda x: x[1],                                                  # W' = S
        lambda x: (x[0] & x[2]) if (x[3] == 0 and x[4] == 0) else x[1],  # S' = W∧C at counter==0, else hold
        lambda x: x[1],                                                  # C' = S
        nxt_c0,
        nxt_c1,
    ]
    return rules, labels


def main():
    print("PROBE 363 (Q209) — is rate-1 the unique binding cadence?")
    print("=" * 80)

    # ---- H1 instrument control ----
    r1, l1 = form(1)
    v1 = verdict(r1, l1)
    ctrl = v1.structure == "triadic" and abs(v1.max_phi - 2.0) < 1e-6
    print("  H1 control  F_1 synchronous triad : %s Φ=%.6f %s"
          % (v1.structure, v1.max_phi, "PASS" if ctrl else "FAIL"))
    assert ctrl, "instrument control failed; aborting"

    rows = []  # (p, n, structure, max_phi, core, core_phi, triad_in)
    for p in (1, 2, 3, 4):
        r, l = form(p)
        v = verdict(r, l)
        core, core_phi = major_complex(r, l)
        triad_in = all(t in core for t in TRIAD)
        rows.append((p, len(l), v.structure, v.max_phi, core, core_phi, triad_in))
        print("  p=%d (n=%d)  %-8s wholeΦ_MIP=%.4f  core=%s coreΦ=%.3f"
              % (p, len(l), v.structure, v.max_phi, core, core_phi))

    print("=" * 80)
    structs = {r[0]: r[2] for r in rows}
    phis = {r[0]: r[3] for r in rows}
    core_phis = {r[0]: r[5] for r in rows}
    triad_in = {r[0]: r[6] for r in rows}
    h2 = all(structs[p] == "dyadic" for p in (2, 3, 4))
    h3 = all(not triad_in[p] for p in (2, 3, 4))
    h4 = core_phis[2] <= core_phis[3] + PHI_EPS and core_phis[3] <= core_phis[4] + PHI_EPS
    h5 = all(phis[p] <= PHI_EPS for p in (2, 3, 4))
    print("  surviving core Φ by period p=2,3,4: %.3f, %.3f, %.3f"
          % (core_phis[2], core_phis[3], core_phis[4]))
    print("  H2 (rate-1 is the unique binding cadence: p>=2 all dyadic): %s"
          % ("SUPPORTED" if h2 else "REFUTED"))
    print("  H3 (the triad leaves the core at every p>=2): %s"
          % ("SUPPORTED" if h3 else "REFUTED"))
    print("  H4 (the surviving counter's Φ is non-decreasing in period): %s"
          % ("SUPPORTED" if h4 else "REFUTED"))
    print("  H5 (whole-system Φ_MIP is zero at every p>=2): %s"
          % ("SUPPORTED" if h5 else "REFUTED"))
    print("=" * 80)


if __name__ == "__main__":
    main()
