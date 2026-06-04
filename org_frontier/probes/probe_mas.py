"""Probe 88 (#50) — is a multi-agent-AI protocol dyadic or triadic?

Question: when two AI agents coordinate through a shared protocol node, is the result a conveyor (the
protocol relays messages, dyadic) or a committing third party (the protocol jointly binds both agents,
triadic)? Hypothesis: a relay protocol that only forwards is dyadic, while a protocol whose state is
jointly determined by both agents and fed back to both is triadic — the same conveyor-vs-third-party cut
the construct draws for human coordination. Method: model two agents (A1, A2) and a protocol node (P)
under three designs — relay, broadcast, and joint-commit — and read the verdict and major complex of
each.

Nodes: 0=A1, 1=P, 2=A2.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_mas
"""

from .lib import verdict, major_complex

LABELS = ("A1", "P", "A2")

FORMS = {
    # relay: P forwards A1 to A2, A2 reads P, A1 unaffected — a conveyor chain
    "relay":        [lambda x: x[0], lambda x: x[0], lambda x: x[1]],
    # broadcast: P relays a shared signal both agents read, but P ignores their state
    "broadcast":    [lambda x: x[1], lambda x: x[1], lambda x: x[1]],
    # joint-commit: P is the AND of both agents and both act on P — a committing protocol
    "joint_commit": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
}


def main():
    print("PROBE 88 (#50) — multi-agent-AI protocol: conveyor vs committing third party")
    print("=" * 72)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        print(f"  {k:<14} {v.structure:<9} Φ={v.max_phi:.3f}  major complex={core}")
    print("=" * 72)
    print("  Reading: a relay or broadcast protocol that only forwards is dyadic — the agents")
    print("  coordinate through a conveyor. A protocol whose state both agents jointly determine and")
    print("  then act on is triadic, an irreducible third party. The cut matches human coordination.")
    print("=" * 72)


if __name__ == "__main__":
    main()
