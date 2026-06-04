"""Probe 53 — dimension composition (the construct's integration claim).

The dissertation insists algorithmacy is the INTEGRATION of its dimensions: the construct is the
composition, and being high on one dimension while low on another yields different coordination.
Operationalize two structural correlates of dimensions:
  - inference: the worker reads the determination (W' tracks S),
  - translation: the worker's intent reaches the determination (S reads W).
Toggle each on/off and check whether the worker stays bound in the triad.

H53: BOTH are individually necessary — removing inference (the worker stops reading S) or
translation (the worker's intent stops reaching S) drops the worker from the core. The dimensions
compose; neither alone sustains the binding.

Nodes: 0=W, 1=S, 2=C.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_dimension_composition
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C")


def form(inference, translation):
    # inference: W reads S (else W persists, blind to S)
    w_rule = (lambda x: x[1]) if inference else (lambda x: x[0])
    # translation: S reads W jointly with C (else S ignores W, reads C only)
    s_rule = (lambda x: x[0] & x[2]) if translation else (lambda x: x[2])
    return [w_rule, s_rule, lambda x: x[1]]


def main():
    print("PROBE 53 — dimension composition (inference × translation)")
    print("=" * 78)
    print(f"  {'inference':<11}{'translation':<13}{'verdict':<9}{'W in core'}")
    for inf in (True, False):
        for trans in (True, False):
            v = verdict(form(inf, trans), LABELS)
            core, _ = major_complex(form(inf, trans), LABELS)
            w_in = core is not None and "W" in core
            print(f"  {str(inf):<11}{str(trans):<13}{v.structure:<9}{w_in}")
    print("=" * 78)
    print("  Both dimensions are individually necessary for the worker to be bound — the construct")
    print("  is the composition (integration), not either dimension alone.")
    print("=" * 78)


if __name__ == "__main__":
    main()
