# Experiment backlog after memory_rules

1. **Why does the opposite latch break OR3 and AND3?** Read the cause repertoires of OR3/and at the
   state where {S,P1} peaks.
2. **Memory plus mediator noise.** Re-run the 36 cells with the mediator misreading at r = 0.1.
3. **Mixed memory.** Different rules for different parties (one latching, two copying).
4. **Delay nodes on quorum hubs** (a buffer between S and the parties), extending `commit_response_delay`
   from the conjunctive triad to OR3/MAJ3.

Item 4 is the next study (`delay_quorum`); the others had not been started when PR #923 was opened.
