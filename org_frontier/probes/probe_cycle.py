"""Probe 39 — is a feedback cycle necessary for the triad?

Graph-theoretic necessity test. A joint determination read acyclically (parties as sources, the
system as a sink) versus the same determination embedded in a feedback cycle. IIT irreducibility is
generally driven by recurrence, so a purely feedforward joint determination should not be triadic.

H39: a directed feedback cycle through the determination is necessary — an acyclic joint
determination (no party reads the system back) is dyadic even though the system reads both parties.

Nodes: 0=W, 1=S, 2=C.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_cycle
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C")

FORMS = {
    # acyclic: W and C are sources (self-loops), S is a sink reading both. No feedback.
    "acyclic_sink":  [lambda x: x[0], lambda x: x[0] & x[2], lambda x: x[2]],
    # one feedback edge: the worker reads S back; counterpart still a source.
    "one_feedback":  [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]],
    # full cycle: both parties read S back (the standard triad).
    "full_cycle":    [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
}


def main():
    print("PROBE 39 — is a feedback cycle necessary for the triad?")
    print("=" * 72)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        print(f"  {k:<16} {v.structure:<8} Φ={v.max_phi:.3f}  core={core}")
    print("=" * 72)


if __name__ == "__main__":
    main()
