"""Probe 22 — worker competition (the gig labor market).

Two workers compete for one counterpart through a platform. Mirror of the counterpart-coalition and
substitutable-counterpart probes, on the worker side: does worker substitutability factor the form,
and does worker solidarity relocate the core?

H22: by symmetry with the counterpart results — substitutable workers (the platform matches either)
factor to dyadic; only an all-required match stays triadic; and a worker coalition (W1↔W2 channel)
relocates the core to {W1,W2}.

Nodes: 0=W1, 1=S, 2=C, 3=W2.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_competition
"""

from .lib import verdict, major_complex

LABELS = ("W1", "S", "C", "W2")

FORMS = {
    # substitutable workers: platform matches C with EITHER worker.
    "substitutable_workers": [lambda x: x[1], lambda x: (x[0] | x[3]) & x[2], lambda x: x[1], lambda x: x[1]],
    # both required: the match needs both workers and the counterpart.
    "both_required":         [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]],
    # worker coalition: the two workers also coordinate directly (union), each matched via S with C.
    "worker_coalition":      [lambda x: x[1] | x[3], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1] | x[0]],
}


def main():
    print("PROBE 22 — worker competition")
    print("=" * 84)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        print(f"  {k:<22} {v.structure:<8} Φ={v.max_phi:.3f}  core={core}")
    print("=" * 84)


if __name__ == "__main__":
    main()
