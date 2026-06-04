"""Probe 71 (#27) — does second-order theory of mind add to the core?

Question: the worker holds a model M1 of the counterpart and a second-order model M2 (a model of the
counterpart's model of the worker). Does M2 join the irreducible core, or stay a deeper sink?
Hypothesis: M2 is read-only relative to the coordination and stays out; only M1, which the worker acts
on, is in (cf. Probe 4). Method: build W, S, C, M1, M2 with M1'=S, M2'=M1, the worker acting on the
first-order model (W'=S∧M1), and read the major complex.

Nodes: 0=W, 1=S, 2=C, 3=M1, 4=M2.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_second_order_tom
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C", "M1", "M2")

FORMS = {
    # worker acts on the first-order model; M2 models M1 but is unused
    "m2_unused":   [lambda x: x[1] & x[3], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1], lambda x: x[3]],
    # worker also acts on the second-order model
    "m2_used":     [lambda x: x[1] & x[3] & x[4], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1], lambda x: x[3]],
}


def main():
    print("PROBE 71 (#27) — second-order theory of mind")
    print("=" * 80)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        print(f"  {k:<12} whole {v.structure:<8} core={core}  "
              f"M1 in: {core and 'M1' in core}  M2 in: {core and 'M2' in core}")
    print("=" * 80)
    print("  Reading: whether the deeper model M2 enters the core says if recursive mentalizing is")
    print("  structural or just a worker burden. A node the worker does not act on stays a sink.")
    print("=" * 80)


if __name__ == "__main__":
    main()
