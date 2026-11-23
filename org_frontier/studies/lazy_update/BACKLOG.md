# Experiment backlog after lazy_update

1. **Exact one-at-a-time update.** Build the non-conditionally-independent random-asynchronous TPM and
   measure how far it is from the λ = 0.75 marginal used here; check what the PyPhi pin accepts.
2. **Why is noisy MAJ3 whole Φ flat (0.026981) under a lazy mediator up to λ = 0.5?** Compare cause
   repertoires at λ = 0 and 0.5.
3. **Unequal laziness.** Slow mediator with fast parties and the reverse at different λ per node.
4. **Deterministic memory rules.** Parties that combine S with their own last state (S OR own, S AND own)
   instead of a random hold.
5. **Laziness on AND3 and 2of4.**

None of these had been started when PR #921 was opened.
