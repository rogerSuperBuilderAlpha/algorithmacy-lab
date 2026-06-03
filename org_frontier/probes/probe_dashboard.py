"""Probe 41 — dashboard vs determination (transparency theater).

Platforms often show the worker a metric/dashboard that is not the signal that actually commits her
fate. Split the system into a visible facet Sv (what the worker reads) and a committing facet Sc
(the determination over W and C). Does the worker stay bound when she reads the real determination,
and decouple when she reads a dashboard detached from it?

H41: when the visible signal tracks the committing determination (aligned), the worker is in the
core; when the dashboard is decoupled from the commit (misaligned), the worker reads a self-
referential display and drops out — binding requires reading the signal that actually determines.

Nodes: 0=W, 1=Sv (visible), 2=Sc (committing), 3=C.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_dashboard
"""

from .lib import verdict, major_complex

LABELS = ("W", "Sv", "Sc", "C")

FORMS = {
    # aligned: the visible signal IS the committing determination; worker reads it.
    "aligned":    [lambda x: x[1], lambda x: x[0] & x[3], lambda x: x[0] & x[3], lambda x: x[2]],
    # misaligned: dashboard shows the worker's own input (decoupled from the commit); Sc still commits.
    "misaligned": [lambda x: x[1], lambda x: x[0], lambda x: x[0] & x[3], lambda x: x[2]],
    # partial: dashboard shows a noisy hint of the commit (Sv = Sc OR worker's input)
    "partial":    [lambda x: x[1], lambda x: (x[0] & x[3]) | x[0], lambda x: x[0] & x[3], lambda x: x[2]],
}


def main():
    print("PROBE 41 — dashboard vs determination (transparency theater)")
    print("=" * 80)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        w_in = core is not None and "W" in core
        print(f"  {k:<14} {v.structure:<8} Φ={v.max_phi:.3f}  core={core}  W in core: {w_in}")
    print("=" * 80)


if __name__ == "__main__":
    main()
