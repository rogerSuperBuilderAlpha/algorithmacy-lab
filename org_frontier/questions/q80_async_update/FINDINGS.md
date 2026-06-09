# Q80 findings — asynchronous update

All four hypotheses confirmed. The dyadic/triadic verdict is preserved under asynchronous update;
synchronicity is not load-bearing for the verdict.

| form | synchronous | asynchronous | verdict preserved |
|---|---|---|---|
| read_recipient | triadic Φ=2.0 | triadic Φ=0.249 | yes |
| broadcast | dyadic Φ=0 | dyadic Φ=0 | yes |
| all_required | triadic Φ=3.0 | triadic Φ=0.196 | yes |

From `probe_async_update.py`.

## What it says

The outreach verdict survives asynchronous update. When one element acts each step and the others hold,
the triadic forms stay triadic and the broadcast stays dyadic; only the magnitude of Φ falls, because the
asynchronous mixture integrates less per step than simultaneous action. The dyadic/triadic line is a
property of the coordination structure, not of the convention that every element updates at once.
Asynchrony does not manufacture irreducibility where the structure had none, and it does not destroy it
where the structure has it. For the application this removes a modelling worry: the law does not depend on
the unrealistic assumption that sender, agent, and recipient all act simultaneously.

## Caveats

- **Confirmatory.** The verdict-preservation predictions held; only the magnitude changed.
- **In-silico.** Boolean models under one asynchronous model (uniform one-element-per-step); other update
  schemes (block, ordered) are untested. Φ read ordinally.
- **Magnitude is not preserved.** Only the binary verdict is robust; the asynchronous Φ is far smaller, so
  Φ magnitude is even less a difficulty scale under varied update.
