"""Probe 31 — a comprehensive discriminant map.

Paper 1 distinguishes algorithmacy from a family of neighbor constructs. Earlier probes did HMC (15),
CMC (19), AI-MC (20) piecemeal. This assembles a single map: a representative form for each neighbor
construct, classified, so the structural signature of the whole construct space is visible at once.

H31: every dyadic-unit construct (CMC, HMC, AI literacy as a knowledge-state, algorithm sensemaking
as an internal process) classifies dyadic; only algorithmacy and the structurally-triadic case
(AI-MC, the known edge case) classify triadic. The verdict is a clean map of the construct space,
with AI-MC the one boundary case flagged.

Nodes vary per form; labels given per entry.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_discriminant_map
"""

from .lib import verdict

# (construct, expected family, labels, rules)
MAP = [
    ("CMC competence",      "dyadic", ("W", "S", "C"),
     [lambda x: x[0], lambda x: x[0], lambda x: x[1]]),                       # conveying medium
    ("HMC",                 "dyadic", ("W", "S", "C"),
     [lambda x: x[1], lambda x: x[0], lambda x: x[2]]),                       # system as partner
    ("AI literacy (state)", "dyadic", ("W", "S", "C"),
     [lambda x: x[1], lambda x: x[0], lambda x: x[2]]),                       # knowledge-state, C uncoupled
    ("algorithm sensemaking", "dyadic", ("W", "S", "C"),
     [lambda x: x[1] & x[0], lambda x: x[0], lambda x: x[2]]),                # internal process in W
    ("AI-MC (edge case)",   "triadic", ("W", "A", "C"),
     [lambda x: x[2], lambda x: x[0], lambda x: x[1]]),                       # W->A->C loop
    ("algorithmacy",        "triadic", ("W", "S", "C"),
     [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]),                # joint determination
]


def main():
    print("PROBE 31 — discriminant map of the construct space")
    print("=" * 74)
    print(f"  {'construct':<24}{'verdict':<9}{'expected':<9}{'match'}")
    ok = 0
    for name, exp, labels, rules in MAP:
        v = verdict(rules, labels)
        m = v.structure == exp
        ok += m
        print(f"  {name:<24}{v.structure:<9}{exp:<9}{'ok' if m else 'MISMATCH'}")
    print("=" * 74)
    print(f"  {ok}/{len(MAP)} match expected family. AI-MC is the one structural boundary case:")
    print("  it is triadic by structure though the dissertation treats it as dyadic-by-unit.")
    print("=" * 74)


if __name__ == "__main__":
    main()
