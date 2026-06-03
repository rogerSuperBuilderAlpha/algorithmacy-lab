"""Probe 25 — genuinely joint vs decomposable determination.

Does the triad require a non-decomposable joint determination, or do separate per-party channels
suffice? Compare a single joint mediator (S commits one determination reading both parties) with a
"split mediator" that handles each party on an independent channel that never combines.

H25: only the genuinely joint determination is triadic; a decomposable/split mediation factors,
because the parties are never bound through one irreducible commit.

Forms:
- joint (n=3): S' = W ∧ C; W'=S, C'=S.  (one joint determination)
- split (n=4): S1 handles W, S2 handles C, no combination. W'=S1, C'=S2, S1'=W, S2'=C.
- split_shared_output (n=4): S1, S2 each commit, a reader R = S1 ∧ S2 but parties read their own Si.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_joint
"""

from .lib import verdict, major_complex


def main():
    print("PROBE 25 — joint vs decomposable determination")
    print("=" * 80)
    cases = [
        ("joint", ("W", "S", "C"),
         [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]),
        ("split", ("W", "S1", "C", "S2"),
         [lambda x: x[1], lambda x: x[0], lambda x: x[3], lambda x: x[2]]),
        ("split_shared_out", ("W", "S1", "C", "S2"),
         [lambda x: x[1], lambda x: x[0] & x[3], lambda x: x[3], lambda x: x[2] & x[1]]),
    ]
    for name, labels, rules in cases:
        v = verdict(rules, labels)
        core, phi = major_complex(rules, labels)
        print(f"  {name:<18} {v.structure:<8} Φ={v.max_phi:.3f}  core={core}")
    print("=" * 80)


if __name__ == "__main__":
    main()
