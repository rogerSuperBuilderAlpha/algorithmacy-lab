# Q84 findings — influence versus membership

All four hypotheses confirmed. An agent outside the core cannot change the coordination's verdict;
influence requires membership.

| coupling | whole-system | maximal complex | core verdict |
|---|---|---|---|
| read-only X | dyadic (Φ=0) | {E, M, R} Φ=2.0 | triadic, unchanged |
| emit-only X | dyadic (Φ=0) | {E, M, R} Φ=2.0 | triadic, unchanged |
| bidirectional-pivotal X | triadic (Φ=3.0) | {E, M, R, X} Φ=3.0 | X joins the core |

From `probe_adversarial_agent.py`.

## What it says

An adversarial agent cannot move the coordination's verdict from outside the core. An agent that only
reads the message, or only emits without being read, leaves the maximal complex {E, M, R} triadic and
unchanged: it is a spectator, and per the Q74 rule the whole-system Φ=0 is its spectator signature, not a
flip of the verdict. Only a bidirectionally-coupled, pivotal agent changes the coordination, and when it
does it joins the core, growing it to {E, M, R, X} at Φ=3.0. Influence over the irreducible coordination
requires membership in it. The structural reading for adversarial settings is direct: an agent positioned
to read or feed a coordination without being read cannot manipulate whether it is dyadic or triadic; to
change the coordination it has to couple into it, where it becomes a detectable member of the core.

## Caveats

- **Confirmatory.** The influence-requires-membership predictions held.
- **In-silico.** Boolean models, evidence about the models. Φ read ordinally.
- **One pivotal coupling.** The bidirectional-pivotal case uses a conjunctive read; other pivotal
  couplings are untested, and a non-pivotal bidirectional agent would stay out (Finding 8).
