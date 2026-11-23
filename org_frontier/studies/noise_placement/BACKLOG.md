# Experiment backlog after noise_placement

1. **Why does party-side noise give OR3 the same Φ as mediator-side noise up to r = 0.2?** Check AND3 and
   2of4 for the same equality, then look at the cause repertoires.
2. **What sets the top/whole ratio?** 4 (MAJ3), 5 (2of4), 6 (weighted quota 3), 16 (3of5): compute 2of5
   and 4of5 at one rate.
3. **Re-score membership on tie sets** for every `quorum_noise_sweep` case.
4. **O04 registry hygiene**, then a ternary majority under input noise on the multivalued overlay.
5. **Asynchronous update** (needs a non-conditionally-independent TPM; check the instrument supports it).

None of these had been started when PR #917 was opened.
