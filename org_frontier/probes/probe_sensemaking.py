"""Probe 72 (#28) — is algorithm sensemaking dyadic across a family?

Question: algorithm sensemaking is a process inside the worker, not a joint determination over two
parties. Probe 31 placed one sensemaking form dyadic; does that hold across a family? Hypothesis: yes;
an internal process that interprets the system for the worker, with no third party committed jointly,
is dyadic. Method: build several internal-process forms (the worker has a sensemaking node P that
processes the system; the counterpart is unconstituted or uncoupled) and classify.

Nodes: 0=W, 1=S, 2=C, 3=P (the worker's sensemaking process).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_sensemaking
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C", "P")

FORMS = {
    # P processes S; worker acts on P; C unconstituted (self-loop)
    "process_only":    [lambda x: x[3], lambda x: x[0], lambda x: x[2], lambda x: x[1]],
    # P integrates S over the worker's own state; still no third-party joint determination
    "reflective":      [lambda x: x[3], lambda x: x[0], lambda x: x[2], lambda x: x[1] & x[0]],
    # P present, S conveys (relay), C reads S but no joint commit
    "process_relay":   [lambda x: x[3], lambda x: x[0], lambda x: x[1], lambda x: x[1]],
}


def main():
    print("PROBE 72 (#28) — algorithm sensemaking across a family")
    print("=" * 78)
    all_dyadic = True
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        all_dyadic = all_dyadic and v.structure == "dyadic"
        print(f"  {k:<16} {v.structure:<8} Φ={v.max_phi:.3f}  core={core}")
    print("=" * 78)
    print(f"  all sensemaking forms dyadic: {all_dyadic}")
    print("  Reading: a process inside the worker that interprets the system, with no third party")
    print("  jointly committed, is dyadic — sensemaking is a worker-side construct, not algorithmacy.")
    print("=" * 78)


if __name__ == "__main__":
    main()
