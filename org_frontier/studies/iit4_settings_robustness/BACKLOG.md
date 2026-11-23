# Experiment backlog after iit4_settings_robustness

1. **Repertoire-distance axis.** Find why `IIT_4.0_SMALL_PHI` and `KLD` fail inside `new_big_phi.sia`
   (an IndexError and a keyword mismatch) and whether a thin adapter makes them comparable.
2. **Four-party families.** Repeat on noisy or four-party forms where Φ is not a round number, to see
   whether one-way cuts ever flip a small positive Φ to zero.
3. **Upstream report.** The `GENERAL` filter in `new_big_phi.sia` is unreachable (`if partitions ==
   "GENERAL"` inside `if partitions is None`); worth an issue on PyPhi.

None of these had been started when this study's PR was opened.
