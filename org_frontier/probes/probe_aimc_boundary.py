"""Probe 70 (#26) — is the AI-MC/algorithmacy boundary recoverable by a timescale criterion?

Question: Probe 20 found the worker→AI→counterpart loop triadic, indistinguishable from algorithmacy;
the distinction was a unit-of-analysis choice. Can a timescale criterion recover it? Hypothesis: if the
AI updates within the worker's own step (absorbed into the worker's production), the form collapses to
a two-party worker–counterpart system; only when the AI is a peer element on the loop's timescale is it
triadic. Method: classify the 3-element loop (A as a separate party), then build the effective two-party
system with A absorbed into the worker (sequential within-step composition) and classify that.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_aimc_boundary
"""

from org_frontier.classifier.classifier import classify_rules

# 3-element loop: 0=W, 1=A (AI), 2=C.  W'=C, A'=W, C'=A
SEPARATE = [lambda x: x[2], lambda x: x[0], lambda x: x[1]]

# A absorbed into the worker (A computes within W's step): effective 2-party system W,C.
# Within a step A := W, then C reads the updated A (= W); W reads C. So C' = W, W' = C.
ABSORBED = [lambda x: x[1], lambda x: x[0]]  # nodes (W, C): W'=C, C'=W


def main():
    print("PROBE 70 (#26) — AI-MC boundary by timescale")
    print("=" * 74)
    v3 = classify_rules(SEPARATE, labels=("W", "A", "C"))
    print(f"  A as a separate party (peer timescale): {v3.structure}  Φ={v3.max_phi:.3f}  "
          f"(3 elements: W,A,C)")
    v2 = classify_rules(ABSORBED, labels=("W", "C"))
    print(f"  A absorbed into the worker (fast):       {v2.structure}  Φ={v2.max_phi:.3f}  "
          f"(2 elements: W,C)")
    print("=" * 74)
    print("  Reading: the Φ>0 verdict does NOT flip — the absorbed two-element loop is still")
    print("  irreducible (Φ=2.0). So a timescale criterion does not recover the distinction through")
    print("  the verdict; what differs is the major-complex ELEMENT COUNT (2 vs 3). The construct's")
    print("  'triadic' must mean an irreducible complex containing a genuine third party, not merely")
    print("  Φ>0. This sharpens Probe 20: AI-MC vs algorithmacy is a counting/boundary question the")
    print("  scalar Φ verdict cannot settle on its own.")
    print("=" * 74)


if __name__ == "__main__":
    main()
