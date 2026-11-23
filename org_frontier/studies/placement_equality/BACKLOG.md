# Experiment backlog after placement_equality

1. ~~**Derive the unanimous-state equality.** Compare cause and effect repertoires of OR3 at 0000 under
   both placements at r = 0.2 and 0.4 to see which distinction changes at 0.4.~~ Tested in
   `unanimous_repertoires`. The match of system φ at r = 0.2 is a match of the two effect values
   (OR3: 1.041518446253012); the cause values differ (1.041518 vs 2.002920). At r = 0.4 the
   mediator-side effect value at 0000 is −0.1242086202819146, which is why the match breaks.
2. **What sets the top/whole ratio?** 4 (MAJ3), 5 (2of4), 6 (weighted quota 3), 16 (3of5): compute 2of5
   and 4of5 at one rate.
3. **Re-score membership on tie sets** for every `quorum_noise_sweep` case.
4. **O04 registry hygiene**, then a ternary majority under input noise on the multivalued overlay.
5. **Asynchronous update** (needs a non-conditionally-independent TPM; check the instrument supports it).

Status: item 1 tested in `unanimous_repertoires` (2026-11-23). Items 2–5 remain open.
