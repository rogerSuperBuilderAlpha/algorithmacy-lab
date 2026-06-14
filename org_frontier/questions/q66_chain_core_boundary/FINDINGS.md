# Q66 findings — where the core sits in an agent chain

Three hypotheses confirmed, one refuted. The refutation revises a Q65 interpretation. Instrument control
passed in every probe (dyadic relay Φ=0.000, fully-coupled triad Φ=0.830).

| H | Test | Result | Verdict |
|---|------|--------|---------|
| H1 | core is {Ad, R} at every depth | d=2 {A2,R}; d=3 {A3,R}; d=4 {E,A1} | **refuted** (`probe_chain_core_depth`) |
| H2 | core size two at every depth | size 2 at d=2,3,4 | confirmed (`probe_chain_core_depth`) |
| H3 | ring binds the whole structure | ring core = full set at d=2,3 | confirmed (`probe_ring_core`) |
| H4 | ring Φ exceeds open-chain 2.0 | ring Φ=4.0; open chain Φ=2.0 | confirmed (`probe_ring_core`) |

## What it says

The irreducible core of an open agent chain is a two-element end pair at every depth (H2). It is not
specifically the recipient-facing pair (H1 refuted): at depths two and three the maximal complex is
{Ad, R}, but at depth four it is {E, A1}, the sender end. The two ends are symmetric maximal complexes of
equal Φ = 2.0, and which one the computation returns is a tie-break that varies with chain length. This
revises Q65, which read the d = 2 result as a recipient-facing localization; the localization is to an
end pair, symmetric between the sender and recipient ends, not biased toward the recipient.

Closing the chain into a loop changes the picture entirely (H3, H4). A conjunctive ring, where the
recipient's state flows back to the sender, has a maximal complex equal to the whole element set at both
sizes, with Φ = 4.0, double the open chain's 2.0. A closed feedback loop binds every element into the
core where an open path leaves all but one end pair outside it. The verdict lives in the closed causal
loop, the same lesson the program found for directed cycles versus closed loops.

## Caveats

- **Revises Q65.** Q65's "recipient-facing core" was the d = 2 tie-break; the symmetric end-pair reading
  here supersedes it. A correction note to Q65 is warranted.
- **In-silico.** Boolean models, evidence about the models. Φ magnitude read ordinally.
- **Conjunctive forms.** The chain and ring use conjunctive commits; other commit functions are untested.
