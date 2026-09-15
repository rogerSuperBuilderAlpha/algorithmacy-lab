"""Probe — Serres H3: the excluded third, included.

Question.  Serres (1982: 8, 21): a parasite is "a break in a message"; "the bit of noise, the small random
           element, transforms one system or one order into another." Noise on the A–B channel, from outside
           (a coin) and from the system itself (N' = A ∧ B). Is the noise in the complex, and what does it do
           to the pair's Φ?
Hypothesis. H3: exogenous — core {A, B}, Φ < 2; endogenous — N in the core.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.serres.probe_serres_third
"""

from org_frontier.thinkers.serres import forms as F


def main():
    print("Serres H3 — noise from outside, and the system's own")
    control = F.run_control(stochastic=True)
    recs = {"dyad": F.evaluate("dyad"), "dyad_exo": F.evaluate_exo(), "dyad_endo": F.evaluate("dyad_endo")}
    exo = recs["dyad_exo"]
    a = set(exo["core"]) == {"A", "B"} and exo["core_phi"] < 2.0 - 1e-6
    b = "N" in recs["dyad_endo"]["core"]
    print("  exogenous: core {A,B} with Φ<2 → %s (Φ=%.3f)   endogenous: N in core → %s (core=%s)" % (
        a, exo["core_phi"], b, tuple(recs["dyad_endo"]["core"])))
    n = int(a) + int(b)
    status = "CONFIRMED" if n == 2 else ("PARTIAL" if n == 1 else "REFUTED")
    print("H3 (noise from outside is excluded and felt; the system's own noise is included): %s" % status)
    F.save("probe_serres_third", {"control": control, "forms": recs, "H3": status})


if __name__ == "__main__":
    main()
