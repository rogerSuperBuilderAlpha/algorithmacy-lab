"""Probe 21 — contestability / accountability.

Paper 1's four-feature mediator includes accountability-vacancy: platform determinations are hard to
contest. Operationalize contestability as how much the worker's state is BOUND by the determination
vs free to override it. Bound (W' = S) = uncontestable; increasingly contestable as the worker can
persist or act against S.

H21: an uncontestable determination (worker bound to S) is triadic; as contestability rises (the
worker can ignore/override S), the worker decouples and the form goes dyadic. Accountability-vacancy
is part of what binds the worker into the triad.

Nodes: 0=W, 1=S, 2=C. S' = W ∧ C; C' = S throughout. Only the worker's binding to S varies.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_contestability
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C")

FORMS = {
    # uncontestable: worker fully bound to the determination.
    "bound":          [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
    # weakly contestable: worker can persist (sticky) against S.
    "sticky_appeal":  [lambda x: x[1] | x[0], lambda x: x[0] & x[2], lambda x: x[1]],
    # strongly contestable: worker overrides S when it dislikes the outcome (acts on its own prior).
    "override":       [lambda x: 1 - x[1], lambda x: x[0] & x[2], lambda x: x[1]],
    # fully autonomous: worker ignores S entirely (acts on itself).
    "autonomous":     [lambda x: x[0], lambda x: x[0] & x[2], lambda x: x[1]],
}


def main():
    print("PROBE 21 — contestability / accountability")
    print("=" * 78)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        w_in = core is not None and "W" in core
        print(f"  {k:<16} {v.structure:<8} Φ={v.max_phi:.3f}  core={core}  W in core: {w_in}")
    print("=" * 78)


if __name__ == "__main__":
    main()
