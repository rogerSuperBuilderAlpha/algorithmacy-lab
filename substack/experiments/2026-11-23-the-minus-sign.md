# The minus sign is already in the effect-side formula

*Algorithmacy Lab, foundations stream. Study: `org_frontier/studies/negative_phi_source/`.*

An earlier survey found 284 negative raw φ values in these noisy-vote runs and recorded that a
negative value is outside what IIT 4.0 defines. This study took one of those numbers — OR3 with a
30% input error rate, the coordinator together with the first party, at the all-zero state, φ =
−0.13178321094580336 — and asked which part of the computation produces the minus sign.

The system value is exactly the effect-side value. The cause-side value is positive:
0.33979877901916944. PyPhi sets the system number to the smaller of the two, with no floor.

On the effect side, the formula is a selectivity times a signed log ratio. Selectivity is
0.6569999999999999. The intact forward repertoire at the specified effect state is
0.6569999999999999, and the partitioned repertoire is 0.7549999999999999, which is larger, so
log2(0.6569999999999999 / 0.7549999999999999) = −0.20058327389011169. Their product is exactly
−0.13178321094580336. No later combination of distinctions or relations is required to produce
the sign.

The same decomposition, to the same system and effect values, holds for the coordinator together
with the second party.

*Reproduce:* `python org_frontier/studies/negative_phi_source/run.py --write`
