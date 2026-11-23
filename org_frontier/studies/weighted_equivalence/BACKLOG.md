# Experiment backlog after weighted_equivalence

1. **Re-score membership on tie sets** for every `quorum_noise_sweep` case.
2. **Derive the unanimous-state equality** from `placement_equality` (OR3 cause/effect repertoires at 0000).
3. **Dummy parties elsewhere**: does adding a never-pivotal party to OR3 or AND3 (a party S reads but
   ignores) always drop whole Φ to 0, with and without party-side noise?
4. **A formula for the drifting ratio** when one party is strictly strongest (fit on (1,1,1,2) q3 and
   (1,1,2,3) q3; predict (1,1,1,3)). Tested in `drifting_ratio/`: the fitted formula is refuted
   (measured ratios 147.065, 76.276 and 41.484 against predicted 199.902, 102.765 and 54.049).
   The unique-heavy top set and the complement still hold. Open items move to that study's backlog.
5. **O04**: a ternary majority under input noise on the multivalued overlay.

None of these had been started when PR #942 was opened.
