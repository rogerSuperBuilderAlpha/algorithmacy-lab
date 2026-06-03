"""Probe 40 — broadcast topology (one-to-many).

A worker reaches many counterparts through a system that broadcasts (fans out) without a joint
determination over them. Does broadcast factor into independent dyads, or is it triadic?

H40: pure broadcast (the system relays the worker to each counterpart independently) factors —
each worker–counterpart pair is its own dyad through the system. Only a joint determination over the
counterparts is triadic.

Nodes: 0=W, 1=S, 2=C1, 3=C2.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_broadcast
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C1", "C2")

FORMS = {
    # broadcast: S relays the worker to both counterparts; no joint determination over them.
    "broadcast_relay": [lambda x: x[1], lambda x: x[0], lambda x: x[1], lambda x: x[1]],
    # broadcast with per-counterpart matching but independent (still no joint over C1,C2)
    "broadcast_match": [lambda x: x[1], lambda x: x[0], lambda x: x[1] & x[2], lambda x: x[1] & x[3]],
    # joint: the determination reads all counterparts together (the pool)
    "joint_pool":      [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]],
}


def main():
    print("PROBE 40 — broadcast topology")
    print("=" * 78)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        print(f"  {k:<18} {v.structure:<8} Φ={v.max_phi:.3f}  core={core}")
    print("=" * 78)


if __name__ == "__main__":
    main()
