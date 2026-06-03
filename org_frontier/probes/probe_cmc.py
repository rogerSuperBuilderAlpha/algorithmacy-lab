"""Probe 19 — CMC (a conveying medium) vs algorithmacy.

Discriminant neighbor: computer-mediated-communication competence stands opposite a medium that
CONVEYS (transmits, scores, displays) but does not commit a joint determination across both parties.
The dissertation's intermediary-vs-mediator distinction: a conveyor is a wire and should factor.

H19: conveying-medium forms (S relays/echoes without a joint determination) are dyadic, even though
a system sits between the parties. Only a joint determination (algorithmacy) is triadic.

Nodes: 0=W, 1=S, 2=C.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_cmc
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C")

FORMS = {
    # one-way conveyor: W -> S -> C (S carries W's signal; nothing commits a joint determination)
    "conveyor_oneway": [lambda x: x[0], lambda x: x[0], lambda x: x[1]],
    # echo medium: S mirrors the worker; counterpart reads the mirror
    "conveyor_echo":   [lambda x: x[1], lambda x: x[0], lambda x: x[1]],
    # scoreboard: S displays an aggregate the worker set; C reads it (no commit over C)
    "conveyor_score":  [lambda x: x[0], lambda x: x[0] | x[1], lambda x: x[1]],
    # contrast: genuine joint determination (algorithmacy)
    "algo_joint":      [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
}


def main():
    print("PROBE 19 — conveying medium (CMC) vs joint determination (algorithmacy)")
    print("=" * 78)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        print(f"  {k:<18} {v.structure:<8} Φ={v.max_phi:.3f}  core={core}")
    print("=" * 78)


if __name__ == "__main__":
    main()
