"""Probe 4 — inferential dimension (the worker's internal model of the counterpart).

The inferential dimension of algorithmacy: the worker reads observed outcomes back to the hidden
counterpart, building a folk theory. Model an internal node M (the worker's estimate of C) that
updates from the system's determinations (M' = S). Does M join the irreducible core?

H4: M joins the core only if the worker ACTS on its inference (W reads M, so M -> W -> S closes a
loop). An inference that is computed but unused (W ignores M) stays a read-only sink, outside.

Nodes: 0=W, 1=S, 2=C, 3=M.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_inference
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C", "M")

FORMS = {
    # inference computed but unused: M tracks S, but the worker acts reactively (W' = S).
    "inference_unused": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
    # inference used: the worker acts on its model (W' = M), M tracks the determination (M' = S).
    "inference_used":   [lambda x: x[3], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
    # inference used + blended: worker combines reaction and model (W' = S AND M).
    "inference_blended": [lambda x: x[1] & x[3], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
}


def main():
    print("PROBE 4 — inferential dimension (folk-theory node M)")
    print("=" * 84)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        m_in = core is not None and "M" in core
        print(f"  {k:<18} whole-system {v.structure:<8} Φ={v.max_phi:.3f}   core={core} Φ={phi:.3f}   "
              f"M in core: {m_in}")
    print("=" * 84)


if __name__ == "__main__":
    main()
